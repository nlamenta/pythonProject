### łańcuchy znaków
my_name = "natalia" #nie myName
my_another_name = my_name

print("my name id: " + str(id(my_name))) #indentyfikator zmiennej przed zmianą
print("my another name id: " + str(id(my_another_name)))

my_name = "ola"
print("my name id: " + str(id(my_name))) #indentyfikator zmiennej po zmianą
print("my another name id: " + str(id(my_another_name)))


print(f"witaj {my_name}") #indentyfikator zmiennej po zmianie
print(f'witaj "{my_name}"')

print(my_name)
print(my_name.title())
print(my_another_name.lower())
print(my_another_name.upper())

login = "    nata123  "
print(f'"{login}"')
print(f'"{login.strip()}"') #ctrl +d, .strip() usuwa białe znaki
print(f'"{login.rstrip()}"') #.rstrip() usuwa białe znaki z prawej strony
print(f'"{login.lstrip()}"') #.lstrip() usuwa białe znaki z lewej strony;
                            #nie zmienia na stałe tylko na czas wywołania metody; jeśli chcemy utworzyć na stałe to robimy nową instancję
login = login.upper()
print(login)

uep_website = "https://ue.poznan.pl"
print(uep_website)
print(uep_website
      .removeprefix("https://")
      .removeprefix("https://")
      .removesuffix("/"))

#usuwanie prefixu; jeśli nie mamy takiego prefixu to nic się nie stanie
#podwójna metoda, druga nic nier robi; ma pokazać, że można tak zagnieżdzać metody

### liczby

universe_age = 140_000_000_000 #podkreślniki tylko wizualnie wyróżnia kod, nie wpływają na  printowanie

x = 0
y = 2
z = 3

x, y, z = 0, 2, 3 #ta linijka oznacza to samo co te trzy wyżej

MAX_CONNECTIONS = 1000
PORT = 800 #parametry wywołania programu, które nie będą zmieniane
