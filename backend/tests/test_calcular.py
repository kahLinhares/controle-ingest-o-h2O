import json

class TestCalcular:
    def test_DeveRetornarPesoAdultoCom80kg(self, client):
        # Arrange
        idade_grupo = "adulto"
        peso = 80

        payload = {
            "idade_grupo": idade_grupo,
            "peso": peso
        }

        # Act
        response = client.post("/calcular", content_type='application/json', data=json.dumps(payload))       
        
        response_json = response.get_json()

        calc_result = 35 * 80  # 2800

        # Assert
        assert response_json['total'] == calc_result
        assert response.status_code == 200
    
    def test_DeveRetornarPesoCriancaCom32_5kg(self, client):
       # Arrange
        idade_grupo = "crianca"
        peso = 32.5

        payload = {
            "idade_grupo": idade_grupo,
            "peso": peso
        }

        # Act
        response = client.post("/calcular", content_type='application/json', data=json.dumps(payload))

       
        response_json = response.get_json()

        calc_result = 50 * 32.5  # 1625

         # Assert
        assert response_json['total'] == calc_result
        assert response.status_code == 200
    
    def test_DeveRetornarErroSePeso0kg(self, client):
        # Arrange
        idade_grupo = "crianca"
        peso = 0

        payload = {
            "idade_grupo": idade_grupo,
            "peso": peso
        }

        # Act
        response = client.post("/calcular", content_type='application/json', data=json.dumps(payload))

        
        response_json = response.get_json()

        # Assert
        assert response_json.get("error", None) == "Peso é obrigatório"
        assert response.status_code == 400


    def test_DeveRetornarErroSePesoNegativo(self, client):
        # Arrange
        idade_grupo = "adulto"
        peso = -20

        payload = {
            "idade_grupo": idade_grupo,
            "peso": peso
        }

        # Act
        response = client.post("/calcular", content_type='application/json', data=json.dumps(payload))

        response_json = response.get_json()

        # Assert
        assert response_json.get("error", None) == "Peso deve ser maior que 0"
        assert response.status_code == 400
    
    def test_DeveRetornarErroSemGrupoIdade(self, client):
        # Arrange
        peso = 100

        payload = {
            "peso": peso
        }

        # Act
        response = client.post("/calcular", content_type='application/json', data=json.dumps(payload))

        response_json = response.get_json()

        # Assert
        assert response_json.get("error", None) == "Grupo de Idade Inválido"
        assert response.status_code == 400

    def test_DeveRetornarErroSemPeso(self, client):
        # Arrange
        idade_grupo = "crianca"

        payload = {
            "idade_grupo": idade_grupo,
        }

        # Act
        response = client.post("/calcular", content_type='application/json', data=json.dumps(payload))

        response_json = response.get_json()

        # Assert
        assert response_json.get("error", None) == "Peso é obrigatório"
        assert response.status_code == 400

        # Test_calculadora_agua.py usando TDD
    def test_calculo_agua_para_gravidas():
        # Assumindo que a função `calcular_agua_para_gravidas` ainda não existe
        from calculadora_agua import calcular_agua_para_gravidas
        
        # Teste básico: 2 litros por dia mais 300 ml para grávidas
        assert calcular_agua_para_gravidas(70) == (70 * 35) + 0.3
