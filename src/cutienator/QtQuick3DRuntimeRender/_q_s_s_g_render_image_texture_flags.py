"""
QSSGRenderImageTextureFlags binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderimagetexture_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGRenderImageTextureFlags to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute


class QSSGRenderImageTextureFlags(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSSGRenderImageTextureFlags: a plain Python object
  standing in front of one C++ QSSGRenderImageTextureFlags.

  C++ hands a QSSGRenderImageTextureFlags around as a copy, so every C++
  QSSGRenderImageTextureFlags behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QSSGRenderImageTextureFlags that has a ritual and
  that Python can call so far, 8 names in all: 'hasTransparency',
  'setHasTransparency', 'isRgbe8', 'setRgbe8', 'isLinear', 'setLinear',
  'isPreMultipliedAlpha', 'setPreMultipliedAlpha'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSSGRenderImageTextureFlags::~QSSGRenderImageTextureFlags()': the
    destructor: Python removes its C++ QSSGRenderImageTextureFlags by it, and
    has no other use for it.

  What to expect
  --------------

  - The C++ QSSGRenderImageTextureFlags is created at the first use, not by
    'QSSGRenderImageTextureFlags(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSSGRenderImageTextureFlags back gives a copy the
    ritual made for Python, in a new cute QSSGRenderImageTextureFlags.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGRenderImageTextureFlags'

  #  Qt's '~QSSGRenderImageTextureFlags()'. Naming it makes this a value
  #  class: Python owns every C++ QSSGRenderImageTextureFlags behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN27QSSGRenderImageTextureFlagsD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def hasTransparency(self) -> bool:
    """
    Calls Qt's 'bool QSSGRenderImageTextureFlags::hasTransparency() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderimagetextureflags.html#hasTransparency
    """
    #  bool QSSGRenderImageTextureFlags::hasTransparency() const
    return self.uglySide.call(
        'ritual_ZNK27QSSGRenderImageTextureFlags15hasTransparencyEv',
    )

  def isRgbe8(self) -> bool:
    """
    Calls Qt's 'bool QSSGRenderImageTextureFlags::isRgbe8() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderimagetextureflags.html#isRgbe8
    """
    #  bool QSSGRenderImageTextureFlags::isRgbe8() const
    return self.uglySide.call(
        'ritual_ZNK27QSSGRenderImageTextureFlags7isRgbe8Ev',
    )

  def isLinear(self) -> bool:
    """
    Calls Qt's 'bool QSSGRenderImageTextureFlags::isLinear() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderimagetextureflags.html#isLinear
    """
    #  bool QSSGRenderImageTextureFlags::isLinear() const
    return self.uglySide.call(
        'ritual_ZNK27QSSGRenderImageTextureFlags8isLinearEv',
    )

  def isPreMultipliedAlpha(self) -> bool:
    """
    Calls Qt's 'bool QSSGRenderImageTextureFlags::isPreMultipliedAlpha()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderimagetextureflags.html
    """
    #  bool QSSGRenderImageTextureFlags::isPreMultipliedAlpha() const
    return self.uglySide.call(
        'ritual_ZNK27QSSGRenderImageTextureFlags20isPreMultipliedAlphaEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setHasTransparency(self, inValue: bool) -> None:
    """
    Calls Qt's 'void QSSGRenderImageTextureFlags::setHasTransparency(bool
    inValue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderimagetextureflags.html

    Parameters
    ----------

    inValue : bool
      Passed on as it is.
    """
    #  void QSSGRenderImageTextureFlags::setHasTransparency(bool inValue)
    self.uglySide.call(
        'ritual_ZN27QSSGRenderImageTextureFlags18setHasTransparencyEb',
        inValue,
    )

  @overload(bool)
  def setRgbe8(self, inValue: bool) -> None:
    """
    Calls Qt's 'void QSSGRenderImageTextureFlags::setRgbe8(bool inValue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderimagetextureflags.html#setRgbe8

    Parameters
    ----------

    inValue : bool
      Passed on as it is.
    """
    #  void QSSGRenderImageTextureFlags::setRgbe8(bool inValue)
    self.uglySide.call(
        'ritual_ZN27QSSGRenderImageTextureFlags8setRgbe8Eb', inValue,
    )

  @overload(bool)
  def setLinear(self, inValue: bool) -> None:
    """
    Calls Qt's 'void QSSGRenderImageTextureFlags::setLinear(bool inValue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderimagetextureflags.html#setLinear

    Parameters
    ----------

    inValue : bool
      Passed on as it is.
    """
    #  void QSSGRenderImageTextureFlags::setLinear(bool inValue)
    self.uglySide.call(
        'ritual_ZN27QSSGRenderImageTextureFlags9setLinearEb', inValue,
    )

  @overload(bool)
  def setPreMultipliedAlpha(self, inValue: bool) -> None:
    """
    Calls Qt's 'void QSSGRenderImageTextureFlags::setPreMultipliedAlpha(bool
    inValue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderimagetextureflags.html

    Parameters
    ----------

    inValue : bool
      Passed on as it is.
    """
    #  void QSSGRenderImageTextureFlags::setPreMultipliedAlpha(bool inValue)
    self.uglySide.call(
        'ritual_ZN27QSSGRenderImageTextureFlags21setPreMultipliedAlphaEb',
        inValue,
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
