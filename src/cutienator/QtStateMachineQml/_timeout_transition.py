"""
TimeoutTransition binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtStateMachineQml/6.12.0/QtStateMachineQml/private/timeouttransition_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means TimeoutTransition to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtQml import QQmlParserStatus
from ..QtStateMachine import QSignalTransition

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


class TimeoutTransition(QSignalTransition, QQmlParserStatus):
  """
  The cute side of Qt's TimeoutTransition: a plain Python object standing in
  front of one C++ TimeoutTransition.

  It is built on the cute 'QSignalTransition', as Qt's TimeoutTransition is
  built on Qt's QSignalTransition, and has everything that class has. It is
  built on the cute 'QQmlParserStatus' as well, as Qt's TimeoutTransition is
  built on Qt's QQmlParserStatus too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's TimeoutTransition that has a ritual and that Python
  can call so far, 6 names in all: 'metaObject', 'tr', 'timeout',
  'setTimeout', 'classBegin', 'componentComplete'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *TimeoutTransition::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int TimeoutTransition::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'TimeoutTransition::~TimeoutTransition()': the destructor: Python
    never removes a C++ TimeoutTransition.
  - Qt's 'QBindable<int> TimeoutTransition::bindableTimeout()': gives a type
    Python has no way to take yet.

  What has no ritual
  ------------------

  2 of the 13 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ TimeoutTransition is created at the first use, not by
    'TimeoutTransition(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ TimeoutTransition.
  - Qt tells when it has removed the C++ TimeoutTransition. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's TimeoutTransition that has no cute function yet,
    'bindableTimeout', holds a function that raises 'NotImplementedError',
    and its docstring says why.
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
    Calls Qt's 'QString TimeoutTransition::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/timeouttransition.html#tr

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
    #  QString TimeoutTransition::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN17TimeoutTransition2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'TimeoutTransition'

  #  Qt's TimeoutTransition is built on more than one class. The part of a
  #  C++ TimeoutTransition that belongs to a class after the first begins
  #  somewhere inside the object, and the ritual named for that class gives
  #  where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QQmlParserStatus': 'ritual_cast_TimeoutTransition_QQmlParserStatus',
  }

  #  A C++ TimeoutTransition Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_TimeoutTransition'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *TimeoutTransition::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/timeouttransition.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *TimeoutTransition::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17TimeoutTransition10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def timeout(self) -> int:
    """
    Calls Qt's 'int TimeoutTransition::timeout() const'.

    Qt's own words: https://doc.qt.io/qt-6/timeouttransition.html#timeout
    """
    #  int TimeoutTransition::timeout() const
    return self.uglySide.call('ritual_ZNK17TimeoutTransition7timeoutEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setTimeout(self, timeout: int) -> None:
    """
    Calls Qt's 'void TimeoutTransition::setTimeout(int timeout)'.

    Qt's own words: https://doc.qt.io/qt-6/timeouttransition.html#setTimeout

    Parameters
    ----------

    timeout : int
      Passed on as it is.
    """
    #  void TimeoutTransition::setTimeout(int timeout)
    self.uglySide.call('ritual_ZN17TimeoutTransition10setTimeoutEi', timeout)

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
    Notes what was given, for Qt's
    'TimeoutTransition::TimeoutTransition(QState *parent)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/timeouttransition.html#TimeoutTransition

    Parameters
    ----------

    parent : Optional[QState]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  TimeoutTransition::TimeoutTransition(QState *parent)
    self._noteCreation(TimeoutTransition, lambda: Rituals.call(
        'ritual_ZN17TimeoutTransitionC1EP6QState', self._addressOf(parent),
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
    Calls Qt's 'void TimeoutTransition::classBegin()'.

    Qt's own words: https://doc.qt.io/qt-6/timeouttransition.html#classBegin
    """
    #  void TimeoutTransition::classBegin()
    ritual = 'ritual_ZN17TimeoutTransition10classBeginEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17TimeoutTransition10classBeginEv'
    self.uglySide.call(ritual)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void TimeoutTransition::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/timeouttransition.html#componentComplete
    """
    #  void TimeoutTransition::componentComplete()
    ritual = 'ritual_ZN17TimeoutTransition17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17TimeoutTransition17componentCompleteEv'
    self.uglySide.call(ritual)

  @staticmethod
  def bindableTimeout(*__, **_) -> Never:
    """
    Qt's 'QBindable<int> TimeoutTransition::bindableTimeout()': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'TimeoutTransition.bindableTimeout' has no cute function yet. Qt's "
        "'QBindable<int> TimeoutTransition::bindableTimeout()': gives a "
        "type Python has no way to take yet.")
