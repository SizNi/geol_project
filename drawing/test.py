well_dt = {'well_data': {
    'columns': {
        1: {'id': 1, 'D': 377, 'from': 0.0, 'till': 34.0, 'type': 'обсадная'},
        2: {'id': 2, 'D': 273, 'from': 0.0, 'till': 74.0, 'type': 'обсадная'},
        3: {'id': 3, 'D': 273, 'from': 70.0, 'till': 95.0, 'type': 'фильтровая', 'filter': {
            1: {'id': 1, 'from': 75.0, 'till': 79.0},
            1: {'id': 2, 'from': 85.0, 'till': 90.0},
        }}
    },
    'pump_type': 'ЭЦВ-6-10-110',
    'pump_depth': 55.0,
    'static_lvl': 32.0,
    'dynamic_lvl': 35.0,
    'well_depth': 95.0
}}
print(well_dt['well_data']['columns'][1])