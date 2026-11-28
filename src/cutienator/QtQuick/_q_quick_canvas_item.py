"""
QQuickCanvasItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickcanvasitem_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickCanvasItem to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from . import QQuickItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QEvent, QMetaObject, QRect, QRectF, QSize, QSizeF
  from ..QtCore import QUrl
  from ..QtQml import QQmlV4Function
  from . import QSGNode, QSGTextureProvider
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QQmlV4Function = WAIT['QQmlV4Function']
  QRect = WAIT['QRect']
  QRectF = WAIT['QRectF']
  QSGNode = WAIT['QSGNode']
  QSize = WAIT['QSize']
  QSizeF = WAIT['QSizeF']
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickCanvasItem(QQuickItem):
  """
  The cute side of Qt's QQuickCanvasItem: a plain Python object standing in
  front of one C++ QQuickCanvasItem.

  It is built on the cute 'QQuickItem', as Qt's QQuickCanvasItem is built on
  Qt's QQuickItem, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickCanvasItem that has a ritual and that Python
  can call so far, 35 names in all: 'metaObject', 'getContext',
  'requestAnimationFrame', 'cancelRequestAnimationFrame', 'requestPaint',
  'markDirty', 'toDataURL', 'isTextureProvider', 'textureProvider', 'paint',
  'painted', 'availableChanged', 'contextTypeChanged', 'contextChanged',
  'canvasSizeChanged', 'tileSizeChanged', 'canvasWindowChanged',
  'renderTargetChanged', 'renderStrategyChanged', 'imageLoaded', 'loadImage',
  'unloadImage', 'sceneGraphInitialized', 'checkAnimationCallbacks',
  'invalidateSceneGraph', 'schedulePolish', 'componentComplete',
  'itemChange', 'updatePolish', 'updatePaintNode', 'geometryChange',
  'releaseResources', 'event', 'delayedCreate', 'tiledRect'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickCanvasItem::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickCanvasItem::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickCanvasItemPrivate *QQuickCanvasItem::d_func()': gives
    'QQuickCanvasItemPrivate', which has no cute class yet.
  - Qt's 'const QQuickCanvasItemPrivate *QQuickCanvasItem::d_func() const':
    gives 'QQuickCanvasItemPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  29 of the 68 functions Qt declares: 25 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 2 not a gap;
  2 leans on 'QQuickCanvasItem.

  What to expect
  --------------

  - The C++ QQuickCanvasItem is created at the first use, not by
    'QQuickCanvasItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickCanvasItem.
  - Qt tells when it has removed the C++ QQuickCanvasItem. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickCanvasItem that has no cute function yet,
    '__init__', 'canvasSize', 'canvasWindow', 'context', 'contextType',
    'createContext', 'initializeContext', 'isAvailable', 'isImageError',
    'isImageLoaded', 'isImageLoading', 'isPaintConnected', 'loadedPixmap',
    'rawContext', 'renderStrategy', 'renderTarget', 'save', 'setCanvasSize',
    'setCanvasWindow', 'setContextType', 'setRenderStrategy',
    'setRenderTarget', 'setTileSize', 'tileSize', 'toImage', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QQuickCanvasItem, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class RenderStrategy(CuteNum):
    """
    The enum 'QQuickCanvasItem::RenderStrategy' of Qt, with the 3 names Qt
    gives in it.
    """

    Immediate = Kee[int](0)
    Threaded = Kee[int](1)
    Cooperative = Kee[int](2)

  class RenderTarget(CuteNum):
    """
    The enum 'QQuickCanvasItem::RenderTarget' of Qt, with the 2 names Qt
    gives in it.
    """

    Image = Kee[int](0)
    FramebufferObject = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QRectF, QSize)
  def tiledRect(window: QRectF, tileSize: QSize) -> QRect:
    """
    Calls Qt's 'QRect QQuickCanvasItem::tiledRect(const QRectF &window, const
    QSize &tileSize)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcanvasitem.html#tiledRect

    Parameters
    ----------

    window : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    tileSize : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QQuickCanvasItem::tiledRect(const QRectF &window, const QSize
    #      &tileSize)
    address = Rituals.call(
        'ritual_ZN16QQuickCanvasItem9tiledRectERK6QRectFRK5QSize',
        CuteMixin._valueOf(window), CuteMixin._valueOf(tileSize),
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickCanvasItem'

  #  A C++ QQuickCanvasItem Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickCanvasItem'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickCanvasItem::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcanvasitem.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickCanvasItem::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QQuickCanvasItem10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(str)
  def toDataURL(self, type: str) -> str:
    """
    Calls Qt's 'QString QQuickCanvasItem::toDataURL(const QString &type)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcanvasitem.html#toDataURL

    Parameters
    ----------

    type : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickCanvasItem::toDataURL(const QString &type) const
    return self.uglySide.call(
        'ritual_ZNK16QQuickCanvasItem9toDataURLERK7QString', type,
    )

  def isTextureProvider(self) -> bool:
    """
    Calls Qt's 'bool QQuickCanvasItem::isTextureProvider() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcanvasitem.html#isTextureProvider
    """
    #  bool QQuickCanvasItem::isTextureProvider() const
    ritual = 'ritual_ZNK16QQuickCanvasItem17isTextureProviderEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QQuickCanvasItem17isTextureProviderEv'
    return self.uglySide.call(ritual)

  def textureProvider(self) -> Optional[QSGTextureProvider]:
    """
    Calls Qt's 'QSGTextureProvider *QQuickCanvasItem::textureProvider()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcanvasitem.html#textureProvider

    Returns
    -------

    Optional[QSGTextureProvider]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGTextureProvider *QQuickCanvasItem::textureProvider() const
    ritual = 'ritual_ZNK16QQuickCanvasItem15textureProviderEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QQuickCanvasItem15textureProviderEv'
    address = self.uglySide.call(ritual)
    from . import QSGTextureProvider
    return QSGTextureProvider._cuteAt(address)

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QQuickCanvasItem::QQuickCanvasItem(QQuickItem *parent)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: no matching constructor for initialization of
    'QQuickItem'.
    """
    raise NotImplementedError(
        "'QQuickCanvasItem.__init__' has no cute function yet. Qt's "
        "'QQuickCanvasItem::QQuickCanvasItem(QQuickItem *parent)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: no matching constructor for "
        "initialization of 'QQuickItem'.")

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

  @overload(QQmlV4Function)
  @overload(NoneType)
  def getContext(self, args: Optional[QQmlV4Function]) -> None:
    """
    Calls Qt's 'void QQuickCanvasItem::getContext(QQmlV4FunctionPtr args)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcanvasitem.html#getContext

    Parameters
    ----------

    args : Optional[QQmlV4Function]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickCanvasItem::getContext(QQmlV4FunctionPtr args)
    self.uglySide.call(
        'ritual_ZN16QQuickCanvasItem10getContextEP14QQmlV4Function',
        self._addressOf(args),
    )

  @overload(QQmlV4Function)
  @overload(NoneType)
  def requestAnimationFrame(self, args: Optional[QQmlV4Function]) -> None:
    """
    Calls Qt's 'void
    QQuickCanvasItem::requestAnimationFrame(QQmlV4FunctionPtr args)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcanvasitem.html#requestAnimationFrame

    Parameters
    ----------

    args : Optional[QQmlV4Function]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickCanvasItem::requestAnimationFrame(QQmlV4FunctionPtr args)
    self.uglySide.call(
        'ritual_ZN16QQuickCanvasItem21requestAnimationFrameEP14QQmlV4Functi'
        'on',
        self._addressOf(args),
    )

  @overload(QQmlV4Function)
  @overload(NoneType)
  def cancelRequestAnimationFrame(
      self,
      args: Optional[QQmlV4Function],
  ) -> None:
    """
    Calls Qt's 'void
    QQuickCanvasItem::cancelRequestAnimationFrame(QQmlV4FunctionPtr args)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcanvasitem.html#cancelRequestAnimationFrame

    Parameters
    ----------

    args : Optional[QQmlV4Function]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickCanvasItem::cancelRequestAnimationFrame(QQmlV4FunctionPtr
    #      args)
    self.uglySide.call(
        'ritual_ZN16QQuickCanvasItem27cancelRequestAnimationFrameEP14QQmlV4'
        'Function',
        self._addressOf(args),
    )

  def requestPaint(self) -> None:
    """
    Calls Qt's 'void QQuickCanvasItem::requestPaint()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcanvasitem.html#requestPaint
    """
    #  void QQuickCanvasItem::requestPaint()
    self.uglySide.call('ritual_ZN16QQuickCanvasItem12requestPaintEv')

  @overload()
  @overload(QRectF)
  def markDirty(self, dirtyRect: Optional[QRectF] = None) -> None:
    """
    Calls Qt's 'void QQuickCanvasItem::markDirty(const QRectF &dirtyRect)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcanvasitem.html#markDirty

    Parameters
    ----------

    dirtyRect : Optional[QRectF]
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own. May be left out, as in Qt: a new 'QRectF()' is then passed on.
    """
    #  void QQuickCanvasItem::markDirty(const QRectF &dirtyRect)
    if dirtyRect is None:
      from ..QtCore import QRectF
      dirtyRect = QRectF()
    self.uglySide.call(
        'ritual_ZN16QQuickCanvasItem9markDirtyERK6QRectF',
        self._valueOf(dirtyRect),
    )

  @overload(QRect)
  def paint(self, region: QRect) -> None:
    """
    Calls Qt's 'void QQuickCanvasItem::paint(const QRect &region)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcanvasitem.html#paint

    Parameters
    ----------

    region : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  void QQuickCanvasItem::paint(const QRect &region)
    self.uglySide.call(
        'ritual_ZN16QQuickCanvasItem5paintERK5QRect', self._valueOf(region),
    )

  def painted(self) -> None:
    """
    Calls Qt's 'void QQuickCanvasItem::painted()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcanvasitem.html#painted
    """
    #  void QQuickCanvasItem::painted()
    self.uglySide.call('ritual_ZN16QQuickCanvasItem7paintedEv')

  def availableChanged(self) -> None:
    """
    Calls Qt's 'void QQuickCanvasItem::availableChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcanvasitem.html#availableChanged
    """
    #  void QQuickCanvasItem::availableChanged()
    self.uglySide.call('ritual_ZN16QQuickCanvasItem16availableChangedEv')

  def contextTypeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickCanvasItem::contextTypeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcanvasitem.html#contextTypeChanged
    """
    #  void QQuickCanvasItem::contextTypeChanged()
    self.uglySide.call('ritual_ZN16QQuickCanvasItem18contextTypeChangedEv')

  def contextChanged(self) -> None:
    """
    Calls Qt's 'void QQuickCanvasItem::contextChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcanvasitem.html#contextChanged
    """
    #  void QQuickCanvasItem::contextChanged()
    self.uglySide.call('ritual_ZN16QQuickCanvasItem14contextChangedEv')

  def canvasSizeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickCanvasItem::canvasSizeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcanvasitem.html#canvasSizeChanged
    """
    #  void QQuickCanvasItem::canvasSizeChanged()
    self.uglySide.call('ritual_ZN16QQuickCanvasItem17canvasSizeChangedEv')

  def tileSizeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickCanvasItem::tileSizeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcanvasitem.html#tileSizeChanged
    """
    #  void QQuickCanvasItem::tileSizeChanged()
    self.uglySide.call('ritual_ZN16QQuickCanvasItem15tileSizeChangedEv')

  def canvasWindowChanged(self) -> None:
    """
    Calls Qt's 'void QQuickCanvasItem::canvasWindowChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcanvasitem.html#canvasWindowChanged
    """
    #  void QQuickCanvasItem::canvasWindowChanged()
    self.uglySide.call('ritual_ZN16QQuickCanvasItem19canvasWindowChangedEv')

  def renderTargetChanged(self) -> None:
    """
    Calls Qt's 'void QQuickCanvasItem::renderTargetChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcanvasitem.html#renderTargetChanged
    """
    #  void QQuickCanvasItem::renderTargetChanged()
    self.uglySide.call('ritual_ZN16QQuickCanvasItem19renderTargetChangedEv')

  def renderStrategyChanged(self) -> None:
    """
    Calls Qt's 'void QQuickCanvasItem::renderStrategyChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcanvasitem.html#renderStrategyChanged
    """
    #  void QQuickCanvasItem::renderStrategyChanged()
    self.uglySide.call(
        'ritual_ZN16QQuickCanvasItem21renderStrategyChangedEv',
    )

  def imageLoaded(self) -> None:
    """
    Calls Qt's 'void QQuickCanvasItem::imageLoaded()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcanvasitem.html#imageLoaded
    """
    #  void QQuickCanvasItem::imageLoaded()
    self.uglySide.call('ritual_ZN16QQuickCanvasItem11imageLoadedEv')

  @overload(QUrl)
  @overload(QUrl, QSizeF)
  def loadImage(
      self,
      url: QUrl,
      sourceSize: Optional[QSizeF] = None,
  ) -> None:
    """
    Calls Qt's 'void QQuickCanvasItem::loadImage(const QUrl &url, QSizeF
    sourceSize)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcanvasitem.html#loadImage

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    sourceSize : Optional[QSizeF]
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own. May be left out, as in Qt: a new 'QSizeF()' is then passed on.
    """
    #  void QQuickCanvasItem::loadImage(const QUrl &url, QSizeF sourceSize)
    if sourceSize is None:
      from ..QtCore import QSizeF
      sourceSize = QSizeF()
    self.uglySide.call(
        'ritual_ZN16QQuickCanvasItem9loadImageERK4QUrl6QSizeF',
        self._valueOf(url), self._valueOf(sourceSize),
    )

  @overload(QUrl)
  def unloadImage(self, url: QUrl) -> None:
    """
    Calls Qt's 'void QQuickCanvasItem::unloadImage(const QUrl &url)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcanvasitem.html#unloadImage

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QQuickCanvasItem::unloadImage(const QUrl &url)
    self.uglySide.call(
        'ritual_ZN16QQuickCanvasItem11unloadImageERK4QUrl',
        self._valueOf(url),
    )

  def sceneGraphInitialized(self) -> None:
    """
    Calls Qt's 'void QQuickCanvasItem::sceneGraphInitialized()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcanvasitem.html#sceneGraphInitialized
    """
    #  void QQuickCanvasItem::sceneGraphInitialized()
    self.uglySide.call(
        'ritual_ZN16QQuickCanvasItem21sceneGraphInitializedEv',
    )

  def checkAnimationCallbacks(self) -> None:
    """
    Calls Qt's 'void QQuickCanvasItem::checkAnimationCallbacks()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcanvasitem.html#checkAnimationCallbacks
    """
    #  void QQuickCanvasItem::checkAnimationCallbacks()
    self.uglySide.call(
        'ritual_ZN16QQuickCanvasItem23checkAnimationCallbacksEv',
    )

  def invalidateSceneGraph(self) -> None:
    """
    Calls Qt's 'void QQuickCanvasItem::invalidateSceneGraph()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcanvasitem.html#invalidateSceneGraph
    """
    #  void QQuickCanvasItem::invalidateSceneGraph()
    self.uglySide.call('ritual_ZN16QQuickCanvasItem20invalidateSceneGraphEv')

  def schedulePolish(self) -> None:
    """
    Calls Qt's 'void QQuickCanvasItem::schedulePolish()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcanvasitem.html#schedulePolish
    """
    #  void QQuickCanvasItem::schedulePolish()
    self.uglySide.call('ritual_ZN16QQuickCanvasItem14schedulePolishEv')

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickCanvasItem::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcanvasitem.html#componentComplete
    """
    #  void QQuickCanvasItem::componentComplete()
    ritual = 'ritual_ZN16QQuickCanvasItem17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QQuickCanvasItem17componentCompleteEv'
    self.uglySide.call(ritual)

  @overload(QQuickItem.ItemChange, QQuickItem.ItemChangeData)
  def itemChange(
      self,
      a0: QQuickItem.ItemChange,
      a1: QQuickItem.ItemChangeData,
  ) -> None:
    """
    Calls Qt's 'void QQuickCanvasItem::itemChange(QQuickItem::ItemChange a0,
    const QQuickItem::ItemChangeData &a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcanvasitem.html#itemChange

    Parameters
    ----------

    a0 : QQuickItem.ItemChange
      Passed on as its number.

    a1 : QQuickItem.ItemChangeData
      Passed on as a value: Qt reads the C++ QQuickItem::ItemChangeData,
      which stays Python's own.
    """
    #  void QQuickCanvasItem::itemChange(QQuickItem::ItemChange a0, const
    #      QQuickItem::ItemChangeData &a1)
    ritual = (
        'ritual_ZN16QQuickCanvasItem10itemChangeEN10QQuickItem10ItemChangeE'
        'RKNS0_14ItemChangeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QQuickCanvasItem10itemChangeEN10QQuickItem10ItemC'
          'hangeERKNS0_14ItemChangeDataE')
    self.uglySide.call(ritual, a0.value, self._valueOf(a1))

  def updatePolish(self) -> None:
    """
    Calls Qt's 'void QQuickCanvasItem::updatePolish()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcanvasitem.html#updatePolish
    """
    #  void QQuickCanvasItem::updatePolish()
    self.uglySide.call('ritual_ZN16QQuickCanvasItem12updatePolishEv')

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
    Calls Qt's 'QSGNode *QQuickCanvasItem::updatePaintNode(QSGNode *a0,
    UpdatePaintNodeData *a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcanvasitem.html#updatePaintNode

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
    #  QSGNode *QQuickCanvasItem::updatePaintNode(QSGNode *a0,
    #      UpdatePaintNodeData *a1)
    address = self.uglySide.call(
        'ritual_ZN16QQuickCanvasItem15updatePaintNodeEP7QSGNodePN10QQuickIt'
        'em19UpdatePaintNodeDataE',
        self._addressOf(a0, 'QSGNode'), self._addressOf(a1),
    )
    from . import QSGNode
    return QSGNode._cuteAt(address)

  @overload(QRectF, QRectF)
  def geometryChange(self, newGeometry: QRectF, oldGeometry: QRectF) -> None:
    """
    Calls Qt's 'void QQuickCanvasItem::geometryChange(const QRectF
    &newGeometry, const QRectF &oldGeometry)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcanvasitem.html#geometryChange

    Parameters
    ----------

    newGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    oldGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QQuickCanvasItem::geometryChange(const QRectF &newGeometry, const
    #      QRectF &oldGeometry)
    self.uglySide.call(
        'ritual_ZN16QQuickCanvasItem14geometryChangeERK6QRectFS2_',
        self._valueOf(newGeometry), self._valueOf(oldGeometry),
    )

  def releaseResources(self) -> None:
    """
    Calls Qt's 'void QQuickCanvasItem::releaseResources()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcanvasitem.html#releaseResources
    """
    #  void QQuickCanvasItem::releaseResources()
    ritual = 'ritual_ZN16QQuickCanvasItem16releaseResourcesEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QQuickCanvasItem16releaseResourcesEv'
    self.uglySide.call(ritual)

  @overload(QEvent)
  @overload(NoneType)
  def event(self, event: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QQuickCanvasItem::event(QEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcanvasitem.html#event

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickCanvasItem::event(QEvent *event)
    ritual = 'ritual_ZN16QQuickCanvasItem5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QQuickCanvasItem5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(event))

  def delayedCreate(self) -> None:
    """
    Calls Qt's 'void QQuickCanvasItem::delayedCreate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcanvasitem.html#delayedCreate
    """
    #  void QQuickCanvasItem::delayedCreate()
    self.uglySide.call('ritual_ZN16QQuickCanvasItem13delayedCreateEv')

  @staticmethod
  def canvasSize(*__, **_) -> Never:
    """
    Qt's 'QSizeF QQuickCanvasItem::canvasSize() const': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: member access into incomplete type 'const QQuickCanvasItemPrivate'.
    """
    raise NotImplementedError(
        "'QQuickCanvasItem.canvasSize' has no cute function yet. Qt's "
        "'QSizeF QQuickCanvasItem::canvasSize() const': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: member access into incomplete type 'const "
        "QQuickCanvasItemPrivate'.")

  @staticmethod
  def canvasWindow(*__, **_) -> Never:
    """
    Qt's 'QRectF QQuickCanvasItem::canvasWindow() const': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: member access into incomplete type 'const QQuickCanvasItemPrivate'.
    """
    raise NotImplementedError(
        "'QQuickCanvasItem.canvasWindow' has no cute function yet. Qt's "
        "'QRectF QQuickCanvasItem::canvasWindow() const': Qt's library has "
        "no name for it, and its code in Qt's source does not compile apart "
        "from its file: member access into incomplete type 'const "
        "QQuickCanvasItemPrivate'.")

  @staticmethod
  def context(*__, **_) -> Never:
    """
    Qt's 'QJSValue QQuickCanvasItem::context() const': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: member access into incomplete type 'const QQuickCanvasItemPrivate'.
    """
    raise NotImplementedError(
        "'QQuickCanvasItem.context' has no cute function yet. Qt's "
        "'QJSValue QQuickCanvasItem::context() const': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: member access into incomplete type 'const "
        "QQuickCanvasItemPrivate'.")

  @staticmethod
  def contextType(*__, **_) -> Never:
    """
    Qt's 'QString QQuickCanvasItem::contextType() const': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: member access into incomplete type 'const QQuickCanvasItemPrivate'.
    """
    raise NotImplementedError(
        "'QQuickCanvasItem.contextType' has no cute function yet. Qt's "
        "'QString QQuickCanvasItem::contextType() const': Qt's library has "
        "no name for it, and its code in Qt's source does not compile apart "
        "from its file: member access into incomplete type 'const "
        "QQuickCanvasItemPrivate'.")

  @staticmethod
  def createContext(*__, **_) -> Never:
    """
    Qt's 'bool QQuickCanvasItem::createContext(const QString &contextType)':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: member access into incomplete type
    'QQuickCanvasItemPrivate'.
    """
    raise NotImplementedError(
        "'QQuickCanvasItem.createContext' has no cute function yet. Qt's "
        "'bool QQuickCanvasItem::createContext(const QString "
        "&contextType)': Qt's library has no name for it, and its code in "
        "Qt's source does not compile apart from its file: member access "
        "into incomplete type 'QQuickCanvasItemPrivate'.")

  @staticmethod
  def initializeContext(*__, **_) -> Never:
    """
    Qt's 'void QQuickCanvasItem::initializeContext(QQuickCanvasContext
    *context, const QVariantMap &args)': Qt's library has no name for it, and
    its code in Qt's source does not compile apart from its file: member
    access into incomplete type 'QQuickCanvasItemPrivate'.
    """
    raise NotImplementedError(
        "'QQuickCanvasItem.initializeContext' has no cute function yet. "
        "Qt's 'void QQuickCanvasItem::initializeContext(QQuickCanvasContext "
        "*context, const QVariantMap &args)': Qt's library has no name for "
        "it, and its code in Qt's source does not compile apart from its "
        "file: member access into incomplete type 'QQuickCanvasItemPrivate'."
    )

  @staticmethod
  def isAvailable(*__, **_) -> Never:
    """
    Qt's 'bool QQuickCanvasItem::isAvailable() const': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: member access into incomplete type 'const QQuickCanvasItemPrivate'.
    """
    raise NotImplementedError(
        "'QQuickCanvasItem.isAvailable' has no cute function yet. Qt's "
        "'bool QQuickCanvasItem::isAvailable() const': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: member access into incomplete type 'const "
        "QQuickCanvasItemPrivate'.")

  @staticmethod
  def isImageError(*__, **_) -> Never:
    """
    Qt's 'bool QQuickCanvasItem::isImageError(const QUrl &url) const': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: member access into incomplete type 'const
    QQuickCanvasItemPrivate'.
    """
    raise NotImplementedError(
        "'QQuickCanvasItem.isImageError' has no cute function yet. Qt's "
        "'bool QQuickCanvasItem::isImageError(const QUrl &url) const': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: member access into incomplete type "
        "'const QQuickCanvasItemPrivate'.")

  @staticmethod
  def isImageLoaded(*__, **_) -> Never:
    """
    Qt's 'bool QQuickCanvasItem::isImageLoaded(const QUrl &url) const': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: member access into incomplete type 'const
    QQuickCanvasItemPrivate'.
    """
    raise NotImplementedError(
        "'QQuickCanvasItem.isImageLoaded' has no cute function yet. Qt's "
        "'bool QQuickCanvasItem::isImageLoaded(const QUrl &url) const': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: member access into incomplete "
        "type 'const QQuickCanvasItemPrivate'.")

  @staticmethod
  def isImageLoading(*__, **_) -> Never:
    """
    Qt's 'bool QQuickCanvasItem::isImageLoading(const QUrl &url) const': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: member access into incomplete type 'const
    QQuickCanvasItemPrivate'.
    """
    raise NotImplementedError(
        "'QQuickCanvasItem.isImageLoading' has no cute function yet. Qt's "
        "'bool QQuickCanvasItem::isImageLoading(const QUrl &url) const': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: member access into incomplete "
        "type 'const QQuickCanvasItemPrivate'.")

  @staticmethod
  def isPaintConnected(*__, **_) -> Never:
    """
    Qt's 'bool QQuickCanvasItem::isPaintConnected()': leans on
    'QQuickCanvasItem::staticMetaObject', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickCanvasItem.isPaintConnected' has no cute function yet. Qt's "
        "'bool QQuickCanvasItem::isPaintConnected()': leans on "
        "'QQuickCanvasItem::staticMetaObject', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def loadedPixmap(*__, **_) -> Never:
    """
    Qt's 'QQmlRefPointer<QQuickCanvasPixmap>
    QQuickCanvasItem::loadedPixmap(const QUrl &url, QSizeF sourceSize)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: member access into incomplete type
    'QQuickCanvasItemPrivate'.
    """
    raise NotImplementedError(
        "'QQuickCanvasItem.loadedPixmap' has no cute function yet. Qt's "
        "'QQmlRefPointer<QQuickCanvasPixmap> "
        "QQuickCanvasItem::loadedPixmap(const QUrl &url, QSizeF "
        "sourceSize)': Qt's library has no name for it, and its code in "
        "Qt's source does not compile apart from its file: member access "
        "into incomplete type 'QQuickCanvasItemPrivate'.")

  @staticmethod
  def rawContext(*__, **_) -> Never:
    """
    Qt's 'QQuickCanvasContext *QQuickCanvasItem::rawContext() const': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: member access into incomplete type 'const
    QQuickCanvasItemPrivate'.
    """
    raise NotImplementedError(
        "'QQuickCanvasItem.rawContext' has no cute function yet. Qt's "
        "'QQuickCanvasContext *QQuickCanvasItem::rawContext() const': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: member access into incomplete type "
        "'const QQuickCanvasItemPrivate'.")

  @staticmethod
  def renderStrategy(*__, **_) -> Never:
    """
    Qt's 'RenderStrategy QQuickCanvasItem::renderStrategy() const': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: member access into incomplete type 'const
    QQuickCanvasItemPrivate'.
    """
    raise NotImplementedError(
        "'QQuickCanvasItem.renderStrategy' has no cute function yet. Qt's "
        "'RenderStrategy QQuickCanvasItem::renderStrategy() const': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: member access into incomplete type "
        "'const QQuickCanvasItemPrivate'.")

  @staticmethod
  def renderTarget(*__, **_) -> Never:
    """
    Qt's 'RenderTarget QQuickCanvasItem::renderTarget() const': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: member access into incomplete type 'const
    QQuickCanvasItemPrivate'.
    """
    raise NotImplementedError(
        "'QQuickCanvasItem.renderTarget' has no cute function yet. Qt's "
        "'RenderTarget QQuickCanvasItem::renderTarget() const': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: member access into incomplete type "
        "'const QQuickCanvasItemPrivate'.")

  @staticmethod
  def save(*__, **_) -> Never:
    """
    Qt's 'bool QQuickCanvasItem::save(const QString &filename, const QSizeF
    &imageSize) const': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: member access into
    incomplete type 'const QQuickCanvasItemPrivate'.
    """
    raise NotImplementedError(
        "'QQuickCanvasItem.save' has no cute function yet. Qt's 'bool "
        "QQuickCanvasItem::save(const QString &filename, const QSizeF "
        "&imageSize) const': Qt's library has no name for it, and its code "
        "in Qt's source does not compile apart from its file: member access "
        "into incomplete type 'const QQuickCanvasItemPrivate'.")

  @staticmethod
  def setCanvasSize(*__, **_) -> Never:
    """
    Qt's 'void QQuickCanvasItem::setCanvasSize(const QSizeF &a0)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: member access into incomplete type
    'QQuickCanvasItemPrivate'.
    """
    raise NotImplementedError(
        "'QQuickCanvasItem.setCanvasSize' has no cute function yet. Qt's "
        "'void QQuickCanvasItem::setCanvasSize(const QSizeF &a0)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: member access into incomplete type "
        "'QQuickCanvasItemPrivate'.")

  @staticmethod
  def setCanvasWindow(*__, **_) -> Never:
    """
    Qt's 'void QQuickCanvasItem::setCanvasWindow(const QRectF &rect)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: member access into incomplete type
    'QQuickCanvasItemPrivate'.
    """
    raise NotImplementedError(
        "'QQuickCanvasItem.setCanvasWindow' has no cute function yet. Qt's "
        "'void QQuickCanvasItem::setCanvasWindow(const QRectF &rect)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: member access into incomplete type "
        "'QQuickCanvasItemPrivate'.")

  @staticmethod
  def setContextType(*__, **_) -> Never:
    """
    Qt's 'void QQuickCanvasItem::setContextType(const QString &contextType)':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: member access into incomplete type
    'QQuickCanvasItemPrivate'.
    """
    raise NotImplementedError(
        "'QQuickCanvasItem.setContextType' has no cute function yet. Qt's "
        "'void QQuickCanvasItem::setContextType(const QString "
        "&contextType)': Qt's library has no name for it, and its code in "
        "Qt's source does not compile apart from its file: member access "
        "into incomplete type 'QQuickCanvasItemPrivate'.")

  @staticmethod
  def setRenderStrategy(*__, **_) -> Never:
    """
    Qt's 'void QQuickCanvasItem::setRenderStrategy(RenderStrategy strategy)':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: member access into incomplete type
    'QQuickCanvasItemPrivate'.
    """
    raise NotImplementedError(
        "'QQuickCanvasItem.setRenderStrategy' has no cute function yet. "
        "Qt's 'void QQuickCanvasItem::setRenderStrategy(RenderStrategy "
        "strategy)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: member access into "
        "incomplete type 'QQuickCanvasItemPrivate'.")

  @staticmethod
  def setRenderTarget(*__, **_) -> Never:
    """
    Qt's 'void QQuickCanvasItem::setRenderTarget(RenderTarget target)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: member access into incomplete type
    'QQuickCanvasItemPrivate'.
    """
    raise NotImplementedError(
        "'QQuickCanvasItem.setRenderTarget' has no cute function yet. Qt's "
        "'void QQuickCanvasItem::setRenderTarget(RenderTarget target)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: member access into incomplete "
        "type 'QQuickCanvasItemPrivate'.")

  @staticmethod
  def setTileSize(*__, **_) -> Never:
    """
    Qt's 'void QQuickCanvasItem::setTileSize(const QSize &a0)': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: member access into incomplete type
    'QQuickCanvasItemPrivate'.
    """
    raise NotImplementedError(
        "'QQuickCanvasItem.setTileSize' has no cute function yet. Qt's "
        "'void QQuickCanvasItem::setTileSize(const QSize &a0)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: member access into incomplete type "
        "'QQuickCanvasItemPrivate'.")

  @staticmethod
  def tileSize(*__, **_) -> Never:
    """
    Qt's 'QSize QQuickCanvasItem::tileSize() const': Qt's library has no name
    for it, and its code in Qt's source does not compile apart from its file:
    member access into incomplete type 'const QQuickCanvasItemPrivate'.
    """
    raise NotImplementedError(
        "'QQuickCanvasItem.tileSize' has no cute function yet. Qt's 'QSize "
        "QQuickCanvasItem::tileSize() const': Qt's library has no name for "
        "it, and its code in Qt's source does not compile apart from its "
        "file: member access into incomplete type 'const "
        "QQuickCanvasItemPrivate'.")

  @staticmethod
  def toImage(*__, **_) -> Never:
    """
    Qt's 'QImage QQuickCanvasItem::toImage(const QRectF &rect) const': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: member access into incomplete type 'const
    QQuickCanvasItemPrivate'.
    """
    raise NotImplementedError(
        "'QQuickCanvasItem.toImage' has no cute function yet. Qt's 'QImage "
        "QQuickCanvasItem::toImage(const QRectF &rect) const': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: member access into incomplete type 'const "
        "QQuickCanvasItemPrivate'.")
