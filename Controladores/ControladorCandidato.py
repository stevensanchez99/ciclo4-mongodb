from Repositorios.RepositorioCandidato import RepositorioCandidato
from Repositorios.RepositorioPartido import RepositorioPartido
from Modelos.Candidato import Candidato
from Modelos.Partido import Partido
class ControladorCandidato():
    def __init__(self):
        print("*** Creando Controlador para el Candidato ***")
        self.repositorioCandidato=RepositorioCandidato()
        self.repositorioPartido=RepositorioPartido()

    # Listado
    def index(self):
        print("La lista de candidatos se completo con éxito")
        return self.repositorioCandidato.findAll()

    # Creacion de candidato
    def create(self, infoCandidato):
        print("Candidato creado con éxito!")
        nuevoCandidato=Candidato(infoCandidato)
        return self.repositorioCandidato.save(nuevoCandidato)


    # Borrar un candidato
    def delete(self, id):
        print("Borrando el candidato con id:  ", id)
        return self.repositorioCandidato.delete(id)

    # actualizacion
    def update(self, id, infoCandidato):
        print("El candidato con id: ", id ," fue actualizado con éxito")
        candidatoActual = Candidato(self.repositorioCandidato.findById(id))
        candidatoActual.cedula=infoCandidato["cedula"]
        candidatoActual.numero = infoCandidato["numero"]
        candidatoActual.nombre = infoCandidato["nombre"]
        candidatoActual.apellido = infoCandidato["apellido"]
        return self.repositorioCandidato.save(candidatoActual)

    # consulta
    def show(self, id):
        print("Consultando... Candidato: ", id)
        elCandidato=Candidato(self.repositorioCandidato.findById(id))
        return elCandidato.__dict__ #almacena

    """
    Relacion Candidato con partido
    """
    def asignarPartido(self, id, id_Partido):
        candidatoActual = Candidato(self.repositorioCandidato.findById(id))
        partidoActual = Partido(self.repositorioPartido.findById(id_Partido))
        candidatoActual.partido = partidoActual
        return self.repositorioCandidato.save(candidatoActual)
