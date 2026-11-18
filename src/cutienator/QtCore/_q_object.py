"""
QObject binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from .._cute_mixin import CuteMixin
from .._meta_cute import MetaCute
from ._q_binding_storage import QBindingStorage
from ._q_event import QEvent
from ._q_meta_object import QMetaObject
from .._ugly import Ugly
from .._wait import WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QObject(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QObject: a plain Python object standing in front
  of one C++ QObject.

    mother = QObject()
    child = QObject(mother)
    child.parent() is mother               # True
    child.setObjectName('cutie')
    child.objectName()                     # 'cutie'
    child.metaObject().className()         # 'QObject'
    child.thread()                         # the QThread Python runs in

  This is the first class written out in full from its ritual file: one
  function here for each ritual in 'occult/rituals/q_object.cpp', with
  the few exceptions listed below. It is written by hand, in the shape a
  program is meant to write the others in.

  What exists
  -----------

  Every function of Qt's QObject that has a ritual and takes and gives
  nothing but numbers, text and objects of a cute class, 25 names in
  all: 'parent', 'setParent', 'objectName', 'setObjectName', 'tr',
  'thread', 'metaObject', 'bindingStorage', 'inherits', 'isWidgetType',
  'isWindowType', 'isQuickItemType', 'isQmlExposed', 'signalsBlocked',
  'blockSignals', 'event', 'eventFilter', 'installEventFilter',
  'removeEventFilter', 'startTimer', 'killTimer', 'disconnect',
  'dumpObjectTree', 'dumpObjectInfo' and 'deleteLater'. Creation takes
  a parent, None, or nothing.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's '~QObject()'. Python never removes a C++ QObject: Qt may
    still use it.
  - Qt's 'killTimer(Qt::TimerId id)'. No enum is reflected yet, so it
    would take an 'int', as 'killTimer(int id)' does, and one name
    cannot have two functions for one signature.
  - Qt's 'bindingStorage() const'. It differs from 'bindingStorage()'
    only in what C++ may do with the answer, which Python cannot say.
  - Qt's 'disconnect(sender, signal, receiver, member)' and
    'disconnect(const QMetaObject::Connection &)'. They are static
    functions, and the other two of that name are not. worktoy lets one
    name be one kind of method.
  - Qt's three 'connect' taking text or QMetaMethod. They give a
    'QMetaObject::Connection', which has no cute class yet. They come
    with the signals.
  - Qt's 'disconnect' taking two QMetaMethod, which has no cute class
    yet.
  - Qt's 'property' and 'setProperty'. They give and take a QVariant,
    which has no cute class yet.
  - Qt's 'moveToThread'. Its declaration takes a second argument, a
    mark of Qt's own named 'Qt::Disambiguated_t', which has no cute
    class.

  What has no ritual yet
  ----------------------

  41 of the 80 functions Qt declares, among them 'children',
  'findChild', 'findChildren' and 'dynamicPropertyNames'. Some take or
  give a type that no ritual can pass yet, as a list. Others are
  patterns for functions, are for a subclass alone, or are signals.

  What to expect
  --------------

  - The C++ QObject is created at the first use, not by 'QObject()'.
  - A function giving an object back gives the very cute object that
    stands for it when there is one, as 'parent' after 'setParent'. For
    an object C++ made itself, as the thread, it gives a new cute object
    made around it.
  - Qt's QString is a plain 'str', taken and given: 'setObjectName'
    takes one and 'objectName' gives one. There is no QString class.
  - Where Qt takes an object or text and reads nothing as 'none given',
    None is taken. Where Qt fills in an argument left out, that is not
    done yet: every argument is given.
  - An enum of Qt is taken and given as its number.
  - A wrong argument is refused in Python, with 'DispatchException',
    and never reaches C++.
  - Python never removes the C++ QObject. Qt does: a parent removes its
    children when it goes, and 'deleteLater' asks for it.
  - Qt tells when it has removed a C++ QObject. Every call on the cute
    object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str, str, int)
  @overload(str, NoneType, int)
  def tr(s: str, c: Optional[str], n: int) -> str:
    """
    Calls Qt's 'QString QObject::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qobject.html#tr

    Parameters
    ----------

    s : str
      Passed on as the bytes of the text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    n : int
      Passed on as it is. Qt fills this in with -1 when it is left out;
      here it has to be given.

    Returns
    -------

    str
      The text Qt gave back: 's' itself when no translation is loaded.
    """
    #  QString QObject::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN7QObject2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  Qt's QThread is built on QObject, so its cute class is made after
  #  this one. 'thread' gives one back all the same; see 'WAIT'.
  QThread = WAIT['QThread']

  #  Qt can watch a QObject and tell when it has removed it. Every class
  #  built on this one is a QObject too, and inherits this.
  __watched_by_qt__ = True

  #  Fallback Variables

  #  Private Variables
  #  The parent given to the constructor, kept until the C++ object is
  #  created.
  __given_parent__: Optional[QObject] = None

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def _createUglySide(self, ) -> None:
    """
    Creates the C++ QObject and the Ugly standing for it.

    'CuteMixin' calls this at the first read of 'uglySide'. The C++
    QObject is created with the parent given to 'QObject(...)', which is
    created first when it is not yet. Qt watches the new C++ QObject
    from here on, so a call made after Qt has removed it is refused.
    """
    #  QObject::QObject(QObject *parent)
    parent = self._addressOf(self.__given_parent__)
    ugly = Ugly()
    ugly.setAddress(Rituals.call('ritual_ZN7QObjectC1EPS_', parent))
    ugly.watch()
    ugly.setCuteSide(self)
    self.__ugly_side__ = ugly
    self.__given_parent__ = None

  def metaObject(self) -> QMetaObject:
    """
    Calls Qt's 'const QMetaObject *QObject::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qobject.html#metaObject

    Returns
    -------

    QMetaObject
      The cute object standing for what Qt gave back.
    """
    #  const QMetaObject *QObject::metaObject() const
    address = self.uglySide.call('ritual_ZNK7QObject10metaObjectEv')
    return QMetaObject._cuteAt(address)

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

  def thread(self) -> QThread:
    """
    Calls Qt's 'QThread *QObject::thread() const'.

    Qt's own words: https://doc.qt.io/qt-6/qobject.html#thread

    Returns
    -------

    QThread
      The cute object standing for what Qt gave back. For an object
      made in the thread Python runs in, that thread is one C++ made
      itself, so a new cute QThread is made around it.

    Raises
    ------

    MissingVariable
      The cute class 'QThread' is not made yet: its file was never
      imported.
    """
    #  QThread *QObject::thread() const
    address = self.uglySide.call('ritual_ZNK7QObject6threadEv')
    return self.QThread._cuteAt(address)

  def bindingStorage(self) -> QBindingStorage:
    """
    Calls Qt's 'QBindingStorage *QObject::bindingStorage()'.

    Qt's own words: https://doc.qt.io/qt-6/qobject.html#bindingStorage

    Returns
    -------

    QBindingStorage
      The cute object standing for what Qt gave back.
    """
    #  QBindingStorage *QObject::bindingStorage()
    address = self.uglySide.call('ritual_ZN7QObject14bindingStorageEv')
    return QBindingStorage._cuteAt(address)

  def parent(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QObject::parent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qobject.html#parent

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back: the very object
      that was given as the parent, when it still exists. None when Qt
      gave back no object.
    """
    #  QObject *QObject::parent() const
    address = self.uglySide.call('ritual_ZNK7QObject6parentEv')
    return QObject._cuteAt(address)

  def objectName(self) -> str:
    """
    Calls Qt's 'QString QObject::objectName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qobject.html#objectName-prop

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QObject::objectName() const
    return self.uglySide.call('ritual_ZNK7QObject10objectNameEv')

  @overload(str)
  def inherits(self, classname: str) -> bool:
    """
    Calls Qt's 'bool QObject::inherits(const char *classname) const'.

    Qt's own words: https://doc.qt.io/qt-6/qobject.html#inherits

    Parameters
    ----------

    classname : str
      Passed on as the bytes of the text.
    """
    #  bool QObject::inherits(const char *classname) const
    return self.uglySide.call(
        'ritual_ZNK7QObject8inheritsEPKc', self._bytesOf(classname),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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

  @overload(str)
  def setObjectName(self, name: str) -> None:
    """
    Calls Qt's 'void QObject::setObjectName(QAnyStringView name)'.

    Qt's own words: https://doc.qt.io/qt-6/qobject.html#objectName-prop

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
      Passed on as the address of its C++ object. None is passed on as
      no object.
    """
    #  void QObject::setParent(QObject *parent)
    self.uglySide.call(
        'ritual_ZN7QObject9setParentEPS_', self._addressOf(parent),
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
    Notes the parent for Qt's 'QObject::QObject(QObject *parent)', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qobject.html#QObject

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None, or nothing at
      all, is passed on as no object.
    """
    self.__given_parent__ = parent

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
  def event(self, event: QEvent) -> bool:
    """
    Calls Qt's 'bool QObject::event(QEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qobject.html#event

    Parameters
    ----------

    event : QEvent
      Passed on as the address of its C++ object.
    """
    #  bool QObject::event(QEvent *event)
    return self.uglySide.call(
        'ritual_ZN7QObject5eventEP6QEvent', self._addressOf(event),
    )

  @overload(THIS, QEvent)
  def eventFilter(self, watched: QObject, event: QEvent) -> bool:
    """
    Calls Qt's 'bool QObject::eventFilter(QObject *watched, QEvent
    *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qobject.html#eventFilter

    Parameters
    ----------

    watched : QObject
      Passed on as the address of its C++ object.

    event : QEvent
      Passed on as the address of its C++ object.
    """
    #  bool QObject::eventFilter(QObject *watched, QEvent *event)
    return self.uglySide.call(
        'ritual_ZN7QObject11eventFilterEPS_P6QEvent',
        self._addressOf(watched), self._addressOf(event),
    )

  @overload(int, int)
  def startTimer(self, interval: int, timerType: int) -> int:
    """
    Calls Qt's 'int QObject::startTimer(int interval, Qt::TimerType
    timerType)'.

    Qt's own words: https://doc.qt.io/qt-6/qobject.html#startTimer

    Parameters
    ----------

    interval : int
      Passed on as it is.

    timerType : int
      The number of a 'Qt::TimerType', as 1 for 'Qt::CoarseTimer'.
      Passed on as it is. Qt fills this in when it is left out; here it
      has to be given.
    """
    #  int QObject::startTimer(int interval, Qt::TimerType timerType)
    return self.uglySide.call(
        'ritual_ZN7QObject10startTimerEiN2Qt9TimerTypeE',
        interval, timerType,
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

  @overload(THIS)
  def installEventFilter(self, filterObj: QObject) -> None:
    """
    Calls Qt's 'void QObject::installEventFilter(QObject *filterObj)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qobject.html#installEventFilter

    Parameters
    ----------

    filterObj : QObject
      Passed on as the address of its C++ object.
    """
    #  void QObject::installEventFilter(QObject *filterObj)
    self.uglySide.call(
        'ritual_ZN7QObject18installEventFilterEPS_',
        self._addressOf(filterObj),
    )

  @overload(THIS)
  def removeEventFilter(self, obj: QObject) -> None:
    """
    Calls Qt's 'void QObject::removeEventFilter(QObject *obj)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qobject.html#removeEventFilter

    Parameters
    ----------

    obj : QObject
      Passed on as the address of its C++ object.
    """
    #  void QObject::removeEventFilter(QObject *obj)
    self.uglySide.call(
        'ritual_ZN7QObject17removeEventFilterEPS_', self._addressOf(obj),
    )

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
      signal: Optional[str],
      receiver: Optional[QObject],
      member: Optional[str],
  ) -> bool:
    """
    Calls Qt's 'bool QObject::disconnect(const char *signal, const
    QObject *receiver, const char *member) const'.

    Qt's own words: https://doc.qt.io/qt-6/qobject.html#disconnect-2

    Parameters
    ----------

    signal : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    receiver : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as
      no object.

    member : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  bool QObject::disconnect(const char *signal,
    #      const QObject *receiver, const char *member) const
    return self.uglySide.call(
        'ritual_ZNK7QObject10disconnectEPKcPKS_S1_',
        self._bytesOf(signal), self._addressOf(receiver),
        self._bytesOf(member),
    )

  @overload(THIS, str)
  @overload(THIS, NoneType)
  def disconnect(self, receiver: QObject, member: Optional[str]) -> bool:
    """
    Calls Qt's 'bool QObject::disconnect(const QObject *receiver, const
    char *member) const'.

    Qt's own words: https://doc.qt.io/qt-6/qobject.html#disconnect-3

    Parameters
    ----------

    receiver : QObject
      Passed on as the address of its C++ object.

    member : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  bool QObject::disconnect(const QObject *receiver,
    #      const char *member) const
    return self.uglySide.call(
        'ritual_ZNK7QObject10disconnectEPKS_PKc',
        self._addressOf(receiver), self._bytesOf(member),
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

  def deleteLater(self) -> None:
    """
    Calls Qt's 'void QObject::deleteLater()'.

    Qt's own words: https://doc.qt.io/qt-6/qobject.html#deleteLater
    """
    #  void QObject::deleteLater()
    self.uglySide.call('ritual_ZN7QObject11deleteLaterEv')
