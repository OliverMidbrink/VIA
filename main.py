#Import packages
import scanpy as sc
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import time
print("Importing via")
start_time = time.time()
import VIA
time_elapsed = time.time() - start_time
print("Done importing via. Took {} seconds".format(time_elapsed))
from datetime import datetime

print(f'{datetime.now()}\tStart reading data')
#Change filename to the address you have saved the h5ad file to. 
adata=sc.read_h5ad( filename='./data/pijuan_gastrulation_via.h5ad') 

print(f'{datetime.now()}\tFinished reading data')
print(adata)
