"""
QQuickRegularPolygonShape binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickShapesDesignHelpers/6.12.0/QtQuickShapesDesignHelpers/private/qquickregularpolygonshape_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickRegularPolygonShape to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtQuickShapes import QQuickShapePath
from ..QtQuick import QQuickItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QQuickRegularPolygonShapePrivate
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


class QQuickRegularPolygonShape(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickRegularPolygonShape: a plain Python object
  standing in front of one C++ QQuickRegularPolygonShape.

  What exists
  -----------

  Every function of Qt's QQuickRegularPolygonShape that has a ritual and that
  Python can call so far, 39 names in all: 'metaObject', 'tr', 'dashOffset',
  'setDashOffset', 'cornerRadius', 'setCornerRadius', 'sideCount',
  'setSideCount', 'strokeWidth', 'setStrokeWidth', 'fillColor',
  'setFillColor', 'strokeColor', 'setStrokeColor', 'capStyle', 'setCapStyle',
  'joinStyle', 'setJoinStyle', 'strokeStyle', 'setStrokeStyle',
  'fillGradient', 'setFillGradient', 'resetFillGradient', 'fillItem',
  'setFillItem', 'cornerRadiusChanged', 'sideCountChanged',
  'strokeColorChanged', 'strokeWidthChanged', 'fillColorChanged',
  'joinStyleChanged', 'capStyleChanged', 'strokeStyleChanged',
  'dashOffsetChanged', 'dashPatternChanged', 'fillGradientChanged',
  'fillItemChanged', 'itemChange', 'd_func'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickRegularPolygonShape::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QQuickRegularPolygonShape::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickRegularPolygonShape::~QQuickRegularPolygonShape()': the
    destructor: Python never removes a C++ QQuickRegularPolygonShape.
  - Qt's 'QList<qreal> QQuickRegularPolygonShape::dashPattern() const': gives
    a type Python has no way to take yet.
  - Qt's 'void QQuickRegularPolygonShape::setDashPattern(const QList<qreal>
    &array)': takes a type Python has no way to hand over yet.
  - Qt's 'const QQuickRegularPolygonShapePrivate
    *QQuickRegularPolygonShape::d_func() const': takes in Python what
    'QQuickRegularPolygonShapePrivate *QQuickRegularPolygonShape::d_func()'
    takes.

  What has no ritual
  ------------------

  4 of the 50 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickRegularPolygonShape is created at the first use, not by
    'QQuickRegularPolygonShape(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickRegularPolygonShape.
  - Qt tells when it has removed the C++ QQuickRegularPolygonShape. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickRegularPolygonShape that has no cute function
    yet, 'dashPattern', 'setDashPattern', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

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
    Calls Qt's 'QString QQuickRegularPolygonShape::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickregularpolygonshape.html#tr

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
    #  QString QQuickRegularPolygonShape::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN25QQuickRegularPolygonShape2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickRegularPolygonShape'

  #  A C++ QQuickRegularPolygonShape Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickRegularPolygonShape'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickRegularPolygonShape::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickregularpolygonshape.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickRegularPolygonShape::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK25QQuickRegularPolygonShape10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def dashOffset(self) -> float:
    """
    Calls Qt's 'qreal QQuickRegularPolygonShape::dashOffset() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickregularpolygonshape.html#dashOffset
    """
    #  qreal QQuickRegularPolygonShape::dashOffset() const
    return self.uglySide.call(
        'ritual_ZNK25QQuickRegularPolygonShape10dashOffsetEv',
    )

  def cornerRadius(self) -> float:
    """
    Calls Qt's 'qreal QQuickRegularPolygonShape::cornerRadius() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickregularpolygonshape.html#cornerRadius
    """
    #  qreal QQuickRegularPolygonShape::cornerRadius() const
    return self.uglySide.call(
        'ritual_ZNK25QQuickRegularPolygonShape12cornerRadiusEv',
    )

  def sideCount(self) -> int:
    """
    Calls Qt's 'int QQuickRegularPolygonShape::sideCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickregularpolygonshape.html#sideCount
    """
    #  int QQuickRegularPolygonShape::sideCount() const
    return self.uglySide.call(
        'ritual_ZNK25QQuickRegularPolygonShape9sideCountEv',
    )

  def strokeWidth(self) -> float:
    """
    Calls Qt's 'qreal QQuickRegularPolygonShape::strokeWidth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickregularpolygonshape.html#strokeWidth
    """
    #  qreal QQuickRegularPolygonShape::strokeWidth() const
    return self.uglySide.call(
        'ritual_ZNK25QQuickRegularPolygonShape11strokeWidthEv',
    )

  def fillColor(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickRegularPolygonShape::fillColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickregularpolygonshape.html#fillColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickRegularPolygonShape::fillColor() const
    address = self.uglySide.call(
        'ritual_ZNK25QQuickRegularPolygonShape9fillColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def strokeColor(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickRegularPolygonShape::strokeColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickregularpolygonshape.html#strokeColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickRegularPolygonShape::strokeColor() const
    address = self.uglySide.call(
        'ritual_ZNK25QQuickRegularPolygonShape11strokeColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def capStyle(self) -> QQuickShapePath.CapStyle:
    """
    Calls Qt's 'QQuickShapePath::CapStyle
    QQuickRegularPolygonShape::capStyle() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickregularpolygonshape.html#capStyle

    Returns
    -------

    QQuickShapePath.CapStyle
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQuickShapePath.CapStyle(number)' gives.
    """
    #  QQuickShapePath::CapStyle QQuickRegularPolygonShape::capStyle() const
    return QQuickShapePath.CapStyle(self.uglySide.call(
        'ritual_ZNK25QQuickRegularPolygonShape8capStyleEv',
    ))

  def joinStyle(self) -> QQuickShapePath.JoinStyle:
    """
    Calls Qt's 'QQuickShapePath::JoinStyle
    QQuickRegularPolygonShape::joinStyle() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickregularpolygonshape.html#joinStyle

    Returns
    -------

    QQuickShapePath.JoinStyle
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQuickShapePath.JoinStyle(number)' gives.
    """
    #  QQuickShapePath::JoinStyle QQuickRegularPolygonShape::joinStyle()
    #      const
    return QQuickShapePath.JoinStyle(self.uglySide.call(
        'ritual_ZNK25QQuickRegularPolygonShape9joinStyleEv',
    ))

  def strokeStyle(self) -> QQuickShapePath.StrokeStyle:
    """
    Calls Qt's 'QQuickShapePath::StrokeStyle
    QQuickRegularPolygonShape::strokeStyle() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickregularpolygonshape.html#strokeStyle

    Returns
    -------

    QQuickShapePath.StrokeStyle
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQuickShapePath.StrokeStyle(number)' gives.
    """
    #  QQuickShapePath::StrokeStyle QQuickRegularPolygonShape::strokeStyle()
    #      const
    return QQuickShapePath.StrokeStyle(self.uglySide.call(
        'ritual_ZNK25QQuickRegularPolygonShape11strokeStyleEv',
    ))

  def fillGradient(self) -> Optional[QQuickShapeGradient]:
    """
    Calls Qt's 'QQuickShapeGradient
    *QQuickRegularPolygonShape::fillGradient() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickregularpolygonshape.html#fillGradient

    Returns
    -------

    Optional[QQuickShapeGradient]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickShapeGradient *QQuickRegularPolygonShape::fillGradient() const
    address = self.uglySide.call(
        'ritual_ZNK25QQuickRegularPolygonShape12fillGradientEv',
    )
    from ..QtQuickShapes import QQuickShapeGradient
    return QQuickShapeGradient._cuteAt(address)

  def fillItem(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickRegularPolygonShape::fillItem() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickregularpolygonshape.html#fillItem

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickRegularPolygonShape::fillItem() const
    address = self.uglySide.call(
        'ritual_ZNK25QQuickRegularPolygonShape8fillItemEv',
    )
    return QQuickItem._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setDashOffset(self, offset: float) -> None:
    """
    Calls Qt's 'void QQuickRegularPolygonShape::setDashOffset(qreal offset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickregularpolygonshape.html#setDashOffset

    Parameters
    ----------

    offset : float
      Passed on as it is.
    """
    #  void QQuickRegularPolygonShape::setDashOffset(qreal offset)
    self.uglySide.call(
        'ritual_ZN25QQuickRegularPolygonShape13setDashOffsetEd', offset,
    )

  @overload(float)
  def setCornerRadius(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickRegularPolygonShape::setCornerRadius(qreal a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickregularpolygonshape.html#setCornerRadius

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickRegularPolygonShape::setCornerRadius(qreal a0)
    self.uglySide.call(
        'ritual_ZN25QQuickRegularPolygonShape15setCornerRadiusEd', a0,
    )

  @overload(int)
  def setSideCount(self, a0: int) -> None:
    """
    Calls Qt's 'void QQuickRegularPolygonShape::setSideCount(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickregularpolygonshape.html#setSideCount

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQuickRegularPolygonShape::setSideCount(int a0)
    self.uglySide.call(
        'ritual_ZN25QQuickRegularPolygonShape12setSideCountEi', a0,
    )

  @overload(float)
  def setStrokeWidth(self, width: float) -> None:
    """
    Calls Qt's 'void QQuickRegularPolygonShape::setStrokeWidth(qreal width)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickregularpolygonshape.html#setStrokeWidth

    Parameters
    ----------

    width : float
      Passed on as it is.
    """
    #  void QQuickRegularPolygonShape::setStrokeWidth(qreal width)
    self.uglySide.call(
        'ritual_ZN25QQuickRegularPolygonShape14setStrokeWidthEd', width,
    )

  @overload(QColor)
  def setFillColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QQuickRegularPolygonShape::setFillColor(const QColor
    &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickregularpolygonshape.html#setFillColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickRegularPolygonShape::setFillColor(const QColor &color)
    self.uglySide.call(
        'ritual_ZN25QQuickRegularPolygonShape12setFillColorERK6QColor',
        self._valueOf(color),
    )

  @overload(QColor)
  def setStrokeColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QQuickRegularPolygonShape::setStrokeColor(const QColor
    &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickregularpolygonshape.html#setStrokeColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickRegularPolygonShape::setStrokeColor(const QColor &color)
    self.uglySide.call(
        'ritual_ZN25QQuickRegularPolygonShape14setStrokeColorERK6QColor',
        self._valueOf(color),
    )

  @overload(QQuickShapePath.CapStyle)
  def setCapStyle(self, style: QQuickShapePath.CapStyle) -> None:
    """
    Calls Qt's 'void
    QQuickRegularPolygonShape::setCapStyle(QQuickShapePath::CapStyle style)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickregularpolygonshape.html#setCapStyle

    Parameters
    ----------

    style : QQuickShapePath.CapStyle
      Passed on as its number.
    """
    #  void QQuickRegularPolygonShape::setCapStyle(QQuickShapePath::CapStyle
    #      style)
    self.uglySide.call(
        'ritual_ZN25QQuickRegularPolygonShape11setCapStyleEN15QQuickShapePa'
        'th8CapStyleE',
        style.value,
    )

  @overload(QQuickShapePath.JoinStyle)
  def setJoinStyle(self, style: QQuickShapePath.JoinStyle) -> None:
    """
    Calls Qt's 'void
    QQuickRegularPolygonShape::setJoinStyle(QQuickShapePath::JoinStyle
    style)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickregularpolygonshape.html#setJoinStyle

    Parameters
    ----------

    style : QQuickShapePath.JoinStyle
      Passed on as its number.
    """
    #  void
    #      QQuickRegularPolygonShape::setJoinStyle(QQuickShapePath::JoinStyle
    #      style)
    self.uglySide.call(
        'ritual_ZN25QQuickRegularPolygonShape12setJoinStyleEN15QQuickShapeP'
        'ath9JoinStyleE',
        style.value,
    )

  @overload(QQuickShapePath.StrokeStyle)
  def setStrokeStyle(self, style: QQuickShapePath.StrokeStyle) -> None:
    """
    Calls Qt's 'void
    QQuickRegularPolygonShape::setStrokeStyle(QQuickShapePath::StrokeStyle
    style)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickregularpolygonshape.html#setStrokeStyle

    Parameters
    ----------

    style : QQuickShapePath.StrokeStyle
      Passed on as its number.
    """
    #  void QQuickRegularPolygonShape::setStrokeStyle(QQuickShapePath::
    #      StrokeStyle style)
    self.uglySide.call(
        'ritual_ZN25QQuickRegularPolygonShape14setStrokeStyleEN15QQuickShap'
        'ePath11StrokeStyleE',
        style.value,
    )

  @overload(QQuickShapeGradient)
  @overload(NoneType)
  def setFillGradient(
      self,
      fillGradient: Optional[QQuickShapeGradient],
  ) -> None:
    """
    Calls Qt's 'void
    QQuickRegularPolygonShape::setFillGradient(QQuickShapeGradient
    *fillGradient)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickregularpolygonshape.html#setFillGradient

    Parameters
    ----------

    fillGradient : Optional[QQuickShapeGradient]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickRegularPolygonShape::setFillGradient(QQuickShapeGradient
    #      *fillGradient)
    self.uglySide.call(
        'ritual_ZN25QQuickRegularPolygonShape15setFillGradientEP19QQuickSha'
        'peGradient',
        self._addressOf(fillGradient),
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def setFillItem(self, newFillItem: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickRegularPolygonShape::setFillItem(QQuickItem
    *newFillItem)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickregularpolygonshape.html#setFillItem

    Parameters
    ----------

    newFillItem : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickRegularPolygonShape::setFillItem(QQuickItem *newFillItem)
    self.uglySide.call(
        'ritual_ZN25QQuickRegularPolygonShape11setFillItemEP10QQuickItem',
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
    'QQuickRegularPolygonShape::QQuickRegularPolygonShape(QQuickItem
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickregularpolygonshape.html

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickRegularPolygonShape::QQuickRegularPolygonShape(QQuickItem
    #      *parent)
    self._noteCreation(QQuickRegularPolygonShape, lambda: Rituals.call(
        'ritual_ZN25QQuickRegularPolygonShapeC1EP10QQuickItem',
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

  def resetFillGradient(self) -> None:
    """
    Calls Qt's 'void QQuickRegularPolygonShape::resetFillGradient()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickregularpolygonshape.html#resetFillGradient
    """
    #  void QQuickRegularPolygonShape::resetFillGradient()
    self.uglySide.call(
        'ritual_ZN25QQuickRegularPolygonShape17resetFillGradientEv',
    )

  def cornerRadiusChanged(self) -> None:
    """
    Calls Qt's 'void QQuickRegularPolygonShape::cornerRadiusChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickregularpolygonshape.html#cornerRadiusChanged
    """
    #  void QQuickRegularPolygonShape::cornerRadiusChanged()
    self.uglySide.call(
        'ritual_ZN25QQuickRegularPolygonShape19cornerRadiusChangedEv',
    )

  def sideCountChanged(self) -> None:
    """
    Calls Qt's 'void QQuickRegularPolygonShape::sideCountChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickregularpolygonshape.html#sideCountChanged
    """
    #  void QQuickRegularPolygonShape::sideCountChanged()
    self.uglySide.call(
        'ritual_ZN25QQuickRegularPolygonShape16sideCountChangedEv',
    )

  def strokeColorChanged(self) -> None:
    """
    Calls Qt's 'void QQuickRegularPolygonShape::strokeColorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickregularpolygonshape.html#strokeColorChanged
    """
    #  void QQuickRegularPolygonShape::strokeColorChanged()
    self.uglySide.call(
        'ritual_ZN25QQuickRegularPolygonShape18strokeColorChangedEv',
    )

  def strokeWidthChanged(self) -> None:
    """
    Calls Qt's 'void QQuickRegularPolygonShape::strokeWidthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickregularpolygonshape.html#strokeWidthChanged
    """
    #  void QQuickRegularPolygonShape::strokeWidthChanged()
    self.uglySide.call(
        'ritual_ZN25QQuickRegularPolygonShape18strokeWidthChangedEv',
    )

  def fillColorChanged(self) -> None:
    """
    Calls Qt's 'void QQuickRegularPolygonShape::fillColorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickregularpolygonshape.html#fillColorChanged
    """
    #  void QQuickRegularPolygonShape::fillColorChanged()
    self.uglySide.call(
        'ritual_ZN25QQuickRegularPolygonShape16fillColorChangedEv',
    )

  def joinStyleChanged(self) -> None:
    """
    Calls Qt's 'void QQuickRegularPolygonShape::joinStyleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickregularpolygonshape.html#joinStyleChanged
    """
    #  void QQuickRegularPolygonShape::joinStyleChanged()
    self.uglySide.call(
        'ritual_ZN25QQuickRegularPolygonShape16joinStyleChangedEv',
    )

  def capStyleChanged(self) -> None:
    """
    Calls Qt's 'void QQuickRegularPolygonShape::capStyleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickregularpolygonshape.html#capStyleChanged
    """
    #  void QQuickRegularPolygonShape::capStyleChanged()
    self.uglySide.call(
        'ritual_ZN25QQuickRegularPolygonShape15capStyleChangedEv',
    )

  def strokeStyleChanged(self) -> None:
    """
    Calls Qt's 'void QQuickRegularPolygonShape::strokeStyleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickregularpolygonshape.html#strokeStyleChanged
    """
    #  void QQuickRegularPolygonShape::strokeStyleChanged()
    self.uglySide.call(
        'ritual_ZN25QQuickRegularPolygonShape18strokeStyleChangedEv',
    )

  def dashOffsetChanged(self) -> None:
    """
    Calls Qt's 'void QQuickRegularPolygonShape::dashOffsetChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickregularpolygonshape.html#dashOffsetChanged
    """
    #  void QQuickRegularPolygonShape::dashOffsetChanged()
    self.uglySide.call(
        'ritual_ZN25QQuickRegularPolygonShape17dashOffsetChangedEv',
    )

  def dashPatternChanged(self) -> None:
    """
    Calls Qt's 'void QQuickRegularPolygonShape::dashPatternChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickregularpolygonshape.html#dashPatternChanged
    """
    #  void QQuickRegularPolygonShape::dashPatternChanged()
    self.uglySide.call(
        'ritual_ZN25QQuickRegularPolygonShape18dashPatternChangedEv',
    )

  def fillGradientChanged(self) -> None:
    """
    Calls Qt's 'void QQuickRegularPolygonShape::fillGradientChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickregularpolygonshape.html#fillGradientChanged
    """
    #  void QQuickRegularPolygonShape::fillGradientChanged()
    self.uglySide.call(
        'ritual_ZN25QQuickRegularPolygonShape19fillGradientChangedEv',
    )

  def fillItemChanged(self) -> None:
    """
    Calls Qt's 'void QQuickRegularPolygonShape::fillItemChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickregularpolygonshape.html#fillItemChanged
    """
    #  void QQuickRegularPolygonShape::fillItemChanged()
    self.uglySide.call(
        'ritual_ZN25QQuickRegularPolygonShape15fillItemChangedEv',
    )

  @overload(QQuickItem.ItemChange, QQuickItem.ItemChangeData)
  def itemChange(
      self,
      change: QQuickItem.ItemChange,
      value: QQuickItem.ItemChangeData,
  ) -> None:
    """
    Calls Qt's 'void QQuickRegularPolygonShape::itemChange(ItemChange change,
    const ItemChangeData &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickregularpolygonshape.html#itemChange

    Parameters
    ----------

    change : QQuickItem.ItemChange
      Passed on as its number.

    value : QQuickItem.ItemChangeData
      Passed on as a value: Qt reads the C++ QQuickItem::ItemChangeData,
      which stays Python's own.
    """
    #  void QQuickRegularPolygonShape::itemChange(ItemChange change, const
    #      ItemChangeData &value)
    ritual = (
        'ritual_ZN25QQuickRegularPolygonShape10itemChangeEN10QQuickItem10It'
        'emChangeERKNS0_14ItemChangeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN25QQuickRegularPolygonShape10itemChangeEN10QQuickIt'
          'em10ItemChangeERKNS0_14ItemChangeDataE')
    self.uglySide.call(ritual, change.value, self._valueOf(value))

  def d_func(self) -> Optional[QQuickRegularPolygonShapePrivate]:
    """
    Calls Qt's 'QQuickRegularPolygonShapePrivate
    *QQuickRegularPolygonShape::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickregularpolygonshape.html#d_func

    Returns
    -------

    Optional[QQuickRegularPolygonShapePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickRegularPolygonShapePrivate *QQuickRegularPolygonShape::d_func()
    address = self.uglySide.call(
        'ritual_ZN25QQuickRegularPolygonShape6d_funcEv',
    )
    from . import QQuickRegularPolygonShapePrivate
    return QQuickRegularPolygonShapePrivate._cuteAt(address)

  @staticmethod
  def dashPattern(*__, **_) -> Never:
    """
    Qt's 'QList<qreal> QQuickRegularPolygonShape::dashPattern() const': gives
    a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQuickRegularPolygonShape.dashPattern' has no cute function yet. "
        "Qt's 'QList<qreal> QQuickRegularPolygonShape::dashPattern() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def setDashPattern(*__, **_) -> Never:
    """
    Qt's 'void QQuickRegularPolygonShape::setDashPattern(const QList<qreal>
    &array)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuickRegularPolygonShape.setDashPattern' has no cute function "
        "yet. Qt's 'void QQuickRegularPolygonShape::setDashPattern(const "
        "QList<qreal> &array)': takes a type Python has no way to hand over "
        "yet.")
