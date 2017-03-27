""" A context manager which only print the total time of process. """

import cProfile


class CProfileContextManager():
    """A context manager of cProfile package used to build patched environment.
    """
    def __init__(self):
        self.original_print_method = cProfile.Profile.print_stats

    def __enter__(self):
        self.patch()

    def __exit__(self):
        self.restore()

    def patch(self):
        """ Replace print_stats method with the custom one. """
        cProfile.Profile.print_stats = self.get_patched_method()

    def restore(self):
        """ Restore the print_stats method. """
        cProfile.Profile.print_stats = self.original_print_method

    def get_patched_method(self):

        def print_stats_with_custom_output(self, sort=-1):
            """ Print total time used during the whole process.  """
            import pstats
            print(pstats.Stats(self).total_tt)

        return print_stats_with_custom_output