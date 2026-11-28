"""
The 'cutienator.QtQuickControls2BasicStyleImpl' package provides the
cute classes of the part of Qt named QtQuickControls2BasicStyleImpl,
under the name PySide6 has for it.

  from cutienator.QtQuickControls2BasicStyleImpl import QQuickBasicBusyIndicator, QQuickBasicProgressBar

A class is brought in the first time it is asked for, with the files it
needs and no others. So bringing in the package costs nothing, and a
program pays for the classes it uses.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import importlib
from typing import TYPE_CHECKING

__all__ = (
    'QQuickBasicBusyIndicator',
    'QQuickBasicProgressBar',
    'QQuickBasicDial',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ._q_quick_basic_busy_indicator import QQuickBasicBusyIndicator
  from ._q_quick_basic_progress_bar import QQuickBasicProgressBar
  from ._q_quick_basic_dial import QQuickBasicDial
else:
  #  Where each class is: the file that is brought in the first
  #  time the class is asked for.
  __class_files__ = {
      'QQuickBasicBusyIndicator': '_q_quick_basic_busy_indicator',
      'QQuickBasicProgressBar': '_q_quick_basic_progress_bar',
      'QQuickBasicDial': '_q_quick_basic_dial',
  }


  def __getattr__(name: str) -> Any:
    """
    Brings in a class of this part the first time it is asked for,
    as by 'from cutienator.QtQuickControls2BasicStyleImpl import QQuickBasicDial'. Python calls
    this for a name the package does not hold yet. The file of the
    class is brought in, which brings in the files that class needs
    and no others, and the class is kept here for the next time.

    Raises
    ------

    AttributeError
      The part has no class of that name.
    """
    try:
      fileName = __class_files__[name]
    except KeyError:
      infoSpec = """module '%s' has no attribute '%s'"""
      raise AttributeError(infoSpec % (__name__, name)) from None
    module = importlib.import_module('.%s' % fileName, __name__)
    value = getattr(module, name)
    globals()[name] = value
    return value


  def __dir__() -> List[str]:
    """Names every class of the part, brought in or not."""
    return [*__all__]
