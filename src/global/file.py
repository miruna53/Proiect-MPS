class File:

    def __init__(self, thresholds, optimal_threshold, f_measures):
        self.thresholds = thresholds
        self.optimal_threshold = optimal_threshold
        self.f_measures = f_measures

    def get_thresholds(self):
        return self.thresholds

    def set_thresholds(self, thresholds):
        self.thresholds = thresholds

    def get_optimal_threshold(self):
        return self.optimal_threshold

    def set_optimal_threshold(self, optimal_threshold):
        self.optimal_threshold = optimal_threshold

    def get_f_measures(self):
        return self.f_measures

    def set_f_measures(self, f_measures):
        self.f_measures = f_measures