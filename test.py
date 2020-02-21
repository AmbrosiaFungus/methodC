from rpy2.robjects.vectors import FloatVector
from rpy2.robjects.packages import importr
from rpy2 import robjects
from rpy2.robjects.vectors import StrVector


packnames = ('mcr', 'ggplot2')

utils = importr("utils")

utils.chooseCRANmirror(ind=1)

utils.install_packages(StrVector(packnames))

mcr = importr('mcr')

#mcr = import_packages(packnames = "mcr", mirror = "CRAN")

x = FloatVector([1,2,3,4,5,6,7,8,9])
y = FloatVector([1,2,3,4,5,6,7,8,9])


#d = {'ID1': [1, 2, 3, 4, 5, 6], 'ID2': [1, 2, 3, 4, 5, 6]}
#sample_data = pd.DataFrame(data=d)
#rdf = com.convert_to_r_dataframe(sample_data)

dem = robjects.r('reg = "Deming"')

result = mcr.mcreg(x, y, dem)

print(mcr.plot(result))


#print(robjects.r(res))

#print(plot_res)


