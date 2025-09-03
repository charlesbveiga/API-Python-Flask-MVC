from flask import Blueprint, jsonify, make_response, request
from app.services.carro_service import CarroService

carros_bp = Blueprint("carros", __name__, url_prefix="/carros")

@carros_bp.route("/", methods=["GET"])
def listar_carros():
    carros = CarroService.listar_carros()
    return make_response(jsonify([
        {"id": c.id, "marca": c.marca, "modelo": c.modelo, "ano": c.ano}
        for c in carros
    ]), 200)

@carros_bp.route("/", methods=["POST"])
def criar_carro():
    dados = request.get_json()
    carro = CarroService.criar_carro(dados["marca"], dados["modelo"], dados["ano"])
    return make_response(jsonify(
        mensagem="Carro cadastrado com sucesso!",
        carro={"id": carro.id, "marca": carro.marca, "modelo": carro.modelo, "ano": carro.ano}
    ), 201)

@carros_bp.route("/<int:carro_id>", methods=["PUT"])
def atualizar_carro(carro_id):
    dados = request.get_json()
    carro = CarroService.atualizar_carro(carro_id, dados)
    if not carro:
        return make_response(jsonify(mensagem="Carro não encontrado."), 404)
    return make_response(jsonify(mensagem="Carro atualizado com sucesso!"), 200)

@carros_bp.route("/<int:carro_id>", methods=["DELETE"])
def deletar_carro(carro_id):
    carro = CarroService.deletar_carro(carro_id)
    if not carro:
        return make_response(jsonify(mensagem="Carro não encontrado."), 404)
    return make_response(jsonify(mensagem="Carro deletado com sucesso!"), 200)