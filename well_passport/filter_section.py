# членение фильтровой колонны на части (надфильтровая, фильтровая, отстойник)


def filter_sec(data):
    filter = data["filter"]
    if data["type"] == "О.С.":
        return [
            {
                "type": "Открытый ствол",
                "from": float(filter["1"]["from"]),
                "till": float(filter["1"]["till"]),
            },
        ]
    else:
        res = []
        # интервал фильтровой колонны в целом
        frm = float(data["from"])
        tll = float(data["till"])
        # добавление надфильтровой и фильтровой части
        for elem in filter:
            if frm != float(filter[elem]["from"]):
                res.append(
                    {
                        "type": "глухая надфильтровая часть",
                        "from": frm,
                        "till": float(filter[elem]["from"]),
                    }
                )
                frm = float(filter[elem]["till"])
            res.append(
                {
                    "type": "фильтрующая часть",
                    "from": float(filter[elem]["from"]),
                    "till": float(filter[elem]["till"]),
                }
            )
        # добавление отстояника
        if tll > frm:
            res.append({"type": "отстойник", "from": frm, "till": tll})
    return res


# filter_sec(a)
