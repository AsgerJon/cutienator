"""
QQuickRectangleShape binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickShapesDesignHelpers/6.12.0/QtQuickShapesDesignHelpers/private/qquickrectangleshape_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickRectangleShape to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtQuickShapes import QQuickShapePath
from ..QtQuick import QQuickItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QQuickRectangleShapePrivate
  from ..QtGui import QColor
  from ..QtQuickShapes import QQuickShapeGradient
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QQuickShapeGradient = WAIT['QQuickShapeGradient']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickRectangleShape(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickRectangleShape: a plain Python object standing
  in front of one C++ QQuickRectangleShape.

  What exists
  -----------

  Every function of Qt's QQuickRectangleShape that has a ritual and that
  Python can call so far, 102 names in all: 'metaObject', 'tr', 'drawTop',
  'setDrawTop', 'resetDrawTop', 'drawRight', 'setDrawRight',
  'resetDrawRight', 'drawBottom', 'setDrawBottom', 'resetDrawBottom',
  'drawLeft', 'setDrawLeft', 'resetDrawLeft', 'radius', 'setRadius',
  'resetRadius', 'topLeftRadius', 'setTopLeftRadius', 'resetTopLeftRadius',
  'topRightRadius', 'setTopRightRadius', 'resetTopRightRadius',
  'bottomLeftRadius', 'setBottomLeftRadius', 'resetBottomLeftRadius',
  'bottomRightRadius', 'setBottomRightRadius', 'resetBottomRightRadius',
  'hasBevel', 'setBevel', 'resetBevel', 'hasTopLeftBevel', 'setTopLeftBevel',
  'resetTopLeftBevel', 'hasTopRightBevel', 'setTopRightBevel',
  'resetTopRightBevel', 'hasBottomLeftBevel', 'setBottomLeftBevel',
  'resetBottomLeftBevel', 'hasBottomRightBevel', 'setBottomRightBevel',
  'resetBottomRightBevel', 'strokeColor', 'setStrokeColor', 'strokeWidth',
  'setStrokeWidth', 'fillColor', 'setFillColor', 'fillRule', 'setFillRule',
  'joinStyle', 'setJoinStyle', 'miterLimit', 'setMiterLimit', 'capStyle',
  'setCapStyle', 'strokeStyle', 'setStrokeStyle', 'dashOffset',
  'setDashOffset', 'fillGradient', 'setFillGradient', 'resetFillGradient',
  'borderMode', 'setBorderMode', 'resetBorderMode', 'fillItem',
  'setFillItem', 'drawTopChanged', 'drawRightChanged', 'drawBottomChanged',
  'drawLeftChanged', 'fillGradientChanged', 'radiusChanged',
  'topLeftRadiusChanged', 'topRightRadiusChanged', 'bottomLeftRadiusChanged',
  'bottomRightRadiusChanged', 'bevelChanged', 'topLeftBevelChanged',
  'topRightBevelChanged', 'bottomLeftBevelChanged',
  'bottomRightBevelChanged', 'shapePathChanged', 'strokeColorChanged',
  'strokeWidthChanged', 'fillColorChanged', 'fillRuleChanged',
  'joinStyleChanged', 'miterLimitChanged', 'capStyleChanged',
  'strokeStyleChanged', 'dashOffsetChanged', 'dashPatternChanged',
  'borderModeChanged', 'fillItemChanged', 'componentComplete', 'itemChange',
  'updatePolish', 'd_func'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickRectangleShape::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickRectangleShape::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickRectangleShape::~QQuickRectangleShape()': the destructor:
    Python never removes a C++ QQuickRectangleShape.
  - Qt's 'QList<qreal> QQuickRectangleShape::dashPattern() const': gives a
    type Python has no way to take yet.
  - Qt's 'void QQuickRectangleShape::setDashPattern(const QList<qreal>
    &array)': takes a type Python has no way to hand over yet.
  - Qt's 'const QQuickRectangleShapePrivate *QQuickRectangleShape::d_func()
    const': takes in Python what 'QQuickRectangleShapePrivate
    *QQuickRectangleShape::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 113 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickRectangleShape is created at the first use, not by
    'QQuickRectangleShape(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickRectangleShape.
  - Qt tells when it has removed the C++ QQuickRectangleShape. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickRectangleShape that has no cute function yet,
    'dashPattern', 'setDashPattern', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QQuickRectangleShape, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class BorderMode(CuteNum, scoped=True):
    """
    The enum 'QQuickRectangleShape::BorderMode' of Qt, with the 3 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    Inside = Kee[int](0)
    Middle = Kee[int](1)
    Outside = Kee[int](2)

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
    Calls Qt's 'QString QQuickRectangleShape::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrectangleshape.html#tr

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
    #  QString QQuickRectangleShape::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN20QQuickRectangleShape2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickRectangleShape'

  #  A C++ QQuickRectangleShape Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickRectangleShape'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickRectangleShape::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshape.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickRectangleShape::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickRectangleShape10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def drawTop(self) -> bool:
    """
    Calls Qt's 'bool QQuickRectangleShape::drawTop() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrectangleshape.html#drawTop
    """
    #  bool QQuickRectangleShape::drawTop() const
    return self.uglySide.call('ritual_ZNK20QQuickRectangleShape7drawTopEv')

  def drawRight(self) -> bool:
    """
    Calls Qt's 'bool QQuickRectangleShape::drawRight() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshape.html#drawRight
    """
    #  bool QQuickRectangleShape::drawRight() const
    return self.uglySide.call('ritual_ZNK20QQuickRectangleShape9drawRightEv')

  def drawBottom(self) -> bool:
    """
    Calls Qt's 'bool QQuickRectangleShape::drawBottom() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshape.html#drawBottom
    """
    #  bool QQuickRectangleShape::drawBottom() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickRectangleShape10drawBottomEv',
    )

  def drawLeft(self) -> bool:
    """
    Calls Qt's 'bool QQuickRectangleShape::drawLeft() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrectangleshape.html#drawLeft
    """
    #  bool QQuickRectangleShape::drawLeft() const
    return self.uglySide.call('ritual_ZNK20QQuickRectangleShape8drawLeftEv')

  def radius(self) -> int:
    """
    Calls Qt's 'int QQuickRectangleShape::radius() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrectangleshape.html#radius
    """
    #  int QQuickRectangleShape::radius() const
    return self.uglySide.call('ritual_ZNK20QQuickRectangleShape6radiusEv')

  def topLeftRadius(self) -> int:
    """
    Calls Qt's 'int QQuickRectangleShape::topLeftRadius() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshape.html#topLeftRadius
    """
    #  int QQuickRectangleShape::topLeftRadius() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickRectangleShape13topLeftRadiusEv',
    )

  def topRightRadius(self) -> int:
    """
    Calls Qt's 'int QQuickRectangleShape::topRightRadius() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshape.html#topRightRadius
    """
    #  int QQuickRectangleShape::topRightRadius() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickRectangleShape14topRightRadiusEv',
    )

  def bottomLeftRadius(self) -> int:
    """
    Calls Qt's 'int QQuickRectangleShape::bottomLeftRadius() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshape.html#bottomLeftRadius
    """
    #  int QQuickRectangleShape::bottomLeftRadius() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickRectangleShape16bottomLeftRadiusEv',
    )

  def bottomRightRadius(self) -> int:
    """
    Calls Qt's 'int QQuickRectangleShape::bottomRightRadius() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshape.html#bottomRightRadius
    """
    #  int QQuickRectangleShape::bottomRightRadius() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickRectangleShape17bottomRightRadiusEv',
    )

  def hasBevel(self) -> bool:
    """
    Calls Qt's 'bool QQuickRectangleShape::hasBevel() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrectangleshape.html#hasBevel
    """
    #  bool QQuickRectangleShape::hasBevel() const
    return self.uglySide.call('ritual_ZNK20QQuickRectangleShape8hasBevelEv')

  def hasTopLeftBevel(self) -> bool:
    """
    Calls Qt's 'bool QQuickRectangleShape::hasTopLeftBevel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshape.html#hasTopLeftBevel
    """
    #  bool QQuickRectangleShape::hasTopLeftBevel() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickRectangleShape15hasTopLeftBevelEv',
    )

  def hasTopRightBevel(self) -> bool:
    """
    Calls Qt's 'bool QQuickRectangleShape::hasTopRightBevel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshape.html#hasTopRightBevel
    """
    #  bool QQuickRectangleShape::hasTopRightBevel() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickRectangleShape16hasTopRightBevelEv',
    )

  def hasBottomLeftBevel(self) -> bool:
    """
    Calls Qt's 'bool QQuickRectangleShape::hasBottomLeftBevel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshape.html#hasBottomLeftBevel
    """
    #  bool QQuickRectangleShape::hasBottomLeftBevel() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickRectangleShape18hasBottomLeftBevelEv',
    )

  def hasBottomRightBevel(self) -> bool:
    """
    Calls Qt's 'bool QQuickRectangleShape::hasBottomRightBevel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshape.html#hasBottomRightBevel
    """
    #  bool QQuickRectangleShape::hasBottomRightBevel() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickRectangleShape19hasBottomRightBevelEv',
    )

  def strokeColor(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickRectangleShape::strokeColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshape.html#strokeColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickRectangleShape::strokeColor() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickRectangleShape11strokeColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def strokeWidth(self) -> float:
    """
    Calls Qt's 'qreal QQuickRectangleShape::strokeWidth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshape.html#strokeWidth
    """
    #  qreal QQuickRectangleShape::strokeWidth() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickRectangleShape11strokeWidthEv',
    )

  def fillColor(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickRectangleShape::fillColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshape.html#fillColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickRectangleShape::fillColor() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickRectangleShape9fillColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def fillRule(self) -> QQuickShapePath.FillRule:
    """
    Calls Qt's 'QQuickShapePath::FillRule QQuickRectangleShape::fillRule()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrectangleshape.html#fillRule

    Returns
    -------

    QQuickShapePath.FillRule
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQuickShapePath.FillRule(number)' gives.
    """
    #  QQuickShapePath::FillRule QQuickRectangleShape::fillRule() const
    return QQuickShapePath.FillRule(self.uglySide.call(
        'ritual_ZNK20QQuickRectangleShape8fillRuleEv',
    ))

  def joinStyle(self) -> QQuickShapePath.JoinStyle:
    """
    Calls Qt's 'QQuickShapePath::JoinStyle QQuickRectangleShape::joinStyle()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshape.html#joinStyle

    Returns
    -------

    QQuickShapePath.JoinStyle
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQuickShapePath.JoinStyle(number)' gives.
    """
    #  QQuickShapePath::JoinStyle QQuickRectangleShape::joinStyle() const
    return QQuickShapePath.JoinStyle(self.uglySide.call(
        'ritual_ZNK20QQuickRectangleShape9joinStyleEv',
    ))

  def miterLimit(self) -> int:
    """
    Calls Qt's 'int QQuickRectangleShape::miterLimit() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshape.html#miterLimit
    """
    #  int QQuickRectangleShape::miterLimit() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickRectangleShape10miterLimitEv',
    )

  def capStyle(self) -> QQuickShapePath.CapStyle:
    """
    Calls Qt's 'QQuickShapePath::CapStyle QQuickRectangleShape::capStyle()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrectangleshape.html#capStyle

    Returns
    -------

    QQuickShapePath.CapStyle
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQuickShapePath.CapStyle(number)' gives.
    """
    #  QQuickShapePath::CapStyle QQuickRectangleShape::capStyle() const
    return QQuickShapePath.CapStyle(self.uglySide.call(
        'ritual_ZNK20QQuickRectangleShape8capStyleEv',
    ))

  def strokeStyle(self) -> QQuickShapePath.StrokeStyle:
    """
    Calls Qt's 'QQuickShapePath::StrokeStyle
    QQuickRectangleShape::strokeStyle() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshape.html#strokeStyle

    Returns
    -------

    QQuickShapePath.StrokeStyle
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQuickShapePath.StrokeStyle(number)' gives.
    """
    #  QQuickShapePath::StrokeStyle QQuickRectangleShape::strokeStyle() const
    return QQuickShapePath.StrokeStyle(self.uglySide.call(
        'ritual_ZNK20QQuickRectangleShape11strokeStyleEv',
    ))

  def dashOffset(self) -> float:
    """
    Calls Qt's 'qreal QQuickRectangleShape::dashOffset() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshape.html#dashOffset
    """
    #  qreal QQuickRectangleShape::dashOffset() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickRectangleShape10dashOffsetEv',
    )

  def fillGradient(self) -> Optional[QQuickShapeGradient]:
    """
    Calls Qt's 'QQuickShapeGradient *QQuickRectangleShape::fillGradient()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshape.html#fillGradient

    Returns
    -------

    Optional[QQuickShapeGradient]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickShapeGradient *QQuickRectangleShape::fillGradient() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickRectangleShape12fillGradientEv',
    )
    from ..QtQuickShapes import QQuickShapeGradient
    return QQuickShapeGradient._cuteAt(address)

  def borderMode(self) -> BorderMode:
    """
    Calls Qt's 'BorderMode QQuickRectangleShape::borderMode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshape.html#borderMode

    Returns
    -------

    BorderMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'BorderMode(number)'
      gives.
    """
    #  BorderMode QQuickRectangleShape::borderMode() const
    return QQuickRectangleShape.BorderMode(self.uglySide.call(
        'ritual_ZNK20QQuickRectangleShape10borderModeEv',
    ))

  def fillItem(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickRectangleShape::fillItem() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrectangleshape.html#fillItem

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickRectangleShape::fillItem() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickRectangleShape8fillItemEv',
    )
    return QQuickItem._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setDrawTop(self, drawTop: bool) -> None:
    """
    Calls Qt's 'void QQuickRectangleShape::setDrawTop(bool drawTop)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshape.html#setDrawTop

    Parameters
    ----------

    drawTop : bool
      Passed on as it is.
    """
    #  void QQuickRectangleShape::setDrawTop(bool drawTop)
    self.uglySide.call(
        'ritual_ZN20QQuickRectangleShape10setDrawTopEb', drawTop,
    )

  @overload(bool)
  def setDrawRight(self, drawRight: bool) -> None:
    """
    Calls Qt's 'void QQuickRectangleShape::setDrawRight(bool drawRight)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshape.html#setDrawRight

    Parameters
    ----------

    drawRight : bool
      Passed on as it is.
    """
    #  void QQuickRectangleShape::setDrawRight(bool drawRight)
    self.uglySide.call(
        'ritual_ZN20QQuickRectangleShape12setDrawRightEb', drawRight,
    )

  @overload(bool)
  def setDrawBottom(self, drawBottom: bool) -> None:
    """
    Calls Qt's 'void QQuickRectangleShape::setDrawBottom(bool drawBottom)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshape.html#setDrawBottom

    Parameters
    ----------

    drawBottom : bool
      Passed on as it is.
    """
    #  void QQuickRectangleShape::setDrawBottom(bool drawBottom)
    self.uglySide.call(
        'ritual_ZN20QQuickRectangleShape13setDrawBottomEb', drawBottom,
    )

  @overload(bool)
  def setDrawLeft(self, drawLeft: bool) -> None:
    """
    Calls Qt's 'void QQuickRectangleShape::setDrawLeft(bool drawLeft)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshape.html#setDrawLeft

    Parameters
    ----------

    drawLeft : bool
      Passed on as it is.
    """
    #  void QQuickRectangleShape::setDrawLeft(bool drawLeft)
    self.uglySide.call(
        'ritual_ZN20QQuickRectangleShape11setDrawLeftEb', drawLeft,
    )

  @overload(int)
  def setRadius(self, radius: int) -> None:
    """
    Calls Qt's 'void QQuickRectangleShape::setRadius(int radius)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshape.html#setRadius

    Parameters
    ----------

    radius : int
      Passed on as it is.
    """
    #  void QQuickRectangleShape::setRadius(int radius)
    self.uglySide.call('ritual_ZN20QQuickRectangleShape9setRadiusEi', radius)

  @overload(int)
  def setTopLeftRadius(self, topLeftRadius: int) -> None:
    """
    Calls Qt's 'void QQuickRectangleShape::setTopLeftRadius(int
    topLeftRadius)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshape.html#setTopLeftRadius

    Parameters
    ----------

    topLeftRadius : int
      Passed on as it is.
    """
    #  void QQuickRectangleShape::setTopLeftRadius(int topLeftRadius)
    self.uglySide.call(
        'ritual_ZN20QQuickRectangleShape16setTopLeftRadiusEi', topLeftRadius,
    )

  @overload(int)
  def setTopRightRadius(self, topRightRadius: int) -> None:
    """
    Calls Qt's 'void QQuickRectangleShape::setTopRightRadius(int
    topRightRadius)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshape.html#setTopRightRadius

    Parameters
    ----------

    topRightRadius : int
      Passed on as it is.
    """
    #  void QQuickRectangleShape::setTopRightRadius(int topRightRadius)
    self.uglySide.call(
        'ritual_ZN20QQuickRectangleShape17setTopRightRadiusEi',
        topRightRadius,
    )

  @overload(int)
  def setBottomLeftRadius(self, bottomLeftRadius: int) -> None:
    """
    Calls Qt's 'void QQuickRectangleShape::setBottomLeftRadius(int
    bottomLeftRadius)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshape.html#setBottomLeftRadius

    Parameters
    ----------

    bottomLeftRadius : int
      Passed on as it is.
    """
    #  void QQuickRectangleShape::setBottomLeftRadius(int bottomLeftRadius)
    self.uglySide.call(
        'ritual_ZN20QQuickRectangleShape19setBottomLeftRadiusEi',
        bottomLeftRadius,
    )

  @overload(int)
  def setBottomRightRadius(self, bottomRightRadius: int) -> None:
    """
    Calls Qt's 'void QQuickRectangleShape::setBottomRightRadius(int
    bottomRightRadius)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshape.html#setBottomRightRadius

    Parameters
    ----------

    bottomRightRadius : int
      Passed on as it is.
    """
    #  void QQuickRectangleShape::setBottomRightRadius(int bottomRightRadius)
    self.uglySide.call(
        'ritual_ZN20QQuickRectangleShape20setBottomRightRadiusEi',
        bottomRightRadius,
    )

  @overload(bool)
  def setBevel(self, bevel: bool) -> None:
    """
    Calls Qt's 'void QQuickRectangleShape::setBevel(bool bevel)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrectangleshape.html#setBevel

    Parameters
    ----------

    bevel : bool
      Passed on as it is.
    """
    #  void QQuickRectangleShape::setBevel(bool bevel)
    self.uglySide.call('ritual_ZN20QQuickRectangleShape8setBevelEb', bevel)

  @overload(bool)
  def setTopLeftBevel(self, topLeftBevel: bool) -> None:
    """
    Calls Qt's 'void QQuickRectangleShape::setTopLeftBevel(bool
    topLeftBevel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshape.html#setTopLeftBevel

    Parameters
    ----------

    topLeftBevel : bool
      Passed on as it is.
    """
    #  void QQuickRectangleShape::setTopLeftBevel(bool topLeftBevel)
    self.uglySide.call(
        'ritual_ZN20QQuickRectangleShape15setTopLeftBevelEb', topLeftBevel,
    )

  @overload(bool)
  def setTopRightBevel(self, topRightBevel: bool) -> None:
    """
    Calls Qt's 'void QQuickRectangleShape::setTopRightBevel(bool
    topRightBevel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshape.html#setTopRightBevel

    Parameters
    ----------

    topRightBevel : bool
      Passed on as it is.
    """
    #  void QQuickRectangleShape::setTopRightBevel(bool topRightBevel)
    self.uglySide.call(
        'ritual_ZN20QQuickRectangleShape16setTopRightBevelEb', topRightBevel,
    )

  @overload(bool)
  def setBottomLeftBevel(self, bottomLeftBevel: bool) -> None:
    """
    Calls Qt's 'void QQuickRectangleShape::setBottomLeftBevel(bool
    bottomLeftBevel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshape.html#setBottomLeftBevel

    Parameters
    ----------

    bottomLeftBevel : bool
      Passed on as it is.
    """
    #  void QQuickRectangleShape::setBottomLeftBevel(bool bottomLeftBevel)
    self.uglySide.call(
        'ritual_ZN20QQuickRectangleShape18setBottomLeftBevelEb',
        bottomLeftBevel,
    )

  @overload(bool)
  def setBottomRightBevel(self, bottomRightBevel: bool) -> None:
    """
    Calls Qt's 'void QQuickRectangleShape::setBottomRightBevel(bool
    bottomRightBevel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshape.html#setBottomRightBevel

    Parameters
    ----------

    bottomRightBevel : bool
      Passed on as it is.
    """
    #  void QQuickRectangleShape::setBottomRightBevel(bool bottomRightBevel)
    self.uglySide.call(
        'ritual_ZN20QQuickRectangleShape19setBottomRightBevelEb',
        bottomRightBevel,
    )

  @overload(QColor)
  def setStrokeColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QQuickRectangleShape::setStrokeColor(const QColor
    &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshape.html#setStrokeColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickRectangleShape::setStrokeColor(const QColor &color)
    self.uglySide.call(
        'ritual_ZN20QQuickRectangleShape14setStrokeColorERK6QColor',
        self._valueOf(color),
    )

  @overload(float)
  def setStrokeWidth(self, width: float) -> None:
    """
    Calls Qt's 'void QQuickRectangleShape::setStrokeWidth(qreal width)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshape.html#setStrokeWidth

    Parameters
    ----------

    width : float
      Passed on as it is.
    """
    #  void QQuickRectangleShape::setStrokeWidth(qreal width)
    self.uglySide.call(
        'ritual_ZN20QQuickRectangleShape14setStrokeWidthEd', width,
    )

  @overload(QColor)
  def setFillColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QQuickRectangleShape::setFillColor(const QColor
    &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshape.html#setFillColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickRectangleShape::setFillColor(const QColor &color)
    self.uglySide.call(
        'ritual_ZN20QQuickRectangleShape12setFillColorERK6QColor',
        self._valueOf(color),
    )

  @overload(QQuickShapePath.FillRule)
  def setFillRule(self, fillRule: QQuickShapePath.FillRule) -> None:
    """
    Calls Qt's 'void
    QQuickRectangleShape::setFillRule(QQuickShapePath::FillRule fillRule)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshape.html#setFillRule

    Parameters
    ----------

    fillRule : QQuickShapePath.FillRule
      Passed on as its number.
    """
    #  void QQuickRectangleShape::setFillRule(QQuickShapePath::FillRule
    #      fillRule)
    self.uglySide.call(
        'ritual_ZN20QQuickRectangleShape11setFillRuleEN15QQuickShapePath8Fi'
        'llRuleE',
        fillRule.value,
    )

  @overload(QQuickShapePath.JoinStyle)
  def setJoinStyle(self, style: QQuickShapePath.JoinStyle) -> None:
    """
    Calls Qt's 'void
    QQuickRectangleShape::setJoinStyle(QQuickShapePath::JoinStyle style)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshape.html#setJoinStyle

    Parameters
    ----------

    style : QQuickShapePath.JoinStyle
      Passed on as its number.
    """
    #  void QQuickRectangleShape::setJoinStyle(QQuickShapePath::JoinStyle
    #      style)
    self.uglySide.call(
        'ritual_ZN20QQuickRectangleShape12setJoinStyleEN15QQuickShapePath9J'
        'oinStyleE',
        style.value,
    )

  @overload(int)
  def setMiterLimit(self, limit: int) -> None:
    """
    Calls Qt's 'void QQuickRectangleShape::setMiterLimit(int limit)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshape.html#setMiterLimit

    Parameters
    ----------

    limit : int
      Passed on as it is.
    """
    #  void QQuickRectangleShape::setMiterLimit(int limit)
    self.uglySide.call(
        'ritual_ZN20QQuickRectangleShape13setMiterLimitEi', limit,
    )

  @overload(QQuickShapePath.CapStyle)
  def setCapStyle(self, style: QQuickShapePath.CapStyle) -> None:
    """
    Calls Qt's 'void
    QQuickRectangleShape::setCapStyle(QQuickShapePath::CapStyle style)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshape.html#setCapStyle

    Parameters
    ----------

    style : QQuickShapePath.CapStyle
      Passed on as its number.
    """
    #  void QQuickRectangleShape::setCapStyle(QQuickShapePath::CapStyle
    #      style)
    self.uglySide.call(
        'ritual_ZN20QQuickRectangleShape11setCapStyleEN15QQuickShapePath8Ca'
        'pStyleE',
        style.value,
    )

  @overload(QQuickShapePath.StrokeStyle)
  def setStrokeStyle(self, style: QQuickShapePath.StrokeStyle) -> None:
    """
    Calls Qt's 'void
    QQuickRectangleShape::setStrokeStyle(QQuickShapePath::StrokeStyle
    style)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshape.html#setStrokeStyle

    Parameters
    ----------

    style : QQuickShapePath.StrokeStyle
      Passed on as its number.
    """
    #  void QQuickRectangleShape::setStrokeStyle(QQuickShapePath::StrokeStyle
    #      style)
    self.uglySide.call(
        'ritual_ZN20QQuickRectangleShape14setStrokeStyleEN15QQuickShapePath'
        '11StrokeStyleE',
        style.value,
    )

  @overload(float)
  def setDashOffset(self, offset: float) -> None:
    """
    Calls Qt's 'void QQuickRectangleShape::setDashOffset(qreal offset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshape.html#setDashOffset

    Parameters
    ----------

    offset : float
      Passed on as it is.
    """
    #  void QQuickRectangleShape::setDashOffset(qreal offset)
    self.uglySide.call(
        'ritual_ZN20QQuickRectangleShape13setDashOffsetEd', offset,
    )

  @overload(QQuickShapeGradient)
  @overload(NoneType)
  def setFillGradient(
      self,
      fillGradient: Optional[QQuickShapeGradient],
  ) -> None:
    """
    Calls Qt's 'void
    QQuickRectangleShape::setFillGradient(QQuickShapeGradient
    *fillGradient)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshape.html#setFillGradient

    Parameters
    ----------

    fillGradient : Optional[QQuickShapeGradient]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickRectangleShape::setFillGradient(QQuickShapeGradient
    #      *fillGradient)
    self.uglySide.call(
        'ritual_ZN20QQuickRectangleShape15setFillGradientEP19QQuickShapeGra'
        'dient',
        self._addressOf(fillGradient),
    )

  @overload(BorderMode)
  def setBorderMode(self, borderMode: BorderMode) -> None:
    """
    Calls Qt's 'void QQuickRectangleShape::setBorderMode(BorderMode
    borderMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshape.html#setBorderMode

    Parameters
    ----------

    borderMode : BorderMode
      Passed on as its number.
    """
    #  void QQuickRectangleShape::setBorderMode(BorderMode borderMode)
    self.uglySide.call(
        'ritual_ZN20QQuickRectangleShape13setBorderModeENS_10BorderModeE',
        borderMode.value,
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def setFillItem(self, newFillItem: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickRectangleShape::setFillItem(QQuickItem
    *newFillItem)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshape.html#setFillItem

    Parameters
    ----------

    newFillItem : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickRectangleShape::setFillItem(QQuickItem *newFillItem)
    self.uglySide.call(
        'ritual_ZN20QQuickRectangleShape11setFillItemEP10QQuickItem',
        self._addressOf(newFillItem),
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
    'QQuickRectangleShape::QQuickRectangleShape(QQuickItem *parent)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshape.html#QQuickRectangleShape

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickRectangleShape::QQuickRectangleShape(QQuickItem *parent)
    self._noteCreation(QQuickRectangleShape, lambda: Rituals.call(
        'ritual_ZN20QQuickRectangleShapeC1EP10QQuickItem',
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

  def resetDrawTop(self) -> None:
    """
    Calls Qt's 'void QQuickRectangleShape::resetDrawTop()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshape.html#resetDrawTop
    """
    #  void QQuickRectangleShape::resetDrawTop()
    self.uglySide.call('ritual_ZN20QQuickRectangleShape12resetDrawTopEv')

  def resetDrawRight(self) -> None:
    """
    Calls Qt's 'void QQuickRectangleShape::resetDrawRight()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshape.html#resetDrawRight
    """
    #  void QQuickRectangleShape::resetDrawRight()
    self.uglySide.call('ritual_ZN20QQuickRectangleShape14resetDrawRightEv')

  def resetDrawBottom(self) -> None:
    """
    Calls Qt's 'void QQuickRectangleShape::resetDrawBottom()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshape.html#resetDrawBottom
    """
    #  void QQuickRectangleShape::resetDrawBottom()
    self.uglySide.call('ritual_ZN20QQuickRectangleShape15resetDrawBottomEv')

  def resetDrawLeft(self) -> None:
    """
    Calls Qt's 'void QQuickRectangleShape::resetDrawLeft()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshape.html#resetDrawLeft
    """
    #  void QQuickRectangleShape::resetDrawLeft()
    self.uglySide.call('ritual_ZN20QQuickRectangleShape13resetDrawLeftEv')

  def resetRadius(self) -> None:
    """
    Calls Qt's 'void QQuickRectangleShape::resetRadius()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshape.html#resetRadius
    """
    #  void QQuickRectangleShape::resetRadius()
    self.uglySide.call('ritual_ZN20QQuickRectangleShape11resetRadiusEv')

  def resetTopLeftRadius(self) -> None:
    """
    Calls Qt's 'void QQuickRectangleShape::resetTopLeftRadius()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshape.html#resetTopLeftRadius
    """
    #  void QQuickRectangleShape::resetTopLeftRadius()
    self.uglySide.call(
        'ritual_ZN20QQuickRectangleShape18resetTopLeftRadiusEv',
    )

  def resetTopRightRadius(self) -> None:
    """
    Calls Qt's 'void QQuickRectangleShape::resetTopRightRadius()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshape.html#resetTopRightRadius
    """
    #  void QQuickRectangleShape::resetTopRightRadius()
    self.uglySide.call(
        'ritual_ZN20QQuickRectangleShape19resetTopRightRadiusEv',
    )

  def resetBottomLeftRadius(self) -> None:
    """
    Calls Qt's 'void QQuickRectangleShape::resetBottomLeftRadius()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshape.html#resetBottomLeftRadius
    """
    #  void QQuickRectangleShape::resetBottomLeftRadius()
    self.uglySide.call(
        'ritual_ZN20QQuickRectangleShape21resetBottomLeftRadiusEv',
    )

  def resetBottomRightRadius(self) -> None:
    """
    Calls Qt's 'void QQuickRectangleShape::resetBottomRightRadius()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshape.html#resetBottomRightRadius
    """
    #  void QQuickRectangleShape::resetBottomRightRadius()
    self.uglySide.call(
        'ritual_ZN20QQuickRectangleShape22resetBottomRightRadiusEv',
    )

  def resetBevel(self) -> None:
    """
    Calls Qt's 'void QQuickRectangleShape::resetBevel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshape.html#resetBevel
    """
    #  void QQuickRectangleShape::resetBevel()
    self.uglySide.call('ritual_ZN20QQuickRectangleShape10resetBevelEv')

  def resetTopLeftBevel(self) -> None:
    """
    Calls Qt's 'void QQuickRectangleShape::resetTopLeftBevel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshape.html#resetTopLeftBevel
    """
    #  void QQuickRectangleShape::resetTopLeftBevel()
    self.uglySide.call(
        'ritual_ZN20QQuickRectangleShape17resetTopLeftBevelEv',
    )

  def resetTopRightBevel(self) -> None:
    """
    Calls Qt's 'void QQuickRectangleShape::resetTopRightBevel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshape.html#resetTopRightBevel
    """
    #  void QQuickRectangleShape::resetTopRightBevel()
    self.uglySide.call(
        'ritual_ZN20QQuickRectangleShape18resetTopRightBevelEv',
    )

  def resetBottomLeftBevel(self) -> None:
    """
    Calls Qt's 'void QQuickRectangleShape::resetBottomLeftBevel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshape.html#resetBottomLeftBevel
    """
    #  void QQuickRectangleShape::resetBottomLeftBevel()
    self.uglySide.call(
        'ritual_ZN20QQuickRectangleShape20resetBottomLeftBevelEv',
    )

  def resetBottomRightBevel(self) -> None:
    """
    Calls Qt's 'void QQuickRectangleShape::resetBottomRightBevel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshape.html#resetBottomRightBevel
    """
    #  void QQuickRectangleShape::resetBottomRightBevel()
    self.uglySide.call(
        'ritual_ZN20QQuickRectangleShape21resetBottomRightBevelEv',
    )

  def resetFillGradient(self) -> None:
    """
    Calls Qt's 'void QQuickRectangleShape::resetFillGradient()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshape.html#resetFillGradient
    """
    #  void QQuickRectangleShape::resetFillGradient()
    self.uglySide.call(
        'ritual_ZN20QQuickRectangleShape17resetFillGradientEv',
    )

  def resetBorderMode(self) -> None:
    """
    Calls Qt's 'void QQuickRectangleShape::resetBorderMode()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshape.html#resetBorderMode
    """
    #  void QQuickRectangleShape::resetBorderMode()
    self.uglySide.call('ritual_ZN20QQuickRectangleShape15resetBorderModeEv')

  def drawTopChanged(self) -> None:
    """
    Calls Qt's 'void QQuickRectangleShape::drawTopChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshape.html#drawTopChanged
    """
    #  void QQuickRectangleShape::drawTopChanged()
    self.uglySide.call('ritual_ZN20QQuickRectangleShape14drawTopChangedEv')

  def drawRightChanged(self) -> None:
    """
    Calls Qt's 'void QQuickRectangleShape::drawRightChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshape.html#drawRightChanged
    """
    #  void QQuickRectangleShape::drawRightChanged()
    self.uglySide.call('ritual_ZN20QQuickRectangleShape16drawRightChangedEv')

  def drawBottomChanged(self) -> None:
    """
    Calls Qt's 'void QQuickRectangleShape::drawBottomChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshape.html#drawBottomChanged
    """
    #  void QQuickRectangleShape::drawBottomChanged()
    self.uglySide.call(
        'ritual_ZN20QQuickRectangleShape17drawBottomChangedEv',
    )

  def drawLeftChanged(self) -> None:
    """
    Calls Qt's 'void QQuickRectangleShape::drawLeftChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshape.html#drawLeftChanged
    """
    #  void QQuickRectangleShape::drawLeftChanged()
    self.uglySide.call('ritual_ZN20QQuickRectangleShape15drawLeftChangedEv')

  def fillGradientChanged(self) -> None:
    """
    Calls Qt's 'void QQuickRectangleShape::fillGradientChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshape.html#fillGradientChanged
    """
    #  void QQuickRectangleShape::fillGradientChanged()
    self.uglySide.call(
        'ritual_ZN20QQuickRectangleShape19fillGradientChangedEv',
    )

  def radiusChanged(self) -> None:
    """
    Calls Qt's 'void QQuickRectangleShape::radiusChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshape.html#radiusChanged
    """
    #  void QQuickRectangleShape::radiusChanged()
    self.uglySide.call('ritual_ZN20QQuickRectangleShape13radiusChangedEv')

  def topLeftRadiusChanged(self) -> None:
    """
    Calls Qt's 'void QQuickRectangleShape::topLeftRadiusChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshape.html#topLeftRadiusChanged
    """
    #  void QQuickRectangleShape::topLeftRadiusChanged()
    self.uglySide.call(
        'ritual_ZN20QQuickRectangleShape20topLeftRadiusChangedEv',
    )

  def topRightRadiusChanged(self) -> None:
    """
    Calls Qt's 'void QQuickRectangleShape::topRightRadiusChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshape.html#topRightRadiusChanged
    """
    #  void QQuickRectangleShape::topRightRadiusChanged()
    self.uglySide.call(
        'ritual_ZN20QQuickRectangleShape21topRightRadiusChangedEv',
    )

  def bottomLeftRadiusChanged(self) -> None:
    """
    Calls Qt's 'void QQuickRectangleShape::bottomLeftRadiusChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshape.html#bottomLeftRadiusChanged
    """
    #  void QQuickRectangleShape::bottomLeftRadiusChanged()
    self.uglySide.call(
        'ritual_ZN20QQuickRectangleShape23bottomLeftRadiusChangedEv',
    )

  def bottomRightRadiusChanged(self) -> None:
    """
    Calls Qt's 'void QQuickRectangleShape::bottomRightRadiusChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshape.html#bottomRightRadiusChanged
    """
    #  void QQuickRectangleShape::bottomRightRadiusChanged()
    self.uglySide.call(
        'ritual_ZN20QQuickRectangleShape24bottomRightRadiusChangedEv',
    )

  def bevelChanged(self) -> None:
    """
    Calls Qt's 'void QQuickRectangleShape::bevelChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshape.html#bevelChanged
    """
    #  void QQuickRectangleShape::bevelChanged()
    self.uglySide.call('ritual_ZN20QQuickRectangleShape12bevelChangedEv')

  def topLeftBevelChanged(self) -> None:
    """
    Calls Qt's 'void QQuickRectangleShape::topLeftBevelChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshape.html#topLeftBevelChanged
    """
    #  void QQuickRectangleShape::topLeftBevelChanged()
    self.uglySide.call(
        'ritual_ZN20QQuickRectangleShape19topLeftBevelChangedEv',
    )

  def topRightBevelChanged(self) -> None:
    """
    Calls Qt's 'void QQuickRectangleShape::topRightBevelChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshape.html#topRightBevelChanged
    """
    #  void QQuickRectangleShape::topRightBevelChanged()
    self.uglySide.call(
        'ritual_ZN20QQuickRectangleShape20topRightBevelChangedEv',
    )

  def bottomLeftBevelChanged(self) -> None:
    """
    Calls Qt's 'void QQuickRectangleShape::bottomLeftBevelChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshape.html#bottomLeftBevelChanged
    """
    #  void QQuickRectangleShape::bottomLeftBevelChanged()
    self.uglySide.call(
        'ritual_ZN20QQuickRectangleShape22bottomLeftBevelChangedEv',
    )

  def bottomRightBevelChanged(self) -> None:
    """
    Calls Qt's 'void QQuickRectangleShape::bottomRightBevelChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshape.html#bottomRightBevelChanged
    """
    #  void QQuickRectangleShape::bottomRightBevelChanged()
    self.uglySide.call(
        'ritual_ZN20QQuickRectangleShape23bottomRightBevelChangedEv',
    )

  def shapePathChanged(self) -> None:
    """
    Calls Qt's 'void QQuickRectangleShape::shapePathChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshape.html#shapePathChanged
    """
    #  void QQuickRectangleShape::shapePathChanged()
    self.uglySide.call('ritual_ZN20QQuickRectangleShape16shapePathChangedEv')

  def strokeColorChanged(self) -> None:
    """
    Calls Qt's 'void QQuickRectangleShape::strokeColorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshape.html#strokeColorChanged
    """
    #  void QQuickRectangleShape::strokeColorChanged()
    self.uglySide.call(
        'ritual_ZN20QQuickRectangleShape18strokeColorChangedEv',
    )

  def strokeWidthChanged(self) -> None:
    """
    Calls Qt's 'void QQuickRectangleShape::strokeWidthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshape.html#strokeWidthChanged
    """
    #  void QQuickRectangleShape::strokeWidthChanged()
    self.uglySide.call(
        'ritual_ZN20QQuickRectangleShape18strokeWidthChangedEv',
    )

  def fillColorChanged(self) -> None:
    """
    Calls Qt's 'void QQuickRectangleShape::fillColorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshape.html#fillColorChanged
    """
    #  void QQuickRectangleShape::fillColorChanged()
    self.uglySide.call('ritual_ZN20QQuickRectangleShape16fillColorChangedEv')

  def fillRuleChanged(self) -> None:
    """
    Calls Qt's 'void QQuickRectangleShape::fillRuleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshape.html#fillRuleChanged
    """
    #  void QQuickRectangleShape::fillRuleChanged()
    self.uglySide.call('ritual_ZN20QQuickRectangleShape15fillRuleChangedEv')

  def joinStyleChanged(self) -> None:
    """
    Calls Qt's 'void QQuickRectangleShape::joinStyleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshape.html#joinStyleChanged
    """
    #  void QQuickRectangleShape::joinStyleChanged()
    self.uglySide.call('ritual_ZN20QQuickRectangleShape16joinStyleChangedEv')

  def miterLimitChanged(self) -> None:
    """
    Calls Qt's 'void QQuickRectangleShape::miterLimitChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshape.html#miterLimitChanged
    """
    #  void QQuickRectangleShape::miterLimitChanged()
    self.uglySide.call(
        'ritual_ZN20QQuickRectangleShape17miterLimitChangedEv',
    )

  def capStyleChanged(self) -> None:
    """
    Calls Qt's 'void QQuickRectangleShape::capStyleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshape.html#capStyleChanged
    """
    #  void QQuickRectangleShape::capStyleChanged()
    self.uglySide.call('ritual_ZN20QQuickRectangleShape15capStyleChangedEv')

  def strokeStyleChanged(self) -> None:
    """
    Calls Qt's 'void QQuickRectangleShape::strokeStyleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshape.html#strokeStyleChanged
    """
    #  void QQuickRectangleShape::strokeStyleChanged()
    self.uglySide.call(
        'ritual_ZN20QQuickRectangleShape18strokeStyleChangedEv',
    )

  def dashOffsetChanged(self) -> None:
    """
    Calls Qt's 'void QQuickRectangleShape::dashOffsetChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshape.html#dashOffsetChanged
    """
    #  void QQuickRectangleShape::dashOffsetChanged()
    self.uglySide.call(
        'ritual_ZN20QQuickRectangleShape17dashOffsetChangedEv',
    )

  def dashPatternChanged(self) -> None:
    """
    Calls Qt's 'void QQuickRectangleShape::dashPatternChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshape.html#dashPatternChanged
    """
    #  void QQuickRectangleShape::dashPatternChanged()
    self.uglySide.call(
        'ritual_ZN20QQuickRectangleShape18dashPatternChangedEv',
    )

  def borderModeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickRectangleShape::borderModeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshape.html#borderModeChanged
    """
    #  void QQuickRectangleShape::borderModeChanged()
    self.uglySide.call(
        'ritual_ZN20QQuickRectangleShape17borderModeChangedEv',
    )

  def fillItemChanged(self) -> None:
    """
    Calls Qt's 'void QQuickRectangleShape::fillItemChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshape.html#fillItemChanged
    """
    #  void QQuickRectangleShape::fillItemChanged()
    self.uglySide.call('ritual_ZN20QQuickRectangleShape15fillItemChangedEv')

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickRectangleShape::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshape.html#componentComplete
    """
    #  void QQuickRectangleShape::componentComplete()
    ritual = 'ritual_ZN20QQuickRectangleShape17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQuickRectangleShape17componentCompleteEv'
    self.uglySide.call(ritual)

  @overload(QQuickItem.ItemChange, QQuickItem.ItemChangeData)
  def itemChange(
      self,
      change: QQuickItem.ItemChange,
      value: QQuickItem.ItemChangeData,
  ) -> None:
    """
    Calls Qt's 'void QQuickRectangleShape::itemChange(ItemChange change,
    const ItemChangeData &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshape.html#itemChange

    Parameters
    ----------

    change : QQuickItem.ItemChange
      Passed on as its number.

    value : QQuickItem.ItemChangeData
      Passed on as a value: Qt reads the C++ QQuickItem::ItemChangeData,
      which stays Python's own.
    """
    #  void QQuickRectangleShape::itemChange(ItemChange change, const
    #      ItemChangeData &value)
    ritual = (
        'ritual_ZN20QQuickRectangleShape10itemChangeEN10QQuickItem10ItemCha'
        'ngeERKNS0_14ItemChangeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQuickRectangleShape10itemChangeEN10QQuickItem10I'
          'temChangeERKNS0_14ItemChangeDataE')
    self.uglySide.call(ritual, change.value, self._valueOf(value))

  def updatePolish(self) -> None:
    """
    Calls Qt's 'void QQuickRectangleShape::updatePolish()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshape.html#updatePolish
    """
    #  void QQuickRectangleShape::updatePolish()
    ritual = 'ritual_ZN20QQuickRectangleShape12updatePolishEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQuickRectangleShape12updatePolishEv'
    self.uglySide.call(ritual)

  def d_func(self) -> Optional[QQuickRectangleShapePrivate]:
    """
    Calls Qt's 'QQuickRectangleShapePrivate *QQuickRectangleShape::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrectangleshape.html#d_func

    Returns
    -------

    Optional[QQuickRectangleShapePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickRectangleShapePrivate *QQuickRectangleShape::d_func()
    address = self.uglySide.call('ritual_ZN20QQuickRectangleShape6d_funcEv')
    from . import QQuickRectangleShapePrivate
    return QQuickRectangleShapePrivate._cuteAt(address)

  @staticmethod
  def dashPattern(*__, **_) -> Never:
    """
    Qt's 'QList<qreal> QQuickRectangleShape::dashPattern() const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQuickRectangleShape.dashPattern' has no cute function yet. Qt's "
        "'QList<qreal> QQuickRectangleShape::dashPattern() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def setDashPattern(*__, **_) -> Never:
    """
    Qt's 'void QQuickRectangleShape::setDashPattern(const QList<qreal>
    &array)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuickRectangleShape.setDashPattern' has no cute function yet. "
        "Qt's 'void QQuickRectangleShape::setDashPattern(const QList<qreal> "
        "&array)': takes a type Python has no way to hand over yet.")
