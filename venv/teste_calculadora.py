from calculadora import Calculadora  ##assert é uma verificação 

def teste_01_soma_0_0():
    calc = Calculadora()
    assert calc.soma(0, 0) == 0 
    
def teste_01_soma_0_10():
    calc = Calculadora()
    assert calc.soma(0, 10) == 10 
    assert calc.soma(10, 0) == 10
    
def teste_01_soma_12_30():
     calc = Calculadora()
     assert calc.soma(12, 30) == 42 
     assert calc.soma(30, 12) == 42
     
     
def test_subtrai_26_18():
    calc = Calculadora()
    assert calc.subtrai(26, 18) == 8
    
def test_subtrai_18_26():
    calc = Calculadora()
    assert calc.subtrai(18, 26) == -8
    
def test_subtrai_15_0():
    calc = Calculadora()
    assert calc.subtrai(15, 0) == 15
    
def test_subtrai_0_0():
    calc = Calculadora()
    assert calc.subtrai(0, 0) == 0

def testt_divisao_8_4():
    calc = Calculadora()
    assert calc.divisao(8, 4 ) == 2