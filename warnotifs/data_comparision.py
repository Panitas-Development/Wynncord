from territories import get_territories

old_data = []

def data_comparision():
    global old_data
    newdata = get_territories()

    if len(old_data) == 0:
        old_data = newdata
        return

    if old_data == newdata: return

