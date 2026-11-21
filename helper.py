from flask import abort

# Checks for required keys and numeric values
# Sorts key-value pairs for model
def sanitize_input(data, PREDICTORS) -> dict[str, float]:
    sorted_data: dict[str, float] = dict()
    if data is None:
        abort(400, "Bad Request: null value error")
    for predictor in PREDICTORS:
        if predictor not in data.keys():
            abort(400, "Bad Request: must include keys (MedInc, HouseAge, AveRooms, AveBedrms,\
                Population, AveOccup, Latitude, Longitude) ")
        try:
            sorted_data[predictor] = data.get(predictor)
        except ValueError:
            abort(400, "Bad Request: values must be numeric")
    return sorted_data