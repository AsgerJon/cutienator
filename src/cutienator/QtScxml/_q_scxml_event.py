"""
QScxmlEvent binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtScxml/qscxmlevent.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVariant = WAIT['QVariant']


class QScxmlEvent(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QScxmlEvent: a plain Python object standing in front
  of one C++ QScxmlEvent.

  C++ hands a QScxmlEvent around as a copy, so every C++ QScxmlEvent behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QScxmlEvent that has a ritual and that Python can
  call so far, 20 names in all: 'name', 'setName', 'eventType', 'scxmlType',
  'sendId', 'setSendId', 'origin', 'setOrigin', 'originType',
  'setOriginType', 'invokeId', 'setInvokeId', 'delay', 'setDelay', 'clear',
  'data', 'setData', 'isErrorEvent', 'errorMessage', 'setErrorMessage'. It
  can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QScxmlEvent::~QScxmlEvent()': the destructor: Python removes its
    C++ QScxmlEvent by it, and has no other use for it.
  - Qt's 'QScxmlEvent &QScxmlEvent::operator=(const QScxmlEvent &other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'void QScxmlEvent::setEventType(const EventType &type)': takes a
    type Python has no way to hand over yet.

  What has no ritual
  ------------------

  3 of the 28 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QScxmlEvent is created at the first use, not by
    'QScxmlEvent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QScxmlEvent back gives a copy the ritual made for
    Python, in a new cute QScxmlEvent.
  - Each name of Qt's QScxmlEvent that has no cute function yet,
    'setEventType', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  #  The enums Qt writes inside QScxmlEvent, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class EventType(CuteNum):
    """
    The enum 'QScxmlEvent::EventType' of Qt, with the 3 names Qt gives in it.
    """

    PlatformEvent = Kee[int](0)
    InternalEvent = Kee[int](1)
    ExternalEvent = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QScxmlEvent'

  #  Qt's '~QScxmlEvent()'. Naming it makes this a value class: Python owns
  #  every C++ QScxmlEvent behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN11QScxmlEventD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def name(self) -> str:
    """
    Calls Qt's 'QString QScxmlEvent::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscxmlevent.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QScxmlEvent::name() const
    return self.uglySide.call('ritual_ZNK11QScxmlEvent4nameEv')

  def eventType(self) -> EventType:
    """
    Calls Qt's 'EventType QScxmlEvent::eventType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscxmlevent.html#eventType

    Returns
    -------

    EventType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'EventType(number)' gives.
    """
    #  EventType QScxmlEvent::eventType() const
    return QScxmlEvent.EventType(self.uglySide.call(
        'ritual_ZNK11QScxmlEvent9eventTypeEv',
    ))

  def scxmlType(self) -> str:
    """
    Calls Qt's 'QString QScxmlEvent::scxmlType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscxmlevent.html#scxmlType

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QScxmlEvent::scxmlType() const
    return self.uglySide.call('ritual_ZNK11QScxmlEvent9scxmlTypeEv')

  def sendId(self) -> str:
    """
    Calls Qt's 'QString QScxmlEvent::sendId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscxmlevent.html#sendId

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QScxmlEvent::sendId() const
    return self.uglySide.call('ritual_ZNK11QScxmlEvent6sendIdEv')

  def origin(self) -> str:
    """
    Calls Qt's 'QString QScxmlEvent::origin() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscxmlevent.html#origin

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QScxmlEvent::origin() const
    return self.uglySide.call('ritual_ZNK11QScxmlEvent6originEv')

  def originType(self) -> str:
    """
    Calls Qt's 'QString QScxmlEvent::originType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscxmlevent.html#originType

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QScxmlEvent::originType() const
    return self.uglySide.call('ritual_ZNK11QScxmlEvent10originTypeEv')

  def invokeId(self) -> str:
    """
    Calls Qt's 'QString QScxmlEvent::invokeId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscxmlevent.html#invokeId

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QScxmlEvent::invokeId() const
    return self.uglySide.call('ritual_ZNK11QScxmlEvent8invokeIdEv')

  def delay(self) -> int:
    """
    Calls Qt's 'int QScxmlEvent::delay() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscxmlevent.html#delay
    """
    #  int QScxmlEvent::delay() const
    return self.uglySide.call('ritual_ZNK11QScxmlEvent5delayEv')

  def data(self) -> QVariant:
    """
    Calls Qt's 'QVariant QScxmlEvent::data() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscxmlevent.html#data

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QScxmlEvent::data() const
    address = self.uglySide.call('ritual_ZNK11QScxmlEvent4dataEv')
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def isErrorEvent(self) -> bool:
    """
    Calls Qt's 'bool QScxmlEvent::isErrorEvent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscxmlevent.html#isErrorEvent
    """
    #  bool QScxmlEvent::isErrorEvent() const
    return self.uglySide.call('ritual_ZNK11QScxmlEvent12isErrorEventEv')

  def errorMessage(self) -> str:
    """
    Calls Qt's 'QString QScxmlEvent::errorMessage() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscxmlevent.html#errorMessage

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QScxmlEvent::errorMessage() const
    return self.uglySide.call('ritual_ZNK11QScxmlEvent12errorMessageEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setName(self, name: str) -> None:
    """
    Calls Qt's 'void QScxmlEvent::setName(const QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qscxmlevent.html#setName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QScxmlEvent::setName(const QString &name)
    self.uglySide.call('ritual_ZN11QScxmlEvent7setNameERK7QString', name)

  @overload(str)
  def setSendId(self, sendId: str) -> None:
    """
    Calls Qt's 'void QScxmlEvent::setSendId(const QString &sendId)'.

    Qt's own words: https://doc.qt.io/qt-6/qscxmlevent.html#setSendId

    Parameters
    ----------

    sendId : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QScxmlEvent::setSendId(const QString &sendId)
    self.uglySide.call('ritual_ZN11QScxmlEvent9setSendIdERK7QString', sendId)

  @overload(str)
  def setOrigin(self, origin: str) -> None:
    """
    Calls Qt's 'void QScxmlEvent::setOrigin(const QString &origin)'.

    Qt's own words: https://doc.qt.io/qt-6/qscxmlevent.html#setOrigin

    Parameters
    ----------

    origin : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QScxmlEvent::setOrigin(const QString &origin)
    self.uglySide.call('ritual_ZN11QScxmlEvent9setOriginERK7QString', origin)

  @overload(str)
  def setOriginType(self, originType: str) -> None:
    """
    Calls Qt's 'void QScxmlEvent::setOriginType(const QString &originType)'.

    Qt's own words: https://doc.qt.io/qt-6/qscxmlevent.html#setOriginType

    Parameters
    ----------

    originType : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QScxmlEvent::setOriginType(const QString &originType)
    self.uglySide.call(
        'ritual_ZN11QScxmlEvent13setOriginTypeERK7QString', originType,
    )

  @overload(str)
  def setInvokeId(self, invokeId: str) -> None:
    """
    Calls Qt's 'void QScxmlEvent::setInvokeId(const QString &invokeId)'.

    Qt's own words: https://doc.qt.io/qt-6/qscxmlevent.html#setInvokeId

    Parameters
    ----------

    invokeId : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QScxmlEvent::setInvokeId(const QString &invokeId)
    self.uglySide.call(
        'ritual_ZN11QScxmlEvent11setInvokeIdERK7QString', invokeId,
    )

  @overload(int)
  def setDelay(self, delayInMiliSecs: int) -> None:
    """
    Calls Qt's 'void QScxmlEvent::setDelay(int delayInMiliSecs)'.

    Qt's own words: https://doc.qt.io/qt-6/qscxmlevent.html#setDelay

    Parameters
    ----------

    delayInMiliSecs : int
      Passed on as it is.
    """
    #  void QScxmlEvent::setDelay(int delayInMiliSecs)
    self.uglySide.call('ritual_ZN11QScxmlEvent8setDelayEi', delayInMiliSecs)

  @overload(QVariant)
  def setData(self, data: QVariant) -> None:
    """
    Calls Qt's 'void QScxmlEvent::setData(const QVariant &data)'.

    Qt's own words: https://doc.qt.io/qt-6/qscxmlevent.html#setData

    Parameters
    ----------

    data : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QScxmlEvent::setData(const QVariant &data)
    self.uglySide.call(
        'ritual_ZN11QScxmlEvent7setDataERK8QVariant', self._valueOf(data),
    )

  @overload(str)
  def setErrorMessage(self, message: str) -> None:
    """
    Calls Qt's 'void QScxmlEvent::setErrorMessage(const QString &message)'.

    Qt's own words: https://doc.qt.io/qt-6/qscxmlevent.html#setErrorMessage

    Parameters
    ----------

    message : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QScxmlEvent::setErrorMessage(const QString &message)
    self.uglySide.call(
        'ritual_ZN11QScxmlEvent15setErrorMessageERK7QString', message,
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
    Notes what was given, for Qt's 'QScxmlEvent::QScxmlEvent()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qscxmlevent.html#QScxmlEvent
    """
    #  QScxmlEvent::QScxmlEvent()
    self._noteCreation(QScxmlEvent, lambda: Rituals.call(
        'ritual_ZN11QScxmlEventC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QScxmlEvent) -> None:
    """
    Notes what was given, for Qt's 'QScxmlEvent::QScxmlEvent(const
    QScxmlEvent &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qscxmlevent.html#QScxmlEvent

    Parameters
    ----------

    other : QScxmlEvent
      Passed on as a value: Qt reads the C++ QScxmlEvent, which stays
      Python's own.
    """
    #  QScxmlEvent::QScxmlEvent(const QScxmlEvent &other)
    self._noteCreation(QScxmlEvent, lambda: Rituals.call(
        'ritual_ZN11QScxmlEventC1ERKS_', self._valueOf(other),
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

  def clear(self) -> None:
    """
    Calls Qt's 'void QScxmlEvent::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qscxmlevent.html#clear
    """
    #  void QScxmlEvent::clear()
    self.uglySide.call('ritual_ZN11QScxmlEvent5clearEv')

  @staticmethod
  def setEventType(*__, **_) -> Never:
    """
    Qt's 'void QScxmlEvent::setEventType(const EventType &type)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QScxmlEvent.setEventType' has no cute function yet. Qt's 'void "
        "QScxmlEvent::setEventType(const EventType &type)': takes a type "
        "Python has no way to hand over yet.")
