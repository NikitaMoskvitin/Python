def new_zveno(value):

    '''Создаем новое звено'''
    return {'value': value, 'next': None}

def sozd_spiska(head):

    '''Создание списка'''

    n = int(input())
    for i in range(n):
        value = int(input())
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

head = None
k = int(input())
head = sozd_spiska(head)
for i in range(k-1):
    udol_lastzv(head)
current = head
while current['next'] != None:
    current = current['next']
print(current['value'])