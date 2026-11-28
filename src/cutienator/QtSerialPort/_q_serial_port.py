"""
QSerialPort binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSerialPort/qserialport.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QIODevice, QIODeviceBase, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QSerialPortInfo, QSerialPortPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSerialPortInfo = WAIT['QSerialPortInfo']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSerialPort(QIODevice):
  """
  The cute side of Qt's QSerialPort: a plain Python object standing in front
  of one C++ QSerialPort.

  It is built on the cute 'QIODevice', as Qt's QSerialPort is built on Qt's
  QIODevice, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSerialPort that has a ritual and that Python can
  call so far, 53 names in all: 'metaObject', 'tr', 'd_func', 'setPortName',
  'portName', 'setPort', 'open', 'close', 'setBaudRate', 'baudRate',
  'setDataBits', 'dataBits', 'setParity', 'parity', 'setStopBits',
  'stopBits', 'setFlowControl', 'flowControl', 'setDataTerminalReady',
  'isDataTerminalReady', 'setRequestToSend', 'isRequestToSend',
  'pinoutSignals', 'flush', 'clear', 'error', 'clearError', 'readBufferSize',
  'setReadBufferSize', 'writeBufferSize', 'setWriteBufferSize',
  'isSequential', 'bytesAvailable', 'bytesToWrite', 'canReadLine',
  'waitForReadyRead', 'waitForBytesWritten', 'setBreakEnabled',
  'isBreakEnabled', 'settingsRestoredOnClose', 'setSettingsRestoredOnClose',
  'handle', 'baudRateChanged', 'dataBitsChanged', 'parityChanged',
  'stopBitsChanged', 'flowControlChanged', 'dataTerminalReadyChanged',
  'requestToSendChanged', 'errorOccurred', 'breakEnabledChanged',
  'settingsRestoredOnCloseChanged', 'writeData'. It can be made from Python,
  in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QSerialPort::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QSerialPort::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'const QSerialPortPrivate *QSerialPort::d_func() const': takes in
    Python what 'QSerialPortPrivate *QSerialPort::d_func()' takes.
  - Qt's 'QSerialPort::~QSerialPort()': the destructor: Python never removes
    a C++ QSerialPort.
  - Qt's 'QBindable<DataBits> QSerialPort::bindableDataBits()': gives a type
    Python has no way to take yet.
  - Qt's 'QBindable<Parity> QSerialPort::bindableParity()': gives a type
    Python has no way to take yet.
  - Qt's 'QBindable<StopBits>
    QSerialPort::bindableStopBits(Qt::Disambiguated_t a0)': gives a type
    Python has no way to take yet.
  - Qt's 'QBindable<FlowControl> QSerialPort::bindableFlowControl()': gives a
    type Python has no way to take yet.
  - Qt's 'QBindable<SerialPortError> QSerialPort::bindableError() const':
    gives a type Python has no way to take yet.
  - Qt's 'QBindable<bool> QSerialPort::bindableIsBreakEnabled()': gives a
    type Python has no way to take yet.
  - Qt's 'qint64 QSerialPort::readData(char *data, qint64 maxSize)': names
    'char', which has no cute class yet.
  - Qt's 'qint64 QSerialPort::readLineData(char *data, qint64 maxSize)':
    names 'char', which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 72 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QSerialPort is created at the first use, not by
    'QSerialPort(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSerialPort.
  - Qt tells when it has removed the C++ QSerialPort. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's QSerialPort that has no cute function yet,
    'bindableDataBits', 'bindableError', 'bindableFlowControl',
    'bindableIsBreakEnabled', 'bindableParity', 'bindableStopBits', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QSerialPort, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class BaudRate(CuteNum):
    """
    The enum 'QSerialPort::BaudRate' of Qt, with the 8 names Qt gives in it.
    """

    Baud1200 = Kee[int](1200)
    Baud2400 = Kee[int](2400)
    Baud4800 = Kee[int](4800)
    Baud9600 = Kee[int](9600)
    Baud19200 = Kee[int](19200)
    Baud38400 = Kee[int](38400)
    Baud57600 = Kee[int](57600)
    Baud115200 = Kee[int](115200)

  class DataBits(CuteNum):
    """
    The enum 'QSerialPort::DataBits' of Qt, with the 4 names Qt gives in it.
    """

    Data5 = Kee[int](5)
    Data6 = Kee[int](6)
    Data7 = Kee[int](7)
    Data8 = Kee[int](8)

  class Direction(CuteFlags):
    """
    The flags enum 'QSerialPort::Direction' of Qt, with the 3 names Qt gives
    in it. Qt names the type of its combinations 'QSerialPort::Directions'.
    """

    Input = 0x1
    Output = 0x2
    AllDirections = 0x3

  Directions = Direction

  class FlowControl(CuteNum):
    """
    The enum 'QSerialPort::FlowControl' of Qt, with the 3 names Qt gives in
    it.
    """

    NoFlowControl = Kee[int](0)
    HardwareControl = Kee[int](1)
    SoftwareControl = Kee[int](2)

  class Parity(CuteNum):
    """
    The enum 'QSerialPort::Parity' of Qt, with the 5 names Qt gives in it.
    """

    NoParity = Kee[int](0)
    EvenParity = Kee[int](2)
    OddParity = Kee[int](3)
    SpaceParity = Kee[int](4)
    MarkParity = Kee[int](5)

  class PinoutSignal(CuteFlags):
    """
    The flags enum 'QSerialPort::PinoutSignal' of Qt, with the 9 names Qt
    gives in it. Qt names the type of its combinations
    'QSerialPort::PinoutSignals'.
    """

    NoSignal = 0x0
    DataTerminalReadySignal = 0x4
    DataCarrierDetectSignal = 0x8
    DataSetReadySignal = 0x10
    RingIndicatorSignal = 0x20
    RequestToSendSignal = 0x40
    ClearToSendSignal = 0x80
    SecondaryTransmittedDataSignal = 0x100
    SecondaryReceivedDataSignal = 0x200

  PinoutSignals = PinoutSignal

  class SerialPortError(CuteNum):
    """
    The enum 'QSerialPort::SerialPortError' of Qt, with the 11 names Qt gives
    in it.
    """

    NoError = Kee[int](0)
    DeviceNotFoundError = Kee[int](1)
    PermissionError = Kee[int](2)
    OpenError = Kee[int](3)
    WriteError = Kee[int](4)
    ReadError = Kee[int](5)
    ResourceError = Kee[int](6)
    UnsupportedOperationError = Kee[int](7)
    UnknownError = Kee[int](8)
    TimeoutError = Kee[int](9)
    NotOpenError = Kee[int](10)

  class StopBits(CuteNum):
    """
    The enum 'QSerialPort::StopBits' of Qt, with the 3 names Qt gives in it.
    """

    OneStop = Kee[int](1)
    OneAndHalfStop = Kee[int](3)
    TwoStop = Kee[int](2)

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
    Calls Qt's 'QString QSerialPort::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qserialport.html#tr

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
    #  QString QSerialPort::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN11QSerialPort2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSerialPort'

  #  A C++ QSerialPort Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSerialPort'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QSerialPort::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qserialport.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QSerialPort::metaObject() const
    address = self.uglySide.call('ritual_ZNK11QSerialPort10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def portName(self) -> str:
    """
    Calls Qt's 'QString QSerialPort::portName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qserialport.html#portName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSerialPort::portName() const
    return self.uglySide.call('ritual_ZNK11QSerialPort8portNameEv')

  @overload()
  @overload(Directions)
  def baudRate(
      self,
      directions: Directions = Directions.AllDirections,
  ) -> int:
    """
    Calls Qt's 'qint32 QSerialPort::baudRate(Directions directions) const'.

    Qt's own words: https://doc.qt.io/qt-6/qserialport.html#baudRate

    Parameters
    ----------

    directions : Directions
      Passed on as its number. May be left out, as in Qt: it is then
      Directions.AllDirections.
    """
    #  qint32 QSerialPort::baudRate(Directions directions) const
    return self.uglySide.call(
        'ritual_ZNK11QSerialPort8baudRateE6QFlagsINS_9DirectionEE',
        directions.value,
    )

  def dataBits(self) -> DataBits:
    """
    Calls Qt's 'DataBits QSerialPort::dataBits() const'.

    Qt's own words: https://doc.qt.io/qt-6/qserialport.html#dataBits

    Returns
    -------

    DataBits
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'DataBits(number)' gives.
    """
    #  DataBits QSerialPort::dataBits() const
    return QSerialPort.DataBits(self.uglySide.call(
        'ritual_ZNK11QSerialPort8dataBitsEv',
    ))

  def parity(self) -> Parity:
    """
    Calls Qt's 'Parity QSerialPort::parity() const'.

    Qt's own words: https://doc.qt.io/qt-6/qserialport.html#parity

    Returns
    -------

    Parity
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Parity(number)' gives.
    """
    #  Parity QSerialPort::parity() const
    return QSerialPort.Parity(self.uglySide.call(
        'ritual_ZNK11QSerialPort6parityEv',
    ))

  def stopBits(self) -> StopBits:
    """
    Calls Qt's 'StopBits QSerialPort::stopBits() const'.

    Qt's own words: https://doc.qt.io/qt-6/qserialport.html#stopBits

    Returns
    -------

    StopBits
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'StopBits(number)' gives.
    """
    #  StopBits QSerialPort::stopBits() const
    return QSerialPort.StopBits(self.uglySide.call(
        'ritual_ZNK11QSerialPort8stopBitsEv',
    ))

  def flowControl(self) -> FlowControl:
    """
    Calls Qt's 'FlowControl QSerialPort::flowControl() const'.

    Qt's own words: https://doc.qt.io/qt-6/qserialport.html#flowControl

    Returns
    -------

    FlowControl
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'FlowControl(number)'
      gives.
    """
    #  FlowControl QSerialPort::flowControl() const
    return QSerialPort.FlowControl(self.uglySide.call(
        'ritual_ZNK11QSerialPort11flowControlEv',
    ))

  def error(self) -> SerialPortError:
    """
    Calls Qt's 'SerialPortError QSerialPort::error() const'.

    Qt's own words: https://doc.qt.io/qt-6/qserialport.html#error

    Returns
    -------

    SerialPortError
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'SerialPortError(number)'
      gives.
    """
    #  SerialPortError QSerialPort::error() const
    return QSerialPort.SerialPortError(self.uglySide.call(
        'ritual_ZNK11QSerialPort5errorEv',
    ))

  def readBufferSize(self) -> int:
    """
    Calls Qt's 'qint64 QSerialPort::readBufferSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qserialport.html#readBufferSize
    """
    #  qint64 QSerialPort::readBufferSize() const
    return self.uglySide.call('ritual_ZNK11QSerialPort14readBufferSizeEv')

  def writeBufferSize(self) -> int:
    """
    Calls Qt's 'qint64 QSerialPort::writeBufferSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qserialport.html#writeBufferSize
    """
    #  qint64 QSerialPort::writeBufferSize() const
    return self.uglySide.call('ritual_ZNK11QSerialPort15writeBufferSizeEv')

  def isSequential(self) -> bool:
    """
    Calls Qt's 'bool QSerialPort::isSequential() const'.

    Qt's own words: https://doc.qt.io/qt-6/qserialport.html#isSequential
    """
    #  bool QSerialPort::isSequential() const
    ritual = 'ritual_ZNK11QSerialPort12isSequentialEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QSerialPort12isSequentialEv'
    return self.uglySide.call(ritual)

  def bytesAvailable(self) -> int:
    """
    Calls Qt's 'qint64 QSerialPort::bytesAvailable() const'.

    Qt's own words: https://doc.qt.io/qt-6/qserialport.html#bytesAvailable
    """
    #  qint64 QSerialPort::bytesAvailable() const
    ritual = 'ritual_ZNK11QSerialPort14bytesAvailableEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QSerialPort14bytesAvailableEv'
    return self.uglySide.call(ritual)

  def bytesToWrite(self) -> int:
    """
    Calls Qt's 'qint64 QSerialPort::bytesToWrite() const'.

    Qt's own words: https://doc.qt.io/qt-6/qserialport.html#bytesToWrite
    """
    #  qint64 QSerialPort::bytesToWrite() const
    ritual = 'ritual_ZNK11QSerialPort12bytesToWriteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QSerialPort12bytesToWriteEv'
    return self.uglySide.call(ritual)

  def canReadLine(self) -> bool:
    """
    Calls Qt's 'bool QSerialPort::canReadLine() const'.

    Qt's own words: https://doc.qt.io/qt-6/qserialport.html#canReadLine
    """
    #  bool QSerialPort::canReadLine() const
    ritual = 'ritual_ZNK11QSerialPort11canReadLineEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QSerialPort11canReadLineEv'
    return self.uglySide.call(ritual)

  def isBreakEnabled(self) -> bool:
    """
    Calls Qt's 'bool QSerialPort::isBreakEnabled() const'.

    Qt's own words: https://doc.qt.io/qt-6/qserialport.html#isBreakEnabled
    """
    #  bool QSerialPort::isBreakEnabled() const
    return self.uglySide.call('ritual_ZNK11QSerialPort14isBreakEnabledEv')

  def settingsRestoredOnClose(self) -> bool:
    """
    Calls Qt's 'bool QSerialPort::settingsRestoredOnClose() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qserialport.html#settingsRestoredOnClose
    """
    #  bool QSerialPort::settingsRestoredOnClose() const
    return self.uglySide.call(
        'ritual_ZNK11QSerialPort23settingsRestoredOnCloseEv',
    )

  def handle(self) -> int:
    """
    Calls Qt's 'Handle QSerialPort::handle() const'.

    Qt's own words: https://doc.qt.io/qt-6/qserialport.html#handle
    """
    #  Handle QSerialPort::handle() const
    return self.uglySide.call('ritual_ZNK11QSerialPort6handleEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setPortName(self, name: str) -> None:
    """
    Calls Qt's 'void QSerialPort::setPortName(const QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qserialport.html#setPortName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QSerialPort::setPortName(const QString &name)
    self.uglySide.call(
        'ritual_ZN11QSerialPort11setPortNameERK7QString', name,
    )

  @overload(QSerialPortInfo)
  def setPort(self, info: QSerialPortInfo) -> None:
    """
    Calls Qt's 'void QSerialPort::setPort(const QSerialPortInfo &info)'.

    Qt's own words: https://doc.qt.io/qt-6/qserialport.html#setPort

    Parameters
    ----------

    info : QSerialPortInfo
      Passed on as a value: Qt reads the C++ QSerialPortInfo, which stays
      Python's own.
    """
    #  void QSerialPort::setPort(const QSerialPortInfo &info)
    self.uglySide.call(
        'ritual_ZN11QSerialPort7setPortERK15QSerialPortInfo',
        self._valueOf(info),
    )

  @overload(int)
  @overload(int, Directions)
  def setBaudRate(
      self,
      baudRate: int,
      directions: Directions = Directions.AllDirections,
  ) -> bool:
    """
    Calls Qt's 'bool QSerialPort::setBaudRate(qint32 baudRate, Directions
    directions)'.

    Qt's own words: https://doc.qt.io/qt-6/qserialport.html#setBaudRate

    Parameters
    ----------

    baudRate : int
      Passed on as it is.

    directions : Directions
      Passed on as its number. May be left out, as in Qt: it is then
      Directions.AllDirections.
    """
    #  bool QSerialPort::setBaudRate(qint32 baudRate, Directions directions)
    return self.uglySide.call(
        'ritual_ZN11QSerialPort11setBaudRateEi6QFlagsINS_9DirectionEE',
        baudRate, directions.value,
    )

  @overload(DataBits)
  def setDataBits(self, dataBits: DataBits) -> bool:
    """
    Calls Qt's 'bool QSerialPort::setDataBits(DataBits dataBits)'.

    Qt's own words: https://doc.qt.io/qt-6/qserialport.html#setDataBits

    Parameters
    ----------

    dataBits : DataBits
      Passed on as its number.
    """
    #  bool QSerialPort::setDataBits(DataBits dataBits)
    return self.uglySide.call(
        'ritual_ZN11QSerialPort11setDataBitsENS_8DataBitsE', dataBits.value,
    )

  @overload(Parity)
  def setParity(self, parity: Parity) -> bool:
    """
    Calls Qt's 'bool QSerialPort::setParity(Parity parity)'.

    Qt's own words: https://doc.qt.io/qt-6/qserialport.html#setParity

    Parameters
    ----------

    parity : Parity
      Passed on as its number.
    """
    #  bool QSerialPort::setParity(Parity parity)
    return self.uglySide.call(
        'ritual_ZN11QSerialPort9setParityENS_6ParityE', parity.value,
    )

  @overload(StopBits)
  def setStopBits(self, stopBits: StopBits) -> bool:
    """
    Calls Qt's 'bool QSerialPort::setStopBits(StopBits stopBits)'.

    Qt's own words: https://doc.qt.io/qt-6/qserialport.html#setStopBits

    Parameters
    ----------

    stopBits : StopBits
      Passed on as its number.
    """
    #  bool QSerialPort::setStopBits(StopBits stopBits)
    return self.uglySide.call(
        'ritual_ZN11QSerialPort11setStopBitsENS_8StopBitsE', stopBits.value,
    )

  @overload(FlowControl)
  def setFlowControl(self, flowControl: FlowControl) -> bool:
    """
    Calls Qt's 'bool QSerialPort::setFlowControl(FlowControl flowControl)'.

    Qt's own words: https://doc.qt.io/qt-6/qserialport.html#setFlowControl

    Parameters
    ----------

    flowControl : FlowControl
      Passed on as its number.
    """
    #  bool QSerialPort::setFlowControl(FlowControl flowControl)
    return self.uglySide.call(
        'ritual_ZN11QSerialPort14setFlowControlENS_11FlowControlE',
        flowControl.value,
    )

  @overload(bool)
  def setDataTerminalReady(self, set: bool) -> bool:
    """
    Calls Qt's 'bool QSerialPort::setDataTerminalReady(bool set)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qserialport.html#setDataTerminalReady

    Parameters
    ----------

    set : bool
      Passed on as it is.
    """
    #  bool QSerialPort::setDataTerminalReady(bool set)
    return self.uglySide.call(
        'ritual_ZN11QSerialPort20setDataTerminalReadyEb', set,
    )

  @overload(bool)
  def setRequestToSend(self, set: bool) -> bool:
    """
    Calls Qt's 'bool QSerialPort::setRequestToSend(bool set)'.

    Qt's own words: https://doc.qt.io/qt-6/qserialport.html#setRequestToSend

    Parameters
    ----------

    set : bool
      Passed on as it is.
    """
    #  bool QSerialPort::setRequestToSend(bool set)
    return self.uglySide.call(
        'ritual_ZN11QSerialPort16setRequestToSendEb', set,
    )

  @overload(int)
  def setReadBufferSize(self, size: int) -> None:
    """
    Calls Qt's 'void QSerialPort::setReadBufferSize(qint64 size)'.

    Qt's own words: https://doc.qt.io/qt-6/qserialport.html#setReadBufferSize

    Parameters
    ----------

    size : int
      Passed on as it is.
    """
    #  void QSerialPort::setReadBufferSize(qint64 size)
    self.uglySide.call('ritual_ZN11QSerialPort17setReadBufferSizeEx', size)

  @overload(int)
  def setWriteBufferSize(self, size: int) -> None:
    """
    Calls Qt's 'void QSerialPort::setWriteBufferSize(qint64 size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qserialport.html#setWriteBufferSize

    Parameters
    ----------

    size : int
      Passed on as it is.
    """
    #  void QSerialPort::setWriteBufferSize(qint64 size)
    self.uglySide.call('ritual_ZN11QSerialPort18setWriteBufferSizeEx', size)

  @overload()
  @overload(bool)
  def setBreakEnabled(self, set: bool = True) -> bool:
    """
    Calls Qt's 'bool QSerialPort::setBreakEnabled(bool set)'.

    Qt's own words: https://doc.qt.io/qt-6/qserialport.html#setBreakEnabled

    Parameters
    ----------

    set : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  bool QSerialPort::setBreakEnabled(bool set)
    return self.uglySide.call(
        'ritual_ZN11QSerialPort15setBreakEnabledEb', set,
    )

  @overload(bool)
  def setSettingsRestoredOnClose(self, restore: bool) -> None:
    """
    Calls Qt's 'void QSerialPort::setSettingsRestoredOnClose(bool restore)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qserialport.html#setSettingsRestoredOnClose

    Parameters
    ----------

    restore : bool
      Passed on as it is.
    """
    #  void QSerialPort::setSettingsRestoredOnClose(bool restore)
    self.uglySide.call(
        'ritual_ZN11QSerialPort26setSettingsRestoredOnCloseEb', restore,
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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's 'QSerialPort::QSerialPort(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qserialport.html#QSerialPort

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QSerialPort::QSerialPort(QObject *parent)
    self._noteCreation(QSerialPort, lambda: Rituals.call(
        'ritual_ZN11QSerialPortC1EP7QObject',
        self._addressOf(parent, 'QObject'),
    ))

  @overload(str)
  @overload(str, QObject)
  @overload(str, NoneType)
  def __init__(self, name: str, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's 'QSerialPort::QSerialPort(const QString
    &name, QObject *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qserialport.html#QSerialPort

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QSerialPort::QSerialPort(const QString &name, QObject *parent)
    self._noteCreation(QSerialPort, lambda: Rituals.call(
        'ritual_ZN11QSerialPortC1ERK7QStringP7QObject',
        name, self._addressOf(parent, 'QObject'),
    ))

  @overload(QSerialPortInfo)
  @overload(QSerialPortInfo, QObject)
  @overload(QSerialPortInfo, NoneType)
  def __init__(
      self,
      info: QSerialPortInfo,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QSerialPort::QSerialPort(const
    QSerialPortInfo &info, QObject *parent)', which is called at the first
    use.

    Qt's own words: https://doc.qt.io/qt-6/qserialport.html#QSerialPort

    Parameters
    ----------

    info : QSerialPortInfo
      Passed on as a value: Qt reads the C++ QSerialPortInfo, which stays
      Python's own.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QSerialPort::QSerialPort(const QSerialPortInfo &info, QObject *parent)
    self._noteCreation(QSerialPort, lambda: Rituals.call(
        'ritual_ZN11QSerialPortC1ERK15QSerialPortInfoP7QObject',
        self._valueOf(info), self._addressOf(parent, 'QObject'),
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

  def d_func(self) -> Optional[QSerialPortPrivate]:
    """
    Calls Qt's 'QSerialPortPrivate *QSerialPort::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qserialport.html#d_func

    Returns
    -------

    Optional[QSerialPortPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSerialPortPrivate *QSerialPort::d_func()
    address = self.uglySide.call('ritual_ZN11QSerialPort6d_funcEv')
    from . import QSerialPortPrivate
    return QSerialPortPrivate._cuteAt(address)

  @overload(QIODeviceBase.OpenMode)
  def open(self, mode: QIODeviceBase.OpenMode) -> bool:
    """
    Calls Qt's 'bool QSerialPort::open(OpenMode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qserialport.html#open

    Parameters
    ----------

    mode : QIODeviceBase.OpenMode
      Passed on as its number.
    """
    #  bool QSerialPort::open(OpenMode mode)
    ritual = (
        'ritual_ZN11QSerialPort4openE6QFlagsIN13QIODeviceBase12OpenModeFlag'
        'EE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN11QSerialPort4openE6QFlagsIN13QIODeviceBase12OpenMo'
          'deFlagEE')
    return self.uglySide.call(ritual, mode.value)

  def close(self) -> None:
    """
    Calls Qt's 'void QSerialPort::close()'.

    Qt's own words: https://doc.qt.io/qt-6/qserialport.html#close
    """
    #  void QSerialPort::close()
    ritual = 'ritual_ZN11QSerialPort5closeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QSerialPort5closeEv'
    self.uglySide.call(ritual)

  def isDataTerminalReady(self) -> bool:
    """
    Calls Qt's 'bool QSerialPort::isDataTerminalReady()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qserialport.html#isDataTerminalReady
    """
    #  bool QSerialPort::isDataTerminalReady()
    return self.uglySide.call(
        'ritual_ZN11QSerialPort19isDataTerminalReadyEv',
    )

  def isRequestToSend(self) -> bool:
    """
    Calls Qt's 'bool QSerialPort::isRequestToSend()'.

    Qt's own words: https://doc.qt.io/qt-6/qserialport.html#isRequestToSend
    """
    #  bool QSerialPort::isRequestToSend()
    return self.uglySide.call('ritual_ZN11QSerialPort15isRequestToSendEv')

  def pinoutSignals(self) -> PinoutSignals:
    """
    Calls Qt's 'PinoutSignals QSerialPort::pinoutSignals()'.

    Qt's own words: https://doc.qt.io/qt-6/qserialport.html#pinoutSignals

    Returns
    -------

    PinoutSignals
      The value standing for the combination Qt gave back.
    """
    #  PinoutSignals QSerialPort::pinoutSignals()
    return QSerialPort.PinoutSignals(self.uglySide.call(
        'ritual_ZN11QSerialPort13pinoutSignalsEv',
    ))

  def flush(self) -> bool:
    """
    Calls Qt's 'bool QSerialPort::flush()'.

    Qt's own words: https://doc.qt.io/qt-6/qserialport.html#flush
    """
    #  bool QSerialPort::flush()
    return self.uglySide.call('ritual_ZN11QSerialPort5flushEv')

  @overload()
  @overload(Directions)
  def clear(self, directions: Directions = Directions.AllDirections) -> bool:
    """
    Calls Qt's 'bool QSerialPort::clear(Directions directions)'.

    Qt's own words: https://doc.qt.io/qt-6/qserialport.html#clear

    Parameters
    ----------

    directions : Directions
      Passed on as its number. May be left out, as in Qt: it is then
      Directions.AllDirections.
    """
    #  bool QSerialPort::clear(Directions directions)
    return self.uglySide.call(
        'ritual_ZN11QSerialPort5clearE6QFlagsINS_9DirectionEE',
        directions.value,
    )

  def clearError(self) -> None:
    """
    Calls Qt's 'void QSerialPort::clearError()'.

    Qt's own words: https://doc.qt.io/qt-6/qserialport.html#clearError
    """
    #  void QSerialPort::clearError()
    self.uglySide.call('ritual_ZN11QSerialPort10clearErrorEv')

  @overload()
  @overload(int)
  def waitForReadyRead(self, msecs: int = 30000) -> bool:
    """
    Calls Qt's 'bool QSerialPort::waitForReadyRead(int msecs)'.

    Qt's own words: https://doc.qt.io/qt-6/qserialport.html#waitForReadyRead

    Parameters
    ----------

    msecs : int
      Passed on as it is. May be left out, as in Qt: it is then 30000.
    """
    #  bool QSerialPort::waitForReadyRead(int msecs)
    ritual = 'ritual_ZN11QSerialPort16waitForReadyReadEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QSerialPort16waitForReadyReadEi'
    return self.uglySide.call(ritual, msecs)

  @overload()
  @overload(int)
  def waitForBytesWritten(self, msecs: int = 30000) -> bool:
    """
    Calls Qt's 'bool QSerialPort::waitForBytesWritten(int msecs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qserialport.html#waitForBytesWritten

    Parameters
    ----------

    msecs : int
      Passed on as it is. May be left out, as in Qt: it is then 30000.
    """
    #  bool QSerialPort::waitForBytesWritten(int msecs)
    ritual = 'ritual_ZN11QSerialPort19waitForBytesWrittenEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QSerialPort19waitForBytesWrittenEi'
    return self.uglySide.call(ritual, msecs)

  @overload(int, Directions)
  def baudRateChanged(self, baudRate: int, directions: Directions) -> None:
    """
    Calls Qt's 'void QSerialPort::baudRateChanged(qint32 baudRate,
    QSerialPort::Directions directions)'.

    Qt's own words: https://doc.qt.io/qt-6/qserialport.html#baudRateChanged

    Parameters
    ----------

    baudRate : int
      Passed on as it is.

    directions : Directions
      Passed on as its number.
    """
    #  void QSerialPort::baudRateChanged(qint32 baudRate,
    #      QSerialPort::Directions directions)
    self.uglySide.call(
        'ritual_ZN11QSerialPort15baudRateChangedEi6QFlagsINS_9DirectionEE',
        baudRate, directions.value,
    )

  @overload(DataBits)
  def dataBitsChanged(self, dataBits: DataBits) -> None:
    """
    Calls Qt's 'void QSerialPort::dataBitsChanged(QSerialPort::DataBits
    dataBits)'.

    Qt's own words: https://doc.qt.io/qt-6/qserialport.html#dataBitsChanged

    Parameters
    ----------

    dataBits : DataBits
      Passed on as its number.
    """
    #  void QSerialPort::dataBitsChanged(QSerialPort::DataBits dataBits)
    self.uglySide.call(
        'ritual_ZN11QSerialPort15dataBitsChangedENS_8DataBitsE',
        dataBits.value,
    )

  @overload(Parity)
  def parityChanged(self, parity: Parity) -> None:
    """
    Calls Qt's 'void QSerialPort::parityChanged(QSerialPort::Parity parity)'.

    Qt's own words: https://doc.qt.io/qt-6/qserialport.html#parityChanged

    Parameters
    ----------

    parity : Parity
      Passed on as its number.
    """
    #  void QSerialPort::parityChanged(QSerialPort::Parity parity)
    self.uglySide.call(
        'ritual_ZN11QSerialPort13parityChangedENS_6ParityE', parity.value,
    )

  @overload(StopBits)
  def stopBitsChanged(self, stopBits: StopBits) -> None:
    """
    Calls Qt's 'void QSerialPort::stopBitsChanged(QSerialPort::StopBits
    stopBits)'.

    Qt's own words: https://doc.qt.io/qt-6/qserialport.html#stopBitsChanged

    Parameters
    ----------

    stopBits : StopBits
      Passed on as its number.
    """
    #  void QSerialPort::stopBitsChanged(QSerialPort::StopBits stopBits)
    self.uglySide.call(
        'ritual_ZN11QSerialPort15stopBitsChangedENS_8StopBitsE',
        stopBits.value,
    )

  @overload(FlowControl)
  def flowControlChanged(self, flowControl: FlowControl) -> None:
    """
    Calls Qt's 'void QSerialPort::flowControlChanged(QSerialPort::FlowControl
    flowControl)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qserialport.html#flowControlChanged

    Parameters
    ----------

    flowControl : FlowControl
      Passed on as its number.
    """
    #  void QSerialPort::flowControlChanged(QSerialPort::FlowControl
    #      flowControl)
    self.uglySide.call(
        'ritual_ZN11QSerialPort18flowControlChangedENS_11FlowControlE',
        flowControl.value,
    )

  @overload(bool)
  def dataTerminalReadyChanged(self, set: bool) -> None:
    """
    Calls Qt's 'void QSerialPort::dataTerminalReadyChanged(bool set)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qserialport.html#dataTerminalReadyChanged

    Parameters
    ----------

    set : bool
      Passed on as it is.
    """
    #  void QSerialPort::dataTerminalReadyChanged(bool set)
    self.uglySide.call(
        'ritual_ZN11QSerialPort24dataTerminalReadyChangedEb', set,
    )

  @overload(bool)
  def requestToSendChanged(self, set: bool) -> None:
    """
    Calls Qt's 'void QSerialPort::requestToSendChanged(bool set)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qserialport.html#requestToSendChanged

    Parameters
    ----------

    set : bool
      Passed on as it is.
    """
    #  void QSerialPort::requestToSendChanged(bool set)
    self.uglySide.call('ritual_ZN11QSerialPort20requestToSendChangedEb', set)

  @overload(SerialPortError)
  def errorOccurred(self, error: SerialPortError) -> None:
    """
    Calls Qt's 'void QSerialPort::errorOccurred(QSerialPort::SerialPortError
    error)'.

    Qt's own words: https://doc.qt.io/qt-6/qserialport.html#errorOccurred

    Parameters
    ----------

    error : SerialPortError
      Passed on as its number.
    """
    #  void QSerialPort::errorOccurred(QSerialPort::SerialPortError error)
    self.uglySide.call(
        'ritual_ZN11QSerialPort13errorOccurredENS_15SerialPortErrorE',
        error.value,
    )

  @overload(bool)
  def breakEnabledChanged(self, set: bool) -> None:
    """
    Calls Qt's 'void QSerialPort::breakEnabledChanged(bool set)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qserialport.html#breakEnabledChanged

    Parameters
    ----------

    set : bool
      Passed on as it is.
    """
    #  void QSerialPort::breakEnabledChanged(bool set)
    self.uglySide.call('ritual_ZN11QSerialPort19breakEnabledChangedEb', set)

  @overload(bool)
  def settingsRestoredOnCloseChanged(self, restore: bool) -> None:
    """
    Calls Qt's 'void QSerialPort::settingsRestoredOnCloseChanged(bool
    restore)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qserialport.html#settingsRestoredOnCloseChanged

    Parameters
    ----------

    restore : bool
      Passed on as it is.
    """
    #  void QSerialPort::settingsRestoredOnCloseChanged(bool restore)
    self.uglySide.call(
        'ritual_ZN11QSerialPort30settingsRestoredOnCloseChangedEb', restore,
    )

  @overload(str, int)
  @overload(NoneType, int)
  def writeData(self, data: Optional[str], maxSize: int) -> int:
    """
    Calls Qt's 'qint64 QSerialPort::writeData(const char *data, qint64
    maxSize)'.

    Qt's own words: https://doc.qt.io/qt-6/qserialport.html#writeData

    Parameters
    ----------

    data : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    maxSize : int
      Passed on as it is.
    """
    #  qint64 QSerialPort::writeData(const char *data, qint64 maxSize)
    return self.uglySide.call(
        'ritual_ZN11QSerialPort9writeDataEPKcx',
        self._bytesOf(data), maxSize,
    )

  @staticmethod
  def bindableDataBits(*__, **_) -> Never:
    """
    Qt's 'QBindable<DataBits> QSerialPort::bindableDataBits()': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSerialPort.bindableDataBits' has no cute function yet. Qt's "
        "'QBindable<DataBits> QSerialPort::bindableDataBits()': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def bindableError(*__, **_) -> Never:
    """
    Qt's 'QBindable<SerialPortError> QSerialPort::bindableError() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSerialPort.bindableError' has no cute function yet. Qt's "
        "'QBindable<SerialPortError> QSerialPort::bindableError() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def bindableFlowControl(*__, **_) -> Never:
    """
    Qt's 'QBindable<FlowControl> QSerialPort::bindableFlowControl()': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSerialPort.bindableFlowControl' has no cute function yet. Qt's "
        "'QBindable<FlowControl> QSerialPort::bindableFlowControl()': gives "
        "a type Python has no way to take yet.")

  @staticmethod
  def bindableIsBreakEnabled(*__, **_) -> Never:
    """
    Qt's 'QBindable<bool> QSerialPort::bindableIsBreakEnabled()': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSerialPort.bindableIsBreakEnabled' has no cute function yet. "
        "Qt's 'QBindable<bool> QSerialPort::bindableIsBreakEnabled()': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def bindableParity(*__, **_) -> Never:
    """
    Qt's 'QBindable<Parity> QSerialPort::bindableParity()': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSerialPort.bindableParity' has no cute function yet. Qt's "
        "'QBindable<Parity> QSerialPort::bindableParity()': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def bindableStopBits(*__, **_) -> Never:
    """
    Qt's 'QBindable<StopBits>
    QSerialPort::bindableStopBits(Qt::Disambiguated_t a0)': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSerialPort.bindableStopBits' has no cute function yet. Qt's "
        "'QBindable<StopBits> "
        "QSerialPort::bindableStopBits(Qt::Disambiguated_t a0)': gives a "
        "type Python has no way to take yet.")
