import numpy as np
import math
import os
import pandas as pd

#Global path settings
path_script = os.path.dirname(os.path.realpath(__file__))
path_data = path_script + "/data_fake.csv"

template_data = pd.read_csv(path_data)

def scenario(biometrics: pd.DataFrame):
    scenario_total = 3
    random_seed = math.floor(np.random.rand() * scenario_total)

    rest_kcal: int = 1800 - biometrics['sex']*300
    rest_kcal += (biometrics['age'] < 20) * 20 * biometrics['age']
    rest_kcal += (biometrics['age'] >= 20 and biometrics['age'] <= 40) * (40 - biometrics['age']) * 20
    rest_kcal += biometrics['weight'] * 3
    rest_kcal += biometrics['height'] // 2
    rest_kcal += math.floor((0.5 - np.random.rand()) * 200)
    
    # stagnation
    if(random_seed == 0):
        pass

    # linear progress
    elif(random_seed == 1):
        pass

    # linear progress into motivation loss
    elif(random_seed == 2):
        pass

    return rest_kcal

temp = np.zeros(template_data.shape[0])

for row in range(len(temp)):
    temp[row] = scenario(template_data.iloc[row])

print(temp)