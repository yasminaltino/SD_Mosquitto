import json
from application.controllers.speak_controller import SpeakController
from application.controllers.system_controller import SystemController
from application.controllers.reader_controller import ReaderController
TOPIC = "/notebook"


def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print(f"Cliente conectado com sucesso: {client}")
        client.subscribe(TOPIC + "/system/volume")
        client.subscribe(TOPIC + "/talk")
        client.subscribe(TOPIC + "/system/block")
        client.subscribe(TOPIC + "/system/battery")
        client.subscribe(TOPIC + "/system/calculator")
        client.subscribe(TOPIC + "/reader/barcode")



        
    else:
        print(f'Erro ao me conectar! codigo={rc}')
        
        
        
def on_subscribe(client, userdata, mid, granted_qos, properties=None):
    print(f'Cliente Subscribed at {TOPIC}')
    print(f'QOS:{granted_qos}')
    
    
def on_message(client, userdata, message, properties=None):
    print('Mensagem recebida!')
    topic = message.topic
    payload = message.payload.decode()
    
    if topic == "/notebook/system/volume":
        try:
            volume = int(payload)
            SystemController.set_volume(volume)
        except ValueError:
            print(f'Payload inválido: {payload}')
            
    if topic == "/notebook/talk":
        try:
            sentence = str(payload)
            SpeakController.talk(sentence)
        except ValueError:
            print(f'Payload inválido: {payload}')
    
    if topic == "/notebook/system/block":
        SystemController.block_screen()
        
    if topic == "/notebook/system/battery":
        SystemController.get_battery()
        
    if topic == "/notebook/system/calculator":
        SystemController.open_calculator()
        
    # if topic == "/notebook/system/interacao":
    #     try:
    #         command = json.loads(payload)
    #         SystemController.autogui(command=command)
    #     except Exception as e:
    #         print(f'Error: {e}')

    if topic == "/notebook/reader/barcode":
        barcode = str(payload)
        ReaderController.process_barcode(barcode)
            
        
        

            
            
            