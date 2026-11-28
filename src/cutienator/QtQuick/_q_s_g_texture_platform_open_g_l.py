"""
QSGTexturePlatformOpenGL binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsgtexture_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QSGTexturePlatformOpenGL to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QNativeInterface

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QSGTexture
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSGTexture = WAIT['QSGTexture']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSGTexturePlatformOpenGL(QNativeInterface.QSGOpenGLTexture):
  """
  The cute side of Qt's QSGTexturePlatformOpenGL: a plain Python object
  standing in front of one C++ QSGTexturePlatformOpenGL.

  It is built on the cute 'QNativeInterface::QSGOpenGLTexture', as Qt's
  QSGTexturePlatformOpenGL is built on Qt's
  QNativeInterface::QSGOpenGLTexture, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSGTexturePlatformOpenGL that has a ritual and that
  Python can call so far, 1 name in all: 'nativeTexture'. It can be made from
  Python, in 1 way; see '__init__'.

  What to expect
  --------------

  - The C++ QSGTexturePlatformOpenGL is created at the first use, not by
    'QSGTexturePlatformOpenGL(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGTexturePlatformOpenGL.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGTexturePlatformOpenGL'

  #  A C++ QSGTexturePlatformOpenGL Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSGTexturePlatformOpenGL'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def nativeTexture(self) -> int:
    """
    Calls Qt's 'uint QSGTexturePlatformOpenGL::nativeTexture() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgtextureplatformopengl.html#nativeTexture
    """
    #  uint QSGTexturePlatformOpenGL::nativeTexture() const
    ritual = 'ritual_ZNK24QSGTexturePlatformOpenGL13nativeTextureEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK24QSGTexturePlatformOpenGL13nativeTextureEv'
    return self.uglySide.call(ritual)

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

  @overload(QSGTexture)
  @overload(NoneType)
  def __init__(self, t: Optional[QSGTexture]) -> None:
    """
    Notes what was given, for Qt's
    'QSGTexturePlatformOpenGL::QSGTexturePlatformOpenGL(QSGTexture *t)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgtextureplatformopengl.html

    Parameters
    ----------

    t : Optional[QSGTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QSGTexturePlatformOpenGL::QSGTexturePlatformOpenGL(QSGTexture *t)
    self._noteCreation(QSGTexturePlatformOpenGL, lambda: Rituals.call(
        'ritual_ZN24QSGTexturePlatformOpenGLC1EP10QSGTexture',
        self._addressOf(t),
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
