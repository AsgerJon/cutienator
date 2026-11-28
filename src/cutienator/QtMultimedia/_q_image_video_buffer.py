"""
QImageVideoBuffer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/6.12.0/QtMultimedia/private/qimagevideobuffer_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QImageVideoBuffer to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QAbstractVideoBuffer, QVideoFrame

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtGui import QImage
  from . import QVideoFrameFormat
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QImage = WAIT['QImage']


class QImageVideoBuffer(QAbstractVideoBuffer):
  """
  The cute side of Qt's QImageVideoBuffer: a plain Python object standing in
  front of one C++ QImageVideoBuffer.

  It is built on the cute 'QAbstractVideoBuffer', as Qt's QImageVideoBuffer
  is built on Qt's QAbstractVideoBuffer, and has everything that class has.

  C++ hands a QImageVideoBuffer around as a copy, so every C++
  QImageVideoBuffer behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QImageVideoBuffer that has a ritual and that Python
  can call so far, 3 names in all: 'map', 'format', 'underlyingImage'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QImageVideoBuffer::~QImageVideoBuffer()': the destructor: Python
    removes its C++ QImageVideoBuffer by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QImageVideoBuffer is created at the first use, not by
    'QImageVideoBuffer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QImageVideoBuffer back gives a copy the ritual made
    for Python, in a new cute QImageVideoBuffer.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QImageVideoBuffer'

  #  Qt's '~QImageVideoBuffer()'. Naming it makes this a value class: Python
  #  owns every C++ QImageVideoBuffer behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN17QImageVideoBufferD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def format(self) -> QVideoFrameFormat:
    """
    Calls Qt's 'QVideoFrameFormat QImageVideoBuffer::format() const'.

    Qt's own words: https://doc.qt.io/qt-6/qimagevideobuffer.html#format

    Returns
    -------

    QVideoFrameFormat
      A new cute QVideoFrameFormat around the copy Qt gave back. Python owns
      it.
    """
    #  QVideoFrameFormat QImageVideoBuffer::format() const
    ritual = 'ritual_ZNK17QImageVideoBuffer6formatEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QImageVideoBuffer6formatEv'
    address = self.uglySide.call(ritual)
    from . import QVideoFrameFormat
    return QVideoFrameFormat._cuteOwning(address)

  def underlyingImage(self) -> QImage:
    """
    Calls Qt's 'QImage QImageVideoBuffer::underlyingImage() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qimagevideobuffer.html#underlyingImage

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QImageVideoBuffer::underlyingImage() const
    address = self.uglySide.call(
        'ritual_ZNK17QImageVideoBuffer15underlyingImageEv',
    )
    from ..QtGui import QImage
    return QImage._cuteOwning(address)

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

  @overload(QImage)
  def __init__(self, image: QImage) -> None:
    """
    Notes what was given, for Qt's
    'QImageVideoBuffer::QImageVideoBuffer(QImage image)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qimagevideobuffer.html#QImageVideoBuffer

    Parameters
    ----------

    image : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.
    """
    #  QImageVideoBuffer::QImageVideoBuffer(QImage image)
    self._noteCreation(QImageVideoBuffer, lambda: Rituals.call(
        'ritual_ZN17QImageVideoBufferC1E6QImage', self._valueOf(image),
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

  @overload(QVideoFrame.MapMode)
  def map(self, mode: QVideoFrame.MapMode) -> QAbstractVideoBuffer.MapData:
    """
    Calls Qt's 'MapData QImageVideoBuffer::map(QVideoFrame::MapMode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qimagevideobuffer.html#map

    Parameters
    ----------

    mode : QVideoFrame.MapMode
      Passed on as its number.

    Returns
    -------

    QAbstractVideoBuffer.MapData
      A new cute QAbstractVideoBuffer::MapData around the copy Qt gave back.
      Python owns it.
    """
    #  MapData QImageVideoBuffer::map(QVideoFrame::MapMode mode)
    ritual = 'ritual_ZN17QImageVideoBuffer3mapEN11QVideoFrame7MapModeE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QImageVideoBuffer3mapEN11QVideoFrame7MapModeE'
    address = self.uglySide.call(ritual, mode.value)
    return QAbstractVideoBuffer.MapData._cuteOwning(address)
