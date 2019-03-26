# adapted from
# https://jupyter-notebook.readthedocs.io/en/latest/examples/Notebook/Importing%20Notebooks.html

import sys
import types
from pathlib import Path

import nbformat
from IPython import get_ipython
from IPython.core.interactiveshell import InteractiveShell

class NotebookLoader:
    """
    module loader for Jupyter notebooks
    """
    def __init__(self, path=None):
        self.shell = InteractiveShell.instance()
        self.path = path

    def load_module(self, modulename):
        """
        import a notebook as a module
        """
        notebook_path = find_notebook(modulename, self.path)
        if not notebook_path:
            raise ImportError(modulename)

        print(f"importing Jupyter notebook from {notebook_path}")

        # load the notebook object
        with notebook_path.open(encoding='utf-8') as f:
            nb = nbformat.read(f, 4)


        # create the module and add it to sys.modules
        # if name in sys.modules:
        #    return sys.modules[name]
        mod = types.ModuleType(modulename)
        mod.__file__ = modulename
        mod.__loader__ = self
        mod.__dict__['get_ipython'] = get_ipython
        sys.modules[modulename] = mod

        # extra work to ensure that magics that would affect the user_ns
        # actually affect the notebook module's ns
        save_user_ns = self.shell.user_ns
        self.shell.user_ns = mod.__dict__

        try:
          for cell in nb.cells:
            if cell.cell_type == 'code':
                # transform the input to executable Python
                code = self.shell.input_transformer_manager.transform_cell(cell.source)
                # run the code in themodule
                exec(code, mod.__dict__)
        finally:
            self.shell.user_ns = save_user_ns
        return mod


def find_notebook(modulename, path=None):
    """
    find a notebook, given its fully qualified name and an optional
    list of paths to search into

    this turns "foo.bar" into "foo/bar.ipynb"
    """
    if path is None:
        path = ['.', './modules', '../modules', '../../modules']
    *splitted_path, fname = modulename.split('.')
    for dir in path:
        candidate = Path(dir).joinpath(*splitted_path) / (fname + ".ipynb")
        if candidate.is_file():
            return candidate


class NotebookFinder:
    """
    module finder that locates Jupyter notebooks
    """
    def __init__(self):
        self.loaders = {}

    def find_module(self, modulename, path=None):
        nb_path = find_notebook(modulename, path)
        if not nb_path:
            return

        key = path
        if path:
            # lists aren't hashable
            key = '/'.join(path)

        if key not in self.loaders:
            self.loaders[key] = NotebookLoader(path)
        return self.loaders[key]
