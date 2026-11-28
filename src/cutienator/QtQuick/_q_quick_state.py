"""
QQuickState binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickstate_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQuickState to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QVariant
  from ..QtQml import QQmlAnyBinding
  from . import QQuickStateAction, QQuickStateGroup, QQuickStateOperation
  from . import QQuickStatePrivate, QQuickTransition
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlAnyBinding = WAIT['QQmlAnyBinding']
  QQuickStateAction = WAIT['QQuickStateAction']
  QQuickStateGroup = WAIT['QQuickStateGroup']
  QQuickTransition = WAIT['QQuickTransition']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickState(QObject):
  """
  The cute side of Qt's QQuickState: a plain Python object standing in front
  of one C++ QQuickState.

  It is built on the cute 'QObject', as Qt's QQuickState is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickState that has a ritual and that Python can
  call so far, 28 names in all: 'metaObject', 'tr', 'name', 'setName',
  'isNamed', 'isWhenKnown', 'when', 'setWhen', 'extends', 'setExtends',
  'operationCount', 'operationAt', 'apply', 'cancel', 'stateGroup',
  'setStateGroup', 'containsPropertyInRevertList', 'changeValueInRevertList',
  'changeBindingInRevertList', 'removeEntryFromRevertList',
  'addEntryToRevertList', 'removeAllEntriesFromRevertList',
  'addEntriesToRevertList', 'valueInRevertList', 'bindingInRevertList',
  'isStateActive', 'completed', 'd_func'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickState::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQuickState::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickState::~QQuickState()': the destructor: Python never removes
    a C++ QQuickState.
  - Qt's 'QQmlListProperty<QQuickStateOperation> QQuickState::changes()':
    gives a type Python has no way to take yet.
  - Qt's 'QQuickState &QQuickState::operator<<(QQuickStateOperation *a0)':
    gives a type Python has no way to take yet.
  - Qt's 'const QQuickStatePrivate *QQuickState::d_func() const': takes in
    Python what 'QQuickStatePrivate *QQuickState::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 39 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickState is created at the first use, not by
    'QQuickState(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickState.
  - Qt tells when it has removed the C++ QQuickState. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's QQuickState that has no cute function yet, 'changes',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
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
    Calls Qt's 'QString QQuickState::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstate.html#tr

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
    #  QString QQuickState::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN11QQuickState2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickState'

  #  A C++ QQuickState Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickState'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickState::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstate.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickState::metaObject() const
    address = self.uglySide.call('ritual_ZNK11QQuickState10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def name(self) -> str:
    """
    Calls Qt's 'QString QQuickState::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstate.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickState::name() const
    return self.uglySide.call('ritual_ZNK11QQuickState4nameEv')

  def isNamed(self) -> bool:
    """
    Calls Qt's 'bool QQuickState::isNamed() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstate.html#isNamed
    """
    #  bool QQuickState::isNamed() const
    return self.uglySide.call('ritual_ZNK11QQuickState7isNamedEv')

  def isWhenKnown(self) -> bool:
    """
    Calls Qt's 'bool QQuickState::isWhenKnown() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstate.html#isWhenKnown
    """
    #  bool QQuickState::isWhenKnown() const
    return self.uglySide.call('ritual_ZNK11QQuickState11isWhenKnownEv')

  def when(self) -> bool:
    """
    Calls Qt's 'bool QQuickState::when() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstate.html#when
    """
    #  bool QQuickState::when() const
    return self.uglySide.call('ritual_ZNK11QQuickState4whenEv')

  def extends(self) -> str:
    """
    Calls Qt's 'QString QQuickState::extends() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstate.html#extends

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickState::extends() const
    return self.uglySide.call('ritual_ZNK11QQuickState7extendsEv')

  def operationCount(self) -> int:
    """
    Calls Qt's 'int QQuickState::operationCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstate.html#operationCount
    """
    #  int QQuickState::operationCount() const
    return self.uglySide.call('ritual_ZNK11QQuickState14operationCountEv')

  @overload(int)
  def operationAt(self, a0: int) -> Optional[QQuickStateOperation]:
    """
    Calls Qt's 'QQuickStateOperation *QQuickState::operationAt(int a0)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstate.html#operationAt

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    Returns
    -------

    Optional[QQuickStateOperation]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickStateOperation *QQuickState::operationAt(int a0) const
    address = self.uglySide.call(
        'ritual_ZNK11QQuickState11operationAtEi', a0,
    )
    from . import QQuickStateOperation
    return QQuickStateOperation._cuteAt(address)

  def stateGroup(self) -> Optional[QQuickStateGroup]:
    """
    Calls Qt's 'QQuickStateGroup *QQuickState::stateGroup() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstate.html#stateGroup

    Returns
    -------

    Optional[QQuickStateGroup]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickStateGroup *QQuickState::stateGroup() const
    address = self.uglySide.call('ritual_ZNK11QQuickState10stateGroupEv')
    from . import QQuickStateGroup
    return QQuickStateGroup._cuteAt(address)

  @overload(QObject, str)
  @overload(NoneType, str)
  def containsPropertyInRevertList(
      self,
      target: Optional[QObject],
      name: str,
  ) -> bool:
    """
    Calls Qt's 'bool QQuickState::containsPropertyInRevertList(QObject
    *target, const QString &name) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstate.html#containsPropertyInRevertList

    Parameters
    ----------

    target : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QQuickState::containsPropertyInRevertList(QObject *target, const
    #      QString &name) const
    return self.uglySide.call(
        'ritual_ZNK11QQuickState28containsPropertyInRevertListEP7QObjectRK7'
        'QString',
        self._addressOf(target, 'QObject'), name,
    )

  @overload(QObject, str)
  @overload(NoneType, str)
  def valueInRevertList(
      self,
      target: Optional[QObject],
      name: str,
  ) -> QVariant:
    """
    Calls Qt's 'QVariant QQuickState::valueInRevertList(QObject *target,
    const QString &name) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstate.html#valueInRevertList

    Parameters
    ----------

    target : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQuickState::valueInRevertList(QObject *target, const QString
    #      &name) const
    address = self.uglySide.call(
        'ritual_ZNK11QQuickState17valueInRevertListEP7QObjectRK7QString',
        self._addressOf(target, 'QObject'), name,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(QObject, str)
  @overload(NoneType, str)
  def bindingInRevertList(
      self,
      target: Optional[QObject],
      name: str,
  ) -> QQmlAnyBinding:
    """
    Calls Qt's 'QQmlAnyBinding QQuickState::bindingInRevertList(QObject
    *target, const QString &name) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstate.html#bindingInRevertList

    Parameters
    ----------

    target : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QQmlAnyBinding
      A new cute QQmlAnyBinding around the copy Qt gave back. Python owns it.
    """
    #  QQmlAnyBinding QQuickState::bindingInRevertList(QObject *target, const
    #      QString &name) const
    address = self.uglySide.call(
        'ritual_ZNK11QQuickState19bindingInRevertListEP7QObjectRK7QString',
        self._addressOf(target, 'QObject'), name,
    )
    from ..QtQml import QQmlAnyBinding
    return QQmlAnyBinding._cuteOwning(address)

  def isStateActive(self) -> bool:
    """
    Calls Qt's 'bool QQuickState::isStateActive() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstate.html#isStateActive
    """
    #  bool QQuickState::isStateActive() const
    return self.uglySide.call('ritual_ZNK11QQuickState13isStateActiveEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setName(self, a0: str) -> None:
    """
    Calls Qt's 'void QQuickState::setName(const QString &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstate.html#setName

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickState::setName(const QString &a0)
    self.uglySide.call('ritual_ZN11QQuickState7setNameERK7QString', a0)

  @overload(bool)
  def setWhen(self, a0: bool) -> None:
    """
    Calls Qt's 'void QQuickState::setWhen(bool a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstate.html#setWhen

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QQuickState::setWhen(bool a0)
    self.uglySide.call('ritual_ZN11QQuickState7setWhenEb', a0)

  @overload(str)
  def setExtends(self, a0: str) -> None:
    """
    Calls Qt's 'void QQuickState::setExtends(const QString &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstate.html#setExtends

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickState::setExtends(const QString &a0)
    self.uglySide.call('ritual_ZN11QQuickState10setExtendsERK7QString', a0)

  @overload(QQuickStateGroup)
  @overload(NoneType)
  def setStateGroup(self, a0: Optional[QQuickStateGroup]) -> None:
    """
    Calls Qt's 'void QQuickState::setStateGroup(QQuickStateGroup *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstate.html#setStateGroup

    Parameters
    ----------

    a0 : Optional[QQuickStateGroup]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickState::setStateGroup(QQuickStateGroup *a0)
    self.uglySide.call(
        'ritual_ZN11QQuickState13setStateGroupEP16QQuickStateGroup',
        self._addressOf(a0),
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
    Notes what was given, for Qt's 'QQuickState::QQuickState(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qquickstate.html#QQuickState

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickState::QQuickState(QObject *parent)
    self._noteCreation(QQuickState, lambda: Rituals.call(
        'ritual_ZN11QQuickStateC1EP7QObject',
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

  @overload(QQuickTransition, THIS)
  @overload(QQuickTransition, NoneType)
  @overload(NoneType, THIS)
  @overload(NoneType, NoneType)
  def apply(
      self,
      a0: Optional[QQuickTransition],
      revert: Optional[QQuickState],
  ) -> None:
    """
    Calls Qt's 'void QQuickState::apply(QQuickTransition *a0, QQuickState
    *revert)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstate.html#apply

    Parameters
    ----------

    a0 : Optional[QQuickTransition]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    revert : Optional[QQuickState]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickState::apply(QQuickTransition *a0, QQuickState *revert)
    self.uglySide.call(
        'ritual_ZN11QQuickState5applyEP16QQuickTransitionPS_',
        self._addressOf(a0), self._addressOf(revert),
    )

  def cancel(self) -> None:
    """
    Calls Qt's 'void QQuickState::cancel()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstate.html#cancel
    """
    #  void QQuickState::cancel()
    self.uglySide.call('ritual_ZN11QQuickState6cancelEv')

  @overload(QObject, str, QVariant)
  @overload(NoneType, str, QVariant)
  def changeValueInRevertList(
      self,
      target: Optional[QObject],
      name: str,
      revertValue: QVariant,
  ) -> bool:
    """
    Calls Qt's 'bool QQuickState::changeValueInRevertList(QObject *target,
    const QString &name, const QVariant &revertValue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstate.html#changeValueInRevertList

    Parameters
    ----------

    target : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    name : str
      Passed on as it is: a QString is made of it for the call.

    revertValue : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  bool QQuickState::changeValueInRevertList(QObject *target, const
    #      QString &name, const QVariant &revertValue)
    return self.uglySide.call(
        'ritual_ZN11QQuickState23changeValueInRevertListEP7QObjectRK7QStrin'
        'gRK8QVariant',
        self._addressOf(target, 'QObject'), name, self._valueOf(revertValue),
    )

  @overload(QObject, str, QQmlAnyBinding)
  @overload(NoneType, str, QQmlAnyBinding)
  def changeBindingInRevertList(
      self,
      target: Optional[QObject],
      name: str,
      binding: QQmlAnyBinding,
  ) -> bool:
    """
    Calls Qt's 'bool QQuickState::changeBindingInRevertList(QObject *target,
    const QString &name, QQmlAnyBinding binding)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstate.html#changeBindingInRevertList

    Parameters
    ----------

    target : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    name : str
      Passed on as it is: a QString is made of it for the call.

    binding : QQmlAnyBinding
      Passed on as a value: Qt reads the C++ QQmlAnyBinding, which stays
      Python's own.
    """
    #  bool QQuickState::changeBindingInRevertList(QObject *target, const
    #      QString &name, QQmlAnyBinding binding)
    return self.uglySide.call(
        'ritual_ZN11QQuickState25changeBindingInRevertListEP7QObjectRK7QStr'
        'ing14QQmlAnyBinding',
        self._addressOf(target, 'QObject'), name, self._valueOf(binding),
    )

  @overload(QObject, str)
  @overload(NoneType, str)
  def removeEntryFromRevertList(
      self,
      target: Optional[QObject],
      name: str,
  ) -> bool:
    """
    Calls Qt's 'bool QQuickState::removeEntryFromRevertList(QObject *target,
    const QString &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstate.html#removeEntryFromRevertList

    Parameters
    ----------

    target : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QQuickState::removeEntryFromRevertList(QObject *target, const
    #      QString &name)
    return self.uglySide.call(
        'ritual_ZN11QQuickState25removeEntryFromRevertListEP7QObjectRK7QStr'
        'ing',
        self._addressOf(target, 'QObject'), name,
    )

  @overload(QQuickStateAction)
  def addEntryToRevertList(self, action: QQuickStateAction) -> None:
    """
    Calls Qt's 'void QQuickState::addEntryToRevertList(const
    QQuickStateAction &action)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstate.html#addEntryToRevertList

    Parameters
    ----------

    action : QQuickStateAction
      Passed on as a value: Qt reads the C++ QQuickStateAction, which stays
      Python's own.
    """
    #  void QQuickState::addEntryToRevertList(const QQuickStateAction
    #      &action)
    self.uglySide.call(
        'ritual_ZN11QQuickState20addEntryToRevertListERK17QQuickStateAction',
        self._valueOf(action),
    )

  @overload(QObject)
  @overload(NoneType)
  def removeAllEntriesFromRevertList(
      self,
      target: Optional[QObject],
  ) -> None:
    """
    Calls Qt's 'void QQuickState::removeAllEntriesFromRevertList(QObject
    *target)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstate.html#removeAllEntriesFromRevertList

    Parameters
    ----------

    target : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickState::removeAllEntriesFromRevertList(QObject *target)
    self.uglySide.call(
        'ritual_ZN11QQuickState30removeAllEntriesFromRevertListEP7QObject',
        self._addressOf(target, 'QObject'),
    )

  @overload(QList[QQuickStateAction])
  def addEntriesToRevertList(
      self,
      actions: QList[QQuickStateAction],
  ) -> None:
    """
    Calls Qt's 'void QQuickState::addEntriesToRevertList(const
    QList<QQuickStateAction> &actions)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstate.html#addEntriesToRevertList

    Parameters
    ----------

    actions : QList[QQuickStateAction]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QQuickState::addEntriesToRevertList(const
    #      QList<QQuickStateAction> &actions)
    self.uglySide.call(
        'ritual_ZN11QQuickState22addEntriesToRevertListERK5QListI17QQuickSt'
        'ateActionE',
        self._valueOf(actions),
    )

  def completed(self) -> None:
    """
    Calls Qt's 'void QQuickState::completed()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstate.html#completed
    """
    #  void QQuickState::completed()
    self.uglySide.call('ritual_ZN11QQuickState9completedEv')

  def d_func(self) -> Optional[QQuickStatePrivate]:
    """
    Calls Qt's 'QQuickStatePrivate *QQuickState::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstate.html#d_func

    Returns
    -------

    Optional[QQuickStatePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickStatePrivate *QQuickState::d_func()
    address = self.uglySide.call('ritual_ZN11QQuickState6d_funcEv')
    from . import QQuickStatePrivate
    return QQuickStatePrivate._cuteAt(address)

  @staticmethod
  def changes(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QQuickStateOperation> QQuickState::changes()':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQuickState.changes' has no cute function yet. Qt's "
        "'QQmlListProperty<QQuickStateOperation> QQuickState::changes()': "
        "gives a type Python has no way to take yet.")


#  Qt's 'QList<QQuickState *>': the list of QQuickState, which
#  'QList[QQuickState]' gives. It is made here, so that there is one as soon
#  as there can be a QQuickState.
QList.createKind(
    QQuickState, 'address',
    make='ritual_list_make_QQuickState_ptr',
    add='ritual_list_add_QQuickState_ptr',
    size='ritual_list_size_QQuickState_ptr',
    at='ritual_list_at_QQuickState_ptr',
    drop='ritual_list_drop_QQuickState_ptr',
)
