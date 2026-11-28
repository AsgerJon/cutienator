"""
QImageData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qimage_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QImageData to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from . import QImage

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QSize
  from . import QImageWriter
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QImageWriter = WAIT['QImageWriter']
  QSize = WAIT['QSize']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QImageData(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QImageData: a plain Python object standing in front
  of one C++ QImageData.

  C++ hands a QImageData around as a copy, so every C++ QImageData behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QImageData that has a ritual and that Python can
  call so far, 6 names in all: 'create', 'get', 'checkForAlphaPixels',
  'convertInPlace', 'doImageIO', 'calculateImageParameters'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QImageData::~QImageData()': the destructor: Python removes its C++
    QImageData by it, and has no other use for it.
  - Qt's 'QImageData *QImageData::create(uchar *data, int w, int h, qsizetype
    bpl, QImage::Format format, bool readOnly, QImageCleanupFunction
    cleanupFunction, void *cleanupInfo)': takes a number to change where it
    is.
  - Qt's 'QImageData *QImageData::get(QImage &img)': takes a type Python has
    no way to hand over yet.

  What to expect
  --------------

  - The C++ QImageData is created at the first use, not by 'QImageData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QImageData back gives a copy the ritual made for
    Python, in a new cute QImageData.
  """

  #  The classes Qt writes inside QImageData, each a class in here as in C++.

  class ImageSizeParameters(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QImageData::ImageSizeParameters: a plain Python
    object standing in front of one C++ QImageData::ImageSizeParameters.

    C++ hands a QImageData::ImageSizeParameters around as a copy, so every
    C++ QImageData::ImageSizeParameters behind a cute one is Python's own: it
    is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    Every function of Qt's QImageData::ImageSizeParameters that has a ritual
    and that Python can call so far, 1 name in all: 'isValid'. None can be
    made from Python: one comes out of a function of another class that gives
    one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QImageData::ImageSizeParameters::~ImageSizeParameters()': the
      destructor: Python removes its C++ QImageData::ImageSizeParameters by
      it, and has no other use for it.

    What to expect
    --------------

    - The C++ QImageData::ImageSizeParameters is created at the first use,
      not by 'QImageData::ImageSizeParameters(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QImageData::ImageSizeParameters back gives a copy
      the ritual made for Python, in a new cute
      QImageData::ImageSizeParameters.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QImageData::ImageSizeParameters'

    #  Qt's '~QImageData::ImageSizeParameters()'. Naming it makes this a
    #  value class: Python owns every C++ QImageData::ImageSizeParameters
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN10QImageData19ImageSizeParametersD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def isValid(self) -> bool:
      """
      Calls Qt's 'bool QImageData::ImageSizeParameters::isValid() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qimagedata-imagesizeparameters.html#isValid
      """
      #  bool QImageData::ImageSizeParameters::isValid() const
      return self.uglySide.call(
          'ritual_ZNK10QImageData19ImageSizeParameters7isValidEv',
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QSize, QImage.Format)
  def create(size: QSize, format: QImage.Format) -> Optional[QImageData]:
    """
    Calls Qt's 'QImageData *QImageData::create(const QSize &size,
    QImage::Format format)'.

    Qt's own words: https://doc.qt.io/qt-6/qimagedata.html#create

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    format : QImage.Format
      Passed on as its number.

    Returns
    -------

    Optional[QImageData]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QImageData *QImageData::create(const QSize &size, QImage::Format
    #      format)
    address = Rituals.call(
        'ritual_ZN10QImageData6createERK5QSizeN6QImage6FormatE',
        CuteMixin._valueOf(size), format.value,
    )
    return QImageData._cuteAt(address)

  @staticmethod
  @overload(QImage)
  def get(img: QImage) -> Optional[QImageData]:
    """
    Calls Qt's 'const QImageData *QImageData::get(const QImage &img)'.

    Qt's own words: https://doc.qt.io/qt-6/qimagedata.html#get

    Parameters
    ----------

    img : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.

    Returns
    -------

    Optional[QImageData]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QImageData *QImageData::get(const QImage &img)
    address = Rituals.call(
        'ritual_ZN10QImageData3getERK6QImage', CuteMixin._valueOf(img),
    )
    return QImageData._cuteAt(address)

  @staticmethod
  @overload(int, int, int)
  def calculateImageParameters(
      width: int,
      height: int,
      depth: int,
  ) -> ImageSizeParameters:
    """
    Calls Qt's 'ImageSizeParameters
    QImageData::calculateImageParameters(qsizetype width, qsizetype height,
    qsizetype depth)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qimagedata.html#calculateImageParameters

    Parameters
    ----------

    width : int
      Passed on as it is.

    height : int
      Passed on as it is.

    depth : int
      Passed on as it is.

    Returns
    -------

    ImageSizeParameters
      A new cute QImageData::ImageSizeParameters around the copy Qt gave
      back. Python owns it.
    """
    #  ImageSizeParameters QImageData::calculateImageParameters(qsizetype
    #      width, qsizetype height, qsizetype depth)
    address = Rituals.call(
        'ritual_ZN10QImageData24calculateImageParametersExxx',
        width, height, depth,
    )
    return QImageData.ImageSizeParameters._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QImageData'

  #  Qt's '~QImageData()'. Naming it makes this a value class: Python owns
  #  every C++ QImageData behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN10QImageDataD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def checkForAlphaPixels(self) -> bool:
    """
    Calls Qt's 'bool QImageData::checkForAlphaPixels() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qimagedata.html#checkForAlphaPixels
    """
    #  bool QImageData::checkForAlphaPixels() const
    return self.uglySide.call(
        'ritual_ZNK10QImageData19checkForAlphaPixelsEv',
    )

  @overload(QImage, QImageWriter, int)
  @overload(QImage, NoneType, int)
  @overload(NoneType, QImageWriter, int)
  @overload(NoneType, NoneType, int)
  def doImageIO(
      self,
      image: Optional[QImage],
      io: Optional[QImageWriter],
      quality: int,
  ) -> bool:
    """
    Calls Qt's 'bool QImageData::doImageIO(const QImage *image, QImageWriter
    *io, int quality) const'.

    Qt's own words: https://doc.qt.io/qt-6/qimagedata.html#doImageIO

    Parameters
    ----------

    image : Optional[QImage]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    io : Optional[QImageWriter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    quality : int
      Passed on as it is.
    """
    #  bool QImageData::doImageIO(const QImage *image, QImageWriter *io, int
    #      quality) const
    return self.uglySide.call(
        'ritual_ZNK10QImageData9doImageIOEPK6QImageP12QImageWriteri',
        self._addressOf(image), self._addressOf(io), quality,
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
    Notes what was given, for Qt's 'QImageData::QImageData()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qimagedata.html#QImageData
    """
    #  QImageData::QImageData()
    self._noteCreation(QImageData, lambda: Rituals.call(
        'ritual_ZN10QImageDataC1Ev',
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

  @overload(QImage.Format, Qt.ImageConversionFlags)
  def convertInPlace(
      self,
      newFormat: QImage.Format,
      a1: Qt.ImageConversionFlags,
  ) -> bool:
    """
    Calls Qt's 'bool QImageData::convertInPlace(QImage::Format newFormat,
    Qt::ImageConversionFlags a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qimagedata.html#convertInPlace

    Parameters
    ----------

    newFormat : QImage.Format
      Passed on as its number.

    a1 : Qt.ImageConversionFlags
      Passed on as its number.
    """
    #  bool QImageData::convertInPlace(QImage::Format newFormat,
    #      Qt::ImageConversionFlags a1)
    return self.uglySide.call(
        'ritual_ZN10QImageData14convertInPlaceEN6QImage6FormatE6QFlagsIN2Qt'
        '19ImageConversionFlagEE',
        newFormat.value, a1.value,
    )
