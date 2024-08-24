import tkinter as tk
import tkinter.ttk as ttk

"""
Dieses Python-Skript verwendet die Tkinter-Bibliothek, um ein grafisches Benutzeroberflächen-Spiel "Tic Tac Toe" zu erstellen. 

Der Code definiert ein Hauptfenster (`root`) und zwei Frames (`frameOben` und `frameUnten`), um die Benutzeroberfläche zu organisieren. Die Frames enthalten verschiedene Widgets, die das Hauptspiel und die Steuerungselemente darstellen.

1. **Globale Variablen**:
    - `activePlayer`: Bestimmt, welcher Spieler ("X" oder "O") gerade am Zug ist.
    - `turnCounter`: Zählt die Anzahl der Züge im aktuellen Spiel.
    - `player1Wins` und `player2Wins`: Zählen die Siege der beiden Spieler.

2. **Hauptfenster und Layout**:
    - Das Hauptfenster (`root`) wird erstellt und benannt.
    - Zwei Frames werden erstellt: `frameOben` für die Anzeige von Spielerinformationen und `frameUnten` für das Spielfeld und die Steuerknöpfe.
    - Die Frames werden so konfiguriert, dass sie sich bei Größenänderungen des Fensters gleichmäßig anpassen.

3. **Labels**:
    - `labelGame`: Zeigt den Titel des Spiels an.
    - `labelPlayer1` und `labelPlayer2`: Zeigen die Namen der Spieler an.
    - `labelPlayer1Wins` und `labelPlayer2Wins`: Zeigen die Anzahl der Siege jedes Spielers an.

4. **Spielfeld**:
    - Ein 3x3 Grid von Buttons (`buttonsSpielfeld`) wird erstellt, um das Spielfeld darzustellen. Jeder Button hat eine `command`-Funktion, die bei einem Klick aufgerufen wird.

5. **Funktionen**:
    - `close_game()`: Beendet die Anwendung.
    - `neustart_game()`: Setzt das Spielfeld zurück und setzt den Zugzähler zurück.
    - `start_game()`: Startet das Spiel, nachdem die Namen der Spieler eingegeben wurden.
    - `open_name_window()`: Öffnet ein neues Fenster zur Eingabe der Spielernamen.
    - `check_for_win(checkPlayer)`: Überprüft, ob der angegebene Spieler gewonnen hat, und aktualisiert die Siegesanzahl. Gibt eine entsprechende Nachricht zurück, wenn ein Spieler gewonnen hat.
    - `update_wins(winner)`: Aktualisiert die Siegesanzahl der Spieler und zeigt die neuen Werte in den Labels an.
    - `on_button_click(row, column)`: Reagiert auf einen Klick auf das Spielfeld, führt den Zug aus, überprüft auf einen Gewinn und wechselt den aktiven Spieler. Zeigt eine Fehlermeldung an, wenn ein ungültiger Zug gemacht wird.
    - `disable_buttons()`: Deaktiviert alle Buttons im Spielfeld, um zu verhindern, dass weitere Züge gemacht werden.

6. **Fehlermeldungen**:
    - Wenn ein Spieler auf ein bereits besetztes Feld klickt, wird ein zusätzliches Fenster mit der Fehlermeldung "Falsche Eingabe!" angezeigt. 

7. **Initialisierung**:
    - Das Hauptfenster wird zunächst verborgen (`root.withdraw()`), um es später nach der Eingabe der Spielernamen anzuzeigen.
    - Das Fenster zur Eingabe der Namen wird geöffnet.

Das Skript bietet eine vollständige Implementierung eines Tic Tac Toe-Spiels mit GUI-Elementen zur Spielerinteraktion und zur Fehlerbehandlung.
"""

activePlayer = "X"
turnCounter = 0
player1Wins = 0
player2Wins = 0

# Hauptfenster
root = tk.Tk()
root.title("Tic Tac Toe")

