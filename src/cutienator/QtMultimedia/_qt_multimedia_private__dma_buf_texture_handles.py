"""
QtMultimediaPrivate::DmaBufTextureHandles binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/6.12.0/QtMultimedia/private/qdmabuftextureimporter_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QtMultimediaPrivate::DmaBufTextureHandles to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from . import QVideoFrameTexturesHandles

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class DmaBufTextureHandles(QVideoFrameTexturesHandles):
  """
  The cute side of Qt's QtMultimediaPrivate::DmaBufTextureHandles: a plain
  Python object standing in front of one C++
  QtMultimediaPrivate::DmaBufTextureHandles.

  It is built on the cute 'QVideoFrameTexturesHandles', as Qt's
  QtMultimediaPrivate::DmaBufTextureHandles is built on Qt's
  QVideoFrameTexturesHandles, and has everything that class has.

  C++ hands a QtMultimediaPrivate::DmaBufTextureHandles around as a copy, so
  every C++ QtMultimediaPrivate::DmaBufTextureHandles behind a cute one is
  Python's own: it is removed, by the ritual named in '__delete_ritual__',
  when the cute object goes.

  What exists
  -----------

  No function of Qt's QtMultimediaPrivate::DmaBufTextureHandles yet. None can
  be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's
    'QtMultimediaPrivate::DmaBufTextureHandles::DmaBufTextureHandles(QRhi
    &rhi, QOpenGLContext *glContext, int nPlanes, std::array<GLuint, 4>
    textures, std::shared_ptr<void> parentKeepAlive)': takes a type Python
    has no way to hand over yet.
  - Qt's
    'QtMultimediaPrivate::DmaBufTextureHandles::~DmaBufTextureHandles()': the
    destructor: Python removes its C++
    QtMultimediaPrivate::DmaBufTextureHandles by it, and has no other use for
    it.
  - Qt's 'quint64
    QtMultimediaPrivate::DmaBufTextureHandles::textureHandle(QRhi &a0, int
    plane)': takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QtMultimediaPrivate::DmaBufTextureHandles is created at the first
    use, not by 'QtMultimediaPrivate::DmaBufTextureHandles(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QtMultimediaPrivate::DmaBufTextureHandles back gives
    a copy the ritual made for Python, in a new cute
    QtMultimediaPrivate::DmaBufTextureHandles.
  - Each name of Qt's QtMultimediaPrivate::DmaBufTextureHandles that has no
    cute function yet, '__init__', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtMultimediaPrivate::DmaBufTextureHandles'

  #  Qt's '~QtMultimediaPrivate::DmaBufTextureHandles()'. Naming it makes
  #  this a value class: Python owns every C++
  #  QtMultimediaPrivate::DmaBufTextureHandles behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = (
      'ritual_ZN19QtMultimediaPrivate20DmaBufTextureHandlesD1Ev')

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's
    'QtMultimediaPrivate::DmaBufTextureHandles::DmaBufTextureHandles(QRhi
    &rhi, QOpenGLContext *glContext, int nPlanes, std::array<GLuint, 4>
    textures, std::shared_ptr<void> parentKeepAlive)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QtMultimediaPrivate.DmaBufTextureHandles.__init__' has no cute "
        "function yet. Qt's "
        "'QtMultimediaPrivate::DmaBufTextureHandles::DmaBufTextureHandles(QR"
        "hi &rhi, QOpenGLContext *glContext, int nPlanes, "
        "std::array<GLuint, 4> textures, std::shared_ptr<void> "
        "parentKeepAlive)': takes a type Python has no way to hand over yet."
    )

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
