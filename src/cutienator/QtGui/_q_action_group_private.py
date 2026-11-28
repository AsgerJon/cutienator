"""
QActionGroupPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qactiongroup_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QActionGroupPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObjectPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QAction, QActionGroup
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAction = WAIT['QAction']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QActionGroupPrivate(QObjectPrivate):
  """
  The cute side of Qt's QActionGroupPrivate: a plain Python object standing
  in front of one C++ QActionGroupPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's QActionGroupPrivate is
  built on Qt's QObjectPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QActionGroupPrivate that has a ritual and that
  Python can call so far, 2 names in all: 'q_func', 'emitSignal'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QActionGroup *QActionGroupPrivate::q_func() const': takes in
    Python what 'QActionGroup *QActionGroupPrivate::q_func()' takes.
  - Qt's 'QActionGroupPrivate::~QActionGroupPrivate()': the destructor:
    Python never removes a C++ QActionGroupPrivate.

  What has no ritual
  ------------------

  3 of the 8 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QActionGroupPrivate is created at the first use, not by
    'QActionGroupPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QActionGroupPrivate.
  """

  #  The enums Qt writes inside QActionGroupPrivate, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class Signal(CuteNum):
    """
    The enum 'QActionGroupPrivate::Signal' of Qt, with the 2 names Qt gives
    in it.
    """

    Triggered = Kee[int](0)
    Hovered = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QActionGroupPrivate'

  #  A C++ QActionGroupPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QActionGroupPrivate'

  #  The functions Qt calls itself that QActionGroupPrivate is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'emitSignal': (
          ('_ZN19QActionGroupPrivate10emitSignalENS_6SignalEP7QAction',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum', 'QtGui:QActionGroupPrivate.Signal'),
               ('address', 'address', 'QtGui:QAction'),
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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QActionGroupPrivate::QActionGroupPrivate()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qactiongroupprivate.html#QActionGroupPrivate
    """
    #  QActionGroupPrivate::QActionGroupPrivate()
    self._noteCreation(QActionGroupPrivate, lambda: Rituals.call(
        'ritual_ZN19QActionGroupPrivateC1Ev',
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

  def q_func(self) -> Optional[QActionGroup]:
    """
    Calls Qt's 'QActionGroup *QActionGroupPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qactiongroupprivate.html#q_func

    Returns
    -------

    Optional[QActionGroup]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QActionGroup *QActionGroupPrivate::q_func()
    address = self.uglySide.call('ritual_ZN19QActionGroupPrivate6q_funcEv')
    from . import QActionGroup
    return QActionGroup._cuteAt(address)

  @overload(Signal, QAction)
  @overload(Signal, NoneType)
  def emitSignal(self, a0: Signal, a1: Optional[QAction]) -> None:
    """
    Calls Qt's 'void QActionGroupPrivate::emitSignal(Signal a0, QAction
    *a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qactiongroupprivate.html#emitSignal

    Parameters
    ----------

    a0 : Signal
      Passed on as its number.

    a1 : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QActionGroupPrivate::emitSignal(Signal a0, QAction *a1)
    ritual = (
        'ritual_ZN19QActionGroupPrivate10emitSignalENS_6SignalEP7QAction')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QActionGroupPrivate10emitSignalENS_6SignalEP7QAct'
          'ion')
    self.uglySide.call(ritual, a0.value, self._addressOf(a1))
