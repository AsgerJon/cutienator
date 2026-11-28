"""
Qt3DRender::Render::ObjectPicker binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/objectpicker_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means Qt3DRender::Render::ObjectPicker to be private: it declares the
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


class ObjectPicker(Qt3DRender.Render.BackendNode):
  """
  The cute side of Qt's Qt3DRender::Render::ObjectPicker: a plain Python
  object standing in front of one C++ Qt3DRender::Render::ObjectPicker.

  It is built on the cute 'Qt3DRender::Render::BackendNode', as Qt's
  Qt3DRender::Render::ObjectPicker is built on Qt's
  Qt3DRender::Render::BackendNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::Render::ObjectPicker that has a ritual
  and that Python can call so far, 9 names in all: 'cleanup',
  'syncFromFrontEnd', 'isPressed', 'isHoverEnabled', 'isDragEnabled',
  'setPressed', 'setPriority', 'priority', 'notifyJob'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DRender::Render::ObjectPicker::~ObjectPicker()': the destructor:
    Python never removes a C++ Qt3DRender::Render::ObjectPicker.

  What to expect
  --------------

  - The C++ Qt3DRender::Render::ObjectPicker is created at the first use, not
    by 'Qt3DRender::Render::ObjectPicker(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::Render::ObjectPicker.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::Render::ObjectPicker'

  #  A C++ Qt3DRender::Render::ObjectPicker Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_Render_ObjectPicker'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isPressed(self) -> bool:
    """
    Calls Qt's 'bool Qt3DRender::Render::ObjectPicker::isPressed() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-objectpicker.html#isPressed
    """
    #  bool Qt3DRender::Render::ObjectPicker::isPressed() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render12ObjectPicker9isPressedEv',
    )

  def isHoverEnabled(self) -> bool:
    """
    Calls Qt's 'bool Qt3DRender::Render::ObjectPicker::isHoverEnabled()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-objectpicker.html#isHoverEnabled
    """
    #  bool Qt3DRender::Render::ObjectPicker::isHoverEnabled() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render12ObjectPicker14isHoverEnabledEv',
    )

  def isDragEnabled(self) -> bool:
    """
    Calls Qt's 'bool Qt3DRender::Render::ObjectPicker::isDragEnabled()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-objectpicker.html#isDragEnabled
    """
    #  bool Qt3DRender::Render::ObjectPicker::isDragEnabled() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render12ObjectPicker13isDragEnabledEv',
    )

  def priority(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::Render::ObjectPicker::priority() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-objectpicker.html#priority
    """
    #  int Qt3DRender::Render::ObjectPicker::priority() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render12ObjectPicker8priorityEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setPressed(self, pressed: bool) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::ObjectPicker::setPressed(bool
    pressed)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-objectpicker.html#setPressed

    Parameters
    ----------

    pressed : bool
      Passed on as it is.
    """
    #  void Qt3DRender::Render::ObjectPicker::setPressed(bool pressed)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render12ObjectPicker10setPressedEb', pressed,
    )

  @overload(int)
  def setPriority(self, priority: int) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::ObjectPicker::setPriority(int
    priority)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-objectpicker.html#setPriority

    Parameters
    ----------

    priority : int
      Passed on as it is.
    """
    #  void Qt3DRender::Render::ObjectPicker::setPriority(int priority)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render12ObjectPicker11setPriorityEi',
        priority,
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
    'Qt3DRender::Render::ObjectPicker::ObjectPicker()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-objectpicker.html#ObjectPicker
    """
    #  Qt3DRender::Render::ObjectPicker::ObjectPicker()
    self._noteCreation(ObjectPicker, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender6Render12ObjectPickerC1Ev',
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
    Calls Qt's 'void Qt3DRender::Render::ObjectPicker::cleanup()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-objectpicker.html#cleanup
    """
    #  void Qt3DRender::Render::ObjectPicker::cleanup()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render12ObjectPicker7cleanupEv',
    )

  @overload(WAIT['Qt3DCore.QNode'], bool)
  @overload(NoneType, bool)
  def syncFromFrontEnd(
      self,
      frontEnd: Optional[Qt3DCore.QNode],
      firstTime: bool,
  ) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::ObjectPicker::syncFromFrontEnd(const
    Qt3DCore::QNode *frontEnd, bool firstTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-objectpicker.html

    Parameters
    ----------

    frontEnd : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    firstTime : bool
      Passed on as it is.
    """
    #  void Qt3DRender::Render::ObjectPicker::syncFromFrontEnd(const
    #      Qt3DCore::QNode *frontEnd, bool firstTime)
    ritual = (
        'ritual_ZN10Qt3DRender6Render12ObjectPicker16syncFromFrontEndEPKN8Q'
        't3DCore5QNodeEb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10Qt3DRender6Render12ObjectPicker16syncFromFrontEnd'
          'EPKN8Qt3DCore5QNodeEb')
    self.uglySide.call(ritual, self._addressOf(frontEnd), firstTime)

  def notifyJob(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::ObjectPicker::notifyJob()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-objectpicker.html#notifyJob
    """
    #  void Qt3DRender::Render::ObjectPicker::notifyJob()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render12ObjectPicker9notifyJobEv',
    )
