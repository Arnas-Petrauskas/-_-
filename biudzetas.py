class biudzetas():
    def __init__(self):
        self.suma = 0
        self.report = []

    def return_balance(self):
        for a in self.report:
            if(a < 0):
                print(f"Išlaidos:{a}")
            else:
                print(f"Pajamos:{a}")
    def smt(self,sumaa):
        self.report.append(sumaa)
    def skaiciuojam(self):
        return sum(self.report)
        
naujas_biudziatas = biudzetas()
   
   
def begining():
    try:
        action = int(input("Kokį veiksmą norite atliki:\n1.Įnešti\n2.Atlikti mokėjimą\n3.Peržiūrėti balansa\n4.Peržiūrėti balansą\n"))
        veiksmas(action)
    except ValueError:
        print("Rašyk skaičius ASILE")
        begining()
        
def veiksmas(action):
    if (action == 1):
        try:
            inesti = int(input("Kokią sumą norite įnesti: "))
            i = 0 + inesti
            naujas_biudziatas.smt(i)
            begining()
        except ValueError:
            print("Prašome vesti sumą")
            begining()
    elif(action == 2):
        try:
            inesti = int(input("Už kiek pirkote: "))
            i = 0 - inesti
            naujas_biudziatas.smt(i)
            begining()
        except ValueError:
            print("Prašome vesti sumą")
            begining()
    elif(action == 3):
        naujas_biudziatas.return_balance()
        begining()
    elif(action ==4):
        likutis = naujas_biudziatas.skaiciuojam()
        if likutis <0:
            print(f"Jūsų skola {likutis}")
        else:
            print(f"Jūsų likutis {likutis}")
        begining()
        

begining()