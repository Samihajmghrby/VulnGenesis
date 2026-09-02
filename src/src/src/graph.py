"""
Application graph engine for VulnGenesis.

Builds a simple directed graph representing relationships
and potential data flows between application components.
"""

from collections import defaultdict
from typing import Dict, List, Set

from models import ApplicationComponent, DataFlow


class ApplicationGraph:
    """Represents application components and their relationships."""

    def __init__(self):
        self.components: Dict[str, ApplicationComponent] = {}
        self.edges: Dict[str, List[str]] = defaultdict(list)

    def add_component(self, component: ApplicationComponent) -> None:
        """Add an application component to the graph."""
        self.components[component.id] = component

    def add_data_flow(self, flow: DataFlow) -> None:
        """Add a directed relationship between two components."""
        if flow.source_id not in self.components:
            raise ValueError(
                f"Source component '{flow.source_id}' does not exist."
            )

        if flow.target_id not in self.components:
            raise ValueError(
                f"Target component '{flow.target_id}' does not exist."
            )

        self.edges[flow.source_id].append(flow.target_id)

    def get_neighbors(self, component_id: str) -> List[str]:
        """Return directly connected components."""
        return self.edges.get(component_id, [])

    def find_paths(
        self,
        start_id: str,
        end_id: str,
    ) -> List[List[str]]:
        """
        Find possible paths between two components using DFS.

        Intended for small research models during the project's
        early development phase.
        """

        paths: List[List[str]] = []

        def dfs(
            current: str,
            target: str,
            path: List[str],
            visited: Set[str],
        ) -> None:
            if current == target:
                paths.append(path.copy())
                return

            for neighbor in self.get_neighbors(current):
                if neighbor not in visited:
                    visited.add(neighbor)
                    path.append(neighbor)

                    dfs(neighbor, target, path, visited)

                    path.pop()
                    visited.remove(neighbor)

        if start_id not in self.components:
            raise ValueError(f"Component '{start_id}' does not exist.")

        if end_id not in self.components:
            raise ValueError(f"Component '{end_id}' does not exist.")

        dfs(start_id, end_id, [start_id], {start_id})

        return paths
