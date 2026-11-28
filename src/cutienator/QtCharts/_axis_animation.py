"""
AxisAnimation binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/6.12.0/QtCharts/private/axisanimation_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means AxisAnimation to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum, WAIT
from . import ChartAnimation

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QPointF, QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPointF = WAIT['QPointF']
  QVariant = WAIT['QVariant']


class AxisAnimation(ChartAnimation):
  """
  The cute side of Qt's AxisAnimation: a plain Python object standing in
  front of one C++ AxisAnimation.

  It is built on the cute 'ChartAnimation', as Qt's AxisAnimation is built on
  Qt's ChartAnimation, and has everything that class has.

  What exists
  -----------

  Every function of Qt's AxisAnimation that has a ritual and that Python can
  call so far, 4 names in all: 'setAnimationType', 'setAnimationPoint',
  'interpolated', 'updateCurrentValue'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'AxisAnimation::AxisAnimation(ChartAxisElement *axis, int duration,
    QEasingCurve &curve)': takes a type Python has no way to hand over yet.
  - Qt's 'AxisAnimation::~AxisAnimation()': the destructor: Python never
    removes a C++ AxisAnimation.
  - Qt's 'void AxisAnimation::setValues(QList<qreal> &oldLayout, const
    QList<qreal> &newLayout)': takes a type Python has no way to hand over
    yet.

  What to expect
  --------------

  - The C++ AxisAnimation is created at the first use, not by
    'AxisAnimation(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ AxisAnimation.
  - Qt tells when it has removed the C++ AxisAnimation. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's AxisAnimation that has no cute function yet,
    '__init__', 'setValues', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside AxisAnimation, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Animation(CuteNum):
    """
    The enum 'AxisAnimation::Animation' of Qt, with the 5 names Qt gives in
    it.
    """

    DefaultAnimation = Kee[int](0)
    ZoomOutAnimation = Kee[int](1)
    ZoomInAnimation = Kee[int](2)
    MoveForwardAnimation = Kee[int](3)
    MoveBackwordAnimation = Kee[int](4)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'AxisAnimation'

  #  A C++ AxisAnimation Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_AxisAnimation'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QVariant, QVariant, float)
  def interpolated(
      self,
      from_: QVariant,
      to: QVariant,
      progress: float,
  ) -> QVariant:
    """
    Calls Qt's 'QVariant AxisAnimation::interpolated(const QVariant &from,
    const QVariant &to, qreal progress) const'.

    Qt's own words: https://doc.qt.io/qt-6/axisanimation.html#interpolated

    Parameters
    ----------

    from_ : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    to : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    progress : float
      Passed on as it is.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant AxisAnimation::interpolated(const QVariant &from, const
    #      QVariant &to, qreal progress) const
    ritual = 'ritual_ZNK13AxisAnimation12interpolatedERK8QVariantS2_d'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13AxisAnimation12interpolatedERK8QVariantS2_d'
    address = self.uglySide.call(
        ritual, self._valueOf(from_), self._valueOf(to), progress,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Animation)
  def setAnimationType(self, type: Animation) -> None:
    """
    Calls Qt's 'void AxisAnimation::setAnimationType(Animation type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/axisanimation.html#setAnimationType

    Parameters
    ----------

    type : Animation
      Passed on as its number.
    """
    #  void AxisAnimation::setAnimationType(Animation type)
    self.uglySide.call(
        'ritual_ZN13AxisAnimation16setAnimationTypeENS_9AnimationE',
        type.value,
    )

  @overload(QPointF)
  def setAnimationPoint(self, point: QPointF) -> None:
    """
    Calls Qt's 'void AxisAnimation::setAnimationPoint(const QPointF &point)'.

    Qt's own words:
    https://doc.qt.io/qt-6/axisanimation.html#setAnimationPoint

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void AxisAnimation::setAnimationPoint(const QPointF &point)
    self.uglySide.call(
        'ritual_ZN13AxisAnimation17setAnimationPointERK7QPointF',
        self._valueOf(point, 'QPointF'),
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
    Qt's 'AxisAnimation::AxisAnimation(ChartAxisElement *axis, int duration,
    QEasingCurve &curve)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'AxisAnimation.__init__' has no cute function yet. Qt's "
        "'AxisAnimation::AxisAnimation(ChartAxisElement *axis, int "
        "duration, QEasingCurve &curve)': takes a type Python has no way to "
        "hand over yet.")

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

  @overload(QVariant)
  def updateCurrentValue(self, value: QVariant) -> None:
    """
    Calls Qt's 'void AxisAnimation::updateCurrentValue(const QVariant
    &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/axisanimation.html#updateCurrentValue

    Parameters
    ----------

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void AxisAnimation::updateCurrentValue(const QVariant &value)
    ritual = 'ritual_ZN13AxisAnimation18updateCurrentValueERK8QVariant'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13AxisAnimation18updateCurrentValueERK8QVariant'
    self.uglySide.call(ritual, self._valueOf(value))

  @staticmethod
  def setValues(*__, **_) -> Never:
    """
    Qt's 'void AxisAnimation::setValues(QList<qreal> &oldLayout, const
    QList<qreal> &newLayout)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'AxisAnimation.setValues' has no cute function yet. Qt's 'void "
        "AxisAnimation::setValues(QList<qreal> &oldLayout, const "
        "QList<qreal> &newLayout)': takes a type Python has no way to hand "
        "over yet.")
