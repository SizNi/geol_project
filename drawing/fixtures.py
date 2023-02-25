# входной формат данных
well_data = {
    # данные по слоям
    'layers': {
        1: {
            'id': 1, 'name': 'Q', 'thick': 45.0, 'sediments': ('мергели',)
        },
        2: {
            'id': 2, 'name': 'J\u2083', 'thick': 10, 'sediments': ('глины',)
        },
        3: {
            'id': 3, 'name': 'J\u2083ox-c', 'thick': 15, 'sediments': ('суглинки',)
        },
        4: {
            'id': 4, 'name': 'C\u2083g-P\u2081a', 'thick': 25, 'sediments': ('известняки',)
        }
    },
    # конструкция скважины
    'well_data': {
        'columns': {
            1: {
                'id': 1, 'D': 377, 'from': 0.0, 'till': 34.0, 'type': 'обсадная'
            },
            2: {
                'id': 2, 'D': 273, 'from': 0.0, 'till': 74.0, 'type': 'обсадная'
            },
            3: {
                'id': 3, 'D': 133, 'from': 59.0, 'till': 95.0, 'type': 'фильтровая', 'filter': {
                    1: {'id': 1, 'from': 75.0, 'till': 79.0},
                    2: {'id': 2, 'from': 85.0, 'till': 90.0},
                }
            }
        },
        # обвес и другие параметры скважины
        'pump_type': 'ЭЦВ-6-10-110',
        'pump_depth': 55.0,
        'static_lvl': 32.0,
        'dynamic_lvl': 35.0,
        'well_depth': 95.0
    }}
