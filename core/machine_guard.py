import uuid

AUTHORIZED_MACHINES = [

    "OFFICE_PC_ID",
    "LAPTOP_ID"
]


def get_machine_id():

    return str(uuid.getnode())


def verify_machine():

    if get_machine_id() not in AUTHORIZED_MACHINES:

        print("Unauthorized machine blocked")

        exit()
