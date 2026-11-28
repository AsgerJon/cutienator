"""
QQuickMultiEffect binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickEffects/6.12.0/QtQuickEffects/private/qquickmultieffect_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuickMultiEffect to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtQuick import QQuickItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QRectF
  from ..QtGui import QColor
  from . import QQuickMultiEffectPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QRectF = WAIT['QRectF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickMultiEffect(QQuickItem):
  """
  The cute side of Qt's QQuickMultiEffect: a plain Python object standing in
  front of one C++ QQuickMultiEffect.

  It is built on the cute 'QQuickItem', as Qt's QQuickMultiEffect is built on
  Qt's QQuickItem, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickMultiEffect that has a ritual and that Python
  can call so far, 94 names in all: 'metaObject', 'tr', 'source',
  'setSource', 'autoPaddingEnabled', 'setAutoPaddingEnabled', 'paddingRect',
  'setPaddingRect', 'brightness', 'setBrightness', 'contrast', 'setContrast',
  'saturation', 'setSaturation', 'colorization', 'setColorization',
  'colorizationColor', 'setColorizationColor', 'blurEnabled',
  'setBlurEnabled', 'blur', 'setBlur', 'blurMax', 'setBlurMax',
  'blurMultiplier', 'setBlurMultiplier', 'shadowEnabled', 'setShadowEnabled',
  'shadowOpacity', 'setShadowOpacity', 'shadowBlur', 'setShadowBlur',
  'shadowHorizontalOffset', 'setShadowHorizontalOffset',
  'shadowVerticalOffset', 'setShadowVerticalOffset', 'shadowColor',
  'setShadowColor', 'shadowScale', 'setShadowScale', 'maskEnabled',
  'setMaskEnabled', 'maskSource', 'setMaskSource', 'maskThresholdMin',
  'setMaskThresholdMin', 'maskSpreadAtMin', 'setMaskSpreadAtMin',
  'maskThresholdMax', 'setMaskThresholdMax', 'maskSpreadAtMax',
  'setMaskSpreadAtMax', 'maskInverted', 'setMaskInverted', 'itemRect',
  'fragmentShader', 'vertexShader', 'hasProxySource', 'shaderChanged',
  'itemSizeChanged', 'sourceChanged', 'autoPaddingEnabledChanged',
  'paddingRectChanged', 'brightnessChanged', 'contrastChanged',
  'saturationChanged', 'colorizationChanged', 'colorizationColorChanged',
  'blurEnabledChanged', 'blurChanged', 'blurMaxChanged',
  'blurMultiplierChanged', 'shadowEnabledChanged', 'shadowOpacityChanged',
  'shadowBlurChanged', 'shadowHorizontalOffsetChanged',
  'shadowVerticalOffsetChanged', 'shadowColorChanged', 'shadowScaleChanged',
  'maskEnabledChanged', 'maskSourceChanged', 'maskThresholdMinChanged',
  'maskSpreadAtMinChanged', 'maskThresholdMaxChanged',
  'maskSpreadAtMaxChanged', 'maskInvertedChanged', 'itemRectChanged',
  'fragmentShaderChanged', 'vertexShaderChanged', 'hasProxySourceChanged',
  'componentComplete', 'geometryChange', 'itemChange', 'd_func'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickMultiEffect::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickMultiEffect::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickMultiEffect::~QQuickMultiEffect()': the destructor: Python
    never removes a C++ QQuickMultiEffect.
  - Qt's 'const QQuickMultiEffectPrivate *QQuickMultiEffect::d_func() const':
    takes in Python what 'QQuickMultiEffectPrivate
    *QQuickMultiEffect::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 101 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickMultiEffect is created at the first use, not by
    'QQuickMultiEffect(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickMultiEffect.
  - Qt tells when it has removed the C++ QQuickMultiEffect. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString QQuickMultiEffect::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmultieffect.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickMultiEffect::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN17QQuickMultiEffect2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickMultiEffect'

  #  A C++ QQuickMultiEffect Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickMultiEffect'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickMultiEffect::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmultieffect.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickMultiEffect::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QQuickMultiEffect10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def source(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickMultiEffect::source() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmultieffect.html#source

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickMultiEffect::source() const
    address = self.uglySide.call('ritual_ZNK17QQuickMultiEffect6sourceEv')
    return QQuickItem._cuteAt(address)

  def autoPaddingEnabled(self) -> bool:
    """
    Calls Qt's 'bool QQuickMultiEffect::autoPaddingEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffect.html#autoPaddingEnabled
    """
    #  bool QQuickMultiEffect::autoPaddingEnabled() const
    return self.uglySide.call(
        'ritual_ZNK17QQuickMultiEffect18autoPaddingEnabledEv',
    )

  def paddingRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QQuickMultiEffect::paddingRect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmultieffect.html#paddingRect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QQuickMultiEffect::paddingRect() const
    address = self.uglySide.call(
        'ritual_ZNK17QQuickMultiEffect11paddingRectEv',
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def brightness(self) -> float:
    """
    Calls Qt's 'qreal QQuickMultiEffect::brightness() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmultieffect.html#brightness
    """
    #  qreal QQuickMultiEffect::brightness() const
    return self.uglySide.call('ritual_ZNK17QQuickMultiEffect10brightnessEv')

  def contrast(self) -> float:
    """
    Calls Qt's 'qreal QQuickMultiEffect::contrast() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmultieffect.html#contrast
    """
    #  qreal QQuickMultiEffect::contrast() const
    return self.uglySide.call('ritual_ZNK17QQuickMultiEffect8contrastEv')

  def saturation(self) -> float:
    """
    Calls Qt's 'qreal QQuickMultiEffect::saturation() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmultieffect.html#saturation
    """
    #  qreal QQuickMultiEffect::saturation() const
    return self.uglySide.call('ritual_ZNK17QQuickMultiEffect10saturationEv')

  def colorization(self) -> float:
    """
    Calls Qt's 'qreal QQuickMultiEffect::colorization() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffect.html#colorization
    """
    #  qreal QQuickMultiEffect::colorization() const
    return self.uglySide.call(
        'ritual_ZNK17QQuickMultiEffect12colorizationEv',
    )

  def colorizationColor(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickMultiEffect::colorizationColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffect.html#colorizationColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickMultiEffect::colorizationColor() const
    address = self.uglySide.call(
        'ritual_ZNK17QQuickMultiEffect17colorizationColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def blurEnabled(self) -> bool:
    """
    Calls Qt's 'bool QQuickMultiEffect::blurEnabled() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmultieffect.html#blurEnabled
    """
    #  bool QQuickMultiEffect::blurEnabled() const
    return self.uglySide.call('ritual_ZNK17QQuickMultiEffect11blurEnabledEv')

  def blur(self) -> float:
    """
    Calls Qt's 'qreal QQuickMultiEffect::blur() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmultieffect.html#blur
    """
    #  qreal QQuickMultiEffect::blur() const
    return self.uglySide.call('ritual_ZNK17QQuickMultiEffect4blurEv')

  def blurMax(self) -> int:
    """
    Calls Qt's 'int QQuickMultiEffect::blurMax() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmultieffect.html#blurMax
    """
    #  int QQuickMultiEffect::blurMax() const
    return self.uglySide.call('ritual_ZNK17QQuickMultiEffect7blurMaxEv')

  def blurMultiplier(self) -> float:
    """
    Calls Qt's 'qreal QQuickMultiEffect::blurMultiplier() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffect.html#blurMultiplier
    """
    #  qreal QQuickMultiEffect::blurMultiplier() const
    return self.uglySide.call(
        'ritual_ZNK17QQuickMultiEffect14blurMultiplierEv',
    )

  def shadowEnabled(self) -> bool:
    """
    Calls Qt's 'bool QQuickMultiEffect::shadowEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffect.html#shadowEnabled
    """
    #  bool QQuickMultiEffect::shadowEnabled() const
    return self.uglySide.call(
        'ritual_ZNK17QQuickMultiEffect13shadowEnabledEv',
    )

  def shadowOpacity(self) -> float:
    """
    Calls Qt's 'qreal QQuickMultiEffect::shadowOpacity() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffect.html#shadowOpacity
    """
    #  qreal QQuickMultiEffect::shadowOpacity() const
    return self.uglySide.call(
        'ritual_ZNK17QQuickMultiEffect13shadowOpacityEv',
    )

  def shadowBlur(self) -> float:
    """
    Calls Qt's 'qreal QQuickMultiEffect::shadowBlur() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmultieffect.html#shadowBlur
    """
    #  qreal QQuickMultiEffect::shadowBlur() const
    return self.uglySide.call('ritual_ZNK17QQuickMultiEffect10shadowBlurEv')

  def shadowHorizontalOffset(self) -> float:
    """
    Calls Qt's 'qreal QQuickMultiEffect::shadowHorizontalOffset() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffect.html#shadowHorizontalOffset
    """
    #  qreal QQuickMultiEffect::shadowHorizontalOffset() const
    return self.uglySide.call(
        'ritual_ZNK17QQuickMultiEffect22shadowHorizontalOffsetEv',
    )

  def shadowVerticalOffset(self) -> float:
    """
    Calls Qt's 'qreal QQuickMultiEffect::shadowVerticalOffset() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffect.html#shadowVerticalOffset
    """
    #  qreal QQuickMultiEffect::shadowVerticalOffset() const
    return self.uglySide.call(
        'ritual_ZNK17QQuickMultiEffect20shadowVerticalOffsetEv',
    )

  def shadowColor(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickMultiEffect::shadowColor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmultieffect.html#shadowColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickMultiEffect::shadowColor() const
    address = self.uglySide.call(
        'ritual_ZNK17QQuickMultiEffect11shadowColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def shadowScale(self) -> float:
    """
    Calls Qt's 'qreal QQuickMultiEffect::shadowScale() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmultieffect.html#shadowScale
    """
    #  qreal QQuickMultiEffect::shadowScale() const
    return self.uglySide.call('ritual_ZNK17QQuickMultiEffect11shadowScaleEv')

  def maskEnabled(self) -> bool:
    """
    Calls Qt's 'bool QQuickMultiEffect::maskEnabled() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmultieffect.html#maskEnabled
    """
    #  bool QQuickMultiEffect::maskEnabled() const
    return self.uglySide.call('ritual_ZNK17QQuickMultiEffect11maskEnabledEv')

  def maskSource(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickMultiEffect::maskSource() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmultieffect.html#maskSource

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickMultiEffect::maskSource() const
    address = self.uglySide.call(
        'ritual_ZNK17QQuickMultiEffect10maskSourceEv',
    )
    return QQuickItem._cuteAt(address)

  def maskThresholdMin(self) -> float:
    """
    Calls Qt's 'qreal QQuickMultiEffect::maskThresholdMin() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffect.html#maskThresholdMin
    """
    #  qreal QQuickMultiEffect::maskThresholdMin() const
    return self.uglySide.call(
        'ritual_ZNK17QQuickMultiEffect16maskThresholdMinEv',
    )

  def maskSpreadAtMin(self) -> float:
    """
    Calls Qt's 'qreal QQuickMultiEffect::maskSpreadAtMin() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffect.html#maskSpreadAtMin
    """
    #  qreal QQuickMultiEffect::maskSpreadAtMin() const
    return self.uglySide.call(
        'ritual_ZNK17QQuickMultiEffect15maskSpreadAtMinEv',
    )

  def maskThresholdMax(self) -> float:
    """
    Calls Qt's 'qreal QQuickMultiEffect::maskThresholdMax() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffect.html#maskThresholdMax
    """
    #  qreal QQuickMultiEffect::maskThresholdMax() const
    return self.uglySide.call(
        'ritual_ZNK17QQuickMultiEffect16maskThresholdMaxEv',
    )

  def maskSpreadAtMax(self) -> float:
    """
    Calls Qt's 'qreal QQuickMultiEffect::maskSpreadAtMax() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffect.html#maskSpreadAtMax
    """
    #  qreal QQuickMultiEffect::maskSpreadAtMax() const
    return self.uglySide.call(
        'ritual_ZNK17QQuickMultiEffect15maskSpreadAtMaxEv',
    )

  def maskInverted(self) -> bool:
    """
    Calls Qt's 'bool QQuickMultiEffect::maskInverted() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffect.html#maskInverted
    """
    #  bool QQuickMultiEffect::maskInverted() const
    return self.uglySide.call(
        'ritual_ZNK17QQuickMultiEffect12maskInvertedEv',
    )

  def itemRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QQuickMultiEffect::itemRect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmultieffect.html#itemRect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QQuickMultiEffect::itemRect() const
    address = self.uglySide.call('ritual_ZNK17QQuickMultiEffect8itemRectEv')
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def fragmentShader(self) -> str:
    """
    Calls Qt's 'QString QQuickMultiEffect::fragmentShader() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffect.html#fragmentShader

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickMultiEffect::fragmentShader() const
    return self.uglySide.call(
        'ritual_ZNK17QQuickMultiEffect14fragmentShaderEv',
    )

  def vertexShader(self) -> str:
    """
    Calls Qt's 'QString QQuickMultiEffect::vertexShader() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffect.html#vertexShader

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickMultiEffect::vertexShader() const
    return self.uglySide.call(
        'ritual_ZNK17QQuickMultiEffect12vertexShaderEv',
    )

  def hasProxySource(self) -> bool:
    """
    Calls Qt's 'bool QQuickMultiEffect::hasProxySource() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffect.html#hasProxySource
    """
    #  bool QQuickMultiEffect::hasProxySource() const
    return self.uglySide.call(
        'ritual_ZNK17QQuickMultiEffect14hasProxySourceEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuickItem)
  @overload(NoneType)
  def setSource(self, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickMultiEffect::setSource(QQuickItem *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmultieffect.html#setSource

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickMultiEffect::setSource(QQuickItem *item)
    self.uglySide.call(
        'ritual_ZN17QQuickMultiEffect9setSourceEP10QQuickItem',
        self._addressOf(item),
    )

  @overload(bool)
  def setAutoPaddingEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QQuickMultiEffect::setAutoPaddingEnabled(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffect.html#setAutoPaddingEnabled

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QQuickMultiEffect::setAutoPaddingEnabled(bool enabled)
    self.uglySide.call(
        'ritual_ZN17QQuickMultiEffect21setAutoPaddingEnabledEb', enabled,
    )

  @overload(QRectF)
  def setPaddingRect(self, rect: QRectF) -> None:
    """
    Calls Qt's 'void QQuickMultiEffect::setPaddingRect(const QRectF &rect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffect.html#setPaddingRect

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QQuickMultiEffect::setPaddingRect(const QRectF &rect)
    self.uglySide.call(
        'ritual_ZN17QQuickMultiEffect14setPaddingRectERK6QRectF',
        self._valueOf(rect),
    )

  @overload(float)
  def setBrightness(self, brightness: float) -> None:
    """
    Calls Qt's 'void QQuickMultiEffect::setBrightness(qreal brightness)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffect.html#setBrightness

    Parameters
    ----------

    brightness : float
      Passed on as it is.
    """
    #  void QQuickMultiEffect::setBrightness(qreal brightness)
    self.uglySide.call(
        'ritual_ZN17QQuickMultiEffect13setBrightnessEd', brightness,
    )

  @overload(float)
  def setContrast(self, contrast: float) -> None:
    """
    Calls Qt's 'void QQuickMultiEffect::setContrast(qreal contrast)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmultieffect.html#setContrast

    Parameters
    ----------

    contrast : float
      Passed on as it is.
    """
    #  void QQuickMultiEffect::setContrast(qreal contrast)
    self.uglySide.call(
        'ritual_ZN17QQuickMultiEffect11setContrastEd', contrast,
    )

  @overload(float)
  def setSaturation(self, saturation: float) -> None:
    """
    Calls Qt's 'void QQuickMultiEffect::setSaturation(qreal saturation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffect.html#setSaturation

    Parameters
    ----------

    saturation : float
      Passed on as it is.
    """
    #  void QQuickMultiEffect::setSaturation(qreal saturation)
    self.uglySide.call(
        'ritual_ZN17QQuickMultiEffect13setSaturationEd', saturation,
    )

  @overload(float)
  def setColorization(self, colorization: float) -> None:
    """
    Calls Qt's 'void QQuickMultiEffect::setColorization(qreal colorization)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffect.html#setColorization

    Parameters
    ----------

    colorization : float
      Passed on as it is.
    """
    #  void QQuickMultiEffect::setColorization(qreal colorization)
    self.uglySide.call(
        'ritual_ZN17QQuickMultiEffect15setColorizationEd', colorization,
    )

  @overload(QColor)
  def setColorizationColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QQuickMultiEffect::setColorizationColor(const QColor
    &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffect.html#setColorizationColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickMultiEffect::setColorizationColor(const QColor &color)
    self.uglySide.call(
        'ritual_ZN17QQuickMultiEffect20setColorizationColorERK6QColor',
        self._valueOf(color),
    )

  @overload(bool)
  def setBlurEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QQuickMultiEffect::setBlurEnabled(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffect.html#setBlurEnabled

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QQuickMultiEffect::setBlurEnabled(bool enabled)
    self.uglySide.call(
        'ritual_ZN17QQuickMultiEffect14setBlurEnabledEb', enabled,
    )

  @overload(float)
  def setBlur(self, blur: float) -> None:
    """
    Calls Qt's 'void QQuickMultiEffect::setBlur(qreal blur)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmultieffect.html#setBlur

    Parameters
    ----------

    blur : float
      Passed on as it is.
    """
    #  void QQuickMultiEffect::setBlur(qreal blur)
    self.uglySide.call('ritual_ZN17QQuickMultiEffect7setBlurEd', blur)

  @overload(int)
  def setBlurMax(self, blurMax: int) -> None:
    """
    Calls Qt's 'void QQuickMultiEffect::setBlurMax(int blurMax)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmultieffect.html#setBlurMax

    Parameters
    ----------

    blurMax : int
      Passed on as it is.
    """
    #  void QQuickMultiEffect::setBlurMax(int blurMax)
    self.uglySide.call('ritual_ZN17QQuickMultiEffect10setBlurMaxEi', blurMax)

  @overload(float)
  def setBlurMultiplier(self, blurMultiplier: float) -> None:
    """
    Calls Qt's 'void QQuickMultiEffect::setBlurMultiplier(qreal
    blurMultiplier)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffect.html#setBlurMultiplier

    Parameters
    ----------

    blurMultiplier : float
      Passed on as it is.
    """
    #  void QQuickMultiEffect::setBlurMultiplier(qreal blurMultiplier)
    self.uglySide.call(
        'ritual_ZN17QQuickMultiEffect17setBlurMultiplierEd', blurMultiplier,
    )

  @overload(bool)
  def setShadowEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QQuickMultiEffect::setShadowEnabled(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffect.html#setShadowEnabled

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QQuickMultiEffect::setShadowEnabled(bool enabled)
    self.uglySide.call(
        'ritual_ZN17QQuickMultiEffect16setShadowEnabledEb', enabled,
    )

  @overload(float)
  def setShadowOpacity(self, shadowOpacity: float) -> None:
    """
    Calls Qt's 'void QQuickMultiEffect::setShadowOpacity(qreal
    shadowOpacity)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffect.html#setShadowOpacity

    Parameters
    ----------

    shadowOpacity : float
      Passed on as it is.
    """
    #  void QQuickMultiEffect::setShadowOpacity(qreal shadowOpacity)
    self.uglySide.call(
        'ritual_ZN17QQuickMultiEffect16setShadowOpacityEd', shadowOpacity,
    )

  @overload(float)
  def setShadowBlur(self, shadowBlur: float) -> None:
    """
    Calls Qt's 'void QQuickMultiEffect::setShadowBlur(qreal shadowBlur)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffect.html#setShadowBlur

    Parameters
    ----------

    shadowBlur : float
      Passed on as it is.
    """
    #  void QQuickMultiEffect::setShadowBlur(qreal shadowBlur)
    self.uglySide.call(
        'ritual_ZN17QQuickMultiEffect13setShadowBlurEd', shadowBlur,
    )

  @overload(float)
  def setShadowHorizontalOffset(self, offset: float) -> None:
    """
    Calls Qt's 'void QQuickMultiEffect::setShadowHorizontalOffset(qreal
    offset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffect.html#setShadowHorizontalOffset

    Parameters
    ----------

    offset : float
      Passed on as it is.
    """
    #  void QQuickMultiEffect::setShadowHorizontalOffset(qreal offset)
    self.uglySide.call(
        'ritual_ZN17QQuickMultiEffect25setShadowHorizontalOffsetEd', offset,
    )

  @overload(float)
  def setShadowVerticalOffset(self, offset: float) -> None:
    """
    Calls Qt's 'void QQuickMultiEffect::setShadowVerticalOffset(qreal
    offset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffect.html#setShadowVerticalOffset

    Parameters
    ----------

    offset : float
      Passed on as it is.
    """
    #  void QQuickMultiEffect::setShadowVerticalOffset(qreal offset)
    self.uglySide.call(
        'ritual_ZN17QQuickMultiEffect23setShadowVerticalOffsetEd', offset,
    )

  @overload(QColor)
  def setShadowColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QQuickMultiEffect::setShadowColor(const QColor &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffect.html#setShadowColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickMultiEffect::setShadowColor(const QColor &color)
    self.uglySide.call(
        'ritual_ZN17QQuickMultiEffect14setShadowColorERK6QColor',
        self._valueOf(color),
    )

  @overload(float)
  def setShadowScale(self, shadowScale: float) -> None:
    """
    Calls Qt's 'void QQuickMultiEffect::setShadowScale(qreal shadowScale)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffect.html#setShadowScale

    Parameters
    ----------

    shadowScale : float
      Passed on as it is.
    """
    #  void QQuickMultiEffect::setShadowScale(qreal shadowScale)
    self.uglySide.call(
        'ritual_ZN17QQuickMultiEffect14setShadowScaleEd', shadowScale,
    )

  @overload(bool)
  def setMaskEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QQuickMultiEffect::setMaskEnabled(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffect.html#setMaskEnabled

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QQuickMultiEffect::setMaskEnabled(bool enabled)
    self.uglySide.call(
        'ritual_ZN17QQuickMultiEffect14setMaskEnabledEb', enabled,
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def setMaskSource(self, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickMultiEffect::setMaskSource(QQuickItem *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffect.html#setMaskSource

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickMultiEffect::setMaskSource(QQuickItem *item)
    self.uglySide.call(
        'ritual_ZN17QQuickMultiEffect13setMaskSourceEP10QQuickItem',
        self._addressOf(item),
    )

  @overload(float)
  def setMaskThresholdMin(self, threshold: float) -> None:
    """
    Calls Qt's 'void QQuickMultiEffect::setMaskThresholdMin(qreal
    threshold)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffect.html#setMaskThresholdMin

    Parameters
    ----------

    threshold : float
      Passed on as it is.
    """
    #  void QQuickMultiEffect::setMaskThresholdMin(qreal threshold)
    self.uglySide.call(
        'ritual_ZN17QQuickMultiEffect19setMaskThresholdMinEd', threshold,
    )

  @overload(float)
  def setMaskSpreadAtMin(self, spread: float) -> None:
    """
    Calls Qt's 'void QQuickMultiEffect::setMaskSpreadAtMin(qreal spread)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffect.html#setMaskSpreadAtMin

    Parameters
    ----------

    spread : float
      Passed on as it is.
    """
    #  void QQuickMultiEffect::setMaskSpreadAtMin(qreal spread)
    self.uglySide.call(
        'ritual_ZN17QQuickMultiEffect18setMaskSpreadAtMinEd', spread,
    )

  @overload(float)
  def setMaskThresholdMax(self, threshold: float) -> None:
    """
    Calls Qt's 'void QQuickMultiEffect::setMaskThresholdMax(qreal
    threshold)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffect.html#setMaskThresholdMax

    Parameters
    ----------

    threshold : float
      Passed on as it is.
    """
    #  void QQuickMultiEffect::setMaskThresholdMax(qreal threshold)
    self.uglySide.call(
        'ritual_ZN17QQuickMultiEffect19setMaskThresholdMaxEd', threshold,
    )

  @overload(float)
  def setMaskSpreadAtMax(self, spread: float) -> None:
    """
    Calls Qt's 'void QQuickMultiEffect::setMaskSpreadAtMax(qreal spread)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffect.html#setMaskSpreadAtMax

    Parameters
    ----------

    spread : float
      Passed on as it is.
    """
    #  void QQuickMultiEffect::setMaskSpreadAtMax(qreal spread)
    self.uglySide.call(
        'ritual_ZN17QQuickMultiEffect18setMaskSpreadAtMaxEd', spread,
    )

  @overload(bool)
  def setMaskInverted(self, inverted: bool) -> None:
    """
    Calls Qt's 'void QQuickMultiEffect::setMaskInverted(bool inverted)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffect.html#setMaskInverted

    Parameters
    ----------

    inverted : bool
      Passed on as it is.
    """
    #  void QQuickMultiEffect::setMaskInverted(bool inverted)
    self.uglySide.call(
        'ritual_ZN17QQuickMultiEffect15setMaskInvertedEb', inverted,
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
  @overload(QQuickItem)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuickItem] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuickMultiEffect::QQuickMultiEffect(QQuickItem *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffect.html#QQuickMultiEffect

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickMultiEffect::QQuickMultiEffect(QQuickItem *parent)
    self._noteCreation(QQuickMultiEffect, lambda: Rituals.call(
        'ritual_ZN17QQuickMultiEffectC1EP10QQuickItem',
        self._addressOf(parent),
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

  def shaderChanged(self) -> None:
    """
    Calls Qt's 'void QQuickMultiEffect::shaderChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffect.html#shaderChanged
    """
    #  void QQuickMultiEffect::shaderChanged()
    self.uglySide.call('ritual_ZN17QQuickMultiEffect13shaderChangedEv')

  def itemSizeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickMultiEffect::itemSizeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffect.html#itemSizeChanged
    """
    #  void QQuickMultiEffect::itemSizeChanged()
    self.uglySide.call('ritual_ZN17QQuickMultiEffect15itemSizeChangedEv')

  def sourceChanged(self) -> None:
    """
    Calls Qt's 'void QQuickMultiEffect::sourceChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffect.html#sourceChanged
    """
    #  void QQuickMultiEffect::sourceChanged()
    self.uglySide.call('ritual_ZN17QQuickMultiEffect13sourceChangedEv')

  def autoPaddingEnabledChanged(self) -> None:
    """
    Calls Qt's 'void QQuickMultiEffect::autoPaddingEnabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffect.html#autoPaddingEnabledChanged
    """
    #  void QQuickMultiEffect::autoPaddingEnabledChanged()
    self.uglySide.call(
        'ritual_ZN17QQuickMultiEffect25autoPaddingEnabledChangedEv',
    )

  def paddingRectChanged(self) -> None:
    """
    Calls Qt's 'void QQuickMultiEffect::paddingRectChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffect.html#paddingRectChanged
    """
    #  void QQuickMultiEffect::paddingRectChanged()
    self.uglySide.call('ritual_ZN17QQuickMultiEffect18paddingRectChangedEv')

  def brightnessChanged(self) -> None:
    """
    Calls Qt's 'void QQuickMultiEffect::brightnessChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffect.html#brightnessChanged
    """
    #  void QQuickMultiEffect::brightnessChanged()
    self.uglySide.call('ritual_ZN17QQuickMultiEffect17brightnessChangedEv')

  def contrastChanged(self) -> None:
    """
    Calls Qt's 'void QQuickMultiEffect::contrastChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffect.html#contrastChanged
    """
    #  void QQuickMultiEffect::contrastChanged()
    self.uglySide.call('ritual_ZN17QQuickMultiEffect15contrastChangedEv')

  def saturationChanged(self) -> None:
    """
    Calls Qt's 'void QQuickMultiEffect::saturationChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffect.html#saturationChanged
    """
    #  void QQuickMultiEffect::saturationChanged()
    self.uglySide.call('ritual_ZN17QQuickMultiEffect17saturationChangedEv')

  def colorizationChanged(self) -> None:
    """
    Calls Qt's 'void QQuickMultiEffect::colorizationChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffect.html#colorizationChanged
    """
    #  void QQuickMultiEffect::colorizationChanged()
    self.uglySide.call('ritual_ZN17QQuickMultiEffect19colorizationChangedEv')

  def colorizationColorChanged(self) -> None:
    """
    Calls Qt's 'void QQuickMultiEffect::colorizationColorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffect.html#colorizationColorChanged
    """
    #  void QQuickMultiEffect::colorizationColorChanged()
    self.uglySide.call(
        'ritual_ZN17QQuickMultiEffect24colorizationColorChangedEv',
    )

  def blurEnabledChanged(self) -> None:
    """
    Calls Qt's 'void QQuickMultiEffect::blurEnabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffect.html#blurEnabledChanged
    """
    #  void QQuickMultiEffect::blurEnabledChanged()
    self.uglySide.call('ritual_ZN17QQuickMultiEffect18blurEnabledChangedEv')

  def blurChanged(self) -> None:
    """
    Calls Qt's 'void QQuickMultiEffect::blurChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmultieffect.html#blurChanged
    """
    #  void QQuickMultiEffect::blurChanged()
    self.uglySide.call('ritual_ZN17QQuickMultiEffect11blurChangedEv')

  def blurMaxChanged(self) -> None:
    """
    Calls Qt's 'void QQuickMultiEffect::blurMaxChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffect.html#blurMaxChanged
    """
    #  void QQuickMultiEffect::blurMaxChanged()
    self.uglySide.call('ritual_ZN17QQuickMultiEffect14blurMaxChangedEv')

  def blurMultiplierChanged(self) -> None:
    """
    Calls Qt's 'void QQuickMultiEffect::blurMultiplierChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffect.html#blurMultiplierChanged
    """
    #  void QQuickMultiEffect::blurMultiplierChanged()
    self.uglySide.call(
        'ritual_ZN17QQuickMultiEffect21blurMultiplierChangedEv',
    )

  def shadowEnabledChanged(self) -> None:
    """
    Calls Qt's 'void QQuickMultiEffect::shadowEnabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffect.html#shadowEnabledChanged
    """
    #  void QQuickMultiEffect::shadowEnabledChanged()
    self.uglySide.call(
        'ritual_ZN17QQuickMultiEffect20shadowEnabledChangedEv',
    )

  def shadowOpacityChanged(self) -> None:
    """
    Calls Qt's 'void QQuickMultiEffect::shadowOpacityChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffect.html#shadowOpacityChanged
    """
    #  void QQuickMultiEffect::shadowOpacityChanged()
    self.uglySide.call(
        'ritual_ZN17QQuickMultiEffect20shadowOpacityChangedEv',
    )

  def shadowBlurChanged(self) -> None:
    """
    Calls Qt's 'void QQuickMultiEffect::shadowBlurChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffect.html#shadowBlurChanged
    """
    #  void QQuickMultiEffect::shadowBlurChanged()
    self.uglySide.call('ritual_ZN17QQuickMultiEffect17shadowBlurChangedEv')

  def shadowHorizontalOffsetChanged(self) -> None:
    """
    Calls Qt's 'void QQuickMultiEffect::shadowHorizontalOffsetChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffect.html
    """
    #  void QQuickMultiEffect::shadowHorizontalOffsetChanged()
    self.uglySide.call(
        'ritual_ZN17QQuickMultiEffect29shadowHorizontalOffsetChangedEv',
    )

  def shadowVerticalOffsetChanged(self) -> None:
    """
    Calls Qt's 'void QQuickMultiEffect::shadowVerticalOffsetChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffect.html#shadowVerticalOffsetChanged
    """
    #  void QQuickMultiEffect::shadowVerticalOffsetChanged()
    self.uglySide.call(
        'ritual_ZN17QQuickMultiEffect27shadowVerticalOffsetChangedEv',
    )

  def shadowColorChanged(self) -> None:
    """
    Calls Qt's 'void QQuickMultiEffect::shadowColorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffect.html#shadowColorChanged
    """
    #  void QQuickMultiEffect::shadowColorChanged()
    self.uglySide.call('ritual_ZN17QQuickMultiEffect18shadowColorChangedEv')

  def shadowScaleChanged(self) -> None:
    """
    Calls Qt's 'void QQuickMultiEffect::shadowScaleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffect.html#shadowScaleChanged
    """
    #  void QQuickMultiEffect::shadowScaleChanged()
    self.uglySide.call('ritual_ZN17QQuickMultiEffect18shadowScaleChangedEv')

  def maskEnabledChanged(self) -> None:
    """
    Calls Qt's 'void QQuickMultiEffect::maskEnabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffect.html#maskEnabledChanged
    """
    #  void QQuickMultiEffect::maskEnabledChanged()
    self.uglySide.call('ritual_ZN17QQuickMultiEffect18maskEnabledChangedEv')

  def maskSourceChanged(self) -> None:
    """
    Calls Qt's 'void QQuickMultiEffect::maskSourceChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffect.html#maskSourceChanged
    """
    #  void QQuickMultiEffect::maskSourceChanged()
    self.uglySide.call('ritual_ZN17QQuickMultiEffect17maskSourceChangedEv')

  def maskThresholdMinChanged(self) -> None:
    """
    Calls Qt's 'void QQuickMultiEffect::maskThresholdMinChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffect.html#maskThresholdMinChanged
    """
    #  void QQuickMultiEffect::maskThresholdMinChanged()
    self.uglySide.call(
        'ritual_ZN17QQuickMultiEffect23maskThresholdMinChangedEv',
    )

  def maskSpreadAtMinChanged(self) -> None:
    """
    Calls Qt's 'void QQuickMultiEffect::maskSpreadAtMinChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffect.html#maskSpreadAtMinChanged
    """
    #  void QQuickMultiEffect::maskSpreadAtMinChanged()
    self.uglySide.call(
        'ritual_ZN17QQuickMultiEffect22maskSpreadAtMinChangedEv',
    )

  def maskThresholdMaxChanged(self) -> None:
    """
    Calls Qt's 'void QQuickMultiEffect::maskThresholdMaxChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffect.html#maskThresholdMaxChanged
    """
    #  void QQuickMultiEffect::maskThresholdMaxChanged()
    self.uglySide.call(
        'ritual_ZN17QQuickMultiEffect23maskThresholdMaxChangedEv',
    )

  def maskSpreadAtMaxChanged(self) -> None:
    """
    Calls Qt's 'void QQuickMultiEffect::maskSpreadAtMaxChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffect.html#maskSpreadAtMaxChanged
    """
    #  void QQuickMultiEffect::maskSpreadAtMaxChanged()
    self.uglySide.call(
        'ritual_ZN17QQuickMultiEffect22maskSpreadAtMaxChangedEv',
    )

  def maskInvertedChanged(self) -> None:
    """
    Calls Qt's 'void QQuickMultiEffect::maskInvertedChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffect.html#maskInvertedChanged
    """
    #  void QQuickMultiEffect::maskInvertedChanged()
    self.uglySide.call('ritual_ZN17QQuickMultiEffect19maskInvertedChangedEv')

  def itemRectChanged(self) -> None:
    """
    Calls Qt's 'void QQuickMultiEffect::itemRectChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffect.html#itemRectChanged
    """
    #  void QQuickMultiEffect::itemRectChanged()
    self.uglySide.call('ritual_ZN17QQuickMultiEffect15itemRectChangedEv')

  def fragmentShaderChanged(self) -> None:
    """
    Calls Qt's 'void QQuickMultiEffect::fragmentShaderChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffect.html#fragmentShaderChanged
    """
    #  void QQuickMultiEffect::fragmentShaderChanged()
    self.uglySide.call(
        'ritual_ZN17QQuickMultiEffect21fragmentShaderChangedEv',
    )

  def vertexShaderChanged(self) -> None:
    """
    Calls Qt's 'void QQuickMultiEffect::vertexShaderChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffect.html#vertexShaderChanged
    """
    #  void QQuickMultiEffect::vertexShaderChanged()
    self.uglySide.call('ritual_ZN17QQuickMultiEffect19vertexShaderChangedEv')

  def hasProxySourceChanged(self) -> None:
    """
    Calls Qt's 'void QQuickMultiEffect::hasProxySourceChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffect.html#hasProxySourceChanged
    """
    #  void QQuickMultiEffect::hasProxySourceChanged()
    self.uglySide.call(
        'ritual_ZN17QQuickMultiEffect21hasProxySourceChangedEv',
    )

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickMultiEffect::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffect.html#componentComplete
    """
    #  void QQuickMultiEffect::componentComplete()
    ritual = 'ritual_ZN17QQuickMultiEffect17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQuickMultiEffect17componentCompleteEv'
    self.uglySide.call(ritual)

  @overload(QRectF, QRectF)
  def geometryChange(self, newGeometry: QRectF, oldGeometry: QRectF) -> None:
    """
    Calls Qt's 'void QQuickMultiEffect::geometryChange(const QRectF
    &newGeometry, const QRectF &oldGeometry)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultieffect.html#geometryChange

    Parameters
    ----------

    newGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    oldGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QQuickMultiEffect::geometryChange(const QRectF &newGeometry,
    #      const QRectF &oldGeometry)
    ritual = 'ritual_ZN17QQuickMultiEffect14geometryChangeERK6QRectFS2_'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQuickMultiEffect14geometryChangeERK6QRectFS2_')
    self.uglySide.call(
        ritual, self._valueOf(newGeometry), self._valueOf(oldGeometry),
    )

  @overload(QQuickItem.ItemChange, QQuickItem.ItemChangeData)
  def itemChange(
      self,
      change: QQuickItem.ItemChange,
      value: QQuickItem.ItemChangeData,
  ) -> None:
    """
    Calls Qt's 'void QQuickMultiEffect::itemChange(ItemChange change, const
    ItemChangeData &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmultieffect.html#itemChange

    Parameters
    ----------

    change : QQuickItem.ItemChange
      Passed on as its number.

    value : QQuickItem.ItemChangeData
      Passed on as a value: Qt reads the C++ QQuickItem::ItemChangeData,
      which stays Python's own.
    """
    #  void QQuickMultiEffect::itemChange(ItemChange change, const
    #      ItemChangeData &value)
    ritual = (
        'ritual_ZN17QQuickMultiEffect10itemChangeEN10QQuickItem10ItemChange'
        'ERKNS0_14ItemChangeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQuickMultiEffect10itemChangeEN10QQuickItem10Item'
          'ChangeERKNS0_14ItemChangeDataE')
    self.uglySide.call(ritual, change.value, self._valueOf(value))

  def d_func(self) -> Optional[QQuickMultiEffectPrivate]:
    """
    Calls Qt's 'QQuickMultiEffectPrivate *QQuickMultiEffect::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmultieffect.html#d_func

    Returns
    -------

    Optional[QQuickMultiEffectPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickMultiEffectPrivate *QQuickMultiEffect::d_func()
    address = self.uglySide.call('ritual_ZN17QQuickMultiEffect6d_funcEv')
    from . import QQuickMultiEffectPrivate
    return QQuickMultiEffectPrivate._cuteAt(address)
