import unittest
from unittest.mock import patch, MagicMock
import io
import sys
import requests
import runpy

class TestClima(unittest.TestCase):

    # Cenário 1: Sucesso (200) - API responde corretamente
    @patch('os.getenv', return_value="chave_valida_simulada")
    @patch('requests.get')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_sucesso_200(self, mock_stdout, mock_get, mock_getenv):
        
        mock_resposta = MagicMock()
        mock_resposta.status_code = 200
        mock_resposta.json.return_value = {
            "weather": [{"description": "céu limpo"}],
            "main": {"temp": 28.5},
            "name": "Fortaleza"
        }
        mock_get.return_value = mock_resposta

        runpy.run_path('clima.py')
        
        saida = mock_stdout.getvalue()
        self.assertIn("Temperatura: 28.5°C", saida)
        self.assertIn("Condição: Céu limpo", saida)

    # Cenário 2: Erro de Autorização (401) - Chave inválida
    @patch('os.getenv', return_value="chave_valida_simulada")
    @patch('requests.get')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_erro_401(self, mock_stdout, mock_get, mock_getenv):
        
        mock_resposta = MagicMock()
        mock_resposta.status_code = 401
        mock_get.return_value = mock_resposta

        runpy.run_path('clima.py')
        
        saida = mock_stdout.getvalue()
        self.assertIn("Erro 401", saida)
        self.assertIn("inválida ou não autorizada", saida)

    # Cenário 3: Demora na Resposta (Timeout) - Sem internet ou API lenta
    @patch('os.getenv', return_value="chave_valida_simulada")
    @patch('requests.get')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_timeout(self, mock_stdout, mock_get, mock_getenv):
        
        mock_get.side_effect = requests.exceptions.Timeout("Timeout simulado")

        runpy.run_path('clima.py')
        
        saida = mock_stdout.getvalue()
        self.assertIn("Erro de timeout", saida)
        self.assertIn("demorou mais de 10 segundos", saida)

if __name__ == '__main__':
    unittest.main()