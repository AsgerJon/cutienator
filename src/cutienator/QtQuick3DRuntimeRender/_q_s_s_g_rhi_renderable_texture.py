"""
QSSGRhiRenderableTexture binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrhicontext_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGRhiRenderableTexture to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import CuteMixin, MetaCute


class QSSGRhiRenderableTexture(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSSGRhiRenderableTexture: a plain Python object
  standing in front of one C++ QSSGRhiRenderableTexture.

  C++ hands a QSSGRhiRenderableTexture around as a copy, so every C++
  QSSGRhiRenderableTexture behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSSGRhiRenderableTexture that has a ritual and that
  Python can call so far, 3 names in all: 'isValid', 'resetRenderTarget',
  'reset'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSSGRhiRenderableTexture::~QSSGRhiRenderableTexture()': the
    destructor: Python removes its C++ QSSGRhiRenderableTexture by it, and
    has no other use for it.

  What to expect
  --------------

  - The C++ QSSGRhiRenderableTexture is created at the first use, not by
    'QSSGRhiRenderableTexture(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSSGRhiRenderableTexture back gives a copy the ritual
    made for Python, in a new cute QSSGRhiRenderableTexture.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGRhiRenderableTexture'

  #  Qt's '~QSSGRhiRenderableTexture()'. Naming it makes this a value class:
  #  Python owns every C++ QSSGRhiRenderableTexture behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN24QSSGRhiRenderableTextureD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QSSGRhiRenderableTexture::isValid() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhirenderabletexture.html#isValid
    """
    #  bool QSSGRhiRenderableTexture::isValid() const
    return self.uglySide.call(
        'ritual_ZNK24QSSGRhiRenderableTexture7isValidEv',
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

  def resetRenderTarget(self) -> None:
    """
    Calls Qt's 'void QSSGRhiRenderableTexture::resetRenderTarget()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhirenderabletexture.html#resetRenderTarget
    """
    #  void QSSGRhiRenderableTexture::resetRenderTarget()
    self.uglySide.call(
        'ritual_ZN24QSSGRhiRenderableTexture17resetRenderTargetEv',
    )

  def reset(self) -> None:
    """
    Calls Qt's 'void QSSGRhiRenderableTexture::reset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhirenderabletexture.html#reset
    """
    #  void QSSGRhiRenderableTexture::reset()
    self.uglySide.call('ritual_ZN24QSSGRhiRenderableTexture5resetEv')
