"""
Core data models for VulnGenesis.

These models represent security-relevant components
that may be discovered during application analysis.
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import List


class ComponentType(str, Enum):
    """Types of components that can exist in an application."""

    API_ENDPOINT = "api_endpoint"
    FUNCTION = "function"
    DATABASE = "database"
    SERVICE = "service"
    EXTERNAL_INPUT = "external_input"
    SENSITIVE_OPERATION = "sensitive_operation"


@dataclass
class ApplicationComponent:
    """Represents a component discovered in an application."""

    id: str
    name: str
    component_type: ComponentType
    description: str = ""


@dataclass
class DataFlow:
    """
    Represents a relationship or potential flow
    between two application components.
    """

    source_id: str
    target_id: str
    description: str = ""


@dataclass
class SecurityFinding:
    """
    Represents a security-relevant observation.

    This does not automatically mean that a vulnerability
    has been confirmed.
    """

    title: str
    description: str
    affected_component_id: str
    confidence: float = 0.0
    evidence: List[str] = field(default_factory=list)
