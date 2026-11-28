"""
QModbusPdu binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSerialBus/qmodbuspdu.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QByteArray
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']


class QModbusPdu(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QModbusPdu: a plain Python object standing in front
  of one C++ QModbusPdu.

  What exists
  -----------

  Every function of Qt's QModbusPdu that has a ritual and that Python can
  call so far, 9 names in all: 'isValid', 'exceptionCode', 'isException',
  'size', 'dataSize', 'functionCode', 'setFunctionCode', 'data', 'setData'.
  It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QModbusPdu::~QModbusPdu()': the destructor: Python never removes a
    C++ QModbusPdu.
  - Qt's 'QModbusPdu::QModbusPdu(const QModbusPdu &a0)': takes a type Python
    has no way to hand over yet.
  - Qt's 'QModbusPdu &QModbusPdu::operator=(const QModbusPdu &a0)':
    assignment: Python binds a name and has no operator for it.

  What has no ritual
  ------------------

  8 of the 22 functions Qt declares: 8 a template.

  What to expect
  --------------

  - The C++ QModbusPdu is created at the first use, not by 'QModbusPdu(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QModbusPdu.
  - Each name of Qt's QModbusPdu that has no cute function yet, 'decode',
    'decodeData', 'encode', 'encodeData', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QModbusPdu, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class ExceptionCode(CuteNum):
    """
    The enum 'QModbusPdu::ExceptionCode' of Qt, with the 11 names Qt gives in
    it.
    """

    IllegalFunction = Kee[int](1)
    IllegalDataAddress = Kee[int](2)
    IllegalDataValue = Kee[int](3)
    ServerDeviceFailure = Kee[int](4)
    Acknowledge = Kee[int](5)
    ServerDeviceBusy = Kee[int](6)
    NegativeAcknowledge = Kee[int](7)
    MemoryParityError = Kee[int](8)
    GatewayPathUnavailable = Kee[int](10)
    GatewayTargetDeviceFailedToRespond = Kee[int](11)
    ExtendedException = Kee[int](255)

  class FunctionCode(CuteNum):
    """
    The enum 'QModbusPdu::FunctionCode' of Qt, with the 21 names Qt gives in
    it.
    """

    Invalid = Kee[int](0)
    ReadCoils = Kee[int](1)
    ReadDiscreteInputs = Kee[int](2)
    ReadHoldingRegisters = Kee[int](3)
    ReadInputRegisters = Kee[int](4)
    WriteSingleCoil = Kee[int](5)
    WriteSingleRegister = Kee[int](6)
    ReadExceptionStatus = Kee[int](7)
    Diagnostics = Kee[int](8)
    GetCommEventCounter = Kee[int](11)
    GetCommEventLog = Kee[int](12)
    WriteMultipleCoils = Kee[int](15)
    WriteMultipleRegisters = Kee[int](16)
    ReportServerId = Kee[int](17)
    ReadFileRecord = Kee[int](20)
    WriteFileRecord = Kee[int](21)
    MaskWriteRegister = Kee[int](22)
    ReadWriteMultipleRegisters = Kee[int](23)
    ReadFifoQueue = Kee[int](24)
    EncapsulatedInterfaceTransport = Kee[int](43)
    UndefinedFunctionCode = Kee[int](256)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QModbusPdu'

  #  A C++ QModbusPdu Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QModbusPdu'

  #  The functions Qt calls itself that QModbusPdu is the first to declare. A
  #  class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'setFunctionCode': (
          ('_ZN10QModbusPdu15setFunctionCodeENS_12FunctionCodeE',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum', 'QtSerialBus:QModbusPdu.FunctionCode'),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QModbusPdu::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmodbuspdu.html#isValid
    """
    #  bool QModbusPdu::isValid() const
    return self.uglySide.call('ritual_ZNK10QModbusPdu7isValidEv')

  def exceptionCode(self) -> ExceptionCode:
    """
    Calls Qt's 'ExceptionCode QModbusPdu::exceptionCode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmodbuspdu.html#exceptionCode

    Returns
    -------

    ExceptionCode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ExceptionCode(number)'
      gives.
    """
    #  ExceptionCode QModbusPdu::exceptionCode() const
    return QModbusPdu.ExceptionCode(self.uglySide.call(
        'ritual_ZNK10QModbusPdu13exceptionCodeEv',
    ))

  def isException(self) -> bool:
    """
    Calls Qt's 'bool QModbusPdu::isException() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmodbuspdu.html#isException
    """
    #  bool QModbusPdu::isException() const
    return self.uglySide.call('ritual_ZNK10QModbusPdu11isExceptionEv')

  def size(self) -> int:
    """
    Calls Qt's 'qint16 QModbusPdu::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmodbuspdu.html#size
    """
    #  qint16 QModbusPdu::size() const
    return self.uglySide.call('ritual_ZNK10QModbusPdu4sizeEv')

  def dataSize(self) -> int:
    """
    Calls Qt's 'qint16 QModbusPdu::dataSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmodbuspdu.html#dataSize
    """
    #  qint16 QModbusPdu::dataSize() const
    return self.uglySide.call('ritual_ZNK10QModbusPdu8dataSizeEv')

  def functionCode(self) -> FunctionCode:
    """
    Calls Qt's 'FunctionCode QModbusPdu::functionCode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmodbuspdu.html#functionCode

    Returns
    -------

    FunctionCode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'FunctionCode(number)'
      gives.
    """
    #  FunctionCode QModbusPdu::functionCode() const
    return QModbusPdu.FunctionCode(self.uglySide.call(
        'ritual_ZNK10QModbusPdu12functionCodeEv',
    ))

  def data(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QModbusPdu::data() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmodbuspdu.html#data

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QModbusPdu::data() const
    address = self.uglySide.call('ritual_ZNK10QModbusPdu4dataEv')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(FunctionCode)
  def setFunctionCode(self, code: FunctionCode) -> None:
    """
    Calls Qt's 'void QModbusPdu::setFunctionCode(FunctionCode code)'.

    Qt's own words: https://doc.qt.io/qt-6/qmodbuspdu.html#setFunctionCode

    Parameters
    ----------

    code : FunctionCode
      Passed on as its number.
    """
    #  void QModbusPdu::setFunctionCode(FunctionCode code)
    ritual = 'ritual_ZN10QModbusPdu15setFunctionCodeENS_12FunctionCodeE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10QModbusPdu15setFunctionCodeENS_12FunctionCodeE')
    self.uglySide.call(ritual, code.value)

  @overload(QByteArray)
  def setData(self, newData: QByteArray) -> None:
    """
    Calls Qt's 'void QModbusPdu::setData(const QByteArray &newData)'.

    Qt's own words: https://doc.qt.io/qt-6/qmodbuspdu.html#setData

    Parameters
    ----------

    newData : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QModbusPdu::setData(const QByteArray &newData)
    self.uglySide.call(
        'ritual_ZN10QModbusPdu7setDataERK10QByteArray',
        self._valueOf(newData),
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
    Notes what was given, for Qt's 'QModbusPdu::QModbusPdu()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qmodbuspdu.html#QModbusPdu
    """
    #  QModbusPdu::QModbusPdu()
    self._noteCreation(QModbusPdu, lambda: Rituals.call(
        'ritual_ZN10QModbusPduC1Ev',
    ))

  @overload(FunctionCode, QByteArray)
  def __init__(self, code: FunctionCode, newData: QByteArray) -> None:
    """
    Notes what was given, for Qt's 'QModbusPdu::QModbusPdu(FunctionCode code,
    const QByteArray &newData)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qmodbuspdu.html#QModbusPdu

    Parameters
    ----------

    code : FunctionCode
      Passed on as its number.

    newData : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  QModbusPdu::QModbusPdu(FunctionCode code, const QByteArray &newData)
    self._noteCreation(QModbusPdu, lambda: Rituals.call(
        'ritual_ZN10QModbusPduC1ENS_12FunctionCodeERK10QByteArray',
        code.value, self._valueOf(newData),
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
  def decode(*__, **_) -> Never:
    """
    Qt's 'QModbusPdu::decode': a template: a pattern and no single function.
    """
    raise NotImplementedError(
        "'QModbusPdu.decode' has no cute function yet. Qt's "
        "'QModbusPdu::decode': a template: a pattern and no single function."
    )

  @staticmethod
  def decodeData(*__, **_) -> Never:
    """
    Qt's 'QModbusPdu::decodeData': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QModbusPdu.decodeData' has no cute function yet. Qt's "
        "'QModbusPdu::decodeData': a template: a pattern and no single "
        "function.")

  @staticmethod
  def encode(*__, **_) -> Never:
    """
    Qt's 'QModbusPdu::encode': a template: a pattern and no single function.
    """
    raise NotImplementedError(
        "'QModbusPdu.encode' has no cute function yet. Qt's "
        "'QModbusPdu::encode': a template: a pattern and no single function."
    )

  @staticmethod
  def encodeData(*__, **_) -> Never:
    """
    Qt's 'QModbusPdu::encodeData': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QModbusPdu.encodeData' has no cute function yet. Qt's "
        "'QModbusPdu::encodeData': a template: a pattern and no single "
        "function.")
