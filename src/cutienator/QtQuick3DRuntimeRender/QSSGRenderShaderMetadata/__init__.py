"""
The namespace 'QSSGRenderShaderMetadata' of Qt, a package of 'cutienator.QtQuick3DRuntimeRender':
what Qt writes inside it, under the names C++ has for it.

  from cutienator.QtQuick3DRuntimeRender import QSSGRenderShaderMetadata
  QSSGRenderShaderMetadata.ShaderMetaData

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
    'ShaderMetaData',
    'InputOutput',
    'Uniform',
    'Image',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from .._q_s_s_g_render_shader_metadata__shader_meta_data import ShaderMetaData
  from .._q_s_s_g_render_shader_metadata__input_output import InputOutput
  from .._q_s_s_g_render_shader_metadata__uniform import Uniform
  from .._q_s_s_g_render_shader_metadata__image import Image
else:
  #  Where each class is: the file in the folder of the part
  #  that is brought in the first time the class is asked for.
  __class_files__ = {
      'ShaderMetaData': '_q_s_s_g_render_shader_metadata__shader_meta_data',
      'InputOutput': '_q_s_s_g_render_shader_metadata__input_output',
      'Uniform': '_q_s_s_g_render_shader_metadata__uniform',
      'Image': '_q_s_s_g_render_shader_metadata__image',
  }
  #  The namespaces right inside this one, each a package.
  __space_packages__ = ()


  def __getattr__(name: str) -> Any:
    """
    Brings in a class or a namespace of this namespace the first time it is
    asked for, as by 'QSSGRenderShaderMetadata.ShaderMetaData'. Python calls
    this for a name the package does not hold yet, and what it gives is kept
    here for the next time.

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
