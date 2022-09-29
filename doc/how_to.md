# Basic how to

Once installed, make sure that it can be imported.

```python
import pygdx.core as gdx
import pandas as pd  
```

If there is no error, everything should be alright.

## Reading a GDX
The package can find a GAMS installation that is in the path, however, to be sure of the GAMS you are using, it is recommended to give it to it directly when creating an instance.

```python
GAMS_FOLDER = r"C:\GAMS\38"    # May look something like this. 
GDX_FILE = r"GDX_File.gdx"
```

Once the paths are set, it is enough with generating an instance of the `GDXFile` class and run the `read_gdx` method.

```python
results = gdx.GDXFile(gdx_path = GDX_FILE, gams_path = GAMS_FOLDER)
results.read_gdx()
```

If this does not return any error, all sets, variables, and parameters of the gdx have been correctly read. You can extract the dictionaries of dataframes as follows:

```python
sets       = results.sets_df
parameters = results.parameters_df
variables  = results.variables_df
```

And each value of the dictionary is a dataframe. 

```python
print(sets["i"])    # Assuming that i is a set present in the gdx, this returns a 
                    # dataframe
```

From there, you can operate with `pandas` normally. 
