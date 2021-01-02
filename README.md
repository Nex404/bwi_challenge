# BWI Coding Challenge Januar 2020
Die Coding Challenge ist im Ordner Challengebeschreibung zu finden. Dort findet man auch eine Excel Datei, in der ich die Werte des Programms auf deren Korrektheit überprüft habe.

## Voraussetzungen
Im Grunde gibt es keine spezifischen Voraussetzungen, außer Python 3 installiert zu haben. Für gewöhnlich ist dies auf Linux Geräten vorinstalliert, falls nicht, kann es im Terminal mithilfe des folgenden Befehls installiert werden.
```
sudo apt update
sudo apt -y upgrade
sudo apt-get install python3.6
``` 
Neuere Versionen von Python sind ebenfalls möglich.

## Code Struktur
Der gegebene Datensatz aus der Challenge wurde extrahiert und in einer selbstgeschriebenen .csv Datei eingefügt. Gelesen werden die Datensätze und die Fahrer mit ihren Gewichten.   
Während der Ausführung kann man die maximale Kapazität der Beladung in kg angeben. Ein default Wert ist dafür 1100kg (wie in der Challenge gegeben). Auch der Datensatz kann verändert werden, wenn man den gegebenen entweder editiert oder einen neuen einfügt und den alten löscht oder aus dem Ordner entfernt.   
(Damit soll eine Verallgemeinerung vorgenommen werden und auch bei kommenden Lieferungen anwendungsnah bleiben)   
Nach der Ausführung findet man die Packlisten für jeden einzelnen LKW im Ordner Truckload und auch ausgegeben im Terminal.

## Algorithmus
Bei den gegebenen Daten sieht man sofort, dass man im Punkt Masse begrenzt ist und einen maximalen Nutzwert erhalten möchte. Als erstes wurde ein Nutzwert/Gramm Verhältnis und dieses absteigend sortiert. Daraufhin wurden die LKWs nacheinander mit den besten (vom Verhältnis) Gegenständen beladen. 

## Ausführung unter Linux(Ubuntu)
### Download des Programms
```
git clone https://github.com/Nex404/bwi_challenge.git
```
### Ausführung des Programms
```
cd Path/to/Folder
python3 bwi_challenge.py
```