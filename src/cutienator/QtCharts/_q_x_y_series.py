"""
QXYSeries binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/qxyseries.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QList
from . import QAbstractSeries

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QPointF
  from ..QtGui import QBrush, QColor, QFont, QImage, QPen
  from . import QXYSeriesPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QBrush = WAIT['QBrush']
  QColor = WAIT['QColor']
  QFont = WAIT['QFont']
  QImage = WAIT['QImage']
  QPen = WAIT['QPen']
  QPointF = WAIT['QPointF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QXYSeries(QAbstractSeries):
  """
  The cute side of Qt's QXYSeries: a plain Python object standing in front of
  one C++ QXYSeries.

  It is built on the cute 'QAbstractSeries', as Qt's QXYSeries is built on
  Qt's QAbstractSeries, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QXYSeries that has a ritual and that Python can call
  so far, 78 names in all: 'metaObject', 'tr', 'append', 'replace', 'remove',
  'removePoints', 'insert', 'clear', 'count', 'points', 'pointsVector', 'at',
  'setPen', 'pen', 'setBrush', 'brush', 'setColor', 'color',
  'setSelectedColor', 'selectedColor', 'setPointsVisible', 'pointsVisible',
  'setPointLabelsFormat', 'pointLabelsFormat', 'setPointLabelsVisible',
  'pointLabelsVisible', 'setPointLabelsFont', 'pointLabelsFont',
  'setPointLabelsColor', 'pointLabelsColor', 'setPointLabelsClipping',
  'pointLabelsClipping', 'isPointSelected', 'selectPoint', 'deselectPoint',
  'setPointSelected', 'selectAllPoints', 'deselectAllPoints',
  'setLightMarker', 'lightMarker', 'setSelectedLightMarker',
  'selectedLightMarker', 'setMarkerSize', 'markerSize',
  'setBestFitLineVisible', 'bestFitLineVisible', 'setBestFitLinePen',
  'bestFitLinePen', 'setBestFitLineColor', 'bestFitLineColor',
  'clearPointConfiguration', 'clearPointsConfiguration', 'clicked',
  'hovered', 'pressed', 'released', 'doubleClicked', 'pointReplaced',
  'pointRemoved', 'pointAdded', 'colorChanged', 'selectedColorChanged',
  'pointsReplaced', 'pointLabelsFormatChanged',
  'pointLabelsVisibilityChanged', 'pointLabelsFontChanged',
  'pointLabelsColorChanged', 'pointLabelsClippingChanged', 'pointsRemoved',
  'penChanged', 'selectedPointsChanged', 'lightMarkerChanged',
  'selectedLightMarkerChanged', 'bestFitLineVisibilityChanged',
  'bestFitLinePenChanged', 'bestFitLineColorChanged', 'markerSizeChanged',
  'd_func'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QXYSeries::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QXYSeries::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QXYSeries::QXYSeries(QXYSeriesPrivate &d, QObject *parent)': takes
    a type Python has no way to hand over yet.
  - Qt's 'QXYSeries::~QXYSeries()': the destructor: Python never removes a
    C++ QXYSeries.
  - Qt's 'QXYSeries &QXYSeries::operator<<(const QPointF &point)': gives a
    type Python has no way to take yet.
  - Qt's 'QXYSeries &QXYSeries::operator<<(const QList<QPointF> &points)':
    gives a type Python has no way to take yet.
  - Qt's 'void QXYSeries::selectPoints(const QList<int> &indexes)': takes a
    type Python has no way to hand over yet.
  - Qt's 'void QXYSeries::deselectPoints(const QList<int> &indexes)': takes a
    type Python has no way to hand over yet.
  - Qt's 'void QXYSeries::toggleSelection(const QList<int> &indexes)': takes
    a type Python has no way to hand over yet.
  - Qt's 'QList<int> QXYSeries::selectedPoints() const': gives a type Python
    has no way to take yet.
  - Qt's 'QPair<qreal, qreal> QXYSeries::bestFitLineEquation(bool &ok)
    const': takes a number to change where it is.
  - Qt's 'void QXYSeries::clearPointConfiguration(const int index, const
    PointConfiguration key)': takes a type Python has no way to hand over
    yet.
  - Qt's 'void QXYSeries::clearPointsConfiguration(const PointConfiguration
    key)': takes a type Python has no way to hand over yet.
  - Qt's 'void QXYSeries::setPointConfiguration(const int index, const
    QHash<PointConfiguration, QVariant> &configuration)': takes a type Python
    has no way to hand over yet.
  - Qt's 'void QXYSeries::setPointConfiguration(const int index, const
    PointConfiguration key, const QVariant &value)': takes a type Python has
    no way to hand over yet.
  - Qt's 'void QXYSeries::setPointsConfiguration(const QHash<int,
    QHash<QXYSeries::PointConfiguration, QVariant>> &pointsConfiguration)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QHash<PointConfiguration, QVariant>
    QXYSeries::pointConfiguration(const int index) const': gives a type
    Python has no way to take yet.
  - Qt's 'PointsConfigurationHash QXYSeries::pointsConfiguration() const':
    gives a type Python has no way to take yet.
  - Qt's 'void QXYSeries::sizeBy(const QList<qreal> &sourceData, const qreal
    minSize, const qreal maxSize)': takes a type Python has no way to hand
    over yet.
  - Qt's 'void QXYSeries::colorBy(const QList<qreal> &sourceData, const
    QLinearGradient &gradient)': takes a type Python has no way to hand over
    yet.
  - Qt's 'void QXYSeries::pointsConfigurationChanged(const
    QXYSeries::PointsConfigurationHash &configuration)': takes a type Python
    has no way to hand over yet.
  - Qt's 'const QXYSeriesPrivate *QXYSeries::d_func() const': takes in Python
    what 'QXYSeriesPrivate *QXYSeries::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 112 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QXYSeries is created at the first use, not by 'QXYSeries(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QXYSeries.
  - Qt tells when it has removed the C++ QXYSeries. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's QXYSeries that has no cute function yet, '__init__',
    'bestFitLineEquation', 'colorBy', 'deselectPoints', 'pointConfiguration',
    'pointsConfiguration', 'pointsConfigurationChanged', 'selectPoints',
    'selectedPoints', 'setPointConfiguration', 'setPointsConfiguration',
    'sizeBy', 'toggleSelection', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QXYSeries, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class PointConfiguration(CuteNum, scoped=True):
    """
    The enum 'QXYSeries::PointConfiguration' of Qt, with the 5 names Qt gives
    in it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    Color = Kee[int](0)
    Size = Kee[int](1)
    Visibility = Kee[int](2)
    LabelVisibility = Kee[int](3)
    LabelFormat = Kee[int](4)

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
    Calls Qt's 'QString QXYSeries::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#tr

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
    #  QString QXYSeries::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN9QXYSeries2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QXYSeries'
  #  The part of Qt it is of, as another part has a class of its name too.
  __qt_part__ = 'QtCharts'

  #  A C++ QXYSeries Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QXYSeries'

  #  The functions Qt calls itself that QXYSeries is the first to declare. A
  #  class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'setPen': (
          ('_ZN9QXYSeries6setPenERK4QPen',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtGui:QPen'),
           )),
      ),
      'setBrush': (
          ('_ZN9QXYSeries8setBrushERK6QBrush',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtGui:QBrush'),
           )),
      ),
      'setColor': (
          ('_ZN9QXYSeries8setColorERK6QColor',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtGui:QColor'),
           )),
      ),
      'color': (
          ('_ZNK9QXYSeries5colorEv',
           ('address', 'value', 'QtGui:QColor'),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QXYSeries::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QXYSeries::metaObject() const
    address = self.uglySide.call('ritual_ZNK9QXYSeries10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def count(self) -> int:
    """
    Calls Qt's 'int QXYSeries::count() const'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#count
    """
    #  int QXYSeries::count() const
    return self.uglySide.call('ritual_ZNK9QXYSeries5countEv')

  def points(self) -> QList[QPointF]:
    """
    Calls Qt's 'QList<QPointF> QXYSeries::points() const'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#points

    Returns
    -------

    QList[QPointF]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QPointF> QXYSeries::points() const
    address = self.uglySide.call('ritual_ZNK9QXYSeries6pointsEv')
    from ..QtCore import QPointF
    return QList[QPointF]._cuteOwning(address)

  def pointsVector(self) -> QList[QPointF]:
    """
    Calls Qt's 'QList<QPointF> QXYSeries::pointsVector() const'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#pointsVector

    Returns
    -------

    QList[QPointF]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QPointF> QXYSeries::pointsVector() const
    address = self.uglySide.call('ritual_ZNK9QXYSeries12pointsVectorEv')
    from ..QtCore import QPointF
    return QList[QPointF]._cuteOwning(address)

  @overload(int)
  def at(self, index: int) -> QPointF:
    """
    Calls Qt's 'const QPointF &QXYSeries::at(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#at

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  const QPointF &QXYSeries::at(int index) const
    address = self.uglySide.call('ritual_ZNK9QXYSeries2atEi', index)
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def pen(self) -> QPen:
    """
    Calls Qt's 'QPen QXYSeries::pen() const'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#pen

    Returns
    -------

    QPen
      A new cute QPen around the copy Qt gave back. Python owns it.
    """
    #  QPen QXYSeries::pen() const
    address = self.uglySide.call('ritual_ZNK9QXYSeries3penEv')
    from ..QtGui import QPen
    return QPen._cuteOwning(address)

  def brush(self) -> QBrush:
    """
    Calls Qt's 'QBrush QXYSeries::brush() const'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#brush

    Returns
    -------

    QBrush
      A new cute QBrush around the copy Qt gave back. Python owns it.
    """
    #  QBrush QXYSeries::brush() const
    address = self.uglySide.call('ritual_ZNK9QXYSeries5brushEv')
    from ..QtGui import QBrush
    return QBrush._cuteOwning(address)

  def color(self) -> QColor:
    """
    Calls Qt's 'QColor QXYSeries::color() const'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#color

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QXYSeries::color() const
    ritual = 'ritual_ZNK9QXYSeries5colorEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK9QXYSeries5colorEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def selectedColor(self) -> QColor:
    """
    Calls Qt's 'QColor QXYSeries::selectedColor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#selectedColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QXYSeries::selectedColor() const
    address = self.uglySide.call('ritual_ZNK9QXYSeries13selectedColorEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def pointsVisible(self) -> bool:
    """
    Calls Qt's 'bool QXYSeries::pointsVisible() const'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#pointsVisible
    """
    #  bool QXYSeries::pointsVisible() const
    return self.uglySide.call('ritual_ZNK9QXYSeries13pointsVisibleEv')

  def pointLabelsFormat(self) -> str:
    """
    Calls Qt's 'QString QXYSeries::pointLabelsFormat() const'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#pointLabelsFormat

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QXYSeries::pointLabelsFormat() const
    return self.uglySide.call('ritual_ZNK9QXYSeries17pointLabelsFormatEv')

  def pointLabelsVisible(self) -> bool:
    """
    Calls Qt's 'bool QXYSeries::pointLabelsVisible() const'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#pointLabelsVisible
    """
    #  bool QXYSeries::pointLabelsVisible() const
    return self.uglySide.call('ritual_ZNK9QXYSeries18pointLabelsVisibleEv')

  def pointLabelsFont(self) -> QFont:
    """
    Calls Qt's 'QFont QXYSeries::pointLabelsFont() const'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#pointLabelsFont

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QXYSeries::pointLabelsFont() const
    address = self.uglySide.call('ritual_ZNK9QXYSeries15pointLabelsFontEv')
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  def pointLabelsColor(self) -> QColor:
    """
    Calls Qt's 'QColor QXYSeries::pointLabelsColor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#pointLabelsColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QXYSeries::pointLabelsColor() const
    address = self.uglySide.call('ritual_ZNK9QXYSeries16pointLabelsColorEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def pointLabelsClipping(self) -> bool:
    """
    Calls Qt's 'bool QXYSeries::pointLabelsClipping() const'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#pointLabelsClipping
    """
    #  bool QXYSeries::pointLabelsClipping() const
    return self.uglySide.call('ritual_ZNK9QXYSeries19pointLabelsClippingEv')

  def lightMarker(self) -> QImage:
    """
    Calls Qt's 'const QImage &QXYSeries::lightMarker() const'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#lightMarker

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  const QImage &QXYSeries::lightMarker() const
    address = self.uglySide.call('ritual_ZNK9QXYSeries11lightMarkerEv')
    from ..QtGui import QImage
    return QImage._cuteOwning(address)

  def selectedLightMarker(self) -> QImage:
    """
    Calls Qt's 'const QImage &QXYSeries::selectedLightMarker() const'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#selectedLightMarker

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  const QImage &QXYSeries::selectedLightMarker() const
    address = self.uglySide.call(
        'ritual_ZNK9QXYSeries19selectedLightMarkerEv',
    )
    from ..QtGui import QImage
    return QImage._cuteOwning(address)

  def markerSize(self) -> float:
    """
    Calls Qt's 'qreal QXYSeries::markerSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#markerSize
    """
    #  qreal QXYSeries::markerSize() const
    return self.uglySide.call('ritual_ZNK9QXYSeries10markerSizeEv')

  def bestFitLineVisible(self) -> bool:
    """
    Calls Qt's 'bool QXYSeries::bestFitLineVisible() const'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#bestFitLineVisible
    """
    #  bool QXYSeries::bestFitLineVisible() const
    return self.uglySide.call('ritual_ZNK9QXYSeries18bestFitLineVisibleEv')

  def bestFitLinePen(self) -> QPen:
    """
    Calls Qt's 'QPen QXYSeries::bestFitLinePen() const'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#bestFitLinePen

    Returns
    -------

    QPen
      A new cute QPen around the copy Qt gave back. Python owns it.
    """
    #  QPen QXYSeries::bestFitLinePen() const
    address = self.uglySide.call('ritual_ZNK9QXYSeries14bestFitLinePenEv')
    from ..QtGui import QPen
    return QPen._cuteOwning(address)

  def bestFitLineColor(self) -> QColor:
    """
    Calls Qt's 'QColor QXYSeries::bestFitLineColor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#bestFitLineColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QXYSeries::bestFitLineColor() const
    address = self.uglySide.call('ritual_ZNK9QXYSeries16bestFitLineColorEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QPen)
  def setPen(self, pen: QPen) -> None:
    """
    Calls Qt's 'void QXYSeries::setPen(const QPen &pen)'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#setPen

    Parameters
    ----------

    pen : QPen
      Passed on as a value: Qt reads the C++ QPen, which stays Python's own.
    """
    #  void QXYSeries::setPen(const QPen &pen)
    ritual = 'ritual_ZN9QXYSeries6setPenERK4QPen'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN9QXYSeries6setPenERK4QPen'
    self.uglySide.call(ritual, self._valueOf(pen))

  @overload(QBrush)
  def setBrush(self, brush: QBrush) -> None:
    """
    Calls Qt's 'void QXYSeries::setBrush(const QBrush &brush)'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#setBrush

    Parameters
    ----------

    brush : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.
    """
    #  void QXYSeries::setBrush(const QBrush &brush)
    ritual = 'ritual_ZN9QXYSeries8setBrushERK6QBrush'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN9QXYSeries8setBrushERK6QBrush'
    self.uglySide.call(ritual, self._valueOf(brush))

  @overload(QColor)
  def setColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QXYSeries::setColor(const QColor &color)'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#setColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QXYSeries::setColor(const QColor &color)
    ritual = 'ritual_ZN9QXYSeries8setColorERK6QColor'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN9QXYSeries8setColorERK6QColor'
    self.uglySide.call(ritual, self._valueOf(color))

  @overload(QColor)
  def setSelectedColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QXYSeries::setSelectedColor(const QColor &color)'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#setSelectedColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QXYSeries::setSelectedColor(const QColor &color)
    self.uglySide.call(
        'ritual_ZN9QXYSeries16setSelectedColorERK6QColor',
        self._valueOf(color),
    )

  @overload()
  @overload(bool)
  def setPointsVisible(self, visible: bool = True) -> None:
    """
    Calls Qt's 'void QXYSeries::setPointsVisible(bool visible)'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#setPointsVisible

    Parameters
    ----------

    visible : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QXYSeries::setPointsVisible(bool visible)
    self.uglySide.call('ritual_ZN9QXYSeries16setPointsVisibleEb', visible)

  @overload(str)
  def setPointLabelsFormat(self, format: str) -> None:
    """
    Calls Qt's 'void QXYSeries::setPointLabelsFormat(const QString &format)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxyseries.html#setPointLabelsFormat

    Parameters
    ----------

    format : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QXYSeries::setPointLabelsFormat(const QString &format)
    self.uglySide.call(
        'ritual_ZN9QXYSeries20setPointLabelsFormatERK7QString', format,
    )

  @overload()
  @overload(bool)
  def setPointLabelsVisible(self, visible: bool = True) -> None:
    """
    Calls Qt's 'void QXYSeries::setPointLabelsVisible(bool visible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxyseries.html#setPointLabelsVisible

    Parameters
    ----------

    visible : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QXYSeries::setPointLabelsVisible(bool visible)
    self.uglySide.call(
        'ritual_ZN9QXYSeries21setPointLabelsVisibleEb', visible,
    )

  @overload(QFont)
  def setPointLabelsFont(self, font: QFont) -> None:
    """
    Calls Qt's 'void QXYSeries::setPointLabelsFont(const QFont &font)'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#setPointLabelsFont

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QXYSeries::setPointLabelsFont(const QFont &font)
    self.uglySide.call(
        'ritual_ZN9QXYSeries18setPointLabelsFontERK5QFont',
        self._valueOf(font),
    )

  @overload(QColor)
  def setPointLabelsColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QXYSeries::setPointLabelsColor(const QColor &color)'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#setPointLabelsColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QXYSeries::setPointLabelsColor(const QColor &color)
    self.uglySide.call(
        'ritual_ZN9QXYSeries19setPointLabelsColorERK6QColor',
        self._valueOf(color),
    )

  @overload()
  @overload(bool)
  def setPointLabelsClipping(self, enabled: bool = True) -> None:
    """
    Calls Qt's 'void QXYSeries::setPointLabelsClipping(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxyseries.html#setPointLabelsClipping

    Parameters
    ----------

    enabled : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QXYSeries::setPointLabelsClipping(bool enabled)
    self.uglySide.call(
        'ritual_ZN9QXYSeries22setPointLabelsClippingEb', enabled,
    )

  @overload(int, bool)
  def setPointSelected(self, index: int, selected: bool) -> None:
    """
    Calls Qt's 'void QXYSeries::setPointSelected(int index, bool selected)'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#setPointSelected

    Parameters
    ----------

    index : int
      Passed on as it is.

    selected : bool
      Passed on as it is.
    """
    #  void QXYSeries::setPointSelected(int index, bool selected)
    self.uglySide.call(
        'ritual_ZN9QXYSeries16setPointSelectedEib', index, selected,
    )

  @overload(QImage)
  def setLightMarker(self, lightMarker: QImage) -> None:
    """
    Calls Qt's 'void QXYSeries::setLightMarker(const QImage &lightMarker)'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#setLightMarker

    Parameters
    ----------

    lightMarker : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.
    """
    #  void QXYSeries::setLightMarker(const QImage &lightMarker)
    self.uglySide.call(
        'ritual_ZN9QXYSeries14setLightMarkerERK6QImage',
        self._valueOf(lightMarker),
    )

  @overload(QImage)
  def setSelectedLightMarker(self, selectedLightMarker: QImage) -> None:
    """
    Calls Qt's 'void QXYSeries::setSelectedLightMarker(const QImage
    &selectedLightMarker)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxyseries.html#setSelectedLightMarker

    Parameters
    ----------

    selectedLightMarker : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.
    """
    #  void QXYSeries::setSelectedLightMarker(const QImage
    #      &selectedLightMarker)
    self.uglySide.call(
        'ritual_ZN9QXYSeries22setSelectedLightMarkerERK6QImage',
        self._valueOf(selectedLightMarker),
    )

  @overload(float)
  def setMarkerSize(self, size: float) -> None:
    """
    Calls Qt's 'void QXYSeries::setMarkerSize(qreal size)'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#setMarkerSize

    Parameters
    ----------

    size : float
      Passed on as it is.
    """
    #  void QXYSeries::setMarkerSize(qreal size)
    self.uglySide.call('ritual_ZN9QXYSeries13setMarkerSizeEd', size)

  @overload()
  @overload(bool)
  def setBestFitLineVisible(self, visible: bool = True) -> None:
    """
    Calls Qt's 'void QXYSeries::setBestFitLineVisible(bool visible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxyseries.html#setBestFitLineVisible

    Parameters
    ----------

    visible : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QXYSeries::setBestFitLineVisible(bool visible)
    self.uglySide.call(
        'ritual_ZN9QXYSeries21setBestFitLineVisibleEb', visible,
    )

  @overload(QPen)
  def setBestFitLinePen(self, pen: QPen) -> None:
    """
    Calls Qt's 'void QXYSeries::setBestFitLinePen(const QPen &pen)'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#setBestFitLinePen

    Parameters
    ----------

    pen : QPen
      Passed on as a value: Qt reads the C++ QPen, which stays Python's own.
    """
    #  void QXYSeries::setBestFitLinePen(const QPen &pen)
    self.uglySide.call(
        'ritual_ZN9QXYSeries17setBestFitLinePenERK4QPen', self._valueOf(pen),
    )

  @overload(QColor)
  def setBestFitLineColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QXYSeries::setBestFitLineColor(const QColor &color)'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#setBestFitLineColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QXYSeries::setBestFitLineColor(const QColor &color)
    self.uglySide.call(
        'ritual_ZN9QXYSeries19setBestFitLineColorERK6QColor',
        self._valueOf(color),
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
    Qt's 'QXYSeries::QXYSeries(QXYSeriesPrivate &d, QObject *parent)': takes
    a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QXYSeries.__init__' has no cute function yet. Qt's "
        "'QXYSeries::QXYSeries(QXYSeriesPrivate &d, QObject *parent)': "
        "takes a type Python has no way to hand over yet.")

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
  def append(self, x: float, y: float) -> None:
    """
    Calls Qt's 'void QXYSeries::append(qreal x, qreal y)'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#append

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void QXYSeries::append(qreal x, qreal y)
    self.uglySide.call('ritual_ZN9QXYSeries6appendEdd', x, y)

  @overload(QPointF)
  def append(self, point: QPointF) -> None:
    """
    Calls Qt's 'void QXYSeries::append(const QPointF &point)'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#append

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QXYSeries::append(const QPointF &point)
    self.uglySide.call(
        'ritual_ZN9QXYSeries6appendERK7QPointF',
        self._valueOf(point, 'QPointF'),
    )

  @overload(QList[QPointF])
  def append(self, points: QList[QPointF]) -> None:
    """
    Calls Qt's 'void QXYSeries::append(const QList<QPointF> &points)'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#append

    Parameters
    ----------

    points : QList[QPointF]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QXYSeries::append(const QList<QPointF> &points)
    self.uglySide.call(
        'ritual_ZN9QXYSeries6appendERK5QListI7QPointFE',
        self._valueOf(points),
    )

  @overload(float, float, float, float)
  def replace(
      self,
      oldX: float,
      oldY: float,
      newX: float,
      newY: float,
  ) -> None:
    """
    Calls Qt's 'void QXYSeries::replace(qreal oldX, qreal oldY, qreal newX,
    qreal newY)'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#replace

    Parameters
    ----------

    oldX : float
      Passed on as it is.

    oldY : float
      Passed on as it is.

    newX : float
      Passed on as it is.

    newY : float
      Passed on as it is.
    """
    #  void QXYSeries::replace(qreal oldX, qreal oldY, qreal newX, qreal
    #      newY)
    self.uglySide.call(
        'ritual_ZN9QXYSeries7replaceEdddd', oldX, oldY, newX, newY,
    )

  @overload(QPointF, QPointF)
  def replace(self, oldPoint: QPointF, newPoint: QPointF) -> None:
    """
    Calls Qt's 'void QXYSeries::replace(const QPointF &oldPoint, const
    QPointF &newPoint)'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#replace

    Parameters
    ----------

    oldPoint : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    newPoint : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QXYSeries::replace(const QPointF &oldPoint, const QPointF
    #      &newPoint)
    self.uglySide.call(
        'ritual_ZN9QXYSeries7replaceERK7QPointFS2_',
        self._valueOf(oldPoint, 'QPointF'), self._valueOf(newPoint,
        'QPointF'),
    )

  @overload(int, float, float)
  def replace(self, index: int, newX: float, newY: float) -> None:
    """
    Calls Qt's 'void QXYSeries::replace(int index, qreal newX, qreal newY)'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#replace

    Parameters
    ----------

    index : int
      Passed on as it is.

    newX : float
      Passed on as it is.

    newY : float
      Passed on as it is.
    """
    #  void QXYSeries::replace(int index, qreal newX, qreal newY)
    self.uglySide.call('ritual_ZN9QXYSeries7replaceEidd', index, newX, newY)

  @overload(int, QPointF)
  def replace(self, index: int, newPoint: QPointF) -> None:
    """
    Calls Qt's 'void QXYSeries::replace(int index, const QPointF &newPoint)'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#replace

    Parameters
    ----------

    index : int
      Passed on as it is.

    newPoint : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QXYSeries::replace(int index, const QPointF &newPoint)
    self.uglySide.call(
        'ritual_ZN9QXYSeries7replaceEiRK7QPointF',
        index, self._valueOf(newPoint, 'QPointF'),
    )

  @overload(QList[QPointF])
  def replace(self, points: QList[QPointF]) -> None:
    """
    Calls Qt's 'void QXYSeries::replace(const QList<QPointF> &points)'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#replace

    Parameters
    ----------

    points : QList[QPointF]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QXYSeries::replace(const QList<QPointF> &points)
    self.uglySide.call(
        'ritual_ZN9QXYSeries7replaceERK5QListI7QPointFE',
        self._valueOf(points),
    )

  @overload(float, float)
  def remove(self, x: float, y: float) -> None:
    """
    Calls Qt's 'void QXYSeries::remove(qreal x, qreal y)'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#remove

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void QXYSeries::remove(qreal x, qreal y)
    self.uglySide.call('ritual_ZN9QXYSeries6removeEdd', x, y)

  @overload(QPointF)
  def remove(self, point: QPointF) -> None:
    """
    Calls Qt's 'void QXYSeries::remove(const QPointF &point)'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#remove

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QXYSeries::remove(const QPointF &point)
    self.uglySide.call(
        'ritual_ZN9QXYSeries6removeERK7QPointF',
        self._valueOf(point, 'QPointF'),
    )

  @overload(int)
  def remove(self, index: int) -> None:
    """
    Calls Qt's 'void QXYSeries::remove(int index)'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#remove

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QXYSeries::remove(int index)
    self.uglySide.call('ritual_ZN9QXYSeries6removeEi', index)

  @overload(int, int)
  def removePoints(self, index: int, count: int) -> None:
    """
    Calls Qt's 'void QXYSeries::removePoints(int index, int count)'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#removePoints

    Parameters
    ----------

    index : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void QXYSeries::removePoints(int index, int count)
    self.uglySide.call('ritual_ZN9QXYSeries12removePointsEii', index, count)

  @overload(int, QPointF)
  def insert(self, index: int, point: QPointF) -> None:
    """
    Calls Qt's 'void QXYSeries::insert(int index, const QPointF &point)'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#insert

    Parameters
    ----------

    index : int
      Passed on as it is.

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QXYSeries::insert(int index, const QPointF &point)
    self.uglySide.call(
        'ritual_ZN9QXYSeries6insertEiRK7QPointF',
        index, self._valueOf(point, 'QPointF'),
    )

  def clear(self) -> None:
    """
    Calls Qt's 'void QXYSeries::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#clear
    """
    #  void QXYSeries::clear()
    self.uglySide.call('ritual_ZN9QXYSeries5clearEv')

  @overload(int)
  def isPointSelected(self, index: int) -> bool:
    """
    Calls Qt's 'bool QXYSeries::isPointSelected(int index)'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#isPointSelected

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  bool QXYSeries::isPointSelected(int index)
    return self.uglySide.call(
        'ritual_ZN9QXYSeries15isPointSelectedEi', index,
    )

  @overload(int)
  def selectPoint(self, index: int) -> None:
    """
    Calls Qt's 'void QXYSeries::selectPoint(int index)'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#selectPoint

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QXYSeries::selectPoint(int index)
    self.uglySide.call('ritual_ZN9QXYSeries11selectPointEi', index)

  @overload(int)
  def deselectPoint(self, index: int) -> None:
    """
    Calls Qt's 'void QXYSeries::deselectPoint(int index)'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#deselectPoint

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QXYSeries::deselectPoint(int index)
    self.uglySide.call('ritual_ZN9QXYSeries13deselectPointEi', index)

  def selectAllPoints(self) -> None:
    """
    Calls Qt's 'void QXYSeries::selectAllPoints()'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#selectAllPoints
    """
    #  void QXYSeries::selectAllPoints()
    self.uglySide.call('ritual_ZN9QXYSeries15selectAllPointsEv')

  def deselectAllPoints(self) -> None:
    """
    Calls Qt's 'void QXYSeries::deselectAllPoints()'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#deselectAllPoints
    """
    #  void QXYSeries::deselectAllPoints()
    self.uglySide.call('ritual_ZN9QXYSeries17deselectAllPointsEv')

  @overload(int)
  def clearPointConfiguration(self, index: int) -> None:
    """
    Calls Qt's 'void QXYSeries::clearPointConfiguration(const int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxyseries.html#clearPointConfiguration

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QXYSeries::clearPointConfiguration(const int index)
    self.uglySide.call(
        'ritual_ZN9QXYSeries23clearPointConfigurationEi', index,
    )

  def clearPointsConfiguration(self) -> None:
    """
    Calls Qt's 'void QXYSeries::clearPointsConfiguration()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxyseries.html#clearPointsConfiguration
    """
    #  void QXYSeries::clearPointsConfiguration()
    self.uglySide.call('ritual_ZN9QXYSeries24clearPointsConfigurationEv')

  @overload(QPointF)
  def clicked(self, point: QPointF) -> None:
    """
    Calls Qt's 'void QXYSeries::clicked(const QPointF &point)'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#clicked

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QXYSeries::clicked(const QPointF &point)
    self.uglySide.call(
        'ritual_ZN9QXYSeries7clickedERK7QPointF',
        self._valueOf(point, 'QPointF'),
    )

  @overload(QPointF, bool)
  def hovered(self, point: QPointF, state: bool) -> None:
    """
    Calls Qt's 'void QXYSeries::hovered(const QPointF &point, bool state)'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#hovered

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    state : bool
      Passed on as it is.
    """
    #  void QXYSeries::hovered(const QPointF &point, bool state)
    self.uglySide.call(
        'ritual_ZN9QXYSeries7hoveredERK7QPointFb',
        self._valueOf(point, 'QPointF'), state,
    )

  @overload(QPointF)
  def pressed(self, point: QPointF) -> None:
    """
    Calls Qt's 'void QXYSeries::pressed(const QPointF &point)'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#pressed

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QXYSeries::pressed(const QPointF &point)
    self.uglySide.call(
        'ritual_ZN9QXYSeries7pressedERK7QPointF',
        self._valueOf(point, 'QPointF'),
    )

  @overload(QPointF)
  def released(self, point: QPointF) -> None:
    """
    Calls Qt's 'void QXYSeries::released(const QPointF &point)'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#released

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QXYSeries::released(const QPointF &point)
    self.uglySide.call(
        'ritual_ZN9QXYSeries8releasedERK7QPointF',
        self._valueOf(point, 'QPointF'),
    )

  @overload(QPointF)
  def doubleClicked(self, point: QPointF) -> None:
    """
    Calls Qt's 'void QXYSeries::doubleClicked(const QPointF &point)'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#doubleClicked

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QXYSeries::doubleClicked(const QPointF &point)
    self.uglySide.call(
        'ritual_ZN9QXYSeries13doubleClickedERK7QPointF',
        self._valueOf(point, 'QPointF'),
    )

  @overload(int)
  def pointReplaced(self, index: int) -> None:
    """
    Calls Qt's 'void QXYSeries::pointReplaced(int index)'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#pointReplaced

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QXYSeries::pointReplaced(int index)
    self.uglySide.call('ritual_ZN9QXYSeries13pointReplacedEi', index)

  @overload(int)
  def pointRemoved(self, index: int) -> None:
    """
    Calls Qt's 'void QXYSeries::pointRemoved(int index)'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#pointRemoved

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QXYSeries::pointRemoved(int index)
    self.uglySide.call('ritual_ZN9QXYSeries12pointRemovedEi', index)

  @overload(int)
  def pointAdded(self, index: int) -> None:
    """
    Calls Qt's 'void QXYSeries::pointAdded(int index)'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#pointAdded

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QXYSeries::pointAdded(int index)
    self.uglySide.call('ritual_ZN9QXYSeries10pointAddedEi', index)

  @overload(QColor)
  def colorChanged(self, color: QColor) -> None:
    """
    Calls Qt's 'void QXYSeries::colorChanged(QColor color)'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#colorChanged

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QXYSeries::colorChanged(QColor color)
    self.uglySide.call(
        'ritual_ZN9QXYSeries12colorChangedE6QColor', self._valueOf(color),
    )

  @overload(QColor)
  def selectedColorChanged(self, color: QColor) -> None:
    """
    Calls Qt's 'void QXYSeries::selectedColorChanged(const QColor &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxyseries.html#selectedColorChanged

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QXYSeries::selectedColorChanged(const QColor &color)
    self.uglySide.call(
        'ritual_ZN9QXYSeries20selectedColorChangedERK6QColor',
        self._valueOf(color),
    )

  def pointsReplaced(self) -> None:
    """
    Calls Qt's 'void QXYSeries::pointsReplaced()'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#pointsReplaced
    """
    #  void QXYSeries::pointsReplaced()
    self.uglySide.call('ritual_ZN9QXYSeries14pointsReplacedEv')

  @overload(str)
  def pointLabelsFormatChanged(self, format: str) -> None:
    """
    Calls Qt's 'void QXYSeries::pointLabelsFormatChanged(const QString
    &format)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxyseries.html#pointLabelsFormatChanged

    Parameters
    ----------

    format : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QXYSeries::pointLabelsFormatChanged(const QString &format)
    self.uglySide.call(
        'ritual_ZN9QXYSeries24pointLabelsFormatChangedERK7QString', format,
    )

  @overload(bool)
  def pointLabelsVisibilityChanged(self, visible: bool) -> None:
    """
    Calls Qt's 'void QXYSeries::pointLabelsVisibilityChanged(bool visible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxyseries.html#pointLabelsVisibilityChanged

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void QXYSeries::pointLabelsVisibilityChanged(bool visible)
    self.uglySide.call(
        'ritual_ZN9QXYSeries28pointLabelsVisibilityChangedEb', visible,
    )

  @overload(QFont)
  def pointLabelsFontChanged(self, font: QFont) -> None:
    """
    Calls Qt's 'void QXYSeries::pointLabelsFontChanged(const QFont &font)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxyseries.html#pointLabelsFontChanged

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QXYSeries::pointLabelsFontChanged(const QFont &font)
    self.uglySide.call(
        'ritual_ZN9QXYSeries22pointLabelsFontChangedERK5QFont',
        self._valueOf(font),
    )

  @overload(QColor)
  def pointLabelsColorChanged(self, color: QColor) -> None:
    """
    Calls Qt's 'void QXYSeries::pointLabelsColorChanged(const QColor
    &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxyseries.html#pointLabelsColorChanged

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QXYSeries::pointLabelsColorChanged(const QColor &color)
    self.uglySide.call(
        'ritual_ZN9QXYSeries23pointLabelsColorChangedERK6QColor',
        self._valueOf(color),
    )

  @overload(bool)
  def pointLabelsClippingChanged(self, clipping: bool) -> None:
    """
    Calls Qt's 'void QXYSeries::pointLabelsClippingChanged(bool clipping)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxyseries.html#pointLabelsClippingChanged

    Parameters
    ----------

    clipping : bool
      Passed on as it is.
    """
    #  void QXYSeries::pointLabelsClippingChanged(bool clipping)
    self.uglySide.call(
        'ritual_ZN9QXYSeries26pointLabelsClippingChangedEb', clipping,
    )

  @overload(int, int)
  def pointsRemoved(self, index: int, count: int) -> None:
    """
    Calls Qt's 'void QXYSeries::pointsRemoved(int index, int count)'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#pointsRemoved

    Parameters
    ----------

    index : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void QXYSeries::pointsRemoved(int index, int count)
    self.uglySide.call('ritual_ZN9QXYSeries13pointsRemovedEii', index, count)

  @overload(QPen)
  def penChanged(self, pen: QPen) -> None:
    """
    Calls Qt's 'void QXYSeries::penChanged(const QPen &pen)'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#penChanged

    Parameters
    ----------

    pen : QPen
      Passed on as a value: Qt reads the C++ QPen, which stays Python's own.
    """
    #  void QXYSeries::penChanged(const QPen &pen)
    self.uglySide.call(
        'ritual_ZN9QXYSeries10penChangedERK4QPen', self._valueOf(pen),
    )

  def selectedPointsChanged(self) -> None:
    """
    Calls Qt's 'void QXYSeries::selectedPointsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxyseries.html#selectedPointsChanged
    """
    #  void QXYSeries::selectedPointsChanged()
    self.uglySide.call('ritual_ZN9QXYSeries21selectedPointsChangedEv')

  @overload(QImage)
  def lightMarkerChanged(self, lightMarker: QImage) -> None:
    """
    Calls Qt's 'void QXYSeries::lightMarkerChanged(const QImage
    &lightMarker)'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#lightMarkerChanged

    Parameters
    ----------

    lightMarker : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.
    """
    #  void QXYSeries::lightMarkerChanged(const QImage &lightMarker)
    self.uglySide.call(
        'ritual_ZN9QXYSeries18lightMarkerChangedERK6QImage',
        self._valueOf(lightMarker),
    )

  @overload(QImage)
  def selectedLightMarkerChanged(self, selectedLightMarker: QImage) -> None:
    """
    Calls Qt's 'void QXYSeries::selectedLightMarkerChanged(const QImage
    &selectedLightMarker)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxyseries.html#selectedLightMarkerChanged

    Parameters
    ----------

    selectedLightMarker : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.
    """
    #  void QXYSeries::selectedLightMarkerChanged(const QImage
    #      &selectedLightMarker)
    self.uglySide.call(
        'ritual_ZN9QXYSeries26selectedLightMarkerChangedERK6QImage',
        self._valueOf(selectedLightMarker),
    )

  @overload(bool)
  def bestFitLineVisibilityChanged(self, visible: bool) -> None:
    """
    Calls Qt's 'void QXYSeries::bestFitLineVisibilityChanged(bool visible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxyseries.html#bestFitLineVisibilityChanged

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void QXYSeries::bestFitLineVisibilityChanged(bool visible)
    self.uglySide.call(
        'ritual_ZN9QXYSeries28bestFitLineVisibilityChangedEb', visible,
    )

  @overload(QPen)
  def bestFitLinePenChanged(self, pen: QPen) -> None:
    """
    Calls Qt's 'void QXYSeries::bestFitLinePenChanged(const QPen &pen)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxyseries.html#bestFitLinePenChanged

    Parameters
    ----------

    pen : QPen
      Passed on as a value: Qt reads the C++ QPen, which stays Python's own.
    """
    #  void QXYSeries::bestFitLinePenChanged(const QPen &pen)
    self.uglySide.call(
        'ritual_ZN9QXYSeries21bestFitLinePenChangedERK4QPen',
        self._valueOf(pen),
    )

  @overload(QColor)
  def bestFitLineColorChanged(self, color: QColor) -> None:
    """
    Calls Qt's 'void QXYSeries::bestFitLineColorChanged(const QColor
    &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxyseries.html#bestFitLineColorChanged

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QXYSeries::bestFitLineColorChanged(const QColor &color)
    self.uglySide.call(
        'ritual_ZN9QXYSeries23bestFitLineColorChangedERK6QColor',
        self._valueOf(color),
    )

  @overload(float)
  def markerSizeChanged(self, size: float) -> None:
    """
    Calls Qt's 'void QXYSeries::markerSizeChanged(qreal size)'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#markerSizeChanged

    Parameters
    ----------

    size : float
      Passed on as it is.
    """
    #  void QXYSeries::markerSizeChanged(qreal size)
    self.uglySide.call('ritual_ZN9QXYSeries17markerSizeChangedEd', size)

  def d_func(self) -> Optional[QXYSeriesPrivate]:
    """
    Calls Qt's 'QXYSeriesPrivate *QXYSeries::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#d_func

    Returns
    -------

    Optional[QXYSeriesPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QXYSeriesPrivate *QXYSeries::d_func()
    address = self.uglySide.call('ritual_ZN9QXYSeries6d_funcEv')
    from . import QXYSeriesPrivate
    return QXYSeriesPrivate._cuteAt(address)

  @staticmethod
  def bestFitLineEquation(*__, **_) -> Never:
    """
    Qt's 'QPair<qreal, qreal> QXYSeries::bestFitLineEquation(bool &ok)
    const': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QXYSeries.bestFitLineEquation' has no cute function yet. Qt's "
        "'QPair<qreal, qreal> QXYSeries::bestFitLineEquation(bool &ok) "
        "const': takes a number to change where it is.")

  @staticmethod
  def colorBy(*__, **_) -> Never:
    """
    Qt's 'void QXYSeries::colorBy(const QList<qreal> &sourceData, const
    QLinearGradient &gradient)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QXYSeries.colorBy' has no cute function yet. Qt's 'void "
        "QXYSeries::colorBy(const QList<qreal> &sourceData, const "
        "QLinearGradient &gradient)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def deselectPoints(*__, **_) -> Never:
    """
    Qt's 'void QXYSeries::deselectPoints(const QList<int> &indexes)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QXYSeries.deselectPoints' has no cute function yet. Qt's 'void "
        "QXYSeries::deselectPoints(const QList<int> &indexes)': takes a "
        "type Python has no way to hand over yet.")

  @staticmethod
  def pointConfiguration(*__, **_) -> Never:
    """
    Qt's 'QHash<PointConfiguration, QVariant>
    QXYSeries::pointConfiguration(const int index) const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QXYSeries.pointConfiguration' has no cute function yet. Qt's "
        "'QHash<PointConfiguration, QVariant> "
        "QXYSeries::pointConfiguration(const int index) const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def pointsConfiguration(*__, **_) -> Never:
    """
    Qt's 'PointsConfigurationHash QXYSeries::pointsConfiguration() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QXYSeries.pointsConfiguration' has no cute function yet. Qt's "
        "'PointsConfigurationHash QXYSeries::pointsConfiguration() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def pointsConfigurationChanged(*__, **_) -> Never:
    """
    Qt's 'void QXYSeries::pointsConfigurationChanged(const
    QXYSeries::PointsConfigurationHash &configuration)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QXYSeries.pointsConfigurationChanged' has no cute function yet. "
        "Qt's 'void QXYSeries::pointsConfigurationChanged(const "
        "QXYSeries::PointsConfigurationHash &configuration)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def selectPoints(*__, **_) -> Never:
    """
    Qt's 'void QXYSeries::selectPoints(const QList<int> &indexes)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QXYSeries.selectPoints' has no cute function yet. Qt's 'void "
        "QXYSeries::selectPoints(const QList<int> &indexes)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def selectedPoints(*__, **_) -> Never:
    """
    Qt's 'QList<int> QXYSeries::selectedPoints() const': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QXYSeries.selectedPoints' has no cute function yet. Qt's "
        "'QList<int> QXYSeries::selectedPoints() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def setPointConfiguration(*__, **_) -> Never:
    """
    - Qt's 'void QXYSeries::setPointConfiguration(const int index, const
      QHash<PointConfiguration, QVariant> &configuration)': takes a type
      Python has no way to hand over yet.
    - Qt's 'void QXYSeries::setPointConfiguration(const int index, const
      PointConfiguration key, const QVariant &value)': takes a type Python
      has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QXYSeries.setPointConfiguration' has no cute function yet. Qt's "
        "'void QXYSeries::setPointConfiguration(const int index, const "
        "QHash<PointConfiguration, QVariant> &configuration)': takes a type "
        "Python has no way to hand over yet. Qt's 'void "
        "QXYSeries::setPointConfiguration(const int index, const "
        "PointConfiguration key, const QVariant &value)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def setPointsConfiguration(*__, **_) -> Never:
    """
    Qt's 'void QXYSeries::setPointsConfiguration(const QHash<int,
    QHash<QXYSeries::PointConfiguration, QVariant>> &pointsConfiguration)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QXYSeries.setPointsConfiguration' has no cute function yet. Qt's "
        "'void QXYSeries::setPointsConfiguration(const QHash<int, "
        "QHash<QXYSeries::PointConfiguration, QVariant>> "
        "&pointsConfiguration)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def sizeBy(*__, **_) -> Never:
    """
    Qt's 'void QXYSeries::sizeBy(const QList<qreal> &sourceData, const qreal
    minSize, const qreal maxSize)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QXYSeries.sizeBy' has no cute function yet. Qt's 'void "
        "QXYSeries::sizeBy(const QList<qreal> &sourceData, const qreal "
        "minSize, const qreal maxSize)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def toggleSelection(*__, **_) -> Never:
    """
    Qt's 'void QXYSeries::toggleSelection(const QList<int> &indexes)': takes
    a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QXYSeries.toggleSelection' has no cute function yet. Qt's 'void "
        "QXYSeries::toggleSelection(const QList<int> &indexes)': takes a "
        "type Python has no way to hand over yet.")
