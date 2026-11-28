"""
Qt3DRender::Render::JointInfo binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/skeletondata_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means Qt3DRender::Render::JointInfo to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class JointInfo(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's Qt3DRender::Render::JointInfo: a plain Python object
  standing in front of one C++ Qt3DRender::Render::JointInfo.

  C++ hands a Qt3DRender::Render::JointInfo around as a copy, so every C++
  Qt3DRender::Render::JointInfo behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  No function of Qt's Qt3DRender::Render::JointInfo yet. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DRender::Render::JointInfo::~JointInfo()': the destructor:
    Python removes its C++ Qt3DRender::Render::JointInfo by it, and has no
    other use for it.

  What to expect
  --------------

  - The C++ Qt3DRender::Render::JointInfo is created at the first use, not by
    'Qt3DRender::Render::JointInfo(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a Qt3DRender::Render::JointInfo back gives a copy the
    ritual made for Python, in a new cute Qt3DRender::Render::JointInfo.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::Render::JointInfo'

  #  Qt's '~Qt3DRender::Render::JointInfo()'. Naming it makes this a value
  #  class: Python owns every C++ Qt3DRender::Render::JointInfo behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN10Qt3DRender6Render9JointInfoD1Ev'

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::Render::JointInfo::JointInfo()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-jointinfo.html#JointInfo
    """
    #  Qt3DRender::Render::JointInfo::JointInfo()
    self._noteCreation(JointInfo, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender6Render9JointInfoC1Ev',
    ))

  @overload(WAIT['Qt3DRender.Render.Joint'], int)
  @overload(NoneType, int)
  def __init__(
      self,
      joint: Optional[Qt3DRender.Render.Joint],
      parentJointIndex: int,
  ) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::Render::JointInfo::JointInfo(Joint *joint, int
    parentJointIndex)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-jointinfo.html#JointInfo

    Parameters
    ----------

    joint : Optional[Qt3DRender.Render.Joint]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parentJointIndex : int
      Passed on as it is.
    """
    #  Qt3DRender::Render::JointInfo::JointInfo(Joint *joint, int
    #      parentJointIndex)
    self._noteCreation(JointInfo, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender6Render9JointInfoC1EPNS0_5JointEi',
        self._addressOf(joint), parentJointIndex,
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
