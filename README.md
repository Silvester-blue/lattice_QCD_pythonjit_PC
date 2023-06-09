Introduction
============
This program is written by myself, and it can be used to calculate the configuration of lattice QCD and some physical quantities on a personal computer.The calculation speed of C/C++ program is fast but the program readability is not high, and the readability of python program is strong but the calculation speed is slow.Therefore, this program is a python program modified by jit to achieve high readability and calculation speed.This program is currently part of the machine learning program and is used to generate training data for machine learning. A more complete version may be gradually displayed in the future.



How to use
============
All functions are placed in the lattice_functions.py file which you can copy to a local python project and call the function directly.

This program can run on a personal computer, and of course it can also run on a server.Given that a PC has a relatively small number of CPU cores, 
it may be possible to overclock the PC to improve single-core performance.It is worth noting that the single-core computing speed of many PC Intel Core CPUs or Ryzen CPUs is faster than the single-core computing speed of many server Xeon processors. Therefore, overclocking is only an option for speed optimization, not a necessary step.

Furthermore, the program has been tested under win10, win11 and ubuntu.As for other computer systems, due to the extensive installation of python and modules, 
this program can also be tried to run.

Some modules that need to be installed in advance are as follows. These modules can be installed through pip.

numpy,numba,matplotlib,PyVista



Part of the functions in lattice_functions.py
============

Initial_conditions()#Initial conditions

average_plaquette()#average of plaquette

total_topological_charge_density()#total topological charge density,a tensor with size Nt*Nx*Ny*Nz

topological_charge()#topological charge

Metropolis_update_su3()#The configuration of lattice QCD is updated by the multi-hit Metropolis algorithm

Metropolis_wilsonflow_total()#The configuration is updated by the multi-hit Metropolis algorithm and the Wilson flow

autocor_fun()#Calculation of Autocorrelation Function

static_quark_potential()#Static QCD quark potential

Example
============

<p align="center">
    <img src="topol_density_wflow600.png"  width="500"/>
</p>
    
<p align="center">
    <i>The image of topological charge density on a time slice is obtained by the multi-hit Metropolis algorithm and Wilson flow</i>
</p>


