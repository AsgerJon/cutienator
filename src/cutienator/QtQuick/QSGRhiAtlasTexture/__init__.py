"""
The namespace 'QSGRhiAtlasTexture' of Qt, a package of 'cutienator.QtQuick':
what Qt writes inside it, under the names C++ has for it.

  from cutienator.QtQuick import QSGRhiAtlasTexture
  QSGRhiAtlasTexture.TextureBase

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
    'TextureBase',
    'Texture',
    'AtlasBase',
    'Manager',
    'Atlas',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from .._q_s_g_rhi_atlas_texture__texture_base import TextureBase
  from .._q_s_g_rhi_atlas_texture__texture import Texture
  from .._q_s_g_rhi_atlas_texture__atlas_base import AtlasBase
  from .._q_s_g_rhi_atlas_texture__manager import Manager
  from .._q_s_g_rhi_atlas_texture__atlas import Atlas
else:
  #  Where each class is: the file in the folder of the part
  #  that is brought in the first time the class is asked for.
  __class_files__ = {
      'TextureBase': '_q_s_g_rhi_atlas_texture__texture_base',
      'Texture': '_q_s_g_rhi_atlas_texture__texture',
      'AtlasBase': '_q_s_g_rhi_atlas_texture__atlas_base',
      'Manager': '_q_s_g_rhi_atlas_texture__manager',
      'Atlas': '_q_s_g_rhi_atlas_texture__atlas',
  }
  #  The namespaces right inside this one, each a package.
  __space_packages__ = ()


  def __getattr__(name: str) -> Any:
    """
    Brings in a class or a namespace of this namespace the first time it is
    asked for, as by 'QSGRhiAtlasTexture.TextureBase'. Python calls this for
    a name the package does not hold yet, and what it gives is kept here for
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
      module = importlib.import_module('..%s' % fileName, __name__)
      value = getattr(module, name)
    globals()[name] = value
    return value


  def __dir__() -> List[str]:
    """Names everything of the namespace, brought in or not."""
    return [*__all__]
