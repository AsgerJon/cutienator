"""
QVideoTextureHelper::QVideoFrameTexturesFromRhiTextureArray binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/6.12.0/QtMultimedia/private/qvideoframetexturefromsource_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QVideoTextureHelper::QVideoFrameTexturesFromRhiTextureArray to be
#  private: it declares the class in a header it calls private. cutienator
#  does not care. Qt hands objects of the class out all the same, and a class
#  we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from . import QVideoFrameTextures

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtGui import QRhiTexture


class QVideoFrameTexturesFromRhiTextureArray(QVideoFrameTextures):
  """
  The cute side of Qt's
  QVideoTextureHelper::QVideoFrameTexturesFromRhiTextureArray: a plain Python
  object standing in front of one C++
  QVideoTextureHelper::QVideoFrameTexturesFromRhiTextureArray.

  It is built on the cute 'QVideoFrameTextures', as Qt's
  QVideoTextureHelper::QVideoFrameTexturesFromRhiTextureArray is built on
  Qt's QVideoFrameTextures, and has everything that class has.

  What exists
  -----------

  Every function of Qt's
  QVideoTextureHelper::QVideoFrameTexturesFromRhiTextureArray that has a
  ritual and that Python can call so far, 1 name in all: 'texture'. None can
  be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QVideoTextureHelper::QVideoFrameTexturesFromRhiTextureArray::
    QVideoFrameTexturesFromRhiTextureArray(RhiTextureArray &&rhiTextures)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QVideoTextureHelper::QVideoFrameTexturesFromRhiTextureArray::
    ~QVideoFrameTexturesFromRhiTextureArray()': the destructor: Python never
    removes a C++
    QVideoTextureHelper::QVideoFrameTexturesFromRhiTextureArray.
  - Qt's 'RhiTextureArray
    &QVideoTextureHelper::QVideoFrameTexturesFromRhiTextureArray::
    textureArray()': gives a type Python has no way to take yet.

  What to expect
  --------------

  - The C++ QVideoTextureHelper::QVideoFrameTexturesFromRhiTextureArray is
    created at the first use, not by
    'QVideoTextureHelper::QVideoFrameTexturesFromRhiTextureArray(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++
    QVideoTextureHelper::QVideoFrameTexturesFromRhiTextureArray.
  - Each name of Qt's
    QVideoTextureHelper::QVideoFrameTexturesFromRhiTextureArray that has no
    cute function yet, '__init__', 'textureArray', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QVideoTextureHelper::QVideoFrameTexturesFromRhiTextureArray'

  #  A C++ QVideoTextureHelper::QVideoFrameTexturesFromRhiTextureArray Python
  #  makes is of a C++ class of ours, in which Python can take functions
  #  over. This ritual hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QVideoTextureHelper_QVideoFrameTexturesFromRhiTextureArray'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def texture(self, plane: int) -> Optional[QRhiTexture]:
    """
    Calls Qt's 'QRhiTexture
    *QVideoTextureHelper::QVideoFrameTexturesFromRhiTextureArray::texture(
    uint plane) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvideotexturehelper-qvideoframetexturesfromrhitexturearray.html

    Parameters
    ----------

    plane : int
      Passed on as it is.

    Returns
    -------

    Optional[QRhiTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiTexture
    #      *QVideoTextureHelper::QVideoFrameTexturesFromRhiTextureArray::
    #      texture(uint plane) const
    ritual = (
        'ritual_ZNK19QVideoTextureHelper38QVideoFrameTexturesFromRhiTexture'
        'Array7textureEj')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK19QVideoTextureHelper38QVideoFrameTexturesFromRhiT'
          'extureArray7textureEj')
    address = self.uglySide.call(ritual, plane)
    from ..QtGui import QRhiTexture
    return QRhiTexture._cuteAt(address)

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
    Qt's 'QVideoTextureHelper::QVideoFrameTexturesFromRhiTextureArray::
    QVideoFrameTexturesFromRhiTextureArray(RhiTextureArray &&rhiTextures)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QVideoTextureHelper.QVideoFrameTexturesFromRhiTextureArray.__init_"
        "_' has no cute function yet. Qt's "
        "'QVideoTextureHelper::QVideoFrameTexturesFromRhiTextureArray::QVide"
        "oFrameTexturesFromRhiTextureArray(RhiTextureArray &&rhiTextures)': "
        "takes a type Python has no way to hand over yet.")

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

  @staticmethod
  def textureArray(*__, **_) -> Never:
    """
    Qt's 'RhiTextureArray
    &QVideoTextureHelper::QVideoFrameTexturesFromRhiTextureArray::
    textureArray()': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QVideoTextureHelper.QVideoFrameTexturesFromRhiTextureArray.texture"
        "Array' has no cute function yet. Qt's 'RhiTextureArray "
        "&QVideoTextureHelper::QVideoFrameTexturesFromRhiTextureArray::textu"
        "reArray()': gives a type Python has no way to take yet.")
