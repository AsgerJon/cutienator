"""
QBitmap binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of QtGui/qbitmap.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from . import QPixmap

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QSize
  from . import QImage, QTransform
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QImage = WAIT['QImage']
  QSize = WAIT['QSize']
  QTransform = WAIT['QTransform']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QBitmap(QPixmap):
  """
  The cute side of Qt's QBitmap: a plain Python object standing in front of
  one C++ QBitmap.

  It is built on the cute 'QPixmap', as Qt's QBitmap is built on Qt's
  QPixmap, and has everything that class has.

  C++ hands a QBitmap around as a copy, so every C++ QBitmap behind a cute
  one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QBitmap that has a ritual and that Python can call
  so far, 4 names in all: 'clear', 'fromImage', 'fromPixmap', 'transformed'.
  It can be made from Python, in 5 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QBitmap::~QBitmap()': the destructor: Python removes its C++
    QBitmap by it, and has no other use for it.
  - Qt's 'QVariant QBitmap::operator QVariant() const': an operator, which is
    not reflected yet.

  What has no ritual
  ------------------

  4 of the 15 functions Qt declares: 4 takes or gives a type that cannot be
  passed yet.

  What to expect
  --------------

  - The C++ QBitmap is created at the first use, not by 'QBitmap(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QBitmap back gives a copy the ritual made for Python,
    in a new cute QBitmap.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QImage)
  @overload(QImage, Qt.ImageConversionFlags)
  def fromImage(
      image: QImage,
      flags: Qt.ImageConversionFlags = Qt.ImageConversionFlags.AutoColor,
  ) -> QBitmap:
    """
    Calls Qt's 'QBitmap QBitmap::fromImage(const QImage &image,
    Qt::ImageConversionFlags flags)'.

    Qt's own words: https://doc.qt.io/qt-6/qbitmap.html#fromImage

    Parameters
    ----------

    image : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.

    flags : Qt.ImageConversionFlags
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.ImageConversionFlags.AutoColor.

    Returns
    -------

    QBitmap
      A new cute QBitmap around the copy Qt gave back. Python owns it.
    """
    #  QBitmap QBitmap::fromImage(const QImage &image,
    #      Qt::ImageConversionFlags flags)
    address = Rituals.call(
        'ritual_ZN7QBitmap9fromImageERK6QImage6QFlagsIN2Qt19ImageConversion'
        'FlagEE',
        CuteMixin._valueOf(image), flags.value,
    )
    return QBitmap._cuteOwning(address)

  @staticmethod
  @overload(QPixmap)
  def fromPixmap(pixmap: QPixmap) -> QBitmap:
    """
    Calls Qt's 'QBitmap QBitmap::fromPixmap(const QPixmap &pixmap)'.

    Qt's own words: https://doc.qt.io/qt-6/qbitmap.html#fromPixmap

    Parameters
    ----------

    pixmap : QPixmap
      Passed on as a value: Qt reads the C++ QPixmap, which stays Python's
      own.

    Returns
    -------

    QBitmap
      A new cute QBitmap around the copy Qt gave back. Python owns it.
    """
    #  QBitmap QBitmap::fromPixmap(const QPixmap &pixmap)
    address = Rituals.call(
        'ritual_ZN7QBitmap10fromPixmapERK7QPixmap',
        CuteMixin._valueOf(pixmap),
    )
    return QBitmap._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QBitmap'

  #  Qt's '~QBitmap()'. Naming it makes this a value class: Python owns every
  #  C++ QBitmap behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN7QBitmapD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QTransform)
  def transformed(self, matrix: QTransform) -> QBitmap:
    """
    Calls Qt's 'QBitmap QBitmap::transformed(const QTransform &matrix)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qbitmap.html#transformed

    Parameters
    ----------

    matrix : QTransform
      Passed on as a value: Qt reads the C++ QTransform, which stays Python's
      own.

    Returns
    -------

    QBitmap
      A new cute QBitmap around the copy Qt gave back. Python owns it.
    """
    #  QBitmap QBitmap::transformed(const QTransform &matrix) const
    address = self.uglySide.call(
        'ritual_ZNK7QBitmap11transformedERK10QTransform',
        self._valueOf(matrix),
    )
    return QBitmap._cuteOwning(address)

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
    Notes what was given, for Qt's 'QBitmap::QBitmap()', which is called at
    the first use.

    Qt's own words: https://doc.qt.io/qt-6/qbitmap.html#QBitmap
    """
    #  QBitmap::QBitmap()
    self._noteCreation(QBitmap, lambda: Rituals.call(
        'ritual_ZN7QBitmapC1Ev',
    ))

  @overload(QPixmap)
  def __init__(self, a0: QPixmap) -> None:
    """
    Notes what was given, for Qt's 'QBitmap::QBitmap(const QPixmap &a0)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qbitmap.html#QBitmap

    Parameters
    ----------

    a0 : QPixmap
      Passed on as a value: Qt reads the C++ QPixmap, which stays Python's
      own.
    """
    #  QBitmap::QBitmap(const QPixmap &a0)
    self._noteCreation(QBitmap, lambda: Rituals.call(
        'ritual_ZN7QBitmapC1ERK7QPixmap', self._valueOf(a0),
    ))

  @overload(int, int)
  def __init__(self, w: int, h: int) -> None:
    """
    Notes what was given, for Qt's 'QBitmap::QBitmap(int w, int h)', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qbitmap.html#QBitmap

    Parameters
    ----------

    w : int
      Passed on as it is.

    h : int
      Passed on as it is.
    """
    #  QBitmap::QBitmap(int w, int h)
    self._noteCreation(QBitmap, lambda: Rituals.call(
        'ritual_ZN7QBitmapC1Eii', w, h,
    ))

  @overload(QSize)
  def __init__(self, a0: QSize) -> None:
    """
    Notes what was given, for Qt's 'QBitmap::QBitmap(const QSize &a0)', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qbitmap.html#QBitmap

    Parameters
    ----------

    a0 : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  QBitmap::QBitmap(const QSize &a0)
    self._noteCreation(QBitmap, lambda: Rituals.call(
        'ritual_ZN7QBitmapC1ERK5QSize', self._valueOf(a0),
    ))

  @overload(str)
  @overload(str, str)
  @overload(str, NoneType)
  def __init__(self, fileName: str, format: Optional[str] = None) -> None:
    """
    Notes what was given, for Qt's 'QBitmap::QBitmap(const QString &fileName,
    const char *format)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qbitmap.html#QBitmap

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.

    format : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.
    """
    #  QBitmap::QBitmap(const QString &fileName, const char *format)
    self._noteCreation(QBitmap, lambda: Rituals.call(
        'ritual_ZN7QBitmapC1ERK7QStringPKc', fileName, self._bytesOf(format),
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

  def clear(self) -> None:
    """
    Calls Qt's 'void QBitmap::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qbitmap.html#clear
    """
    #  void QBitmap::clear()
    self.uglySide.call('ritual_ZN7QBitmap5clearEv')
