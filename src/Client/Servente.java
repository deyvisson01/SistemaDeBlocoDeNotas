
package Client;

import Client.Message;

public class Servente {
    public static int IPVAR = 1500;
    public static int countIDMsg = 0;
    
    public Message doOperation(Message msgToSend){
        System.out.println("MENSAGEM ENVIADA: ");
        System.out.println(msgToSend.toString());
        Message return_msg = new Message(-1,-1,null,-1,null);
        
        SocketC socketClient = new SocketC("127.0.0.1",2009,IPVAR);
        socketClient.send(msgToSend.getJSONMessage(msgToSend).toString());
        
        return_msg = return_msg.convertStrJSONToMessage(socketClient.request());
        System.out.println("MENSAGEM RECEBIDA: ");
        System.out.println(return_msg.toString());
        if((msgToSend.getRequestId()==return_msg.getRequestId())){
            System.out.println("SOLICITAÇÂO CORRETA! ID DA SOLICITAÇÂO: "+msgToSend.getRequestId());
        }else{
           System.out.println("SOLICITAÇÂO INCORRETA!ID ESPERADO: "+msgToSend.getRequestId());
        }
        socketClient.closeAll();
        IPVAR++;
        return return_msg;
    }
}
