objects = []


def gen_id(arr):
    ids = 0
    check = True
    while check:
        check_tmp = False
        for i in arr:
            if i.get_id() == ids:
                check_tmp = True
        if check_tmp:
            ids = ids + 1
        else:
            check = False
    return ids


class Vehicle:
    def __init__(self):
        self.key = ''
        self.power = 0
        self.tmp_char = 0
        self.id = 0
        self.consumption = 0

    def get_id(self):
        return self.id


    def get_key(self):
        return self.key


    def set_char(self, key, power, tmp_char, idd, con):
        self.key = key
        self.power = power
        self.tmp_char = tmp_char
        self.id = idd
        self.consumption = con

    def get_char(self):
        return self.id, self.power, self.tmp_char, self.consumption


f = open('in.txt')


def in_Car(new_veh):
    text = f.readline()
    a = text.split(' ')
    key = 'CAR'
    power = int(a[0])
    tmp = int(a[1])
    con = int(a[2])
    idd = gen_id(objects)
    new_veh.set_char( key, power, tmp, idd, con)

    return new_veh


def new_func(veh):
    if veh.key == 'BUS':
        return 75 * veh.tmp_char / veh.power
    elif veh.key == 'TRUCK':
        return veh.tmp_char / veh.power
    elif veh.key == 'CAR':
        return 5*75 / veh.power

def sort_objects():
    N = len(objects)
    for i in range(N - 1):
        for j in range(N - i - 1):
            if objects[j].get_key() > objects[j+1].get_key():
                objects[j], objects[j+1] = objects[j+1], objects[j]


def in_Bus(new_veh):
    text = f.readline()
    a = text.split(' ')
    key = 'BUS'
    power = int(a[0])
    tmp = int(a[1])
    con = int(a[2])
    idd = gen_id(objects)
    new_veh.set_char( key, power, tmp, idd, con)

    return new_veh


def in_Truck(new_veh):
    text = f.readline()
    a = text.split(' ')
    key = 'TRUCK'
    power = int(a[0])
    tmp = int(a[1])
    con = int(a[2])
    idd = gen_id(objects)
    new_veh.set_char( key, power, tmp, idd, con)

    return new_veh


def out_Car(out_veh):
    a = out_veh.get_char()
    print(f'{a[0]}: It is CAR, Power = {a[1]}, Max speed = {a[2]}, consumption = {a[3]}')


def car_info(out_veh):
    a = out_veh.get_char()
    return f'{a[0]}: It is CAR, Power = {a[1]}, Max speed = {a[2]}, consumption = {a[3]}'


def out_Bus(out_veh):
    a = out_veh.get_char()
    print(f'{a[0]}: It is BUS, Power = {a[1]}, capacity = {a[2]}, consumption = {a[3]}')


def bus_info(out_veh):
    a = out_veh.get_char()
    return f'{a[0]}: It is BUS, Power = {a[1]}, capacity = {a[2]}, consumption = {a[3]}'


def out_Truck(out_veh):
    a = out_veh.get_char()
    print(f'{a[0]}: It is TRUCK, Power = {a[1]}, maxWeight = {a[2]}, consumption = {a[3]}')


def truck_info(out_veh):
    a = out_veh.get_char()
    return f'{a[0]}: It is TRUCK, Power = {a[1]}, maxWeight = {a[2]}, consumption = {a[3]}'


def clear_container():
    objects.clear()


def file_in():
    check = True
    while check:
        text = f.readline()
        if text == '':
            check = False
        else:
            text = text.split('\n')
            type = int(text[0])
            if type == 1:  # ?????? BUS
                veh = Vehicle()
                veh = in_Bus(veh)
                objects.append(veh)
            elif type == 2:
                veh1 = Vehicle()
                veh1 = in_Truck(veh1)
                objects.append(veh1)
            elif type == 3:
                veh1 = Vehicle()
                veh1 = in_Car(veh1)
                objects.append(veh1)
