"""
The 'cutienator.QtQuickEffects' package provides the cute classes of the
part of Qt named QtQuickEffects, under the name PySide6 has for it.

  from cutienator.QtQuickEffects import QGfxSourceProxyME, QQuickMultiEffect

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
    'QGfxSourceProxyME',
    'QQuickMultiEffect',
    'QQuickMultiEffectPrivate',
    'QQuickRectangularShadow',
    'QQuickRectangularShadowPrivate',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ._q_gfx_source_proxy_m_e import QGfxSourceProxyME
  from ._q_quick_multi_effect import QQuickMultiEffect
  from ._q_quick_multi_effect_private import QQuickMultiEffectPrivate
  from ._q_quick_rectangular_shadow import QQuickRectangularShadow
  from ._q_quick_rectangular_shadow_private import QQuickRectangularShadowPrivate
else:
  #  Where each class is: the file that is brought in the first
  #  time the class is asked for.
  __class_files__ = {
      'QGfxSourceProxyME': '_q_gfx_source_proxy_m_e',
      'QQuickMultiEffect': '_q_quick_multi_effect',
      'QQuickMultiEffectPrivate': '_q_quick_multi_effect_private',
      'QQuickRectangularShadow': '_q_quick_rectangular_shadow',
      'QQuickRectangularShadowPrivate': '_q_quick_rectangular_shadow_private',
  }


  def __getattr__(name: str) -> Any:
    """
    Brings in a class of this part the first time it is asked for,
    as by 'from cutienator.QtQuickEffects import QQuickRectangularShadowPrivate'. Python calls
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
