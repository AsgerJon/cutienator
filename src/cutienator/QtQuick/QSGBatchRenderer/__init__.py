"""
The namespace 'QSGBatchRenderer' of Qt, a package of 'cutienator.QtQuick':
what Qt writes inside it, under the names C++ has for it.

  from cutienator.QtQuick import QSGBatchRenderer
  QSGBatchRenderer.BatchRootInfo

A class is brought in the first time it is asked for.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.PackageGenerator. Changes made here are
#  lost.
from __future__ import annotations

import importlib
from typing import TYPE_CHECKING

from .._q_s_g_batch_renderer import QSGBatchRenderer as _Enums

#  The enums of the namespace, and the names of their
#  members, as names of the package itself, where C++ has
#  them: 'Qt.AlignLeft'.
globals().update({
    name: value for name, value in _Enums.__dict__.items()
    if not name.startswith('_')})

__all__ = (
    'BatchRootInfo',
    'Buffer',
    'ClipState',
    'DrawSet',
    'GraphicsState',
    'Node',
    'RenderPassState',
    'ShaderKey',
    'ShaderManagerShader',
    'StencilClipState',
    'Visualizer',
    'ClipBatchRootInfo',
    'Pt',
    'Rect',
    'GraphicsPipelineStateKey',
    'RhiVisualizer',
    'Batch',
    'Element',
    'RenderNodeElement',
    'Updater',
    'Renderer',
    'ShaderManager',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from .._q_s_g_batch_renderer__batch_root_info import BatchRootInfo
  from .._q_s_g_batch_renderer__buffer import Buffer
  from .._q_s_g_batch_renderer__clip_state import ClipState
  from .._q_s_g_batch_renderer__draw_set import DrawSet
  from .._q_s_g_batch_renderer__graphics_state import GraphicsState
  from .._q_s_g_batch_renderer__node import Node
  from .._q_s_g_batch_renderer__render_pass_state import RenderPassState
  from .._q_s_g_batch_renderer__shader_key import ShaderKey
  from .._q_s_g_batch_renderer__shader_manager_shader import ShaderManagerShader
  from .._q_s_g_batch_renderer__stencil_clip_state import StencilClipState
  from .._q_s_g_batch_renderer__visualizer import Visualizer
  from .._q_s_g_batch_renderer__clip_batch_root_info import ClipBatchRootInfo
  from .._q_s_g_batch_renderer__pt import Pt
  from .._q_s_g_batch_renderer__rect import Rect
  from .._q_s_g_batch_renderer__graphics_pipeline_state_key import GraphicsPipelineStateKey
  from .._q_s_g_batch_renderer__rhi_visualizer import RhiVisualizer
  from .._q_s_g_batch_renderer__batch import Batch
  from .._q_s_g_batch_renderer__element import Element
  from .._q_s_g_batch_renderer__render_node_element import RenderNodeElement
  from .._q_s_g_batch_renderer__updater import Updater
  from .._q_s_g_batch_renderer__renderer import Renderer
  from .._q_s_g_batch_renderer__shader_manager import ShaderManager
else:
  #  Where each class is: the file in the folder of the part
  #  that is brought in the first time the class is asked for.
  __class_files__ = {
      'BatchRootInfo': '_q_s_g_batch_renderer__batch_root_info',
      'Buffer': '_q_s_g_batch_renderer__buffer',
      'ClipState': '_q_s_g_batch_renderer__clip_state',
      'DrawSet': '_q_s_g_batch_renderer__draw_set',
      'GraphicsState': '_q_s_g_batch_renderer__graphics_state',
      'Node': '_q_s_g_batch_renderer__node',
      'RenderPassState': '_q_s_g_batch_renderer__render_pass_state',
      'ShaderKey': '_q_s_g_batch_renderer__shader_key',
      'ShaderManagerShader': '_q_s_g_batch_renderer__shader_manager_shader',
      'StencilClipState': '_q_s_g_batch_renderer__stencil_clip_state',
      'Visualizer': '_q_s_g_batch_renderer__visualizer',
      'ClipBatchRootInfo': '_q_s_g_batch_renderer__clip_batch_root_info',
      'Pt': '_q_s_g_batch_renderer__pt',
      'Rect': '_q_s_g_batch_renderer__rect',
      'GraphicsPipelineStateKey': '_q_s_g_batch_renderer__graphics_pipeline_state_key',
      'RhiVisualizer': '_q_s_g_batch_renderer__rhi_visualizer',
      'Batch': '_q_s_g_batch_renderer__batch',
      'Element': '_q_s_g_batch_renderer__element',
      'RenderNodeElement': '_q_s_g_batch_renderer__render_node_element',
      'Updater': '_q_s_g_batch_renderer__updater',
      'Renderer': '_q_s_g_batch_renderer__renderer',
      'ShaderManager': '_q_s_g_batch_renderer__shader_manager',
  }
  #  The namespaces right inside this one, each a package.
  __space_packages__ = ()


  def __getattr__(name: str) -> Any:
    """
    Brings in a class or a namespace of this namespace the first time it is
    asked for, as by 'QSGBatchRenderer.BatchRootInfo'. Python calls this for
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
    return [*__all__, *(
        name for name in _Enums.__dict__ if not name.startswith('_'))]
