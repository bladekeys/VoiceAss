import socket
import client
import task_card
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('192.168.1.76', 65535))
clients = []
cards = []

def del_card(card):
    i = 0
    for crd in cards:
        flag = task_card.compare_cards(crd,card)
        if flag == 0 or flag == 1:
            del cards[i]
        i+=1


def is_card_in_cards(card):
    for crd in cards:
        flag = task_card.compare_cards(crd, card)
        if flag == 0:
            return 0
        elif flag == 1:
            return 1
    return 2


def get_client_addres(nikname):
    for clt in clients:
        if clt.is_in_group(nikname):
            return clt.addres
    return None


def is_new_client(addres):
    for client1 in clients:
        if client1.addres[0] == addres[0] and client1.addres[1] == addres[1]:
            return False
    return True

print ('Start Server')
while True:
    data, addres = sock.recvfrom(1024)
    content = data.decode('utf-8')
    for clt in clients:
        sock.sendto("success".encode('utf-8'), clt.addres)
    #Авторизация на сервере
    if content.startswith('autorize'):
        if is_new_client(addres):
            cl_new = client.Client()
            cl_new.set_client(content[9:].split(','), addres)
            clients.append(cl_new)
            print("Client \""+cl_new.group[len(cl_new.group)-1]+"\" autorized succesfull!", addres)
            sock.sendto("success".encode('utf-8'), addres)
    #Перенаправление задач
    if content.startswith('card'):
        content = content[5:]
        list_content = content.split(',')
        nikname = list_content[0]
        del list_content[0]
        content = ''.join(list_content)
        tc = task_card.convert_string_to_card(content)
        flag = is_card_in_cards(tc)
        if flag == 2:
            cards.append(tc)
            nik = tc.group
            addres = get_client_addres(nik)
            if addres:
                sock.sendto(tc.convert_to_string().encode('utf-8'), addres)
                print('Send message to ', addres, ' data = \"', tc.convert_to_string()[:10], '...\"')
            else:
                print('Failed to send data to '+nik)
        elif flag == 1:
            nik = tc.author
            addres = get_client_addres(nik)
            if addres:
                sock.sendto(tc.convert_to_string().encode('utf-8'), addres)
                print('Send message to ', addres, ' data = \"', tc.convert_to_string()[:10], '...\"')
                if tc.status == 'ready':
                    del_card(tc)
            else:
                print('Failed to send data to ' + nik)






