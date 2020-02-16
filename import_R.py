#i need the package mcr for a method comparison


from rpy2.robjects.packages import importr
from rpy2.robjects.vectors import StrVector



def import_packages(packnames, mirror):
    """this function imports desired R-packages and lets you choose from which mirror eg. CRAN or Bioconductor """

    utils = importr("utils")

    if mirror == "CRAN":
        utils.chooseCRANmirror(ind=1) # select the first mirror in the list


    elif mirror == "Bioconductor":
        utils.chooseBioCmirror(ind=1) # select the first mirror in the list

    else:
        raise "ERROR: can't find mirror to load packages from"


    utils.install_packages(StrVector(packnames))



mcr = import_packages(packnames = "mcr", mirror = "CRAN")