from functools import reduce
from typing import List, Dict, Callable, Any


alunos_db = [
    {'id': 1, 'nome': 'Carlos Cauan', 'notas': [9.0, 8.5, 9.5, 10.0]},
    {'id': 2, 'nome': 'Fabiano pascal', 'notas': [6.0, 7.5, 5.5, 6.5]},
    {'id': 3, 'nome': 'Roberto jose', 'notas': [8.0, 8.5, 7.5, 9.0]},
    {'id': 4, 'nome': 'Javax da silva', 'notas': [4.0, 5.5, 6.0, 3.5]},
    {'id': 5, 'nome': 'Stacker overflow filho', 'notas': [9.5, 9.0, 10.0, 10.0]},
]


def calcular_media(aluno: Dict) -> float:
    total = sum(aluno['notas'])
    return total / len(aluno['notas']) if aluno['notas'] else 0.0

def criar_verificador_status(nota_de_corte: float) -> Callable[[float], str]:
    def verificar(media: float) -> str:
        return "Aprovado" if media >= nota_de_corte else "Reprovado"
    return verificar

def processar_dados_alunos(
    alunos: List[Dict],
    funcao_processamento: Callable[[Dict], Any]
) -> List[Any]:
    
    return [funcao_processamento(aluno) for aluno in alunos]

def obter_nomes_aprovados(alunos_processados: List[Dict]) -> List[str]:

    return [aluno['nome'] for aluno in alunos_processados if aluno['status'] == 'Aprovado']

def encontrar_melhor_aluno(alunos_processados: List[Dict]) -> Dict:
    
    if not alunos_processados:
        return {}
    return max(alunos_processados, key=lambda aluno: aluno['media'])


def main():
    
    print(">>> INICIANDO ANÁLISE DE DESEMPENHO DE ALUNOS <<<\n")

    verificador_aprovacao_7 = criar_verificador_status(7.0)
    print(f"--> [Closure] Critério de aprovação definido: média >= 7.0\n")

    def adicionar_media(aluno: Dict) -> Dict:
    
        return {**aluno, 'media': round(calcular_media(aluno), 2)}

    alunos_com_media = processar_dados_alunos(alunos_db, adicionar_media)

    def adicionar_status(aluno: Dict) -> Dict:
        
        return {**aluno, 'status': verificador_aprovacao_7(aluno['media'])}

    alunos_com_status = processar_dados_alunos(alunos_com_media, adicionar_status)

    print("--> [Alta Ordem] Dados dos alunos processados com média e status:")
    for aluno in alunos_com_status:
        print(f"    - {aluno['nome']}: Média = {aluno['media']}, Status = {aluno['status']}")
    print("-" * 50)

    aprovados = obter_nomes_aprovados(alunos_com_status)
    print(f"--> [List Comprehension] Alunos aprovados: {aprovados}\n")

    melhor_aluno = encontrar_melhor_aluno(alunos_com_status)
    print(f"--> [Lambda] Aluno com melhor desempenho: "
          f"{melhor_aluno['nome']} (Média: {melhor_aluno['media']})\n")

    print(">>> ANÁLISE CONCLUÍDA <<<\n")
    print("--- Relatório Final ---")
    print(f"Dados brutos: {alunos_db}")
    print(f"Dados processados: {alunos_com_status}")


if __name__ == "__main__":
    main()
