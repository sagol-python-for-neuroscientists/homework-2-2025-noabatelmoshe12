from enum import Enum
from collections import namedtuple

Condition = Enum("Condition", ("CURE", "HEALTHY", "SICK", "DYING", "DEAD"))
Agent = namedtuple("Agent", ("name", "category"))

def meetup(agent_listing: tuple) -> list:
    def improve(condition):
        if condition == Condition.DYING:
            return Condition.SICK
        elif condition == Condition.SICK:
            return Condition.HEALTHY
        return condition

    def worsen(condition):
        if condition == Condition.SICK:
            return Condition.DYING
        elif condition == Condition.DYING:
            return Condition.DEAD
        return condition

    result_agents = []
    active_agents = []

    for agent in agent_listing:
        if agent.category in (Condition.HEALTHY, Condition.DEAD):
            result_agents.append(agent)
        else:
            active_agents.append(agent)

    i = 0
    while i < len(active_agents):
        a1 = active_agents[i]
        if i + 1 >= len(active_agents):
            # No pair, just one agent left
            result_agents.append(a1)
            break

        a2 = active_agents[i + 1]

        if a1.category == Condition.CURE and a2.category != Condition.CURE:
            result_agents.append(a1)
            result_agents.append(Agent(a2.name, improve(a2.category)))
        elif a2.category == Condition.CURE and a1.category != Condition.CURE:
            result_agents.append(Agent(a1.name, improve(a1.category)))
            result_agents.append(a2)
        elif a1.category == Condition.CURE and a2.category == Condition.CURE:
            result_agents.extend([a1, a2])
        else:
            result_agents.append(Agent(a1.name, worsen(a1.category)))
            result_agents.append(Agent(a2.name, worsen(a2.category)))

        i += 2

    return result_agents
