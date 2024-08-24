# Tic Tac Toe - Ein Beginner-Projekt mit Tkinter

Dieses Projekt ist eine einfache Implementierung des klassischen Tic-Tac-Toe-Spiels in Python unter Verwendung der `tkinter`-Bibliothek zur Erstellung einer grafischen Benutzeroberfläche (GUI). Es eignet sich hervorragend für Einsteiger, die das Programmieren mit Python und die Verwendung von GUI-Elementen erlernen möchten.

## Projektübersicht

Dieses Spiel bietet:

- Eine grafische Benutzeroberfläche, die mit `tkinter` erstellt wurde.
- Ein 3x3 Tic-Tac-Toe-Spielbrett, auf dem zwei Spieler abwechselnd spielen können.
- Eine Funktion zur Eingabe der Spielernamen.
- Eine Punkteanzeige, die die Anzahl der gewonnenen Spiele für jeden Spieler zählt.
- Die Möglichkeit, das Spiel neu zu starten oder zu beenden.
- Eine einfache Fehlerbehandlung, die eine Fehlermeldung anzeigt, wenn ein ungültiger Zug gemacht wird (z.B. wenn ein bereits belegtes Feld angeklickt wird).

## Funktionen und Features

- **start_game()**: Startet das Spiel nach der Eingabe der Spielernamen.
- **on_button_click(row, column)**: Reagiert auf den Klick eines Spielers auf das Spielfeld, aktualisiert den Zug und wechselt den Spieler.
- **check_for_win(checkPlayer)**: Überprüft nach jedem Zug, ob ein Spieler gewonnen hat.
- **neustart_game()**: Setzt das Spielfeld zurück, um eine neue Runde zu beginnen.
- **close_game()**: Beendet das Spiel.
- **disable_buttons()**: Deaktiviert alle Spielfeld-Buttons, wenn das Spiel endet.

## Weiterführende Ideen

Dieses Projekt kann als Ausgangspunkt für weiterführende Ideen und Erweiterungen dienen:

- **KI-Gegner hinzufügen**: Implementiere einen Algorithmus, der es ermöglicht, gegen den Computer zu spielen.
- **Unentschieden erkennen**: Füge eine Logik hinzu, die erkennt, wenn das Spiel unentschieden endet.
- **Verbesserte GUI**: Ändere das Design des Spielfeldes oder füge Animationen hinzu.
- **Speicherbare Statistiken**: Implementiere eine Möglichkeit, die Spielstatistiken dauerhaft zu speichern.

## Fazit

Dieses Tic-Tac-Toe-Projekt ist ein großartiger Einstieg in die GUI-Programmierung mit Python.
