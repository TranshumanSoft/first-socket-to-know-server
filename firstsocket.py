import socket
mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.connect(('twitter.com', 80))
cmd = 'GET http://twitter.com/TranshumanSoft HTTP/1.0\n\n'.encode()
mysocket.send(cmd)
while True:
    data = mysocket.recv(4096)
    if (len(data) < 1):
        break
    info = data.decode()
    for line in info.split("\n"):
        line = line.lower()
        if line.startswith("server:"):
            print(f"You have the {line}.")
mysocket.close()
#We have here the name of the server with this socket exercise
#cmd = 'GET / HTTP/1.0\n\n'.encode() --> If you only use "/", you take the HTML code, also if you put /index.html