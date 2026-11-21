"""
QMargins binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qmargins.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from . import QMarginsF


class QMargins(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QMargins: a plain Python object standing in front of
  one C++ QMargins.

  C++ hands a QMargins around as a copy, so every C++ QMargins behind a cute
  one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QMargins that has a ritual and that Python can call
  so far, 10 names in all: 'isNull', 'left', 'top', 'right', 'bottom',
  'setLeft', 'setTop', 'setRight', 'setBottom', 'toMarginsF'. It can be made
  from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QMargins::~QMargins()': the destructor: Python removes its C++
    QMargins by it, and has no other use for it.

  What has no ritual
  ------------------

  9 of the 22 functions Qt declares: 8 takes or gives a type that cannot be
  passed yet; 1 private.

  What to expect
  --------------

  - The C++ QMargins is created at the first use, not by 'QMargins(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QMargins back gives a copy the ritual made for
    Python, in a new cute QMargins.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QMargins'

  #  Qt's '~QMargins()'. Naming it makes this a value class: Python owns
  #  every C++ QMargins behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN8QMarginsD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QMargins::isNull() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmargins.html#isNull
    """
    #  bool QMargins::isNull() const
    return self.uglySide.call('ritual_ZNK8QMargins6isNullEv')

  def left(self) -> int:
    """
    Calls Qt's 'int QMargins::left() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmargins.html#left
    """
    #  int QMargins::left() const
    return self.uglySide.call('ritual_ZNK8QMargins4leftEv')

  def top(self) -> int:
    """
    Calls Qt's 'int QMargins::top() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmargins.html#top
    """
    #  int QMargins::top() const
    return self.uglySide.call('ritual_ZNK8QMargins3topEv')

  def right(self) -> int:
    """
    Calls Qt's 'int QMargins::right() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmargins.html#right
    """
    #  int QMargins::right() const
    return self.uglySide.call('ritual_ZNK8QMargins5rightEv')

  def bottom(self) -> int:
    """
    Calls Qt's 'int QMargins::bottom() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmargins.html#bottom
    """
    #  int QMargins::bottom() const
    return self.uglySide.call('ritual_ZNK8QMargins6bottomEv')

  def toMarginsF(self) -> QMarginsF:
    """
    Calls Qt's 'QMarginsF QMargins::toMarginsF() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmargins.html#toMarginsF

    Returns
    -------

    QMarginsF
      A new cute QMarginsF around the copy Qt gave back. Python owns it.
    """
    #  QMarginsF QMargins::toMarginsF() const
    address = self.uglySide.call('ritual_ZNK8QMargins10toMarginsFEv')
    from . import QMarginsF
    return QMarginsF._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setLeft(self, left: int) -> None:
    """
    Calls Qt's 'void QMargins::setLeft(int left)'.

    Qt's own words: https://doc.qt.io/qt-6/qmargins.html#setLeft

    Parameters
    ----------

    left : int
      Passed on as it is.
    """
    #  void QMargins::setLeft(int left)
    self.uglySide.call('ritual_ZN8QMargins7setLeftEi', left)

  @overload(int)
  def setTop(self, top: int) -> None:
    """
    Calls Qt's 'void QMargins::setTop(int top)'.

    Qt's own words: https://doc.qt.io/qt-6/qmargins.html#setTop

    Parameters
    ----------

    top : int
      Passed on as it is.
    """
    #  void QMargins::setTop(int top)
    self.uglySide.call('ritual_ZN8QMargins6setTopEi', top)

  @overload(int)
  def setRight(self, right: int) -> None:
    """
    Calls Qt's 'void QMargins::setRight(int right)'.

    Qt's own words: https://doc.qt.io/qt-6/qmargins.html#setRight

    Parameters
    ----------

    right : int
      Passed on as it is.
    """
    #  void QMargins::setRight(int right)
    self.uglySide.call('ritual_ZN8QMargins8setRightEi', right)

  @overload(int)
  def setBottom(self, bottom: int) -> None:
    """
    Calls Qt's 'void QMargins::setBottom(int bottom)'.

    Qt's own words: https://doc.qt.io/qt-6/qmargins.html#setBottom

    Parameters
    ----------

    bottom : int
      Passed on as it is.
    """
    #  void QMargins::setBottom(int bottom)
    self.uglySide.call('ritual_ZN8QMargins9setBottomEi', bottom)

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
    Notes what was given, for Qt's 'QMargins::QMargins()', which is called at
    the first use.

    Qt's own words: https://doc.qt.io/qt-6/qmargins.html#QMargins
    """
    #  QMargins::QMargins()
    self._noteCreation(QMargins, lambda: Rituals.call(
        'ritual_ZN8QMarginsC1Ev',
    ))

  @overload(int, int, int, int)
  def __init__(self, left: int, top: int, right: int, bottom: int) -> None:
    """
    Notes what was given, for Qt's 'QMargins::QMargins(int left, int top, int
    right, int bottom)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qmargins.html#QMargins

    Parameters
    ----------

    left : int
      Passed on as it is.

    top : int
      Passed on as it is.

    right : int
      Passed on as it is.

    bottom : int
      Passed on as it is.
    """
    #  QMargins::QMargins(int left, int top, int right, int bottom)
    self._noteCreation(QMargins, lambda: Rituals.call(
        'ritual_ZN8QMarginsC1Eiiii', left, top, right, bottom,
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
