"""
QQmlInstantiationInterrupt binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlvme_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QQmlInstantiationInterrupt to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QDeadlineTimer
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDeadlineTimer = WAIT['QDeadlineTimer']


class QQmlInstantiationInterrupt(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlInstantiationInterrupt: a plain Python object
  standing in front of one C++ QQmlInstantiationInterrupt.

  C++ hands a QQmlInstantiationInterrupt around as a copy, so every C++
  QQmlInstantiationInterrupt behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QQmlInstantiationInterrupt that has a ritual and
  that Python can call so far, 1 name in all: 'shouldInterrupt'. It can be
  made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's
    'QQmlInstantiationInterrupt::QQmlInstantiationInterrupt(std::atomic<bool>
    *runWhile, QDeadlineTimer deadline)': names 'std::atomic<bool>', which
    has no cute class yet.
  - Qt's 'QQmlInstantiationInterrupt::~QQmlInstantiationInterrupt()': the
    destructor: Python removes its C++ QQmlInstantiationInterrupt by it, and
    has no other use for it.

  What to expect
  --------------

  - The C++ QQmlInstantiationInterrupt is created at the first use, not by
    'QQmlInstantiationInterrupt(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlInstantiationInterrupt back gives a copy the
    ritual made for Python, in a new cute QQmlInstantiationInterrupt.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlInstantiationInterrupt'

  #  Qt's '~QQmlInstantiationInterrupt()'. Naming it makes this a value
  #  class: Python owns every C++ QQmlInstantiationInterrupt behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN26QQmlInstantiationInterruptD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def shouldInterrupt(self) -> bool:
    """
    Calls Qt's 'bool QQmlInstantiationInterrupt::shouldInterrupt() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlinstantiationinterrupt.html#shouldInterrupt
    """
    #  bool QQmlInstantiationInterrupt::shouldInterrupt() const
    return self.uglySide.call(
        'ritual_ZNK26QQmlInstantiationInterrupt15shouldInterruptEv',
    )

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
    'QQmlInstantiationInterrupt::QQmlInstantiationInterrupt()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlinstantiationinterrupt.html
    """
    #  QQmlInstantiationInterrupt::QQmlInstantiationInterrupt()
    self._noteCreation(QQmlInstantiationInterrupt, lambda: Rituals.call(
        'ritual_ZN26QQmlInstantiationInterruptC1Ev',
    ))

  @overload(QDeadlineTimer)
  def __init__(self, deadline: QDeadlineTimer) -> None:
    """
    Notes what was given, for Qt's
    'QQmlInstantiationInterrupt::QQmlInstantiationInterrupt(QDeadlineTimer
    deadline)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlinstantiationinterrupt.html

    Parameters
    ----------

    deadline : QDeadlineTimer
      Passed on as a value: Qt reads the C++ QDeadlineTimer, which stays
      Python's own.
    """
    #  QQmlInstantiationInterrupt::QQmlInstantiationInterrupt(QDeadlineTimer
    #      deadline)
    self._noteCreation(QQmlInstantiationInterrupt, lambda: Rituals.call(
        'ritual_ZN26QQmlInstantiationInterruptC1E14QDeadlineTimer',
        self._valueOf(deadline),
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
