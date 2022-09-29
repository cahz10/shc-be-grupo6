from django.contrib import admin
from .models.user import User
from .models.paciente import Paciente
from .models.medico import Medico
from .models.signos_vitales import signosVitales
from .models.familiar import Familiar
from .models.auxiliar import Auxiliar
from .models.enfermero import Enfermero
from .models.enfermero_paciente import Enfermero_Paciente
from .models.familiar_paciente import Familiar_Paciente
from .models.medico_paciente import Medico_Paciente
from .models.historia_clinica import Historia_Clinica


admin.site.register(User)
admin.site.register(Paciente)
admin.site.register(Medico)
admin.site.register(Familiar)
admin.site.register(signosVitales)
admin.site.register(Auxiliar)
admin.site.register(Enfermero)
admin.site.register(Enfermero_Paciente)
admin.site.register(Familiar_Paciente)
admin.site.register(Medico_Paciente)
admin.site.register(Historia_Clinica)


