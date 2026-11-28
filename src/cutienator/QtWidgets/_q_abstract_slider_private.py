"""
QAbstractSliderPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qabstractslider_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QAbstractSliderPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..occult import Rituals
from ..QtCore import Qt
from . import QWidgetPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QAbstractSlider


class QAbstractSliderPrivate(QWidgetPrivate):
  """
  The cute side of Qt's QAbstractSliderPrivate: a plain Python object
  standing in front of one C++ QAbstractSliderPrivate.

  It is built on the cute 'QWidgetPrivate', as Qt's QAbstractSliderPrivate is
  built on Qt's QWidgetPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAbstractSliderPrivate that has a ritual and that
  Python can call so far, 8 names in all: 'q_func', 'setSteps',
  'effectiveSingleStep', 'itemviewChangeSingleStep', 'bound',
  'overflowSafeAdd', 'setAdjustedSliderPosition', 'scrollByDelta'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QAbstractSlider *QAbstractSliderPrivate::q_func() const':
    takes in Python what 'QAbstractSlider *QAbstractSliderPrivate::q_func()'
    takes.
  - Qt's 'QAbstractSliderPrivate::~QAbstractSliderPrivate()': the destructor:
    Python never removes a C++ QAbstractSliderPrivate.

  What to expect
  --------------

  - The C++ QAbstractSliderPrivate is created at the first use, not by
    'QAbstractSliderPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAbstractSliderPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAbstractSliderPrivate'

  #  A C++ QAbstractSliderPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAbstractSliderPrivate'

  #  The functions Qt calls itself that QAbstractSliderPrivate is the first
  #  to declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'bound': (
          ('_ZNK22QAbstractSliderPrivate5boundEi',
           ('int', 'number', ''),
           (
               ('int', 'number', ''),
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

  def effectiveSingleStep(self) -> int:
    """
    Calls Qt's 'int QAbstractSliderPrivate::effectiveSingleStep() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractsliderprivate.html#effectiveSingleStep
    """
    #  int QAbstractSliderPrivate::effectiveSingleStep() const
    return self.uglySide.call(
        'ritual_ZNK22QAbstractSliderPrivate19effectiveSingleStepEv',
    )

  @overload(int)
  def bound(self, val: int) -> int:
    """
    Calls Qt's 'int QAbstractSliderPrivate::bound(int val) const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractsliderprivate.html#bound

    Parameters
    ----------

    val : int
      Passed on as it is.
    """
    #  int QAbstractSliderPrivate::bound(int val) const
    ritual = 'ritual_ZNK22QAbstractSliderPrivate5boundEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK22QAbstractSliderPrivate5boundEi'
    return self.uglySide.call(ritual, val)

  @overload(int)
  def overflowSafeAdd(self, add: int) -> int:
    """
    Calls Qt's 'int QAbstractSliderPrivate::overflowSafeAdd(int add) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractsliderprivate.html#overflowSafeAdd

    Parameters
    ----------

    add : int
      Passed on as it is.
    """
    #  int QAbstractSliderPrivate::overflowSafeAdd(int add) const
    return self.uglySide.call(
        'ritual_ZNK22QAbstractSliderPrivate15overflowSafeAddEi', add,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int, int)
  def setSteps(self, single: int, page: int) -> None:
    """
    Calls Qt's 'void QAbstractSliderPrivate::setSteps(int single, int page)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractsliderprivate.html#setSteps

    Parameters
    ----------

    single : int
      Passed on as it is.

    page : int
      Passed on as it is.
    """
    #  void QAbstractSliderPrivate::setSteps(int single, int page)
    self.uglySide.call(
        'ritual_ZN22QAbstractSliderPrivate8setStepsEii', single, page,
    )

  @overload(int)
  def setAdjustedSliderPosition(self, position: int) -> None:
    """
    Calls Qt's 'void QAbstractSliderPrivate::setAdjustedSliderPosition(int
    position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractsliderprivate.html

    Parameters
    ----------

    position : int
      Passed on as it is.
    """
    #  void QAbstractSliderPrivate::setAdjustedSliderPosition(int position)
    self.uglySide.call(
        'ritual_ZN22QAbstractSliderPrivate25setAdjustedSliderPositionEi',
        position,
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QAbstractSliderPrivate::QAbstractSliderPrivate()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractsliderprivate.html#QAbstractSliderPrivate
    """
    #  QAbstractSliderPrivate::QAbstractSliderPrivate()
    self._noteCreation(QAbstractSliderPrivate, lambda: Rituals.call(
        'ritual_ZN22QAbstractSliderPrivateC1Ev',
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

  def q_func(self) -> Optional[QAbstractSlider]:
    """
    Calls Qt's 'QAbstractSlider *QAbstractSliderPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractsliderprivate.html#q_func

    Returns
    -------

    Optional[QAbstractSlider]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractSlider *QAbstractSliderPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN22QAbstractSliderPrivate6q_funcEv',
    )
    from . import QAbstractSlider
    return QAbstractSlider._cuteAt(address)

  @overload(int)
  def itemviewChangeSingleStep(self, step: int) -> None:
    """
    Calls Qt's 'void QAbstractSliderPrivate::itemviewChangeSingleStep(int
    step)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractsliderprivate.html

    Parameters
    ----------

    step : int
      Passed on as it is.
    """
    #  void QAbstractSliderPrivate::itemviewChangeSingleStep(int step)
    self.uglySide.call(
        'ritual_ZN22QAbstractSliderPrivate24itemviewChangeSingleStepEi',
        step,
    )

  @overload(Qt.Orientation, Qt.KeyboardModifiers, int)
  def scrollByDelta(
      self,
      orientation: Qt.Orientation,
      modifiers: Qt.KeyboardModifiers,
      delta: int,
  ) -> bool:
    """
    Calls Qt's 'bool QAbstractSliderPrivate::scrollByDelta(Qt::Orientation
    orientation, Qt::KeyboardModifiers modifiers, int delta)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractsliderprivate.html#scrollByDelta

    Parameters
    ----------

    orientation : Qt.Orientation
      Passed on as its number.

    modifiers : Qt.KeyboardModifiers
      Passed on as its number.

    delta : int
      Passed on as it is.
    """
    #  bool QAbstractSliderPrivate::scrollByDelta(Qt::Orientation
    #      orientation, Qt::KeyboardModifiers modifiers, int delta)
    return self.uglySide.call(
        'ritual_ZN22QAbstractSliderPrivate13scrollByDeltaEN2Qt11Orientation'
        'E6QFlagsINS0_16KeyboardModifierEEi',
        orientation.value, modifiers.value, delta,
    )
