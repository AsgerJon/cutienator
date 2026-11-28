"""
QWebEngineFindTextResult binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWebEngineCore/qwebenginefindtextresult.h, Qt 6.12.0. Changes made here
#  are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals


class QWebEngineFindTextResult(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QWebEngineFindTextResult: a plain Python object
  standing in front of one C++ QWebEngineFindTextResult.

  C++ hands a QWebEngineFindTextResult around as a copy, so every C++
  QWebEngineFindTextResult behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QWebEngineFindTextResult that has a ritual and that
  Python can call so far, 2 names in all: 'numberOfMatches', 'activeMatch'.
  It can be made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QWebEngineFindTextResult &QWebEngineFindTextResult::operator=(const
    QWebEngineFindTextResult &other)': assignment: Python binds a name and
    has no operator for it.
  - Qt's 'QWebEngineFindTextResult::~QWebEngineFindTextResult()': the
    destructor: Python removes its C++ QWebEngineFindTextResult by it, and
    has no other use for it.

  What has no ritual
  ------------------

  3 of the 10 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QWebEngineFindTextResult is created at the first use, not by
    'QWebEngineFindTextResult(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QWebEngineFindTextResult back gives a copy the ritual
    made for Python, in a new cute QWebEngineFindTextResult.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWebEngineFindTextResult'

  #  Qt's '~QWebEngineFindTextResult()'. Naming it makes this a value class:
  #  Python owns every C++ QWebEngineFindTextResult behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN24QWebEngineFindTextResultD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def numberOfMatches(self) -> int:
    """
    Calls Qt's 'int QWebEngineFindTextResult::numberOfMatches() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginefindtextresult.html#numberOfMatches
    """
    #  int QWebEngineFindTextResult::numberOfMatches() const
    return self.uglySide.call(
        'ritual_ZNK24QWebEngineFindTextResult15numberOfMatchesEv',
    )

  def activeMatch(self) -> int:
    """
    Calls Qt's 'int QWebEngineFindTextResult::activeMatch() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginefindtextresult.html#activeMatch
    """
    #  int QWebEngineFindTextResult::activeMatch() const
    return self.uglySide.call(
        'ritual_ZNK24QWebEngineFindTextResult11activeMatchEv',
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
    'QWebEngineFindTextResult::QWebEngineFindTextResult()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginefindtextresult.html
    """
    #  QWebEngineFindTextResult::QWebEngineFindTextResult()
    self._noteCreation(QWebEngineFindTextResult, lambda: Rituals.call(
        'ritual_ZN24QWebEngineFindTextResultC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QWebEngineFindTextResult) -> None:
    """
    Notes what was given, for Qt's
    'QWebEngineFindTextResult::QWebEngineFindTextResult(const
    QWebEngineFindTextResult &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginefindtextresult.html

    Parameters
    ----------

    other : QWebEngineFindTextResult
      Passed on as a value: Qt reads the C++ QWebEngineFindTextResult, which
      stays Python's own.
    """
    #  QWebEngineFindTextResult::QWebEngineFindTextResult(const
    #      QWebEngineFindTextResult &other)
    self._noteCreation(QWebEngineFindTextResult, lambda: Rituals.call(
        'ritual_ZN24QWebEngineFindTextResultC1ERKS_', self._valueOf(other),
    ))

  @overload(int, int)
  def __init__(self, numberOfMatches: int, activeMatch: int) -> None:
    """
    Notes what was given, for Qt's
    'QWebEngineFindTextResult::QWebEngineFindTextResult(int numberOfMatches,
    int activeMatch)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginefindtextresult.html

    Parameters
    ----------

    numberOfMatches : int
      Passed on as it is.

    activeMatch : int
      Passed on as it is.
    """
    #  QWebEngineFindTextResult::QWebEngineFindTextResult(int
    #      numberOfMatches, int activeMatch)
    self._noteCreation(QWebEngineFindTextResult, lambda: Rituals.call(
        'ritual_ZN24QWebEngineFindTextResultC1Eii',
        numberOfMatches, activeMatch,
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
