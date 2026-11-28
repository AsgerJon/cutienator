"""
Qt3DRender::QGeometryRenderer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/qgeometryrenderer.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGeometryRenderer(Qt3DCore.QBoundingVolume):
  """
  The cute side of Qt's Qt3DRender::QGeometryRenderer: a plain Python object
  standing in front of one C++ Qt3DRender::QGeometryRenderer.

  It is built on the cute 'Qt3DCore::QBoundingVolume', as Qt's
  Qt3DRender::QGeometryRenderer is built on Qt's Qt3DCore::QBoundingVolume,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QGeometryRenderer that has a ritual and
  that Python can call so far, 39 names in all: 'metaObject', 'tr',
  'instanceCount', 'vertexCount', 'indexOffset', 'firstInstance',
  'firstVertex', 'indexBufferByteOffset', 'restartIndexValue',
  'verticesPerPatch', 'primitiveRestartEnabled', 'geometry', 'primitiveType',
  'sortIndex', 'setInstanceCount', 'setVertexCount', 'setIndexOffset',
  'setFirstInstance', 'setFirstVertex', 'setIndexBufferByteOffset',
  'setRestartIndexValue', 'setVerticesPerPatch',
  'setPrimitiveRestartEnabled', 'setGeometry', 'setPrimitiveType',
  'setSortIndex', 'instanceCountChanged', 'vertexCountChanged',
  'indexOffsetChanged', 'firstInstanceChanged', 'firstVertexChanged',
  'indexBufferByteOffsetChanged', 'restartIndexValueChanged',
  'verticesPerPatchChanged', 'primitiveRestartEnabledChanged',
  'geometryChanged', 'primitiveTypeChanged', 'sortIndexChanged', 'd_func'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DRender::QGeometryRenderer::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int Qt3DRender::QGeometryRenderer::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DRender::QGeometryRenderer::~QGeometryRenderer()': the
    destructor: Python never removes a C++ Qt3DRender::QGeometryRenderer.
  - Qt's 'Qt3DRender::QGeometryRenderer::QGeometryRenderer(
    QGeometryRendererPrivate &dd, Qt3DCore::QNode *parent)': takes a type
    Python has no way to hand over yet.
  - Qt's 'const QGeometryRendererPrivate
    *Qt3DRender::QGeometryRenderer::d_func() const': takes in Python what
    'QGeometryRendererPrivate *Qt3DRender::QGeometryRenderer::d_func()'
    takes.

  What has no ritual
  ------------------

  2 of the 47 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DRender::QGeometryRenderer is created at the first use, not by
    'Qt3DRender::QGeometryRenderer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::QGeometryRenderer.
  - Qt tells when it has removed the C++ Qt3DRender::QGeometryRenderer. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside Qt3DRender::QGeometryRenderer, each a class
  #  in here as in C++, and the names Qt has for the combinations of its
  #  flags enums.

  class PrimitiveType(CuteNum):
    """
    The enum 'Qt3DRender::QGeometryRenderer::PrimitiveType' of Qt, with the
    12 names Qt gives in it.
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
    Calls Qt's 'QString Qt3DRender::QGeometryRenderer::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qgeometryrenderer.html#tr

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
    #  QString Qt3DRender::QGeometryRenderer::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN10Qt3DRender17QGeometryRenderer2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::QGeometryRenderer'

  #  A C++ Qt3DRender::QGeometryRenderer Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_QGeometryRenderer'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *Qt3DRender::QGeometryRenderer::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qgeometryrenderer.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DRender::QGeometryRenderer::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender17QGeometryRenderer10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def instanceCount(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::QGeometryRenderer::instanceCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qgeometryrenderer.html#instanceCount
    """
    #  int Qt3DRender::QGeometryRenderer::instanceCount() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender17QGeometryRenderer13instanceCountEv',
    )

  def vertexCount(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::QGeometryRenderer::vertexCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qgeometryrenderer.html#vertexCount
    """
    #  int Qt3DRender::QGeometryRenderer::vertexCount() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender17QGeometryRenderer11vertexCountEv',
    )

  def indexOffset(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::QGeometryRenderer::indexOffset() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qgeometryrenderer.html#indexOffset
    """
    #  int Qt3DRender::QGeometryRenderer::indexOffset() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender17QGeometryRenderer11indexOffsetEv',
    )

  def firstInstance(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::QGeometryRenderer::firstInstance() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qgeometryrenderer.html#firstInstance
    """
    #  int Qt3DRender::QGeometryRenderer::firstInstance() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender17QGeometryRenderer13firstInstanceEv',
    )

  def firstVertex(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::QGeometryRenderer::firstVertex() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qgeometryrenderer.html#firstVertex
    """
    #  int Qt3DRender::QGeometryRenderer::firstVertex() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender17QGeometryRenderer11firstVertexEv',
    )

  def indexBufferByteOffset(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::QGeometryRenderer::indexBufferByteOffset()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qgeometryrenderer.html
    """
    #  int Qt3DRender::QGeometryRenderer::indexBufferByteOffset() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender17QGeometryRenderer21indexBufferByteOffsetEv',
    )

  def restartIndexValue(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::QGeometryRenderer::restartIndexValue()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qgeometryrenderer.html
    """
    #  int Qt3DRender::QGeometryRenderer::restartIndexValue() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender17QGeometryRenderer17restartIndexValueEv',
    )

  def verticesPerPatch(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::QGeometryRenderer::verticesPerPatch() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qgeometryrenderer.html#verticesPerPatch
    """
    #  int Qt3DRender::QGeometryRenderer::verticesPerPatch() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender17QGeometryRenderer16verticesPerPatchEv',
    )

  def primitiveRestartEnabled(self) -> bool:
    """
    Calls Qt's 'bool Qt3DRender::QGeometryRenderer::primitiveRestartEnabled()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qgeometryrenderer.html
    """
    #  bool Qt3DRender::QGeometryRenderer::primitiveRestartEnabled() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender17QGeometryRenderer23primitiveRestartEnabled'
        'Ev',
    )

  def geometry(self) -> Optional[Qt3DCore.QGeometry]:
    """
    Calls Qt's 'Qt3DCore::QGeometry
    *Qt3DRender::QGeometryRenderer::geometry() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qgeometryrenderer.html#geometry

    Returns
    -------

    Optional[Qt3DCore.QGeometry]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Qt3DCore::QGeometry *Qt3DRender::QGeometryRenderer::geometry() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender17QGeometryRenderer8geometryEv',
    )
    return Qt3DCore.QGeometry._cuteAt(address)

  def primitiveType(self) -> PrimitiveType:
    """
    Calls Qt's 'PrimitiveType Qt3DRender::QGeometryRenderer::primitiveType()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qgeometryrenderer.html#primitiveType

    Returns
    -------

    PrimitiveType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'PrimitiveType(number)'
      gives.
    """
    #  PrimitiveType Qt3DRender::QGeometryRenderer::primitiveType() const
    return QGeometryRenderer.PrimitiveType(self.uglySide.call(
        'ritual_ZNK10Qt3DRender17QGeometryRenderer13primitiveTypeEv',
    ))

  def sortIndex(self) -> float:
    """
    Calls Qt's 'float Qt3DRender::QGeometryRenderer::sortIndex() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qgeometryrenderer.html#sortIndex
    """
    #  float Qt3DRender::QGeometryRenderer::sortIndex() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender17QGeometryRenderer9sortIndexEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setInstanceCount(self, instanceCount: int) -> None:
    """
    Calls Qt's 'void Qt3DRender::QGeometryRenderer::setInstanceCount(int
    instanceCount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qgeometryrenderer.html#setInstanceCount

    Parameters
    ----------

    instanceCount : int
      Passed on as it is.
    """
    #  void Qt3DRender::QGeometryRenderer::setInstanceCount(int
    #      instanceCount)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender17QGeometryRenderer16setInstanceCountEi',
        instanceCount,
    )

  @overload(int)
  def setVertexCount(self, vertexCount: int) -> None:
    """
    Calls Qt's 'void Qt3DRender::QGeometryRenderer::setVertexCount(int
    vertexCount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qgeometryrenderer.html#setVertexCount

    Parameters
    ----------

    vertexCount : int
      Passed on as it is.
    """
    #  void Qt3DRender::QGeometryRenderer::setVertexCount(int vertexCount)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender17QGeometryRenderer14setVertexCountEi',
        vertexCount,
    )

  @overload(int)
  def setIndexOffset(self, indexOffset: int) -> None:
    """
    Calls Qt's 'void Qt3DRender::QGeometryRenderer::setIndexOffset(int
    indexOffset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qgeometryrenderer.html#setIndexOffset

    Parameters
    ----------

    indexOffset : int
      Passed on as it is.
    """
    #  void Qt3DRender::QGeometryRenderer::setIndexOffset(int indexOffset)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender17QGeometryRenderer14setIndexOffsetEi',
        indexOffset,
    )

  @overload(int)
  def setFirstInstance(self, firstInstance: int) -> None:
    """
    Calls Qt's 'void Qt3DRender::QGeometryRenderer::setFirstInstance(int
    firstInstance)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qgeometryrenderer.html#setFirstInstance

    Parameters
    ----------

    firstInstance : int
      Passed on as it is.
    """
    #  void Qt3DRender::QGeometryRenderer::setFirstInstance(int
    #      firstInstance)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender17QGeometryRenderer16setFirstInstanceEi',
        firstInstance,
    )

  @overload(int)
  def setFirstVertex(self, firstVertex: int) -> None:
    """
    Calls Qt's 'void Qt3DRender::QGeometryRenderer::setFirstVertex(int
    firstVertex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qgeometryrenderer.html#setFirstVertex

    Parameters
    ----------

    firstVertex : int
      Passed on as it is.
    """
    #  void Qt3DRender::QGeometryRenderer::setFirstVertex(int firstVertex)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender17QGeometryRenderer14setFirstVertexEi',
        firstVertex,
    )

  @overload(int)
  def setIndexBufferByteOffset(self, offset: int) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QGeometryRenderer::setIndexBufferByteOffset(int offset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qgeometryrenderer.html

    Parameters
    ----------

    offset : int
      Passed on as it is.
    """
    #  void Qt3DRender::QGeometryRenderer::setIndexBufferByteOffset(int
    #      offset)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender17QGeometryRenderer24setIndexBufferByteOffset'
        'Ei',
        offset,
    )

  @overload(int)
  def setRestartIndexValue(self, index: int) -> None:
    """
    Calls Qt's 'void Qt3DRender::QGeometryRenderer::setRestartIndexValue(int
    index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qgeometryrenderer.html

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void Qt3DRender::QGeometryRenderer::setRestartIndexValue(int index)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender17QGeometryRenderer20setRestartIndexValueEi',
        index,
    )

  @overload(int)
  def setVerticesPerPatch(self, verticesPerPatch: int) -> None:
    """
    Calls Qt's 'void Qt3DRender::QGeometryRenderer::setVerticesPerPatch(int
    verticesPerPatch)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qgeometryrenderer.html

    Parameters
    ----------

    verticesPerPatch : int
      Passed on as it is.
    """
    #  void Qt3DRender::QGeometryRenderer::setVerticesPerPatch(int
    #      verticesPerPatch)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender17QGeometryRenderer19setVerticesPerPatchEi',
        verticesPerPatch,
    )

  @overload(bool)
  def setPrimitiveRestartEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QGeometryRenderer::setPrimitiveRestartEnabled(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qgeometryrenderer.html

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void Qt3DRender::QGeometryRenderer::setPrimitiveRestartEnabled(bool
    #      enabled)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender17QGeometryRenderer26setPrimitiveRestartEnabl'
        'edEb',
        enabled,
    )

  @overload(WAIT['Qt3DCore.QGeometry'])
  @overload(NoneType)
  def setGeometry(self, geometry: Optional[Qt3DCore.QGeometry]) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QGeometryRenderer::setGeometry(Qt3DCore::QGeometry
    *geometry)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qgeometryrenderer.html#setGeometry

    Parameters
    ----------

    geometry : Optional[Qt3DCore.QGeometry]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::QGeometryRenderer::setGeometry(Qt3DCore::QGeometry
    #      *geometry)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender17QGeometryRenderer11setGeometryEPN8Qt3DCore9'
        'QGeometryE',
        self._addressOf(geometry),
    )

  @overload(PrimitiveType)
  def setPrimitiveType(self, primitiveType: PrimitiveType) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QGeometryRenderer::setPrimitiveType(PrimitiveType
    primitiveType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qgeometryrenderer.html#setPrimitiveType

    Parameters
    ----------

    primitiveType : PrimitiveType
      Passed on as its number.
    """
    #  void Qt3DRender::QGeometryRenderer::setPrimitiveType(PrimitiveType
    #      primitiveType)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender17QGeometryRenderer16setPrimitiveTypeENS0_13P'
        'rimitiveTypeE',
        primitiveType.value,
    )

  @overload(float)
  def setSortIndex(self, sortIndex: float) -> None:
    """
    Calls Qt's 'void Qt3DRender::QGeometryRenderer::setSortIndex(float
    sortIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qgeometryrenderer.html#setSortIndex

    Parameters
    ----------

    sortIndex : float
      Passed on as it is.
    """
    #  void Qt3DRender::QGeometryRenderer::setSortIndex(float sortIndex)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender17QGeometryRenderer12setSortIndexEf',
        sortIndex,
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
    'Qt3DRender::QGeometryRenderer::QGeometryRenderer(Qt3DCore::QNode
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qgeometryrenderer.html

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DRender::QGeometryRenderer::QGeometryRenderer(Qt3DCore::QNode
    #      *parent)
    self._noteCreation(QGeometryRenderer, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender17QGeometryRendererC1EPN8Qt3DCore5QNodeE',
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
    Calls Qt's 'void Qt3DRender::QGeometryRenderer::instanceCountChanged(int
    instanceCount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qgeometryrenderer.html

    Parameters
    ----------

    instanceCount : int
      Passed on as it is.
    """
    #  void Qt3DRender::QGeometryRenderer::instanceCountChanged(int
    #      instanceCount)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender17QGeometryRenderer20instanceCountChangedEi',
        instanceCount,
    )

  @overload(int)
  def vertexCountChanged(self, vertexCount: int) -> None:
    """
    Calls Qt's 'void Qt3DRender::QGeometryRenderer::vertexCountChanged(int
    vertexCount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qgeometryrenderer.html

    Parameters
    ----------

    vertexCount : int
      Passed on as it is.
    """
    #  void Qt3DRender::QGeometryRenderer::vertexCountChanged(int
    #      vertexCount)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender17QGeometryRenderer18vertexCountChangedEi',
        vertexCount,
    )

  @overload(int)
  def indexOffsetChanged(self, indexOffset: int) -> None:
    """
    Calls Qt's 'void Qt3DRender::QGeometryRenderer::indexOffsetChanged(int
    indexOffset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qgeometryrenderer.html

    Parameters
    ----------

    indexOffset : int
      Passed on as it is.
    """
    #  void Qt3DRender::QGeometryRenderer::indexOffsetChanged(int
    #      indexOffset)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender17QGeometryRenderer18indexOffsetChangedEi',
        indexOffset,
    )

  @overload(int)
  def firstInstanceChanged(self, firstInstance: int) -> None:
    """
    Calls Qt's 'void Qt3DRender::QGeometryRenderer::firstInstanceChanged(int
    firstInstance)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qgeometryrenderer.html

    Parameters
    ----------

    firstInstance : int
      Passed on as it is.
    """
    #  void Qt3DRender::QGeometryRenderer::firstInstanceChanged(int
    #      firstInstance)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender17QGeometryRenderer20firstInstanceChangedEi',
        firstInstance,
    )

  @overload(int)
  def firstVertexChanged(self, firstVertex: int) -> None:
    """
    Calls Qt's 'void Qt3DRender::QGeometryRenderer::firstVertexChanged(int
    firstVertex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qgeometryrenderer.html

    Parameters
    ----------

    firstVertex : int
      Passed on as it is.
    """
    #  void Qt3DRender::QGeometryRenderer::firstVertexChanged(int
    #      firstVertex)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender17QGeometryRenderer18firstVertexChangedEi',
        firstVertex,
    )

  @overload(int)
  def indexBufferByteOffsetChanged(self, offset: int) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QGeometryRenderer::indexBufferByteOffsetChanged(int offset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qgeometryrenderer.html

    Parameters
    ----------

    offset : int
      Passed on as it is.
    """
    #  void Qt3DRender::QGeometryRenderer::indexBufferByteOffsetChanged(int
    #      offset)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender17QGeometryRenderer28indexBufferByteOffsetCha'
        'ngedEi',
        offset,
    )

  @overload(int)
  def restartIndexValueChanged(self, restartIndexValue: int) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QGeometryRenderer::restartIndexValueChanged(int
    restartIndexValue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qgeometryrenderer.html

    Parameters
    ----------

    restartIndexValue : int
      Passed on as it is.
    """
    #  void Qt3DRender::QGeometryRenderer::restartIndexValueChanged(int
    #      restartIndexValue)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender17QGeometryRenderer24restartIndexValueChanged'
        'Ei',
        restartIndexValue,
    )

  @overload(int)
  def verticesPerPatchChanged(self, verticesPerPatch: int) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QGeometryRenderer::verticesPerPatchChanged(int
    verticesPerPatch)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qgeometryrenderer.html

    Parameters
    ----------

    verticesPerPatch : int
      Passed on as it is.
    """
    #  void Qt3DRender::QGeometryRenderer::verticesPerPatchChanged(int
    #      verticesPerPatch)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender17QGeometryRenderer23verticesPerPatchChangedE'
        'i',
        verticesPerPatch,
    )

  @overload(bool)
  def primitiveRestartEnabledChanged(
      self,
      primitiveRestartEnabled: bool,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QGeometryRenderer::primitiveRestartEnabledChanged(bool
    primitiveRestartEnabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qgeometryrenderer.html

    Parameters
    ----------

    primitiveRestartEnabled : bool
      Passed on as it is.
    """
    #  void
    #      Qt3DRender::QGeometryRenderer::primitiveRestartEnabledChanged(bool
    #      primitiveRestartEnabled)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender17QGeometryRenderer30primitiveRestartEnabledC'
        'hangedEb',
        primitiveRestartEnabled,
    )

  @overload(WAIT['Qt3DCore.QGeometry'])
  @overload(NoneType)
  def geometryChanged(self, geometry: Optional[Qt3DCore.QGeometry]) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QGeometryRenderer::geometryChanged(Qt3DCore::QGeometry
    *geometry)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qgeometryrenderer.html#geometryChanged

    Parameters
    ----------

    geometry : Optional[Qt3DCore.QGeometry]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void
    #      Qt3DRender::QGeometryRenderer::geometryChanged(Qt3DCore::QGeometry
    #      *geometry)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender17QGeometryRenderer15geometryChangedEPN8Qt3DC'
        'ore9QGeometryE',
        self._addressOf(geometry),
    )

  @overload(PrimitiveType)
  def primitiveTypeChanged(self, primitiveType: PrimitiveType) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QGeometryRenderer::primitiveTypeChanged(PrimitiveType
    primitiveType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qgeometryrenderer.html

    Parameters
    ----------

    primitiveType : PrimitiveType
      Passed on as its number.
    """
    #  void Qt3DRender::QGeometryRenderer::primitiveTypeChanged(PrimitiveType
    #      primitiveType)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender17QGeometryRenderer20primitiveTypeChangedENS0'
        '_13PrimitiveTypeE',
        primitiveType.value,
    )

  @overload(float)
  def sortIndexChanged(self, sortIndex: float) -> None:
    """
    Calls Qt's 'void Qt3DRender::QGeometryRenderer::sortIndexChanged(float
    sortIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qgeometryrenderer.html#sortIndexChanged

    Parameters
    ----------

    sortIndex : float
      Passed on as it is.
    """
    #  void Qt3DRender::QGeometryRenderer::sortIndexChanged(float sortIndex)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender17QGeometryRenderer16sortIndexChangedEf',
        sortIndex,
    )

  def d_func(self) -> Optional[Qt3DRender.QGeometryRendererPrivate]:
    """
    Calls Qt's 'QGeometryRendererPrivate
    *Qt3DRender::QGeometryRenderer::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qgeometryrenderer.html#d_func

    Returns
    -------

    Optional[Qt3DRender.QGeometryRendererPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGeometryRendererPrivate *Qt3DRender::QGeometryRenderer::d_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender17QGeometryRenderer6d_funcEv',
    )
    return Qt3DRender.QGeometryRendererPrivate._cuteAt(address)
