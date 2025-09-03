from app.models.carro_model import Carro
from app.repositories.carro_repository import CarroRepository

class CarroService:
    @staticmethod
    def listar_carros():
        return CarroRepository.listar()

    @staticmethod
    def buscar_carro(carro_id: int):
        return CarroRepository.buscar_por_id(carro_id)

    @staticmethod
    def criar_carro(marca: str, modelo: str, ano: int):
        carro = Carro(marca=marca, modelo=modelo, ano=ano)
        return CarroRepository.salvar(carro)

    @staticmethod
    def atualizar_carro(carro_id: int, dados: dict):
        carro = CarroRepository.buscar_por_id(carro_id)
        if not carro:
            return None
        carro.marca = dados.get("marca", carro.marca)
        carro.modelo = dados.get("modelo", carro.modelo)
        carro.ano = dados.get("ano", carro.ano)
        return CarroRepository.salvar(carro)

    @staticmethod
    def deletar_carro(carro_id: int):
        carro = CarroRepository.buscar_por_id(carro_id)
        if not carro:
            return None
        CarroRepository.deletar(carro)
        return carro
