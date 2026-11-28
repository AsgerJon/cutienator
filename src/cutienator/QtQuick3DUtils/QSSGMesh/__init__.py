"""
The namespace 'QSSGMesh' of Qt, a package of 'cutienator.QtQuick3DUtils':
what Qt writes inside it, under the names C++ has for it.

  from cutienator.QtQuick3DUtils import QSSGMesh
  QSSGMesh.AssetMeshSubset

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
    'AssetMeshSubset',
    'AssetVertexEntry',
    'MeshVertexStream',
    'RuntimeMeshData',
    'MeshInternal',
    'Mesh',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from .._q_s_s_g_mesh__asset_mesh_subset import AssetMeshSubset
  from .._q_s_s_g_mesh__asset_vertex_entry import AssetVertexEntry
  from .._q_s_s_g_mesh__mesh_vertex_stream import MeshVertexStream
  from .._q_s_s_g_mesh__runtime_mesh_data import RuntimeMeshData
  from .._q_s_s_g_mesh__mesh_internal import MeshInternal
  from .._q_s_s_g_mesh__mesh import Mesh
else:
  #  Where each class is: the file in the folder of the part
  #  that is brought in the first time the class is asked for.
  __class_files__ = {
      'AssetMeshSubset': '_q_s_s_g_mesh__asset_mesh_subset',
      'AssetVertexEntry': '_q_s_s_g_mesh__asset_vertex_entry',
      'MeshVertexStream': '_q_s_s_g_mesh__mesh_vertex_stream',
      'RuntimeMeshData': '_q_s_s_g_mesh__runtime_mesh_data',
      'MeshInternal': '_q_s_s_g_mesh__mesh_internal',
      'Mesh': '_q_s_s_g_mesh__mesh',
  }
  #  The namespaces right inside this one, each a package.
  __space_packages__ = ()


  def __getattr__(name: str) -> Any:
    """
    Brings in a class or a namespace of this namespace the first time it is
    asked for, as by 'QSSGMesh.AssetMeshSubset'. Python calls this for a name
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
