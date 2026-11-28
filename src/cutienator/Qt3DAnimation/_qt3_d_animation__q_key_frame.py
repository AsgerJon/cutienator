"""
Qt3DAnimation::QKeyFrame binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DAnimation/qkeyframe.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtGui import QVector2D
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVector2D = WAIT['QVector2D']


class QKeyFrame(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's Qt3DAnimation::QKeyFrame: a plain Python object
  standing in front of one C++ Qt3DAnimation::QKeyFrame.

  C++ hands a Qt3DAnimation::QKeyFrame around as a copy, so every C++
  Qt3DAnimation::QKeyFrame behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's Qt3DAnimation::QKeyFrame that has a ritual and that
  Python can call so far, 10 names in all: 'setCoordinates', 'coordinates',
  'setLeftControlPoint', 'leftControlPoint', 'setRightControlPoint',
  'rightControlPoint', 'setInterpolationType', 'interpolationType', '__eq__',
  '__ne__'. It can be made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DAnimation::QKeyFrame::~QKeyFrame()': the destructor: Python
    removes its C++ Qt3DAnimation::QKeyFrame by it, and has no other use for
    it.

  What to expect
  --------------

  - The C++ Qt3DAnimation::QKeyFrame is created at the first use, not by
    'Qt3DAnimation::QKeyFrame(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a Qt3DAnimation::QKeyFrame back gives a copy the ritual
    made for Python, in a new cute Qt3DAnimation::QKeyFrame.
  """

  #  The enums Qt writes inside Qt3DAnimation::QKeyFrame, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class InterpolationType(CuteNum):
    """
    The enum 'Qt3DAnimation::QKeyFrame::InterpolationType' of Qt, with the 3
    names Qt gives in it.
    """

    ConstantInterpolation = Kee[int](0)
    LinearInterpolation = Kee[int](1)
    BezierInterpolation = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DAnimation::QKeyFrame'

  #  Qt's '~Qt3DAnimation::QKeyFrame()'. Naming it makes this a value class:
  #  Python owns every C++ Qt3DAnimation::QKeyFrame behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN13Qt3DAnimation9QKeyFrameD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def coordinates(self) -> QVector2D:
    """
    Calls Qt's 'QVector2D Qt3DAnimation::QKeyFrame::coordinates() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qkeyframe.html#coordinates

    Returns
    -------

    QVector2D
      A new cute QVector2D around the copy Qt gave back. Python owns it.
    """
    #  QVector2D Qt3DAnimation::QKeyFrame::coordinates() const
    address = self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation9QKeyFrame11coordinatesEv',
    )
    from ..QtGui import QVector2D
    return QVector2D._cuteOwning(address)

  def leftControlPoint(self) -> QVector2D:
    """
    Calls Qt's 'QVector2D Qt3DAnimation::QKeyFrame::leftControlPoint()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qkeyframe.html#leftControlPoint

    Returns
    -------

    QVector2D
      A new cute QVector2D around the copy Qt gave back. Python owns it.
    """
    #  QVector2D Qt3DAnimation::QKeyFrame::leftControlPoint() const
    address = self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation9QKeyFrame16leftControlPointEv',
    )
    from ..QtGui import QVector2D
    return QVector2D._cuteOwning(address)

  def rightControlPoint(self) -> QVector2D:
    """
    Calls Qt's 'QVector2D Qt3DAnimation::QKeyFrame::rightControlPoint()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qkeyframe.html#rightControlPoint

    Returns
    -------

    QVector2D
      A new cute QVector2D around the copy Qt gave back. Python owns it.
    """
    #  QVector2D Qt3DAnimation::QKeyFrame::rightControlPoint() const
    address = self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation9QKeyFrame17rightControlPointEv',
    )
    from ..QtGui import QVector2D
    return QVector2D._cuteOwning(address)

  def interpolationType(self) -> InterpolationType:
    """
    Calls Qt's 'InterpolationType
    Qt3DAnimation::QKeyFrame::interpolationType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qkeyframe.html#interpolationType

    Returns
    -------

    InterpolationType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'InterpolationType(number)' gives.
    """
    #  InterpolationType Qt3DAnimation::QKeyFrame::interpolationType() const
    return QKeyFrame.InterpolationType(self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation9QKeyFrame17interpolationTypeEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QVector2D)
  def setCoordinates(self, coords: QVector2D) -> None:
    """
    Calls Qt's 'void Qt3DAnimation::QKeyFrame::setCoordinates(QVector2D
    coords)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qkeyframe.html#setCoordinates

    Parameters
    ----------

    coords : QVector2D
      Passed on as a value: Qt reads the C++ QVector2D, which stays Python's
      own.
    """
    #  void Qt3DAnimation::QKeyFrame::setCoordinates(QVector2D coords)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation9QKeyFrame14setCoordinatesE9QVector2D',
        self._valueOf(coords),
    )

  @overload(QVector2D)
  def setLeftControlPoint(self, lh: QVector2D) -> None:
    """
    Calls Qt's 'void Qt3DAnimation::QKeyFrame::setLeftControlPoint(QVector2D
    lh)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qkeyframe.html#setLeftControlPoint

    Parameters
    ----------

    lh : QVector2D
      Passed on as a value: Qt reads the C++ QVector2D, which stays Python's
      own.
    """
    #  void Qt3DAnimation::QKeyFrame::setLeftControlPoint(QVector2D lh)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation9QKeyFrame19setLeftControlPointE9QVector2D',
        self._valueOf(lh),
    )

  @overload(QVector2D)
  def setRightControlPoint(self, rh: QVector2D) -> None:
    """
    Calls Qt's 'void Qt3DAnimation::QKeyFrame::setRightControlPoint(QVector2D
    rh)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qkeyframe.html#setRightControlPoint

    Parameters
    ----------

    rh : QVector2D
      Passed on as a value: Qt reads the C++ QVector2D, which stays Python's
      own.
    """
    #  void Qt3DAnimation::QKeyFrame::setRightControlPoint(QVector2D rh)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation9QKeyFrame20setRightControlPointE9QVector2'
        'D',
        self._valueOf(rh),
    )

  @overload(InterpolationType)
  def setInterpolationType(self, interp: InterpolationType) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::QKeyFrame::setInterpolationType(InterpolationType
    interp)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qkeyframe.html#setInterpolationType

    Parameters
    ----------

    interp : InterpolationType
      Passed on as its number.
    """
    #  void Qt3DAnimation::QKeyFrame::setInterpolationType(InterpolationType
    #      interp)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation9QKeyFrame20setInterpolationTypeENS0_17Int'
        'erpolationTypeE',
        interp.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, a1: QKeyFrame) -> bool:
    """
    Calls Qt's 'bool operator==(const QKeyFrame &a0, const QKeyFrame &a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qkeyframe.html#operator==

    Parameters
    ----------

    a1 : QKeyFrame
      Passed on as a value: Qt reads the C++ Qt3DAnimation::QKeyFrame, which
      stays Python's own.
    """
    #  bool operator==(const QKeyFrame &a0, const QKeyFrame &a1)
    return Rituals.call(
        'ritual_ZN13Qt3DAnimationeqERKNS_9QKeyFrameES2_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(a1),
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
  def __ne__(self, a1: QKeyFrame) -> bool:
    """
    Calls Qt's 'bool operator!=(const QKeyFrame &a0, const QKeyFrame &a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qkeyframe.html#operator!=

    Parameters
    ----------

    a1 : QKeyFrame
      Passed on as a value: Qt reads the C++ Qt3DAnimation::QKeyFrame, which
      stays Python's own.
    """
    #  bool operator!=(const QKeyFrame &a0, const QKeyFrame &a1)
    return Rituals.call(
        'ritual_ZN13Qt3DAnimationneERKNS_9QKeyFrameES2_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(a1),
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
    Notes what was given, for Qt's 'Qt3DAnimation::QKeyFrame::QKeyFrame()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qkeyframe.html#QKeyFrame
    """
    #  Qt3DAnimation::QKeyFrame::QKeyFrame()
    self._noteCreation(QKeyFrame, lambda: Rituals.call(
        'ritual_ZN13Qt3DAnimation9QKeyFrameC1Ev',
    ))

  @overload(QVector2D)
  def __init__(self, coords: QVector2D) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DAnimation::QKeyFrame::QKeyFrame(QVector2D coords)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qkeyframe.html#QKeyFrame

    Parameters
    ----------

    coords : QVector2D
      Passed on as a value: Qt reads the C++ QVector2D, which stays Python's
      own.
    """
    #  Qt3DAnimation::QKeyFrame::QKeyFrame(QVector2D coords)
    self._noteCreation(QKeyFrame, lambda: Rituals.call(
        'ritual_ZN13Qt3DAnimation9QKeyFrameC1E9QVector2D',
        self._valueOf(coords),
    ))

  @overload(QVector2D, QVector2D, QVector2D)
  def __init__(
      self,
      coords: QVector2D,
      lh: QVector2D,
      rh: QVector2D,
  ) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DAnimation::QKeyFrame::QKeyFrame(QVector2D coords, QVector2D lh,
    QVector2D rh)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qkeyframe.html#QKeyFrame

    Parameters
    ----------

    coords : QVector2D
      Passed on as a value: Qt reads the C++ QVector2D, which stays Python's
      own.

    lh : QVector2D
      Passed on as a value: Qt reads the C++ QVector2D, which stays Python's
      own.

    rh : QVector2D
      Passed on as a value: Qt reads the C++ QVector2D, which stays Python's
      own.
    """
    #  Qt3DAnimation::QKeyFrame::QKeyFrame(QVector2D coords, QVector2D lh,
    #      QVector2D rh)
    self._noteCreation(QKeyFrame, lambda: Rituals.call(
        'ritual_ZN13Qt3DAnimation9QKeyFrameC1E9QVector2DS1_S1_',
        self._valueOf(coords), self._valueOf(lh), self._valueOf(rh),
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
