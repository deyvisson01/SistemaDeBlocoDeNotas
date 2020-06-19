import glob
import os
import socket
import json
import threading
import numpy as np
import sys
from os import rmdir

#mapaArquivos=dict()

def arquivoss(pasta):
    caminhos = [os.path.join(pasta, nome) for nome in os.listdir(pasta)]
    arquivos = [arq for arq in caminhos if os.path.isfile(arq)]
    
    return arquivos
    pass

def caminhos(pasta): 
    mapaArquivos=dict()
    arrayfiles = None
    arrayfiles = list()
    url = str(pasta)
    
    a = [os.path.join(pasta, nome) for nome in os.listdir(pasta)]
    b = str()
    c = str()
    for val in a:
        b = val
        c = b.split(url)[1]
        
        d = arquivoss(str(pasta+c))
        
        if np.size(d) > 0:
            
            for val2 in d:
                arrayfiles.append(str(val2).split(pasta+c+"/")[1])
        mapaArquivos[c]=arrayfiles
        arrayfiles=list()
    return mapaArquivos
        #arrayfiles.clear()
        # print("ARRAY DEPOIS DO CLEAR: "+str(arrayfiles))
        
    pass

def listFiles(mapaArquivos):
    teste = ""
    i = 0
    j = 0
    for (key,value) in mapaArquivos.items():
        #teste += "|"
        j = 0
        i = i+1
        print(key)
        teste += str(key+"<>")
        if np.size(value) > 0:
            for arquivo in value:
                print(arquivo)
                j = j+1
                teste += str(arquivo+",")
        else:
            print(value)
            teste += str("vazio,")
        teste += str("-")
        
        print(mapaArquivos)
        print("COM O CLEAR: ")
        #mapaArquivos.clear()
        #mapaArquivos = dict()
        #print(mapaArquivos)
        teste += str(j)

    print(i)
    teste += str("#")
    teste += str(i) 
    print(teste)
    return teste
    
    pass

def StrToJson(msg):
    return json.loads(msg)

def SetMSG(msg):
    msgjson = StrToJson(msg)
    msgRequest = Message()

    msgRequest.setMessage(JSON_MSG=msgjson)

    return (msgRequest)

    pass


class SocketServer:
    def __init__(self, serverPort=2000, serverHost="127.0.0.1"):
        self.PortServer = serverPort
        self.HostServer = serverHost
        self.socket = socket.socket()
        self.socket.bind((self.HostServer,self.PortServer))
        self.socket.listen(5)
    pass

    def read(self, conn):
        length_of_message = int.from_bytes(conn.recv(2), byteorder='big')
        msg = conn.recv(length_of_message).decode("UTF-8")
        return msg

    def send(self, msg, conn):
        conn.send(len(str(msg).encode("UTF-8")).to_bytes(2, byteorder='big'))
        conn.send(str(msg).encode("UTF-8"))


class Message:
    def __init__(self):
        self.MessageType = None
        self.requestId = None
        self.MethodReference = None
        self.MethodId = None
        self.arguments = None
        pass

    def setMessage(self, JSON_MSG):
        self.MessageType = JSON_MSG["MessageType"]
        self.requestId = JSON_MSG["requestId"]
        self.MethodReference = JSON_MSG["MethodReference"]
        self.MethodId = JSON_MSG["MethodId"]
        self.arguments = JSON_MSG["arguments"]
        pass

    def ConvertObjectMessageToJSON(self):

        return json.dumps({"MessageType": self.MessageType, "requestId": self.requestId,
                           "MethodReference": self.MethodReference, "MethodId": self.MethodId,
                           "arguments": self.arguments})


def MountReturnMsg(op, arg):

    try:
        if op.MethodId == 0:
            op.MessageType = 1
            op.arguments = arg
            pass

        if op.MethodId == 1:
            op.MessageType = 1
            op.arguments = arg
            pass

        if op.MethodId == 2:
            op.MessageType = 1
            op.arguments = arg
            pass

        if op.MethodId == 3:
            op.MessageType = 1
            op.arguments = arg
            pass

        if op.MethodId == 4:
            op.MessageType = 1
            op.arguments = arg
            pass

        if op.MethodId == 5:
            op.MessageType = 1
            op.arguments = arg
            pass

        if op.MethodId == 6:
            op.MessageType = 1
            op.arguments = arg
            pass

        if op.MethodId == 7:
            op.MessageType = 1
            op.arguments = arg
            pass

        if op.MethodId == 8:
            op.MessageType = 1
            op.arguments = arg
            pass
        
        if op.MethodId == 9:
            op.MessageType = 1
            op.arguments = arg
            
            pass

    except KeyError:
        print("Error 404")

    pass

    return op.ConvertObjectMessageToJSON()

    pass

