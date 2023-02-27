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
            "name": "J3",
            "thick": 10,
            "sediments": ("суглинки", "глины", "супеси"),
        },
        3: {
            "id": 3,
            "name": "J3ox-c",
            "thick": 15,
            "sediments": ("мел", "гнейсы", "граниты"),
            "interlayers": ("глины",),
        },
        4: {
            "id": 4,
            "name": "C3g-P1a",
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
            "name": "N2",
            "thick": 45.0,
            "sediments": ("пески мелкие", "пески средние", "пески крупные"),
            "interlayers": ("глины",),
        },
        2: {
            "id": 2,
            "name": "N1-2",
            "thick": 10,
            "sediments": ("суглинки", "глины", "супеси"),
        },
        3: {
            "id": 3,
            "name": "K1",
            "thick": 15,
            "sediments": ("мел", "гнейсы", "граниты"),
            "interlayers": ("глины",),
        },
        4: {
            "id": 4,
            "name": "T3",
            "thick": 25,
            "sediments": (
                "известняки",
                "доломиты",
            ),
            "interlayers": ("глины",),
        },
        5: {
            "id": 5,
            "name": "T2",
            "thick": 10,
            "sediments": (
                "известняки",
                "доломиты",
            ),
        },
        6: {
            "id": 6,
            "name": "T1kus-kus",
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


# входной формат данных
well_data_3 = {
    # данные по слоям
    "layers": {
        1: {
            "id": 1,
            "name": "Q",
            "thick": 10.0,
            "sediments": ("пески мелкие",),
            "interlayers": ("глины",),
        },
        2: {
            "id": 2,
            "name": "N2",
            "thick": 10,
            "sediments": ("суглинки", "глины", "супеси"),
        },
        3: {
            "id": 3,
            "name": "N1",
            "thick": 10,
            "sediments": ("мел", "гнейсы", "граниты"),
            "interlayers": ("глины",),
        },
        4: {
            "id": 4,
            "name": "K2",
            "thick": 10,
            "sediments": ("суглинки", "супеси"),
            "interlayers": ("глины",),
        },
        5: {
            "id": 5,
            "name": "K1",
            "thick": 10,
            "sediments": ("пески мелкие",),
            "interlayers": ("песчаники",),
        },
        6: {
            "id": 6,
            "name": "J3kl-ox",
            "thick": 10,
            "sediments": ("глины",),
            "interlayers": ("суглинки",),
        },
        7: {
            "id": 7,
            "name": "J2",
            "thick": 10,
            "sediments": ("глины",),
        },
        8: {
            "id": 8,
            "name": "J1",
            "thick": 10,
            "sediments": ("супеси",),
        },
        9: {
            "id": 9,
            "name": "T3",
            "thick": 10,
            "sediments": ("граниты",),
        },
        10: {
            "id": 10,
            "name": "T2",
            "thick": 10,
            "sediments": ("гнейсы",),
        },
        11: {
            "id": 11,
            "name": "T2",
            "thick": 10,
            "sediments": ("доломиты",),
        },
        12: {
            "id": 12,
            "name": "P3",
            "thick": 10,
            "sediments": ("мел",),
        },
        13: {
            "id": 13,
            "name": "P2",
            "thick": 10,
            "sediments": ("граниты", 'известняки'),
        },
        14: {
            "id": 14,
            "name": "P1",
            "thick": 10,
            "sediments": ("граниты", 'известняки'),
        },
        15: {
            "id": 15,
            "name": "C3",
            "thick": 10,
            "sediments": ('известняки', 'глины'),
        },
        16: {
            "id": 16,
            "name": "C2",
            "thick": 10,
            "sediments": ('известняки', 'глины'),
        },
        17: {
            "id": 17,
            "name": "C1",
            "thick": 10,
            "sediments": ('известняки', 'глины', 'доломиты'),
        },
        18: {
            "id": 18,
            "name": "D2",
            "thick": 10,
            "sediments": ('глины',),
        },
        19: {
            "id": 19,
            "name": "S2",
            "thick": 10,
            "sediments": ('гнейсы',),
        },
    },
    # данные по скважине
    "well_data": {
        "columns": {
            1: {"id": 1, "D": 377, "from": 0.0, "till": 34.0, "type": "обсадная"},
            2: {"id": 2, "D": 273, "from": 10.0, "till": 74.0, "type": "обсадная"},
            3: {"id": 3, "D": 213, "from": 50.0, "till": 96.0, "type": "обсадная"},
            4: {"id": 4, "D": 133, "from": 94.0, "till": 176.0, "type": "обсадная"},
            5: {
                "id": 5,
                "D": 113,
                "from": 170.0,
                "till": 190.0,
                "type": "фильтровая",
                "filter": {
                        1: {"id": 1, "from": 177.0, "till": 180.0},
                        2: {"id": 2, "from": 183.0, "till": 185.0},
                        3: {"id": 3, "from": 186.0, "till": 188.0},
                },
            },
        },
        "pump_type": "Grundfos SP-15",
        "pump_depth": 81.0,
        "static_lvl": 110.0,
        "dynamic_lvl": 125.0,
        "well_depth": 190.0,
    },
}
