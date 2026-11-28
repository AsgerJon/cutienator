"""
State binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtStateMachineQml/6.12.0/QtStateMachineQml/private/state_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means State to be private: it declares the class in a header it calls
#  private. cutienator does not care. Qt hands objects of the class out all
#  the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtQml import QQmlParserStatus
from ..QtStateMachine import QState

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class State(QState, QQmlParserStatus):
  """
  The cute side of Qt's State: a plain Python object standing in front of one
  C++ State.

  It is built on the cute 'QState', as Qt's State is built on Qt's QState,
  and has everything that class has. It is built on the cute
  'QQmlParserStatus' as well, as Qt's State is built on Qt's QQmlParserStatus
  too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's State that has a ritual and that Python can call so
  far, 7 names in all: 'metaObject', 'tr', 'classBegin', 'componentComplete',
  'childrenChanged', 'childrenContentChanged',
  '_qt_property_m_childrenComputedProperty_offset'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *State::qt_metacast(const char *a0)': one of Qt's own inner
    workings.
  - Qt's 'int State::qt_metacall(QMetaObject::Call a0, int a1, void **a2)':
    one of Qt's own inner workings.
  - Qt's 'QQmlListProperty<QObject> State::children()': gives a type Python
    has no way to take yet.
  - Qt's 'QBindable<QQmlListProperty<QObject>> State::bindableChildren()
    const': gives a type Python has no way to take yet.
  - Qt's 'QQmlListProperty<QObject> State::childrenActualCalculation()
    const': gives a type Python has no way to take yet.

  What has no ritual
  ------------------

  2 of the 15 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ State is created at the first use, not by 'State(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ State.
  - Qt tells when it has removed the C++ State. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's State that has no cute function yet,
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
    Calls Qt's 'QString State::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/state.html#tr

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
    #  QString State::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN5State2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def _qt_property_m_childrenComputedProperty_offset() -> int:
    """
    Calls Qt's 'size_t
    State::_qt_property_m_childrenComputedProperty_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/state.html
    """
    #  size_t State::_qt_property_m_childrenComputedProperty_offset()
    return Rituals.call(
        'ritual_ZN5State46_qt_property_m_childrenComputedProperty_offsetEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'State'

  #  Qt's State is built on more than one class. The part of a C++ State that
  #  belongs to a class after the first begins somewhere inside the object,
  #  and the ritual named for that class gives where; see
  #  'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QQmlParserStatus': 'ritual_cast_State_QQmlParserStatus',
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
    Calls Qt's 'const QMetaObject *State::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/state.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *State::metaObject() const
    address = self.uglySide.call('ritual_ZNK5State10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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
  @overload(QState)
  @overload(NoneType)
  def __init__(self, parent: Optional[QState] = None) -> None:
    """
    Notes what was given, for Qt's 'State::State(QState *parent)', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/state.html#State

    Parameters
    ----------

    parent : Optional[QState]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  State::State(QState *parent)
    self._noteCreation(State, lambda: Rituals.call(
        'ritual_ZN5StateC1EP6QState', self._addressOf(parent),
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
    Calls Qt's 'void State::classBegin()'.

    Qt's own words: https://doc.qt.io/qt-6/state.html#classBegin
    """
    #  void State::classBegin()
    ritual = 'ritual_ZN5State10classBeginEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN5State10classBeginEv'
    self.uglySide.call(ritual)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void State::componentComplete()'.

    Qt's own words: https://doc.qt.io/qt-6/state.html#componentComplete
    """
    #  void State::componentComplete()
    ritual = 'ritual_ZN5State17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN5State17componentCompleteEv'
    self.uglySide.call(ritual)

  def childrenChanged(self) -> None:
    """
    Calls Qt's 'void State::childrenChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/state.html#childrenChanged
    """
    #  void State::childrenChanged()
    self.uglySide.call('ritual_ZN5State15childrenChangedEv')

  def childrenContentChanged(self) -> None:
    """
    Calls Qt's 'void State::childrenContentChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/state.html#childrenContentChanged
    """
    #  void State::childrenContentChanged()
    self.uglySide.call('ritual_ZN5State22childrenContentChangedEv')

  @staticmethod
  def bindableChildren(*__, **_) -> Never:
    """
    Qt's 'QBindable<QQmlListProperty<QObject>> State::bindableChildren()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'State.bindableChildren' has no cute function yet. Qt's "
        "'QBindable<QQmlListProperty<QObject>> State::bindableChildren() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def childrenActualCalculation(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QObject> State::childrenActualCalculation()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'State.childrenActualCalculation' has no cute function yet. Qt's "
        "'QQmlListProperty<QObject> State::childrenActualCalculation() "
        "const': gives a type Python has no way to take yet.")
