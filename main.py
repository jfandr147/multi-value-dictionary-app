from operations import Operations
import util as u


def print_welcome():
    print(f'Welcome to Multi-Value Dictionary App')


def handle_input():
    memory_dictionary = {}
    o = Operations(memory_dictionary)
    while True:
        try:
            input_command = str(input())
            command_pieces = input_command.split(' ')
            if len(command_pieces) > 0:
                operation = command_pieces[0]
                parameters = [p for p in command_pieces[1:]]
                match operation:
                    case 'KEYS':
                        output, message = o.keys()
                    case 'MEMBERS':
                        output, message = o.members(parameters[0])
                    case 'ADD':
                        output, message = o.add(parameters[0], parameters[1])
                    case 'REMOVE':
                        output, message = o.remove_member(parameters[0], parameters[1])
                    case 'REMOVEALL':
                        output, message = o.remove_all(parameters[0])
                    case 'CLEAR':
                        output, message = o.clear()
                    case 'KEYEXISTS':
                        output, message = o.key_exists(parameters[0])
                    case 'MEMBEREXISTS':
                        output, message = o.member_exists(parameters[0], parameters[1])
                    case 'ALLMEMBERS':
                        output, message = o.all_members()
                    case 'ITEMS':
                        output, message = o.items()
                    case _:
                        output, message = None, "Operation Not Supported"

                u.print_output(output, message)
        except IndexError as i:
            print("Error Occurred, Missing One or More Input Parameter for Operation")
        except Exception as e:
            print("Unknown Error Occurred During Operation, Check Syntax")


if __name__ == '__main__':
    print_welcome()
    handle_input()
