"""
Qt3DExtras::QTextureAtlasData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DExtras/6.12.0/Qt3DExtras/private/qtextureatlas_p_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DExtras::QTextureAtlasData to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtGui import QImage
from . import Qt3DExtras

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QByteArray


class QTextureAtlasData(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's Qt3DExtras::QTextureAtlasData: a plain Python object
  standing in front of one C++ Qt3DExtras::QTextureAtlasData.

  What exists
  -----------

  Every function of Qt's Qt3DExtras::QTextureAtlasData that has a ritual and
  that Python can call so far, 4 names in all: 'width', 'height', 'addImage',
  'createUpdatedImageData'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DExtras::QTextureAtlasData::~QTextureAtlasData()': the
    destructor: Python never removes a C++ Qt3DExtras::QTextureAtlasData.

  What to expect
  --------------

  - The C++ Qt3DExtras::QTextureAtlasData is created at the first use, not by
    'Qt3DExtras::QTextureAtlasData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DExtras::QTextureAtlasData.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DExtras::QTextureAtlasData'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def width(self) -> int:
    """
    Calls Qt's 'int Qt3DExtras::QTextureAtlasData::width() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qtextureatlasdata.html#width
    """
    #  int Qt3DExtras::QTextureAtlasData::width() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DExtras17QTextureAtlasData5widthEv',
    )

  def height(self) -> int:
    """
    Calls Qt's 'int Qt3DExtras::QTextureAtlasData::height() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qtextureatlasdata.html#height
    """
    #  int Qt3DExtras::QTextureAtlasData::height() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DExtras17QTextureAtlasData6heightEv',
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

  @overload(int, int, QImage.Format)
  def __init__(self, w: int, h: int, fmt: QImage.Format) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DExtras::QTextureAtlasData::QTextureAtlasData(int w, int h,
    QImage::Format fmt)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qtextureatlasdata.html

    Parameters
    ----------

    w : int
      Passed on as it is.

    h : int
      Passed on as it is.

    fmt : QImage.Format
      Passed on as its number.
    """
    #  Qt3DExtras::QTextureAtlasData::QTextureAtlasData(int w, int h,
    #      QImage::Format fmt)
    self._noteCreation(QTextureAtlasData, lambda: Rituals.call(
        'ritual_ZN10Qt3DExtras17QTextureAtlasDataC1EiiN6QImage6FormatE',
        w, h, fmt.value,
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

  @overload(WAIT['Qt3DExtras.AtlasTexture'], QImage)
  def addImage(
      self,
      texture: Qt3DExtras.AtlasTexture,
      image: QImage,
  ) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QTextureAtlasData::addImage(const
    AtlasTexture &texture, const QImage &image)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qtextureatlasdata.html#addImage

    Parameters
    ----------

    texture : Qt3DExtras.AtlasTexture
      Passed on as a value: Qt reads the C++ Qt3DExtras::AtlasTexture, which
      stays Python's own.

    image : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.
    """
    #  void Qt3DExtras::QTextureAtlasData::addImage(const AtlasTexture
    #      &texture, const QImage &image)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras17QTextureAtlasData8addImageERKNS_12AtlasText'
        'ureERK6QImage',
        self._valueOf(texture), self._valueOf(image),
    )

  def createUpdatedImageData(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray
    Qt3DExtras::QTextureAtlasData::createUpdatedImageData()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qtextureatlasdata.html

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray Qt3DExtras::QTextureAtlasData::createUpdatedImageData()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DExtras17QTextureAtlasData22createUpdatedImageDataEv',
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)
