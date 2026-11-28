"""
QQuickRhiItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/qquickrhiitem.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from . import QQuickItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject, QRectF, QSize
  from . import QQuickRhiItemPrivate, QQuickRhiItemRenderer, QSGNode
  from . import QSGTextureProvider
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QRectF = WAIT['QRectF']
  QSGNode = WAIT['QSGNode']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickRhiItem(QQuickItem):
  """
  The cute side of Qt's QQuickRhiItem: a plain Python object standing in
  front of one C++ QQuickRhiItem.

  It is built on the cute 'QQuickItem', as Qt's QQuickRhiItem is built on
  Qt's QQuickItem, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickRhiItem that has a ritual and that Python can
  call so far, 34 names in all: 'metaObject', 'tr', 'd_func', 'sampleCount',
  'setSampleCount', 'colorBufferFormat', 'setColorBufferFormat',
  'isMirrorVerticallyEnabled', 'setMirrorVertically', 'alphaBlending',
  'setAlphaBlending', 'fixedColorBufferWidth', 'setFixedColorBufferWidth',
  'fixedColorBufferHeight', 'setFixedColorBufferHeight',
  'effectiveColorBufferSize', 'isTextureProvider', 'textureProvider',
  'sampleCountChanged', 'colorBufferFormatChanged',
  'autoRenderTargetChanged', 'mirrorVerticallyChanged',
  'alphaBlendingChanged', 'fixedColorBufferWidthChanged',
  'fixedColorBufferHeightChanged', 'effectiveColorBufferSizeChanged',
  'createRenderer', 'isAutoRenderTargetEnabled', 'setAutoRenderTarget',
  'updatePaintNode', 'event', 'geometryChange', 'releaseResources',
  'invalidateSceneGraph'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickRhiItem::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQuickRhiItem::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'const QQuickRhiItemPrivate *QQuickRhiItem::d_func() const': takes
    in Python what 'QQuickRhiItemPrivate *QQuickRhiItem::d_func()' takes.
  - Qt's 'QQuickRhiItem::~QQuickRhiItem()': the destructor: Python never
    removes a C++ QQuickRhiItem.
  - Qt's 'QQuickRhiItem::QQuickRhiItem(QQuickRhiItemPrivate &dd, QQuickItem
    *parent)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 42 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickRhiItem is created at the first use, not by
    'QQuickRhiItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickRhiItem.
  - Qt tells when it has removed the C++ QQuickRhiItem. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QQuickRhiItem, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class TextureFormat(CuteNum, scoped=True):
    """
    The enum 'QQuickRhiItem::TextureFormat' of Qt, with the 4 names Qt gives
    in it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    RGBA8 = Kee[int](0)
    RGBA16F = Kee[int](1)
    RGBA32F = Kee[int](2)
    RGB10A2 = Kee[int](3)

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
    Calls Qt's 'QString QQuickRhiItem::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrhiitem.html#tr

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
    #  QString QQuickRhiItem::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN13QQuickRhiItem2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickRhiItem'

  #  A C++ QQuickRhiItem Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickRhiItem'

  #  The functions Qt calls itself that QQuickRhiItem is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'createRenderer': (
          ('_ZN13QQuickRhiItem14createRendererEv',
           ('address', 'address', 'QtQuick:QQuickRhiItemRenderer'),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickRhiItem::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrhiitem.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickRhiItem::metaObject() const
    address = self.uglySide.call('ritual_ZNK13QQuickRhiItem10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def sampleCount(self) -> int:
    """
    Calls Qt's 'int QQuickRhiItem::sampleCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrhiitem.html#sampleCount
    """
    #  int QQuickRhiItem::sampleCount() const
    return self.uglySide.call('ritual_ZNK13QQuickRhiItem11sampleCountEv')

  def colorBufferFormat(self) -> TextureFormat:
    """
    Calls Qt's 'TextureFormat QQuickRhiItem::colorBufferFormat() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrhiitem.html#colorBufferFormat

    Returns
    -------

    TextureFormat
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'TextureFormat(number)'
      gives.
    """
    #  TextureFormat QQuickRhiItem::colorBufferFormat() const
    return QQuickRhiItem.TextureFormat(self.uglySide.call(
        'ritual_ZNK13QQuickRhiItem17colorBufferFormatEv',
    ))

  def isMirrorVerticallyEnabled(self) -> bool:
    """
    Calls Qt's 'bool QQuickRhiItem::isMirrorVerticallyEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrhiitem.html#isMirrorVerticallyEnabled
    """
    #  bool QQuickRhiItem::isMirrorVerticallyEnabled() const
    return self.uglySide.call(
        'ritual_ZNK13QQuickRhiItem25isMirrorVerticallyEnabledEv',
    )

  def alphaBlending(self) -> bool:
    """
    Calls Qt's 'bool QQuickRhiItem::alphaBlending() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrhiitem.html#alphaBlending
    """
    #  bool QQuickRhiItem::alphaBlending() const
    return self.uglySide.call('ritual_ZNK13QQuickRhiItem13alphaBlendingEv')

  def fixedColorBufferWidth(self) -> int:
    """
    Calls Qt's 'int QQuickRhiItem::fixedColorBufferWidth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrhiitem.html#fixedColorBufferWidth
    """
    #  int QQuickRhiItem::fixedColorBufferWidth() const
    return self.uglySide.call(
        'ritual_ZNK13QQuickRhiItem21fixedColorBufferWidthEv',
    )

  def fixedColorBufferHeight(self) -> int:
    """
    Calls Qt's 'int QQuickRhiItem::fixedColorBufferHeight() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrhiitem.html#fixedColorBufferHeight
    """
    #  int QQuickRhiItem::fixedColorBufferHeight() const
    return self.uglySide.call(
        'ritual_ZNK13QQuickRhiItem22fixedColorBufferHeightEv',
    )

  def effectiveColorBufferSize(self) -> QSize:
    """
    Calls Qt's 'QSize QQuickRhiItem::effectiveColorBufferSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrhiitem.html#effectiveColorBufferSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QQuickRhiItem::effectiveColorBufferSize() const
    address = self.uglySide.call(
        'ritual_ZNK13QQuickRhiItem24effectiveColorBufferSizeEv',
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def isTextureProvider(self) -> bool:
    """
    Calls Qt's 'bool QQuickRhiItem::isTextureProvider() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrhiitem.html#isTextureProvider
    """
    #  bool QQuickRhiItem::isTextureProvider() const
    ritual = 'ritual_ZNK13QQuickRhiItem17isTextureProviderEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13QQuickRhiItem17isTextureProviderEv'
    return self.uglySide.call(ritual)

  def textureProvider(self) -> Optional[QSGTextureProvider]:
    """
    Calls Qt's 'QSGTextureProvider *QQuickRhiItem::textureProvider() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrhiitem.html#textureProvider

    Returns
    -------

    Optional[QSGTextureProvider]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGTextureProvider *QQuickRhiItem::textureProvider() const
    ritual = 'ritual_ZNK13QQuickRhiItem15textureProviderEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13QQuickRhiItem15textureProviderEv'
    address = self.uglySide.call(ritual)
    from . import QSGTextureProvider
    return QSGTextureProvider._cuteAt(address)

  def isAutoRenderTargetEnabled(self) -> bool:
    """
    Calls Qt's 'bool QQuickRhiItem::isAutoRenderTargetEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrhiitem.html#isAutoRenderTargetEnabled
    """
    #  bool QQuickRhiItem::isAutoRenderTargetEnabled() const
    return self.uglySide.call(
        'ritual_ZNK13QQuickRhiItem25isAutoRenderTargetEnabledEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setSampleCount(self, samples: int) -> None:
    """
    Calls Qt's 'void QQuickRhiItem::setSampleCount(int samples)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrhiitem.html#setSampleCount

    Parameters
    ----------

    samples : int
      Passed on as it is.
    """
    #  void QQuickRhiItem::setSampleCount(int samples)
    self.uglySide.call('ritual_ZN13QQuickRhiItem14setSampleCountEi', samples)

  @overload(TextureFormat)
  def setColorBufferFormat(self, format: TextureFormat) -> None:
    """
    Calls Qt's 'void QQuickRhiItem::setColorBufferFormat(TextureFormat
    format)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrhiitem.html#setColorBufferFormat

    Parameters
    ----------

    format : TextureFormat
      Passed on as its number.
    """
    #  void QQuickRhiItem::setColorBufferFormat(TextureFormat format)
    self.uglySide.call(
        'ritual_ZN13QQuickRhiItem20setColorBufferFormatENS_13TextureFormatE',
        format.value,
    )

  @overload(bool)
  def setMirrorVertically(self, enable: bool) -> None:
    """
    Calls Qt's 'void QQuickRhiItem::setMirrorVertically(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrhiitem.html#setMirrorVertically

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QQuickRhiItem::setMirrorVertically(bool enable)
    self.uglySide.call(
        'ritual_ZN13QQuickRhiItem19setMirrorVerticallyEb', enable,
    )

  @overload(bool)
  def setAlphaBlending(self, enable: bool) -> None:
    """
    Calls Qt's 'void QQuickRhiItem::setAlphaBlending(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrhiitem.html#setAlphaBlending

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QQuickRhiItem::setAlphaBlending(bool enable)
    self.uglySide.call(
        'ritual_ZN13QQuickRhiItem16setAlphaBlendingEb', enable,
    )

  @overload(int)
  def setFixedColorBufferWidth(self, width: int) -> None:
    """
    Calls Qt's 'void QQuickRhiItem::setFixedColorBufferWidth(int width)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrhiitem.html#setFixedColorBufferWidth

    Parameters
    ----------

    width : int
      Passed on as it is.
    """
    #  void QQuickRhiItem::setFixedColorBufferWidth(int width)
    self.uglySide.call(
        'ritual_ZN13QQuickRhiItem24setFixedColorBufferWidthEi', width,
    )

  @overload(int)
  def setFixedColorBufferHeight(self, height: int) -> None:
    """
    Calls Qt's 'void QQuickRhiItem::setFixedColorBufferHeight(int height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrhiitem.html#setFixedColorBufferHeight

    Parameters
    ----------

    height : int
      Passed on as it is.
    """
    #  void QQuickRhiItem::setFixedColorBufferHeight(int height)
    self.uglySide.call(
        'ritual_ZN13QQuickRhiItem25setFixedColorBufferHeightEi', height,
    )

  @overload(bool)
  def setAutoRenderTarget(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QQuickRhiItem::setAutoRenderTarget(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrhiitem.html#setAutoRenderTarget

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QQuickRhiItem::setAutoRenderTarget(bool enabled)
    self.uglySide.call(
        'ritual_ZN13QQuickRhiItem19setAutoRenderTargetEb', enabled,
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
    Notes what was given, for Qt's 'QQuickRhiItem::QQuickRhiItem(QQuickItem
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qquickrhiitem.html#QQuickRhiItem

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickRhiItem::QQuickRhiItem(QQuickItem *parent)
    self._noteCreation(QQuickRhiItem, lambda: Rituals.call(
        'ritual_ZN13QQuickRhiItemC1EP10QQuickItem', self._addressOf(parent),
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

  def d_func(self) -> Optional[QQuickRhiItemPrivate]:
    """
    Calls Qt's 'QQuickRhiItemPrivate *QQuickRhiItem::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrhiitem.html#d_func

    Returns
    -------

    Optional[QQuickRhiItemPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickRhiItemPrivate *QQuickRhiItem::d_func()
    address = self.uglySide.call('ritual_ZN13QQuickRhiItem6d_funcEv')
    from . import QQuickRhiItemPrivate
    return QQuickRhiItemPrivate._cuteAt(address)

  def sampleCountChanged(self) -> None:
    """
    Calls Qt's 'void QQuickRhiItem::sampleCountChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrhiitem.html#sampleCountChanged
    """
    #  void QQuickRhiItem::sampleCountChanged()
    self.uglySide.call('ritual_ZN13QQuickRhiItem18sampleCountChangedEv')

  def colorBufferFormatChanged(self) -> None:
    """
    Calls Qt's 'void QQuickRhiItem::colorBufferFormatChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrhiitem.html#colorBufferFormatChanged
    """
    #  void QQuickRhiItem::colorBufferFormatChanged()
    self.uglySide.call(
        'ritual_ZN13QQuickRhiItem24colorBufferFormatChangedEv',
    )

  def autoRenderTargetChanged(self) -> None:
    """
    Calls Qt's 'void QQuickRhiItem::autoRenderTargetChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrhiitem.html#autoRenderTargetChanged
    """
    #  void QQuickRhiItem::autoRenderTargetChanged()
    self.uglySide.call('ritual_ZN13QQuickRhiItem23autoRenderTargetChangedEv')

  def mirrorVerticallyChanged(self) -> None:
    """
    Calls Qt's 'void QQuickRhiItem::mirrorVerticallyChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrhiitem.html#mirrorVerticallyChanged
    """
    #  void QQuickRhiItem::mirrorVerticallyChanged()
    self.uglySide.call('ritual_ZN13QQuickRhiItem23mirrorVerticallyChangedEv')

  def alphaBlendingChanged(self) -> None:
    """
    Calls Qt's 'void QQuickRhiItem::alphaBlendingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrhiitem.html#alphaBlendingChanged
    """
    #  void QQuickRhiItem::alphaBlendingChanged()
    self.uglySide.call('ritual_ZN13QQuickRhiItem20alphaBlendingChangedEv')

  def fixedColorBufferWidthChanged(self) -> None:
    """
    Calls Qt's 'void QQuickRhiItem::fixedColorBufferWidthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrhiitem.html#fixedColorBufferWidthChanged
    """
    #  void QQuickRhiItem::fixedColorBufferWidthChanged()
    self.uglySide.call(
        'ritual_ZN13QQuickRhiItem28fixedColorBufferWidthChangedEv',
    )

  def fixedColorBufferHeightChanged(self) -> None:
    """
    Calls Qt's 'void QQuickRhiItem::fixedColorBufferHeightChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrhiitem.html#fixedColorBufferHeightChanged
    """
    #  void QQuickRhiItem::fixedColorBufferHeightChanged()
    self.uglySide.call(
        'ritual_ZN13QQuickRhiItem29fixedColorBufferHeightChangedEv',
    )

  def effectiveColorBufferSizeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickRhiItem::effectiveColorBufferSizeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrhiitem.html#effectiveColorBufferSizeChanged
    """
    #  void QQuickRhiItem::effectiveColorBufferSizeChanged()
    self.uglySide.call(
        'ritual_ZN13QQuickRhiItem31effectiveColorBufferSizeChangedEv',
    )

  def createRenderer(self) -> Optional[QQuickRhiItemRenderer]:
    """
    Calls Qt's 'QQuickRhiItemRenderer *QQuickRhiItem::createRenderer()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrhiitem.html#createRenderer

    Returns
    -------

    Optional[QQuickRhiItemRenderer]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickRhiItemRenderer *QQuickRhiItem::createRenderer()
    address = self.uglySide.call(
        'ritual_ZN13QQuickRhiItem14createRendererEv',
    )
    from . import QQuickRhiItemRenderer
    return QQuickRhiItemRenderer._cuteAt(address)

  @overload(QSGNode, QQuickItem.UpdatePaintNodeData)
  @overload(QSGNode, NoneType)
  @overload(NoneType, QQuickItem.UpdatePaintNodeData)
  @overload(NoneType, NoneType)
  def updatePaintNode(
      self,
      a0: Optional[QSGNode],
      a1: Optional[QQuickItem.UpdatePaintNodeData],
  ) -> Optional[QSGNode]:
    """
    Calls Qt's 'QSGNode *QQuickRhiItem::updatePaintNode(QSGNode *a0,
    UpdatePaintNodeData *a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrhiitem.html#updatePaintNode

    Parameters
    ----------

    a0 : Optional[QSGNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : Optional[QQuickItem.UpdatePaintNodeData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QSGNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGNode *QQuickRhiItem::updatePaintNode(QSGNode *a0,
    #      UpdatePaintNodeData *a1)
    ritual = (
        'ritual_ZN13QQuickRhiItem15updatePaintNodeEP7QSGNodePN10QQuickItem1'
        '9UpdatePaintNodeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN13QQuickRhiItem15updatePaintNodeEP7QSGNodePN10QQuic'
          'kItem19UpdatePaintNodeDataE')
    address = self.uglySide.call(
        ritual, self._addressOf(a0, 'QSGNode'), self._addressOf(a1),
    )
    from . import QSGNode
    return QSGNode._cuteAt(address)

  @overload(QEvent)
  @overload(NoneType)
  def event(self, a0: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QQuickRhiItem::event(QEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrhiitem.html#event

    Parameters
    ----------

    a0 : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickRhiItem::event(QEvent *a0)
    ritual = 'ritual_ZN13QQuickRhiItem5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QQuickRhiItem5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QRectF, QRectF)
  def geometryChange(self, newGeometry: QRectF, oldGeometry: QRectF) -> None:
    """
    Calls Qt's 'void QQuickRhiItem::geometryChange(const QRectF &newGeometry,
    const QRectF &oldGeometry)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrhiitem.html#geometryChange

    Parameters
    ----------

    newGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    oldGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QQuickRhiItem::geometryChange(const QRectF &newGeometry, const
    #      QRectF &oldGeometry)
    ritual = 'ritual_ZN13QQuickRhiItem14geometryChangeERK6QRectFS2_'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QQuickRhiItem14geometryChangeERK6QRectFS2_'
    self.uglySide.call(
        ritual, self._valueOf(newGeometry), self._valueOf(oldGeometry),
    )

  def releaseResources(self) -> None:
    """
    Calls Qt's 'void QQuickRhiItem::releaseResources()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrhiitem.html#releaseResources
    """
    #  void QQuickRhiItem::releaseResources()
    ritual = 'ritual_ZN13QQuickRhiItem16releaseResourcesEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QQuickRhiItem16releaseResourcesEv'
    self.uglySide.call(ritual)

  def invalidateSceneGraph(self) -> None:
    """
    Calls Qt's 'void QQuickRhiItem::invalidateSceneGraph()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrhiitem.html#invalidateSceneGraph
    """
    #  void QQuickRhiItem::invalidateSceneGraph()
    self.uglySide.call('ritual_ZN13QQuickRhiItem20invalidateSceneGraphEv')
