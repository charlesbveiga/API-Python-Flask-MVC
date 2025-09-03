from app import app, db
from app.models.carro_model import Carro

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

        if Carro.query.count() == 0:
            exemplos = [
                Carro(marca="Fiat", modelo="Uno", ano=2010),
                Carro(marca="Volkswagen", modelo="Golf", ano=2015),
                Carro(marca="Chevrolet", modelo="Corsa", ano=2008),
            ]
            db.session.add_all(exemplos)
            db.session.commit()
            print(">>> Inseridos 3 carros de exemplo no banco.")
        else:
            print(">>> Banco já possui registros, nada a inserir.")

    app.run(debug=True)
