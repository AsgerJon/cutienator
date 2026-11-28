"""
QQuickPaintedItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/qquickpainteditem.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, WAIT
from ..occult import Rituals
from . import QQuickItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QRect, QRectF, QSize
  from ..QtGui import QColor, QPainter
  from . import QQuickPaintedItemPrivate, QSGNode, QSGTextureProvider
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QPainter = WAIT['QPainter']
  QRect = WAIT['QRect']
  QSGNode = WAIT['QSGNode']
  QSize = WAIT['QSize']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickPaintedItem(QQuickItem):
  """
  The cute side of Qt's QQuickPaintedItem: a plain Python object standing in
  front of one C++ QQuickPaintedItem.

  It is built on the cute 'QQuickItem', as Qt's QQuickPaintedItem is built on
  Qt's QQuickItem, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickPaintedItem that has a ritual and that Python
  can call so far, 37 names in all: 'metaObject', 'tr', 'update',
  'opaquePainting', 'setOpaquePainting', 'antialiasing', 'setAntialiasing',
  'mipmap', 'setMipmap', 'performanceHints', 'setPerformanceHint',
  'setPerformanceHints', 'contentsBoundingRect', 'contentsSize',
  'setContentsSize', 'resetContentsSize', 'contentsScale',
  'setContentsScale', 'textureSize', 'setTextureSize', 'fillColor',
  'setFillColor', 'renderTarget', 'setRenderTarget', 'paint',
  'isTextureProvider', 'textureProvider', 'fillColorChanged',
  'contentsSizeChanged', 'contentsScaleChanged', 'renderTargetChanged',
  'textureSizeChanged', 'updatePaintNode', 'releaseResources', 'itemChange',
  'invalidateSceneGraph', 'd_func'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickPaintedItem::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickPaintedItem::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickPaintedItem::qt_qmlMarker_uncreatable()': one of Qt's
    own inner workings.
  - Qt's 'QQuickPaintedItem::~QQuickPaintedItem()': the destructor: Python
    never removes a C++ QQuickPaintedItem.
  - Qt's 'QQuickPaintedItem::QQuickPaintedItem(QQuickPaintedItemPrivate &dd,
    QQuickItem *parent)': takes a type Python has no way to hand over yet.
  - Qt's 'const QQuickPaintedItemPrivate *QQuickPaintedItem::d_func() const':
    takes in Python what 'QQuickPaintedItemPrivate
    *QQuickPaintedItem::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 48 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickPaintedItem is created at the first use, not by
    'QQuickPaintedItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickPaintedItem.
  - Qt tells when it has removed the C++ QQuickPaintedItem. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QQuickPaintedItem, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class PerformanceHint(CuteFlags):
    """
    The flags enum 'QQuickPaintedItem::PerformanceHint' of Qt, with the 1
    names Qt gives in it. Qt names the type of its combinations
    'QQuickPaintedItem::PerformanceHints'.
    """

    FastFBOResizing = 0x1

  PerformanceHints = PerformanceHint

  class RenderTarget(CuteNum):
    """
    The enum 'QQuickPaintedItem::RenderTarget' of Qt, with the 3 names Qt
    gives in it.
    """

    Image = Kee[int](0)
    FramebufferObject = Kee[int](1)
    InvertedYFramebufferObject = Kee[int](2)

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
    Calls Qt's 'QString QQuickPaintedItem::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpainteditem.html#tr

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
    #  QString QQuickPaintedItem::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN17QQuickPaintedItem2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickPaintedItem'

  #  A C++ QQuickPaintedItem Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickPaintedItem'

  #  The functions Qt calls itself that QQuickPaintedItem is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'paint': (
          ('_ZN17QQuickPaintedItem5paintEP8QPainter',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QPainter'),
           )),
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
    Calls Qt's 'const QMetaObject *QQuickPaintedItem::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpainteditem.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickPaintedItem::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QQuickPaintedItem10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def opaquePainting(self) -> bool:
    """
    Calls Qt's 'bool QQuickPaintedItem::opaquePainting() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpainteditem.html#opaquePainting
    """
    #  bool QQuickPaintedItem::opaquePainting() const
    return self.uglySide.call(
        'ritual_ZNK17QQuickPaintedItem14opaquePaintingEv',
    )

  def antialiasing(self) -> bool:
    """
    Calls Qt's 'bool QQuickPaintedItem::antialiasing() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpainteditem.html#antialiasing
    """
    #  bool QQuickPaintedItem::antialiasing() const
    return self.uglySide.call(
        'ritual_ZNK17QQuickPaintedItem12antialiasingEv',
    )

  def mipmap(self) -> bool:
    """
    Calls Qt's 'bool QQuickPaintedItem::mipmap() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpainteditem.html#mipmap
    """
    #  bool QQuickPaintedItem::mipmap() const
    return self.uglySide.call('ritual_ZNK17QQuickPaintedItem6mipmapEv')

  def performanceHints(self) -> PerformanceHints:
    """
    Calls Qt's 'PerformanceHints QQuickPaintedItem::performanceHints()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpainteditem.html#performanceHints

    Returns
    -------

    PerformanceHints
      The value standing for the combination Qt gave back.
    """
    #  PerformanceHints QQuickPaintedItem::performanceHints() const
    return QQuickPaintedItem.PerformanceHints(self.uglySide.call(
        'ritual_ZNK17QQuickPaintedItem16performanceHintsEv',
    ))

  def contentsBoundingRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QQuickPaintedItem::contentsBoundingRect() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpainteditem.html#contentsBoundingRect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QQuickPaintedItem::contentsBoundingRect() const
    address = self.uglySide.call(
        'ritual_ZNK17QQuickPaintedItem20contentsBoundingRectEv',
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def contentsSize(self) -> QSize:
    """
    Calls Qt's 'QSize QQuickPaintedItem::contentsSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpainteditem.html#contentsSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QQuickPaintedItem::contentsSize() const
    address = self.uglySide.call(
        'ritual_ZNK17QQuickPaintedItem12contentsSizeEv',
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def contentsScale(self) -> float:
    """
    Calls Qt's 'qreal QQuickPaintedItem::contentsScale() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpainteditem.html#contentsScale
    """
    #  qreal QQuickPaintedItem::contentsScale() const
    return self.uglySide.call(
        'ritual_ZNK17QQuickPaintedItem13contentsScaleEv',
    )

  def textureSize(self) -> QSize:
    """
    Calls Qt's 'QSize QQuickPaintedItem::textureSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpainteditem.html#textureSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QQuickPaintedItem::textureSize() const
    address = self.uglySide.call(
        'ritual_ZNK17QQuickPaintedItem11textureSizeEv',
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def fillColor(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickPaintedItem::fillColor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpainteditem.html#fillColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickPaintedItem::fillColor() const
    address = self.uglySide.call('ritual_ZNK17QQuickPaintedItem9fillColorEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def renderTarget(self) -> RenderTarget:
    """
    Calls Qt's 'RenderTarget QQuickPaintedItem::renderTarget() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpainteditem.html#renderTarget

    Returns
    -------

    RenderTarget
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'RenderTarget(number)'
      gives.
    """
    #  RenderTarget QQuickPaintedItem::renderTarget() const
    return QQuickPaintedItem.RenderTarget(self.uglySide.call(
        'ritual_ZNK17QQuickPaintedItem12renderTargetEv',
    ))

  def isTextureProvider(self) -> bool:
    """
    Calls Qt's 'bool QQuickPaintedItem::isTextureProvider() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpainteditem.html#isTextureProvider
    """
    #  bool QQuickPaintedItem::isTextureProvider() const
    ritual = 'ritual_ZNK17QQuickPaintedItem17isTextureProviderEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QQuickPaintedItem17isTextureProviderEv'
    return self.uglySide.call(ritual)

  def textureProvider(self) -> Optional[QSGTextureProvider]:
    """
    Calls Qt's 'QSGTextureProvider *QQuickPaintedItem::textureProvider()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpainteditem.html#textureProvider

    Returns
    -------

    Optional[QSGTextureProvider]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGTextureProvider *QQuickPaintedItem::textureProvider() const
    ritual = 'ritual_ZNK17QQuickPaintedItem15textureProviderEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QQuickPaintedItem15textureProviderEv'
    address = self.uglySide.call(ritual)
    from . import QSGTextureProvider
    return QSGTextureProvider._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setOpaquePainting(self, opaque: bool) -> None:
    """
    Calls Qt's 'void QQuickPaintedItem::setOpaquePainting(bool opaque)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpainteditem.html#setOpaquePainting

    Parameters
    ----------

    opaque : bool
      Passed on as it is.
    """
    #  void QQuickPaintedItem::setOpaquePainting(bool opaque)
    self.uglySide.call(
        'ritual_ZN17QQuickPaintedItem17setOpaquePaintingEb', opaque,
    )

  @overload(bool)
  def setAntialiasing(self, enable: bool) -> None:
    """
    Calls Qt's 'void QQuickPaintedItem::setAntialiasing(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpainteditem.html#setAntialiasing

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QQuickPaintedItem::setAntialiasing(bool enable)
    self.uglySide.call(
        'ritual_ZN17QQuickPaintedItem15setAntialiasingEb', enable,
    )

  @overload(bool)
  def setMipmap(self, enable: bool) -> None:
    """
    Calls Qt's 'void QQuickPaintedItem::setMipmap(bool enable)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpainteditem.html#setMipmap

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QQuickPaintedItem::setMipmap(bool enable)
    self.uglySide.call('ritual_ZN17QQuickPaintedItem9setMipmapEb', enable)

  @overload(PerformanceHint)
  @overload(PerformanceHint, bool)
  def setPerformanceHint(
      self,
      hint: PerformanceHint,
      enabled: bool = True,
  ) -> None:
    """
    Calls Qt's 'void QQuickPaintedItem::setPerformanceHint(PerformanceHint
    hint, bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpainteditem.html#setPerformanceHint

    Parameters
    ----------

    hint : PerformanceHint
      Passed on as its number.

    enabled : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QQuickPaintedItem::setPerformanceHint(PerformanceHint hint, bool
    #      enabled)
    self.uglySide.call(
        'ritual_ZN17QQuickPaintedItem18setPerformanceHintENS_15PerformanceH'
        'intEb',
        hint.value, enabled,
    )

  @overload(PerformanceHints)
  def setPerformanceHints(self, hints: PerformanceHints) -> None:
    """
    Calls Qt's 'void QQuickPaintedItem::setPerformanceHints(PerformanceHints
    hints)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpainteditem.html#setPerformanceHints

    Parameters
    ----------

    hints : PerformanceHints
      Passed on as its number.
    """
    #  void QQuickPaintedItem::setPerformanceHints(PerformanceHints hints)
    self.uglySide.call(
        'ritual_ZN17QQuickPaintedItem19setPerformanceHintsE6QFlagsINS_15Per'
        'formanceHintEE',
        hints.value,
    )

  @overload(QSize)
  def setContentsSize(self, a0: QSize) -> None:
    """
    Calls Qt's 'void QQuickPaintedItem::setContentsSize(const QSize &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpainteditem.html#setContentsSize

    Parameters
    ----------

    a0 : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QQuickPaintedItem::setContentsSize(const QSize &a0)
    self.uglySide.call(
        'ritual_ZN17QQuickPaintedItem15setContentsSizeERK5QSize',
        self._valueOf(a0),
    )

  @overload(float)
  def setContentsScale(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickPaintedItem::setContentsScale(qreal a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpainteditem.html#setContentsScale

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickPaintedItem::setContentsScale(qreal a0)
    self.uglySide.call(
        'ritual_ZN17QQuickPaintedItem16setContentsScaleEd', a0,
    )

  @overload(QSize)
  def setTextureSize(self, size: QSize) -> None:
    """
    Calls Qt's 'void QQuickPaintedItem::setTextureSize(const QSize &size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpainteditem.html#setTextureSize

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QQuickPaintedItem::setTextureSize(const QSize &size)
    self.uglySide.call(
        'ritual_ZN17QQuickPaintedItem14setTextureSizeERK5QSize',
        self._valueOf(size),
    )

  @overload(QColor)
  def setFillColor(self, a0: QColor) -> None:
    """
    Calls Qt's 'void QQuickPaintedItem::setFillColor(const QColor &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpainteditem.html#setFillColor

    Parameters
    ----------

    a0 : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickPaintedItem::setFillColor(const QColor &a0)
    self.uglySide.call(
        'ritual_ZN17QQuickPaintedItem12setFillColorERK6QColor',
        self._valueOf(a0),
    )

  @overload(RenderTarget)
  def setRenderTarget(self, target: RenderTarget) -> None:
    """
    Calls Qt's 'void QQuickPaintedItem::setRenderTarget(RenderTarget
    target)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpainteditem.html#setRenderTarget

    Parameters
    ----------

    target : RenderTarget
      Passed on as its number.
    """
    #  void QQuickPaintedItem::setRenderTarget(RenderTarget target)
    self.uglySide.call(
        'ritual_ZN17QQuickPaintedItem15setRenderTargetENS_12RenderTargetE',
        target.value,
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
    'QQuickPaintedItem::QQuickPaintedItem(QQuickItem *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpainteditem.html#QQuickPaintedItem

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickPaintedItem::QQuickPaintedItem(QQuickItem *parent)
    self._noteCreation(QQuickPaintedItem, lambda: Rituals.call(
        'ritual_ZN17QQuickPaintedItemC1EP10QQuickItem',
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

  @overload()
  @overload(QRect)
  def update(self, rect: Optional[QRect] = None) -> None:
    """
    Calls Qt's 'void QQuickPaintedItem::update(const QRect &rect)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpainteditem.html#update

    Parameters
    ----------

    rect : Optional[QRect]
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
      May be left out, as in Qt: a new 'QRect()' is then passed on.
    """
    #  void QQuickPaintedItem::update(const QRect &rect)
    if rect is None:
      from ..QtCore import QRect
      rect = QRect()
    self.uglySide.call(
        'ritual_ZN17QQuickPaintedItem6updateERK5QRect', self._valueOf(rect),
    )

  def resetContentsSize(self) -> None:
    """
    Calls Qt's 'void QQuickPaintedItem::resetContentsSize()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpainteditem.html#resetContentsSize
    """
    #  void QQuickPaintedItem::resetContentsSize()
    self.uglySide.call('ritual_ZN17QQuickPaintedItem17resetContentsSizeEv')

  @overload(QPainter)
  @overload(NoneType)
  def paint(self, painter: Optional[QPainter]) -> None:
    """
    Calls Qt's 'void QQuickPaintedItem::paint(QPainter *painter)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpainteditem.html#paint

    Parameters
    ----------

    painter : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPaintedItem::paint(QPainter *painter)
    self.uglySide.call(
        'ritual_ZN17QQuickPaintedItem5paintEP8QPainter',
        self._addressOf(painter),
    )

  def fillColorChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPaintedItem::fillColorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpainteditem.html#fillColorChanged
    """
    #  void QQuickPaintedItem::fillColorChanged()
    self.uglySide.call('ritual_ZN17QQuickPaintedItem16fillColorChangedEv')

  def contentsSizeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPaintedItem::contentsSizeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpainteditem.html#contentsSizeChanged
    """
    #  void QQuickPaintedItem::contentsSizeChanged()
    self.uglySide.call('ritual_ZN17QQuickPaintedItem19contentsSizeChangedEv')

  def contentsScaleChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPaintedItem::contentsScaleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpainteditem.html#contentsScaleChanged
    """
    #  void QQuickPaintedItem::contentsScaleChanged()
    self.uglySide.call(
        'ritual_ZN17QQuickPaintedItem20contentsScaleChangedEv',
    )

  def renderTargetChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPaintedItem::renderTargetChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpainteditem.html#renderTargetChanged
    """
    #  void QQuickPaintedItem::renderTargetChanged()
    self.uglySide.call('ritual_ZN17QQuickPaintedItem19renderTargetChangedEv')

  def textureSizeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPaintedItem::textureSizeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpainteditem.html#textureSizeChanged
    """
    #  void QQuickPaintedItem::textureSizeChanged()
    self.uglySide.call('ritual_ZN17QQuickPaintedItem18textureSizeChangedEv')

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
    Calls Qt's 'QSGNode *QQuickPaintedItem::updatePaintNode(QSGNode *a0,
    UpdatePaintNodeData *a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpainteditem.html#updatePaintNode

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
    #  QSGNode *QQuickPaintedItem::updatePaintNode(QSGNode *a0,
    #      UpdatePaintNodeData *a1)
    ritual = (
        'ritual_ZN17QQuickPaintedItem15updatePaintNodeEP7QSGNodePN10QQuickI'
        'tem19UpdatePaintNodeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQuickPaintedItem15updatePaintNodeEP7QSGNodePN10Q'
          'QuickItem19UpdatePaintNodeDataE')
    address = self.uglySide.call(
        ritual, self._addressOf(a0, 'QSGNode'), self._addressOf(a1),
    )
    from . import QSGNode
    return QSGNode._cuteAt(address)

  def releaseResources(self) -> None:
    """
    Calls Qt's 'void QQuickPaintedItem::releaseResources()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpainteditem.html#releaseResources
    """
    #  void QQuickPaintedItem::releaseResources()
    ritual = 'ritual_ZN17QQuickPaintedItem16releaseResourcesEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQuickPaintedItem16releaseResourcesEv'
    self.uglySide.call(ritual)

  @overload(QQuickItem.ItemChange, QQuickItem.ItemChangeData)
  def itemChange(
      self,
      a0: QQuickItem.ItemChange,
      a1: QQuickItem.ItemChangeData,
  ) -> None:
    """
    Calls Qt's 'void QQuickPaintedItem::itemChange(ItemChange a0, const
    ItemChangeData &a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpainteditem.html#itemChange

    Parameters
    ----------

    a0 : QQuickItem.ItemChange
      Passed on as its number.

    a1 : QQuickItem.ItemChangeData
      Passed on as a value: Qt reads the C++ QQuickItem::ItemChangeData,
      which stays Python's own.
    """
    #  void QQuickPaintedItem::itemChange(ItemChange a0, const ItemChangeData
    #      &a1)
    ritual = (
        'ritual_ZN17QQuickPaintedItem10itemChangeEN10QQuickItem10ItemChange'
        'ERKNS0_14ItemChangeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQuickPaintedItem10itemChangeEN10QQuickItem10Item'
          'ChangeERKNS0_14ItemChangeDataE')
    self.uglySide.call(ritual, a0.value, self._valueOf(a1))

  def invalidateSceneGraph(self) -> None:
    """
    Calls Qt's 'void QQuickPaintedItem::invalidateSceneGraph()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpainteditem.html#invalidateSceneGraph
    """
    #  void QQuickPaintedItem::invalidateSceneGraph()
    self.uglySide.call(
        'ritual_ZN17QQuickPaintedItem20invalidateSceneGraphEv',
    )

  def d_func(self) -> Optional[QQuickPaintedItemPrivate]:
    """
    Calls Qt's 'QQuickPaintedItemPrivate *QQuickPaintedItem::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpainteditem.html#d_func

    Returns
    -------

    Optional[QQuickPaintedItemPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickPaintedItemPrivate *QQuickPaintedItem::d_func()
    address = self.uglySide.call('ritual_ZN17QQuickPaintedItem6d_funcEv')
    from . import QQuickPaintedItemPrivate
    return QQuickPaintedItemPrivate._cuteAt(address)
