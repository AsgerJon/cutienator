"""
QSSGRenderGeometry binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendergeometry_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGRenderGeometry to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtQuick3DUtils import QSSGMesh
from . import QSSGRenderGraphObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QByteArray
  from ..QtGui import QVector3D
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QVector3D = WAIT['QVector3D']


class QSSGRenderGeometry(QSSGRenderGraphObject):
  """
  The cute side of Qt's QSSGRenderGeometry: a plain Python object standing in
  front of one C++ QSSGRenderGeometry.

  It is built on the cute 'QSSGRenderGraphObject', as Qt's QSSGRenderGeometry
  is built on Qt's QSSGRenderGraphObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSSGRenderGeometry that has a ritual and that Python
  can call so far, 22 names in all: 'vertexBuffer', 'indexBuffer',
  'attributeCount', 'attribute', 'boundsMin', 'boundsMax', 'stride',
  'setVertexData', 'setIndexData', 'setStride', 'setBounds', 'addAttribute',
  'addSubset', 'clear', 'clearAttributes', 'generationId', 'meshData',
  'clearVertexAndIndex', 'clearTarget', 'setTargetData',
  'addTargetAttribute', 'markDirty'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSSGRenderGeometry::~QSSGRenderGeometry()': the destructor: Python
    never removes a C++ QSSGRenderGeometry.
  - Qt's 'QByteArray &QSSGRenderGeometry::vertexBuffer()': gives a type
    Python has no way to take yet.
  - Qt's 'QByteArray &QSSGRenderGeometry::indexBuffer()': gives a type Python
    has no way to take yet.
  - Qt's 'QSSGMesh::Mesh::DrawMode QSSGRenderGeometry::primitiveType()
    const': gives the enum 'QSSGRenderDrawMode', whose class cannot be named
    here.
  - Qt's 'void QSSGRenderGeometry::setPrimitiveType(QSSGMesh::Mesh::DrawMode
    type)': names the enum 'QSSGRenderDrawMode', whose class cannot be named
    here.
  - Qt's 'void
    QSSGRenderGeometry::addAttribute(QSSGMesh::RuntimeMeshData::Attribute::
    Semantic semantic, int offset, QSSGMesh::Mesh::ComponentType
    componentType)': names the enum 'QSSGRenderComponentType', whose class
    cannot be named here.

  What has no ritual
  ------------------

  3 of the 33 functions Qt declares: 2 forbidden; 1 cannot be called and
  cannot be called through the meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ QSSGRenderGeometry is created at the first use, not by
    'QSSGRenderGeometry(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSSGRenderGeometry.
  - Each name of Qt's QSSGRenderGeometry that has no cute function yet,
    'primitiveType', 'setPrimitiveType', 'targetStride', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  #  The classes Qt writes inside QSSGRenderGeometry, each a class in here as
  #  in C++.

  class Attribute(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QSSGRenderGeometry::Attribute: a plain Python
    object standing in front of one C++ QSSGRenderGeometry::Attribute.

    C++ hands a QSSGRenderGeometry::Attribute around as a copy, so every C++
    QSSGRenderGeometry::Attribute behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    No function of Qt's QSSGRenderGeometry::Attribute yet. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QSSGRenderGeometry::Attribute::~Attribute()': the destructor:
      Python removes its C++ QSSGRenderGeometry::Attribute by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QSSGRenderGeometry::Attribute is created at the first use, not
      by 'QSSGRenderGeometry::Attribute(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QSSGRenderGeometry::Attribute back gives a copy the
      ritual made for Python, in a new cute QSSGRenderGeometry::Attribute.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QSSGRenderGeometry::Attribute'

    #  Qt's '~QSSGRenderGeometry::Attribute()'. Naming it makes this a value
    #  class: Python owns every C++ QSSGRenderGeometry::Attribute behind a
    #  cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN18QSSGRenderGeometry9AttributeD1Ev'

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

  class TargetAttribute(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QSSGRenderGeometry::TargetAttribute: a plain Python
    object standing in front of one C++ QSSGRenderGeometry::TargetAttribute.

    C++ hands a QSSGRenderGeometry::TargetAttribute around as a copy, so
    every C++ QSSGRenderGeometry::TargetAttribute behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    No function of Qt's QSSGRenderGeometry::TargetAttribute yet. None can be
    made from Python: one comes out of a function of another class that gives
    one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QSSGRenderGeometry::TargetAttribute::~TargetAttribute()': the
      destructor: Python removes its C++ QSSGRenderGeometry::TargetAttribute
      by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QSSGRenderGeometry::TargetAttribute is created at the first
      use, not by 'QSSGRenderGeometry::TargetAttribute(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QSSGRenderGeometry::TargetAttribute back gives a
      copy the ritual made for Python, in a new cute
      QSSGRenderGeometry::TargetAttribute.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QSSGRenderGeometry::TargetAttribute'

    #  Qt's '~QSSGRenderGeometry::TargetAttribute()'. Naming it makes this a
    #  value class: Python owns every C++ QSSGRenderGeometry::TargetAttribute
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN18QSSGRenderGeometry15TargetAttributeD1Ev'

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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGRenderGeometry'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def vertexBuffer(self) -> QByteArray:
    """
    Calls Qt's 'const QByteArray &QSSGRenderGeometry::vertexBuffer() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrendergeometry.html#vertexBuffer

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  const QByteArray &QSSGRenderGeometry::vertexBuffer() const
    address = self.uglySide.call(
        'ritual_ZNK18QSSGRenderGeometry12vertexBufferEv',
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def indexBuffer(self) -> QByteArray:
    """
    Calls Qt's 'const QByteArray &QSSGRenderGeometry::indexBuffer() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrendergeometry.html#indexBuffer

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  const QByteArray &QSSGRenderGeometry::indexBuffer() const
    address = self.uglySide.call(
        'ritual_ZNK18QSSGRenderGeometry11indexBufferEv',
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def attributeCount(self) -> int:
    """
    Calls Qt's 'int QSSGRenderGeometry::attributeCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrendergeometry.html#attributeCount
    """
    #  int QSSGRenderGeometry::attributeCount() const
    return self.uglySide.call(
        'ritual_ZNK18QSSGRenderGeometry14attributeCountEv',
    )

  @overload(int)
  def attribute(self, idx: int) -> Attribute:
    """
    Calls Qt's 'Attribute QSSGRenderGeometry::attribute(int idx) const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrendergeometry.html#attribute

    Parameters
    ----------

    idx : int
      Passed on as it is.

    Returns
    -------

    Attribute
      A new cute QSSGRenderGeometry::Attribute around the copy Qt gave back.
      Python owns it.
    """
    #  Attribute QSSGRenderGeometry::attribute(int idx) const
    address = self.uglySide.call(
        'ritual_ZNK18QSSGRenderGeometry9attributeEi', idx,
    )
    return QSSGRenderGeometry.Attribute._cuteOwning(address)

  def boundsMin(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D QSSGRenderGeometry::boundsMin() const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrendergeometry.html#boundsMin

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QSSGRenderGeometry::boundsMin() const
    address = self.uglySide.call(
        'ritual_ZNK18QSSGRenderGeometry9boundsMinEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def boundsMax(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D QSSGRenderGeometry::boundsMax() const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrendergeometry.html#boundsMax

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QSSGRenderGeometry::boundsMax() const
    address = self.uglySide.call(
        'ritual_ZNK18QSSGRenderGeometry9boundsMaxEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def stride(self) -> int:
    """
    Calls Qt's 'int QSSGRenderGeometry::stride() const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrendergeometry.html#stride
    """
    #  int QSSGRenderGeometry::stride() const
    return self.uglySide.call('ritual_ZNK18QSSGRenderGeometry6strideEv')

  def generationId(self) -> int:
    """
    Calls Qt's 'uint32_t QSSGRenderGeometry::generationId() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrendergeometry.html#generationId
    """
    #  uint32_t QSSGRenderGeometry::generationId() const
    return self.uglySide.call(
        'ritual_ZNK18QSSGRenderGeometry12generationIdEv',
    )

  def meshData(self) -> QSSGMesh.RuntimeMeshData:
    """
    Calls Qt's 'const QSSGMesh::RuntimeMeshData
    &QSSGRenderGeometry::meshData() const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrendergeometry.html#meshData

    Returns
    -------

    QSSGMesh.RuntimeMeshData
      A new cute QSSGMesh::RuntimeMeshData around the copy Qt gave back.
      Python owns it.
    """
    #  const QSSGMesh::RuntimeMeshData &QSSGRenderGeometry::meshData() const
    address = self.uglySide.call('ritual_ZNK18QSSGRenderGeometry8meshDataEv')
    return QSSGMesh.RuntimeMeshData._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QByteArray)
  def setVertexData(self, data: QByteArray) -> None:
    """
    Calls Qt's 'void QSSGRenderGeometry::setVertexData(const QByteArray
    &data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrendergeometry.html#setVertexData

    Parameters
    ----------

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QSSGRenderGeometry::setVertexData(const QByteArray &data)
    self.uglySide.call(
        'ritual_ZN18QSSGRenderGeometry13setVertexDataERK10QByteArray',
        self._valueOf(data),
    )

  @overload(QByteArray)
  def setIndexData(self, data: QByteArray) -> None:
    """
    Calls Qt's 'void QSSGRenderGeometry::setIndexData(const QByteArray
    &data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrendergeometry.html#setIndexData

    Parameters
    ----------

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QSSGRenderGeometry::setIndexData(const QByteArray &data)
    self.uglySide.call(
        'ritual_ZN18QSSGRenderGeometry12setIndexDataERK10QByteArray',
        self._valueOf(data),
    )

  @overload(int)
  def setStride(self, stride: int) -> None:
    """
    Calls Qt's 'void QSSGRenderGeometry::setStride(int stride)'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrendergeometry.html#setStride

    Parameters
    ----------

    stride : int
      Passed on as it is.
    """
    #  void QSSGRenderGeometry::setStride(int stride)
    self.uglySide.call('ritual_ZN18QSSGRenderGeometry9setStrideEi', stride)

  @overload(QVector3D, QVector3D)
  def setBounds(self, min: QVector3D, max: QVector3D) -> None:
    """
    Calls Qt's 'void QSSGRenderGeometry::setBounds(const QVector3D &min,
    const QVector3D &max)'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrendergeometry.html#setBounds

    Parameters
    ----------

    min : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    max : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QSSGRenderGeometry::setBounds(const QVector3D &min, const
    #      QVector3D &max)
    self.uglySide.call(
        'ritual_ZN18QSSGRenderGeometry9setBoundsERK9QVector3DS2_',
        self._valueOf(min), self._valueOf(max),
    )

  @overload(QByteArray)
  def setTargetData(self, data: QByteArray) -> None:
    """
    Calls Qt's 'void QSSGRenderGeometry::setTargetData(const QByteArray
    &data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrendergeometry.html#setTargetData

    Parameters
    ----------

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QSSGRenderGeometry::setTargetData(const QByteArray &data)
    self.uglySide.call(
        'ritual_ZN18QSSGRenderGeometry13setTargetDataERK10QByteArray',
        self._valueOf(data),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QSSGRenderGeometry::QSSGRenderGeometry()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrendergeometry.html#QSSGRenderGeometry
    """
    #  QSSGRenderGeometry::QSSGRenderGeometry()
    self._noteCreation(QSSGRenderGeometry, lambda: Rituals.call(
        'ritual_ZN18QSSGRenderGeometryC1Ev',
    ))

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

  @overload(Attribute)
  def addAttribute(self, att: Attribute) -> None:
    """
    Calls Qt's 'void QSSGRenderGeometry::addAttribute(const Attribute &att)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrendergeometry.html#addAttribute

    Parameters
    ----------

    att : Attribute
      Passed on as a value: Qt reads the C++ QSSGRenderGeometry::Attribute,
      which stays Python's own.
    """
    #  void QSSGRenderGeometry::addAttribute(const Attribute &att)
    self.uglySide.call(
        'ritual_ZN18QSSGRenderGeometry12addAttributeERKNS_9AttributeE',
        self._valueOf(att),
    )

  @overload(int, int, QVector3D, QVector3D)
  @overload(int, int, QVector3D, QVector3D, str)
  def addSubset(
      self,
      offset: int,
      count: int,
      boundsMin: QVector3D,
      boundsMax: QVector3D,
      name: str = '',
  ) -> None:
    """
    Calls Qt's 'void QSSGRenderGeometry::addSubset(quint32 offset, quint32
    count, const QVector3D &boundsMin, const QVector3D &boundsMax, const
    QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrendergeometry.html#addSubset

    Parameters
    ----------

    offset : int
      Passed on as it is.

    count : int
      Passed on as it is.

    boundsMin : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    boundsMax : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    name : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  void QSSGRenderGeometry::addSubset(quint32 offset, quint32 count,
    #      const QVector3D &boundsMin, const QVector3D &boundsMax, const
    #      QString &name)
    self.uglySide.call(
        'ritual_ZN18QSSGRenderGeometry9addSubsetEjjRK9QVector3DS2_RK7QStrin'
        'g',
        offset, count, self._valueOf(boundsMin), self._valueOf(boundsMax),
        name,
    )

  def clear(self) -> None:
    """
    Calls Qt's 'void QSSGRenderGeometry::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrendergeometry.html#clear
    """
    #  void QSSGRenderGeometry::clear()
    self.uglySide.call('ritual_ZN18QSSGRenderGeometry5clearEv')

  def clearAttributes(self) -> None:
    """
    Calls Qt's 'void QSSGRenderGeometry::clearAttributes()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrendergeometry.html#clearAttributes
    """
    #  void QSSGRenderGeometry::clearAttributes()
    self.uglySide.call('ritual_ZN18QSSGRenderGeometry15clearAttributesEv')

  def clearVertexAndIndex(self) -> None:
    """
    Calls Qt's 'void QSSGRenderGeometry::clearVertexAndIndex()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrendergeometry.html#clearVertexAndIndex
    """
    #  void QSSGRenderGeometry::clearVertexAndIndex()
    self.uglySide.call(
        'ritual_ZN18QSSGRenderGeometry19clearVertexAndIndexEv',
    )

  def clearTarget(self) -> None:
    """
    Calls Qt's 'void QSSGRenderGeometry::clearTarget()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrendergeometry.html#clearTarget
    """
    #  void QSSGRenderGeometry::clearTarget()
    self.uglySide.call('ritual_ZN18QSSGRenderGeometry11clearTargetEv')

  @overload(int, QSSGMesh.RuntimeMeshData.Attribute.Semantic, int)
  @overload(int, QSSGMesh.RuntimeMeshData.Attribute.Semantic, int, int)
  def addTargetAttribute(
      self,
      targetId: int,
      semantic: QSSGMesh.RuntimeMeshData.Attribute.Semantic,
      offset: int,
      stride: int = 0,
  ) -> None:
    """
    Calls Qt's 'void QSSGRenderGeometry::addTargetAttribute(quint32 targetId,
    QSSGMesh::RuntimeMeshData::Attribute::Semantic semantic, int offset, int
    stride)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrendergeometry.html#addTargetAttribute

    Parameters
    ----------

    targetId : int
      Passed on as it is.

    semantic : QSSGMesh.RuntimeMeshData.Attribute.Semantic
      Passed on as its number.

    offset : int
      Passed on as it is.

    stride : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  void QSSGRenderGeometry::addTargetAttribute(quint32 targetId,
    #      QSSGMesh::RuntimeMeshData::Attribute::Semantic semantic, int
    #      offset, int stride)
    self.uglySide.call(
        'ritual_ZN18QSSGRenderGeometry18addTargetAttributeEjN8QSSGMesh15Run'
        'timeMeshData9Attribute8SemanticEii',
        targetId, semantic.value, offset, stride,
    )

  @overload(TargetAttribute)
  def addTargetAttribute(self, att: TargetAttribute) -> None:
    """
    Calls Qt's 'void QSSGRenderGeometry::addTargetAttribute(const
    TargetAttribute &att)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrendergeometry.html#addTargetAttribute

    Parameters
    ----------

    att : TargetAttribute
      Passed on as a value: Qt reads the C++
      QSSGRenderGeometry::TargetAttribute, which stays Python's own.
    """
    #  void QSSGRenderGeometry::addTargetAttribute(const TargetAttribute
    #      &att)
    self.uglySide.call(
        'ritual_ZN18QSSGRenderGeometry18addTargetAttributeERKNS_15TargetAtt'
        'ributeE',
        self._valueOf(att),
    )

  def markDirty(self) -> None:
    """
    Calls Qt's 'void QSSGRenderGeometry::markDirty()'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrendergeometry.html#markDirty
    """
    #  void QSSGRenderGeometry::markDirty()
    self.uglySide.call('ritual_ZN18QSSGRenderGeometry9markDirtyEv')

  @staticmethod
  def primitiveType(*__, **_) -> Never:
    """
    Qt's 'QSSGMesh::Mesh::DrawMode QSSGRenderGeometry::primitiveType()
    const': gives the enum 'QSSGRenderDrawMode', whose class cannot be named
    here.
    """
    raise NotImplementedError(
        "'QSSGRenderGeometry.primitiveType' has no cute function yet. Qt's "
        "'QSSGMesh::Mesh::DrawMode QSSGRenderGeometry::primitiveType() "
        "const': gives the enum 'QSSGRenderDrawMode', whose class cannot be "
        "named here.")

  @staticmethod
  def setPrimitiveType(*__, **_) -> Never:
    """
    Qt's 'void QSSGRenderGeometry::setPrimitiveType(QSSGMesh::Mesh::DrawMode
    type)': names the enum 'QSSGRenderDrawMode', whose class cannot be named
    here.
    """
    raise NotImplementedError(
        "'QSSGRenderGeometry.setPrimitiveType' has no cute function yet. "
        "Qt's 'void "
        "QSSGRenderGeometry::setPrimitiveType(QSSGMesh::Mesh::DrawMode "
        "type)': names the enum 'QSSGRenderDrawMode', whose class cannot be "
        "named here.")

  @staticmethod
  def targetStride(*__, **_) -> Never:
    """
    Qt's 'int QSSGRenderGeometry::targetStride() const': cannot be called and
    cannot be called through the meta-object and cannot be copied: no header
    file has its code, Qt's source does not mark it or its class for use from
    outside Qt or writes it 'inline' or nowhere, and it is no signal, slot or
    invokable function giving back nothing, of a class built on QObject, and
    Qt's source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QSSGRenderGeometry.targetStride' has no cute function yet. Qt's "
        "'int QSSGRenderGeometry::targetStride() const': cannot be called "
        "and cannot be called through the meta-object and cannot be copied: "
        "no header file has its code, Qt's source does not mark it or its "
        "class for use from outside Qt or writes it 'inline' or nowhere, "
        "and it is no signal, slot or invokable function giving back "
        "nothing, of a class built on QObject, and Qt's source has no code "
        "for it that could be told from the rest.")
