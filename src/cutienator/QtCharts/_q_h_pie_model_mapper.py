"""
QHPieModelMapper binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/qhpiemodelmapper.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QPieModelMapper

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QAbstractItemModel, QMetaObject
  from . import QPieSeries
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractItemModel = WAIT['QAbstractItemModel']
  QPieSeries = WAIT['QtCharts:QPieSeries']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QHPieModelMapper(QPieModelMapper):
  """
  The cute side of Qt's QHPieModelMapper: a plain Python object standing in
  front of one C++ QHPieModelMapper.

  It is built on the cute 'QPieModelMapper', as Qt's QHPieModelMapper is
  built on Qt's QPieModelMapper, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QHPieModelMapper that has a ritual and that Python
  can call so far, 20 names in all: 'metaObject', 'tr', 'model', 'setModel',
  'series', 'setSeries', 'valuesRow', 'setValuesRow', 'labelsRow',
  'setLabelsRow', 'firstColumn', 'setFirstColumn', 'columnCount',
  'setColumnCount', 'seriesReplaced', 'modelReplaced', 'valuesRowChanged',
  'labelsRowChanged', 'firstColumnChanged', 'columnCountChanged'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QHPieModelMapper::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QHPieModelMapper::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 25 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QHPieModelMapper is created at the first use, not by
    'QHPieModelMapper(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QHPieModelMapper.
  - Qt tells when it has removed the C++ QHPieModelMapper. Every call on the
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
    Calls Qt's 'QString QHPieModelMapper::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qhpiemodelmapper.html#tr

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
    #  QString QHPieModelMapper::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN16QHPieModelMapper2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QHPieModelMapper'

  #  A C++ QHPieModelMapper Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QHPieModelMapper'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QHPieModelMapper::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhpiemodelmapper.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QHPieModelMapper::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QHPieModelMapper10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def model(self) -> Optional[QAbstractItemModel]:
    """
    Calls Qt's 'QAbstractItemModel *QHPieModelMapper::model() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhpiemodelmapper.html#model

    Returns
    -------

    Optional[QAbstractItemModel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractItemModel *QHPieModelMapper::model() const
    address = self.uglySide.call('ritual_ZNK16QHPieModelMapper5modelEv')
    from ..QtCore import QAbstractItemModel
    return QAbstractItemModel._cuteAt(address)

  def series(self) -> Optional[QPieSeries]:
    """
    Calls Qt's 'QPieSeries *QHPieModelMapper::series() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhpiemodelmapper.html#series

    Returns
    -------

    Optional[QPieSeries]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPieSeries *QHPieModelMapper::series() const
    address = self.uglySide.call('ritual_ZNK16QHPieModelMapper6seriesEv')
    from . import QPieSeries
    return QPieSeries._cuteAt(address)

  def valuesRow(self) -> int:
    """
    Calls Qt's 'int QHPieModelMapper::valuesRow() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhpiemodelmapper.html#valuesRow
    """
    #  int QHPieModelMapper::valuesRow() const
    return self.uglySide.call('ritual_ZNK16QHPieModelMapper9valuesRowEv')

  def labelsRow(self) -> int:
    """
    Calls Qt's 'int QHPieModelMapper::labelsRow() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhpiemodelmapper.html#labelsRow
    """
    #  int QHPieModelMapper::labelsRow() const
    return self.uglySide.call('ritual_ZNK16QHPieModelMapper9labelsRowEv')

  def firstColumn(self) -> int:
    """
    Calls Qt's 'int QHPieModelMapper::firstColumn() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhpiemodelmapper.html#firstColumn
    """
    #  int QHPieModelMapper::firstColumn() const
    return self.uglySide.call('ritual_ZNK16QHPieModelMapper11firstColumnEv')

  def columnCount(self) -> int:
    """
    Calls Qt's 'int QHPieModelMapper::columnCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhpiemodelmapper.html#columnCount
    """
    #  int QHPieModelMapper::columnCount() const
    return self.uglySide.call('ritual_ZNK16QHPieModelMapper11columnCountEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAbstractItemModel)
  @overload(NoneType)
  def setModel(self, model: Optional[QAbstractItemModel]) -> None:
    """
    Calls Qt's 'void QHPieModelMapper::setModel(QAbstractItemModel *model)'.

    Qt's own words: https://doc.qt.io/qt-6/qhpiemodelmapper.html#setModel

    Parameters
    ----------

    model : Optional[QAbstractItemModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QHPieModelMapper::setModel(QAbstractItemModel *model)
    self.uglySide.call(
        'ritual_ZN16QHPieModelMapper8setModelEP18QAbstractItemModel',
        self._addressOf(model),
    )

  @overload(QPieSeries)
  @overload(NoneType)
  def setSeries(self, series: Optional[QPieSeries]) -> None:
    """
    Calls Qt's 'void QHPieModelMapper::setSeries(QPieSeries *series)'.

    Qt's own words: https://doc.qt.io/qt-6/qhpiemodelmapper.html#setSeries

    Parameters
    ----------

    series : Optional[QPieSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QHPieModelMapper::setSeries(QPieSeries *series)
    self.uglySide.call(
        'ritual_ZN16QHPieModelMapper9setSeriesEP10QPieSeries',
        self._addressOf(series),
    )

  @overload(int)
  def setValuesRow(self, valuesRow: int) -> None:
    """
    Calls Qt's 'void QHPieModelMapper::setValuesRow(int valuesRow)'.

    Qt's own words: https://doc.qt.io/qt-6/qhpiemodelmapper.html#setValuesRow

    Parameters
    ----------

    valuesRow : int
      Passed on as it is.
    """
    #  void QHPieModelMapper::setValuesRow(int valuesRow)
    self.uglySide.call(
        'ritual_ZN16QHPieModelMapper12setValuesRowEi', valuesRow,
    )

  @overload(int)
  def setLabelsRow(self, labelsRow: int) -> None:
    """
    Calls Qt's 'void QHPieModelMapper::setLabelsRow(int labelsRow)'.

    Qt's own words: https://doc.qt.io/qt-6/qhpiemodelmapper.html#setLabelsRow

    Parameters
    ----------

    labelsRow : int
      Passed on as it is.
    """
    #  void QHPieModelMapper::setLabelsRow(int labelsRow)
    self.uglySide.call(
        'ritual_ZN16QHPieModelMapper12setLabelsRowEi', labelsRow,
    )

  @overload(int)
  def setFirstColumn(self, firstColumn: int) -> None:
    """
    Calls Qt's 'void QHPieModelMapper::setFirstColumn(int firstColumn)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhpiemodelmapper.html#setFirstColumn

    Parameters
    ----------

    firstColumn : int
      Passed on as it is.
    """
    #  void QHPieModelMapper::setFirstColumn(int firstColumn)
    self.uglySide.call(
        'ritual_ZN16QHPieModelMapper14setFirstColumnEi', firstColumn,
    )

  @overload(int)
  def setColumnCount(self, columnCount: int) -> None:
    """
    Calls Qt's 'void QHPieModelMapper::setColumnCount(int columnCount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhpiemodelmapper.html#setColumnCount

    Parameters
    ----------

    columnCount : int
      Passed on as it is.
    """
    #  void QHPieModelMapper::setColumnCount(int columnCount)
    self.uglySide.call(
        'ritual_ZN16QHPieModelMapper14setColumnCountEi', columnCount,
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
    Notes what was given, for Qt's
    'QHPieModelMapper::QHPieModelMapper(QObject *parent)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qhpiemodelmapper.html#QHPieModelMapper

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QHPieModelMapper::QHPieModelMapper(QObject *parent)
    self._noteCreation(QHPieModelMapper, lambda: Rituals.call(
        'ritual_ZN16QHPieModelMapperC1EP7QObject',
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

  def seriesReplaced(self) -> None:
    """
    Calls Qt's 'void QHPieModelMapper::seriesReplaced()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhpiemodelmapper.html#seriesReplaced
    """
    #  void QHPieModelMapper::seriesReplaced()
    self.uglySide.call('ritual_ZN16QHPieModelMapper14seriesReplacedEv')

  def modelReplaced(self) -> None:
    """
    Calls Qt's 'void QHPieModelMapper::modelReplaced()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhpiemodelmapper.html#modelReplaced
    """
    #  void QHPieModelMapper::modelReplaced()
    self.uglySide.call('ritual_ZN16QHPieModelMapper13modelReplacedEv')

  def valuesRowChanged(self) -> None:
    """
    Calls Qt's 'void QHPieModelMapper::valuesRowChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhpiemodelmapper.html#valuesRowChanged
    """
    #  void QHPieModelMapper::valuesRowChanged()
    self.uglySide.call('ritual_ZN16QHPieModelMapper16valuesRowChangedEv')

  def labelsRowChanged(self) -> None:
    """
    Calls Qt's 'void QHPieModelMapper::labelsRowChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhpiemodelmapper.html#labelsRowChanged
    """
    #  void QHPieModelMapper::labelsRowChanged()
    self.uglySide.call('ritual_ZN16QHPieModelMapper16labelsRowChangedEv')

  def firstColumnChanged(self) -> None:
    """
    Calls Qt's 'void QHPieModelMapper::firstColumnChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhpiemodelmapper.html#firstColumnChanged
    """
    #  void QHPieModelMapper::firstColumnChanged()
    self.uglySide.call('ritual_ZN16QHPieModelMapper18firstColumnChangedEv')

  def columnCountChanged(self) -> None:
    """
    Calls Qt's 'void QHPieModelMapper::columnCountChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhpiemodelmapper.html#columnCountChanged
    """
    #  void QHPieModelMapper::columnCountChanged()
    self.uglySide.call('ritual_ZN16QHPieModelMapper18columnCountChangedEv')
