# входной формат данных
well_data_1 = {
    # данные по слоям
    "layers": {
        1: {
            "id": 1,
            "name": "Q",
            "thick": 45.0,
            "sediments": ("пески мелкие", "пески средние", "пески крупные"),
            "interlayers": ("глины",),
        },
        2: {
            "id": 2,
            "name": "J\u2083",
            "thick": 10,
            "sediments": ("суглинки", "глины", "супеси"),
        },
        3: {
            "id": 3,
            "name": "J\u2083ox-c",
            "thick": 15,
            "sediments": ("мел", "гнейсы", "граниты"),
            "interlayers": ("глины",),
        },
        4: {
            "id": 4,
            "name": "C\u2083g-P\u2081a",
            "thick": 25,
            "sediments": (
                "известняки",
                "доломиты",
            ),
            "interlayers": ("глины",),
        },
    },
    # данные по скважине
    "well_data": {
        "columns": {
            1: {"id": 1, "D": 377, "from": 0.0, "till": 34.0, "type": "обсадная"},
            2: {"id": 2, "D": 273, "from": 0.0, "till": 74.0, "type": "обсадная"},
            3: {
                "id": 3,
                "D": 133,
                "from": 59.0,
                "till": 95.0,
                "type": "фильтровая",
                "filter": {
                    1: {"id": 1, "from": 75.0, "till": 79.0},
                    2: {"id": 2, "from": 85.0, "till": 90.0},
                },
            },
        },
        "pump_type": "ЭЦВ-6-10-110",
        "pump_depth": 55.0,
        "static_lvl": 32.0,
        "dynamic_lvl": 35.0,
        "well_depth": 95.0,
    },
}


# входной формат данных
well_data_2 = {
    # данные по слоям
    "layers": {
        1: {
            "id": 1,
            "name": "N\u2082",
            "thick": 45.0,
            "sediments": ("пески мелкие", "пески средние", "пески крупные"),
            "interlayers": ("глины",),
        },
        2: {
            "id": 2,
            "name": "N\u2081",
            "thick": 10,
            "sediments": ("суглинки", "глины", "супеси"),
        },
        3: {
            "id": 3,
            "name": "K\u2081",
            "thick": 15,
            "sediments": ("мел", "гнейсы", "граниты"),
            "interlayers": ("глины",),
        },
        4: {
            "id": 4,
            "name": "T\u2083",
            "thick": 25,
            "sediments": (
                "известняки",
                "доломиты",
            ),
            "interlayers": ("глины",),
        },
        5: {
            "id": 5,
            "name": "T\u2082",
            "thick": 10,
            "sediments": (
                "известняки",
                "доломиты",
            ),
        },
        6: {
            "id": 6,
            "name": "T\u2081",
            "thick": 10,
            "sediments": (
                "известняки",
                "доломиты",
            ),
        },
    },
    # данные по скважине
    "well_data": {
        "columns": {
            1: {"id": 1, "D": 377, "from": 0.0, "till": 34.0, "type": "обсадная"},
            2: {"id": 2, "D": 273, "from": 10.0, "till": 74.0, "type": "обсадная"},
            3: {"id": 3, "D": 213, "from": 50.0, "till": 96.0, "type": "обсадная"},
            4: {
                "id": 4,
                "D": 133,
                "from": 88.0,
                "till": 115.0,
                "type": "фильтровая",
                "filter": {
                    1: {"id": 1, "from": 98.0, "till": 103.0},
                    2: {"id": 2, "from": 104.0, "till": 109.0},
                    3: {"id": 3, "from": 112.0, "till": 114.0},
                },
            },
        },
        "pump_type": "Grundfos SP-15",
        "pump_depth": 75.0,
        "static_lvl": 32.0,
        "dynamic_lvl": 55.0,
        "well_depth": 115.0,
    },
}
