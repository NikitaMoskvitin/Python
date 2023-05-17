def new_zveno(value):

    '''Создаем новое звено'''
    return {'value': value, 'next': None}

def sozd_spiska(head):

    '''Создание списка'''

    for i in range(len(a)):
        value = a[i]
        current = new_zveno(value)
        if head == None:
            head = current
        else:
            prev['next'] = current
        prev = current
    return head

def pechat(head):

    '''Печать списка'''

    current = head
    while current != None:
        print(current['value'], end = " ")
        current = current['next']

head = None
a = input().split()
head = sozd_spiska(head)
b = input().split()
current = head
while current['value'] != b[0]:
    prev = current
    current = current['next']
    if current == None:
        break
if current != None:
    current['value'] = b[1]
pechat(head)

