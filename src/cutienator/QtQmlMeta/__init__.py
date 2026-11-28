"""
The 'cutienator.QtQmlMeta' package provides the cute classes of the part
of Qt named QtQmlMeta, under the name PySide6 has for it.

  from cutienator.QtQmlMeta import QQmlMetaDependencies, QQmlConnections

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
    'QQmlMetaDependencies',
    'QQmlConnections',
    'QQmlTimer',
    'QQmlLoggingCategory',
    'QQmlBind',
    'QQmlConnectionsParser',
    'QQmlLocaleEnums',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ._q_qml_meta_dependencies import QQmlMetaDependencies
  from ._q_qml_connections import QQmlConnections
  from ._q_qml_timer import QQmlTimer
  from ._q_qml_logging_category import QQmlLoggingCategory
  from ._q_qml_bind import QQmlBind
  from ._q_qml_connections_parser import QQmlConnectionsParser
  from ._q_qml_locale_enums import QQmlLocaleEnums
else:
  #  Where each class is: the file that is brought in the first
  #  time the class is asked for.
  __class_files__ = {
      'QQmlMetaDependencies': '_q_qml_meta_dependencies',
      'QQmlConnections': '_q_qml_connections',
      'QQmlTimer': '_q_qml_timer',
      'QQmlLoggingCategory': '_q_qml_logging_category',
      'QQmlBind': '_q_qml_bind',
      'QQmlConnectionsParser': '_q_qml_connections_parser',
      'QQmlLocaleEnums': '_q_qml_locale_enums',
  }


  def __getattr__(name: str) -> Any:
    """
    Brings in a class of this part the first time it is asked for,
    as by 'from cutienator.QtQmlMeta import QQmlLocaleEnums'. Python calls
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
