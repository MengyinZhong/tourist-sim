class TouristInitSpec:

    # MODEL = "model"
    # AGE_GROUP = "age_group"
    # SPEED = "speed"
    # TIME_BUDGET = "time_budget"
    # PATH_EVAL_DIST = "path_eval_dist"

    def __init__(self, model, age_group, speed, time_budget, path_eval_dist=2):
        self.model = model
        self.age_group = age_group
        self.speed = speed
        self.time_budget = time_budget # Timer object
        self.path_eval_dist = path_eval_dist
