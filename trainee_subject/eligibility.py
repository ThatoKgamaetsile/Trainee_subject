from edc_constants.constants import YES


class TraineeStatusEvaluator:

    def __init__(self, trainee_status=None):
        self.eligible = None
        if trainee_status == YES:
            self.eligible = True
        else:
            self.eligible = False


class Eligibility:

    def __init__(self, trainee_status=None):
        self.trainee_status_evaluator = TraineeStatusEvaluator(
            trainee_status=trainee_status)
        self.criteria = dict(
            trainee_status=self.trainee_status_evaluator.eligible)
        self.eligible = all(self.criteria.values())






