"""
QCborStreamReader binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qcborstreamreader.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QByteArray, QCborError, QIODevice, qfloat16
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QIODevice = WAIT['QIODevice']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QCborStreamReader(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QCborStreamReader: a plain Python object standing in
  front of one C++ QCborStreamReader.

  What exists
  -----------

  Every function of Qt's QCborStreamReader that has a ritual and that Python
  can call so far, 47 names in all: 'setDevice', 'device', 'addData',
  'reparse', 'clear', 'reset', 'lastError', 'currentOffset', 'isValid',
  'containerDepth', 'parentContainerType', 'hasNext', 'next', 'type',
  'isUnsignedInteger', 'isNegativeInteger', 'isInteger', 'isByteArray',
  'isString', 'isArray', 'isMap', 'isTag', 'isSimpleType', 'isFloat16',
  'isFloat', 'isDouble', 'isInvalid', 'isFalse', 'isTrue', 'isBool',
  'isNull', 'isUndefined', 'isLengthKnown', 'length', 'isContainer',
  'enterContainer', 'leaveContainer', 'currentStringChunkSize', 'toBool',
  'toUnsignedInteger', 'toFloat16', 'toFloat', 'toDouble', 'toInteger',
  'readAllString', 'readAllUtf8String', 'readAllByteArray'. It can be made
  from Python, in 4 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QCborStreamReader::~QCborStreamReader()': the destructor: Python
    never removes a C++ QCborStreamReader.
  - Qt's 'bool QCborStreamReader::isSimpleType(QCborSimpleType st) const':
    names the enum 'QCborSimpleType', whose class cannot be named here.
  - Qt's 'QCborTag QCborStreamReader::toTag() const': gives the enum
    'QCborTag', whose class cannot be named here.
  - Qt's 'QCborNegativeInteger QCborStreamReader::toNegativeInteger() const':
    gives the enum 'QCborNegativeInteger', whose class cannot be named here.
  - Qt's 'QCborSimpleType QCborStreamReader::toSimpleType() const': gives the
    enum 'QCborSimpleType', whose class cannot be named here.

  What has no ritual
  ------------------

  24 of the 81 functions Qt declares: 10 private; 9 takes or gives a type
  that cannot be passed yet; 2 a template; 2 forbidden; 1 declared and
  nowhere to be found.

  What to expect
  --------------

  - The C++ QCborStreamReader is created at the first use, not by
    'QCborStreamReader(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QCborStreamReader.
  """

  #  The enums Qt writes inside QCborStreamReader, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class StringResultCode(CuteNum):
    """
    The enum 'QCborStreamReader::StringResultCode' of Qt, with the 3 names Qt
    gives in it.
    """

    EndOfString = Kee[int](0)
    Ok = Kee[int](1)
    Error = Kee[int](-1)

  class Type(CuteNum):
    """
    The enum 'QCborStreamReader::Type' of Qt, with the 15 names Qt gives in
    it.
    """

    UnsignedInteger = Kee[int](0)
    NegativeInteger = Kee[int](32)
    ByteString = Kee[int](64)
    ByteArray = Kee[int](64)
    TextString = Kee[int](96)
    String = Kee[int](96)
    Array = Kee[int](128)
    Map = Kee[int](160)
    Tag = Kee[int](192)
    SimpleType = Kee[int](224)
    HalfFloat = Kee[int](249)
    Float16 = Kee[int](249)
    Float = Kee[int](250)
    Double = Kee[int](251)
    Invalid = Kee[int](255)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCborStreamReader'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def device(self) -> Optional[QIODevice]:
    """
    Calls Qt's 'QIODevice *QCborStreamReader::device() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborstreamreader.html#device

    Returns
    -------

    Optional[QIODevice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QIODevice *QCborStreamReader::device() const
    address = self.uglySide.call('ritual_ZNK17QCborStreamReader6deviceEv')
    from . import QIODevice
    return QIODevice._cuteAt(address)

  def lastError(self) -> QCborError:
    """
    Calls Qt's 'QCborError QCborStreamReader::lastError() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborstreamreader.html#lastError

    Returns
    -------

    QCborError
      A new cute QCborError around the copy Qt gave back. Python owns it.
    """
    #  QCborError QCborStreamReader::lastError() const
    address = self.uglySide.call('ritual_ZNK17QCborStreamReader9lastErrorEv')
    from . import QCborError
    return QCborError._cuteOwning(address)

  def currentOffset(self) -> int:
    """
    Calls Qt's 'qint64 QCborStreamReader::currentOffset() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcborstreamreader.html#currentOffset
    """
    #  qint64 QCborStreamReader::currentOffset() const
    return self.uglySide.call(
        'ritual_ZNK17QCborStreamReader13currentOffsetEv',
    )

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QCborStreamReader::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborstreamreader.html#isValid
    """
    #  bool QCborStreamReader::isValid() const
    return self.uglySide.call('ritual_ZNK17QCborStreamReader7isValidEv')

  def containerDepth(self) -> int:
    """
    Calls Qt's 'int QCborStreamReader::containerDepth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcborstreamreader.html#containerDepth
    """
    #  int QCborStreamReader::containerDepth() const
    return self.uglySide.call(
        'ritual_ZNK17QCborStreamReader14containerDepthEv',
    )

  def parentContainerType(self) -> Type:
    """
    Calls Qt's 'QCborStreamReader::Type
    QCborStreamReader::parentContainerType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcborstreamreader.html#parentContainerType

    Returns
    -------

    Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Type(number)' gives.
    """
    #  QCborStreamReader::Type QCborStreamReader::parentContainerType() const
    return QCborStreamReader.Type(self.uglySide.call(
        'ritual_ZNK17QCborStreamReader19parentContainerTypeEv',
    ))

  def hasNext(self) -> bool:
    """
    Calls Qt's 'bool QCborStreamReader::hasNext() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborstreamreader.html#hasNext
    """
    #  bool QCborStreamReader::hasNext() const
    return self.uglySide.call('ritual_ZNK17QCborStreamReader7hasNextEv')

  def type(self) -> Type:
    """
    Calls Qt's 'Type QCborStreamReader::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborstreamreader.html#type

    Returns
    -------

    Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Type(number)' gives.
    """
    #  Type QCborStreamReader::type() const
    return QCborStreamReader.Type(self.uglySide.call(
        'ritual_ZNK17QCborStreamReader4typeEv',
    ))

  def isUnsignedInteger(self) -> bool:
    """
    Calls Qt's 'bool QCborStreamReader::isUnsignedInteger() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcborstreamreader.html#isUnsignedInteger
    """
    #  bool QCborStreamReader::isUnsignedInteger() const
    return self.uglySide.call(
        'ritual_ZNK17QCborStreamReader17isUnsignedIntegerEv',
    )

  def isNegativeInteger(self) -> bool:
    """
    Calls Qt's 'bool QCborStreamReader::isNegativeInteger() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcborstreamreader.html#isNegativeInteger
    """
    #  bool QCborStreamReader::isNegativeInteger() const
    return self.uglySide.call(
        'ritual_ZNK17QCborStreamReader17isNegativeIntegerEv',
    )

  def isInteger(self) -> bool:
    """
    Calls Qt's 'bool QCborStreamReader::isInteger() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborstreamreader.html#isInteger
    """
    #  bool QCborStreamReader::isInteger() const
    return self.uglySide.call('ritual_ZNK17QCborStreamReader9isIntegerEv')

  def isByteArray(self) -> bool:
    """
    Calls Qt's 'bool QCborStreamReader::isByteArray() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborstreamreader.html#isByteArray
    """
    #  bool QCborStreamReader::isByteArray() const
    return self.uglySide.call('ritual_ZNK17QCborStreamReader11isByteArrayEv')

  def isString(self) -> bool:
    """
    Calls Qt's 'bool QCborStreamReader::isString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborstreamreader.html#isString
    """
    #  bool QCborStreamReader::isString() const
    return self.uglySide.call('ritual_ZNK17QCborStreamReader8isStringEv')

  def isArray(self) -> bool:
    """
    Calls Qt's 'bool QCborStreamReader::isArray() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborstreamreader.html#isArray
    """
    #  bool QCborStreamReader::isArray() const
    return self.uglySide.call('ritual_ZNK17QCborStreamReader7isArrayEv')

  def isMap(self) -> bool:
    """
    Calls Qt's 'bool QCborStreamReader::isMap() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborstreamreader.html#isMap
    """
    #  bool QCborStreamReader::isMap() const
    return self.uglySide.call('ritual_ZNK17QCborStreamReader5isMapEv')

  def isTag(self) -> bool:
    """
    Calls Qt's 'bool QCborStreamReader::isTag() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborstreamreader.html#isTag
    """
    #  bool QCborStreamReader::isTag() const
    return self.uglySide.call('ritual_ZNK17QCborStreamReader5isTagEv')

  def isSimpleType(self) -> bool:
    """
    Calls Qt's 'bool QCborStreamReader::isSimpleType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcborstreamreader.html#isSimpleType
    """
    #  bool QCborStreamReader::isSimpleType() const
    return self.uglySide.call(
        'ritual_ZNK17QCborStreamReader12isSimpleTypeEv',
    )

  def isFloat16(self) -> bool:
    """
    Calls Qt's 'bool QCborStreamReader::isFloat16() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborstreamreader.html#isFloat16
    """
    #  bool QCborStreamReader::isFloat16() const
    return self.uglySide.call('ritual_ZNK17QCborStreamReader9isFloat16Ev')

  def isFloat(self) -> bool:
    """
    Calls Qt's 'bool QCborStreamReader::isFloat() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborstreamreader.html#isFloat
    """
    #  bool QCborStreamReader::isFloat() const
    return self.uglySide.call('ritual_ZNK17QCborStreamReader7isFloatEv')

  def isDouble(self) -> bool:
    """
    Calls Qt's 'bool QCborStreamReader::isDouble() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborstreamreader.html#isDouble
    """
    #  bool QCborStreamReader::isDouble() const
    return self.uglySide.call('ritual_ZNK17QCborStreamReader8isDoubleEv')

  def isInvalid(self) -> bool:
    """
    Calls Qt's 'bool QCborStreamReader::isInvalid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborstreamreader.html#isInvalid
    """
    #  bool QCborStreamReader::isInvalid() const
    return self.uglySide.call('ritual_ZNK17QCborStreamReader9isInvalidEv')

  def isFalse(self) -> bool:
    """
    Calls Qt's 'bool QCborStreamReader::isFalse() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborstreamreader.html#isFalse
    """
    #  bool QCborStreamReader::isFalse() const
    return self.uglySide.call('ritual_ZNK17QCborStreamReader7isFalseEv')

  def isTrue(self) -> bool:
    """
    Calls Qt's 'bool QCborStreamReader::isTrue() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborstreamreader.html#isTrue
    """
    #  bool QCborStreamReader::isTrue() const
    return self.uglySide.call('ritual_ZNK17QCborStreamReader6isTrueEv')

  def isBool(self) -> bool:
    """
    Calls Qt's 'bool QCborStreamReader::isBool() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborstreamreader.html#isBool
    """
    #  bool QCborStreamReader::isBool() const
    return self.uglySide.call('ritual_ZNK17QCborStreamReader6isBoolEv')

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QCborStreamReader::isNull() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborstreamreader.html#isNull
    """
    #  bool QCborStreamReader::isNull() const
    return self.uglySide.call('ritual_ZNK17QCborStreamReader6isNullEv')

  def isUndefined(self) -> bool:
    """
    Calls Qt's 'bool QCborStreamReader::isUndefined() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborstreamreader.html#isUndefined
    """
    #  bool QCborStreamReader::isUndefined() const
    return self.uglySide.call('ritual_ZNK17QCborStreamReader11isUndefinedEv')

  def isLengthKnown(self) -> bool:
    """
    Calls Qt's 'bool QCborStreamReader::isLengthKnown() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcborstreamreader.html#isLengthKnown
    """
    #  bool QCborStreamReader::isLengthKnown() const
    return self.uglySide.call(
        'ritual_ZNK17QCborStreamReader13isLengthKnownEv',
    )

  def length(self) -> int:
    """
    Calls Qt's 'quint64 QCborStreamReader::length() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborstreamreader.html#length
    """
    #  quint64 QCborStreamReader::length() const
    return self.uglySide.call('ritual_ZNK17QCborStreamReader6lengthEv')

  def isContainer(self) -> bool:
    """
    Calls Qt's 'bool QCborStreamReader::isContainer() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborstreamreader.html#isContainer
    """
    #  bool QCborStreamReader::isContainer() const
    return self.uglySide.call('ritual_ZNK17QCborStreamReader11isContainerEv')

  def currentStringChunkSize(self) -> int:
    """
    Calls Qt's 'qsizetype QCborStreamReader::currentStringChunkSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcborstreamreader.html#currentStringChunkSize
    """
    #  qsizetype QCborStreamReader::currentStringChunkSize() const
    return self.uglySide.call(
        'ritual_ZNK17QCborStreamReader22currentStringChunkSizeEv',
    )

  def toBool(self) -> bool:
    """
    Calls Qt's 'bool QCborStreamReader::toBool() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborstreamreader.html#toBool
    """
    #  bool QCborStreamReader::toBool() const
    return self.uglySide.call('ritual_ZNK17QCborStreamReader6toBoolEv')

  def toUnsignedInteger(self) -> int:
    """
    Calls Qt's 'quint64 QCborStreamReader::toUnsignedInteger() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcborstreamreader.html#toUnsignedInteger
    """
    #  quint64 QCborStreamReader::toUnsignedInteger() const
    return self.uglySide.call(
        'ritual_ZNK17QCborStreamReader17toUnsignedIntegerEv',
    )

  def toFloat16(self) -> qfloat16:
    """
    Calls Qt's 'qfloat16 QCborStreamReader::toFloat16() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborstreamreader.html#toFloat16

    Returns
    -------

    qfloat16
      A new cute qfloat16 around the copy Qt gave back. Python owns it.
    """
    #  qfloat16 QCborStreamReader::toFloat16() const
    address = self.uglySide.call('ritual_ZNK17QCborStreamReader9toFloat16Ev')
    from . import qfloat16
    return qfloat16._cuteOwning(address)

  def toFloat(self) -> float:
    """
    Calls Qt's 'float QCborStreamReader::toFloat() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborstreamreader.html#toFloat
    """
    #  float QCborStreamReader::toFloat() const
    return self.uglySide.call('ritual_ZNK17QCborStreamReader7toFloatEv')

  def toDouble(self) -> float:
    """
    Calls Qt's 'double QCborStreamReader::toDouble() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborstreamreader.html#toDouble
    """
    #  double QCborStreamReader::toDouble() const
    return self.uglySide.call('ritual_ZNK17QCborStreamReader8toDoubleEv')

  def toInteger(self) -> int:
    """
    Calls Qt's 'qint64 QCborStreamReader::toInteger() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborstreamreader.html#toInteger
    """
    #  qint64 QCborStreamReader::toInteger() const
    return self.uglySide.call('ritual_ZNK17QCborStreamReader9toIntegerEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QIODevice)
  @overload(NoneType)
  def setDevice(self, device: Optional[QIODevice]) -> None:
    """
    Calls Qt's 'void QCborStreamReader::setDevice(QIODevice *device)'.

    Qt's own words: https://doc.qt.io/qt-6/qcborstreamreader.html#setDevice

    Parameters
    ----------

    device : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QCborStreamReader::setDevice(QIODevice *device)
    self.uglySide.call(
        'ritual_ZN17QCborStreamReader9setDeviceEP9QIODevice',
        self._addressOf(device),
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
    Notes what was given, for Qt's 'QCborStreamReader::QCborStreamReader()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcborstreamreader.html#QCborStreamReader
    """
    #  QCborStreamReader::QCborStreamReader()
    self._noteCreation(QCborStreamReader, lambda: Rituals.call(
        'ritual_ZN17QCborStreamReaderC1Ev',
    ))

  @overload(str, int)
  @overload(NoneType, int)
  def __init__(self, data: Optional[str], len: int) -> None:
    """
    Notes what was given, for Qt's
    'QCborStreamReader::QCborStreamReader(const char *data, qsizetype len)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcborstreamreader.html#QCborStreamReader

    Parameters
    ----------

    data : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    len : int
      Passed on as it is.
    """
    #  QCborStreamReader::QCborStreamReader(const char *data, qsizetype len)
    self._noteCreation(QCborStreamReader, lambda: Rituals.call(
        'ritual_ZN17QCborStreamReaderC1EPKcx', self._bytesOf(data), len,
    ))

  @overload(QByteArray)
  def __init__(self, data: QByteArray) -> None:
    """
    Notes what was given, for Qt's
    'QCborStreamReader::QCborStreamReader(const QByteArray &data)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcborstreamreader.html#QCborStreamReader

    Parameters
    ----------

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  QCborStreamReader::QCborStreamReader(const QByteArray &data)
    self._noteCreation(QCborStreamReader, lambda: Rituals.call(
        'ritual_ZN17QCborStreamReaderC1ERK10QByteArray', self._valueOf(data),
    ))

  @overload(QIODevice)
  @overload(NoneType)
  def __init__(self, device: Optional[QIODevice]) -> None:
    """
    Notes what was given, for Qt's
    'QCborStreamReader::QCborStreamReader(QIODevice *device)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcborstreamreader.html#QCborStreamReader

    Parameters
    ----------

    device : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QCborStreamReader::QCborStreamReader(QIODevice *device)
    self._noteCreation(QCborStreamReader, lambda: Rituals.call(
        'ritual_ZN17QCborStreamReaderC1EP9QIODevice',
        self._addressOf(device),
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

  @overload(QByteArray)
  def addData(self, data: QByteArray) -> None:
    """
    Calls Qt's 'void QCborStreamReader::addData(const QByteArray &data)'.

    Qt's own words: https://doc.qt.io/qt-6/qcborstreamreader.html#addData

    Parameters
    ----------

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QCborStreamReader::addData(const QByteArray &data)
    self.uglySide.call(
        'ritual_ZN17QCborStreamReader7addDataERK10QByteArray',
        self._valueOf(data),
    )

  @overload(str, int)
  @overload(NoneType, int)
  def addData(self, data: Optional[str], len: int) -> None:
    """
    Calls Qt's 'void QCborStreamReader::addData(const char *data, qsizetype
    len)'.

    Qt's own words: https://doc.qt.io/qt-6/qcborstreamreader.html#addData

    Parameters
    ----------

    data : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    len : int
      Passed on as it is.
    """
    #  void QCborStreamReader::addData(const char *data, qsizetype len)
    self.uglySide.call(
        'ritual_ZN17QCborStreamReader7addDataEPKcx',
        self._bytesOf(data), len,
    )

  def reparse(self) -> None:
    """
    Calls Qt's 'void QCborStreamReader::reparse()'.

    Qt's own words: https://doc.qt.io/qt-6/qcborstreamreader.html#reparse
    """
    #  void QCborStreamReader::reparse()
    self.uglySide.call('ritual_ZN17QCborStreamReader7reparseEv')

  def clear(self) -> None:
    """
    Calls Qt's 'void QCborStreamReader::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qcborstreamreader.html#clear
    """
    #  void QCborStreamReader::clear()
    self.uglySide.call('ritual_ZN17QCborStreamReader5clearEv')

  def reset(self) -> None:
    """
    Calls Qt's 'void QCborStreamReader::reset()'.

    Qt's own words: https://doc.qt.io/qt-6/qcborstreamreader.html#reset
    """
    #  void QCborStreamReader::reset()
    self.uglySide.call('ritual_ZN17QCborStreamReader5resetEv')

  @overload()
  @overload(int)
  def next(self, maxRecursion: int = 10000) -> bool:
    """
    Calls Qt's 'bool QCborStreamReader::next(int maxRecursion)'.

    Qt's own words: https://doc.qt.io/qt-6/qcborstreamreader.html#next

    Parameters
    ----------

    maxRecursion : int
      Passed on as it is. May be left out, as in Qt: it is then 10000.
    """
    #  bool QCborStreamReader::next(int maxRecursion)
    return self.uglySide.call(
        'ritual_ZN17QCborStreamReader4nextEi', maxRecursion,
    )

  def enterContainer(self) -> bool:
    """
    Calls Qt's 'bool QCborStreamReader::enterContainer()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcborstreamreader.html#enterContainer
    """
    #  bool QCborStreamReader::enterContainer()
    return self.uglySide.call(
        'ritual_ZN17QCborStreamReader14enterContainerEv',
    )

  def leaveContainer(self) -> bool:
    """
    Calls Qt's 'bool QCborStreamReader::leaveContainer()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcborstreamreader.html#leaveContainer
    """
    #  bool QCborStreamReader::leaveContainer()
    return self.uglySide.call(
        'ritual_ZN17QCborStreamReader14leaveContainerEv',
    )

  def readAllString(self) -> str:
    """
    Calls Qt's 'QString QCborStreamReader::readAllString()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcborstreamreader.html#readAllString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QCborStreamReader::readAllString()
    return self.uglySide.call(
        'ritual_ZN17QCborStreamReader13readAllStringEv',
    )

  def readAllUtf8String(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QCborStreamReader::readAllUtf8String()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcborstreamreader.html#readAllUtf8String

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QCborStreamReader::readAllUtf8String()
    address = self.uglySide.call(
        'ritual_ZN17QCborStreamReader17readAllUtf8StringEv',
    )
    from . import QByteArray
    return QByteArray._cuteOwning(address)

  def readAllByteArray(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QCborStreamReader::readAllByteArray()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcborstreamreader.html#readAllByteArray

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QCborStreamReader::readAllByteArray()
    address = self.uglySide.call(
        'ritual_ZN17QCborStreamReader16readAllByteArrayEv',
    )
    from . import QByteArray
    return QByteArray._cuteOwning(address)
