"""
The `html5plus` package provides a set of tools and utilities for processing and enhancing HTML content.

The main components of the package include:

- `HTMLProcessor`: A class responsible for parsing and processing HTML documents.
- `HTMLProcessorConductor`: A class that orchestrates the HTML processing workflow.
- `ProjectManager`: A class that manages the project-level configuration and settings.

The package also includes a set of common utility functions and modules, as well as a plugin system for extending the functionality.

Users can import the main classes and functions from the package-level, e.g.:

```python
from html5plus import HTMLProcessor, HTMLProcessorConductor, ProjectManager
Refer to the individual module and class docstrings for more detailed information on the available functionality.
"""

import logging

from .htmlprocessor import HTMLProcessor
from .htmlprocessorconductor import HTMLProcessorConductor
from .projectmanager import ProjectManager

from .common import *
from .plugins import *

all = ['HTMLProcessor', 'HTMLProcessorConductor', 'ProjectManager']

