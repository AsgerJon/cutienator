"""
QOpenGLDebugLogger binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpenGL/qopengldebug.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum
from ..occult import Rituals
from ..QtCore import QList, QObject
from . import QOpenGLDebugMessage

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QOpenGLDebugLogger(QObject):
  """
  The cute side of Qt's QOpenGLDebugLogger: a plain Python object standing in
  front of one C++ QOpenGLDebugLogger.

  It is built on the cute 'QObject', as Qt's QOpenGLDebugLogger is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QOpenGLDebugLogger that has a ritual and that Python
  can call so far, 15 names in all: 'metaObject', 'tr', 'initialize',
  'isLogging', 'loggingMode', 'maximumMessageLength', 'pushGroup',
  'popGroup', 'enableMessages', 'disableMessages', 'loggedMessages',
  'logMessage', 'startLogging', 'stopLogging', 'messageLogged'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QOpenGLDebugLogger::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QOpenGLDebugLogger::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QOpenGLDebugLogger::~QOpenGLDebugLogger()': the destructor: Python
    never removes a C++ QOpenGLDebugLogger.
  - Qt's 'void QOpenGLDebugLogger::enableMessages(const QList<GLuint> &ids,
    QOpenGLDebugMessage::Sources sources, QOpenGLDebugMessage::Types types)':
    takes a type Python has no way to hand over yet.
  - Qt's 'void QOpenGLDebugLogger::disableMessages(const QList<GLuint> &ids,
    QOpenGLDebugMessage::Sources sources, QOpenGLDebugMessage::Types types)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QOpenGLDebugLoggerPrivate *QOpenGLDebugLogger::d_func()': gives
    'QOpenGLDebugLoggerPrivate', which has no cute class yet.
  - Qt's 'const QOpenGLDebugLoggerPrivate *QOpenGLDebugLogger::d_func()
    const': gives 'QOpenGLDebugLoggerPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 27 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QOpenGLDebugLogger is created at the first use, not by
    'QOpenGLDebugLogger(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QOpenGLDebugLogger.
  - Qt tells when it has removed the C++ QOpenGLDebugLogger. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QOpenGLDebugLogger, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class LoggingMode(CuteNum):
    """
    The enum 'QOpenGLDebugLogger::LoggingMode' of Qt, with the 2 names Qt
    gives in it.
    """

    AsynchronousLogging = Kee[int](0)
    SynchronousLogging = Kee[int](1)

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
    Calls Qt's 'QString QOpenGLDebugLogger::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qopengldebuglogger.html#tr

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
    #  QString QOpenGLDebugLogger::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN18QOpenGLDebugLogger2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpenGLDebugLogger'

  #  A C++ QOpenGLDebugLogger Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QOpenGLDebugLogger'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QOpenGLDebugLogger::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopengldebuglogger.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QOpenGLDebugLogger::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QOpenGLDebugLogger10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isLogging(self) -> bool:
    """
    Calls Qt's 'bool QOpenGLDebugLogger::isLogging() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopengldebuglogger.html#isLogging
    """
    #  bool QOpenGLDebugLogger::isLogging() const
    return self.uglySide.call('ritual_ZNK18QOpenGLDebugLogger9isLoggingEv')

  def loggingMode(self) -> LoggingMode:
    """
    Calls Qt's 'LoggingMode QOpenGLDebugLogger::loggingMode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengldebuglogger.html#loggingMode

    Returns
    -------

    LoggingMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'LoggingMode(number)'
      gives.
    """
    #  LoggingMode QOpenGLDebugLogger::loggingMode() const
    return QOpenGLDebugLogger.LoggingMode(self.uglySide.call(
        'ritual_ZNK18QOpenGLDebugLogger11loggingModeEv',
    ))

  def maximumMessageLength(self) -> int:
    """
    Calls Qt's 'qint64 QOpenGLDebugLogger::maximumMessageLength() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengldebuglogger.html#maximumMessageLength
    """
    #  qint64 QOpenGLDebugLogger::maximumMessageLength() const
    return self.uglySide.call(
        'ritual_ZNK18QOpenGLDebugLogger20maximumMessageLengthEv',
    )

  def loggedMessages(self) -> QList[QOpenGLDebugMessage]:
    """
    Calls Qt's 'QList<QOpenGLDebugMessage>
    QOpenGLDebugLogger::loggedMessages() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengldebuglogger.html#loggedMessages

    Returns
    -------

    QList[QOpenGLDebugMessage]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QOpenGLDebugMessage> QOpenGLDebugLogger::loggedMessages() const
    address = self.uglySide.call(
        'ritual_ZNK18QOpenGLDebugLogger14loggedMessagesEv',
    )
    return QList[QOpenGLDebugMessage]._cuteOwning(address)

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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QOpenGLDebugLogger::QOpenGLDebugLogger(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengldebuglogger.html#QOpenGLDebugLogger

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QOpenGLDebugLogger::QOpenGLDebugLogger(QObject *parent)
    self._noteCreation(QOpenGLDebugLogger, lambda: Rituals.call(
        'ritual_ZN18QOpenGLDebugLoggerC1EP7QObject',
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

  def initialize(self) -> bool:
    """
    Calls Qt's 'bool QOpenGLDebugLogger::initialize()'.

    Qt's own words: https://doc.qt.io/qt-6/qopengldebuglogger.html#initialize
    """
    #  bool QOpenGLDebugLogger::initialize()
    return self.uglySide.call('ritual_ZN18QOpenGLDebugLogger10initializeEv')

  @overload(str)
  @overload(str, int)
  @overload(str, int, QOpenGLDebugMessage.Source)
  def pushGroup(
      self,
      name: str,
      id: int = 0,
      source: QOpenGLDebugMessage.Source = (
          QOpenGLDebugMessage.Source.ApplicationSource),
  ) -> None:
    """
    Calls Qt's 'void QOpenGLDebugLogger::pushGroup(const QString &name,
    GLuint id, QOpenGLDebugMessage::Source source)'.

    Qt's own words: https://doc.qt.io/qt-6/qopengldebuglogger.html#pushGroup

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    id : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    source : QOpenGLDebugMessage.Source
      Passed on as its number. May be left out, as in Qt: it is then
      QOpenGLDebugMessage.Source.ApplicationSource.
    """
    #  void QOpenGLDebugLogger::pushGroup(const QString &name, GLuint id,
    #      QOpenGLDebugMessage::Source source)
    self.uglySide.call(
        'ritual_ZN18QOpenGLDebugLogger9pushGroupERK7QStringjN19QOpenGLDebug'
        'Message6SourceE',
        name, id, source.value,
    )

  def popGroup(self) -> None:
    """
    Calls Qt's 'void QOpenGLDebugLogger::popGroup()'.

    Qt's own words: https://doc.qt.io/qt-6/qopengldebuglogger.html#popGroup
    """
    #  void QOpenGLDebugLogger::popGroup()
    self.uglySide.call('ritual_ZN18QOpenGLDebugLogger8popGroupEv')

  @overload()
  @overload(QOpenGLDebugMessage.Sources)
  @overload(QOpenGLDebugMessage.Sources, QOpenGLDebugMessage.Types)
  @overload(
      QOpenGLDebugMessage.Sources, QOpenGLDebugMessage.Types,
      QOpenGLDebugMessage.Severities,
  )
  def enableMessages(
      self,
      sources: QOpenGLDebugMessage.Sources = (
          QOpenGLDebugMessage.Sources.AnySource),
      types: QOpenGLDebugMessage.Types = QOpenGLDebugMessage.Types.AnyType,
      severities: QOpenGLDebugMessage.Severities = (
          QOpenGLDebugMessage.Severities.AnySeverity),
  ) -> None:
    """
    Calls Qt's 'void
    QOpenGLDebugLogger::enableMessages(QOpenGLDebugMessage::Sources sources,
    QOpenGLDebugMessage::Types types, QOpenGLDebugMessage::Severities
    severities)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengldebuglogger.html#enableMessages

    Parameters
    ----------

    sources : QOpenGLDebugMessage.Sources
      Passed on as its number. May be left out, as in Qt: it is then
      QOpenGLDebugMessage.Sources.AnySource.

    types : QOpenGLDebugMessage.Types
      Passed on as its number. May be left out, as in Qt: it is then
      QOpenGLDebugMessage.Types.AnyType.

    severities : QOpenGLDebugMessage.Severities
      Passed on as its number. May be left out, as in Qt: it is then
      QOpenGLDebugMessage.Severities.AnySeverity.
    """
    #  void QOpenGLDebugLogger::enableMessages(QOpenGLDebugMessage::Sources
    #      sources, QOpenGLDebugMessage::Types types,
    #      QOpenGLDebugMessage::Severities severities)
    self.uglySide.call(
        'ritual_ZN18QOpenGLDebugLogger14enableMessagesE6QFlagsIN19QOpenGLDe'
        'bugMessage6SourceEES0_INS1_4TypeEES0_INS1_8SeverityEE',
        sources.value, types.value, severities.value,
    )

  @overload()
  @overload(QOpenGLDebugMessage.Sources)
  @overload(QOpenGLDebugMessage.Sources, QOpenGLDebugMessage.Types)
  @overload(
      QOpenGLDebugMessage.Sources, QOpenGLDebugMessage.Types,
      QOpenGLDebugMessage.Severities,
  )
  def disableMessages(
      self,
      sources: QOpenGLDebugMessage.Sources = (
          QOpenGLDebugMessage.Sources.AnySource),
      types: QOpenGLDebugMessage.Types = QOpenGLDebugMessage.Types.AnyType,
      severities: QOpenGLDebugMessage.Severities = (
          QOpenGLDebugMessage.Severities.AnySeverity),
  ) -> None:
    """
    Calls Qt's 'void
    QOpenGLDebugLogger::disableMessages(QOpenGLDebugMessage::Sources sources,
    QOpenGLDebugMessage::Types types, QOpenGLDebugMessage::Severities
    severities)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengldebuglogger.html#disableMessages

    Parameters
    ----------

    sources : QOpenGLDebugMessage.Sources
      Passed on as its number. May be left out, as in Qt: it is then
      QOpenGLDebugMessage.Sources.AnySource.

    types : QOpenGLDebugMessage.Types
      Passed on as its number. May be left out, as in Qt: it is then
      QOpenGLDebugMessage.Types.AnyType.

    severities : QOpenGLDebugMessage.Severities
      Passed on as its number. May be left out, as in Qt: it is then
      QOpenGLDebugMessage.Severities.AnySeverity.
    """
    #  void QOpenGLDebugLogger::disableMessages(QOpenGLDebugMessage::Sources
    #      sources, QOpenGLDebugMessage::Types types,
    #      QOpenGLDebugMessage::Severities severities)
    self.uglySide.call(
        'ritual_ZN18QOpenGLDebugLogger15disableMessagesE6QFlagsIN19QOpenGLD'
        'ebugMessage6SourceEES0_INS1_4TypeEES0_INS1_8SeverityEE',
        sources.value, types.value, severities.value,
    )

  @overload(QOpenGLDebugMessage)
  def logMessage(self, debugMessage: QOpenGLDebugMessage) -> None:
    """
    Calls Qt's 'void QOpenGLDebugLogger::logMessage(const QOpenGLDebugMessage
    &debugMessage)'.

    Qt's own words: https://doc.qt.io/qt-6/qopengldebuglogger.html#logMessage

    Parameters
    ----------

    debugMessage : QOpenGLDebugMessage
      Passed on as a value: Qt reads the C++ QOpenGLDebugMessage, which stays
      Python's own.
    """
    #  void QOpenGLDebugLogger::logMessage(const QOpenGLDebugMessage
    #      &debugMessage)
    self.uglySide.call(
        'ritual_ZN18QOpenGLDebugLogger10logMessageERK19QOpenGLDebugMessage',
        self._valueOf(debugMessage),
    )

  @overload()
  @overload(LoggingMode)
  def startLogging(
      self,
      loggingMode: LoggingMode = LoggingMode.AsynchronousLogging,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLDebugLogger::startLogging(LoggingMode
    loggingMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengldebuglogger.html#startLogging

    Parameters
    ----------

    loggingMode : LoggingMode
      Passed on as its number. May be left out, as in Qt: it is then
      LoggingMode.AsynchronousLogging.
    """
    #  void QOpenGLDebugLogger::startLogging(LoggingMode loggingMode)
    self.uglySide.call(
        'ritual_ZN18QOpenGLDebugLogger12startLoggingENS_11LoggingModeE',
        loggingMode.value,
    )

  def stopLogging(self) -> None:
    """
    Calls Qt's 'void QOpenGLDebugLogger::stopLogging()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengldebuglogger.html#stopLogging
    """
    #  void QOpenGLDebugLogger::stopLogging()
    self.uglySide.call('ritual_ZN18QOpenGLDebugLogger11stopLoggingEv')

  @overload(QOpenGLDebugMessage)
  def messageLogged(self, debugMessage: QOpenGLDebugMessage) -> None:
    """
    Calls Qt's 'void QOpenGLDebugLogger::messageLogged(const
    QOpenGLDebugMessage &debugMessage)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengldebuglogger.html#messageLogged

    Parameters
    ----------

    debugMessage : QOpenGLDebugMessage
      Passed on as a value: Qt reads the C++ QOpenGLDebugMessage, which stays
      Python's own.
    """
    #  void QOpenGLDebugLogger::messageLogged(const QOpenGLDebugMessage
    #      &debugMessage)
    self.uglySide.call(
        'ritual_ZN18QOpenGLDebugLogger13messageLoggedERK19QOpenGLDebugMessa'
        'ge',
        self._valueOf(debugMessage),
    )
