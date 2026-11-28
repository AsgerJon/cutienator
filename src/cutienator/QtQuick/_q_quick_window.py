"""
QQuickWindow binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/qquickwindow.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObject
from ..QtGui import QWindow
from . import QSGRendererInterface

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject, QRunnable
  from ..QtGui import QAccessibleInterface, QCloseEvent, QColor, QExposeEvent
  from ..QtGui import QFocusEvent, QHideEvent, QImage, QKeyEvent, QMouseEvent
  from ..QtGui import QResizeEvent, QRhi, QRhiSwapChain, QRhiTexture, QScreen
  from ..QtGui import QShowEvent, QTabletEvent, QWheelEvent
  from ..QtQml import QQmlIncubationController
  from . import QQuickCloseEvent, QQuickGraphicsConfiguration
  from . import QQuickGraphicsDevice, QQuickItem, QQuickRenderControl
  from . import QQuickRenderTarget, QQuickWindowPrivate, QSGImageNode
  from . import QSGNinePatchNode, QSGRectangleNode, QSGTextNode, QSGTexture
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QCloseEvent = WAIT['QCloseEvent']
  QColor = WAIT['QColor']
  QEvent = WAIT['QEvent']
  QExposeEvent = WAIT['QExposeEvent']
  QFocusEvent = WAIT['QFocusEvent']
  QHideEvent = WAIT['QHideEvent']
  QImage = WAIT['QImage']
  QKeyEvent = WAIT['QKeyEvent']
  QMouseEvent = WAIT['QMouseEvent']
  QQuickCloseEvent = WAIT['QQuickCloseEvent']
  QQuickGraphicsConfiguration = WAIT['QQuickGraphicsConfiguration']
  QQuickGraphicsDevice = WAIT['QQuickGraphicsDevice']
  QQuickRenderControl = WAIT['QQuickRenderControl']
  QQuickRenderTarget = WAIT['QQuickRenderTarget']
  QResizeEvent = WAIT['QResizeEvent']
  QRhiTexture = WAIT['QRhiTexture']
  QRunnable = WAIT['QRunnable']
  QScreen = WAIT['QScreen']
  QShowEvent = WAIT['QShowEvent']
  QTabletEvent = WAIT['QTabletEvent']
  QWheelEvent = WAIT['QWheelEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickWindow(QWindow):
  """
  The cute side of Qt's QQuickWindow: a plain Python object standing in front
  of one C++ QQuickWindow.

  It is built on the cute 'QWindow', as Qt's QQuickWindow is built on Qt's
  QWindow, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickWindow that has a ritual and that Python can
  call so far, 90 names in all: 'metaObject', 'tr', 'd_func', 'contentItem',
  'activeFocusItem', 'focusObject', 'mouseGrabberItem', 'grabWindow',
  'setRenderTarget', 'renderTarget', 'graphicsStateInfo',
  'beginExternalCommands', 'endExternalCommands', 'incubationController',
  'accessibleRoot', 'createTextureFromImage', 'createTextureFromRhiTexture',
  'setColor', 'color', 'hasDefaultAlphaBuffer', 'setDefaultAlphaBuffer',
  'setPersistentGraphics', 'isPersistentGraphics', 'setPersistentSceneGraph',
  'isPersistentSceneGraph', 'isSceneGraphInitialized', 'scheduleRenderJob',
  'effectiveDevicePixelRatio', 'rendererInterface', 'setGraphicsApi',
  'graphicsApi', 'setSceneGraphBackend', 'sceneGraphBackend',
  'setGraphicsDevice', 'graphicsDevice', 'setGraphicsConfiguration',
  'graphicsConfiguration', 'createRectangleNode', 'createImageNode',
  'createNinePatchNode', 'createTextNode', 'textRenderType',
  'setTextRenderType', 'rhi', 'swapChain', 'frameSwapped',
  'sceneGraphInitialized', 'sceneGraphInvalidated', 'beforeSynchronizing',
  'afterSynchronizing', 'beforeRendering', 'afterRendering',
  'afterAnimating', 'sceneGraphAboutToStop', 'closing', 'colorChanged',
  'activeFocusItemChanged', 'sceneGraphError', 'beforeRenderPassRecording',
  'afterRenderPassRecording', 'paletteChanged', 'paletteCreated',
  'beforeFrameBegin', 'afterFrameEnd', 'devicePixelRatioChanged', 'update',
  'releaseResources', 'exposeEvent', 'resizeEvent', 'showEvent', 'hideEvent',
  'closeEvent', 'focusInEvent', 'focusOutEvent', 'event', 'keyPressEvent',
  'keyReleaseEvent', 'mousePressEvent', 'mouseReleaseEvent',
  'mouseDoubleClickEvent', 'mouseMoveEvent', 'wheelEvent', 'tabletEvent',
  'maybeUpdate', 'cleanupSceneGraph', 'physicalDpiChanged',
  'handleScreenChanged', 'runJobsAfterSwap', 'handleApplicationStateChanged',
  'handleFontDatabaseChanged'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickWindow::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQuickWindow::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'const QQuickWindowPrivate *QQuickWindow::d_func() const': takes in
    Python what 'QQuickWindowPrivate *QQuickWindow::d_func()' takes.
  - Qt's 'QQuickWindow::~QQuickWindow()': the destructor: Python never
    removes a C++ QQuickWindow.
  - Qt's 'QQuickWindow::QQuickWindow(QQuickWindowPrivate &dd, QWindow
    *parent)': takes a type Python has no way to hand over yet.
  - Qt's 'QQuickWindow::QQuickWindow(QQuickWindowPrivate &dd,
    QQuickRenderControl *control)': takes a type Python has no way to hand
    over yet.
  - Qt's 'QQmlInfo operator<<(QQmlInfo info, const QQuickWindow *window)': an
    operator between other classes, written inside this one.

  What has no ritual
  ------------------

  4 of the 104 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickWindow is created at the first use, not by
    'QQuickWindow(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickWindow.
  - Qt tells when it has removed the C++ QQuickWindow. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  #  The enums Qt writes inside QQuickWindow, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class CreateTextureOption(CuteFlags):
    """
    The flags enum 'QQuickWindow::CreateTextureOption' of Qt, with the 5
    names Qt gives in it. Qt names the type of its combinations
    'QQuickWindow::CreateTextureOptions'.
    """

    TextureHasAlphaChannel = 0x1
    TextureHasMipmaps = 0x2
    TextureOwnsGLTexture = 0x4
    TextureCanUseAtlas = 0x8
    TextureIsOpaque = 0x10

  CreateTextureOptions = CreateTextureOption

  class RenderStage(CuteNum):
    """
    The enum 'QQuickWindow::RenderStage' of Qt, with the 6 names Qt gives in
    it.
    """

    BeforeSynchronizingStage = Kee[int](0)
    AfterSynchronizingStage = Kee[int](1)
    BeforeRenderingStage = Kee[int](2)
    AfterRenderingStage = Kee[int](3)
    AfterSwapStage = Kee[int](4)
    NoStage = Kee[int](5)

  class SceneGraphError(CuteNum):
    """
    The enum 'QQuickWindow::SceneGraphError' of Qt, with the 1 names Qt gives
    in it.
    """

    ContextNotAvailable = Kee[int](1)

  class TextRenderType(CuteNum):
    """
    The enum 'QQuickWindow::TextRenderType' of Qt, with the 3 names Qt gives
    in it.
    """

    QtTextRendering = Kee[int](0)
    NativeTextRendering = Kee[int](1)
    CurveTextRendering = Kee[int](2)

  #  The classes Qt writes inside QQuickWindow, each a class in here as in
  #  C++.

  class GraphicsStateInfo(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQuickWindow::GraphicsStateInfo: a plain Python
    object standing in front of one C++ QQuickWindow::GraphicsStateInfo.

    C++ hands a QQuickWindow::GraphicsStateInfo around as a copy, so every
    C++ QQuickWindow::GraphicsStateInfo behind a cute one is Python's own: it
    is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    No function of Qt's QQuickWindow::GraphicsStateInfo yet. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQuickWindow::GraphicsStateInfo::~GraphicsStateInfo()': the
      destructor: Python removes its C++ QQuickWindow::GraphicsStateInfo by
      it, and has no other use for it.

    What to expect
    --------------

    - The C++ QQuickWindow::GraphicsStateInfo is created at the first use,
      not by 'QQuickWindow::GraphicsStateInfo(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQuickWindow::GraphicsStateInfo back gives a copy
      the ritual made for Python, in a new cute
      QQuickWindow::GraphicsStateInfo.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQuickWindow::GraphicsStateInfo'

    #  Qt's '~QQuickWindow::GraphicsStateInfo()'. Naming it makes this a
    #  value class: Python owns every C++ QQuickWindow::GraphicsStateInfo
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN12QQuickWindow17GraphicsStateInfoD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
    Calls Qt's 'QString QQuickWindow::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwindow.html#tr

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
    #  QString QQuickWindow::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN12QQuickWindow2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def hasDefaultAlphaBuffer() -> bool:
    """
    Calls Qt's 'bool QQuickWindow::hasDefaultAlphaBuffer()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindow.html#hasDefaultAlphaBuffer
    """
    #  bool QQuickWindow::hasDefaultAlphaBuffer()
    return Rituals.call('ritual_ZN12QQuickWindow21hasDefaultAlphaBufferEv')

  @staticmethod
  @overload(bool)
  def setDefaultAlphaBuffer(useAlpha: bool) -> None:
    """
    Calls Qt's 'void QQuickWindow::setDefaultAlphaBuffer(bool useAlpha)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindow.html#setDefaultAlphaBuffer

    Parameters
    ----------

    useAlpha : bool
      Passed on as it is.
    """
    #  void QQuickWindow::setDefaultAlphaBuffer(bool useAlpha)
    Rituals.call(
        'ritual_ZN12QQuickWindow21setDefaultAlphaBufferEb', useAlpha,
    )

  @staticmethod
  @overload(QSGRendererInterface.GraphicsApi)
  def setGraphicsApi(api: QSGRendererInterface.GraphicsApi) -> None:
    """
    Calls Qt's 'void
    QQuickWindow::setGraphicsApi(QSGRendererInterface::GraphicsApi api)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwindow.html#setGraphicsApi

    Parameters
    ----------

    api : QSGRendererInterface.GraphicsApi
      Passed on as its number.
    """
    #  void QQuickWindow::setGraphicsApi(QSGRendererInterface::GraphicsApi
    #      api)
    Rituals.call(
        'ritual_ZN12QQuickWindow14setGraphicsApiEN20QSGRendererInterface11G'
        'raphicsApiE',
        api.value,
    )

  @staticmethod
  def graphicsApi() -> QSGRendererInterface.GraphicsApi:
    """
    Calls Qt's 'QSGRendererInterface::GraphicsApi
    QQuickWindow::graphicsApi()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwindow.html#graphicsApi

    Returns
    -------

    QSGRendererInterface.GraphicsApi
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QSGRendererInterface.GraphicsApi(number)' gives.
    """
    #  QSGRendererInterface::GraphicsApi QQuickWindow::graphicsApi()
    return QSGRendererInterface.GraphicsApi(Rituals.call(
        'ritual_ZN12QQuickWindow11graphicsApiEv',
    ))

  @staticmethod
  @overload(str)
  def setSceneGraphBackend(backend: str) -> None:
    """
    Calls Qt's 'void QQuickWindow::setSceneGraphBackend(const QString
    &backend)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindow.html#setSceneGraphBackend

    Parameters
    ----------

    backend : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickWindow::setSceneGraphBackend(const QString &backend)
    Rituals.call(
        'ritual_ZN12QQuickWindow20setSceneGraphBackendERK7QString', backend,
    )

  @staticmethod
  def sceneGraphBackend() -> str:
    """
    Calls Qt's 'QString QQuickWindow::sceneGraphBackend()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindow.html#sceneGraphBackend

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickWindow::sceneGraphBackend()
    return Rituals.call('ritual_ZN12QQuickWindow17sceneGraphBackendEv')

  @staticmethod
  def textRenderType() -> TextRenderType:
    """
    Calls Qt's 'TextRenderType QQuickWindow::textRenderType()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwindow.html#textRenderType

    Returns
    -------

    TextRenderType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'TextRenderType(number)'
      gives.
    """
    #  TextRenderType QQuickWindow::textRenderType()
    return QQuickWindow.TextRenderType(Rituals.call(
        'ritual_ZN12QQuickWindow14textRenderTypeEv',
    ))

  @staticmethod
  @overload(TextRenderType)
  def setTextRenderType(renderType: TextRenderType) -> None:
    """
    Calls Qt's 'void QQuickWindow::setTextRenderType(TextRenderType
    renderType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindow.html#setTextRenderType

    Parameters
    ----------

    renderType : TextRenderType
      Passed on as its number.
    """
    #  void QQuickWindow::setTextRenderType(TextRenderType renderType)
    Rituals.call(
        'ritual_ZN12QQuickWindow17setTextRenderTypeENS_14TextRenderTypeE',
        renderType.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickWindow'

  #  A C++ QQuickWindow Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickWindow'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickWindow::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwindow.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickWindow::metaObject() const
    address = self.uglySide.call('ritual_ZNK12QQuickWindow10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def contentItem(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickWindow::contentItem() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwindow.html#contentItem

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickWindow::contentItem() const
    address = self.uglySide.call('ritual_ZNK12QQuickWindow11contentItemEv')
    from . import QQuickItem
    return QQuickItem._cuteAt(address)

  def activeFocusItem(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickWindow::activeFocusItem() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwindow.html#activeFocusItem

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickWindow::activeFocusItem() const
    address = self.uglySide.call(
        'ritual_ZNK12QQuickWindow15activeFocusItemEv',
    )
    from . import QQuickItem
    return QQuickItem._cuteAt(address)

  def focusObject(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QQuickWindow::focusObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwindow.html#focusObject

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QQuickWindow::focusObject() const
    ritual = 'ritual_ZNK12QQuickWindow11focusObjectEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK12QQuickWindow11focusObjectEv'
    address = self.uglySide.call(ritual)
    return QObject._cuteAt(address)

  def mouseGrabberItem(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickWindow::mouseGrabberItem() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwindow.html#mouseGrabberItem

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickWindow::mouseGrabberItem() const
    address = self.uglySide.call(
        'ritual_ZNK12QQuickWindow16mouseGrabberItemEv',
    )
    from . import QQuickItem
    return QQuickItem._cuteAt(address)

  def renderTarget(self) -> QQuickRenderTarget:
    """
    Calls Qt's 'QQuickRenderTarget QQuickWindow::renderTarget() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwindow.html#renderTarget

    Returns
    -------

    QQuickRenderTarget
      A new cute QQuickRenderTarget around the copy Qt gave back. Python owns
      it.
    """
    #  QQuickRenderTarget QQuickWindow::renderTarget() const
    address = self.uglySide.call('ritual_ZNK12QQuickWindow12renderTargetEv')
    from . import QQuickRenderTarget
    return QQuickRenderTarget._cuteOwning(address)

  def incubationController(self) -> Optional[QQmlIncubationController]:
    """
    Calls Qt's 'QQmlIncubationController
    *QQuickWindow::incubationController() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindow.html#incubationController

    Returns
    -------

    Optional[QQmlIncubationController]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlIncubationController *QQuickWindow::incubationController() const
    address = self.uglySide.call(
        'ritual_ZNK12QQuickWindow20incubationControllerEv',
    )
    from ..QtQml import QQmlIncubationController
    return QQmlIncubationController._cuteAt(address)

  def accessibleRoot(self) -> Optional[QAccessibleInterface]:
    """
    Calls Qt's 'QAccessibleInterface *QQuickWindow::accessibleRoot() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwindow.html#accessibleRoot

    Returns
    -------

    Optional[QAccessibleInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAccessibleInterface *QQuickWindow::accessibleRoot() const
    ritual = 'ritual_ZNK12QQuickWindow14accessibleRootEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK12QQuickWindow14accessibleRootEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QAccessibleInterface
    return QAccessibleInterface._cuteAt(address)

  @overload(QImage)
  def createTextureFromImage(self, image: QImage) -> Optional[QSGTexture]:
    """
    Calls Qt's 'QSGTexture *QQuickWindow::createTextureFromImage(const QImage
    &image) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindow.html#createTextureFromImage

    Parameters
    ----------

    image : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.

    Returns
    -------

    Optional[QSGTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGTexture *QQuickWindow::createTextureFromImage(const QImage &image)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK12QQuickWindow22createTextureFromImageERK6QImage',
        self._valueOf(image),
    )
    from . import QSGTexture
    return QSGTexture._cuteAt(address)

  @overload(QImage, CreateTextureOptions)
  def createTextureFromImage(
      self,
      image: QImage,
      options: CreateTextureOptions,
  ) -> Optional[QSGTexture]:
    """
    Calls Qt's 'QSGTexture *QQuickWindow::createTextureFromImage(const QImage
    &image, CreateTextureOptions options) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindow.html#createTextureFromImage

    Parameters
    ----------

    image : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.

    options : CreateTextureOptions
      Passed on as its number.

    Returns
    -------

    Optional[QSGTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGTexture *QQuickWindow::createTextureFromImage(const QImage &image,
    #      CreateTextureOptions options) const
    address = self.uglySide.call(
        'ritual_ZNK12QQuickWindow22createTextureFromImageERK6QImage6QFlagsI'
        'NS_19CreateTextureOptionEE',
        self._valueOf(image), options.value,
    )
    from . import QSGTexture
    return QSGTexture._cuteAt(address)

  @overload(QRhiTexture)
  @overload(NoneType)
  @overload(QRhiTexture, CreateTextureOptions)
  @overload(NoneType, CreateTextureOptions)
  def createTextureFromRhiTexture(
      self,
      texture: Optional[QRhiTexture],
      options: CreateTextureOptions = CreateTextureOptions(),
  ) -> Optional[QSGTexture]:
    """
    Calls Qt's 'QSGTexture
    *QQuickWindow::createTextureFromRhiTexture(QRhiTexture *texture,
    CreateTextureOptions options) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindow.html#createTextureFromRhiTexture

    Parameters
    ----------

    texture : Optional[QRhiTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    options : CreateTextureOptions
      Passed on as its number. May be left out, as in Qt: it is then
      CreateTextureOptions().

    Returns
    -------

    Optional[QSGTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGTexture *QQuickWindow::createTextureFromRhiTexture(QRhiTexture
    #      *texture, CreateTextureOptions options) const
    address = self.uglySide.call(
        'ritual_ZNK12QQuickWindow27createTextureFromRhiTextureEP11QRhiTextu'
        're6QFlagsINS_19CreateTextureOptionEE',
        self._addressOf(texture), options.value,
    )
    from . import QSGTexture
    return QSGTexture._cuteAt(address)

  def color(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickWindow::color() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwindow.html#color

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickWindow::color() const
    address = self.uglySide.call('ritual_ZNK12QQuickWindow5colorEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def isPersistentGraphics(self) -> bool:
    """
    Calls Qt's 'bool QQuickWindow::isPersistentGraphics() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindow.html#isPersistentGraphics
    """
    #  bool QQuickWindow::isPersistentGraphics() const
    return self.uglySide.call(
        'ritual_ZNK12QQuickWindow20isPersistentGraphicsEv',
    )

  def isPersistentSceneGraph(self) -> bool:
    """
    Calls Qt's 'bool QQuickWindow::isPersistentSceneGraph() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindow.html#isPersistentSceneGraph
    """
    #  bool QQuickWindow::isPersistentSceneGraph() const
    return self.uglySide.call(
        'ritual_ZNK12QQuickWindow22isPersistentSceneGraphEv',
    )

  def isSceneGraphInitialized(self) -> bool:
    """
    Calls Qt's 'bool QQuickWindow::isSceneGraphInitialized() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindow.html#isSceneGraphInitialized
    """
    #  bool QQuickWindow::isSceneGraphInitialized() const
    return self.uglySide.call(
        'ritual_ZNK12QQuickWindow23isSceneGraphInitializedEv',
    )

  def effectiveDevicePixelRatio(self) -> float:
    """
    Calls Qt's 'qreal QQuickWindow::effectiveDevicePixelRatio() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindow.html#effectiveDevicePixelRatio
    """
    #  qreal QQuickWindow::effectiveDevicePixelRatio() const
    return self.uglySide.call(
        'ritual_ZNK12QQuickWindow25effectiveDevicePixelRatioEv',
    )

  def rendererInterface(self) -> Optional[QSGRendererInterface]:
    """
    Calls Qt's 'QSGRendererInterface *QQuickWindow::rendererInterface()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindow.html#rendererInterface

    Returns
    -------

    Optional[QSGRendererInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGRendererInterface *QQuickWindow::rendererInterface() const
    address = self.uglySide.call(
        'ritual_ZNK12QQuickWindow17rendererInterfaceEv',
    )
    return QSGRendererInterface._cuteAt(address)

  def graphicsDevice(self) -> QQuickGraphicsDevice:
    """
    Calls Qt's 'QQuickGraphicsDevice QQuickWindow::graphicsDevice() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwindow.html#graphicsDevice

    Returns
    -------

    QQuickGraphicsDevice
      A new cute QQuickGraphicsDevice around the copy Qt gave back. Python
      owns it.
    """
    #  QQuickGraphicsDevice QQuickWindow::graphicsDevice() const
    address = self.uglySide.call(
        'ritual_ZNK12QQuickWindow14graphicsDeviceEv',
    )
    from . import QQuickGraphicsDevice
    return QQuickGraphicsDevice._cuteOwning(address)

  def graphicsConfiguration(self) -> QQuickGraphicsConfiguration:
    """
    Calls Qt's 'QQuickGraphicsConfiguration
    QQuickWindow::graphicsConfiguration() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindow.html#graphicsConfiguration

    Returns
    -------

    QQuickGraphicsConfiguration
      A new cute QQuickGraphicsConfiguration around the copy Qt gave back.
      Python owns it.
    """
    #  QQuickGraphicsConfiguration QQuickWindow::graphicsConfiguration()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK12QQuickWindow21graphicsConfigurationEv',
    )
    from . import QQuickGraphicsConfiguration
    return QQuickGraphicsConfiguration._cuteOwning(address)

  def createRectangleNode(self) -> Optional[QSGRectangleNode]:
    """
    Calls Qt's 'QSGRectangleNode *QQuickWindow::createRectangleNode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindow.html#createRectangleNode

    Returns
    -------

    Optional[QSGRectangleNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGRectangleNode *QQuickWindow::createRectangleNode() const
    address = self.uglySide.call(
        'ritual_ZNK12QQuickWindow19createRectangleNodeEv',
    )
    from . import QSGRectangleNode
    return QSGRectangleNode._cuteAt(address)

  def createImageNode(self) -> Optional[QSGImageNode]:
    """
    Calls Qt's 'QSGImageNode *QQuickWindow::createImageNode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwindow.html#createImageNode

    Returns
    -------

    Optional[QSGImageNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGImageNode *QQuickWindow::createImageNode() const
    address = self.uglySide.call(
        'ritual_ZNK12QQuickWindow15createImageNodeEv',
    )
    from . import QSGImageNode
    return QSGImageNode._cuteAt(address)

  def createNinePatchNode(self) -> Optional[QSGNinePatchNode]:
    """
    Calls Qt's 'QSGNinePatchNode *QQuickWindow::createNinePatchNode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindow.html#createNinePatchNode

    Returns
    -------

    Optional[QSGNinePatchNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGNinePatchNode *QQuickWindow::createNinePatchNode() const
    address = self.uglySide.call(
        'ritual_ZNK12QQuickWindow19createNinePatchNodeEv',
    )
    from . import QSGNinePatchNode
    return QSGNinePatchNode._cuteAt(address)

  def createTextNode(self) -> Optional[QSGTextNode]:
    """
    Calls Qt's 'QSGTextNode *QQuickWindow::createTextNode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwindow.html#createTextNode

    Returns
    -------

    Optional[QSGTextNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGTextNode *QQuickWindow::createTextNode() const
    address = self.uglySide.call(
        'ritual_ZNK12QQuickWindow14createTextNodeEv',
    )
    from . import QSGTextNode
    return QSGTextNode._cuteAt(address)

  def rhi(self) -> Optional[QRhi]:
    """
    Calls Qt's 'QRhi *QQuickWindow::rhi() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwindow.html#rhi

    Returns
    -------

    Optional[QRhi]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhi *QQuickWindow::rhi() const
    address = self.uglySide.call('ritual_ZNK12QQuickWindow3rhiEv')
    from ..QtGui import QRhi
    return QRhi._cuteAt(address)

  def swapChain(self) -> Optional[QRhiSwapChain]:
    """
    Calls Qt's 'QRhiSwapChain *QQuickWindow::swapChain() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwindow.html#swapChain

    Returns
    -------

    Optional[QRhiSwapChain]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiSwapChain *QQuickWindow::swapChain() const
    address = self.uglySide.call('ritual_ZNK12QQuickWindow9swapChainEv')
    from ..QtGui import QRhiSwapChain
    return QRhiSwapChain._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuickRenderTarget)
  def setRenderTarget(self, target: QQuickRenderTarget) -> None:
    """
    Calls Qt's 'void QQuickWindow::setRenderTarget(const QQuickRenderTarget
    &target)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwindow.html#setRenderTarget

    Parameters
    ----------

    target : QQuickRenderTarget
      Passed on as a value: Qt reads the C++ QQuickRenderTarget, which stays
      Python's own.
    """
    #  void QQuickWindow::setRenderTarget(const QQuickRenderTarget &target)
    self.uglySide.call(
        'ritual_ZN12QQuickWindow15setRenderTargetERK18QQuickRenderTarget',
        self._valueOf(target),
    )

  @overload(QColor)
  def setColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QQuickWindow::setColor(const QColor &color)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwindow.html#setColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickWindow::setColor(const QColor &color)
    self.uglySide.call(
        'ritual_ZN12QQuickWindow8setColorERK6QColor', self._valueOf(color),
    )

  @overload(bool)
  def setPersistentGraphics(self, persistent: bool) -> None:
    """
    Calls Qt's 'void QQuickWindow::setPersistentGraphics(bool persistent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindow.html#setPersistentGraphics

    Parameters
    ----------

    persistent : bool
      Passed on as it is.
    """
    #  void QQuickWindow::setPersistentGraphics(bool persistent)
    self.uglySide.call(
        'ritual_ZN12QQuickWindow21setPersistentGraphicsEb', persistent,
    )

  @overload(bool)
  def setPersistentSceneGraph(self, persistent: bool) -> None:
    """
    Calls Qt's 'void QQuickWindow::setPersistentSceneGraph(bool persistent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindow.html#setPersistentSceneGraph

    Parameters
    ----------

    persistent : bool
      Passed on as it is.
    """
    #  void QQuickWindow::setPersistentSceneGraph(bool persistent)
    self.uglySide.call(
        'ritual_ZN12QQuickWindow23setPersistentSceneGraphEb', persistent,
    )

  @overload(QQuickGraphicsDevice)
  def setGraphicsDevice(self, device: QQuickGraphicsDevice) -> None:
    """
    Calls Qt's 'void QQuickWindow::setGraphicsDevice(const
    QQuickGraphicsDevice &device)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindow.html#setGraphicsDevice

    Parameters
    ----------

    device : QQuickGraphicsDevice
      Passed on as a value: Qt reads the C++ QQuickGraphicsDevice, which
      stays Python's own.
    """
    #  void QQuickWindow::setGraphicsDevice(const QQuickGraphicsDevice
    #      &device)
    self.uglySide.call(
        'ritual_ZN12QQuickWindow17setGraphicsDeviceERK20QQuickGraphicsDevic'
        'e',
        self._valueOf(device),
    )

  @overload(QQuickGraphicsConfiguration)
  def setGraphicsConfiguration(
      self,
      config: QQuickGraphicsConfiguration,
  ) -> None:
    """
    Calls Qt's 'void QQuickWindow::setGraphicsConfiguration(const
    QQuickGraphicsConfiguration &config)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindow.html#setGraphicsConfiguration

    Parameters
    ----------

    config : QQuickGraphicsConfiguration
      Passed on as a value: Qt reads the C++ QQuickGraphicsConfiguration,
      which stays Python's own.
    """
    #  void QQuickWindow::setGraphicsConfiguration(const
    #      QQuickGraphicsConfiguration &config)
    self.uglySide.call(
        'ritual_ZN12QQuickWindow24setGraphicsConfigurationERK27QQuickGraphi'
        'csConfiguration',
        self._valueOf(config),
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
  @overload(QWindow)
  @overload(NoneType)
  def __init__(self, parent: Optional[QWindow] = None) -> None:
    """
    Notes what was given, for Qt's 'QQuickWindow::QQuickWindow(QWindow
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qquickwindow.html#QQuickWindow

    Parameters
    ----------

    parent : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickWindow::QQuickWindow(QWindow *parent)
    self._noteCreation(QQuickWindow, lambda: Rituals.call(
        'ritual_ZN12QQuickWindowC1EP7QWindow', self._addressOf(parent),
    ))

  @overload(QQuickRenderControl)
  def __init__(self, renderControl: Optional[QQuickRenderControl]) -> None:
    """
    Notes what was given, for Qt's
    'QQuickWindow::QQuickWindow(QQuickRenderControl *renderControl)', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qquickwindow.html#QQuickWindow

    Parameters
    ----------

    renderControl : Optional[QQuickRenderControl]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQuickWindow::QQuickWindow(QQuickRenderControl *renderControl)
    self._noteCreation(QQuickWindow, lambda: Rituals.call(
        'ritual_ZN12QQuickWindowC1EP19QQuickRenderControl',
        self._addressOf(renderControl),
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

  def d_func(self) -> Optional[QQuickWindowPrivate]:
    """
    Calls Qt's 'QQuickWindowPrivate *QQuickWindow::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwindow.html#d_func

    Returns
    -------

    Optional[QQuickWindowPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickWindowPrivate *QQuickWindow::d_func()
    address = self.uglySide.call('ritual_ZN12QQuickWindow6d_funcEv')
    from . import QQuickWindowPrivate
    return QQuickWindowPrivate._cuteAt(address)

  def grabWindow(self) -> QImage:
    """
    Calls Qt's 'QImage QQuickWindow::grabWindow()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwindow.html#grabWindow

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QQuickWindow::grabWindow()
    address = self.uglySide.call('ritual_ZN12QQuickWindow10grabWindowEv')
    from ..QtGui import QImage
    return QImage._cuteOwning(address)

  def graphicsStateInfo(self) -> GraphicsStateInfo:
    """
    Calls Qt's 'const GraphicsStateInfo &QQuickWindow::graphicsStateInfo()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindow.html#graphicsStateInfo

    Returns
    -------

    GraphicsStateInfo
      A new cute QQuickWindow::GraphicsStateInfo around the copy Qt gave
      back. Python owns it.
    """
    #  const GraphicsStateInfo &QQuickWindow::graphicsStateInfo()
    address = self.uglySide.call(
        'ritual_ZN12QQuickWindow17graphicsStateInfoEv',
    )
    return QQuickWindow.GraphicsStateInfo._cuteOwning(address)

  def beginExternalCommands(self) -> None:
    """
    Calls Qt's 'void QQuickWindow::beginExternalCommands()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindow.html#beginExternalCommands
    """
    #  void QQuickWindow::beginExternalCommands()
    self.uglySide.call('ritual_ZN12QQuickWindow21beginExternalCommandsEv')

  def endExternalCommands(self) -> None:
    """
    Calls Qt's 'void QQuickWindow::endExternalCommands()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindow.html#endExternalCommands
    """
    #  void QQuickWindow::endExternalCommands()
    self.uglySide.call('ritual_ZN12QQuickWindow19endExternalCommandsEv')

  @overload(QRunnable, RenderStage)
  @overload(NoneType, RenderStage)
  def scheduleRenderJob(
      self,
      job: Optional[QRunnable],
      schedule: RenderStage,
  ) -> None:
    """
    Calls Qt's 'void QQuickWindow::scheduleRenderJob(QRunnable *job,
    RenderStage schedule)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindow.html#scheduleRenderJob

    Parameters
    ----------

    job : Optional[QRunnable]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    schedule : RenderStage
      Passed on as its number.
    """
    #  void QQuickWindow::scheduleRenderJob(QRunnable *job, RenderStage
    #      schedule)
    self.uglySide.call(
        'ritual_ZN12QQuickWindow17scheduleRenderJobEP9QRunnableNS_11RenderS'
        'tageE',
        self._addressOf(job, 'QRunnable'), schedule.value,
    )

  def frameSwapped(self) -> None:
    """
    Calls Qt's 'void QQuickWindow::frameSwapped()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwindow.html#frameSwapped
    """
    #  void QQuickWindow::frameSwapped()
    self.uglySide.call('ritual_ZN12QQuickWindow12frameSwappedEv')

  def sceneGraphInitialized(self) -> None:
    """
    Calls Qt's 'void QQuickWindow::sceneGraphInitialized()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindow.html#sceneGraphInitialized
    """
    #  void QQuickWindow::sceneGraphInitialized()
    self.uglySide.call('ritual_ZN12QQuickWindow21sceneGraphInitializedEv')

  def sceneGraphInvalidated(self) -> None:
    """
    Calls Qt's 'void QQuickWindow::sceneGraphInvalidated()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindow.html#sceneGraphInvalidated
    """
    #  void QQuickWindow::sceneGraphInvalidated()
    self.uglySide.call('ritual_ZN12QQuickWindow21sceneGraphInvalidatedEv')

  def beforeSynchronizing(self) -> None:
    """
    Calls Qt's 'void QQuickWindow::beforeSynchronizing()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindow.html#beforeSynchronizing
    """
    #  void QQuickWindow::beforeSynchronizing()
    self.uglySide.call('ritual_ZN12QQuickWindow19beforeSynchronizingEv')

  def afterSynchronizing(self) -> None:
    """
    Calls Qt's 'void QQuickWindow::afterSynchronizing()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindow.html#afterSynchronizing
    """
    #  void QQuickWindow::afterSynchronizing()
    self.uglySide.call('ritual_ZN12QQuickWindow18afterSynchronizingEv')

  def beforeRendering(self) -> None:
    """
    Calls Qt's 'void QQuickWindow::beforeRendering()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwindow.html#beforeRendering
    """
    #  void QQuickWindow::beforeRendering()
    self.uglySide.call('ritual_ZN12QQuickWindow15beforeRenderingEv')

  def afterRendering(self) -> None:
    """
    Calls Qt's 'void QQuickWindow::afterRendering()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwindow.html#afterRendering
    """
    #  void QQuickWindow::afterRendering()
    self.uglySide.call('ritual_ZN12QQuickWindow14afterRenderingEv')

  def afterAnimating(self) -> None:
    """
    Calls Qt's 'void QQuickWindow::afterAnimating()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwindow.html#afterAnimating
    """
    #  void QQuickWindow::afterAnimating()
    self.uglySide.call('ritual_ZN12QQuickWindow14afterAnimatingEv')

  def sceneGraphAboutToStop(self) -> None:
    """
    Calls Qt's 'void QQuickWindow::sceneGraphAboutToStop()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindow.html#sceneGraphAboutToStop
    """
    #  void QQuickWindow::sceneGraphAboutToStop()
    self.uglySide.call('ritual_ZN12QQuickWindow21sceneGraphAboutToStopEv')

  @overload(QQuickCloseEvent)
  @overload(NoneType)
  def closing(self, close: Optional[QQuickCloseEvent]) -> None:
    """
    Calls Qt's 'void QQuickWindow::closing(QQuickCloseEvent *close)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwindow.html#closing

    Parameters
    ----------

    close : Optional[QQuickCloseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickWindow::closing(QQuickCloseEvent *close)
    self.uglySide.call(
        'ritual_ZN12QQuickWindow7closingEP16QQuickCloseEvent',
        self._addressOf(close),
    )

  @overload(QColor)
  def colorChanged(self, a0: QColor) -> None:
    """
    Calls Qt's 'void QQuickWindow::colorChanged(const QColor &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwindow.html#colorChanged

    Parameters
    ----------

    a0 : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickWindow::colorChanged(const QColor &a0)
    self.uglySide.call(
        'ritual_ZN12QQuickWindow12colorChangedERK6QColor', self._valueOf(a0),
    )

  def activeFocusItemChanged(self) -> None:
    """
    Calls Qt's 'void QQuickWindow::activeFocusItemChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindow.html#activeFocusItemChanged
    """
    #  void QQuickWindow::activeFocusItemChanged()
    self.uglySide.call('ritual_ZN12QQuickWindow22activeFocusItemChangedEv')

  @overload(SceneGraphError, str)
  def sceneGraphError(self, error: SceneGraphError, message: str) -> None:
    """
    Calls Qt's 'void
    QQuickWindow::sceneGraphError(QQuickWindow::SceneGraphError error, const
    QString &message)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwindow.html#sceneGraphError

    Parameters
    ----------

    error : SceneGraphError
      Passed on as its number.

    message : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickWindow::sceneGraphError(QQuickWindow::SceneGraphError
    #      error, const QString &message)
    self.uglySide.call(
        'ritual_ZN12QQuickWindow15sceneGraphErrorENS_15SceneGraphErrorERK7Q'
        'String',
        error.value, message,
    )

  def beforeRenderPassRecording(self) -> None:
    """
    Calls Qt's 'void QQuickWindow::beforeRenderPassRecording()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindow.html#beforeRenderPassRecording
    """
    #  void QQuickWindow::beforeRenderPassRecording()
    self.uglySide.call(
        'ritual_ZN12QQuickWindow25beforeRenderPassRecordingEv',
    )

  def afterRenderPassRecording(self) -> None:
    """
    Calls Qt's 'void QQuickWindow::afterRenderPassRecording()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindow.html#afterRenderPassRecording
    """
    #  void QQuickWindow::afterRenderPassRecording()
    self.uglySide.call('ritual_ZN12QQuickWindow24afterRenderPassRecordingEv')

  def paletteChanged(self) -> None:
    """
    Calls Qt's 'void QQuickWindow::paletteChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwindow.html#paletteChanged
    """
    #  void QQuickWindow::paletteChanged()
    self.uglySide.call('ritual_ZN12QQuickWindow14paletteChangedEv')

  def paletteCreated(self) -> None:
    """
    Calls Qt's 'void QQuickWindow::paletteCreated()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwindow.html#paletteCreated
    """
    #  void QQuickWindow::paletteCreated()
    self.uglySide.call('ritual_ZN12QQuickWindow14paletteCreatedEv')

  def beforeFrameBegin(self) -> None:
    """
    Calls Qt's 'void QQuickWindow::beforeFrameBegin()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwindow.html#beforeFrameBegin
    """
    #  void QQuickWindow::beforeFrameBegin()
    self.uglySide.call('ritual_ZN12QQuickWindow16beforeFrameBeginEv')

  def afterFrameEnd(self) -> None:
    """
    Calls Qt's 'void QQuickWindow::afterFrameEnd()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwindow.html#afterFrameEnd
    """
    #  void QQuickWindow::afterFrameEnd()
    self.uglySide.call('ritual_ZN12QQuickWindow13afterFrameEndEv')

  def devicePixelRatioChanged(self) -> None:
    """
    Calls Qt's 'void QQuickWindow::devicePixelRatioChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindow.html#devicePixelRatioChanged
    """
    #  void QQuickWindow::devicePixelRatioChanged()
    self.uglySide.call('ritual_ZN12QQuickWindow23devicePixelRatioChangedEv')

  def update(self) -> None:
    """
    Calls Qt's 'void QQuickWindow::update()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwindow.html#update
    """
    #  void QQuickWindow::update()
    self.uglySide.call('ritual_ZN12QQuickWindow6updateEv')

  def releaseResources(self) -> None:
    """
    Calls Qt's 'void QQuickWindow::releaseResources()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwindow.html#releaseResources
    """
    #  void QQuickWindow::releaseResources()
    self.uglySide.call('ritual_ZN12QQuickWindow16releaseResourcesEv')

  @overload(QExposeEvent)
  @overload(NoneType)
  def exposeEvent(self, a0: Optional[QExposeEvent]) -> None:
    """
    Calls Qt's 'void QQuickWindow::exposeEvent(QExposeEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwindow.html#exposeEvent

    Parameters
    ----------

    a0 : Optional[QExposeEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickWindow::exposeEvent(QExposeEvent *a0)
    ritual = 'ritual_ZN12QQuickWindow11exposeEventEP12QExposeEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QQuickWindow11exposeEventEP12QExposeEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QResizeEvent)
  @overload(NoneType)
  def resizeEvent(self, a0: Optional[QResizeEvent]) -> None:
    """
    Calls Qt's 'void QQuickWindow::resizeEvent(QResizeEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwindow.html#resizeEvent

    Parameters
    ----------

    a0 : Optional[QResizeEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickWindow::resizeEvent(QResizeEvent *a0)
    ritual = 'ritual_ZN12QQuickWindow11resizeEventEP12QResizeEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QQuickWindow11resizeEventEP12QResizeEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QShowEvent)
  @overload(NoneType)
  def showEvent(self, a0: Optional[QShowEvent]) -> None:
    """
    Calls Qt's 'void QQuickWindow::showEvent(QShowEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwindow.html#showEvent

    Parameters
    ----------

    a0 : Optional[QShowEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickWindow::showEvent(QShowEvent *a0)
    ritual = 'ritual_ZN12QQuickWindow9showEventEP10QShowEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QQuickWindow9showEventEP10QShowEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QHideEvent)
  @overload(NoneType)
  def hideEvent(self, a0: Optional[QHideEvent]) -> None:
    """
    Calls Qt's 'void QQuickWindow::hideEvent(QHideEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwindow.html#hideEvent

    Parameters
    ----------

    a0 : Optional[QHideEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickWindow::hideEvent(QHideEvent *a0)
    ritual = 'ritual_ZN12QQuickWindow9hideEventEP10QHideEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QQuickWindow9hideEventEP10QHideEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QCloseEvent)
  @overload(NoneType)
  def closeEvent(self, a0: Optional[QCloseEvent]) -> None:
    """
    Calls Qt's 'void QQuickWindow::closeEvent(QCloseEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwindow.html#closeEvent

    Parameters
    ----------

    a0 : Optional[QCloseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickWindow::closeEvent(QCloseEvent *a0)
    ritual = 'ritual_ZN12QQuickWindow10closeEventEP11QCloseEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QQuickWindow10closeEventEP11QCloseEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QFocusEvent)
  @overload(NoneType)
  def focusInEvent(self, a0: Optional[QFocusEvent]) -> None:
    """
    Calls Qt's 'void QQuickWindow::focusInEvent(QFocusEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwindow.html#focusInEvent

    Parameters
    ----------

    a0 : Optional[QFocusEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickWindow::focusInEvent(QFocusEvent *a0)
    ritual = 'ritual_ZN12QQuickWindow12focusInEventEP11QFocusEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QQuickWindow12focusInEventEP11QFocusEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QFocusEvent)
  @overload(NoneType)
  def focusOutEvent(self, a0: Optional[QFocusEvent]) -> None:
    """
    Calls Qt's 'void QQuickWindow::focusOutEvent(QFocusEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwindow.html#focusOutEvent

    Parameters
    ----------

    a0 : Optional[QFocusEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickWindow::focusOutEvent(QFocusEvent *a0)
    ritual = 'ritual_ZN12QQuickWindow13focusOutEventEP11QFocusEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QQuickWindow13focusOutEventEP11QFocusEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QEvent)
  @overload(NoneType)
  def event(self, a0: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QQuickWindow::event(QEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwindow.html#event

    Parameters
    ----------

    a0 : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickWindow::event(QEvent *a0)
    ritual = 'ritual_ZN12QQuickWindow5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QQuickWindow5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QKeyEvent)
  @overload(NoneType)
  def keyPressEvent(self, a0: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void QQuickWindow::keyPressEvent(QKeyEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwindow.html#keyPressEvent

    Parameters
    ----------

    a0 : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickWindow::keyPressEvent(QKeyEvent *a0)
    ritual = 'ritual_ZN12QQuickWindow13keyPressEventEP9QKeyEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QQuickWindow13keyPressEventEP9QKeyEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QKeyEvent)
  @overload(NoneType)
  def keyReleaseEvent(self, a0: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void QQuickWindow::keyReleaseEvent(QKeyEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwindow.html#keyReleaseEvent

    Parameters
    ----------

    a0 : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickWindow::keyReleaseEvent(QKeyEvent *a0)
    ritual = 'ritual_ZN12QQuickWindow15keyReleaseEventEP9QKeyEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QQuickWindow15keyReleaseEventEP9QKeyEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mousePressEvent(self, a0: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QQuickWindow::mousePressEvent(QMouseEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwindow.html#mousePressEvent

    Parameters
    ----------

    a0 : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickWindow::mousePressEvent(QMouseEvent *a0)
    ritual = 'ritual_ZN12QQuickWindow15mousePressEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QQuickWindow15mousePressEventEP11QMouseEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseReleaseEvent(self, a0: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QQuickWindow::mouseReleaseEvent(QMouseEvent *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindow.html#mouseReleaseEvent

    Parameters
    ----------

    a0 : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickWindow::mouseReleaseEvent(QMouseEvent *a0)
    ritual = 'ritual_ZN12QQuickWindow17mouseReleaseEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN12QQuickWindow17mouseReleaseEventEP11QMouseEvent')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseDoubleClickEvent(self, a0: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QQuickWindow::mouseDoubleClickEvent(QMouseEvent *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindow.html#mouseDoubleClickEvent

    Parameters
    ----------

    a0 : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickWindow::mouseDoubleClickEvent(QMouseEvent *a0)
    ritual = 'ritual_ZN12QQuickWindow21mouseDoubleClickEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN12QQuickWindow21mouseDoubleClickEventEP11QMouseEven'
          't')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseMoveEvent(self, a0: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QQuickWindow::mouseMoveEvent(QMouseEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwindow.html#mouseMoveEvent

    Parameters
    ----------

    a0 : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickWindow::mouseMoveEvent(QMouseEvent *a0)
    ritual = 'ritual_ZN12QQuickWindow14mouseMoveEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QQuickWindow14mouseMoveEventEP11QMouseEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QWheelEvent)
  @overload(NoneType)
  def wheelEvent(self, a0: Optional[QWheelEvent]) -> None:
    """
    Calls Qt's 'void QQuickWindow::wheelEvent(QWheelEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwindow.html#wheelEvent

    Parameters
    ----------

    a0 : Optional[QWheelEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickWindow::wheelEvent(QWheelEvent *a0)
    ritual = 'ritual_ZN12QQuickWindow10wheelEventEP11QWheelEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QQuickWindow10wheelEventEP11QWheelEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QTabletEvent)
  @overload(NoneType)
  def tabletEvent(self, a0: Optional[QTabletEvent]) -> None:
    """
    Calls Qt's 'void QQuickWindow::tabletEvent(QTabletEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwindow.html#tabletEvent

    Parameters
    ----------

    a0 : Optional[QTabletEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickWindow::tabletEvent(QTabletEvent *a0)
    ritual = 'ritual_ZN12QQuickWindow11tabletEventEP12QTabletEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QQuickWindow11tabletEventEP12QTabletEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  def maybeUpdate(self) -> None:
    """
    Calls Qt's 'void QQuickWindow::maybeUpdate()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwindow.html#maybeUpdate
    """
    #  void QQuickWindow::maybeUpdate()
    self.uglySide.call('ritual_ZN12QQuickWindow11maybeUpdateEv')

  def cleanupSceneGraph(self) -> None:
    """
    Calls Qt's 'void QQuickWindow::cleanupSceneGraph()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindow.html#cleanupSceneGraph
    """
    #  void QQuickWindow::cleanupSceneGraph()
    self.uglySide.call('ritual_ZN12QQuickWindow17cleanupSceneGraphEv')

  def physicalDpiChanged(self) -> None:
    """
    Calls Qt's 'void QQuickWindow::physicalDpiChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindow.html#physicalDpiChanged
    """
    #  void QQuickWindow::physicalDpiChanged()
    self.uglySide.call('ritual_ZN12QQuickWindow18physicalDpiChangedEv')

  @overload(QScreen)
  @overload(NoneType)
  def handleScreenChanged(self, screen: Optional[QScreen]) -> None:
    """
    Calls Qt's 'void QQuickWindow::handleScreenChanged(QScreen *screen)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindow.html#handleScreenChanged

    Parameters
    ----------

    screen : Optional[QScreen]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickWindow::handleScreenChanged(QScreen *screen)
    self.uglySide.call(
        'ritual_ZN12QQuickWindow19handleScreenChangedEP7QScreen',
        self._addressOf(screen),
    )

  def runJobsAfterSwap(self) -> None:
    """
    Calls Qt's 'void QQuickWindow::runJobsAfterSwap()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwindow.html#runJobsAfterSwap
    """
    #  void QQuickWindow::runJobsAfterSwap()
    self.uglySide.call('ritual_ZN12QQuickWindow16runJobsAfterSwapEv')

  @overload(Qt.ApplicationState)
  def handleApplicationStateChanged(
      self,
      state: Qt.ApplicationState,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickWindow::handleApplicationStateChanged(Qt::ApplicationState state)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindow.html#handleApplicationStateChanged

    Parameters
    ----------

    state : Qt.ApplicationState
      Passed on as its number.
    """
    #  void QQuickWindow::handleApplicationStateChanged(Qt::ApplicationState
    #      state)
    self.uglySide.call(
        'ritual_ZN12QQuickWindow29handleApplicationStateChangedEN2Qt16Appli'
        'cationStateE',
        state.value,
    )

  def handleFontDatabaseChanged(self) -> None:
    """
    Calls Qt's 'void QQuickWindow::handleFontDatabaseChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindow.html#handleFontDatabaseChanged
    """
    #  void QQuickWindow::handleFontDatabaseChanged()
    self.uglySide.call(
        'ritual_ZN12QQuickWindow25handleFontDatabaseChangedEv',
    )
