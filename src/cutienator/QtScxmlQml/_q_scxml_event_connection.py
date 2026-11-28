"""
QScxmlEventConnection binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtScxmlQml/6.12.0/QtScxmlQml/private/eventconnection_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QScxmlEventConnection to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject, QStringList
from ..QtQml import QQmlParserStatus

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtScxml import QScxmlEvent, QScxmlStateMachine
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QScxmlEvent = WAIT['QScxmlEvent']
  QScxmlStateMachine = WAIT['QScxmlStateMachine']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QScxmlEventConnection(QObject, QQmlParserStatus):
  """
  The cute side of Qt's QScxmlEventConnection: a plain Python object standing
  in front of one C++ QScxmlEventConnection.

  It is built on the cute 'QObject', as Qt's QScxmlEventConnection is built
  on Qt's QObject, and has everything that class has. It is built on the cute
  'QQmlParserStatus' as well, as Qt's QScxmlEventConnection is built on Qt's
  QQmlParserStatus too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QScxmlEventConnection that has a ritual and that
  Python can call so far, 14 names in all: 'metaObject', 'tr', 'events',
  'setEvents', 'stateMachine', 'setStateMachine', 'eventsChanged',
  'stateMachineChanged', 'occurred', '_qt_property_m_stateMachine_offset',
  '_qt_property_m_events_offset', 'doConnect', 'classBegin',
  'componentComplete'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QScxmlEventConnection::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QScxmlEventConnection::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QScxmlEventConnection::~QScxmlEventConnection()': the destructor:
    Python never removes a C++ QScxmlEventConnection.
  - Qt's 'QBindable<QStringList> QScxmlEventConnection::bindableEvents()':
    gives a type Python has no way to take yet.
  - Qt's 'QBindable<QScxmlStateMachine *>
    QScxmlEventConnection::bindableStateMachine()': gives a type Python has
    no way to take yet.

  What has no ritual
  ------------------

  2 of the 22 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QScxmlEventConnection is created at the first use, not by
    'QScxmlEventConnection(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QScxmlEventConnection.
  - Qt tells when it has removed the C++ QScxmlEventConnection. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QScxmlEventConnection that has no cute function yet,
    'bindableEvents', 'bindableStateMachine', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

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
    Calls Qt's 'QString QScxmlEventConnection::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qscxmleventconnection.html#tr

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
    #  QString QScxmlEventConnection::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN21QScxmlEventConnection2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def _qt_property_m_stateMachine_offset() -> int:
    """
    Calls Qt's 'size_t
    QScxmlEventConnection::_qt_property_m_stateMachine_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmleventconnection.html
    """
    #  size_t QScxmlEventConnection::_qt_property_m_stateMachine_offset()
    return Rituals.call(
        'ritual_ZN21QScxmlEventConnection34_qt_property_m_stateMachine_offs'
        'etEv',
    )

  @staticmethod
  def _qt_property_m_events_offset() -> int:
    """
    Calls Qt's 'size_t
    QScxmlEventConnection::_qt_property_m_events_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmleventconnection.html
    """
    #  size_t QScxmlEventConnection::_qt_property_m_events_offset()
    return Rituals.call(
        'ritual_ZN21QScxmlEventConnection28_qt_property_m_events_offsetEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QScxmlEventConnection'

  #  Qt's QScxmlEventConnection is built on more than one class. The part of
  #  a C++ QScxmlEventConnection that belongs to a class after the first
  #  begins somewhere inside the object, and the ritual named for that class
  #  gives where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QQmlParserStatus':
          'ritual_cast_QScxmlEventConnection_QQmlParserStatus',
  }

  #  A C++ QScxmlEventConnection Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QScxmlEventConnection'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QScxmlEventConnection::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmleventconnection.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QScxmlEventConnection::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK21QScxmlEventConnection10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def events(self) -> QStringList:
    """
    Calls Qt's 'QStringList QScxmlEventConnection::events() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscxmleventconnection.html#events

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QScxmlEventConnection::events() const
    address = self.uglySide.call(
        'ritual_ZNK21QScxmlEventConnection6eventsEv',
    )
    return QStringList._cuteOwning(address)

  def stateMachine(self) -> Optional[QScxmlStateMachine]:
    """
    Calls Qt's 'QScxmlStateMachine *QScxmlEventConnection::stateMachine()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmleventconnection.html#stateMachine

    Returns
    -------

    Optional[QScxmlStateMachine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QScxmlStateMachine *QScxmlEventConnection::stateMachine() const
    address = self.uglySide.call(
        'ritual_ZNK21QScxmlEventConnection12stateMachineEv',
    )
    from ..QtScxml import QScxmlStateMachine
    return QScxmlStateMachine._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QStringList)
  def setEvents(self, events: QStringList) -> None:
    """
    Calls Qt's 'void QScxmlEventConnection::setEvents(const QStringList
    &events)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmleventconnection.html#setEvents

    Parameters
    ----------

    events : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QScxmlEventConnection::setEvents(const QStringList &events)
    self.uglySide.call(
        'ritual_ZN21QScxmlEventConnection9setEventsERK5QListI7QStringE',
        self._valueOf(events),
    )

  @overload(QScxmlStateMachine)
  @overload(NoneType)
  def setStateMachine(
      self,
      stateMachine: Optional[QScxmlStateMachine],
  ) -> None:
    """
    Calls Qt's 'void
    QScxmlEventConnection::setStateMachine(QScxmlStateMachine
    *stateMachine)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmleventconnection.html#setStateMachine

    Parameters
    ----------

    stateMachine : Optional[QScxmlStateMachine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QScxmlEventConnection::setStateMachine(QScxmlStateMachine
    #      *stateMachine)
    self.uglySide.call(
        'ritual_ZN21QScxmlEventConnection15setStateMachineEP18QScxmlStateMa'
        'chine',
        self._addressOf(stateMachine),
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
    Notes what was given, for Qt's
    'QScxmlEventConnection::QScxmlEventConnection(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmleventconnection.html#QScxmlEventConnection

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QScxmlEventConnection::QScxmlEventConnection(QObject *parent)
    self._noteCreation(QScxmlEventConnection, lambda: Rituals.call(
        'ritual_ZN21QScxmlEventConnectionC1EP7QObject',
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

  def eventsChanged(self) -> None:
    """
    Calls Qt's 'void QScxmlEventConnection::eventsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmleventconnection.html#eventsChanged
    """
    #  void QScxmlEventConnection::eventsChanged()
    self.uglySide.call('ritual_ZN21QScxmlEventConnection13eventsChangedEv')

  def stateMachineChanged(self) -> None:
    """
    Calls Qt's 'void QScxmlEventConnection::stateMachineChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmleventconnection.html#stateMachineChanged
    """
    #  void QScxmlEventConnection::stateMachineChanged()
    self.uglySide.call(
        'ritual_ZN21QScxmlEventConnection19stateMachineChangedEv',
    )

  @overload(QScxmlEvent)
  def occurred(self, event: QScxmlEvent) -> None:
    """
    Calls Qt's 'void QScxmlEventConnection::occurred(const QScxmlEvent
    &event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmleventconnection.html#occurred

    Parameters
    ----------

    event : QScxmlEvent
      Passed on as a value: Qt reads the C++ QScxmlEvent, which stays
      Python's own.
    """
    #  void QScxmlEventConnection::occurred(const QScxmlEvent &event)
    self.uglySide.call(
        'ritual_ZN21QScxmlEventConnection8occurredERK11QScxmlEvent',
        self._valueOf(event),
    )

  def doConnect(self) -> None:
    """
    Calls Qt's 'void QScxmlEventConnection::doConnect()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmleventconnection.html#doConnect
    """
    #  void QScxmlEventConnection::doConnect()
    self.uglySide.call('ritual_ZN21QScxmlEventConnection9doConnectEv')

  def classBegin(self) -> None:
    """
    Calls Qt's 'void QScxmlEventConnection::classBegin()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmleventconnection.html#classBegin
    """
    #  void QScxmlEventConnection::classBegin()
    ritual = 'ritual_ZN21QScxmlEventConnection10classBeginEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QScxmlEventConnection10classBeginEv'
    self.uglySide.call(ritual)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QScxmlEventConnection::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmleventconnection.html#componentComplete
    """
    #  void QScxmlEventConnection::componentComplete()
    ritual = 'ritual_ZN21QScxmlEventConnection17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QScxmlEventConnection17componentCompleteEv'
    self.uglySide.call(ritual)

  @staticmethod
  def bindableEvents(*__, **_) -> Never:
    """
    Qt's 'QBindable<QStringList> QScxmlEventConnection::bindableEvents()':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QScxmlEventConnection.bindableEvents' has no cute function yet. "
        "Qt's 'QBindable<QStringList> "
        "QScxmlEventConnection::bindableEvents()': gives a type Python has "
        "no way to take yet.")

  @staticmethod
  def bindableStateMachine(*__, **_) -> Never:
    """
    Qt's 'QBindable<QScxmlStateMachine *>
    QScxmlEventConnection::bindableStateMachine()': gives a type Python has
    no way to take yet.
    """
    raise NotImplementedError(
        "'QScxmlEventConnection.bindableStateMachine' has no cute function "
        "yet. Qt's 'QBindable<QScxmlStateMachine *> "
        "QScxmlEventConnection::bindableStateMachine()': gives a type "
        "Python has no way to take yet.")
