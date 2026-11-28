"""
Qt3DAnimation::Animation::FCurve binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DAnimation/6.12.0/Qt3DAnimation/private/fcurve_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means Qt3DAnimation::Animation::FCurve to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import Qt3DAnimation

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QJsonObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QJsonObject = WAIT['QJsonObject']


class FCurve(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's Qt3DAnimation::Animation::FCurve: a plain Python
  object standing in front of one C++ Qt3DAnimation::Animation::FCurve.

  C++ hands a Qt3DAnimation::Animation::FCurve around as a copy, so every C++
  Qt3DAnimation::Animation::FCurve behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's Qt3DAnimation::Animation::FCurve that has a ritual
  and that Python can call so far, 10 names in all: 'keyframeCount',
  'appendKeyframe', 'clearKeyframes', 'localTime', 'keyframe', 'startTime',
  'endTime', 'lowerKeyframeBound', 'read', 'setFromQChannelComponent'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Keyframe &Qt3DAnimation::Animation::FCurve::keyframe(int index)':
    gives a type Python has no way to take yet.
  - Qt's 'Qt3DAnimation::Animation::FCurve::~FCurve()': the destructor:
    Python removes its C++ Qt3DAnimation::Animation::FCurve by it, and has no
    other use for it.

  What has no ritual
  ------------------

  4 of the 17 functions Qt declares: 3 leans on 'Qt3DAnimation; 1 takes or
  gives a type that cannot be passed yet.

  What to expect
  --------------

  - The C++ Qt3DAnimation::Animation::FCurve is created at the first use, not
    by 'Qt3DAnimation::Animation::FCurve(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a Qt3DAnimation::Animation::FCurve back gives a copy
    the ritual made for Python, in a new cute
    Qt3DAnimation::Animation::FCurve.
  - Each name of Qt's Qt3DAnimation::Animation::FCurve that has no cute
    function yet, 'evaluateAtTime', 'evaluateAtTimeAsSlerp', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DAnimation::Animation::FCurve'

  #  Qt's '~Qt3DAnimation::Animation::FCurve()'. Naming it makes this a value
  #  class: Python owns every C++ Qt3DAnimation::Animation::FCurve behind a
  #  cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN13Qt3DAnimation9Animation6FCurveD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def keyframeCount(self) -> int:
    """
    Calls Qt's 'int Qt3DAnimation::Animation::FCurve::keyframeCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-fcurve.html#keyframeCount
    """
    #  int Qt3DAnimation::Animation::FCurve::keyframeCount() const
    return self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation9Animation6FCurve13keyframeCountEv',
    )

  @overload(int)
  def localTime(self, index: int) -> float:
    """
    Calls Qt's 'const float &Qt3DAnimation::Animation::FCurve::localTime(int
    index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-fcurve.html#localTime

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  const float &Qt3DAnimation::Animation::FCurve::localTime(int index)
    #      const
    return self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation9Animation6FCurve9localTimeEi', index,
    )

  @overload(int)
  def keyframe(self, index: int) -> Qt3DAnimation.Animation.Keyframe:
    """
    Calls Qt's 'const Keyframe
    &Qt3DAnimation::Animation::FCurve::keyframe(int index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-fcurve.html#keyframe

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Qt3DAnimation.Animation.Keyframe
      A new cute Qt3DAnimation::Animation::Keyframe around the copy Qt gave
      back. Python owns it.
    """
    #  const Keyframe &Qt3DAnimation::Animation::FCurve::keyframe(int index)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation9Animation6FCurve8keyframeEi', index,
    )
    return Qt3DAnimation.Animation.Keyframe._cuteOwning(address)

  def startTime(self) -> float:
    """
    Calls Qt's 'float Qt3DAnimation::Animation::FCurve::startTime() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-fcurve.html#startTime
    """
    #  float Qt3DAnimation::Animation::FCurve::startTime() const
    return self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation9Animation6FCurve9startTimeEv',
    )

  def endTime(self) -> float:
    """
    Calls Qt's 'float Qt3DAnimation::Animation::FCurve::endTime() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-fcurve.html#endTime
    """
    #  float Qt3DAnimation::Animation::FCurve::endTime() const
    return self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation9Animation6FCurve7endTimeEv',
    )

  @overload(float)
  def lowerKeyframeBound(self, localTime: float) -> int:
    """
    Calls Qt's 'int
    Qt3DAnimation::Animation::FCurve::lowerKeyframeBound(float localTime)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-fcurve.html

    Parameters
    ----------

    localTime : float
      Passed on as it is.
    """
    #  int Qt3DAnimation::Animation::FCurve::lowerKeyframeBound(float
    #      localTime) const
    return self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation9Animation6FCurve18lowerKeyframeBoundEf',
        localTime,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['Qt3DAnimation.QChannelComponent'])
  def setFromQChannelComponent(
      self,
      qcc: Qt3DAnimation.QChannelComponent,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::Animation::FCurve::setFromQChannelComponent(const
    QChannelComponent &qcc)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-fcurve.html

    Parameters
    ----------

    qcc : Qt3DAnimation.QChannelComponent
      Passed on as a value: Qt reads the C++
      Qt3DAnimation::QChannelComponent, which stays Python's own.
    """
    #  void Qt3DAnimation::Animation::FCurve::setFromQChannelComponent(const
    #      QChannelComponent &qcc)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation9Animation6FCurve24setFromQChannelComponen'
        'tERKNS_17QChannelComponentE',
        self._valueOf(qcc),
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
    'Qt3DAnimation::Animation::FCurve::FCurve()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-fcurve.html#FCurve
    """
    #  Qt3DAnimation::Animation::FCurve::FCurve()
    self._noteCreation(FCurve, lambda: Rituals.call(
        'ritual_ZN13Qt3DAnimation9Animation6FCurveC1Ev',
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

  @overload(float, WAIT['Qt3DAnimation.Animation.Keyframe'])
  def appendKeyframe(
      self,
      localTime: float,
      keyframe: Qt3DAnimation.Animation.Keyframe,
  ) -> None:
    """
    Calls Qt's 'void Qt3DAnimation::Animation::FCurve::appendKeyframe(float
    localTime, const Keyframe &keyframe)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-fcurve.html#appendKeyframe

    Parameters
    ----------

    localTime : float
      Passed on as it is.

    keyframe : Qt3DAnimation.Animation.Keyframe
      Passed on as a value: Qt reads the C++
      Qt3DAnimation::Animation::Keyframe, which stays Python's own.
    """
    #  void Qt3DAnimation::Animation::FCurve::appendKeyframe(float localTime,
    #      const Keyframe &keyframe)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation9Animation6FCurve14appendKeyframeEfRKNS0_8'
        'KeyframeE',
        localTime, self._valueOf(keyframe),
    )

  def clearKeyframes(self) -> None:
    """
    Calls Qt's 'void Qt3DAnimation::Animation::FCurve::clearKeyframes()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-fcurve.html#clearKeyframes
    """
    #  void Qt3DAnimation::Animation::FCurve::clearKeyframes()
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation9Animation6FCurve14clearKeyframesEv',
    )

  @overload(QJsonObject)
  def read(self, json: QJsonObject) -> None:
    """
    Calls Qt's 'void Qt3DAnimation::Animation::FCurve::read(const QJsonObject
    &json)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-fcurve.html#read

    Parameters
    ----------

    json : QJsonObject
      Passed on as a value: Qt reads the C++ QJsonObject, which stays
      Python's own.
    """
    #  void Qt3DAnimation::Animation::FCurve::read(const QJsonObject &json)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation9Animation6FCurve4readERK11QJsonObject',
        self._valueOf(json),
    )

  @staticmethod
  def evaluateAtTime(*__, **_) -> Never:
    """
    - Qt's 'float Qt3DAnimation::Animation::FCurve::evaluateAtTime(float
      localTime) const': leans on
      'Qt3DAnimation::Animation::BezierEvaluator::findCubicRoots(float
      const*, float*)', which Qt's source does not mark for use from outside
      Qt and has no code for that could be taken.
    - Qt's 'float Qt3DAnimation::Animation::FCurve::evaluateAtTime(float
      localTime, int lowerBound) const': leans on
      'Qt3DAnimation::Animation::BezierEvaluator::findCubicRoots(float
      const*, float*)', which Qt's source does not mark for use from outside
      Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.Animation.FCurve.evaluateAtTime' has no cute "
        "function yet. Qt's 'float "
        "Qt3DAnimation::Animation::FCurve::evaluateAtTime(float localTime) "
        "const': leans on "
        "'Qt3DAnimation::Animation::BezierEvaluator::findCubicRoots(float "
        "const*, float*)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken. Qt's 'float "
        "Qt3DAnimation::Animation::FCurve::evaluateAtTime(float localTime, "
        "int lowerBound) const': leans on "
        "'Qt3DAnimation::Animation::BezierEvaluator::findCubicRoots(float "
        "const*, float*)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

  @staticmethod
  def evaluateAtTimeAsSlerp(*__, **_) -> Never:
    """
    Qt's 'float Qt3DAnimation::Animation::FCurve::evaluateAtTimeAsSlerp(float
    localTime, int lowerBound, float halfTheta, float sinHalfTheta, float
    reverseQ1) const': leans on
    'Qt3DAnimation::Animation::BezierEvaluator::findCubicRoots(float const*,
    float*)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.Animation.FCurve.evaluateAtTimeAsSlerp' has no cute "
        "function yet. Qt's 'float "
        "Qt3DAnimation::Animation::FCurve::evaluateAtTimeAsSlerp(float "
        "localTime, int lowerBound, float halfTheta, float sinHalfTheta, "
        "float reverseQ1) const': leans on "
        "'Qt3DAnimation::Animation::BezierEvaluator::findCubicRoots(float "
        "const*, float*)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")
