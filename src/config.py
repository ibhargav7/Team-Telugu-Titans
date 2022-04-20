import configparser
config = configparser.ConfigParser()

config.add_section('info')
config.set('info', 'teacher_name', 'bhargav')
config.set('info', 'student_name', 'qwerty')

with open(r"configfile.ini", 'w') as configfile:
    config.write(configfile)