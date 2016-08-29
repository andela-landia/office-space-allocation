import sqlite3

rooms = {
    'Office': {},
    'LivingSpace': {}
}


class Amity(object):
    """Super class for amity"""

    def __init__(self):
        super(Amity, self).__init__()
        # self.rooms = {
        #     'Office': [],
        #     'LivingSpace': []
        # }

    def create_room(self, args):
        """Allows user to enter a list of room names specifying
                whether office or living spaces"""

        room_type = None

        # Assign a group of rooms to a room type
        if room_type is None:
            room_type = raw_input(
                "Enter room type: \n o: Office space \n l: Living space: \n")

            if room_type != "o" and room_type != "l":
                room_type = raw_input(
                    "Try again. Enter Room Type:\n o: Office space \n l: Living space: \n")
            room_type = room_type.upper()

        # Adds room to the rooms dict
        for room in args["<room_name>"]:
            if room_type == "O":
                rooms['Office'].update({room: []})
            elif room_type == "L":
                rooms['LivingSpace'].update({room: []})

        print "You have created the following rooms: \n"\
            + "OFFICES: " + ', '.join(rooms['Office'].keys()) +\
            "\nLIVING SPACES: " + ', '.join(rooms['LivingSpace'].keys())

        return rooms

    def save_state(self,args):
        """
        Takes up an optional argument --db that specifies the database to store the data in rooms and people dictionary.
        Creates database and saves data.
        """
        print args

    def load_state(self):
        pass
