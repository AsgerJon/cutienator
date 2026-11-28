"""
QSGSoftwareRenderListBuilder binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsgsoftwarerenderlistbuilder_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QSGSoftwareRenderListBuilder to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QSGNodeVisitorEx

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QSGAbstractSoftwareRenderer, QSGClipNode, QSGGeometryNode
  from . import QSGGlyphNode, QSGInternalImageNode, QSGInternalRectangleNode
  from . import QSGNode, QSGOpacityNode, QSGPainterNode, QSGRenderNode
  from . import QSGRootNode, QSGSpriteNode, QSGTransformNode
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSGAbstractSoftwareRenderer = WAIT['QSGAbstractSoftwareRenderer']
  QSGClipNode = WAIT['QSGClipNode']
  QSGGeometryNode = WAIT['QSGGeometryNode']
  QSGGlyphNode = WAIT['QSGGlyphNode']
  QSGInternalImageNode = WAIT['QSGInternalImageNode']
  QSGInternalRectangleNode = WAIT['QSGInternalRectangleNode']
  QSGNode = WAIT['QSGNode']
  QSGOpacityNode = WAIT['QSGOpacityNode']
  QSGPainterNode = WAIT['QSGPainterNode']
  QSGRenderNode = WAIT['QSGRenderNode']
  QSGRootNode = WAIT['QSGRootNode']
  QSGSpriteNode = WAIT['QSGSpriteNode']
  QSGTransformNode = WAIT['QSGTransformNode']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSGSoftwareRenderListBuilder(QSGNodeVisitorEx):
  """
  The cute side of Qt's QSGSoftwareRenderListBuilder: a plain Python object
  standing in front of one C++ QSGSoftwareRenderListBuilder.

  It is built on the cute 'QSGNodeVisitorEx', as Qt's
  QSGSoftwareRenderListBuilder is built on Qt's QSGNodeVisitorEx, and has
  everything that class has.

  C++ hands a QSGSoftwareRenderListBuilder around as a copy, so every C++
  QSGSoftwareRenderListBuilder behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QSGSoftwareRenderListBuilder that has a ritual and
  that Python can call so far, 3 names in all: 'visit', 'endVisit',
  'addRenderableNode'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSGSoftwareRenderListBuilder::~QSGSoftwareRenderListBuilder()': the
    destructor: Python removes its C++ QSGSoftwareRenderListBuilder by it,
    and has no other use for it.

  What to expect
  --------------

  - The C++ QSGSoftwareRenderListBuilder is created at the first use, not by
    'QSGSoftwareRenderListBuilder(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSGSoftwareRenderListBuilder back gives a copy the
    ritual made for Python, in a new cute QSGSoftwareRenderListBuilder.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGSoftwareRenderListBuilder'

  #  Qt's '~QSGSoftwareRenderListBuilder()'. Naming it makes this a value
  #  class: Python owns every C++ QSGSoftwareRenderListBuilder behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN28QSGSoftwareRenderListBuilderD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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

  @overload(QSGAbstractSoftwareRenderer)
  @overload(NoneType)
  def __init__(
      self,
      renderer: Optional[QSGAbstractSoftwareRenderer],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QSGSoftwareRenderListBuilder::QSGSoftwareRenderListBuilder(
    QSGAbstractSoftwareRenderer *renderer)', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarerenderlistbuilder.html

    Parameters
    ----------

    renderer : Optional[QSGAbstractSoftwareRenderer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QSGSoftwareRenderListBuilder::QSGSoftwareRenderListBuilder(
    #      QSGAbstractSoftwareRenderer *renderer)
    self._noteCreation(QSGSoftwareRenderListBuilder, lambda: Rituals.call(
        'ritual_ZN28QSGSoftwareRenderListBuilderC1EP27QSGAbstractSoftwareRe'
        'nderer',
        self._addressOf(renderer),
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

  @overload(QSGTransformNode)
  @overload(NoneType)
  def visit(self, a0: Optional[QSGTransformNode]) -> bool:
    """
    Calls Qt's 'bool QSGSoftwareRenderListBuilder::visit(QSGTransformNode
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarerenderlistbuilder.html#visit

    Parameters
    ----------

    a0 : Optional[QSGTransformNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QSGSoftwareRenderListBuilder::visit(QSGTransformNode *a0)
    ritual = (
        'ritual_ZN28QSGSoftwareRenderListBuilder5visitEP16QSGTransformNode')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN28QSGSoftwareRenderListBuilder5visitEP16QSGTransfor'
          'mNode')
    return self.uglySide.call(
        ritual, self._addressOf(a0, 'QSGTransformNode'),
    )

  @overload(QSGClipNode)
  def visit(self, a0: Optional[QSGClipNode]) -> bool:
    """
    Calls Qt's 'bool QSGSoftwareRenderListBuilder::visit(QSGClipNode *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarerenderlistbuilder.html#visit

    Parameters
    ----------

    a0 : Optional[QSGClipNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QSGSoftwareRenderListBuilder::visit(QSGClipNode *a0)
    ritual = 'ritual_ZN28QSGSoftwareRenderListBuilder5visitEP11QSGClipNode'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN28QSGSoftwareRenderListBuilder5visitEP11QSGClipNode')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QSGInternalImageNode)
  def visit(self, a0: Optional[QSGInternalImageNode]) -> bool:
    """
    Calls Qt's 'bool QSGSoftwareRenderListBuilder::visit(QSGInternalImageNode
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarerenderlistbuilder.html#visit

    Parameters
    ----------

    a0 : Optional[QSGInternalImageNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QSGSoftwareRenderListBuilder::visit(QSGInternalImageNode *a0)
    ritual = (
        'ritual_ZN28QSGSoftwareRenderListBuilder5visitEP20QSGInternalImageN'
        'ode')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN28QSGSoftwareRenderListBuilder5visitEP20QSGInternal'
          'ImageNode')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QSGPainterNode)
  def visit(self, a0: Optional[QSGPainterNode]) -> bool:
    """
    Calls Qt's 'bool QSGSoftwareRenderListBuilder::visit(QSGPainterNode
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarerenderlistbuilder.html#visit

    Parameters
    ----------

    a0 : Optional[QSGPainterNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QSGSoftwareRenderListBuilder::visit(QSGPainterNode *a0)
    ritual = (
        'ritual_ZN28QSGSoftwareRenderListBuilder5visitEP14QSGPainterNode')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN28QSGSoftwareRenderListBuilder5visitEP14QSGPainterN'
          'ode')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QSGInternalRectangleNode)
  def visit(self, a0: Optional[QSGInternalRectangleNode]) -> bool:
    """
    Calls Qt's 'bool
    QSGSoftwareRenderListBuilder::visit(QSGInternalRectangleNode *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarerenderlistbuilder.html#visit

    Parameters
    ----------

    a0 : Optional[QSGInternalRectangleNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QSGSoftwareRenderListBuilder::visit(QSGInternalRectangleNode *a0)
    ritual = (
        'ritual_ZN28QSGSoftwareRenderListBuilder5visitEP24QSGInternalRectan'
        'gleNode')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN28QSGSoftwareRenderListBuilder5visitEP24QSGInternal'
          'RectangleNode')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QSGGlyphNode)
  def visit(self, a0: Optional[QSGGlyphNode]) -> bool:
    """
    Calls Qt's 'bool QSGSoftwareRenderListBuilder::visit(QSGGlyphNode *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarerenderlistbuilder.html#visit

    Parameters
    ----------

    a0 : Optional[QSGGlyphNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QSGSoftwareRenderListBuilder::visit(QSGGlyphNode *a0)
    ritual = 'ritual_ZN28QSGSoftwareRenderListBuilder5visitEP12QSGGlyphNode'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN28QSGSoftwareRenderListBuilder5visitEP12QSGGlyphNod'
          'e')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QSGSpriteNode)
  def visit(self, a0: Optional[QSGSpriteNode]) -> bool:
    """
    Calls Qt's 'bool QSGSoftwareRenderListBuilder::visit(QSGSpriteNode *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarerenderlistbuilder.html#visit

    Parameters
    ----------

    a0 : Optional[QSGSpriteNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QSGSoftwareRenderListBuilder::visit(QSGSpriteNode *a0)
    ritual = 'ritual_ZN28QSGSoftwareRenderListBuilder5visitEP13QSGSpriteNode'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN28QSGSoftwareRenderListBuilder5visitEP13QSGSpriteNo'
          'de')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QSGGeometryNode)
  def visit(self, a0: Optional[QSGGeometryNode]) -> bool:
    """
    Calls Qt's 'bool QSGSoftwareRenderListBuilder::visit(QSGGeometryNode
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarerenderlistbuilder.html#visit

    Parameters
    ----------

    a0 : Optional[QSGGeometryNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QSGSoftwareRenderListBuilder::visit(QSGGeometryNode *a0)
    ritual = (
        'ritual_ZN28QSGSoftwareRenderListBuilder5visitEP15QSGGeometryNode')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN28QSGSoftwareRenderListBuilder5visitEP15QSGGeometry'
          'Node')
    return self.uglySide.call(ritual, self._addressOf(a0, 'QSGGeometryNode'))

  @overload(QSGOpacityNode)
  def visit(self, a0: Optional[QSGOpacityNode]) -> bool:
    """
    Calls Qt's 'bool QSGSoftwareRenderListBuilder::visit(QSGOpacityNode
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarerenderlistbuilder.html#visit

    Parameters
    ----------

    a0 : Optional[QSGOpacityNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QSGSoftwareRenderListBuilder::visit(QSGOpacityNode *a0)
    ritual = (
        'ritual_ZN28QSGSoftwareRenderListBuilder5visitEP14QSGOpacityNode')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN28QSGSoftwareRenderListBuilder5visitEP14QSGOpacityN'
          'ode')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QSGRootNode)
  def visit(self, a0: Optional[QSGRootNode]) -> bool:
    """
    Calls Qt's 'bool QSGSoftwareRenderListBuilder::visit(QSGRootNode *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarerenderlistbuilder.html#visit

    Parameters
    ----------

    a0 : Optional[QSGRootNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QSGSoftwareRenderListBuilder::visit(QSGRootNode *a0)
    ritual = 'ritual_ZN28QSGSoftwareRenderListBuilder5visitEP11QSGRootNode'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN28QSGSoftwareRenderListBuilder5visitEP11QSGRootNode')
    return self.uglySide.call(ritual, self._addressOf(a0, 'QSGRootNode'))

  @overload(QSGRenderNode)
  def visit(self, a0: Optional[QSGRenderNode]) -> bool:
    """
    Calls Qt's 'bool QSGSoftwareRenderListBuilder::visit(QSGRenderNode *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarerenderlistbuilder.html#visit

    Parameters
    ----------

    a0 : Optional[QSGRenderNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QSGSoftwareRenderListBuilder::visit(QSGRenderNode *a0)
    ritual = 'ritual_ZN28QSGSoftwareRenderListBuilder5visitEP13QSGRenderNode'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN28QSGSoftwareRenderListBuilder5visitEP13QSGRenderNo'
          'de')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QSGTransformNode)
  @overload(NoneType)
  def endVisit(self, a0: Optional[QSGTransformNode]) -> None:
    """
    Calls Qt's 'void QSGSoftwareRenderListBuilder::endVisit(QSGTransformNode
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarerenderlistbuilder.html#endVisit

    Parameters
    ----------

    a0 : Optional[QSGTransformNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGSoftwareRenderListBuilder::endVisit(QSGTransformNode *a0)
    ritual = (
        'ritual_ZN28QSGSoftwareRenderListBuilder8endVisitEP16QSGTransformNo'
        'de')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN28QSGSoftwareRenderListBuilder8endVisitEP16QSGTrans'
          'formNode')
    self.uglySide.call(ritual, self._addressOf(a0, 'QSGTransformNode'))

  @overload(QSGClipNode)
  def endVisit(self, a0: Optional[QSGClipNode]) -> None:
    """
    Calls Qt's 'void QSGSoftwareRenderListBuilder::endVisit(QSGClipNode
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarerenderlistbuilder.html#endVisit

    Parameters
    ----------

    a0 : Optional[QSGClipNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGSoftwareRenderListBuilder::endVisit(QSGClipNode *a0)
    ritual = (
        'ritual_ZN28QSGSoftwareRenderListBuilder8endVisitEP11QSGClipNode')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN28QSGSoftwareRenderListBuilder8endVisitEP11QSGClipN'
          'ode')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QSGInternalImageNode)
  def endVisit(self, a0: Optional[QSGInternalImageNode]) -> None:
    """
    Calls Qt's 'void
    QSGSoftwareRenderListBuilder::endVisit(QSGInternalImageNode *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarerenderlistbuilder.html#endVisit

    Parameters
    ----------

    a0 : Optional[QSGInternalImageNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGSoftwareRenderListBuilder::endVisit(QSGInternalImageNode *a0)
    ritual = (
        'ritual_ZN28QSGSoftwareRenderListBuilder8endVisitEP20QSGInternalIma'
        'geNode')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN28QSGSoftwareRenderListBuilder8endVisitEP20QSGInter'
          'nalImageNode')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QSGPainterNode)
  def endVisit(self, a0: Optional[QSGPainterNode]) -> None:
    """
    Calls Qt's 'void QSGSoftwareRenderListBuilder::endVisit(QSGPainterNode
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarerenderlistbuilder.html#endVisit

    Parameters
    ----------

    a0 : Optional[QSGPainterNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGSoftwareRenderListBuilder::endVisit(QSGPainterNode *a0)
    ritual = (
        'ritual_ZN28QSGSoftwareRenderListBuilder8endVisitEP14QSGPainterNode')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN28QSGSoftwareRenderListBuilder8endVisitEP14QSGPaint'
          'erNode')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QSGInternalRectangleNode)
  def endVisit(self, a0: Optional[QSGInternalRectangleNode]) -> None:
    """
    Calls Qt's 'void
    QSGSoftwareRenderListBuilder::endVisit(QSGInternalRectangleNode *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarerenderlistbuilder.html#endVisit

    Parameters
    ----------

    a0 : Optional[QSGInternalRectangleNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGSoftwareRenderListBuilder::endVisit(QSGInternalRectangleNode
    #      *a0)
    ritual = (
        'ritual_ZN28QSGSoftwareRenderListBuilder8endVisitEP24QSGInternalRec'
        'tangleNode')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN28QSGSoftwareRenderListBuilder8endVisitEP24QSGInter'
          'nalRectangleNode')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QSGGlyphNode)
  def endVisit(self, a0: Optional[QSGGlyphNode]) -> None:
    """
    Calls Qt's 'void QSGSoftwareRenderListBuilder::endVisit(QSGGlyphNode
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarerenderlistbuilder.html#endVisit

    Parameters
    ----------

    a0 : Optional[QSGGlyphNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGSoftwareRenderListBuilder::endVisit(QSGGlyphNode *a0)
    ritual = (
        'ritual_ZN28QSGSoftwareRenderListBuilder8endVisitEP12QSGGlyphNode')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN28QSGSoftwareRenderListBuilder8endVisitEP12QSGGlyph'
          'Node')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QSGSpriteNode)
  def endVisit(self, a0: Optional[QSGSpriteNode]) -> None:
    """
    Calls Qt's 'void QSGSoftwareRenderListBuilder::endVisit(QSGSpriteNode
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarerenderlistbuilder.html#endVisit

    Parameters
    ----------

    a0 : Optional[QSGSpriteNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGSoftwareRenderListBuilder::endVisit(QSGSpriteNode *a0)
    ritual = (
        'ritual_ZN28QSGSoftwareRenderListBuilder8endVisitEP13QSGSpriteNode')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN28QSGSoftwareRenderListBuilder8endVisitEP13QSGSprit'
          'eNode')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QSGGeometryNode)
  def endVisit(self, a0: Optional[QSGGeometryNode]) -> None:
    """
    Calls Qt's 'void QSGSoftwareRenderListBuilder::endVisit(QSGGeometryNode
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarerenderlistbuilder.html#endVisit

    Parameters
    ----------

    a0 : Optional[QSGGeometryNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGSoftwareRenderListBuilder::endVisit(QSGGeometryNode *a0)
    ritual = (
        'ritual_ZN28QSGSoftwareRenderListBuilder8endVisitEP15QSGGeometryNod'
        'e')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN28QSGSoftwareRenderListBuilder8endVisitEP15QSGGeome'
          'tryNode')
    self.uglySide.call(ritual, self._addressOf(a0, 'QSGGeometryNode'))

  @overload(QSGOpacityNode)
  def endVisit(self, a0: Optional[QSGOpacityNode]) -> None:
    """
    Calls Qt's 'void QSGSoftwareRenderListBuilder::endVisit(QSGOpacityNode
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarerenderlistbuilder.html#endVisit

    Parameters
    ----------

    a0 : Optional[QSGOpacityNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGSoftwareRenderListBuilder::endVisit(QSGOpacityNode *a0)
    ritual = (
        'ritual_ZN28QSGSoftwareRenderListBuilder8endVisitEP14QSGOpacityNode')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN28QSGSoftwareRenderListBuilder8endVisitEP14QSGOpaci'
          'tyNode')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QSGRootNode)
  def endVisit(self, a0: Optional[QSGRootNode]) -> None:
    """
    Calls Qt's 'void QSGSoftwareRenderListBuilder::endVisit(QSGRootNode
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarerenderlistbuilder.html#endVisit

    Parameters
    ----------

    a0 : Optional[QSGRootNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGSoftwareRenderListBuilder::endVisit(QSGRootNode *a0)
    ritual = (
        'ritual_ZN28QSGSoftwareRenderListBuilder8endVisitEP11QSGRootNode')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN28QSGSoftwareRenderListBuilder8endVisitEP11QSGRootN'
          'ode')
    self.uglySide.call(ritual, self._addressOf(a0, 'QSGRootNode'))

  @overload(QSGRenderNode)
  def endVisit(self, a0: Optional[QSGRenderNode]) -> None:
    """
    Calls Qt's 'void QSGSoftwareRenderListBuilder::endVisit(QSGRenderNode
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarerenderlistbuilder.html#endVisit

    Parameters
    ----------

    a0 : Optional[QSGRenderNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGSoftwareRenderListBuilder::endVisit(QSGRenderNode *a0)
    ritual = (
        'ritual_ZN28QSGSoftwareRenderListBuilder8endVisitEP13QSGRenderNode')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN28QSGSoftwareRenderListBuilder8endVisitEP13QSGRende'
          'rNode')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QSGNode)
  @overload(NoneType)
  def addRenderableNode(self, node: Optional[QSGNode]) -> bool:
    """
    Calls Qt's 'bool QSGSoftwareRenderListBuilder::addRenderableNode(QSGNode
    *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarerenderlistbuilder.html

    Parameters
    ----------

    node : Optional[QSGNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QSGSoftwareRenderListBuilder::addRenderableNode(QSGNode *node)
    return self.uglySide.call(
        'ritual_ZN28QSGSoftwareRenderListBuilder17addRenderableNodeEP7QSGNo'
        'de',
        self._addressOf(node, 'QSGNode'),
    )
