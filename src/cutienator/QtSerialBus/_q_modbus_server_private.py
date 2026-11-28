"""
QModbusServerPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSerialBus/6.12.0/QtSerialBus/private/qmodbusserver_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QModbusServerPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum, WAIT
from ..occult import Rituals
from . import QModbusDevicePrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QModbusCommEvent, QModbusRequest, QModbusResponse
  from . import QModbusServer
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QModbusCommEvent = WAIT['QModbusCommEvent']
  QModbusRequest = WAIT['QModbusRequest']


class QModbusServerPrivate(QModbusDevicePrivate):
  """
  The cute side of Qt's QModbusServerPrivate: a plain Python object standing
  in front of one C++ QModbusServerPrivate.

  It is built on the cute 'QModbusDevicePrivate', as Qt's
  QModbusServerPrivate is built on Qt's QModbusDevicePrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QModbusServerPrivate that has a ritual and that
  Python can call so far, 11 names in all: 'q_func',
  'resetCommunicationCounters', 'incrementCounter',
  'processReadCoilsRequest', 'processReadDiscreteInputsRequest',
  'processReadHoldingRegistersRequest', 'processReadInputRegistersRequest',
  'processWriteSingleCoilRequest', 'processWriteSingleRegisterRequest',
  'processWriteMultipleCoilsRequest', 'storeModbusCommEvent'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QModbusServer *QModbusServerPrivate::q_func() const': takes
    in Python what 'QModbusServer *QModbusServerPrivate::q_func()' takes.
  - Qt's 'bool QModbusServerPrivate::setMap(const QModbusDataUnitMap &map)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QModbusResponse QModbusServerPrivate::readBits(const QModbusPdu
    &request, QModbusDataUnit::RegisterType unitType)': takes a type Python
    has no way to hand over yet.

  What has no ritual
  ------------------

  13 of the 28 functions Qt declares: 12 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 1 leans on
  'QModbusServerPrivate.

  What to expect
  --------------

  - The C++ QModbusServerPrivate is created at the first use, not by
    'QModbusServerPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QModbusServerPrivate.
  - Each name of Qt's QModbusServerPrivate that has no cute function yet,
    'processDiagnosticsRequest',
    'processEncapsulatedInterfaceTransportRequest',
    'processGetCommEventCounterRequest', 'processGetCommEventLogRequest',
    'processMaskWriteRegisterRequest', 'processReadExceptionStatusRequest',
    'processReadFifoQueueRequest',
    'processReadWriteMultipleRegistersRequest',
    'processReportServerIdRequest', 'processRequest',
    'processWriteMultipleRegistersRequest', 'readBits', 'readBytes',
    'setMap', 'writeSingle', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QModbusServerPrivate, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class Counter(CuteNum):
    """
    The enum 'QModbusServerPrivate::Counter' of Qt, with the 9 names Qt gives
    in it.
    """

    CommEvent = Kee[int](1)
    BusMessage = Kee[int](11)
    BusCommunicationError = Kee[int](12)
    BusExceptionError = Kee[int](13)
    ServerMessage = Kee[int](14)
    ServerNoResponse = Kee[int](15)
    ServerNAK = Kee[int](16)
    ServerBusy = Kee[int](17)
    BusCharacterOverrun = Kee[int](18)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QModbusServerPrivate'

  #  A C++ QModbusServerPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QModbusServerPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QModbusServerPrivate::QModbusServerPrivate()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qmodbusserverprivate.html#QModbusServerPrivate
    """
    #  QModbusServerPrivate::QModbusServerPrivate()
    self._noteCreation(QModbusServerPrivate, lambda: Rituals.call(
        'ritual_ZN20QModbusServerPrivateC1Ev',
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

  def q_func(self) -> Optional[QModbusServer]:
    """
    Calls Qt's 'QModbusServer *QModbusServerPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qmodbusserverprivate.html#q_func

    Returns
    -------

    Optional[QModbusServer]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QModbusServer *QModbusServerPrivate::q_func()
    address = self.uglySide.call('ritual_ZN20QModbusServerPrivate6q_funcEv')
    from . import QModbusServer
    return QModbusServer._cuteAt(address)

  def resetCommunicationCounters(self) -> None:
    """
    Calls Qt's 'void QModbusServerPrivate::resetCommunicationCounters()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmodbusserverprivate.html
    """
    #  void QModbusServerPrivate::resetCommunicationCounters()
    self.uglySide.call(
        'ritual_ZN20QModbusServerPrivate26resetCommunicationCountersEv',
    )

  @overload(Counter)
  def incrementCounter(self, counter: Counter) -> None:
    """
    Calls Qt's 'void
    QModbusServerPrivate::incrementCounter(QModbusServerPrivate::Counter
    counter)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmodbusserverprivate.html#incrementCounter

    Parameters
    ----------

    counter : Counter
      Passed on as its number.
    """
    #  void QModbusServerPrivate::incrementCounter(QModbusServerPrivate::
    #      Counter counter)
    self.uglySide.call(
        'ritual_ZN20QModbusServerPrivate16incrementCounterENS_7CounterE',
        counter.value,
    )

  @overload(QModbusRequest)
  def processReadCoilsRequest(
      self,
      request: QModbusRequest,
  ) -> QModbusResponse:
    """
    Calls Qt's 'QModbusResponse
    QModbusServerPrivate::processReadCoilsRequest(const QModbusRequest
    &request)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmodbusserverprivate.html#processReadCoilsRequest

    Parameters
    ----------

    request : QModbusRequest
      Passed on as a value: Qt reads the C++ QModbusRequest, which stays
      Python's own.

    Returns
    -------

    QModbusResponse
      A new cute QModbusResponse around the copy Qt gave back. Python owns
      it.
    """
    #  QModbusResponse QModbusServerPrivate::processReadCoilsRequest(const
    #      QModbusRequest &request)
    address = self.uglySide.call(
        'ritual_ZN20QModbusServerPrivate23processReadCoilsRequestERK14QModb'
        'usRequest',
        self._valueOf(request),
    )
    from . import QModbusResponse
    return QModbusResponse._cuteOwning(address)

  @overload(QModbusRequest)
  def processReadDiscreteInputsRequest(
      self,
      request: QModbusRequest,
  ) -> QModbusResponse:
    """
    Calls Qt's 'QModbusResponse
    QModbusServerPrivate::processReadDiscreteInputsRequest(const
    QModbusRequest &request)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmodbusserverprivate.html

    Parameters
    ----------

    request : QModbusRequest
      Passed on as a value: Qt reads the C++ QModbusRequest, which stays
      Python's own.

    Returns
    -------

    QModbusResponse
      A new cute QModbusResponse around the copy Qt gave back. Python owns
      it.
    """
    #  QModbusResponse
    #      QModbusServerPrivate::processReadDiscreteInputsRequest(const
    #      QModbusRequest &request)
    address = self.uglySide.call(
        'ritual_ZN20QModbusServerPrivate32processReadDiscreteInputsRequestE'
        'RK14QModbusRequest',
        self._valueOf(request),
    )
    from . import QModbusResponse
    return QModbusResponse._cuteOwning(address)

  @overload(QModbusRequest)
  def processReadHoldingRegistersRequest(
      self,
      request: QModbusRequest,
  ) -> QModbusResponse:
    """
    Calls Qt's 'QModbusResponse
    QModbusServerPrivate::processReadHoldingRegistersRequest(const
    QModbusRequest &request)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmodbusserverprivate.html

    Parameters
    ----------

    request : QModbusRequest
      Passed on as a value: Qt reads the C++ QModbusRequest, which stays
      Python's own.

    Returns
    -------

    QModbusResponse
      A new cute QModbusResponse around the copy Qt gave back. Python owns
      it.
    """
    #  QModbusResponse
    #      QModbusServerPrivate::processReadHoldingRegistersRequest(const
    #      QModbusRequest &request)
    address = self.uglySide.call(
        'ritual_ZN20QModbusServerPrivate34processReadHoldingRegistersReques'
        'tERK14QModbusRequest',
        self._valueOf(request),
    )
    from . import QModbusResponse
    return QModbusResponse._cuteOwning(address)

  @overload(QModbusRequest)
  def processReadInputRegistersRequest(
      self,
      request: QModbusRequest,
  ) -> QModbusResponse:
    """
    Calls Qt's 'QModbusResponse
    QModbusServerPrivate::processReadInputRegistersRequest(const
    QModbusRequest &request)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmodbusserverprivate.html

    Parameters
    ----------

    request : QModbusRequest
      Passed on as a value: Qt reads the C++ QModbusRequest, which stays
      Python's own.

    Returns
    -------

    QModbusResponse
      A new cute QModbusResponse around the copy Qt gave back. Python owns
      it.
    """
    #  QModbusResponse
    #      QModbusServerPrivate::processReadInputRegistersRequest(const
    #      QModbusRequest &request)
    address = self.uglySide.call(
        'ritual_ZN20QModbusServerPrivate32processReadInputRegistersRequestE'
        'RK14QModbusRequest',
        self._valueOf(request),
    )
    from . import QModbusResponse
    return QModbusResponse._cuteOwning(address)

  @overload(QModbusRequest)
  def processWriteSingleCoilRequest(
      self,
      request: QModbusRequest,
  ) -> QModbusResponse:
    """
    Calls Qt's 'QModbusResponse
    QModbusServerPrivate::processWriteSingleCoilRequest(const QModbusRequest
    &request)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmodbusserverprivate.html

    Parameters
    ----------

    request : QModbusRequest
      Passed on as a value: Qt reads the C++ QModbusRequest, which stays
      Python's own.

    Returns
    -------

    QModbusResponse
      A new cute QModbusResponse around the copy Qt gave back. Python owns
      it.
    """
    #  QModbusResponse
    #      QModbusServerPrivate::processWriteSingleCoilRequest(const
    #      QModbusRequest &request)
    address = self.uglySide.call(
        'ritual_ZN20QModbusServerPrivate29processWriteSingleCoilRequestERK1'
        '4QModbusRequest',
        self._valueOf(request),
    )
    from . import QModbusResponse
    return QModbusResponse._cuteOwning(address)

  @overload(QModbusRequest)
  def processWriteSingleRegisterRequest(
      self,
      request: QModbusRequest,
  ) -> QModbusResponse:
    """
    Calls Qt's 'QModbusResponse
    QModbusServerPrivate::processWriteSingleRegisterRequest(const
    QModbusRequest &request)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmodbusserverprivate.html

    Parameters
    ----------

    request : QModbusRequest
      Passed on as a value: Qt reads the C++ QModbusRequest, which stays
      Python's own.

    Returns
    -------

    QModbusResponse
      A new cute QModbusResponse around the copy Qt gave back. Python owns
      it.
    """
    #  QModbusResponse
    #      QModbusServerPrivate::processWriteSingleRegisterRequest(const
    #      QModbusRequest &request)
    address = self.uglySide.call(
        'ritual_ZN20QModbusServerPrivate33processWriteSingleRegisterRequest'
        'ERK14QModbusRequest',
        self._valueOf(request),
    )
    from . import QModbusResponse
    return QModbusResponse._cuteOwning(address)

  @overload(QModbusRequest)
  def processWriteMultipleCoilsRequest(
      self,
      request: QModbusRequest,
  ) -> QModbusResponse:
    """
    Calls Qt's 'QModbusResponse
    QModbusServerPrivate::processWriteMultipleCoilsRequest(const
    QModbusRequest &request)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmodbusserverprivate.html

    Parameters
    ----------

    request : QModbusRequest
      Passed on as a value: Qt reads the C++ QModbusRequest, which stays
      Python's own.

    Returns
    -------

    QModbusResponse
      A new cute QModbusResponse around the copy Qt gave back. Python owns
      it.
    """
    #  QModbusResponse
    #      QModbusServerPrivate::processWriteMultipleCoilsRequest(const
    #      QModbusRequest &request)
    address = self.uglySide.call(
        'ritual_ZN20QModbusServerPrivate32processWriteMultipleCoilsRequestE'
        'RK14QModbusRequest',
        self._valueOf(request),
    )
    from . import QModbusResponse
    return QModbusResponse._cuteOwning(address)

  @overload(QModbusCommEvent)
  def storeModbusCommEvent(self, eventByte: QModbusCommEvent) -> None:
    """
    Calls Qt's 'void QModbusServerPrivate::storeModbusCommEvent(const
    QModbusCommEvent &eventByte)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmodbusserverprivate.html#storeModbusCommEvent

    Parameters
    ----------

    eventByte : QModbusCommEvent
      Passed on as a value: Qt reads the C++ QModbusCommEvent, which stays
      Python's own.
    """
    #  void QModbusServerPrivate::storeModbusCommEvent(const QModbusCommEvent
    #      &eventByte)
    self.uglySide.call(
        'ritual_ZN20QModbusServerPrivate20storeModbusCommEventERK16QModbusC'
        'ommEvent',
        self._valueOf(eventByte),
    )

  @staticmethod
  def processDiagnosticsRequest(*__, **_) -> Never:
    """
    Qt's 'QModbusResponse
    QModbusServerPrivate::processDiagnosticsRequest(const QModbusRequest
    &request)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: use of undeclared identifier
    'CHECK_SIZE_EQUALS'.
    """
    raise NotImplementedError(
        "'QModbusServerPrivate.processDiagnosticsRequest' has no cute "
        "function yet. Qt's 'QModbusResponse "
        "QModbusServerPrivate::processDiagnosticsRequest(const "
        "QModbusRequest &request)': Qt's library has no name for it, and "
        "its code in Qt's source does not compile apart from its file: use "
        "of undeclared identifier 'CHECK_SIZE_EQUALS'.")

  @staticmethod
  def processEncapsulatedInterfaceTransportRequest(*__, **_) -> Never:
    """
    Qt's 'QModbusResponse
    QModbusServerPrivate::processEncapsulatedInterfaceTransportRequest(const
    QModbusRequest &request)': Qt's library has no name for it, and its code
    in Qt's source does not compile apart from its file: use of undeclared
    identifier 'CHECK_SIZE_LESS_THAN'.
    """
    raise NotImplementedError(
        "'QModbusServerPrivate.processEncapsulatedInterfaceTransportRequest'"
        " has no cute function yet. Qt's 'QModbusResponse "
        "QModbusServerPrivate::processEncapsulatedInterfaceTransportRequest("
        "const QModbusRequest &request)': Qt's library has no name for it, "
        "and its code in Qt's source does not compile apart from its file: "
        "use of undeclared identifier 'CHECK_SIZE_LESS_THAN'.")

  @staticmethod
  def processGetCommEventCounterRequest(*__, **_) -> Never:
    """
    Qt's 'QModbusResponse
    QModbusServerPrivate::processGetCommEventCounterRequest(const
    QModbusRequest &request)': Qt's library has no name for it, and its code
    in Qt's source does not compile apart from its file: use of undeclared
    identifier 'CHECK_SIZE_EQUALS'.
    """
    raise NotImplementedError(
        "'QModbusServerPrivate.processGetCommEventCounterRequest' has no "
        "cute function yet. Qt's 'QModbusResponse "
        "QModbusServerPrivate::processGetCommEventCounterRequest(const "
        "QModbusRequest &request)': Qt's library has no name for it, and "
        "its code in Qt's source does not compile apart from its file: use "
        "of undeclared identifier 'CHECK_SIZE_EQUALS'.")

  @staticmethod
  def processGetCommEventLogRequest(*__, **_) -> Never:
    """
    Qt's 'QModbusResponse
    QModbusServerPrivate::processGetCommEventLogRequest(const QModbusRequest
    &request)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: use of undeclared identifier
    'CHECK_SIZE_EQUALS'.
    """
    raise NotImplementedError(
        "'QModbusServerPrivate.processGetCommEventLogRequest' has no cute "
        "function yet. Qt's 'QModbusResponse "
        "QModbusServerPrivate::processGetCommEventLogRequest(const "
        "QModbusRequest &request)': Qt's library has no name for it, and "
        "its code in Qt's source does not compile apart from its file: use "
        "of undeclared identifier 'CHECK_SIZE_EQUALS'.")

  @staticmethod
  def processMaskWriteRegisterRequest(*__, **_) -> Never:
    """
    Qt's 'QModbusResponse
    QModbusServerPrivate::processMaskWriteRegisterRequest(const
    QModbusRequest &request)': Qt's library has no name for it, and its code
    in Qt's source does not compile apart from its file: use of undeclared
    identifier 'CHECK_SIZE_EQUALS'.
    """
    raise NotImplementedError(
        "'QModbusServerPrivate.processMaskWriteRegisterRequest' has no cute "
        "function yet. Qt's 'QModbusResponse "
        "QModbusServerPrivate::processMaskWriteRegisterRequest(const "
        "QModbusRequest &request)': Qt's library has no name for it, and "
        "its code in Qt's source does not compile apart from its file: use "
        "of undeclared identifier 'CHECK_SIZE_EQUALS'.")

  @staticmethod
  def processReadExceptionStatusRequest(*__, **_) -> Never:
    """
    Qt's 'QModbusResponse
    QModbusServerPrivate::processReadExceptionStatusRequest(const
    QModbusRequest &request)': Qt's library has no name for it, and its code
    in Qt's source does not compile apart from its file: use of undeclared
    identifier 'CHECK_SIZE_EQUALS'.
    """
    raise NotImplementedError(
        "'QModbusServerPrivate.processReadExceptionStatusRequest' has no "
        "cute function yet. Qt's 'QModbusResponse "
        "QModbusServerPrivate::processReadExceptionStatusRequest(const "
        "QModbusRequest &request)': Qt's library has no name for it, and "
        "its code in Qt's source does not compile apart from its file: use "
        "of undeclared identifier 'CHECK_SIZE_EQUALS'.")

  @staticmethod
  def processReadFifoQueueRequest(*__, **_) -> Never:
    """
    Qt's 'QModbusResponse
    QModbusServerPrivate::processReadFifoQueueRequest(const QModbusRequest
    &request)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: use of undeclared identifier
    'CHECK_SIZE_LESS_THAN'.
    """
    raise NotImplementedError(
        "'QModbusServerPrivate.processReadFifoQueueRequest' has no cute "
        "function yet. Qt's 'QModbusResponse "
        "QModbusServerPrivate::processReadFifoQueueRequest(const "
        "QModbusRequest &request)': Qt's library has no name for it, and "
        "its code in Qt's source does not compile apart from its file: use "
        "of undeclared identifier 'CHECK_SIZE_LESS_THAN'.")

  @staticmethod
  def processReadWriteMultipleRegistersRequest(*__, **_) -> Never:
    """
    Qt's 'QModbusResponse
    QModbusServerPrivate::processReadWriteMultipleRegistersRequest(const
    QModbusRequest &request)': Qt's library has no name for it, and its code
    in Qt's source does not compile apart from its file: use of undeclared
    identifier 'CHECK_SIZE_LESS_THAN'.
    """
    raise NotImplementedError(
        "'QModbusServerPrivate.processReadWriteMultipleRegistersRequest' "
        "has no cute function yet. Qt's 'QModbusResponse "
        "QModbusServerPrivate::processReadWriteMultipleRegistersRequest(cons"
        "t QModbusRequest &request)': Qt's library has no name for it, and "
        "its code in Qt's source does not compile apart from its file: use "
        "of undeclared identifier 'CHECK_SIZE_LESS_THAN'.")

  @staticmethod
  def processReportServerIdRequest(*__, **_) -> Never:
    """
    Qt's 'QModbusResponse
    QModbusServerPrivate::processReportServerIdRequest(const QModbusRequest
    &request)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: use of undeclared identifier
    'CHECK_SIZE_EQUALS'.
    """
    raise NotImplementedError(
        "'QModbusServerPrivate.processReportServerIdRequest' has no cute "
        "function yet. Qt's 'QModbusResponse "
        "QModbusServerPrivate::processReportServerIdRequest(const "
        "QModbusRequest &request)': Qt's library has no name for it, and "
        "its code in Qt's source does not compile apart from its file: use "
        "of undeclared identifier 'CHECK_SIZE_EQUALS'.")

  @staticmethod
  def processRequest(*__, **_) -> Never:
    """
    Qt's 'QModbusResponse QModbusServerPrivate::processRequest(const
    QModbusPdu &request)': leans on
    'QModbusServerPrivate::processDiagnosticsRequest(QModbusRequest const&)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QModbusServerPrivate.processRequest' has no cute function yet. "
        "Qt's 'QModbusResponse QModbusServerPrivate::processRequest(const "
        "QModbusPdu &request)': leans on "
        "'QModbusServerPrivate::processDiagnosticsRequest(QModbusRequest "
        "const&)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def processWriteMultipleRegistersRequest(*__, **_) -> Never:
    """
    Qt's 'QModbusResponse
    QModbusServerPrivate::processWriteMultipleRegistersRequest(const
    QModbusRequest &request)': Qt's library has no name for it, and its code
    in Qt's source does not compile apart from its file: use of undeclared
    identifier 'CHECK_SIZE_LESS_THAN'.
    """
    raise NotImplementedError(
        "'QModbusServerPrivate.processWriteMultipleRegistersRequest' has no "
        "cute function yet. Qt's 'QModbusResponse "
        "QModbusServerPrivate::processWriteMultipleRegistersRequest(const "
        "QModbusRequest &request)': Qt's library has no name for it, and "
        "its code in Qt's source does not compile apart from its file: use "
        "of undeclared identifier 'CHECK_SIZE_LESS_THAN'.")

  @staticmethod
  def readBits(*__, **_) -> Never:
    """
    Qt's 'QModbusResponse QModbusServerPrivate::readBits(const QModbusPdu
    &request, QModbusDataUnit::RegisterType unitType)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QModbusServerPrivate.readBits' has no cute function yet. Qt's "
        "'QModbusResponse QModbusServerPrivate::readBits(const QModbusPdu "
        "&request, QModbusDataUnit::RegisterType unitType)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def readBytes(*__, **_) -> Never:
    """
    Qt's 'QModbusResponse QModbusServerPrivate::readBytes(const QModbusPdu
    &request, QModbusDataUnit::RegisterType unitType)': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: use of undeclared identifier 'CHECK_SIZE_EQUALS'.
    """
    raise NotImplementedError(
        "'QModbusServerPrivate.readBytes' has no cute function yet. Qt's "
        "'QModbusResponse QModbusServerPrivate::readBytes(const QModbusPdu "
        "&request, QModbusDataUnit::RegisterType unitType)': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier "
        "'CHECK_SIZE_EQUALS'.")

  @staticmethod
  def setMap(*__, **_) -> Never:
    """
    Qt's 'bool QModbusServerPrivate::setMap(const QModbusDataUnitMap &map)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QModbusServerPrivate.setMap' has no cute function yet. Qt's 'bool "
        "QModbusServerPrivate::setMap(const QModbusDataUnitMap &map)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def writeSingle(*__, **_) -> Never:
    """
    Qt's 'QModbusResponse QModbusServerPrivate::writeSingle(const QModbusPdu
    &request, QModbusDataUnit::RegisterType unitType)': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: use of undeclared identifier 'CHECK_SIZE_EQUALS'.
    """
    raise NotImplementedError(
        "'QModbusServerPrivate.writeSingle' has no cute function yet. Qt's "
        "'QModbusResponse QModbusServerPrivate::writeSingle(const "
        "QModbusPdu &request, QModbusDataUnit::RegisterType unitType)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'CHECK_SIZE_EQUALS'.")
