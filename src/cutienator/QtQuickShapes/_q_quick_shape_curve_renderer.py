"""
QQuickShapeCurveRenderer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickShapes/6.12.0/QtQuickShapes/private/qquickshapecurverenderer_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickShapeCurveRenderer to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QList
from . import QQuickAbstractPathRenderer, QQuickShapePath

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QQuickShapeGradient
  from ..QtGui import QColor, QPainterPath, QPen
  from ..QtQuick import QQuadPath, QQuickItem, QQuickWindow
  from ..QtQuick import QSGCurveAbstractNode, QSGNode, QSGTransform
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QPainterPath = WAIT['QPainterPath']
  QPen = WAIT['QPen']
  QQuadPath = WAIT['QQuadPath']
  QQuickItem = WAIT['QQuickItem']
  QQuickShapeGradient = WAIT['QQuickShapeGradient']
  QQuickWindow = WAIT['QQuickWindow']
  QSGNode = WAIT['QSGNode']
  QSGTransform = WAIT['QSGTransform']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickShapeCurveRenderer(QQuickAbstractPathRenderer):
  """
  The cute side of Qt's QQuickShapeCurveRenderer: a plain Python object
  standing in front of one C++ QQuickShapeCurveRenderer.

  It is built on the cute 'QQuickAbstractPathRenderer', as Qt's
  QQuickShapeCurveRenderer is built on Qt's QQuickAbstractPathRenderer, and
  has everything that class has.

  C++ hands a QQuickShapeCurveRenderer around as a copy, so every C++
  QQuickShapeCurveRenderer behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQuickShapeCurveRenderer that has a ritual and that
  Python can call so far, 24 names in all: 'setPath', 'setStrokeColor',
  'setStrokeWidth', 'setCosmeticStroke', 'setFillColor', 'setFillRule',
  'setJoinStyle', 'setCapStyle', 'setFillGradient', 'setStrokeGradient',
  'setFillTextureProvider', 'setFillTransform', 'endSync', 'flags',
  'handleSceneChange', 'updateNode', 'setRootNode', 'clearNodeReferences',
  'debugVisualization', 'setDebugVisualization', 'maybeUpdateAsyncItem',
  'addFillNodes', 'addTriangulatingStrokerNodes', 'addCurveStrokeNodes'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQuickShapeCurveRenderer::~QQuickShapeCurveRenderer()': the
    destructor: Python removes its C++ QQuickShapeCurveRenderer by it, and
    has no other use for it.
  - Qt's 'void QQuickShapeCurveRenderer::beginSync(int totalCount, bool
    *countChanged)': takes a number to change where it is.
  - Qt's 'void QQuickShapeCurveRenderer::setStrokeStyle(int index,
    QQuickShapePath::StrokeStyle strokeStyle, qreal dashOffset, const
    QList<qreal> &dashPattern)': takes a type Python has no way to hand over
    yet.
  - Qt's 'void QQuickShapeCurveRenderer::setAsyncCallback(void (*)(void *)
    a0, void *a1)': takes a type Python has no way to hand over yet.
  - Qt's 'void QQuickShapeCurveRenderer::setUpRunner(PathData *pathData)':
    names 'QQuickShapeCurveRenderer::PathData', which has no cute class yet.
  - Qt's 'void QQuickShapeCurveRenderer::processPath(PathData *pathData)':
    names 'QQuickShapeCurveRenderer::PathData', which has no cute class yet.

  What to expect
  --------------

  - The C++ QQuickShapeCurveRenderer is created at the first use, not by
    'QQuickShapeCurveRenderer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQuickShapeCurveRenderer back gives a copy the ritual
    made for Python, in a new cute QQuickShapeCurveRenderer.
  - Each name of Qt's QQuickShapeCurveRenderer that has no cute function yet,
    'processPath', 'setUpRunner', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QQuickShapeCurveRenderer, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class DebugVisualizationOption(CuteNum):
    """
    The enum 'QQuickShapeCurveRenderer::DebugVisualizationOption' of Qt, with
    the 3 names Qt gives in it.
    """

    NoDebug = Kee[int](0)
    DebugCurves = Kee[int](1)
    DebugWireframe = Kee[int](2)

  class DirtyFlag(CuteNum):
    """
    The enum 'QQuickShapeCurveRenderer::DirtyFlag' of Qt, with the 4 names Qt
    gives in it.
    """

    PathDirty = Kee[int](1)
    FillDirty = Kee[int](2)
    StrokeDirty = Kee[int](4)
    UniformsDirty = Kee[int](8)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def debugVisualization() -> int:
    """
    Calls Qt's 'int QQuickShapeCurveRenderer::debugVisualization()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapecurverenderer.html#debugVisualization
    """
    #  int QQuickShapeCurveRenderer::debugVisualization()
    return Rituals.call(
        'ritual_ZN24QQuickShapeCurveRenderer18debugVisualizationEv',
    )

  @staticmethod
  @overload(int)
  def setDebugVisualization(options: int) -> None:
    """
    Calls Qt's 'void QQuickShapeCurveRenderer::setDebugVisualization(int
    options)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapecurverenderer.html

    Parameters
    ----------

    options : int
      Passed on as it is.
    """
    #  void QQuickShapeCurveRenderer::setDebugVisualization(int options)
    Rituals.call(
        'ritual_ZN24QQuickShapeCurveRenderer21setDebugVisualizationEi',
        options,
    )

  @staticmethod
  @overload(QQuadPath)
  def addFillNodes(path: QQuadPath) -> QList[QSGCurveAbstractNode]:
    """
    Calls Qt's 'NodeList QQuickShapeCurveRenderer::addFillNodes(const
    QQuadPath &path)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapecurverenderer.html#addFillNodes

    Parameters
    ----------

    path : QQuadPath
      Passed on as a value: Qt reads the C++ QQuadPath, which stays Python's
      own.

    Returns
    -------

    QList[QSGCurveAbstractNode]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  NodeList QQuickShapeCurveRenderer::addFillNodes(const QQuadPath &path)
    address = Rituals.call(
        'ritual_ZN24QQuickShapeCurveRenderer12addFillNodesERK9QQuadPath',
        CuteMixin._valueOf(path),
    )
    from ..QtQuick import QSGCurveAbstractNode
    return QList[QSGCurveAbstractNode]._cuteOwning(address)

  @staticmethod
  @overload(QQuadPath, QPen)
  def addTriangulatingStrokerNodes(
      path: QQuadPath,
      pen: QPen,
  ) -> QList[QSGCurveAbstractNode]:
    """
    Calls Qt's 'NodeList
    QQuickShapeCurveRenderer::addTriangulatingStrokerNodes(const QQuadPath
    &path, const QPen &pen)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapecurverenderer.html

    Parameters
    ----------

    path : QQuadPath
      Passed on as a value: Qt reads the C++ QQuadPath, which stays Python's
      own.

    pen : QPen
      Passed on as a value: Qt reads the C++ QPen, which stays Python's own.

    Returns
    -------

    QList[QSGCurveAbstractNode]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  NodeList QQuickShapeCurveRenderer::addTriangulatingStrokerNodes(const
    #      QQuadPath &path, const QPen &pen)
    address = Rituals.call(
        'ritual_ZN24QQuickShapeCurveRenderer28addTriangulatingStrokerNodesE'
        'RK9QQuadPathRK4QPen',
        CuteMixin._valueOf(path), CuteMixin._valueOf(pen),
    )
    from ..QtQuick import QSGCurveAbstractNode
    return QList[QSGCurveAbstractNode]._cuteOwning(address)

  @staticmethod
  @overload(QQuadPath, QPen)
  def addCurveStrokeNodes(
      path: QQuadPath,
      pen: QPen,
  ) -> QList[QSGCurveAbstractNode]:
    """
    Calls Qt's 'NodeList QQuickShapeCurveRenderer::addCurveStrokeNodes(const
    QQuadPath &path, const QPen &pen)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapecurverenderer.html#addCurveStrokeNodes

    Parameters
    ----------

    path : QQuadPath
      Passed on as a value: Qt reads the C++ QQuadPath, which stays Python's
      own.

    pen : QPen
      Passed on as a value: Qt reads the C++ QPen, which stays Python's own.

    Returns
    -------

    QList[QSGCurveAbstractNode]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  NodeList QQuickShapeCurveRenderer::addCurveStrokeNodes(const QQuadPath
    #      &path, const QPen &pen)
    address = Rituals.call(
        'ritual_ZN24QQuickShapeCurveRenderer19addCurveStrokeNodesERK9QQuadP'
        'athRK4QPen',
        CuteMixin._valueOf(path), CuteMixin._valueOf(pen),
    )
    from ..QtQuick import QSGCurveAbstractNode
    return QList[QSGCurveAbstractNode]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickShapeCurveRenderer'

  #  A C++ QQuickShapeCurveRenderer Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickShapeCurveRenderer'

  #  Qt's '~QQuickShapeCurveRenderer()'. Naming it makes this a value class:
  #  Python owns every C++ QQuickShapeCurveRenderer behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN24QQuickShapeCurveRendererD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def flags(self) -> QQuickAbstractPathRenderer.Flags:
    """
    Calls Qt's 'Flags QQuickShapeCurveRenderer::flags() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapecurverenderer.html#flags

    Returns
    -------

    QQuickAbstractPathRenderer.Flags
      The value standing for the combination Qt gave back.
    """
    #  Flags QQuickShapeCurveRenderer::flags() const
    ritual = 'ritual_ZNK24QQuickShapeCurveRenderer5flagsEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK24QQuickShapeCurveRenderer5flagsEv'
    return QQuickAbstractPathRenderer.Flags(self.uglySide.call(ritual))

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
    Calls Qt's 'void QQuickShapeCurveRenderer::setPath(int index, const
    QPainterPath &path, QQuickShapePath::PathHints pathHints)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapecurverenderer.html#setPath

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
    #  void QQuickShapeCurveRenderer::setPath(int index, const QPainterPath
    #      &path, QQuickShapePath::PathHints pathHints)
    ritual = (
        'ritual_ZN24QQuickShapeCurveRenderer7setPathEiRK12QPainterPath6QFla'
        'gsIN15QQuickShapePath8PathHintEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QQuickShapeCurveRenderer7setPathEiRK12QPainterPat'
          'h6QFlagsIN15QQuickShapePath8PathHintEE')
    self.uglySide.call(ritual, index, self._valueOf(path), pathHints.value)

  @overload(int, QColor)
  def setStrokeColor(self, index: int, color: QColor) -> None:
    """
    Calls Qt's 'void QQuickShapeCurveRenderer::setStrokeColor(int index,
    const QColor &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapecurverenderer.html#setStrokeColor

    Parameters
    ----------

    index : int
      Passed on as it is.

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickShapeCurveRenderer::setStrokeColor(int index, const QColor
    #      &color)
    ritual = 'ritual_ZN24QQuickShapeCurveRenderer14setStrokeColorEiRK6QColor'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QQuickShapeCurveRenderer14setStrokeColorEiRK6QCol'
          'or')
    self.uglySide.call(ritual, index, self._valueOf(color))

  @overload(int, float)
  def setStrokeWidth(self, index: int, w: float) -> None:
    """
    Calls Qt's 'void QQuickShapeCurveRenderer::setStrokeWidth(int index,
    qreal w)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapecurverenderer.html#setStrokeWidth

    Parameters
    ----------

    index : int
      Passed on as it is.

    w : float
      Passed on as it is.
    """
    #  void QQuickShapeCurveRenderer::setStrokeWidth(int index, qreal w)
    ritual = 'ritual_ZN24QQuickShapeCurveRenderer14setStrokeWidthEid'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN24QQuickShapeCurveRenderer14setStrokeWidthEid'
    self.uglySide.call(ritual, index, w)

  @overload(int, bool)
  def setCosmeticStroke(self, index: int, c: bool) -> None:
    """
    Calls Qt's 'void QQuickShapeCurveRenderer::setCosmeticStroke(int index,
    bool c)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapecurverenderer.html#setCosmeticStroke

    Parameters
    ----------

    index : int
      Passed on as it is.

    c : bool
      Passed on as it is.
    """
    #  void QQuickShapeCurveRenderer::setCosmeticStroke(int index, bool c)
    ritual = 'ritual_ZN24QQuickShapeCurveRenderer17setCosmeticStrokeEib'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QQuickShapeCurveRenderer17setCosmeticStrokeEib')
    self.uglySide.call(ritual, index, c)

  @overload(int, QColor)
  def setFillColor(self, index: int, color: QColor) -> None:
    """
    Calls Qt's 'void QQuickShapeCurveRenderer::setFillColor(int index, const
    QColor &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapecurverenderer.html#setFillColor

    Parameters
    ----------

    index : int
      Passed on as it is.

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickShapeCurveRenderer::setFillColor(int index, const QColor
    #      &color)
    ritual = 'ritual_ZN24QQuickShapeCurveRenderer12setFillColorEiRK6QColor'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QQuickShapeCurveRenderer12setFillColorEiRK6QColor')
    self.uglySide.call(ritual, index, self._valueOf(color))

  @overload(int, QQuickShapePath.FillRule)
  def setFillRule(
      self,
      index: int,
      fillRule: QQuickShapePath.FillRule,
  ) -> None:
    """
    Calls Qt's 'void QQuickShapeCurveRenderer::setFillRule(int index,
    QQuickShapePath::FillRule fillRule)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapecurverenderer.html#setFillRule

    Parameters
    ----------

    index : int
      Passed on as it is.

    fillRule : QQuickShapePath.FillRule
      Passed on as its number.
    """
    #  void QQuickShapeCurveRenderer::setFillRule(int index,
    #      QQuickShapePath::FillRule fillRule)
    ritual = (
        'ritual_ZN24QQuickShapeCurveRenderer11setFillRuleEiN15QQuickShapePa'
        'th8FillRuleE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QQuickShapeCurveRenderer11setFillRuleEiN15QQuickS'
          'hapePath8FillRuleE')
    self.uglySide.call(ritual, index, fillRule.value)

  @overload(int, QQuickShapePath.JoinStyle, int)
  def setJoinStyle(
      self,
      index: int,
      joinStyle: QQuickShapePath.JoinStyle,
      miterLimit: int,
  ) -> None:
    """
    Calls Qt's 'void QQuickShapeCurveRenderer::setJoinStyle(int index,
    QQuickShapePath::JoinStyle joinStyle, int miterLimit)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapecurverenderer.html#setJoinStyle

    Parameters
    ----------

    index : int
      Passed on as it is.

    joinStyle : QQuickShapePath.JoinStyle
      Passed on as its number.

    miterLimit : int
      Passed on as it is.
    """
    #  void QQuickShapeCurveRenderer::setJoinStyle(int index,
    #      QQuickShapePath::JoinStyle joinStyle, int miterLimit)
    ritual = (
        'ritual_ZN24QQuickShapeCurveRenderer12setJoinStyleEiN15QQuickShapeP'
        'ath9JoinStyleEi')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QQuickShapeCurveRenderer12setJoinStyleEiN15QQuick'
          'ShapePath9JoinStyleEi')
    self.uglySide.call(ritual, index, joinStyle.value, miterLimit)

  @overload(int, QQuickShapePath.CapStyle)
  def setCapStyle(
      self,
      index: int,
      capStyle: QQuickShapePath.CapStyle,
  ) -> None:
    """
    Calls Qt's 'void QQuickShapeCurveRenderer::setCapStyle(int index,
    QQuickShapePath::CapStyle capStyle)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapecurverenderer.html#setCapStyle

    Parameters
    ----------

    index : int
      Passed on as it is.

    capStyle : QQuickShapePath.CapStyle
      Passed on as its number.
    """
    #  void QQuickShapeCurveRenderer::setCapStyle(int index,
    #      QQuickShapePath::CapStyle capStyle)
    ritual = (
        'ritual_ZN24QQuickShapeCurveRenderer11setCapStyleEiN15QQuickShapePa'
        'th8CapStyleE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QQuickShapeCurveRenderer11setCapStyleEiN15QQuickS'
          'hapePath8CapStyleE')
    self.uglySide.call(ritual, index, capStyle.value)

  @overload(int, QQuickShapeGradient)
  @overload(int, NoneType)
  def setFillGradient(
      self,
      index: int,
      gradient: Optional[QQuickShapeGradient],
  ) -> None:
    """
    Calls Qt's 'void QQuickShapeCurveRenderer::setFillGradient(int index,
    QQuickShapeGradient *gradient)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapecurverenderer.html#setFillGradient

    Parameters
    ----------

    index : int
      Passed on as it is.

    gradient : Optional[QQuickShapeGradient]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickShapeCurveRenderer::setFillGradient(int index,
    #      QQuickShapeGradient *gradient)
    ritual = (
        'ritual_ZN24QQuickShapeCurveRenderer15setFillGradientEiP19QQuickSha'
        'peGradient')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QQuickShapeCurveRenderer15setFillGradientEiP19QQu'
          'ickShapeGradient')
    self.uglySide.call(ritual, index, self._addressOf(gradient))

  @overload(int, QQuickShapeGradient)
  @overload(int, NoneType)
  def setStrokeGradient(
      self,
      index: int,
      gradient: Optional[QQuickShapeGradient],
  ) -> None:
    """
    Calls Qt's 'void QQuickShapeCurveRenderer::setStrokeGradient(int index,
    QQuickShapeGradient *gradient)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapecurverenderer.html#setStrokeGradient

    Parameters
    ----------

    index : int
      Passed on as it is.

    gradient : Optional[QQuickShapeGradient]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickShapeCurveRenderer::setStrokeGradient(int index,
    #      QQuickShapeGradient *gradient)
    ritual = (
        'ritual_ZN24QQuickShapeCurveRenderer17setStrokeGradientEiP19QQuickS'
        'hapeGradient')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QQuickShapeCurveRenderer17setStrokeGradientEiP19Q'
          'QuickShapeGradient')
    self.uglySide.call(ritual, index, self._addressOf(gradient))

  @overload(int, QQuickItem)
  @overload(int, NoneType)
  def setFillTextureProvider(
      self,
      index: int,
      textureProviderItem: Optional[QQuickItem],
  ) -> None:
    """
    Calls Qt's 'void QQuickShapeCurveRenderer::setFillTextureProvider(int
    index, QQuickItem *textureProviderItem)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapecurverenderer.html

    Parameters
    ----------

    index : int
      Passed on as it is.

    textureProviderItem : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickShapeCurveRenderer::setFillTextureProvider(int index,
    #      QQuickItem *textureProviderItem)
    ritual = (
        'ritual_ZN24QQuickShapeCurveRenderer22setFillTextureProviderEiP10QQ'
        'uickItem')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QQuickShapeCurveRenderer22setFillTextureProviderE'
          'iP10QQuickItem')
    self.uglySide.call(ritual, index, self._addressOf(textureProviderItem))

  @overload(int, QSGTransform)
  def setFillTransform(self, index: int, transform: QSGTransform) -> None:
    """
    Calls Qt's 'void QQuickShapeCurveRenderer::setFillTransform(int index,
    const QSGTransform &transform)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapecurverenderer.html#setFillTransform

    Parameters
    ----------

    index : int
      Passed on as it is.

    transform : QSGTransform
      Passed on as a value: Qt reads the C++ QSGTransform, which stays
      Python's own.
    """
    #  void QQuickShapeCurveRenderer::setFillTransform(int index, const
    #      QSGTransform &transform)
    ritual = (
        'ritual_ZN24QQuickShapeCurveRenderer16setFillTransformEiRK12QSGTran'
        'sform')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QQuickShapeCurveRenderer16setFillTransformEiRK12Q'
          'SGTransform')
    self.uglySide.call(ritual, index, self._valueOf(transform))

  @overload(QSGNode)
  @overload(NoneType)
  def setRootNode(self, node: Optional[QSGNode]) -> None:
    """
    Calls Qt's 'void QQuickShapeCurveRenderer::setRootNode(QSGNode *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapecurverenderer.html#setRootNode

    Parameters
    ----------

    node : Optional[QSGNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickShapeCurveRenderer::setRootNode(QSGNode *node)
    self.uglySide.call(
        'ritual_ZN24QQuickShapeCurveRenderer11setRootNodeEP7QSGNode',
        self._addressOf(node, 'QSGNode'),
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

  @overload(QQuickItem)
  @overload(NoneType)
  def __init__(self, item: Optional[QQuickItem]) -> None:
    """
    Notes what was given, for Qt's
    'QQuickShapeCurveRenderer::QQuickShapeCurveRenderer(QQuickItem *item)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapecurverenderer.html

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQuickShapeCurveRenderer::QQuickShapeCurveRenderer(QQuickItem *item)
    self._noteCreation(QQuickShapeCurveRenderer, lambda: Rituals.call(
        'ritual_ZN24QQuickShapeCurveRendererC1EP10QQuickItem',
        self._addressOf(item),
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

  @overload(bool)
  def endSync(self, async_: bool) -> None:
    """
    Calls Qt's 'void QQuickShapeCurveRenderer::endSync(bool async)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapecurverenderer.html#endSync

    Parameters
    ----------

    async_ : bool
      Passed on as it is.
    """
    #  void QQuickShapeCurveRenderer::endSync(bool async)
    ritual = 'ritual_ZN24QQuickShapeCurveRenderer7endSyncEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN24QQuickShapeCurveRenderer7endSyncEb'
    self.uglySide.call(ritual, async_)

  @overload(QQuickWindow)
  @overload(NoneType)
  def handleSceneChange(self, window: Optional[QQuickWindow]) -> None:
    """
    Calls Qt's 'void QQuickShapeCurveRenderer::handleSceneChange(QQuickWindow
    *window)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapecurverenderer.html#handleSceneChange

    Parameters
    ----------

    window : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickShapeCurveRenderer::handleSceneChange(QQuickWindow *window)
    ritual = (
        'ritual_ZN24QQuickShapeCurveRenderer17handleSceneChangeEP12QQuickWi'
        'ndow')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QQuickShapeCurveRenderer17handleSceneChangeEP12QQ'
          'uickWindow')
    self.uglySide.call(ritual, self._addressOf(window))

  def updateNode(self) -> None:
    """
    Calls Qt's 'void QQuickShapeCurveRenderer::updateNode()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapecurverenderer.html#updateNode
    """
    #  void QQuickShapeCurveRenderer::updateNode()
    ritual = 'ritual_ZN24QQuickShapeCurveRenderer10updateNodeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN24QQuickShapeCurveRenderer10updateNodeEv'
    self.uglySide.call(ritual)

  def clearNodeReferences(self) -> None:
    """
    Calls Qt's 'void QQuickShapeCurveRenderer::clearNodeReferences()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapecurverenderer.html#clearNodeReferences
    """
    #  void QQuickShapeCurveRenderer::clearNodeReferences()
    self.uglySide.call(
        'ritual_ZN24QQuickShapeCurveRenderer19clearNodeReferencesEv',
    )

  def maybeUpdateAsyncItem(self) -> None:
    """
    Calls Qt's 'void QQuickShapeCurveRenderer::maybeUpdateAsyncItem()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapecurverenderer.html#maybeUpdateAsyncItem
    """
    #  void QQuickShapeCurveRenderer::maybeUpdateAsyncItem()
    self.uglySide.call(
        'ritual_ZN24QQuickShapeCurveRenderer20maybeUpdateAsyncItemEv',
    )

  @staticmethod
  def processPath(*__, **_) -> Never:
    """
    Qt's 'void QQuickShapeCurveRenderer::processPath(PathData *pathData)':
    names 'QQuickShapeCurveRenderer::PathData', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuickShapeCurveRenderer.processPath' has no cute function yet. "
        "Qt's 'void QQuickShapeCurveRenderer::processPath(PathData "
        "*pathData)': names 'QQuickShapeCurveRenderer::PathData', which has "
        "no cute class yet.")

  @staticmethod
  def setUpRunner(*__, **_) -> Never:
    """
    Qt's 'void QQuickShapeCurveRenderer::setUpRunner(PathData *pathData)':
    names 'QQuickShapeCurveRenderer::PathData', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuickShapeCurveRenderer.setUpRunner' has no cute function yet. "
        "Qt's 'void QQuickShapeCurveRenderer::setUpRunner(PathData "
        "*pathData)': names 'QQuickShapeCurveRenderer::PathData', which has "
        "no cute class yet.")
