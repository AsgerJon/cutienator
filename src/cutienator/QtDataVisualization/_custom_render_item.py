"""
CustomRenderItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDataVisualization/6.12.0/QtDataVisualization/private/customrenderitem_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means CustomRenderItem to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QList
from ..QtGui import QImage
from . import AbstractRenderItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtGui import QColor, QVector3D, QVector4D
  from . import Abstract3DRenderer, ObjectHelper, QCustom3DItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  Abstract3DRenderer = WAIT['Abstract3DRenderer']
  QColor = WAIT['QColor']
  QCustom3DItem = WAIT['QtDataVisualization:QCustom3DItem']
  QVector3D = WAIT['QVector3D']
  QVector4D = WAIT['QVector4D']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class CustomRenderItem(AbstractRenderItem):
  """
  The cute side of Qt's CustomRenderItem: a plain Python object standing in
  front of one C++ CustomRenderItem.

  It is built on the cute 'AbstractRenderItem', as Qt's CustomRenderItem is
  built on Qt's AbstractRenderItem, and has everything that class has.

  What exists
  -----------

  Every function of Qt's CustomRenderItem that has a ritual and that Python
  can call so far, 76 names in all: 'setTexture', 'texture', 'mesh',
  'setScaling', 'scaling', 'setOrigScaling', 'origScaling', 'setPosition',
  'position', 'setOrigPosition', 'origPosition', 'setPositionAbsolute',
  'isPositionAbsolute', 'setScalingAbsolute', 'isScalingAbsolute',
  'setBlendNeeded', 'isBlendNeeded', 'setVisible', 'isVisible',
  'setItemPointer', 'itemPointer', 'setValid', 'isValid', 'setIndex',
  'index', 'setShadowCasting', 'isShadowCasting', 'setFacingCamera',
  'isFacingCamera', 'setRenderer', 'setLabelItem', 'isLabel',
  'setTextureWidth', 'textureWidth', 'setTextureHeight', 'textureHeight',
  'setTextureDepth', 'textureDepth', 'textureSize', 'setColorTable',
  'colorTable', 'setVolume', 'isVolume', 'setTextureFormat', 'textureFormat',
  'setSliceIndexX', 'setSliceIndexY', 'setSliceIndexZ', 'sliceFractions',
  'sliceIndexX', 'sliceIndexY', 'sliceIndexZ', 'setAlphaMultiplier',
  'alphaMultiplier', 'setPreserveOpacity', 'preserveOpacity',
  'setUseHighDefShader', 'useHighDefShader', 'setMinBounds', 'minBounds',
  'setMaxBounds', 'maxBounds', 'minBoundsNormal', 'maxBoundsNormal',
  'setDrawSlices', 'drawSlices', 'setDrawSliceFrames', 'drawSliceFrames',
  'setSliceFrameColor', 'sliceFrameColor', 'setSliceFrameWidths',
  'sliceFrameWidths', 'setSliceFrameGaps', 'sliceFrameGaps',
  'setSliceFrameThicknesses', 'sliceFrameThicknesses'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'CustomRenderItem::~CustomRenderItem()': the destructor: Python
    never removes a C++ CustomRenderItem.
  - Qt's 'void CustomRenderItem::setColorTable(const QList<QRgb> &colors)':
    takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 82 functions Qt declares: 2 forbidden; 2 leans on 'ObjectHelper.

  What to expect
  --------------

  - The C++ CustomRenderItem is created at the first use, not by
    'CustomRenderItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ CustomRenderItem.
  - Each name of Qt's CustomRenderItem that has no cute function yet,
    '__init__', 'setMesh', holds a function that raises
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
  __qt_class__ = 'CustomRenderItem'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def texture(self) -> int:
    """
    Calls Qt's 'GLuint CustomRenderItem::texture() const'.

    Qt's own words: https://doc.qt.io/qt-6/customrenderitem.html#texture
    """
    #  GLuint CustomRenderItem::texture() const
    return self.uglySide.call('ritual_ZNK16CustomRenderItem7textureEv')

  def mesh(self) -> Optional[ObjectHelper]:
    """
    Calls Qt's 'ObjectHelper *CustomRenderItem::mesh() const'.

    Qt's own words: https://doc.qt.io/qt-6/customrenderitem.html#mesh

    Returns
    -------

    Optional[ObjectHelper]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  ObjectHelper *CustomRenderItem::mesh() const
    address = self.uglySide.call('ritual_ZNK16CustomRenderItem4meshEv')
    from . import ObjectHelper
    return ObjectHelper._cuteAt(address)

  def scaling(self) -> QVector3D:
    """
    Calls Qt's 'const QVector3D &CustomRenderItem::scaling() const'.

    Qt's own words: https://doc.qt.io/qt-6/customrenderitem.html#scaling

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  const QVector3D &CustomRenderItem::scaling() const
    address = self.uglySide.call('ritual_ZNK16CustomRenderItem7scalingEv')
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def origScaling(self) -> QVector3D:
    """
    Calls Qt's 'const QVector3D &CustomRenderItem::origScaling() const'.

    Qt's own words: https://doc.qt.io/qt-6/customrenderitem.html#origScaling

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  const QVector3D &CustomRenderItem::origScaling() const
    address = self.uglySide.call(
        'ritual_ZNK16CustomRenderItem11origScalingEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def position(self) -> QVector3D:
    """
    Calls Qt's 'const QVector3D &CustomRenderItem::position() const'.

    Qt's own words: https://doc.qt.io/qt-6/customrenderitem.html#position

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  const QVector3D &CustomRenderItem::position() const
    address = self.uglySide.call('ritual_ZNK16CustomRenderItem8positionEv')
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def origPosition(self) -> QVector3D:
    """
    Calls Qt's 'const QVector3D &CustomRenderItem::origPosition() const'.

    Qt's own words: https://doc.qt.io/qt-6/customrenderitem.html#origPosition

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  const QVector3D &CustomRenderItem::origPosition() const
    address = self.uglySide.call(
        'ritual_ZNK16CustomRenderItem12origPositionEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def isPositionAbsolute(self) -> bool:
    """
    Calls Qt's 'bool CustomRenderItem::isPositionAbsolute() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/customrenderitem.html#isPositionAbsolute
    """
    #  bool CustomRenderItem::isPositionAbsolute() const
    return self.uglySide.call(
        'ritual_ZNK16CustomRenderItem18isPositionAbsoluteEv',
    )

  def isScalingAbsolute(self) -> bool:
    """
    Calls Qt's 'bool CustomRenderItem::isScalingAbsolute() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/customrenderitem.html#isScalingAbsolute
    """
    #  bool CustomRenderItem::isScalingAbsolute() const
    return self.uglySide.call(
        'ritual_ZNK16CustomRenderItem17isScalingAbsoluteEv',
    )

  def isBlendNeeded(self) -> bool:
    """
    Calls Qt's 'bool CustomRenderItem::isBlendNeeded() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/customrenderitem.html#isBlendNeeded
    """
    #  bool CustomRenderItem::isBlendNeeded() const
    return self.uglySide.call(
        'ritual_ZNK16CustomRenderItem13isBlendNeededEv',
    )

  def isVisible(self) -> bool:
    """
    Calls Qt's 'bool CustomRenderItem::isVisible() const'.

    Qt's own words: https://doc.qt.io/qt-6/customrenderitem.html#isVisible
    """
    #  bool CustomRenderItem::isVisible() const
    return self.uglySide.call('ritual_ZNK16CustomRenderItem9isVisibleEv')

  def itemPointer(self) -> Optional[QCustom3DItem]:
    """
    Calls Qt's 'QCustom3DItem *CustomRenderItem::itemPointer() const'.

    Qt's own words: https://doc.qt.io/qt-6/customrenderitem.html#itemPointer

    Returns
    -------

    Optional[QCustom3DItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCustom3DItem *CustomRenderItem::itemPointer() const
    address = self.uglySide.call(
        'ritual_ZNK16CustomRenderItem11itemPointerEv',
    )
    from . import QCustom3DItem
    return QCustom3DItem._cuteAt(address)

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool CustomRenderItem::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/customrenderitem.html#isValid
    """
    #  bool CustomRenderItem::isValid() const
    return self.uglySide.call('ritual_ZNK16CustomRenderItem7isValidEv')

  def index(self) -> int:
    """
    Calls Qt's 'int CustomRenderItem::index() const'.

    Qt's own words: https://doc.qt.io/qt-6/customrenderitem.html#index
    """
    #  int CustomRenderItem::index() const
    return self.uglySide.call('ritual_ZNK16CustomRenderItem5indexEv')

  def isShadowCasting(self) -> bool:
    """
    Calls Qt's 'bool CustomRenderItem::isShadowCasting() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/customrenderitem.html#isShadowCasting
    """
    #  bool CustomRenderItem::isShadowCasting() const
    return self.uglySide.call(
        'ritual_ZNK16CustomRenderItem15isShadowCastingEv',
    )

  def isFacingCamera(self) -> bool:
    """
    Calls Qt's 'bool CustomRenderItem::isFacingCamera() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/customrenderitem.html#isFacingCamera
    """
    #  bool CustomRenderItem::isFacingCamera() const
    return self.uglySide.call(
        'ritual_ZNK16CustomRenderItem14isFacingCameraEv',
    )

  def isLabel(self) -> bool:
    """
    Calls Qt's 'bool CustomRenderItem::isLabel() const'.

    Qt's own words: https://doc.qt.io/qt-6/customrenderitem.html#isLabel
    """
    #  bool CustomRenderItem::isLabel() const
    return self.uglySide.call('ritual_ZNK16CustomRenderItem7isLabelEv')

  def textureWidth(self) -> int:
    """
    Calls Qt's 'int CustomRenderItem::textureWidth() const'.

    Qt's own words: https://doc.qt.io/qt-6/customrenderitem.html#textureWidth
    """
    #  int CustomRenderItem::textureWidth() const
    return self.uglySide.call('ritual_ZNK16CustomRenderItem12textureWidthEv')

  def textureHeight(self) -> int:
    """
    Calls Qt's 'int CustomRenderItem::textureHeight() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/customrenderitem.html#textureHeight
    """
    #  int CustomRenderItem::textureHeight() const
    return self.uglySide.call(
        'ritual_ZNK16CustomRenderItem13textureHeightEv',
    )

  def textureDepth(self) -> int:
    """
    Calls Qt's 'int CustomRenderItem::textureDepth() const'.

    Qt's own words: https://doc.qt.io/qt-6/customrenderitem.html#textureDepth
    """
    #  int CustomRenderItem::textureDepth() const
    return self.uglySide.call('ritual_ZNK16CustomRenderItem12textureDepthEv')

  def textureSize(self) -> int:
    """
    Calls Qt's 'int CustomRenderItem::textureSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/customrenderitem.html#textureSize
    """
    #  int CustomRenderItem::textureSize() const
    return self.uglySide.call('ritual_ZNK16CustomRenderItem11textureSizeEv')

  def colorTable(self) -> QList[QVector4D]:
    """
    Calls Qt's 'const QList<QVector4D> &CustomRenderItem::colorTable()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/customrenderitem.html#colorTable

    Returns
    -------

    QList[QVector4D]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  const QList<QVector4D> &CustomRenderItem::colorTable() const
    address = self.uglySide.call(
        'ritual_ZNK16CustomRenderItem10colorTableEv',
    )
    from ..QtGui import QVector4D
    return QList[QVector4D]._cuteOwning(address)

  def isVolume(self) -> bool:
    """
    Calls Qt's 'bool CustomRenderItem::isVolume() const'.

    Qt's own words: https://doc.qt.io/qt-6/customrenderitem.html#isVolume
    """
    #  bool CustomRenderItem::isVolume() const
    return self.uglySide.call('ritual_ZNK16CustomRenderItem8isVolumeEv')

  def textureFormat(self) -> QImage.Format:
    """
    Calls Qt's 'QImage::Format CustomRenderItem::textureFormat() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/customrenderitem.html#textureFormat

    Returns
    -------

    QImage.Format
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QImage.Format(number)'
      gives.
    """
    #  QImage::Format CustomRenderItem::textureFormat() const
    return QImage.Format(self.uglySide.call(
        'ritual_ZNK16CustomRenderItem13textureFormatEv',
    ))

  def sliceFractions(self) -> QVector3D:
    """
    Calls Qt's 'const QVector3D &CustomRenderItem::sliceFractions() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/customrenderitem.html#sliceFractions

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  const QVector3D &CustomRenderItem::sliceFractions() const
    address = self.uglySide.call(
        'ritual_ZNK16CustomRenderItem14sliceFractionsEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def sliceIndexX(self) -> int:
    """
    Calls Qt's 'int CustomRenderItem::sliceIndexX() const'.

    Qt's own words: https://doc.qt.io/qt-6/customrenderitem.html#sliceIndexX
    """
    #  int CustomRenderItem::sliceIndexX() const
    return self.uglySide.call('ritual_ZNK16CustomRenderItem11sliceIndexXEv')

  def sliceIndexY(self) -> int:
    """
    Calls Qt's 'int CustomRenderItem::sliceIndexY() const'.

    Qt's own words: https://doc.qt.io/qt-6/customrenderitem.html#sliceIndexY
    """
    #  int CustomRenderItem::sliceIndexY() const
    return self.uglySide.call('ritual_ZNK16CustomRenderItem11sliceIndexYEv')

  def sliceIndexZ(self) -> int:
    """
    Calls Qt's 'int CustomRenderItem::sliceIndexZ() const'.

    Qt's own words: https://doc.qt.io/qt-6/customrenderitem.html#sliceIndexZ
    """
    #  int CustomRenderItem::sliceIndexZ() const
    return self.uglySide.call('ritual_ZNK16CustomRenderItem11sliceIndexZEv')

  def alphaMultiplier(self) -> float:
    """
    Calls Qt's 'float CustomRenderItem::alphaMultiplier() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/customrenderitem.html#alphaMultiplier
    """
    #  float CustomRenderItem::alphaMultiplier() const
    return self.uglySide.call(
        'ritual_ZNK16CustomRenderItem15alphaMultiplierEv',
    )

  def preserveOpacity(self) -> bool:
    """
    Calls Qt's 'bool CustomRenderItem::preserveOpacity() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/customrenderitem.html#preserveOpacity
    """
    #  bool CustomRenderItem::preserveOpacity() const
    return self.uglySide.call(
        'ritual_ZNK16CustomRenderItem15preserveOpacityEv',
    )

  def useHighDefShader(self) -> bool:
    """
    Calls Qt's 'bool CustomRenderItem::useHighDefShader() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/customrenderitem.html#useHighDefShader
    """
    #  bool CustomRenderItem::useHighDefShader() const
    return self.uglySide.call(
        'ritual_ZNK16CustomRenderItem16useHighDefShaderEv',
    )

  def minBounds(self) -> QVector3D:
    """
    Calls Qt's 'const QVector3D &CustomRenderItem::minBounds() const'.

    Qt's own words: https://doc.qt.io/qt-6/customrenderitem.html#minBounds

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  const QVector3D &CustomRenderItem::minBounds() const
    address = self.uglySide.call('ritual_ZNK16CustomRenderItem9minBoundsEv')
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def maxBounds(self) -> QVector3D:
    """
    Calls Qt's 'const QVector3D &CustomRenderItem::maxBounds() const'.

    Qt's own words: https://doc.qt.io/qt-6/customrenderitem.html#maxBounds

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  const QVector3D &CustomRenderItem::maxBounds() const
    address = self.uglySide.call('ritual_ZNK16CustomRenderItem9maxBoundsEv')
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def minBoundsNormal(self) -> QVector3D:
    """
    Calls Qt's 'const QVector3D &CustomRenderItem::minBoundsNormal() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/customrenderitem.html#minBoundsNormal

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  const QVector3D &CustomRenderItem::minBoundsNormal() const
    address = self.uglySide.call(
        'ritual_ZNK16CustomRenderItem15minBoundsNormalEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def maxBoundsNormal(self) -> QVector3D:
    """
    Calls Qt's 'const QVector3D &CustomRenderItem::maxBoundsNormal() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/customrenderitem.html#maxBoundsNormal

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  const QVector3D &CustomRenderItem::maxBoundsNormal() const
    address = self.uglySide.call(
        'ritual_ZNK16CustomRenderItem15maxBoundsNormalEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def drawSlices(self) -> bool:
    """
    Calls Qt's 'bool CustomRenderItem::drawSlices() const'.

    Qt's own words: https://doc.qt.io/qt-6/customrenderitem.html#drawSlices
    """
    #  bool CustomRenderItem::drawSlices() const
    return self.uglySide.call('ritual_ZNK16CustomRenderItem10drawSlicesEv')

  def drawSliceFrames(self) -> bool:
    """
    Calls Qt's 'bool CustomRenderItem::drawSliceFrames() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/customrenderitem.html#drawSliceFrames
    """
    #  bool CustomRenderItem::drawSliceFrames() const
    return self.uglySide.call(
        'ritual_ZNK16CustomRenderItem15drawSliceFramesEv',
    )

  def sliceFrameColor(self) -> QVector4D:
    """
    Calls Qt's 'const QVector4D &CustomRenderItem::sliceFrameColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/customrenderitem.html#sliceFrameColor

    Returns
    -------

    QVector4D
      A new cute QVector4D around the copy Qt gave back. Python owns it.
    """
    #  const QVector4D &CustomRenderItem::sliceFrameColor() const
    address = self.uglySide.call(
        'ritual_ZNK16CustomRenderItem15sliceFrameColorEv',
    )
    from ..QtGui import QVector4D
    return QVector4D._cuteOwning(address)

  def sliceFrameWidths(self) -> QVector3D:
    """
    Calls Qt's 'const QVector3D &CustomRenderItem::sliceFrameWidths() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/customrenderitem.html#sliceFrameWidths

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  const QVector3D &CustomRenderItem::sliceFrameWidths() const
    address = self.uglySide.call(
        'ritual_ZNK16CustomRenderItem16sliceFrameWidthsEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def sliceFrameGaps(self) -> QVector3D:
    """
    Calls Qt's 'const QVector3D &CustomRenderItem::sliceFrameGaps() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/customrenderitem.html#sliceFrameGaps

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  const QVector3D &CustomRenderItem::sliceFrameGaps() const
    address = self.uglySide.call(
        'ritual_ZNK16CustomRenderItem14sliceFrameGapsEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def sliceFrameThicknesses(self) -> QVector3D:
    """
    Calls Qt's 'const QVector3D &CustomRenderItem::sliceFrameThicknesses()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/customrenderitem.html#sliceFrameThicknesses

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  const QVector3D &CustomRenderItem::sliceFrameThicknesses() const
    address = self.uglySide.call(
        'ritual_ZNK16CustomRenderItem21sliceFrameThicknessesEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setTexture(self, texture: int) -> None:
    """
    Calls Qt's 'void CustomRenderItem::setTexture(GLuint texture)'.

    Qt's own words: https://doc.qt.io/qt-6/customrenderitem.html#setTexture

    Parameters
    ----------

    texture : int
      Passed on as it is.
    """
    #  void CustomRenderItem::setTexture(GLuint texture)
    self.uglySide.call('ritual_ZN16CustomRenderItem10setTextureEj', texture)

  @overload(QVector3D)
  def setScaling(self, scaling: QVector3D) -> None:
    """
    Calls Qt's 'void CustomRenderItem::setScaling(const QVector3D &scaling)'.

    Qt's own words: https://doc.qt.io/qt-6/customrenderitem.html#setScaling

    Parameters
    ----------

    scaling : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void CustomRenderItem::setScaling(const QVector3D &scaling)
    self.uglySide.call(
        'ritual_ZN16CustomRenderItem10setScalingERK9QVector3D',
        self._valueOf(scaling),
    )

  @overload(QVector3D)
  def setOrigScaling(self, scaling: QVector3D) -> None:
    """
    Calls Qt's 'void CustomRenderItem::setOrigScaling(const QVector3D
    &scaling)'.

    Qt's own words:
    https://doc.qt.io/qt-6/customrenderitem.html#setOrigScaling

    Parameters
    ----------

    scaling : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void CustomRenderItem::setOrigScaling(const QVector3D &scaling)
    self.uglySide.call(
        'ritual_ZN16CustomRenderItem14setOrigScalingERK9QVector3D',
        self._valueOf(scaling),
    )

  @overload(QVector3D)
  def setPosition(self, position: QVector3D) -> None:
    """
    Calls Qt's 'void CustomRenderItem::setPosition(const QVector3D
    &position)'.

    Qt's own words: https://doc.qt.io/qt-6/customrenderitem.html#setPosition

    Parameters
    ----------

    position : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void CustomRenderItem::setPosition(const QVector3D &position)
    self.uglySide.call(
        'ritual_ZN16CustomRenderItem11setPositionERK9QVector3D',
        self._valueOf(position),
    )

  @overload(QVector3D)
  def setOrigPosition(self, position: QVector3D) -> None:
    """
    Calls Qt's 'void CustomRenderItem::setOrigPosition(const QVector3D
    &position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/customrenderitem.html#setOrigPosition

    Parameters
    ----------

    position : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void CustomRenderItem::setOrigPosition(const QVector3D &position)
    self.uglySide.call(
        'ritual_ZN16CustomRenderItem15setOrigPositionERK9QVector3D',
        self._valueOf(position),
    )

  @overload(bool)
  def setPositionAbsolute(self, absolute: bool) -> None:
    """
    Calls Qt's 'void CustomRenderItem::setPositionAbsolute(bool absolute)'.

    Qt's own words:
    https://doc.qt.io/qt-6/customrenderitem.html#setPositionAbsolute

    Parameters
    ----------

    absolute : bool
      Passed on as it is.
    """
    #  void CustomRenderItem::setPositionAbsolute(bool absolute)
    self.uglySide.call(
        'ritual_ZN16CustomRenderItem19setPositionAbsoluteEb', absolute,
    )

  @overload(bool)
  def setScalingAbsolute(self, absolute: bool) -> None:
    """
    Calls Qt's 'void CustomRenderItem::setScalingAbsolute(bool absolute)'.

    Qt's own words:
    https://doc.qt.io/qt-6/customrenderitem.html#setScalingAbsolute

    Parameters
    ----------

    absolute : bool
      Passed on as it is.
    """
    #  void CustomRenderItem::setScalingAbsolute(bool absolute)
    self.uglySide.call(
        'ritual_ZN16CustomRenderItem18setScalingAbsoluteEb', absolute,
    )

  @overload(bool)
  def setBlendNeeded(self, blend: bool) -> None:
    """
    Calls Qt's 'void CustomRenderItem::setBlendNeeded(bool blend)'.

    Qt's own words:
    https://doc.qt.io/qt-6/customrenderitem.html#setBlendNeeded

    Parameters
    ----------

    blend : bool
      Passed on as it is.
    """
    #  void CustomRenderItem::setBlendNeeded(bool blend)
    self.uglySide.call(
        'ritual_ZN16CustomRenderItem14setBlendNeededEb', blend,
    )

  @overload(bool)
  def setVisible(self, visible: bool) -> None:
    """
    Calls Qt's 'void CustomRenderItem::setVisible(bool visible)'.

    Qt's own words: https://doc.qt.io/qt-6/customrenderitem.html#setVisible

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void CustomRenderItem::setVisible(bool visible)
    self.uglySide.call('ritual_ZN16CustomRenderItem10setVisibleEb', visible)

  @overload(QCustom3DItem)
  @overload(NoneType)
  def setItemPointer(self, item: Optional[QCustom3DItem]) -> None:
    """
    Calls Qt's 'void CustomRenderItem::setItemPointer(QCustom3DItem *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/customrenderitem.html#setItemPointer

    Parameters
    ----------

    item : Optional[QCustom3DItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void CustomRenderItem::setItemPointer(QCustom3DItem *item)
    self.uglySide.call(
        'ritual_ZN16CustomRenderItem14setItemPointerEP13QCustom3DItem',
        self._addressOf(item),
    )

  @overload(bool)
  def setValid(self, valid: bool) -> None:
    """
    Calls Qt's 'void CustomRenderItem::setValid(bool valid)'.

    Qt's own words: https://doc.qt.io/qt-6/customrenderitem.html#setValid

    Parameters
    ----------

    valid : bool
      Passed on as it is.
    """
    #  void CustomRenderItem::setValid(bool valid)
    self.uglySide.call('ritual_ZN16CustomRenderItem8setValidEb', valid)

  @overload(int)
  def setIndex(self, index: int) -> None:
    """
    Calls Qt's 'void CustomRenderItem::setIndex(int index)'.

    Qt's own words: https://doc.qt.io/qt-6/customrenderitem.html#setIndex

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void CustomRenderItem::setIndex(int index)
    self.uglySide.call('ritual_ZN16CustomRenderItem8setIndexEi', index)

  @overload(bool)
  def setShadowCasting(self, shadowCasting: bool) -> None:
    """
    Calls Qt's 'void CustomRenderItem::setShadowCasting(bool shadowCasting)'.

    Qt's own words:
    https://doc.qt.io/qt-6/customrenderitem.html#setShadowCasting

    Parameters
    ----------

    shadowCasting : bool
      Passed on as it is.
    """
    #  void CustomRenderItem::setShadowCasting(bool shadowCasting)
    self.uglySide.call(
        'ritual_ZN16CustomRenderItem16setShadowCastingEb', shadowCasting,
    )

  @overload(bool)
  def setFacingCamera(self, facing: bool) -> None:
    """
    Calls Qt's 'void CustomRenderItem::setFacingCamera(bool facing)'.

    Qt's own words:
    https://doc.qt.io/qt-6/customrenderitem.html#setFacingCamera

    Parameters
    ----------

    facing : bool
      Passed on as it is.
    """
    #  void CustomRenderItem::setFacingCamera(bool facing)
    self.uglySide.call(
        'ritual_ZN16CustomRenderItem15setFacingCameraEb', facing,
    )

  @overload(Abstract3DRenderer)
  @overload(NoneType)
  def setRenderer(self, renderer: Optional[Abstract3DRenderer]) -> None:
    """
    Calls Qt's 'void CustomRenderItem::setRenderer(Abstract3DRenderer
    *renderer)'.

    Qt's own words: https://doc.qt.io/qt-6/customrenderitem.html#setRenderer

    Parameters
    ----------

    renderer : Optional[Abstract3DRenderer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void CustomRenderItem::setRenderer(Abstract3DRenderer *renderer)
    self.uglySide.call(
        'ritual_ZN16CustomRenderItem11setRendererEP18Abstract3DRenderer',
        self._addressOf(renderer),
    )

  @overload(bool)
  def setLabelItem(self, isLabel: bool) -> None:
    """
    Calls Qt's 'void CustomRenderItem::setLabelItem(bool isLabel)'.

    Qt's own words: https://doc.qt.io/qt-6/customrenderitem.html#setLabelItem

    Parameters
    ----------

    isLabel : bool
      Passed on as it is.
    """
    #  void CustomRenderItem::setLabelItem(bool isLabel)
    self.uglySide.call(
        'ritual_ZN16CustomRenderItem12setLabelItemEb', isLabel,
    )

  @overload(int)
  def setTextureWidth(self, width: int) -> None:
    """
    Calls Qt's 'void CustomRenderItem::setTextureWidth(int width)'.

    Qt's own words:
    https://doc.qt.io/qt-6/customrenderitem.html#setTextureWidth

    Parameters
    ----------

    width : int
      Passed on as it is.
    """
    #  void CustomRenderItem::setTextureWidth(int width)
    self.uglySide.call(
        'ritual_ZN16CustomRenderItem15setTextureWidthEi', width,
    )

  @overload(int)
  def setTextureHeight(self, height: int) -> None:
    """
    Calls Qt's 'void CustomRenderItem::setTextureHeight(int height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/customrenderitem.html#setTextureHeight

    Parameters
    ----------

    height : int
      Passed on as it is.
    """
    #  void CustomRenderItem::setTextureHeight(int height)
    self.uglySide.call(
        'ritual_ZN16CustomRenderItem16setTextureHeightEi', height,
    )

  @overload(int)
  def setTextureDepth(self, depth: int) -> None:
    """
    Calls Qt's 'void CustomRenderItem::setTextureDepth(int depth)'.

    Qt's own words:
    https://doc.qt.io/qt-6/customrenderitem.html#setTextureDepth

    Parameters
    ----------

    depth : int
      Passed on as it is.
    """
    #  void CustomRenderItem::setTextureDepth(int depth)
    self.uglySide.call(
        'ritual_ZN16CustomRenderItem15setTextureDepthEi', depth,
    )

  @overload(QList[QVector4D])
  def setColorTable(self, colors: QList[QVector4D]) -> None:
    """
    Calls Qt's 'void CustomRenderItem::setColorTable(const QList<QVector4D>
    &colors)'.

    Qt's own words:
    https://doc.qt.io/qt-6/customrenderitem.html#setColorTable

    Parameters
    ----------

    colors : QList[QVector4D]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void CustomRenderItem::setColorTable(const QList<QVector4D> &colors)
    self.uglySide.call(
        'ritual_ZN16CustomRenderItem13setColorTableERK5QListI9QVector4DE',
        self._valueOf(colors),
    )

  @overload(bool)
  def setVolume(self, volume: bool) -> None:
    """
    Calls Qt's 'void CustomRenderItem::setVolume(bool volume)'.

    Qt's own words: https://doc.qt.io/qt-6/customrenderitem.html#setVolume

    Parameters
    ----------

    volume : bool
      Passed on as it is.
    """
    #  void CustomRenderItem::setVolume(bool volume)
    self.uglySide.call('ritual_ZN16CustomRenderItem9setVolumeEb', volume)

  @overload(QImage.Format)
  def setTextureFormat(self, format: QImage.Format) -> None:
    """
    Calls Qt's 'void CustomRenderItem::setTextureFormat(QImage::Format
    format)'.

    Qt's own words:
    https://doc.qt.io/qt-6/customrenderitem.html#setTextureFormat

    Parameters
    ----------

    format : QImage.Format
      Passed on as its number.
    """
    #  void CustomRenderItem::setTextureFormat(QImage::Format format)
    self.uglySide.call(
        'ritual_ZN16CustomRenderItem16setTextureFormatEN6QImage6FormatE',
        format.value,
    )

  @overload(int)
  def setSliceIndexX(self, index: int) -> None:
    """
    Calls Qt's 'void CustomRenderItem::setSliceIndexX(int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/customrenderitem.html#setSliceIndexX

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void CustomRenderItem::setSliceIndexX(int index)
    self.uglySide.call(
        'ritual_ZN16CustomRenderItem14setSliceIndexXEi', index,
    )

  @overload(int)
  def setSliceIndexY(self, index: int) -> None:
    """
    Calls Qt's 'void CustomRenderItem::setSliceIndexY(int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/customrenderitem.html#setSliceIndexY

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void CustomRenderItem::setSliceIndexY(int index)
    self.uglySide.call(
        'ritual_ZN16CustomRenderItem14setSliceIndexYEi', index,
    )

  @overload(int)
  def setSliceIndexZ(self, index: int) -> None:
    """
    Calls Qt's 'void CustomRenderItem::setSliceIndexZ(int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/customrenderitem.html#setSliceIndexZ

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void CustomRenderItem::setSliceIndexZ(int index)
    self.uglySide.call(
        'ritual_ZN16CustomRenderItem14setSliceIndexZEi', index,
    )

  @overload(float)
  def setAlphaMultiplier(self, mult: float) -> None:
    """
    Calls Qt's 'void CustomRenderItem::setAlphaMultiplier(float mult)'.

    Qt's own words:
    https://doc.qt.io/qt-6/customrenderitem.html#setAlphaMultiplier

    Parameters
    ----------

    mult : float
      Passed on as it is.
    """
    #  void CustomRenderItem::setAlphaMultiplier(float mult)
    self.uglySide.call(
        'ritual_ZN16CustomRenderItem18setAlphaMultiplierEf', mult,
    )

  @overload(bool)
  def setPreserveOpacity(self, enable: bool) -> None:
    """
    Calls Qt's 'void CustomRenderItem::setPreserveOpacity(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/customrenderitem.html#setPreserveOpacity

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void CustomRenderItem::setPreserveOpacity(bool enable)
    self.uglySide.call(
        'ritual_ZN16CustomRenderItem18setPreserveOpacityEb', enable,
    )

  @overload(bool)
  def setUseHighDefShader(self, enable: bool) -> None:
    """
    Calls Qt's 'void CustomRenderItem::setUseHighDefShader(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/customrenderitem.html#setUseHighDefShader

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void CustomRenderItem::setUseHighDefShader(bool enable)
    self.uglySide.call(
        'ritual_ZN16CustomRenderItem19setUseHighDefShaderEb', enable,
    )

  @overload(QVector3D)
  def setMinBounds(self, bounds: QVector3D) -> None:
    """
    Calls Qt's 'void CustomRenderItem::setMinBounds(const QVector3D
    &bounds)'.

    Qt's own words: https://doc.qt.io/qt-6/customrenderitem.html#setMinBounds

    Parameters
    ----------

    bounds : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void CustomRenderItem::setMinBounds(const QVector3D &bounds)
    self.uglySide.call(
        'ritual_ZN16CustomRenderItem12setMinBoundsERK9QVector3D',
        self._valueOf(bounds),
    )

  @overload(QVector3D)
  def setMaxBounds(self, bounds: QVector3D) -> None:
    """
    Calls Qt's 'void CustomRenderItem::setMaxBounds(const QVector3D
    &bounds)'.

    Qt's own words: https://doc.qt.io/qt-6/customrenderitem.html#setMaxBounds

    Parameters
    ----------

    bounds : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void CustomRenderItem::setMaxBounds(const QVector3D &bounds)
    self.uglySide.call(
        'ritual_ZN16CustomRenderItem12setMaxBoundsERK9QVector3D',
        self._valueOf(bounds),
    )

  @overload(bool)
  def setDrawSlices(self, enable: bool) -> None:
    """
    Calls Qt's 'void CustomRenderItem::setDrawSlices(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/customrenderitem.html#setDrawSlices

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void CustomRenderItem::setDrawSlices(bool enable)
    self.uglySide.call(
        'ritual_ZN16CustomRenderItem13setDrawSlicesEb', enable,
    )

  @overload(bool)
  def setDrawSliceFrames(self, enable: bool) -> None:
    """
    Calls Qt's 'void CustomRenderItem::setDrawSliceFrames(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/customrenderitem.html#setDrawSliceFrames

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void CustomRenderItem::setDrawSliceFrames(bool enable)
    self.uglySide.call(
        'ritual_ZN16CustomRenderItem18setDrawSliceFramesEb', enable,
    )

  @overload(QColor)
  def setSliceFrameColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void CustomRenderItem::setSliceFrameColor(const QColor
    &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/customrenderitem.html#setSliceFrameColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void CustomRenderItem::setSliceFrameColor(const QColor &color)
    self.uglySide.call(
        'ritual_ZN16CustomRenderItem18setSliceFrameColorERK6QColor',
        self._valueOf(color),
    )

  @overload(QVector3D)
  def setSliceFrameWidths(self, widths: QVector3D) -> None:
    """
    Calls Qt's 'void CustomRenderItem::setSliceFrameWidths(const QVector3D
    &widths)'.

    Qt's own words:
    https://doc.qt.io/qt-6/customrenderitem.html#setSliceFrameWidths

    Parameters
    ----------

    widths : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void CustomRenderItem::setSliceFrameWidths(const QVector3D &widths)
    self.uglySide.call(
        'ritual_ZN16CustomRenderItem19setSliceFrameWidthsERK9QVector3D',
        self._valueOf(widths),
    )

  @overload(QVector3D)
  def setSliceFrameGaps(self, gaps: QVector3D) -> None:
    """
    Calls Qt's 'void CustomRenderItem::setSliceFrameGaps(const QVector3D
    &gaps)'.

    Qt's own words:
    https://doc.qt.io/qt-6/customrenderitem.html#setSliceFrameGaps

    Parameters
    ----------

    gaps : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void CustomRenderItem::setSliceFrameGaps(const QVector3D &gaps)
    self.uglySide.call(
        'ritual_ZN16CustomRenderItem17setSliceFrameGapsERK9QVector3D',
        self._valueOf(gaps),
    )

  @overload(QVector3D)
  def setSliceFrameThicknesses(self, thicknesses: QVector3D) -> None:
    """
    Calls Qt's 'void CustomRenderItem::setSliceFrameThicknesses(const
    QVector3D &thicknesses)'.

    Qt's own words:
    https://doc.qt.io/qt-6/customrenderitem.html#setSliceFrameThicknesses

    Parameters
    ----------

    thicknesses : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void CustomRenderItem::setSliceFrameThicknesses(const QVector3D
    #      &thicknesses)
    self.uglySide.call(
        'ritual_ZN16CustomRenderItem24setSliceFrameThicknessesERK9QVector3D',
        self._valueOf(thicknesses),
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'CustomRenderItem::CustomRenderItem()': leans on
    'ObjectHelper::releaseObjectHelper(Abstract3DRenderer const*,
    ObjectHelper*&)', which Qt's source does not mark for use from outside Qt
    and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'CustomRenderItem.__init__' has no cute function yet. Qt's "
        "'CustomRenderItem::CustomRenderItem()': leans on "
        "'ObjectHelper::releaseObjectHelper(Abstract3DRenderer const*, "
        "ObjectHelper*&)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

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
  def setMesh(*__, **_) -> Never:
    """
    Qt's 'bool CustomRenderItem::setMesh(const QString &meshFile)': leans on
    'ObjectHelper::getObjectHelper(Abstract3DRenderer const*, QString
    const&)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'CustomRenderItem.setMesh' has no cute function yet. Qt's 'bool "
        "CustomRenderItem::setMesh(const QString &meshFile)': leans on "
        "'ObjectHelper::getObjectHelper(Abstract3DRenderer const*, QString "
        "const&)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")
