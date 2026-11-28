"""
Qt3DRender::Render::VSyncFrameAdvanceService binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/vsyncframeadvanceservice_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means Qt3DRender::Render::VSyncFrameAdvanceService to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..occult import Rituals
from ..Qt3DCore import Qt3DCore


class VSyncFrameAdvanceService(Qt3DCore.QAbstractFrameAdvanceService):
  """
  The cute side of Qt's Qt3DRender::Render::VSyncFrameAdvanceService: a plain
  Python object standing in front of one C++
  Qt3DRender::Render::VSyncFrameAdvanceService.

  It is built on the cute 'Qt3DCore::QAbstractFrameAdvanceService', as Qt's
  Qt3DRender::Render::VSyncFrameAdvanceService is built on Qt's
  Qt3DCore::QAbstractFrameAdvanceService, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::Render::VSyncFrameAdvanceService that
  has a ritual and that Python can call so far, 4 names in all:
  'waitForNextFrame', 'start', 'stop', 'proceedToNextFrame'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's
    'Qt3DRender::Render::VSyncFrameAdvanceService::~VSyncFrameAdvanceService(
    )': the destructor: Python never removes a C++
    Qt3DRender::Render::VSyncFrameAdvanceService.

  What has no ritual
  ------------------

  2 of the 8 functions Qt declares: 2 the compiler refuses its ritual as it
  would be written here.

  What to expect
  --------------

  - The C++ Qt3DRender::Render::VSyncFrameAdvanceService is created at the
    first use, not by 'Qt3DRender::Render::VSyncFrameAdvanceService(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++
    Qt3DRender::Render::VSyncFrameAdvanceService.
  - Qt tells when it has removed the C++
    Qt3DRender::Render::VSyncFrameAdvanceService. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::Render::VSyncFrameAdvanceService'

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

  @overload(bool)
  def __init__(self, drivenByRenderThread: bool) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::Render::VSyncFrameAdvanceService::VSyncFrameAdvanceService(
    bool drivenByRenderThread)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-vsyncframeadvanceservice.html

    Parameters
    ----------

    drivenByRenderThread : bool
      Passed on as it is.
    """
    #  Qt3DRender::Render::VSyncFrameAdvanceService::
    #      VSyncFrameAdvanceService(bool drivenByRenderThread)
    self._noteCreation(VSyncFrameAdvanceService, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender6Render24VSyncFrameAdvanceServiceC1Eb',
        drivenByRenderThread,
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

  def waitForNextFrame(self) -> int:
    """
    Calls Qt's 'qint64
    Qt3DRender::Render::VSyncFrameAdvanceService::waitForNextFrame()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-vsyncframeadvanceservice.html
    """
    #  qint64
    #      Qt3DRender::Render::VSyncFrameAdvanceService::waitForNextFrame()
    return self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render24VSyncFrameAdvanceService16waitForNex'
        'tFrameEv',
    )

  def start(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::VSyncFrameAdvanceService::start()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-vsyncframeadvanceservice.html
    """
    #  void Qt3DRender::Render::VSyncFrameAdvanceService::start()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render24VSyncFrameAdvanceService5startEv',
    )

  def stop(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::VSyncFrameAdvanceService::stop()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-vsyncframeadvanceservice.html
    """
    #  void Qt3DRender::Render::VSyncFrameAdvanceService::stop()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render24VSyncFrameAdvanceService4stopEv',
    )

  def proceedToNextFrame(self) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::VSyncFrameAdvanceService::proceedToNextFrame()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-vsyncframeadvanceservice.html
    """
    #  void
    #      Qt3DRender::Render::VSyncFrameAdvanceService::proceedToNextFrame()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render24VSyncFrameAdvanceService18proceedToN'
        'extFrameEv',
    )
