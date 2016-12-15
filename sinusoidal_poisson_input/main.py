#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Simulation of figures 3 & 4 in Hill-Tononi paper.
# Author: Pablo Martinez Cañada (pablomc@ugr.es)

import nest
import nest.topology as tp
import numpy as np
import time
import math

import figure_4_plot
reload(figure_4_plot)

import figure_3_plot
reload(figure_3_plot)

sim_fig_3 = True
sim_fig_4 = False

if sim_fig_4:

    Params = {
        'Np': 40, # cells in the primary visual area
        'Ns': 30, # cells in the secondary visual area
        'visSize': 8.0, # visual angle (degrees)
        'ret_rate': 30.0, # average firing rate of retina ganglion cells (spikes^(-1))
        'ret_amplitude': 0.0, # amplitude of the sinusoidal poisson generator
                              # used for retina ganglion cells (spikes^(-1))
        'temporal_frequency': 0.0, # frequency of the generator (Hz)
        'threads': 24, # threads to use in NEST simulation
        #'intervals': [1000.0, 1000.0, 7500.0],  # keiko
        #'intervals': [500.0],  # Intervals (in ms) of the waking,transition
        'intervals': [500.0, 500.0, 500.0, 500.0, 3000.0],  # Intervals (in ms) of the waking,transition
                                           # and sleep modes
        'resolution': 1.0 # Simulation step (in ms)
    }

    # Run simulation of figure 4
    figure_4_plot.simulation(Params)



if sim_fig_3:

    Params = {
        'Np': 40,
        'Ns': 30,
        'visSize': 8.0,
        'ret_rate': 150.0,#20.0,
        'ret_amplitude': 0.0, # random
        'temporal_frequency': 2.0, # (Hz)
        'spatial_frequency' : 0.5, # (cpd)
        'threads': 24,
        #'intervals': [100.0, 250.0, 650.0],  # original
        'intervals': [5000.0],  # keiko
        'resolution': 1.0,
        'phi_dg': 0.0,  # vertical
        #'phi_dg': 0.5*np.pi, # horizontal
        #--- vertical
        #'lambda_dg': 2.0,  # visSize / number_of_lines
        #'input_flag': True,
        #'data_folder': '/home/kfujii2/newNEST2/ht_model_pablo_based/data/2Hz_vertical_2016Dec07_rate05/'
        #'data_folder': '/media/kfujii2/TOSHIBA EXT/experimental_data/lobustness_frequency/2Hz_vertical_rate150/'
        #
        #--- random
        'lambda_dg': -1.0,  # visSize / number_of_lines
        'input_flag': False,
        #'data_folder': '/home/kfujii2/newNEST2/ht_model_pablo_based/data/random_2016Dec07_rate500/'
        'data_folder': '/media/kfujii2/TOSHIBA EXT/experimental_data/lobustness_frequency/random_rate150/'
    }

    # Run simulation of figure 3
    figure_3_plot.simulation(Params)