def SAIR(op, args, conn, sc):
    mapaArquivos = dict()
    print(mapaArquivos)
    arg = "SAIR"
    
    sc.send(str(MountReturnMsg(op, arg)), conn=conn)
    pass

def LOGIN(op, args, conn, sc):
    mapaArquivos = dict()
    print(mapaArquivos)
    newargs = args.split('-')

    username = newargs[0]
    password = newargs[1]

    if not os.path.exists(username):
        arg = "FALHA"

    else:
        print("# # # # CHECANDO DADOS DO USUÁRIO! # # # # ")
        print(username+"\n")

        url = str("Login") + str("/") + str(username)
        file = open(url, "r")
        linha = file.read()
        print(linha)

        dados = linha.split('-')

        if dados[0] == username and dados[1] == password:
            arg = "LOGIN"
        else:
            arg = "FALHA"

        file.close()

        sc.send(str(MountReturnMsg(op, arg)), conn=conn)

    pass


def CADASTRO(op, args, conn, sc):

    newargs = args.split('-')

    username = newargs[0]
    password = newargs[1]

    if not os.path.exists(username):
        os.mkdir(username)
        print("# # # # Diretório criado! # # # # \n")
        print(username)

        url = str("Login")+str("/")+str(username)
        file = open(url, "w")

        dados = str(username)+str("-")+str(password)
        file.write(dados)

        file.close()
        
        os.mkdir(username+"/Default")
        print("# # # # Pasta default criada! # # # # \n")
        print(username+"/Default")

        url = str(username)+str("/")+str("Default/Welcome")
        file = open(url, "w")

        dados = str("Bem vindo ao Bloco de notas!")
        file.write(dados)

        file.close()
        
        arg = "CONCLUIDO"

    else:
        arg = "ERRO1"

    sc.send(str(MountReturnMsg(op, arg)), conn=conn)


def CRIARPASTA(op, args, conn, sc):

    newargs = args.split('-')

    username = newargs[0]
    namepasta = newargs[1]
    url = str(username)+str("/")+str(namepasta)
    if not os.path.exists(url):
        os.mkdir(url)
        print("# # # # Diretório criado! # # # #\n")
        print(url)
        arg = "CONCLUIDO"

        sc.send(str(MountReturnMsg(op, arg)), conn=conn)

    pass


def CRIARNOTA(op, args, conn, sc):
    newargs = args.split('-')

    username = newargs[0]
    namepasta = newargs[1]
    namenota = newargs[2]
    conteudo = newargs[3]
    url = str(username) + str("/") + str(namepasta)

    if not os.path.exists(url):
        print("# # # # Diretório não existe! # # # #\n")
        print(url)
        arg = "FALHA"
    else:
        newurl = str(username) + str("/") + str(namepasta) + str("/") + str(namenota)
        file = open(newurl, "w")
        dados = str(conteudo)
        file.write(dados)

        file.close()
        arg = "CONCLUIDO"

        sc.send(str(MountReturnMsg(op, arg)), conn=conn)

    pass


def LERNOTA(op, args, conn, sc):

    newargs = args.split('-')

    username = newargs[0]
    namepasta = newargs[1]
    namenota = newargs[2]

    url = str(username) + str("/") + str(namepasta)
    print(url)
    newurl = str(username) + str("/") + str(namepasta) + str("/") + str(namenota)
    print(newurl)
    if not os.path.exists(newurl):
        print("# # # # Diretório não existe! # # # #\n")
        print(newurl)
        arg = "FALHA"
        print(arg)

    else:
        newurl = str(username) + str("/") + str(namepasta) + str("/") + str(namenota)
        file = open(newurl, "r")
        arg = file.read()
        print(arg)
        file.close()

    sc.send(str(MountReturnMsg(op, arg)), conn=conn)

    pass


def DELETANOTA(op, args, conn, sc):

    newargs = args.split('-')
    #      USUÁRIO
    username = newargs[0]

    #     URLS
    namepasta = newargs[1]
    namenota = newargs[2]
    newurl = str(username) + str("/") + str(namepasta)
    if not os.path.exists(newurl):
        arg = "ERRO1"
    else:
        newurl = str(username) + str("/") + str(namepasta) + str("/") + str(namenota)
        if not os.path.exists(newurl):
            arg = "ERRO2"
        else:
            os.remove(newurl)
            arg = "CONCLUIDO"

    sc.send(str(MountReturnMsg(op, arg)), conn=conn)
    pass


