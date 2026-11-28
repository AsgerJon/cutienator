"""
Qt3DCore::QGeometryView binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DCore/qgeometryview.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from . import Qt3DCore

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGeometryView(Qt3DCore.QNode):
  """
  The cute side of Qt's Qt3DCore::QGeometryView: a plain Python object
  standing in front of one C++ Qt3DCore::QGeometryView.

  It is built on the cute 'Qt3DCore::QNode', as Qt's Qt3DCore::QGeometryView
  is built on Qt's Qt3DCore::QNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DCore::QGeometryView that has a ritual and that
  Python can call so far, 36 names in all: 'metaObject', 'tr',
  'instanceCount', 'vertexCount', 'indexOffset', 'firstInstance',
  'firstVertex', 'indexBufferByteOffset', 'restartIndexValue',
  'verticesPerPatch', 'primitiveRestartEnabled', 'geometry', 'primitiveType',
  'setInstanceCount', 'setVertexCount', 'setIndexOffset', 'setFirstInstance',
  'setFirstVertex', 'setIndexBufferByteOffset', 'setRestartIndexValue',
  'setVerticesPerPatch', 'setPrimitiveRestartEnabled', 'setGeometry',
  'setPrimitiveType', 'instanceCountChanged', 'vertexCountChanged',
  'indexOffsetChanged', 'firstInstanceChanged', 'firstVertexChanged',
  'indexBufferByteOffsetChanged', 'restartIndexValueChanged',
  'verticesPerPatchChanged', 'primitiveRestartEnabledChanged',
  'geometryChanged', 'primitiveTypeChanged', 'd_func'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DCore::QGeometryView::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int Qt3DCore::QGeometryView::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DCore::QGeometryView::~QGeometryView()': the destructor: Python
    never removes a C++ Qt3DCore::QGeometryView.
  - Qt's 'Qt3DCore::QGeometryView::QGeometryView(QGeometryViewPrivate &dd,
    Qt3DCore::QNode *parent)': takes a type Python has no way to hand over
    yet.
  - Qt's 'const QGeometryViewPrivate *Qt3DCore::QGeometryView::d_func()
    const': takes in Python what 'QGeometryViewPrivate
    *Qt3DCore::QGeometryView::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 46 functions Qt declares: 2 not a gap; 2 cannot be called and
  cannot be called through the meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ Qt3DCore::QGeometryView is created at the first use, not by
    'Qt3DCore::QGeometryView(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DCore::QGeometryView.
  - Qt tells when it has removed the C++ Qt3DCore::QGeometryView. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's Qt3DCore::QGeometryView that has no cute function yet,
    'geometryFactory', 'setGeometryFactory', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside Qt3DCore::QGeometryView, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class PrimitiveType(CuteNum):
    """
    The enum 'Qt3DCore::QGeometryView::PrimitiveType' of Qt, with the 12
    names Qt gives in it.
    """

    Points = Kee[int](0)
    Lines = Kee[int](1)
    LineLoop = Kee[int](2)
    LineStrip = Kee[int](3)
    Triangles = Kee[int](4)
    TriangleStrip = Kee[int](5)
    TriangleFan = Kee[int](6)
    LinesAdjacency = Kee[int](10)
    TrianglesAdjacency = Kee[int](12)
    LineStripAdjacency = Kee[int](11)
    TriangleStripAdjacency = Kee[int](13)
    Patches = Kee[int](14)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString Qt3DCore::QGeometryView::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qgeometryview.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString Qt3DCore::QGeometryView::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN8Qt3DCore13QGeometryView2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DCore::QGeometryView'

  #  A C++ Qt3DCore::QGeometryView Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DCore_QGeometryView'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DCore::QGeometryView::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qgeometryview.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DCore::QGeometryView::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore13QGeometryView10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def instanceCount(self) -> int:
    """
    Calls Qt's 'int Qt3DCore::QGeometryView::instanceCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qgeometryview.html#instanceCount
    """
    #  int Qt3DCore::QGeometryView::instanceCount() const
    return self.uglySide.call(
        'ritual_ZNK8Qt3DCore13QGeometryView13instanceCountEv',
    )

  def vertexCount(self) -> int:
    """
    Calls Qt's 'int Qt3DCore::QGeometryView::vertexCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qgeometryview.html#vertexCount
    """
    #  int Qt3DCore::QGeometryView::vertexCount() const
    return self.uglySide.call(
        'ritual_ZNK8Qt3DCore13QGeometryView11vertexCountEv',
    )

  def indexOffset(self) -> int:
    """
    Calls Qt's 'int Qt3DCore::QGeometryView::indexOffset() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qgeometryview.html#indexOffset
    """
    #  int Qt3DCore::QGeometryView::indexOffset() const
    return self.uglySide.call(
        'ritual_ZNK8Qt3DCore13QGeometryView11indexOffsetEv',
    )

  def firstInstance(self) -> int:
    """
    Calls Qt's 'int Qt3DCore::QGeometryView::firstInstance() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qgeometryview.html#firstInstance
    """
    #  int Qt3DCore::QGeometryView::firstInstance() const
    return self.uglySide.call(
        'ritual_ZNK8Qt3DCore13QGeometryView13firstInstanceEv',
    )

  def firstVertex(self) -> int:
    """
    Calls Qt's 'int Qt3DCore::QGeometryView::firstVertex() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qgeometryview.html#firstVertex
    """
    #  int Qt3DCore::QGeometryView::firstVertex() const
    return self.uglySide.call(
        'ritual_ZNK8Qt3DCore13QGeometryView11firstVertexEv',
    )

  def indexBufferByteOffset(self) -> int:
    """
    Calls Qt's 'int Qt3DCore::QGeometryView::indexBufferByteOffset() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qgeometryview.html#indexBufferByteOffset
    """
    #  int Qt3DCore::QGeometryView::indexBufferByteOffset() const
    return self.uglySide.call(
        'ritual_ZNK8Qt3DCore13QGeometryView21indexBufferByteOffsetEv',
    )

  def restartIndexValue(self) -> int:
    """
    Calls Qt's 'int Qt3DCore::QGeometryView::restartIndexValue() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qgeometryview.html#restartIndexValue
    """
    #  int Qt3DCore::QGeometryView::restartIndexValue() const
    return self.uglySide.call(
        'ritual_ZNK8Qt3DCore13QGeometryView17restartIndexValueEv',
    )

  def verticesPerPatch(self) -> int:
    """
    Calls Qt's 'int Qt3DCore::QGeometryView::verticesPerPatch() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qgeometryview.html#verticesPerPatch
    """
    #  int Qt3DCore::QGeometryView::verticesPerPatch() const
    return self.uglySide.call(
        'ritual_ZNK8Qt3DCore13QGeometryView16verticesPerPatchEv',
    )

  def primitiveRestartEnabled(self) -> bool:
    """
    Calls Qt's 'bool Qt3DCore::QGeometryView::primitiveRestartEnabled()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qgeometryview.html
    """
    #  bool Qt3DCore::QGeometryView::primitiveRestartEnabled() const
    return self.uglySide.call(
        'ritual_ZNK8Qt3DCore13QGeometryView23primitiveRestartEnabledEv',
    )

  def geometry(self) -> Optional[Qt3DCore.QGeometry]:
    """
    Calls Qt's 'QGeometry *Qt3DCore::QGeometryView::geometry() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qgeometryview.html#geometry

    Returns
    -------

    Optional[Qt3DCore.QGeometry]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGeometry *Qt3DCore::QGeometryView::geometry() const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore13QGeometryView8geometryEv',
    )
    return Qt3DCore.QGeometry._cuteAt(address)

  def primitiveType(self) -> PrimitiveType:
    """
    Calls Qt's 'PrimitiveType Qt3DCore::QGeometryView::primitiveType()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qgeometryview.html#primitiveType

    Returns
    -------

    PrimitiveType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'PrimitiveType(number)'
      gives.
    """
    #  PrimitiveType Qt3DCore::QGeometryView::primitiveType() const
    return QGeometryView.PrimitiveType(self.uglySide.call(
        'ritual_ZNK8Qt3DCore13QGeometryView13primitiveTypeEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setInstanceCount(self, instanceCount: int) -> None:
    """
    Calls Qt's 'void Qt3DCore::QGeometryView::setInstanceCount(int
    instanceCount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qgeometryview.html#setInstanceCount

    Parameters
    ----------

    instanceCount : int
      Passed on as it is.
    """
    #  void Qt3DCore::QGeometryView::setInstanceCount(int instanceCount)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore13QGeometryView16setInstanceCountEi',
        instanceCount,
    )

  @overload(int)
  def setVertexCount(self, vertexCount: int) -> None:
    """
    Calls Qt's 'void Qt3DCore::QGeometryView::setVertexCount(int
    vertexCount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qgeometryview.html#setVertexCount

    Parameters
    ----------

    vertexCount : int
      Passed on as it is.
    """
    #  void Qt3DCore::QGeometryView::setVertexCount(int vertexCount)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore13QGeometryView14setVertexCountEi', vertexCount,
    )

  @overload(int)
  def setIndexOffset(self, indexOffset: int) -> None:
    """
    Calls Qt's 'void Qt3DCore::QGeometryView::setIndexOffset(int
    indexOffset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qgeometryview.html#setIndexOffset

    Parameters
    ----------

    indexOffset : int
      Passed on as it is.
    """
    #  void Qt3DCore::QGeometryView::setIndexOffset(int indexOffset)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore13QGeometryView14setIndexOffsetEi', indexOffset,
    )

  @overload(int)
  def setFirstInstance(self, firstInstance: int) -> None:
    """
    Calls Qt's 'void Qt3DCore::QGeometryView::setFirstInstance(int
    firstInstance)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qgeometryview.html#setFirstInstance

    Parameters
    ----------

    firstInstance : int
      Passed on as it is.
    """
    #  void Qt3DCore::QGeometryView::setFirstInstance(int firstInstance)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore13QGeometryView16setFirstInstanceEi',
        firstInstance,
    )

  @overload(int)
  def setFirstVertex(self, firstVertex: int) -> None:
    """
    Calls Qt's 'void Qt3DCore::QGeometryView::setFirstVertex(int
    firstVertex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qgeometryview.html#setFirstVertex

    Parameters
    ----------

    firstVertex : int
      Passed on as it is.
    """
    #  void Qt3DCore::QGeometryView::setFirstVertex(int firstVertex)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore13QGeometryView14setFirstVertexEi', firstVertex,
    )

  @overload(int)
  def setIndexBufferByteOffset(self, offset: int) -> None:
    """
    Calls Qt's 'void Qt3DCore::QGeometryView::setIndexBufferByteOffset(int
    offset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qgeometryview.html

    Parameters
    ----------

    offset : int
      Passed on as it is.
    """
    #  void Qt3DCore::QGeometryView::setIndexBufferByteOffset(int offset)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore13QGeometryView24setIndexBufferByteOffsetEi',
        offset,
    )

  @overload(int)
  def setRestartIndexValue(self, index: int) -> None:
    """
    Calls Qt's 'void Qt3DCore::QGeometryView::setRestartIndexValue(int
    index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qgeometryview.html#setRestartIndexValue

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void Qt3DCore::QGeometryView::setRestartIndexValue(int index)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore13QGeometryView20setRestartIndexValueEi', index,
    )

  @overload(int)
  def setVerticesPerPatch(self, verticesPerPatch: int) -> None:
    """
    Calls Qt's 'void Qt3DCore::QGeometryView::setVerticesPerPatch(int
    verticesPerPatch)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qgeometryview.html#setVerticesPerPatch

    Parameters
    ----------

    verticesPerPatch : int
      Passed on as it is.
    """
    #  void Qt3DCore::QGeometryView::setVerticesPerPatch(int
    #      verticesPerPatch)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore13QGeometryView19setVerticesPerPatchEi',
        verticesPerPatch,
    )

  @overload(bool)
  def setPrimitiveRestartEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void Qt3DCore::QGeometryView::setPrimitiveRestartEnabled(bool
    enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qgeometryview.html

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void Qt3DCore::QGeometryView::setPrimitiveRestartEnabled(bool enabled)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore13QGeometryView26setPrimitiveRestartEnabledEb',
        enabled,
    )

  @overload(WAIT['Qt3DCore.QGeometry'])
  @overload(NoneType)
  def setGeometry(self, geometry: Optional[Qt3DCore.QGeometry]) -> None:
    """
    Calls Qt's 'void Qt3DCore::QGeometryView::setGeometry(QGeometry
    *geometry)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qgeometryview.html#setGeometry

    Parameters
    ----------

    geometry : Optional[Qt3DCore.QGeometry]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DCore::QGeometryView::setGeometry(QGeometry *geometry)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore13QGeometryView11setGeometryEPNS_9QGeometryE',
        self._addressOf(geometry),
    )

  @overload(PrimitiveType)
  def setPrimitiveType(self, primitiveType: PrimitiveType) -> None:
    """
    Calls Qt's 'void Qt3DCore::QGeometryView::setPrimitiveType(PrimitiveType
    primitiveType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qgeometryview.html#setPrimitiveType

    Parameters
    ----------

    primitiveType : PrimitiveType
      Passed on as its number.
    """
    #  void Qt3DCore::QGeometryView::setPrimitiveType(PrimitiveType
    #      primitiveType)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore13QGeometryView16setPrimitiveTypeENS0_13Primitiv'
        'eTypeE',
        primitiveType.value,
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
  @overload(Qt3DCore.QNode)
  @overload(NoneType)
  def __init__(self, parent: Optional[Qt3DCore.QNode] = None) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DCore::QGeometryView::QGeometryView(Qt3DCore::QNode *parent)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qgeometryview.html#QGeometryView

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DCore::QGeometryView::QGeometryView(Qt3DCore::QNode *parent)
    self._noteCreation(QGeometryView, lambda: Rituals.call(
        'ritual_ZN8Qt3DCore13QGeometryViewC1EPNS_5QNodeE',
        self._addressOf(parent),
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

  @overload(int)
  def instanceCountChanged(self, instanceCount: int) -> None:
    """
    Calls Qt's 'void Qt3DCore::QGeometryView::instanceCountChanged(int
    instanceCount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qgeometryview.html#instanceCountChanged

    Parameters
    ----------

    instanceCount : int
      Passed on as it is.
    """
    #  void Qt3DCore::QGeometryView::instanceCountChanged(int instanceCount)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore13QGeometryView20instanceCountChangedEi',
        instanceCount,
    )

  @overload(int)
  def vertexCountChanged(self, vertexCount: int) -> None:
    """
    Calls Qt's 'void Qt3DCore::QGeometryView::vertexCountChanged(int
    vertexCount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qgeometryview.html#vertexCountChanged

    Parameters
    ----------

    vertexCount : int
      Passed on as it is.
    """
    #  void Qt3DCore::QGeometryView::vertexCountChanged(int vertexCount)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore13QGeometryView18vertexCountChangedEi',
        vertexCount,
    )

  @overload(int)
  def indexOffsetChanged(self, indexOffset: int) -> None:
    """
    Calls Qt's 'void Qt3DCore::QGeometryView::indexOffsetChanged(int
    indexOffset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qgeometryview.html#indexOffsetChanged

    Parameters
    ----------

    indexOffset : int
      Passed on as it is.
    """
    #  void Qt3DCore::QGeometryView::indexOffsetChanged(int indexOffset)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore13QGeometryView18indexOffsetChangedEi',
        indexOffset,
    )

  @overload(int)
  def firstInstanceChanged(self, firstInstance: int) -> None:
    """
    Calls Qt's 'void Qt3DCore::QGeometryView::firstInstanceChanged(int
    firstInstance)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qgeometryview.html#firstInstanceChanged

    Parameters
    ----------

    firstInstance : int
      Passed on as it is.
    """
    #  void Qt3DCore::QGeometryView::firstInstanceChanged(int firstInstance)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore13QGeometryView20firstInstanceChangedEi',
        firstInstance,
    )

  @overload(int)
  def firstVertexChanged(self, firstVertex: int) -> None:
    """
    Calls Qt's 'void Qt3DCore::QGeometryView::firstVertexChanged(int
    firstVertex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qgeometryview.html#firstVertexChanged

    Parameters
    ----------

    firstVertex : int
      Passed on as it is.
    """
    #  void Qt3DCore::QGeometryView::firstVertexChanged(int firstVertex)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore13QGeometryView18firstVertexChangedEi',
        firstVertex,
    )

  @overload(int)
  def indexBufferByteOffsetChanged(self, offset: int) -> None:
    """
    Calls Qt's 'void
    Qt3DCore::QGeometryView::indexBufferByteOffsetChanged(int offset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qgeometryview.html

    Parameters
    ----------

    offset : int
      Passed on as it is.
    """
    #  void Qt3DCore::QGeometryView::indexBufferByteOffsetChanged(int offset)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore13QGeometryView28indexBufferByteOffsetChangedEi',
        offset,
    )

  @overload(int)
  def restartIndexValueChanged(self, restartIndexValue: int) -> None:
    """
    Calls Qt's 'void Qt3DCore::QGeometryView::restartIndexValueChanged(int
    restartIndexValue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qgeometryview.html

    Parameters
    ----------

    restartIndexValue : int
      Passed on as it is.
    """
    #  void Qt3DCore::QGeometryView::restartIndexValueChanged(int
    #      restartIndexValue)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore13QGeometryView24restartIndexValueChangedEi',
        restartIndexValue,
    )

  @overload(int)
  def verticesPerPatchChanged(self, verticesPerPatch: int) -> None:
    """
    Calls Qt's 'void Qt3DCore::QGeometryView::verticesPerPatchChanged(int
    verticesPerPatch)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qgeometryview.html

    Parameters
    ----------

    verticesPerPatch : int
      Passed on as it is.
    """
    #  void Qt3DCore::QGeometryView::verticesPerPatchChanged(int
    #      verticesPerPatch)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore13QGeometryView23verticesPerPatchChangedEi',
        verticesPerPatch,
    )

  @overload(bool)
  def primitiveRestartEnabledChanged(
      self,
      primitiveRestartEnabled: bool,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DCore::QGeometryView::primitiveRestartEnabledChanged(bool
    primitiveRestartEnabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qgeometryview.html

    Parameters
    ----------

    primitiveRestartEnabled : bool
      Passed on as it is.
    """
    #  void Qt3DCore::QGeometryView::primitiveRestartEnabledChanged(bool
    #      primitiveRestartEnabled)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore13QGeometryView30primitiveRestartEnabledChangedE'
        'b',
        primitiveRestartEnabled,
    )

  @overload(WAIT['Qt3DCore.QGeometry'])
  @overload(NoneType)
  def geometryChanged(self, geometry: Optional[Qt3DCore.QGeometry]) -> None:
    """
    Calls Qt's 'void Qt3DCore::QGeometryView::geometryChanged(QGeometry
    *geometry)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qgeometryview.html#geometryChanged

    Parameters
    ----------

    geometry : Optional[Qt3DCore.QGeometry]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DCore::QGeometryView::geometryChanged(QGeometry *geometry)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore13QGeometryView15geometryChangedEPNS_9QGeometryE',
        self._addressOf(geometry),
    )

  @overload(PrimitiveType)
  def primitiveTypeChanged(self, primitiveType: PrimitiveType) -> None:
    """
    Calls Qt's 'void
    Qt3DCore::QGeometryView::primitiveTypeChanged(PrimitiveType
    primitiveType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qgeometryview.html#primitiveTypeChanged

    Parameters
    ----------

    primitiveType : PrimitiveType
      Passed on as its number.
    """
    #  void Qt3DCore::QGeometryView::primitiveTypeChanged(PrimitiveType
    #      primitiveType)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore13QGeometryView20primitiveTypeChangedENS0_13Prim'
        'itiveTypeE',
        primitiveType.value,
    )

  def d_func(self) -> Optional[Qt3DCore.QGeometryViewPrivate]:
    """
    Calls Qt's 'QGeometryViewPrivate *Qt3DCore::QGeometryView::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qgeometryview.html#d_func

    Returns
    -------

    Optional[Qt3DCore.QGeometryViewPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGeometryViewPrivate *Qt3DCore::QGeometryView::d_func()
    address = self.uglySide.call(
        'ritual_ZN8Qt3DCore13QGeometryView6d_funcEv',
    )
    return Qt3DCore.QGeometryViewPrivate._cuteAt(address)

  @staticmethod
  def geometryFactory(*__, **_) -> Never:
    """
    Qt's 'QGeometryFactoryPtr Qt3DCore::QGeometryView::geometryFactory()
    const': cannot be called and cannot be called through the meta-object and
    cannot be copied: no header file has its code, Qt's source does not mark
    it or its class for use from outside Qt or writes it 'inline' or nowhere,
    and it is no signal, slot or invokable function giving back nothing, of a
    class built on QObject, and Qt's source has no code for it that could be
    told from the rest.
    """
    raise NotImplementedError(
        "'Qt3DCore.QGeometryView.geometryFactory' has no cute function yet. "
        "Qt's 'QGeometryFactoryPtr "
        "Qt3DCore::QGeometryView::geometryFactory() const': cannot be "
        "called and cannot be called through the meta-object and cannot be "
        "copied: no header file has its code, Qt's source does not mark it "
        "or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")

  @staticmethod
  def setGeometryFactory(*__, **_) -> Never:
    """
    Qt's 'void Qt3DCore::QGeometryView::setGeometryFactory(const
    QGeometryFactoryPtr &factory)': cannot be called and cannot be called
    through the meta-object and cannot be copied: no header file has its
    code, Qt's source does not mark it or its class for use from outside Qt
    or writes it 'inline' or nowhere, and it is no signal, slot or invokable
    function giving back nothing, of a class built on QObject, and Qt's
    source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'Qt3DCore.QGeometryView.setGeometryFactory' has no cute function "
        "yet. Qt's 'void Qt3DCore::QGeometryView::setGeometryFactory(const "
        "QGeometryFactoryPtr &factory)': cannot be called and cannot be "
        "called through the meta-object and cannot be copied: no header "
        "file has its code, Qt's source does not mark it or its class for "
        "use from outside Qt or writes it 'inline' or nowhere, and it is no "
        "signal, slot or invokable function giving back nothing, of a class "
        "built on QObject, and Qt's source has no code for it that could be "
        "told from the rest.")
