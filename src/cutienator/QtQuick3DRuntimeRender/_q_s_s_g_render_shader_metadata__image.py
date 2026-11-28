"""
QSSGRenderShaderMetadata::Image binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendershadermetadata_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGRenderShaderMetadata::Image to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..occult import Rituals
from . import QSSGRenderShaderMetadata


class Image(QSSGRenderShaderMetadata.Uniform):
  """
  The cute side of Qt's QSSGRenderShaderMetadata::Image: a plain Python
  object standing in front of one C++ QSSGRenderShaderMetadata::Image.

  It is built on the cute 'QSSGRenderShaderMetadata::Uniform', as Qt's
  QSSGRenderShaderMetadata::Image is built on Qt's
  QSSGRenderShaderMetadata::Uniform, and has everything that class has.

  C++ hands a QSSGRenderShaderMetadata::Image around as a copy, so every C++
  QSSGRenderShaderMetadata::Image behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  No function of Qt's QSSGRenderShaderMetadata::Image yet. It can be made
  from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSSGRenderShaderMetadata::Image::~Image()': the destructor: Python
    removes its C++ QSSGRenderShaderMetadata::Image by it, and has no other
    use for it.

  What to expect
  --------------

  - The C++ QSSGRenderShaderMetadata::Image is created at the first use, not
    by 'QSSGRenderShaderMetadata::Image(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSSGRenderShaderMetadata::Image back gives a copy the
    ritual made for Python, in a new cute QSSGRenderShaderMetadata::Image.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGRenderShaderMetadata::Image'

  #  Qt's '~QSSGRenderShaderMetadata::Image()'. Naming it makes this a value
  #  class: Python owns every C++ QSSGRenderShaderMetadata::Image behind a
  #  cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN24QSSGRenderShaderMetadata5ImageD1Ev'

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
    'QSSGRenderShaderMetadata::Image::Image()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrendershadermetadata-image.html#Image
    """
    #  QSSGRenderShaderMetadata::Image::Image()
    self._noteCreation(Image, lambda: Rituals.call(
        'ritual_ZN24QSSGRenderShaderMetadata5ImageC1Ev',
    ))

  @overload(QSSGRenderShaderMetadata.Uniform)
  def __init__(self, u: QSSGRenderShaderMetadata.Uniform) -> None:
    """
    Notes what was given, for Qt's
    'QSSGRenderShaderMetadata::Image::Image(const Uniform &u)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrendershadermetadata-image.html#Image

    Parameters
    ----------

    u : QSSGRenderShaderMetadata.Uniform
      Passed on as a value: Qt reads the C++
      QSSGRenderShaderMetadata::Uniform, which stays Python's own.
    """
    #  QSSGRenderShaderMetadata::Image::Image(const Uniform &u)
    self._noteCreation(Image, lambda: Rituals.call(
        'ritual_ZN24QSSGRenderShaderMetadata5ImageC1ERKNS_7UniformE',
        self._valueOf(u),
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
