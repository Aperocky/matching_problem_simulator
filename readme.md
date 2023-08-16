example run:

```
from sim import MatchingSimulator
simulation = MatchingSimulator(10000, 81, "NEAR")
simulation.run()
```

use `RANDOM` to simulate classical algorithm. `NEAR` for new algorithm.

Currently utility are still considered to be all random.

It will print out iteration data for each iteration, at the end, `simulation.paths` and `simulation.edges` can be inspected and used to generate histograms.

