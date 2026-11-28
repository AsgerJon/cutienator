"""
QModbusSerialAdu binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSerialBus/6.12.0/QtSerialBus/private/qmodbusadu_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QModbusSerialAdu to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QModbusSerialAdu(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QModbusSerialAdu: a plain Python object standing in
  front of one C++ QModbusSerialAdu.

  C++ hands a QModbusSerialAdu around as a copy, so every C++
  QModbusSerialAdu behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QModbusSerialAdu that has a ritual and that Python
  can call so far, 9 names in all: 'size', 'data', 'rawSize', 'rawData',
  'serverAddress', 'matchingChecksum', 'calculateLRC', 'calculateCRC',
  'crc_reflect'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QModbusPdu QModbusSerialAdu::pdu() const': gives a type Python has
    no way to take yet.
  - Qt's 'QByteArray QModbusSerialAdu::create(Type type, int serverAddress,
    const QModbusPdu &pdu, char delimiter)': takes a type Python has no way
    to hand over yet.
  - Qt's 'QModbusSerialAdu::~QModbusSerialAdu()': the destructor: Python
    removes its C++ QModbusSerialAdu by it, and has no other use for it.

  What has no ritual
  ------------------

  1 of the 14 functions Qt declares: 1 a template.

  What to expect
  --------------

  - The C++ QModbusSerialAdu is created at the first use, not by
    'QModbusSerialAdu(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QModbusSerialAdu back gives a copy the ritual made
    for Python, in a new cute QModbusSerialAdu.
  - Each name of Qt's QModbusSerialAdu that has no cute function yet,
    'checksum', 'create', 'pdu', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QModbusSerialAdu, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Type(CuteNum):
    """
    The enum 'QModbusSerialAdu::Type' of Qt, with the 2 names Qt gives in it.
    """

    Ascii = Kee[int](0)
    Rtu = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str, int)
  @overload(NoneType, int)
  def calculateLRC(data: Optional[str], len: int) -> int:
    """
    Calls Qt's 'quint8 QModbusSerialAdu::calculateLRC(const char *data,
    qint32 len)'.

    Qt's own words: https://doc.qt.io/qt-6/qmodbusserialadu.html#calculateLRC

    Parameters
    ----------

    data : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    len : int
      Passed on as it is.
    """
    #  quint8 QModbusSerialAdu::calculateLRC(const char *data, qint32 len)
    return Rituals.call(
        'ritual_ZN16QModbusSerialAdu12calculateLRCEPKci',
        CuteMixin._bytesOf(data), len,
    )

  @staticmethod
  @overload(str, int)
  @overload(NoneType, int)
  def calculateCRC(data: Optional[str], len: int) -> int:
    """
    Calls Qt's 'quint16 QModbusSerialAdu::calculateCRC(const char *data,
    qint32 len)'.

    Qt's own words: https://doc.qt.io/qt-6/qmodbusserialadu.html#calculateCRC

    Parameters
    ----------

    data : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    len : int
      Passed on as it is.
    """
    #  quint16 QModbusSerialAdu::calculateCRC(const char *data, qint32 len)
    return Rituals.call(
        'ritual_ZN16QModbusSerialAdu12calculateCRCEPKci',
        CuteMixin._bytesOf(data), len,
    )

  @staticmethod
  @overload(int, int)
  def crc_reflect(data: int, len: int) -> int:
    """
    Calls Qt's 'quint16 QModbusSerialAdu::crc_reflect(quint16 data, qint32
    len)'.

    Qt's own words: https://doc.qt.io/qt-6/qmodbusserialadu.html#crc_reflect

    Parameters
    ----------

    data : int
      Passed on as it is.

    len : int
      Passed on as it is.
    """
    #  quint16 QModbusSerialAdu::crc_reflect(quint16 data, qint32 len)
    return Rituals.call(
        'ritual_ZN16QModbusSerialAdu11crc_reflectEti', data, len,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QModbusSerialAdu'

  #  Qt's '~QModbusSerialAdu()'. Naming it makes this a value class: Python
  #  owns every C++ QModbusSerialAdu behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN16QModbusSerialAduD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def size(self) -> int:
    """
    Calls Qt's 'int QModbusSerialAdu::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmodbusserialadu.html#size
    """
    #  int QModbusSerialAdu::size() const
    return self.uglySide.call('ritual_ZNK16QModbusSerialAdu4sizeEv')

  def data(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QModbusSerialAdu::data() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmodbusserialadu.html#data

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QModbusSerialAdu::data() const
    address = self.uglySide.call('ritual_ZNK16QModbusSerialAdu4dataEv')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def rawSize(self) -> int:
    """
    Calls Qt's 'int QModbusSerialAdu::rawSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmodbusserialadu.html#rawSize
    """
    #  int QModbusSerialAdu::rawSize() const
    return self.uglySide.call('ritual_ZNK16QModbusSerialAdu7rawSizeEv')

  def rawData(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QModbusSerialAdu::rawData() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmodbusserialadu.html#rawData

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QModbusSerialAdu::rawData() const
    address = self.uglySide.call('ritual_ZNK16QModbusSerialAdu7rawDataEv')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def serverAddress(self) -> int:
    """
    Calls Qt's 'int QModbusSerialAdu::serverAddress() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmodbusserialadu.html#serverAddress
    """
    #  int QModbusSerialAdu::serverAddress() const
    return self.uglySide.call(
        'ritual_ZNK16QModbusSerialAdu13serverAddressEv',
    )

  def matchingChecksum(self) -> bool:
    """
    Calls Qt's 'bool QModbusSerialAdu::matchingChecksum() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmodbusserialadu.html#matchingChecksum
    """
    #  bool QModbusSerialAdu::matchingChecksum() const
    return self.uglySide.call(
        'ritual_ZNK16QModbusSerialAdu16matchingChecksumEv',
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

  @overload(Type, QByteArray)
  def __init__(self, type: Type, data: QByteArray) -> None:
    """
    Notes what was given, for Qt's 'QModbusSerialAdu::QModbusSerialAdu(Type
    type, const QByteArray &data)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qmodbusserialadu.html#QModbusSerialAdu

    Parameters
    ----------

    type : Type
      Passed on as its number.

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  QModbusSerialAdu::QModbusSerialAdu(Type type, const QByteArray &data)
    self._noteCreation(QModbusSerialAdu, lambda: Rituals.call(
        'ritual_ZN16QModbusSerialAduC1ENS_4TypeERK10QByteArray',
        type.value, self._valueOf(data),
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

  @staticmethod
  def checksum(*__, **_) -> Never:
    """
    Qt's 'QModbusSerialAdu::checksum': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QModbusSerialAdu.checksum' has no cute function yet. Qt's "
        "'QModbusSerialAdu::checksum': a template: a pattern and no single "
        "function.")

  @staticmethod
  def create(*__, **_) -> Never:
    """
    Qt's 'QByteArray QModbusSerialAdu::create(Type type, int serverAddress,
    const QModbusPdu &pdu, char delimiter)': takes a type Python has no way
    to hand over yet.
    """
    raise NotImplementedError(
        "'QModbusSerialAdu.create' has no cute function yet. Qt's "
        "'QByteArray QModbusSerialAdu::create(Type type, int serverAddress, "
        "const QModbusPdu &pdu, char delimiter)': takes a type Python has "
        "no way to hand over yet.")

  @staticmethod
  def pdu(*__, **_) -> Never:
    """
    Qt's 'QModbusPdu QModbusSerialAdu::pdu() const': gives a type Python has
    no way to take yet.
    """
    raise NotImplementedError(
        "'QModbusSerialAdu.pdu' has no cute function yet. Qt's 'QModbusPdu "
        "QModbusSerialAdu::pdu() const': gives a type Python has no way to "
        "take yet.")
