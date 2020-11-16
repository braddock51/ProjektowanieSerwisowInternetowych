from file_manager import FileManager

# zadanie 1

def function_1(a_list, b_list):
    array = []
    length = 0
    
    if len(a_list) > len(b_list):
        length = len(a_list)
    else:
        length = len(b_list)
    
    for i in range(length):
        if i % 2 == 0:
            array.append(a_list[i])
        else:
            array.append(b_list[i])
    
    return array
    
print(function_1([0,2,4],[1,3,5]))

# zadanie 2

def function_2(data_text):
    return {'length': len(data_text), 'letters': list(data_text), 'big_letters': data_text.upper(), 'small_letters': data_text.lower()}

print(function_2('Dog'))

# zadanie 3

def function_3(text, letter):
    new_text = list(text)
    length = len(new_text)
    print(f"length = {length}\nnew_text = {len(new_text)}")
    for i in range(length):
        if new_text[i] == letter:
            new_text[i] = ''
    return ''.join(new_text)

text = function_3('Be or not to be', 'e')
print(text)
    
# zadanie 4

class IncorrectValueError(Exception):
    def __init__(self, value):
        message = f"Got a bad value: {value}"
        super().__init__(message)

def function_4(temperature_data ,temperature_type):
    if temperature_type != 'Fahrenheit' and temperature_type != 'Rankine' and temperature_type != 'Kelvin':
        raise IncorrectValueError(temperature_type)

    if temperature_type == 'Fahrenheit':
        
        return temperature_data * 1.8 + 32
    
    elif temperature_type == 'Rankine':
        
        return (temperature_data + 273.15) * (9 / 5)
    
    elif temperature_type == 'Kelvin':

        return temperature_data + 273.15

print(function_4(20, 'Fahrenheit'))
print(function_4(20, 'Rankine'))
print(function_4(20, 'Kelvin'))

# zadanie 5

class Calculator:

    @staticmethod
    def add(x, y):
        return x + y
    
    @staticmethod
    def difference(x, y):
        return x - y
    
    @staticmethod
    def multiply(x, y):
        return x * y
    
    @staticmethod
    def divide(x, y):
        return x/ y

print(Calculator.add(5, 4))

# zadanie 6

class ScienceCalculator(Calculator):

    @staticmethod
    def power(x, pow):
        return x ** pow

print(ScienceCalculator.power(2, 2))

# zadanie 7

def function_5(string):
    array_string = list(string)
    counter = 0
    for i in range(len(string)-1, -1, -1):
        array_string[counter] = string[i]
        counter += 1
    
    return "".join(array_string)

print(function_5('koteł'))

# zadanie 9

data = FileManager('02 Wprowadzenie do Python/some_text.txt')

data.update_file('\nAdded update in the end of the file')
print(data.read_file())