# Frames
frameOben = ttk.Frame(root, width=360, height=360)
frameOben.grid(column=0, row=0, sticky="nsew")

frameUnten = ttk.Frame(root, width=360, height=360)
frameUnten.grid(column=0, row=1, sticky="nsew", pady=30, padx=20)

# frameoben gewichten
for i in range(2):
    frameOben.grid_columnconfigure(i, weight=1)

# frameUnten gewichten
for i in range(4):
    frameUnten.grid_rowconfigure(i ,weight=1)
    frameUnten.grid_columnconfigure(i, weight=1)

# Labels
labelGame = ttk.Label(frameOben, text="Tic Tac Toe", font=("Helvetica", 20), anchor="center")
labelGame.grid(row=0, column=0, columnspan=2, pady=30, sticky="nsew")

labelPlayer1 = ttk.Label(frameOben, text="Spieler 1", font=("Helvetica", 14, "underline"), background="#F28B82")
labelPlayer1.grid(row=1, column=0)

labelPlayer1Wins = ttk.Label(frameOben, text="Siege: 0", font=("Helvetica", 10))
labelPlayer1Wins.grid(row=2, column=0)

labelPlayer2 = ttk.Label(frameOben, text="Spieler 2", font=("Helvetica", 14))
labelPlayer2.grid(row=1, column=1)

labelPlayer2Wins = ttk.Label(frameOben, text="Siege: 0", font=("Helvetica", 10))
labelPlayer2Wins.grid(row=2, column=1)

# Buttons Spielfeld
buttonsSpielfeld = [[None for _ in range(3)] for _ in range(3)]

for row in range(3):
    for col in range(3):
        button = tk.Button(frameUnten, text="", height=5, width=10, 
                           command=lambda r=row, c=col: on_button_click(r, c))
        button.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)
        buttonsSpielfeld[row][col] = button
    

# Spiel beenden
def close_game():
     root.destroy()

frameUnten.grid_rowconfigure(3, weight=0, minsize=30)

tk.Button(frameUnten, text="Beenden", command=close_game).grid(row=4, column=0, sticky="nsew")

# Spiel neustarten 
def neustart_game():

    global turnCounter

    for row in range(3):
        for col in range(3):
            buttonsSpielfeld[row][col].config(text="", state=tk.ACTIVE)

    turnCounter = 0  

tk.Button(frameUnten, text="Neustart", command=neustart_game).grid(row=4, column=2, sticky="nsew")

# Funktion, um das Namen-Fenster zu erstellen
def start_game():

    # Wenn keine Eingabe, dannn Standart-Text
    if entry_player1.get():
        labelPlayer1.config(text=entry_player1.get())
    if entry_player2.get():
        labelPlayer2.config(text=entry_player2.get())

    root.deiconify()
    player_name_window.destroy()

# Funktion, in der Namen eingegeben werden
def open_name_window():

    # Variablen Erstellen
    global player_name_window, entry_player1, entry_player2

    # Hauptfenster erstellen
    player_name_window = tk.Toplevel(root)
    player_name_window.title("Spielernamen eingeben")

    # Content Frame
    frame_name = ttk.Frame(player_name_window, padding="10")
    frame_name.grid(row=0, column=0, sticky="nsew")

    # Labels
    ttk.Label(frame_name, text="Name Spieler 1:").grid(row=0, column=0, padx=5, pady=5)
    entry_player1 = ttk.Entry(frame_name, font=("Helvetica", 12))
    entry_player1.grid(row=0, column=1, padx=5, pady=5)

    ttk.Label(frame_name, text="Name Spieler 2:").grid(row=1, column=0, padx=5, pady=5)
    entry_player2 = ttk.Entry(frame_name, font=("Helvetica", 12))
    entry_player2.grid(row=1, column=1, padx=5, pady=5)

    # Button
    tk.Button(frame_name, text="Spiel starten", command=start_game).grid(row=2, column=0, columnspan=2, pady=10)

