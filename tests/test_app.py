# Tests generados automáticamente por Cursor
# Prompt utilizado: "Genera un test unitario simple para verificar que la ruta home funciona"

import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    """Prueba que la página de inicio carga correctamente"""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Bienvenido" in response.data