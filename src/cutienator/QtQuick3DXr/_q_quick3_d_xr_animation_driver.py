"""
QQuick3DXrAnimationDriver binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DXr/6.12.0/QtQuick3DXr/private/qquick3dxranimationdriver_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuick3DXrAnimationDriver to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..occult import Rituals
from ..QtCore import QAnimationDriver


class QQuick3DXrAnimationDriver(QAnimationDriver):
  """
  The cute side of Qt's QQuick3DXrAnimationDriver: a plain Python object
  standing in front of one C++ QQuick3DXrAnimationDriver.

  It is built on the cute 'QAnimationDriver', as Qt's
  QQuick3DXrAnimationDriver is built on Qt's QAnimationDriver, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DXrAnimationDriver that has a ritual and that
  Python can call so far, 4 names in all: 'advance', 'elapsed', 'setStep',
  'start'. It can be made from Python, in 1 way; see '__init__'.

  What to expect
  --------------

  - The C++ QQuick3DXrAnimationDriver is created at the first use, not by
    'QQuick3DXrAnimationDriver(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DXrAnimationDriver.
  - Qt tells when it has removed the C++ QQuick3DXrAnimationDriver. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DXrAnimationDriver'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def elapsed(self) -> int:
    """
    Calls Qt's 'qint64 QQuick3DXrAnimationDriver::elapsed() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxranimationdriver.html#elapsed
    """
    #  qint64 QQuick3DXrAnimationDriver::elapsed() const
    ritual = 'ritual_ZNK25QQuick3DXrAnimationDriver7elapsedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK25QQuick3DXrAnimationDriver7elapsedEv'
    return self.uglySide.call(ritual)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setStep(self, stepSize: int) -> None:
    """
    Calls Qt's 'void QQuick3DXrAnimationDriver::setStep(int stepSize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxranimationdriver.html#setStep

    Parameters
    ----------

    stepSize : int
      Passed on as it is.
    """
    #  void QQuick3DXrAnimationDriver::setStep(int stepSize)
    self.uglySide.call(
        'ritual_ZN25QQuick3DXrAnimationDriver7setStepEi', stepSize,
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
    'QQuick3DXrAnimationDriver::QQuick3DXrAnimationDriver()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxranimationdriver.html
    """
    #  QQuick3DXrAnimationDriver::QQuick3DXrAnimationDriver()
    self._noteCreation(QQuick3DXrAnimationDriver, lambda: Rituals.call(
        'ritual_ZN25QQuick3DXrAnimationDriverC1Ev',
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

  def advance(self) -> None:
    """
    Calls Qt's 'void QQuick3DXrAnimationDriver::advance()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxranimationdriver.html#advance
    """
    #  void QQuick3DXrAnimationDriver::advance()
    ritual = 'ritual_ZN25QQuick3DXrAnimationDriver7advanceEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN25QQuick3DXrAnimationDriver7advanceEv'
    self.uglySide.call(ritual)

  def start(self) -> None:
    """
    Calls Qt's 'void QQuick3DXrAnimationDriver::start()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxranimationdriver.html#start
    """
    #  void QQuick3DXrAnimationDriver::start()
    ritual = 'ritual_ZN25QQuick3DXrAnimationDriver5startEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN25QQuick3DXrAnimationDriver5startEv'
    self.uglySide.call(ritual)
