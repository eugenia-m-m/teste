class SistemaAdocao:
    def __init__(self):
        self.list_animais = []

    def cadastrar_Animal(self, id, nome, especie, sexo, idade, raca, disponibilidade):
        for pet in self.list_animais:
            if pet.id == id:
                return "Animal já cadastrado."

        animal = Animal(id, nome, especie, sexo, idade, raca, disponibilidade)
        self.list_animais.append(animal)
        return "Animal cadastrado com sucesso."

    def pesquisar_Animal(self, id_animal):
        for animal in self.list_animais:
            if animal.id == id_animal:
                return animal
        return None

    def editar_Animal(self, id_animal):
        for animal in self.list_animais:
            if animal.id == id_animal:
                animal.nome = input("Digite o novo nome do animal: ")
                animal.especie = input("Digite a nova espécie do animal: ")
                animal.sexo = input("Digite o novo sexo do animal: ")
                animal.idade = input("Digite a nova idade do animal: ")
                animal.raca = input("Digite a nova raça do animal: ")
                animal.disponibilidade = input("Digite a disponibilidade do animal: ")
                return "Animal atualizado com sucesso."
            
            else:
                return "Animal nao encontrado."

    def listar_Animais(self):
        if not self.list_animais:
            return "Nenhum animal cadastrado."
        
        resultado = "\n---------------- Animais cadastrados ----------------\n"

        for animal in self.list_animais:
            resultado += f"ID: {animal.id}\n"
            resultado += f"Nome: {animal.nome}\n"
            resultado += f"Espécie: {animal.especie}\n"
            resultado += f"Sexo: {animal.sexo}\n"
            resultado += f"Idade: {animal.idade}\n"
            resultado += f"Raça: {animal.raca}\n"
            resultado += f"Disponibilidade: {animal.disponibilidade}\n"
            resultado += "-" * 40 + "\n"
        return resultado
    
    def remover_Animal(self, id_animal): 
        animal = int(input("Digite o ID do animal que deseja remover: "))
        for animais in self.list_animais:
            if animal == id_animal:
                self.list_animais.remove(animais)
            return "Animal removido com sucesso."
        return "Animal nao encontrado."
    
class Animal:
    def __init__(self, id, nome, especie, sexo, idade, raca, disponibilidade):
        self.id = id
        self.nome = nome
        self.especie = especie
        self.sexo = sexo
        self.idade = idade
        self.raca = raca
        self.disponibilidade = disponibilidade
class Adotante:
    def __init__(self, nome, idade, rg, cpf, comprovante):
        self.__nome = nome
        self.__idade = idade
        self.__rg = rg
        self.__cpf = cpf
        self.__comprovante = comprovante

    @property
    def mostrar_nome (self):
        return self.__nome

    @property
    def mostrar_idade (self):
        return self.__idade

# class Adocao:
    
sistema = SistemaAdocao()
sistema.cadastrar_Animal(1, "Luna", "Cachorro", "Fêmea", "2 anos", "Labrador", "Sim")
sistema.cadastrar_Animal(2, "Rex", "Cachorro", "Macho", "3 anos", "Vira-lata", "Sim")
sistema.cadastrar_Animal(3, "Toby", "Gato", "Macho", "1 ano", "Siames", "Sim")
sistema.cadastrar_Animal(4, "Charlie", "Gato", "Macho", "2 anos", "Persa", "Sim")

print(sistema.listar_Animais())

print(sistema.pesquisar_Animal(2))

print(sistema.listar_Animais())

print(sistema.editar_Animal(2))

print(sistema.listar_Animais())

print(sistema.remover_Animal(2))

print(sistema.listar_Animais())