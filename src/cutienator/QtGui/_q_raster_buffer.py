"""
QRasterBuffer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qpaintengine_raster_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QRasterBuffer to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QImage

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QColor
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QRasterBuffer(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QRasterBuffer: a plain Python object standing in
  front of one C++ QRasterBuffer.

  C++ hands a QRasterBuffer around as a copy, so every C++ QRasterBuffer
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QRasterBuffer that has a ritual and that Python can
  call so far, 7 names in all: 'init', 'prepare', 'width', 'height',
  'bytesPerLine', 'bytesPerPixel', 'colorizeBitmap'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QRasterBuffer::~QRasterBuffer()': the destructor: Python removes
    its C++ QRasterBuffer by it, and has no other use for it.

  What has no ritual
  ------------------

  3 of the 12 functions Qt declares: 2 takes or gives a type that cannot be
  passed yet; 1 a template.

  What to expect
  --------------

  - The C++ QRasterBuffer is created at the first use, not by
    'QRasterBuffer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QRasterBuffer back gives a copy the ritual made for
    Python, in a new cute QRasterBuffer.
  - Each name of Qt's QRasterBuffer that has no cute function yet, 'buffer',
    'scanLine', 'stride', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QRasterBuffer'

  #  Qt's '~QRasterBuffer()'. Naming it makes this a value class: Python owns
  #  every C++ QRasterBuffer behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN13QRasterBufferD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def width(self) -> int:
    """
    Calls Qt's 'int QRasterBuffer::width() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrasterbuffer.html#width
    """
    #  int QRasterBuffer::width() const
    return self.uglySide.call('ritual_ZNK13QRasterBuffer5widthEv')

  def height(self) -> int:
    """
    Calls Qt's 'int QRasterBuffer::height() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrasterbuffer.html#height
    """
    #  int QRasterBuffer::height() const
    return self.uglySide.call('ritual_ZNK13QRasterBuffer6heightEv')

  def bytesPerLine(self) -> int:
    """
    Calls Qt's 'qsizetype QRasterBuffer::bytesPerLine() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrasterbuffer.html#bytesPerLine
    """
    #  qsizetype QRasterBuffer::bytesPerLine() const
    return self.uglySide.call('ritual_ZNK13QRasterBuffer12bytesPerLineEv')

  def bytesPerPixel(self) -> int:
    """
    Calls Qt's 'int QRasterBuffer::bytesPerPixel() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrasterbuffer.html#bytesPerPixel
    """
    #  int QRasterBuffer::bytesPerPixel() const
    return self.uglySide.call('ritual_ZNK13QRasterBuffer13bytesPerPixelEv')

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
    Notes what was given, for Qt's 'QRasterBuffer::QRasterBuffer()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qrasterbuffer.html#QRasterBuffer
    """
    #  QRasterBuffer::QRasterBuffer()
    self._noteCreation(QRasterBuffer, lambda: Rituals.call(
        'ritual_ZN13QRasterBufferC1Ev',
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

  def init(self) -> None:
    """
    Calls Qt's 'void QRasterBuffer::init()'.

    Qt's own words: https://doc.qt.io/qt-6/qrasterbuffer.html#init
    """
    #  void QRasterBuffer::init()
    self.uglySide.call('ritual_ZN13QRasterBuffer4initEv')

  @overload(QImage)
  @overload(NoneType)
  def prepare(self, image: Optional[QImage]) -> QImage.Format:
    """
    Calls Qt's 'QImage::Format QRasterBuffer::prepare(QImage *image)'.

    Qt's own words: https://doc.qt.io/qt-6/qrasterbuffer.html#prepare

    Parameters
    ----------

    image : Optional[QImage]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QImage.Format
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QImage.Format(number)'
      gives.
    """
    #  QImage::Format QRasterBuffer::prepare(QImage *image)
    return QImage.Format(self.uglySide.call(
        'ritual_ZN13QRasterBuffer7prepareEP6QImage', self._addressOf(image),
    ))

  @overload(QImage, QColor)
  def colorizeBitmap(self, image: QImage, color: QColor) -> QImage:
    """
    Calls Qt's 'QImage QRasterBuffer::colorizeBitmap(const QImage &image,
    const QColor &color)'.

    Qt's own words: https://doc.qt.io/qt-6/qrasterbuffer.html#colorizeBitmap

    Parameters
    ----------

    image : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QRasterBuffer::colorizeBitmap(const QImage &image, const QColor
    #      &color)
    address = self.uglySide.call(
        'ritual_ZN13QRasterBuffer14colorizeBitmapERK6QImageRK6QColor',
        self._valueOf(image), self._valueOf(color),
    )
    return QImage._cuteOwning(address)

  @staticmethod
  def buffer(*__, **_) -> Never:
    """
    Qt's 'uchar *QRasterBuffer::buffer() const': takes or gives a type that
    cannot be passed yet: uchar *.
    """
    raise NotImplementedError(
        "'QRasterBuffer.buffer' has no cute function yet. Qt's 'uchar "
        "*QRasterBuffer::buffer() const': takes or gives a type that cannot "
        "be passed yet: uchar *.")

  @staticmethod
  def scanLine(*__, **_) -> Never:
    """
    Qt's 'uchar *QRasterBuffer::scanLine(int y)': takes or gives a type that
    cannot be passed yet: uchar *.
    """
    raise NotImplementedError(
        "'QRasterBuffer.scanLine' has no cute function yet. Qt's 'uchar "
        "*QRasterBuffer::scanLine(int y)': takes or gives a type that "
        "cannot be passed yet: uchar *.")

  @staticmethod
  def stride(*__, **_) -> Never:
    """
    Qt's 'QRasterBuffer::stride': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QRasterBuffer.stride' has no cute function yet. Qt's "
        "'QRasterBuffer::stride': a template: a pattern and no single "
        "function.")
