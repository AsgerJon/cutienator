"""
The namespace 'Qt3DRender::Render::Quick' of Qt, a package of 'cutienator.Qt3DQuickRender':
what Qt writes inside it, under the names C++ has for it.

  from cutienator.Qt3DQuickRender import Qt3DRender
  Qt3DRender.Render.Quick.Quick3DEffect

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
    'Quick3DEffect',
    'Quick3DLayerFilter',
    'Quick3DMaterial',
    'Quick3DMemoryBarrier',
    'Quick3DRenderPass',
    'Quick3DRenderPassFilter',
    'Quick3DRenderTargetOutput',
    'Quick3DScene',
    'Quick3DStateSet',
    'Quick3DTechnique',
    'Quick3DTechniqueFilter',
    'Quick3DTextureExtension',
    'Quick3DViewport',
    'Quick3DShaderDataArray',
    'Quick3DParameter',
    'Quick3DParameterPrivate',
    'Quick3DRayCasterPrivate',
    'Quick3DScreenRayCasterPrivate',
    'Quick3DShaderData',
    'Quick3DRayCaster',
    'Quick3DScreenRayCaster',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ...._qt3_d_render__render__quick__quick3_d_effect import Quick3DEffect
  from ...._qt3_d_render__render__quick__quick3_d_layer_filter import Quick3DLayerFilter
  from ...._qt3_d_render__render__quick__quick3_d_material import Quick3DMaterial
  from ...._qt3_d_render__render__quick__quick3_d_memory_barrier import Quick3DMemoryBarrier
  from ...._qt3_d_render__render__quick__quick3_d_render_pass import Quick3DRenderPass
  from ...._qt3_d_render__render__quick__quick3_d_render_pass_filter import Quick3DRenderPassFilter
  from ...._qt3_d_render__render__quick__quick3_d_render_target_output import Quick3DRenderTargetOutput
  from ...._qt3_d_render__render__quick__quick3_d_scene import Quick3DScene
  from ...._qt3_d_render__render__quick__quick3_d_state_set import Quick3DStateSet
  from ...._qt3_d_render__render__quick__quick3_d_technique import Quick3DTechnique
  from ...._qt3_d_render__render__quick__quick3_d_technique_filter import Quick3DTechniqueFilter
  from ...._qt3_d_render__render__quick__quick3_d_texture_extension import Quick3DTextureExtension
  from ...._qt3_d_render__render__quick__quick3_d_viewport import Quick3DViewport
  from ...._qt3_d_render__render__quick__quick3_d_shader_data_array import Quick3DShaderDataArray
  from ...._qt3_d_render__render__quick__quick3_d_parameter import Quick3DParameter
  from ...._qt3_d_render__render__quick__quick3_d_parameter_private import Quick3DParameterPrivate
  from ...._qt3_d_render__render__quick__quick3_d_ray_caster_private import Quick3DRayCasterPrivate
  from ...._qt3_d_render__render__quick__quick3_d_screen_ray_caster_private import Quick3DScreenRayCasterPrivate
  from ...._qt3_d_render__render__quick__quick3_d_shader_data import Quick3DShaderData
  from ...._qt3_d_render__render__quick__quick3_d_ray_caster import Quick3DRayCaster
  from ...._qt3_d_render__render__quick__quick3_d_screen_ray_caster import Quick3DScreenRayCaster
else:
  #  Where each class is: the file in the folder of the part
  #  that is brought in the first time the class is asked for.
  __class_files__ = {
      'Quick3DEffect': '_qt3_d_render__render__quick__quick3_d_effect',
      'Quick3DLayerFilter': '_qt3_d_render__render__quick__quick3_d_layer_filter',
      'Quick3DMaterial': '_qt3_d_render__render__quick__quick3_d_material',
      'Quick3DMemoryBarrier': '_qt3_d_render__render__quick__quick3_d_memory_barrier',
      'Quick3DRenderPass': '_qt3_d_render__render__quick__quick3_d_render_pass',
      'Quick3DRenderPassFilter': '_qt3_d_render__render__quick__quick3_d_render_pass_filter',
      'Quick3DRenderTargetOutput': '_qt3_d_render__render__quick__quick3_d_render_target_output',
      'Quick3DScene': '_qt3_d_render__render__quick__quick3_d_scene',
      'Quick3DStateSet': '_qt3_d_render__render__quick__quick3_d_state_set',
      'Quick3DTechnique': '_qt3_d_render__render__quick__quick3_d_technique',
      'Quick3DTechniqueFilter': '_qt3_d_render__render__quick__quick3_d_technique_filter',
      'Quick3DTextureExtension': '_qt3_d_render__render__quick__quick3_d_texture_extension',
      'Quick3DViewport': '_qt3_d_render__render__quick__quick3_d_viewport',
      'Quick3DShaderDataArray': '_qt3_d_render__render__quick__quick3_d_shader_data_array',
      'Quick3DParameter': '_qt3_d_render__render__quick__quick3_d_parameter',
      'Quick3DParameterPrivate': '_qt3_d_render__render__quick__quick3_d_parameter_private',
      'Quick3DRayCasterPrivate': '_qt3_d_render__render__quick__quick3_d_ray_caster_private',
      'Quick3DScreenRayCasterPrivate': '_qt3_d_render__render__quick__quick3_d_screen_ray_caster_private',
      'Quick3DShaderData': '_qt3_d_render__render__quick__quick3_d_shader_data',
      'Quick3DRayCaster': '_qt3_d_render__render__quick__quick3_d_ray_caster',
      'Quick3DScreenRayCaster': '_qt3_d_render__render__quick__quick3_d_screen_ray_caster',
  }
  #  The namespaces right inside this one, each a package.
  __space_packages__ = ()


  def __getattr__(name: str) -> Any:
    """
    Brings in a class or a namespace of this namespace the first time it is
    asked for, as by 'Qt3DRender.Render.Quick.Quick3DEffect'. Python calls
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
      module = importlib.import_module('....%s' % fileName, __name__)
      value = getattr(module, name)
    globals()[name] = value
    return value


  def __dir__() -> List[str]:
    """Names everything of the namespace, brought in or not."""
    return [*__all__]
