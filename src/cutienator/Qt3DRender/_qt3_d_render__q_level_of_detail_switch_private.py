"""
Qt3DRender::QLevelOfDetailSwitchPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/qlevelofdetailswitch_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DRender::QLevelOfDetailSwitchPrivate to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional


class QLevelOfDetailSwitchPrivate(Qt3DRender.QLevelOfDetailPrivate):
  """
  The cute side of Qt's Qt3DRender::QLevelOfDetailSwitchPrivate: a plain
  Python object standing in front of one C++
  Qt3DRender::QLevelOfDetailSwitchPrivate.

  It is built on the cute 'Qt3DRender::QLevelOfDetailPrivate', as Qt's
  Qt3DRender::QLevelOfDetailSwitchPrivate is built on Qt's
  Qt3DRender::QLevelOfDetailPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QLevelOfDetailSwitchPrivate that has a
  ritual and that Python can call so far, 2 names in all: 'q_func',
  'setCurrentIndex'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QLevelOfDetailSwitch
    *Qt3DRender::QLevelOfDetailSwitchPrivate::q_func() const': takes in
    Python what 'QLevelOfDetailSwitch
    *Qt3DRender::QLevelOfDetailSwitchPrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ Qt3DRender::QLevelOfDetailSwitchPrivate is created at the first
    use, not by 'Qt3DRender::QLevelOfDetailSwitchPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::QLevelOfDetailSwitchPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::QLevelOfDetailSwitchPrivate'

  #  A C++ Qt3DRender::QLevelOfDetailSwitchPrivate Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_QLevelOfDetailSwitchPrivate'

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

  @overload(int)
  def setCurrentIndex(self, currentIndex: int) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QLevelOfDetailSwitchPrivate::setCurrentIndex(int
    currentIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qlevelofdetailswitchprivate.html

    Parameters
    ----------

    currentIndex : int
      Passed on as it is.
    """
    #  void Qt3DRender::QLevelOfDetailSwitchPrivate::setCurrentIndex(int
    #      currentIndex)
    ritual = (
        'ritual_ZN10Qt3DRender27QLevelOfDetailSwitchPrivate15setCurrentInde'
        'xEi')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10Qt3DRender27QLevelOfDetailSwitchPrivate15setCurre'
          'ntIndexEi')
    self.uglySide.call(ritual, currentIndex)

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
    'Qt3DRender::QLevelOfDetailSwitchPrivate::QLevelOfDetailSwitchPrivate()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qlevelofdetailswitchprivate.html
    """
    #  Qt3DRender::QLevelOfDetailSwitchPrivate::QLevelOfDetailSwitchPrivate()
    self._noteCreation(QLevelOfDetailSwitchPrivate, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender27QLevelOfDetailSwitchPrivateC1Ev',
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

  def q_func(self) -> Optional[Qt3DRender.QLevelOfDetailSwitch]:
    """
    Calls Qt's 'QLevelOfDetailSwitch
    *Qt3DRender::QLevelOfDetailSwitchPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qlevelofdetailswitchprivate.html#q_func

    Returns
    -------

    Optional[Qt3DRender.QLevelOfDetailSwitch]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLevelOfDetailSwitch
    #      *Qt3DRender::QLevelOfDetailSwitchPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender27QLevelOfDetailSwitchPrivate6q_funcEv',
    )
    return Qt3DRender.QLevelOfDetailSwitch._cuteAt(address)
