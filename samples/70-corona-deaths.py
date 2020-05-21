# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: all
#     formats: py:percent
#     notebook_metadata_filter: all,-language_info,-toc,-jupytext.text_representation.jupytext_version,-jupytext.text_representation.format_version
#     text_representation:
#       extension: .py
#       format_name: percent
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %%
# focus on these top countries
nb_top = 10
# on this number of days
nb_days = 30
# for text output
nb_text_days = 3

def strip_2020(x):
    stage1 = x.replace('2020-', '')
    month, day = stage1.split('-')
    if day == "1": 
        return stage1
    else:
        return day


# %%
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib notebook

# %%
# + cell_style="center"
from ipywidgets import HTML
css = """
<style>
.outline {
    font-size: 25px;
    font-weight: bold;
    padding-left: 5px;
    padding-right: 5px;
    color: orange;
}
</style>"""
def outline(*args):
    return f"<span class='outline'>{''.join(str(x) for x in args)}</span>"


# %% [markdown]
# -

# %%
import json
import requests

# %%
req = requests.get("https://pomber.github.io/covid19/timeseries.json")
encoded = req.text
decoded = json.loads(encoded)

# %%
NB_COUNTRIES = len(decoded)
NB_DAYS = max(len(country) for country in decoded.values())

# %%
country = "France"
yesterday_in_france = decoded[country][-1]
france_deaths = yesterday_in_france['deaths']
france_last_24h = france_deaths - decoded[country][-2]['deaths']
yesterday_in_france


# %%
def one_day(encoded, index=-1):
    return {country: decoded[country][-1] for country in decoded}


# %%
all_countries_yesterday = one_day(encoded)

# %%
# check consistency
from functools import reduce
reduce(lambda x,y : (x == y) and x, [country['date'] for country in all_countries_yesterday.values()])

# %%
last_24h = sum(country[-1]['deaths']-country[-2]['deaths'] for country in decoded.values())
last_24h


# %%
# yesterday is -1
# ...
def total_deaths(day_index):
    all_countries_at_day = []
    for country_dates in decoded.values():
        try:
            all_countries_at_day.append(country_dates[day_index])
        except IndexError:
            pass
    if not all_countries_at_day:
        return
    theday = reduce(lambda x,y : (x == y) and x,
                    [country['date'] for country in all_countries_at_day])
    if not theday:
        raise ValueError(f"whoops, something wrong with {day_index}")
    return day_index, theday, sum(country['deaths'] for country in all_countries_at_day)


# %%
# + cell_style="center"
_, yesterday, TOTAL_DEATHS = total_deaths(-1)
summary = f"""
{outline(yesterday, ":")} data is available on {NB_COUNTRIES} countries and on {NB_DAYS} days
<br>{outline(TOTAL_DEATHS)} total deaths worldwide, {outline(last_24h)} during the last 24h
<br>{outline(france_deaths)} total deaths in France, {outline(france_last_24h)} during the last 24h
"""
HTML(css+summary)


# %% [markdown]
# -

# %%
def show_day(index, label=None):
    if label is None:
        label = f"{-index} days ago"
    _, date, deaths = total_deaths(index)
    _, _, previous = total_deaths(index-1)
    print(f"{label} ({date}) {deaths} people had died ({deaths-previous} more in a day)")


# %%
show_day(-1, "yesterday")

# %%
show_day(-2)

# %%
show_day(-3)

# %%
ALL_DAYS, DEATHS, LABELS, DEATHS_DERIV = [], [], [], []

past = 0
for index in range(-NB_DAYS-3, 0):
    deaths = total_deaths(index)
    if deaths:
        index, date, nb = deaths
        ALL_DAYS.append(index)
        DEATHS.append(nb)
        LABELS.append(strip_2020(date))
        if not past:
            DEATHS_DERIV.append(0)
        else:
            DEATHS_DERIV.append(nb-past)
        past = nb


# %%
# utility to show only one tick every n
# make sure the last one is on though
def fewer_x_ticks(axis, period):
    tick_labels = list(axis.xaxis.get_ticklabels())
    last = len(tick_labels) - 1
    for index, label in enumerate(tick_labels):
        if (index - last) % period != 0:
            label.set_visible(False)


# %%
# + scrolled=false
fig = plt.figure(figsize=(8, 6))
ax_total = fig.add_subplot(111)
ax_daily = ax_total.twinx()

# %%
plt.xticks(ALL_DAYS, LABELS, rotation='vertical')

