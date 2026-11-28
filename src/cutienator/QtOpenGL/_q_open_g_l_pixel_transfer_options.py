"""
QOpenGLPixelTransferOptions binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpenGL/qopenglpixeltransferoptions.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QOpenGLPixelTransferOptions(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QOpenGLPixelTransferOptions: a plain Python object
  standing in front of one C++ QOpenGLPixelTransferOptions.

  C++ hands a QOpenGLPixelTransferOptions around as a copy, so every C++
  QOpenGLPixelTransferOptions behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QOpenGLPixelTransferOptions that has a ritual and
  that Python can call so far, 16 names in all: 'setAlignment', 'alignment',
  'setSkipImages', 'skipImages', 'setSkipRows', 'skipRows', 'setSkipPixels',
  'skipPixels', 'setImageHeight', 'imageHeight', 'setRowLength', 'rowLength',
  'setLeastSignificantByteFirst', 'isLeastSignificantBitFirst',
  'setSwapBytesEnabled', 'isSwapBytesEnabled'. It can be made from Python, in
  2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QOpenGLPixelTransferOptions
    &QOpenGLPixelTransferOptions::operator=(QOpenGLPixelTransferOptions
    &&other)': assignment: Python binds a name and has no operator for it.
  - Qt's 'QOpenGLPixelTransferOptions
    &QOpenGLPixelTransferOptions::operator=(const QOpenGLPixelTransferOptions
    &a0)': assignment: Python binds a name and has no operator for it.
  - Qt's 'QOpenGLPixelTransferOptions::~QOpenGLPixelTransferOptions()': the
    destructor: Python removes its C++ QOpenGLPixelTransferOptions by it, and
    has no other use for it.
  - Qt's 'void QOpenGLPixelTransferOptions::swap(QOpenGLPixelTransferOptions
    &other)': takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QOpenGLPixelTransferOptions is created at the first use, not by
    'QOpenGLPixelTransferOptions(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QOpenGLPixelTransferOptions back gives a copy the
    ritual made for Python, in a new cute QOpenGLPixelTransferOptions.
  - Each name of Qt's QOpenGLPixelTransferOptions that has no cute function
    yet, 'swap', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpenGLPixelTransferOptions'

  #  Qt's '~QOpenGLPixelTransferOptions()'. Naming it makes this a value
  #  class: Python owns every C++ QOpenGLPixelTransferOptions behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN27QOpenGLPixelTransferOptionsD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def alignment(self) -> int:
    """
    Calls Qt's 'int QOpenGLPixelTransferOptions::alignment() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglpixeltransferoptions.html#alignment
    """
    #  int QOpenGLPixelTransferOptions::alignment() const
    return self.uglySide.call(
        'ritual_ZNK27QOpenGLPixelTransferOptions9alignmentEv',
    )

  def skipImages(self) -> int:
    """
    Calls Qt's 'int QOpenGLPixelTransferOptions::skipImages() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglpixeltransferoptions.html#skipImages
    """
    #  int QOpenGLPixelTransferOptions::skipImages() const
    return self.uglySide.call(
        'ritual_ZNK27QOpenGLPixelTransferOptions10skipImagesEv',
    )

  def skipRows(self) -> int:
    """
    Calls Qt's 'int QOpenGLPixelTransferOptions::skipRows() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglpixeltransferoptions.html#skipRows
    """
    #  int QOpenGLPixelTransferOptions::skipRows() const
    return self.uglySide.call(
        'ritual_ZNK27QOpenGLPixelTransferOptions8skipRowsEv',
    )

  def skipPixels(self) -> int:
    """
    Calls Qt's 'int QOpenGLPixelTransferOptions::skipPixels() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglpixeltransferoptions.html#skipPixels
    """
    #  int QOpenGLPixelTransferOptions::skipPixels() const
    return self.uglySide.call(
        'ritual_ZNK27QOpenGLPixelTransferOptions10skipPixelsEv',
    )

  def imageHeight(self) -> int:
    """
    Calls Qt's 'int QOpenGLPixelTransferOptions::imageHeight() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglpixeltransferoptions.html#imageHeight
    """
    #  int QOpenGLPixelTransferOptions::imageHeight() const
    return self.uglySide.call(
        'ritual_ZNK27QOpenGLPixelTransferOptions11imageHeightEv',
    )

  def rowLength(self) -> int:
    """
    Calls Qt's 'int QOpenGLPixelTransferOptions::rowLength() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglpixeltransferoptions.html#rowLength
    """
    #  int QOpenGLPixelTransferOptions::rowLength() const
    return self.uglySide.call(
        'ritual_ZNK27QOpenGLPixelTransferOptions9rowLengthEv',
    )

  def isLeastSignificantBitFirst(self) -> bool:
    """
    Calls Qt's 'bool
    QOpenGLPixelTransferOptions::isLeastSignificantBitFirst() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglpixeltransferoptions.html
    """
    #  bool QOpenGLPixelTransferOptions::isLeastSignificantBitFirst() const
    return self.uglySide.call(
        'ritual_ZNK27QOpenGLPixelTransferOptions26isLeastSignificantBitFirs'
        'tEv',
    )

  def isSwapBytesEnabled(self) -> bool:
    """
    Calls Qt's 'bool QOpenGLPixelTransferOptions::isSwapBytesEnabled()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglpixeltransferoptions.html
    """
    #  bool QOpenGLPixelTransferOptions::isSwapBytesEnabled() const
    return self.uglySide.call(
        'ritual_ZNK27QOpenGLPixelTransferOptions18isSwapBytesEnabledEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setAlignment(self, alignment: int) -> None:
    """
    Calls Qt's 'void QOpenGLPixelTransferOptions::setAlignment(int
    alignment)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglpixeltransferoptions.html#setAlignment

    Parameters
    ----------

    alignment : int
      Passed on as it is.
    """
    #  void QOpenGLPixelTransferOptions::setAlignment(int alignment)
    self.uglySide.call(
        'ritual_ZN27QOpenGLPixelTransferOptions12setAlignmentEi', alignment,
    )

  @overload(int)
  def setSkipImages(self, skipImages: int) -> None:
    """
    Calls Qt's 'void QOpenGLPixelTransferOptions::setSkipImages(int
    skipImages)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglpixeltransferoptions.html#setSkipImages

    Parameters
    ----------

    skipImages : int
      Passed on as it is.
    """
    #  void QOpenGLPixelTransferOptions::setSkipImages(int skipImages)
    self.uglySide.call(
        'ritual_ZN27QOpenGLPixelTransferOptions13setSkipImagesEi',
        skipImages,
    )

  @overload(int)
  def setSkipRows(self, skipRows: int) -> None:
    """
    Calls Qt's 'void QOpenGLPixelTransferOptions::setSkipRows(int skipRows)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglpixeltransferoptions.html#setSkipRows

    Parameters
    ----------

    skipRows : int
      Passed on as it is.
    """
    #  void QOpenGLPixelTransferOptions::setSkipRows(int skipRows)
    self.uglySide.call(
        'ritual_ZN27QOpenGLPixelTransferOptions11setSkipRowsEi', skipRows,
    )

  @overload(int)
  def setSkipPixels(self, skipPixels: int) -> None:
    """
    Calls Qt's 'void QOpenGLPixelTransferOptions::setSkipPixels(int
    skipPixels)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglpixeltransferoptions.html#setSkipPixels

    Parameters
    ----------

    skipPixels : int
      Passed on as it is.
    """
    #  void QOpenGLPixelTransferOptions::setSkipPixels(int skipPixels)
    self.uglySide.call(
        'ritual_ZN27QOpenGLPixelTransferOptions13setSkipPixelsEi',
        skipPixels,
    )

  @overload(int)
  def setImageHeight(self, imageHeight: int) -> None:
    """
    Calls Qt's 'void QOpenGLPixelTransferOptions::setImageHeight(int
    imageHeight)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglpixeltransferoptions.html#setImageHeight

    Parameters
    ----------

    imageHeight : int
      Passed on as it is.
    """
    #  void QOpenGLPixelTransferOptions::setImageHeight(int imageHeight)
    self.uglySide.call(
        'ritual_ZN27QOpenGLPixelTransferOptions14setImageHeightEi',
        imageHeight,
    )

  @overload(int)
  def setRowLength(self, rowLength: int) -> None:
    """
    Calls Qt's 'void QOpenGLPixelTransferOptions::setRowLength(int
    rowLength)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglpixeltransferoptions.html#setRowLength

    Parameters
    ----------

    rowLength : int
      Passed on as it is.
    """
    #  void QOpenGLPixelTransferOptions::setRowLength(int rowLength)
    self.uglySide.call(
        'ritual_ZN27QOpenGLPixelTransferOptions12setRowLengthEi', rowLength,
    )

  @overload(bool)
  def setLeastSignificantByteFirst(self, lsbFirst: bool) -> None:
    """
    Calls Qt's 'void
    QOpenGLPixelTransferOptions::setLeastSignificantByteFirst(bool
    lsbFirst)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglpixeltransferoptions.html

    Parameters
    ----------

    lsbFirst : bool
      Passed on as it is.
    """
    #  void QOpenGLPixelTransferOptions::setLeastSignificantByteFirst(bool
    #      lsbFirst)
    self.uglySide.call(
        'ritual_ZN27QOpenGLPixelTransferOptions28setLeastSignificantByteFir'
        'stEb',
        lsbFirst,
    )

  @overload(bool)
  def setSwapBytesEnabled(self, swapBytes: bool) -> None:
    """
    Calls Qt's 'void QOpenGLPixelTransferOptions::setSwapBytesEnabled(bool
    swapBytes)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglpixeltransferoptions.html

    Parameters
    ----------

    swapBytes : bool
      Passed on as it is.
    """
    #  void QOpenGLPixelTransferOptions::setSwapBytesEnabled(bool swapBytes)
    self.uglySide.call(
        'ritual_ZN27QOpenGLPixelTransferOptions19setSwapBytesEnabledEb',
        swapBytes,
    )

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
    'QOpenGLPixelTransferOptions::QOpenGLPixelTransferOptions()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglpixeltransferoptions.html
    """
    #  QOpenGLPixelTransferOptions::QOpenGLPixelTransferOptions()
    self._noteCreation(QOpenGLPixelTransferOptions, lambda: Rituals.call(
        'ritual_ZN27QOpenGLPixelTransferOptionsC1Ev',
    ))

  @overload(THIS)
  def __init__(self, a0: QOpenGLPixelTransferOptions) -> None:
    """
    Notes what was given, for Qt's
    'QOpenGLPixelTransferOptions::QOpenGLPixelTransferOptions(const
    QOpenGLPixelTransferOptions &a0)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglpixeltransferoptions.html

    Parameters
    ----------

    a0 : QOpenGLPixelTransferOptions
      Passed on as a value: Qt reads the C++ QOpenGLPixelTransferOptions,
      which stays Python's own.
    """
    #  QOpenGLPixelTransferOptions::QOpenGLPixelTransferOptions(const
    #      QOpenGLPixelTransferOptions &a0)
    self._noteCreation(QOpenGLPixelTransferOptions, lambda: Rituals.call(
        'ritual_ZN27QOpenGLPixelTransferOptionsC1ERKS_', self._valueOf(a0),
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

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLPixelTransferOptions::swap(QOpenGLPixelTransferOptions
    &other)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QOpenGLPixelTransferOptions.swap' has no cute function yet. Qt's "
        "'void "
        "QOpenGLPixelTransferOptions::swap(QOpenGLPixelTransferOptions "
        "&other)': takes a type Python has no way to hand over yet.")
