# Module
# Sind Libraries, die sich aus Skripten bilden, und Funktionalitäten bringen die wir brauchen
# Enthalten Code der sich mit genau einem Thema befasst
# Können importiert werden und teilweise installiert werden

# Wie importiere ich ein Modul?
# import <Name>
# from <Name> import <Member>

# import M006
# Importiert das gesamte Skript, führt es komplett aus, und stellt alle Funktionen/Klassen/Variablen/... zu Verfügung
# Um Member anzugreifen muss der Modulname vor jedem Member geschrieben werden -> M006.<Name>

# from M006 import countCase
# Einzelne Member aus dem Modul importieren. Hier werden die Member direkt in den Code eingebunden -> müssen nicht über Modulname angegriffen werden
# from M006 import countCase, sumNumbers, listTeilnehmer -> Mehrere Member importieren
# from M006 import * -> Alles importieren

# Mit as <Name> können imports umbenannt werden
# import M006 as M6
# from M006 import countCase as cc

import M007b

print(__name__)