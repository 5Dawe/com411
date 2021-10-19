
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
import basics.repetitions.nested_loop.nested as loop_nested
import basics.repetitions.nested_loop.nesting as nesting
import basics.repetitions.while_loop.len as len
import basics.repetitions.while_loop.simple as while_simple
import basics.repetitions.while_loop.ascii as while_ascii
import basics.repetitions.while_loop.count as while_count
import basics.repetitions.while_loop.factorial as while_factorial
import basics.repetitions.while_loop.sum_100 as while_sum_100
import basics.repetitions.while_loop.sum_user_numbers as while_sum_user_numbers








def run_block_a():
    print("Which program in 'Block A: Basics' do you wish to run?")
    print(f"\nand_operator   #   guess_the_number   #   range")
    print(f"or_operator   #   nestception   #   characters")
    print(f"ascii_code   #   nested   #   reverse")
    print(f"function_calls   #   ascii_art   #   count_down")
    print(f"function_with_loop   #   escape_characters   #   nested")
    print(f"function_with_nesting   #   simple_message   #   nesting")
    print(f"function_with_parameter   #   multiline_message   #   len")
    print(f"function_with_parameters   #   comparison_operators   #   simple")
    print(f"return_values   #   counter   #   while_ascii")
    print(f"simple_function   #   if_   #   while_count")
    print(f"ascii_robot   #   if_elif_else   #   while_factorial")
    print(f"data_types   #   if_else   #   while_sum_100")
    print(f"string_operators   #   modulo_operator   #   while_sum_user_numbers")
    print(f"user_input   #   simple   #   ")

    response = input()
    if response == "and_operator":
        and_operator.run()
    elif response == "or_operator":
        or_operator.run()
    elif response == "ascii_code":
        ascii_code.run()
    elif response == "function_calls":
        function_calls.run()
    elif response == "function_with_loop":
        function_with_loop.run()
    elif response == "function_with_nesting":
        function_with_nesting.run()
    elif response == "function_with_parameter":
        function_with_parameter.run()
    elif response == "function_with_parameters":
        function_with_parameters.run()
    elif response == "return_values":
        return_values.run()
    elif response == "simple_function":
        simple_function.run()
    elif response == "ascii_robot":
        ascii_robot.run()
    elif response == "data_types":
        data_types.run()
    elif response == "string_operators":
        string_operators.run()
    elif response == "user_input":
        user_input.run()
    elif response == "guess_the_number":
        guess_the_number.run()
    elif response == "nestception":
        nestception.run()
    elif response == "nested":
        nested.run()
    elif response == "ascii_art":
        ascii_art.run()
    elif response == "escape_characters":
        escape_characters.run()
    elif response == "simple_message":
        simple_message.run()
    elif response == "multiline_message":
        multiline_message.run()
    elif response == "comparison_operators":
        comparison_operators.run()
    elif response == "counter":
        counter.run()
    elif response == "if_":
        if_.run()
    elif response == "if_elif_else":
        if_elif_else.run()
    elif response == "if_else":
        if_else.run()
    elif response == "modulo_operator":
        modulo_operator.run()
    elif response == "simple":
        simple.run()
    elif response == "range":
        range.run()
    elif response == "characters":
        characters.run()
    elif response == "reverse":
        reverse.run()
    elif response == "count_down":
        count_down.run()
    elif response == "loop_nested":
        loop_nested.run()
    if response == "nesting":
        nesting.run()
    elif response == "len":
        len.run()
    elif response == "while_simple":
        while_simple.run()
    elif response == "while_ascii":
        while_ascii.run()
    elif response == "while_count":
        while_count.run()
    elif response == "while_factorial":
        while_factorial.run()
    elif response == "while_sum_100":
        while_sum_100.run()
    elif response == "while_sum_user_numbers":
        while_sum_user_numbers.run()
    else:
        print()

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