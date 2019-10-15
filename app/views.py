from flask import render_template, request, redirect, jsonify

from app.dashboard import Dashboard, DashboardManager
from app import app

@app.route('/<dash_id>', methods=['GET'])
def index(dash_id):
    dashboard = dash_manager.get_dashboard_by_id(dash_id)

    if dashboard is None:
        return render_template('layouts/default.html',
            content=render_template('pages/not_found.html', dash_id=d_id))

    return render_template('layouts/default.html',
        content=render_template('pages/index.html', dashboard=dashboard))

@app.route('/<dash_id>/vars', methods=['GET'])
def get_vars(dash_id):
    dashboard = dash_manager.get_dashboard_by_id(dash_id)

    # Dashboard by id not found
    if dashboard is None:
        return jsonify(1)

    # Succces
    return jsonify(dashboard.get_vars())

@app.route('/<dash_id>/arrs', methods=['GET'])
def get_arrs(dash_id):
    dashboard = dash_manager.get_dashboard_by_id(dash_id)

    # Dashboard by id not found
    if dashboard is None:
        return jsonify(1)

    # Success
    return jsonify(dashboard.get_arrs())

@app.route('/<dash_id>/vars/<var_name>', methods=['GET'])
def get_var(dash_id, var_name):
    dashboard = dash_manager.get_dashboard_by_id(dash_id)

    # Dashboard by id not found
    if dashboard is None:
        return jsonify(1)

    variable = dashboard.get_var(var_name)

    # Variable not found
    if variable == None:
        return jsonify(2)

    return jsonify(variable)

@app.route('/<dash_id>/vars/<var_name>/<new_value>', methods=['GET'])
def set_var(dash_id, var_name, new_value):
    dashboard = dash_manager.get_dashboard_by_id(dash_id)

    # Dashboard by id not found
    if dashboard is None:
        return jsonify(1)
    
    # Invalid variable type
    if dashboard.get_var(var_name)['type'] == 'num':
        if not isinstance(new_value, int) or not isinstance(new_value, float):
            return jsonify(2)

    result = dashboard.set_var_value(var_name, new_value)

    if result == 0:
        return jsonify(0)

    # Success
    return jsonify(3)


@app.route('/<dash_id>/arrs/<arr_name>/<new_value>', methods=['GET'])
def set_arr_value(dash_id, arr_name, new_value):
    dashboard = dash_manager.get_dashboard_by_id(dash_id)

    # Dashboard by id not found
    if dashboard is None:
        return jsonify(1)

    # Invalid variable type
    if dashboard.get_arr(arr_name)['type'] == 'num':
        for val in new_value:
            if not isinstance(val, int) or not isinstance(val, float):
                return jsonify(2)
    
    # Length does not correspond
    if not len(new_value) is len(dashboard.get_arr(arr_name)['value']):
        return jsonify(3)

    result = dashboard.set_arr_value(arr_name, new_value)

    if result == 0:
        return jsonify(0)

    return jsonify(1)

dash_manager = DashboardManager()
d_id, d_token = dash_manager.add_dashboard('Dashboard 1')

dash = dash_manager.get_dashboard_by_id(d_id)
dash.set_id('test')
dash.add_var('var1', 'num')
dash.add_var('var2', 'num')
dash.add_var('var3', 'str')
dash.add_var('var4', 'str')
dash.add_arr('arr1', 'num')
dash.set_arr_value('arr1', [0, 1, 2, 3, 4])
dash.set_arr_labels('arr1', ['a', 'b', 'c', 'd', 'e'])