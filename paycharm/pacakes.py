import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mtl
from prettytable import PrettyTable

def library_used_versions():
    print('Package Versions:',
        f'\nPandas: {pd.__version__}, '
        f'\nMatplotlib: {mtl.__version__},')

library_used_versions()
