"""
QInternal binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qnamespace.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute


class QInternal(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QInternal: a plain Python object standing in front of
  one C++ QInternal.

  C++ hands a QInternal around as a copy, so every C++ QInternal behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QInternal yet. None can be made from Python: one comes
  out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QInternal::~QInternal()': the destructor: Python removes its C++
    QInternal by it, and has no other use for it.

  What has no ritual
  ------------------

  3 of the 4 functions Qt declares: 3 takes or gives a type that cannot be
  passed yet.

  What to expect
  --------------

  - The C++ QInternal is created at the first use, not by 'QInternal(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QInternal back gives a copy the ritual made for
    Python, in a new cute QInternal.
  """

  #  The enums Qt writes inside QInternal, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class CallMode(CuteNum):
    """
    The enum 'QInternal::CallMode' of Qt, with the 2 names Qt gives in it.
    """

    Testing = Kee[int](0)
    Live = Kee[int](1)

  class Callback(CuteNum):
    """
    The enum 'QInternal::Callback' of Qt, with the 2 names Qt gives in it.
    """

    EventNotifyCallback = Kee[int](0)
    LastCallback = Kee[int](1)

  class DockPosition(CuteNum):
    """
    The enum 'QInternal::DockPosition' of Qt, with the 5 names Qt gives in
    it.
    """

    LeftDock = Kee[int](0)
    RightDock = Kee[int](1)
    TopDock = Kee[int](2)
    BottomDock = Kee[int](3)
    DockCount = Kee[int](4)

  class PaintDeviceFlags(CuteNum):
    """
    The enum 'QInternal::PaintDeviceFlags' of Qt, with the 11 names Qt gives
    in it.
    """

    UnknownDevice = Kee[int](0)
    Widget = Kee[int](1)
    Pixmap = Kee[int](2)
    Image = Kee[int](3)
    Printer = Kee[int](4)
    Picture = Kee[int](5)
    Pbuffer = Kee[int](6)
    FramebufferObject = Kee[int](7)
    CustomRaster = Kee[int](8)
    PaintBuffer = Kee[int](10)
    OpenGL = Kee[int](11)

  class RelayoutType(CuteNum):
    """
    The enum 'QInternal::RelayoutType' of Qt, with the 3 names Qt gives in
    it.
    """

    RelayoutNormal = Kee[int](0)
    RelayoutDragging = Kee[int](1)
    RelayoutDropped = Kee[int](2)

  class SaveStateRule(CuteNum):
    """
    The enum 'QInternal::SaveStateRule' of Qt, with the 2 names Qt gives in
    it.
    """

    KeepSavedState = Kee[int](0)
    ClearSavedState = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QInternal'

  #  Qt's '~QInternal()'. Naming it makes this a value class: Python owns
  #  every C++ QInternal behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN9QInternalD1Ev'

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
