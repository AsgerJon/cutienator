"""
QLineSeries binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGraphs/qlineseries.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum
from ..occult import Rituals
from ..QtCore import Qt, QObject
from . import QAbstractSeries, QXYSeries

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QPointF
  from ..QtCharts import QLineSeriesPrivate

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QLineSeries(QXYSeries):
  """
  The cute side of Qt's QLineSeries: a plain Python object standing in front
  of one C++ QLineSeries.

  It is built on the cute 'QXYSeries', as Qt's QLineSeries is built on Qt's
  QXYSeries, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QLineSeries that has a ritual and that Python can
  call so far, 24 names in all: 'metaObject', 'tr', 'type', 'width',
  'setWidth', 'capStyle', 'setCapStyle', 'joinStyle', 'setJoinStyle',
  'lineStyle', 'setLineStyle', 'strokeStyle', 'setStrokeStyle', 'dashOffset',
  'setDashOffset', 'dataPointCoordinatesAt', 'widthChanged',
  'capStyleChanged', 'joinStyleChanged', 'lineStyleChanged',
  'strokeStyleChanged', 'dashOffsetChanged', 'componentComplete', 'd_func'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QLineSeries::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QLineSeries::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QLineSeries::~QLineSeries()': the destructor: Python never removes
    a C++ QLineSeries.
  - Qt's 'QList<qreal> QLineSeries::dashPattern() const': gives a type Python
    has no way to take yet.
  - Qt's 'void QLineSeries::setDashPattern(const QList<qreal> &pattern)':
    takes a type Python has no way to hand over yet.
  - Qt's 'void QLineSeries::dashPatternChanged(const QList<qreal>
    &newDashPattern)': takes a type Python has no way to hand over yet.
  - Qt's 'QLineSeries::QLineSeries(QLineSeriesPrivate &dd, QObject *parent)':
    takes a type Python has no way to hand over yet.
  - Qt's 'const QLineSeriesPrivate *QLineSeries::d_func() const': takes in
    Python what 'QLineSeriesPrivate *QLineSeries::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 37 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QLineSeries is created at the first use, not by
    'QLineSeries(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QLineSeries.
  - Qt tells when it has removed the C++ QLineSeries. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's QLineSeries that has no cute function yet,
    'dashPattern', 'dashPatternChanged', 'setDashPattern', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QLineSeries, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class LineStyle(CuteNum, scoped=True):
    """
    The enum 'QLineSeries::LineStyle' of Qt, with the 4 names Qt gives in it.
    C++ keeps these names inside the enum, so the class that holds the enum
    does not have them.
    """

    Straight = Kee[int](0)
    StepLeft = Kee[int](1)
    StepRight = Kee[int](2)
    StepCenter = Kee[int](3)

  class StrokeStyle(CuteNum, scoped=True):
    """
    The enum 'QLineSeries::StrokeStyle' of Qt, with the 2 names Qt gives in
    it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    SolidLine = Kee[int](1)
    DashLine = Kee[int](2)

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
    Calls Qt's 'QString QLineSeries::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qlineseries.html#tr

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
    #  QString QLineSeries::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN11QLineSeries2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QLineSeries'
  #  The part of Qt it is of, as another part has a class of its name too.
  __qt_part__ = 'QtGraphs'

  #  A C++ QLineSeries Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QLineSeries'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QLineSeries::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlineseries.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QLineSeries::metaObject() const
    address = self.uglySide.call('ritual_ZNK11QLineSeries10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def type(self) -> QAbstractSeries.SeriesType:
    """
    Calls Qt's 'QAbstractSeries::SeriesType QLineSeries::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlineseries.html#type

    Returns
    -------

    QAbstractSeries.SeriesType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QAbstractSeries.SeriesType(number)' gives.
    """
    #  QAbstractSeries::SeriesType QLineSeries::type() const
    ritual = 'ritual_ZNK11QLineSeries4typeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QLineSeries4typeEv'
    return QAbstractSeries.SeriesType(self.uglySide.call(ritual))

  def width(self) -> float:
    """
    Calls Qt's 'qreal QLineSeries::width() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlineseries.html#width
    """
    #  qreal QLineSeries::width() const
    return self.uglySide.call('ritual_ZNK11QLineSeries5widthEv')

  def capStyle(self) -> Qt.PenCapStyle:
    """
    Calls Qt's 'Qt::PenCapStyle QLineSeries::capStyle() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlineseries.html#capStyle

    Returns
    -------

    Qt.PenCapStyle
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.PenCapStyle(number)'
      gives.
    """
    #  Qt::PenCapStyle QLineSeries::capStyle() const
    return Qt.PenCapStyle(self.uglySide.call(
        'ritual_ZNK11QLineSeries8capStyleEv',
    ))

  def joinStyle(self) -> Qt.PenJoinStyle:
    """
    Calls Qt's 'Qt::PenJoinStyle QLineSeries::joinStyle() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlineseries.html#joinStyle

    Returns
    -------

    Qt.PenJoinStyle
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.PenJoinStyle(number)'
      gives.
    """
    #  Qt::PenJoinStyle QLineSeries::joinStyle() const
    return Qt.PenJoinStyle(self.uglySide.call(
        'ritual_ZNK11QLineSeries9joinStyleEv',
    ))

  def lineStyle(self) -> LineStyle:
    """
    Calls Qt's 'QLineSeries::LineStyle QLineSeries::lineStyle() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlineseries.html#lineStyle

    Returns
    -------

    LineStyle
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'LineStyle(number)' gives.
    """
    #  QLineSeries::LineStyle QLineSeries::lineStyle() const
    return QLineSeries.LineStyle(self.uglySide.call(
        'ritual_ZNK11QLineSeries9lineStyleEv',
    ))

  def strokeStyle(self) -> StrokeStyle:
    """
    Calls Qt's 'QLineSeries::StrokeStyle QLineSeries::strokeStyle() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlineseries.html#strokeStyle

    Returns
    -------

    StrokeStyle
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'StrokeStyle(number)'
      gives.
    """
    #  QLineSeries::StrokeStyle QLineSeries::strokeStyle() const
    return QLineSeries.StrokeStyle(self.uglySide.call(
        'ritual_ZNK11QLineSeries11strokeStyleEv',
    ))

  def dashOffset(self) -> float:
    """
    Calls Qt's 'qreal QLineSeries::dashOffset() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlineseries.html#dashOffset
    """
    #  qreal QLineSeries::dashOffset() const
    return self.uglySide.call('ritual_ZNK11QLineSeries10dashOffsetEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setWidth(self, newWidth: float) -> None:
    """
    Calls Qt's 'void QLineSeries::setWidth(qreal newWidth)'.

    Qt's own words: https://doc.qt.io/qt-6/qlineseries.html#setWidth

    Parameters
    ----------

    newWidth : float
      Passed on as it is.
    """
    #  void QLineSeries::setWidth(qreal newWidth)
    self.uglySide.call('ritual_ZN11QLineSeries8setWidthEd', newWidth)

  @overload(Qt.PenCapStyle)
  def setCapStyle(self, newCapStyle: Qt.PenCapStyle) -> None:
    """
    Calls Qt's 'void QLineSeries::setCapStyle(Qt::PenCapStyle newCapStyle)'.

    Qt's own words: https://doc.qt.io/qt-6/qlineseries.html#setCapStyle

    Parameters
    ----------

    newCapStyle : Qt.PenCapStyle
      Passed on as its number.
    """
    #  void QLineSeries::setCapStyle(Qt::PenCapStyle newCapStyle)
    self.uglySide.call(
        'ritual_ZN11QLineSeries11setCapStyleEN2Qt11PenCapStyleE',
        newCapStyle.value,
    )

  @overload(Qt.PenJoinStyle)
  def setJoinStyle(self, newJoinStyle: Qt.PenJoinStyle) -> None:
    """
    Calls Qt's 'void QLineSeries::setJoinStyle(Qt::PenJoinStyle
    newJoinStyle)'.

    Qt's own words: https://doc.qt.io/qt-6/qlineseries.html#setJoinStyle

    Parameters
    ----------

    newJoinStyle : Qt.PenJoinStyle
      Passed on as its number.
    """
    #  void QLineSeries::setJoinStyle(Qt::PenJoinStyle newJoinStyle)
    self.uglySide.call(
        'ritual_ZN11QLineSeries12setJoinStyleEN2Qt12PenJoinStyleE',
        newJoinStyle.value,
    )

  @overload(LineStyle)
  def setLineStyle(self, newLineStyle: LineStyle) -> None:
    """
    Calls Qt's 'void QLineSeries::setLineStyle(QLineSeries::LineStyle
    newLineStyle)'.

    Qt's own words: https://doc.qt.io/qt-6/qlineseries.html#setLineStyle

    Parameters
    ----------

    newLineStyle : LineStyle
      Passed on as its number.
    """
    #  void QLineSeries::setLineStyle(QLineSeries::LineStyle newLineStyle)
    self.uglySide.call(
        'ritual_ZN11QLineSeries12setLineStyleENS_9LineStyleE',
        newLineStyle.value,
    )

  @overload(StrokeStyle)
  def setStrokeStyle(self, newStrokeStyle: StrokeStyle) -> None:
    """
    Calls Qt's 'void QLineSeries::setStrokeStyle(QLineSeries::StrokeStyle
    newStrokeStyle)'.

    Qt's own words: https://doc.qt.io/qt-6/qlineseries.html#setStrokeStyle

    Parameters
    ----------

    newStrokeStyle : StrokeStyle
      Passed on as its number.
    """
    #  void QLineSeries::setStrokeStyle(QLineSeries::StrokeStyle
    #      newStrokeStyle)
    self.uglySide.call(
        'ritual_ZN11QLineSeries14setStrokeStyleENS_11StrokeStyleE',
        newStrokeStyle.value,
    )

  @overload(float)
  def setDashOffset(self, newDashOffset: float) -> None:
    """
    Calls Qt's 'void QLineSeries::setDashOffset(qreal newDashOffset)'.

    Qt's own words: https://doc.qt.io/qt-6/qlineseries.html#setDashOffset

    Parameters
    ----------

    newDashOffset : float
      Passed on as it is.
    """
    #  void QLineSeries::setDashOffset(qreal newDashOffset)
    self.uglySide.call(
        'ritual_ZN11QLineSeries13setDashOffsetEd', newDashOffset,
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
    Notes what was given, for Qt's 'QLineSeries::QLineSeries(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qlineseries.html#QLineSeries

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QLineSeries::QLineSeries(QObject *parent)
    self._noteCreation(QLineSeries, lambda: Rituals.call(
        'ritual_ZN11QLineSeriesC1EP7QObject',
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

  @overload(float, float)
  def dataPointCoordinatesAt(self, x: float, y: float) -> QPointF:
    """
    Calls Qt's 'QPointF QLineSeries::dataPointCoordinatesAt(qreal x, qreal
    y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlineseries.html#dataPointCoordinatesAt

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QLineSeries::dataPointCoordinatesAt(qreal x, qreal y)
    address = self.uglySide.call(
        'ritual_ZN11QLineSeries22dataPointCoordinatesAtEdd', x, y,
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def widthChanged(self) -> None:
    """
    Calls Qt's 'void QLineSeries::widthChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qlineseries.html#widthChanged
    """
    #  void QLineSeries::widthChanged()
    self.uglySide.call('ritual_ZN11QLineSeries12widthChangedEv')

  def capStyleChanged(self) -> None:
    """
    Calls Qt's 'void QLineSeries::capStyleChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qlineseries.html#capStyleChanged
    """
    #  void QLineSeries::capStyleChanged()
    self.uglySide.call('ritual_ZN11QLineSeries15capStyleChangedEv')

  @overload(Qt.PenJoinStyle)
  def joinStyleChanged(self, newJoinStyle: Qt.PenJoinStyle) -> None:
    """
    Calls Qt's 'void QLineSeries::joinStyleChanged(Qt::PenJoinStyle
    newJoinStyle)'.

    Qt's own words: https://doc.qt.io/qt-6/qlineseries.html#joinStyleChanged

    Parameters
    ----------

    newJoinStyle : Qt.PenJoinStyle
      Passed on as its number.
    """
    #  void QLineSeries::joinStyleChanged(Qt::PenJoinStyle newJoinStyle)
    self.uglySide.call(
        'ritual_ZN11QLineSeries16joinStyleChangedEN2Qt12PenJoinStyleE',
        newJoinStyle.value,
    )

  @overload(LineStyle)
  def lineStyleChanged(self, newLineStyle: LineStyle) -> None:
    """
    Calls Qt's 'void QLineSeries::lineStyleChanged(QLineSeries::LineStyle
    newLineStyle)'.

    Qt's own words: https://doc.qt.io/qt-6/qlineseries.html#lineStyleChanged

    Parameters
    ----------

    newLineStyle : LineStyle
      Passed on as its number.
    """
    #  void QLineSeries::lineStyleChanged(QLineSeries::LineStyle
    #      newLineStyle)
    self.uglySide.call(
        'ritual_ZN11QLineSeries16lineStyleChangedENS_9LineStyleE',
        newLineStyle.value,
    )

  @overload(StrokeStyle)
  def strokeStyleChanged(self, newStrokeStyle: StrokeStyle) -> None:
    """
    Calls Qt's 'void QLineSeries::strokeStyleChanged(QLineSeries::StrokeStyle
    newStrokeStyle)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlineseries.html#strokeStyleChanged

    Parameters
    ----------

    newStrokeStyle : StrokeStyle
      Passed on as its number.
    """
    #  void QLineSeries::strokeStyleChanged(QLineSeries::StrokeStyle
    #      newStrokeStyle)
    self.uglySide.call(
        'ritual_ZN11QLineSeries18strokeStyleChangedENS_11StrokeStyleE',
        newStrokeStyle.value,
    )

  @overload(float)
  def dashOffsetChanged(self, newDashOffset: float) -> None:
    """
    Calls Qt's 'void QLineSeries::dashOffsetChanged(qreal newDashOffset)'.

    Qt's own words: https://doc.qt.io/qt-6/qlineseries.html#dashOffsetChanged

    Parameters
    ----------

    newDashOffset : float
      Passed on as it is.
    """
    #  void QLineSeries::dashOffsetChanged(qreal newDashOffset)
    self.uglySide.call(
        'ritual_ZN11QLineSeries17dashOffsetChangedEd', newDashOffset,
    )

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QLineSeries::componentComplete()'.

    Qt's own words: https://doc.qt.io/qt-6/qlineseries.html#componentComplete
    """
    #  void QLineSeries::componentComplete()
    ritual = 'ritual_ZN11QLineSeries17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QLineSeries17componentCompleteEv'
    self.uglySide.call(ritual)

  def d_func(self) -> Optional[QLineSeriesPrivate]:
    """
    Calls Qt's 'QLineSeriesPrivate *QLineSeries::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qlineseries.html#d_func

    Returns
    -------

    Optional[QLineSeriesPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLineSeriesPrivate *QLineSeries::d_func()
    address = self.uglySide.call('ritual_ZN11QLineSeries6d_funcEv')
    from ..QtCharts import QLineSeriesPrivate
    return QLineSeriesPrivate._cuteAt(address)

  @staticmethod
  def dashPattern(*__, **_) -> Never:
    """
    Qt's 'QList<qreal> QLineSeries::dashPattern() const': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QLineSeries.dashPattern' has no cute function yet. Qt's "
        "'QList<qreal> QLineSeries::dashPattern() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def dashPatternChanged(*__, **_) -> Never:
    """
    Qt's 'void QLineSeries::dashPatternChanged(const QList<qreal>
    &newDashPattern)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QLineSeries.dashPatternChanged' has no cute function yet. Qt's "
        "'void QLineSeries::dashPatternChanged(const QList<qreal> "
        "&newDashPattern)': takes a type Python has no way to hand over yet."
    )

  @staticmethod
  def setDashPattern(*__, **_) -> Never:
    """
    Qt's 'void QLineSeries::setDashPattern(const QList<qreal> &pattern)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QLineSeries.setDashPattern' has no cute function yet. Qt's 'void "
        "QLineSeries::setDashPattern(const QList<qreal> &pattern)': takes a "
        "type Python has no way to hand over yet.")
