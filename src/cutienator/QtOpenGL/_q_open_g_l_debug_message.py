"""
QOpenGLDebugMessage binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpenGL/qopengldebug.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags, MetaCute
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QOpenGLDebugMessage(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QOpenGLDebugMessage: a plain Python object standing
  in front of one C++ QOpenGLDebugMessage.

  C++ hands a QOpenGLDebugMessage around as a copy, so every C++
  QOpenGLDebugMessage behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QOpenGLDebugMessage that has a ritual and that
  Python can call so far, 9 names in all: 'source', 'type', 'severity', 'id',
  'message', 'createApplicationMessage', 'createThirdPartyMessage', '__eq__',
  '__ne__'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QOpenGLDebugMessage &QOpenGLDebugMessage::operator=(const
    QOpenGLDebugMessage &debugMessage)': assignment: Python binds a name and
    has no operator for it.
  - Qt's 'QOpenGLDebugMessage
    &QOpenGLDebugMessage::operator=(QOpenGLDebugMessage &&other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QOpenGLDebugMessage::~QOpenGLDebugMessage()': the destructor:
    Python removes its C++ QOpenGLDebugMessage by it, and has no other use
    for it.
  - Qt's 'void QOpenGLDebugMessage::swap(QOpenGLDebugMessage &other)': takes
    a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QOpenGLDebugMessage is created at the first use, not by
    'QOpenGLDebugMessage(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QOpenGLDebugMessage back gives a copy the ritual made
    for Python, in a new cute QOpenGLDebugMessage.
  - Each name of Qt's QOpenGLDebugMessage that has no cute function yet,
    'swap', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The enums Qt writes inside QOpenGLDebugMessage, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class Severity(CuteFlags, number='unsigned int'):
    """
    The flags enum 'QOpenGLDebugMessage::Severity' of Qt, with the 7 names Qt
    gives in it. Qt names the type of its combinations
    'QOpenGLDebugMessage::Severities'.
    """

    InvalidSeverity = 0x0
    HighSeverity = 0x1
    MediumSeverity = 0x2
    LowSeverity = 0x4
    NotificationSeverity = 0x8
    LastSeverity = 0x8
    AnySeverity = 0xffffffff

  Severities = Severity

  class Source(CuteFlags, number='unsigned int'):
    """
    The flags enum 'QOpenGLDebugMessage::Source' of Qt, with the 9 names Qt
    gives in it. Qt names the type of its combinations
    'QOpenGLDebugMessage::Sources'.
    """

    InvalidSource = 0x0
    APISource = 0x1
    WindowSystemSource = 0x2
    ShaderCompilerSource = 0x4
    ThirdPartySource = 0x8
    ApplicationSource = 0x10
    OtherSource = 0x20
    LastSource = 0x20
    AnySource = 0xffffffff

  Sources = Source

  class Type(CuteFlags, number='unsigned int'):
    """
    The flags enum 'QOpenGLDebugMessage::Type' of Qt, with the 12 names Qt
    gives in it. Qt names the type of its combinations
    'QOpenGLDebugMessage::Types'.
    """

    InvalidType = 0x0
    ErrorType = 0x1
    DeprecatedBehaviorType = 0x2
    UndefinedBehaviorType = 0x4
    PortabilityType = 0x8
    PerformanceType = 0x10
    OtherType = 0x20
    MarkerType = 0x40
    GroupPushType = 0x80
    GroupPopType = 0x100
    LastType = 0x100
    AnyType = 0xffffffff

  Types = Type

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(str, int)
  @overload(str, int, Severity)
  @overload(str, int, Severity, Type)
  def createApplicationMessage(
      text: str,
      id: int = 0,
      severity: Severity = Severity.NotificationSeverity,
      type: Type = Type.OtherType,
  ) -> QOpenGLDebugMessage:
    """
    Calls Qt's 'QOpenGLDebugMessage
    QOpenGLDebugMessage::createApplicationMessage(const QString &text, GLuint
    id, Severity severity, Type type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengldebugmessage.html#createApplicationMessage

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.

    id : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    severity : Severity
      Passed on as its number. May be left out, as in Qt: it is then
      Severity.NotificationSeverity.

    type : Type
      Passed on as its number. May be left out, as in Qt: it is then
      Type.OtherType.

    Returns
    -------

    QOpenGLDebugMessage
      A new cute QOpenGLDebugMessage around the copy Qt gave back. Python
      owns it.
    """
    #  QOpenGLDebugMessage
    #      QOpenGLDebugMessage::createApplicationMessage(const QString &text,
    #      GLuint id, Severity severity, Type type)
    address = Rituals.call(
        'ritual_ZN19QOpenGLDebugMessage24createApplicationMessageERK7QStrin'
        'gjNS_8SeverityENS_4TypeE',
        text, id, severity.value, type.value,
    )
    return QOpenGLDebugMessage._cuteOwning(address)

  @staticmethod
  @overload(str)
  @overload(str, int)
  @overload(str, int, Severity)
  @overload(str, int, Severity, Type)
  def createThirdPartyMessage(
      text: str,
      id: int = 0,
      severity: Severity = Severity.NotificationSeverity,
      type: Type = Type.OtherType,
  ) -> QOpenGLDebugMessage:
    """
    Calls Qt's 'QOpenGLDebugMessage
    QOpenGLDebugMessage::createThirdPartyMessage(const QString &text, GLuint
    id, Severity severity, Type type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengldebugmessage.html#createThirdPartyMessage

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.

    id : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    severity : Severity
      Passed on as its number. May be left out, as in Qt: it is then
      Severity.NotificationSeverity.

    type : Type
      Passed on as its number. May be left out, as in Qt: it is then
      Type.OtherType.

    Returns
    -------

    QOpenGLDebugMessage
      A new cute QOpenGLDebugMessage around the copy Qt gave back. Python
      owns it.
    """
    #  QOpenGLDebugMessage QOpenGLDebugMessage::createThirdPartyMessage(const
    #      QString &text, GLuint id, Severity severity, Type type)
    address = Rituals.call(
        'ritual_ZN19QOpenGLDebugMessage23createThirdPartyMessageERK7QString'
        'jNS_8SeverityENS_4TypeE',
        text, id, severity.value, type.value,
    )
    return QOpenGLDebugMessage._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpenGLDebugMessage'

  #  Qt's '~QOpenGLDebugMessage()'. Naming it makes this a value class:
  #  Python owns every C++ QOpenGLDebugMessage behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = 'ritual_ZN19QOpenGLDebugMessageD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def source(self) -> Source:
    """
    Calls Qt's 'Source QOpenGLDebugMessage::source() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopengldebugmessage.html#source

    Returns
    -------

    Source
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Source(number)' gives.
    """
    #  Source QOpenGLDebugMessage::source() const
    return QOpenGLDebugMessage.Source(self.uglySide.call(
        'ritual_ZNK19QOpenGLDebugMessage6sourceEv',
    ))

  def type(self) -> Type:
    """
    Calls Qt's 'Type QOpenGLDebugMessage::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopengldebugmessage.html#type

    Returns
    -------

    Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Type(number)' gives.
    """
    #  Type QOpenGLDebugMessage::type() const
    return QOpenGLDebugMessage.Type(self.uglySide.call(
        'ritual_ZNK19QOpenGLDebugMessage4typeEv',
    ))

  def severity(self) -> Severity:
    """
    Calls Qt's 'Severity QOpenGLDebugMessage::severity() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopengldebugmessage.html#severity

    Returns
    -------

    Severity
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Severity(number)' gives.
    """
    #  Severity QOpenGLDebugMessage::severity() const
    return QOpenGLDebugMessage.Severity(self.uglySide.call(
        'ritual_ZNK19QOpenGLDebugMessage8severityEv',
    ))

  def id(self) -> int:
    """
    Calls Qt's 'GLuint QOpenGLDebugMessage::id() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopengldebugmessage.html#id
    """
    #  GLuint QOpenGLDebugMessage::id() const
    return self.uglySide.call('ritual_ZNK19QOpenGLDebugMessage2idEv')

  def message(self) -> str:
    """
    Calls Qt's 'QString QOpenGLDebugMessage::message() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopengldebugmessage.html#message

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QOpenGLDebugMessage::message() const
    return self.uglySide.call('ritual_ZNK19QOpenGLDebugMessage7messageEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, debugMessage: QOpenGLDebugMessage) -> bool:
    """
    Calls Qt's 'bool QOpenGLDebugMessage::operator==(const
    QOpenGLDebugMessage &debugMessage) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengldebugmessage.html#operator==

    Parameters
    ----------

    debugMessage : QOpenGLDebugMessage
      Passed on as a value: Qt reads the C++ QOpenGLDebugMessage, which stays
      Python's own.
    """
    #  bool QOpenGLDebugMessage::operator==(const QOpenGLDebugMessage
    #      &debugMessage) const
    return self.uglySide.call(
        'ritual_ZNK19QOpenGLDebugMessageeqERKS_',
        self._valueOf(debugMessage),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(self, debugMessage: QOpenGLDebugMessage) -> bool:
    """
    Calls Qt's 'bool QOpenGLDebugMessage::operator!=(const
    QOpenGLDebugMessage &debugMessage) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengldebugmessage.html#operator!=

    Parameters
    ----------

    debugMessage : QOpenGLDebugMessage
      Passed on as a value: Qt reads the C++ QOpenGLDebugMessage, which stays
      Python's own.
    """
    #  bool QOpenGLDebugMessage::operator!=(const QOpenGLDebugMessage
    #      &debugMessage) const
    return self.uglySide.call(
        'ritual_ZNK19QOpenGLDebugMessageneERKS_',
        self._valueOf(debugMessage),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QOpenGLDebugMessage::QOpenGLDebugMessage()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengldebugmessage.html#QOpenGLDebugMessage
    """
    #  QOpenGLDebugMessage::QOpenGLDebugMessage()
    self._noteCreation(QOpenGLDebugMessage, lambda: Rituals.call(
        'ritual_ZN19QOpenGLDebugMessageC1Ev',
    ))

  @overload(THIS)
  def __init__(self, debugMessage: QOpenGLDebugMessage) -> None:
    """
    Notes what was given, for Qt's
    'QOpenGLDebugMessage::QOpenGLDebugMessage(const QOpenGLDebugMessage
    &debugMessage)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengldebugmessage.html#QOpenGLDebugMessage

    Parameters
    ----------

    debugMessage : QOpenGLDebugMessage
      Passed on as a value: Qt reads the C++ QOpenGLDebugMessage, which stays
      Python's own.
    """
    #  QOpenGLDebugMessage::QOpenGLDebugMessage(const QOpenGLDebugMessage
    #      &debugMessage)
    self._noteCreation(QOpenGLDebugMessage, lambda: Rituals.call(
        'ritual_ZN19QOpenGLDebugMessageC1ERKS_', self._valueOf(debugMessage),
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
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLDebugMessage::swap(QOpenGLDebugMessage &other)': takes
    a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QOpenGLDebugMessage.swap' has no cute function yet. Qt's 'void "
        "QOpenGLDebugMessage::swap(QOpenGLDebugMessage &other)': takes a "
        "type Python has no way to hand over yet.")


#  Qt's 'QList<QOpenGLDebugMessage>': the list of QOpenGLDebugMessage, which
#  'QList[QOpenGLDebugMessage]' gives. It is made here, so that there is one
#  as soon as there can be a QOpenGLDebugMessage.
QList.createKind(
    QOpenGLDebugMessage, 'value',
    make='ritual_list_make_QOpenGLDebugMessage',
    add='ritual_list_add_QOpenGLDebugMessage',
    size='ritual_list_size_QOpenGLDebugMessage',
    at='ritual_list_at_QOpenGLDebugMessage',
    drop='ritual_list_drop_QOpenGLDebugMessage',
)
