"""
Qt3DRender::Render::ComputeCommand binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/computecommand_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DRender::Render::ComputeCommand to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class ComputeCommand(Qt3DRender.Render.BackendNode):
  """
  The cute side of Qt's Qt3DRender::Render::ComputeCommand: a plain Python
  object standing in front of one C++ Qt3DRender::Render::ComputeCommand.

  It is built on the cute 'Qt3DRender::Render::BackendNode', as Qt's
  Qt3DRender::Render::ComputeCommand is built on Qt's
  Qt3DRender::Render::BackendNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::Render::ComputeCommand that has a ritual
  and that Python can call so far, 10 names in all: 'cleanup',
  'syncFromFrontEnd', 'x', 'y', 'z', 'frameCount', 'runType',
  'updateFrameCount', 'hasReachedFrameCount', 'resetHasReachedFrameCount'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DRender::Render::ComputeCommand::~ComputeCommand()': the
    destructor: Python never removes a C++
    Qt3DRender::Render::ComputeCommand.

  What to expect
  --------------

  - The C++ Qt3DRender::Render::ComputeCommand is created at the first use,
    not by 'Qt3DRender::Render::ComputeCommand(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::Render::ComputeCommand.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::Render::ComputeCommand'

  #  A C++ Qt3DRender::Render::ComputeCommand Python makes is of a C++ class
  #  of ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_Render_ComputeCommand'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def x(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::Render::ComputeCommand::x() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-computecommand.html#x
    """
    #  int Qt3DRender::Render::ComputeCommand::x() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render14ComputeCommand1xEv',
    )

  def y(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::Render::ComputeCommand::y() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-computecommand.html#y
    """
    #  int Qt3DRender::Render::ComputeCommand::y() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render14ComputeCommand1yEv',
    )

  def z(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::Render::ComputeCommand::z() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-computecommand.html#z
    """
    #  int Qt3DRender::Render::ComputeCommand::z() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render14ComputeCommand1zEv',
    )

  def frameCount(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::Render::ComputeCommand::frameCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-computecommand.html#frameCount
    """
    #  int Qt3DRender::Render::ComputeCommand::frameCount() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render14ComputeCommand10frameCountEv',
    )

  def runType(self) -> Qt3DRender.QComputeCommand.RunType:
    """
    Calls Qt's 'QComputeCommand::RunType
    Qt3DRender::Render::ComputeCommand::runType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-computecommand.html#runType

    Returns
    -------

    Qt3DRender.QComputeCommand.RunType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt3DRender.QComputeCommand.RunType(number)' gives.
    """
    #  QComputeCommand::RunType Qt3DRender::Render::ComputeCommand::runType()
    #      const
    return Qt3DRender.QComputeCommand.RunType(self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render14ComputeCommand7runTypeEv',
    ))

  def hasReachedFrameCount(self) -> bool:
    """
    Calls Qt's 'bool
    Qt3DRender::Render::ComputeCommand::hasReachedFrameCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-computecommand.html
    """
    #  bool Qt3DRender::Render::ComputeCommand::hasReachedFrameCount() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render14ComputeCommand20hasReachedFrameCoun'
        'tEv',
    )

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::Render::ComputeCommand::ComputeCommand()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-computecommand.html
    """
    #  Qt3DRender::Render::ComputeCommand::ComputeCommand()
    self._noteCreation(ComputeCommand, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender6Render14ComputeCommandC1Ev',
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

  def cleanup(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::ComputeCommand::cleanup()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-computecommand.html#cleanup
    """
    #  void Qt3DRender::Render::ComputeCommand::cleanup()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render14ComputeCommand7cleanupEv',
    )

  @overload(WAIT['Qt3DCore.QNode'], bool)
  @overload(NoneType, bool)
  def syncFromFrontEnd(
      self,
      frontEnd: Optional[Qt3DCore.QNode],
      firstTime: bool,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::ComputeCommand::syncFromFrontEnd(const
    Qt3DCore::QNode *frontEnd, bool firstTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-computecommand.html

    Parameters
    ----------

    frontEnd : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    firstTime : bool
      Passed on as it is.
    """
    #  void Qt3DRender::Render::ComputeCommand::syncFromFrontEnd(const
    #      Qt3DCore::QNode *frontEnd, bool firstTime)
    ritual = (
        'ritual_ZN10Qt3DRender6Render14ComputeCommand16syncFromFrontEndEPKN'
        '8Qt3DCore5QNodeEb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10Qt3DRender6Render14ComputeCommand16syncFromFrontE'
          'ndEPKN8Qt3DCore5QNodeEb')
    self.uglySide.call(ritual, self._addressOf(frontEnd), firstTime)

  def updateFrameCount(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::ComputeCommand::updateFrameCount()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-computecommand.html
    """
    #  void Qt3DRender::Render::ComputeCommand::updateFrameCount()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render14ComputeCommand16updateFrameCountEv',
    )

  def resetHasReachedFrameCount(self) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::ComputeCommand::resetHasReachedFrameCount()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-computecommand.html
    """
    #  void Qt3DRender::Render::ComputeCommand::resetHasReachedFrameCount()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render14ComputeCommand25resetHasReachedFrame'
        'CountEv',
    )
