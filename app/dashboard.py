import json
import string
import random

class DashboardManager():
    def __init__(self):
        self.dashboards = []
    
    def add_dashboard(self, Name, Layout):
        dashboard = Dashboard(Name, Layout)
        self.dashboards.append(dashboard)
        return dashboard.id, dashboard.token
    
    def get_dashboard_by_id(self, ID):
        result = None
        for dashboard in self.dashboards:
            if dashboard.id == ID:
                result = dashboard
        
        return result

class Dashboard():
    def __init__(self, Name, Layout):
        _id, _token = random_string(), random_string(N=64)
        self.id = _id
        self.token = _token
        self.name = Name
        self.vars = []
        self.arrs = []
        self.layout = Layout
    
    def set_id(self, ID):
        self.id = ID

    def add_var(self, Name, Type):
        self.vars.append({'type': Type, 'name': Name, 'value': 0})
    
    def set_var_value(self, VarName, Value):
        variable = self.get_var(VarName)
        variable_index = self.get_vars().index(variable)

        variable['value'] = Value

        self.vars[variable_index] = variable

        return 1
    
    def get_vars(self):
        return self.vars
    
    def get_var(self, VarName):
        result = None
        for variable in self.get_vars():
            if variable['name'] == VarName:
                result = variable
                break
        
        return result
    
    def add_arr(self, Name):
        self.arrs.append({'name': Name, 'value': [], 'labels': []})
    
    def set_arr_value(self, ArrName, Value):
        array = self.get_arr(ArrName)
        array_index = self.get_arrs().index(array)

        array['value'] = Value

        self.arrs[array_index] = array

        return 1

    def set_arr_labels(self, ArrName, Labels):
        array = self.get_arr(ArrName)
        array_index = self.get_arrs().index(array)

        array['labels'] = Labels

        self.arrs[array_index] = array

        return 1
    
    def get_arrs(self):
        return self.arrs
    
    def get_arr(self, ArrName):
        result = None
        for array in self.get_arrs():
            if array['name'] == ArrName:
                result = array
                break
        
        return result

def random_string(N=20):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(N))