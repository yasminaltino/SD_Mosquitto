import os
import subprocess
import psutil
# import pyautogui
import json


class SystemController:
    def block_screen():
        os.system("gnome-screensaver-command -l")
        
    def set_volume(level: int):
        subprocess.run(["amixer", "sset", "Master", f"{level}%"])
        
    def get_battery():
        battery = psutil.sensors_battery()
        if battery:
            percent = battery.percent
            charging = "Sim" if battery.power_plugged else "Não"
            message = f"Bateria: {percent}%\nCarregando: {charging}"
        else:
            message = "Informação da bateria não disponível."

        # Send a notification
        subprocess.run(["notify-send", "-u", "critical", "-t", "5000", "Estado da Bateria", message])

    def open_calculator():
        subprocess.Popen(["galculator"])
        
    # def autogui(command):
    #     print(command)
    #     try:
    #         action = command.get("acao")
            
    #         if action == "mover_mouse":
    #             x = int(command.get("x", 0))
    #             y = int(command.get("y", 0))
    #             pyautogui.moveTo(x=y,y=y)
                
    #         elif action == "clicar":
    #             button = command.get("botão")
    #             if button is None:
    #                 print("Campo 'botão' faltando na mensagem!")
    #             else:
    #                 pyautogui.click(button=button)
    #         else:
    #             print(f"Ação desconhecida ou vazia: {action} - nenhuma operação executada.")
                    
    #     except Exception as e:
    #         print(f"Erro no comando: {e}")        
        
        
