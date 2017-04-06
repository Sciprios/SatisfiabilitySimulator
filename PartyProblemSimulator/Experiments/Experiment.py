from threading import Thread

class Experiment(Thread):
    """ An experiment to be run on the Party Problem Simulator. """

    def run(self):
        """ Should be implemented to execute the experiment and save results. """
        results = self._do_experiment()
        self._save_results(results)
    
    def _do_experiment(self):
        """ Execute the experiment and return results. """
        raise NotImplementedError("The do_experiment method of Experiment is not implemented.")
    
    def _test_method(self, method, no_trials, test_cases):
        """ Assess a single instance. """
        raise NotImplementedError("The do_trial method of Experiment is not implemented.")

    def _do_trial(self, method, equation, variable_count):
        """ Assess a single instance. """
        raise NotImplementedError("The do_trial method of Experiment is not implemented.")

    def _save_results(self, results):
        """ Saves the results of this experiment to disk. """
        raise NotImplementedError("The save_results method of Experiment is not implemented.")