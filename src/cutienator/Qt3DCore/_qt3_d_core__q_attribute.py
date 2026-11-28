"""
Qt3DCore::QAttribute binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DCore/qattribute.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from . import Qt3DCore

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAttribute(Qt3DCore.QNode):
  """
  The cute side of Qt's Qt3DCore::QAttribute: a plain Python object standing
  in front of one C++ Qt3DCore::QAttribute.

  It is built on the cute 'Qt3DCore::QNode', as Qt's Qt3DCore::QAttribute is
  built on Qt's Qt3DCore::QNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DCore::QAttribute that has a ritual and that
  Python can call so far, 41 names in all: 'metaObject', 'tr', 'buffer',
  'name', 'vertexBaseType', 'vertexSize', 'count', 'byteStride',
  'byteOffset', 'divisor', 'attributeType', 'defaultPositionAttributeName',
  'defaultNormalAttributeName', 'defaultColorAttributeName',
  'defaultTextureCoordinateAttributeName', 'defaultTangentAttributeName',
  'defaultJointIndicesAttributeName', 'defaultJointWeightsAttributeName',
  'defaultTextureCoordinate1AttributeName',
  'defaultTextureCoordinate2AttributeName', 'setBuffer', 'setName',
  'setVertexBaseType', 'setVertexSize', 'setCount', 'setByteStride',
  'setByteOffset', 'setDivisor', 'setAttributeType', 'bufferChanged',
  'nameChanged', 'vertexBaseTypeChanged', 'vertexSizeChanged',
  'dataTypeChanged', 'dataSizeChanged', 'countChanged', 'byteStrideChanged',
  'byteOffsetChanged', 'divisorChanged', 'attributeTypeChanged', 'd_func'. It
  can be made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DCore::QAttribute::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int Qt3DCore::QAttribute::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DCore::QAttribute::~QAttribute()': the destructor: Python never
    removes a C++ Qt3DCore::QAttribute.
  - Qt's 'const QAttributePrivate *Qt3DCore::QAttribute::d_func() const':
    takes in Python what 'QAttributePrivate *Qt3DCore::QAttribute::d_func()'
    takes.

  What has no ritual
  ------------------

  2 of the 50 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DCore::QAttribute is created at the first use, not by
    'Qt3DCore::QAttribute(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DCore::QAttribute.
  - Qt tells when it has removed the C++ Qt3DCore::QAttribute. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside Qt3DCore::QAttribute, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class AttributeType(CuteNum):
    """
    The enum 'Qt3DCore::QAttribute::AttributeType' of Qt, with the 3 names Qt
    gives in it.
    """

    VertexAttribute = Kee[int](0)
    IndexAttribute = Kee[int](1)
    DrawIndirectAttribute = Kee[int](2)

  class VertexBaseType(CuteNum):
    """
    The enum 'Qt3DCore::QAttribute::VertexBaseType' of Qt, with the 9 names
    Qt gives in it.
    """

    Byte = Kee[int](0)
    UnsignedByte = Kee[int](1)
    Short = Kee[int](2)
    UnsignedShort = Kee[int](3)
    Int = Kee[int](4)
    UnsignedInt = Kee[int](5)
    HalfFloat = Kee[int](6)
    Float = Kee[int](7)
    Double = Kee[int](8)

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
    Calls Qt's 'QString Qt3DCore::QAttribute::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qattribute.html#tr

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
    #  QString Qt3DCore::QAttribute::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN8Qt3DCore10QAttribute2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def defaultPositionAttributeName() -> str:
    """
    Calls Qt's 'QString
    Qt3DCore::QAttribute::defaultPositionAttributeName()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qattribute.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString Qt3DCore::QAttribute::defaultPositionAttributeName()
    return Rituals.call(
        'ritual_ZN8Qt3DCore10QAttribute28defaultPositionAttributeNameEv',
    )

  @staticmethod
  def defaultNormalAttributeName() -> str:
    """
    Calls Qt's 'QString Qt3DCore::QAttribute::defaultNormalAttributeName()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qattribute.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString Qt3DCore::QAttribute::defaultNormalAttributeName()
    return Rituals.call(
        'ritual_ZN8Qt3DCore10QAttribute26defaultNormalAttributeNameEv',
    )

  @staticmethod
  def defaultColorAttributeName() -> str:
    """
    Calls Qt's 'QString Qt3DCore::QAttribute::defaultColorAttributeName()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qattribute.html#defaultColorAttributeName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString Qt3DCore::QAttribute::defaultColorAttributeName()
    return Rituals.call(
        'ritual_ZN8Qt3DCore10QAttribute25defaultColorAttributeNameEv',
    )

  @staticmethod
  def defaultTextureCoordinateAttributeName() -> str:
    """
    Calls Qt's 'QString
    Qt3DCore::QAttribute::defaultTextureCoordinateAttributeName()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qattribute.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString Qt3DCore::QAttribute::defaultTextureCoordinateAttributeName()
    return Rituals.call(
        'ritual_ZN8Qt3DCore10QAttribute37defaultTextureCoordinateAttributeN'
        'ameEv',
    )

  @staticmethod
  def defaultTangentAttributeName() -> str:
    """
    Calls Qt's 'QString Qt3DCore::QAttribute::defaultTangentAttributeName()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qattribute.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString Qt3DCore::QAttribute::defaultTangentAttributeName()
    return Rituals.call(
        'ritual_ZN8Qt3DCore10QAttribute27defaultTangentAttributeNameEv',
    )

  @staticmethod
  def defaultJointIndicesAttributeName() -> str:
    """
    Calls Qt's 'QString
    Qt3DCore::QAttribute::defaultJointIndicesAttributeName()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qattribute.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString Qt3DCore::QAttribute::defaultJointIndicesAttributeName()
    return Rituals.call(
        'ritual_ZN8Qt3DCore10QAttribute32defaultJointIndicesAttributeNameEv',
    )

  @staticmethod
  def defaultJointWeightsAttributeName() -> str:
    """
    Calls Qt's 'QString
    Qt3DCore::QAttribute::defaultJointWeightsAttributeName()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qattribute.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString Qt3DCore::QAttribute::defaultJointWeightsAttributeName()
    return Rituals.call(
        'ritual_ZN8Qt3DCore10QAttribute32defaultJointWeightsAttributeNameEv',
    )

  @staticmethod
  def defaultTextureCoordinate1AttributeName() -> str:
    """
    Calls Qt's 'QString
    Qt3DCore::QAttribute::defaultTextureCoordinate1AttributeName()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qattribute.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString Qt3DCore::QAttribute::defaultTextureCoordinate1AttributeName()
    return Rituals.call(
        'ritual_ZN8Qt3DCore10QAttribute38defaultTextureCoordinate1Attribute'
        'NameEv',
    )

  @staticmethod
  def defaultTextureCoordinate2AttributeName() -> str:
    """
    Calls Qt's 'QString
    Qt3DCore::QAttribute::defaultTextureCoordinate2AttributeName()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qattribute.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString Qt3DCore::QAttribute::defaultTextureCoordinate2AttributeName()
    return Rituals.call(
        'ritual_ZN8Qt3DCore10QAttribute38defaultTextureCoordinate2Attribute'
        'NameEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DCore::QAttribute'

  #  A C++ Qt3DCore::QAttribute Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DCore_QAttribute'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DCore::QAttribute::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qattribute.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DCore::QAttribute::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore10QAttribute10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def buffer(self) -> Optional[Qt3DCore.QBuffer]:
    """
    Calls Qt's 'QBuffer *Qt3DCore::QAttribute::buffer() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qattribute.html#buffer

    Returns
    -------

    Optional[Qt3DCore.QBuffer]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QBuffer *Qt3DCore::QAttribute::buffer() const
    address = self.uglySide.call('ritual_ZNK8Qt3DCore10QAttribute6bufferEv')
    return Qt3DCore.QBuffer._cuteAt(address)

  def name(self) -> str:
    """
    Calls Qt's 'QString Qt3DCore::QAttribute::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qattribute.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString Qt3DCore::QAttribute::name() const
    return self.uglySide.call('ritual_ZNK8Qt3DCore10QAttribute4nameEv')

  def vertexBaseType(self) -> VertexBaseType:
    """
    Calls Qt's 'VertexBaseType Qt3DCore::QAttribute::vertexBaseType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qattribute.html#vertexBaseType

    Returns
    -------

    VertexBaseType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'VertexBaseType(number)'
      gives.
    """
    #  VertexBaseType Qt3DCore::QAttribute::vertexBaseType() const
    return QAttribute.VertexBaseType(self.uglySide.call(
        'ritual_ZNK8Qt3DCore10QAttribute14vertexBaseTypeEv',
    ))

  def vertexSize(self) -> int:
    """
    Calls Qt's 'uint Qt3DCore::QAttribute::vertexSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qattribute.html#vertexSize
    """
    #  uint Qt3DCore::QAttribute::vertexSize() const
    return self.uglySide.call(
        'ritual_ZNK8Qt3DCore10QAttribute10vertexSizeEv',
    )

  def count(self) -> int:
    """
    Calls Qt's 'uint Qt3DCore::QAttribute::count() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qattribute.html#count
    """
    #  uint Qt3DCore::QAttribute::count() const
    return self.uglySide.call('ritual_ZNK8Qt3DCore10QAttribute5countEv')

  def byteStride(self) -> int:
    """
    Calls Qt's 'uint Qt3DCore::QAttribute::byteStride() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qattribute.html#byteStride
    """
    #  uint Qt3DCore::QAttribute::byteStride() const
    return self.uglySide.call(
        'ritual_ZNK8Qt3DCore10QAttribute10byteStrideEv',
    )

  def byteOffset(self) -> int:
    """
    Calls Qt's 'uint Qt3DCore::QAttribute::byteOffset() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qattribute.html#byteOffset
    """
    #  uint Qt3DCore::QAttribute::byteOffset() const
    return self.uglySide.call(
        'ritual_ZNK8Qt3DCore10QAttribute10byteOffsetEv',
    )

  def divisor(self) -> int:
    """
    Calls Qt's 'uint Qt3DCore::QAttribute::divisor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qattribute.html#divisor
    """
    #  uint Qt3DCore::QAttribute::divisor() const
    return self.uglySide.call('ritual_ZNK8Qt3DCore10QAttribute7divisorEv')

  def attributeType(self) -> AttributeType:
    """
    Calls Qt's 'AttributeType Qt3DCore::QAttribute::attributeType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qattribute.html#attributeType

    Returns
    -------

    AttributeType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'AttributeType(number)'
      gives.
    """
    #  AttributeType Qt3DCore::QAttribute::attributeType() const
    return QAttribute.AttributeType(self.uglySide.call(
        'ritual_ZNK8Qt3DCore10QAttribute13attributeTypeEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['Qt3DCore.QBuffer'])
  @overload(NoneType)
  def setBuffer(self, buffer: Optional[Qt3DCore.QBuffer]) -> None:
    """
    Calls Qt's 'void Qt3DCore::QAttribute::setBuffer(QBuffer *buffer)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qattribute.html#setBuffer

    Parameters
    ----------

    buffer : Optional[Qt3DCore.QBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DCore::QAttribute::setBuffer(QBuffer *buffer)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore10QAttribute9setBufferEPNS_7QBufferE',
        self._addressOf(buffer),
    )

  @overload(str)
  def setName(self, name: str) -> None:
    """
    Calls Qt's 'void Qt3DCore::QAttribute::setName(const QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qattribute.html#setName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void Qt3DCore::QAttribute::setName(const QString &name)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore10QAttribute7setNameERK7QString', name,
    )

  @overload(VertexBaseType)
  def setVertexBaseType(self, type: VertexBaseType) -> None:
    """
    Calls Qt's 'void Qt3DCore::QAttribute::setVertexBaseType(VertexBaseType
    type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qattribute.html#setVertexBaseType

    Parameters
    ----------

    type : VertexBaseType
      Passed on as its number.
    """
    #  void Qt3DCore::QAttribute::setVertexBaseType(VertexBaseType type)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore10QAttribute17setVertexBaseTypeENS0_14VertexBase'
        'TypeE',
        type.value,
    )

  @overload(int)
  def setVertexSize(self, size: int) -> None:
    """
    Calls Qt's 'void Qt3DCore::QAttribute::setVertexSize(uint size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qattribute.html#setVertexSize

    Parameters
    ----------

    size : int
      Passed on as it is.
    """
    #  void Qt3DCore::QAttribute::setVertexSize(uint size)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore10QAttribute13setVertexSizeEj', size,
    )

  @overload(int)
  def setCount(self, count: int) -> None:
    """
    Calls Qt's 'void Qt3DCore::QAttribute::setCount(uint count)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qattribute.html#setCount

    Parameters
    ----------

    count : int
      Passed on as it is.
    """
    #  void Qt3DCore::QAttribute::setCount(uint count)
    self.uglySide.call('ritual_ZN8Qt3DCore10QAttribute8setCountEj', count)

  @overload(int)
  def setByteStride(self, byteStride: int) -> None:
    """
    Calls Qt's 'void Qt3DCore::QAttribute::setByteStride(uint byteStride)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qattribute.html#setByteStride

    Parameters
    ----------

    byteStride : int
      Passed on as it is.
    """
    #  void Qt3DCore::QAttribute::setByteStride(uint byteStride)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore10QAttribute13setByteStrideEj', byteStride,
    )

  @overload(int)
  def setByteOffset(self, byteOffset: int) -> None:
    """
    Calls Qt's 'void Qt3DCore::QAttribute::setByteOffset(uint byteOffset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qattribute.html#setByteOffset

    Parameters
    ----------

    byteOffset : int
      Passed on as it is.
    """
    #  void Qt3DCore::QAttribute::setByteOffset(uint byteOffset)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore10QAttribute13setByteOffsetEj', byteOffset,
    )

  @overload(int)
  def setDivisor(self, divisor: int) -> None:
    """
    Calls Qt's 'void Qt3DCore::QAttribute::setDivisor(uint divisor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qattribute.html#setDivisor

    Parameters
    ----------

    divisor : int
      Passed on as it is.
    """
    #  void Qt3DCore::QAttribute::setDivisor(uint divisor)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore10QAttribute10setDivisorEj', divisor,
    )

  @overload(AttributeType)
  def setAttributeType(self, attributeType: AttributeType) -> None:
    """
    Calls Qt's 'void Qt3DCore::QAttribute::setAttributeType(AttributeType
    attributeType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qattribute.html#setAttributeType

    Parameters
    ----------

    attributeType : AttributeType
      Passed on as its number.
    """
    #  void Qt3DCore::QAttribute::setAttributeType(AttributeType
    #      attributeType)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore10QAttribute16setAttributeTypeENS0_13AttributeTy'
        'peE',
        attributeType.value,
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
    Notes what was given, for Qt's 'Qt3DCore::QAttribute::QAttribute(QNode
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qattribute.html#QAttribute

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DCore::QAttribute::QAttribute(QNode *parent)
    self._noteCreation(QAttribute, lambda: Rituals.call(
        'ritual_ZN8Qt3DCore10QAttributeC1EPNS_5QNodeE',
        self._addressOf(parent),
    ))

  @overload(WAIT['Qt3DCore.QBuffer'], VertexBaseType, int, int)
  @overload(NoneType, VertexBaseType, int, int)
  @overload(WAIT['Qt3DCore.QBuffer'], VertexBaseType, int, int, int)
  @overload(NoneType, VertexBaseType, int, int, int)
  @overload(WAIT['Qt3DCore.QBuffer'], VertexBaseType, int, int, int, int)
  @overload(NoneType, VertexBaseType, int, int, int, int)
  @overload(
      WAIT['Qt3DCore.QBuffer'], VertexBaseType, int, int, int, int,
      Qt3DCore.QNode,
  )
  @overload(
      WAIT['Qt3DCore.QBuffer'], VertexBaseType, int, int, int, int, NoneType,
  )
  @overload(NoneType, VertexBaseType, int, int, int, int, Qt3DCore.QNode)
  @overload(NoneType, VertexBaseType, int, int, int, int, NoneType)
  def __init__(
      self,
      buf: Optional[Qt3DCore.QBuffer],
      vertexBaseType: VertexBaseType,
      vertexSize: int,
      count: int,
      offset: int = 0,
      stride: int = 0,
      parent: Optional[Qt3DCore.QNode] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'Qt3DCore::QAttribute::QAttribute(QBuffer
    *buf, VertexBaseType vertexBaseType, uint vertexSize, uint count, uint
    offset, uint stride, QNode *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qattribute.html#QAttribute

    Parameters
    ----------

    buf : Optional[Qt3DCore.QBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    vertexBaseType : VertexBaseType
      Passed on as its number.

    vertexSize : int
      Passed on as it is.

    count : int
      Passed on as it is.

    offset : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    stride : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DCore::QAttribute::QAttribute(QBuffer *buf, VertexBaseType
    #      vertexBaseType, uint vertexSize, uint count, uint offset, uint
    #      stride, QNode *parent)
    self._noteCreation(QAttribute, lambda: Rituals.call(
        'ritual_ZN8Qt3DCore10QAttributeC1EPNS_7QBufferENS0_14VertexBaseType'
        'EjjjjPNS_5QNodeE',
        self._addressOf(buf), vertexBaseType.value, vertexSize, count,
        offset, stride, self._addressOf(parent),
    ))

  @overload(WAIT['Qt3DCore.QBuffer'], str, VertexBaseType, int, int)
  @overload(NoneType, str, VertexBaseType, int, int)
  @overload(WAIT['Qt3DCore.QBuffer'], str, VertexBaseType, int, int, int)
  @overload(NoneType, str, VertexBaseType, int, int, int)
  @overload(
      WAIT['Qt3DCore.QBuffer'], str, VertexBaseType, int, int, int, int,
  )
  @overload(NoneType, str, VertexBaseType, int, int, int, int)
  @overload(
      WAIT['Qt3DCore.QBuffer'], str, VertexBaseType, int, int, int, int,
      Qt3DCore.QNode,
  )
  @overload(
      WAIT['Qt3DCore.QBuffer'], str, VertexBaseType, int, int, int, int,
      NoneType,
  )
  @overload(
      NoneType, str, VertexBaseType, int, int, int, int, Qt3DCore.QNode,
  )
  @overload(NoneType, str, VertexBaseType, int, int, int, int, NoneType)
  def __init__(
      self,
      buf: Optional[Qt3DCore.QBuffer],
      name: str,
      vertexBaseType: VertexBaseType,
      vertexSize: int,
      count: int,
      offset: int = 0,
      stride: int = 0,
      parent: Optional[Qt3DCore.QNode] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'Qt3DCore::QAttribute::QAttribute(QBuffer
    *buf, const QString &name, VertexBaseType vertexBaseType, uint
    vertexSize, uint count, uint offset, uint stride, QNode *parent)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qattribute.html#QAttribute

    Parameters
    ----------

    buf : Optional[Qt3DCore.QBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    name : str
      Passed on as it is: a QString is made of it for the call.

    vertexBaseType : VertexBaseType
      Passed on as its number.

    vertexSize : int
      Passed on as it is.

    count : int
      Passed on as it is.

    offset : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    stride : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DCore::QAttribute::QAttribute(QBuffer *buf, const QString &name,
    #      VertexBaseType vertexBaseType, uint vertexSize, uint count, uint
    #      offset, uint stride, QNode *parent)
    self._noteCreation(QAttribute, lambda: Rituals.call(
        'ritual_ZN8Qt3DCore10QAttributeC1EPNS_7QBufferERK7QStringNS0_14Vert'
        'exBaseTypeEjjjjPNS_5QNodeE',
        self._addressOf(buf), name, vertexBaseType.value, vertexSize, count,
        offset, stride, self._addressOf(parent),
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

  @overload(WAIT['Qt3DCore.QBuffer'])
  @overload(NoneType)
  def bufferChanged(self, buffer: Optional[Qt3DCore.QBuffer]) -> None:
    """
    Calls Qt's 'void Qt3DCore::QAttribute::bufferChanged(QBuffer *buffer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qattribute.html#bufferChanged

    Parameters
    ----------

    buffer : Optional[Qt3DCore.QBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DCore::QAttribute::bufferChanged(QBuffer *buffer)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore10QAttribute13bufferChangedEPNS_7QBufferE',
        self._addressOf(buffer),
    )

  @overload(str)
  def nameChanged(self, name: str) -> None:
    """
    Calls Qt's 'void Qt3DCore::QAttribute::nameChanged(const QString &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qattribute.html#nameChanged

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void Qt3DCore::QAttribute::nameChanged(const QString &name)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore10QAttribute11nameChangedERK7QString', name,
    )

  @overload(VertexBaseType)
  def vertexBaseTypeChanged(self, vertexBaseType: VertexBaseType) -> None:
    """
    Calls Qt's 'void
    Qt3DCore::QAttribute::vertexBaseTypeChanged(VertexBaseType
    vertexBaseType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qattribute.html#vertexBaseTypeChanged

    Parameters
    ----------

    vertexBaseType : VertexBaseType
      Passed on as its number.
    """
    #  void Qt3DCore::QAttribute::vertexBaseTypeChanged(VertexBaseType
    #      vertexBaseType)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore10QAttribute21vertexBaseTypeChangedENS0_14Vertex'
        'BaseTypeE',
        vertexBaseType.value,
    )

  @overload(int)
  def vertexSizeChanged(self, vertexSize: int) -> None:
    """
    Calls Qt's 'void Qt3DCore::QAttribute::vertexSizeChanged(uint
    vertexSize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qattribute.html#vertexSizeChanged

    Parameters
    ----------

    vertexSize : int
      Passed on as it is.
    """
    #  void Qt3DCore::QAttribute::vertexSizeChanged(uint vertexSize)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore10QAttribute17vertexSizeChangedEj', vertexSize,
    )

  @overload(VertexBaseType)
  def dataTypeChanged(self, vertexBaseType: VertexBaseType) -> None:
    """
    Calls Qt's 'void Qt3DCore::QAttribute::dataTypeChanged(VertexBaseType
    vertexBaseType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qattribute.html#dataTypeChanged

    Parameters
    ----------

    vertexBaseType : VertexBaseType
      Passed on as its number.
    """
    #  void Qt3DCore::QAttribute::dataTypeChanged(VertexBaseType
    #      vertexBaseType)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore10QAttribute15dataTypeChangedENS0_14VertexBaseTy'
        'peE',
        vertexBaseType.value,
    )

  @overload(int)
  def dataSizeChanged(self, vertexSize: int) -> None:
    """
    Calls Qt's 'void Qt3DCore::QAttribute::dataSizeChanged(uint vertexSize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qattribute.html#dataSizeChanged

    Parameters
    ----------

    vertexSize : int
      Passed on as it is.
    """
    #  void Qt3DCore::QAttribute::dataSizeChanged(uint vertexSize)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore10QAttribute15dataSizeChangedEj', vertexSize,
    )

  @overload(int)
  def countChanged(self, count: int) -> None:
    """
    Calls Qt's 'void Qt3DCore::QAttribute::countChanged(uint count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qattribute.html#countChanged

    Parameters
    ----------

    count : int
      Passed on as it is.
    """
    #  void Qt3DCore::QAttribute::countChanged(uint count)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore10QAttribute12countChangedEj', count,
    )

  @overload(int)
  def byteStrideChanged(self, byteStride: int) -> None:
    """
    Calls Qt's 'void Qt3DCore::QAttribute::byteStrideChanged(uint
    byteStride)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qattribute.html#byteStrideChanged

    Parameters
    ----------

    byteStride : int
      Passed on as it is.
    """
    #  void Qt3DCore::QAttribute::byteStrideChanged(uint byteStride)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore10QAttribute17byteStrideChangedEj', byteStride,
    )

  @overload(int)
  def byteOffsetChanged(self, byteOffset: int) -> None:
    """
    Calls Qt's 'void Qt3DCore::QAttribute::byteOffsetChanged(uint
    byteOffset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qattribute.html#byteOffsetChanged

    Parameters
    ----------

    byteOffset : int
      Passed on as it is.
    """
    #  void Qt3DCore::QAttribute::byteOffsetChanged(uint byteOffset)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore10QAttribute17byteOffsetChangedEj', byteOffset,
    )

  @overload(int)
  def divisorChanged(self, divisor: int) -> None:
    """
    Calls Qt's 'void Qt3DCore::QAttribute::divisorChanged(uint divisor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qattribute.html#divisorChanged

    Parameters
    ----------

    divisor : int
      Passed on as it is.
    """
    #  void Qt3DCore::QAttribute::divisorChanged(uint divisor)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore10QAttribute14divisorChangedEj', divisor,
    )

  @overload(AttributeType)
  def attributeTypeChanged(self, attributeType: AttributeType) -> None:
    """
    Calls Qt's 'void Qt3DCore::QAttribute::attributeTypeChanged(AttributeType
    attributeType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qattribute.html#attributeTypeChanged

    Parameters
    ----------

    attributeType : AttributeType
      Passed on as its number.
    """
    #  void Qt3DCore::QAttribute::attributeTypeChanged(AttributeType
    #      attributeType)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore10QAttribute20attributeTypeChangedENS0_13Attribu'
        'teTypeE',
        attributeType.value,
    )

  def d_func(self) -> Optional[Qt3DCore.QAttributePrivate]:
    """
    Calls Qt's 'QAttributePrivate *Qt3DCore::QAttribute::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qattribute.html#d_func

    Returns
    -------

    Optional[Qt3DCore.QAttributePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAttributePrivate *Qt3DCore::QAttribute::d_func()
    address = self.uglySide.call('ritual_ZN8Qt3DCore10QAttribute6d_funcEv')
    return Qt3DCore.QAttributePrivate._cuteAt(address)
