class EmpresasSetores:
    def __init__(self, fk_cnpj, setor, total_funcionarios, qtd_homens, qtd_mulheres, idade_media_homens, idade_media_mulheres):
        self.fk_cnpj = fk_cnpj
        self.setor = setor.strip()
        self.total_funcionarios = int(total_funcionarios)
        self.qtd_homens = int(qtd_homens)
        self.qtd_mulheres = int(qtd_mulheres)
        self.idade_media_homens = float(idade_media_homens)
        self.idade_media_mulheres = float(idade_media_mulheres)

    def relatorio(self):
        return {
            'fk_cnpj': self.fk_cnpj,
            'setor': self.setor,
            'total_funcionarios': self.total_funcionarios,
            'qtd_homens': self.qtd_homens,
            'qtd_mulheres': self.qtd_mulheres,
            'taxa_homens': self.qtd_homens / self.total_funcionarios,
            'taxa_mulheres': self.qtd_mulheres / self.total_funcionarios,
            'idade_media_homens': self.idade_media_homens,
            'idade_media_mulheres': self.idade_media_mulheres
        }
    
    def from_tuple(data):
        return EmpresasSetores(data[1], data[2], data[3], data[4], data[5], data[6], data[7])
    
    def from_list(data):
        return [EmpresasSetores.from_tuple(item) for item in data]
    
    def __str__(self):
        return f'{self.fk_cnpj} - {self.setor} - {self.total_funcionarios} - {self.qtd_homens} - {self.qtd_mulheres} - {self.idade_media_homens} - {self.idade_media_mulheres}'