"""
Qt3DRender::QTextureData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/qtexturedata.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QTextureData(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's Qt3DRender::QTextureData: a plain Python object
  standing in front of one C++ Qt3DRender::QTextureData.

  C++ hands a Qt3DRender::QTextureData around as a copy, so every C++
  Qt3DRender::QTextureData behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QTextureData that has a ritual and that
  Python can call so far, 30 names in all: 'target', 'setTarget', 'format',
  'setFormat', 'width', 'setWidth', 'height', 'setHeight', 'depth',
  'setDepth', 'layers', 'setLayers', 'isAutoMipMapGenerationEnabled',
  'setAutoMipMapGenerationEnabled', 'maximumAnisotropy',
  'setMaximumAnisotropy', 'minificationFilter', 'setMinificationFilter',
  'magnificationFilter', 'setMagnificationFilter', 'wrapModeX',
  'setWrapModeX', 'wrapModeY', 'setWrapModeY', 'wrapModeZ', 'setWrapModeZ',
  'comparisonFunction', 'setComparisonFunction', 'comparisonMode',
  'setComparisonMode'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DRender::QTextureData::~QTextureData()': the destructor: Python
    removes its C++ Qt3DRender::QTextureData by it, and has no other use for
    it.
  - Qt's 'QList<QTextureImageDataPtr> Qt3DRender::QTextureData::imageData()
    const': gives a type Python has no way to take yet.
  - Qt's 'void Qt3DRender::QTextureData::addImageData(const
    QTextureImageDataPtr &imageData)': takes a type Python has no way to hand
    over yet.

  What has no ritual
  ------------------

  2 of the 36 functions Qt declares: 2 the compiler refuses its ritual as it
  would be written here.

  What to expect
  --------------

  - The C++ Qt3DRender::QTextureData is created at the first use, not by
    'Qt3DRender::QTextureData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a Qt3DRender::QTextureData back gives a copy the ritual
    made for Python, in a new cute Qt3DRender::QTextureData.
  - Each name of Qt's Qt3DRender::QTextureData that has no cute function yet,
    'addImageData', 'd_func', 'imageData', holds a function that raises
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
  __qt_class__ = 'Qt3DRender::QTextureData'

  #  Qt's '~Qt3DRender::QTextureData()'. Naming it makes this a value class:
  #  Python owns every C++ Qt3DRender::QTextureData behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN10Qt3DRender12QTextureDataD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def target(self) -> Qt3DRender.QAbstractTexture.Target:
    """
    Calls Qt's 'QAbstractTexture::Target Qt3DRender::QTextureData::target()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtexturedata.html#target

    Returns
    -------

    Qt3DRender.QAbstractTexture.Target
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt3DRender.QAbstractTexture.Target(number)' gives.
    """
    #  QAbstractTexture::Target Qt3DRender::QTextureData::target() const
    return Qt3DRender.QAbstractTexture.Target(self.uglySide.call(
        'ritual_ZNK10Qt3DRender12QTextureData6targetEv',
    ))

  def format(self) -> Qt3DRender.QAbstractTexture.TextureFormat:
    """
    Calls Qt's 'QAbstractTexture::TextureFormat
    Qt3DRender::QTextureData::format() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtexturedata.html#format

    Returns
    -------

    Qt3DRender.QAbstractTexture.TextureFormat
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt3DRender.QAbstractTexture.TextureFormat(number)' gives.
    """
    #  QAbstractTexture::TextureFormat Qt3DRender::QTextureData::format()
    #      const
    return Qt3DRender.QAbstractTexture.TextureFormat(self.uglySide.call(
        'ritual_ZNK10Qt3DRender12QTextureData6formatEv',
    ))

  def width(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::QTextureData::width() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qtexturedata.html#width
    """
    #  int Qt3DRender::QTextureData::width() const
    return self.uglySide.call('ritual_ZNK10Qt3DRender12QTextureData5widthEv')

  def height(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::QTextureData::height() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtexturedata.html#height
    """
    #  int Qt3DRender::QTextureData::height() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender12QTextureData6heightEv',
    )

  def depth(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::QTextureData::depth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qtexturedata.html#depth
    """
    #  int Qt3DRender::QTextureData::depth() const
    return self.uglySide.call('ritual_ZNK10Qt3DRender12QTextureData5depthEv')

  def layers(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::QTextureData::layers() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtexturedata.html#layers
    """
    #  int Qt3DRender::QTextureData::layers() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender12QTextureData6layersEv',
    )

  def isAutoMipMapGenerationEnabled(self) -> bool:
    """
    Calls Qt's 'bool
    Qt3DRender::QTextureData::isAutoMipMapGenerationEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtexturedata.html
    """
    #  bool Qt3DRender::QTextureData::isAutoMipMapGenerationEnabled() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender12QTextureData29isAutoMipMapGenerationEnable'
        'dEv',
    )

  def maximumAnisotropy(self) -> float:
    """
    Calls Qt's 'float Qt3DRender::QTextureData::maximumAnisotropy() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtexturedata.html#maximumAnisotropy
    """
    #  float Qt3DRender::QTextureData::maximumAnisotropy() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender12QTextureData17maximumAnisotropyEv',
    )

  def minificationFilter(self) -> Qt3DRender.QAbstractTexture.Filter:
    """
    Calls Qt's 'QAbstractTexture::Filter
    Qt3DRender::QTextureData::minificationFilter() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtexturedata.html#minificationFilter

    Returns
    -------

    Qt3DRender.QAbstractTexture.Filter
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt3DRender.QAbstractTexture.Filter(number)' gives.
    """
    #  QAbstractTexture::Filter
    #      Qt3DRender::QTextureData::minificationFilter() const
    return Qt3DRender.QAbstractTexture.Filter(self.uglySide.call(
        'ritual_ZNK10Qt3DRender12QTextureData18minificationFilterEv',
    ))

  def magnificationFilter(self) -> Qt3DRender.QAbstractTexture.Filter:
    """
    Calls Qt's 'QAbstractTexture::Filter
    Qt3DRender::QTextureData::magnificationFilter() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtexturedata.html#magnificationFilter

    Returns
    -------

    Qt3DRender.QAbstractTexture.Filter
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt3DRender.QAbstractTexture.Filter(number)' gives.
    """
    #  QAbstractTexture::Filter
    #      Qt3DRender::QTextureData::magnificationFilter() const
    return Qt3DRender.QAbstractTexture.Filter(self.uglySide.call(
        'ritual_ZNK10Qt3DRender12QTextureData19magnificationFilterEv',
    ))

  def wrapModeX(self) -> Qt3DRender.QTextureWrapMode.WrapMode:
    """
    Calls Qt's 'QTextureWrapMode::WrapMode
    Qt3DRender::QTextureData::wrapModeX() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtexturedata.html#wrapModeX

    Returns
    -------

    Qt3DRender.QTextureWrapMode.WrapMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt3DRender.QTextureWrapMode.WrapMode(number)' gives.
    """
    #  QTextureWrapMode::WrapMode Qt3DRender::QTextureData::wrapModeX() const
    return Qt3DRender.QTextureWrapMode.WrapMode(self.uglySide.call(
        'ritual_ZNK10Qt3DRender12QTextureData9wrapModeXEv',
    ))

  def wrapModeY(self) -> Qt3DRender.QTextureWrapMode.WrapMode:
    """
    Calls Qt's 'QTextureWrapMode::WrapMode
    Qt3DRender::QTextureData::wrapModeY() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtexturedata.html#wrapModeY

    Returns
    -------

    Qt3DRender.QTextureWrapMode.WrapMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt3DRender.QTextureWrapMode.WrapMode(number)' gives.
    """
    #  QTextureWrapMode::WrapMode Qt3DRender::QTextureData::wrapModeY() const
    return Qt3DRender.QTextureWrapMode.WrapMode(self.uglySide.call(
        'ritual_ZNK10Qt3DRender12QTextureData9wrapModeYEv',
    ))

  def wrapModeZ(self) -> Qt3DRender.QTextureWrapMode.WrapMode:
    """
    Calls Qt's 'QTextureWrapMode::WrapMode
    Qt3DRender::QTextureData::wrapModeZ() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtexturedata.html#wrapModeZ

    Returns
    -------

    Qt3DRender.QTextureWrapMode.WrapMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt3DRender.QTextureWrapMode.WrapMode(number)' gives.
    """
    #  QTextureWrapMode::WrapMode Qt3DRender::QTextureData::wrapModeZ() const
    return Qt3DRender.QTextureWrapMode.WrapMode(self.uglySide.call(
        'ritual_ZNK10Qt3DRender12QTextureData9wrapModeZEv',
    ))

  def comparisonFunction(
      self,
  ) -> Qt3DRender.QAbstractTexture.ComparisonFunction:
    """
    Calls Qt's 'QAbstractTexture::ComparisonFunction
    Qt3DRender::QTextureData::comparisonFunction() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtexturedata.html#comparisonFunction

    Returns
    -------

    Qt3DRender.QAbstractTexture.ComparisonFunction
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt3DRender.QAbstractTexture.ComparisonFunction(number)' gives.
    """
    #  QAbstractTexture::ComparisonFunction
    #      Qt3DRender::QTextureData::comparisonFunction() const
    return Qt3DRender.QAbstractTexture.ComparisonFunction(self.uglySide.call(
        'ritual_ZNK10Qt3DRender12QTextureData18comparisonFunctionEv',
    ))

  def comparisonMode(self) -> Qt3DRender.QAbstractTexture.ComparisonMode:
    """
    Calls Qt's 'QAbstractTexture::ComparisonMode
    Qt3DRender::QTextureData::comparisonMode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtexturedata.html#comparisonMode

    Returns
    -------

    Qt3DRender.QAbstractTexture.ComparisonMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt3DRender.QAbstractTexture.ComparisonMode(number)' gives.
    """
    #  QAbstractTexture::ComparisonMode
    #      Qt3DRender::QTextureData::comparisonMode() const
    return Qt3DRender.QAbstractTexture.ComparisonMode(self.uglySide.call(
        'ritual_ZNK10Qt3DRender12QTextureData14comparisonModeEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Qt3DRender.QAbstractTexture.Target)
  def setTarget(self, target: Qt3DRender.QAbstractTexture.Target) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QTextureData::setTarget(QAbstractTexture::Target target)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtexturedata.html#setTarget

    Parameters
    ----------

    target : Qt3DRender.QAbstractTexture.Target
      Passed on as its number.
    """
    #  void Qt3DRender::QTextureData::setTarget(QAbstractTexture::Target
    #      target)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender12QTextureData9setTargetENS_16QAbstractTextur'
        'e6TargetE',
        target.value,
    )

  @overload(Qt3DRender.QAbstractTexture.TextureFormat)
  def setFormat(self, a0: Qt3DRender.QAbstractTexture.TextureFormat) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QTextureData::setFormat(QAbstractTexture::TextureFormat a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtexturedata.html#setFormat

    Parameters
    ----------

    a0 : Qt3DRender.QAbstractTexture.TextureFormat
      Passed on as its number.
    """
    #  void Qt3DRender::QTextureData::setFormat(QAbstractTexture::
    #      TextureFormat a0)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender12QTextureData9setFormatENS_16QAbstractTextur'
        'e13TextureFormatE',
        a0.value,
    )

  @overload(int)
  def setWidth(self, width: int) -> None:
    """
    Calls Qt's 'void Qt3DRender::QTextureData::setWidth(int width)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtexturedata.html#setWidth

    Parameters
    ----------

    width : int
      Passed on as it is.
    """
    #  void Qt3DRender::QTextureData::setWidth(int width)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender12QTextureData8setWidthEi', width,
    )

  @overload(int)
  def setHeight(self, height: int) -> None:
    """
    Calls Qt's 'void Qt3DRender::QTextureData::setHeight(int height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtexturedata.html#setHeight

    Parameters
    ----------

    height : int
      Passed on as it is.
    """
    #  void Qt3DRender::QTextureData::setHeight(int height)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender12QTextureData9setHeightEi', height,
    )

  @overload(int)
  def setDepth(self, depth: int) -> None:
    """
    Calls Qt's 'void Qt3DRender::QTextureData::setDepth(int depth)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtexturedata.html#setDepth

    Parameters
    ----------

    depth : int
      Passed on as it is.
    """
    #  void Qt3DRender::QTextureData::setDepth(int depth)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender12QTextureData8setDepthEi', depth,
    )

  @overload(int)
  def setLayers(self, layers: int) -> None:
    """
    Calls Qt's 'void Qt3DRender::QTextureData::setLayers(int layers)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtexturedata.html#setLayers

    Parameters
    ----------

    layers : int
      Passed on as it is.
    """
    #  void Qt3DRender::QTextureData::setLayers(int layers)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender12QTextureData9setLayersEi', layers,
    )

  @overload(bool)
  def setAutoMipMapGenerationEnabled(
      self,
      isAutoMipMapGenerationEnabled: bool,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QTextureData::setAutoMipMapGenerationEnabled(bool
    isAutoMipMapGenerationEnabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtexturedata.html

    Parameters
    ----------

    isAutoMipMapGenerationEnabled : bool
      Passed on as it is.
    """
    #  void Qt3DRender::QTextureData::setAutoMipMapGenerationEnabled(bool
    #      isAutoMipMapGenerationEnabled)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender12QTextureData30setAutoMipMapGenerationEnable'
        'dEb',
        isAutoMipMapGenerationEnabled,
    )

  @overload(float)
  def setMaximumAnisotropy(self, maximumAnisotropy: float) -> None:
    """
    Calls Qt's 'void Qt3DRender::QTextureData::setMaximumAnisotropy(float
    maximumAnisotropy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtexturedata.html#setMaximumAnisotropy

    Parameters
    ----------

    maximumAnisotropy : float
      Passed on as it is.
    """
    #  void Qt3DRender::QTextureData::setMaximumAnisotropy(float
    #      maximumAnisotropy)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender12QTextureData20setMaximumAnisotropyEf',
        maximumAnisotropy,
    )

  @overload(Qt3DRender.QAbstractTexture.Filter)
  def setMinificationFilter(
      self,
      filter: Qt3DRender.QAbstractTexture.Filter,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QTextureData::setMinificationFilter(QAbstractTexture::Filter
    filter)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtexturedata.html#setMinificationFilter

    Parameters
    ----------

    filter : Qt3DRender.QAbstractTexture.Filter
      Passed on as its number.
    """
    #  void Qt3DRender::QTextureData::setMinificationFilter(
    #      QAbstractTexture::Filter filter)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender12QTextureData21setMinificationFilterENS_16QA'
        'bstractTexture6FilterE',
        filter.value,
    )

  @overload(Qt3DRender.QAbstractTexture.Filter)
  def setMagnificationFilter(
      self,
      filter: Qt3DRender.QAbstractTexture.Filter,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QTextureData::setMagnificationFilter(QAbstractTexture::Filter
    filter)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtexturedata.html

    Parameters
    ----------

    filter : Qt3DRender.QAbstractTexture.Filter
      Passed on as its number.
    """
    #  void Qt3DRender::QTextureData::setMagnificationFilter(
    #      QAbstractTexture::Filter filter)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender12QTextureData22setMagnificationFilterENS_16Q'
        'AbstractTexture6FilterE',
        filter.value,
    )

  @overload(Qt3DRender.QTextureWrapMode.WrapMode)
  def setWrapModeX(
      self,
      wrapModeX: Qt3DRender.QTextureWrapMode.WrapMode,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QTextureData::setWrapModeX(QTextureWrapMode::WrapMode
    wrapModeX)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtexturedata.html#setWrapModeX

    Parameters
    ----------

    wrapModeX : Qt3DRender.QTextureWrapMode.WrapMode
      Passed on as its number.
    """
    #  void Qt3DRender::QTextureData::setWrapModeX(QTextureWrapMode::WrapMode
    #      wrapModeX)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender12QTextureData12setWrapModeXENS_16QTextureWra'
        'pMode8WrapModeE',
        wrapModeX.value,
    )

  @overload(Qt3DRender.QTextureWrapMode.WrapMode)
  def setWrapModeY(
      self,
      wrapModeY: Qt3DRender.QTextureWrapMode.WrapMode,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QTextureData::setWrapModeY(QTextureWrapMode::WrapMode
    wrapModeY)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtexturedata.html#setWrapModeY

    Parameters
    ----------

    wrapModeY : Qt3DRender.QTextureWrapMode.WrapMode
      Passed on as its number.
    """
    #  void Qt3DRender::QTextureData::setWrapModeY(QTextureWrapMode::WrapMode
    #      wrapModeY)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender12QTextureData12setWrapModeYENS_16QTextureWra'
        'pMode8WrapModeE',
        wrapModeY.value,
    )

  @overload(Qt3DRender.QTextureWrapMode.WrapMode)
  def setWrapModeZ(
      self,
      wrapModeZ: Qt3DRender.QTextureWrapMode.WrapMode,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QTextureData::setWrapModeZ(QTextureWrapMode::WrapMode
    wrapModeZ)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtexturedata.html#setWrapModeZ

    Parameters
    ----------

    wrapModeZ : Qt3DRender.QTextureWrapMode.WrapMode
      Passed on as its number.
    """
    #  void Qt3DRender::QTextureData::setWrapModeZ(QTextureWrapMode::WrapMode
    #      wrapModeZ)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender12QTextureData12setWrapModeZENS_16QTextureWra'
        'pMode8WrapModeE',
        wrapModeZ.value,
    )

  @overload(Qt3DRender.QAbstractTexture.ComparisonFunction)
  def setComparisonFunction(
      self,
      comparisonFunction: Qt3DRender.QAbstractTexture.ComparisonFunction,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QTextureData::setComparisonFunction(QAbstractTexture::
    ComparisonFunction comparisonFunction)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtexturedata.html#setComparisonFunction

    Parameters
    ----------

    comparisonFunction : Qt3DRender.QAbstractTexture.ComparisonFunction
      Passed on as its number.
    """
    #  void Qt3DRender::QTextureData::setComparisonFunction(
    #      QAbstractTexture::ComparisonFunction comparisonFunction)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender12QTextureData21setComparisonFunctionENS_16QA'
        'bstractTexture18ComparisonFunctionE',
        comparisonFunction.value,
    )

  @overload(Qt3DRender.QAbstractTexture.ComparisonMode)
  def setComparisonMode(
      self,
      comparisonMode: Qt3DRender.QAbstractTexture.ComparisonMode,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QTextureData::setComparisonMode(QAbstractTexture::
    ComparisonMode comparisonMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtexturedata.html#setComparisonMode

    Parameters
    ----------

    comparisonMode : Qt3DRender.QAbstractTexture.ComparisonMode
      Passed on as its number.
    """
    #  void Qt3DRender::QTextureData::setComparisonMode(QAbstractTexture::
    #      ComparisonMode comparisonMode)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender12QTextureData17setComparisonModeENS_16QAbstr'
        'actTexture14ComparisonModeE',
        comparisonMode.value,
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
    'Qt3DRender::QTextureData::QTextureData()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtexturedata.html#QTextureData
    """
    #  Qt3DRender::QTextureData::QTextureData()
    self._noteCreation(QTextureData, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender12QTextureDataC1Ev',
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
  def addImageData(*__, **_) -> Never:
    """
    Qt's 'void Qt3DRender::QTextureData::addImageData(const
    QTextureImageDataPtr &imageData)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.QTextureData.addImageData' has no cute function yet. "
        "Qt's 'void Qt3DRender::QTextureData::addImageData(const "
        "QTextureImageDataPtr &imageData)': takes a type Python has no way "
        "to hand over yet.")

  @staticmethod
  def d_func(*__, **_) -> Never:
    """
    - Qt's 'QTextureDataPrivate *Qt3DRender::QTextureData::d_func()': the
      compiler refuses its ritual as it would be written here: unknown type
      name 'QTextureDataPrivate'; did you mean
      'Qt3DRender::QTextureDataPrivate'?.
    - Qt's 'const QTextureDataPrivate *Qt3DRender::QTextureData::d_func()
      const': the compiler refuses its ritual as it would be written here:
      unknown type name 'QTextureDataPrivate'; did you mean
      'Qt3DRender::QTextureDataPrivate'?.
    """
    raise NotImplementedError(
        "'Qt3DRender.QTextureData.d_func' has no cute function yet. Qt's "
        "'QTextureDataPrivate *Qt3DRender::QTextureData::d_func()': the "
        "compiler refuses its ritual as it would be written here: unknown "
        "type name 'QTextureDataPrivate'; did you mean "
        "'Qt3DRender::QTextureDataPrivate'?. Qt's 'const "
        "QTextureDataPrivate *Qt3DRender::QTextureData::d_func() const': "
        "the compiler refuses its ritual as it would be written here: "
        "unknown type name 'QTextureDataPrivate'; did you mean "
        "'Qt3DRender::QTextureDataPrivate'?.")

  @staticmethod
  def imageData(*__, **_) -> Never:
    """
    Qt's 'QList<QTextureImageDataPtr> Qt3DRender::QTextureData::imageData()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.QTextureData.imageData' has no cute function yet. Qt's "
        "'QList<QTextureImageDataPtr> Qt3DRender::QTextureData::imageData() "
        "const': gives a type Python has no way to take yet.")
