def test_DeveRetornarBackendOnline(client):
    # Arrange & Act
    response = client.get('/')

    # Assert
    assert b"Backend online!" in response.data