def check_for_win(checkPlayer):

    global player1Wins, labelPlayer2Wins

    print(checkPlayer)
    # Überprüfen der Reihen
    for i in range(3):
        if all(buttonsSpielfeld[i][j].cget("text") == checkPlayer for j in range(3)):
            update_wins(checkPlayer)
            return f"{checkPlayer} hat gewonnen (Reihe {i + 1})!"

    # Überprüfen der Spalten
    for i in range(3):
        if all(buttonsSpielfeld[j][i].cget("text") == checkPlayer for j in range(3)):
            update_wins(checkPlayer)
            return f"{checkPlayer} hat gewonnen (Spalte {i + 1})!"

    # Überprüfen der ersten Diagonale
    if all(buttonsSpielfeld[i][i].cget("text") == checkPlayer for i in range(3)):
        update_wins(checkPlayer)
        return f"{checkPlayer} hat gewonnen (Diagonale von oben links nach unten rechts)!"

    # Überprüfen der zweiten Diagonale
    if all(buttonsSpielfeld[i][2 - i].cget("text") == checkPlayer for i in range(3)):
        update_wins(checkPlayer)
        return f"{checkPlayer} hat gewonnen (Diagonale von oben rechts nach unten links)!"

    return None
        
def update_wins(winner):
    global player1Wins, player2Wins

    if winner == "X":
        player1Wins += 1
        labelPlayer1Wins.config(text=f"Siege: {player1Wins}")
    elif winner == "O":
        player2Wins += 1
        labelPlayer2Wins.config(text=f"Siege: {player2Wins}")

def on_button_click(row, column):
    global activePlayer, turnCounter

    # Sicherstellen, dass nur leere Felder bearbeitet werden
    if buttonsSpielfeld[row][column].cget("text") == "":
        # Zug ausführen
        buttonsSpielfeld[row][column].config(text=activePlayer)
        
        # Gewinn überprüfen
        result = check_for_win(activePlayer)
        if result:
            print(result)
            # beenden oder zurücksetzen
            disable_buttons()
            return

        # Spieler wechseln
        if activePlayer == "X":
            activePlayer = "O"
            labelPlayer1.config(background="")
            labelPlayer1.config(font=("Helvetica", 14))
            labelPlayer2.config(background="#F28B82")
            labelPlayer2.config(font=("Helvetica", 14, "underline"))
        else:
            activePlayer = "X"
            labelPlayer2.config(background="")
            labelPlayer2.config(font=("Helvetica", 14))
            labelPlayer1.config(background="#F28B82")
            labelPlayer1.config(font=("Helvetica", 14, "underline"))

        turnCounter += 1
    else:
        falsche_eingabe_fenster = tk.Toplevel(root)
        falsche_eingabe_fenster.title("Fehler!")

        frame_falsche_eingabe_fenster = ttk.Frame(falsche_eingabe_fenster, padding=10)
        frame_falsche_eingabe_fenster.grid(row=0, column="0", sticky="nsew")

        labelFalscheEingabe = ttk.Label(frame_falsche_eingabe_fenster, text="Falsche Eingabe!", font=("Helvetica", 14))
        labelFalscheEingabe.grid(column=0, row=0)

        buttonVerstanden = tk.Button(frame_falsche_eingabe_fenster, text="Verstanden", 
                                     command=lambda: falsche_eingabe_fenster.destroy())
        buttonVerstanden.grid(row=1, column=0, pady=10)
        
        frame_falsche_eingabe_fenster.grid_columnconfigure(0, weight=1)

def disable_buttons():
    for row in range(3):
        for col in range(3):
            buttonsSpielfeld[row][col].config(state=tk.DISABLED)



# Verstecke Hauptfesnter
root.withdraw()

# Öffne Fenster für Eingabe der Namen
open_name_window()

root.mainloop()