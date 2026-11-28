"""
Qt3DAnimation::Animation::FunctionRangeFinder binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DAnimation/6.12.0/Qt3DAnimation/private/functionrangefinder_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means Qt3DAnimation::Animation::FunctionRangeFinder to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class FunctionRangeFinder(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's Qt3DAnimation::Animation::FunctionRangeFinder: a
  plain Python object standing in front of one C++
  Qt3DAnimation::Animation::FunctionRangeFinder.

  C++ hands a Qt3DAnimation::Animation::FunctionRangeFinder around as a copy,
  so every C++ Qt3DAnimation::Animation::FunctionRangeFinder behind a cute
  one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's Qt3DAnimation::Animation::FunctionRangeFinder that
  has a ritual and that Python can call so far, 9 names in all:
  'findLowerBound', 'rangeSize', 'setRangeSize', 'isAscending',
  'setAscending', 'correlationThreshold',
  'updateAutomaticCorrelationThreshold', 'locate', 'hunt'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DAnimation::Animation::FunctionRangeFinder::FunctionRangeFinder(
    QList<float> *x)': names 'QList<float>', which has no cute class yet.
  - Qt's
    'Qt3DAnimation::Animation::FunctionRangeFinder::~FunctionRangeFinder()':
    the destructor: Python removes its C++
    Qt3DAnimation::Animation::FunctionRangeFinder by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ Qt3DAnimation::Animation::FunctionRangeFinder is created at the
    first use, not by 'Qt3DAnimation::Animation::FunctionRangeFinder(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a Qt3DAnimation::Animation::FunctionRangeFinder back
    gives a copy the ritual made for Python, in a new cute
    Qt3DAnimation::Animation::FunctionRangeFinder.
  - Each name of Qt's Qt3DAnimation::Animation::FunctionRangeFinder that has
    no cute function yet, '__init__', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DAnimation::Animation::FunctionRangeFinder'

  #  Qt's '~Qt3DAnimation::Animation::FunctionRangeFinder()'. Naming it makes
  #  this a value class: Python owns every C++
  #  Qt3DAnimation::Animation::FunctionRangeFinder behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = (
      'ritual_ZN13Qt3DAnimation9Animation19FunctionRangeFinderD1Ev')

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def findLowerBound(self, x: float) -> int:
    """
    Calls Qt's 'int
    Qt3DAnimation::Animation::FunctionRangeFinder::findLowerBound(float x)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-functionrangefinder.html

    Parameters
    ----------

    x : float
      Passed on as it is.
    """
    #  int Qt3DAnimation::Animation::FunctionRangeFinder::findLowerBound(
    #      float x) const
    return self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation9Animation19FunctionRangeFinder14findLowe'
        'rBoundEf',
        x,
    )

  def rangeSize(self) -> int:
    """
    Calls Qt's 'int
    Qt3DAnimation::Animation::FunctionRangeFinder::rangeSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-functionrangefinder.html
    """
    #  int Qt3DAnimation::Animation::FunctionRangeFinder::rangeSize() const
    return self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation9Animation19FunctionRangeFinder9rangeSize'
        'Ev',
    )

  def isAscending(self) -> bool:
    """
    Calls Qt's 'bool
    Qt3DAnimation::Animation::FunctionRangeFinder::isAscending() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-functionrangefinder.html
    """
    #  bool Qt3DAnimation::Animation::FunctionRangeFinder::isAscending()
    #      const
    return self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation9Animation19FunctionRangeFinder11isAscend'
        'ingEv',
    )

  def correlationThreshold(self) -> int:
    """
    Calls Qt's 'int
    Qt3DAnimation::Animation::FunctionRangeFinder::correlationThreshold()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-functionrangefinder.html
    """
    #  int Qt3DAnimation::Animation::FunctionRangeFinder::
    #      correlationThreshold() const
    return self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation9Animation19FunctionRangeFinder20correlat'
        'ionThresholdEv',
    )

  @overload(float)
  def locate(self, x: float) -> int:
    """
    Calls Qt's 'int
    Qt3DAnimation::Animation::FunctionRangeFinder::locate(float x) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-functionrangefinder.html

    Parameters
    ----------

    x : float
      Passed on as it is.
    """
    #  int Qt3DAnimation::Animation::FunctionRangeFinder::locate(float x)
    #      const
    return self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation9Animation19FunctionRangeFinder6locateEf',
        x,
    )

  @overload(float)
  def hunt(self, x: float) -> int:
    """
    Calls Qt's 'int Qt3DAnimation::Animation::FunctionRangeFinder::hunt(float
    x) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-functionrangefinder.html

    Parameters
    ----------

    x : float
      Passed on as it is.
    """
    #  int Qt3DAnimation::Animation::FunctionRangeFinder::hunt(float x) const
    return self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation9Animation19FunctionRangeFinder4huntEf', x,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setRangeSize(self, rangeSize: int) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::Animation::FunctionRangeFinder::setRangeSize(int
    rangeSize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-functionrangefinder.html

    Parameters
    ----------

    rangeSize : int
      Passed on as it is.
    """
    #  void Qt3DAnimation::Animation::FunctionRangeFinder::setRangeSize(int
    #      rangeSize)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation9Animation19FunctionRangeFinder12setRangeS'
        'izeEi',
        rangeSize,
    )

  @overload(bool)
  def setAscending(self, ascending: bool) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::Animation::FunctionRangeFinder::setAscending(bool
    ascending)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-functionrangefinder.html

    Parameters
    ----------

    ascending : bool
      Passed on as it is.
    """
    #  void Qt3DAnimation::Animation::FunctionRangeFinder::setAscending(bool
    #      ascending)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation9Animation19FunctionRangeFinder12setAscend'
        'ingEb',
        ascending,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'Qt3DAnimation::Animation::FunctionRangeFinder::FunctionRangeFinder(
    QList<float> *x)': names 'QList<float>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.Animation.FunctionRangeFinder.__init__' has no cute "
        "function yet. Qt's "
        "'Qt3DAnimation::Animation::FunctionRangeFinder::FunctionRangeFinder"
        "(QList<float> *x)': names 'QList<float>', which has no cute class "
        "yet.")

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

  def updateAutomaticCorrelationThreshold(self) -> None:
    """
    Calls Qt's 'void Qt3DAnimation::Animation::FunctionRangeFinder::
    updateAutomaticCorrelationThreshold()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-functionrangefinder.html
    """
    #  void Qt3DAnimation::Animation::FunctionRangeFinder::
    #      updateAutomaticCorrelationThreshold()
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation9Animation19FunctionRangeFinder35updateAut'
        'omaticCorrelationThresholdEv',
    )
