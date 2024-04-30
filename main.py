

class Calculator():

    def __init__(self) -> None:
        pass

    def start(self):
        self.victories = int(input("Qual o total de vitórias? "))
        self.defeats = int(input("Qual o total de derrotas? "))
        self.rank = self.get_rank()

    def get_rank(self):
        self.balance = self.victories - self.defeats
        if self.balance <= 10:
            return "Ferro"
        elif 11 <= self.balance <= 20:
            return "Bronze"
        elif 21 <= self.balance <= 50:
            return "Prata"
        elif 51 <= self.balance <= 80:
            return "Ouro"
        elif 81 <= self.balance <= 90:
            return "Diamante"
        elif 91 <= self.balance <= 100:
            return "Lendário"
        elif self.balance >= 101:
            return "Imortal"
        else:
            return "Error"

    def execute(self):
        self.start()
        print(self)

    def __str__(self) -> str:
        return f"O Herói tem de saldo de {self.balance} está no nível {self.rank}"


if __name__ == "__main__":
    Calculator().execute()
