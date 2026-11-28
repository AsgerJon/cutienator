"""
QNativeInterface::QSGOpenGLTexture binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/qsgtexture_platform.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QQuickWindow

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QSize
  from . import QSGTexture
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSize = WAIT['QSize']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSGOpenGLTexture(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QNativeInterface::QSGOpenGLTexture: a plain Python
  object standing in front of one C++ QNativeInterface::QSGOpenGLTexture.

  What exists
  -----------

  Every function of Qt's QNativeInterface::QSGOpenGLTexture that has a ritual
  and that Python can call so far, 3 names in all: 'nativeTexture',
  'fromNative', 'fromNativeExternalOES'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QNativeInterface::QSGOpenGLTexture::~QSGOpenGLTexture()': the
    destructor: Python never removes a C++
    QNativeInterface::QSGOpenGLTexture.

  What has no ritual
  ------------------

  4 of the 9 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ QNativeInterface::QSGOpenGLTexture is created at the first use,
    not by 'QNativeInterface::QSGOpenGLTexture(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QNativeInterface::QSGOpenGLTexture.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(int, QQuickWindow, QSize)
  @overload(int, NoneType, QSize)
  @overload(int, QQuickWindow, QSize, QQuickWindow.CreateTextureOptions)
  @overload(int, NoneType, QSize, QQuickWindow.CreateTextureOptions)
  def fromNative(
      textureId: int,
      window: Optional[QQuickWindow],
      size: QSize,
      options: QQuickWindow.CreateTextureOptions = (
          QQuickWindow.CreateTextureOptions()),
  ) -> Optional[QSGTexture]:
    """
    Calls Qt's 'QSGTexture
    *QNativeInterface::QSGOpenGLTexture::fromNative(GLuint textureId,
    QQuickWindow *window, const QSize &size,
    QQuickWindow::CreateTextureOptions options)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnativeinterface-qsgopengltexture.html#fromNative

    Parameters
    ----------

    textureId : int
      Passed on as it is.

    window : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    options : QQuickWindow.CreateTextureOptions
      Passed on as its number. May be left out, as in Qt: it is then
      QQuickWindow.CreateTextureOptions().

    Returns
    -------

    Optional[QSGTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGTexture *QNativeInterface::QSGOpenGLTexture::fromNative(GLuint
    #      textureId, QQuickWindow *window, const QSize &size,
    #      QQuickWindow::CreateTextureOptions options)
    address = Rituals.call(
        'ritual_ZN16QNativeInterface16QSGOpenGLTexture10fromNativeEjP12QQui'
        'ckWindowRK5QSize6QFlagsINS1_19CreateTextureOptionEE',
        textureId, CuteMixin._addressOf(window), CuteMixin._valueOf(size),
        options.value,
    )
    from . import QSGTexture
    return QSGTexture._cuteAt(address)

  @staticmethod
  @overload(int, QQuickWindow, QSize)
  @overload(int, NoneType, QSize)
  @overload(int, QQuickWindow, QSize, QQuickWindow.CreateTextureOptions)
  @overload(int, NoneType, QSize, QQuickWindow.CreateTextureOptions)
  def fromNativeExternalOES(
      textureId: int,
      window: Optional[QQuickWindow],
      size: QSize,
      options: QQuickWindow.CreateTextureOptions = (
          QQuickWindow.CreateTextureOptions()),
  ) -> Optional[QSGTexture]:
    """
    Calls Qt's 'QSGTexture
    *QNativeInterface::QSGOpenGLTexture::fromNativeExternalOES(GLuint
    textureId, QQuickWindow *window, const QSize &size,
    QQuickWindow::CreateTextureOptions options)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnativeinterface-qsgopengltexture.html

    Parameters
    ----------

    textureId : int
      Passed on as it is.

    window : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    options : QQuickWindow.CreateTextureOptions
      Passed on as its number. May be left out, as in Qt: it is then
      QQuickWindow.CreateTextureOptions().

    Returns
    -------

    Optional[QSGTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGTexture
    #      *QNativeInterface::QSGOpenGLTexture::fromNativeExternalOES(GLuint
    #      textureId, QQuickWindow *window, const QSize &size,
    #      QQuickWindow::CreateTextureOptions options)
    address = Rituals.call(
        'ritual_ZN16QNativeInterface16QSGOpenGLTexture21fromNativeExternalO'
        'ESEjP12QQuickWindowRK5QSize6QFlagsINS1_19CreateTextureOptionEE',
        textureId, CuteMixin._addressOf(window), CuteMixin._valueOf(size),
        options.value,
    )
    from . import QSGTexture
    return QSGTexture._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QNativeInterface::QSGOpenGLTexture'

  #  A C++ QNativeInterface::QSGOpenGLTexture Python makes is of a C++ class
  #  of ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QNativeInterface_QSGOpenGLTexture'

  #  The functions Qt calls itself that QNativeInterface::QSGOpenGLTexture is
  #  the first to declare. A class of a program built on it can write one
  #  anew, and Qt then calls that. For each name: the key C++ knows the
  #  function by, what it gives, and what it takes.
  __virtual_functions__ = {
      'nativeTexture': (
          ('_ZNK16QNativeInterface16QSGOpenGLTexture13nativeTextureEv',
           ('unsigned int', 'number', ''),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def nativeTexture(self) -> int:
    """
    Calls Qt's 'GLuint QNativeInterface::QSGOpenGLTexture::nativeTexture()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnativeinterface-qsgopengltexture.html
    """
    #  GLuint QNativeInterface::QSGOpenGLTexture::nativeTexture() const
    return self.uglySide.call(
        'ritual_ZNK16QNativeInterface16QSGOpenGLTexture13nativeTextureEv',
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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QNativeInterface::QSGOpenGLTexture::QSGOpenGLTexture()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qnativeinterface-qsgopengltexture.html
    """
    #  QNativeInterface::QSGOpenGLTexture::QSGOpenGLTexture()
    self._noteCreation(QSGOpenGLTexture, lambda: Rituals.call(
        'ritual_ZN16QNativeInterface16QSGOpenGLTextureC1Ev',
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
