from rpy2.robjects.vectors import FloatVector
from rpy2.robjects.packages import importr
from rpy2 import robjects
from import_R import import_packages
from rpy2.robjects import r, pandas2ri
import pandas as pd
from sklearn.datasets import load_iris

#mcr = import_packages(packnames = ("mcr", "ggplot2"), mirror = "CRAN")


mcr = importr('mcr')
r = robjects.r

x = FloatVector([1,2,3,4,5,6,7,8,9])
y = FloatVector([1,2,3,4,5,6,7,8,9])

rprint = robjects.r["print"]

rmcreg = robjects.r['mcreg']
rplot = robjects.r['plot']


grdevices = importr('grDevices')

result = rmcreg(x, y, method_reg = "Deming", alpha = 0.05)
grdevices.png(file="MethodComparison.png", width=512, height=512)

p = rplot(result)

grdevices.dev_off()

data = load_iris()
df = pd.DataFrame(data.data, columns=data.feature_names)
#print(df.head())

r.data('iris')
pandas2ri.activate()
#r_dataframe = pandas2ri.py2ri(df)

grdevices = importr('grDevices')

result2 = rmcreg(r['iris']["Petal.Length"], r['iris']["Petal.Width"],
                 method_reg = "PaBa", alpha = 0.05)
grdevices.png(file="iris.png", width=512, height=512)

p = rplot(result2, identity=False)

grdevices.dev_off()
print(r['iris']["Petal.Length"])