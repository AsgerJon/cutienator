"""
The 'cutienator.QtWebEngineWidgets' package provides the cute classes of
the part of Qt named QtWebEngineWidgets, under the name PySide6 has for
it.

  from cutienator.QtWebEngineWidgets import DefaultNotificationPresenter, QWebEngineView

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
    'DefaultNotificationPresenter',
    'QWebEngineView',
    'QWebEngineViewAccessible',
    'QtWebEngineCore',
    'QtWebEngineWidgetUI',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ._default_notification_presenter import DefaultNotificationPresenter
  from ._q_web_engine_view import QWebEngineView
  from ._q_web_engine_view_accessible import QWebEngineViewAccessible
  from . import QtWebEngineCore
  from . import QtWebEngineWidgetUI
else:
  #  Where each class is: the file that is brought in the first
  #  time the class is asked for.
  __class_files__ = {
      'DefaultNotificationPresenter': '_default_notification_presenter',
      'QWebEngineView': '_q_web_engine_view',
      'QWebEngineViewAccessible': '_q_web_engine_view_accessible',
  }
  #  The namespaces of the part, each a package of its own.
  __space_packages__ = ('QtWebEngineCore', 'QtWebEngineWidgetUI',)


  def __getattr__(name: str) -> Any:
    """
    Brings in a class of this part the first time it is asked for,
    as by 'from cutienator.QtWebEngineWidgets import QWebEngineViewAccessible'. Python calls
    this for a name the package does not hold yet. The file of the
    class is brought in, which brings in the files that class needs
    and no others, and the class is kept here for the next time.

    Raises
    ------

    AttributeError
      The part has no class of that name.
    """
    if name in __space_packages__:
      value = importlib.import_module('.%s' % name, __name__)
      globals()[name] = value
      return value
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
