import math
import pytest
from bmi_calc.core import bmi, category

def test_bmi_calculo_basico():
    assert math.isclose(bmi(70, 1.75), 22.8571428571, rel_tol=1e-6)

def test_bmi_valores_invalidos():
    import pytest
    with pytest.raises(ValueError):
        bmi(0, 1.7)
    with pytest.raises(ValueError):
        bmi(70, 0)

def test_categoria():
    assert category(17.0) == "Abaixo do peso"
    assert category(18.5) == "Peso normal"
    assert category(24.9) == "Peso normal"
    assert category(25.0) == "Sobrepeso"
    assert category(29.9) == "Sobrepeso"
    assert category(30.0) == "Obesidade"
