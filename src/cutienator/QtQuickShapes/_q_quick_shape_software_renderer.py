"""
QQuickShapeSoftwareRenderer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickShapes/6.12.0/QtQuickShapes/private/qquickshapesoftwarerenderer_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickShapeSoftwareRenderer to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum, WAIT
from . import QQuickAbstractPathRenderer, QQuickShapePath

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QQuickShapeGradient, QQuickShapeSoftwareRenderNode
  from ..QtGui import QColor, QPainterPath
  from ..QtQuick import QQuickItem, QQuickWindow, QSGTransform
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QPainterPath = WAIT['QPainterPath']
  QQuickItem = WAIT['QQuickItem']
  QQuickShapeGradient = WAIT['QQuickShapeGradient']
  QQuickShapeSoftwareRenderNode = WAIT['QQuickShapeSoftwareRenderNode']
  QQuickWindow = WAIT['QQuickWindow']
  QSGTransform = WAIT['QSGTransform']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickShapeSoftwareRenderer(QQuickAbstractPathRenderer):
  """
  The cute side of Qt's QQuickShapeSoftwareRenderer: a plain Python object
  standing in front of one C++ QQuickShapeSoftwareRenderer.

  It is built on the cute 'QQuickAbstractPathRenderer', as Qt's
  QQuickShapeSoftwareRenderer is built on Qt's QQuickAbstractPathRenderer,
  and has everything that class has.

  C++ hands a QQuickShapeSoftwareRenderer around as a copy, so every C++
  QQuickShapeSoftwareRenderer behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QQuickShapeSoftwareRenderer that has a ritual and
  that Python can call so far, 17 names in all: 'setPath', 'setStrokeColor',
  'setStrokeWidth', 'setCosmeticStroke', 'setFillColor', 'setFillRule',
  'setJoinStyle', 'setCapStyle', 'setFillGradient', 'setStrokeGradient',
  'setFillTextureProvider', 'setFillTransform', 'setTriangulationScale',
  'endSync', 'handleSceneChange', 'updateNode', 'setNode'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QQuickShapeSoftwareRenderer::beginSync(int totalCount, bool
    *countChanged)': takes a number to change where it is.
  - Qt's 'void QQuickShapeSoftwareRenderer::setStrokeStyle(int index,
    QQuickShapePath::StrokeStyle strokeStyle, qreal dashOffset, const
    QList<qreal> &dashPattern)': takes a type Python has no way to hand over
    yet.
  - Qt's 'QQuickShapeSoftwareRenderer::~QQuickShapeSoftwareRenderer()': the
    destructor: Python removes its C++ QQuickShapeSoftwareRenderer by it, and
    has no other use for it.

  What to expect
  --------------

  - The C++ QQuickShapeSoftwareRenderer is created at the first use, not by
    'QQuickShapeSoftwareRenderer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQuickShapeSoftwareRenderer back gives a copy the
    ritual made for Python, in a new cute QQuickShapeSoftwareRenderer.
  """

  #  The enums Qt writes inside QQuickShapeSoftwareRenderer, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class Dirty(CuteNum):
    """
    The enum 'QQuickShapeSoftwareRenderer::Dirty' of Qt, with the 5 names Qt
    gives in it.
    """

    DirtyPath = Kee[int](1)
    DirtyPen = Kee[int](2)
    DirtyFillRule = Kee[int](4)
    DirtyBrush = Kee[int](8)
    DirtyList = Kee[int](16)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickShapeSoftwareRenderer'

  #  Qt's '~QQuickShapeSoftwareRenderer()'. Naming it makes this a value
  #  class: Python owns every C++ QQuickShapeSoftwareRenderer behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN27QQuickShapeSoftwareRendererD1Ev'

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

  @overload(int, QPainterPath)
  @overload(int, QPainterPath, QQuickShapePath.PathHints)
  def setPath(
      self,
      index: int,
      path: QPainterPath,
      pathHints: QQuickShapePath.PathHints = QQuickShapePath.PathHints(),
  ) -> None:
    """
    Calls Qt's 'void QQuickShapeSoftwareRenderer::setPath(int index, const
    QPainterPath &path, QQuickShapePath::PathHints pathHints)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapesoftwarerenderer.html#setPath

    Parameters
    ----------

    index : int
      Passed on as it is.

    path : QPainterPath
      Passed on as a value: Qt reads the C++ QPainterPath, which stays
      Python's own.

    pathHints : QQuickShapePath.PathHints
      Passed on as its number. May be left out, as in Qt: it is then
      QQuickShapePath.PathHints().
    """
    #  void QQuickShapeSoftwareRenderer::setPath(int index, const
    #      QPainterPath &path, QQuickShapePath::PathHints pathHints)
    ritual = (
        'ritual_ZN27QQuickShapeSoftwareRenderer7setPathEiRK12QPainterPath6Q'
        'FlagsIN15QQuickShapePath8PathHintEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN27QQuickShapeSoftwareRenderer7setPathEiRK12QPainter'
          'Path6QFlagsIN15QQuickShapePath8PathHintEE')
    self.uglySide.call(ritual, index, self._valueOf(path), pathHints.value)

  @overload(int, QColor)
  def setStrokeColor(self, index: int, color: QColor) -> None:
    """
    Calls Qt's 'void QQuickShapeSoftwareRenderer::setStrokeColor(int index,
    const QColor &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapesoftwarerenderer.html#setStrokeColor

    Parameters
    ----------

    index : int
      Passed on as it is.

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickShapeSoftwareRenderer::setStrokeColor(int index, const
    #      QColor &color)
    ritual = (
        'ritual_ZN27QQuickShapeSoftwareRenderer14setStrokeColorEiRK6QColor')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN27QQuickShapeSoftwareRenderer14setStrokeColorEiRK6Q'
          'Color')
    self.uglySide.call(ritual, index, self._valueOf(color))

  @overload(int, float)
  def setStrokeWidth(self, index: int, w: float) -> None:
    """
    Calls Qt's 'void QQuickShapeSoftwareRenderer::setStrokeWidth(int index,
    qreal w)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapesoftwarerenderer.html#setStrokeWidth

    Parameters
    ----------

    index : int
      Passed on as it is.

    w : float
      Passed on as it is.
    """
    #  void QQuickShapeSoftwareRenderer::setStrokeWidth(int index, qreal w)
    ritual = 'ritual_ZN27QQuickShapeSoftwareRenderer14setStrokeWidthEid'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN27QQuickShapeSoftwareRenderer14setStrokeWidthEid')
    self.uglySide.call(ritual, index, w)

  @overload(int, bool)
  def setCosmeticStroke(self, index: int, c: bool) -> None:
    """
    Calls Qt's 'void QQuickShapeSoftwareRenderer::setCosmeticStroke(int
    index, bool c)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapesoftwarerenderer.html#setCosmeticStroke

    Parameters
    ----------

    index : int
      Passed on as it is.

    c : bool
      Passed on as it is.
    """
    #  void QQuickShapeSoftwareRenderer::setCosmeticStroke(int index, bool c)
    ritual = 'ritual_ZN27QQuickShapeSoftwareRenderer17setCosmeticStrokeEib'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN27QQuickShapeSoftwareRenderer17setCosmeticStrokeEib')
    self.uglySide.call(ritual, index, c)

  @overload(int, QColor)
  def setFillColor(self, index: int, color: QColor) -> None:
    """
    Calls Qt's 'void QQuickShapeSoftwareRenderer::setFillColor(int index,
    const QColor &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapesoftwarerenderer.html#setFillColor

    Parameters
    ----------

    index : int
      Passed on as it is.

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickShapeSoftwareRenderer::setFillColor(int index, const QColor
    #      &color)
    ritual = (
        'ritual_ZN27QQuickShapeSoftwareRenderer12setFillColorEiRK6QColor')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN27QQuickShapeSoftwareRenderer12setFillColorEiRK6QCo'
          'lor')
    self.uglySide.call(ritual, index, self._valueOf(color))

  @overload(int, QQuickShapePath.FillRule)
  def setFillRule(
      self,
      index: int,
      fillRule: QQuickShapePath.FillRule,
  ) -> None:
    """
    Calls Qt's 'void QQuickShapeSoftwareRenderer::setFillRule(int index,
    QQuickShapePath::FillRule fillRule)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapesoftwarerenderer.html#setFillRule

    Parameters
    ----------

    index : int
      Passed on as it is.

    fillRule : QQuickShapePath.FillRule
      Passed on as its number.
    """
    #  void QQuickShapeSoftwareRenderer::setFillRule(int index,
    #      QQuickShapePath::FillRule fillRule)
    ritual = (
        'ritual_ZN27QQuickShapeSoftwareRenderer11setFillRuleEiN15QQuickShap'
        'ePath8FillRuleE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN27QQuickShapeSoftwareRenderer11setFillRuleEiN15QQui'
          'ckShapePath8FillRuleE')
    self.uglySide.call(ritual, index, fillRule.value)

  @overload(int, QQuickShapePath.JoinStyle, int)
  def setJoinStyle(
      self,
      index: int,
      joinStyle: QQuickShapePath.JoinStyle,
      miterLimit: int,
  ) -> None:
    """
    Calls Qt's 'void QQuickShapeSoftwareRenderer::setJoinStyle(int index,
    QQuickShapePath::JoinStyle joinStyle, int miterLimit)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapesoftwarerenderer.html#setJoinStyle

    Parameters
    ----------

    index : int
      Passed on as it is.

    joinStyle : QQuickShapePath.JoinStyle
      Passed on as its number.

    miterLimit : int
      Passed on as it is.
    """
    #  void QQuickShapeSoftwareRenderer::setJoinStyle(int index,
    #      QQuickShapePath::JoinStyle joinStyle, int miterLimit)
    ritual = (
        'ritual_ZN27QQuickShapeSoftwareRenderer12setJoinStyleEiN15QQuickSha'
        'pePath9JoinStyleEi')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN27QQuickShapeSoftwareRenderer12setJoinStyleEiN15QQu'
          'ickShapePath9JoinStyleEi')
    self.uglySide.call(ritual, index, joinStyle.value, miterLimit)

  @overload(int, QQuickShapePath.CapStyle)
  def setCapStyle(
      self,
      index: int,
      capStyle: QQuickShapePath.CapStyle,
  ) -> None:
    """
    Calls Qt's 'void QQuickShapeSoftwareRenderer::setCapStyle(int index,
    QQuickShapePath::CapStyle capStyle)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapesoftwarerenderer.html#setCapStyle

    Parameters
    ----------

    index : int
      Passed on as it is.

    capStyle : QQuickShapePath.CapStyle
      Passed on as its number.
    """
    #  void QQuickShapeSoftwareRenderer::setCapStyle(int index,
    #      QQuickShapePath::CapStyle capStyle)
    ritual = (
        'ritual_ZN27QQuickShapeSoftwareRenderer11setCapStyleEiN15QQuickShap'
        'ePath8CapStyleE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN27QQuickShapeSoftwareRenderer11setCapStyleEiN15QQui'
          'ckShapePath8CapStyleE')
    self.uglySide.call(ritual, index, capStyle.value)

  @overload(int, QQuickShapeGradient)
  @overload(int, NoneType)
  def setFillGradient(
      self,
      index: int,
      gradient: Optional[QQuickShapeGradient],
  ) -> None:
    """
    Calls Qt's 'void QQuickShapeSoftwareRenderer::setFillGradient(int index,
    QQuickShapeGradient *gradient)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapesoftwarerenderer.html#setFillGradient

    Parameters
    ----------

    index : int
      Passed on as it is.

    gradient : Optional[QQuickShapeGradient]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickShapeSoftwareRenderer::setFillGradient(int index,
    #      QQuickShapeGradient *gradient)
    self.uglySide.call(
        'ritual_ZN27QQuickShapeSoftwareRenderer15setFillGradientEiP19QQuick'
        'ShapeGradient',
        index, self._addressOf(gradient),
    )

  @overload(int, QQuickShapeGradient)
  @overload(int, NoneType)
  def setStrokeGradient(
      self,
      index: int,
      gradient: Optional[QQuickShapeGradient],
  ) -> None:
    """
    Calls Qt's 'void QQuickShapeSoftwareRenderer::setStrokeGradient(int
    index, QQuickShapeGradient *gradient)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapesoftwarerenderer.html#setStrokeGradient

    Parameters
    ----------

    index : int
      Passed on as it is.

    gradient : Optional[QQuickShapeGradient]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickShapeSoftwareRenderer::setStrokeGradient(int index,
    #      QQuickShapeGradient *gradient)
    self.uglySide.call(
        'ritual_ZN27QQuickShapeSoftwareRenderer17setStrokeGradientEiP19QQui'
        'ckShapeGradient',
        index, self._addressOf(gradient),
    )

  @overload(int, QQuickItem)
  @overload(int, NoneType)
  def setFillTextureProvider(
      self,
      index: int,
      textureProviderItem: Optional[QQuickItem],
  ) -> None:
    """
    Calls Qt's 'void QQuickShapeSoftwareRenderer::setFillTextureProvider(int
    index, QQuickItem *textureProviderItem)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapesoftwarerenderer.html

    Parameters
    ----------

    index : int
      Passed on as it is.

    textureProviderItem : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickShapeSoftwareRenderer::setFillTextureProvider(int index,
    #      QQuickItem *textureProviderItem)
    ritual = (
        'ritual_ZN27QQuickShapeSoftwareRenderer22setFillTextureProviderEiP1'
        '0QQuickItem')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN27QQuickShapeSoftwareRenderer22setFillTextureProvid'
          'erEiP10QQuickItem')
    self.uglySide.call(ritual, index, self._addressOf(textureProviderItem))

  @overload(int, QSGTransform)
  def setFillTransform(self, index: int, transform: QSGTransform) -> None:
    """
    Calls Qt's 'void QQuickShapeSoftwareRenderer::setFillTransform(int index,
    const QSGTransform &transform)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapesoftwarerenderer.html#setFillTransform

    Parameters
    ----------

    index : int
      Passed on as it is.

    transform : QSGTransform
      Passed on as a value: Qt reads the C++ QSGTransform, which stays
      Python's own.
    """
    #  void QQuickShapeSoftwareRenderer::setFillTransform(int index, const
    #      QSGTransform &transform)
    ritual = (
        'ritual_ZN27QQuickShapeSoftwareRenderer16setFillTransformEiRK12QSGT'
        'ransform')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN27QQuickShapeSoftwareRenderer16setFillTransformEiRK'
          '12QSGTransform')
    self.uglySide.call(ritual, index, self._valueOf(transform))

  @overload(int, float)
  def setTriangulationScale(self, index: int, scale: float) -> None:
    """
    Calls Qt's 'void QQuickShapeSoftwareRenderer::setTriangulationScale(int
    index, qreal scale)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapesoftwarerenderer.html

    Parameters
    ----------

    index : int
      Passed on as it is.

    scale : float
      Passed on as it is.
    """
    #  void QQuickShapeSoftwareRenderer::setTriangulationScale(int index,
    #      qreal scale)
    ritual = (
        'ritual_ZN27QQuickShapeSoftwareRenderer21setTriangulationScaleEid')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN27QQuickShapeSoftwareRenderer21setTriangulationScal'
          'eEid')
    self.uglySide.call(ritual, index, scale)

  @overload(QQuickShapeSoftwareRenderNode)
  @overload(NoneType)
  def setNode(self, node: Optional[QQuickShapeSoftwareRenderNode]) -> None:
    """
    Calls Qt's 'void
    QQuickShapeSoftwareRenderer::setNode(QQuickShapeSoftwareRenderNode
    *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapesoftwarerenderer.html#setNode

    Parameters
    ----------

    node : Optional[QQuickShapeSoftwareRenderNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void
    #      QQuickShapeSoftwareRenderer::setNode(QQuickShapeSoftwareRenderNode
    #      *node)
    self.uglySide.call(
        'ritual_ZN27QQuickShapeSoftwareRenderer7setNodeEP29QQuickShapeSoftw'
        'areRenderNode',
        self._addressOf(node),
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

  @overload(bool)
  def endSync(self, async_: bool) -> None:
    """
    Calls Qt's 'void QQuickShapeSoftwareRenderer::endSync(bool async)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapesoftwarerenderer.html#endSync

    Parameters
    ----------

    async_ : bool
      Passed on as it is.
    """
    #  void QQuickShapeSoftwareRenderer::endSync(bool async)
    ritual = 'ritual_ZN27QQuickShapeSoftwareRenderer7endSyncEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN27QQuickShapeSoftwareRenderer7endSyncEb'
    self.uglySide.call(ritual, async_)

  @overload(QQuickWindow)
  @overload(NoneType)
  def handleSceneChange(self, window: Optional[QQuickWindow]) -> None:
    """
    Calls Qt's 'void
    QQuickShapeSoftwareRenderer::handleSceneChange(QQuickWindow *window)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapesoftwarerenderer.html#handleSceneChange

    Parameters
    ----------

    window : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickShapeSoftwareRenderer::handleSceneChange(QQuickWindow
    #      *window)
    ritual = (
        'ritual_ZN27QQuickShapeSoftwareRenderer17handleSceneChangeEP12QQuic'
        'kWindow')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN27QQuickShapeSoftwareRenderer17handleSceneChangeEP1'
          '2QQuickWindow')
    self.uglySide.call(ritual, self._addressOf(window))

  def updateNode(self) -> None:
    """
    Calls Qt's 'void QQuickShapeSoftwareRenderer::updateNode()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapesoftwarerenderer.html#updateNode
    """
    #  void QQuickShapeSoftwareRenderer::updateNode()
    ritual = 'ritual_ZN27QQuickShapeSoftwareRenderer10updateNodeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN27QQuickShapeSoftwareRenderer10updateNodeEv'
    self.uglySide.call(ritual)
