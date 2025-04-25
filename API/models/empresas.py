class Empresas:
    def __init__(self, nome, cnpj, endereco, setor_atividade):
        self.nome = nome
        self.cnpj = cnpj
        self.endereco = endereco
        self.setor_atividade = setor_atividade.strip()

    def from_tuple(data):
        return Empresas(data[1], data[2], data[3], data[4])
    
    def from_list(data):
        return [Empresas.from_tuple(item) for item in data]
    
    def __str__(self):
        return f'{self.nome} - {self.cnpj} - {self.endereco} - {self.setor_atividade}'