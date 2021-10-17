
import basics.Decisions.and_operator as and_operator
import basics.Decisions.or_operator as or_operator
import basics.functions.ascii_code as ascii_code
import basics.functions.function_calls as function_calls
import basics.functions.function_with_loop as function_with_loop
import basics.functions.function_with_nesting as function_with_nesting
import basics.functions.function_with_parameter as function_with_parameter
import basics.functions.function_with_parameters as function_with_parameters
import basics.functions.return_values as return_values
import basics.functions.simple_function as simple_function
import basics.input.ascii_robot as ascii_robot
import basics.input.data_types as data_types
import basics.input.string_operators as string_operators
import basics.input.user_input as user_input
import basics.modules.guess_the_number as guess_the_number
import basics.Nested_decision.nestception as nestception
import basics.Nested_decision.nested as nested
import basics.output.ascii_art as ascii_art
import basics.output.escape_characters as escape_characters
import basics.output.simple_message as simple_message
import basics.output.multiline_message as multiline_message
import basics.simple_decision.comparison_operators as comparison_operators
import basics.simple_decision.counter as counter
import basics.simple_decision.if_ as if_
import basics.simple_decision.if_elif_else as if_elif_else
import basics.simple_decision.if_else as if_else
import basics.simple_decision.Modulo_operator as modulo_operator
import basics.repetitions.for_loop.simple as simple
import basics.repetitions.for_loop.range as range
import basics.repetitions.for_loop.characters as characters
import basics.repetitions.for_loop.Reverse as reverse
import basics.repetitions.for_loop.count_down as count_down
import basics.repetitions.nested_loop.nested as nested
import basics.repetitions.nested_loop.nesting as nesting
import basics.repetitions.while_loop.len as len
import basics.repetitions.while_loop.simple as simple
import basics.repetitions.while_loop.ascii
import basics.repetitions.while_loop.count
import basics.repetitions.while_loop.factorial
import basics.repetitions.while_loop.sum_100
import basics.repetitions.while_loop.sum_user_numbers








def run_block_a():
    print("Which program in 'Block A: Basics' do you wish to run?")
    response = input()
    if response == "simple_message":
        simple_message.run()
    elif response == "multiline_message":
        multiline_message.run()
    elif response == "and_operator":
        and_operator.run()
    elif response == "multiline_message":
        multiline_message.run()

def run():

    while(True):
        print("What would you like to do?")
        print("[a] Run 'Block A: Basics' programs")
        print("[q] Quit")
        response = input()

        if response == "a":
            run_block_a()
        elif response == "q":
            break
        else:
            print("Invalid option! Please try again.")

run()