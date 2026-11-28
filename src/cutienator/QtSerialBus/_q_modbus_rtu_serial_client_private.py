"""
QModbusRtuSerialClientPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSerialBus/6.12.0/QtSerialBus/private/qmodbusrtuserialclient_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QModbusRtuSerialClientPrivate to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QModbusClientPrivate, QModbusReply
from ..QtSerialPort import QSerialPort

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QIODevice
  from . import QModbusDataUnit, QModbusRequest, QModbusResponse
  from . import QModbusRtuSerialClient
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QModbusDataUnit = WAIT['QModbusDataUnit']
  QModbusRequest = WAIT['QModbusRequest']
  QModbusResponse = WAIT['QModbusResponse']


class QModbusRtuSerialClientPrivate(QModbusClientPrivate):
  """
  The cute side of Qt's QModbusRtuSerialClientPrivate: a plain Python object
  standing in front of one C++ QModbusRtuSerialClientPrivate.

  It is built on the cute 'QModbusClientPrivate', as Qt's
  QModbusRtuSerialClientPrivate is built on Qt's QModbusClientPrivate, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QModbusRtuSerialClientPrivate that has a ritual and
  that Python can call so far, 13 names in all: 'q_func', 'onReadyRead',
  'onAboutToClose', 'onResponseTimeout', 'onBytesWritten', 'onError',
  'setupEnvironment', 'enqueueRequest', 'scheduleNextRequest',
  'processQueue', 'canMatchRequestAndResponse', 'isOpen', 'device'. None can
  be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QModbusRtuSerialClient
    *QModbusRtuSerialClientPrivate::q_func() const': takes in Python what
    'QModbusRtuSerialClient *QModbusRtuSerialClientPrivate::q_func()' takes.

  What has no ritual
  ------------------

  1 of the 15 functions Qt declares: 1 leans on 'Timer.

  What to expect
  --------------

  - The C++ QModbusRtuSerialClientPrivate is created at the first use, not by
    'QModbusRtuSerialClientPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QModbusRtuSerialClientPrivate.
  - Each name of Qt's QModbusRtuSerialClientPrivate that has no cute function
    yet, 'setupSerialPort', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QModbusRtuSerialClientPrivate'

  #  A C++ QModbusRtuSerialClientPrivate Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QModbusRtuSerialClientPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QModbusResponse, int)
  def canMatchRequestAndResponse(
      self,
      response: QModbusResponse,
      sendingServer: int,
  ) -> bool:
    """
    Calls Qt's 'bool
    QModbusRtuSerialClientPrivate::canMatchRequestAndResponse(const
    QModbusResponse &response, int sendingServer) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmodbusrtuserialclientprivate.html

    Parameters
    ----------

    response : QModbusResponse
      Passed on as a value: Qt reads the C++ QModbusResponse, which stays
      Python's own.

    sendingServer : int
      Passed on as it is.
    """
    #  bool QModbusRtuSerialClientPrivate::canMatchRequestAndResponse(const
    #      QModbusResponse &response, int sendingServer) const
    return self.uglySide.call(
        'ritual_ZNK29QModbusRtuSerialClientPrivate26canMatchRequestAndRespo'
        'nseERK15QModbusResponsei',
        self._valueOf(response), sendingServer,
    )

  def isOpen(self) -> bool:
    """
    Calls Qt's 'bool QModbusRtuSerialClientPrivate::isOpen() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmodbusrtuserialclientprivate.html#isOpen
    """
    #  bool QModbusRtuSerialClientPrivate::isOpen() const
    ritual = 'ritual_ZNK29QModbusRtuSerialClientPrivate6isOpenEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK29QModbusRtuSerialClientPrivate6isOpenEv'
    return self.uglySide.call(ritual)

  def device(self) -> Optional[QIODevice]:
    """
    Calls Qt's 'QIODevice *QModbusRtuSerialClientPrivate::device() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmodbusrtuserialclientprivate.html#device

    Returns
    -------

    Optional[QIODevice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QIODevice *QModbusRtuSerialClientPrivate::device() const
    ritual = 'ritual_ZNK29QModbusRtuSerialClientPrivate6deviceEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK29QModbusRtuSerialClientPrivate6deviceEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QIODevice
    return QIODevice._cuteAt(address)

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

  def q_func(self) -> Optional[QModbusRtuSerialClient]:
    """
    Calls Qt's 'QModbusRtuSerialClient
    *QModbusRtuSerialClientPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmodbusrtuserialclientprivate.html#q_func

    Returns
    -------

    Optional[QModbusRtuSerialClient]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QModbusRtuSerialClient *QModbusRtuSerialClientPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN29QModbusRtuSerialClientPrivate6q_funcEv',
    )
    from . import QModbusRtuSerialClient
    return QModbusRtuSerialClient._cuteAt(address)

  def onReadyRead(self) -> None:
    """
    Calls Qt's 'void QModbusRtuSerialClientPrivate::onReadyRead()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmodbusrtuserialclientprivate.html#onReadyRead
    """
    #  void QModbusRtuSerialClientPrivate::onReadyRead()
    self.uglySide.call(
        'ritual_ZN29QModbusRtuSerialClientPrivate11onReadyReadEv',
    )

  def onAboutToClose(self) -> None:
    """
    Calls Qt's 'void QModbusRtuSerialClientPrivate::onAboutToClose()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmodbusrtuserialclientprivate.html#onAboutToClose
    """
    #  void QModbusRtuSerialClientPrivate::onAboutToClose()
    self.uglySide.call(
        'ritual_ZN29QModbusRtuSerialClientPrivate14onAboutToCloseEv',
    )

  @overload(int)
  def onResponseTimeout(self, timerId: int) -> None:
    """
    Calls Qt's 'void QModbusRtuSerialClientPrivate::onResponseTimeout(int
    timerId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmodbusrtuserialclientprivate.html

    Parameters
    ----------

    timerId : int
      Passed on as it is.
    """
    #  void QModbusRtuSerialClientPrivate::onResponseTimeout(int timerId)
    self.uglySide.call(
        'ritual_ZN29QModbusRtuSerialClientPrivate17onResponseTimeoutEi',
        timerId,
    )

  @overload(int)
  def onBytesWritten(self, bytes: int) -> None:
    """
    Calls Qt's 'void QModbusRtuSerialClientPrivate::onBytesWritten(qint64
    bytes)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmodbusrtuserialclientprivate.html#onBytesWritten

    Parameters
    ----------

    bytes : int
      Passed on as it is.
    """
    #  void QModbusRtuSerialClientPrivate::onBytesWritten(qint64 bytes)
    self.uglySide.call(
        'ritual_ZN29QModbusRtuSerialClientPrivate14onBytesWrittenEx', bytes,
    )

  @overload(QSerialPort.SerialPortError)
  def onError(self, error: QSerialPort.SerialPortError) -> None:
    """
    Calls Qt's 'void
    QModbusRtuSerialClientPrivate::onError(QSerialPort::SerialPortError
    error)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmodbusrtuserialclientprivate.html#onError

    Parameters
    ----------

    error : QSerialPort.SerialPortError
      Passed on as its number.
    """
    #  void QModbusRtuSerialClientPrivate::onError(QSerialPort::
    #      SerialPortError error)
    self.uglySide.call(
        'ritual_ZN29QModbusRtuSerialClientPrivate7onErrorEN11QSerialPort15S'
        'erialPortErrorE',
        error.value,
    )

  def setupEnvironment(self) -> None:
    """
    Calls Qt's 'void QModbusRtuSerialClientPrivate::setupEnvironment()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmodbusrtuserialclientprivate.html
    """
    #  void QModbusRtuSerialClientPrivate::setupEnvironment()
    self.uglySide.call(
        'ritual_ZN29QModbusRtuSerialClientPrivate16setupEnvironmentEv',
    )

  @overload(QModbusRequest, int, QModbusDataUnit, QModbusReply.ReplyType)
  def enqueueRequest(
      self,
      request: QModbusRequest,
      serverAddress: int,
      unit: QModbusDataUnit,
      type: QModbusReply.ReplyType,
  ) -> Optional[QModbusReply]:
    """
    Calls Qt's 'QModbusReply
    *QModbusRtuSerialClientPrivate::enqueueRequest(const QModbusRequest
    &request, int serverAddress, const QModbusDataUnit &unit,
    QModbusReply::ReplyType type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmodbusrtuserialclientprivate.html#enqueueRequest

    Parameters
    ----------

    request : QModbusRequest
      Passed on as a value: Qt reads the C++ QModbusRequest, which stays
      Python's own.

    serverAddress : int
      Passed on as it is.

    unit : QModbusDataUnit
      Passed on as a value: Qt reads the C++ QModbusDataUnit, which stays
      Python's own.

    type : QModbusReply.ReplyType
      Passed on as its number.

    Returns
    -------

    Optional[QModbusReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QModbusReply *QModbusRtuSerialClientPrivate::enqueueRequest(const
    #      QModbusRequest &request, int serverAddress, const QModbusDataUnit
    #      &unit, QModbusReply::ReplyType type)
    ritual = (
        'ritual_ZN29QModbusRtuSerialClientPrivate14enqueueRequestERK14QModb'
        'usRequestiRK15QModbusDataUnitN12QModbusReply9ReplyTypeE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN29QModbusRtuSerialClientPrivate14enqueueRequestERK1'
          '4QModbusRequestiRK15QModbusDataUnitN12QModbusReply9ReplyTypeE')
    address = self.uglySide.call(
        ritual,
        self._valueOf(request), serverAddress, self._valueOf(unit),
        type.value,
    )
    return QModbusReply._cuteAt(address)

  @overload(int)
  def scheduleNextRequest(self, delay: int) -> None:
    """
    Calls Qt's 'void QModbusRtuSerialClientPrivate::scheduleNextRequest(int
    delay)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmodbusrtuserialclientprivate.html

    Parameters
    ----------

    delay : int
      Passed on as it is.
    """
    #  void QModbusRtuSerialClientPrivate::scheduleNextRequest(int delay)
    self.uglySide.call(
        'ritual_ZN29QModbusRtuSerialClientPrivate19scheduleNextRequestEi',
        delay,
    )

  def processQueue(self) -> None:
    """
    Calls Qt's 'void QModbusRtuSerialClientPrivate::processQueue()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmodbusrtuserialclientprivate.html#processQueue
    """
    #  void QModbusRtuSerialClientPrivate::processQueue()
    self.uglySide.call(
        'ritual_ZN29QModbusRtuSerialClientPrivate12processQueueEv',
    )

  @staticmethod
  def setupSerialPort(*__, **_) -> Never:
    """
    Qt's 'void QModbusRtuSerialClientPrivate::setupSerialPort()': leans on
    'Timer::staticMetaObject', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QModbusRtuSerialClientPrivate.setupSerialPort' has no cute "
        "function yet. Qt's 'void "
        "QModbusRtuSerialClientPrivate::setupSerialPort()': leans on "
        "'Timer::staticMetaObject', which Qt's source does not mark for use "
        "from outside Qt and has no code for that could be taken.")
