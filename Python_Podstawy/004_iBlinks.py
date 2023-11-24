'''
Ten skrypt policzy ile razy mrugamy okiem w czasie X lat.
Zakładamy, ze:
-liczba mrugniec na minute to 20
-liczba minut w godzinie to 60
-liczba godzin w dobie to 24
-liczba lat jest wprowadzana przez uzytkownika (X)
Uwaga! 
Nie uwzgledniamy lat przestepnych! Kazdy rok ma 365 dni.
Zakladamy, ze spimy zdrowe 8h dziennie. 
Liczba godzin na dobe bedzie wiec wynosic 16 :)
'''

#liczba mrugniec okiem na minute
blinksPerMin = 20
#liczba minut na godzine i liczba godzin w dobie
minInHour = 60
hoursInDay = 16
#liczba dni w roku i liczba lat 
daysInYear = 365
X=input("Wprowadz liczbe lat i zatwierdz enterem:")
X=int(X)
print("W ciagu ",X,"lat mrugniesz az",((20*60*16*365)*X),"razy! :o")