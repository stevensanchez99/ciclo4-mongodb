from Modelos.Resultados import Resultados
from Modelos.Mesa import Mesa
from Modelos.Candidato import Candidato
from Repositorios.RepositorioResultados import RepositorioResultados
from Repositorios.RepositorioCandidato import RepositorioCandidato
from Repositorios.RepositorioMesa import RepositorioMesa

class ControladorResultados():

    def __init__(self):
        print("*** Creando Controlador para los resultados de las votaciones ***")
        self.repositorioResultados = RepositorioResultados()
        self.repositorioMesa = RepositorioMesa()
        self.repositorioCandidato = RepositorioCandidato()

        # Listado resultados
    def index(self):
        print("La lista de los resultados de las votaciones se completo con éxito")
        return self.repositorioResultados.findAll()

    """
    ASIGNACIÓN CANDIDATO Y PARTIDO A RESULTADO
    """
    def create(self, infoResultados, id_mesa, id_candidato):
        nuevoResultado= Resultados(infoResultados)
        laMesa = Mesa(self.repositorioMesa.findById(id_mesa))
        elCandidato = Candidato(self.repositorioCandidato.findById(id_candidato))
        nuevoResultado.mesa = laMesa
        nuevoResultado.candidato = elCandidato
        return self.repositorioResultados.save(nuevoResultado)

        # consulta de resultados
    def show(self, id):
        print("Consultando... Resultados de las votaciones: ", id)
        losResultados = Resultados(self.repositorioResultados.findById(id))
        return losResultados.__dict__

        """# Creacion de un resultado
    def create(self, infoResultados):
        print("Los resultados de las votaciones fueron creados con éxito!")
        nuevoResultado = Resultados(infoResultados)
        return self.repositorioResultados.save(nuevoResultado)
        """

        """
        MODIFICACIÓN DE RESULTADOS
        """

        # actualizacion de los resultados
    def update(self, id, infoResultados, id_mesa, id_candidato):
        print("los resultados con id: ", id, " fueron actualizados con éxito")
        ResultadoActual = Resultados(self.repositorioResultados.findById(id))
        ResultadoActual.numero = infoResultados["numero"]
        ResultadoActual.idPartido = infoResultados["idPartido"]
        return self.repositorioResultados.save(ResultadoActual)
        laMesa = Mesa(self.repositorioMesa.findById(id_mesa))
        elcandidato = Candidato(self.repositorioCandidato.findById(id_candidato))
        ResultadoActual.mesa = laMesa
        ResultadoActual.candidato = elcandidato
        return self.repositorioResultados.save(ResultadoActual)

        # Borrar un resultado
    def delete(self, id):
        print("Borrando los resultados con id:  ", id)
        return self.repositorioResultados.delete(id)
