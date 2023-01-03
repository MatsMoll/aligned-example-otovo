from titanic.source import titanic_source
from aligned import FeatureView, FeatureViewMetadata, Entity, HttpStreamSource
from aligned import Int32, Bool, Float, String
from aligned.compiler.transformation_factory import FillNaStrategy
from math import floor, ceil

class TitanicPassenger(FeatureView):
    
    metadata = FeatureViewMetadata(
        name="titanic",
        description="Some features from the titanic dataset",
        batch_source=titanic_source,
        stream_source=HttpStreamSource(topic_name="titanic")
    )
    
    passenger_id = Entity(dtype=Int32())
    
    # Input values
    age = (
        Float()
            .description("A float as some have decimals")
            .is_required()
            .lower_bound(0, is_inclusive=True)
            .upper_bound(110)
    )

    name = String()
    sex = String().accepted_values(["male", "female"])
    survived = Bool().description("If the passenger survived").is_required()
    sibsp = Int32().lower_bound(0).description("Number of siblings on titanic")
    cabin = String()

    # Creates two one hot encoded values
    is_male, is_female = sex.one_hot_encode(['male', 'female'])
    
    # Standard scale the age.
    # This will fit the scaler using a data slice from the batch source
    # limited to maximum 100 rows. We can also uese a time constraint if wanted
    # scaled_age = age.standard_scaled(limit=100).fill_na(0)

    # Fill missing values with a constant 0 value
    constant_filled_age = age.fill_na(0)

    # Fill a missing value with the mean from a selected subsample in the batch source
    # feture request - add a validation step on large datasets that checks if the mean is close to the fill inn value?
    #                  if using the mean fill strategy
    mean_filled_age = age.fill_na(FillNaStrategy.mean(limit=100))
    
    # String operations that return a Bool.
    is_mr = name.contains('Mr.')

    # may not make a lot of sense in this case, but this will
    # encode male as 0 and female as 1
    ordinal_sex = sex.ordinal_categories(["male", "female"]).is_required()

    # A lot of the common operations that is expected
    has_siblings = sibsp != 0
    ratio = constant_filled_age / age
    floor_ratio = constant_filled_age // age
    adding = sibsp + age
    greater_than = sibsp > age
    subtracting = sibsp - age
    floored_age = floor(age)
    ceiled_age = ceil(age)
    rounded_age = round(age)
    abs_scaled_age = abs(constant_filled_age)

    # Some logical operators
    inverted_is_mr = ~is_mr
    logical_and = is_mr & survived
    logical_or = is_mr | survived

    

