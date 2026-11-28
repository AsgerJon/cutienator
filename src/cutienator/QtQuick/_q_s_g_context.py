"""
QSGContext binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsgcontext_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QSGContext to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QSGTextNode

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QAnimationDriver, QMetaObject, QRectF, QSize
  from ..QtGui import QColor, QImage, QSurfaceFormat
  from . import QQuickPaintedItem, QQuickTextureFactory, QSGGlyphNode
  from . import QSGGuiThreadShaderEffectManager, QSGImageNode
  from . import QSGInternalImageNode, QSGInternalRectangleNode
  from . import QSGInternalTextNode, QSGLayer, QSGNinePatchNode
  from . import QSGPainterNode, QSGRectangleNode, QSGRenderContext
  from . import QSGRenderLoop, QSGRendererInterface, QSGShaderEffectNode
  from . import QSGSpriteNode
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAnimationDriver = WAIT['QAnimationDriver']
  QColor = WAIT['QColor']
  QImage = WAIT['QImage']
  QQuickPaintedItem = WAIT['QQuickPaintedItem']
  QRectF = WAIT['QRectF']
  QSGRenderContext = WAIT['QSGRenderContext']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSGContext(QObject):
  """
  The cute side of Qt's QSGContext: a plain Python object standing in front
  of one C++ QSGContext.

  It is built on the cute 'QObject', as Qt's QSGContext is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSGContext that has a ritual and that Python can
  call so far, 30 names in all: 'metaObject', 'tr',
  'renderContextInitialized', 'renderContextInvalidated',
  'createRenderContext', 'createInternalRectangleNode',
  'createInternalImageNode', 'createInternalTextNode', 'createPainterNode',
  'createGlyphNode', 'createLayer', 'createGuiThreadShaderEffectManager',
  'createShaderEffectNode', 'createSpriteNode', 'createAnimationDriver',
  'vsyncIntervalForAnimationDriver', 'isVSyncDependent', 'minimumFBOSize',
  'defaultSurfaceFormat', 'rendererInterface', 'createTextNode',
  'createRectangleNode', 'createImageNode', 'createNinePatchNode',
  'processTextRenderType', 'createDefaultContext',
  'createTextureFactoryFromImage', 'createWindowManager', 'setBackend',
  'backend'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QSGContext::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QSGContext::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QSGContext::~QSGContext()': the destructor: Python never removes a
    C++ QSGContext.

  What has no ritual
  ------------------

  2 of the 37 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QSGContext is created at the first use, not by 'QSGContext(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGContext.
  - Qt tells when it has removed the C++ QSGContext. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  #  The enums Qt writes inside QSGContext, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class AntialiasingMethod(CuteNum):
    """
    The enum 'QSGContext::AntialiasingMethod' of Qt, with the 3 names Qt
    gives in it.
    """

    UndecidedAntialiasing = Kee[int](0)
    VertexAntialiasing = Kee[int](1)
    MsaaAntialiasing = Kee[int](2)

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
    Calls Qt's 'QString QSGContext::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgcontext.html#tr

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
    #  QString QSGContext::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN10QSGContext2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def createDefaultContext() -> Optional[QSGContext]:
    """
    Calls Qt's 'QSGContext *QSGContext::createDefaultContext()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgcontext.html#createDefaultContext

    Returns
    -------

    Optional[QSGContext]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGContext *QSGContext::createDefaultContext()
    address = Rituals.call('ritual_ZN10QSGContext20createDefaultContextEv')
    return QSGContext._cuteAt(address)

  @staticmethod
  @overload(QImage)
  def createTextureFactoryFromImage(
      image: QImage,
  ) -> Optional[QQuickTextureFactory]:
    """
    Calls Qt's 'QQuickTextureFactory
    *QSGContext::createTextureFactoryFromImage(const QImage &image)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgcontext.html#createTextureFactoryFromImage

    Parameters
    ----------

    image : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.

    Returns
    -------

    Optional[QQuickTextureFactory]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickTextureFactory *QSGContext::createTextureFactoryFromImage(const
    #      QImage &image)
    address = Rituals.call(
        'ritual_ZN10QSGContext29createTextureFactoryFromImageERK6QImage',
        CuteMixin._valueOf(image),
    )
    from . import QQuickTextureFactory
    return QQuickTextureFactory._cuteAt(address)

  @staticmethod
  def createWindowManager() -> Optional[QSGRenderLoop]:
    """
    Calls Qt's 'QSGRenderLoop *QSGContext::createWindowManager()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgcontext.html#createWindowManager

    Returns
    -------

    Optional[QSGRenderLoop]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGRenderLoop *QSGContext::createWindowManager()
    address = Rituals.call('ritual_ZN10QSGContext19createWindowManagerEv')
    from . import QSGRenderLoop
    return QSGRenderLoop._cuteAt(address)

  @staticmethod
  @overload(str)
  def setBackend(backend: str) -> None:
    """
    Calls Qt's 'void QSGContext::setBackend(const QString &backend)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgcontext.html#setBackend

    Parameters
    ----------

    backend : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QSGContext::setBackend(const QString &backend)
    Rituals.call('ritual_ZN10QSGContext10setBackendERK7QString', backend)

  @staticmethod
  def backend() -> str:
    """
    Calls Qt's 'QString QSGContext::backend()'.

    Qt's own words: https://doc.qt.io/qt-6/qsgcontext.html#backend

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSGContext::backend()
    return Rituals.call('ritual_ZN10QSGContext7backendEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGContext'

  #  A C++ QSGContext Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSGContext'

  #  The functions Qt calls itself that QSGContext is the first to declare. A
  #  class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'renderContextInitialized': (
          ('_ZN10QSGContext24renderContextInitializedEP16QSGRenderContext',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QSGRenderContext'),
           )),
      ),
      'renderContextInvalidated': (
          ('_ZN10QSGContext24renderContextInvalidatedEP16QSGRenderContext',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QSGRenderContext'),
           )),
      ),
      'createRenderContext': (
          ('_ZN10QSGContext19createRenderContextEv',
           ('address', 'address', 'QtQuick:QSGRenderContext'),
           ()),
      ),
      'createInternalRectangleNode': (
          ('_ZN10QSGContext27createInternalRectangleNodeEv',
           ('address', 'address', 'QtQuick:QSGInternalRectangleNode'),
           ()),
      ),
      'createInternalImageNode': (
          ('_ZN10QSGContext23createInternalImageNodeEP16QSGRenderContext',
           ('address', 'address', 'QtQuick:QSGInternalImageNode'),
           (
               ('address', 'address', 'QtQuick:QSGRenderContext'),
           )),
      ),
      'createInternalTextNode': (
          ('_ZN10QSGContext22createInternalTextNodeEP16QSGRenderContext',
           ('address', 'address', 'QtQuick:QSGInternalTextNode'),
           (
               ('address', 'address', 'QtQuick:QSGRenderContext'),
           )),
      ),
      'createPainterNode': (
          ('_ZN10QSGContext17createPainterNodeEP17QQuickPaintedItem',
           ('address', 'address', 'QtQuick:QSGPainterNode'),
           (
               ('address', 'address', 'QtQuick:QQuickPaintedItem'),
           )),
      ),
      'createGlyphNode': (
          ('_ZN10QSGContext15createGlyphNodeEP16QSGRenderContextN11QSGTextN'
           'ode10RenderTypeE',
           ('address', 'address', 'QtQuick:QSGGlyphNode'),
           (
               ('address', 'address', 'QtQuick:QSGRenderContext'),
               ('int', 'enum', 'QtQuick:QSGTextNode.RenderType'),
           )),
      ),
      'createLayer': (
          ('_ZN10QSGContext11createLayerEP16QSGRenderContext',
           ('address', 'address', 'QtQuick:QSGLayer'),
           (
               ('address', 'address', 'QtQuick:QSGRenderContext'),
           )),
      ),
      'createGuiThreadShaderEffectManager': (
          ('_ZN10QSGContext34createGuiThreadShaderEffectManagerEv',
           ('address', 'address', 'QtQuick:QSGGuiThreadShaderEffectManager'),
           ()),
      ),
      'createShaderEffectNode': (
          ('_ZN10QSGContext22createShaderEffectNodeEP16QSGRenderContext',
           ('address', 'address', 'QtQuick:QSGShaderEffectNode'),
           (
               ('address', 'address', 'QtQuick:QSGRenderContext'),
           )),
      ),
      'createSpriteNode': (
          ('_ZN10QSGContext16createSpriteNodeEv',
           ('address', 'address', 'QtQuick:QSGSpriteNode'),
           ()),
      ),
      'createAnimationDriver': (
          ('_ZN10QSGContext21createAnimationDriverEP7QObject',
           ('address', 'address', 'QtCore:QAnimationDriver'),
           (
               ('address', 'address', 'QtCore:QObject'),
           )),
      ),
      'vsyncIntervalForAnimationDriver': (
          ('_ZN10QSGContext31vsyncIntervalForAnimationDriverEP16QAnimationD'
           'river',
           ('float', 'number', ''),
           (
               ('address', 'address', 'QtCore:QAnimationDriver'),
           )),
      ),
      'isVSyncDependent': (
          ('_ZN10QSGContext16isVSyncDependentEP16QAnimationDriver',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtCore:QAnimationDriver'),
           )),
      ),
      'minimumFBOSize': (
          ('_ZNK10QSGContext14minimumFBOSizeEv',
           ('address', 'value', 'QtCore:QSize'),
           ()),
      ),
      'defaultSurfaceFormat': (
          ('_ZNK10QSGContext20defaultSurfaceFormatEv',
           ('address', 'value', 'QtGui:QSurfaceFormat'),
           ()),
      ),
      'rendererInterface': (
          ('_ZN10QSGContext17rendererInterfaceEP16QSGRenderContext',
           ('address', 'address', 'QtQuick:QSGRendererInterface'),
           (
               ('address', 'address', 'QtQuick:QSGRenderContext'),
           )),
      ),
      'createTextNode': (
          ('_ZN10QSGContext14createTextNodeEP16QSGRenderContext',
           ('address', 'address', 'QtQuick:QSGTextNode'),
           (
               ('address', 'address', 'QtQuick:QSGRenderContext'),
           )),
      ),
      'createRectangleNode': (
          ('_ZN10QSGContext19createRectangleNodeEv',
           ('address', 'address', 'QtQuick:QSGRectangleNode'),
           ()),
      ),
      'createImageNode': (
          ('_ZN10QSGContext15createImageNodeEv',
           ('address', 'address', 'QtQuick:QSGImageNode'),
           ()),
      ),
      'createNinePatchNode': (
          ('_ZN10QSGContext19createNinePatchNodeEv',
           ('address', 'address', 'QtQuick:QSGNinePatchNode'),
           ()),
      ),
      'processTextRenderType': (
          ('_ZN10QSGContext21processTextRenderTypeEN11QSGTextNode10RenderTy'
           'peE',
           ('int', 'enum', 'QtQuick:QSGTextNode.RenderType'),
           (
               ('int', 'enum', 'QtQuick:QSGTextNode.RenderType'),
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
    Calls Qt's 'const QMetaObject *QSGContext::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgcontext.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QSGContext::metaObject() const
    address = self.uglySide.call('ritual_ZNK10QSGContext10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def minimumFBOSize(self) -> QSize:
    """
    Calls Qt's 'QSize QSGContext::minimumFBOSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgcontext.html#minimumFBOSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QSGContext::minimumFBOSize() const
    ritual = 'ritual_ZNK10QSGContext14minimumFBOSizeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK10QSGContext14minimumFBOSizeEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def defaultSurfaceFormat(self) -> QSurfaceFormat:
    """
    Calls Qt's 'QSurfaceFormat QSGContext::defaultSurfaceFormat() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgcontext.html#defaultSurfaceFormat

    Returns
    -------

    QSurfaceFormat
      A new cute QSurfaceFormat around the copy Qt gave back. Python owns it.
    """
    #  QSurfaceFormat QSGContext::defaultSurfaceFormat() const
    address = self.uglySide.call(
        'ritual_ZNK10QSGContext20defaultSurfaceFormatEv',
    )
    from ..QtGui import QSurfaceFormat
    return QSurfaceFormat._cuteOwning(address)

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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's 'QSGContext::QSGContext(QObject *parent)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsgcontext.html#QSGContext

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QSGContext::QSGContext(QObject *parent)
    self._noteCreation(QSGContext, lambda: Rituals.call(
        'ritual_ZN10QSGContextC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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

  @overload(QSGRenderContext)
  @overload(NoneType)
  def renderContextInitialized(
      self,
      renderContext: Optional[QSGRenderContext],
  ) -> None:
    """
    Calls Qt's 'void QSGContext::renderContextInitialized(QSGRenderContext
    *renderContext)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgcontext.html#renderContextInitialized

    Parameters
    ----------

    renderContext : Optional[QSGRenderContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGContext::renderContextInitialized(QSGRenderContext
    #      *renderContext)
    ritual = (
        'ritual_ZN10QSGContext24renderContextInitializedEP16QSGRenderContex'
        't')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10QSGContext24renderContextInitializedEP16QSGRender'
          'Context')
    self.uglySide.call(ritual, self._addressOf(renderContext))

  @overload(QSGRenderContext)
  @overload(NoneType)
  def renderContextInvalidated(
      self,
      renderContext: Optional[QSGRenderContext],
  ) -> None:
    """
    Calls Qt's 'void QSGContext::renderContextInvalidated(QSGRenderContext
    *renderContext)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgcontext.html#renderContextInvalidated

    Parameters
    ----------

    renderContext : Optional[QSGRenderContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGContext::renderContextInvalidated(QSGRenderContext
    #      *renderContext)
    ritual = (
        'ritual_ZN10QSGContext24renderContextInvalidatedEP16QSGRenderContex'
        't')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10QSGContext24renderContextInvalidatedEP16QSGRender'
          'Context')
    self.uglySide.call(ritual, self._addressOf(renderContext))

  def createRenderContext(self) -> Optional[QSGRenderContext]:
    """
    Calls Qt's 'QSGRenderContext *QSGContext::createRenderContext()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgcontext.html#createRenderContext

    Returns
    -------

    Optional[QSGRenderContext]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGRenderContext *QSGContext::createRenderContext()
    address = self.uglySide.call(
        'ritual_ZN10QSGContext19createRenderContextEv',
    )
    from . import QSGRenderContext
    return QSGRenderContext._cuteAt(address)

  @overload(QRectF, QColor)
  def createInternalRectangleNode(
      self,
      rect: QRectF,
      c: QColor,
  ) -> Optional[QSGInternalRectangleNode]:
    """
    Calls Qt's 'QSGInternalRectangleNode
    *QSGContext::createInternalRectangleNode(const QRectF &rect, const QColor
    &c)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgcontext.html#createInternalRectangleNode

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    c : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.

    Returns
    -------

    Optional[QSGInternalRectangleNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGInternalRectangleNode
    #      *QSGContext::createInternalRectangleNode(const QRectF &rect, const
    #      QColor &c)
    address = self.uglySide.call(
        'ritual_ZN10QSGContext27createInternalRectangleNodeERK6QRectFRK6QCo'
        'lor',
        self._valueOf(rect), self._valueOf(c),
    )
    from . import QSGInternalRectangleNode
    return QSGInternalRectangleNode._cuteAt(address)

  @overload()
  def createInternalRectangleNode(
      self,
  ) -> Optional[QSGInternalRectangleNode]:
    """
    Calls Qt's 'QSGInternalRectangleNode
    *QSGContext::createInternalRectangleNode()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgcontext.html#createInternalRectangleNode

    Returns
    -------

    Optional[QSGInternalRectangleNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGInternalRectangleNode *QSGContext::createInternalRectangleNode()
    address = self.uglySide.call(
        'ritual_ZN10QSGContext27createInternalRectangleNodeEv',
    )
    from . import QSGInternalRectangleNode
    return QSGInternalRectangleNode._cuteAt(address)

  @overload(QSGRenderContext)
  @overload(NoneType)
  def createInternalImageNode(
      self,
      renderContext: Optional[QSGRenderContext],
  ) -> Optional[QSGInternalImageNode]:
    """
    Calls Qt's 'QSGInternalImageNode
    *QSGContext::createInternalImageNode(QSGRenderContext *renderContext)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgcontext.html#createInternalImageNode

    Parameters
    ----------

    renderContext : Optional[QSGRenderContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QSGInternalImageNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGInternalImageNode
    #      *QSGContext::createInternalImageNode(QSGRenderContext
    #      *renderContext)
    address = self.uglySide.call(
        'ritual_ZN10QSGContext23createInternalImageNodeEP16QSGRenderContext',
        self._addressOf(renderContext),
    )
    from . import QSGInternalImageNode
    return QSGInternalImageNode._cuteAt(address)

  @overload(QSGRenderContext)
  @overload(NoneType)
  def createInternalTextNode(
      self,
      renderContext: Optional[QSGRenderContext],
  ) -> Optional[QSGInternalTextNode]:
    """
    Calls Qt's 'QSGInternalTextNode
    *QSGContext::createInternalTextNode(QSGRenderContext *renderContext)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgcontext.html#createInternalTextNode

    Parameters
    ----------

    renderContext : Optional[QSGRenderContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QSGInternalTextNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGInternalTextNode
    #      *QSGContext::createInternalTextNode(QSGRenderContext
    #      *renderContext)
    ritual = (
        'ritual_ZN10QSGContext22createInternalTextNodeEP16QSGRenderContext')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10QSGContext22createInternalTextNodeEP16QSGRenderCo'
          'ntext')
    address = self.uglySide.call(ritual, self._addressOf(renderContext))
    from . import QSGInternalTextNode
    return QSGInternalTextNode._cuteAt(address)

  @overload(QQuickPaintedItem)
  @overload(NoneType)
  def createPainterNode(
      self,
      item: Optional[QQuickPaintedItem],
  ) -> Optional[QSGPainterNode]:
    """
    Calls Qt's 'QSGPainterNode
    *QSGContext::createPainterNode(QQuickPaintedItem *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgcontext.html#createPainterNode

    Parameters
    ----------

    item : Optional[QQuickPaintedItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QSGPainterNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGPainterNode *QSGContext::createPainterNode(QQuickPaintedItem *item)
    address = self.uglySide.call(
        'ritual_ZN10QSGContext17createPainterNodeEP17QQuickPaintedItem',
        self._addressOf(item),
    )
    from . import QSGPainterNode
    return QSGPainterNode._cuteAt(address)

  @overload(QSGRenderContext, QSGTextNode.RenderType)
  @overload(NoneType, QSGTextNode.RenderType)
  def createGlyphNode(
      self,
      rc: Optional[QSGRenderContext],
      renderType: QSGTextNode.RenderType,
  ) -> Optional[QSGGlyphNode]:
    """
    Calls Qt's 'QSGGlyphNode *QSGContext::createGlyphNode(QSGRenderContext
    *rc, QSGTextNode::RenderType renderType)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgcontext.html#createGlyphNode

    Parameters
    ----------

    rc : Optional[QSGRenderContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    renderType : QSGTextNode.RenderType
      Passed on as its number.

    Returns
    -------

    Optional[QSGGlyphNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGGlyphNode *QSGContext::createGlyphNode(QSGRenderContext *rc,
    #      QSGTextNode::RenderType renderType)
    address = self.uglySide.call(
        'ritual_ZN10QSGContext15createGlyphNodeEP16QSGRenderContextN11QSGTe'
        'xtNode10RenderTypeE',
        self._addressOf(rc), renderType.value,
    )
    from . import QSGGlyphNode
    return QSGGlyphNode._cuteAt(address)

  @overload(QSGRenderContext)
  @overload(NoneType)
  def createLayer(
      self,
      renderContext: Optional[QSGRenderContext],
  ) -> Optional[QSGLayer]:
    """
    Calls Qt's 'QSGLayer *QSGContext::createLayer(QSGRenderContext
    *renderContext)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgcontext.html#createLayer

    Parameters
    ----------

    renderContext : Optional[QSGRenderContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QSGLayer]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGLayer *QSGContext::createLayer(QSGRenderContext *renderContext)
    address = self.uglySide.call(
        'ritual_ZN10QSGContext11createLayerEP16QSGRenderContext',
        self._addressOf(renderContext),
    )
    from . import QSGLayer
    return QSGLayer._cuteAt(address)

  def createGuiThreadShaderEffectManager(
      self,
  ) -> Optional[QSGGuiThreadShaderEffectManager]:
    """
    Calls Qt's 'QSGGuiThreadShaderEffectManager
    *QSGContext::createGuiThreadShaderEffectManager()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgcontext.html#createGuiThreadShaderEffectManager

    Returns
    -------

    Optional[QSGGuiThreadShaderEffectManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGGuiThreadShaderEffectManager
    #      *QSGContext::createGuiThreadShaderEffectManager()
    ritual = 'ritual_ZN10QSGContext34createGuiThreadShaderEffectManagerEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10QSGContext34createGuiThreadShaderEffectManagerEv')
    address = self.uglySide.call(ritual)
    from . import QSGGuiThreadShaderEffectManager
    return QSGGuiThreadShaderEffectManager._cuteAt(address)

  @overload(QSGRenderContext)
  @overload(NoneType)
  def createShaderEffectNode(
      self,
      renderContext: Optional[QSGRenderContext],
  ) -> Optional[QSGShaderEffectNode]:
    """
    Calls Qt's 'QSGShaderEffectNode
    *QSGContext::createShaderEffectNode(QSGRenderContext *renderContext)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgcontext.html#createShaderEffectNode

    Parameters
    ----------

    renderContext : Optional[QSGRenderContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QSGShaderEffectNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGShaderEffectNode
    #      *QSGContext::createShaderEffectNode(QSGRenderContext
    #      *renderContext)
    ritual = (
        'ritual_ZN10QSGContext22createShaderEffectNodeEP16QSGRenderContext')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10QSGContext22createShaderEffectNodeEP16QSGRenderCo'
          'ntext')
    address = self.uglySide.call(ritual, self._addressOf(renderContext))
    from . import QSGShaderEffectNode
    return QSGShaderEffectNode._cuteAt(address)

  def createSpriteNode(self) -> Optional[QSGSpriteNode]:
    """
    Calls Qt's 'QSGSpriteNode *QSGContext::createSpriteNode()'.

    Qt's own words: https://doc.qt.io/qt-6/qsgcontext.html#createSpriteNode

    Returns
    -------

    Optional[QSGSpriteNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGSpriteNode *QSGContext::createSpriteNode()
    address = self.uglySide.call('ritual_ZN10QSGContext16createSpriteNodeEv')
    from . import QSGSpriteNode
    return QSGSpriteNode._cuteAt(address)

  @overload(QObject)
  @overload(NoneType)
  def createAnimationDriver(
      self,
      parent: Optional[QObject],
  ) -> Optional[QAnimationDriver]:
    """
    Calls Qt's 'QAnimationDriver *QSGContext::createAnimationDriver(QObject
    *parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgcontext.html#createAnimationDriver

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QAnimationDriver]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAnimationDriver *QSGContext::createAnimationDriver(QObject *parent)
    ritual = 'ritual_ZN10QSGContext21createAnimationDriverEP7QObject'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QSGContext21createAnimationDriverEP7QObject'
    address = self.uglySide.call(ritual, self._addressOf(parent, 'QObject'))
    from ..QtCore import QAnimationDriver
    return QAnimationDriver._cuteAt(address)

  @overload(QAnimationDriver)
  @overload(NoneType)
  def vsyncIntervalForAnimationDriver(
      self,
      driver: Optional[QAnimationDriver],
  ) -> float:
    """
    Calls Qt's 'float
    QSGContext::vsyncIntervalForAnimationDriver(QAnimationDriver *driver)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgcontext.html#vsyncIntervalForAnimationDriver

    Parameters
    ----------

    driver : Optional[QAnimationDriver]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  float QSGContext::vsyncIntervalForAnimationDriver(QAnimationDriver
    #      *driver)
    ritual = (
        'ritual_ZN10QSGContext31vsyncIntervalForAnimationDriverEP16QAnimati'
        'onDriver')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10QSGContext31vsyncIntervalForAnimationDriverEP16QA'
          'nimationDriver')
    return self.uglySide.call(ritual, self._addressOf(driver))

  @overload(QAnimationDriver)
  @overload(NoneType)
  def isVSyncDependent(self, driver: Optional[QAnimationDriver]) -> bool:
    """
    Calls Qt's 'bool QSGContext::isVSyncDependent(QAnimationDriver *driver)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgcontext.html#isVSyncDependent

    Parameters
    ----------

    driver : Optional[QAnimationDriver]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QSGContext::isVSyncDependent(QAnimationDriver *driver)
    ritual = 'ritual_ZN10QSGContext16isVSyncDependentEP16QAnimationDriver'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10QSGContext16isVSyncDependentEP16QAnimationDriver')
    return self.uglySide.call(ritual, self._addressOf(driver))

  @overload(QSGRenderContext)
  @overload(NoneType)
  def rendererInterface(
      self,
      renderContext: Optional[QSGRenderContext],
  ) -> Optional[QSGRendererInterface]:
    """
    Calls Qt's 'QSGRendererInterface
    *QSGContext::rendererInterface(QSGRenderContext *renderContext)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgcontext.html#rendererInterface

    Parameters
    ----------

    renderContext : Optional[QSGRenderContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QSGRendererInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGRendererInterface *QSGContext::rendererInterface(QSGRenderContext
    #      *renderContext)
    ritual = 'ritual_ZN10QSGContext17rendererInterfaceEP16QSGRenderContext'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10QSGContext17rendererInterfaceEP16QSGRenderContext')
    address = self.uglySide.call(ritual, self._addressOf(renderContext))
    from . import QSGRendererInterface
    return QSGRendererInterface._cuteAt(address)

  @overload(QSGRenderContext)
  @overload(NoneType)
  def createTextNode(
      self,
      renderContext: Optional[QSGRenderContext],
  ) -> Optional[QSGTextNode]:
    """
    Calls Qt's 'QSGTextNode *QSGContext::createTextNode(QSGRenderContext
    *renderContext)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgcontext.html#createTextNode

    Parameters
    ----------

    renderContext : Optional[QSGRenderContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QSGTextNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGTextNode *QSGContext::createTextNode(QSGRenderContext
    #      *renderContext)
    ritual = 'ritual_ZN10QSGContext14createTextNodeEP16QSGRenderContext'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10QSGContext14createTextNodeEP16QSGRenderContext')
    address = self.uglySide.call(ritual, self._addressOf(renderContext))
    return QSGTextNode._cuteAt(address)

  def createRectangleNode(self) -> Optional[QSGRectangleNode]:
    """
    Calls Qt's 'QSGRectangleNode *QSGContext::createRectangleNode()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgcontext.html#createRectangleNode

    Returns
    -------

    Optional[QSGRectangleNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGRectangleNode *QSGContext::createRectangleNode()
    address = self.uglySide.call(
        'ritual_ZN10QSGContext19createRectangleNodeEv',
    )
    from . import QSGRectangleNode
    return QSGRectangleNode._cuteAt(address)

  def createImageNode(self) -> Optional[QSGImageNode]:
    """
    Calls Qt's 'QSGImageNode *QSGContext::createImageNode()'.

    Qt's own words: https://doc.qt.io/qt-6/qsgcontext.html#createImageNode

    Returns
    -------

    Optional[QSGImageNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGImageNode *QSGContext::createImageNode()
    address = self.uglySide.call('ritual_ZN10QSGContext15createImageNodeEv')
    from . import QSGImageNode
    return QSGImageNode._cuteAt(address)

  def createNinePatchNode(self) -> Optional[QSGNinePatchNode]:
    """
    Calls Qt's 'QSGNinePatchNode *QSGContext::createNinePatchNode()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgcontext.html#createNinePatchNode

    Returns
    -------

    Optional[QSGNinePatchNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGNinePatchNode *QSGContext::createNinePatchNode()
    address = self.uglySide.call(
        'ritual_ZN10QSGContext19createNinePatchNodeEv',
    )
    from . import QSGNinePatchNode
    return QSGNinePatchNode._cuteAt(address)

  @overload(QSGTextNode.RenderType)
  def processTextRenderType(
      self,
      renderType: QSGTextNode.RenderType,
  ) -> QSGTextNode.RenderType:
    """
    Calls Qt's 'QSGTextNode::RenderType
    QSGContext::processTextRenderType(QSGTextNode::RenderType renderType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgcontext.html#processTextRenderType

    Parameters
    ----------

    renderType : QSGTextNode.RenderType
      Passed on as its number.

    Returns
    -------

    QSGTextNode.RenderType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QSGTextNode.RenderType(number)' gives.
    """
    #  QSGTextNode::RenderType
    #      QSGContext::processTextRenderType(QSGTextNode::RenderType
    #      renderType)
    return QSGTextNode.RenderType(self.uglySide.call(
        'ritual_ZN10QSGContext21processTextRenderTypeEN11QSGTextNode10Rende'
        'rTypeE',
        renderType.value,
    ))
