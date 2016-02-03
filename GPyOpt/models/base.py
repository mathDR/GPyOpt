# Copyright (c) 2015, Javier Gonzalez
# Copyright (c) 2015, the GPy Authors (see GPy AUTHORS.txt)
# Licensed under the BSD 3-clause license (see LICENSE.txt)

import abc
import numpy as np
from astropy.convolution.core import Kernel

class BOModel(object):
    __metaclass__ = abc.ABCMeta
    """
    The abstract Model for Bayesian Optimization
    """
    
    @abc.abstractmethod
    def updateModel(self, X_all, Y_all, X_new, Y_new):
        "Augment the dataset of the model"
        return
    
    @abc.abstractmethod
    def predict(self, X):
        "Get the predicted mean and std at X."
        return

    @abc.abstractmethod
    def predict_withGradients(self, X):
        "Get the gradients of the predicted mean and variance at X."
        return
    
    @abc.abstractmethod
    def get_fmin(self):
        "Get the minimum of the current model."
        return

    