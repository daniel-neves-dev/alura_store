import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import matplotlib as mtl
from prettytable import PrettyTable

def library_used_versions():
    print('Package Versions:',
        f'\nPandas: {pd.__version__}, '
        f'\nMatplotlib: {mtl.__version__},')

