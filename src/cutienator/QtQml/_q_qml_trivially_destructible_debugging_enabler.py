"""
QQmlTriviallyDestructibleDebuggingEnabler binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/qqmldebug.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals


class QQmlTriviallyDestructibleDebuggingEnabler(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlTriviallyDestructibleDebuggingEnabler: a plain
  Python object standing in front of one C++
  QQmlTriviallyDestructibleDebuggingEnabler.

  C++ hands a QQmlTriviallyDestructibleDebuggingEnabler around as a copy, so
  every C++ QQmlTriviallyDestructibleDebuggingEnabler behind a cute one is
  Python's own: it is removed, by the ritual named in '__delete_ritual__',
  when the cute object goes.

  What exists
  -----------

  No function of Qt's QQmlTriviallyDestructibleDebuggingEnabler yet. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlTriviallyDestructibleDebuggingEnabler::
    ~QQmlTriviallyDestructibleDebuggingEnabler()': the destructor: Python
    removes its C++ QQmlTriviallyDestructibleDebuggingEnabler by it, and has
    no other use for it.

  What to expect
  --------------

  - The C++ QQmlTriviallyDestructibleDebuggingEnabler is created at the first
    use, not by 'QQmlTriviallyDestructibleDebuggingEnabler(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlTriviallyDestructibleDebuggingEnabler back gives
    a copy the ritual made for Python, in a new cute
    QQmlTriviallyDestructibleDebuggingEnabler.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlTriviallyDestructibleDebuggingEnabler'

  #  Qt's '~QQmlTriviallyDestructibleDebuggingEnabler()'. Naming it makes
  #  this a value class: Python owns every C++
  #  QQmlTriviallyDestructibleDebuggingEnabler behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = (
      'ritual_ZN12_GLOBAL__N_141QQmlTriviallyDestructibleDebuggingEnablerD1Ev')

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
  @overload(bool)
  def __init__(self, printWarning: bool = True) -> None:
    """
    Notes what was given, for Qt's
    'QQmlTriviallyDestructibleDebuggingEnabler::
    QQmlTriviallyDestructibleDebuggingEnabler(bool printWarning)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltriviallydestructibledebuggingenabler.html

    Parameters
    ----------

    printWarning : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  QQmlTriviallyDestructibleDebuggingEnabler::
    #      QQmlTriviallyDestructibleDebuggingEnabler(bool printWarning)
    self._noteCreation(
        QQmlTriviallyDestructibleDebuggingEnabler, lambda: Rituals.call(
            'ritual_ZN12_GLOBAL__N_141QQmlTriviallyDestructibleDebuggingEna'
            'blerC1Eb',
            printWarning,
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
