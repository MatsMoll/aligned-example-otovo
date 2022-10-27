from aligned.model import ModelService
from titanic.passenger import TitanicPassenger

titanic_model = ModelService(
    features=[
        TitanicPassenger.select_all()
    ]
)