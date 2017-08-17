#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 23:06:16 2017

@author: sss
"""
import pylab
import numpy
from ps3b_precompiled_35 import *

#==============================================================================
# def simulationWithoutDrug(numViruses, maxPop, maxBirthProb, clearProb,
#                           numTrials):
#     """
#     Run the simulation and plot the graph for problem 3 (no drugs are used,
#     viruses do not have any drug resistance).    
#     For each of numTrials trial, instantiates a patient, runs a simulation
#     for 300 timesteps, and plots the average virus population size as a
#     function of time.
# 
#     numViruses: number of SimpleVirus to create for patient (an integer)
#     maxPop: maximum virus population for patient (an integer)
#     maxBirthProb: Maximum reproduction probability (a float between 0-1)        
#     clearProb: Maximum clearance probability (a float between 0-1)
#     numTrials: number of simulation runs to execute (an integer)
#     """
#     TIME_STEPS = 300            
#     
#     patients = []
#     for trial in range(numTrials):
#         viruses = [SimpleVirus(maxBirthProb, clearProb)] * numViruses
#         patient = Patient(viruses, maxPop)
#         patients.append(patient)
#     
#     avg_population_at_each_time_step_list = []
#     for time_step in range(TIME_STEPS):
#         populations = []
#         for p in patients:
#             populations.append(p.update())
#         avg_population = numpy.mean(populations)
#         avg_population_at_each_time_step_list.append(avg_population)
#         
#     pylab.plot([i for i in range(TIME_STEPS)], avg_population_at_each_time_step_list)  
#==============================================================================

def simulationWithDrug(numViruses, maxPop, maxBirthProb, clearProb, resistances,
                       mutProb, numTrials):
    """
    Runs simulations and plots graphs for problem 5.

    For each of numTrials trials, instantiates a patient, runs a simulation for
    150 timesteps, adds guttagonol, and runs the simulation for an additional
    150 timesteps.  At the end plots the average virus population size
    (for both the total virus population and the guttagonol-resistant virus
    population) as a function of time.

    numViruses: number of ResistantVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
    clearProb: maximum clearance probability (a float between 0-1)
    resistances: a dictionary of drugs that each ResistantVirus is resistant to
                 (e.g., {'guttagonol': False})
    mutProb: mutation probability for each ResistantVirus particle
             (a float between 0-1). 
    numTrials: number of simulation runs to execute (an integer)
    
    """
    TIME_STEPS = 150
    GUTT = "guttagonol"
    
    # Create patients for all trials
    patients = []
    for trial in range(numTrials):
        viruses = [ResistantVirus(maxBirthProb, clearProb, resistances, mutProb)] * numViruses
        patient = TreatedPatient(viruses, maxPop)
        patients.append(patient)
    
    # Create two empty list for total_pop and guttagonol-resistant_pop    
    avg_total_pops = []
    avg_guttr_pops = []

    # First 150 timesteps without drugs
    for time_step in range(TIME_STEPS):
        total_pops = []
        guttr_pops = []
        for p in patients:
            total_pops.append(p.update())
            guttr_pops.append(p.getResistPop([GUTT]))
        avg_total_pops.append(sum(total_pops) / len(total_pops))
        avg_guttr_pops.append(sum(guttr_pops) / len(guttr_pops))        
        
    # Add drug "guttagonol"
    for p in patients:
        p.addPrescription(GUTT)
     
    # Another 150 timesteps with drug "guttagonol"
    for time_step in range(TIME_STEPS):
        total_pops = []
        guttr_pops = []
        for p in patients:
            total_pops.append(p.update())
            guttr_pops.append(p.getResistPop([GUTT]))
        avg_total_pops.append(sum(total_pops) / len(total_pops))
        avg_guttr_pops.append(sum(guttr_pops) / len(guttr_pops))        
    
    # Plot
    pylab.figure("total_pop vs guttagonol_resistant_pop")
    pylab.title("Population Simulation With Drug")
    pylab.xlabel("Time Steps")
    pylab.ylabel("Population")
    pylab.plot(avg_total_pops, label="Total Population")
    pylab.plot(avg_guttr_pops, label="Guttagonol-resistant Population")
    pylab.legend(loc="best")
    pylab.show()
    
    print(avg_total_pops)
    print(avg_guttr_pops)

    
if __name__ == "__main__":
#    simulationWithDrug(100, 1000, 0.1, 0.05, {"guttagonol": False}, 0.005, 100)
    simulationWithDrug(1, 10, 1.0, 0.0, {}, 1.0, 5)