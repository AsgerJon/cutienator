"""
QMarginsF binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qmargins.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from . import QMargins
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMargins = WAIT['QMargins']


class QMarginsF(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QMarginsF: a plain Python object standing in front of
  one C++ QMarginsF.

  C++ hands a QMarginsF around as a copy, so every C++ QMarginsF behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QMarginsF that has a ritual and that Python can call
  so far, 10 names in all: 'isNull', 'left', 'top', 'right', 'bottom',
  'setLeft', 'setTop', 'setRight', 'setBottom', 'toMargins'. It can be made
  from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QMarginsF::~QMarginsF()': the destructor: Python removes its C++
    QMarginsF by it, and has no other use for it.

  What has no ritual
  ------------------

  6 of the 20 functions Qt declares: 6 takes or gives a type that cannot be
  passed yet.

  What to expect
  --------------

  - The C++ QMarginsF is created at the first use, not by 'QMarginsF(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QMarginsF back gives a copy the ritual made for
    Python, in a new cute QMarginsF.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QMarginsF'

  #  Qt's '~QMarginsF()'. Naming it makes this a value class: Python owns
  #  every C++ QMarginsF behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN9QMarginsFD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QMarginsF::isNull() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmarginsf.html#isNull
    """
    #  bool QMarginsF::isNull() const
    return self.uglySide.call('ritual_ZNK9QMarginsF6isNullEv')

  def left(self) -> float:
    """
    Calls Qt's 'qreal QMarginsF::left() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmarginsf.html#left
    """
    #  qreal QMarginsF::left() const
    return self.uglySide.call('ritual_ZNK9QMarginsF4leftEv')

  def top(self) -> float:
    """
    Calls Qt's 'qreal QMarginsF::top() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmarginsf.html#top
    """
    #  qreal QMarginsF::top() const
    return self.uglySide.call('ritual_ZNK9QMarginsF3topEv')

  def right(self) -> float:
    """
    Calls Qt's 'qreal QMarginsF::right() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmarginsf.html#right
    """
    #  qreal QMarginsF::right() const
    return self.uglySide.call('ritual_ZNK9QMarginsF5rightEv')

  def bottom(self) -> float:
    """
    Calls Qt's 'qreal QMarginsF::bottom() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmarginsf.html#bottom
    """
    #  qreal QMarginsF::bottom() const
    return self.uglySide.call('ritual_ZNK9QMarginsF6bottomEv')

  def toMargins(self) -> QMargins:
    """
    Calls Qt's 'QMargins QMarginsF::toMargins() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmarginsf.html#toMargins

    Returns
    -------

    QMargins
      A new cute QMargins around the copy Qt gave back. Python owns it.
    """
    #  QMargins QMarginsF::toMargins() const
    address = self.uglySide.call('ritual_ZNK9QMarginsF9toMarginsEv')
    from . import QMargins
    return QMargins._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setLeft(self, aleft: float) -> None:
    """
    Calls Qt's 'void QMarginsF::setLeft(qreal aleft)'.

    Qt's own words: https://doc.qt.io/qt-6/qmarginsf.html#setLeft

    Parameters
    ----------

    aleft : float
      Passed on as it is.
    """
    #  void QMarginsF::setLeft(qreal aleft)
    self.uglySide.call('ritual_ZN9QMarginsF7setLeftEd', aleft)

  @overload(float)
  def setTop(self, atop: float) -> None:
    """
    Calls Qt's 'void QMarginsF::setTop(qreal atop)'.

    Qt's own words: https://doc.qt.io/qt-6/qmarginsf.html#setTop

    Parameters
    ----------

    atop : float
      Passed on as it is.
    """
    #  void QMarginsF::setTop(qreal atop)
    self.uglySide.call('ritual_ZN9QMarginsF6setTopEd', atop)

  @overload(float)
  def setRight(self, aright: float) -> None:
    """
    Calls Qt's 'void QMarginsF::setRight(qreal aright)'.

    Qt's own words: https://doc.qt.io/qt-6/qmarginsf.html#setRight

    Parameters
    ----------

    aright : float
      Passed on as it is.
    """
    #  void QMarginsF::setRight(qreal aright)
    self.uglySide.call('ritual_ZN9QMarginsF8setRightEd', aright)

  @overload(float)
  def setBottom(self, abottom: float) -> None:
    """
    Calls Qt's 'void QMarginsF::setBottom(qreal abottom)'.

    Qt's own words: https://doc.qt.io/qt-6/qmarginsf.html#setBottom

    Parameters
    ----------

    abottom : float
      Passed on as it is.
    """
    #  void QMarginsF::setBottom(qreal abottom)
    self.uglySide.call('ritual_ZN9QMarginsF9setBottomEd', abottom)

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
    Notes what was given, for Qt's 'QMarginsF::QMarginsF()', which is called
    at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qmarginsf.html#QMarginsF
    """
    #  QMarginsF::QMarginsF()
    self._noteCreation(QMarginsF, lambda: Rituals.call(
        'ritual_ZN9QMarginsFC1Ev',
    ))

  @overload(float, float, float, float)
  def __init__(
      self,
      left: float,
      top: float,
      right: float,
      bottom: float,
  ) -> None:
    """
    Notes what was given, for Qt's 'QMarginsF::QMarginsF(qreal left, qreal
    top, qreal right, qreal bottom)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qmarginsf.html#QMarginsF

    Parameters
    ----------

    left : float
      Passed on as it is.

    top : float
      Passed on as it is.

    right : float
      Passed on as it is.

    bottom : float
      Passed on as it is.
    """
    #  QMarginsF::QMarginsF(qreal left, qreal top, qreal right, qreal bottom)
    self._noteCreation(QMarginsF, lambda: Rituals.call(
        'ritual_ZN9QMarginsFC1Edddd', left, top, right, bottom,
    ))

  @overload(QMargins)
  def __init__(self, margins: QMargins) -> None:
    """
    Notes what was given, for Qt's 'QMarginsF::QMarginsF(const QMargins
    &margins)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qmarginsf.html#QMarginsF

    Parameters
    ----------

    margins : QMargins
      Passed on as a value: Qt reads the C++ QMargins, which stays Python's
      own.
    """
    #  QMarginsF::QMarginsF(const QMargins &margins)
    self._noteCreation(QMarginsF, lambda: Rituals.call(
        'ritual_ZN9QMarginsFC1ERK8QMargins', self._valueOf(margins),
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
