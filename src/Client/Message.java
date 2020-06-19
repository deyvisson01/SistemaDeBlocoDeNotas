package Client;

import org.json.*;

public class Message {
    private int MessageType;
    private int requestId;
    private String MethodReference;
    private int MethodId;
    private String arguments;
    
    public Message(int messageType, int requestId, String methodReference, int methodId, String arguments) {
        this.MessageType = messageType;
        this.requestId = requestId;
        this.MethodReference = methodReference;
        this.MethodId = methodId;
        this.arguments = arguments;
    }
    
    public int getMessageType() {
        return MessageType;
    }
    public void setMessageType(int messageType) {
        MessageType = messageType;
    }
    public int getRequestId() {
        return requestId;
    }
    public void setRequestId(int requestId) {
        this.requestId = requestId;
    }
    public String getMethodReference() {
        return MethodReference;
    }
    public void setMethodReference(String methodReference) {
        MethodReference = methodReference;
    }
    public int getMethodId() {
        return MethodId;
    }
    public void setMethodId(int methodId) {
        MethodId = methodId;
    }
    public String getArguments() {
        return arguments;
    }
    public void setArguments(String arguments) {
        this.arguments = arguments;
    }

    public JSONObject getJSONMessage(Message msg){
        JSONObject jasonMSG = new JSONObject();
        try {
            jasonMSG.put("MessageType",msg.getMessageType());
            jasonMSG.put("requestId",msg.getRequestId());
            jasonMSG.put("MethodReference",msg.getMethodReference());
            jasonMSG.put("MethodId",msg.getMethodId());
            jasonMSG.put("arguments",msg.getArguments());
        }catch (Exception e){

        }
        return jasonMSG;
    }

    public Message convertStrJSONToMessage(String JSONSTRMessage){
        Message msg = null;
        try {
            JSONObject jsonOBJ = new JSONObject(JSONSTRMessage);
            msg = new Message(jsonOBJ.getInt("MessageType"),
                            jsonOBJ.getInt("requestId"),
                            jsonOBJ.getString("MethodReference"),
                            jsonOBJ.getInt("MethodId"),
                            jsonOBJ.getString("arguments"));
            
        } catch (JSONException e) {
            e.printStackTrace();
        }
        return msg;
    }
    
    public Message convertStrJSONToTree(String JSONSTRMessage){
        Message msg = null;
        try {
            JSONObject jsonOBJ = new JSONObject(JSONSTRMessage);
            msg = new Message(jsonOBJ.getInt("MessageType"),
                            jsonOBJ.getInt("requestId"),
                            jsonOBJ.getString("MethodReference"),
                            jsonOBJ.getInt("MethodId"),
                            jsonOBJ.getString("arguments"));
            
        } catch (JSONException e) {
            e.printStackTrace();
        }
        return msg;
    }

    @Override
    public String toString() {
        return "Message{" +
                "MessageType=" + MessageType +
                ", requestId=" + requestId +
                ", MethodReference='" + MethodReference + 
                ", MethodId=" + MethodId +
                ", arguments=" + arguments +
                '}';
    }
}
