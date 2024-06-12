from warnings import warn

from st7789 import *  # noqa F403

warn(
    'Using "import ST7789" is deprecated. Please "import st7789" (all lowercase)!',
    DeprecationWarning,
    stacklevel=2,
)
