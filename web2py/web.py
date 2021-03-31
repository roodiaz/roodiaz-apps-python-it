db.define_table(
    "alumno",
    Field("dni", type="integer"),
    Field("nombre", type="string"),
    Field("fecha_alta", type="date"),
    Field("curso_actual", type="string", requires=IS_IN_SET(["Python", "Java", "PHP"]))
)

def alumnos():
    return {"grid": SQLFORM.grid(db.alumno, user_signature=False)}
