# Sistema de monitoreo Apollo-11
## Entregables
1. Repositorio con código correspondiente con la solución.
2. Tablero de Trello con la distribución del trabajo y actividades asignadas por el grupo.

# Objetivo general
> Implementar un sistema de monitoreo basado en transmisión de archivos que operará en intervalos de 20 segundos. Este sistema permitirá mantener un control minucioso sobre el estado operativo de cada uno de los satélites, naves espaciales, vehículos espaciales y otros componentes clave.


# Criterios nombre archivos
> El nombre del archivo deberá seguir el siguiente formato estándar:
> APL[ORBONE|CLNM|TMRS|GALXONE|UNKN]-0000[1-1000].log.El identificador "APL" seguido de un código correspondiente a la misión permitirá un seguimiento preciso y la asociación de los archivos con los dispositivos específicos utilizados en cada misión.

# Contenido del archivo
* Cada archivo generado para una misión deberá contener internamente datos en un formato semiestructurado que incluirá los siguientes campos: fecha (date), misión (mission), tipo de dispositivo (device_type), estado del dispositivo (device_status) y hash.

    * Formato fecha: ddmmyyHHMMSS
    * Misiones: OrbitOne, ColonyMoon, VacMars, GalaxyTwo
    * Tipo dispositivo: navigation system, satellite, Nave, Computador, Sensor Gravedad, Vehiculo Lunar, etc.
    * Los estados posibles para cada dispositivo son: excellent (excelente), good (bueno), warning (advertencia), faulty (defectuoso), killed (inoperable) y unknown (desconocido).
    * Hash: Generación de hash a partir de la fecha, misión, tipo de dispositivo y estado del dispositivo. Solo se genera hash si el nombre del archivo es diferente de **unknown**