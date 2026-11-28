"""
QQuickSimpleAction binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickstate_p_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQuickSimpleAction to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QObject, QVariant
  from ..QtQml import QQmlAnyBinding, QQmlProperty
  from . import QQuickStateAction, QQuickStateActionEvent
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlAnyBinding = WAIT['QQmlAnyBinding']
  QQmlProperty = WAIT['QQmlProperty']
  QQuickStateAction = WAIT['QQuickStateAction']
  QVariant = WAIT['QVariant']


class QQuickSimpleAction(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickSimpleAction: a plain Python object standing in
  front of one C++ QQuickSimpleAction.

  C++ hands a QQuickSimpleAction around as a copy, so every C++
  QQuickSimpleAction behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQuickSimpleAction that has a ritual and that Python
  can call so far, 10 names in all: 'setProperty', 'property', 'setValue',
  'value', 'setBinding', 'binding', 'specifiedObject', 'specifiedProperty',
  'event', 'reverseEvent'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQuickSimpleAction::~QQuickSimpleAction()': the destructor: Python
    removes its C++ QQuickSimpleAction by it, and has no other use for it.
  - Qt's 'QQuickSimpleAction &QQuickSimpleAction::operator=(const
    QQuickSimpleAction &other)': assignment: Python binds a name and has no
    operator for it.

  What to expect
  --------------

  - The C++ QQuickSimpleAction is created at the first use, not by
    'QQuickSimpleAction(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQuickSimpleAction back gives a copy the ritual made
    for Python, in a new cute QQuickSimpleAction.
  """

  #  The enums Qt writes inside QQuickSimpleAction, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class State(CuteNum):
    """
    The enum 'QQuickSimpleAction::State' of Qt, with the 2 names Qt gives in
    it.
    """

    StartState = Kee[int](0)
    EndState = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickSimpleAction'

  #  Qt's '~QQuickSimpleAction()'. Naming it makes this a value class: Python
  #  owns every C++ QQuickSimpleAction behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN18QQuickSimpleActionD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def property(self) -> QQmlProperty:
    """
    Calls Qt's 'const QQmlProperty &QQuickSimpleAction::property() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksimpleaction.html#property

    Returns
    -------

    QQmlProperty
      A new cute QQmlProperty around the copy Qt gave back. Python owns it.
    """
    #  const QQmlProperty &QQuickSimpleAction::property() const
    address = self.uglySide.call('ritual_ZNK18QQuickSimpleAction8propertyEv')
    from ..QtQml import QQmlProperty
    return QQmlProperty._cuteOwning(address)

  def value(self) -> QVariant:
    """
    Calls Qt's 'const QVariant &QQuickSimpleAction::value() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksimpleaction.html#value

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  const QVariant &QQuickSimpleAction::value() const
    address = self.uglySide.call('ritual_ZNK18QQuickSimpleAction5valueEv')
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def binding(self) -> QQmlAnyBinding:
    """
    Calls Qt's 'QQmlAnyBinding QQuickSimpleAction::binding() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksimpleaction.html#binding

    Returns
    -------

    QQmlAnyBinding
      A new cute QQmlAnyBinding around the copy Qt gave back. Python owns it.
    """
    #  QQmlAnyBinding QQuickSimpleAction::binding() const
    address = self.uglySide.call('ritual_ZNK18QQuickSimpleAction7bindingEv')
    from ..QtQml import QQmlAnyBinding
    return QQmlAnyBinding._cuteOwning(address)

  def specifiedObject(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QQuickSimpleAction::specifiedObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksimpleaction.html#specifiedObject

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QQuickSimpleAction::specifiedObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QQuickSimpleAction15specifiedObjectEv',
    )
    from ..QtCore import QObject
    return QObject._cuteAt(address)

  def specifiedProperty(self) -> str:
    """
    Calls Qt's 'const QString &QQuickSimpleAction::specifiedProperty()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksimpleaction.html#specifiedProperty

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  const QString &QQuickSimpleAction::specifiedProperty() const
    return self.uglySide.call(
        'ritual_ZNK18QQuickSimpleAction17specifiedPropertyEv',
    )

  def event(self) -> Optional[QQuickStateActionEvent]:
    """
    Calls Qt's 'QQuickStateActionEvent *QQuickSimpleAction::event() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksimpleaction.html#event

    Returns
    -------

    Optional[QQuickStateActionEvent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickStateActionEvent *QQuickSimpleAction::event() const
    address = self.uglySide.call('ritual_ZNK18QQuickSimpleAction5eventEv')
    from . import QQuickStateActionEvent
    return QQuickStateActionEvent._cuteAt(address)

  def reverseEvent(self) -> bool:
    """
    Calls Qt's 'bool QQuickSimpleAction::reverseEvent() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksimpleaction.html#reverseEvent
    """
    #  bool QQuickSimpleAction::reverseEvent() const
    return self.uglySide.call(
        'ritual_ZNK18QQuickSimpleAction12reverseEventEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQmlProperty)
  def setProperty(self, property: QQmlProperty) -> None:
    """
    Calls Qt's 'void QQuickSimpleAction::setProperty(const QQmlProperty
    &property)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksimpleaction.html#setProperty

    Parameters
    ----------

    property : QQmlProperty
      Passed on as a value: Qt reads the C++ QQmlProperty, which stays
      Python's own.
    """
    #  void QQuickSimpleAction::setProperty(const QQmlProperty &property)
    self.uglySide.call(
        'ritual_ZN18QQuickSimpleAction11setPropertyERK12QQmlProperty',
        self._valueOf(property),
    )

  @overload(QVariant)
  def setValue(self, value: QVariant) -> None:
    """
    Calls Qt's 'void QQuickSimpleAction::setValue(const QVariant &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksimpleaction.html#setValue

    Parameters
    ----------

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QQuickSimpleAction::setValue(const QVariant &value)
    self.uglySide.call(
        'ritual_ZN18QQuickSimpleAction8setValueERK8QVariant',
        self._valueOf(value),
    )

  @overload(QQmlAnyBinding)
  def setBinding(self, binding: QQmlAnyBinding) -> None:
    """
    Calls Qt's 'void QQuickSimpleAction::setBinding(QQmlAnyBinding binding)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksimpleaction.html#setBinding

    Parameters
    ----------

    binding : QQmlAnyBinding
      Passed on as a value: Qt reads the C++ QQmlAnyBinding, which stays
      Python's own.
    """
    #  void QQuickSimpleAction::setBinding(QQmlAnyBinding binding)
    self.uglySide.call(
        'ritual_ZN18QQuickSimpleAction10setBindingE14QQmlAnyBinding',
        self._valueOf(binding),
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

  @overload(QQuickStateAction)
  @overload(QQuickStateAction, State)
  def __init__(
      self,
      a: QQuickStateAction,
      state: State = State.StartState,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQuickSimpleAction::QQuickSimpleAction(const QQuickStateAction &a, State
    state)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksimpleaction.html#QQuickSimpleAction

    Parameters
    ----------

    a : QQuickStateAction
      Passed on as a value: Qt reads the C++ QQuickStateAction, which stays
      Python's own.

    state : State
      Passed on as its number. May be left out, as in Qt: it is then
      State.StartState.
    """
    #  QQuickSimpleAction::QQuickSimpleAction(const QQuickStateAction &a,
    #      State state)
    self._noteCreation(QQuickSimpleAction, lambda: Rituals.call(
        'ritual_ZN18QQuickSimpleActionC1ERK17QQuickStateActionNS_5StateE',
        self._valueOf(a), state.value,
    ))

  @overload(THIS)
  def __init__(self, other: QQuickSimpleAction) -> None:
    """
    Notes what was given, for Qt's
    'QQuickSimpleAction::QQuickSimpleAction(const QQuickSimpleAction
    &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksimpleaction.html#QQuickSimpleAction

    Parameters
    ----------

    other : QQuickSimpleAction
      Passed on as a value: Qt reads the C++ QQuickSimpleAction, which stays
      Python's own.
    """
    #  QQuickSimpleAction::QQuickSimpleAction(const QQuickSimpleAction
    #      &other)
    self._noteCreation(QQuickSimpleAction, lambda: Rituals.call(
        'ritual_ZN18QQuickSimpleActionC1ERKS_', self._valueOf(other),
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
