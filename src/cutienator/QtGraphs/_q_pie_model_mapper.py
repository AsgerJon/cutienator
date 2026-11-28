"""
QPieModelMapper binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGraphs/qpiemodelmapper.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QAbstractItemModel, QMetaObject
  from . import QPieModelMapperPrivate, QPieSeries
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractItemModel = WAIT['QAbstractItemModel']
  QPieSeries = WAIT['QtGraphs:QPieSeries']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPieModelMapper(QObject):
  """
  The cute side of Qt's QPieModelMapper: a plain Python object standing in
  front of one C++ QPieModelMapper.

  It is built on the cute 'QObject', as Qt's QPieModelMapper is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QPieModelMapper that has a ritual and that Python
  can call so far, 26 names in all: 'metaObject', 'tr', 'd_func', 'series',
  'setSeries', 'first', 'setFirst', 'count', 'setCount', 'valuesSection',
  'setValuesSection', 'labelsSection', 'setLabelsSection', 'orientation',
  'setOrientation', 'model', 'setModel', 'seriesChanged', 'modelChanged',
  'valuesSectionChanged', 'labelsSectionChanged', 'firstChanged',
  'countChanged', 'orientationChanged', 'onSliceLabelChanged',
  'onSliceValueChanged'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QPieModelMapper::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QPieModelMapper::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'const QPieModelMapperPrivate *QPieModelMapper::d_func() const':
    takes in Python what 'QPieModelMapperPrivate *QPieModelMapper::d_func()'
    takes.
  - Qt's 'QPieModelMapper::~QPieModelMapper()': the destructor: Python never
    removes a C++ QPieModelMapper.
  - Qt's 'QPieModelMapper::QPieModelMapper(QPieModelMapperPrivate &dd,
    QObject *parent)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  6 of the 38 functions Qt declares: 4 forbidden; 2 not a gap.

  What to expect
  --------------

  - The C++ QPieModelMapper is created at the first use, not by
    'QPieModelMapper(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPieModelMapper.
  - Qt tells when it has removed the C++ QPieModelMapper. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString QPieModelMapper::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qpiemodelmapper.html#tr

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
    #  QString QPieModelMapper::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN15QPieModelMapper2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPieModelMapper'
  #  The part of Qt it is of, as another part has a class of its name too.
  __qt_part__ = 'QtGraphs'

  #  A C++ QPieModelMapper Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPieModelMapper'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QPieModelMapper::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpiemodelmapper.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QPieModelMapper::metaObject() const
    address = self.uglySide.call('ritual_ZNK15QPieModelMapper10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def series(self) -> Optional[QPieSeries]:
    """
    Calls Qt's 'QPieSeries *QPieModelMapper::series() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpiemodelmapper.html#series

    Returns
    -------

    Optional[QPieSeries]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPieSeries *QPieModelMapper::series() const
    address = self.uglySide.call('ritual_ZNK15QPieModelMapper6seriesEv')
    from . import QPieSeries
    return QPieSeries._cuteAt(address)

  def first(self) -> int:
    """
    Calls Qt's 'qsizetype QPieModelMapper::first() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpiemodelmapper.html#first
    """
    #  qsizetype QPieModelMapper::first() const
    return self.uglySide.call('ritual_ZNK15QPieModelMapper5firstEv')

  def count(self) -> int:
    """
    Calls Qt's 'qsizetype QPieModelMapper::count() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpiemodelmapper.html#count
    """
    #  qsizetype QPieModelMapper::count() const
    return self.uglySide.call('ritual_ZNK15QPieModelMapper5countEv')

  def valuesSection(self) -> int:
    """
    Calls Qt's 'qsizetype QPieModelMapper::valuesSection() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpiemodelmapper.html#valuesSection
    """
    #  qsizetype QPieModelMapper::valuesSection() const
    return self.uglySide.call('ritual_ZNK15QPieModelMapper13valuesSectionEv')

  def labelsSection(self) -> int:
    """
    Calls Qt's 'qsizetype QPieModelMapper::labelsSection() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpiemodelmapper.html#labelsSection
    """
    #  qsizetype QPieModelMapper::labelsSection() const
    return self.uglySide.call('ritual_ZNK15QPieModelMapper13labelsSectionEv')

  def orientation(self) -> Qt.Orientation:
    """
    Calls Qt's 'Qt::Orientation QPieModelMapper::orientation() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpiemodelmapper.html#orientation

    Returns
    -------

    Qt.Orientation
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.Orientation(number)'
      gives.
    """
    #  Qt::Orientation QPieModelMapper::orientation() const
    return Qt.Orientation(self.uglySide.call(
        'ritual_ZNK15QPieModelMapper11orientationEv',
    ))

  def model(self) -> Optional[QAbstractItemModel]:
    """
    Calls Qt's 'QAbstractItemModel *QPieModelMapper::model() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpiemodelmapper.html#model

    Returns
    -------

    Optional[QAbstractItemModel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractItemModel *QPieModelMapper::model() const
    address = self.uglySide.call('ritual_ZNK15QPieModelMapper5modelEv')
    from ..QtCore import QAbstractItemModel
    return QAbstractItemModel._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QPieSeries)
  @overload(NoneType)
  def setSeries(self, series: Optional[QPieSeries]) -> None:
    """
    Calls Qt's 'void QPieModelMapper::setSeries(QPieSeries *series)'.

    Qt's own words: https://doc.qt.io/qt-6/qpiemodelmapper.html#setSeries

    Parameters
    ----------

    series : Optional[QPieSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPieModelMapper::setSeries(QPieSeries *series)
    self.uglySide.call(
        'ritual_ZN15QPieModelMapper9setSeriesEP10QPieSeries',
        self._addressOf(series),
    )

  @overload(int)
  def setFirst(self, first: int) -> None:
    """
    Calls Qt's 'void QPieModelMapper::setFirst(qsizetype first)'.

    Qt's own words: https://doc.qt.io/qt-6/qpiemodelmapper.html#setFirst

    Parameters
    ----------

    first : int
      Passed on as it is.
    """
    #  void QPieModelMapper::setFirst(qsizetype first)
    self.uglySide.call('ritual_ZN15QPieModelMapper8setFirstEx', first)

  @overload(int)
  def setCount(self, count: int) -> None:
    """
    Calls Qt's 'void QPieModelMapper::setCount(qsizetype count)'.

    Qt's own words: https://doc.qt.io/qt-6/qpiemodelmapper.html#setCount

    Parameters
    ----------

    count : int
      Passed on as it is.
    """
    #  void QPieModelMapper::setCount(qsizetype count)
    self.uglySide.call('ritual_ZN15QPieModelMapper8setCountEx', count)

  @overload(int)
  def setValuesSection(self, valuesSection: int) -> None:
    """
    Calls Qt's 'void QPieModelMapper::setValuesSection(qsizetype
    valuesSection)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpiemodelmapper.html#setValuesSection

    Parameters
    ----------

    valuesSection : int
      Passed on as it is.
    """
    #  void QPieModelMapper::setValuesSection(qsizetype valuesSection)
    self.uglySide.call(
        'ritual_ZN15QPieModelMapper16setValuesSectionEx', valuesSection,
    )

  @overload(int)
  def setLabelsSection(self, labelsSection: int) -> None:
    """
    Calls Qt's 'void QPieModelMapper::setLabelsSection(qsizetype
    labelsSection)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpiemodelmapper.html#setLabelsSection

    Parameters
    ----------

    labelsSection : int
      Passed on as it is.
    """
    #  void QPieModelMapper::setLabelsSection(qsizetype labelsSection)
    self.uglySide.call(
        'ritual_ZN15QPieModelMapper16setLabelsSectionEx', labelsSection,
    )

  @overload(Qt.Orientation)
  def setOrientation(self, orientation: Qt.Orientation) -> None:
    """
    Calls Qt's 'void QPieModelMapper::setOrientation(Qt::Orientation
    orientation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpiemodelmapper.html#setOrientation

    Parameters
    ----------

    orientation : Qt.Orientation
      Passed on as its number.
    """
    #  void QPieModelMapper::setOrientation(Qt::Orientation orientation)
    self.uglySide.call(
        'ritual_ZN15QPieModelMapper14setOrientationEN2Qt11OrientationE',
        orientation.value,
    )

  @overload(QAbstractItemModel)
  @overload(NoneType)
  def setModel(self, model: Optional[QAbstractItemModel]) -> None:
    """
    Calls Qt's 'void QPieModelMapper::setModel(QAbstractItemModel *model)'.

    Qt's own words: https://doc.qt.io/qt-6/qpiemodelmapper.html#setModel

    Parameters
    ----------

    model : Optional[QAbstractItemModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPieModelMapper::setModel(QAbstractItemModel *model)
    self.uglySide.call(
        'ritual_ZN15QPieModelMapper8setModelEP18QAbstractItemModel',
        self._addressOf(model),
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
    Notes what was given, for Qt's 'QPieModelMapper::QPieModelMapper(QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qpiemodelmapper.html#QPieModelMapper

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QPieModelMapper::QPieModelMapper(QObject *parent)
    self._noteCreation(QPieModelMapper, lambda: Rituals.call(
        'ritual_ZN15QPieModelMapperC1EP7QObject',
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

  def d_func(self) -> Optional[QPieModelMapperPrivate]:
    """
    Calls Qt's 'QPieModelMapperPrivate *QPieModelMapper::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qpiemodelmapper.html#d_func

    Returns
    -------

    Optional[QPieModelMapperPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPieModelMapperPrivate *QPieModelMapper::d_func()
    address = self.uglySide.call('ritual_ZN15QPieModelMapper6d_funcEv')
    from . import QPieModelMapperPrivate
    return QPieModelMapperPrivate._cuteAt(address)

  def seriesChanged(self) -> None:
    """
    Calls Qt's 'void QPieModelMapper::seriesChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qpiemodelmapper.html#seriesChanged
    """
    #  void QPieModelMapper::seriesChanged()
    self.uglySide.call('ritual_ZN15QPieModelMapper13seriesChangedEv')

  def modelChanged(self) -> None:
    """
    Calls Qt's 'void QPieModelMapper::modelChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qpiemodelmapper.html#modelChanged
    """
    #  void QPieModelMapper::modelChanged()
    self.uglySide.call('ritual_ZN15QPieModelMapper12modelChangedEv')

  def valuesSectionChanged(self) -> None:
    """
    Calls Qt's 'void QPieModelMapper::valuesSectionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpiemodelmapper.html#valuesSectionChanged
    """
    #  void QPieModelMapper::valuesSectionChanged()
    self.uglySide.call('ritual_ZN15QPieModelMapper20valuesSectionChangedEv')

  def labelsSectionChanged(self) -> None:
    """
    Calls Qt's 'void QPieModelMapper::labelsSectionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpiemodelmapper.html#labelsSectionChanged
    """
    #  void QPieModelMapper::labelsSectionChanged()
    self.uglySide.call('ritual_ZN15QPieModelMapper20labelsSectionChangedEv')

  def firstChanged(self) -> None:
    """
    Calls Qt's 'void QPieModelMapper::firstChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qpiemodelmapper.html#firstChanged
    """
    #  void QPieModelMapper::firstChanged()
    self.uglySide.call('ritual_ZN15QPieModelMapper12firstChangedEv')

  def countChanged(self) -> None:
    """
    Calls Qt's 'void QPieModelMapper::countChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qpiemodelmapper.html#countChanged
    """
    #  void QPieModelMapper::countChanged()
    self.uglySide.call('ritual_ZN15QPieModelMapper12countChangedEv')

  def orientationChanged(self) -> None:
    """
    Calls Qt's 'void QPieModelMapper::orientationChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpiemodelmapper.html#orientationChanged
    """
    #  void QPieModelMapper::orientationChanged()
    self.uglySide.call('ritual_ZN15QPieModelMapper18orientationChangedEv')

  def onSliceLabelChanged(self) -> None:
    """
    Calls Qt's 'void QPieModelMapper::onSliceLabelChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpiemodelmapper.html#onSliceLabelChanged
    """
    #  void QPieModelMapper::onSliceLabelChanged()
    self.uglySide.call('ritual_ZN15QPieModelMapper19onSliceLabelChangedEv')

  def onSliceValueChanged(self) -> None:
    """
    Calls Qt's 'void QPieModelMapper::onSliceValueChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpiemodelmapper.html#onSliceValueChanged
    """
    #  void QPieModelMapper::onSliceValueChanged()
    self.uglySide.call('ritual_ZN15QPieModelMapper19onSliceValueChangedEv')
