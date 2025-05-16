def print_it(function):

    def wrapper(*args, **kwargs):

        # print out the positional arguments and the keyword arguments
        print(f'Positional arguments : {args}')
        print(f'Keyword arguments : {kwargs}')

        # run the function itself and capture the return value
        result = function(*args, **kwargs)

        # print out the result
        print(f'Result : {result}')

        # return the result
        return result
    return wrapper


@print_it
def get_modulus(arg1, arg2):

    return arg1 % arg2


answer = get_modulus(10, arg2=3)

print(answer)
