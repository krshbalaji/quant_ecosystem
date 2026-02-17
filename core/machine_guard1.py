import socket
import hashlib


def get_machine_id():

    name = socket.gethostname()

    return hashlib.sha256(name.encode()).hexdigest()


# ADD BOTH MACHINE IDs HERE
AUTHORIZED_MACHINES = [

    # Office PC
    "ADD_OFFICE_MACHINE_ID",

    # Home Laptop
    "2b1aa12fefb5903201006bb730bc6c507710308ba12a70356e8a6b9e6d7906ee",

]


def authorize_machine():

    machine_id = get_machine_id()

    print("Machine ID:", machine_id)

    if machine_id in AUTHORIZED_MACHINES:

        print("Machine authorized")

        return True

    print("Unauthorized machine blocked")

    return False
