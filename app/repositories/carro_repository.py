from app.models.carro_model import Carro
from app.extensions import db

class CarroRepository:
    @staticmethod
    def listar():
        return Carro.query.all()

    @staticmethod
    def buscar_por_id(carro_id: int):
        return Carro.query.get(carro_id)

    @staticmethod
    def salvar(carro: Carro):
        db.session.add(carro)
        db.session.commit()
        return carro

    @staticmethod
    def deletar(carro: Carro):
        db.session.delete(carro)
        db.session.commit()
