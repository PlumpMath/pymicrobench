# Ignore flake8 E722 warning in the whole file:
# flake8: noqa

import perf
from six.moves import xrange

from pybench import Test


class TryRaiseExcept(Test):

    version = 2.0
    operations = 2 + 3 + 3
    inner_loops = 8

    def test(self, loops):

        error = ValueError
        range_it = xrange(loops)
        t0 = perf.perf_counter()

        for _ in range_it:
            try:
                raise error("something")
            except:
                pass
            try:
                raise error("something")
            except:
                pass
            try:
                raise error("something")
            except:
                pass
            try:
                raise error("something")
            except:
                pass
            try:
                raise error("something")
            except:
                pass
            try:
                raise error("something")
            except:
                pass
            try:
                raise error("something")
            except:
                pass
            try:
                raise error("something")
            except:
                pass

        return perf.perf_counter() - t0


class TryExcept(Test):

    version = 2.0
    operations = 15 * 10
    # try/except repeated 150 times!
    inner_loops = 150

    def test(self, loops):

        range_it = xrange(loops)
        t0 = perf.perf_counter()

        for _ in range_it:
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass

            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass

            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass

            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass

            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass

            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass

            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass

            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass

            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass

            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass

            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass

            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass

            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass

            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass

            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass
            try:
                pass
            except:
                pass

        return perf.perf_counter() - t0
