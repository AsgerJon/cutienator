"""
QAreaSeries binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/qareaseries.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QAbstractSeries

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QPointF
  from ..QtGui import QBrush, QColor, QFont, QPen
  from . import QAreaSeriesPrivate, QLineSeries
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QBrush = WAIT['QBrush']
  QColor = WAIT['QColor']
  QFont = WAIT['QFont']
  QLineSeries = WAIT['QtCharts:QLineSeries']
  QPen = WAIT['QPen']
  QPointF = WAIT['QPointF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAreaSeries(QAbstractSeries):
  """
  The cute side of Qt's QAreaSeries: a plain Python object standing in front
  of one C++ QAreaSeries.

  It is built on the cute 'QAbstractSeries', as Qt's QAreaSeries is built on
  Qt's QAbstractSeries, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAreaSeries that has a ritual and that Python can
  call so far, 41 names in all: 'metaObject', 'tr', 'type', 'setUpperSeries',
  'upperSeries', 'setLowerSeries', 'lowerSeries', 'setPen', 'pen',
  'setBrush', 'brush', 'setColor', 'color', 'setBorderColor', 'borderColor',
  'setPointsVisible', 'pointsVisible', 'setPointLabelsFormat',
  'pointLabelsFormat', 'setPointLabelsVisible', 'pointLabelsVisible',
  'setPointLabelsFont', 'pointLabelsFont', 'setPointLabelsColor',
  'pointLabelsColor', 'setPointLabelsClipping', 'pointLabelsClipping',
  'clicked', 'hovered', 'pressed', 'released', 'doubleClicked', 'selected',
  'colorChanged', 'borderColorChanged', 'pointLabelsFormatChanged',
  'pointLabelsVisibilityChanged', 'pointLabelsFontChanged',
  'pointLabelsColorChanged', 'pointLabelsClippingChanged', 'd_func'. It can
  be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QAreaSeries::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QAreaSeries::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QAreaSeries::~QAreaSeries()': the destructor: Python never removes
    a C++ QAreaSeries.
  - Qt's 'const QAreaSeriesPrivate *QAreaSeries::d_func() const': takes in
    Python what 'QAreaSeriesPrivate *QAreaSeries::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 51 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QAreaSeries is created at the first use, not by
    'QAreaSeries(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAreaSeries.
  - Qt tells when it has removed the C++ QAreaSeries. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
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
    Calls Qt's 'QString QAreaSeries::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qareaseries.html#tr

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
    #  QString QAreaSeries::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN11QAreaSeries2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAreaSeries'
  #  The part of Qt it is of, as another part has a class of its name too.
  __qt_part__ = 'QtCharts'

  #  A C++ QAreaSeries Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAreaSeries'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QAreaSeries::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qareaseries.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QAreaSeries::metaObject() const
    address = self.uglySide.call('ritual_ZNK11QAreaSeries10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def type(self) -> QAbstractSeries.SeriesType:
    """
    Calls Qt's 'QAbstractSeries::SeriesType QAreaSeries::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qareaseries.html#type

    Returns
    -------

    QAbstractSeries.SeriesType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QAbstractSeries.SeriesType(number)' gives.
    """
    #  QAbstractSeries::SeriesType QAreaSeries::type() const
    ritual = 'ritual_ZNK11QAreaSeries4typeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QAreaSeries4typeEv'
    return QAbstractSeries.SeriesType(self.uglySide.call(ritual))

  def upperSeries(self) -> Optional[QLineSeries]:
    """
    Calls Qt's 'QLineSeries *QAreaSeries::upperSeries() const'.

    Qt's own words: https://doc.qt.io/qt-6/qareaseries.html#upperSeries

    Returns
    -------

    Optional[QLineSeries]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLineSeries *QAreaSeries::upperSeries() const
    address = self.uglySide.call('ritual_ZNK11QAreaSeries11upperSeriesEv')
    from . import QLineSeries
    return QLineSeries._cuteAt(address)

  def lowerSeries(self) -> Optional[QLineSeries]:
    """
    Calls Qt's 'QLineSeries *QAreaSeries::lowerSeries() const'.

    Qt's own words: https://doc.qt.io/qt-6/qareaseries.html#lowerSeries

    Returns
    -------

    Optional[QLineSeries]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLineSeries *QAreaSeries::lowerSeries() const
    address = self.uglySide.call('ritual_ZNK11QAreaSeries11lowerSeriesEv')
    from . import QLineSeries
    return QLineSeries._cuteAt(address)

  def pen(self) -> QPen:
    """
    Calls Qt's 'QPen QAreaSeries::pen() const'.

    Qt's own words: https://doc.qt.io/qt-6/qareaseries.html#pen

    Returns
    -------

    QPen
      A new cute QPen around the copy Qt gave back. Python owns it.
    """
    #  QPen QAreaSeries::pen() const
    address = self.uglySide.call('ritual_ZNK11QAreaSeries3penEv')
    from ..QtGui import QPen
    return QPen._cuteOwning(address)

  def brush(self) -> QBrush:
    """
    Calls Qt's 'QBrush QAreaSeries::brush() const'.

    Qt's own words: https://doc.qt.io/qt-6/qareaseries.html#brush

    Returns
    -------

    QBrush
      A new cute QBrush around the copy Qt gave back. Python owns it.
    """
    #  QBrush QAreaSeries::brush() const
    address = self.uglySide.call('ritual_ZNK11QAreaSeries5brushEv')
    from ..QtGui import QBrush
    return QBrush._cuteOwning(address)

  def color(self) -> QColor:
    """
    Calls Qt's 'QColor QAreaSeries::color() const'.

    Qt's own words: https://doc.qt.io/qt-6/qareaseries.html#color

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QAreaSeries::color() const
    address = self.uglySide.call('ritual_ZNK11QAreaSeries5colorEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def borderColor(self) -> QColor:
    """
    Calls Qt's 'QColor QAreaSeries::borderColor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qareaseries.html#borderColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QAreaSeries::borderColor() const
    address = self.uglySide.call('ritual_ZNK11QAreaSeries11borderColorEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def pointsVisible(self) -> bool:
    """
    Calls Qt's 'bool QAreaSeries::pointsVisible() const'.

    Qt's own words: https://doc.qt.io/qt-6/qareaseries.html#pointsVisible
    """
    #  bool QAreaSeries::pointsVisible() const
    return self.uglySide.call('ritual_ZNK11QAreaSeries13pointsVisibleEv')

  def pointLabelsFormat(self) -> str:
    """
    Calls Qt's 'QString QAreaSeries::pointLabelsFormat() const'.

    Qt's own words: https://doc.qt.io/qt-6/qareaseries.html#pointLabelsFormat

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAreaSeries::pointLabelsFormat() const
    return self.uglySide.call('ritual_ZNK11QAreaSeries17pointLabelsFormatEv')

  def pointLabelsVisible(self) -> bool:
    """
    Calls Qt's 'bool QAreaSeries::pointLabelsVisible() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qareaseries.html#pointLabelsVisible
    """
    #  bool QAreaSeries::pointLabelsVisible() const
    return self.uglySide.call(
        'ritual_ZNK11QAreaSeries18pointLabelsVisibleEv',
    )

  def pointLabelsFont(self) -> QFont:
    """
    Calls Qt's 'QFont QAreaSeries::pointLabelsFont() const'.

    Qt's own words: https://doc.qt.io/qt-6/qareaseries.html#pointLabelsFont

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QAreaSeries::pointLabelsFont() const
    address = self.uglySide.call(
        'ritual_ZNK11QAreaSeries15pointLabelsFontEv',
    )
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  def pointLabelsColor(self) -> QColor:
    """
    Calls Qt's 'QColor QAreaSeries::pointLabelsColor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qareaseries.html#pointLabelsColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QAreaSeries::pointLabelsColor() const
    address = self.uglySide.call(
        'ritual_ZNK11QAreaSeries16pointLabelsColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def pointLabelsClipping(self) -> bool:
    """
    Calls Qt's 'bool QAreaSeries::pointLabelsClipping() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qareaseries.html#pointLabelsClipping
    """
    #  bool QAreaSeries::pointLabelsClipping() const
    return self.uglySide.call(
        'ritual_ZNK11QAreaSeries19pointLabelsClippingEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QLineSeries)
  @overload(NoneType)
  def setUpperSeries(self, series: Optional[QLineSeries]) -> None:
    """
    Calls Qt's 'void QAreaSeries::setUpperSeries(QLineSeries *series)'.

    Qt's own words: https://doc.qt.io/qt-6/qareaseries.html#setUpperSeries

    Parameters
    ----------

    series : Optional[QLineSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAreaSeries::setUpperSeries(QLineSeries *series)
    self.uglySide.call(
        'ritual_ZN11QAreaSeries14setUpperSeriesEP11QLineSeries',
        self._addressOf(series),
    )

  @overload(QLineSeries)
  @overload(NoneType)
  def setLowerSeries(self, series: Optional[QLineSeries]) -> None:
    """
    Calls Qt's 'void QAreaSeries::setLowerSeries(QLineSeries *series)'.

    Qt's own words: https://doc.qt.io/qt-6/qareaseries.html#setLowerSeries

    Parameters
    ----------

    series : Optional[QLineSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAreaSeries::setLowerSeries(QLineSeries *series)
    self.uglySide.call(
        'ritual_ZN11QAreaSeries14setLowerSeriesEP11QLineSeries',
        self._addressOf(series),
    )

  @overload(QPen)
  def setPen(self, pen: QPen) -> None:
    """
    Calls Qt's 'void QAreaSeries::setPen(const QPen &pen)'.

    Qt's own words: https://doc.qt.io/qt-6/qareaseries.html#setPen

    Parameters
    ----------

    pen : QPen
      Passed on as a value: Qt reads the C++ QPen, which stays Python's own.
    """
    #  void QAreaSeries::setPen(const QPen &pen)
    self.uglySide.call(
        'ritual_ZN11QAreaSeries6setPenERK4QPen', self._valueOf(pen),
    )

  @overload(QBrush)
  def setBrush(self, brush: QBrush) -> None:
    """
    Calls Qt's 'void QAreaSeries::setBrush(const QBrush &brush)'.

    Qt's own words: https://doc.qt.io/qt-6/qareaseries.html#setBrush

    Parameters
    ----------

    brush : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.
    """
    #  void QAreaSeries::setBrush(const QBrush &brush)
    self.uglySide.call(
        'ritual_ZN11QAreaSeries8setBrushERK6QBrush', self._valueOf(brush),
    )

  @overload(QColor)
  def setColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QAreaSeries::setColor(const QColor &color)'.

    Qt's own words: https://doc.qt.io/qt-6/qareaseries.html#setColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QAreaSeries::setColor(const QColor &color)
    self.uglySide.call(
        'ritual_ZN11QAreaSeries8setColorERK6QColor', self._valueOf(color),
    )

  @overload(QColor)
  def setBorderColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QAreaSeries::setBorderColor(const QColor &color)'.

    Qt's own words: https://doc.qt.io/qt-6/qareaseries.html#setBorderColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QAreaSeries::setBorderColor(const QColor &color)
    self.uglySide.call(
        'ritual_ZN11QAreaSeries14setBorderColorERK6QColor',
        self._valueOf(color),
    )

  @overload()
  @overload(bool)
  def setPointsVisible(self, visible: bool = True) -> None:
    """
    Calls Qt's 'void QAreaSeries::setPointsVisible(bool visible)'.

    Qt's own words: https://doc.qt.io/qt-6/qareaseries.html#setPointsVisible

    Parameters
    ----------

    visible : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QAreaSeries::setPointsVisible(bool visible)
    self.uglySide.call('ritual_ZN11QAreaSeries16setPointsVisibleEb', visible)

  @overload(str)
  def setPointLabelsFormat(self, format: str) -> None:
    """
    Calls Qt's 'void QAreaSeries::setPointLabelsFormat(const QString
    &format)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qareaseries.html#setPointLabelsFormat

    Parameters
    ----------

    format : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QAreaSeries::setPointLabelsFormat(const QString &format)
    self.uglySide.call(
        'ritual_ZN11QAreaSeries20setPointLabelsFormatERK7QString', format,
    )

  @overload()
  @overload(bool)
  def setPointLabelsVisible(self, visible: bool = True) -> None:
    """
    Calls Qt's 'void QAreaSeries::setPointLabelsVisible(bool visible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qareaseries.html#setPointLabelsVisible

    Parameters
    ----------

    visible : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QAreaSeries::setPointLabelsVisible(bool visible)
    self.uglySide.call(
        'ritual_ZN11QAreaSeries21setPointLabelsVisibleEb', visible,
    )

  @overload(QFont)
  def setPointLabelsFont(self, font: QFont) -> None:
    """
    Calls Qt's 'void QAreaSeries::setPointLabelsFont(const QFont &font)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qareaseries.html#setPointLabelsFont

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QAreaSeries::setPointLabelsFont(const QFont &font)
    self.uglySide.call(
        'ritual_ZN11QAreaSeries18setPointLabelsFontERK5QFont',
        self._valueOf(font),
    )

  @overload(QColor)
  def setPointLabelsColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QAreaSeries::setPointLabelsColor(const QColor &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qareaseries.html#setPointLabelsColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QAreaSeries::setPointLabelsColor(const QColor &color)
    self.uglySide.call(
        'ritual_ZN11QAreaSeries19setPointLabelsColorERK6QColor',
        self._valueOf(color),
    )

  @overload()
  @overload(bool)
  def setPointLabelsClipping(self, enabled: bool = True) -> None:
    """
    Calls Qt's 'void QAreaSeries::setPointLabelsClipping(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qareaseries.html#setPointLabelsClipping

    Parameters
    ----------

    enabled : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QAreaSeries::setPointLabelsClipping(bool enabled)
    self.uglySide.call(
        'ritual_ZN11QAreaSeries22setPointLabelsClippingEb', enabled,
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

  @overload(QLineSeries)
  @overload(QLineSeries, QLineSeries)
  @overload(QLineSeries, NoneType)
  @overload(NoneType, QLineSeries)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      upperSeries: Optional[QLineSeries],
      lowerSeries: Optional[QLineSeries] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QAreaSeries::QAreaSeries(QLineSeries
    *upperSeries, QLineSeries *lowerSeries)', which is called at the first
    use.

    Qt's own words: https://doc.qt.io/qt-6/qareaseries.html#QAreaSeries

    Parameters
    ----------

    upperSeries : Optional[QLineSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    lowerSeries : Optional[QLineSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QAreaSeries::QAreaSeries(QLineSeries *upperSeries, QLineSeries
    #      *lowerSeries)
    self._noteCreation(QAreaSeries, lambda: Rituals.call(
        'ritual_ZN11QAreaSeriesC1EP11QLineSeriesS1_',
        self._addressOf(upperSeries), self._addressOf(lowerSeries),
    ))

  @overload()
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's 'QAreaSeries::QAreaSeries(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qareaseries.html#QAreaSeries

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QAreaSeries::QAreaSeries(QObject *parent)
    self._noteCreation(QAreaSeries, lambda: Rituals.call(
        'ritual_ZN11QAreaSeriesC1EP7QObject',
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

  @overload(QPointF)
  def clicked(self, point: QPointF) -> None:
    """
    Calls Qt's 'void QAreaSeries::clicked(const QPointF &point)'.

    Qt's own words: https://doc.qt.io/qt-6/qareaseries.html#clicked

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QAreaSeries::clicked(const QPointF &point)
    self.uglySide.call(
        'ritual_ZN11QAreaSeries7clickedERK7QPointF',
        self._valueOf(point, 'QPointF'),
    )

  @overload(QPointF, bool)
  def hovered(self, point: QPointF, state: bool) -> None:
    """
    Calls Qt's 'void QAreaSeries::hovered(const QPointF &point, bool state)'.

    Qt's own words: https://doc.qt.io/qt-6/qareaseries.html#hovered

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    state : bool
      Passed on as it is.
    """
    #  void QAreaSeries::hovered(const QPointF &point, bool state)
    self.uglySide.call(
        'ritual_ZN11QAreaSeries7hoveredERK7QPointFb',
        self._valueOf(point, 'QPointF'), state,
    )

  @overload(QPointF)
  def pressed(self, point: QPointF) -> None:
    """
    Calls Qt's 'void QAreaSeries::pressed(const QPointF &point)'.

    Qt's own words: https://doc.qt.io/qt-6/qareaseries.html#pressed

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QAreaSeries::pressed(const QPointF &point)
    self.uglySide.call(
        'ritual_ZN11QAreaSeries7pressedERK7QPointF',
        self._valueOf(point, 'QPointF'),
    )

  @overload(QPointF)
  def released(self, point: QPointF) -> None:
    """
    Calls Qt's 'void QAreaSeries::released(const QPointF &point)'.

    Qt's own words: https://doc.qt.io/qt-6/qareaseries.html#released

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QAreaSeries::released(const QPointF &point)
    self.uglySide.call(
        'ritual_ZN11QAreaSeries8releasedERK7QPointF',
        self._valueOf(point, 'QPointF'),
    )

  @overload(QPointF)
  def doubleClicked(self, point: QPointF) -> None:
    """
    Calls Qt's 'void QAreaSeries::doubleClicked(const QPointF &point)'.

    Qt's own words: https://doc.qt.io/qt-6/qareaseries.html#doubleClicked

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QAreaSeries::doubleClicked(const QPointF &point)
    self.uglySide.call(
        'ritual_ZN11QAreaSeries13doubleClickedERK7QPointF',
        self._valueOf(point, 'QPointF'),
    )

  def selected(self) -> None:
    """
    Calls Qt's 'void QAreaSeries::selected()'.

    Qt's own words: https://doc.qt.io/qt-6/qareaseries.html#selected
    """
    #  void QAreaSeries::selected()
    self.uglySide.call('ritual_ZN11QAreaSeries8selectedEv')

  @overload(QColor)
  def colorChanged(self, color: QColor) -> None:
    """
    Calls Qt's 'void QAreaSeries::colorChanged(QColor color)'.

    Qt's own words: https://doc.qt.io/qt-6/qareaseries.html#colorChanged

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QAreaSeries::colorChanged(QColor color)
    self.uglySide.call(
        'ritual_ZN11QAreaSeries12colorChangedE6QColor', self._valueOf(color),
    )

  @overload(QColor)
  def borderColorChanged(self, color: QColor) -> None:
    """
    Calls Qt's 'void QAreaSeries::borderColorChanged(QColor color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qareaseries.html#borderColorChanged

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QAreaSeries::borderColorChanged(QColor color)
    self.uglySide.call(
        'ritual_ZN11QAreaSeries18borderColorChangedE6QColor',
        self._valueOf(color),
    )

  @overload(str)
  def pointLabelsFormatChanged(self, format: str) -> None:
    """
    Calls Qt's 'void QAreaSeries::pointLabelsFormatChanged(const QString
    &format)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qareaseries.html#pointLabelsFormatChanged

    Parameters
    ----------

    format : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QAreaSeries::pointLabelsFormatChanged(const QString &format)
    self.uglySide.call(
        'ritual_ZN11QAreaSeries24pointLabelsFormatChangedERK7QString',
        format,
    )

  @overload(bool)
  def pointLabelsVisibilityChanged(self, visible: bool) -> None:
    """
    Calls Qt's 'void QAreaSeries::pointLabelsVisibilityChanged(bool
    visible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qareaseries.html#pointLabelsVisibilityChanged

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void QAreaSeries::pointLabelsVisibilityChanged(bool visible)
    self.uglySide.call(
        'ritual_ZN11QAreaSeries28pointLabelsVisibilityChangedEb', visible,
    )

  @overload(QFont)
  def pointLabelsFontChanged(self, font: QFont) -> None:
    """
    Calls Qt's 'void QAreaSeries::pointLabelsFontChanged(const QFont &font)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qareaseries.html#pointLabelsFontChanged

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QAreaSeries::pointLabelsFontChanged(const QFont &font)
    self.uglySide.call(
        'ritual_ZN11QAreaSeries22pointLabelsFontChangedERK5QFont',
        self._valueOf(font),
    )

  @overload(QColor)
  def pointLabelsColorChanged(self, color: QColor) -> None:
    """
    Calls Qt's 'void QAreaSeries::pointLabelsColorChanged(const QColor
    &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qareaseries.html#pointLabelsColorChanged

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QAreaSeries::pointLabelsColorChanged(const QColor &color)
    self.uglySide.call(
        'ritual_ZN11QAreaSeries23pointLabelsColorChangedERK6QColor',
        self._valueOf(color),
    )

  @overload(bool)
  def pointLabelsClippingChanged(self, clipping: bool) -> None:
    """
    Calls Qt's 'void QAreaSeries::pointLabelsClippingChanged(bool clipping)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qareaseries.html#pointLabelsClippingChanged

    Parameters
    ----------

    clipping : bool
      Passed on as it is.
    """
    #  void QAreaSeries::pointLabelsClippingChanged(bool clipping)
    self.uglySide.call(
        'ritual_ZN11QAreaSeries26pointLabelsClippingChangedEb', clipping,
    )

  def d_func(self) -> Optional[QAreaSeriesPrivate]:
    """
    Calls Qt's 'QAreaSeriesPrivate *QAreaSeries::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qareaseries.html#d_func

    Returns
    -------

    Optional[QAreaSeriesPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAreaSeriesPrivate *QAreaSeries::d_func()
    address = self.uglySide.call('ritual_ZN11QAreaSeries6d_funcEv')
    from . import QAreaSeriesPrivate
    return QAreaSeriesPrivate._cuteAt(address)
