"""
QtMultimediaPrivate::QDmaBufVideoBuffer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/6.12.0/QtMultimedia/private/qdmabufvideobuffer_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QtMultimediaPrivate::QDmaBufVideoBuffer to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from . import QAbstractVideoBuffer, QHwVideoBuffer, QVideoFrame
from . import QVideoFrameFormat

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QSize


class QDmaBufVideoBuffer(QHwVideoBuffer):
  """
  The cute side of Qt's QtMultimediaPrivate::QDmaBufVideoBuffer: a plain
  Python object standing in front of one C++
  QtMultimediaPrivate::QDmaBufVideoBuffer.

  It is built on the cute 'QHwVideoBuffer', as Qt's
  QtMultimediaPrivate::QDmaBufVideoBuffer is built on Qt's QHwVideoBuffer,
  and has everything that class has.

  C++ hands a QtMultimediaPrivate::QDmaBufVideoBuffer around as a copy, so
  every C++ QtMultimediaPrivate::QDmaBufVideoBuffer behind a cute one is
  Python's own: it is removed, by the ritual named in '__delete_ritual__',
  when the cute object goes.

  What exists
  -----------

  Every function of Qt's QtMultimediaPrivate::QDmaBufVideoBuffer that has a
  ritual and that Python can call so far, 5 names in all: 'isDmaBuf', 'map',
  'unmap', 'pixelFormat', 'size'. None can be made from Python: one comes out
  of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QtMultimediaPrivate::QDmaBufVideoBuffer::QDmaBufVideoBuffer(
    QVideoFrameFormat::PixelFormat format, QSize size, QSpan<const
    DmaBufPlane> planes, std::shared_ptr<void> keepAlive)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QtMultimediaPrivate::QDmaBufVideoBuffer::~QDmaBufVideoBuffer()':
    the destructor: Python removes its C++
    QtMultimediaPrivate::QDmaBufVideoBuffer by it, and has no other use for
    it.
  - Qt's 'QVideoFrameTexturesUPtr
    QtMultimediaPrivate::QDmaBufVideoBuffer::mapTextures(QRhi &rhi,
    QVideoFrameTexturesUPtr &oldTextures)': takes a type Python has no way to
    hand over yet.

  What to expect
  --------------

  - The C++ QtMultimediaPrivate::QDmaBufVideoBuffer is created at the first
    use, not by 'QtMultimediaPrivate::QDmaBufVideoBuffer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QtMultimediaPrivate::QDmaBufVideoBuffer back gives a
    copy the ritual made for Python, in a new cute
    QtMultimediaPrivate::QDmaBufVideoBuffer.
  - Each name of Qt's QtMultimediaPrivate::QDmaBufVideoBuffer that has no
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
  __qt_class__ = 'QtMultimediaPrivate::QDmaBufVideoBuffer'

  #  Qt's '~QtMultimediaPrivate::QDmaBufVideoBuffer()'. Naming it makes this
  #  a value class: Python owns every C++
  #  QtMultimediaPrivate::QDmaBufVideoBuffer behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = (
      'ritual_ZN19QtMultimediaPrivate18QDmaBufVideoBufferD1Ev')

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isDmaBuf(self) -> bool:
    """
    Calls Qt's 'bool QtMultimediaPrivate::QDmaBufVideoBuffer::isDmaBuf()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtmultimediaprivate-qdmabufvideobuffer.html
    """
    #  bool QtMultimediaPrivate::QDmaBufVideoBuffer::isDmaBuf() const
    return self.uglySide.call(
        'ritual_ZNK19QtMultimediaPrivate18QDmaBufVideoBuffer8isDmaBufEv',
    )

  def pixelFormat(self) -> QVideoFrameFormat.PixelFormat:
    """
    Calls Qt's 'QVideoFrameFormat::PixelFormat
    QtMultimediaPrivate::QDmaBufVideoBuffer::pixelFormat() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtmultimediaprivate-qdmabufvideobuffer.html

    Returns
    -------

    QVideoFrameFormat.PixelFormat
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QVideoFrameFormat.PixelFormat(number)' gives.
    """
    #  QVideoFrameFormat::PixelFormat
    #      QtMultimediaPrivate::QDmaBufVideoBuffer::pixelFormat() const
    return QVideoFrameFormat.PixelFormat(self.uglySide.call(
        'ritual_ZNK19QtMultimediaPrivate18QDmaBufVideoBuffer11pixelFormatEv',
    ))

  def size(self) -> QSize:
    """
    Calls Qt's 'QSize QtMultimediaPrivate::QDmaBufVideoBuffer::size() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtmultimediaprivate-qdmabufvideobuffer.html#size

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QtMultimediaPrivate::QDmaBufVideoBuffer::size() const
    address = self.uglySide.call(
        'ritual_ZNK19QtMultimediaPrivate18QDmaBufVideoBuffer4sizeEv',
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

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
    Qt's 'QtMultimediaPrivate::QDmaBufVideoBuffer::QDmaBufVideoBuffer(
    QVideoFrameFormat::PixelFormat format, QSize size, QSpan<const
    DmaBufPlane> planes, std::shared_ptr<void> keepAlive)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QtMultimediaPrivate.QDmaBufVideoBuffer.__init__' has no cute "
        "function yet. Qt's "
        "'QtMultimediaPrivate::QDmaBufVideoBuffer::QDmaBufVideoBuffer(QVideo"
        "FrameFormat::PixelFormat format, QSize size, QSpan<const "
        "DmaBufPlane> planes, std::shared_ptr<void> keepAlive)': takes a "
        "type Python has no way to hand over yet.")

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
    Calls Qt's 'MapData
    QtMultimediaPrivate::QDmaBufVideoBuffer::map(QVideoFrame::MapMode mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtmultimediaprivate-qdmabufvideobuffer.html#map

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
    #  MapData
    #      QtMultimediaPrivate::QDmaBufVideoBuffer::map(QVideoFrame::MapMode
    #      mode)
    address = self.uglySide.call(
        'ritual_ZN19QtMultimediaPrivate18QDmaBufVideoBuffer3mapEN11QVideoFr'
        'ame7MapModeE',
        mode.value,
    )
    return QAbstractVideoBuffer.MapData._cuteOwning(address)

  def unmap(self) -> None:
    """
    Calls Qt's 'void QtMultimediaPrivate::QDmaBufVideoBuffer::unmap()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtmultimediaprivate-qdmabufvideobuffer.html#unmap
    """
    #  void QtMultimediaPrivate::QDmaBufVideoBuffer::unmap()
    self.uglySide.call(
        'ritual_ZN19QtMultimediaPrivate18QDmaBufVideoBuffer5unmapEv',
    )
