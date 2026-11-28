"""
QWebSocketDataProcessor binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWebSockets/6.12.0/QtWebSockets/private/qwebsocketdataprocessor_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QWebSocketDataProcessor to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QWebSocketProtocol

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QMetaObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']


class QWebSocketDataProcessor(QObject):
  """
  The cute side of Qt's QWebSocketDataProcessor: a plain Python object
  standing in front of one C++ QWebSocketDataProcessor.

  It is built on the cute 'QObject', as Qt's QWebSocketDataProcessor is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QWebSocketDataProcessor that has a ritual and that
  Python can call so far, 16 names in all: 'metaObject',
  'setMaxAllowedFrameSize', 'maxAllowedFrameSize',
  'setMaxAllowedMessageSize', 'maxAllowedMessageSize', 'maxMessageSize',
  'maxFrameSize', 'pingReceived', 'pongReceived', 'closeReceived',
  'textFrameReceived', 'binaryFrameReceived', 'textMessageReceived',
  'binaryMessageReceived', 'errorEncountered', 'clear'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QWebSocketDataProcessor::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QWebSocketDataProcessor::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QWebSocketDataProcessor::~QWebSocketDataProcessor()': the
    destructor: Python never removes a C++ QWebSocketDataProcessor.
  - Qt's 'void
    QWebSocketDataProcessor::setIdleTimeout(std::chrono::milliseconds
    timeout)': takes a type Python has no way to hand over yet.
  - Qt's 'std::chrono::milliseconds QWebSocketDataProcessor::idleTimeout()
    const': gives a type Python has no way to take yet.

  What has no ritual
  ------------------

  10 of the 31 functions Qt declares: 6 leans on 'QWebSocketDataProcessor; 2
  not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QWebSocketDataProcessor is created at the first use, not by
    'QWebSocketDataProcessor(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWebSocketDataProcessor.
  - Qt tells when it has removed the C++ QWebSocketDataProcessor. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QWebSocketDataProcessor that has no cute function yet,
    '__init__', 'idleTimeout', 'process', 'processControlFrame',
    'reportError', 'setIdleTimeout', 'timeout', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def maxMessageSize() -> int:
    """
    Calls Qt's 'quint64 QWebSocketDataProcessor::maxMessageSize()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocketdataprocessor.html#maxMessageSize
    """
    #  quint64 QWebSocketDataProcessor::maxMessageSize()
    return Rituals.call(
        'ritual_ZN23QWebSocketDataProcessor14maxMessageSizeEv',
    )

  @staticmethod
  def maxFrameSize() -> int:
    """
    Calls Qt's 'quint64 QWebSocketDataProcessor::maxFrameSize()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocketdataprocessor.html#maxFrameSize
    """
    #  quint64 QWebSocketDataProcessor::maxFrameSize()
    return Rituals.call('ritual_ZN23QWebSocketDataProcessor12maxFrameSizeEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWebSocketDataProcessor'

  #  A C++ QWebSocketDataProcessor Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QWebSocketDataProcessor'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QWebSocketDataProcessor::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocketdataprocessor.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QWebSocketDataProcessor::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK23QWebSocketDataProcessor10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def maxAllowedFrameSize(self) -> int:
    """
    Calls Qt's 'quint64 QWebSocketDataProcessor::maxAllowedFrameSize()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocketdataprocessor.html#maxAllowedFrameSize
    """
    #  quint64 QWebSocketDataProcessor::maxAllowedFrameSize() const
    return self.uglySide.call(
        'ritual_ZNK23QWebSocketDataProcessor19maxAllowedFrameSizeEv',
    )

  def maxAllowedMessageSize(self) -> int:
    """
    Calls Qt's 'quint64 QWebSocketDataProcessor::maxAllowedMessageSize()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocketdataprocessor.html#maxAllowedMessageSize
    """
    #  quint64 QWebSocketDataProcessor::maxAllowedMessageSize() const
    return self.uglySide.call(
        'ritual_ZNK23QWebSocketDataProcessor21maxAllowedMessageSizeEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setMaxAllowedFrameSize(self, maxAllowedFrameSize: int) -> None:
    """
    Calls Qt's 'void QWebSocketDataProcessor::setMaxAllowedFrameSize(quint64
    maxAllowedFrameSize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocketdataprocessor.html

    Parameters
    ----------

    maxAllowedFrameSize : int
      Passed on as it is.
    """
    #  void QWebSocketDataProcessor::setMaxAllowedFrameSize(quint64
    #      maxAllowedFrameSize)
    self.uglySide.call(
        'ritual_ZN23QWebSocketDataProcessor22setMaxAllowedFrameSizeEy',
        maxAllowedFrameSize,
    )

  @overload(int)
  def setMaxAllowedMessageSize(self, maxAllowedMessageSize: int) -> None:
    """
    Calls Qt's 'void
    QWebSocketDataProcessor::setMaxAllowedMessageSize(quint64
    maxAllowedMessageSize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocketdataprocessor.html

    Parameters
    ----------

    maxAllowedMessageSize : int
      Passed on as it is.
    """
    #  void QWebSocketDataProcessor::setMaxAllowedMessageSize(quint64
    #      maxAllowedMessageSize)
    self.uglySide.call(
        'ritual_ZN23QWebSocketDataProcessor24setMaxAllowedMessageSizeEy',
        maxAllowedMessageSize,
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QWebSocketDataProcessor::QWebSocketDataProcessor(QObject *parent)':
    leans on 'QWebSocketDataProcessor::qt_metacall(QMetaObject::Call, int,
    void**)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QWebSocketDataProcessor.__init__' has no cute function yet. Qt's "
        "'QWebSocketDataProcessor::QWebSocketDataProcessor(QObject "
        "*parent)': leans on "
        "'QWebSocketDataProcessor::qt_metacall(QMetaObject::Call, int, "
        "void**)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

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
  def pingReceived(self, data: QByteArray) -> None:
    """
    Calls Qt's 'void QWebSocketDataProcessor::pingReceived(const QByteArray
    &data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocketdataprocessor.html#pingReceived

    Parameters
    ----------

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QWebSocketDataProcessor::pingReceived(const QByteArray &data)
    self.uglySide.call(
        'ritual_ZN23QWebSocketDataProcessor12pingReceivedERK10QByteArray',
        self._valueOf(data),
    )

  @overload(QByteArray)
  def pongReceived(self, data: QByteArray) -> None:
    """
    Calls Qt's 'void QWebSocketDataProcessor::pongReceived(const QByteArray
    &data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocketdataprocessor.html#pongReceived

    Parameters
    ----------

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QWebSocketDataProcessor::pongReceived(const QByteArray &data)
    self.uglySide.call(
        'ritual_ZN23QWebSocketDataProcessor12pongReceivedERK10QByteArray',
        self._valueOf(data),
    )

  @overload(QWebSocketProtocol.CloseCode, str)
  def closeReceived(
      self,
      closeCode: QWebSocketProtocol.CloseCode,
      closeReason: str,
  ) -> None:
    """
    Calls Qt's 'void
    QWebSocketDataProcessor::closeReceived(QWebSocketProtocol::CloseCode
    closeCode, const QString &closeReason)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocketdataprocessor.html#closeReceived

    Parameters
    ----------

    closeCode : QWebSocketProtocol.CloseCode
      Passed on as its number.

    closeReason : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWebSocketDataProcessor::closeReceived(QWebSocketProtocol::
    #      CloseCode closeCode, const QString &closeReason)
    self.uglySide.call(
        'ritual_ZN23QWebSocketDataProcessor13closeReceivedEN18QWebSocketPro'
        'tocol9CloseCodeERK7QString',
        closeCode.value, closeReason,
    )

  @overload(str, bool)
  def textFrameReceived(self, frame: str, lastFrame: bool) -> None:
    """
    Calls Qt's 'void QWebSocketDataProcessor::textFrameReceived(const QString
    &frame, bool lastFrame)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocketdataprocessor.html#textFrameReceived

    Parameters
    ----------

    frame : str
      Passed on as it is: a QString is made of it for the call.

    lastFrame : bool
      Passed on as it is.
    """
    #  void QWebSocketDataProcessor::textFrameReceived(const QString &frame,
    #      bool lastFrame)
    self.uglySide.call(
        'ritual_ZN23QWebSocketDataProcessor17textFrameReceivedERK7QStringb',
        frame, lastFrame,
    )

  @overload(QByteArray, bool)
  def binaryFrameReceived(self, frame: QByteArray, lastFrame: bool) -> None:
    """
    Calls Qt's 'void QWebSocketDataProcessor::binaryFrameReceived(const
    QByteArray &frame, bool lastFrame)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocketdataprocessor.html#binaryFrameReceived

    Parameters
    ----------

    frame : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    lastFrame : bool
      Passed on as it is.
    """
    #  void QWebSocketDataProcessor::binaryFrameReceived(const QByteArray
    #      &frame, bool lastFrame)
    self.uglySide.call(
        'ritual_ZN23QWebSocketDataProcessor19binaryFrameReceivedERK10QByteA'
        'rrayb',
        self._valueOf(frame), lastFrame,
    )

  @overload(str)
  def textMessageReceived(self, message: str) -> None:
    """
    Calls Qt's 'void QWebSocketDataProcessor::textMessageReceived(const
    QString &message)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocketdataprocessor.html#textMessageReceived

    Parameters
    ----------

    message : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWebSocketDataProcessor::textMessageReceived(const QString
    #      &message)
    self.uglySide.call(
        'ritual_ZN23QWebSocketDataProcessor19textMessageReceivedERK7QString',
        message,
    )

  @overload(QByteArray)
  def binaryMessageReceived(self, message: QByteArray) -> None:
    """
    Calls Qt's 'void QWebSocketDataProcessor::binaryMessageReceived(const
    QByteArray &message)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocketdataprocessor.html#binaryMessageReceived

    Parameters
    ----------

    message : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QWebSocketDataProcessor::binaryMessageReceived(const QByteArray
    #      &message)
    self.uglySide.call(
        'ritual_ZN23QWebSocketDataProcessor21binaryMessageReceivedERK10QByt'
        'eArray',
        self._valueOf(message),
    )

  @overload(QWebSocketProtocol.CloseCode, str)
  def errorEncountered(
      self,
      code: QWebSocketProtocol.CloseCode,
      description: str,
  ) -> None:
    """
    Calls Qt's 'void
    QWebSocketDataProcessor::errorEncountered(QWebSocketProtocol::CloseCode
    code, const QString &description)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocketdataprocessor.html#errorEncountered

    Parameters
    ----------

    code : QWebSocketProtocol.CloseCode
      Passed on as its number.

    description : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWebSocketDataProcessor::errorEncountered(QWebSocketProtocol::
    #      CloseCode code, const QString &description)
    self.uglySide.call(
        'ritual_ZN23QWebSocketDataProcessor16errorEncounteredEN18QWebSocket'
        'Protocol9CloseCodeERK7QString',
        code.value, description,
    )

  def clear(self) -> None:
    """
    Calls Qt's 'void QWebSocketDataProcessor::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocketdataprocessor.html#clear
    """
    #  void QWebSocketDataProcessor::clear()
    self.uglySide.call('ritual_ZN23QWebSocketDataProcessor5clearEv')

  @staticmethod
  def idleTimeout(*__, **_) -> Never:
    """
    Qt's 'std::chrono::milliseconds QWebSocketDataProcessor::idleTimeout()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QWebSocketDataProcessor.idleTimeout' has no cute function yet. "
        "Qt's 'std::chrono::milliseconds "
        "QWebSocketDataProcessor::idleTimeout() const': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def process(*__, **_) -> Never:
    """
    Qt's 'bool QWebSocketDataProcessor::process(QIODevice *pIoDevice)': leans
    on 'QWebSocketDataProcessor::pingReceived(QByteArray const&)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QWebSocketDataProcessor.process' has no cute function yet. Qt's "
        "'bool QWebSocketDataProcessor::process(QIODevice *pIoDevice)': "
        "leans on 'QWebSocketDataProcessor::pingReceived(QByteArray "
        "const&)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def processControlFrame(*__, **_) -> Never:
    """
    Qt's 'bool QWebSocketDataProcessor::processControlFrame(const
    QWebSocketFrame &frame)': leans on
    'QWebSocketDataProcessor::pingReceived(QByteArray const&)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QWebSocketDataProcessor.processControlFrame' has no cute function "
        "yet. Qt's 'bool QWebSocketDataProcessor::processControlFrame(const "
        "QWebSocketFrame &frame)': leans on "
        "'QWebSocketDataProcessor::pingReceived(QByteArray const&)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def reportError(*__, **_) -> Never:
    """
    Qt's 'void
    QWebSocketDataProcessor::reportError(QWebSocketProtocol::CloseCode code,
    const QString &description)': leans on
    'QWebSocketDataProcessor::errorEncountered(QWebSocketProtocol::CloseCode,
    QString const&)', which Qt's source does not mark for use from outside Qt
    and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QWebSocketDataProcessor.reportError' has no cute function yet. "
        "Qt's 'void "
        "QWebSocketDataProcessor::reportError(QWebSocketProtocol::CloseCode "
        "code, const QString &description)': leans on "
        "'QWebSocketDataProcessor::errorEncountered(QWebSocketProtocol::Clos"
        "eCode, QString const&)', which Qt's source does not mark for use "
        "from outside Qt and has no code for that could be taken.")

  @staticmethod
  def setIdleTimeout(*__, **_) -> Never:
    """
    Qt's 'void
    QWebSocketDataProcessor::setIdleTimeout(std::chrono::milliseconds
    timeout)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QWebSocketDataProcessor.setIdleTimeout' has no cute function yet. "
        "Qt's 'void "
        "QWebSocketDataProcessor::setIdleTimeout(std::chrono::milliseconds "
        "timeout)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def timeout(*__, **_) -> Never:
    """
    Qt's 'void QWebSocketDataProcessor::timeout()': leans on
    'QWebSocketDataProcessor::errorEncountered(QWebSocketProtocol::CloseCode,
    QString const&)', which Qt's source does not mark for use from outside Qt
    and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QWebSocketDataProcessor.timeout' has no cute function yet. Qt's "
        "'void QWebSocketDataProcessor::timeout()': leans on "
        "'QWebSocketDataProcessor::errorEncountered(QWebSocketProtocol::Clos"
        "eCode, QString const&)', which Qt's source does not mark for use "
        "from outside Qt and has no code for that could be taken.")
