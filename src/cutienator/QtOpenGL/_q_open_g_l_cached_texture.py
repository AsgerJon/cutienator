"""
QOpenGLCachedTexture binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpenGL/6.12.0/QtOpenGL/private/qopengltexturecache_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QOpenGLCachedTexture to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QOpenGLTextureUploader

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtGui import QOpenGLContext
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QOpenGLContext = WAIT['QOpenGLContext']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QOpenGLCachedTexture(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QOpenGLCachedTexture: a plain Python object standing
  in front of one C++ QOpenGLCachedTexture.

  C++ hands a QOpenGLCachedTexture around as a copy, so every C++
  QOpenGLCachedTexture behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QOpenGLCachedTexture that has a ritual and that
  Python can call so far, 2 names in all: 'id', 'options'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QOpenGLCachedTexture::~QOpenGLCachedTexture()': the destructor:
    Python removes its C++ QOpenGLCachedTexture by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QOpenGLCachedTexture is created at the first use, not by
    'QOpenGLCachedTexture(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QOpenGLCachedTexture back gives a copy the ritual
    made for Python, in a new cute QOpenGLCachedTexture.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpenGLCachedTexture'

  #  Qt's '~QOpenGLCachedTexture()'. Naming it makes this a value class:
  #  Python owns every C++ QOpenGLCachedTexture behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN20QOpenGLCachedTextureD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def id(self) -> int:
    """
    Calls Qt's 'GLuint QOpenGLCachedTexture::id() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglcachedtexture.html#id
    """
    #  GLuint QOpenGLCachedTexture::id() const
    return self.uglySide.call('ritual_ZNK20QOpenGLCachedTexture2idEv')

  def options(self) -> QOpenGLTextureUploader.BindOptions:
    """
    Calls Qt's 'QOpenGLTextureUploader::BindOptions
    QOpenGLCachedTexture::options() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglcachedtexture.html#options

    Returns
    -------

    QOpenGLTextureUploader.BindOptions
      The value standing for the combination Qt gave back.
    """
    #  QOpenGLTextureUploader::BindOptions QOpenGLCachedTexture::options()
    #      const
    return QOpenGLTextureUploader.BindOptions(self.uglySide.call(
        'ritual_ZNK20QOpenGLCachedTexture7optionsEv',
    ))

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

  @overload(int, QOpenGLTextureUploader.BindOptions, QOpenGLContext)
  @overload(int, QOpenGLTextureUploader.BindOptions, NoneType)
  def __init__(
      self,
      id: int,
      options: QOpenGLTextureUploader.BindOptions,
      context: Optional[QOpenGLContext],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QOpenGLCachedTexture::QOpenGLCachedTexture(GLuint id,
    QOpenGLTextureUploader::BindOptions options, QOpenGLContext *context)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglcachedtexture.html#QOpenGLCachedTexture

    Parameters
    ----------

    id : int
      Passed on as it is.

    options : QOpenGLTextureUploader.BindOptions
      Passed on as its number.

    context : Optional[QOpenGLContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QOpenGLCachedTexture::QOpenGLCachedTexture(GLuint id,
    #      QOpenGLTextureUploader::BindOptions options, QOpenGLContext
    #      *context)
    self._noteCreation(QOpenGLCachedTexture, lambda: Rituals.call(
        'ritual_ZN20QOpenGLCachedTextureC1Ej6QFlagsIN22QOpenGLTextureUpload'
        'er10BindOptionEEP14QOpenGLContext',
        id, options.value, self._addressOf(context),
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
