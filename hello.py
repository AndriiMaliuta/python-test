name2 = 'Petro'
names = ["Ignat", "Petro", "Lyvko"]


def add_to_names(new_name):
    names.append(new_name)

add_to_names("Brunnie")

for name in names:
    print("Name is " + name)


def print_smth(name):
    print(name)
    print(name2)


if __name__ == '__main__':
    print_smth('vasyl')
