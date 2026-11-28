"""
QSSGRenderLight binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderlight_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGRenderLight to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum
from ..occult import Rituals
from . import QSSGRenderGraphObject, QSSGRenderNode


class QSSGRenderLight(QSSGRenderNode):
  """
  The cute side of Qt's QSSGRenderLight: a plain Python object standing in
  front of one C++ QSSGRenderLight.

  It is built on the cute 'QSSGRenderNode', as Qt's QSSGRenderLight is built
  on Qt's QSSGRenderNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSSGRenderLight that has a ritual and that Python
  can call so far, 4 names in all: 'isEnabled', 'isDirty', 'markDirty',
  'clearDirty'. It can be made from Python, in 1 way; see '__init__'.

  What to expect
  --------------

  - The C++ QSSGRenderLight is created at the first use, not by
    'QSSGRenderLight(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSSGRenderLight.
  """

  #  The enums Qt writes inside QSSGRenderLight, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class DirtyFlag(CuteNum, scoped=True):
    """
    The enum 'QSSGRenderLight::DirtyFlag' of Qt, with the 1 names Qt gives in
    it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    LightDirty = Kee[int](1)

  class SoftShadowQuality(CuteNum, scoped=True):
    """
    The enum 'QSSGRenderLight::SoftShadowQuality' of Qt, with the 6 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    Hard = Kee[int](0)
    PCF4 = Kee[int](1)
    PCF8 = Kee[int](2)
    PCF16 = Kee[int](3)
    PCF32 = Kee[int](4)
    PCF64 = Kee[int](5)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGRenderLight'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isEnabled(self) -> bool:
    """
    Calls Qt's 'bool QSSGRenderLight::isEnabled() const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrenderlight.html#isEnabled
    """
    #  bool QSSGRenderLight::isEnabled() const
    return self.uglySide.call('ritual_ZNK15QSSGRenderLight9isEnabledEv')

  @overload(DirtyFlag)
  def isDirty(self, dirtyFlag: DirtyFlag) -> bool:
    """
    Calls Qt's 'bool QSSGRenderLight::isDirty(DirtyFlag dirtyFlag) const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrenderlight.html#isDirty

    Parameters
    ----------

    dirtyFlag : DirtyFlag
      Passed on as its number.
    """
    #  bool QSSGRenderLight::isDirty(DirtyFlag dirtyFlag) const
    return self.uglySide.call(
        'ritual_ZNK15QSSGRenderLight7isDirtyENS_9DirtyFlagE',
        dirtyFlag.value,
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
  @overload(QSSGRenderGraphObject.Type)
  def __init__(
      self,
      type: QSSGRenderGraphObject.Type = (
          QSSGRenderGraphObject.Type.DirectionalLight),
  ) -> None:
    """
    Notes what was given, for Qt's 'QSSGRenderLight::QSSGRenderLight(Type
    type)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderlight.html#QSSGRenderLight

    Parameters
    ----------

    type : QSSGRenderGraphObject.Type
      Passed on as its number. May be left out, as in Qt: it is then
      QSSGRenderGraphObject.Type.DirectionalLight.
    """
    #  QSSGRenderLight::QSSGRenderLight(Type type)
    self._noteCreation(QSSGRenderLight, lambda: Rituals.call(
        'ritual_ZN15QSSGRenderLightC1EN21QSSGRenderGraphObject4TypeE',
        type.value,
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

  @overload(DirtyFlag)
  def markDirty(self, dirtyFlag: DirtyFlag) -> None:
    """
    Calls Qt's 'void QSSGRenderLight::markDirty(DirtyFlag dirtyFlag)'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrenderlight.html#markDirty

    Parameters
    ----------

    dirtyFlag : DirtyFlag
      Passed on as its number.
    """
    #  void QSSGRenderLight::markDirty(DirtyFlag dirtyFlag)
    self.uglySide.call(
        'ritual_ZN15QSSGRenderLight9markDirtyENS_9DirtyFlagE',
        dirtyFlag.value,
    )

  @overload(DirtyFlag)
  def clearDirty(self, dirtyFlag: DirtyFlag) -> None:
    """
    Calls Qt's 'void QSSGRenderLight::clearDirty(DirtyFlag dirtyFlag)'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrenderlight.html#clearDirty

    Parameters
    ----------

    dirtyFlag : DirtyFlag
      Passed on as its number.
    """
    #  void QSSGRenderLight::clearDirty(DirtyFlag dirtyFlag)
    self.uglySide.call(
        'ritual_ZN15QSSGRenderLight10clearDirtyENS_9DirtyFlagE',
        dirtyFlag.value,
    )
