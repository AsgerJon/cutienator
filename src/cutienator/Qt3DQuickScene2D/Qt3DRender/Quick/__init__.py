"""
The namespace 'Qt3DRender::Quick' of Qt, a package of 'cutienator.Qt3DQuickScene2D':
what Qt writes inside it, under the names C++ has for it.

  from cutienator.Qt3DQuickScene2D import Qt3DRender
  Qt3DRender.Quick.QScene2DData

A class is brought in the first time it is asked for.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.PackageGenerator. Changes made here are
#  lost.
from __future__ import annotations

import importlib
from typing import TYPE_CHECKING

__all__ = (
    'QScene2DData',
    'Scene2DSharedObject',
    'QScene2dForeign',
    'Scene2DEvent',
    'QScene2DPrivate',
    'QScene2D',
    'Scene2DManager',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ..._qt3_d_render__quick__q_scene2_d_data import QScene2DData
  from ..._qt3_d_render__quick__scene2_d_shared_object import Scene2DSharedObject
  from ..._qt3_d_render__quick__q_scene2d_foreign import QScene2dForeign
  from ..._qt3_d_render__quick__scene2_d_event import Scene2DEvent
  from ..._qt3_d_render__quick__q_scene2_d_private import QScene2DPrivate
  from ..._qt3_d_render__quick__q_scene2_d import QScene2D
  from ..._qt3_d_render__quick__scene2_d_manager import Scene2DManager
else:
  #  Where each class is: the file in the folder of the part
  #  that is brought in the first time the class is asked for.
  __class_files__ = {
      'QScene2DData': '_qt3_d_render__quick__q_scene2_d_data',
      'Scene2DSharedObject': '_qt3_d_render__quick__scene2_d_shared_object',
      'QScene2dForeign': '_qt3_d_render__quick__q_scene2d_foreign',
      'Scene2DEvent': '_qt3_d_render__quick__scene2_d_event',
      'QScene2DPrivate': '_qt3_d_render__quick__q_scene2_d_private',
      'QScene2D': '_qt3_d_render__quick__q_scene2_d',
      'Scene2DManager': '_qt3_d_render__quick__scene2_d_manager',
  }
  #  The namespaces right inside this one, each a package.
  __space_packages__ = ()


  def __getattr__(name: str) -> Any:
    """
    Brings in a class or a namespace of this namespace the first time it is
    asked for, as by 'Qt3DRender.Quick.QScene2DData'. Python calls this for a
    name the package does not hold yet, and what it gives is kept here for
    the next time.

    Raises
    ------

    AttributeError
      The namespace has nothing of that name.
    """
    if name in __space_packages__:
      value = importlib.import_module('.%s' % name, __name__)
    else:
      try:
        fileName = __class_files__[name]
      except KeyError:
        infoSpec = """module '%s' has no attribute '%s'"""
        raise AttributeError(infoSpec % (__name__, name)) from None
      module = importlib.import_module('...%s' % fileName, __name__)
      value = getattr(module, name)
    globals()[name] = value
    return value


  def __dir__() -> List[str]:
    """Names everything of the namespace, brought in or not."""
    return [*__all__]
