# членение фильтровой колонны на части (надфильтровая, фильтровая, отстойник)


def filter_sec(data):
    filters = data["filter"]
    result = []
    # print(data)

    if data["type"] == "О.С.":
        # Для типа "О.С." добавляем только одну часть - открытый ствол
        result.append(
            {
                "type": "Открытый ствол",
                "from": float(filters["1"]["from"]),
                "till": float(filters["1"]["till"]),
            }
        )
    else:
        # Для остальных типов
        frm = float(data["from"])  # Начальная точка фильтровой колонны
        tll = float(data["till"])  # Конечная точка фильтровой колонны

        for elem in filters:
            if frm != float(filters[elem]["from"]):
                # Добавляем надфильтровую часть, если есть разрыв
                result.append(
                    {
                        "type": "глухая надфильтровая часть",
                        "from": frm,
                        "till": float(filters[elem]["from"]),
                    }
                )
                frm = float(filters[elem]["till"])

            # Добавляем фильтрующую часть
            result.append(
                {
                    "type": "фильтрующая часть",
                    "from": float(filters[elem]["from"]),
                    "till": float(filters[elem]["till"]),
                }
            )

        if tll > frm:
            # Добавляем отстойник, если есть оставшаяся часть после фильтров
            result.append(
                {
                    "type": "отстойник",
                    "from": frm,
                    "till": tll,
                }
            )
    return result
