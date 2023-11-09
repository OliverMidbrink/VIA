#Import packages
import scanpy as sc
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import time, os
print("Importing via")
start_time = time.time()
import VIA
time_elapsed = time.time() - start_time
print("Done importing via. Took {} seconds".format(time_elapsed))
from datetime import datetime

if not os.path.exists("pijuan_gastrulation_via.h5ad"):
    print("Downloading data")
    start_time = time.time()
    from VIA.datasets_via import _mouse_gastrulation_sala
    _mouse_gastrulation_sala()
    os.system("python VIA/datasets_via.py")
    time_elapsed = time.time() - start_time
    print("Done. Took {} seconds. ". format(time_elapsed))


print(f'{datetime.now()}\tStart reading data')
#Change filename to the address you have saved the h5ad file to. 
adata=sc.read_h5ad(filename='./pijuan_gastrulation_via.h5ad') 

print(f'{datetime.now()}\tFinished reading data')
print(adata)
