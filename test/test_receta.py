
import unittest
from datetime import datetime, timedelta 
from models.receta import Receta
from models.paciente import Paciente 
from models.medico import Medico
from models.especialidad import Especialidad 
from models.exception import ( NombreInvalidoError, MatriculaInvalidaError, EspecialidadVaciaError)

class TestReceta(unittest.TestCase):

    def setUp(self):

        self.especialidad_general = Especialidad("Medicina General", ["lunes", "miércoles"])


        self.paciente_valido = Paciente("Sofia Ramos", "40567890", "12/06/1995")

        self.medico_valido = Medico("Dra. Laura Flores", "MP23456", [self.especialidad_general])

        self.lista_medicamentos_ok = ["Amoxicilina 500mg", "Ibuprofeno 400mg", "Vitamina C"]
        self.lista_medicamentos_vacia = [] 
        self.lista_medicamentos_con_invalido = ["Paracetamol", "", "Aspirina"]
        self.lista_medicamentos_con_tipo_incorrecto = ["Jarabe", 123, "Pastillas"] 

    def test_str_muestra_formato_correcto_de_receta(self):

        print("\n--- Probando el formato de impresión de la receta (__str__) ---")
        fecha_fija_para_str = datetime(2025, 1, 15, 12, 30, 0) 

        receta_para_str = Receta(self.paciente_valido, self.medico_valido, ["Analgesico", "Antihistaminico"])

        fecha_generada_formateada = receta_para_str._Receta__fecha.strftime("%Y-%m-%d %H:%M:%S")
        expected_output = (
            f"Receta(\n"
            f"  Paciente: Sofia Ramos (DNI: 40567890)\n"
            f"  Médico: Dra. Laura Flores (Matrícula: MP23456)\n"
            f"  Medicamentos: [Analgesico, Antihistaminico]\n"
            f"  Fecha de Emisión: {fecha_generada_formateada}\n"
            f")"
        )


if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)