from aligned.model import Model
from titanic.passenger import TitanicPassenger

titanic_model = Model(
    features=[
        TitanicPassenger.select(lambda view: [
            view.constant_filled_age,
            view.is_male,
            view.is_mr,
            view.has_siblings,
            view.survived
        ])
    ],
    target=TitanicPassenger().survived
)