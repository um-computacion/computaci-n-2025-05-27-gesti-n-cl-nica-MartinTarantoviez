import unittest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from src.models.receta import Receta
from src.models.paciente import Paciente
from src.models.medico import Medico

class TestReceta(unittest.TestCase):
    def test_creacion_receta(self):
        p = Paciente("Juan", "1", "01/01/2000")
        m = Medico("Dr. A", "M1")
        r = Receta(p, m, ["Paracetamol"])
        self.assertIn("Paracetamol", str(r))

    def test_receta_sin_medicamentos(self):
        p = Paciente("Juan", "1", "01/01/2000")
        m = Medico("Dr. A", "M1")
        with self.assertRaises(ValueError):
            Receta(p, m, [])

    def test_receta_datos_invalidos(self):
        p = Paciente("Juan", "1", "01/01/2000")
        m = Medico("Dr. A", "M1")
        
        with self.assertRaises(ValueError):
            Receta(None, m, ["Paracetamol"])
        with self.assertRaises(ValueError):
            Receta(p, None, ["Paracetamol"])
        with self.assertRaises(ValueError):
            Receta(p, m, None)