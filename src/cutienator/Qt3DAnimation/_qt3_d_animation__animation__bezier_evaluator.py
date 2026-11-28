"""
Qt3DAnimation::Animation::BezierEvaluator binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DAnimation/6.12.0/Qt3DAnimation/private/bezierevaluator_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DAnimation::Animation::BezierEvaluator to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import Qt3DAnimation

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class BezierEvaluator(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's Qt3DAnimation::Animation::BezierEvaluator: a plain
  Python object standing in front of one C++
  Qt3DAnimation::Animation::BezierEvaluator.

  C++ hands a Qt3DAnimation::Animation::BezierEvaluator around as a copy, so
  every C++ Qt3DAnimation::Animation::BezierEvaluator behind a cute one is
  Python's own: it is removed, by the ritual named in '__delete_ritual__',
  when the cute object goes.

  What exists
  -----------

  No function of Qt's Qt3DAnimation::Animation::BezierEvaluator yet. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DAnimation::Animation::BezierEvaluator::~BezierEvaluator()': the
    destructor: Python removes its C++
    Qt3DAnimation::Animation::BezierEvaluator by it, and has no other use for
    it.

  What has no ritual
  ------------------

  3 of the 5 functions Qt declares: 2 leans on 'Qt3DAnimation; 1 Qt's library
  has no name for it, and its code in Qt's source does not compile apart from
  its file.

  What to expect
  --------------

  - The C++ Qt3DAnimation::Animation::BezierEvaluator is created at the first
    use, not by 'Qt3DAnimation::Animation::BezierEvaluator(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a Qt3DAnimation::Animation::BezierEvaluator back gives
    a copy the ritual made for Python, in a new cute
    Qt3DAnimation::Animation::BezierEvaluator.
  - Each name of Qt's Qt3DAnimation::Animation::BezierEvaluator that has no
    cute function yet, 'findCubicRoots', 'parameterForTime', 'valueForTime',
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
  __qt_class__ = 'Qt3DAnimation::Animation::BezierEvaluator'

  #  Qt's '~Qt3DAnimation::Animation::BezierEvaluator()'. Naming it makes
  #  this a value class: Python owns every C++
  #  Qt3DAnimation::Animation::BezierEvaluator behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = (
      'ritual_ZN13Qt3DAnimation9Animation15BezierEvaluatorD1Ev')

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

  @overload(
      float, WAIT['Qt3DAnimation.Animation.Keyframe'], float,
      WAIT['Qt3DAnimation.Animation.Keyframe'],
  )
  def __init__(
      self,
      time0: float,
      keyframe0: Qt3DAnimation.Animation.Keyframe,
      time1: float,
      keyframe1: Qt3DAnimation.Animation.Keyframe,
  ) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DAnimation::Animation::BezierEvaluator::BezierEvaluator(float time0,
    const Keyframe &keyframe0, float time1, const Keyframe &keyframe1)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-bezierevaluator.html

    Parameters
    ----------

    time0 : float
      Passed on as it is.

    keyframe0 : Qt3DAnimation.Animation.Keyframe
      Passed on as a value: Qt reads the C++
      Qt3DAnimation::Animation::Keyframe, which stays Python's own.

    time1 : float
      Passed on as it is.

    keyframe1 : Qt3DAnimation.Animation.Keyframe
      Passed on as a value: Qt reads the C++
      Qt3DAnimation::Animation::Keyframe, which stays Python's own.
    """
    #  Qt3DAnimation::Animation::BezierEvaluator::BezierEvaluator(float
    #      time0, const Keyframe &keyframe0, float time1, const Keyframe
    #      &keyframe1)
    self._noteCreation(BezierEvaluator, lambda: Rituals.call(
        'ritual_ZN13Qt3DAnimation9Animation15BezierEvaluatorC1EfRKNS0_8Keyf'
        'rameEfS4_',
        time0, self._valueOf(keyframe0), time1, self._valueOf(keyframe1),
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
  def findCubicRoots(*__, **_) -> Never:
    """
    Qt's 'int Qt3DAnimation::Animation::BezierEvaluator::findCubicRoots(const
    float *coefficients, float *roots)': Qt's library has no name for it, and
    its code in Qt's source does not compile apart from its file: use of
    undeclared identifier 'almostZero'.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.Animation.BezierEvaluator.findCubicRoots' has no "
        "cute function yet. Qt's 'int "
        "Qt3DAnimation::Animation::BezierEvaluator::findCubicRoots(const "
        "float *coefficients, float *roots)': Qt's library has no name for "
        "it, and its code in Qt's source does not compile apart from its "
        "file: use of undeclared identifier 'almostZero'.")

  @staticmethod
  def parameterForTime(*__, **_) -> Never:
    """
    Qt's 'float
    Qt3DAnimation::Animation::BezierEvaluator::parameterForTime(float time)
    const': leans on
    'Qt3DAnimation::Animation::BezierEvaluator::findCubicRoots(float const*,
    float*)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.Animation.BezierEvaluator.parameterForTime' has no "
        "cute function yet. Qt's 'float "
        "Qt3DAnimation::Animation::BezierEvaluator::parameterForTime(float "
        "time) const': leans on "
        "'Qt3DAnimation::Animation::BezierEvaluator::findCubicRoots(float "
        "const*, float*)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

  @staticmethod
  def valueForTime(*__, **_) -> Never:
    """
    Qt's 'float Qt3DAnimation::Animation::BezierEvaluator::valueForTime(float
    time) const': leans on
    'Qt3DAnimation::Animation::BezierEvaluator::findCubicRoots(float const*,
    float*)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.Animation.BezierEvaluator.valueForTime' has no cute "
        "function yet. Qt's 'float "
        "Qt3DAnimation::Animation::BezierEvaluator::valueForTime(float "
        "time) const': leans on "
        "'Qt3DAnimation::Animation::BezierEvaluator::findCubicRoots(float "
        "const*, float*)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")
