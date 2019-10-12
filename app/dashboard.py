import json
import string
import random

class DashboardManager():
    def __init__(self):
        self.dashboards = []
    
    def add_dashboard(self, Name):
        dashboard = Dashboard(Name)
        self.dashboards.append(dashboard)
        return dashboard.id, dashboard.token
    
    def get_dashboard_by_id(self, ID):
        result = None
        for dashboard in self.dashboards:
            if dashboard.id == ID:
                result = dashboard
        
        return result

class Dashboard():
    def __init__(self, Name):
        _id, _token = random_string(), random_string(N=64)
        self.id = _id
        self.token = _token
        self.name = Name
        self.vars = []
        self.layout = [
                [
                    {
                        "type": "text",
                        "name": "text1",
                        "background": "#fff",
                        "color": "#999",
                        "var_index": [0],
                        "width": 0
                    },
                    {
                        "type": "text",
                        "name": "text2",
                        "background": "#fff",
                        "color": "#999",
                        "var_index": [1],
                        "width": 0
                    },
                    {
                        "type": "text",
                        "name": "text3",
                        "background": "#fff",
                        "color": "#999",
                        "var_index": [2],
                        "width": 0
                    },
                    {
                        "type": "text",
                        "name": "text4",
                        "background": "#fff",
                        "color": "#999",
                        "var_index": [3],
                        "width": 0
                    }
                ],
                [
                    {
                        "type": "plot",
                        "name": "plot1",
                        "background": "#23255c",
                        "color": "#fff",
                        "var_index": [0, 1],
                        "width": 8,
                        "config": {
                        }
                    },
                    {
                        "type": "plot",
                        "name": "plot2",
                        "background": "#23255c",
                        "color": "#fff",
                        "var_index": [1],
                        "width": 4,
                        "config": {
                        }
                    }
                ]
            ]
    
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

def random_string(N=20):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(N))