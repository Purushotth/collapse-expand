import sys, re
input_list = filter(lambda x:x!=' \r\n', list(sys.stdin))
output_list = []
cnt = 0
last_value = ''
previous_star_count = 0
for id in range(len(input_list)):
     star_match = re.match('(\*+)[^\**](.*)', input_list[id])
     dot_match = re.match('(\.+)[^\.*](.*)', input_list[id])
     if star_match:
        star_count = len(star_match.group(1))
        if star_count == 1:
            cnt += 1
            last_value = str(cnt) + ' ' + star_match.group(2)
        else:
            if '.' not in last_value:
                last_value = str(last_value.split()[0]) + '.1' + ' ' + star_match.group(2)
            else:
                if star_count>previous_star_count:
                    last_value = str(last_value).split()[0] + '.1' + ' ' + star_match.group(2)
                elif star_count < previous_star_count:
                    difference = previous_star_count-star_count
                    splited_list = last_value.split('.')
                    last_value = '.'.join(splited_list[0:difference-1])+'.'+str(int(splited_list[:difference][-1])+1) + ' ' + star_match.group(2)
        output_list.append(last_value)
        previous_star_count = star_count
     elif dot_match:
        dot_count = len(dot_match.group(1))
        if id != len(input_list)-1:
            next_dot_match = re.match('(\.+)[^\.*](.*)', input_list[id+1])
            if next_dot_match:
                next_dot_count = len(next_dot_match.group(1))
                if next_dot_count>dot_count:
                    output_list.append('  + ' + dot_match.group(2))
                else:
                    output_list.append('  - ' + dot_match.group(2))
            else:
                if id != len(input_list)-1:
                    next_star_match = re.match('(\*+)[^\**](.*)', input_list[id+1])
                    if not next_star_match:
                        output_list.append('  + ' + dot_match.group(2))
                    else:
                        output_list.append('  - ' + dot_match.group(2))
                else:
                    output_list.append('  - ' + dot_match.group(2))
        else:
            output_list.append('  - ' + dot_match.group(2))
     else:
        next_dot_count = 0
        output_list.append('     ' +input_list[id].strip('\r\n'))
print '\n'.join(output_list)