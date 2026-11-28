"""
QSSGMesh::Mesh binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qssgmesh_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QSSGMesh::Mesh to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QSSGMesh

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QIODevice, QString
  from ..QtGui import QMatrix4x4
  from . import QSSGRenderVertexBufferEntry
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QIODevice = WAIT['QIODevice']
  QMatrix4x4 = WAIT['QMatrix4x4']
  QString = WAIT['QString']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Mesh(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSSGMesh::Mesh: a plain Python object standing in
  front of one C++ QSSGMesh::Mesh.

  C++ hands a QSSGMesh::Mesh around as a copy, so every C++ QSSGMesh::Mesh
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSSGMesh::Mesh that has a ritual and that Python can
  call so far, 9 names in all: 'vertexBuffer', 'indexBuffer', 'targetBuffer',
  'loadMesh', 'fromRuntimeData', 'isValid', 'save', 'hasLightmapUVChannel',
  'createLightmapUVChannel'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QVector<Subset> QSSGMesh::Mesh::subsets() const': gives a type
    Python has no way to take yet.
  - Qt's 'QMap<quint32, Mesh> QSSGMesh::Mesh::loadAll(QIODevice *device)':
    gives a type Python has no way to take yet.
  - Qt's 'Mesh QSSGMesh::Mesh::fromAssetData(const QVector<AssetVertexEntry>
    &vbufEntries, const QByteArray &indexBufferData, ComponentType
    indexComponentType, const QVector<AssetMeshSubset> &subsets, quint32
    numTargets, quint32 numTargetComps)': takes a type Python has no way to
    hand over yet.
  - Qt's 'DrawMode QSSGMesh::Mesh::drawMode() const': gives the enum
    'QSSGRenderDrawMode', whose class cannot be named here.
  - Qt's 'Winding QSSGMesh::Mesh::winding() const': gives the enum
    'QSSGRenderWinding', whose class cannot be named here.
  - Qt's 'QSSGMesh::Mesh::~Mesh()': the destructor: Python removes its C++
    QSSGMesh::Mesh by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QSSGMesh::Mesh is created at the first use, not by
    'QSSGMesh::Mesh(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSSGMesh::Mesh back gives a copy the ritual made for
    Python, in a new cute QSSGMesh::Mesh.
  - Each name of Qt's QSSGMesh::Mesh that has no cute function yet,
    'drawMode', 'fromAssetData', 'loadAll', 'subsets', 'winding', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  #  The classes Qt writes inside QSSGMesh::Mesh, each a class in here as in
  #  C++.

  class IndexBuffer(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QSSGMesh::Mesh::IndexBuffer: a plain Python object
    standing in front of one C++ QSSGMesh::Mesh::IndexBuffer.

    C++ hands a QSSGMesh::Mesh::IndexBuffer around as a copy, so every C++
    QSSGMesh::Mesh::IndexBuffer behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    No function of Qt's QSSGMesh::Mesh::IndexBuffer yet. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QSSGMesh::Mesh::IndexBuffer::~IndexBuffer()': the destructor:
      Python removes its C++ QSSGMesh::Mesh::IndexBuffer by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QSSGMesh::Mesh::IndexBuffer is created at the first use, not by
      'QSSGMesh::Mesh::IndexBuffer(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QSSGMesh::Mesh::IndexBuffer back gives a copy the
      ritual made for Python, in a new cute QSSGMesh::Mesh::IndexBuffer.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QSSGMesh::Mesh::IndexBuffer'

    #  Qt's '~QSSGMesh::Mesh::IndexBuffer()'. Naming it makes this a value
    #  class: Python owns every C++ QSSGMesh::Mesh::IndexBuffer behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN8QSSGMesh4Mesh11IndexBufferD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  class Lod(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QSSGMesh::Mesh::Lod: a plain Python object standing
    in front of one C++ QSSGMesh::Mesh::Lod.

    C++ hands a QSSGMesh::Mesh::Lod around as a copy, so every C++
    QSSGMesh::Mesh::Lod behind a cute one is Python's own: it is removed, by
    the ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QSSGMesh::Mesh::Lod yet. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QSSGMesh::Mesh::Lod::~Lod()': the destructor: Python removes its
      C++ QSSGMesh::Mesh::Lod by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QSSGMesh::Mesh::Lod is created at the first use, not by
      'QSSGMesh::Mesh::Lod(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QSSGMesh::Mesh::Lod back gives a copy the ritual
      made for Python, in a new cute QSSGMesh::Mesh::Lod.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QSSGMesh::Mesh::Lod'

    #  Qt's '~QSSGMesh::Mesh::Lod()'. Naming it makes this a value class:
    #  Python owns every C++ QSSGMesh::Mesh::Lod behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN8QSSGMesh4Mesh3LodD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  class Subset(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QSSGMesh::Mesh::Subset: a plain Python object
    standing in front of one C++ QSSGMesh::Mesh::Subset.

    C++ hands a QSSGMesh::Mesh::Subset around as a copy, so every C++
    QSSGMesh::Mesh::Subset behind a cute one is Python's own: it is removed,
    by the ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QSSGMesh::Mesh::Subset yet. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QSSGMesh::Mesh::Subset::~Subset()': the destructor: Python
      removes its C++ QSSGMesh::Mesh::Subset by it, and has no other use for
      it.

    What to expect
    --------------

    - The C++ QSSGMesh::Mesh::Subset is created at the first use, not by
      'QSSGMesh::Mesh::Subset(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QSSGMesh::Mesh::Subset back gives a copy the ritual
      made for Python, in a new cute QSSGMesh::Mesh::Subset.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QSSGMesh::Mesh::Subset'

    #  Qt's '~QSSGMesh::Mesh::Subset()'. Naming it makes this a value class:
    #  Python owns every C++ QSSGMesh::Mesh::Subset behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN8QSSGMesh4Mesh6SubsetD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  class SubsetBounds(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QSSGMesh::Mesh::SubsetBounds: a plain Python object
    standing in front of one C++ QSSGMesh::Mesh::SubsetBounds.

    C++ hands a QSSGMesh::Mesh::SubsetBounds around as a copy, so every C++
    QSSGMesh::Mesh::SubsetBounds behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    No function of Qt's QSSGMesh::Mesh::SubsetBounds yet. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QSSGMesh::Mesh::SubsetBounds::~SubsetBounds()': the destructor:
      Python removes its C++ QSSGMesh::Mesh::SubsetBounds by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QSSGMesh::Mesh::SubsetBounds is created at the first use, not
      by 'QSSGMesh::Mesh::SubsetBounds(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QSSGMesh::Mesh::SubsetBounds back gives a copy the
      ritual made for Python, in a new cute QSSGMesh::Mesh::SubsetBounds.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QSSGMesh::Mesh::SubsetBounds'

    #  Qt's '~QSSGMesh::Mesh::SubsetBounds()'. Naming it makes this a value
    #  class: Python owns every C++ QSSGMesh::Mesh::SubsetBounds behind a
    #  cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN8QSSGMesh4Mesh12SubsetBoundsD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  class TargetBuffer(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QSSGMesh::Mesh::TargetBuffer: a plain Python object
    standing in front of one C++ QSSGMesh::Mesh::TargetBuffer.

    C++ hands a QSSGMesh::Mesh::TargetBuffer around as a copy, so every C++
    QSSGMesh::Mesh::TargetBuffer behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    No function of Qt's QSSGMesh::Mesh::TargetBuffer yet. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QSSGMesh::Mesh::TargetBuffer::~TargetBuffer()': the destructor:
      Python removes its C++ QSSGMesh::Mesh::TargetBuffer by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QSSGMesh::Mesh::TargetBuffer is created at the first use, not
      by 'QSSGMesh::Mesh::TargetBuffer(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QSSGMesh::Mesh::TargetBuffer back gives a copy the
      ritual made for Python, in a new cute QSSGMesh::Mesh::TargetBuffer.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QSSGMesh::Mesh::TargetBuffer'

    #  Qt's '~QSSGMesh::Mesh::TargetBuffer()'. Naming it makes this a value
    #  class: Python owns every C++ QSSGMesh::Mesh::TargetBuffer behind a
    #  cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN8QSSGMesh4Mesh12TargetBufferD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  class VertexBuffer(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QSSGMesh::Mesh::VertexBuffer: a plain Python object
    standing in front of one C++ QSSGMesh::Mesh::VertexBuffer.

    C++ hands a QSSGMesh::Mesh::VertexBuffer around as a copy, so every C++
    QSSGMesh::Mesh::VertexBuffer behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    No function of Qt's QSSGMesh::Mesh::VertexBuffer yet. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QSSGMesh::Mesh::VertexBuffer::~VertexBuffer()': the destructor:
      Python removes its C++ QSSGMesh::Mesh::VertexBuffer by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QSSGMesh::Mesh::VertexBuffer is created at the first use, not
      by 'QSSGMesh::Mesh::VertexBuffer(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QSSGMesh::Mesh::VertexBuffer back gives a copy the
      ritual made for Python, in a new cute QSSGMesh::Mesh::VertexBuffer.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QSSGMesh::Mesh::VertexBuffer'

    #  Qt's '~QSSGMesh::Mesh::VertexBuffer()'. Naming it makes this a value
    #  class: Python owns every C++ QSSGMesh::Mesh::VertexBuffer behind a
    #  cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN8QSSGMesh4Mesh12VertexBufferD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  class VertexBufferEntry(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QSSGMesh::Mesh::VertexBufferEntry: a plain Python
    object standing in front of one C++ QSSGMesh::Mesh::VertexBufferEntry.

    C++ hands a QSSGMesh::Mesh::VertexBufferEntry around as a copy, so every
    C++ QSSGMesh::Mesh::VertexBufferEntry behind a cute one is Python's own:
    it is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    Every function of Qt's QSSGMesh::Mesh::VertexBufferEntry that has a
    ritual and that Python can call so far, 1 name in all:
    'toRenderVertexBufferEntry'. None can be made from Python: one comes out
    of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QSSGMesh::Mesh::VertexBufferEntry::~VertexBufferEntry()': the
      destructor: Python removes its C++ QSSGMesh::Mesh::VertexBufferEntry by
      it, and has no other use for it.

    What to expect
    --------------

    - The C++ QSSGMesh::Mesh::VertexBufferEntry is created at the first use,
      not by 'QSSGMesh::Mesh::VertexBufferEntry(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QSSGMesh::Mesh::VertexBufferEntry back gives a copy
      the ritual made for Python, in a new cute
      QSSGMesh::Mesh::VertexBufferEntry.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QSSGMesh::Mesh::VertexBufferEntry'

    #  Qt's '~QSSGMesh::Mesh::VertexBufferEntry()'. Naming it makes this a
    #  value class: Python owns every C++ QSSGMesh::Mesh::VertexBufferEntry
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN8QSSGMesh4Mesh17VertexBufferEntryD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def toRenderVertexBufferEntry(self) -> QSSGRenderVertexBufferEntry:
      """
      Calls Qt's 'QSSGRenderVertexBufferEntry
      QSSGMesh::Mesh::VertexBufferEntry::toRenderVertexBufferEntry() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qssgmesh-mesh-vertexbufferentry.html

      Returns
      -------

      QSSGRenderVertexBufferEntry
        A new cute QSSGRenderVertexBufferEntry around the copy Qt gave back.
        Python owns it.
      """
      #  QSSGRenderVertexBufferEntry
      #      QSSGMesh::Mesh::VertexBufferEntry::toRenderVertexBufferEntry()
      #      const
      address = self.uglySide.call(
          'ritual_ZNK8QSSGMesh4Mesh17VertexBufferEntry25toRenderVertexBuffe'
          'rEntryEv',
      )
      from . import QSSGRenderVertexBufferEntry
      return QSSGRenderVertexBufferEntry._cuteOwning(address)

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QIODevice)
  @overload(NoneType)
  @overload(QIODevice, int)
  @overload(NoneType, int)
  def loadMesh(device: Optional[QIODevice], id: int = 0) -> Mesh:
    """
    Calls Qt's 'Mesh QSSGMesh::Mesh::loadMesh(QIODevice *device, quint32
    id)'.

    Qt's own words: https://doc.qt.io/qt-6/qssgmesh-mesh.html#loadMesh

    Parameters
    ----------

    device : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    id : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    Returns
    -------

    Mesh
      A new cute QSSGMesh::Mesh around the copy Qt gave back. Python owns it.
    """
    #  Mesh QSSGMesh::Mesh::loadMesh(QIODevice *device, quint32 id)
    address = Rituals.call(
        'ritual_ZN8QSSGMesh4Mesh8loadMeshEP9QIODevicej',
        CuteMixin._addressOf(device), id,
    )
    return Mesh._cuteOwning(address)

  @staticmethod
  @overload(WAIT['QSSGMesh.RuntimeMeshData'], QString)
  @overload(WAIT['QSSGMesh.RuntimeMeshData'], NoneType)
  def fromRuntimeData(
      data: QSSGMesh.RuntimeMeshData,
      error: Optional[QString],
  ) -> Mesh:
    """
    Calls Qt's 'Mesh QSSGMesh::Mesh::fromRuntimeData(const RuntimeMeshData
    &data, QString *error)'.

    Qt's own words: https://doc.qt.io/qt-6/qssgmesh-mesh.html#fromRuntimeData

    Parameters
    ----------

    data : QSSGMesh.RuntimeMeshData
      Passed on as a value: Qt reads the C++ QSSGMesh::RuntimeMeshData, which
      stays Python's own.

    error : Optional[QString]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Mesh
      A new cute QSSGMesh::Mesh around the copy Qt gave back. Python owns it.
    """
    #  Mesh QSSGMesh::Mesh::fromRuntimeData(const RuntimeMeshData &data,
    #      QString *error)
    address = Rituals.call(
        'ritual_ZN8QSSGMesh4Mesh15fromRuntimeDataERKNS_15RuntimeMeshDataEP7'
        'QString',
        CuteMixin._valueOf(data), CuteMixin._addressOf(error),
    )
    return Mesh._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGMesh::Mesh'

  #  Qt's '~QSSGMesh::Mesh()'. Naming it makes this a value class: Python
  #  owns every C++ QSSGMesh::Mesh behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN8QSSGMesh4MeshD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def vertexBuffer(self) -> VertexBuffer:
    """
    Calls Qt's 'VertexBuffer QSSGMesh::Mesh::vertexBuffer() const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgmesh-mesh.html#vertexBuffer

    Returns
    -------

    VertexBuffer
      A new cute QSSGMesh::Mesh::VertexBuffer around the copy Qt gave back.
      Python owns it.
    """
    #  VertexBuffer QSSGMesh::Mesh::vertexBuffer() const
    address = self.uglySide.call('ritual_ZNK8QSSGMesh4Mesh12vertexBufferEv')
    return QSSGMesh.Mesh.VertexBuffer._cuteOwning(address)

  def indexBuffer(self) -> IndexBuffer:
    """
    Calls Qt's 'IndexBuffer QSSGMesh::Mesh::indexBuffer() const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgmesh-mesh.html#indexBuffer

    Returns
    -------

    IndexBuffer
      A new cute QSSGMesh::Mesh::IndexBuffer around the copy Qt gave back.
      Python owns it.
    """
    #  IndexBuffer QSSGMesh::Mesh::indexBuffer() const
    address = self.uglySide.call('ritual_ZNK8QSSGMesh4Mesh11indexBufferEv')
    return QSSGMesh.Mesh.IndexBuffer._cuteOwning(address)

  def targetBuffer(self) -> TargetBuffer:
    """
    Calls Qt's 'TargetBuffer QSSGMesh::Mesh::targetBuffer() const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgmesh-mesh.html#targetBuffer

    Returns
    -------

    TargetBuffer
      A new cute QSSGMesh::Mesh::TargetBuffer around the copy Qt gave back.
      Python owns it.
    """
    #  TargetBuffer QSSGMesh::Mesh::targetBuffer() const
    address = self.uglySide.call('ritual_ZNK8QSSGMesh4Mesh12targetBufferEv')
    return QSSGMesh.Mesh.TargetBuffer._cuteOwning(address)

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QSSGMesh::Mesh::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgmesh-mesh.html#isValid
    """
    #  bool QSSGMesh::Mesh::isValid() const
    return self.uglySide.call('ritual_ZNK8QSSGMesh4Mesh7isValidEv')

  @overload(QIODevice)
  @overload(NoneType)
  @overload(QIODevice, int)
  @overload(NoneType, int)
  def save(self, device: Optional[QIODevice], id: int = 0) -> int:
    """
    Calls Qt's 'quint32 QSSGMesh::Mesh::save(QIODevice *device, quint32 id)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgmesh-mesh.html#save

    Parameters
    ----------

    device : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    id : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  quint32 QSSGMesh::Mesh::save(QIODevice *device, quint32 id) const
    return self.uglySide.call(
        'ritual_ZNK8QSSGMesh4Mesh4saveEP9QIODevicej',
        self._addressOf(device), id,
    )

  def hasLightmapUVChannel(self) -> bool:
    """
    Calls Qt's 'bool QSSGMesh::Mesh::hasLightmapUVChannel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgmesh-mesh.html#hasLightmapUVChannel
    """
    #  bool QSSGMesh::Mesh::hasLightmapUVChannel() const
    return self.uglySide.call(
        'ritual_ZNK8QSSGMesh4Mesh20hasLightmapUVChannelEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float, QMatrix4x4)
  def createLightmapUVChannel(
      self,
      texelsPerUnit: float,
      scale: QMatrix4x4,
  ) -> bool:
    """
    Calls Qt's 'bool QSSGMesh::Mesh::createLightmapUVChannel(float
    texelsPerUnit, const QMatrix4x4 &scale)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgmesh-mesh.html#createLightmapUVChannel

    Parameters
    ----------

    texelsPerUnit : float
      Passed on as it is.

    scale : QMatrix4x4
      Passed on as a value: Qt reads the C++ QMatrix4x4, which stays Python's
      own.
    """
    #  bool QSSGMesh::Mesh::createLightmapUVChannel(float texelsPerUnit,
    #      const QMatrix4x4 &scale)
    return self.uglySide.call(
        'ritual_ZN8QSSGMesh4Mesh23createLightmapUVChannelEfRK10QMatrix4x4',
        texelsPerUnit, self._valueOf(scale),
    )

  @staticmethod
  def drawMode(*__, **_) -> Never:
    """
    Qt's 'DrawMode QSSGMesh::Mesh::drawMode() const': gives the enum
    'QSSGRenderDrawMode', whose class cannot be named here.
    """
    raise NotImplementedError(
        "'QSSGMesh.Mesh.drawMode' has no cute function yet. Qt's 'DrawMode "
        "QSSGMesh::Mesh::drawMode() const': gives the enum "
        "'QSSGRenderDrawMode', whose class cannot be named here.")

  @staticmethod
  def fromAssetData(*__, **_) -> Never:
    """
    Qt's 'Mesh QSSGMesh::Mesh::fromAssetData(const QVector<AssetVertexEntry>
    &vbufEntries, const QByteArray &indexBufferData, ComponentType
    indexComponentType, const QVector<AssetMeshSubset> &subsets, quint32
    numTargets, quint32 numTargetComps)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QSSGMesh.Mesh.fromAssetData' has no cute function yet. Qt's 'Mesh "
        "QSSGMesh::Mesh::fromAssetData(const QVector<AssetVertexEntry> "
        "&vbufEntries, const QByteArray &indexBufferData, ComponentType "
        "indexComponentType, const QVector<AssetMeshSubset> &subsets, "
        "quint32 numTargets, quint32 numTargetComps)': takes a type Python "
        "has no way to hand over yet.")

  @staticmethod
  def loadAll(*__, **_) -> Never:
    """
    Qt's 'QMap<quint32, Mesh> QSSGMesh::Mesh::loadAll(QIODevice *device)':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSSGMesh.Mesh.loadAll' has no cute function yet. Qt's "
        "'QMap<quint32, Mesh> QSSGMesh::Mesh::loadAll(QIODevice *device)': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def subsets(*__, **_) -> Never:
    """
    Qt's 'QVector<Subset> QSSGMesh::Mesh::subsets() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSSGMesh.Mesh.subsets' has no cute function yet. Qt's "
        "'QVector<Subset> QSSGMesh::Mesh::subsets() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def winding(*__, **_) -> Never:
    """
    Qt's 'Winding QSSGMesh::Mesh::winding() const': gives the enum
    'QSSGRenderWinding', whose class cannot be named here.
    """
    raise NotImplementedError(
        "'QSSGMesh.Mesh.winding' has no cute function yet. Qt's 'Winding "
        "QSSGMesh::Mesh::winding() const': gives the enum "
        "'QSSGRenderWinding', whose class cannot be named here.")
