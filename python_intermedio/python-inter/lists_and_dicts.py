def run():
    my_list = [1, 'hello', True, 4.5]
    my_dict = {'firstname': 'Guillermo', 'lastname': 'Moreno'}

    super_list = [
      {'firstname': 'Guillermo', 'lastname': 'Moreno'},
      {'firstname': 'Ana', 'lastname': 'Quezada'},
      {'firstname': 'Sergio', 'lastname': 'Mendez'},
      {'firstname': 'Jose', 'lastname': 'Perez'}
    ]

    super_dict = {
      'natural_nums': [1, 2, 3, 4, 5],
      'integer_nums': [-1, -2, 0, 1, 2],
      'floating_nums': [1.1, 4.5, 6.43]
    }

    # for key, value in super_dict.items():
    #     print(key, '-', value)
    for i in super_list:
        print(i.items())


if __name__ == '__main__':
    run()