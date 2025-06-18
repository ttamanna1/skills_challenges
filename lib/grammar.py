class GrammarStats:
    def __init__(self):
        self.total_checks = 0
        self.good_checks = 0

    def check(self, text):
        # Parameters:
        #   text: string
        # Returns:
        #   bool: true if the text begins with a capital letter and ends with a
        #         sentence-ending punctuation mark, false otherwise
        is_good = text[0].isupper() and text[-1] in '.?!'
        self.total_checks += 1
        if is_good:
            self.good_checks += 1
        return is_good

    def percentage_good(self):
        # Returns:
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.
        if self.total_checks == 0:
            return 0 
        return round((self.good_checks / self.total_checks) * 100)
