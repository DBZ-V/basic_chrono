import time
import os
import keyboard
from datetime import datetime

def read_previous_time(file_path):
    if not os.path.exists(file_path):
        return 0
    try:
        with open(file_path, "r") as f:
            content = f.read().strip()
            hours, minutes, seconds = map(int, content.split(":"))
            return hours * 3600 + minutes * 60 + seconds
    except:
        return 0

file_path = "chrono.txt"
previous_elapsed = read_previous_time(file_path)
start_time = time.time() - previous_elapsed
paused = False
pause_start = 0

try:
    print(
    "Commandes disponibles :\n"
    "  [²]  → Pause / Reprendre\n"
    "  [-]  → Reset (quand en pause)\n"
    "  [E]  → Exporter le chrono\n"
    "  [&]  → Fermer (quand en pause)"
)

    while True:
        if keyboard.is_pressed('²'):
            if not paused:
                paused = True
                pause_start = time.time()
                previous_elapsed = int(pause_start - start_time)
                print("\n || Pause... Appuiez sur [²] pour continuer.", end="\r", flush=True)
                while keyboard.is_pressed('²'):
                    pass
            else:
                paused = False
                pause_duration = time.time() - pause_start
                start_time += pause_duration
                print("->  Reprise! ", end="\r", flush=True)
                print("\n")
                while keyboard.is_pressed('²'):
                    pass

        if not paused:
            elapsed = int(time.time() - start_time)
            hours = elapsed // 3600
            minutes = (elapsed % 3600) // 60
            seconds = elapsed % 60
            with open(file_path, "w") as f:
                f.write(f"{hours:02}:{minutes:02}:{seconds:02}")
            print(f"{hours:02}:{minutes:02}:{seconds:02}", end="\r", flush=True)
            time.sleep(0.21)

        # RESET avec [-] si en pause
        if paused and keyboard.is_pressed('-'):
            with open("chrono.txt", "w") as f:
                f.write("00:00:00")
            previous_elapsed = 0
            start_time = time.time()
            print("\n<- Reset effectué. Appuiez sur [²] pour recommencer.      ", end="\r", flush=True)
            while keyboard.is_pressed('-'):
                pass

        # EXPORT avec [E]
        if keyboard.is_pressed('e'):
            elapsed = int(time.time() - start_time) if not paused else previous_elapsed
            hours = elapsed // 3600
            minutes = (elapsed % 3600) // 60
            seconds = elapsed % 60
            export_time = f"{hours:02}:{minutes:02}:{seconds:02}"

            now = datetime.now().strftime("%d-%m-%Y %H-%M-%S")
            
            # Créer le dossier "Historique" s'il n'existe pas
            export_folder = "Historique"
            os.makedirs(export_folder, exist_ok=True)

            # Créer le chemin complet du fichier
            export_filename = f"Chrono du {now}.txt"
            export_path = os.path.join(export_folder, export_filename)

            with open(export_path, "w") as export_file:
                export_file.write(export_time)

            print(f"\n en cours Exporté sous: {export_filename}", end="\r", flush=True)
            print(" [ DONE ]")
            while keyboard.is_pressed('e'):
                pass

        # QUITTER avec [&]
        if paused and keyboard.is_pressed('&'):
            elapsed = int(time.time() - start_time) if not paused else previous_elapsed
            hours = elapsed // 3600
            minutes = (elapsed % 3600) // 60
            seconds = elapsed % 60
            with open(file_path, "w") as f:
                f.write(f"{hours:02}:{minutes:02}:{seconds:02}")
            print(f"\n Chronomètre arrêté à {hours:02}:{minutes:02}:{seconds:02}.")
            break


except KeyboardInterrupt:
    print("\nChronomètre arrêté.")
