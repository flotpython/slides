def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case 401 | 403 :
            return "Not allowed"
        case _:
            return "Something's wrong with the internet"

print(http_error(404))

