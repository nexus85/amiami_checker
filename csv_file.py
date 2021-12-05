

def write_check(data):
    with open('data.csv', 'a', encoding='UTF-8') as f:
        f.write(data)


def read_check():
    f = open('data.csv', 'r', encoding='UTF-8')
    last_line = f.readlines()[-1]
    try:
        s = last_line.split(';')[-1].strip()
        if s == 'True':
            STATUS = True
        else:
            STATUS = False
    except:
            STATUS = False
    finally:
        f.close()
    return STATUS


def count_check(n):
    f = open('data.csv', 'r', encoding='UTF-8')
    count = len(f.readlines())
    f.seek(0)
    try:
        line = f.readlines()[-1]
    except:
        line = '2021.11.11;10.10.10;False\n'



    # print(line)
    if count >= n:
        k = open('data.csv', 'w', encoding='UTF-8')
        k.write(line)
        k.close()
    f.close()





if __name__ == '__main__':
    count_check(5)