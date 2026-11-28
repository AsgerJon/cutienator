"""
QOpenGLGlyphTexture binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpenGL/6.12.0/QtOpenGL/private/qopengltextureglyphcache_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QOpenGLGlyphTexture to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtGui import QOpenGLSharedResource

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


class QOpenGLGlyphTexture(QOpenGLSharedResource):
  """
  The cute side of Qt's QOpenGLGlyphTexture: a plain Python object standing
  in front of one C++ QOpenGLGlyphTexture.

  It is built on the cute 'QOpenGLSharedResource', as Qt's
  QOpenGLGlyphTexture is built on Qt's QOpenGLSharedResource, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QOpenGLGlyphTexture that has a ritual and that
  Python can call so far, 2 names in all: 'freeResource',
  'invalidateResource'. It can be made from Python, in 1 way; see '__init__'.

  What to expect
  --------------

  - The C++ QOpenGLGlyphTexture is created at the first use, not by
    'QOpenGLGlyphTexture(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QOpenGLGlyphTexture.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpenGLGlyphTexture'

  #  A C++ QOpenGLGlyphTexture Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QOpenGLGlyphTexture'

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

  @overload(QOpenGLContext)
  @overload(NoneType)
  def __init__(self, ctx: Optional[QOpenGLContext]) -> None:
    """
    Notes what was given, for Qt's
    'QOpenGLGlyphTexture::QOpenGLGlyphTexture(QOpenGLContext *ctx)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglglyphtexture.html#QOpenGLGlyphTexture

    Parameters
    ----------

    ctx : Optional[QOpenGLContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QOpenGLGlyphTexture::QOpenGLGlyphTexture(QOpenGLContext *ctx)
    self._noteCreation(QOpenGLGlyphTexture, lambda: Rituals.call(
        'ritual_ZN19QOpenGLGlyphTextureC1EP14QOpenGLContext',
        self._addressOf(ctx),
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

  @overload(QOpenGLContext)
  @overload(NoneType)
  def freeResource(self, context: Optional[QOpenGLContext]) -> None:
    """
    Calls Qt's 'void QOpenGLGlyphTexture::freeResource(QOpenGLContext
    *context)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglglyphtexture.html#freeResource

    Parameters
    ----------

    context : Optional[QOpenGLContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QOpenGLGlyphTexture::freeResource(QOpenGLContext *context)
    ritual = 'ritual_ZN19QOpenGLGlyphTexture12freeResourceEP14QOpenGLContext'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QOpenGLGlyphTexture12freeResourceEP14QOpenGLConte'
          'xt')
    self.uglySide.call(ritual, self._addressOf(context))

  def invalidateResource(self) -> None:
    """
    Calls Qt's 'void QOpenGLGlyphTexture::invalidateResource()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglglyphtexture.html#invalidateResource
    """
    #  void QOpenGLGlyphTexture::invalidateResource()
    ritual = 'ritual_ZN19QOpenGLGlyphTexture18invalidateResourceEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QOpenGLGlyphTexture18invalidateResourceEv'
    self.uglySide.call(ritual)
