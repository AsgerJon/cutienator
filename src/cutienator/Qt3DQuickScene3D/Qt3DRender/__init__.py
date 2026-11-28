"""
The namespace 'Qt3DRender' of Qt, a package of 'cutienator.Qt3DQuickScene3D':
what Qt writes inside it, under the names C++ has for it.

  from cutienator.Qt3DQuickScene3D import Qt3DRender
  Qt3DRender.Scene3DItem

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
    'Scene3DItem',
    'Scene3DRenderer',
    'Scene3DSGMaterial',
    'Scene3DSGMaterialShader',
    'Scene3DSGNode',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from .._qt3_d_render__scene3_d_item import Scene3DItem
  from .._qt3_d_render__scene3_d_renderer import Scene3DRenderer
  from .._qt3_d_render__scene3_d_s_g_material import Scene3DSGMaterial
  from .._qt3_d_render__scene3_d_s_g_material_shader import Scene3DSGMaterialShader
  from .._qt3_d_render__scene3_d_s_g_node import Scene3DSGNode
else:
  #  Where each class is: the file in the folder of the part
  #  that is brought in the first time the class is asked for.
  __class_files__ = {
      'Scene3DItem': '_qt3_d_render__scene3_d_item',
      'Scene3DRenderer': '_qt3_d_render__scene3_d_renderer',
      'Scene3DSGMaterial': '_qt3_d_render__scene3_d_s_g_material',
      'Scene3DSGMaterialShader': '_qt3_d_render__scene3_d_s_g_material_shader',
      'Scene3DSGNode': '_qt3_d_render__scene3_d_s_g_node',
  }
  #  The namespaces right inside this one, each a package.
  __space_packages__ = ()


  def __getattr__(name: str) -> Any:
    """
    Brings in a class or a namespace of this namespace the first time it is
    asked for, as by 'Qt3DRender.Scene3DItem'. Python calls this for a name
    the package does not hold yet, and what it gives is kept here for the
    next time.

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
      module = importlib.import_module('..%s' % fileName, __name__)
      value = getattr(module, name)
    globals()[name] = value
    return value


  def __dir__() -> List[str]:
    """Names everything of the namespace, brought in or not."""
    return [*__all__]
