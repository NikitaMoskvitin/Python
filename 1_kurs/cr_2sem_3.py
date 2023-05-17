def new_zveno(value):

    '''Создаем новое звено'''
    return {'value': value, 'next': None}

def sozd_spiska():

    '''Создание списка'''

    head = None
    for i in range(len(a)):
        value = a[i]
        current = new_zveno(value)
        if head == None:
            head = current
        else:
            prev['next'] = current
        prev = current
    return head
def udol_lastzv(head):

    '''Удаление последнего элемента'''

    perv1 = head
    current = head['next']
    while current != None:
        prev2 = perv1
        perv1 = current
        current = current['next']
    prev2['next'] = None

def udol_1zv(head):

    '''Удаление первого элемента'''

    prev = head
    current = prev['next']
    head = current
    return head

a = input().split()
head = sozd_spiska()
dlina = 0
current = head
while current != None:
    current = current['next']
    dlina = dlina + 1
k = 0
for i in range(dlina//2):
    current = head
    nach = current['value']
    while current['next'] != None:
        current = current['next']
    conec = current['value']
    if conec == nach:
        udol_lastzv(head)
        head = udol_1zv(head)
    else:
        k = 1
        break
if k == 0:
    print("Yes")
else:
    print("No")
