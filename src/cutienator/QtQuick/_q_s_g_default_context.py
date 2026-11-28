"""
QSGDefaultContext binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsgdefaultcontext_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QSGDefaultContext to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QSGContext, QSGRendererInterface, QSGTextNode

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtGui import QSurfaceFormat
  from . import QQuickPaintedItem, QSGGlyphNode
  from . import QSGGuiThreadShaderEffectManager, QSGImageNode
  from . import QSGInternalImageNode, QSGInternalRectangleNode
  from . import QSGInternalTextNode, QSGLayer, QSGNinePatchNode
  from . import QSGPainterNode, QSGRectangleNode, QSGRenderContext
  from . import QSGShaderEffectNode, QSGSpriteNode
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickPaintedItem = WAIT['QQuickPaintedItem']
  QSGRenderContext = WAIT['QSGRenderContext']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSGDefaultContext(QSGContext, QSGRendererInterface):
  """
  The cute side of Qt's QSGDefaultContext: a plain Python object standing in
  front of one C++ QSGDefaultContext.

  It is built on the cute 'QSGContext', as Qt's QSGDefaultContext is built on
  Qt's QSGContext, and has everything that class has. It is built on the cute
  'QSGRendererInterface' as well, as Qt's QSGDefaultContext is built on Qt's
  QSGRendererInterface too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSGDefaultContext that has a ritual and that Python
  can call so far, 24 names in all: 'renderContextInitialized',
  'renderContextInvalidated', 'createRenderContext',
  'createInternalRectangleNode', 'createInternalImageNode',
  'createPainterNode', 'createGlyphNode', 'createInternalTextNode',
  'createLayer', 'defaultSurfaceFormat', 'rendererInterface',
  'createRectangleNode', 'createImageNode', 'createNinePatchNode',
  'createSpriteNode', 'createGuiThreadShaderEffectManager',
  'createShaderEffectNode', 'setDistanceFieldEnabled',
  'isDistanceFieldEnabled', 'processTextRenderType', 'graphicsApi',
  'shaderType', 'shaderCompilationType', 'shaderSourceType'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSGDefaultContext::~QSGDefaultContext()': the destructor: Python
    never removes a C++ QSGDefaultContext.
  - Qt's 'void *QSGDefaultContext::getResource(QQuickWindow *window, Resource
    resource) const': gives 'void', which has no cute class yet.

  What to expect
  --------------

  - The C++ QSGDefaultContext is created at the first use, not by
    'QSGDefaultContext(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGDefaultContext.
  - Qt tells when it has removed the C++ QSGDefaultContext. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGDefaultContext'

  #  Qt's QSGDefaultContext is built on more than one class. The part of a
  #  C++ QSGDefaultContext that belongs to a class after the first begins
  #  somewhere inside the object, and the ritual named for that class gives
  #  where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QSGRendererInterface':
          'ritual_cast_QSGDefaultContext_QSGRendererInterface',
  }

  #  A C++ QSGDefaultContext Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSGDefaultContext'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def defaultSurfaceFormat(self) -> QSurfaceFormat:
    """
    Calls Qt's 'QSurfaceFormat QSGDefaultContext::defaultSurfaceFormat()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultcontext.html#defaultSurfaceFormat

    Returns
    -------

    QSurfaceFormat
      A new cute QSurfaceFormat around the copy Qt gave back. Python owns it.
    """
    #  QSurfaceFormat QSGDefaultContext::defaultSurfaceFormat() const
    ritual = 'ritual_ZNK17QSGDefaultContext20defaultSurfaceFormatEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QSGDefaultContext20defaultSurfaceFormatEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QSurfaceFormat
    return QSurfaceFormat._cuteOwning(address)

  def isDistanceFieldEnabled(self) -> bool:
    """
    Calls Qt's 'bool QSGDefaultContext::isDistanceFieldEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultcontext.html#isDistanceFieldEnabled
    """
    #  bool QSGDefaultContext::isDistanceFieldEnabled() const
    return self.uglySide.call(
        'ritual_ZNK17QSGDefaultContext22isDistanceFieldEnabledEv',
    )

  def graphicsApi(self) -> QSGRendererInterface.GraphicsApi:
    """
    Calls Qt's 'GraphicsApi QSGDefaultContext::graphicsApi() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgdefaultcontext.html#graphicsApi

    Returns
    -------

    QSGRendererInterface.GraphicsApi
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QSGRendererInterface.GraphicsApi(number)' gives.
    """
    #  GraphicsApi QSGDefaultContext::graphicsApi() const
    ritual = 'ritual_ZNK17QSGDefaultContext11graphicsApiEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QSGDefaultContext11graphicsApiEv'
    return QSGRendererInterface.GraphicsApi(self.uglySide.call(ritual))

  def shaderType(self) -> QSGRendererInterface.ShaderType:
    """
    Calls Qt's 'ShaderType QSGDefaultContext::shaderType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgdefaultcontext.html#shaderType

    Returns
    -------

    QSGRendererInterface.ShaderType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QSGRendererInterface.ShaderType(number)' gives.
    """
    #  ShaderType QSGDefaultContext::shaderType() const
    ritual = 'ritual_ZNK17QSGDefaultContext10shaderTypeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QSGDefaultContext10shaderTypeEv'
    return QSGRendererInterface.ShaderType(self.uglySide.call(ritual))

  def shaderCompilationType(
      self,
  ) -> QSGRendererInterface.ShaderCompilationTypes:
    """
    Calls Qt's 'ShaderCompilationTypes
    QSGDefaultContext::shaderCompilationType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultcontext.html#shaderCompilationType

    Returns
    -------

    QSGRendererInterface.ShaderCompilationTypes
      The value standing for the combination Qt gave back.
    """
    #  ShaderCompilationTypes QSGDefaultContext::shaderCompilationType()
    #      const
    ritual = 'ritual_ZNK17QSGDefaultContext21shaderCompilationTypeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QSGDefaultContext21shaderCompilationTypeEv'
    return QSGRendererInterface.ShaderCompilationTypes(self.uglySide.call(
        ritual,
    ))

  def shaderSourceType(self) -> QSGRendererInterface.ShaderSourceTypes:
    """
    Calls Qt's 'ShaderSourceTypes QSGDefaultContext::shaderSourceType()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultcontext.html#shaderSourceType

    Returns
    -------

    QSGRendererInterface.ShaderSourceTypes
      The value standing for the combination Qt gave back.
    """
    #  ShaderSourceTypes QSGDefaultContext::shaderSourceType() const
    ritual = 'ritual_ZNK17QSGDefaultContext16shaderSourceTypeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QSGDefaultContext16shaderSourceTypeEv'
    return QSGRendererInterface.ShaderSourceTypes(self.uglySide.call(ritual))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setDistanceFieldEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QSGDefaultContext::setDistanceFieldEnabled(bool
    enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultcontext.html#setDistanceFieldEnabled

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QSGDefaultContext::setDistanceFieldEnabled(bool enabled)
    self.uglySide.call(
        'ritual_ZN17QSGDefaultContext23setDistanceFieldEnabledEb', enabled,
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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QSGDefaultContext::QSGDefaultContext(QObject *parent)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultcontext.html#QSGDefaultContext

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QSGDefaultContext::QSGDefaultContext(QObject *parent)
    self._noteCreation(QSGDefaultContext, lambda: Rituals.call(
        'ritual_ZN17QSGDefaultContextC1EP7QObject',
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
    Calls Qt's 'void
    QSGDefaultContext::renderContextInitialized(QSGRenderContext
    *renderContext)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultcontext.html#renderContextInitialized

    Parameters
    ----------

    renderContext : Optional[QSGRenderContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGDefaultContext::renderContextInitialized(QSGRenderContext
    #      *renderContext)
    ritual = (
        'ritual_ZN17QSGDefaultContext24renderContextInitializedEP16QSGRende'
        'rContext')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QSGDefaultContext24renderContextInitializedEP16QS'
          'GRenderContext')
    self.uglySide.call(ritual, self._addressOf(renderContext))

  @overload(QSGRenderContext)
  @overload(NoneType)
  def renderContextInvalidated(self, a0: Optional[QSGRenderContext]) -> None:
    """
    Calls Qt's 'void
    QSGDefaultContext::renderContextInvalidated(QSGRenderContext *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultcontext.html#renderContextInvalidated

    Parameters
    ----------

    a0 : Optional[QSGRenderContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGDefaultContext::renderContextInvalidated(QSGRenderContext *a0)
    ritual = (
        'ritual_ZN17QSGDefaultContext24renderContextInvalidatedEP16QSGRende'
        'rContext')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QSGDefaultContext24renderContextInvalidatedEP16QS'
          'GRenderContext')
    self.uglySide.call(ritual, self._addressOf(a0))

  def createRenderContext(self) -> Optional[QSGRenderContext]:
    """
    Calls Qt's 'QSGRenderContext *QSGDefaultContext::createRenderContext()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultcontext.html#createRenderContext

    Returns
    -------

    Optional[QSGRenderContext]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGRenderContext *QSGDefaultContext::createRenderContext()
    ritual = 'ritual_ZN17QSGDefaultContext19createRenderContextEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QSGDefaultContext19createRenderContextEv'
    address = self.uglySide.call(ritual)
    from . import QSGRenderContext
    return QSGRenderContext._cuteAt(address)

  def createInternalRectangleNode(
      self,
  ) -> Optional[QSGInternalRectangleNode]:
    """
    Calls Qt's 'QSGInternalRectangleNode
    *QSGDefaultContext::createInternalRectangleNode()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultcontext.html#createInternalRectangleNode

    Returns
    -------

    Optional[QSGInternalRectangleNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGInternalRectangleNode
    #      *QSGDefaultContext::createInternalRectangleNode()
    ritual = 'ritual_ZN17QSGDefaultContext27createInternalRectangleNodeEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QSGDefaultContext27createInternalRectangleNodeEv')
    address = self.uglySide.call(ritual)
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
    *QSGDefaultContext::createInternalImageNode(QSGRenderContext
    *renderContext)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultcontext.html#createInternalImageNode

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
    #      *QSGDefaultContext::createInternalImageNode(QSGRenderContext
    #      *renderContext)
    ritual = (
        'ritual_ZN17QSGDefaultContext23createInternalImageNodeEP16QSGRender'
        'Context')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QSGDefaultContext23createInternalImageNodeEP16QSG'
          'RenderContext')
    address = self.uglySide.call(ritual, self._addressOf(renderContext))
    from . import QSGInternalImageNode
    return QSGInternalImageNode._cuteAt(address)

  @overload(QQuickPaintedItem)
  @overload(NoneType)
  def createPainterNode(
      self,
      item: Optional[QQuickPaintedItem],
  ) -> Optional[QSGPainterNode]:
    """
    Calls Qt's 'QSGPainterNode
    *QSGDefaultContext::createPainterNode(QQuickPaintedItem *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultcontext.html#createPainterNode

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
    #  QSGPainterNode *QSGDefaultContext::createPainterNode(QQuickPaintedItem
    #      *item)
    ritual = (
        'ritual_ZN17QSGDefaultContext17createPainterNodeEP17QQuickPaintedIt'
        'em')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QSGDefaultContext17createPainterNodeEP17QQuickPai'
          'ntedItem')
    address = self.uglySide.call(ritual, self._addressOf(item))
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
    Calls Qt's 'QSGGlyphNode
    *QSGDefaultContext::createGlyphNode(QSGRenderContext *rc,
    QSGTextNode::RenderType renderType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultcontext.html#createGlyphNode

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
    #  QSGGlyphNode *QSGDefaultContext::createGlyphNode(QSGRenderContext *rc,
    #      QSGTextNode::RenderType renderType)
    ritual = (
        'ritual_ZN17QSGDefaultContext15createGlyphNodeEP16QSGRenderContextN'
        '11QSGTextNode10RenderTypeE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QSGDefaultContext15createGlyphNodeEP16QSGRenderCo'
          'ntextN11QSGTextNode10RenderTypeE')
    address = self.uglySide.call(
        ritual, self._addressOf(rc), renderType.value,
    )
    from . import QSGGlyphNode
    return QSGGlyphNode._cuteAt(address)

  @overload(QSGRenderContext)
  @overload(NoneType)
  def createInternalTextNode(
      self,
      renderContext: Optional[QSGRenderContext],
  ) -> Optional[QSGInternalTextNode]:
    """
    Calls Qt's 'QSGInternalTextNode
    *QSGDefaultContext::createInternalTextNode(QSGRenderContext
    *renderContext)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultcontext.html#createInternalTextNode

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
    #      *QSGDefaultContext::createInternalTextNode(QSGRenderContext
    #      *renderContext)
    ritual = (
        'ritual_ZN17QSGDefaultContext22createInternalTextNodeEP16QSGRenderC'
        'ontext')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QSGDefaultContext22createInternalTextNodeEP16QSGR'
          'enderContext')
    address = self.uglySide.call(ritual, self._addressOf(renderContext))
    from . import QSGInternalTextNode
    return QSGInternalTextNode._cuteAt(address)

  @overload(QSGRenderContext)
  @overload(NoneType)
  def createLayer(
      self,
      renderContext: Optional[QSGRenderContext],
  ) -> Optional[QSGLayer]:
    """
    Calls Qt's 'QSGLayer *QSGDefaultContext::createLayer(QSGRenderContext
    *renderContext)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgdefaultcontext.html#createLayer

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
    #  QSGLayer *QSGDefaultContext::createLayer(QSGRenderContext
    #      *renderContext)
    ritual = 'ritual_ZN17QSGDefaultContext11createLayerEP16QSGRenderContext'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QSGDefaultContext11createLayerEP16QSGRenderContex'
          't')
    address = self.uglySide.call(ritual, self._addressOf(renderContext))
    from . import QSGLayer
    return QSGLayer._cuteAt(address)

  @overload(QSGRenderContext)
  @overload(NoneType)
  def rendererInterface(
      self,
      renderContext: Optional[QSGRenderContext],
  ) -> Optional[QSGRendererInterface]:
    """
    Calls Qt's 'QSGRendererInterface
    *QSGDefaultContext::rendererInterface(QSGRenderContext *renderContext)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultcontext.html#rendererInterface

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
    #  QSGRendererInterface
    #      *QSGDefaultContext::rendererInterface(QSGRenderContext
    #      *renderContext)
    ritual = (
        'ritual_ZN17QSGDefaultContext17rendererInterfaceEP16QSGRenderContex'
        't')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QSGDefaultContext17rendererInterfaceEP16QSGRender'
          'Context')
    address = self.uglySide.call(ritual, self._addressOf(renderContext))
    return QSGRendererInterface._cuteAt(address)

  def createRectangleNode(self) -> Optional[QSGRectangleNode]:
    """
    Calls Qt's 'QSGRectangleNode *QSGDefaultContext::createRectangleNode()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultcontext.html#createRectangleNode

    Returns
    -------

    Optional[QSGRectangleNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGRectangleNode *QSGDefaultContext::createRectangleNode()
    ritual = 'ritual_ZN17QSGDefaultContext19createRectangleNodeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QSGDefaultContext19createRectangleNodeEv'
    address = self.uglySide.call(ritual)
    from . import QSGRectangleNode
    return QSGRectangleNode._cuteAt(address)

  def createImageNode(self) -> Optional[QSGImageNode]:
    """
    Calls Qt's 'QSGImageNode *QSGDefaultContext::createImageNode()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultcontext.html#createImageNode

    Returns
    -------

    Optional[QSGImageNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGImageNode *QSGDefaultContext::createImageNode()
    ritual = 'ritual_ZN17QSGDefaultContext15createImageNodeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QSGDefaultContext15createImageNodeEv'
    address = self.uglySide.call(ritual)
    from . import QSGImageNode
    return QSGImageNode._cuteAt(address)

  def createNinePatchNode(self) -> Optional[QSGNinePatchNode]:
    """
    Calls Qt's 'QSGNinePatchNode *QSGDefaultContext::createNinePatchNode()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultcontext.html#createNinePatchNode

    Returns
    -------

    Optional[QSGNinePatchNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGNinePatchNode *QSGDefaultContext::createNinePatchNode()
    ritual = 'ritual_ZN17QSGDefaultContext19createNinePatchNodeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QSGDefaultContext19createNinePatchNodeEv'
    address = self.uglySide.call(ritual)
    from . import QSGNinePatchNode
    return QSGNinePatchNode._cuteAt(address)

  def createSpriteNode(self) -> Optional[QSGSpriteNode]:
    """
    Calls Qt's 'QSGSpriteNode *QSGDefaultContext::createSpriteNode()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultcontext.html#createSpriteNode

    Returns
    -------

    Optional[QSGSpriteNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGSpriteNode *QSGDefaultContext::createSpriteNode()
    ritual = 'ritual_ZN17QSGDefaultContext16createSpriteNodeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QSGDefaultContext16createSpriteNodeEv'
    address = self.uglySide.call(ritual)
    from . import QSGSpriteNode
    return QSGSpriteNode._cuteAt(address)

  def createGuiThreadShaderEffectManager(
      self,
  ) -> Optional[QSGGuiThreadShaderEffectManager]:
    """
    Calls Qt's 'QSGGuiThreadShaderEffectManager
    *QSGDefaultContext::createGuiThreadShaderEffectManager()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultcontext.html

    Returns
    -------

    Optional[QSGGuiThreadShaderEffectManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGGuiThreadShaderEffectManager
    #      *QSGDefaultContext::createGuiThreadShaderEffectManager()
    ritual = (
        'ritual_ZN17QSGDefaultContext34createGuiThreadShaderEffectManagerEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QSGDefaultContext34createGuiThreadShaderEffectMan'
          'agerEv')
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
    *QSGDefaultContext::createShaderEffectNode(QSGRenderContext
    *renderContext)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultcontext.html#createShaderEffectNode

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
    #      *QSGDefaultContext::createShaderEffectNode(QSGRenderContext
    #      *renderContext)
    ritual = (
        'ritual_ZN17QSGDefaultContext22createShaderEffectNodeEP16QSGRenderC'
        'ontext')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QSGDefaultContext22createShaderEffectNodeEP16QSGR'
          'enderContext')
    address = self.uglySide.call(ritual, self._addressOf(renderContext))
    from . import QSGShaderEffectNode
    return QSGShaderEffectNode._cuteAt(address)

  @overload(QSGTextNode.RenderType)
  def processTextRenderType(
      self,
      renderType: QSGTextNode.RenderType,
  ) -> QSGTextNode.RenderType:
    """
    Calls Qt's 'QSGTextNode::RenderType
    QSGDefaultContext::processTextRenderType(QSGTextNode::RenderType
    renderType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultcontext.html#processTextRenderType

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
    #      QSGDefaultContext::processTextRenderType(QSGTextNode::RenderType
    #      renderType)
    ritual = (
        'ritual_ZN17QSGDefaultContext21processTextRenderTypeEN11QSGTextNode'
        '10RenderTypeE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QSGDefaultContext21processTextRenderTypeEN11QSGTe'
          'xtNode10RenderTypeE')
    return QSGTextNode.RenderType(self.uglySide.call(
        ritual, renderType.value,
    ))
