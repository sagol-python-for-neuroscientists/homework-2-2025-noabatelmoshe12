from enum import Enum
from collections import namedtuple
from itertools import zip_longest

# Enum for agent conditions
Condition = Enum("Condition", ["CURE", "HEALTHY", "SICK", "DYING", "DEAD"])


# Named tuple for an Agent
Agent = namedtuple("Agent", ("name", "category"))

def interact(agent1, agent2):
    """Apply interaction rules between two agents."""
    if agent1.category == Condition.CURE:
        if agent2.category == Condition.SICK:
            return agent1, Agent(agent2.name, Condition.HEALTHY)
        elif agent2.category == Condition.DYING:
            return agent1, Agent(agent2.name, Condition.SICK)
        else:
            return agent1, agent2
    if agent2.category == Condition.CURE:
        if agent1.category == Condition.SICK:
            return Agent(agent1.name, Condition.HEALTHY), agent2
        elif agent1.category == Condition.DYING:
            return Agent(agent1.name, Condition.SICK), agent2
        else:
            return agent1, agent2

    if agent1.category == Condition.SICK and agent2.category == Condition.DYING:
        return Agent(agent1.name, Condition.DYING), Agent(agent2.name, Condition.DEAD)
    elif agent1.category == Condition.DYING and agent2.category == Condition.SICK:
        return Agent(agent1.name, Condition.DEAD), Agent(agent2.name, Condition.DYING)
    elif agent1.category == Condition.DYING and agent2.category == Condition.DYING:
        return Agent(agent1.name, Condition.DEAD), Agent(agent2.name, Condition.DEAD)

    return agent1, agent2

def meetup(agent_listing: tuple) -> list:
    """Model the outcome of the meetings of pairs of agents."""
    filtered_agents = [agent for agent in agent_listing if agent.category not in {Condition.HEALTHY, Condition.DEAD}]

    updated_agents = []
    for agent1, agent2 in zip_longest(filtered_agents[::2], filtered_agents[1::2], fillvalue=None):
        if agent2 is None:
            updated_agents.append(agent1)
        else:
            updated_agents.append(interact(agent1, agent2))

    flattened_agents = [agent for pair in updated_agents for agent in (pair if isinstance(pair, tuple) else (pair,))]

    return flattened_agents

if __name__ == '__main__':
    # Question 2
    agents = (
        Agent("A", Condition.CURE),
        Agent("B", Condition.SICK),
        Agent("C", Condition.DYING),
        Agent("D", Condition.HEALTHY),
        Agent("E", Condition.SICK),
        Agent("F", Condition.DYING),
    )
    result = meetup(agents)
    print(f"Question 2 solution: {result}")
