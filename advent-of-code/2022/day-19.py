# Modules
import re
import math


# Import Data
with open("day-19.txt", 'r') as file:
    blueprints = file.readlines()


# Classes and Functions
class Factory:
    def __init__(self, blueprints) -> None:
        self.blueprints = blueprints
        self.quality_level = 0
    
    def calc_num_geodes_opened(self, blueprint, time):
        """Calculate the number of geodes that can be opened using BFS

        Args:
            blueprint (list): a single blueprint from the puzzle input
            time (int): the remaining time to open geodes

        Returns:
            int: the maximum number of geodes that can be opened for that blueprint
        """
        max_geodes_opened = 0
        
        costs = list(map(int, re.findall(r"\d+", blueprint)))
        robot_costs = (
            # Resource costs for building each robot
            # ( Ore, Clay, Obsidian, Geode )
            (costs[1], 0, 0, 0),
            (costs[2], 0, 0, 0),
            (costs[3], costs[4], 0, 0),
            (costs[5], 0, costs[6], 0)
        )
        
        visited = set()
        queue = list()
        queue.append(
            # ( time remaining, resource counts, robot counts )
            # ( time remaining, (Ore, Clay, Obsidian, Geode), (Ore Robot, Clay Robot, Obsidian Robot, Geode Robot) )
            (time, (0, 0, 0, 0), (1, 0, 0, 0))
        )
        
        # The maximum amount of each resource that could be spent in one turn
        max_spend = [max(cost[i] for cost in robot_costs) for i in range(4)]
        
        # Breadth First Search
        while len(queue) > 0:
            time, resources, robots = queue.pop()
            
            ##> How many geodes can the current number of Geode Robots create in remaining time?
            geodes_can_create = resources[3] + (time * robots[3])
            
            if geodes_can_create > max_geodes_opened:
                max_geodes_opened = geodes_can_create
            
            ##> Skip if time is up or we have searched this combination before
            if time == 0 or (time, resources, robots) in visited:
                continue
            
            ##> Add this visited combination so it can be skipped later
            visited.add((time, resources, robots))
            
            ##> For each resource (Ore, Clay, Obsidian, Geode)
            for resource in range(4):
                ###> Will ALWAYS want to make more Geode Robots
                ###> We do not want too many robots for a single resource
                ###> If we already are producing more resources than we can spend in a single turn, then skip
                if resource != 3 and robots[resource] >= max_spend[resource]:
                    continue
                
                ###> Check if we have enough robots creating enough resources to build the next robot
                if any(robots[i] == 0 for i, cost in enumerate(robot_costs[resource]) if cost > 0):
                    continue
                
                ###> If we have enough robots to create the resources we need, how long will it take for them to create enough resources?
                ###> (cost - resources[i]) = how many additional resources do we need before we can keep going?
                ###> (cost - resources[i]) / robots[i] = how many additional turns the robots will need to make those additional resources
                ###> Append the list with 0 so that the maxium never goes negative
                wait = max(
                    [math.ceil((cost - resources[i]) / robots[i]) for i, cost in enumerate(robot_costs[resource]) if cost > 0] + [0]
                )
                
                ###> If we do not have enough time to wait, continue on to the next resource
                if time < wait:
                    continue
                
                ###> Use Robots to create more of the resource
                next_resource = [resources[i] + (robots[i] * (wait + 1)) - robot_costs[resource][i] for i in range(4)]
                
                ###> Create new robot
                next_robots = list(robots)
                next_robots[resource] += 1
                
                queue.append((time - wait - 1, tuple(next_resource), tuple(next_robots)))
                
        return max_geodes_opened
    
    
    def solve_part1(self, time):
        """Solve Part 1 by calculating the quality level

        Args:
            time (int): the time remaining to open geodes
        """
        for id, blueprint in enumerate(self.blueprints):
            blueprint_id = id + 1
            max_geodes = self.calc_num_geodes_opened(blueprint, time)
            
            self.quality_level += blueprint_id * max_geodes
            

# Question 1
factory = Factory(blueprints)
factory.solve_part1(24)

print(f"Answer 1: {factory.quality_level}")
