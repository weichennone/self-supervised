from .contrastive import Contrastive
from .w_mse import WMSE
from .byol import BYOL
from .mxent import MXENT

METHOD_LIST = ["contrastive", "w_mse", "byol"]


def get_method(name):
    assert name in METHOD_LIST
    if name == "contrastive":
        return Contrastive
    elif name == "w_mse":
        #return WMSE
        return MXENT
    elif name == "byol":
        return BYOL
