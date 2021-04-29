def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict ={"firstname": "Facundo", "lastname":"Garcia"}

    super_list = [
        {"firstname": "Facundo", "lastname":"Garcia"},
        {"firstname": "Miguel", "lastname":"Torres"},
        {"firstname": "Pepe", "lastname":"Rodelo"},
        {"firstname": "Suzana", "lastname":"Martinez"},
        {"firstname": "Jose", "lastname":"Garcia"},
    ]

    super_dict = {
        "natural_num": [1,2,3,4,5],
        "integer_num": [-1,-2,0,1,2],
        "floating_num": [1.1,4.5,6.43]
    }

    for key, value in super_dict.items():
        print(key,"-",value)

    for i in super_list:
        print(i["firstname"],i["lastname"])

if __name__ == '__main__':
    run()