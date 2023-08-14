import random


"""
New (attempt) algorithm for stable matching problem
"""
class MatchingSimulator():

    def __init__(self, n, delta):
        self.n = n
        self.delta = delta

        # whole process iteration count
        self.iter_count = 0
        # a try_set for all possible tries.
        self.try_set = set(range(delta))
        self.paths = {}
        self.edges = {}
        for i in range(n):
            # PATHS
            # times: times proposing
            # found: currently found match
            # tried: All past proposal attempts
            self.paths[i] = {"times": 0, "found": -1, "tried": set()}
            # EDGES
            # suitor: current round proposed paths
            # chosen: currently chosen path
            # weight: all historical proposal count
            self.edges[i] = {"suitor": [], "chosen": -1, "weight": 0}
        self.complete = False

    # Get all paths that need to propose for current round
    def get_paths_needing_to_propose(self):
        to_propose = []
        for i in range(self.n):
            if self.paths[i]["found"] == -1:
                to_propose.append(i)
        return to_propose

    # Paths are to propose here
    def run_propose(self):
        to_propose = self.get_paths_needing_to_propose()
        for p in to_propose:
            if len(self.paths[p]["tried"]) >= self.delta/3:
                self.iter_data["loner_count"] += 1
                continue # No possible proposal target, stay lonely
            self.paths[p]["times"] += 1
            # Find proposal target, avoid previously proposed.
            curr_selection = random.choice(list(self.try_set - self.paths[p]["tried"]))
            self.paths[p]["tried"].add(curr_selection)
            proposal_target = (curr_selection + p) % self.n
            # Add proposal to the edge selected.
            self.edges[proposal_target]["suitor"].append(p)
        self.iter_data["proposal_count"] = len(to_propose) - self.iter_data["loner_count"]

    # proposals are evaluated here
    def match(self):
        for i in range(self.n):
            edge = self.edges[i]
            if not edge["suitor"]:
                continue # nothing to do here as no proposal came in

            proposal_count = len(edge["suitor"])
            winner = random.choice(edge["suitor"])
            if edge["chosen"] == -1:
                self.paths[winner]["found"] = i
                edge["chosen"] = winner
                self.iter_data["new_match_count"] += 1
            else:
                chance = proposal_count/(proposal_count + edge["weight"])
                if random.random() < chance:
                    self.paths[edge["chosen"]]["found"] = -1 # Previous match go home
                    edge["chosen"] = winner
                    self.paths[winner]["found"] = i
                    self.iter_data["bump_count"] += 1
            edge["weight"] += len(edge["suitor"])
            edge["suitor"] = []

    def run_iteration(self):
        if self.complete:
            print("Simulation is over")
            return
        self.iter_count += 1
        self.iter_data = {
            "iteration": self.iter_count,
            "proposal_count": 0, # This rounds proposal count
            "new_match_count": 0, # New matches (path -> non-matched edge)
            "bump_count": 0, # Bumped matches (path -> replace other path from same edge)
            "loner_count": 0 # Paths that have exhausted all options
        }
        self.run_propose()
        self.match()
        print(self.iter_data)
        if self.iter_data["proposal_count"] == 0:
            self.complete = True

    def run(self):
        while not self.complete:
            self.run_iteration()
