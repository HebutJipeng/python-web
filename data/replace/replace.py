with open('./simple.test.entitystar', 'r', encoding='utf-8') as f:
    with open('./output.test', 'w', encoding='utf-8') as ff:
        lines = f.readlines()
        lastline = ''
        for line in lines:
            if '\'s' in line:
                print('hahah \'s =>', line)
                part = line.split('\'s')[1]
                if 'I' in part:
                    print('I in')
                    lineI = line.replace('\'s', '')
                    ff.write(lineI)
                    ff.write('\'s I\n')
                elif 'B' in part:
                    print('B in')
                    lineB = line.replace('\'s', '')
                    ff.write(lineB)
                    ff.write('\'s I\n')
                elif 'O' in part:
                    print('O in', lastline)
                    if lastline != '\n' and lastline.split(' ')[1] != '0':
                        lineC = line.replace('\'s O', ' I')
                    else:
                        lineC = line.replace('\'s', '')
                    ff.write(lineC)
                    ff.write('\'s O\n')
            else:
                print('no \'s =>', line)
                ff.write(line)
            lastline = line
        
