import random #funkce pro náhodné generování čísel

jmeno = "Tobiáš" 
prijmeni = "Kubáň" #proměnná pro jméno a příjmení

print(jmeno, prijmeni) #výpis jména a příjmení

vek = input("Zadej svůj věk: ") #získání věku od uživatele jako text

vek = int(vek)
print("Zadal jsi věk:", vek) #výpis věku 


promenna1 = "Algoritmizace" #definice první proměnné
promenna2 = "Python" #definice druhé proměnné

print(len(promenna1)) #výpis délky napsaného textu  v proměnné1
print(len(promenna2)) #výpis délky napsaného textu  v proměnné2

jablka = 6 #hodnota proměnné



l = 0 #proměnné pro hrušky

for i in range(5): #cyklus který se 5x opakuje a přy každém opakování přičte 3.(akorát že se neopakuje 5x ale rovnou vypíše výsledek)
    hrušky += 3
print(l) #výpis výsledné hodnoty hrušek

try:
    vek2 = int(input("Zadejte svůj věk: ")) #získání věku od uživatele a převod na číslo
    print("Děkuji") #potvrzení o úspěšném zadání čísla
except ValueError:
    print("Zadej celočíselnou hodnotu.") #text který se ukáže když zadáte něco jiného než číslo


w = random.randint(1, 10)#generování náhodného čísla mezi 1 a 10
print(w)#výpis náhodného čísla
