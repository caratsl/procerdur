from vehicles import *



file_in()
if len(objects) == 0:
    print("Container is empty")
else:
    print("Container is filled")
    print(f"Contains {len(objects)} element(s)")
    sort_objects()
    for i in objects:
        if i.key == 'BUS':
            out_Bus(i)
        elif i.key == 'TRUCK':
            out_Truck(i)

    clear_container()
    print("Container is empty")
    print(f"Contains {len(objects)} element(s)")

