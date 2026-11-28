"""
QQuickMultiEffectPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickEffects/6.12.0/QtQuickEffects/private/qquickmultieffect_p_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuickMultiEffectPrivate to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtQuick import QQuickItemPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QRectF
  from ..QtGui import QColor
  from ..QtQuick import QQuickItem
  from . import QQuickMultiEffect
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QQuickItem = WAIT['QQuickItem']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickMultiEffectPrivate(QQuickItemPrivate):
  """
  The cute side of Qt's QQuickMultiEffectPrivate: a plain Python object
  standing in front of one C++ QQuickMultiEffectPrivate.

  It is built on the cute 'QQuickItemPrivate', as Qt's
  QQuickMultiEffectPrivate is built on Qt's QQuickItemPrivate, and has
  everything that class has. Qt's QQuickMultiEffectPrivate is built on Qt's
  QSafeQuickItemChangeListener<QQuickMultiEffectPrivate> as well, which is
  not reflected.

  What exists
  -----------

  Every function of Qt's QQuickMultiEffectPrivate that has a ritual and that
  Python can call so far, 60 names in all: 'q_func', 'source',
  'autoPaddingEnabled', 'paddingRect', 'brightness', 'setBrightness',
  'contrast', 'setContrast', 'saturation', 'setSaturation', 'colorization',
  'setColorization', 'colorizationColor', 'setColorizationColor',
  'blurEnabled', 'blur', 'setBlur', 'blurMax', 'blurMultiplier',
  'shadowEnabled', 'shadowOpacity', 'setShadowOpacity', 'shadowBlur',
  'setShadowBlur', 'shadowHorizontalOffset', 'setShadowHorizontalOffset',
  'shadowVerticalOffset', 'setShadowVerticalOffset', 'shadowColor',
  'setShadowColor', 'shadowScale', 'setShadowScale', 'maskEnabled',
  'maskSource', 'setMaskSource', 'maskThresholdMin', 'setMaskThresholdMin',
  'maskSpreadAtMin', 'setMaskSpreadAtMin', 'maskThresholdMax',
  'setMaskThresholdMax', 'maskSpreadAtMax', 'setMaskSpreadAtMax',
  'maskInverted', 'setMaskInverted', 'itemRect', 'fragmentShader',
  'vertexShader', 'hasProxySource', 'updateMaskThresholdSpread',
  'updateCenterOffset', 'updateShadowOffset', 'updateColorizationColor',
  'updateShadowColor', 'calculateLod', 'blurWeight', 'updateBlurWeights',
  'updateShadowBlurWeights', 'updateBlurItemsAmount',
  'updateProxyActiveCheck'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuickMultiEffect *QQuickMultiEffectPrivate::q_func() const':
    takes in Python what 'QQuickMultiEffect
    *QQuickMultiEffectPrivate::q_func()' takes.
  - Qt's 'QQuickMultiEffectPrivate::~QQuickMultiEffectPrivate()': the
    destructor: Python never removes a C++ QQuickMultiEffectPrivate.
  - Qt's 'void QQuickMultiEffectPrivate::getBlurWeights(float blurLod,
    QVector4D &blurWeight1, QVector2D &blurWeight2)': takes a type Python has
    no way to hand over yet.

  What has no ritual
  ------------------

  18 of the 81 functions Qt declares: 14 leans on 'QGfxSourceProxyME; 2 Qt's
  library has no name for it, and its code in Qt's source does not compile
  apart from its file; 2 leans on 'QQuickMultiEffectPrivate.

  What to expect
  --------------

  - The C++ QQuickMultiEffectPrivate is created at the first use, not by
    'QQuickMultiEffectPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickMultiEffectPrivate.
  - Each name of Qt's QQuickMultiEffectPrivate that has no cute function yet,
    '__init__', 'getBlurWeights', 'handleGeometryChange', 'handleItemChange',
    'initialize', 'itemDestroyed', 'proxyOutputChanged',
    'setAutoPaddingEnabled', 'setBlurEnabled', 'setBlurMax',
    'setBlurMultiplier', 'setMaskEnabled', 'setPaddingRect',
    'setShadowEnabled', 'setSource', 'updateBlurItemSizes',
    'updateBlurLevel', 'updateEffectShaders', 'updateSourcePadding', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickMultiEffectPrivate'

  #  A C++ QQuickMultiEffectPrivate Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickMultiEffectPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def source(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickMultiEffectPrivate::source() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffectprivate.html#source

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickMultiEffectPrivate::source() const
    address = self.uglySide.call(
        'ritual_ZNK24QQuickMultiEffectPrivate6sourceEv',
    )
    from ..QtQuick import QQuickItem
    return QQuickItem._cuteAt(address)

  def autoPaddingEnabled(self) -> bool:
    """
    Calls Qt's 'bool QQuickMultiEffectPrivate::autoPaddingEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffectprivate.html#autoPaddingEnabled
    """
    #  bool QQuickMultiEffectPrivate::autoPaddingEnabled() const
    return self.uglySide.call(
        'ritual_ZNK24QQuickMultiEffectPrivate18autoPaddingEnabledEv',
    )

  def paddingRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QQuickMultiEffectPrivate::paddingRect() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffectprivate.html#paddingRect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QQuickMultiEffectPrivate::paddingRect() const
    address = self.uglySide.call(
        'ritual_ZNK24QQuickMultiEffectPrivate11paddingRectEv',
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def brightness(self) -> float:
    """
    Calls Qt's 'qreal QQuickMultiEffectPrivate::brightness() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffectprivate.html#brightness
    """
    #  qreal QQuickMultiEffectPrivate::brightness() const
    return self.uglySide.call(
        'ritual_ZNK24QQuickMultiEffectPrivate10brightnessEv',
    )

  def contrast(self) -> float:
    """
    Calls Qt's 'qreal QQuickMultiEffectPrivate::contrast() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffectprivate.html#contrast
    """
    #  qreal QQuickMultiEffectPrivate::contrast() const
    return self.uglySide.call(
        'ritual_ZNK24QQuickMultiEffectPrivate8contrastEv',
    )

  def saturation(self) -> float:
    """
    Calls Qt's 'qreal QQuickMultiEffectPrivate::saturation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffectprivate.html#saturation
    """
    #  qreal QQuickMultiEffectPrivate::saturation() const
    return self.uglySide.call(
        'ritual_ZNK24QQuickMultiEffectPrivate10saturationEv',
    )

  def colorization(self) -> float:
    """
    Calls Qt's 'qreal QQuickMultiEffectPrivate::colorization() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffectprivate.html#colorization
    """
    #  qreal QQuickMultiEffectPrivate::colorization() const
    return self.uglySide.call(
        'ritual_ZNK24QQuickMultiEffectPrivate12colorizationEv',
    )

  def colorizationColor(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickMultiEffectPrivate::colorizationColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffectprivate.html#colorizationColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickMultiEffectPrivate::colorizationColor() const
    address = self.uglySide.call(
        'ritual_ZNK24QQuickMultiEffectPrivate17colorizationColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def blurEnabled(self) -> bool:
    """
    Calls Qt's 'bool QQuickMultiEffectPrivate::blurEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffectprivate.html#blurEnabled
    """
    #  bool QQuickMultiEffectPrivate::blurEnabled() const
    return self.uglySide.call(
        'ritual_ZNK24QQuickMultiEffectPrivate11blurEnabledEv',
    )

  def blur(self) -> float:
    """
    Calls Qt's 'qreal QQuickMultiEffectPrivate::blur() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmultieffectprivate.html#blur
    """
    #  qreal QQuickMultiEffectPrivate::blur() const
    return self.uglySide.call('ritual_ZNK24QQuickMultiEffectPrivate4blurEv')

  def blurMax(self) -> int:
    """
    Calls Qt's 'int QQuickMultiEffectPrivate::blurMax() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffectprivate.html#blurMax
    """
    #  int QQuickMultiEffectPrivate::blurMax() const
    return self.uglySide.call(
        'ritual_ZNK24QQuickMultiEffectPrivate7blurMaxEv',
    )

  def blurMultiplier(self) -> float:
    """
    Calls Qt's 'qreal QQuickMultiEffectPrivate::blurMultiplier() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffectprivate.html#blurMultiplier
    """
    #  qreal QQuickMultiEffectPrivate::blurMultiplier() const
    return self.uglySide.call(
        'ritual_ZNK24QQuickMultiEffectPrivate14blurMultiplierEv',
    )

  def shadowEnabled(self) -> bool:
    """
    Calls Qt's 'bool QQuickMultiEffectPrivate::shadowEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffectprivate.html#shadowEnabled
    """
    #  bool QQuickMultiEffectPrivate::shadowEnabled() const
    return self.uglySide.call(
        'ritual_ZNK24QQuickMultiEffectPrivate13shadowEnabledEv',
    )

  def shadowOpacity(self) -> float:
    """
    Calls Qt's 'qreal QQuickMultiEffectPrivate::shadowOpacity() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffectprivate.html#shadowOpacity
    """
    #  qreal QQuickMultiEffectPrivate::shadowOpacity() const
    return self.uglySide.call(
        'ritual_ZNK24QQuickMultiEffectPrivate13shadowOpacityEv',
    )

  def shadowBlur(self) -> float:
    """
    Calls Qt's 'qreal QQuickMultiEffectPrivate::shadowBlur() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffectprivate.html#shadowBlur
    """
    #  qreal QQuickMultiEffectPrivate::shadowBlur() const
    return self.uglySide.call(
        'ritual_ZNK24QQuickMultiEffectPrivate10shadowBlurEv',
    )

  def shadowHorizontalOffset(self) -> float:
    """
    Calls Qt's 'qreal QQuickMultiEffectPrivate::shadowHorizontalOffset()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffectprivate.html
    """
    #  qreal QQuickMultiEffectPrivate::shadowHorizontalOffset() const
    return self.uglySide.call(
        'ritual_ZNK24QQuickMultiEffectPrivate22shadowHorizontalOffsetEv',
    )

  def shadowVerticalOffset(self) -> float:
    """
    Calls Qt's 'qreal QQuickMultiEffectPrivate::shadowVerticalOffset()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffectprivate.html#shadowVerticalOffset
    """
    #  qreal QQuickMultiEffectPrivate::shadowVerticalOffset() const
    return self.uglySide.call(
        'ritual_ZNK24QQuickMultiEffectPrivate20shadowVerticalOffsetEv',
    )

  def shadowColor(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickMultiEffectPrivate::shadowColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffectprivate.html#shadowColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickMultiEffectPrivate::shadowColor() const
    address = self.uglySide.call(
        'ritual_ZNK24QQuickMultiEffectPrivate11shadowColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def shadowScale(self) -> float:
    """
    Calls Qt's 'qreal QQuickMultiEffectPrivate::shadowScale() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffectprivate.html#shadowScale
    """
    #  qreal QQuickMultiEffectPrivate::shadowScale() const
    return self.uglySide.call(
        'ritual_ZNK24QQuickMultiEffectPrivate11shadowScaleEv',
    )

  def maskEnabled(self) -> bool:
    """
    Calls Qt's 'bool QQuickMultiEffectPrivate::maskEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffectprivate.html#maskEnabled
    """
    #  bool QQuickMultiEffectPrivate::maskEnabled() const
    return self.uglySide.call(
        'ritual_ZNK24QQuickMultiEffectPrivate11maskEnabledEv',
    )

  def maskSource(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickMultiEffectPrivate::maskSource() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffectprivate.html#maskSource

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickMultiEffectPrivate::maskSource() const
    address = self.uglySide.call(
        'ritual_ZNK24QQuickMultiEffectPrivate10maskSourceEv',
    )
    from ..QtQuick import QQuickItem
    return QQuickItem._cuteAt(address)

  def maskThresholdMin(self) -> float:
    """
    Calls Qt's 'qreal QQuickMultiEffectPrivate::maskThresholdMin() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffectprivate.html#maskThresholdMin
    """
    #  qreal QQuickMultiEffectPrivate::maskThresholdMin() const
    return self.uglySide.call(
        'ritual_ZNK24QQuickMultiEffectPrivate16maskThresholdMinEv',
    )

  def maskSpreadAtMin(self) -> float:
    """
    Calls Qt's 'qreal QQuickMultiEffectPrivate::maskSpreadAtMin() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffectprivate.html#maskSpreadAtMin
    """
    #  qreal QQuickMultiEffectPrivate::maskSpreadAtMin() const
    return self.uglySide.call(
        'ritual_ZNK24QQuickMultiEffectPrivate15maskSpreadAtMinEv',
    )

  def maskThresholdMax(self) -> float:
    """
    Calls Qt's 'qreal QQuickMultiEffectPrivate::maskThresholdMax() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffectprivate.html#maskThresholdMax
    """
    #  qreal QQuickMultiEffectPrivate::maskThresholdMax() const
    return self.uglySide.call(
        'ritual_ZNK24QQuickMultiEffectPrivate16maskThresholdMaxEv',
    )

  def maskSpreadAtMax(self) -> float:
    """
    Calls Qt's 'qreal QQuickMultiEffectPrivate::maskSpreadAtMax() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffectprivate.html#maskSpreadAtMax
    """
    #  qreal QQuickMultiEffectPrivate::maskSpreadAtMax() const
    return self.uglySide.call(
        'ritual_ZNK24QQuickMultiEffectPrivate15maskSpreadAtMaxEv',
    )

  def maskInverted(self) -> bool:
    """
    Calls Qt's 'bool QQuickMultiEffectPrivate::maskInverted() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffectprivate.html#maskInverted
    """
    #  bool QQuickMultiEffectPrivate::maskInverted() const
    return self.uglySide.call(
        'ritual_ZNK24QQuickMultiEffectPrivate12maskInvertedEv',
    )

  def itemRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QQuickMultiEffectPrivate::itemRect() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffectprivate.html#itemRect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QQuickMultiEffectPrivate::itemRect() const
    address = self.uglySide.call(
        'ritual_ZNK24QQuickMultiEffectPrivate8itemRectEv',
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def fragmentShader(self) -> str:
    """
    Calls Qt's 'QString QQuickMultiEffectPrivate::fragmentShader() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffectprivate.html#fragmentShader

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickMultiEffectPrivate::fragmentShader() const
    return self.uglySide.call(
        'ritual_ZNK24QQuickMultiEffectPrivate14fragmentShaderEv',
    )

  def vertexShader(self) -> str:
    """
    Calls Qt's 'QString QQuickMultiEffectPrivate::vertexShader() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffectprivate.html#vertexShader

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickMultiEffectPrivate::vertexShader() const
    return self.uglySide.call(
        'ritual_ZNK24QQuickMultiEffectPrivate12vertexShaderEv',
    )

  def hasProxySource(self) -> bool:
    """
    Calls Qt's 'bool QQuickMultiEffectPrivate::hasProxySource() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffectprivate.html#hasProxySource
    """
    #  bool QQuickMultiEffectPrivate::hasProxySource() const
    return self.uglySide.call(
        'ritual_ZNK24QQuickMultiEffectPrivate14hasProxySourceEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setBrightness(self, brightness: float) -> None:
    """
    Calls Qt's 'void QQuickMultiEffectPrivate::setBrightness(qreal
    brightness)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffectprivate.html#setBrightness

    Parameters
    ----------

    brightness : float
      Passed on as it is.
    """
    #  void QQuickMultiEffectPrivate::setBrightness(qreal brightness)
    self.uglySide.call(
        'ritual_ZN24QQuickMultiEffectPrivate13setBrightnessEd', brightness,
    )

  @overload(float)
  def setContrast(self, contrast: float) -> None:
    """
    Calls Qt's 'void QQuickMultiEffectPrivate::setContrast(qreal contrast)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffectprivate.html#setContrast

    Parameters
    ----------

    contrast : float
      Passed on as it is.
    """
    #  void QQuickMultiEffectPrivate::setContrast(qreal contrast)
    self.uglySide.call(
        'ritual_ZN24QQuickMultiEffectPrivate11setContrastEd', contrast,
    )

  @overload(float)
  def setSaturation(self, saturation: float) -> None:
    """
    Calls Qt's 'void QQuickMultiEffectPrivate::setSaturation(qreal
    saturation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffectprivate.html#setSaturation

    Parameters
    ----------

    saturation : float
      Passed on as it is.
    """
    #  void QQuickMultiEffectPrivate::setSaturation(qreal saturation)
    self.uglySide.call(
        'ritual_ZN24QQuickMultiEffectPrivate13setSaturationEd', saturation,
    )

  @overload(float)
  def setColorization(self, colorization: float) -> None:
    """
    Calls Qt's 'void QQuickMultiEffectPrivate::setColorization(qreal
    colorization)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffectprivate.html#setColorization

    Parameters
    ----------

    colorization : float
      Passed on as it is.
    """
    #  void QQuickMultiEffectPrivate::setColorization(qreal colorization)
    self.uglySide.call(
        'ritual_ZN24QQuickMultiEffectPrivate15setColorizationEd',
        colorization,
    )

  @overload(QColor)
  def setColorizationColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QQuickMultiEffectPrivate::setColorizationColor(const
    QColor &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffectprivate.html#setColorizationColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickMultiEffectPrivate::setColorizationColor(const QColor
    #      &color)
    self.uglySide.call(
        'ritual_ZN24QQuickMultiEffectPrivate20setColorizationColorERK6QColo'
        'r',
        self._valueOf(color),
    )

  @overload(float)
  def setBlur(self, blur: float) -> None:
    """
    Calls Qt's 'void QQuickMultiEffectPrivate::setBlur(qreal blur)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffectprivate.html#setBlur

    Parameters
    ----------

    blur : float
      Passed on as it is.
    """
    #  void QQuickMultiEffectPrivate::setBlur(qreal blur)
    self.uglySide.call('ritual_ZN24QQuickMultiEffectPrivate7setBlurEd', blur)

  @overload(float)
  def setShadowOpacity(self, shadowOpacity: float) -> None:
    """
    Calls Qt's 'void QQuickMultiEffectPrivate::setShadowOpacity(qreal
    shadowOpacity)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffectprivate.html#setShadowOpacity

    Parameters
    ----------

    shadowOpacity : float
      Passed on as it is.
    """
    #  void QQuickMultiEffectPrivate::setShadowOpacity(qreal shadowOpacity)
    self.uglySide.call(
        'ritual_ZN24QQuickMultiEffectPrivate16setShadowOpacityEd',
        shadowOpacity,
    )

  @overload(float)
  def setShadowBlur(self, shadowBlur: float) -> None:
    """
    Calls Qt's 'void QQuickMultiEffectPrivate::setShadowBlur(qreal
    shadowBlur)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffectprivate.html#setShadowBlur

    Parameters
    ----------

    shadowBlur : float
      Passed on as it is.
    """
    #  void QQuickMultiEffectPrivate::setShadowBlur(qreal shadowBlur)
    self.uglySide.call(
        'ritual_ZN24QQuickMultiEffectPrivate13setShadowBlurEd', shadowBlur,
    )

  @overload(float)
  def setShadowHorizontalOffset(self, offset: float) -> None:
    """
    Calls Qt's 'void
    QQuickMultiEffectPrivate::setShadowHorizontalOffset(qreal offset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffectprivate.html

    Parameters
    ----------

    offset : float
      Passed on as it is.
    """
    #  void QQuickMultiEffectPrivate::setShadowHorizontalOffset(qreal offset)
    self.uglySide.call(
        'ritual_ZN24QQuickMultiEffectPrivate25setShadowHorizontalOffsetEd',
        offset,
    )

  @overload(float)
  def setShadowVerticalOffset(self, offset: float) -> None:
    """
    Calls Qt's 'void QQuickMultiEffectPrivate::setShadowVerticalOffset(qreal
    offset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffectprivate.html

    Parameters
    ----------

    offset : float
      Passed on as it is.
    """
    #  void QQuickMultiEffectPrivate::setShadowVerticalOffset(qreal offset)
    self.uglySide.call(
        'ritual_ZN24QQuickMultiEffectPrivate23setShadowVerticalOffsetEd',
        offset,
    )

  @overload(QColor)
  def setShadowColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QQuickMultiEffectPrivate::setShadowColor(const QColor
    &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffectprivate.html#setShadowColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickMultiEffectPrivate::setShadowColor(const QColor &color)
    self.uglySide.call(
        'ritual_ZN24QQuickMultiEffectPrivate14setShadowColorERK6QColor',
        self._valueOf(color),
    )

  @overload(float)
  def setShadowScale(self, shadowScale: float) -> None:
    """
    Calls Qt's 'void QQuickMultiEffectPrivate::setShadowScale(qreal
    shadowScale)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffectprivate.html#setShadowScale

    Parameters
    ----------

    shadowScale : float
      Passed on as it is.
    """
    #  void QQuickMultiEffectPrivate::setShadowScale(qreal shadowScale)
    self.uglySide.call(
        'ritual_ZN24QQuickMultiEffectPrivate14setShadowScaleEd', shadowScale,
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def setMaskSource(self, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickMultiEffectPrivate::setMaskSource(QQuickItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffectprivate.html#setMaskSource

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickMultiEffectPrivate::setMaskSource(QQuickItem *item)
    self.uglySide.call(
        'ritual_ZN24QQuickMultiEffectPrivate13setMaskSourceEP10QQuickItem',
        self._addressOf(item),
    )

  @overload(float)
  def setMaskThresholdMin(self, threshold: float) -> None:
    """
    Calls Qt's 'void QQuickMultiEffectPrivate::setMaskThresholdMin(qreal
    threshold)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffectprivate.html#setMaskThresholdMin

    Parameters
    ----------

    threshold : float
      Passed on as it is.
    """
    #  void QQuickMultiEffectPrivate::setMaskThresholdMin(qreal threshold)
    self.uglySide.call(
        'ritual_ZN24QQuickMultiEffectPrivate19setMaskThresholdMinEd',
        threshold,
    )

  @overload(float)
  def setMaskSpreadAtMin(self, spread: float) -> None:
    """
    Calls Qt's 'void QQuickMultiEffectPrivate::setMaskSpreadAtMin(qreal
    spread)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffectprivate.html#setMaskSpreadAtMin

    Parameters
    ----------

    spread : float
      Passed on as it is.
    """
    #  void QQuickMultiEffectPrivate::setMaskSpreadAtMin(qreal spread)
    self.uglySide.call(
        'ritual_ZN24QQuickMultiEffectPrivate18setMaskSpreadAtMinEd', spread,
    )

  @overload(float)
  def setMaskThresholdMax(self, threshold: float) -> None:
    """
    Calls Qt's 'void QQuickMultiEffectPrivate::setMaskThresholdMax(qreal
    threshold)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffectprivate.html#setMaskThresholdMax

    Parameters
    ----------

    threshold : float
      Passed on as it is.
    """
    #  void QQuickMultiEffectPrivate::setMaskThresholdMax(qreal threshold)
    self.uglySide.call(
        'ritual_ZN24QQuickMultiEffectPrivate19setMaskThresholdMaxEd',
        threshold,
    )

  @overload(float)
  def setMaskSpreadAtMax(self, spread: float) -> None:
    """
    Calls Qt's 'void QQuickMultiEffectPrivate::setMaskSpreadAtMax(qreal
    spread)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffectprivate.html#setMaskSpreadAtMax

    Parameters
    ----------

    spread : float
      Passed on as it is.
    """
    #  void QQuickMultiEffectPrivate::setMaskSpreadAtMax(qreal spread)
    self.uglySide.call(
        'ritual_ZN24QQuickMultiEffectPrivate18setMaskSpreadAtMaxEd', spread,
    )

  @overload(bool)
  def setMaskInverted(self, inverted: bool) -> None:
    """
    Calls Qt's 'void QQuickMultiEffectPrivate::setMaskInverted(bool
    inverted)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffectprivate.html#setMaskInverted

    Parameters
    ----------

    inverted : bool
      Passed on as it is.
    """
    #  void QQuickMultiEffectPrivate::setMaskInverted(bool inverted)
    self.uglySide.call(
        'ritual_ZN24QQuickMultiEffectPrivate15setMaskInvertedEb', inverted,
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
    Qt's 'QQuickMultiEffectPrivate::QQuickMultiEffectPrivate()': leans on
    'QGfxSourceProxyME::inputChanged()', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickMultiEffectPrivate.__init__' has no cute function yet. Qt's "
        "'QQuickMultiEffectPrivate::QQuickMultiEffectPrivate()': leans on "
        "'QGfxSourceProxyME::inputChanged()', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

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

  def q_func(self) -> Optional[QQuickMultiEffect]:
    """
    Calls Qt's 'QQuickMultiEffect *QQuickMultiEffectPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffectprivate.html#q_func

    Returns
    -------

    Optional[QQuickMultiEffect]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickMultiEffect *QQuickMultiEffectPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN24QQuickMultiEffectPrivate6q_funcEv',
    )
    from . import QQuickMultiEffect
    return QQuickMultiEffect._cuteAt(address)

  def updateMaskThresholdSpread(self) -> None:
    """
    Calls Qt's 'void QQuickMultiEffectPrivate::updateMaskThresholdSpread()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffectprivate.html
    """
    #  void QQuickMultiEffectPrivate::updateMaskThresholdSpread()
    self.uglySide.call(
        'ritual_ZN24QQuickMultiEffectPrivate25updateMaskThresholdSpreadEv',
    )

  def updateCenterOffset(self) -> None:
    """
    Calls Qt's 'void QQuickMultiEffectPrivate::updateCenterOffset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffectprivate.html#updateCenterOffset
    """
    #  void QQuickMultiEffectPrivate::updateCenterOffset()
    self.uglySide.call(
        'ritual_ZN24QQuickMultiEffectPrivate18updateCenterOffsetEv',
    )

  def updateShadowOffset(self) -> None:
    """
    Calls Qt's 'void QQuickMultiEffectPrivate::updateShadowOffset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffectprivate.html#updateShadowOffset
    """
    #  void QQuickMultiEffectPrivate::updateShadowOffset()
    self.uglySide.call(
        'ritual_ZN24QQuickMultiEffectPrivate18updateShadowOffsetEv',
    )

  def updateColorizationColor(self) -> None:
    """
    Calls Qt's 'void QQuickMultiEffectPrivate::updateColorizationColor()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffectprivate.html
    """
    #  void QQuickMultiEffectPrivate::updateColorizationColor()
    self.uglySide.call(
        'ritual_ZN24QQuickMultiEffectPrivate23updateColorizationColorEv',
    )

  def updateShadowColor(self) -> None:
    """
    Calls Qt's 'void QQuickMultiEffectPrivate::updateShadowColor()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffectprivate.html#updateShadowColor
    """
    #  void QQuickMultiEffectPrivate::updateShadowColor()
    self.uglySide.call(
        'ritual_ZN24QQuickMultiEffectPrivate17updateShadowColorEv',
    )

  @overload(float)
  def calculateLod(self, blurAmount: float) -> float:
    """
    Calls Qt's 'float QQuickMultiEffectPrivate::calculateLod(float
    blurAmount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffectprivate.html#calculateLod

    Parameters
    ----------

    blurAmount : float
      Passed on as it is.
    """
    #  float QQuickMultiEffectPrivate::calculateLod(float blurAmount)
    return self.uglySide.call(
        'ritual_ZN24QQuickMultiEffectPrivate12calculateLodEf', blurAmount,
    )

  @overload(float)
  def blurWeight(self, v: float) -> float:
    """
    Calls Qt's 'float QQuickMultiEffectPrivate::blurWeight(float v)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffectprivate.html#blurWeight

    Parameters
    ----------

    v : float
      Passed on as it is.
    """
    #  float QQuickMultiEffectPrivate::blurWeight(float v)
    return self.uglySide.call(
        'ritual_ZN24QQuickMultiEffectPrivate10blurWeightEf', v,
    )

  def updateBlurWeights(self) -> None:
    """
    Calls Qt's 'void QQuickMultiEffectPrivate::updateBlurWeights()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffectprivate.html#updateBlurWeights
    """
    #  void QQuickMultiEffectPrivate::updateBlurWeights()
    self.uglySide.call(
        'ritual_ZN24QQuickMultiEffectPrivate17updateBlurWeightsEv',
    )

  def updateShadowBlurWeights(self) -> None:
    """
    Calls Qt's 'void QQuickMultiEffectPrivate::updateShadowBlurWeights()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffectprivate.html
    """
    #  void QQuickMultiEffectPrivate::updateShadowBlurWeights()
    self.uglySide.call(
        'ritual_ZN24QQuickMultiEffectPrivate23updateShadowBlurWeightsEv',
    )

  @overload(int)
  def updateBlurItemsAmount(self, blurLevel: int) -> None:
    """
    Calls Qt's 'void QQuickMultiEffectPrivate::updateBlurItemsAmount(int
    blurLevel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffectprivate.html

    Parameters
    ----------

    blurLevel : int
      Passed on as it is.
    """
    #  void QQuickMultiEffectPrivate::updateBlurItemsAmount(int blurLevel)
    self.uglySide.call(
        'ritual_ZN24QQuickMultiEffectPrivate21updateBlurItemsAmountEi',
        blurLevel,
    )

  def updateProxyActiveCheck(self) -> None:
    """
    Calls Qt's 'void QQuickMultiEffectPrivate::updateProxyActiveCheck()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffectprivate.html
    """
    #  void QQuickMultiEffectPrivate::updateProxyActiveCheck()
    self.uglySide.call(
        'ritual_ZN24QQuickMultiEffectPrivate22updateProxyActiveCheckEv',
    )

  @staticmethod
  def getBlurWeights(*__, **_) -> Never:
    """
    Qt's 'void QQuickMultiEffectPrivate::getBlurWeights(float blurLod,
    QVector4D &blurWeight1, QVector2D &blurWeight2)': takes a type Python has
    no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuickMultiEffectPrivate.getBlurWeights' has no cute function "
        "yet. Qt's 'void QQuickMultiEffectPrivate::getBlurWeights(float "
        "blurLod, QVector4D &blurWeight1, QVector2D &blurWeight2)': takes a "
        "type Python has no way to hand over yet.")

  @staticmethod
  def handleGeometryChange(*__, **_) -> Never:
    """
    Qt's 'void QQuickMultiEffectPrivate::handleGeometryChange(const QRectF
    &newGeometry, const QRectF &oldGeometry)': leans on
    'QGfxSourceProxyME::activeChanged()', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickMultiEffectPrivate.handleGeometryChange' has no cute "
        "function yet. Qt's 'void "
        "QQuickMultiEffectPrivate::handleGeometryChange(const QRectF "
        "&newGeometry, const QRectF &oldGeometry)': leans on "
        "'QGfxSourceProxyME::activeChanged()', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def handleItemChange(*__, **_) -> Never:
    """
    Qt's 'void
    QQuickMultiEffectPrivate::handleItemChange(QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData &value)': leans on
    'QGfxSourceProxyME::activeChanged()', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickMultiEffectPrivate.handleItemChange' has no cute function "
        "yet. Qt's 'void "
        "QQuickMultiEffectPrivate::handleItemChange(QQuickItem::ItemChange "
        "change, const QQuickItem::ItemChangeData &value)': leans on "
        "'QGfxSourceProxyME::activeChanged()', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def initialize(*__, **_) -> Never:
    """
    Qt's 'void QQuickMultiEffectPrivate::initialize()': leans on
    'QGfxSourceProxyME::activeChanged()', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickMultiEffectPrivate.initialize' has no cute function yet. "
        "Qt's 'void QQuickMultiEffectPrivate::initialize()': leans on "
        "'QGfxSourceProxyME::activeChanged()', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def itemDestroyed(*__, **_) -> Never:
    """
    Qt's 'void QQuickMultiEffectPrivate::itemDestroyed(QQuickItem *item)':
    leans on 'QGfxSourceProxyME::inputChanged()', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickMultiEffectPrivate.itemDestroyed' has no cute function yet. "
        "Qt's 'void QQuickMultiEffectPrivate::itemDestroyed(QQuickItem "
        "*item)': leans on 'QGfxSourceProxyME::inputChanged()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def proxyOutputChanged(*__, **_) -> Never:
    """
    Qt's 'void QQuickMultiEffectPrivate::proxyOutputChanged()': leans on
    'QGfxSourceProxyME::sourceRectChanged()', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickMultiEffectPrivate.proxyOutputChanged' has no cute function "
        "yet. Qt's 'void QQuickMultiEffectPrivate::proxyOutputChanged()': "
        "leans on 'QGfxSourceProxyME::sourceRectChanged()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def setAutoPaddingEnabled(*__, **_) -> Never:
    """
    Qt's 'void QQuickMultiEffectPrivate::setAutoPaddingEnabled(bool
    enabled)': leans on 'QGfxSourceProxyME::sourceRectChanged()', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QQuickMultiEffectPrivate.setAutoPaddingEnabled' has no cute "
        "function yet. Qt's 'void "
        "QQuickMultiEffectPrivate::setAutoPaddingEnabled(bool enabled)': "
        "leans on 'QGfxSourceProxyME::sourceRectChanged()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def setBlurEnabled(*__, **_) -> Never:
    """
    Qt's 'void QQuickMultiEffectPrivate::setBlurEnabled(bool enabled)': leans
    on 'QGfxSourceProxyME::sourceRectChanged()', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickMultiEffectPrivate.setBlurEnabled' has no cute function "
        "yet. Qt's 'void QQuickMultiEffectPrivate::setBlurEnabled(bool "
        "enabled)': leans on 'QGfxSourceProxyME::sourceRectChanged()', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def setBlurMax(*__, **_) -> Never:
    """
    Qt's 'void QQuickMultiEffectPrivate::setBlurMax(int blurMax)': leans on
    'QGfxSourceProxyME::sourceRectChanged()', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickMultiEffectPrivate.setBlurMax' has no cute function yet. "
        "Qt's 'void QQuickMultiEffectPrivate::setBlurMax(int blurMax)': "
        "leans on 'QGfxSourceProxyME::sourceRectChanged()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def setBlurMultiplier(*__, **_) -> Never:
    """
    Qt's 'void QQuickMultiEffectPrivate::setBlurMultiplier(qreal
    blurMultiplier)': leans on 'QGfxSourceProxyME::sourceRectChanged()',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickMultiEffectPrivate.setBlurMultiplier' has no cute function "
        "yet. Qt's 'void QQuickMultiEffectPrivate::setBlurMultiplier(qreal "
        "blurMultiplier)': leans on "
        "'QGfxSourceProxyME::sourceRectChanged()', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def setMaskEnabled(*__, **_) -> Never:
    """
    Qt's 'void QQuickMultiEffectPrivate::setMaskEnabled(bool enabled)': leans
    on 'QQuickMultiEffectPrivate::updateEffectShaders()', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QQuickMultiEffectPrivate.setMaskEnabled' has no cute function "
        "yet. Qt's 'void QQuickMultiEffectPrivate::setMaskEnabled(bool "
        "enabled)': leans on "
        "'QQuickMultiEffectPrivate::updateEffectShaders()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def setPaddingRect(*__, **_) -> Never:
    """
    Qt's 'void QQuickMultiEffectPrivate::setPaddingRect(const QRectF &rect)':
    leans on 'QGfxSourceProxyME::sourceRectChanged()', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickMultiEffectPrivate.setPaddingRect' has no cute function "
        "yet. Qt's 'void QQuickMultiEffectPrivate::setPaddingRect(const "
        "QRectF &rect)': leans on 'QGfxSourceProxyME::sourceRectChanged()', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def setShadowEnabled(*__, **_) -> Never:
    """
    Qt's 'void QQuickMultiEffectPrivate::setShadowEnabled(bool enabled)':
    leans on 'QGfxSourceProxyME::sourceRectChanged()', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickMultiEffectPrivate.setShadowEnabled' has no cute function "
        "yet. Qt's 'void QQuickMultiEffectPrivate::setShadowEnabled(bool "
        "enabled)': leans on 'QGfxSourceProxyME::sourceRectChanged()', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def setSource(*__, **_) -> Never:
    """
    Qt's 'void QQuickMultiEffectPrivate::setSource(QQuickItem *item)': leans
    on 'QGfxSourceProxyME::inputChanged()', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickMultiEffectPrivate.setSource' has no cute function yet. "
        "Qt's 'void QQuickMultiEffectPrivate::setSource(QQuickItem *item)': "
        "leans on 'QGfxSourceProxyME::inputChanged()', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def updateBlurItemSizes(*__, **_) -> Never:
    """
    Qt's 'void QQuickMultiEffectPrivate::updateBlurItemSizes(bool
    forceUpdate)': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: use of undeclared identifier
    'lcQuickEffect'.
    """
    raise NotImplementedError(
        "'QQuickMultiEffectPrivate.updateBlurItemSizes' has no cute "
        "function yet. Qt's 'void "
        "QQuickMultiEffectPrivate::updateBlurItemSizes(bool forceUpdate)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'lcQuickEffect'.")

  @staticmethod
  def updateBlurLevel(*__, **_) -> Never:
    """
    Qt's 'void QQuickMultiEffectPrivate::updateBlurLevel(bool forceUpdate)':
    leans on 'QQuickMultiEffectPrivate::updateBlurItemSizes(bool)', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QQuickMultiEffectPrivate.updateBlurLevel' has no cute function "
        "yet. Qt's 'void QQuickMultiEffectPrivate::updateBlurLevel(bool "
        "forceUpdate)': leans on "
        "'QQuickMultiEffectPrivate::updateBlurItemSizes(bool)', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def updateEffectShaders(*__, **_) -> Never:
    """
    Qt's 'void QQuickMultiEffectPrivate::updateEffectShaders()': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: use of undeclared identifier 'lcQuickEffect'.
    """
    raise NotImplementedError(
        "'QQuickMultiEffectPrivate.updateEffectShaders' has no cute "
        "function yet. Qt's 'void "
        "QQuickMultiEffectPrivate::updateEffectShaders()': Qt's library has "
        "no name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier 'lcQuickEffect'.")

  @staticmethod
  def updateSourcePadding(*__, **_) -> Never:
    """
    Qt's 'void QQuickMultiEffectPrivate::updateSourcePadding()': leans on
    'QGfxSourceProxyME::sourceRectChanged()', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickMultiEffectPrivate.updateSourcePadding' has no cute "
        "function yet. Qt's 'void "
        "QQuickMultiEffectPrivate::updateSourcePadding()': leans on "
        "'QGfxSourceProxyME::sourceRectChanged()', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")
