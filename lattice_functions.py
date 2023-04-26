import os
import time
import  numpy as np
from numba import njit , prange,set_num_threads

set_num_threads(4)








@njit(parallel=True)
def staple():
    print('staple')

@njit
def plaquette():
    print('plaquette')

@njit(parallel=True)
def average_plaquette():
    print('average_plaquette')

@njit
def F_munu():
    print('F_munu')

@njit(parallel=True)
def total_topological_charge_density():
    print('total_topological_charge_density')

@njit
def topological_charge():
    print('topological_charge')

def Initial_conditions():
    print('Initial_conditions')

@njit
def wilsonflow_update():
    print('wilsonflow_update')

@njit
def Metropolis_update_su3():
    print('Metropolis_update_su3')

def Metropolis_wilsonflow_total():
    print('Metropolis_wilsonflow_total')

@njit
def autocor_fun():
    print('autocor_fun')


@njit
def static_quark_potential():
    print('static_quark_potential')