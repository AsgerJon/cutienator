"""
QMemoryVideoBuffer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/6.12.0/QtMultimedia/private/qmemoryvideobuffer_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QMemoryVideoBuffer to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QAbstractVideoBuffer, QVideoFrame

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QByteArray
  from . import QVideoFrameFormat
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']


class QMemoryVideoBuffer(QAbstractVideoBuffer):
  """
  The cute side of Qt's QMemoryVideoBuffer: a plain Python object standing in
  front of one C++ QMemoryVideoBuffer.

  It is built on the cute 'QAbstractVideoBuffer', as Qt's QMemoryVideoBuffer
  is built on Qt's QAbstractVideoBuffer, and has everything that class has.

  C++ hands a QMemoryVideoBuffer around as a copy, so every C++
  QMemoryVideoBuffer behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QMemoryVideoBuffer that has a ritual and that Python
  can call so far, 2 names in all: 'map', 'format'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QMemoryVideoBuffer::~QMemoryVideoBuffer()': the destructor: Python
    removes its C++ QMemoryVideoBuffer by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QMemoryVideoBuffer is created at the first use, not by
    'QMemoryVideoBuffer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QMemoryVideoBuffer back gives a copy the ritual made
    for Python, in a new cute QMemoryVideoBuffer.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QMemoryVideoBuffer'

  #  A C++ QMemoryVideoBuffer Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QMemoryVideoBuffer'

  #  Qt's '~QMemoryVideoBuffer()'. Naming it makes this a value class: Python
  #  owns every C++ QMemoryVideoBuffer behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN18QMemoryVideoBufferD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def format(self) -> QVideoFrameFormat:
    """
    Calls Qt's 'QVideoFrameFormat QMemoryVideoBuffer::format() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmemoryvideobuffer.html#format

    Returns
    -------

    QVideoFrameFormat
      A new cute QVideoFrameFormat around the copy Qt gave back. Python owns
      it.
    """
    #  QVideoFrameFormat QMemoryVideoBuffer::format() const
    ritual = 'ritual_ZNK18QMemoryVideoBuffer6formatEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18QMemoryVideoBuffer6formatEv'
    address = self.uglySide.call(ritual)
    from . import QVideoFrameFormat
    return QVideoFrameFormat._cuteOwning(address)

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

  @overload(QByteArray, int)
  def __init__(self, data: QByteArray, bytesPerLine: int) -> None:
    """
    Notes what was given, for Qt's
    'QMemoryVideoBuffer::QMemoryVideoBuffer(QByteArray data, int
    bytesPerLine)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qmemoryvideobuffer.html#QMemoryVideoBuffer

    Parameters
    ----------

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    bytesPerLine : int
      Passed on as it is.
    """
    #  QMemoryVideoBuffer::QMemoryVideoBuffer(QByteArray data, int
    #      bytesPerLine)
    self._noteCreation(QMemoryVideoBuffer, lambda: Rituals.call(
        'ritual_ZN18QMemoryVideoBufferC1E10QByteArrayi',
        self._valueOf(data), bytesPerLine,
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
    Calls Qt's 'MapData QMemoryVideoBuffer::map(QVideoFrame::MapMode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qmemoryvideobuffer.html#map

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
    #  MapData QMemoryVideoBuffer::map(QVideoFrame::MapMode mode)
    ritual = 'ritual_ZN18QMemoryVideoBuffer3mapEN11QVideoFrame7MapModeE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QMemoryVideoBuffer3mapEN11QVideoFrame7MapModeE')
    address = self.uglySide.call(ritual, mode.value)
    return QAbstractVideoBuffer.MapData._cuteOwning(address)
