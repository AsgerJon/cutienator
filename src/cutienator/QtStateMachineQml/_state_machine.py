"""
StateMachine binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtStateMachineQml/6.12.0/QtStateMachineQml/private/statemachine_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means StateMachine to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QObject
from ..QtQml import QQmlParserStatus
from ..QtStateMachine import QStateMachine

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class StateMachine(QStateMachine, QQmlParserStatus):
  """
  The cute side of Qt's StateMachine: a plain Python object standing in front
  of one C++ StateMachine.

  It is built on the cute 'QStateMachine', as Qt's StateMachine is built on
  Qt's QStateMachine, and has everything that class has. It is built on the
  cute 'QQmlParserStatus' as well, as Qt's StateMachine is built on Qt's
  QQmlParserStatus too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's StateMachine that has a ritual and that Python can
  call so far, 11 names in all: 'metaObject', 'tr', 'classBegin',
  'componentComplete', 'isRunning', 'setRunning', 'checkChildMode',
  'childrenChanged', 'qmlRunningChanged', 'childrenContentChanged',
  '_qt_property_m_childrenComputedProperty_offset'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *StateMachine::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int StateMachine::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QQmlListProperty<QObject> StateMachine::children()': gives a type
    Python has no way to take yet.
  - Qt's 'QBindable<QQmlListProperty<QObject>>
    StateMachine::bindableChildren() const': gives a type Python has no way
    to take yet.
  - Qt's 'QQmlListProperty<QObject> StateMachine::childrenActualCalculation()
    const': gives a type Python has no way to take yet.

  What has no ritual
  ------------------

  2 of the 19 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ StateMachine is created at the first use, not by
    'StateMachine(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ StateMachine.
  - Qt tells when it has removed the C++ StateMachine. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's StateMachine that has no cute function yet,
    'bindableChildren', 'childrenActualCalculation', holds a function that
    raises 'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString StateMachine::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/statemachine.html#tr

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
    #  QString StateMachine::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN12StateMachine2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def _qt_property_m_childrenComputedProperty_offset() -> int:
    """
    Calls Qt's 'size_t
    StateMachine::_qt_property_m_childrenComputedProperty_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/statemachine.html
    """
    #  size_t StateMachine::_qt_property_m_childrenComputedProperty_offset()
    return Rituals.call(
        'ritual_ZN12StateMachine46_qt_property_m_childrenComputedProperty_o'
        'ffsetEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'StateMachine'

  #  Qt's StateMachine is built on more than one class. The part of a C++
  #  StateMachine that belongs to a class after the first begins somewhere
  #  inside the object, and the ritual named for that class gives where; see
  #  'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QQmlParserStatus': 'ritual_cast_StateMachine_QQmlParserStatus',
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
    Calls Qt's 'const QMetaObject *StateMachine::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/statemachine.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *StateMachine::metaObject() const
    address = self.uglySide.call('ritual_ZNK12StateMachine10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isRunning(self) -> bool:
    """
    Calls Qt's 'bool StateMachine::isRunning() const'.

    Qt's own words: https://doc.qt.io/qt-6/statemachine.html#isRunning
    """
    #  bool StateMachine::isRunning() const
    return self.uglySide.call('ritual_ZNK12StateMachine9isRunningEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setRunning(self, running: bool) -> None:
    """
    Calls Qt's 'void StateMachine::setRunning(bool running)'.

    Qt's own words: https://doc.qt.io/qt-6/statemachine.html#setRunning

    Parameters
    ----------

    running : bool
      Passed on as it is.
    """
    #  void StateMachine::setRunning(bool running)
    self.uglySide.call('ritual_ZN12StateMachine10setRunningEb', running)

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
    Notes what was given, for Qt's 'StateMachine::StateMachine(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/statemachine.html#StateMachine

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  StateMachine::StateMachine(QObject *parent)
    self._noteCreation(StateMachine, lambda: Rituals.call(
        'ritual_ZN12StateMachineC1EP7QObject',
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

  def classBegin(self) -> None:
    """
    Calls Qt's 'void StateMachine::classBegin()'.

    Qt's own words: https://doc.qt.io/qt-6/statemachine.html#classBegin
    """
    #  void StateMachine::classBegin()
    ritual = 'ritual_ZN12StateMachine10classBeginEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12StateMachine10classBeginEv'
    self.uglySide.call(ritual)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void StateMachine::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/statemachine.html#componentComplete
    """
    #  void StateMachine::componentComplete()
    ritual = 'ritual_ZN12StateMachine17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12StateMachine17componentCompleteEv'
    self.uglySide.call(ritual)

  def checkChildMode(self) -> None:
    """
    Calls Qt's 'void StateMachine::checkChildMode()'.

    Qt's own words: https://doc.qt.io/qt-6/statemachine.html#checkChildMode
    """
    #  void StateMachine::checkChildMode()
    self.uglySide.call('ritual_ZN12StateMachine14checkChildModeEv')

  def childrenChanged(self) -> None:
    """
    Calls Qt's 'void StateMachine::childrenChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/statemachine.html#childrenChanged
    """
    #  void StateMachine::childrenChanged()
    self.uglySide.call('ritual_ZN12StateMachine15childrenChangedEv')

  def qmlRunningChanged(self) -> None:
    """
    Calls Qt's 'void StateMachine::qmlRunningChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/statemachine.html#qmlRunningChanged
    """
    #  void StateMachine::qmlRunningChanged()
    self.uglySide.call('ritual_ZN12StateMachine17qmlRunningChangedEv')

  def childrenContentChanged(self) -> None:
    """
    Calls Qt's 'void StateMachine::childrenContentChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/statemachine.html#childrenContentChanged
    """
    #  void StateMachine::childrenContentChanged()
    self.uglySide.call('ritual_ZN12StateMachine22childrenContentChangedEv')

  @staticmethod
  def bindableChildren(*__, **_) -> Never:
    """
    Qt's 'QBindable<QQmlListProperty<QObject>>
    StateMachine::bindableChildren() const': gives a type Python has no way
    to take yet.
    """
    raise NotImplementedError(
        "'StateMachine.bindableChildren' has no cute function yet. Qt's "
        "'QBindable<QQmlListProperty<QObject>> "
        "StateMachine::bindableChildren() const': gives a type Python has "
        "no way to take yet.")

  @staticmethod
  def childrenActualCalculation(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QObject> StateMachine::childrenActualCalculation()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'StateMachine.childrenActualCalculation' has no cute function yet. "
        "Qt's 'QQmlListProperty<QObject> "
        "StateMachine::childrenActualCalculation() const': gives a type "
        "Python has no way to take yet.")
