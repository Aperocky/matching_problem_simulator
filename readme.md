example run:

```
from sim import MatchingSimulator
from sim import get_hist_bins


simulation = MatchingSimulator(10000, 81, "NEAR")
simulation.run()
get_hist_bins(simulation)
```

use `RANDOM` to simulate classical algorithm. `NEAR` for new algorithm.

Currently utility are still considered to be all random.

It will print out iteration data for each iteration, at the end, `simulation.paths` and `simulation.edges` can be inspected and used to generate histograms. `get_hist_bins` functions help with that.
