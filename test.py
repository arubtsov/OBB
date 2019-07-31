from draft import *
# create a train station
platform = Platform('platform 1')
train_station = TrainStation('Linz')
train_station.add_platform(platform)
# create a train
train_1 = ICE('ICE 1')
platform.accept_train(train_1)
train_section_1 = TrainSection('First section')
train_section_2 = TrainSection('Second section')
train_section_3 = TrainSection('Third section')
train_1.dock_section(train_section_1)
train_1.dock_section(train_section_2)
train_1.dock_section(train_section_3)
train_1.print_sections()
# Expected output: First section - Second section - Third section
# create persons
person_1 = Person('Franz', 'Mair')
person_2 = Person('Michael', 'Schuh')
person_3 = Person('Herbert', 'Sailer')
person_4 = Person('Michaela', 'Mader')
train_section_1.get_on_train(person_1)
# Expected output: Franz Mair is on the train now
train_section_1.get_on_train(person_2)
# Expected output: Michael Schuh is on the train now
train_section_2.get_on_train(person_3)
# Expected output: Herbert Sailer is on the train now
train_section_3.get_on_train(person_4)
# Expected output: Michaela Mader is on the train now
train_section_2.get_off_train(person_3)
# Expected output: Herbert Sailer has left the train
# query passengers
train_1.show_current_passengers()
# Expected output: Franz Mair, Michel Schuh, Michaela Mader
train_1.count_passengers()
# Expected output: 3
