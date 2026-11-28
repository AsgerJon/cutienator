"""
QXYSeries binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGraphs/qxyseries.h, Qt 6.12.0. Changes made here are lost.
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

  from ..QtCore import QMetaObject, QPoint, QPointF, QVariant
  from ..QtGui import QColor
  from ..QtQml import QQmlComponent
  from ..QtCharts import QXYSeriesPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QPoint = WAIT['QPoint']
  QPointF = WAIT['QPointF']
  QQmlComponent = WAIT['QQmlComponent']
  QVariant = WAIT['QVariant']

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
  so far, 57 names in all: 'metaObject', 'tr', 'append', 'replace', 'remove',
  'insert', 'clear', 'at', 'find', 'removeMultiple', 'take', 'points',
  'setColor', 'color', 'setSelectedColor', 'selectedColor', 'count',
  'values', 'setValues', 'isPointSelected', 'selectPoint', 'deselectPoint',
  'setPointSelected', 'selectAllPoints', 'deselectAllPoints',
  'pointDelegate', 'setPointDelegate', 'isDraggable', 'setDraggable',
  'valueMapping', 'setValueMapping', 'valueMin', 'setValueMin', 'stepSize',
  'setStepSize', 'pointReplaced', 'pointRemoved', 'pointAdded',
  'pointsAdded', 'colorChanged', 'selectedColorChanged', 'pointsReplaced',
  'pointsRemoved', 'selectedPointsChanged', 'pointDelegateChanged',
  'draggableChanged', 'seriesUpdated', 'countChanged', 'clicked',
  'doubleClicked', 'pressed', 'released', 'valuesChanged',
  'valueMappingChanged', 'valueMinChanged', 'stepSizeChanged', 'd_func'. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QXYSeries::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QXYSeries::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QXYSeries::QXYSeries(QXYSeriesPrivate &dd, QObject *parent)': takes
    a type Python has no way to hand over yet.
  - Qt's 'QXYSeries::~QXYSeries()': the destructor: Python never removes a
    C++ QXYSeries.
  - Qt's 'QXYSeries &QXYSeries::operator<<(QPointF point)': gives a type
    Python has no way to take yet.
  - Qt's 'QXYSeries &QXYSeries::operator<<(const QList<QPointF> &points)':
    gives a type Python has no way to take yet.
  - Qt's 'void QXYSeries::selectPoints(const QList<qsizetype> &indexes)':
    takes a type Python has no way to hand over yet.
  - Qt's 'void QXYSeries::deselectPoints(const QList<qsizetype> &indexes)':
    takes a type Python has no way to hand over yet.
  - Qt's 'void QXYSeries::toggleSelection(const QList<qsizetype> &indexes)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QList<qsizetype> QXYSeries::selectedPoints() const': gives a type
    Python has no way to take yet.
  - Qt's 'void QXYSeries::qt_qmlMarker_uncreatable()': one of Qt's own inner
    workings.
  - Qt's 'const QXYSeriesPrivate *QXYSeries::d_func() const': takes in Python
    what 'QXYSeriesPrivate *QXYSeries::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 81 functions Qt declares: 2 not a gap; 2 forbidden.

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
    'deselectPoints', 'selectPoints', 'selectedPoints', 'toggleSelection',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  #  The enums Qt writes inside QXYSeries, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class QmlIsUncreatable(CuteNum, scoped=True):
    """
    The enum 'QXYSeries::QmlIsUncreatable' of Qt, with the 1 names Qt gives
    in it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    yes = Kee[int](1)

  class ValueMapping(CuteNum, scoped=True):
    """
    The enum 'QXYSeries::ValueMapping' of Qt, with the 2 names Qt gives in
    it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    X = Kee[int](0)
    Y = Kee[int](1)

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
  __qt_part__ = 'QtGraphs'

  #  A C++ QXYSeries Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QXYSeries'

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

  @overload(int)
  def at(self, index: int) -> QPointF:
    """
    Calls Qt's 'QPointF QXYSeries::at(qsizetype index) const'.

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
    #  QPointF QXYSeries::at(qsizetype index) const
    address = self.uglySide.call('ritual_ZNK9QXYSeries2atEx', index)
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  @overload(QPointF)
  def find(self, point: QPointF) -> int:
    """
    Calls Qt's 'qsizetype QXYSeries::find(QPointF point) const'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#find

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  qsizetype QXYSeries::find(QPointF point) const
    return self.uglySide.call(
        'ritual_ZNK9QXYSeries4findE7QPointF',
        self._valueOf(point, 'QPointF'),
    )

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
    address = self.uglySide.call('ritual_ZNK9QXYSeries5colorEv')
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

  def count(self) -> int:
    """
    Calls Qt's 'qsizetype QXYSeries::count() const'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#count
    """
    #  qsizetype QXYSeries::count() const
    return self.uglySide.call('ritual_ZNK9QXYSeries5countEv')

  def values(self) -> QList[QVariant]:
    """
    Calls Qt's 'QVariantList QXYSeries::values() const'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#values

    Returns
    -------

    QList[QVariant]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QVariantList QXYSeries::values() const
    address = self.uglySide.call('ritual_ZNK9QXYSeries6valuesEv')
    from ..QtCore import QVariant
    return QList[QVariant]._cuteOwning(address)

  @overload(int)
  def isPointSelected(self, index: int) -> bool:
    """
    Calls Qt's 'bool QXYSeries::isPointSelected(qsizetype index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#isPointSelected

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  bool QXYSeries::isPointSelected(qsizetype index) const
    return self.uglySide.call(
        'ritual_ZNK9QXYSeries15isPointSelectedEx', index,
    )

  def pointDelegate(self) -> Optional[QQmlComponent]:
    """
    Calls Qt's 'QQmlComponent *QXYSeries::pointDelegate() const'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#pointDelegate

    Returns
    -------

    Optional[QQmlComponent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlComponent *QXYSeries::pointDelegate() const
    address = self.uglySide.call('ritual_ZNK9QXYSeries13pointDelegateEv')
    from ..QtQml import QQmlComponent
    return QQmlComponent._cuteAt(address)

  def isDraggable(self) -> bool:
    """
    Calls Qt's 'bool QXYSeries::isDraggable() const'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#isDraggable
    """
    #  bool QXYSeries::isDraggable() const
    return self.uglySide.call('ritual_ZNK9QXYSeries11isDraggableEv')

  def valueMapping(self) -> ValueMapping:
    """
    Calls Qt's 'ValueMapping QXYSeries::valueMapping() const'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#valueMapping

    Returns
    -------

    ValueMapping
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ValueMapping(number)'
      gives.
    """
    #  ValueMapping QXYSeries::valueMapping() const
    return QXYSeries.ValueMapping(self.uglySide.call(
        'ritual_ZNK9QXYSeries12valueMappingEv',
    ))

  def valueMin(self) -> float:
    """
    Calls Qt's 'qreal QXYSeries::valueMin() const'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#valueMin
    """
    #  qreal QXYSeries::valueMin() const
    return self.uglySide.call('ritual_ZNK9QXYSeries8valueMinEv')

  def stepSize(self) -> float:
    """
    Calls Qt's 'qreal QXYSeries::stepSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#stepSize
    """
    #  qreal QXYSeries::stepSize() const
    return self.uglySide.call('ritual_ZNK9QXYSeries8stepSizeEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QColor)
  def setColor(self, newColor: QColor) -> None:
    """
    Calls Qt's 'void QXYSeries::setColor(QColor newColor)'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#setColor

    Parameters
    ----------

    newColor : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QXYSeries::setColor(QColor newColor)
    self.uglySide.call(
        'ritual_ZN9QXYSeries8setColorE6QColor', self._valueOf(newColor),
    )

  @overload(QColor)
  def setSelectedColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QXYSeries::setSelectedColor(QColor color)'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#setSelectedColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QXYSeries::setSelectedColor(QColor color)
    self.uglySide.call(
        'ritual_ZN9QXYSeries16setSelectedColorE6QColor',
        self._valueOf(color),
    )

  @overload(QList[QVariant])
  def setValues(self, values: QList[QVariant]) -> None:
    """
    Calls Qt's 'void QXYSeries::setValues(QVariantList values)'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#setValues

    Parameters
    ----------

    values : QList[QVariant]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QXYSeries::setValues(QVariantList values)
    self.uglySide.call(
        'ritual_ZN9QXYSeries9setValuesE5QListI8QVariantE',
        self._valueOf(values),
    )

  @overload(int, bool)
  def setPointSelected(self, index: int, selected: bool) -> None:
    """
    Calls Qt's 'void QXYSeries::setPointSelected(qsizetype index, bool
    selected)'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#setPointSelected

    Parameters
    ----------

    index : int
      Passed on as it is.

    selected : bool
      Passed on as it is.
    """
    #  void QXYSeries::setPointSelected(qsizetype index, bool selected)
    self.uglySide.call(
        'ritual_ZN9QXYSeries16setPointSelectedExb', index, selected,
    )

  @overload(QQmlComponent)
  @overload(NoneType)
  def setPointDelegate(
      self,
      newPointDelegate: Optional[QQmlComponent],
  ) -> None:
    """
    Calls Qt's 'void QXYSeries::setPointDelegate(QQmlComponent
    *newPointDelegate)'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#setPointDelegate

    Parameters
    ----------

    newPointDelegate : Optional[QQmlComponent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QXYSeries::setPointDelegate(QQmlComponent *newPointDelegate)
    self.uglySide.call(
        'ritual_ZN9QXYSeries16setPointDelegateEP13QQmlComponent',
        self._addressOf(newPointDelegate),
    )

  @overload(bool)
  def setDraggable(self, newDraggable: bool) -> None:
    """
    Calls Qt's 'void QXYSeries::setDraggable(bool newDraggable)'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#setDraggable

    Parameters
    ----------

    newDraggable : bool
      Passed on as it is.
    """
    #  void QXYSeries::setDraggable(bool newDraggable)
    self.uglySide.call('ritual_ZN9QXYSeries12setDraggableEb', newDraggable)

  @overload(ValueMapping)
  def setValueMapping(self, newHint: ValueMapping) -> None:
    """
    Calls Qt's 'void QXYSeries::setValueMapping(ValueMapping newHint)'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#setValueMapping

    Parameters
    ----------

    newHint : ValueMapping
      Passed on as its number.
    """
    #  void QXYSeries::setValueMapping(ValueMapping newHint)
    self.uglySide.call(
        'ritual_ZN9QXYSeries15setValueMappingENS_12ValueMappingE',
        newHint.value,
    )

  @overload(float)
  def setValueMin(self, newMin: float) -> None:
    """
    Calls Qt's 'void QXYSeries::setValueMin(qreal newMin)'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#setValueMin

    Parameters
    ----------

    newMin : float
      Passed on as it is.
    """
    #  void QXYSeries::setValueMin(qreal newMin)
    self.uglySide.call('ritual_ZN9QXYSeries11setValueMinEd', newMin)

  @overload(float)
  def setStepSize(self, stepSize: float) -> None:
    """
    Calls Qt's 'void QXYSeries::setStepSize(qreal stepSize)'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#setStepSize

    Parameters
    ----------

    stepSize : float
      Passed on as it is.
    """
    #  void QXYSeries::setStepSize(qreal stepSize)
    self.uglySide.call('ritual_ZN9QXYSeries11setStepSizeEd', stepSize)

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
    Qt's 'QXYSeries::QXYSeries(QXYSeriesPrivate &dd, QObject *parent)': takes
    a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QXYSeries.__init__' has no cute function yet. Qt's "
        "'QXYSeries::QXYSeries(QXYSeriesPrivate &dd, QObject *parent)': "
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
    Calls Qt's 'void QXYSeries::append(QPointF point)'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#append

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QXYSeries::append(QPointF point)
    self.uglySide.call(
        'ritual_ZN9QXYSeries6appendE7QPointF',
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
    Calls Qt's 'void QXYSeries::replace(QPointF oldPoint, QPointF newPoint)'.

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
    #  void QXYSeries::replace(QPointF oldPoint, QPointF newPoint)
    self.uglySide.call(
        'ritual_ZN9QXYSeries7replaceE7QPointFS0_',
        self._valueOf(oldPoint, 'QPointF'), self._valueOf(newPoint,
        'QPointF'),
    )

  @overload(int, float, float)
  def replace(self, index: int, newX: float, newY: float) -> None:
    """
    Calls Qt's 'void QXYSeries::replace(qsizetype index, qreal newX, qreal
    newY)'.

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
    #  void QXYSeries::replace(qsizetype index, qreal newX, qreal newY)
    self.uglySide.call('ritual_ZN9QXYSeries7replaceExdd', index, newX, newY)

  @overload(int, QPointF)
  def replace(self, index: int, newPoint: QPointF) -> None:
    """
    Calls Qt's 'void QXYSeries::replace(qsizetype index, QPointF newPoint)'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#replace

    Parameters
    ----------

    index : int
      Passed on as it is.

    newPoint : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QXYSeries::replace(qsizetype index, QPointF newPoint)
    self.uglySide.call(
        'ritual_ZN9QXYSeries7replaceEx7QPointF',
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
    Calls Qt's 'void QXYSeries::remove(QPointF point)'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#remove

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QXYSeries::remove(QPointF point)
    self.uglySide.call(
        'ritual_ZN9QXYSeries6removeE7QPointF',
        self._valueOf(point, 'QPointF'),
    )

  @overload(int)
  def remove(self, index: int) -> None:
    """
    Calls Qt's 'void QXYSeries::remove(qsizetype index)'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#remove

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QXYSeries::remove(qsizetype index)
    self.uglySide.call('ritual_ZN9QXYSeries6removeEx', index)

  @overload(int, QPointF)
  def insert(self, index: int, point: QPointF) -> None:
    """
    Calls Qt's 'void QXYSeries::insert(qsizetype index, QPointF point)'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#insert

    Parameters
    ----------

    index : int
      Passed on as it is.

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QXYSeries::insert(qsizetype index, QPointF point)
    self.uglySide.call(
        'ritual_ZN9QXYSeries6insertEx7QPointF',
        index, self._valueOf(point, 'QPointF'),
    )

  def clear(self) -> None:
    """
    Calls Qt's 'void QXYSeries::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#clear
    """
    #  void QXYSeries::clear()
    self.uglySide.call('ritual_ZN9QXYSeries5clearEv')

  @overload(int, int)
  def removeMultiple(self, index: int, count: int) -> None:
    """
    Calls Qt's 'void QXYSeries::removeMultiple(qsizetype index, qsizetype
    count)'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#removeMultiple

    Parameters
    ----------

    index : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void QXYSeries::removeMultiple(qsizetype index, qsizetype count)
    self.uglySide.call(
        'ritual_ZN9QXYSeries14removeMultipleExx', index, count,
    )

  @overload(QPointF)
  def take(self, point: QPointF) -> bool:
    """
    Calls Qt's 'bool QXYSeries::take(QPointF point)'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#take

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  bool QXYSeries::take(QPointF point)
    return self.uglySide.call(
        'ritual_ZN9QXYSeries4takeE7QPointF', self._valueOf(point, 'QPointF'),
    )

  @overload(int)
  def selectPoint(self, index: int) -> None:
    """
    Calls Qt's 'void QXYSeries::selectPoint(qsizetype index)'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#selectPoint

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QXYSeries::selectPoint(qsizetype index)
    self.uglySide.call('ritual_ZN9QXYSeries11selectPointEx', index)

  @overload(int)
  def deselectPoint(self, index: int) -> None:
    """
    Calls Qt's 'void QXYSeries::deselectPoint(qsizetype index)'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#deselectPoint

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QXYSeries::deselectPoint(qsizetype index)
    self.uglySide.call('ritual_ZN9QXYSeries13deselectPointEx', index)

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
  def pointReplaced(self, index: int) -> None:
    """
    Calls Qt's 'void QXYSeries::pointReplaced(qsizetype index)'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#pointReplaced

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QXYSeries::pointReplaced(qsizetype index)
    self.uglySide.call('ritual_ZN9QXYSeries13pointReplacedEx', index)

  @overload(int)
  def pointRemoved(self, index: int) -> None:
    """
    Calls Qt's 'void QXYSeries::pointRemoved(qsizetype index)'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#pointRemoved

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QXYSeries::pointRemoved(qsizetype index)
    self.uglySide.call('ritual_ZN9QXYSeries12pointRemovedEx', index)

  @overload(int)
  def pointAdded(self, index: int) -> None:
    """
    Calls Qt's 'void QXYSeries::pointAdded(qsizetype index)'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#pointAdded

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QXYSeries::pointAdded(qsizetype index)
    self.uglySide.call('ritual_ZN9QXYSeries10pointAddedEx', index)

  @overload(int, int)
  def pointsAdded(self, start: int, end: int) -> None:
    """
    Calls Qt's 'void QXYSeries::pointsAdded(qsizetype start, qsizetype end)'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#pointsAdded

    Parameters
    ----------

    start : int
      Passed on as it is.

    end : int
      Passed on as it is.
    """
    #  void QXYSeries::pointsAdded(qsizetype start, qsizetype end)
    self.uglySide.call('ritual_ZN9QXYSeries11pointsAddedExx', start, end)

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
    Calls Qt's 'void QXYSeries::selectedColorChanged(QColor color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxyseries.html#selectedColorChanged

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QXYSeries::selectedColorChanged(QColor color)
    self.uglySide.call(
        'ritual_ZN9QXYSeries20selectedColorChangedE6QColor',
        self._valueOf(color),
    )

  def pointsReplaced(self) -> None:
    """
    Calls Qt's 'void QXYSeries::pointsReplaced()'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#pointsReplaced
    """
    #  void QXYSeries::pointsReplaced()
    self.uglySide.call('ritual_ZN9QXYSeries14pointsReplacedEv')

  @overload(int, int)
  def pointsRemoved(self, index: int, count: int) -> None:
    """
    Calls Qt's 'void QXYSeries::pointsRemoved(qsizetype index, qsizetype
    count)'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#pointsRemoved

    Parameters
    ----------

    index : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void QXYSeries::pointsRemoved(qsizetype index, qsizetype count)
    self.uglySide.call('ritual_ZN9QXYSeries13pointsRemovedExx', index, count)

  def selectedPointsChanged(self) -> None:
    """
    Calls Qt's 'void QXYSeries::selectedPointsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxyseries.html#selectedPointsChanged
    """
    #  void QXYSeries::selectedPointsChanged()
    self.uglySide.call('ritual_ZN9QXYSeries21selectedPointsChangedEv')

  def pointDelegateChanged(self) -> None:
    """
    Calls Qt's 'void QXYSeries::pointDelegateChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxyseries.html#pointDelegateChanged
    """
    #  void QXYSeries::pointDelegateChanged()
    self.uglySide.call('ritual_ZN9QXYSeries20pointDelegateChangedEv')

  def draggableChanged(self) -> None:
    """
    Calls Qt's 'void QXYSeries::draggableChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#draggableChanged
    """
    #  void QXYSeries::draggableChanged()
    self.uglySide.call('ritual_ZN9QXYSeries16draggableChangedEv')

  def seriesUpdated(self) -> None:
    """
    Calls Qt's 'void QXYSeries::seriesUpdated()'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#seriesUpdated
    """
    #  void QXYSeries::seriesUpdated()
    self.uglySide.call('ritual_ZN9QXYSeries13seriesUpdatedEv')

  def countChanged(self) -> None:
    """
    Calls Qt's 'void QXYSeries::countChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#countChanged
    """
    #  void QXYSeries::countChanged()
    self.uglySide.call('ritual_ZN9QXYSeries12countChangedEv')

  @overload(QPoint)
  def clicked(self, point: QPoint) -> None:
    """
    Calls Qt's 'void QXYSeries::clicked(QPoint point)'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#clicked

    Parameters
    ----------

    point : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QXYSeries::clicked(QPoint point)
    self.uglySide.call(
        'ritual_ZN9QXYSeries7clickedE6QPoint', self._valueOf(point),
    )

  @overload(QPoint)
  def doubleClicked(self, point: QPoint) -> None:
    """
    Calls Qt's 'void QXYSeries::doubleClicked(QPoint point)'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#doubleClicked

    Parameters
    ----------

    point : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QXYSeries::doubleClicked(QPoint point)
    self.uglySide.call(
        'ritual_ZN9QXYSeries13doubleClickedE6QPoint', self._valueOf(point),
    )

  @overload(QPoint)
  def pressed(self, point: QPoint) -> None:
    """
    Calls Qt's 'void QXYSeries::pressed(QPoint point)'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#pressed

    Parameters
    ----------

    point : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QXYSeries::pressed(QPoint point)
    self.uglySide.call(
        'ritual_ZN9QXYSeries7pressedE6QPoint', self._valueOf(point),
    )

  @overload(QPoint)
  def released(self, point: QPoint) -> None:
    """
    Calls Qt's 'void QXYSeries::released(QPoint point)'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#released

    Parameters
    ----------

    point : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QXYSeries::released(QPoint point)
    self.uglySide.call(
        'ritual_ZN9QXYSeries8releasedE6QPoint', self._valueOf(point),
    )

  @overload(QList[QVariant])
  def valuesChanged(self, values: QList[QVariant]) -> None:
    """
    Calls Qt's 'void QXYSeries::valuesChanged(const QVariantList &values)'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#valuesChanged

    Parameters
    ----------

    values : QList[QVariant]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QXYSeries::valuesChanged(const QVariantList &values)
    self.uglySide.call(
        'ritual_ZN9QXYSeries13valuesChangedERK5QListI8QVariantE',
        self._valueOf(values),
    )

  @overload(ValueMapping)
  def valueMappingChanged(self, newHint: ValueMapping) -> None:
    """
    Calls Qt's 'void QXYSeries::valueMappingChanged(QXYSeries::ValueMapping
    newHint)'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#valueMappingChanged

    Parameters
    ----------

    newHint : ValueMapping
      Passed on as its number.
    """
    #  void QXYSeries::valueMappingChanged(QXYSeries::ValueMapping newHint)
    self.uglySide.call(
        'ritual_ZN9QXYSeries19valueMappingChangedENS_12ValueMappingE',
        newHint.value,
    )

  @overload(float)
  def valueMinChanged(self, newMin: float) -> None:
    """
    Calls Qt's 'void QXYSeries::valueMinChanged(qreal newMin)'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#valueMinChanged

    Parameters
    ----------

    newMin : float
      Passed on as it is.
    """
    #  void QXYSeries::valueMinChanged(qreal newMin)
    self.uglySide.call('ritual_ZN9QXYSeries15valueMinChangedEd', newMin)

  @overload(float)
  def stepSizeChanged(self, newStepSize: float) -> None:
    """
    Calls Qt's 'void QXYSeries::stepSizeChanged(qreal newStepSize)'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseries.html#stepSizeChanged

    Parameters
    ----------

    newStepSize : float
      Passed on as it is.
    """
    #  void QXYSeries::stepSizeChanged(qreal newStepSize)
    self.uglySide.call('ritual_ZN9QXYSeries15stepSizeChangedEd', newStepSize)

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
    from ..QtCharts import QXYSeriesPrivate
    return QXYSeriesPrivate._cuteAt(address)

  @staticmethod
  def deselectPoints(*__, **_) -> Never:
    """
    Qt's 'void QXYSeries::deselectPoints(const QList<qsizetype> &indexes)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QXYSeries.deselectPoints' has no cute function yet. Qt's 'void "
        "QXYSeries::deselectPoints(const QList<qsizetype> &indexes)': takes "
        "a type Python has no way to hand over yet.")

  @staticmethod
  def selectPoints(*__, **_) -> Never:
    """
    Qt's 'void QXYSeries::selectPoints(const QList<qsizetype> &indexes)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QXYSeries.selectPoints' has no cute function yet. Qt's 'void "
        "QXYSeries::selectPoints(const QList<qsizetype> &indexes)': takes a "
        "type Python has no way to hand over yet.")

  @staticmethod
  def selectedPoints(*__, **_) -> Never:
    """
    Qt's 'QList<qsizetype> QXYSeries::selectedPoints() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QXYSeries.selectedPoints' has no cute function yet. Qt's "
        "'QList<qsizetype> QXYSeries::selectedPoints() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def toggleSelection(*__, **_) -> Never:
    """
    Qt's 'void QXYSeries::toggleSelection(const QList<qsizetype> &indexes)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QXYSeries.toggleSelection' has no cute function yet. Qt's 'void "
        "QXYSeries::toggleSelection(const QList<qsizetype> &indexes)': "
        "takes a type Python has no way to hand over yet.")
