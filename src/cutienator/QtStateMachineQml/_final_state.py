"""
FinalState binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtStateMachineQml/6.12.0/QtStateMachineQml/private/finalstate_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means FinalState to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtStateMachine import QFinalState

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtStateMachine import QState
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QState = WAIT['QState']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class FinalState(QFinalState):
  """
  The cute side of Qt's FinalState: a plain Python object standing in front
  of one C++ FinalState.

  It is built on the cute 'QFinalState', as Qt's FinalState is built on Qt's
  QFinalState, and has everything that class has.

  What exists
  -----------

  Every function of Qt's FinalState that has a ritual and that Python can
  call so far, 5 names in all: 'metaObject', 'tr', 'childrenChanged',
  'childrenContentChanged', '_qt_property_m_childrenComputedProperty_offset'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *FinalState::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int FinalState::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QQmlListProperty<QObject> FinalState::children()': gives a type
    Python has no way to take yet.
  - Qt's 'QBindable<QQmlListProperty<QObject>> FinalState::bindableChildren()
    const': gives a type Python has no way to take yet.
  - Qt's 'QQmlListProperty<QObject> FinalState::childrenActualCalculation()
    const': gives a type Python has no way to take yet.

  What has no ritual
  ------------------

  2 of the 13 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ FinalState is created at the first use, not by 'FinalState(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ FinalState.
  - Qt tells when it has removed the C++ FinalState. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's FinalState that has no cute function yet,
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
    Calls Qt's 'QString FinalState::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/finalstate.html#tr

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
    #  QString FinalState::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN10FinalState2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def _qt_property_m_childrenComputedProperty_offset() -> int:
    """
    Calls Qt's 'size_t
    FinalState::_qt_property_m_childrenComputedProperty_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/finalstate.html
    """
    #  size_t FinalState::_qt_property_m_childrenComputedProperty_offset()
    return Rituals.call(
        'ritual_ZN10FinalState46_qt_property_m_childrenComputedProperty_off'
        'setEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'FinalState'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *FinalState::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/finalstate.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *FinalState::metaObject() const
    address = self.uglySide.call('ritual_ZNK10FinalState10metaObjectEv')
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
    Notes what was given, for Qt's 'FinalState::FinalState(QState *parent)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/finalstate.html#FinalState

    Parameters
    ----------

    parent : Optional[QState]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  FinalState::FinalState(QState *parent)
    self._noteCreation(FinalState, lambda: Rituals.call(
        'ritual_ZN10FinalStateC1EP6QState', self._addressOf(parent),
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

  def childrenChanged(self) -> None:
    """
    Calls Qt's 'void FinalState::childrenChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/finalstate.html#childrenChanged
    """
    #  void FinalState::childrenChanged()
    self.uglySide.call('ritual_ZN10FinalState15childrenChangedEv')

  def childrenContentChanged(self) -> None:
    """
    Calls Qt's 'void FinalState::childrenContentChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/finalstate.html#childrenContentChanged
    """
    #  void FinalState::childrenContentChanged()
    self.uglySide.call('ritual_ZN10FinalState22childrenContentChangedEv')

  @staticmethod
  def bindableChildren(*__, **_) -> Never:
    """
    Qt's 'QBindable<QQmlListProperty<QObject>> FinalState::bindableChildren()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'FinalState.bindableChildren' has no cute function yet. Qt's "
        "'QBindable<QQmlListProperty<QObject>> "
        "FinalState::bindableChildren() const': gives a type Python has no "
        "way to take yet.")

  @staticmethod
  def childrenActualCalculation(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QObject> FinalState::childrenActualCalculation()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'FinalState.childrenActualCalculation' has no cute function yet. "
        "Qt's 'QQmlListProperty<QObject> "
        "FinalState::childrenActualCalculation() const': gives a type "
        "Python has no way to take yet.")
