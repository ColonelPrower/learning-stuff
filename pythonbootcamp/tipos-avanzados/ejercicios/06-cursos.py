"""
Filtrar cursos
"""

cursos = [
        {"nombre":"html","estado":"en progreso"},
        {"nombre":"css3","estado":"completado"},
        {"nombre":"Sql","estado":"no iniciado"},
        {"nombre":"Python","estado":"en progreso"},
        {"nombre":"Js,html,css,nodejs","estado":"completado"},
        {"nombre":"React","estado":"no iniciado"}
        ]

def filtrar_cursos(cursos):
    progreso = []
    completo = []
    noIniciado = []

    for curso in cursos:
        match curso["estado"]:
            case "en progreso":
                progreso.append(curso["nombre"])
            case "completado":
                completo.append(curso["nombre"])
            case "no iniciado":
                noIniciado.append(curso["nombre"])
    print("Cursos en progreso:")
    for i in progreso:
        print(f"- {i}")
    print("Cursos completados")
    for i in completo:
        print(f"- {i}")
    print("Cursos no iniciados")
    for i in noIniciado:
        print(f"- {i}")

filtrar_cursos(cursos)
