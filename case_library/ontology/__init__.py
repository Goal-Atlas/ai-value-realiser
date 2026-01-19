"""AI Case Library Ontology"""
from pathlib import Path
import yaml

ONTOLOGY_DIR = Path(__file__).parent
CURRENT_VERSION = "1.0"

def load_ontology(version: str = CURRENT_VERSION) -> dict:
    """Load ontology definition from YAML file."""
    ontology_path = ONTOLOGY_DIR / f"ontology_v{version}.yaml"
    with open(ontology_path) as f:
        return yaml.safe_load(f)
