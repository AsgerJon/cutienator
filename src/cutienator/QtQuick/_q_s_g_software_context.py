"""
QSGSoftwareContext binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsgsoftwarecontext_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QSGSoftwareContext to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QSGContext, QSGRendererInterface, QSGTextNode

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QSurfaceFormat
  from . import QQuickPaintedItem, QSGGlyphNode, QSGImageNode
  from . import QSGInternalImageNode, QSGInternalRectangleNode, QSGLayer
  from . import QSGNinePatchNode, QSGPainterNode, QSGRectangleNode
  from . import QSGRenderContext, QSGSpriteNode
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickPaintedItem = WAIT['QQuickPaintedItem']
  QSGRenderContext = WAIT['QSGRenderContext']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSGSoftwareContext(QSGContext, QSGRendererInterface):
  """
  The cute side of Qt's QSGSoftwareContext: a plain Python object standing in
  front of one C++ QSGSoftwareContext.

  It is built on the cute 'QSGContext', as Qt's QSGSoftwareContext is built
  on Qt's QSGContext, and has everything that class has. It is built on the
  cute 'QSGRendererInterface' as well, as Qt's QSGSoftwareContext is built on
  Qt's QSGRendererInterface too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSGSoftwareContext that has a ritual and that Python
  can call so far, 18 names in all: 'metaObject', 'createRenderContext',
  'createInternalRectangleNode', 'createInternalImageNode',
  'createPainterNode', 'createGlyphNode', 'createLayer',
  'defaultSurfaceFormat', 'rendererInterface', 'createRectangleNode',
  'createImageNode', 'createNinePatchNode', 'createSpriteNode',
  'processTextRenderType', 'graphicsApi', 'shaderType',
  'shaderCompilationType', 'shaderSourceType'. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QSGSoftwareContext::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QSGSoftwareContext::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'void *QSGSoftwareContext::getResource(QQuickWindow *window,
    Resource resource) const': gives 'void', which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 25 functions Qt declares: 2 not a gap; 2 leans on
  'QSGSoftwareContext.

  What to expect
  --------------

  - The C++ QSGSoftwareContext is created at the first use, not by
    'QSGSoftwareContext(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGSoftwareContext.
  - Qt tells when it has removed the C++ QSGSoftwareContext. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QSGSoftwareContext that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGSoftwareContext'

  #  Qt's QSGSoftwareContext is built on more than one class. The part of a
  #  C++ QSGSoftwareContext that belongs to a class after the first begins
  #  somewhere inside the object, and the ritual named for that class gives
  #  where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QSGRendererInterface':
          'ritual_cast_QSGSoftwareContext_QSGRendererInterface',
  }

  #  A C++ QSGSoftwareContext Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSGSoftwareContext'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QSGSoftwareContext::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgsoftwarecontext.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QSGSoftwareContext::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QSGSoftwareContext10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def defaultSurfaceFormat(self) -> QSurfaceFormat:
    """
    Calls Qt's 'QSurfaceFormat QSGSoftwareContext::defaultSurfaceFormat()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarecontext.html#defaultSurfaceFormat

    Returns
    -------

    QSurfaceFormat
      A new cute QSurfaceFormat around the copy Qt gave back. Python owns it.
    """
    #  QSurfaceFormat QSGSoftwareContext::defaultSurfaceFormat() const
    ritual = 'ritual_ZNK18QSGSoftwareContext20defaultSurfaceFormatEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18QSGSoftwareContext20defaultSurfaceFormatEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QSurfaceFormat
    return QSurfaceFormat._cuteOwning(address)

  def graphicsApi(self) -> QSGRendererInterface.GraphicsApi:
    """
    Calls Qt's 'GraphicsApi QSGSoftwareContext::graphicsApi() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarecontext.html#graphicsApi

    Returns
    -------

    QSGRendererInterface.GraphicsApi
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QSGRendererInterface.GraphicsApi(number)' gives.
    """
    #  GraphicsApi QSGSoftwareContext::graphicsApi() const
    ritual = 'ritual_ZNK18QSGSoftwareContext11graphicsApiEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18QSGSoftwareContext11graphicsApiEv'
    return QSGRendererInterface.GraphicsApi(self.uglySide.call(ritual))

  def shaderType(self) -> QSGRendererInterface.ShaderType:
    """
    Calls Qt's 'ShaderType QSGSoftwareContext::shaderType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgsoftwarecontext.html#shaderType

    Returns
    -------

    QSGRendererInterface.ShaderType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QSGRendererInterface.ShaderType(number)' gives.
    """
    #  ShaderType QSGSoftwareContext::shaderType() const
    ritual = 'ritual_ZNK18QSGSoftwareContext10shaderTypeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18QSGSoftwareContext10shaderTypeEv'
    return QSGRendererInterface.ShaderType(self.uglySide.call(ritual))

  def shaderCompilationType(
      self,
  ) -> QSGRendererInterface.ShaderCompilationTypes:
    """
    Calls Qt's 'ShaderCompilationTypes
    QSGSoftwareContext::shaderCompilationType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarecontext.html#shaderCompilationType

    Returns
    -------

    QSGRendererInterface.ShaderCompilationTypes
      The value standing for the combination Qt gave back.
    """
    #  ShaderCompilationTypes QSGSoftwareContext::shaderCompilationType()
    #      const
    ritual = 'ritual_ZNK18QSGSoftwareContext21shaderCompilationTypeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18QSGSoftwareContext21shaderCompilationTypeEv'
    return QSGRendererInterface.ShaderCompilationTypes(self.uglySide.call(
        ritual,
    ))

  def shaderSourceType(self) -> QSGRendererInterface.ShaderSourceTypes:
    """
    Calls Qt's 'ShaderSourceTypes QSGSoftwareContext::shaderSourceType()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarecontext.html#shaderSourceType

    Returns
    -------

    QSGRendererInterface.ShaderSourceTypes
      The value standing for the combination Qt gave back.
    """
    #  ShaderSourceTypes QSGSoftwareContext::shaderSourceType() const
    ritual = 'ritual_ZNK18QSGSoftwareContext16shaderSourceTypeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18QSGSoftwareContext16shaderSourceTypeEv'
    return QSGRendererInterface.ShaderSourceTypes(self.uglySide.call(ritual))

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
    Qt's 'QSGSoftwareContext::QSGSoftwareContext(QObject *parent)': leans on
    'QSGSoftwareContext::qt_metacall(QMetaObject::Call, int, void**)', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QSGSoftwareContext.__init__' has no cute function yet. Qt's "
        "'QSGSoftwareContext::QSGSoftwareContext(QObject *parent)': leans "
        "on 'QSGSoftwareContext::qt_metacall(QMetaObject::Call, int, "
        "void**)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

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

  def createRenderContext(self) -> Optional[QSGRenderContext]:
    """
    Calls Qt's 'QSGRenderContext *QSGSoftwareContext::createRenderContext()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarecontext.html#createRenderContext

    Returns
    -------

    Optional[QSGRenderContext]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGRenderContext *QSGSoftwareContext::createRenderContext()
    address = self.uglySide.call(
        'ritual_ZN18QSGSoftwareContext19createRenderContextEv',
    )
    from . import QSGRenderContext
    return QSGRenderContext._cuteAt(address)

  def createInternalRectangleNode(
      self,
  ) -> Optional[QSGInternalRectangleNode]:
    """
    Calls Qt's 'QSGInternalRectangleNode
    *QSGSoftwareContext::createInternalRectangleNode()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarecontext.html

    Returns
    -------

    Optional[QSGInternalRectangleNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGInternalRectangleNode
    #      *QSGSoftwareContext::createInternalRectangleNode()
    address = self.uglySide.call(
        'ritual_ZN18QSGSoftwareContext27createInternalRectangleNodeEv',
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
    *QSGSoftwareContext::createInternalImageNode(QSGRenderContext
    *renderContext)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarecontext.html#createInternalImageNode

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
    #      *QSGSoftwareContext::createInternalImageNode(QSGRenderContext
    #      *renderContext)
    address = self.uglySide.call(
        'ritual_ZN18QSGSoftwareContext23createInternalImageNodeEP16QSGRende'
        'rContext',
        self._addressOf(renderContext),
    )
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
    *QSGSoftwareContext::createPainterNode(QQuickPaintedItem *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarecontext.html#createPainterNode

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
    #  QSGPainterNode
    #      *QSGSoftwareContext::createPainterNode(QQuickPaintedItem *item)
    address = self.uglySide.call(
        'ritual_ZN18QSGSoftwareContext17createPainterNodeEP17QQuickPaintedI'
        'tem',
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
    Calls Qt's 'QSGGlyphNode
    *QSGSoftwareContext::createGlyphNode(QSGRenderContext *rc,
    QSGTextNode::RenderType renderType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarecontext.html#createGlyphNode

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
    #  QSGGlyphNode *QSGSoftwareContext::createGlyphNode(QSGRenderContext
    #      *rc, QSGTextNode::RenderType renderType)
    ritual = (
        'ritual_ZN18QSGSoftwareContext15createGlyphNodeEP16QSGRenderContext'
        'N11QSGTextNode10RenderTypeE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QSGSoftwareContext15createGlyphNodeEP16QSGRenderC'
          'ontextN11QSGTextNode10RenderTypeE')
    address = self.uglySide.call(
        ritual, self._addressOf(rc), renderType.value,
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
    Calls Qt's 'QSGLayer *QSGSoftwareContext::createLayer(QSGRenderContext
    *renderContext)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarecontext.html#createLayer

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
    #  QSGLayer *QSGSoftwareContext::createLayer(QSGRenderContext
    #      *renderContext)
    address = self.uglySide.call(
        'ritual_ZN18QSGSoftwareContext11createLayerEP16QSGRenderContext',
        self._addressOf(renderContext),
    )
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
    *QSGSoftwareContext::rendererInterface(QSGRenderContext *renderContext)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarecontext.html#rendererInterface

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
    #      *QSGSoftwareContext::rendererInterface(QSGRenderContext
    #      *renderContext)
    ritual = (
        'ritual_ZN18QSGSoftwareContext17rendererInterfaceEP16QSGRenderConte'
        'xt')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QSGSoftwareContext17rendererInterfaceEP16QSGRende'
          'rContext')
    address = self.uglySide.call(ritual, self._addressOf(renderContext))
    return QSGRendererInterface._cuteAt(address)

  def createRectangleNode(self) -> Optional[QSGRectangleNode]:
    """
    Calls Qt's 'QSGRectangleNode *QSGSoftwareContext::createRectangleNode()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarecontext.html#createRectangleNode

    Returns
    -------

    Optional[QSGRectangleNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGRectangleNode *QSGSoftwareContext::createRectangleNode()
    ritual = 'ritual_ZN18QSGSoftwareContext19createRectangleNodeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QSGSoftwareContext19createRectangleNodeEv'
    address = self.uglySide.call(ritual)
    from . import QSGRectangleNode
    return QSGRectangleNode._cuteAt(address)

  def createImageNode(self) -> Optional[QSGImageNode]:
    """
    Calls Qt's 'QSGImageNode *QSGSoftwareContext::createImageNode()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarecontext.html#createImageNode

    Returns
    -------

    Optional[QSGImageNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGImageNode *QSGSoftwareContext::createImageNode()
    ritual = 'ritual_ZN18QSGSoftwareContext15createImageNodeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QSGSoftwareContext15createImageNodeEv'
    address = self.uglySide.call(ritual)
    from . import QSGImageNode
    return QSGImageNode._cuteAt(address)

  def createNinePatchNode(self) -> Optional[QSGNinePatchNode]:
    """
    Calls Qt's 'QSGNinePatchNode *QSGSoftwareContext::createNinePatchNode()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarecontext.html#createNinePatchNode

    Returns
    -------

    Optional[QSGNinePatchNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGNinePatchNode *QSGSoftwareContext::createNinePatchNode()
    address = self.uglySide.call(
        'ritual_ZN18QSGSoftwareContext19createNinePatchNodeEv',
    )
    from . import QSGNinePatchNode
    return QSGNinePatchNode._cuteAt(address)

  def createSpriteNode(self) -> Optional[QSGSpriteNode]:
    """
    Calls Qt's 'QSGSpriteNode *QSGSoftwareContext::createSpriteNode()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarecontext.html#createSpriteNode

    Returns
    -------

    Optional[QSGSpriteNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGSpriteNode *QSGSoftwareContext::createSpriteNode()
    address = self.uglySide.call(
        'ritual_ZN18QSGSoftwareContext16createSpriteNodeEv',
    )
    from . import QSGSpriteNode
    return QSGSpriteNode._cuteAt(address)

  @overload(QSGTextNode.RenderType)
  def processTextRenderType(
      self,
      renderType: QSGTextNode.RenderType,
  ) -> QSGTextNode.RenderType:
    """
    Calls Qt's 'QSGTextNode::RenderType
    QSGSoftwareContext::processTextRenderType(QSGTextNode::RenderType
    renderType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarecontext.html#processTextRenderType

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
    #      QSGSoftwareContext::processTextRenderType(QSGTextNode::RenderType
    #      renderType)
    ritual = (
        'ritual_ZN18QSGSoftwareContext21processTextRenderTypeEN11QSGTextNod'
        'e10RenderTypeE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QSGSoftwareContext21processTextRenderTypeEN11QSGT'
          'extNode10RenderTypeE')
    return QSGTextNode.RenderType(self.uglySide.call(
        ritual, renderType.value,
    ))
