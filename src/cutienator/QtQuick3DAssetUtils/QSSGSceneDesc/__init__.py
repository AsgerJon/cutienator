"""
The namespace 'QSSGSceneDesc' of Qt, a package of 'cutienator.QtQuick3DAssetUtils':
what Qt writes inside it, under the names C++ has for it.

  from cutienator.QtQuick3DAssetUtils import QSSGSceneDesc
  QSSGSceneDesc.Animation

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
    'Animation',
    'Flag',
    'ListView',
    'NodeList',
    'Property',
    'Scene',
    'Node',
    'Camera',
    'Joint',
    'Light',
    'Material',
    'Mesh',
    'Model',
    'MorphTarget',
    'Skeleton',
    'Skin',
    'Texture',
    'TextureData',
    'PropertyCall',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from .._q_s_s_g_scene_desc__animation import Animation
  from .._q_s_s_g_scene_desc__flag import Flag
  from .._q_s_s_g_scene_desc__list_view import ListView
  from .._q_s_s_g_scene_desc__node_list import NodeList
  from .._q_s_s_g_scene_desc__property import Property
  from .._q_s_s_g_scene_desc__scene import Scene
  from .._q_s_s_g_scene_desc__node import Node
  from .._q_s_s_g_scene_desc__camera import Camera
  from .._q_s_s_g_scene_desc__joint import Joint
  from .._q_s_s_g_scene_desc__light import Light
  from .._q_s_s_g_scene_desc__material import Material
  from .._q_s_s_g_scene_desc__mesh import Mesh
  from .._q_s_s_g_scene_desc__model import Model
  from .._q_s_s_g_scene_desc__morph_target import MorphTarget
  from .._q_s_s_g_scene_desc__skeleton import Skeleton
  from .._q_s_s_g_scene_desc__skin import Skin
  from .._q_s_s_g_scene_desc__texture import Texture
  from .._q_s_s_g_scene_desc__texture_data import TextureData
  from .._q_s_s_g_scene_desc__property_call import PropertyCall
else:
  #  Where each class is: the file in the folder of the part
  #  that is brought in the first time the class is asked for.
  __class_files__ = {
      'Animation': '_q_s_s_g_scene_desc__animation',
      'Flag': '_q_s_s_g_scene_desc__flag',
      'ListView': '_q_s_s_g_scene_desc__list_view',
      'NodeList': '_q_s_s_g_scene_desc__node_list',
      'Property': '_q_s_s_g_scene_desc__property',
      'Scene': '_q_s_s_g_scene_desc__scene',
      'Node': '_q_s_s_g_scene_desc__node',
      'Camera': '_q_s_s_g_scene_desc__camera',
      'Joint': '_q_s_s_g_scene_desc__joint',
      'Light': '_q_s_s_g_scene_desc__light',
      'Material': '_q_s_s_g_scene_desc__material',
      'Mesh': '_q_s_s_g_scene_desc__mesh',
      'Model': '_q_s_s_g_scene_desc__model',
      'MorphTarget': '_q_s_s_g_scene_desc__morph_target',
      'Skeleton': '_q_s_s_g_scene_desc__skeleton',
      'Skin': '_q_s_s_g_scene_desc__skin',
      'Texture': '_q_s_s_g_scene_desc__texture',
      'TextureData': '_q_s_s_g_scene_desc__texture_data',
      'PropertyCall': '_q_s_s_g_scene_desc__property_call',
  }
  #  The namespaces right inside this one, each a package.
  __space_packages__ = ()


  def __getattr__(name: str) -> Any:
    """
    Brings in a class or a namespace of this namespace the first time it is
    asked for, as by 'QSSGSceneDesc.Animation'. Python calls this for a name
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
