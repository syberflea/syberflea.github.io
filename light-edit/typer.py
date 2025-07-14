def check_typing_task(task, log):
    virtual_string = ''
    cursor_position = 0

    for key in log:
        if key == 'delete':
            if cursor_position < len(virtual_string):
                virtual_string = virtual_string[:cursor_position] + virtual_string[cursor_position+1:]
        elif key == 'bspace':
            if cursor_position > 0:
                virtual_string = virtual_string[:cursor_position-1] + virtual_string[cursor_position:]
                cursor_position -= 1
        elif key == 'left':
            if cursor_position > 0:
                cursor_position -= 1
        elif key == 'right':
            if cursor_position < len(virtual_string):
                cursor_position += 1
        elif key == '':
            continue
        else:
            virtual_string = virtual_string[:cursor_position] + key + virtual_string[cursor_position:]
            cursor_position += len(key)

    return virtual_string == task

a = input()
b = input().split('<')
c = [predicat.split('>') for predicat in b]
flat_list = sum(c, [])

if check_typing_task(a, flat_list):
    print('Yes')
else:
    print('No')