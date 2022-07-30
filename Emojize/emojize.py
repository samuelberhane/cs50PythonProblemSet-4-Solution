import emoji
input_string = input('Input: ')
if " " in input_string:
    input_string = input_string.split(' ')
    final_string = ''
    for i in range(len(input_string)):
        if ':' in input_string[i] and '_' in input_string[i]:
            output = emoji.emojize(input_string[i])
            final_string += input_string[i-1] + " " + output
        elif ':' in input_string[i]:
            output = emoji.emojize(input_string[i],language = 'alias')
            final_string += input_string[i-1] + " " + output
else:
    if "_" in input_string:
        final_string = emoji.emojize(input_string)
    else:
        final_string = emoji.emojize(input_string,language = 'alias')


print('Output:',final_string)
