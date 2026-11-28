"""
QModbusDevice binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSerialBus/qmodbusdevice.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QIODevice, QMetaObject, QVariant
  from . import QModbusDevicePrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QModbusDevice(QObject):
  """
  The cute side of Qt's QModbusDevice: a plain Python object standing in
  front of one C++ QModbusDevice.

  It is built on the cute 'QObject', as Qt's QModbusDevice is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QModbusDevice that has a ritual and that Python can
  call so far, 17 names in all: 'metaObject', 'tr', 'd_func',
  'connectionParameter', 'setConnectionParameter', 'connectDevice',
  'disconnectDevice', 'state', 'error', 'errorString', 'device',
  'errorOccurred', 'stateChanged', 'setState', 'setError', 'open', 'close'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QModbusDevice::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QModbusDevice::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'const QModbusDevicePrivate *QModbusDevice::d_func() const': takes
    in Python what 'QModbusDevicePrivate *QModbusDevice::d_func()' takes.
  - Qt's 'QModbusDevice::~QModbusDevice()': the destructor: Python never
    removes a C++ QModbusDevice.
  - Qt's 'QModbusDevice::QModbusDevice(QModbusDevicePrivate &dd, QObject
    *parent)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 25 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QModbusDevice is created at the first use, not by
    'QModbusDevice(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QModbusDevice.
  - Qt tells when it has removed the C++ QModbusDevice. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QModbusDevice, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class ConnectionParameter(CuteNum):
    """
    The enum 'QModbusDevice::ConnectionParameter' of Qt, with the 7 names Qt
    gives in it.
    """

    SerialPortNameParameter = Kee[int](0)
    SerialParityParameter = Kee[int](1)
    SerialBaudRateParameter = Kee[int](2)
    SerialDataBitsParameter = Kee[int](3)
    SerialStopBitsParameter = Kee[int](4)
    NetworkPortParameter = Kee[int](5)
    NetworkAddressParameter = Kee[int](6)

  class Error(CuteNum):
    """
    The enum 'QModbusDevice::Error' of Qt, with the 10 names Qt gives in it.
    """

    NoError = Kee[int](0)
    ReadError = Kee[int](1)
    WriteError = Kee[int](2)
    ConnectionError = Kee[int](3)
    ConfigurationError = Kee[int](4)
    TimeoutError = Kee[int](5)
    ProtocolError = Kee[int](6)
    ReplyAbortedError = Kee[int](7)
    UnknownError = Kee[int](8)
    InvalidResponseError = Kee[int](9)

  class IntermediateError(CuteNum):
    """
    The enum 'QModbusDevice::IntermediateError' of Qt, with the 2 names Qt
    gives in it.
    """

    ResponseCrcError = Kee[int](0)
    ResponseRequestMismatch = Kee[int](1)

  class State(CuteNum):
    """
    The enum 'QModbusDevice::State' of Qt, with the 4 names Qt gives in it.
    """

    UnconnectedState = Kee[int](0)
    ConnectingState = Kee[int](1)
    ConnectedState = Kee[int](2)
    ClosingState = Kee[int](3)

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
    Calls Qt's 'QString QModbusDevice::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qmodbusdevice.html#tr

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
    #  QString QModbusDevice::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN13QModbusDevice2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QModbusDevice'

  #  A C++ QModbusDevice Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QModbusDevice'

  #  The functions Qt calls itself that QModbusDevice is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'open': (
          ('_ZN13QModbusDevice4openEv',
           ('bool', 'number', ''),
           ()),
      ),
      'close': (
          ('_ZN13QModbusDevice5closeEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QModbusDevice::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmodbusdevice.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QModbusDevice::metaObject() const
    address = self.uglySide.call('ritual_ZNK13QModbusDevice10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(ConnectionParameter)
  def connectionParameter(self, parameter: ConnectionParameter) -> QVariant:
    """
    Calls Qt's 'QVariant
    QModbusDevice::connectionParameter(ConnectionParameter parameter) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmodbusdevice.html#connectionParameter

    Parameters
    ----------

    parameter : ConnectionParameter
      Passed on as its number.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QModbusDevice::connectionParameter(ConnectionParameter
    #      parameter) const
    address = self.uglySide.call(
        'ritual_ZNK13QModbusDevice19connectionParameterENS_19ConnectionPara'
        'meterE',
        parameter.value,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def state(self) -> State:
    """
    Calls Qt's 'State QModbusDevice::state() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmodbusdevice.html#state

    Returns
    -------

    State
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'State(number)' gives.
    """
    #  State QModbusDevice::state() const
    return QModbusDevice.State(self.uglySide.call(
        'ritual_ZNK13QModbusDevice5stateEv',
    ))

  def error(self) -> Error:
    """
    Calls Qt's 'Error QModbusDevice::error() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmodbusdevice.html#error

    Returns
    -------

    Error
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Error(number)' gives.
    """
    #  Error QModbusDevice::error() const
    return QModbusDevice.Error(self.uglySide.call(
        'ritual_ZNK13QModbusDevice5errorEv',
    ))

  def errorString(self) -> str:
    """
    Calls Qt's 'QString QModbusDevice::errorString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmodbusdevice.html#errorString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QModbusDevice::errorString() const
    return self.uglySide.call('ritual_ZNK13QModbusDevice11errorStringEv')

  def device(self) -> Optional[QIODevice]:
    """
    Calls Qt's 'QIODevice *QModbusDevice::device() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmodbusdevice.html#device

    Returns
    -------

    Optional[QIODevice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QIODevice *QModbusDevice::device() const
    address = self.uglySide.call('ritual_ZNK13QModbusDevice6deviceEv')
    from ..QtCore import QIODevice
    return QIODevice._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(ConnectionParameter, QVariant)
  def setConnectionParameter(
      self,
      parameter: ConnectionParameter,
      value: QVariant,
  ) -> None:
    """
    Calls Qt's 'void
    QModbusDevice::setConnectionParameter(ConnectionParameter parameter,
    const QVariant &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmodbusdevice.html#setConnectionParameter

    Parameters
    ----------

    parameter : ConnectionParameter
      Passed on as its number.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QModbusDevice::setConnectionParameter(ConnectionParameter
    #      parameter, const QVariant &value)
    self.uglySide.call(
        'ritual_ZN13QModbusDevice22setConnectionParameterENS_19ConnectionPa'
        'rameterERK8QVariant',
        parameter.value, self._valueOf(value),
    )

  @overload(State)
  def setState(self, newState: State) -> None:
    """
    Calls Qt's 'void QModbusDevice::setState(QModbusDevice::State newState)'.

    Qt's own words: https://doc.qt.io/qt-6/qmodbusdevice.html#setState

    Parameters
    ----------

    newState : State
      Passed on as its number.
    """
    #  void QModbusDevice::setState(QModbusDevice::State newState)
    self.uglySide.call(
        'ritual_ZN13QModbusDevice8setStateENS_5StateE', newState.value,
    )

  @overload(str, Error)
  def setError(self, errorText: str, error: Error) -> None:
    """
    Calls Qt's 'void QModbusDevice::setError(const QString &errorText,
    QModbusDevice::Error error)'.

    Qt's own words: https://doc.qt.io/qt-6/qmodbusdevice.html#setError

    Parameters
    ----------

    errorText : str
      Passed on as it is: a QString is made of it for the call.

    error : Error
      Passed on as its number.
    """
    #  void QModbusDevice::setError(const QString &errorText,
    #      QModbusDevice::Error error)
    self.uglySide.call(
        'ritual_ZN13QModbusDevice8setErrorERK7QStringNS_5ErrorE',
        errorText, error.value,
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
    Notes what was given, for Qt's 'QModbusDevice::QModbusDevice(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qmodbusdevice.html#QModbusDevice

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QModbusDevice::QModbusDevice(QObject *parent)
    self._noteCreation(QModbusDevice, lambda: Rituals.call(
        'ritual_ZN13QModbusDeviceC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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

  def d_func(self) -> Optional[QModbusDevicePrivate]:
    """
    Calls Qt's 'QModbusDevicePrivate *QModbusDevice::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qmodbusdevice.html#d_func

    Returns
    -------

    Optional[QModbusDevicePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QModbusDevicePrivate *QModbusDevice::d_func()
    address = self.uglySide.call('ritual_ZN13QModbusDevice6d_funcEv')
    from . import QModbusDevicePrivate
    return QModbusDevicePrivate._cuteAt(address)

  def connectDevice(self) -> bool:
    """
    Calls Qt's 'bool QModbusDevice::connectDevice()'.

    Qt's own words: https://doc.qt.io/qt-6/qmodbusdevice.html#connectDevice
    """
    #  bool QModbusDevice::connectDevice()
    return self.uglySide.call('ritual_ZN13QModbusDevice13connectDeviceEv')

  def disconnectDevice(self) -> None:
    """
    Calls Qt's 'void QModbusDevice::disconnectDevice()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmodbusdevice.html#disconnectDevice
    """
    #  void QModbusDevice::disconnectDevice()
    self.uglySide.call('ritual_ZN13QModbusDevice16disconnectDeviceEv')

  @overload(Error)
  def errorOccurred(self, error: Error) -> None:
    """
    Calls Qt's 'void QModbusDevice::errorOccurred(QModbusDevice::Error
    error)'.

    Qt's own words: https://doc.qt.io/qt-6/qmodbusdevice.html#errorOccurred

    Parameters
    ----------

    error : Error
      Passed on as its number.
    """
    #  void QModbusDevice::errorOccurred(QModbusDevice::Error error)
    self.uglySide.call(
        'ritual_ZN13QModbusDevice13errorOccurredENS_5ErrorE', error.value,
    )

  @overload(State)
  def stateChanged(self, state: State) -> None:
    """
    Calls Qt's 'void QModbusDevice::stateChanged(QModbusDevice::State
    state)'.

    Qt's own words: https://doc.qt.io/qt-6/qmodbusdevice.html#stateChanged

    Parameters
    ----------

    state : State
      Passed on as its number.
    """
    #  void QModbusDevice::stateChanged(QModbusDevice::State state)
    self.uglySide.call(
        'ritual_ZN13QModbusDevice12stateChangedENS_5StateE', state.value,
    )

  def open(self) -> bool:
    """
    Calls Qt's 'bool QModbusDevice::open()'.

    Qt's own words: https://doc.qt.io/qt-6/qmodbusdevice.html#open
    """
    #  bool QModbusDevice::open()
    return self.uglySide.call('ritual_ZN13QModbusDevice4openEv')

  def close(self) -> None:
    """
    Calls Qt's 'void QModbusDevice::close()'.

    Qt's own words: https://doc.qt.io/qt-6/qmodbusdevice.html#close
    """
    #  void QModbusDevice::close()
    self.uglySide.call('ritual_ZN13QModbusDevice5closeEv')
