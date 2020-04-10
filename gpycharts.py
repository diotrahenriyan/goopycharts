# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # Creating Graphs with Python and GooPyCharts
# Source: [datascience+](https://datascienceplus.com/creating-graphs-with-python-and-goopycharts/)
# %% [markdown]
# ## Install gpcharts library
# 
# ```python
# pip install gpcharts
# ```
# %% [markdown]
# ## Our First Graph
# 

# %%
from gpcharts import figure
my_plot = figure(title='Demo')
my_plot.plot([1, 2, 10, 15, 12, 23])

# %% [markdown]
# ## Creating a Bar Graph

# %%
fig3 = figure()
xVals = ['Temps','2016-03-20','2016-03-21','2016-03-25','2016-04-01']
yVals = [['Shakuras','Korhal','Aiur'],[10,30,40],[12,28,41],[15,34,38],[8,33,47]]

fig3.title = 'Weather over Days'
fig3.ylabel = 'Dates'
fig3.bar(xVals, yVals)

# %% [markdown]
# ## Creating Other Types of Graphs

# %%
my_fig = figure()
xVals = ['Dates','2016-03-20','2016-03-21','2016-03-25','2016-04-01']
yVals = [['Shakuras','Korhal','Aiur'],[10,30,40],[12,28,41],[15,34,38],[8,33,47]]

my_fig.title = 'Scatter Plot'
my_fig.ylabel = 'Temps'

my_fig.scatter(xVals, yVals)

