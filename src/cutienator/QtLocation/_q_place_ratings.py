"""
QPlaceRatings binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/qplaceratings.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QPlaceRatings(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QPlaceRatings: a plain Python object standing in
  front of one C++ QPlaceRatings.

  C++ hands a QPlaceRatings around as a copy, so every C++ QPlaceRatings
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QPlaceRatings that has a ritual and that Python can
  call so far, 10 names in all: '__eq__', '__ne__', 'average', 'setAverage',
  'count', 'setCount', 'maximum', 'setMaximum', 'isEmpty', 'isEqual'. It can
  be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPlaceRatings::QPlaceRatings(QPlaceRatings &&other)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QPlaceRatings::~QPlaceRatings()': the destructor: Python removes
    its C++ QPlaceRatings by it, and has no other use for it.
  - Qt's 'QPlaceRatings &QPlaceRatings::operator=(const QPlaceRatings
    &other)': assignment: Python binds a name and has no operator for it.
  - Qt's 'QPlaceRatings &QPlaceRatings::operator=(QPlaceRatings &&other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'void QPlaceRatings::swap(QPlaceRatings &other)': takes a type
    Python has no way to hand over yet.

  What has no ritual
  ------------------

  3 of the 20 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QPlaceRatings is created at the first use, not by
    'QPlaceRatings(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QPlaceRatings back gives a copy the ritual made for
    Python, in a new cute QPlaceRatings.
  - Each name of Qt's QPlaceRatings that has no cute function yet, 'swap',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPlaceRatings'

  #  Qt's '~QPlaceRatings()'. Naming it makes this a value class: Python owns
  #  every C++ QPlaceRatings behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN13QPlaceRatingsD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def average(self) -> float:
    """
    Calls Qt's 'qreal QPlaceRatings::average() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplaceratings.html#average
    """
    #  qreal QPlaceRatings::average() const
    return self.uglySide.call('ritual_ZNK13QPlaceRatings7averageEv')

  def count(self) -> int:
    """
    Calls Qt's 'int QPlaceRatings::count() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplaceratings.html#count
    """
    #  int QPlaceRatings::count() const
    return self.uglySide.call('ritual_ZNK13QPlaceRatings5countEv')

  def maximum(self) -> float:
    """
    Calls Qt's 'qreal QPlaceRatings::maximum() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplaceratings.html#maximum
    """
    #  qreal QPlaceRatings::maximum() const
    return self.uglySide.call('ritual_ZNK13QPlaceRatings7maximumEv')

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QPlaceRatings::isEmpty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplaceratings.html#isEmpty
    """
    #  bool QPlaceRatings::isEmpty() const
    return self.uglySide.call('ritual_ZNK13QPlaceRatings7isEmptyEv')

  @overload(THIS)
  def isEqual(self, other: QPlaceRatings) -> bool:
    """
    Calls Qt's 'bool QPlaceRatings::isEqual(const QPlaceRatings &other)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qplaceratings.html#isEqual

    Parameters
    ----------

    other : QPlaceRatings
      Passed on as a value: Qt reads the C++ QPlaceRatings, which stays
      Python's own.
    """
    #  bool QPlaceRatings::isEqual(const QPlaceRatings &other) const
    return self.uglySide.call(
        'ritual_ZNK13QPlaceRatings7isEqualERKS_', self._valueOf(other),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setAverage(self, average: float) -> None:
    """
    Calls Qt's 'void QPlaceRatings::setAverage(qreal average)'.

    Qt's own words: https://doc.qt.io/qt-6/qplaceratings.html#setAverage

    Parameters
    ----------

    average : float
      Passed on as it is.
    """
    #  void QPlaceRatings::setAverage(qreal average)
    self.uglySide.call('ritual_ZN13QPlaceRatings10setAverageEd', average)

  @overload(int)
  def setCount(self, count: int) -> None:
    """
    Calls Qt's 'void QPlaceRatings::setCount(int count)'.

    Qt's own words: https://doc.qt.io/qt-6/qplaceratings.html#setCount

    Parameters
    ----------

    count : int
      Passed on as it is.
    """
    #  void QPlaceRatings::setCount(int count)
    self.uglySide.call('ritual_ZN13QPlaceRatings8setCountEi', count)

  @overload(float)
  def setMaximum(self, max: float) -> None:
    """
    Calls Qt's 'void QPlaceRatings::setMaximum(qreal max)'.

    Qt's own words: https://doc.qt.io/qt-6/qplaceratings.html#setMaximum

    Parameters
    ----------

    max : float
      Passed on as it is.
    """
    #  void QPlaceRatings::setMaximum(qreal max)
    self.uglySide.call('ritual_ZN13QPlaceRatings10setMaximumEd', max)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QPlaceRatings) -> bool:
    """
    Calls Qt's 'bool operator==(const QPlaceRatings &lhs, const QPlaceRatings
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qplaceratings.html#operator==

    Parameters
    ----------

    rhs : QPlaceRatings
      Passed on as a value: Qt reads the C++ QPlaceRatings, which stays
      Python's own.
    """
    #  bool operator==(const QPlaceRatings &lhs, const QPlaceRatings &rhs)
    return Rituals.call(
        'ritual_ZeqRK13QPlaceRatingsS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(self, rhs: QPlaceRatings) -> bool:
    """
    Calls Qt's 'bool operator!=(const QPlaceRatings &lhs, const QPlaceRatings
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qplaceratings.html#operator!=

    Parameters
    ----------

    rhs : QPlaceRatings
      Passed on as a value: Qt reads the C++ QPlaceRatings, which stays
      Python's own.
    """
    #  bool operator!=(const QPlaceRatings &lhs, const QPlaceRatings &rhs)
    return Rituals.call(
        'ritual_ZneRK13QPlaceRatingsS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QPlaceRatings::QPlaceRatings()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qplaceratings.html#QPlaceRatings
    """
    #  QPlaceRatings::QPlaceRatings()
    self._noteCreation(QPlaceRatings, lambda: Rituals.call(
        'ritual_ZN13QPlaceRatingsC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QPlaceRatings) -> None:
    """
    Notes what was given, for Qt's 'QPlaceRatings::QPlaceRatings(const
    QPlaceRatings &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qplaceratings.html#QPlaceRatings

    Parameters
    ----------

    other : QPlaceRatings
      Passed on as a value: Qt reads the C++ QPlaceRatings, which stays
      Python's own.
    """
    #  QPlaceRatings::QPlaceRatings(const QPlaceRatings &other)
    self._noteCreation(QPlaceRatings, lambda: Rituals.call(
        'ritual_ZN13QPlaceRatingsC1ERKS_', self._valueOf(other),
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

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QPlaceRatings::swap(QPlaceRatings &other)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QPlaceRatings.swap' has no cute function yet. Qt's 'void "
        "QPlaceRatings::swap(QPlaceRatings &other)': takes a type Python "
        "has no way to hand over yet.")
