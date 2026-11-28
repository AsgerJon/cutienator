"""
The namespace 'QtGraphicsAnchorLayout' of Qt, a package of 'cutienator.QtWidgets':
what Qt writes inside it, under the names C++ has for it.

  from cutienator.QtWidgets import QtGraphicsAnchorLayout
  QtGraphicsAnchorLayout.GraphPath

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
    'GraphPath',
    'AnchorData',
    'ParallelAnchorData',
    'SequentialAnchorData',
    'AnchorVertex',
    'AnchorVertexPair',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from .._qt_graphics_anchor_layout__graph_path import GraphPath
  from .._qt_graphics_anchor_layout__anchor_data import AnchorData
  from .._qt_graphics_anchor_layout__parallel_anchor_data import ParallelAnchorData
  from .._qt_graphics_anchor_layout__sequential_anchor_data import SequentialAnchorData
  from .._qt_graphics_anchor_layout__anchor_vertex import AnchorVertex
  from .._qt_graphics_anchor_layout__anchor_vertex_pair import AnchorVertexPair
else:
  #  Where each class is: the file in the folder of the part
  #  that is brought in the first time the class is asked for.
  __class_files__ = {
      'GraphPath': '_qt_graphics_anchor_layout__graph_path',
      'AnchorData': '_qt_graphics_anchor_layout__anchor_data',
      'ParallelAnchorData': '_qt_graphics_anchor_layout__parallel_anchor_data',
      'SequentialAnchorData': '_qt_graphics_anchor_layout__sequential_anchor_data',
      'AnchorVertex': '_qt_graphics_anchor_layout__anchor_vertex',
      'AnchorVertexPair': '_qt_graphics_anchor_layout__anchor_vertex_pair',
  }
  #  The namespaces right inside this one, each a package.
  __space_packages__ = ()


  def __getattr__(name: str) -> Any:
    """
    Brings in a class or a namespace of this namespace the first time it is
    asked for, as by 'QtGraphicsAnchorLayout.GraphPath'. Python calls this
    for a name the package does not hold yet, and what it gives is kept here
    for the next time.

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
