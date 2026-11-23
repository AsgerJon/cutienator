"""
QObject binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qobject.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import Qt, QList, QMetaObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QBindingStorage, QByteArray, QChildEvent, QEvent, QMetaMethod
  from . import QThread, QTimerEvent, QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QChildEvent = WAIT['QChildEvent']
  QEvent = WAIT['QEvent']
  QMetaMethod = WAIT['QMetaMethod']
  QTimerEvent = WAIT['QTimerEvent']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QObject(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QObject: a plain Python object standing in front of
  one C++ QObject.

  What exists
  -----------

  Every function of Qt's QObject that has a ritual and that Python can call
  so far, 41 names in all: 'metaObject', 'tr', 'event', 'eventFilter',
  'objectName', 'setObjectName', 'isWidgetType', 'isWindowType',
  'isQuickItemType', 'isQmlExposed', 'signalsBlocked', 'blockSignals',
  'thread', 'startTimer', 'killTimer', 'children', 'setParent',
  'installEventFilter', 'removeEventFilter', 'connect', 'disconnect',
  'dumpObjectTree', 'dumpObjectInfo', 'setProperty', 'property',
  'dynamicPropertyNames', 'bindingStorage', 'parent', 'inherits',
  'deleteLater', 'sender', 'senderSignalIndex', 'receivers',
  'isSignalConnected', 'timerEvent', 'childEvent', 'customEvent',
  'connectNotify', 'disconnectNotify', 'doSetObjectName', 'doSetProperty'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QObject::~QObject()': the destructor: Python never removes a C++
    QObject.
  - Qt's 'const QBindingStorage *QObject::bindingStorage() const': takes in
    Python what 'QBindingStorage *QObject::bindingStorage()' takes.

  What has no ritual
  ------------------

  29 of the 80 functions Qt declares: 13 takes or gives a type that cannot be
  passed yet; 11 a template; 2 a signal; 2 forbidden; 1 declared and nowhere
  to be found.

  What to expect
  --------------

  - The C++ QObject is created at the first use, not by 'QObject(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QObject.
  - Qt tells when it has removed the C++ QObject. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
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
    Calls Qt's 'QString QObject::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qobject.html#tr

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
    #  QString QObject::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN7QObject2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(THIS, str, THIS, str)
  @overload(THIS, str, THIS, NoneType)
  @overload(THIS, str, NoneType, str)
  @overload(THIS, str, NoneType, NoneType)
  @overload(THIS, NoneType, THIS, str)
  @overload(THIS, NoneType, THIS, NoneType)
  @overload(THIS, NoneType, NoneType, str)
  @overload(THIS, NoneType, NoneType, NoneType)
  @overload(NoneType, str, THIS, str)
  @overload(NoneType, str, THIS, NoneType)
  @overload(NoneType, str, NoneType, str)
  @overload(NoneType, str, NoneType, NoneType)
  @overload(NoneType, NoneType, THIS, str)
  @overload(NoneType, NoneType, THIS, NoneType)
  @overload(NoneType, NoneType, NoneType, str)
  @overload(NoneType, NoneType, NoneType, NoneType)
  @overload(THIS, str, THIS, str, Qt.ConnectionType)
  @overload(THIS, str, THIS, NoneType, Qt.ConnectionType)
  @overload(THIS, str, NoneType, str, Qt.ConnectionType)
  @overload(THIS, str, NoneType, NoneType, Qt.ConnectionType)
  @overload(THIS, NoneType, THIS, str, Qt.ConnectionType)
  @overload(THIS, NoneType, THIS, NoneType, Qt.ConnectionType)
  @overload(THIS, NoneType, NoneType, str, Qt.ConnectionType)
  @overload(THIS, NoneType, NoneType, NoneType, Qt.ConnectionType)
  @overload(NoneType, str, THIS, str, Qt.ConnectionType)
  @overload(NoneType, str, THIS, NoneType, Qt.ConnectionType)
  @overload(NoneType, str, NoneType, str, Qt.ConnectionType)
  @overload(NoneType, str, NoneType, NoneType, Qt.ConnectionType)
  @overload(NoneType, NoneType, THIS, str, Qt.ConnectionType)
  @overload(NoneType, NoneType, THIS, NoneType, Qt.ConnectionType)
  @overload(NoneType, NoneType, NoneType, str, Qt.ConnectionType)
  @overload(NoneType, NoneType, NoneType, NoneType, Qt.ConnectionType)
  def connect(
      sender: Optional[QObject],
      signal: Optional[str],
      receiver: Optional[QObject],
      member: Optional[str],
      a4: Qt.ConnectionType = Qt.ConnectionType.AutoConnection,
  ) -> QMetaObject.Connection:
    """
    Calls Qt's 'QMetaObject::Connection QObject::connect(const QObject
    *sender, const char *signal, const QObject *receiver, const char *member,
    Qt::ConnectionType a4)'.

    Qt's own words: https://doc.qt.io/qt-6/qobject.html#connect

    Parameters
    ----------

    sender : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    signal : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    receiver : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    member : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    a4 : Qt.ConnectionType
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.ConnectionType.AutoConnection.

    Returns
    -------

    QMetaObject.Connection
      A new cute QMetaObject::Connection around the copy Qt gave back. Python
      owns it.
    """
    #  QMetaObject::Connection QObject::connect(const QObject *sender, const
    #      char *signal, const QObject *receiver, const char *member,
    #      Qt::ConnectionType a4)
    address = Rituals.call(
        'ritual_ZN7QObject7connectEPKS_PKcS1_S3_N2Qt14ConnectionTypeE',
        CuteMixin._addressOf(sender), CuteMixin._bytesOf(signal),
        CuteMixin._addressOf(receiver), CuteMixin._bytesOf(member), a4.value,
    )
    return QMetaObject.Connection._cuteOwning(address)

  @staticmethod
  @overload(THIS, QMetaMethod, THIS, QMetaMethod)
  @overload(THIS, QMetaMethod, NoneType, QMetaMethod)
  @overload(NoneType, QMetaMethod, THIS, QMetaMethod)
  @overload(NoneType, QMetaMethod, NoneType, QMetaMethod)
  @overload(THIS, QMetaMethod, THIS, QMetaMethod, Qt.ConnectionType)
  @overload(THIS, QMetaMethod, NoneType, QMetaMethod, Qt.ConnectionType)
  @overload(NoneType, QMetaMethod, THIS, QMetaMethod, Qt.ConnectionType)
  @overload(NoneType, QMetaMethod, NoneType, QMetaMethod, Qt.ConnectionType)
  def connect(
      sender: Optional[QObject],
      signal: QMetaMethod,
      receiver: Optional[QObject],
      method: QMetaMethod,
      type: Qt.ConnectionType = Qt.ConnectionType.AutoConnection,
  ) -> QMetaObject.Connection:
    """
    Calls Qt's 'QMetaObject::Connection QObject::connect(const QObject
    *sender, const QMetaMethod &signal, const QObject *receiver, const
    QMetaMethod &method, Qt::ConnectionType type)'.

    Qt's own words: https://doc.qt.io/qt-6/qobject.html#connect

    Parameters
    ----------

    sender : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    signal : QMetaMethod
      Passed on as a value: Qt reads the C++ QMetaMethod, which stays
      Python's own.

    receiver : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    method : QMetaMethod
      Passed on as a value: Qt reads the C++ QMetaMethod, which stays
      Python's own.

    type : Qt.ConnectionType
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.ConnectionType.AutoConnection.

    Returns
    -------

    QMetaObject.Connection
      A new cute QMetaObject::Connection around the copy Qt gave back. Python
      owns it.
    """
    #  QMetaObject::Connection QObject::connect(const QObject *sender, const
    #      QMetaMethod &signal, const QObject *receiver, const QMetaMethod
    #      &method, Qt::ConnectionType type)
    address = Rituals.call(
        'ritual_ZN7QObject7connectEPKS_RK11QMetaMethodS1_S4_N2Qt14Connectio'
        'nTypeE',
        CuteMixin._addressOf(sender), CuteMixin._valueOf(signal),
        CuteMixin._addressOf(receiver), CuteMixin._valueOf(method),
        type.value,
    )
    return QMetaObject.Connection._cuteOwning(address)

  @overload(THIS, str, str)
  @overload(THIS, str, NoneType)
  @overload(THIS, NoneType, str)
  @overload(THIS, NoneType, NoneType)
  @overload(NoneType, str, str)
  @overload(NoneType, str, NoneType)
  @overload(NoneType, NoneType, str)
  @overload(NoneType, NoneType, NoneType)
  @overload(THIS, str, str, Qt.ConnectionType)
  @overload(THIS, str, NoneType, Qt.ConnectionType)
  @overload(THIS, NoneType, str, Qt.ConnectionType)
  @overload(THIS, NoneType, NoneType, Qt.ConnectionType)
  @overload(NoneType, str, str, Qt.ConnectionType)
  @overload(NoneType, str, NoneType, Qt.ConnectionType)
  @overload(NoneType, NoneType, str, Qt.ConnectionType)
  @overload(NoneType, NoneType, NoneType, Qt.ConnectionType)
  def connect(
      self,
      sender: Optional[QObject],
      signal: Optional[str],
      member: Optional[str],
      type: Qt.ConnectionType = Qt.ConnectionType.AutoConnection,
  ) -> QMetaObject.Connection:
    """
    Calls Qt's 'QMetaObject::Connection QObject::connect(const QObject
    *sender, const char *signal, const char *member, Qt::ConnectionType type)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qobject.html#connect

    Parameters
    ----------

    sender : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    signal : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    member : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    type : Qt.ConnectionType
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.ConnectionType.AutoConnection.

    Returns
    -------

    QMetaObject.Connection
      A new cute QMetaObject::Connection around the copy Qt gave back. Python
      owns it.
    """
    #  QMetaObject::Connection QObject::connect(const QObject *sender, const
    #      char *signal, const char *member, Qt::ConnectionType type) const
    address = self.uglySide.call(
        'ritual_ZNK7QObject7connectEPKS_PKcS3_N2Qt14ConnectionTypeE',
        self._addressOf(sender), self._bytesOf(signal),
        self._bytesOf(member), type.value,
    )
    return QMetaObject.Connection._cuteOwning(address)

  @staticmethod
  @overload(THIS, str, THIS, str)
  @overload(THIS, str, THIS, NoneType)
  @overload(THIS, str, NoneType, str)
  @overload(THIS, str, NoneType, NoneType)
  @overload(THIS, NoneType, THIS, str)
  @overload(THIS, NoneType, THIS, NoneType)
  @overload(THIS, NoneType, NoneType, str)
  @overload(THIS, NoneType, NoneType, NoneType)
  @overload(NoneType, str, THIS, str)
  @overload(NoneType, str, THIS, NoneType)
  @overload(NoneType, str, NoneType, str)
  @overload(NoneType, str, NoneType, NoneType)
  @overload(NoneType, NoneType, THIS, str)
  @overload(NoneType, NoneType, THIS, NoneType)
  @overload(NoneType, NoneType, NoneType, str)
  @overload(NoneType, NoneType, NoneType, NoneType)
  def disconnect(
      sender: Optional[QObject],
      signal: Optional[str],
      receiver: Optional[QObject],
      member: Optional[str],
  ) -> bool:
    """
    Calls Qt's 'bool QObject::disconnect(const QObject *sender, const char
    *signal, const QObject *receiver, const char *member)'.

    Qt's own words: https://doc.qt.io/qt-6/qobject.html#disconnect

    Parameters
    ----------

    sender : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    signal : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    receiver : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    member : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  bool QObject::disconnect(const QObject *sender, const char *signal,
    #      const QObject *receiver, const char *member)
    return Rituals.call(
        'ritual_ZN7QObject10disconnectEPKS_PKcS1_S3_',
        CuteMixin._addressOf(sender), CuteMixin._bytesOf(signal),
        CuteMixin._addressOf(receiver), CuteMixin._bytesOf(member),
    )

  @staticmethod
  @overload(THIS, QMetaMethod, THIS, QMetaMethod)
  @overload(THIS, QMetaMethod, NoneType, QMetaMethod)
  @overload(NoneType, QMetaMethod, THIS, QMetaMethod)
  @overload(NoneType, QMetaMethod, NoneType, QMetaMethod)
  def disconnect(
      sender: Optional[QObject],
      signal: QMetaMethod,
      receiver: Optional[QObject],
      member: QMetaMethod,
  ) -> bool:
    """
    Calls Qt's 'bool QObject::disconnect(const QObject *sender, const
    QMetaMethod &signal, const QObject *receiver, const QMetaMethod
    &member)'.

    Qt's own words: https://doc.qt.io/qt-6/qobject.html#disconnect

    Parameters
    ----------

    sender : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    signal : QMetaMethod
      Passed on as a value: Qt reads the C++ QMetaMethod, which stays
      Python's own.

    receiver : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    member : QMetaMethod
      Passed on as a value: Qt reads the C++ QMetaMethod, which stays
      Python's own.
    """
    #  bool QObject::disconnect(const QObject *sender, const QMetaMethod
    #      &signal, const QObject *receiver, const QMetaMethod &member)
    return Rituals.call(
        'ritual_ZN7QObject10disconnectEPKS_RK11QMetaMethodS1_S4_',
        CuteMixin._addressOf(sender), CuteMixin._valueOf(signal),
        CuteMixin._addressOf(receiver), CuteMixin._valueOf(member),
    )

  @overload()
  @overload(str)
  @overload(NoneType)
  @overload(str, THIS)
  @overload(str, NoneType)
  @overload(NoneType, THIS)
  @overload(NoneType, NoneType)
  @overload(str, THIS, str)
  @overload(str, THIS, NoneType)
  @overload(str, NoneType, str)
  @overload(str, NoneType, NoneType)
  @overload(NoneType, THIS, str)
  @overload(NoneType, THIS, NoneType)
  @overload(NoneType, NoneType, str)
  @overload(NoneType, NoneType, NoneType)
  def disconnect(
      self,
      signal: Optional[str] = None,
      receiver: Optional[QObject] = None,
      member: Optional[str] = None,
  ) -> bool:
    """
    Calls Qt's 'bool QObject::disconnect(const char *signal, const QObject
    *receiver, const char *member) const'.

    Qt's own words: https://doc.qt.io/qt-6/qobject.html#disconnect

    Parameters
    ----------

    signal : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    receiver : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    member : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.
    """
    #  bool QObject::disconnect(const char *signal, const QObject *receiver,
    #      const char *member) const
    return self.uglySide.call(
        'ritual_ZNK7QObject10disconnectEPKcPKS_S1_',
        self._bytesOf(signal), self._addressOf(receiver),
        self._bytesOf(member),
    )

  @overload(THIS)
  @overload(THIS, str)
  @overload(THIS, NoneType)
  @overload(NoneType, str)
  def disconnect(
      self,
      receiver: Optional[QObject],
      member: Optional[str] = None,
  ) -> bool:
    """
    Calls Qt's 'bool QObject::disconnect(const QObject *receiver, const char
    *member) const'.

    Qt's own words: https://doc.qt.io/qt-6/qobject.html#disconnect

    Parameters
    ----------

    receiver : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    member : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.
    """
    #  bool QObject::disconnect(const QObject *receiver, const char *member)
    #      const
    return self.uglySide.call(
        'ritual_ZNK7QObject10disconnectEPKS_PKc',
        self._addressOf(receiver), self._bytesOf(member),
    )

  @staticmethod
  @overload(QMetaObject.Connection)
  def disconnect(a0: QMetaObject.Connection) -> bool:
    """
    Calls Qt's 'bool QObject::disconnect(const QMetaObject::Connection &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qobject.html#disconnect

    Parameters
    ----------

    a0 : QMetaObject.Connection
      Passed on as a value: Qt reads the C++ QMetaObject::Connection, which
      stays Python's own.
    """
    #  bool QObject::disconnect(const QMetaObject::Connection &a0)
    return Rituals.call(
        'ritual_ZN7QObject10disconnectERKN11QMetaObject10ConnectionE',
        CuteMixin._valueOf(a0),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QObject'

  #  Qt can watch a QObject and tell when it has removed it. Every class
  #  built on this one is a QObject too, and inherits this.
  __watched_by_qt__ = True

  #  A C++ QObject Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QObject'

  #  The functions Qt calls itself that QObject is the first to declare. A
  #  class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'event': (
          ('_ZN7QObject5eventEP6QEvent',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtCore:QEvent'),
           )),
      ),
      'eventFilter': (
          ('_ZN7QObject11eventFilterEPS_P6QEvent',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtCore:QObject'),
               ('address', 'address', 'QtCore:QEvent'),
           )),
      ),
      'timerEvent': (
          ('_ZN7QObject10timerEventEP11QTimerEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCore:QTimerEvent'),
           )),
      ),
      'childEvent': (
          ('_ZN7QObject10childEventEP11QChildEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCore:QChildEvent'),
           )),
      ),
      'customEvent': (
          ('_ZN7QObject11customEventEP6QEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCore:QEvent'),
           )),
      ),
      'connectNotify': (
          ('_ZN7QObject13connectNotifyERK11QMetaMethod',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QMetaMethod'),
           )),
      ),
      'disconnectNotify': (
          ('_ZN7QObject16disconnectNotifyERK11QMetaMethod',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QMetaMethod'),
           )),
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
    Calls Qt's 'const QMetaObject *QObject::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qobject.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QObject::metaObject() const
    address = self.uglySide.call('ritual_ZNK7QObject10metaObjectEv')
    return QMetaObject._cuteAt(address)

  def objectName(self) -> str:
    """
    Calls Qt's 'QString QObject::objectName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qobject.html#objectName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QObject::objectName() const
    return self.uglySide.call('ritual_ZNK7QObject10objectNameEv')

  def isWidgetType(self) -> bool:
    """
    Calls Qt's 'bool QObject::isWidgetType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qobject.html#isWidgetType
    """
    #  bool QObject::isWidgetType() const
    return self.uglySide.call('ritual_ZNK7QObject12isWidgetTypeEv')

  def isWindowType(self) -> bool:
    """
    Calls Qt's 'bool QObject::isWindowType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qobject.html#isWindowType
    """
    #  bool QObject::isWindowType() const
    return self.uglySide.call('ritual_ZNK7QObject12isWindowTypeEv')

  def isQuickItemType(self) -> bool:
    """
    Calls Qt's 'bool QObject::isQuickItemType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qobject.html#isQuickItemType
    """
    #  bool QObject::isQuickItemType() const
    return self.uglySide.call('ritual_ZNK7QObject15isQuickItemTypeEv')

  def isQmlExposed(self) -> bool:
    """
    Calls Qt's 'bool QObject::isQmlExposed() const'.

    Qt's own words: https://doc.qt.io/qt-6/qobject.html#isQmlExposed
    """
    #  bool QObject::isQmlExposed() const
    return self.uglySide.call('ritual_ZNK7QObject12isQmlExposedEv')

  def signalsBlocked(self) -> bool:
    """
    Calls Qt's 'bool QObject::signalsBlocked() const'.

    Qt's own words: https://doc.qt.io/qt-6/qobject.html#signalsBlocked
    """
    #  bool QObject::signalsBlocked() const
    return self.uglySide.call('ritual_ZNK7QObject14signalsBlockedEv')

  def thread(self) -> Optional[QThread]:
    """
    Calls Qt's 'QThread *QObject::thread() const'.

    Qt's own words: https://doc.qt.io/qt-6/qobject.html#thread

    Returns
    -------

    Optional[QThread]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QThread *QObject::thread() const
    address = self.uglySide.call('ritual_ZNK7QObject6threadEv')
    from . import QThread
    return QThread._cuteAt(address)

  def children(self) -> QList[QObject]:
    """
    Calls Qt's 'const QObjectList &QObject::children() const'.

    Qt's own words: https://doc.qt.io/qt-6/qobject.html#children

    Returns
    -------

    QList[QObject]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  const QObjectList &QObject::children() const
    address = self.uglySide.call('ritual_ZNK7QObject8childrenEv')
    return QList[QObject]._cuteOwning(address)

  @overload(str)
  @overload(NoneType)
  def property(self, name: Optional[str]) -> QVariant:
    """
    Calls Qt's 'QVariant QObject::property(const char *name) const'.

    Qt's own words: https://doc.qt.io/qt-6/qobject.html#property

    Parameters
    ----------

    name : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QObject::property(const char *name) const
    address = self.uglySide.call(
        'ritual_ZNK7QObject8propertyEPKc', self._bytesOf(name),
    )
    from . import QVariant
    return QVariant._cuteOwning(address)

  def dynamicPropertyNames(self) -> QList[QByteArray]:
    """
    Calls Qt's 'QList<QByteArray> QObject::dynamicPropertyNames() const'.

    Qt's own words: https://doc.qt.io/qt-6/qobject.html#dynamicPropertyNames

    Returns
    -------

    QList[QByteArray]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QByteArray> QObject::dynamicPropertyNames() const
    address = self.uglySide.call(
        'ritual_ZNK7QObject20dynamicPropertyNamesEv',
    )
    from . import QByteArray
    return QList[QByteArray]._cuteOwning(address)

  def parent(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QObject::parent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qobject.html#parent

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QObject::parent() const
    address = self.uglySide.call('ritual_ZNK7QObject6parentEv')
    return QObject._cuteAt(address)

  @overload(str)
  @overload(NoneType)
  def inherits(self, classname: Optional[str]) -> bool:
    """
    Calls Qt's 'bool QObject::inherits(const char *classname) const'.

    Qt's own words: https://doc.qt.io/qt-6/qobject.html#inherits

    Parameters
    ----------

    classname : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  bool QObject::inherits(const char *classname) const
    return self.uglySide.call(
        'ritual_ZNK7QObject8inheritsEPKc', self._bytesOf(classname),
    )

  def sender(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QObject::sender() const'.

    Qt's own words: https://doc.qt.io/qt-6/qobject.html#sender

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QObject::sender() const
    address = self.uglySide.call('ritual_ZNK7QObject6senderEv')
    return QObject._cuteAt(address)

  def senderSignalIndex(self) -> int:
    """
    Calls Qt's 'int QObject::senderSignalIndex() const'.

    Qt's own words: https://doc.qt.io/qt-6/qobject.html#senderSignalIndex
    """
    #  int QObject::senderSignalIndex() const
    return self.uglySide.call('ritual_ZNK7QObject17senderSignalIndexEv')

  @overload(str)
  @overload(NoneType)
  def receivers(self, signal: Optional[str]) -> int:
    """
    Calls Qt's 'int QObject::receivers(const char *signal) const'.

    Qt's own words: https://doc.qt.io/qt-6/qobject.html#receivers

    Parameters
    ----------

    signal : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  int QObject::receivers(const char *signal) const
    return self.uglySide.call(
        'ritual_ZNK7QObject9receiversEPKc', self._bytesOf(signal),
    )

  @overload(QMetaMethod)
  def isSignalConnected(self, signal: QMetaMethod) -> bool:
    """
    Calls Qt's 'bool QObject::isSignalConnected(const QMetaMethod &signal)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qobject.html#isSignalConnected

    Parameters
    ----------

    signal : QMetaMethod
      Passed on as a value: Qt reads the C++ QMetaMethod, which stays
      Python's own.
    """
    #  bool QObject::isSignalConnected(const QMetaMethod &signal) const
    return self.uglySide.call(
        'ritual_ZNK7QObject17isSignalConnectedERK11QMetaMethod',
        self._valueOf(signal),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setObjectName(self, name: str) -> None:
    """
    Calls Qt's 'void QObject::setObjectName(QAnyStringView name)'.

    Qt's own words: https://doc.qt.io/qt-6/qobject.html#setObjectName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QObject::setObjectName(QAnyStringView name)
    self.uglySide.call(
        'ritual_ZN7QObject13setObjectNameE14QAnyStringView', name,
    )

  @overload(THIS)
  @overload(NoneType)
  def setParent(self, parent: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QObject::setParent(QObject *parent)'.

    Qt's own words: https://doc.qt.io/qt-6/qobject.html#setParent

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QObject::setParent(QObject *parent)
    self.uglySide.call(
        'ritual_ZN7QObject9setParentEPS_', self._addressOf(parent),
    )

  @overload(str, QVariant)
  @overload(NoneType, QVariant)
  def setProperty(self, name: Optional[str], value: QVariant) -> bool:
    """
    Calls Qt's 'bool QObject::setProperty(const char *name, const QVariant
    &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qobject.html#setProperty

    Parameters
    ----------

    name : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  bool QObject::setProperty(const char *name, const QVariant &value)
    return self.uglySide.call(
        'ritual_ZN7QObject11setPropertyEPKcRK8QVariant',
        self._bytesOf(name), self._valueOf(value),
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
  @overload(THIS)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's 'QObject::QObject(QObject *parent)', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qobject.html#QObject

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QObject::QObject(QObject *parent)
    self._noteCreation(QObject, lambda: Rituals.call(
        'ritual_ZN7QObjectC1EPS_', self._addressOf(parent),
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

  @overload(QEvent)
  @overload(NoneType)
  def event(self, event: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QObject::event(QEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qobject.html#event

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QObject::event(QEvent *event)
    ritual = 'ritual_ZN7QObject5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN7QObject5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(event))

  @overload(THIS, QEvent)
  @overload(THIS, NoneType)
  @overload(NoneType, QEvent)
  @overload(NoneType, NoneType)
  def eventFilter(
      self,
      watched: Optional[QObject],
      event: Optional[QEvent],
  ) -> bool:
    """
    Calls Qt's 'bool QObject::eventFilter(QObject *watched, QEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qobject.html#eventFilter

    Parameters
    ----------

    watched : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QObject::eventFilter(QObject *watched, QEvent *event)
    ritual = 'ritual_ZN7QObject11eventFilterEPS_P6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN7QObject11eventFilterEPS_P6QEvent'
    return self.uglySide.call(
        ritual, self._addressOf(watched), self._addressOf(event),
    )

  @overload(bool)
  def blockSignals(self, b: bool) -> bool:
    """
    Calls Qt's 'bool QObject::blockSignals(bool b)'.

    Qt's own words: https://doc.qt.io/qt-6/qobject.html#blockSignals

    Parameters
    ----------

    b : bool
      Passed on as it is.
    """
    #  bool QObject::blockSignals(bool b)
    return self.uglySide.call('ritual_ZN7QObject12blockSignalsEb', b)

  @overload(int)
  @overload(int, Qt.TimerType)
  def startTimer(
      self,
      interval: int,
      timerType: Qt.TimerType = Qt.TimerType.CoarseTimer,
  ) -> int:
    """
    Calls Qt's 'int QObject::startTimer(int interval, Qt::TimerType
    timerType)'.

    Qt's own words: https://doc.qt.io/qt-6/qobject.html#startTimer

    Parameters
    ----------

    interval : int
      Passed on as it is.

    timerType : Qt.TimerType
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.TimerType.CoarseTimer.
    """
    #  int QObject::startTimer(int interval, Qt::TimerType timerType)
    return self.uglySide.call(
        'ritual_ZN7QObject10startTimerEiN2Qt9TimerTypeE',
        interval, timerType.value,
    )

  @overload(int)
  def killTimer(self, id: int) -> None:
    """
    Calls Qt's 'void QObject::killTimer(int id)'.

    Qt's own words: https://doc.qt.io/qt-6/qobject.html#killTimer

    Parameters
    ----------

    id : int
      Passed on as it is.
    """
    #  void QObject::killTimer(int id)
    self.uglySide.call('ritual_ZN7QObject9killTimerEi', id)

  @overload(Qt.TimerId)
  def killTimer(self, id: Qt.TimerId) -> None:
    """
    Calls Qt's 'void QObject::killTimer(Qt::TimerId id)'.

    Qt's own words: https://doc.qt.io/qt-6/qobject.html#killTimer

    Parameters
    ----------

    id : Qt.TimerId
      Passed on as its number.
    """
    #  void QObject::killTimer(Qt::TimerId id)
    self.uglySide.call('ritual_ZN7QObject9killTimerEN2Qt7TimerIdE', id.value)

  @overload(THIS)
  @overload(NoneType)
  def installEventFilter(self, filterObj: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QObject::installEventFilter(QObject *filterObj)'.

    Qt's own words: https://doc.qt.io/qt-6/qobject.html#installEventFilter

    Parameters
    ----------

    filterObj : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QObject::installEventFilter(QObject *filterObj)
    self.uglySide.call(
        'ritual_ZN7QObject18installEventFilterEPS_',
        self._addressOf(filterObj),
    )

  @overload(THIS)
  @overload(NoneType)
  def removeEventFilter(self, obj: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QObject::removeEventFilter(QObject *obj)'.

    Qt's own words: https://doc.qt.io/qt-6/qobject.html#removeEventFilter

    Parameters
    ----------

    obj : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QObject::removeEventFilter(QObject *obj)
    self.uglySide.call(
        'ritual_ZN7QObject17removeEventFilterEPS_', self._addressOf(obj),
    )

  def dumpObjectTree(self) -> None:
    """
    Calls Qt's 'void QObject::dumpObjectTree() const'.

    Qt's own words: https://doc.qt.io/qt-6/qobject.html#dumpObjectTree
    """
    #  void QObject::dumpObjectTree() const
    self.uglySide.call('ritual_ZNK7QObject14dumpObjectTreeEv')

  def dumpObjectInfo(self) -> None:
    """
    Calls Qt's 'void QObject::dumpObjectInfo() const'.

    Qt's own words: https://doc.qt.io/qt-6/qobject.html#dumpObjectInfo
    """
    #  void QObject::dumpObjectInfo() const
    self.uglySide.call('ritual_ZNK7QObject14dumpObjectInfoEv')

  def bindingStorage(self) -> Optional[QBindingStorage]:
    """
    Calls Qt's 'QBindingStorage *QObject::bindingStorage()'.

    Qt's own words: https://doc.qt.io/qt-6/qobject.html#bindingStorage

    Returns
    -------

    Optional[QBindingStorage]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QBindingStorage *QObject::bindingStorage()
    address = self.uglySide.call('ritual_ZN7QObject14bindingStorageEv')
    from . import QBindingStorage
    return QBindingStorage._cuteAt(address)

  def deleteLater(self) -> None:
    """
    Calls Qt's 'void QObject::deleteLater()'.

    Qt's own words: https://doc.qt.io/qt-6/qobject.html#deleteLater
    """
    #  void QObject::deleteLater()
    self.uglySide.call('ritual_ZN7QObject11deleteLaterEv')

  @overload(QTimerEvent)
  @overload(NoneType)
  def timerEvent(self, event: Optional[QTimerEvent]) -> None:
    """
    Calls Qt's 'void QObject::timerEvent(QTimerEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qobject.html#timerEvent

    Parameters
    ----------

    event : Optional[QTimerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QObject::timerEvent(QTimerEvent *event)
    ritual = 'ritual_ZN7QObject10timerEventEP11QTimerEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN7QObject10timerEventEP11QTimerEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QChildEvent)
  @overload(NoneType)
  def childEvent(self, event: Optional[QChildEvent]) -> None:
    """
    Calls Qt's 'void QObject::childEvent(QChildEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qobject.html#childEvent

    Parameters
    ----------

    event : Optional[QChildEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QObject::childEvent(QChildEvent *event)
    ritual = 'ritual_ZN7QObject10childEventEP11QChildEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN7QObject10childEventEP11QChildEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QEvent)
  @overload(NoneType)
  def customEvent(self, event: Optional[QEvent]) -> None:
    """
    Calls Qt's 'void QObject::customEvent(QEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qobject.html#customEvent

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QObject::customEvent(QEvent *event)
    ritual = 'ritual_ZN7QObject11customEventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN7QObject11customEventEP6QEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QMetaMethod)
  def connectNotify(self, signal: QMetaMethod) -> None:
    """
    Calls Qt's 'void QObject::connectNotify(const QMetaMethod &signal)'.

    Qt's own words: https://doc.qt.io/qt-6/qobject.html#connectNotify

    Parameters
    ----------

    signal : QMetaMethod
      Passed on as a value: Qt reads the C++ QMetaMethod, which stays
      Python's own.
    """
    #  void QObject::connectNotify(const QMetaMethod &signal)
    ritual = 'ritual_ZN7QObject13connectNotifyERK11QMetaMethod'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN7QObject13connectNotifyERK11QMetaMethod'
    self.uglySide.call(ritual, self._valueOf(signal))

  @overload(QMetaMethod)
  def disconnectNotify(self, signal: QMetaMethod) -> None:
    """
    Calls Qt's 'void QObject::disconnectNotify(const QMetaMethod &signal)'.

    Qt's own words: https://doc.qt.io/qt-6/qobject.html#disconnectNotify

    Parameters
    ----------

    signal : QMetaMethod
      Passed on as a value: Qt reads the C++ QMetaMethod, which stays
      Python's own.
    """
    #  void QObject::disconnectNotify(const QMetaMethod &signal)
    ritual = 'ritual_ZN7QObject16disconnectNotifyERK11QMetaMethod'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN7QObject16disconnectNotifyERK11QMetaMethod'
    self.uglySide.call(ritual, self._valueOf(signal))

  @overload(str)
  def doSetObjectName(self, name: str) -> None:
    """
    Calls Qt's 'void QObject::doSetObjectName(const QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qobject.html#doSetObjectName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QObject::doSetObjectName(const QString &name)
    self.uglySide.call('ritual_ZN7QObject15doSetObjectNameERK7QString', name)

  @overload(str, QVariant, QVariant)
  @overload(str, QVariant, NoneType)
  @overload(NoneType, QVariant, QVariant)
  @overload(NoneType, QVariant, NoneType)
  def doSetProperty(
      self,
      name: Optional[str],
      value: QVariant,
      rvalue: Optional[QVariant],
  ) -> bool:
    """
    Calls Qt's 'bool QObject::doSetProperty(const char *name, const QVariant
    &value, QVariant *rvalue)'.

    Qt's own words: https://doc.qt.io/qt-6/qobject.html#doSetProperty

    Parameters
    ----------

    name : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    rvalue : Optional[QVariant]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QObject::doSetProperty(const char *name, const QVariant &value,
    #      QVariant *rvalue)
    return self.uglySide.call(
        'ritual_ZN7QObject13doSetPropertyEPKcRK8QVariantPS2_',
        self._bytesOf(name), self._valueOf(value), self._addressOf(rvalue),
    )


#  Qt's 'QList<QObject *>': the list of QObject, which 'QList[QObject]'
#  gives. It is made here, so that there is one as soon as there can be a
#  QObject. Qt has a name of its own for it.
QObjectList = QList.createKind(
    QObject, 'address',
    name='QObjectList',
    make='ritual_list_make_QObject_ptr',
    add='ritual_list_add_QObject_ptr',
    size='ritual_list_size_QObject_ptr',
    at='ritual_list_at_QObject_ptr',
    drop='ritual_list_drop_QObject_ptr',
)
