"""
VulnGenesis
AI-Assisted Security Hypothesis Generation
for Contextual Vulnerability Discovery.

Demo entry point for the early VulnGenesis prototype.
"""

from graph import ApplicationGraph
from models import (
    ApplicationComponent,
    ComponentType,
    DataFlow,
)


def build_demo_application() -> ApplicationGraph:
    """Build a small authorized demo application model."""

    graph = ApplicationGraph()

    components = [
        ApplicationComponent(
            id="user_input",
            name="User Input",
            component_type=ComponentType.EXTERNAL_INPUT,
            description="Authorized demo input source.",
        ),
        ApplicationComponent(
            id="api",
            name="API Endpoint",
            component_type=ComponentType.API_ENDPOINT,
            description="Demo application API endpoint.",
        ),
        ApplicationComponent(
            id="processor",
            name="Input Processor",
            component_type=ComponentType.FUNCTION,
            description="Demo processing function.",
        ),
        ApplicationComponent(
            id="sensitive_operation",
            name="Sensitive Operation",
            component_type=ComponentType.SENSITIVE_OPERATION,
            description="Demo security-relevant operation.",
        ),
    ]

    for component in components:
        graph.add_component(component)

    flows = [
        DataFlow(
            source_id="user_input",
            target_id="api",
            description="Input reaches the API.",
        ),
        DataFlow(
            source_id="api",
            target_id="processor",
            description="API forwards input for processing.",
        ),
        DataFlow(
            source_id="processor",
            target_id="sensitive_operation",
            description="Processed data reaches a sensitive operation.",
        ),
    ]

    for flow in flows:
        graph.add_data_flow(flow)

    return graph


def main():
    print("=" * 60)
    print("VulnGenesis")
    print("Contextual Security Research Prototype")
    print("=" * 60)

    graph = build_demo_application()

    paths = graph.find_paths(
        start_id="user_input",
        end_id="sensitive_operation",
    )

    print("\nPotential application paths:\n")

    for index, path in enumerate(paths, start=1):
        component_names = [
            graph.components[component_id].name
            for component_id in path
        ]

        print(f"Path {index}:")
        print("  " + " -> ".join(component_names))

    print(
        "\nNote: This prototype models application relationships "
        "for authorized security research only."
    )


if __name__ == "__main__":
    main()
