import unittest
from analise_desempenho import (
    calcular_media,
    criar_verificador_status,
    processar_dados_alunos,
    obter_nomes_aprovados,
    encontrar_melhor_aluno
)

class TestAnaliseDesempenho(unittest.TestCase):

    def setUp(self):

        self.aluno_exemplo_1 = {'id': 1, 'nome': 'Ana Silva', 'notas': [10.0, 8.0, 9.0]}
        self.aluno_exemplo_2 = {'id': 2, 'nome': 'Bruno Costa', 'notas': [5.0, 6.0, 7.0]}

        self.alunos_processados = [
            {'id': 1, 'nome': 'Ana Silva', 'media': 9.25, 'status': 'Aprovado'},
            {'id': 2, 'nome': 'Bruno Costa', 'media': 6.38, 'status': 'Reprovado'},
            {'id': 3, 'nome': 'Carla Dias', 'media': 8.25, 'status': 'Aprovado'}
        ]

    def test_calcular_media(self):

        self.assertAlmostEqual(calcular_media(self.aluno_exemplo_1), 9.0)
        self.assertAlmostEqual(calcular_media(self.aluno_exemplo_2), 6.0)
        self.assertEqual(calcular_media({'nome': 'Sem Notas', 'notas': []}), 0.0)

    def test_closure_criar_verificador_status(self):
    
        verificador_nota_7 = criar_verificador_status(7.0)
        self.assertEqual(verificador_nota_7(9.0), "Aprovado")
        self.assertEqual(verificador_nota_7(7.0), "Aprovado")
        self.assertEqual(verificador_nota_7(6.9), "Reprovado")

        verificador_nota_5 = criar_verificador_status(5.0)
        self.assertEqual(verificador_nota_5(5.1), "Aprovado")
        self.assertEqual(verificador_nota_5(4.9), "Reprovado")

    def test_alta_ordem_processar_dados_alunos(self):
        
        alunos = [self.aluno_exemplo_1, self.aluno_exemplo_2]
        extrator_de_nome = lambda aluno: aluno['nome']
        nomes = processar_dados_alunos(alunos, extrator_de_nome)
        self.assertEqual(nomes, ['Ana Silva', 'Bruno Costa'])

    def test_list_comprehension_obter_nomes_aprovados(self):
        
        nomes_aprovados = obter_nomes_aprovados(self.alunos_processados)
        self.assertEqual(len(nomes_aprovados), 2)
        self.assertIn('Ana Silva', nomes_aprovados)
        self.assertIn('Carla Dias', nomes_aprovados)
        self.assertNotIn('Bruno Costa', nomes_aprovados)

    def test_lambda_encontrar_melhor_aluno(self):
        
        melhor_aluno = encontrar_melhor_aluno(self.alunos_processados)
        self.assertEqual(melhor_aluno['nome'], 'Ana Silva')
        self.assertEqual(melhor_aluno['media'], 9.25)
        
        self.assertEqual(encontrar_melhor_aluno([]), {})

if __name__ == '__main__':
    unittest.main(verbosity=2)