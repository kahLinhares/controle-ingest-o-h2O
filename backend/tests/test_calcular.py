import json

def test_calcular(client):
    test_cases = [
        {
            "idade_grupo": "adulto",
            "peso": 80
        },
        {
            "idade_grupo": "adulto",
            "peso": -1
        },
    ]
    for payload in test_cases:
        response = client.post("/calcular", json=payload)  # Envia payload como JSON
    
        response_json = response.get_json()  # Extrai JSON da resposta
        
        if 'error' in response_json:
            assert response.status_code == 400  # Verifica o código de status 400 para erro
            assert 'total' not in response_json  # Verifica se não há 'total' se há um erro
            assert response_json['error'] == 'Peso deve ser maior que 0'  # Verifica a mensagem de erro específica
        else:
            ml_agua = 0
    
            if payload["idade_grupo"] == "adulto":
                ml_agua = 35
            elif payload["idade_grupo"] == "crianca":
                ml_agua = 50
    
            expected_total = payload["peso"] * ml_agua
    
            assert 'total' in response_json  # Verifica se 'total' está presente no JSON
            assert response_json['total'] == expected_total  # Verifica se o valor calculado está correto
