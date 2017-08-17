import random
import pylab

# Global Variables
MAXRABBITPOP = 1000

#CURRENTRABBITPOP = 500
#CURRENTFOXPOP = 30

CURRENTRABBITPOP = 50
CURRENTFOXPOP = 300

def rabbitGrowth():
    """ 
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up, 
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP

    # TO DO    
    temp_r_pop = CURRENTRABBITPOP
    for i in range(temp_r_pop):
        if random.random() < (1.0 - CURRENTRABBITPOP/MAXRABBITPOP):
            CURRENTRABBITPOP += 1
#    print("current rabbit pop:", CURRENTRABBITPOP)
            
def foxGrowth():
    """ 
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat 
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP

    # TO DO    
    temp_f_pop = CURRENTFOXPOP
    for i in range(temp_f_pop):
        if random.random() < (CURRENTRABBITPOP / MAXRABBITPOP):
            if CURRENTRABBITPOP > 10:
                CURRENTRABBITPOP -= 1
                if random.random() < (1/3):
                    CURRENTFOXPOP += 1
        else:
            if random.random() < (9/10):
                if CURRENTFOXPOP > 10:
                    CURRENTFOXPOP -= 1
    
#    print("current rabbit pop: {}, current fox pop: {}".format(
#            CURRENTRABBITPOP, CURRENTFOXPOP))

            
def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the 
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """

    # TO DO
    r_pops = []
    f_pops = []
    for i in range(numSteps):
        rabbitGrowth()
        foxGrowth()
        r_pops.append(CURRENTRABBITPOP)
        f_pops.append(CURRENTFOXPOP)

    pylab.figure("rabbit_vs_fox")
    pylab.title("Rabbits and Foxes Population Simulation")
    pylab.xlabel("Steps")
    pylab.ylabel("Populations")
    pylab.plot(r_pops, label="Rabbit pops")
    pylab.plot(f_pops, label="Fox pops")
    pylab.legend()
    pylab.show()
    
    return (r_pops, f_pops)

if __name__ == "__main__":
    rp, fp = runSimulation(200)
    r_coeff = pylab.polyfit(range(len(rp)), rp, 2)
    pylab.plot(pylab.polyval(r_coeff, range(len(rp))))
    
    f_coeff = pylab.polyfit(range(len(fp)), fp, 2)
    pylab.plot(pylab.polyval(f_coeff, range(len(fp))))
