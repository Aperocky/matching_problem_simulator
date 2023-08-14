example run:

```
from sim import MatchingSimulator
simulation = MatchingSimulator(10000, 81)
simulation.run()
```

It will print out iteration data, at the end, `sim.paths` and `sim.edges` can be inspected and used to generate histograms.
