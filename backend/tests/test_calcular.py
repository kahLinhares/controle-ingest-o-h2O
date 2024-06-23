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

        ml_agua = 0

        if payload["idade_grupo"] == "adulto":
            ml_agua = 35
        elif payload["idade_grupo"] == "crianca":
            ml_agua = 50

        expected_total = payload["peso"] * ml_agua

        assert response_json['total'] == expected_total
