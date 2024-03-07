import socket

"""Documentation rough class to deepen your knowledge in this powerful language!"""

'''comment'''


def printer():
    # to make comments use this
    print("brunno", "teste")
    print("brunno", "stephanie", sep="-", end="##")
    '''Print of CPF rough'''
    print("123", "176", "070", sep=".", end="-")
    print(10)
    iprinter()

def iprinter():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    print(f"Hostname: {hostname}")
    print(f"IP Address: {ip_address}")

printer()