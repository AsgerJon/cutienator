"""
QSSGRenderParticles binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderparticles_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGRenderParticles to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum
from ..occult import Rituals
from . import QSSGRenderNode


class QSSGRenderParticles(QSSGRenderNode):
  """
  The cute side of Qt's QSSGRenderParticles: a plain Python object standing
  in front of one C++ QSSGRenderParticles.

  It is built on the cute 'QSSGRenderNode', as Qt's QSSGRenderParticles is
  built on Qt's QSSGRenderNode, and has everything that class has.

  What exists
  -----------

  No function of Qt's QSSGRenderParticles yet. It can be made from Python, in
  1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSSGRenderParticles::~QSSGRenderParticles()': the destructor:
    Python never removes a C++ QSSGRenderParticles.

  What has no ritual
  ------------------

  2 of the 4 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QSSGRenderParticles is created at the first use, not by
    'QSSGRenderParticles(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSSGRenderParticles.
  """

  #  The enums Qt writes inside QSSGRenderParticles, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class BlendMode(CuteNum, scoped=True):
    """
    The enum 'QSSGRenderParticles::BlendMode' of Qt, with the 3 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    SourceOver = Kee[int](0)
    Screen = Kee[int](1)
    Multiply = Kee[int](2)

  class FeatureLevel(CuteNum, scoped=True):
    """
    The enum 'QSSGRenderParticles::FeatureLevel' of Qt, with the 12 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    Simple = Kee[int](0)
    Mapped = Kee[int](1)
    Animated = Kee[int](2)
    SimpleVLight = Kee[int](3)
    MappedVLight = Kee[int](4)
    AnimatedVLight = Kee[int](5)
    Line = Kee[int](6)
    LineMapped = Kee[int](7)
    LineAnimated = Kee[int](8)
    LineVLight = Kee[int](9)
    LineMappedVLight = Kee[int](10)
    LineAnimatedVLight = Kee[int](11)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGRenderParticles'

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
    'QSSGRenderParticles::QSSGRenderParticles()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderparticles.html#QSSGRenderParticles
    """
    #  QSSGRenderParticles::QSSGRenderParticles()
    self._noteCreation(QSSGRenderParticles, lambda: Rituals.call(
        'ritual_ZN19QSSGRenderParticlesC1Ev',
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
