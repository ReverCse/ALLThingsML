import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pylab import rcParams

from preprocessing import *
from math_util import *
from plotting import *

%matplotlib inline

sns.set(style = 'whitegrid',palette='muted',font_scale=1.5)

rcParams['figure.figsize'] = 12, 6

RANDOM_SEEP = 42

np.random.seed(RANDOM_SEED)


