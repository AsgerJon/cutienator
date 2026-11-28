"""
QtMultimediaPrivate::DmaBufEglContext binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/6.12.0/QtMultimedia/private/qdmabuftextureimporter_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QtMultimediaPrivate::DmaBufEglContext to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtGui import QOpenGLContext, QRhi
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRhi = WAIT['QRhi']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class DmaBufEglContext(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QtMultimediaPrivate::DmaBufEglContext: a plain Python
  object standing in front of one C++ QtMultimediaPrivate::DmaBufEglContext.

  C++ hands a QtMultimediaPrivate::DmaBufEglContext around as a copy, so
  every C++ QtMultimediaPrivate::DmaBufEglContext behind a cute one is
  Python's own: it is removed, by the ritual named in '__delete_ritual__',
  when the cute object goes.

  What exists
  -----------

  Every function of Qt's QtMultimediaPrivate::DmaBufEglContext that has a
  ritual and that Python can call so far, 3 names in all: 'isValid',
  'invalidate', 'glContext'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'EGLDisplay QtMultimediaPrivate::DmaBufEglContext::eglDisplay()
    const': gives 'void', which has no cute class yet.
  - Qt's 'QtMultimediaPrivate::DmaBufEglContext::~DmaBufEglContext()': the
    destructor: Python removes its C++ QtMultimediaPrivate::DmaBufEglContext
    by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QtMultimediaPrivate::DmaBufEglContext is created at the first
    use, not by 'QtMultimediaPrivate::DmaBufEglContext(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QtMultimediaPrivate::DmaBufEglContext back gives a
    copy the ritual made for Python, in a new cute
    QtMultimediaPrivate::DmaBufEglContext.
  - Each name of Qt's QtMultimediaPrivate::DmaBufEglContext that has no cute
    function yet, 'eglDisplay', holds a function that raises
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
  __qt_class__ = 'QtMultimediaPrivate::DmaBufEglContext'

  #  Qt's '~QtMultimediaPrivate::DmaBufEglContext()'. Naming it makes this a
  #  value class: Python owns every C++ QtMultimediaPrivate::DmaBufEglContext
  #  behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN19QtMultimediaPrivate16DmaBufEglContextD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QtMultimediaPrivate::DmaBufEglContext::isValid() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtmultimediaprivate-dmabufeglcontext.html#isValid
    """
    #  bool QtMultimediaPrivate::DmaBufEglContext::isValid() const
    return self.uglySide.call(
        'ritual_ZNK19QtMultimediaPrivate16DmaBufEglContext7isValidEv',
    )

  def glContext(self) -> Optional[QOpenGLContext]:
    """
    Calls Qt's 'QOpenGLContext
    *QtMultimediaPrivate::DmaBufEglContext::glContext() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtmultimediaprivate-dmabufeglcontext.html

    Returns
    -------

    Optional[QOpenGLContext]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QOpenGLContext *QtMultimediaPrivate::DmaBufEglContext::glContext()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK19QtMultimediaPrivate16DmaBufEglContext9glContextEv',
    )
    from ..QtGui import QOpenGLContext
    return QOpenGLContext._cuteAt(address)

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

  @overload(QRhi)
  @overload(NoneType)
  def __init__(self, rhi: Optional[QRhi]) -> None:
    """
    Notes what was given, for Qt's
    'QtMultimediaPrivate::DmaBufEglContext::DmaBufEglContext(QRhi *rhi)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtmultimediaprivate-dmabufeglcontext.html

    Parameters
    ----------

    rhi : Optional[QRhi]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QtMultimediaPrivate::DmaBufEglContext::DmaBufEglContext(QRhi *rhi)
    self._noteCreation(DmaBufEglContext, lambda: Rituals.call(
        'ritual_ZN19QtMultimediaPrivate16DmaBufEglContextC1EP4QRhi',
        self._addressOf(rhi),
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

  def invalidate(self) -> None:
    """
    Calls Qt's 'void QtMultimediaPrivate::DmaBufEglContext::invalidate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtmultimediaprivate-dmabufeglcontext.html
    """
    #  void QtMultimediaPrivate::DmaBufEglContext::invalidate()
    self.uglySide.call(
        'ritual_ZN19QtMultimediaPrivate16DmaBufEglContext10invalidateEv',
    )

  @staticmethod
  def eglDisplay(*__, **_) -> Never:
    """
    Qt's 'EGLDisplay QtMultimediaPrivate::DmaBufEglContext::eglDisplay()
    const': gives 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QtMultimediaPrivate.DmaBufEglContext.eglDisplay' has no cute "
        "function yet. Qt's 'EGLDisplay "
        "QtMultimediaPrivate::DmaBufEglContext::eglDisplay() const': gives "
        "'void', which has no cute class yet.")
