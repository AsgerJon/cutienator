"""
Qt3DAnimation::Animation::Clock binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DAnimation/6.12.0/Qt3DAnimation/private/clock_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means Qt3DAnimation::Animation::Clock to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DAnimation

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Clock(Qt3DAnimation.Animation.BackendNode):
  """
  The cute side of Qt's Qt3DAnimation::Animation::Clock: a plain Python
  object standing in front of one C++ Qt3DAnimation::Animation::Clock.

  It is built on the cute 'Qt3DAnimation::Animation::BackendNode', as Qt's
  Qt3DAnimation::Animation::Clock is built on Qt's
  Qt3DAnimation::Animation::BackendNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DAnimation::Animation::Clock that has a ritual
  and that Python can call so far, 4 names in all: 'syncFromFrontEnd',
  'cleanup', 'setPlaybackRate', 'playbackRate'. It can be made from Python,
  in 1 way; see '__init__'.

  What to expect
  --------------

  - The C++ Qt3DAnimation::Animation::Clock is created at the first use, not
    by 'Qt3DAnimation::Animation::Clock(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DAnimation::Animation::Clock.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DAnimation::Animation::Clock'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def playbackRate(self) -> float:
    """
    Calls Qt's 'double Qt3DAnimation::Animation::Clock::playbackRate()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-clock.html#playbackRate
    """
    #  double Qt3DAnimation::Animation::Clock::playbackRate() const
    return self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation9Animation5Clock12playbackRateEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setPlaybackRate(self, playbackRate: float) -> None:
    """
    Calls Qt's 'void Qt3DAnimation::Animation::Clock::setPlaybackRate(double
    playbackRate)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-clock.html#setPlaybackRate

    Parameters
    ----------

    playbackRate : float
      Passed on as it is.
    """
    #  void Qt3DAnimation::Animation::Clock::setPlaybackRate(double
    #      playbackRate)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation9Animation5Clock15setPlaybackRateEd',
        playbackRate,
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
    'Qt3DAnimation::Animation::Clock::Clock()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-clock.html#Clock
    """
    #  Qt3DAnimation::Animation::Clock::Clock()
    self._noteCreation(Clock, lambda: Rituals.call(
        'ritual_ZN13Qt3DAnimation9Animation5ClockC1Ev',
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

  @overload(WAIT['Qt3DCore.QNode'], bool)
  @overload(NoneType, bool)
  def syncFromFrontEnd(
      self,
      frontEnd: Optional[Qt3DCore.QNode],
      firstTime: bool,
  ) -> None:
    """
    Calls Qt's 'void Qt3DAnimation::Animation::Clock::syncFromFrontEnd(const
    Qt3DCore::QNode *frontEnd, bool firstTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-clock.html

    Parameters
    ----------

    frontEnd : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    firstTime : bool
      Passed on as it is.
    """
    #  void Qt3DAnimation::Animation::Clock::syncFromFrontEnd(const
    #      Qt3DCore::QNode *frontEnd, bool firstTime)
    ritual = (
        'ritual_ZN13Qt3DAnimation9Animation5Clock16syncFromFrontEndEPKN8Qt3'
        'DCore5QNodeEb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN13Qt3DAnimation9Animation5Clock16syncFromFrontEndEP'
          'KN8Qt3DCore5QNodeEb')
    self.uglySide.call(ritual, self._addressOf(frontEnd), firstTime)

  def cleanup(self) -> None:
    """
    Calls Qt's 'void Qt3DAnimation::Animation::Clock::cleanup()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-clock.html#cleanup
    """
    #  void Qt3DAnimation::Animation::Clock::cleanup()
    self.uglySide.call('ritual_ZN13Qt3DAnimation9Animation5Clock7cleanupEv')
