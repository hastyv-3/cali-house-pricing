from flask import abort

# Checks for required keys and numeric values
# Sorts key-value pairs for model
def sanitize_input(data, PREDICTORS) -> dict[str, float]:
    sorted_data: dict[str, float] = dict()
    for predictor in PREDICTORS:
        if predictor not in data.keys():
            abort(400, "Bad Request: must include keys (MedInc, HouseAge, AveRooms, AveBedrms,\
                Population, AveOccup, Latitude, Longitude) ")
        try:
            value = float(data.get(predictor))
        except ValueError:
            abort(400, "Bad Request: values must be numeric")
        sorted_data[predictor] = data.get(predictor)
    return sorted_data