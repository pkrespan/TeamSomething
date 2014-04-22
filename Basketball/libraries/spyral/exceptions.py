"""
This module defines custom exceptions that are thrown throughout spyral.
"""

import warnings

class SceneHasNoSizeError(Exception):
    pass
class NotStylableError(Exception):
    pass
class NoImageError(Exception):
    pass
class BackgroundSizeError(Exception):
    pass
class LayersAlreadySetError(Exception):
    pass

# Warnings
class UnusedStyleWarning(Warning):
    pass


# Convenience Wrappers
def unused_style_warning(obj, properties):
    warnings.warn("%r does not understand style properties %s" %
                  (obj, ','.join(properties)),
                  UnusedStyleWarning)