# %%
color = 'tab:blue'
ax_total.plot(ALL_DAYS, DEATHS, label="worldwide deaths")
ax_total.legend(loc='upper left')
ax_total.margins(0.05)
ax_total.set_ylabel("total", color=color)
ax_total.tick_params(axis='y', labelcolor=color)
fewer_x_ticks(ax_total, 5)

# %%
color = 'tab:orange'
ax_daily.plot(ALL_DAYS, DEATHS_DERIV, color=color, label="daily")
ax_daily.margins(0.05)
ax_daily.tick_params(axis='y', labelcolor=color)
ax_daily.legend(loc="lower right")

# %%
plt.show();

# %%
decoded_items = list(decoded.items())
decoded_items.sort(key=lambda cd:cd[1][-1]['deaths'], reverse=True)
top_countries = [c for (c, d) in decoded_items[:nb_top]]

for country in top_countries:
    print(f"{10*'='} {country}")
    for day in reversed(decoded[country][-nb_text_days:]):
        print(day)

# %%
# we need to go one day further 
# so as to be able to compute the delta for the first day
c = decoded[top_countries[0]]
last_days = [strip_2020(d['date']) for d in c[-(nb_days+1):]]

# %%
# number of deaths
Y = np.zeros(shape=( nb_top, nb_days+1))
# same but summed over countries to show all numbers on the same graph
YS = np.zeros(shape=( nb_top, nb_days+1))

# %%
for i_top in range(nb_top):
    country_name = top_countries[i_top]
    country = decoded[country_name]
    for i_day, day in enumerate(last_days):
        Y [ i_top, i_day] = country[-(nb_days+1-i_day)]['deaths']
        YS[ i_top, i_day] = country[-(nb_days+1-i_day)]['deaths']
        if i_top:
            YS[i_top, i_day] += YS[i_top-1, i_day]        

# %%
top_countries

# %%
# + cell_style="center"
plt.figure(figsize=(10, 6))

# %%
for top in range(nb_top):
    plt.plot(last_days[1:], YS[top][1:])    
plt.legend(top_countries)
plt.show()

# %%
# + scrolled=false {"scrolled": false}
# this is the max number of daily deaths in one country 
# using this as ylim for all drawings would result in a 
# series of superposable diagrams
# but that's not very good for smaller countries so..
MAX_DEATHS = decoded[top_countries[0]][-1]['deaths']

# %% scrolled=false
for top in range(nb_top):
    color = 'tab:blue'
    country_name = top_countries[top]
    fig = plt.figure(figsize=(8, 3))
    ax_total = fig.add_subplot(111)
    ax_daily = ax_total.twinx()
    MAX_DEATHS_COUNTRY = decoded[country_name][-1]['deaths']
    ax_total.set_ylim(0, MAX_DEATHS_COUNTRY*1.1)
    ax_total.set_ylabel("total")
    ax_total.plot(last_days[1:], Y[top][1:], label=f"{country_name}: {MAX_DEATHS_COUNTRY}")
    ax_total.tick_params(axis='y', labelcolor=color)
    ax_total.legend(loc="upper left")
    
    color = 'tab:orange'
    Y_shift = Y[top][:-1]
    Y_daily = Y[top][1:]-Y_shift
    ax_daily.plot(last_days[1:], Y_daily, label="daily", color=color)
    ax_daily.set_ylim(0, max(Y_daily)*1.1)
    ax_daily.set_ylabel("daily", color=color)
    ax_daily.tick_params(axis='y', labelcolor=color)
    plt.show()
# -

# %%
decoded['India'][-1]

# %%
decoded['US'][-1]

# %% [markdown]
# *****

# %%
import pandas as pd


# %%
def extract_last_days(countryname, value, days):
    country = decoded[countryname]
    cropped = country[-(days):]
    dates = np.array([chunk['date'] for chunk in cropped])
    # take one more than requested for computing deltas including
    # for the first day (we need the value the day before the first day)
    cropped = country[-(days+1):]
    values = np.array([chunk[value] for chunk in cropped])
    # shift one day so we get the value from the day before
    shifted = np.roll(values, 1)
    # the daily increase; ignore first value which is wrong
    deltas = (values - shifted)[1:]
    relevant = values[1:]
    # all 3 arrays dates, deltas and relevant have the same shape
    data = {'dates': dates, value: relevant, 'deltas': deltas}
    return pd.DataFrame(data=data)
    

df = extract_last_days('France', 'deaths', 45)
    

# %%
df.plot();
