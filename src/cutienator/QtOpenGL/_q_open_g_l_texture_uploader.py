"""
QOpenGLTextureUploader binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpenGL/6.12.0/QtOpenGL/private/qopengltextureuploader_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QOpenGLTextureUploader to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QSize
  from ..QtGui import QImage
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QImage = WAIT['QImage']
  QSize = WAIT['QSize']


class QOpenGLTextureUploader(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QOpenGLTextureUploader: a plain Python object
  standing in front of one C++ QOpenGLTextureUploader.

  C++ hands a QOpenGLTextureUploader around as a copy, so every C++
  QOpenGLTextureUploader behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QOpenGLTextureUploader that has a ritual and that
  Python can call so far, 1 name in all: 'textureImage'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QOpenGLTextureUploader::~QOpenGLTextureUploader()': the destructor:
    Python removes its C++ QOpenGLTextureUploader by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QOpenGLTextureUploader is created at the first use, not by
    'QOpenGLTextureUploader(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QOpenGLTextureUploader back gives a copy the ritual
    made for Python, in a new cute QOpenGLTextureUploader.
  """

  #  The enums Qt writes inside QOpenGLTextureUploader, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class BindOption(CuteFlags):
    """
    The flags enum 'QOpenGLTextureUploader::BindOption' of Qt, with the 5
    names Qt gives in it. Qt names the type of its combinations
    'QOpenGLTextureUploader::BindOptions'.
    """

    NoBindOption = 0x0
    PremultipliedAlphaBindOption = 0x1
    UseRedForAlphaAndLuminanceBindOption = 0x2
    SRgbBindOption = 0x4
    PowerOfTwoBindOption = 0x8

  BindOptions = BindOption

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(int, QImage, BindOptions)
  @overload(int, QImage, BindOptions, QSize)
  def textureImage(
      target: int,
      image: QImage,
      options: BindOptions,
      maxSize: Optional[QSize] = None,
  ) -> int:
    """
    Calls Qt's 'qsizetype QOpenGLTextureUploader::textureImage(GLenum target,
    const QImage &image, BindOptions options, QSize maxSize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltextureuploader.html#textureImage

    Parameters
    ----------

    target : int
      Passed on as it is.

    image : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.

    options : BindOptions
      Passed on as its number.

    maxSize : Optional[QSize]
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
      May be left out, as in Qt: a new 'QSize()' is then passed on.
    """
    #  qsizetype QOpenGLTextureUploader::textureImage(GLenum target, const
    #      QImage &image, BindOptions options, QSize maxSize)
    if maxSize is None:
      from ..QtCore import QSize
      maxSize = QSize()
    return Rituals.call(
        'ritual_ZN22QOpenGLTextureUploader12textureImageEjRK6QImage6QFlagsI'
        'NS_10BindOptionEE5QSize',
        target, CuteMixin._valueOf(image), options.value,
        CuteMixin._valueOf(maxSize),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpenGLTextureUploader'

  #  Qt's '~QOpenGLTextureUploader()'. Naming it makes this a value class:
  #  Python owns every C++ QOpenGLTextureUploader behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN22QOpenGLTextureUploaderD1Ev'

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
