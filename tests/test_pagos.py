import unittest
from unittest.mock import patch
from src.pagos import procesar_pago  

class TestVerificarSaldo(unittest.TestCase):
   
    @patch('src.pagos.verificar_saldo_en_banco')
    def test_pago_suficiente(self, mock_verificar_saldo):
     
        mock_verificar_saldo.return_value = 3000

        resultado = procesar_pago(usuario='Ricardo', monto=2000, verificador=mock_verificar_saldo)
           
        self.assertTrue(resultado)

    @patch('src.pagos.verificar_saldo_en_banco')
    def test_pago_insuficiente(self, mock_verificar_saldo):
        mock_verificar_saldo.return_value = 1000

        resultado = procesar_pago(usuario='Ricardo', monto=2000, verificador=mock_verificar_saldo)
        
        self.assertFalse(resultado)

    @patch('src.pagos.verificar_saldo_en_banco')
    def test_pago_exacto(self, mock_verificar_saldo):
        mock_verificar_saldo.return_value = 2000

        resultado = procesar_pago(usuario='Ricardo', monto=2000, verificador=mock_verificar_saldo)
        
        self.assertTrue(resultado)
  
unittest.main(argv=[''], exit=False)
i