# Process internal data from simulation


def get_hist_bins(simulation):
    paths = simulation.paths
    edges = simulation.edges
    paths_bin = get_hist_bin([len(v["tried"]) for k, v in paths.items()])
    edges_bin = get_hist_bin([v["weight"] for k, v in edges.items()])
    return {
        "paths_bin": paths_bin,
        "edges_bin": edges_bin
    }


def get_hist_bin(numbers):
    hist_bin = {}
    for n in numbers:
        if n in hist_bin:
            hist_bin[n] += 1
        else:
            hist_bin[n] = 1
    res = [[k, v] for k, v in hist_bin.items()]
    res.sort()
    return res
