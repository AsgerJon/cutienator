"""
QSerialPortPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSerialPort/6.12.0/QtSerialPort/private/qserialport_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QSerialPortPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QIODevicePrivate
from . import QSerialPort

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QSerialPortErrorInfo
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSerialPortErrorInfo = WAIT['QSerialPortErrorInfo']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSerialPortPrivate(QIODevicePrivate):
  """
  The cute side of Qt's QSerialPortPrivate: a plain Python object standing in
  front of one C++ QSerialPortPrivate.

  It is built on the cute 'QIODevicePrivate', as Qt's QSerialPortPrivate is
  built on Qt's QIODevicePrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSerialPortPrivate that has a ritual and that Python
  can call so far, 18 names in all: 'q_func', 'setError', 'setBindableError',
  '_qt_property_error_offset', 'setBindableDataBits',
  '_qt_property_dataBits_offset', 'setBindableParity',
  '_qt_property_parity_offset', 'setBindableStopBits',
  '_qt_property_stopBits_offset', 'setBindableFlowControl',
  '_qt_property_flowControl_offset', 'setBindableBreakEnabled',
  '_qt_property_isBreakEnabled_offset', 'isReadNotificationEnabled',
  'isWriteNotificationEnabled', 'writeToPort', 'handleException'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QSerialPort *QSerialPortPrivate::q_func() const': takes in
    Python what 'QSerialPort *QSerialPortPrivate::q_func()' takes.
  - Qt's 'qint64 QSerialPortPrivate::readFromPort(char *data, qint64
    maxSize)': names 'char', which has no cute class yet.

  What has no ritual
  ------------------

  33 of the 54 functions Qt declares: 23 cannot be called and cannot be
  called through the meta-object and cannot be copied; 8 leans on
  'QSerialPortPrivate; 2 Qt's library has no name for it, and its code in
  Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QSerialPortPrivate is created at the first use, not by
    'QSerialPortPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSerialPortPrivate.
  - Each name of Qt's QSerialPortPrivate that has no cute function yet,
    'clear', 'close', 'completeAsyncWrite', 'flush', 'getSystemError',
    'getTermios', 'initialize', 'open', 'pinoutSignals', 'readFromPort',
    'readNotification', 'sendBreak', 'setBaudRate', 'setBreakEnabled',
    'setCustomBaudRate', 'setDataBits', 'setDataTerminalReady',
    'setFlowControl', 'setParity', 'setReadNotificationEnabled',
    'setRequestToSend', 'setStandardBaudRate', 'setStopBits', 'setTermios',
    'setWriteNotificationEnabled', 'settingFromBaudRate',
    'standardBaudRates', 'startAsyncRead', 'startAsyncWrite',
    'waitForBytesWritten', 'waitForReadOrWrite', 'waitForReadyRead',
    'writeData', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def _qt_property_error_offset() -> int:
    """
    Calls Qt's 'size_t QSerialPortPrivate::_qt_property_error_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qserialportprivate.html#_qt_property_error_offset
    """
    #  size_t QSerialPortPrivate::_qt_property_error_offset()
    return Rituals.call(
        'ritual_ZN18QSerialPortPrivate25_qt_property_error_offsetEv',
    )

  @staticmethod
  def _qt_property_dataBits_offset() -> int:
    """
    Calls Qt's 'size_t QSerialPortPrivate::_qt_property_dataBits_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qserialportprivate.html
    """
    #  size_t QSerialPortPrivate::_qt_property_dataBits_offset()
    return Rituals.call(
        'ritual_ZN18QSerialPortPrivate28_qt_property_dataBits_offsetEv',
    )

  @staticmethod
  def _qt_property_parity_offset() -> int:
    """
    Calls Qt's 'size_t QSerialPortPrivate::_qt_property_parity_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qserialportprivate.html#_qt_property_parity_offset
    """
    #  size_t QSerialPortPrivate::_qt_property_parity_offset()
    return Rituals.call(
        'ritual_ZN18QSerialPortPrivate26_qt_property_parity_offsetEv',
    )

  @staticmethod
  def _qt_property_stopBits_offset() -> int:
    """
    Calls Qt's 'size_t QSerialPortPrivate::_qt_property_stopBits_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qserialportprivate.html
    """
    #  size_t QSerialPortPrivate::_qt_property_stopBits_offset()
    return Rituals.call(
        'ritual_ZN18QSerialPortPrivate28_qt_property_stopBits_offsetEv',
    )

  @staticmethod
  def _qt_property_flowControl_offset() -> int:
    """
    Calls Qt's 'size_t
    QSerialPortPrivate::_qt_property_flowControl_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qserialportprivate.html
    """
    #  size_t QSerialPortPrivate::_qt_property_flowControl_offset()
    return Rituals.call(
        'ritual_ZN18QSerialPortPrivate31_qt_property_flowControl_offsetEv',
    )

  @staticmethod
  def _qt_property_isBreakEnabled_offset() -> int:
    """
    Calls Qt's 'size_t
    QSerialPortPrivate::_qt_property_isBreakEnabled_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qserialportprivate.html
    """
    #  size_t QSerialPortPrivate::_qt_property_isBreakEnabled_offset()
    return Rituals.call(
        'ritual_ZN18QSerialPortPrivate34_qt_property_isBreakEnabled_offsetE'
        'v',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSerialPortPrivate'

  #  A C++ QSerialPortPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSerialPortPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isReadNotificationEnabled(self) -> bool:
    """
    Calls Qt's 'bool QSerialPortPrivate::isReadNotificationEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qserialportprivate.html#isReadNotificationEnabled
    """
    #  bool QSerialPortPrivate::isReadNotificationEnabled() const
    return self.uglySide.call(
        'ritual_ZNK18QSerialPortPrivate25isReadNotificationEnabledEv',
    )

  def isWriteNotificationEnabled(self) -> bool:
    """
    Calls Qt's 'bool QSerialPortPrivate::isWriteNotificationEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qserialportprivate.html#isWriteNotificationEnabled
    """
    #  bool QSerialPortPrivate::isWriteNotificationEnabled() const
    return self.uglySide.call(
        'ritual_ZNK18QSerialPortPrivate26isWriteNotificationEnabledEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QSerialPortErrorInfo)
  def setError(self, errorInfo: QSerialPortErrorInfo) -> None:
    """
    Calls Qt's 'void QSerialPortPrivate::setError(const QSerialPortErrorInfo
    &errorInfo)'.

    Qt's own words: https://doc.qt.io/qt-6/qserialportprivate.html#setError

    Parameters
    ----------

    errorInfo : QSerialPortErrorInfo
      Passed on as a value: Qt reads the C++ QSerialPortErrorInfo, which
      stays Python's own.
    """
    #  void QSerialPortPrivate::setError(const QSerialPortErrorInfo
    #      &errorInfo)
    self.uglySide.call(
        'ritual_ZN18QSerialPortPrivate8setErrorERK20QSerialPortErrorInfo',
        self._valueOf(errorInfo),
    )

  @overload(QSerialPort.SerialPortError)
  def setBindableError(self, error: QSerialPort.SerialPortError) -> None:
    """
    Calls Qt's 'void
    QSerialPortPrivate::setBindableError(QSerialPort::SerialPortError
    error)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qserialportprivate.html#setBindableError

    Parameters
    ----------

    error : QSerialPort.SerialPortError
      Passed on as its number.
    """
    #  void QSerialPortPrivate::setBindableError(QSerialPort::SerialPortError
    #      error)
    self.uglySide.call(
        'ritual_ZN18QSerialPortPrivate16setBindableErrorEN11QSerialPort15Se'
        'rialPortErrorE',
        error.value,
    )

  @overload(QSerialPort.DataBits)
  def setBindableDataBits(self, dataBits: QSerialPort.DataBits) -> bool:
    """
    Calls Qt's 'bool
    QSerialPortPrivate::setBindableDataBits(QSerialPort::DataBits dataBits)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qserialportprivate.html#setBindableDataBits

    Parameters
    ----------

    dataBits : QSerialPort.DataBits
      Passed on as its number.
    """
    #  bool QSerialPortPrivate::setBindableDataBits(QSerialPort::DataBits
    #      dataBits)
    return self.uglySide.call(
        'ritual_ZN18QSerialPortPrivate19setBindableDataBitsEN11QSerialPort8'
        'DataBitsE',
        dataBits.value,
    )

  @overload(QSerialPort.Parity)
  def setBindableParity(self, parity: QSerialPort.Parity) -> bool:
    """
    Calls Qt's 'bool
    QSerialPortPrivate::setBindableParity(QSerialPort::Parity parity)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qserialportprivate.html#setBindableParity

    Parameters
    ----------

    parity : QSerialPort.Parity
      Passed on as its number.
    """
    #  bool QSerialPortPrivate::setBindableParity(QSerialPort::Parity parity)
    return self.uglySide.call(
        'ritual_ZN18QSerialPortPrivate17setBindableParityEN11QSerialPort6Pa'
        'rityE',
        parity.value,
    )

  @overload(QSerialPort.StopBits)
  def setBindableStopBits(self, stopBits: QSerialPort.StopBits) -> bool:
    """
    Calls Qt's 'bool
    QSerialPortPrivate::setBindableStopBits(QSerialPort::StopBits stopBits)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qserialportprivate.html#setBindableStopBits

    Parameters
    ----------

    stopBits : QSerialPort.StopBits
      Passed on as its number.
    """
    #  bool QSerialPortPrivate::setBindableStopBits(QSerialPort::StopBits
    #      stopBits)
    return self.uglySide.call(
        'ritual_ZN18QSerialPortPrivate19setBindableStopBitsEN11QSerialPort8'
        'StopBitsE',
        stopBits.value,
    )

  @overload(QSerialPort.FlowControl)
  def setBindableFlowControl(
      self,
      flowControl: QSerialPort.FlowControl,
  ) -> bool:
    """
    Calls Qt's 'bool
    QSerialPortPrivate::setBindableFlowControl(QSerialPort::FlowControl
    flowControl)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qserialportprivate.html#setBindableFlowControl

    Parameters
    ----------

    flowControl : QSerialPort.FlowControl
      Passed on as its number.
    """
    #  bool QSerialPortPrivate::setBindableFlowControl(QSerialPort::
    #      FlowControl flowControl)
    return self.uglySide.call(
        'ritual_ZN18QSerialPortPrivate22setBindableFlowControlEN11QSerialPo'
        'rt11FlowControlE',
        flowControl.value,
    )

  @overload(bool)
  def setBindableBreakEnabled(self, isBreakEnabled: bool) -> bool:
    """
    Calls Qt's 'bool QSerialPortPrivate::setBindableBreakEnabled(bool
    isBreakEnabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qserialportprivate.html#setBindableBreakEnabled

    Parameters
    ----------

    isBreakEnabled : bool
      Passed on as it is.
    """
    #  bool QSerialPortPrivate::setBindableBreakEnabled(bool isBreakEnabled)
    return self.uglySide.call(
        'ritual_ZN18QSerialPortPrivate23setBindableBreakEnabledEb',
        isBreakEnabled,
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
    'QSerialPortPrivate::QSerialPortPrivate()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qserialportprivate.html#QSerialPortPrivate
    """
    #  QSerialPortPrivate::QSerialPortPrivate()
    self._noteCreation(QSerialPortPrivate, lambda: Rituals.call(
        'ritual_ZN18QSerialPortPrivateC1Ev',
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

  def q_func(self) -> Optional[QSerialPort]:
    """
    Calls Qt's 'QSerialPort *QSerialPortPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qserialportprivate.html#q_func

    Returns
    -------

    Optional[QSerialPort]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSerialPort *QSerialPortPrivate::q_func()
    address = self.uglySide.call('ritual_ZN18QSerialPortPrivate6q_funcEv')
    return QSerialPort._cuteAt(address)

  @overload(str, int)
  @overload(NoneType, int)
  def writeToPort(self, data: Optional[str], maxSize: int) -> int:
    """
    Calls Qt's 'qint64 QSerialPortPrivate::writeToPort(const char *data,
    qint64 maxSize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qserialportprivate.html#writeToPort

    Parameters
    ----------

    data : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    maxSize : int
      Passed on as it is.
    """
    #  qint64 QSerialPortPrivate::writeToPort(const char *data, qint64
    #      maxSize)
    return self.uglySide.call(
        'ritual_ZN18QSerialPortPrivate11writeToPortEPKcx',
        self._bytesOf(data), maxSize,
    )

  def handleException(self) -> None:
    """
    Calls Qt's 'void QSerialPortPrivate::handleException()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qserialportprivate.html#handleException
    """
    #  void QSerialPortPrivate::handleException()
    self.uglySide.call('ritual_ZN18QSerialPortPrivate15handleExceptionEv')

  @staticmethod
  def clear(*__, **_) -> Never:
    """
    Qt's 'bool QSerialPortPrivate::clear(QSerialPort::Directions
    directions)': cannot be called and cannot be called through the
    meta-object and cannot be copied: no header file has its code, Qt's
    source does not mark it or its class for use from outside Qt or writes it
    'inline' or nowhere, and it is no signal, slot or invokable function
    giving back nothing, of a class built on QObject, and Qt's source has no
    code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QSerialPortPrivate.clear' has no cute function yet. Qt's 'bool "
        "QSerialPortPrivate::clear(QSerialPort::Directions directions)': "
        "cannot be called and cannot be called through the meta-object and "
        "cannot be copied: no header file has its code, Qt's source does "
        "not mark it or its class for use from outside Qt or writes it "
        "'inline' or nowhere, and it is no signal, slot or invokable "
        "function giving back nothing, of a class built on QObject, and "
        "Qt's source has no code for it that could be told from the rest.")

  @staticmethod
  def close(*__, **_) -> Never:
    """
    Qt's 'void QSerialPortPrivate::close()': cannot be called and cannot be
    called through the meta-object and cannot be copied: no header file has
    its code, Qt's source does not mark it or its class for use from outside
    Qt or writes it 'inline' or nowhere, and it is no signal, slot or
    invokable function giving back nothing, of a class built on QObject, and
    Qt's source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QSerialPortPrivate.close' has no cute function yet. Qt's 'void "
        "QSerialPortPrivate::close()': cannot be called and cannot be "
        "called through the meta-object and cannot be copied: no header "
        "file has its code, Qt's source does not mark it or its class for "
        "use from outside Qt or writes it 'inline' or nowhere, and it is no "
        "signal, slot or invokable function giving back nothing, of a class "
        "built on QObject, and Qt's source has no code for it that could be "
        "told from the rest.")

  @staticmethod
  def completeAsyncWrite(*__, **_) -> Never:
    """
    Qt's 'bool QSerialPortPrivate::completeAsyncWrite()': leans on
    'QSerialPortPrivate::getSystemError(int) const', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QSerialPortPrivate.completeAsyncWrite' has no cute function yet. "
        "Qt's 'bool QSerialPortPrivate::completeAsyncWrite()': leans on "
        "'QSerialPortPrivate::getSystemError(int) const', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def flush(*__, **_) -> Never:
    """
    Qt's 'bool QSerialPortPrivate::flush()': cannot be called and cannot be
    called through the meta-object and cannot be copied: no header file has
    its code, Qt's source does not mark it or its class for use from outside
    Qt or writes it 'inline' or nowhere, and it is no signal, slot or
    invokable function giving back nothing, of a class built on QObject, and
    Qt's source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QSerialPortPrivate.flush' has no cute function yet. Qt's 'bool "
        "QSerialPortPrivate::flush()': cannot be called and cannot be "
        "called through the meta-object and cannot be copied: no header "
        "file has its code, Qt's source does not mark it or its class for "
        "use from outside Qt or writes it 'inline' or nowhere, and it is no "
        "signal, slot or invokable function giving back nothing, of a class "
        "built on QObject, and Qt's source has no code for it that could be "
        "told from the rest.")

  @staticmethod
  def getSystemError(*__, **_) -> Never:
    """
    Qt's 'QSerialPortErrorInfo QSerialPortPrivate::getSystemError(int
    systemErrorCode) const': cannot be called and cannot be called through
    the meta-object and cannot be copied: no header file has its code, Qt's
    source does not mark it or its class for use from outside Qt or writes it
    'inline' or nowhere, and it is no signal, slot or invokable function
    giving back nothing, of a class built on QObject, and Qt's source has no
    code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QSerialPortPrivate.getSystemError' has no cute function yet. Qt's "
        "'QSerialPortErrorInfo QSerialPortPrivate::getSystemError(int "
        "systemErrorCode) const': cannot be called and cannot be called "
        "through the meta-object and cannot be copied: no header file has "
        "its code, Qt's source does not mark it or its class for use from "
        "outside Qt or writes it 'inline' or nowhere, and it is no signal, "
        "slot or invokable function giving back nothing, of a class built "
        "on QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def getTermios(*__, **_) -> Never:
    """
    Qt's 'bool QSerialPortPrivate::getTermios(termios *tio)': leans on
    'QSerialPortPrivate::getSystemError(int) const', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QSerialPortPrivate.getTermios' has no cute function yet. Qt's "
        "'bool QSerialPortPrivate::getTermios(termios *tio)': leans on "
        "'QSerialPortPrivate::getSystemError(int) const', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def initialize(*__, **_) -> Never:
    """
    Qt's 'bool QSerialPortPrivate::initialize(QIODevice::OpenMode mode)':
    cannot be called and cannot be called through the meta-object and cannot
    be copied: no header file has its code, Qt's source does not mark it or
    its class for use from outside Qt or writes it 'inline' or nowhere, and
    it is no signal, slot or invokable function giving back nothing, of a
    class built on QObject, and Qt's source has no code for it that could be
    told from the rest.
    """
    raise NotImplementedError(
        "'QSerialPortPrivate.initialize' has no cute function yet. Qt's "
        "'bool QSerialPortPrivate::initialize(QIODevice::OpenMode mode)': "
        "cannot be called and cannot be called through the meta-object and "
        "cannot be copied: no header file has its code, Qt's source does "
        "not mark it or its class for use from outside Qt or writes it "
        "'inline' or nowhere, and it is no signal, slot or invokable "
        "function giving back nothing, of a class built on QObject, and "
        "Qt's source has no code for it that could be told from the rest.")

  @staticmethod
  def open(*__, **_) -> Never:
    """
    Qt's 'bool QSerialPortPrivate::open(QIODevice::OpenMode mode)': cannot be
    called and cannot be called through the meta-object and cannot be copied:
    no header file has its code, Qt's source does not mark it or its class
    for use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QSerialPortPrivate.open' has no cute function yet. Qt's 'bool "
        "QSerialPortPrivate::open(QIODevice::OpenMode mode)': cannot be "
        "called and cannot be called through the meta-object and cannot be "
        "copied: no header file has its code, Qt's source does not mark it "
        "or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")

  @staticmethod
  def pinoutSignals(*__, **_) -> Never:
    """
    Qt's 'QSerialPort::PinoutSignals QSerialPortPrivate::pinoutSignals()':
    cannot be called and cannot be called through the meta-object and cannot
    be copied: no header file has its code, Qt's source does not mark it or
    its class for use from outside Qt or writes it 'inline' or nowhere, and
    it is no signal, slot or invokable function giving back nothing, of a
    class built on QObject, and Qt's source has no code for it that could be
    told from the rest.
    """
    raise NotImplementedError(
        "'QSerialPortPrivate.pinoutSignals' has no cute function yet. Qt's "
        "'QSerialPort::PinoutSignals QSerialPortPrivate::pinoutSignals()': "
        "cannot be called and cannot be called through the meta-object and "
        "cannot be copied: no header file has its code, Qt's source does "
        "not mark it or its class for use from outside Qt or writes it "
        "'inline' or nowhere, and it is no signal, slot or invokable "
        "function giving back nothing, of a class built on QObject, and "
        "Qt's source has no code for it that could be told from the rest.")

  @staticmethod
  def readFromPort(*__, **_) -> Never:
    """
    Qt's 'qint64 QSerialPortPrivate::readFromPort(char *data, qint64
    maxSize)': names 'char', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QSerialPortPrivate.readFromPort' has no cute function yet. Qt's "
        "'qint64 QSerialPortPrivate::readFromPort(char *data, qint64 "
        "maxSize)': names 'char', which has no cute class yet.")

  @staticmethod
  def readNotification(*__, **_) -> Never:
    """
    Qt's 'bool QSerialPortPrivate::readNotification()': leans on
    'QSerialPortPrivate::getSystemError(int) const', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QSerialPortPrivate.readNotification' has no cute function yet. "
        "Qt's 'bool QSerialPortPrivate::readNotification()': leans on "
        "'QSerialPortPrivate::getSystemError(int) const', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def sendBreak(*__, **_) -> Never:
    """
    Qt's 'bool QSerialPortPrivate::sendBreak(int duration)': cannot be called
    and cannot be called through the meta-object and cannot be copied: no
    header file has its code, Qt's source does not mark it or its class for
    use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QSerialPortPrivate.sendBreak' has no cute function yet. Qt's "
        "'bool QSerialPortPrivate::sendBreak(int duration)': cannot be "
        "called and cannot be called through the meta-object and cannot be "
        "copied: no header file has its code, Qt's source does not mark it "
        "or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")

  @staticmethod
  def setBaudRate(*__, **_) -> Never:
    """
    - Qt's 'bool QSerialPortPrivate::setBaudRate()': cannot be called and
      cannot be called through the meta-object and cannot be copied: no
      header file has its code, Qt's source does not mark it or its class for
      use from outside Qt or writes it 'inline' or nowhere, and it is no
      signal, slot or invokable function giving back nothing, of a class
      built on QObject, and Qt's source has no code for it that could be told
      from the rest.
    - Qt's 'bool QSerialPortPrivate::setBaudRate(qint32 baudRate,
      QSerialPort::Directions directions)': cannot be called and cannot be
      called through the meta-object and cannot be copied: no header file has
      its code, Qt's source does not mark it or its class for use from
      outside Qt or writes it 'inline' or nowhere, and it is no signal, slot
      or invokable function giving back nothing, of a class built on QObject,
      and Qt's source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QSerialPortPrivate.setBaudRate' has no cute function yet. Qt's "
        "'bool QSerialPortPrivate::setBaudRate()': cannot be called and "
        "cannot be called through the meta-object and cannot be copied: no "
        "header file has its code, Qt's source does not mark it or its "
        "class for use from outside Qt or writes it 'inline' or nowhere, "
        "and it is no signal, slot or invokable function giving back "
        "nothing, of a class built on QObject, and Qt's source has no code "
        "for it that could be told from the rest. Qt's 'bool "
        "QSerialPortPrivate::setBaudRate(qint32 baudRate, "
        "QSerialPort::Directions directions)': cannot be called and cannot "
        "be called through the meta-object and cannot be copied: no header "
        "file has its code, Qt's source does not mark it or its class for "
        "use from outside Qt or writes it 'inline' or nowhere, and it is no "
        "signal, slot or invokable function giving back nothing, of a class "
        "built on QObject, and Qt's source has no code for it that could be "
        "told from the rest.")

  @staticmethod
  def setBreakEnabled(*__, **_) -> Never:
    """
    Qt's 'bool QSerialPortPrivate::setBreakEnabled(bool set)': cannot be
    called and cannot be called through the meta-object and cannot be copied:
    no header file has its code, Qt's source does not mark it or its class
    for use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QSerialPortPrivate.setBreakEnabled' has no cute function yet. "
        "Qt's 'bool QSerialPortPrivate::setBreakEnabled(bool set)': cannot "
        "be called and cannot be called through the meta-object and cannot "
        "be copied: no header file has its code, Qt's source does not mark "
        "it or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")

  @staticmethod
  def setCustomBaudRate(*__, **_) -> Never:
    """
    Qt's 'bool QSerialPortPrivate::setCustomBaudRate(qint32 baudRate,
    QSerialPort::Directions directions)': cannot be called and cannot be
    called through the meta-object and cannot be copied: no header file has
    its code, Qt's source does not mark it or its class for use from outside
    Qt or writes it 'inline' or nowhere, and it is no signal, slot or
    invokable function giving back nothing, of a class built on QObject, and
    Qt's source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QSerialPortPrivate.setCustomBaudRate' has no cute function yet. "
        "Qt's 'bool QSerialPortPrivate::setCustomBaudRate(qint32 baudRate, "
        "QSerialPort::Directions directions)': cannot be called and cannot "
        "be called through the meta-object and cannot be copied: no header "
        "file has its code, Qt's source does not mark it or its class for "
        "use from outside Qt or writes it 'inline' or nowhere, and it is no "
        "signal, slot or invokable function giving back nothing, of a class "
        "built on QObject, and Qt's source has no code for it that could be "
        "told from the rest.")

  @staticmethod
  def setDataBits(*__, **_) -> Never:
    """
    Qt's 'bool QSerialPortPrivate::setDataBits(QSerialPort::DataBits
    dataBits)': cannot be called and cannot be called through the meta-object
    and cannot be copied: no header file has its code, Qt's source does not
    mark it or its class for use from outside Qt or writes it 'inline' or
    nowhere, and it is no signal, slot or invokable function giving back
    nothing, of a class built on QObject, and Qt's source has no code for it
    that could be told from the rest.
    """
    raise NotImplementedError(
        "'QSerialPortPrivate.setDataBits' has no cute function yet. Qt's "
        "'bool QSerialPortPrivate::setDataBits(QSerialPort::DataBits "
        "dataBits)': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def setDataTerminalReady(*__, **_) -> Never:
    """
    Qt's 'bool QSerialPortPrivate::setDataTerminalReady(bool set)': cannot be
    called and cannot be called through the meta-object and cannot be copied:
    no header file has its code, Qt's source does not mark it or its class
    for use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QSerialPortPrivate.setDataTerminalReady' has no cute function "
        "yet. Qt's 'bool QSerialPortPrivate::setDataTerminalReady(bool "
        "set)': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def setFlowControl(*__, **_) -> Never:
    """
    Qt's 'bool QSerialPortPrivate::setFlowControl(QSerialPort::FlowControl
    flowControl)': cannot be called and cannot be called through the
    meta-object and cannot be copied: no header file has its code, Qt's
    source does not mark it or its class for use from outside Qt or writes it
    'inline' or nowhere, and it is no signal, slot or invokable function
    giving back nothing, of a class built on QObject, and Qt's source has no
    code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QSerialPortPrivate.setFlowControl' has no cute function yet. Qt's "
        "'bool QSerialPortPrivate::setFlowControl(QSerialPort::FlowControl "
        "flowControl)': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def setParity(*__, **_) -> Never:
    """
    Qt's 'bool QSerialPortPrivate::setParity(QSerialPort::Parity parity)':
    cannot be called and cannot be called through the meta-object and cannot
    be copied: no header file has its code, Qt's source does not mark it or
    its class for use from outside Qt or writes it 'inline' or nowhere, and
    it is no signal, slot or invokable function giving back nothing, of a
    class built on QObject, and Qt's source has no code for it that could be
    told from the rest.
    """
    raise NotImplementedError(
        "'QSerialPortPrivate.setParity' has no cute function yet. Qt's "
        "'bool QSerialPortPrivate::setParity(QSerialPort::Parity parity)': "
        "cannot be called and cannot be called through the meta-object and "
        "cannot be copied: no header file has its code, Qt's source does "
        "not mark it or its class for use from outside Qt or writes it "
        "'inline' or nowhere, and it is no signal, slot or invokable "
        "function giving back nothing, of a class built on QObject, and "
        "Qt's source has no code for it that could be told from the rest.")

  @staticmethod
  def setReadNotificationEnabled(*__, **_) -> Never:
    """
    Qt's 'void QSerialPortPrivate::setReadNotificationEnabled(bool enable)':
    leans on 'QSerialPortPrivate::getSystemError(int) const', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QSerialPortPrivate.setReadNotificationEnabled' has no cute "
        "function yet. Qt's 'void "
        "QSerialPortPrivate::setReadNotificationEnabled(bool enable)': "
        "leans on 'QSerialPortPrivate::getSystemError(int) const', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def setRequestToSend(*__, **_) -> Never:
    """
    Qt's 'bool QSerialPortPrivate::setRequestToSend(bool set)': cannot be
    called and cannot be called through the meta-object and cannot be copied:
    no header file has its code, Qt's source does not mark it or its class
    for use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QSerialPortPrivate.setRequestToSend' has no cute function yet. "
        "Qt's 'bool QSerialPortPrivate::setRequestToSend(bool set)': cannot "
        "be called and cannot be called through the meta-object and cannot "
        "be copied: no header file has its code, Qt's source does not mark "
        "it or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")

  @staticmethod
  def setStandardBaudRate(*__, **_) -> Never:
    """
    Qt's 'bool QSerialPortPrivate::setStandardBaudRate(qint32 baudRate,
    QSerialPort::Directions directions)': Qt's library has no name for it,
    and its code in Qt's source does not compile apart from its file:
    variable has incomplete type 'struct termios2'.
    """
    raise NotImplementedError(
        "'QSerialPortPrivate.setStandardBaudRate' has no cute function yet. "
        "Qt's 'bool QSerialPortPrivate::setStandardBaudRate(qint32 "
        "baudRate, QSerialPort::Directions directions)': Qt's library has "
        "no name for it, and its code in Qt's source does not compile apart "
        "from its file: variable has incomplete type 'struct termios2'.")

  @staticmethod
  def setStopBits(*__, **_) -> Never:
    """
    Qt's 'bool QSerialPortPrivate::setStopBits(QSerialPort::StopBits
    stopBits)': cannot be called and cannot be called through the meta-object
    and cannot be copied: no header file has its code, Qt's source does not
    mark it or its class for use from outside Qt or writes it 'inline' or
    nowhere, and it is no signal, slot or invokable function giving back
    nothing, of a class built on QObject, and Qt's source has no code for it
    that could be told from the rest.
    """
    raise NotImplementedError(
        "'QSerialPortPrivate.setStopBits' has no cute function yet. Qt's "
        "'bool QSerialPortPrivate::setStopBits(QSerialPort::StopBits "
        "stopBits)': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def setTermios(*__, **_) -> Never:
    """
    Qt's 'bool QSerialPortPrivate::setTermios(const termios *tio)': leans on
    'QSerialPortPrivate::getSystemError(int) const', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QSerialPortPrivate.setTermios' has no cute function yet. Qt's "
        "'bool QSerialPortPrivate::setTermios(const termios *tio)': leans "
        "on 'QSerialPortPrivate::getSystemError(int) const', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def setWriteNotificationEnabled(*__, **_) -> Never:
    """
    Qt's 'void QSerialPortPrivate::setWriteNotificationEnabled(bool enable)':
    leans on 'QSerialPortPrivate::getSystemError(int) const', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QSerialPortPrivate.setWriteNotificationEnabled' has no cute "
        "function yet. Qt's 'void "
        "QSerialPortPrivate::setWriteNotificationEnabled(bool enable)': "
        "leans on 'QSerialPortPrivate::getSystemError(int) const', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def settingFromBaudRate(*__, **_) -> Never:
    """
    Qt's 'qint32 QSerialPortPrivate::settingFromBaudRate(qint32 baudRate)':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: use of undeclared identifier
    'standardBaudRateMap'; did you mean 'standardBaudRates'?.
    """
    raise NotImplementedError(
        "'QSerialPortPrivate.settingFromBaudRate' has no cute function yet. "
        "Qt's 'qint32 QSerialPortPrivate::settingFromBaudRate(qint32 "
        "baudRate)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'standardBaudRateMap'; did you mean "
        "'standardBaudRates'?.")

  @staticmethod
  def standardBaudRates(*__, **_) -> Never:
    """
    Qt's 'QList<qint32> QSerialPortPrivate::standardBaudRates()': cannot be
    called and cannot be called through the meta-object and cannot be copied:
    no header file has its code, Qt's source does not mark it or its class
    for use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QSerialPortPrivate.standardBaudRates' has no cute function yet. "
        "Qt's 'QList<qint32> QSerialPortPrivate::standardBaudRates()': "
        "cannot be called and cannot be called through the meta-object and "
        "cannot be copied: no header file has its code, Qt's source does "
        "not mark it or its class for use from outside Qt or writes it "
        "'inline' or nowhere, and it is no signal, slot or invokable "
        "function giving back nothing, of a class built on QObject, and "
        "Qt's source has no code for it that could be told from the rest.")

  @staticmethod
  def startAsyncRead(*__, **_) -> Never:
    """
    Qt's 'bool QSerialPortPrivate::startAsyncRead()': cannot be called and
    cannot be called through the meta-object and cannot be copied: no header
    file has its code, Qt's source does not mark it or its class for use from
    outside Qt or writes it 'inline' or nowhere, and it is no signal, slot or
    invokable function giving back nothing, of a class built on QObject, and
    Qt's source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QSerialPortPrivate.startAsyncRead' has no cute function yet. Qt's "
        "'bool QSerialPortPrivate::startAsyncRead()': cannot be called and "
        "cannot be called through the meta-object and cannot be copied: no "
        "header file has its code, Qt's source does not mark it or its "
        "class for use from outside Qt or writes it 'inline' or nowhere, "
        "and it is no signal, slot or invokable function giving back "
        "nothing, of a class built on QObject, and Qt's source has no code "
        "for it that could be told from the rest.")

  @staticmethod
  def startAsyncWrite(*__, **_) -> Never:
    """
    Qt's 'bool QSerialPortPrivate::startAsyncWrite()': leans on
    'QSerialPortPrivate::getSystemError(int) const', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QSerialPortPrivate.startAsyncWrite' has no cute function yet. "
        "Qt's 'bool QSerialPortPrivate::startAsyncWrite()': leans on "
        "'QSerialPortPrivate::getSystemError(int) const', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def waitForBytesWritten(*__, **_) -> Never:
    """
    Qt's 'bool QSerialPortPrivate::waitForBytesWritten(int msec)': cannot be
    called and cannot be called through the meta-object and cannot be copied:
    no header file has its code, Qt's source does not mark it or its class
    for use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QSerialPortPrivate.waitForBytesWritten' has no cute function yet. "
        "Qt's 'bool QSerialPortPrivate::waitForBytesWritten(int msec)': "
        "cannot be called and cannot be called through the meta-object and "
        "cannot be copied: no header file has its code, Qt's source does "
        "not mark it or its class for use from outside Qt or writes it "
        "'inline' or nowhere, and it is no signal, slot or invokable "
        "function giving back nothing, of a class built on QObject, and "
        "Qt's source has no code for it that could be told from the rest.")

  @staticmethod
  def waitForReadOrWrite(*__, **_) -> Never:
    """
    Qt's 'bool QSerialPortPrivate::waitForReadOrWrite(bool *selectForRead,
    bool *selectForWrite, bool checkRead, bool checkWrite, int msecs)': leans
    on 'QSerialPortPrivate::getSystemError(int) const', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QSerialPortPrivate.waitForReadOrWrite' has no cute function yet. "
        "Qt's 'bool QSerialPortPrivate::waitForReadOrWrite(bool "
        "*selectForRead, bool *selectForWrite, bool checkRead, bool "
        "checkWrite, int msecs)': leans on "
        "'QSerialPortPrivate::getSystemError(int) const', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def waitForReadyRead(*__, **_) -> Never:
    """
    Qt's 'bool QSerialPortPrivate::waitForReadyRead(int msec)': cannot be
    called and cannot be called through the meta-object and cannot be copied:
    no header file has its code, Qt's source does not mark it or its class
    for use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QSerialPortPrivate.waitForReadyRead' has no cute function yet. "
        "Qt's 'bool QSerialPortPrivate::waitForReadyRead(int msec)': cannot "
        "be called and cannot be called through the meta-object and cannot "
        "be copied: no header file has its code, Qt's source does not mark "
        "it or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")

  @staticmethod
  def writeData(*__, **_) -> Never:
    """
    Qt's 'qint64 QSerialPortPrivate::writeData(const char *data, qint64
    maxSize)': cannot be called and cannot be called through the meta-object
    and cannot be copied: no header file has its code, Qt's source does not
    mark it or its class for use from outside Qt or writes it 'inline' or
    nowhere, and it is no signal, slot or invokable function giving back
    nothing, of a class built on QObject, and Qt's source has no code for it
    that could be told from the rest.
    """
    raise NotImplementedError(
        "'QSerialPortPrivate.writeData' has no cute function yet. Qt's "
        "'qint64 QSerialPortPrivate::writeData(const char *data, qint64 "
        "maxSize)': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")
