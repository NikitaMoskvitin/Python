def new_zveno(value):

    '''Создаем новое звено'''
    return {'value': value, 'next': None}

def sozd_spiska():

    '''Создание списка'''

    head = None
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

def pechat(head):

    '''Печать списка'''

    current = head
    while current != None:
        print(current['value'])
        current = current['next']

def sort_pol(head):
    current = head
    i = 0
    while current != None:
        current = current['next']
        i = i + 1

    c1 = head
    for j in range(i-1):
        m = c1['value']
        prev = c1
        current = c1['next']
        k = 0
        while current !=  None:
            if current['value'] < m:
                m = current['value']
                m_sled = current['next']
                m_prev = prev
                k = 1
            prev = current
            current = current['next']
        if k == 0:
            c0 = c1
            c1 = c1['next']
            continue
        if c1['value'] == m_prev['value']:
            c3 = c1['next']
            c1['value'], c3 ['value'] = c3['value'], c1 ['value']
            c0 = c1
            c1 = c3
            continue
        next_c1 = c1['next']
        if c1 == head:
            c1['next'] = m_sled
            head = new_zveno(m)
            head['next'] = next_c1
            m_prev['next'] = c1
            c0 = head
        else:
            c1['next'] = m_sled
            M = new_zveno(m)
            M['next'] = next_c1
            m_prev['next'] = c1
            c0['next'] = M
            c0 = M
        c1 = c0['next']
    return head

def sort_otr(head):
    current = head
    i = 0
    while current != None:
        current = current['next']
        i = i + 1

    c1 = head
    for j in range(i-1):
        if c1['value'] <= 0:
            c0 = c1
            c1 = c1['next']
            continue
        else:
            m = c1['value']
        prev = c1
        current = c1['next']
        k = 0
        while current !=  None:
            if current['value'] < m and current['value'] > 0:
                m = current['value']
                m_sled = current['next']
                m_prev = prev
                k = 1
            prev = current
            current = current['next']
        if k == 0:
            c0 = c1
            c1 = c1['next']
            continue
        if c1['value'] == m_prev['value']:
            c3 = c1['next']
            c1['value'], c3 ['value'] = c3['value'], c1 ['value']
            c0 = c1
            c1 = c3
            continue
        next_c1 = c1['next']
        if c1 == head:
            c1['next'] = m_sled
            head = new_zveno(m)
            head['next'] = next_c1
            m_prev['next'] = c1
            c0 = head
        else:
            c1['next'] = m_sled
            M = new_zveno(m)
            M['next'] = next_c1
            m_prev['next'] = c1
            c0['next'] = M
            c0 = M
        c1 = c0['next']
    return head

head = sozd_spiska()
head = sort_pol(head)
pechat(head)

head = sozd_spiska()
head = sort_otr(head)
pechat(head)