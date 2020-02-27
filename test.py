from rpy2.robjects.vectors import FloatVector
from rpy2.robjects.packages import importr
from rpy2 import robjects
from rpy2.robjects.vectors import StrVector

packnames = ('mcr', 'ggplot2')

utils = importr("utils")

utils.chooseCRANmirror(ind=1)

#utils.install_packages(StrVector(packnames))

mcr = importr('mcr')
r = robjects.r
#mcr = import_packages(packnames = "mcr", mirror = "CRAN")

x = FloatVector([1,2,3,4,5,6,7,8,9])
y = FloatVector([1,2,3,4,5,6,7,8,9])

rprint = robjects.r["print"]

rmcreg = robjects.r['mcreg']
rplot = robjects.r['plot']

#dem = robjects.r('reg = "Deming"')

result = rmcreg(x, y)

print(result)



