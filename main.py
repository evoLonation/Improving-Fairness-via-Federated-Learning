import sys, os
working_dir = '.'
sys.path.insert(1, os.path.join(working_dir, 'FedFB'))
os.environ["PYTHONPATH"] = os.path.join(working_dir, 'FedFB')


from DP_run import *


print('zzy: import done, ready to execute sim_dp')
# sim_dp('fedavg', 'logistic regression', 'synthetic')
sim_dp('fedavg', 'logistic regression', 'adult')
# sim_dp('fedfb', 'logistic regression', 'adult')

# sim_dp_man(
#   'fflfb', 
#   'multilayer perceptron', 
#   'synthetic', 
#   alpha = (0.05,0.04,0.03), 
#   num_rounds = 2
# )