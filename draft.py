class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.full_name = "{} {}".format(self.name, self.surname)


class TrainSection:
    def __init__(self, name, capacity=30):
        self.name = name
        self.next = None
        self.capacity = capacity
        self.passengers = {}

    def dock_next_section(self, next_section):
        self.next = next_section

    def get_on_train(self, passnager):
        self.passengers[passnager.full_name] = passnager
        print("{} is on the train now.".format(passnager.full_name))

    def get_off_train(self, passnager):
        del self.passengers[passnager.full_name]
        print("{} has left the train.".format(passnager.full_name))

    def get_passangers_count(self):
        return len(self.passengers)
    
    def get_passangers_names(self):
        return self.passengers.keys()


class Train:
    def __init__(self, name):
        self.name = name
        self.head = None

    def __iter__(self):
        current = self.head

        while current is not None:            
            yield current
            current = current.next

    def dock_section(self, section):
        last_section = None

        for docked_section in self:
            last_section = docked_section

        if last_section is not None:
            last_section.dock_next_section(section)
        else:
            self.head = section

    def print_sections(self):
        section_names = []
        
        for section in self:
            section_names.append(section.name)

        print(' - '.join(section_names))

    def show_current_passengers(self):
        passenger_names = []        

        for section in self:
            passenger_names.extend(section.get_passangers_names())

        print(', '.join(passenger_names))

        return passenger_names

    def count_passengers(self):
        count = 0        

        for section in self:
            count += section.get_passangers_count()

        print('Passengers count: {}'.format(count))

        return count


class ICE(Train):
    def dock_train(self, train):
        self.dock_section(train.head)


class Railjet(Train):
    def close_windows(self):
        print('Windows closed')


class Platform:
    def __init__(self, name):
        self.name = name
        self.train = None

    def accept_train(self, train):
        self.train = train


class TrainStation:
    def __init__(self, name):
        self.name = name
        self.platforms = {}

    def add_platform(self, platform):
        self.platforms[platform.name] = platform
