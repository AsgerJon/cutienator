"""
QQuickActionGroup binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickactiongroup_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickActionGroup to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QQuickAction, QQuickActionGroupAttached
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickAction = WAIT['QQuickAction']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickActionGroup(QObject):
  """
  The cute side of Qt's QQuickActionGroup: a plain Python object standing in
  front of one C++ QQuickActionGroup.

  It is built on the cute 'QObject', as Qt's QQuickActionGroup is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickActionGroup that has a ritual and that Python
  can call so far, 16 names in all: 'metaObject', 'tr',
  'qmlAttachedProperties', 'checkedAction', 'setCheckedAction',
  'isExclusive', 'setExclusive', 'isEnabled', 'setEnabled', 'addAction',
  'removeAction', 'checkedActionChanged', 'actionsChanged',
  'exclusiveChanged', 'enabledChanged', 'triggered'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickActionGroup::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickActionGroup::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickActionGroup::qt_qmlMarker_attached()': one of Qt's own
    inner workings.
  - Qt's 'QQuickActionGroup::~QQuickActionGroup()': the destructor: Python
    never removes a C++ QQuickActionGroup.
  - Qt's 'QQmlListProperty<QQuickAction> QQuickActionGroup::actions()': gives
    a type Python has no way to take yet.
  - Qt's 'QQuickActionGroupPrivate *QQuickActionGroup::d_func()': gives
    'QQuickActionGroupPrivate', which has no cute class yet.
  - Qt's 'const QQuickActionGroupPrivate *QQuickActionGroup::d_func() const':
    gives 'QQuickActionGroupPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 28 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickActionGroup is created at the first use, not by
    'QQuickActionGroup(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickActionGroup.
  - Qt tells when it has removed the C++ QQuickActionGroup. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickActionGroup that has no cute function yet,
    'actions', holds a function that raises 'NotImplementedError', and its
    docstring says why.
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
    Calls Qt's 'QString QQuickActionGroup::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickactiongroup.html#tr

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
    #  QString QQuickActionGroup::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN17QQuickActionGroup2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  def qmlAttachedProperties(
      object: Optional[QObject],
  ) -> Optional[QQuickActionGroupAttached]:
    """
    Calls Qt's 'QQuickActionGroupAttached
    *QQuickActionGroup::qmlAttachedProperties(QObject *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickactiongroup.html#qmlAttachedProperties

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickActionGroupAttached]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickActionGroupAttached
    #      *QQuickActionGroup::qmlAttachedProperties(QObject *object)
    address = Rituals.call(
        'ritual_ZN17QQuickActionGroup21qmlAttachedPropertiesEP7QObject',
        CuteMixin._addressOf(object, 'QObject'),
    )
    from . import QQuickActionGroupAttached
    return QQuickActionGroupAttached._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickActionGroup'

  #  A C++ QQuickActionGroup Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickActionGroup'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickActionGroup::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickactiongroup.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickActionGroup::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QQuickActionGroup10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def checkedAction(self) -> Optional[QQuickAction]:
    """
    Calls Qt's 'QQuickAction *QQuickActionGroup::checkedAction() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickactiongroup.html#checkedAction

    Returns
    -------

    Optional[QQuickAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickAction *QQuickActionGroup::checkedAction() const
    address = self.uglySide.call(
        'ritual_ZNK17QQuickActionGroup13checkedActionEv',
    )
    from . import QQuickAction
    return QQuickAction._cuteAt(address)

  def isExclusive(self) -> bool:
    """
    Calls Qt's 'bool QQuickActionGroup::isExclusive() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickactiongroup.html#isExclusive
    """
    #  bool QQuickActionGroup::isExclusive() const
    return self.uglySide.call('ritual_ZNK17QQuickActionGroup11isExclusiveEv')

  def isEnabled(self) -> bool:
    """
    Calls Qt's 'bool QQuickActionGroup::isEnabled() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickactiongroup.html#isEnabled
    """
    #  bool QQuickActionGroup::isEnabled() const
    return self.uglySide.call('ritual_ZNK17QQuickActionGroup9isEnabledEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuickAction)
  @overload(NoneType)
  def setCheckedAction(self, checkedAction: Optional[QQuickAction]) -> None:
    """
    Calls Qt's 'void QQuickActionGroup::setCheckedAction(QQuickAction
    *checkedAction)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickactiongroup.html#setCheckedAction

    Parameters
    ----------

    checkedAction : Optional[QQuickAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickActionGroup::setCheckedAction(QQuickAction *checkedAction)
    self.uglySide.call(
        'ritual_ZN17QQuickActionGroup16setCheckedActionEP12QQuickAction',
        self._addressOf(checkedAction),
    )

  @overload(bool)
  def setExclusive(self, exclusive: bool) -> None:
    """
    Calls Qt's 'void QQuickActionGroup::setExclusive(bool exclusive)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickactiongroup.html#setExclusive

    Parameters
    ----------

    exclusive : bool
      Passed on as it is.
    """
    #  void QQuickActionGroup::setExclusive(bool exclusive)
    self.uglySide.call(
        'ritual_ZN17QQuickActionGroup12setExclusiveEb', exclusive,
    )

  @overload(bool)
  def setEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QQuickActionGroup::setEnabled(bool enabled)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickactiongroup.html#setEnabled

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QQuickActionGroup::setEnabled(bool enabled)
    self.uglySide.call('ritual_ZN17QQuickActionGroup10setEnabledEb', enabled)

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
    'QQuickActionGroup::QQuickActionGroup(QObject *parent)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickactiongroup.html#QQuickActionGroup

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickActionGroup::QQuickActionGroup(QObject *parent)
    self._noteCreation(QQuickActionGroup, lambda: Rituals.call(
        'ritual_ZN17QQuickActionGroupC1EP7QObject',
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

  @overload(QQuickAction)
  @overload(NoneType)
  def addAction(self, action: Optional[QQuickAction]) -> None:
    """
    Calls Qt's 'void QQuickActionGroup::addAction(QQuickAction *action)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickactiongroup.html#addAction

    Parameters
    ----------

    action : Optional[QQuickAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickActionGroup::addAction(QQuickAction *action)
    self.uglySide.call(
        'ritual_ZN17QQuickActionGroup9addActionEP12QQuickAction',
        self._addressOf(action),
    )

  @overload(QQuickAction)
  @overload(NoneType)
  def removeAction(self, action: Optional[QQuickAction]) -> None:
    """
    Calls Qt's 'void QQuickActionGroup::removeAction(QQuickAction *action)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickactiongroup.html#removeAction

    Parameters
    ----------

    action : Optional[QQuickAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickActionGroup::removeAction(QQuickAction *action)
    self.uglySide.call(
        'ritual_ZN17QQuickActionGroup12removeActionEP12QQuickAction',
        self._addressOf(action),
    )

  def checkedActionChanged(self) -> None:
    """
    Calls Qt's 'void QQuickActionGroup::checkedActionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickactiongroup.html#checkedActionChanged
    """
    #  void QQuickActionGroup::checkedActionChanged()
    self.uglySide.call(
        'ritual_ZN17QQuickActionGroup20checkedActionChangedEv',
    )

  def actionsChanged(self) -> None:
    """
    Calls Qt's 'void QQuickActionGroup::actionsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickactiongroup.html#actionsChanged
    """
    #  void QQuickActionGroup::actionsChanged()
    self.uglySide.call('ritual_ZN17QQuickActionGroup14actionsChangedEv')

  def exclusiveChanged(self) -> None:
    """
    Calls Qt's 'void QQuickActionGroup::exclusiveChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickactiongroup.html#exclusiveChanged
    """
    #  void QQuickActionGroup::exclusiveChanged()
    self.uglySide.call('ritual_ZN17QQuickActionGroup16exclusiveChangedEv')

  def enabledChanged(self) -> None:
    """
    Calls Qt's 'void QQuickActionGroup::enabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickactiongroup.html#enabledChanged
    """
    #  void QQuickActionGroup::enabledChanged()
    self.uglySide.call('ritual_ZN17QQuickActionGroup14enabledChangedEv')

  @overload(QQuickAction)
  @overload(NoneType)
  def triggered(self, action: Optional[QQuickAction]) -> None:
    """
    Calls Qt's 'void QQuickActionGroup::triggered(QQuickAction *action)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickactiongroup.html#triggered

    Parameters
    ----------

    action : Optional[QQuickAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickActionGroup::triggered(QQuickAction *action)
    self.uglySide.call(
        'ritual_ZN17QQuickActionGroup9triggeredEP12QQuickAction',
        self._addressOf(action),
    )

  @staticmethod
  def actions(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QQuickAction> QQuickActionGroup::actions()': gives
    a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQuickActionGroup.actions' has no cute function yet. Qt's "
        "'QQmlListProperty<QQuickAction> QQuickActionGroup::actions()': "
        "gives a type Python has no way to take yet.")
