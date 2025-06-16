# Sistema de Gestión Clínica

## Descripción
Sistema en Python para gestionar pacientes, médicos, turnos y recetas médicas con interfaz de línea de comandos.

## Requisitos
- Python 3.7 o superior
- No requiere librerías externas

## Estructura del Proyecto
```
├── documentacion.py
├── main.py                 # Punto de entrada
├── cli/
│   └── cli.py              # Interfaz de usuario
├── models/                
│   ├── clinica.py          # Lógica principal
│   ├── paciente.py         # Paciente
│   ├── medico.py           # Médico
│   ├── especialidad.py     # Especialidades médicas
│   ├── turno.py            # Turnos médicos
│   ├── receta.py           # Recetas médicas
│   ├── historia_clinica.py # Historial pacientes
│   └── exception.py        # Excepciones personalizadas
└── test/                   # Test unitarios
    ├──test_clinica.py
    ├──test_especialidad.py
    ├──test_historia clinica.py
    ├──test_medico.py
    ├──test_receta.py
    └──test_turno.py
```

## Ejecución
```bash
python3 main.py
```

## Funcionalidades

### 1. Agregar Paciente
- Nombre, DNI (8 dígitos), fecha nacimiento (dd/mm/aaaa)
- Crea automáticamente historia clínica

### 2. Agregar Médico
- Nombre, matrícula, especialidades con días de atención

### 3. Agendar Turno
- DNI paciente, matrícula médico, especialidad, fecha/hora
- Valida que el médico atienda esa especialidad ese día

### 4. Agregar Especialidad a Médico
- Asigna nueva especialidad con días de atención

### 5. Emitir Receta
- Lista de medicamentos para un paciente

### 6. Ver Historia Clínica
- Muestra turnos y recetas del paciente

### 7-9. Listados
- Ver todos los turnos/pacientes/médicos

## Ejecución de Tests
```bash
python -m unittest 
```

## Validaciones Principales
- DNI único de 8 dígitos
- Fechas en formato dd/mm/aaaa
- Médicos deben tener al menos una especialidad
- No turnos duplicados para mismo médico/fecha
- Médico debe atender la especialidad el día solicitado

## Flujo Recomendado
1. Registrar médicos con especialidades
2. Registrar pacientes
3. Agendar turnos
4. Emitir recetas
5. Consultar historias clínicas

## Manejo de Errores
Sistema completo de excepciones personalizadas para cada tipo de error (DNI inválido, paciente no existe, turno duplicado, etc.).

