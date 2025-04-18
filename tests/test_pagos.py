import unittest
from unittest.mock import patch
from src.pagos import procesar_pago  # Solo importa lo que necesitas

class TestVerificarSaldo(unittest.TestCase):
   
    @patch('src.pagos.verificar_saldo_en_banco')
    def test_pago_suficiente(self, mock_verificar_saldo):
        # Configura el mock para devolver 3000
        mock_verificar_saldo.return_value = 3000

        # Llama a procesar_pago y pasa el mock
        resultado = procesar_pago(usuario='Ricardo', monto=2000, verificador=mock_verificar_saldo)
           
        # Verifica que el resultado sea True (saldo suficiente)
        self.assertTrue(resultado)

    @patch('src.pagos.verificar_saldo_en_banco')
    def test_pago_insuficiente(self, mock_verificar_saldo):
        # Configura el mock para devolver 1000
        mock_verificar_saldo.return_value = 1000

        # Llama a procesar_pago
        resultado = procesar_pago(usuario='Ricardo', monto=2000, verificador=mock_verificar_saldo)
        
        # Verifica que el resultado sea False (saldo insuficiente)
        self.assertFalse(resultado)

    @patch('src.pagos.verificar_saldo_en_banco')
    def test_pago_exacto(self, mock_verificar_saldo):
        # Configura el mock para devolver 2000
        mock_verificar_saldo.return_value = 2000

        # Llama a procesar_pago
        resultado = procesar_pago(usuario='Ricardo', monto=2000, verificador=mock_verificar_saldo)
        
        # Verifica que el resultado sea True (pago exacto)
        self.assertTrue(resultado)
  
# Ejecuta las pruebas
unittest.main(argv=[''], exit=False)
