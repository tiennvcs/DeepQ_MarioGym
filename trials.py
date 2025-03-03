from ..actions import RIGHT_ONLY, SIMPLE_MOVEMENT, COMPLEX_MOVEMENT

# Trial 1: RIGHT_ONLY
# ##############################################################################
# GAME = 'super_mario_bros-2'                                                  #
# NUM_ACTIONS = len(SIMPLE_MOVEMENT)                                           #
# GAMMA = 0.99  # decay rate of past observations                              #
# OBSERVE = 100000.                                                            #
# EXPLORE = 2000000. # frames over which to anneal epsilon                     #
# INITIAL_EPSILON = 0.0001 # initial value of epsilon                          #
# FINAL_EPSILON = 0.0001 # final value of epsilon                              #
# REPLAY_MEMORY = 50000 # number of previos transitions to remember            #
# BATCH  = 32 # size of mini-batch                                             #
# FRAME_PER_ACTION = 1                                                         #
# ##############################################################################


# Trial 2: SIMPLE_MOVEMENT
###############################################################################
GAME = 'super_mario_bros-2'                                                    #
NUM_ACTIONS = len(SIMPLE_MOVEMENT)                                             #
GAMMA = 0.99  # decay rate of past observations                                #
OBSERVE = 100000.                                                              #
EXPLORE = 2000000. # frames over which to anneal epsilon                       #
INITIAL_EPSILON = 0.0001 # initial value of epsilon                            #
FINAL_EPSILON = 0.0001 # final value of epsilon                                #
REPLAY_MEMORY = 50000 # number of previos transitions to remember              #
BATCH  = 32 # size of mini-batch                                               #
FRAME_PER_ACTION = 1                                                           #
# ##############################################################################


# Trial 3: COMPLEX_MOVEMENT
################################################################################
GAME = 'super_mario_bros-2'                                                    #
NUM_ACTIONS = len(COMPLEX_MOVEMENT)                                            #
GAMMA = 0.99  # decay rate of past observations                                #
OBSERVE = 100000.                                                              #
EXPLORE = 2000000. # frames over which to anneal epsilon                       #
INITIAL_EPSILON = 0.0001 # initial value of epsilon                            #
FINAL_EPSILON = 0.0001 # final value of epsilon                                #
REPLAY_MEMORY = 50000 # number of previos transitions to remember              #
BATCH  = 32 # size of mini-batch                                               #
FRAME_PER_ACTION = 1                                                           #
# ##############################################################################

# Trial 4: higher initial epsilon
################################################################################
GAME = 'super_mario_bros-2'                                                    #
NUM_ACTIONS = len(SIMPLE_MOVEMENT)                                             #
GAMMA = 0.99  # decay rate of past observations                                #
OBSERVE = 100000.                                                              #
EXPLORE = 2000000. # frames over which to anneal epsilon                       #
INITIAL_EPSILON = 0.001 # initial value of epsilon                             #
FINAL_EPSILON = 0.0001 # final value of epsilon                                #
REPLAY_MEMORY = 50000 # number of previos transitions to remember              #
BATCH  = 32 # size of mini-batch                                               #
FRAME_PER_ACTION = 1                                                           #
# ##############################################################################


# Trial 4: higher initial epsilon
################################################################################
GAME = 'super_mario_bros-2'                                                    #
NUM_ACTIONS = len(SIMPLE_MOVEMENT)                                             #
GAMMA = 0.99  # decay rate of past observations                                #
OBSERVE = 100000.                                                              #
EXPLORE = 2000000. # frames over which to anneal epsilon                       #
INITIAL_EPSILON = 0.01 # initial value of epsilon                             #
FINAL_EPSILON = 0.0001 # final value of epsilon                                #
REPLAY_MEMORY = 50000 # number of previos transitions to remember              #
BATCH  = 32 # size of mini-batch                                               #
FRAME_PER_ACTION = 1                                                           #
# ##############################################################################

# Trial 5: higher initial epsilon
################################################################################
GAME = 'super_mario_bros-2'                                                    #
NUM_ACTIONS = len(SIMPLE_MOVEMENT)                                             #
GAMMA = 0.99  # decay rate of past observations                                #
OBSERVE = 100000.                                                              #
EXPLORE = 2000000. # frames over which to anneal epsilon                       #
INITIAL_EPSILON = 0.1 # initial value of epsilon                               #
FINAL_EPSILON = 0.0001 # final value of epsilon                                #
REPLAY_MEMORY = 50000 # number of previos transitions to remember              #
BATCH  = 32 # size of mini-batch                                               #
FRAME_PER_ACTION = 1                                                           #
# ##############################################################################

# Trial 6: higher initial epsilon and higher bacth size for training
################################################################################
GAME = 'super_mario_bros-2'                                                    #
NUM_ACTIONS = len(SIMPLE_MOVEMENT)                                             #
GAMMA = 0.99  # decay rate of past observations                                #
OBSERVE = 100000.                                                              #
EXPLORE = 2000000. # frames over which to anneal epsilon                       #
INITIAL_EPSILON = 0.001 # initial value of epsilon                               #
FINAL_EPSILON = 0.0001 # final value of epsilon                                #
REPLAY_MEMORY = 50000 # number of previos transitions to remember              #
BATCH  = 64 # size of mini-batch                                               #
FRAME_PER_ACTION = 1                                                           #
# ##############################################################################
