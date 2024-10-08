import json


try:
   
    with open('faturamento.json', 'r') as arquivo:
        dados = json.load(arquivo)
    
   
    faturamento_diario = dados['faturamento']
    
  
    faturamento_diario = [x for x in faturamento_diario if x > 0]
    
 
    menor_faturamento = min(faturamento_diario)
    maior_faturamento = max(faturamento_diario)
    

    media_faturamento = sum(faturamento_diario) / len(faturamento_diario)
    
  
    dias_acima_media = sum(1 for x in faturamento_diario if x > media_faturamento)
    
   
    print(f"Menor faturamento: R${menor_faturamento:.2f}")
    print(f"Maior faturamento: R${maior_faturamento:.2f}")
    print(f"Número de dias acima da média: {dias_acima_media}")

except FileNotFoundError:
    print("Arquivo 'faturamento.json' não encontrado. Verifique se o arquivo está no diretório correto.")
except json.JSONDecodeError:
    print("Erro ao processar o arquivo JSON. Verifique o conteúdo.")
