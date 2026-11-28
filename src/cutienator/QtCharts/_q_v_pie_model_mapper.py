"""
QVPieModelMapper binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/qvpiemodelmapper.h, Qt 6.12.0. Changes made here are lost.
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


class QVPieModelMapper(QPieModelMapper):
  """
  The cute side of Qt's QVPieModelMapper: a plain Python object standing in
  front of one C++ QVPieModelMapper.

  It is built on the cute 'QPieModelMapper', as Qt's QVPieModelMapper is
  built on Qt's QPieModelMapper, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QVPieModelMapper that has a ritual and that Python
  can call so far, 20 names in all: 'metaObject', 'tr', 'model', 'setModel',
  'series', 'setSeries', 'valuesColumn', 'setValuesColumn', 'labelsColumn',
  'setLabelsColumn', 'firstRow', 'setFirstRow', 'rowCount', 'setRowCount',
  'seriesReplaced', 'modelReplaced', 'valuesColumnChanged',
  'labelsColumnChanged', 'firstRowChanged', 'rowCountChanged'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QVPieModelMapper::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QVPieModelMapper::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 25 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QVPieModelMapper is created at the first use, not by
    'QVPieModelMapper(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QVPieModelMapper.
  - Qt tells when it has removed the C++ QVPieModelMapper. Every call on the
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
    Calls Qt's 'QString QVPieModelMapper::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qvpiemodelmapper.html#tr

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
    #  QString QVPieModelMapper::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN16QVPieModelMapper2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QVPieModelMapper'

  #  A C++ QVPieModelMapper Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QVPieModelMapper'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QVPieModelMapper::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvpiemodelmapper.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QVPieModelMapper::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QVPieModelMapper10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def model(self) -> Optional[QAbstractItemModel]:
    """
    Calls Qt's 'QAbstractItemModel *QVPieModelMapper::model() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvpiemodelmapper.html#model

    Returns
    -------

    Optional[QAbstractItemModel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractItemModel *QVPieModelMapper::model() const
    address = self.uglySide.call('ritual_ZNK16QVPieModelMapper5modelEv')
    from ..QtCore import QAbstractItemModel
    return QAbstractItemModel._cuteAt(address)

  def series(self) -> Optional[QPieSeries]:
    """
    Calls Qt's 'QPieSeries *QVPieModelMapper::series() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvpiemodelmapper.html#series

    Returns
    -------

    Optional[QPieSeries]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPieSeries *QVPieModelMapper::series() const
    address = self.uglySide.call('ritual_ZNK16QVPieModelMapper6seriesEv')
    from . import QPieSeries
    return QPieSeries._cuteAt(address)

  def valuesColumn(self) -> int:
    """
    Calls Qt's 'int QVPieModelMapper::valuesColumn() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvpiemodelmapper.html#valuesColumn
    """
    #  int QVPieModelMapper::valuesColumn() const
    return self.uglySide.call('ritual_ZNK16QVPieModelMapper12valuesColumnEv')

  def labelsColumn(self) -> int:
    """
    Calls Qt's 'int QVPieModelMapper::labelsColumn() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvpiemodelmapper.html#labelsColumn
    """
    #  int QVPieModelMapper::labelsColumn() const
    return self.uglySide.call('ritual_ZNK16QVPieModelMapper12labelsColumnEv')

  def firstRow(self) -> int:
    """
    Calls Qt's 'int QVPieModelMapper::firstRow() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvpiemodelmapper.html#firstRow
    """
    #  int QVPieModelMapper::firstRow() const
    return self.uglySide.call('ritual_ZNK16QVPieModelMapper8firstRowEv')

  def rowCount(self) -> int:
    """
    Calls Qt's 'int QVPieModelMapper::rowCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvpiemodelmapper.html#rowCount
    """
    #  int QVPieModelMapper::rowCount() const
    return self.uglySide.call('ritual_ZNK16QVPieModelMapper8rowCountEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAbstractItemModel)
  @overload(NoneType)
  def setModel(self, model: Optional[QAbstractItemModel]) -> None:
    """
    Calls Qt's 'void QVPieModelMapper::setModel(QAbstractItemModel *model)'.

    Qt's own words: https://doc.qt.io/qt-6/qvpiemodelmapper.html#setModel

    Parameters
    ----------

    model : Optional[QAbstractItemModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QVPieModelMapper::setModel(QAbstractItemModel *model)
    self.uglySide.call(
        'ritual_ZN16QVPieModelMapper8setModelEP18QAbstractItemModel',
        self._addressOf(model),
    )

  @overload(QPieSeries)
  @overload(NoneType)
  def setSeries(self, series: Optional[QPieSeries]) -> None:
    """
    Calls Qt's 'void QVPieModelMapper::setSeries(QPieSeries *series)'.

    Qt's own words: https://doc.qt.io/qt-6/qvpiemodelmapper.html#setSeries

    Parameters
    ----------

    series : Optional[QPieSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QVPieModelMapper::setSeries(QPieSeries *series)
    self.uglySide.call(
        'ritual_ZN16QVPieModelMapper9setSeriesEP10QPieSeries',
        self._addressOf(series),
    )

  @overload(int)
  def setValuesColumn(self, valuesColumn: int) -> None:
    """
    Calls Qt's 'void QVPieModelMapper::setValuesColumn(int valuesColumn)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvpiemodelmapper.html#setValuesColumn

    Parameters
    ----------

    valuesColumn : int
      Passed on as it is.
    """
    #  void QVPieModelMapper::setValuesColumn(int valuesColumn)
    self.uglySide.call(
        'ritual_ZN16QVPieModelMapper15setValuesColumnEi', valuesColumn,
    )

  @overload(int)
  def setLabelsColumn(self, labelsColumn: int) -> None:
    """
    Calls Qt's 'void QVPieModelMapper::setLabelsColumn(int labelsColumn)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvpiemodelmapper.html#setLabelsColumn

    Parameters
    ----------

    labelsColumn : int
      Passed on as it is.
    """
    #  void QVPieModelMapper::setLabelsColumn(int labelsColumn)
    self.uglySide.call(
        'ritual_ZN16QVPieModelMapper15setLabelsColumnEi', labelsColumn,
    )

  @overload(int)
  def setFirstRow(self, firstRow: int) -> None:
    """
    Calls Qt's 'void QVPieModelMapper::setFirstRow(int firstRow)'.

    Qt's own words: https://doc.qt.io/qt-6/qvpiemodelmapper.html#setFirstRow

    Parameters
    ----------

    firstRow : int
      Passed on as it is.
    """
    #  void QVPieModelMapper::setFirstRow(int firstRow)
    self.uglySide.call(
        'ritual_ZN16QVPieModelMapper11setFirstRowEi', firstRow,
    )

  @overload(int)
  def setRowCount(self, rowCount: int) -> None:
    """
    Calls Qt's 'void QVPieModelMapper::setRowCount(int rowCount)'.

    Qt's own words: https://doc.qt.io/qt-6/qvpiemodelmapper.html#setRowCount

    Parameters
    ----------

    rowCount : int
      Passed on as it is.
    """
    #  void QVPieModelMapper::setRowCount(int rowCount)
    self.uglySide.call(
        'ritual_ZN16QVPieModelMapper11setRowCountEi', rowCount,
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
    'QVPieModelMapper::QVPieModelMapper(QObject *parent)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qvpiemodelmapper.html#QVPieModelMapper

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QVPieModelMapper::QVPieModelMapper(QObject *parent)
    self._noteCreation(QVPieModelMapper, lambda: Rituals.call(
        'ritual_ZN16QVPieModelMapperC1EP7QObject',
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
    Calls Qt's 'void QVPieModelMapper::seriesReplaced()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvpiemodelmapper.html#seriesReplaced
    """
    #  void QVPieModelMapper::seriesReplaced()
    self.uglySide.call('ritual_ZN16QVPieModelMapper14seriesReplacedEv')

  def modelReplaced(self) -> None:
    """
    Calls Qt's 'void QVPieModelMapper::modelReplaced()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvpiemodelmapper.html#modelReplaced
    """
    #  void QVPieModelMapper::modelReplaced()
    self.uglySide.call('ritual_ZN16QVPieModelMapper13modelReplacedEv')

  def valuesColumnChanged(self) -> None:
    """
    Calls Qt's 'void QVPieModelMapper::valuesColumnChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvpiemodelmapper.html#valuesColumnChanged
    """
    #  void QVPieModelMapper::valuesColumnChanged()
    self.uglySide.call('ritual_ZN16QVPieModelMapper19valuesColumnChangedEv')

  def labelsColumnChanged(self) -> None:
    """
    Calls Qt's 'void QVPieModelMapper::labelsColumnChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvpiemodelmapper.html#labelsColumnChanged
    """
    #  void QVPieModelMapper::labelsColumnChanged()
    self.uglySide.call('ritual_ZN16QVPieModelMapper19labelsColumnChangedEv')

  def firstRowChanged(self) -> None:
    """
    Calls Qt's 'void QVPieModelMapper::firstRowChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvpiemodelmapper.html#firstRowChanged
    """
    #  void QVPieModelMapper::firstRowChanged()
    self.uglySide.call('ritual_ZN16QVPieModelMapper15firstRowChangedEv')

  def rowCountChanged(self) -> None:
    """
    Calls Qt's 'void QVPieModelMapper::rowCountChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvpiemodelmapper.html#rowCountChanged
    """
    #  void QVPieModelMapper::rowCountChanged()
    self.uglySide.call('ritual_ZN16QVPieModelMapper15rowCountChangedEv')
