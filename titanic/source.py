from aligned import FileSource

titanic_source = FileSource.csv_at(
    "data/titanic.csv", 
    mapping_keys={
        'PassengerId': 'passenger_id',
        'Age': 'age',
        'Name': 'name',
        'Sex': 'sex',
        'Survived': 'survived',
        'SibSp': 'sibsp',
        'Cabin': 'cabin',
})