name = "Janusz"

print(len(name)) #Length - długość. Czyli ile zmienna name ma znaków
print(name.capitalize()) #Zamienia pierwszą literę na wielką lub wielka na mala
print(name.upper()) #Zamienia wszystkie litery na wielkie a wielkie na male
print(name.lower()) # _"_ na małe
print(name[0]) #Wyświetla tylko konkretny znak. Liczymy od zera!
print(name[0:2]) #Wyświetla 2 kolejne znaki liczone od zera
print(name[3:]) #Wyświetla wszystkie kolejne znaki od 3 litery, liczone od zera
print(name[-3:]) #Wyświetla wszystkie kolejne znaki od 3 litery od końca, liczone od 1

channel = "Jak to jest byc skryba?"
print(channel.split(" ")) #Dzielimy podane zdanie na mniejsze części. Po split podajemy znak, według jakiego dzielimy. Tutaj spacja.

join_string=" " #Łączymy wyrazy w zdanie oddzielajac je spacja
print(join_string.join(['Jak', 'to', 'jest', 'byc', 'skryba?']))

print(name.startswith("J")) #Sprawdzenie, czy string zaczyna sie jakims znakiem
print(name.endswith("J")) #Sprawdzenie, czy string konczy sie jakims znakiem

print(name.lstrip("J")) #Usuwa litere J z lewej strony
print(name.rstrip("z")) #Usuwa litere z z prawej strony
print(name.strip("n")) #Usuwa litery n z obu stron stringa
print(name.strip()) #Usuwa wszystkie spacje ze stringa

last_name = "Typowy"
print(name+" "+last_name) #Łączenie stringów
print(join_string.join([name,last_name])) #Łączenie stringów joinem

james_bond = 7
print(str(james_bond).zfill(3)) #zamiana inta na stringa, nastepnie .zfill ilosc znakow z lewej strony, z ktorych ma sie skladac nowy string