def DELETAPASTA(op, args, conn, sc):

    newargs = args.split('-')
    #      USUÁRIO
    username = newargs[0]

    #     URLS
    namepasta = newargs[1]
    newurl = str(username) + str("/") + str(namepasta)
    if not os.path.exists(newurl):
        arg = "ERRO1"
    else:
        rmdir(newurl)
        arg = "CONCLUIDO"

    sc.send(str(MountReturnMsg(op, arg)), conn=conn)

    pass


def EDITANOTA(op, args, conn, sc):

    newargs = args.split('-')
#      USUÁRIO
    username = newargs[0]

#     URLS ANTIGOS
    oldnamepasta = newargs[1]
    oldnamenota = newargs[2]

#     URLS NOVOS
    newnamepasta = newargs[3]
    newnamenota = newargs[4]

    conteudo = newargs[5]

    if newnamepasta == oldnamepasta:
        if newnamenota == oldnamenota:
            newurl = str(username) + str("/") + str(newnamepasta) + str("/") + str(newnamenota)
            print("PASTA IGUAL ARQUIVO IGUAL")
            file = open(newurl, "w")
            dados = str(conteudo)
            file.write(dados)

            file.close()
            arg = "CONCLUIDO"
        else:
            newurl = str(username) + str("/") + str(newnamepasta) + str("/") + str(newnamenota)
            if not os.path.exists(newurl):
                file = open(newurl, "w")
                dados = str(conteudo)
                file.write(dados)

                file.close()
                arg = "CONCLUIDO"

                oldurl = str(username) + str("/") + str(oldnamepasta) + str("/") + str(oldnamenota)
                os.remove(oldurl)
            else:
                arg = "ERRO2"

    else:
        newurl = str(username) + str("/") + str(newnamepasta)
        if not os.path.exists(newurl):
            arg = "ERRO1"
        else:
            newurl = str(username) + str("/") + str(newnamepasta) + str("/") + str(newnamenota)
            if not os.path.exists(newurl):
                file = open(newurl, "w")
                dados = str(conteudo)
                file.write(dados)

                file.close()
                arg = "CONCLUIDO"

                oldurl = str(username) + str("/") + str(oldnamepasta) + str("/") + str(oldnamenota)
                os.remove(oldurl)
            else:
                arg = "ERRO2"

    sc.send(str(MountReturnMsg(op, arg)), conn=conn)
pass


def LIST_PASTA(op, args, conn, sc):
    
    arg = listFiles(caminhos(args))
    
    sc.send(str(MountReturnMsg(op, arg)), conn=conn)


def selectFunc(op, args, conn, sc):

    try:
        if op.MethodId == 0:
            LOGIN(op, args, conn, sc)
            pass
        if op.MethodId == 1:
            CADASTRO(op, args, conn, sc)
            pass
        if op.MethodId == 2:
            CRIARNOTA(op, args, conn, sc)
            pass
        if op.MethodId == 3:
            CRIARPASTA(op, args, conn, sc)
            pass
        if op.MethodId == 4:
            LERNOTA(op, args, conn, sc)
            pass
        if op.MethodId == 5:
            DELETANOTA(op, args, conn, sc)
            pass
        if op.MethodId == 6:
            EDITANOTA(op, args, conn, sc)
            pass
        if op.MethodId == 7:
            LIST_PASTA(op, args, conn, sc)
            pass
        if op.MethodId == 8:
            DELETAPASTA(op, args, conn, sc)
            pass
        if op.MethodId == 9:
            SAIR(op, args, conn, sc)
            pass

    except KeyError:
        print("Error 404")
    pass


def waitRequest():

    sc = SocketServer(serverPort=2009, serverHost="127.0.0.1")
    print("# # # # # # # SERVIDOR BLOCO DE NOTAS ONLINE # # # # # # #")

    while True:
        (conn, addr) = sc.socket.accept()
        print("\n SOLICITAÇÃO DO CLIENTE RECEBIDA!")
        print("Client: ", addr)
        msg = sc.read(conn=conn)

        op = SetMSG(msg)

        decodeJSON = json.loads(msg)

        newMT = decodeJSON["MessageType"]
        newRID = decodeJSON["requestId"]
        newMREF = decodeJSON["MethodReference"]
        newMID = decodeJSON["MethodId"]
        newARG = decodeJSON["arguments"]

        print("REFERENCIA: ", op.MethodReference)

        print("SOLICITAÇÃO: ")
        print(newMT, newRID, newMREF, newMID, newARG)

        selectFunc(op, newARG, conn, sc)

        print("# # # # FIM DA SOLICITAÇÃO # # # #\n")
        conn.close()

    pass


thr = threading.Thread(target=waitRequest())
thr.start()
