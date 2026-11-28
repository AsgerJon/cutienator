"""
QQuickShapeGenericRenderer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickShapes/6.12.0/QtQuickShapes/private/qquickshapegenericrenderer_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickShapeGenericRenderer to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from . import QQuickAbstractPathRenderer, QQuickShapePath

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QQuickShapeGenericNode, QQuickShapeGradient
  from ..QtGui import QColor, QPainterPath
  from ..QtQuick import QQuickItem, QQuickWindow, QSGTransform
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QPainterPath = WAIT['QPainterPath']
  QQuickItem = WAIT['QQuickItem']
  QQuickShapeGenericNode = WAIT['QQuickShapeGenericNode']
  QQuickShapeGradient = WAIT['QQuickShapeGradient']
  QQuickWindow = WAIT['QQuickWindow']
  QSGTransform = WAIT['QSGTransform']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickShapeGenericRenderer(QQuickAbstractPathRenderer):
  """
  The cute side of Qt's QQuickShapeGenericRenderer: a plain Python object
  standing in front of one C++ QQuickShapeGenericRenderer.

  It is built on the cute 'QQuickAbstractPathRenderer', as Qt's
  QQuickShapeGenericRenderer is built on Qt's QQuickAbstractPathRenderer, and
  has everything that class has.

  C++ hands a QQuickShapeGenericRenderer around as a copy, so every C++
  QQuickShapeGenericRenderer behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QQuickShapeGenericRenderer that has a ritual and
  that Python can call so far, 19 names in all: 'setPath', 'setStrokeColor',
  'setStrokeWidth', 'setCosmeticStroke', 'setFillColor', 'setFillRule',
  'setJoinStyle', 'setCapStyle', 'setFillGradient', 'setStrokeGradient',
  'setFillTextureProvider', 'setFillTransform', 'setTriangulationScale',
  'endSync', 'flags', 'handleSceneChange', 'updateNode', 'setRootNode',
  'maybeUpdateAsyncItem'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQuickShapeGenericRenderer::~QQuickShapeGenericRenderer()': the
    destructor: Python removes its C++ QQuickShapeGenericRenderer by it, and
    has no other use for it.
  - Qt's 'void QQuickShapeGenericRenderer::beginSync(int totalCount, bool
    *countChanged)': takes a number to change where it is.
  - Qt's 'void QQuickShapeGenericRenderer::setStrokeStyle(int index,
    QQuickShapePath::StrokeStyle strokeStyle, qreal dashOffset, const
    QList<qreal> &dashPattern)': takes a type Python has no way to hand over
    yet.
  - Qt's 'void QQuickShapeGenericRenderer::setAsyncCallback(void (*)(void *)
    a0, void *a1)': takes a type Python has no way to hand over yet.
  - Qt's 'void QQuickShapeGenericRenderer::triangulateFill(const QPainterPath
    &path, const Color4ub &fillColor, VertexContainerType *fillVertices,
    IndexContainerType *fillIndices, QSGGeometry::Type *indexType, bool
    supportsElementIndexUint, qreal triangulationScale)': names
    'QQuickShapeGenericRenderer::VertexContainerType', which has no cute
    class yet.

  What has no ritual
  ------------------

  5 of the 29 functions Qt declares: 3 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 1 leans on
  'QQuickShapeGenericStrokeFillNode; 1 leans on 'QQuickShapeGenericRenderer.

  What to expect
  --------------

  - The C++ QQuickShapeGenericRenderer is created at the first use, not by
    'QQuickShapeGenericRenderer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQuickShapeGenericRenderer back gives a copy the
    ritual made for Python, in a new cute QQuickShapeGenericRenderer.
  - Each name of Qt's QQuickShapeGenericRenderer that has no cute function
    yet, '__init__', 'triangulateFill', 'triangulateStroke',
    'updateFillNode', 'updateShadowDataInNode', 'updateStrokeNode', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QQuickShapeGenericRenderer, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class Dirty(CuteNum):
    """
    The enum 'QQuickShapeGenericRenderer::Dirty' of Qt, with the 8 names Qt
    gives in it.
    """

    DirtyFillGeom = Kee[int](1)
    DirtyStrokeGeom = Kee[int](2)
    DirtyColor = Kee[int](4)
    DirtyFillGradient = Kee[int](8)
    DirtyFillTransform = Kee[int](16)
    DirtyFillTexture = Kee[int](32)
    DirtyList = Kee[int](64)
    DirtyStrokeGradient = Kee[int](128)

  #  The classes Qt writes inside QQuickShapeGenericRenderer, each a class in
  #  here as in C++.

  class Color4ub(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQuickShapeGenericRenderer::Color4ub: a plain
    Python object standing in front of one C++
    QQuickShapeGenericRenderer::Color4ub.

    C++ hands a QQuickShapeGenericRenderer::Color4ub around as a copy, so
    every C++ QQuickShapeGenericRenderer::Color4ub behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    No function of Qt's QQuickShapeGenericRenderer::Color4ub yet. None can be
    made from Python: one comes out of a function of another class that gives
    one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQuickShapeGenericRenderer::Color4ub::~Color4ub()': the
      destructor: Python removes its C++ QQuickShapeGenericRenderer::Color4ub
      by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QQuickShapeGenericRenderer::Color4ub is created at the first
      use, not by 'QQuickShapeGenericRenderer::Color4ub(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQuickShapeGenericRenderer::Color4ub back gives a
      copy the ritual made for Python, in a new cute
      QQuickShapeGenericRenderer::Color4ub.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQuickShapeGenericRenderer::Color4ub'

    #  Qt's '~QQuickShapeGenericRenderer::Color4ub()'. Naming it makes this a
    #  value class: Python owns every C++
    #  QQuickShapeGenericRenderer::Color4ub behind a cute one, and removes it
    #  by this ritual.
    __delete_ritual__ = 'ritual_ZN26QQuickShapeGenericRenderer8Color4ubD1Ev'

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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickShapeGenericRenderer'

  #  A C++ QQuickShapeGenericRenderer Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickShapeGenericRenderer'

  #  Qt's '~QQuickShapeGenericRenderer()'. Naming it makes this a value
  #  class: Python owns every C++ QQuickShapeGenericRenderer behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN26QQuickShapeGenericRendererD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def flags(self) -> QQuickAbstractPathRenderer.Flags:
    """
    Calls Qt's 'Flags QQuickShapeGenericRenderer::flags() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapegenericrenderer.html#flags

    Returns
    -------

    QQuickAbstractPathRenderer.Flags
      The value standing for the combination Qt gave back.
    """
    #  Flags QQuickShapeGenericRenderer::flags() const
    ritual = 'ritual_ZNK26QQuickShapeGenericRenderer5flagsEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK26QQuickShapeGenericRenderer5flagsEv'
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
    Calls Qt's 'void QQuickShapeGenericRenderer::setPath(int index, const
    QPainterPath &path, QQuickShapePath::PathHints pathHints)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapegenericrenderer.html#setPath

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
    #  void QQuickShapeGenericRenderer::setPath(int index, const QPainterPath
    #      &path, QQuickShapePath::PathHints pathHints)
    ritual = (
        'ritual_ZN26QQuickShapeGenericRenderer7setPathEiRK12QPainterPath6QF'
        'lagsIN15QQuickShapePath8PathHintEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN26QQuickShapeGenericRenderer7setPathEiRK12QPainterP'
          'ath6QFlagsIN15QQuickShapePath8PathHintEE')
    self.uglySide.call(ritual, index, self._valueOf(path), pathHints.value)

  @overload(int, QColor)
  def setStrokeColor(self, index: int, color: QColor) -> None:
    """
    Calls Qt's 'void QQuickShapeGenericRenderer::setStrokeColor(int index,
    const QColor &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapegenericrenderer.html#setStrokeColor

    Parameters
    ----------

    index : int
      Passed on as it is.

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickShapeGenericRenderer::setStrokeColor(int index, const
    #      QColor &color)
    self.uglySide.call(
        'ritual_ZN26QQuickShapeGenericRenderer14setStrokeColorEiRK6QColor',
        index, self._valueOf(color),
    )

  @overload(int, float)
  def setStrokeWidth(self, index: int, w: float) -> None:
    """
    Calls Qt's 'void QQuickShapeGenericRenderer::setStrokeWidth(int index,
    qreal w)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapegenericrenderer.html#setStrokeWidth

    Parameters
    ----------

    index : int
      Passed on as it is.

    w : float
      Passed on as it is.
    """
    #  void QQuickShapeGenericRenderer::setStrokeWidth(int index, qreal w)
    ritual = 'ritual_ZN26QQuickShapeGenericRenderer14setStrokeWidthEid'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN26QQuickShapeGenericRenderer14setStrokeWidthEid'
    self.uglySide.call(ritual, index, w)

  @overload(int, bool)
  def setCosmeticStroke(self, index: int, c: bool) -> None:
    """
    Calls Qt's 'void QQuickShapeGenericRenderer::setCosmeticStroke(int index,
    bool c)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapegenericrenderer.html#setCosmeticStroke

    Parameters
    ----------

    index : int
      Passed on as it is.

    c : bool
      Passed on as it is.
    """
    #  void QQuickShapeGenericRenderer::setCosmeticStroke(int index, bool c)
    ritual = 'ritual_ZN26QQuickShapeGenericRenderer17setCosmeticStrokeEib'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN26QQuickShapeGenericRenderer17setCosmeticStrokeEib')
    self.uglySide.call(ritual, index, c)

  @overload(int, QColor)
  def setFillColor(self, index: int, color: QColor) -> None:
    """
    Calls Qt's 'void QQuickShapeGenericRenderer::setFillColor(int index,
    const QColor &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapegenericrenderer.html#setFillColor

    Parameters
    ----------

    index : int
      Passed on as it is.

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickShapeGenericRenderer::setFillColor(int index, const QColor
    #      &color)
    ritual = 'ritual_ZN26QQuickShapeGenericRenderer12setFillColorEiRK6QColor'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN26QQuickShapeGenericRenderer12setFillColorEiRK6QCol'
          'or')
    self.uglySide.call(ritual, index, self._valueOf(color))

  @overload(int, QQuickShapePath.FillRule)
  def setFillRule(
      self,
      index: int,
      fillRule: QQuickShapePath.FillRule,
  ) -> None:
    """
    Calls Qt's 'void QQuickShapeGenericRenderer::setFillRule(int index,
    QQuickShapePath::FillRule fillRule)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapegenericrenderer.html#setFillRule

    Parameters
    ----------

    index : int
      Passed on as it is.

    fillRule : QQuickShapePath.FillRule
      Passed on as its number.
    """
    #  void QQuickShapeGenericRenderer::setFillRule(int index,
    #      QQuickShapePath::FillRule fillRule)
    ritual = (
        'ritual_ZN26QQuickShapeGenericRenderer11setFillRuleEiN15QQuickShape'
        'Path8FillRuleE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN26QQuickShapeGenericRenderer11setFillRuleEiN15QQuic'
          'kShapePath8FillRuleE')
    self.uglySide.call(ritual, index, fillRule.value)

  @overload(int, QQuickShapePath.JoinStyle, int)
  def setJoinStyle(
      self,
      index: int,
      joinStyle: QQuickShapePath.JoinStyle,
      miterLimit: int,
  ) -> None:
    """
    Calls Qt's 'void QQuickShapeGenericRenderer::setJoinStyle(int index,
    QQuickShapePath::JoinStyle joinStyle, int miterLimit)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapegenericrenderer.html#setJoinStyle

    Parameters
    ----------

    index : int
      Passed on as it is.

    joinStyle : QQuickShapePath.JoinStyle
      Passed on as its number.

    miterLimit : int
      Passed on as it is.
    """
    #  void QQuickShapeGenericRenderer::setJoinStyle(int index,
    #      QQuickShapePath::JoinStyle joinStyle, int miterLimit)
    ritual = (
        'ritual_ZN26QQuickShapeGenericRenderer12setJoinStyleEiN15QQuickShap'
        'ePath9JoinStyleEi')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN26QQuickShapeGenericRenderer12setJoinStyleEiN15QQui'
          'ckShapePath9JoinStyleEi')
    self.uglySide.call(ritual, index, joinStyle.value, miterLimit)

  @overload(int, QQuickShapePath.CapStyle)
  def setCapStyle(
      self,
      index: int,
      capStyle: QQuickShapePath.CapStyle,
  ) -> None:
    """
    Calls Qt's 'void QQuickShapeGenericRenderer::setCapStyle(int index,
    QQuickShapePath::CapStyle capStyle)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapegenericrenderer.html#setCapStyle

    Parameters
    ----------

    index : int
      Passed on as it is.

    capStyle : QQuickShapePath.CapStyle
      Passed on as its number.
    """
    #  void QQuickShapeGenericRenderer::setCapStyle(int index,
    #      QQuickShapePath::CapStyle capStyle)
    ritual = (
        'ritual_ZN26QQuickShapeGenericRenderer11setCapStyleEiN15QQuickShape'
        'Path8CapStyleE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN26QQuickShapeGenericRenderer11setCapStyleEiN15QQuic'
          'kShapePath8CapStyleE')
    self.uglySide.call(ritual, index, capStyle.value)

  @overload(int, QQuickShapeGradient)
  @overload(int, NoneType)
  def setFillGradient(
      self,
      index: int,
      gradient: Optional[QQuickShapeGradient],
  ) -> None:
    """
    Calls Qt's 'void QQuickShapeGenericRenderer::setFillGradient(int index,
    QQuickShapeGradient *gradient)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapegenericrenderer.html#setFillGradient

    Parameters
    ----------

    index : int
      Passed on as it is.

    gradient : Optional[QQuickShapeGradient]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickShapeGenericRenderer::setFillGradient(int index,
    #      QQuickShapeGradient *gradient)
    ritual = (
        'ritual_ZN26QQuickShapeGenericRenderer15setFillGradientEiP19QQuickS'
        'hapeGradient')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN26QQuickShapeGenericRenderer15setFillGradientEiP19Q'
          'QuickShapeGradient')
    self.uglySide.call(ritual, index, self._addressOf(gradient))

  @overload(int, QQuickShapeGradient)
  @overload(int, NoneType)
  def setStrokeGradient(
      self,
      index: int,
      gradient: Optional[QQuickShapeGradient],
  ) -> None:
    """
    Calls Qt's 'void QQuickShapeGenericRenderer::setStrokeGradient(int index,
    QQuickShapeGradient *gradient)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapegenericrenderer.html#setStrokeGradient

    Parameters
    ----------

    index : int
      Passed on as it is.

    gradient : Optional[QQuickShapeGradient]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickShapeGenericRenderer::setStrokeGradient(int index,
    #      QQuickShapeGradient *gradient)
    self.uglySide.call(
        'ritual_ZN26QQuickShapeGenericRenderer17setStrokeGradientEiP19QQuic'
        'kShapeGradient',
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
    Calls Qt's 'void QQuickShapeGenericRenderer::setFillTextureProvider(int
    index, QQuickItem *textureProviderItem)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapegenericrenderer.html

    Parameters
    ----------

    index : int
      Passed on as it is.

    textureProviderItem : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickShapeGenericRenderer::setFillTextureProvider(int index,
    #      QQuickItem *textureProviderItem)
    ritual = (
        'ritual_ZN26QQuickShapeGenericRenderer22setFillTextureProviderEiP10'
        'QQuickItem')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN26QQuickShapeGenericRenderer22setFillTextureProvide'
          'rEiP10QQuickItem')
    self.uglySide.call(ritual, index, self._addressOf(textureProviderItem))

  @overload(int, QSGTransform)
  def setFillTransform(self, index: int, transform: QSGTransform) -> None:
    """
    Calls Qt's 'void QQuickShapeGenericRenderer::setFillTransform(int index,
    const QSGTransform &transform)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapegenericrenderer.html#setFillTransform

    Parameters
    ----------

    index : int
      Passed on as it is.

    transform : QSGTransform
      Passed on as a value: Qt reads the C++ QSGTransform, which stays
      Python's own.
    """
    #  void QQuickShapeGenericRenderer::setFillTransform(int index, const
    #      QSGTransform &transform)
    ritual = (
        'ritual_ZN26QQuickShapeGenericRenderer16setFillTransformEiRK12QSGTr'
        'ansform')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN26QQuickShapeGenericRenderer16setFillTransformEiRK1'
          '2QSGTransform')
    self.uglySide.call(ritual, index, self._valueOf(transform))

  @overload(int, float)
  def setTriangulationScale(self, index: int, scale: float) -> None:
    """
    Calls Qt's 'void QQuickShapeGenericRenderer::setTriangulationScale(int
    index, qreal scale)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapegenericrenderer.html

    Parameters
    ----------

    index : int
      Passed on as it is.

    scale : float
      Passed on as it is.
    """
    #  void QQuickShapeGenericRenderer::setTriangulationScale(int index,
    #      qreal scale)
    ritual = (
        'ritual_ZN26QQuickShapeGenericRenderer21setTriangulationScaleEid')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN26QQuickShapeGenericRenderer21setTriangulationScale'
          'Eid')
    self.uglySide.call(ritual, index, scale)

  @overload(QQuickShapeGenericNode)
  @overload(NoneType)
  def setRootNode(self, node: Optional[QQuickShapeGenericNode]) -> None:
    """
    Calls Qt's 'void
    QQuickShapeGenericRenderer::setRootNode(QQuickShapeGenericNode *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapegenericrenderer.html#setRootNode

    Parameters
    ----------

    node : Optional[QQuickShapeGenericNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickShapeGenericRenderer::setRootNode(QQuickShapeGenericNode
    #      *node)
    self.uglySide.call(
        'ritual_ZN26QQuickShapeGenericRenderer11setRootNodeEP22QQuickShapeG'
        'enericNode',
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QQuickShapeGenericRenderer::QQuickShapeGenericRenderer(QQuickItem
    *item)': leans on 'QQuickShapeGenericRenderer::setStrokeColor(int, QColor
    const&)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickShapeGenericRenderer.__init__' has no cute function yet. "
        "Qt's "
        "'QQuickShapeGenericRenderer::QQuickShapeGenericRenderer(QQuickItem "
        "*item)': leans on 'QQuickShapeGenericRenderer::setStrokeColor(int, "
        "QColor const&)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

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
    Calls Qt's 'void QQuickShapeGenericRenderer::endSync(bool async)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapegenericrenderer.html#endSync

    Parameters
    ----------

    async_ : bool
      Passed on as it is.
    """
    #  void QQuickShapeGenericRenderer::endSync(bool async)
    self.uglySide.call(
        'ritual_ZN26QQuickShapeGenericRenderer7endSyncEb', async_,
    )

  @overload(QQuickWindow)
  @overload(NoneType)
  def handleSceneChange(self, window: Optional[QQuickWindow]) -> None:
    """
    Calls Qt's 'void
    QQuickShapeGenericRenderer::handleSceneChange(QQuickWindow *window)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapegenericrenderer.html#handleSceneChange

    Parameters
    ----------

    window : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickShapeGenericRenderer::handleSceneChange(QQuickWindow
    #      *window)
    ritual = (
        'ritual_ZN26QQuickShapeGenericRenderer17handleSceneChangeEP12QQuick'
        'Window')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN26QQuickShapeGenericRenderer17handleSceneChangeEP12'
          'QQuickWindow')
    self.uglySide.call(ritual, self._addressOf(window))

  def updateNode(self) -> None:
    """
    Calls Qt's 'void QQuickShapeGenericRenderer::updateNode()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapegenericrenderer.html#updateNode
    """
    #  void QQuickShapeGenericRenderer::updateNode()
    self.uglySide.call('ritual_ZN26QQuickShapeGenericRenderer10updateNodeEv')

  def maybeUpdateAsyncItem(self) -> None:
    """
    Calls Qt's 'void QQuickShapeGenericRenderer::maybeUpdateAsyncItem()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapegenericrenderer.html
    """
    #  void QQuickShapeGenericRenderer::maybeUpdateAsyncItem()
    self.uglySide.call(
        'ritual_ZN26QQuickShapeGenericRenderer20maybeUpdateAsyncItemEv',
    )

  @staticmethod
  def triangulateFill(*__, **_) -> Never:
    """
    Qt's 'void QQuickShapeGenericRenderer::triangulateFill(const QPainterPath
    &path, const Color4ub &fillColor, VertexContainerType *fillVertices,
    IndexContainerType *fillIndices, QSGGeometry::Type *indexType, bool
    supportsElementIndexUint, qreal triangulationScale)': names
    'QQuickShapeGenericRenderer::VertexContainerType', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QQuickShapeGenericRenderer.triangulateFill' has no cute function "
        "yet. Qt's 'void QQuickShapeGenericRenderer::triangulateFill(const "
        "QPainterPath &path, const Color4ub &fillColor, VertexContainerType "
        "*fillVertices, IndexContainerType *fillIndices, QSGGeometry::Type "
        "*indexType, bool supportsElementIndexUint, qreal "
        "triangulationScale)': names "
        "'QQuickShapeGenericRenderer::VertexContainerType', which has no "
        "cute class yet.")

  @staticmethod
  def triangulateStroke(*__, **_) -> Never:
    """
    Qt's 'void QQuickShapeGenericRenderer::triangulateStroke(const
    QPainterPath &path, const QPen &pen, const Color4ub &strokeColor,
    VertexContainerType *strokeVertices, const QSize &clipSize, qreal
    triangulationScale)': Qt's library has no name for it, and its code in
    Qt's source does not compile apart from its file: unknown type name
    'ColoredVertex'.
    """
    raise NotImplementedError(
        "'QQuickShapeGenericRenderer.triangulateStroke' has no cute "
        "function yet. Qt's 'void "
        "QQuickShapeGenericRenderer::triangulateStroke(const QPainterPath "
        "&path, const QPen &pen, const Color4ub &strokeColor, "
        "VertexContainerType *strokeVertices, const QSize &clipSize, qreal "
        "triangulationScale)': Qt's library has no name for it, and its "
        "code in Qt's source does not compile apart from its file: unknown "
        "type name 'ColoredVertex'.")

  @staticmethod
  def updateFillNode(*__, **_) -> Never:
    """
    Qt's 'void QQuickShapeGenericRenderer::updateFillNode(ShapePathData *d,
    QQuickShapeGenericNode *node)': Qt's library has no name for it, and its
    code in Qt's source does not compile apart from its file: unknown type
    name 'ColoredVertex'.
    """
    raise NotImplementedError(
        "'QQuickShapeGenericRenderer.updateFillNode' has no cute function "
        "yet. Qt's 'void "
        "QQuickShapeGenericRenderer::updateFillNode(ShapePathData *d, "
        "QQuickShapeGenericNode *node)': Qt's library has no name for it, "
        "and its code in Qt's source does not compile apart from its file: "
        "unknown type name 'ColoredVertex'.")

  @staticmethod
  def updateShadowDataInNode(*__, **_) -> Never:
    """
    Qt's 'void
    QQuickShapeGenericRenderer::updateShadowDataInNode(ShapePathData *d,
    QQuickShapeGenericStrokeFillNode *n)': leans on
    'QQuickShapeGenericStrokeFillNode::staticMetaObject', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QQuickShapeGenericRenderer.updateShadowDataInNode' has no cute "
        "function yet. Qt's 'void "
        "QQuickShapeGenericRenderer::updateShadowDataInNode(ShapePathData "
        "*d, QQuickShapeGenericStrokeFillNode *n)': leans on "
        "'QQuickShapeGenericStrokeFillNode::staticMetaObject', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def updateStrokeNode(*__, **_) -> Never:
    """
    Qt's 'void QQuickShapeGenericRenderer::updateStrokeNode(ShapePathData *d,
    QQuickShapeGenericNode *node)': Qt's library has no name for it, and its
    code in Qt's source does not compile apart from its file: unknown type
    name 'ColoredVertex'.
    """
    raise NotImplementedError(
        "'QQuickShapeGenericRenderer.updateStrokeNode' has no cute function "
        "yet. Qt's 'void "
        "QQuickShapeGenericRenderer::updateStrokeNode(ShapePathData *d, "
        "QQuickShapeGenericNode *node)': Qt's library has no name for it, "
        "and its code in Qt's source does not compile apart from its file: "
        "unknown type name 'ColoredVertex'.")
