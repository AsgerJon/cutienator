"""
Qt3DRender::Render::SkeletonManager binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/managers_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means Qt3DRender::Render::SkeletonManager to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class SkeletonManager(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's Qt3DRender::Render::SkeletonManager: a plain Python
  object standing in front of one C++ Qt3DRender::Render::SkeletonManager.

  What exists
  -----------

  No function of Qt's Qt3DRender::Render::SkeletonManager yet. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void
    Qt3DRender::Render::SkeletonManager::addDirtySkeleton(DirtyFlag
    dirtyFlag, HSkeleton skeletonHandle)': takes a type Python has no way to
    hand over yet.
  - Qt's 'QList<HSkeleton>
    Qt3DRender::Render::SkeletonManager::takeDirtySkeletons(DirtyFlag
    dirtyFlag)': gives a type Python has no way to take yet.

  What to expect
  --------------

  - The C++ Qt3DRender::Render::SkeletonManager is created at the first use,
    not by 'Qt3DRender::Render::SkeletonManager(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::Render::SkeletonManager.
  - Each name of Qt's Qt3DRender::Render::SkeletonManager that has no cute
    function yet, 'addDirtySkeleton', 'takeDirtySkeletons', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside Qt3DRender::Render::SkeletonManager, each a
  #  class in here as in C++, and the names Qt has for the combinations of
  #  its flags enums.

  class DirtyFlag(CuteNum):
    """
    The enum 'Qt3DRender::Render::SkeletonManager::DirtyFlag' of Qt, with the
    2 names Qt gives in it.
    """

    SkeletonDataDirty = Kee[int](0)
    SkeletonTransformsDirty = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::Render::SkeletonManager'

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

  @staticmethod
  def addDirtySkeleton(*__, **_) -> Never:
    """
    Qt's 'void
    Qt3DRender::Render::SkeletonManager::addDirtySkeleton(DirtyFlag
    dirtyFlag, HSkeleton skeletonHandle)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.SkeletonManager.addDirtySkeleton' has no cute "
        "function yet. Qt's 'void "
        "Qt3DRender::Render::SkeletonManager::addDirtySkeleton(DirtyFlag "
        "dirtyFlag, HSkeleton skeletonHandle)': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def takeDirtySkeletons(*__, **_) -> Never:
    """
    Qt's 'QList<HSkeleton>
    Qt3DRender::Render::SkeletonManager::takeDirtySkeletons(DirtyFlag
    dirtyFlag)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.SkeletonManager.takeDirtySkeletons' has no cute "
        "function yet. Qt's 'QList<HSkeleton> "
        "Qt3DRender::Render::SkeletonManager::takeDirtySkeletons(DirtyFlag "
        "dirtyFlag)': gives a type Python has no way to take yet.")
