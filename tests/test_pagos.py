from src.pagos import *
from unittest.mock import MagicMock

class TestVerificarSaldo(unittest.TestCase):
  def test_verificarSaldo(self):
    mock_verificar_saldo = MagicMock(return_value=100.0)
    verificar = mock_verificar_saldo(usuario='Ricardo')
    
    

unittest.main(argv=[''], exit=False)