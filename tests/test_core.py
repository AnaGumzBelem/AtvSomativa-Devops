import pytest
import math
from bmi_calc.core import bmi, category


def test_bmi_calculo_basico():
    assert math.isclose(bmi(70, 1.75), 22.8571428571, rel_tol=1e-6)


def test_bmi_peso_zero():
    with pytest.raises(ValueError):
        bmi(0, 1.7)


def test_bmi_altura_zero():
    with pytest.raises(ValueError):
        bmi(70, 0)


def test_categoria_abaixo_do_peso():
    assert category(17.0) == "Abaixo do peso"


def test_categoria_peso_normal():
    assert category(24.9) == "Peso normal"
