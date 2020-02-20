from rpy2.robjects import pandas2ri
pandas2ri.activate()
from rpy2.robjects import FloatVector
from rpy2.robjects.packages import importr
from rpy2.robjects.vectors import StrVector

# packnames = ('mcr', 'ggplot2')
#
# utils = importr("utils")
#
# utils.chooseCRANmirror(ind=1)
#
# utils.install_packages(StrVector(packnames))

mcr = importr('mcr')

#mcr = import_packages(packnames = "mcr", mirror = "CRAN")

x = FloatVector([1,2,3,4,5,6,7,8,9])
y = FloatVector([1,2,3,4,5,6,7,8,9])


#d = {'ID1': [1, 2, 3, 4, 5, 6], 'ID2': [1, 2, 3, 4, 5, 6]}
#sample_data = pd.DataFrame(data=d)
#rdf = com.convert_to_r_dataframe(sample_data)



result = mcr.mcreg(x,y)

plot_res = mcr.plot(result)

print(plot_res)

from rpy2 import robjects
from rpy2.robjects import Formula, Environment
from rpy2.robjects.vectors import IntVector, FloatVector
from rpy2.robjects.lib import grid
from rpy2.robjects.packages import importr, data
from rpy2.rinterface import RRuntimeError
import warnings

# The R 'print' function
rprint = robjects.globalenv.get("print")
stats = importr('stats')
grdevices = importr('grDevices')
base = importr('base')
datasets = importr('datasets')

grid.activate()

import math, datetime
import rpy2.robjects.lib.ggplot2 as ggplot2
import rpy2.robjects as ro
from rpy2.robjects.packages import importr
base = importr('base')

mtcars = data(datasets).fetch('mtcars')['mtcars']

pp = ggplot2.ggplot(mtcars) + \
     ggplot2.aes_string(x='wt', y='mpg', col='factor(cyl)') + \
     ggplot2.geom_point() + \
     ggplot2.geom_smooth(ggplot2.aes_string(group = 'cyl'),
                         method = 'lm')
pp.plot()


