def print_output(output_object, message):
    if type(output_object) is dict:
        print_dictionary_console(output_object)
    elif type(output_object) is list:
        print_list_console(output_object)
    elif not output_object:
        print_message_console(message)


def print_dictionary_console(dict_obj):
    counter = 1
    for the_key in dict_obj.keys():
        for member in dict_obj[the_key]:
            print("{}) {}: {}".format(counter, the_key, member))
            counter += 1


def print_list_console(the_list):
    counter = 1
    for m in the_list:
        print("{}) {}".format(counter, m))
        counter += 1


def print_message_console(message):
    print(") {}".format(message))
