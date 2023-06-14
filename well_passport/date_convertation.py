from datetime import datetime


# расчет разницы в часах между началом и концом ОФР
def convertation_date(start, end):
    # преобращование даты начала и конца в объект dt
    end_dt = datetime(
        int(end[-4:]), int(end[-7:-5]), int(end[-10:-8]), int(end[0:2]), int(end[3:5])
    )
    start_dt = datetime(
        int(start[-4:]),
        int(start[-7:-5]),
        int(start[-10:-8]),
        int(start[0:2]),
        int(start[3:5]),
    )
    # считаем разницу
    res = end_dt - start_dt
    res_s = res.total_seconds()
    return divmod(res_s, 3600)[0]


# start = "14:00, 15.10.2009"
# end = "23:00, 15.10.2009"
# convertation_date(start, end)
