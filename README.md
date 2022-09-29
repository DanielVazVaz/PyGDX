# PyGDX
Use of the GAMS' Python API to read GDX files to pandas dataframes. It should work for any Python version higher than 3.8 and for any GAMS version higher than 32.

## Installation 
Install the latest version of this repository to your machine following one of the options below accordingly to your preferences:

- users with git:
```
git clone https://github.com/DanielVazVaz/PySIS.git
cd PySIS
pip install -e .
```
- users without git:

Browser to https://github.com/DanielVazVaz/PyGDX, click on the Code button and select Download ZIP. Unzip the files from your Download folder to the desired one. Open a terminal inside the folder you just unzipped (make sure this is the folder containing the setup.py file). Run the following command in the terminal:
```
pip install -e .
```

## About 0 values
As you know, a GDX saves what considers important data, and therefore, all parameters that are equal to zero (**parameters**, not **variables**), are not saved in it. 

It is recommended to save parameters with an epsilon in GAMS. This being:
```gams
PARAMETERS
a(i) Some parameter which has 0 for some i
;

*Whole model here
*solving the model

a(i) = a(i) + EPS;
execute_unload 'results';
```
Therefore, you make sure that the value of the parameter is saved on the GDX. 

