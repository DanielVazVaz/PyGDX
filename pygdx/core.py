from .version_check import GAMS_PATH, PYTHON_VERSION
import sys
import os
import pandas as pd

class GDXFile:
    """Main class of the GDX file
    """
    def __init__(self, gdx_path: str, gams_path: str = GAMS_PATH) -> None:
        self.gams_path = gams_path
        if not self.gams_path:
            print("WARNING!!: Gams path is not found. Set it up with the method set_gams_path")
        else:
            self.gams_path = gams_path
            self.set_gams_path(self.gams_path)
        self.gdx_path = gdx_path
        self.python_version = PYTHON_VERSION
        
    def set_gams_path(self, gams_path: str) -> None:
        """Sets the GAMS path

        Args:
            gams_path (str): Raw path to the GAMS folder.
        """
        self.gams_path = gams_path
        apifile_gams_folder = os.path.join(self.gams_path, "apifiles", "Python", "gams")
        apifile_api_folder  = os.path.join(self.gams_path, "apifiles", 
                                           "Python", f"api_{PYTHON_VERSION[0]}{PYTHON_VERSION[1]}")
        for folder in [apifile_gams_folder, apifile_api_folder]:
            if folder not in sys.path:
                sys.path.append(folder)
        import gams
        self.gams_module = gams
        
    def get_workspace(self) -> "GamsWorkspace":
        """Gets the workspace object
        
        Returns:
            GamsWorkspace: Gams workspace object
        """       
        return self.gams_module.GamsWorkspace(system_directory = self.gams_path,
                                              working_directory = os.getcwd())
    def read_gdx(self):
        """Reads the GDX file. Creates the workspace, the database from a given gdx,
        and creates the dataframes of sets, variables and parameters.
        """
        self.ws = self.get_workspace()
        self.database = self.ws.add_database_from_gdx(self.gdx_path)
        self.classify_data(self.database)
        
    def classify_data(self, database):
        """Creates the dictionaries of sets, parameters, and variables that point to
        gams objects. It also creates the dataframes for these three data structures.

        Args:
            database (GamsDatabase): Gams database object
        """        
        self.sets       = {}
        self.parameters = {}
        self.variables  = {}
        for i in database:
            if type(i) == self.gams_module.GamsSet:
                self.sets[i.name] = i
            elif type(i) == self.gams_module.GamsParameter:
                self.parameters[i.name] = i
            elif type(i) == self.gams_module.GamsVariable:
                self.variables[i.name] = i
                
        self.sets_df       = {}
        self.parameters_df = {}
        self.variables_df  = {}
        for s in self.sets:
            self.sets_df[s]       = self._set_to_df(self.sets[s])
        for p in self.parameters:
            self.parameters_df[p] = self._parameter_to_df(self.parameters[p])
        for v in self.variables:
            self.variables_df[v]  = self._variable_to_df(self.variables[v])

    def _set_to_df(self, set_object):
        """Transforms a gams set object into a 
        dataframe

        Args:
            set_object (GamsSet): Gams object for the set
        """
        df = pd.DataFrame()
        list_sets = [s for s in set_object]
        list_domains = set_object.domains
        length_domains = len(list_domains)
        for j in range(length_domains):
            df[j] = [k.key(j) for k in list_sets]
        if list_domains[0] == "*":
            df.columns = [set_object.name]
        else:
            df.columns = [domain.name for domain in list_domains]
        df["Value"] = True
        return df

    def _parameter_to_df(self, param_object):
        """Transforms a gams parameter object into a 
        dataframe

        Args:
            param_object (GamsParameter): Gams object for the parameter
        """
        df = pd.DataFrame()
        list_params = [s for s in param_object]
        list_domains = param_object.domains
        length_domains = len(list_domains)
        for j in range(length_domains):
            df[j] = [k.key(j) for k in list_params]
        if length_domains == 0:
            pass
        else:
            ## For some reason, some domains are read as *. So for those we put a try and catch it with the name
            try:
                df.columns = [domain.name for domain in list_domains]
            except:
                df.columns = [domain for domain in list_domains]
        df["Value"] = [v.value for v in param_object]
        return df
    
    def _variable_to_df(self, var_object):
        """Transforms a gams variable object into a 
        dataframe

        Args:
            var_object (GamsVariable): Gams object for the variable
        """
        df = pd.DataFrame()
        list_sets = [s for s in var_object]
        list_domains = var_object.domains
        length_domains = len(list_domains)
        for j in range(length_domains):
            df[j] = [k.key(j) for k in list_sets]
        if length_domains == 0:
            pass
        else:
            ## For some reason, some domains are read as *. So for those we put a try and catch it with the name
            try:
                df.columns = [domain.name for domain in list_domains]
            except:
                df.columns = [domain for domain in list_domains]
        df["Level"] = [v.level for v in var_object]
        df["LB"] = [v.lower for v in var_object]
        df["UB"] = [v.upper for v in var_object]
        return df
        




