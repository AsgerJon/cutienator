"""
QVBarModelMapper binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/qvbarmodelmapper.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QBarModelMapper

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QAbstractItemModel, QMetaObject
  from . import QAbstractBarSeries
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractBarSeries = WAIT['QAbstractBarSeries']
  QAbstractItemModel = WAIT['QAbstractItemModel']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QVBarModelMapper(QBarModelMapper):
  """
  The cute side of Qt's QVBarModelMapper: a plain Python object standing in
  front of one C++ QVBarModelMapper.

  It is built on the cute 'QBarModelMapper', as Qt's QVBarModelMapper is
  built on Qt's QBarModelMapper, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QVBarModelMapper that has a ritual and that Python
  can call so far, 20 names in all: 'metaObject', 'tr', 'model', 'setModel',
  'series', 'setSeries', 'firstBarSetColumn', 'setFirstBarSetColumn',
  'lastBarSetColumn', 'setLastBarSetColumn', 'firstRow', 'setFirstRow',
  'rowCount', 'setRowCount', 'seriesReplaced', 'modelReplaced',
  'firstBarSetColumnChanged', 'lastBarSetColumnChanged', 'firstRowChanged',
  'rowCountChanged'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QVBarModelMapper::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QVBarModelMapper::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 25 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QVBarModelMapper is created at the first use, not by
    'QVBarModelMapper(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QVBarModelMapper.
  - Qt tells when it has removed the C++ QVBarModelMapper. Every call on the
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
    Calls Qt's 'QString QVBarModelMapper::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qvbarmodelmapper.html#tr

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
    #  QString QVBarModelMapper::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN16QVBarModelMapper2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QVBarModelMapper'

  #  A C++ QVBarModelMapper Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QVBarModelMapper'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QVBarModelMapper::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvbarmodelmapper.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QVBarModelMapper::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QVBarModelMapper10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def model(self) -> Optional[QAbstractItemModel]:
    """
    Calls Qt's 'QAbstractItemModel *QVBarModelMapper::model() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvbarmodelmapper.html#model

    Returns
    -------

    Optional[QAbstractItemModel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractItemModel *QVBarModelMapper::model() const
    address = self.uglySide.call('ritual_ZNK16QVBarModelMapper5modelEv')
    from ..QtCore import QAbstractItemModel
    return QAbstractItemModel._cuteAt(address)

  def series(self) -> Optional[QAbstractBarSeries]:
    """
    Calls Qt's 'QAbstractBarSeries *QVBarModelMapper::series() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvbarmodelmapper.html#series

    Returns
    -------

    Optional[QAbstractBarSeries]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractBarSeries *QVBarModelMapper::series() const
    address = self.uglySide.call('ritual_ZNK16QVBarModelMapper6seriesEv')
    from . import QAbstractBarSeries
    return QAbstractBarSeries._cuteAt(address)

  def firstBarSetColumn(self) -> int:
    """
    Calls Qt's 'int QVBarModelMapper::firstBarSetColumn() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvbarmodelmapper.html#firstBarSetColumn
    """
    #  int QVBarModelMapper::firstBarSetColumn() const
    return self.uglySide.call(
        'ritual_ZNK16QVBarModelMapper17firstBarSetColumnEv',
    )

  def lastBarSetColumn(self) -> int:
    """
    Calls Qt's 'int QVBarModelMapper::lastBarSetColumn() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvbarmodelmapper.html#lastBarSetColumn
    """
    #  int QVBarModelMapper::lastBarSetColumn() const
    return self.uglySide.call(
        'ritual_ZNK16QVBarModelMapper16lastBarSetColumnEv',
    )

  def firstRow(self) -> int:
    """
    Calls Qt's 'int QVBarModelMapper::firstRow() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvbarmodelmapper.html#firstRow
    """
    #  int QVBarModelMapper::firstRow() const
    return self.uglySide.call('ritual_ZNK16QVBarModelMapper8firstRowEv')

  def rowCount(self) -> int:
    """
    Calls Qt's 'int QVBarModelMapper::rowCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvbarmodelmapper.html#rowCount
    """
    #  int QVBarModelMapper::rowCount() const
    return self.uglySide.call('ritual_ZNK16QVBarModelMapper8rowCountEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAbstractItemModel)
  @overload(NoneType)
  def setModel(self, model: Optional[QAbstractItemModel]) -> None:
    """
    Calls Qt's 'void QVBarModelMapper::setModel(QAbstractItemModel *model)'.

    Qt's own words: https://doc.qt.io/qt-6/qvbarmodelmapper.html#setModel

    Parameters
    ----------

    model : Optional[QAbstractItemModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QVBarModelMapper::setModel(QAbstractItemModel *model)
    self.uglySide.call(
        'ritual_ZN16QVBarModelMapper8setModelEP18QAbstractItemModel',
        self._addressOf(model),
    )

  @overload(QAbstractBarSeries)
  @overload(NoneType)
  def setSeries(self, series: Optional[QAbstractBarSeries]) -> None:
    """
    Calls Qt's 'void QVBarModelMapper::setSeries(QAbstractBarSeries
    *series)'.

    Qt's own words: https://doc.qt.io/qt-6/qvbarmodelmapper.html#setSeries

    Parameters
    ----------

    series : Optional[QAbstractBarSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QVBarModelMapper::setSeries(QAbstractBarSeries *series)
    self.uglySide.call(
        'ritual_ZN16QVBarModelMapper9setSeriesEP18QAbstractBarSeries',
        self._addressOf(series),
    )

  @overload(int)
  def setFirstBarSetColumn(self, firstBarSetColumn: int) -> None:
    """
    Calls Qt's 'void QVBarModelMapper::setFirstBarSetColumn(int
    firstBarSetColumn)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvbarmodelmapper.html#setFirstBarSetColumn

    Parameters
    ----------

    firstBarSetColumn : int
      Passed on as it is.
    """
    #  void QVBarModelMapper::setFirstBarSetColumn(int firstBarSetColumn)
    self.uglySide.call(
        'ritual_ZN16QVBarModelMapper20setFirstBarSetColumnEi',
        firstBarSetColumn,
    )

  @overload(int)
  def setLastBarSetColumn(self, lastBarSetColumn: int) -> None:
    """
    Calls Qt's 'void QVBarModelMapper::setLastBarSetColumn(int
    lastBarSetColumn)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvbarmodelmapper.html#setLastBarSetColumn

    Parameters
    ----------

    lastBarSetColumn : int
      Passed on as it is.
    """
    #  void QVBarModelMapper::setLastBarSetColumn(int lastBarSetColumn)
    self.uglySide.call(
        'ritual_ZN16QVBarModelMapper19setLastBarSetColumnEi',
        lastBarSetColumn,
    )

  @overload(int)
  def setFirstRow(self, firstRow: int) -> None:
    """
    Calls Qt's 'void QVBarModelMapper::setFirstRow(int firstRow)'.

    Qt's own words: https://doc.qt.io/qt-6/qvbarmodelmapper.html#setFirstRow

    Parameters
    ----------

    firstRow : int
      Passed on as it is.
    """
    #  void QVBarModelMapper::setFirstRow(int firstRow)
    self.uglySide.call(
        'ritual_ZN16QVBarModelMapper11setFirstRowEi', firstRow,
    )

  @overload(int)
  def setRowCount(self, rowCount: int) -> None:
    """
    Calls Qt's 'void QVBarModelMapper::setRowCount(int rowCount)'.

    Qt's own words: https://doc.qt.io/qt-6/qvbarmodelmapper.html#setRowCount

    Parameters
    ----------

    rowCount : int
      Passed on as it is.
    """
    #  void QVBarModelMapper::setRowCount(int rowCount)
    self.uglySide.call(
        'ritual_ZN16QVBarModelMapper11setRowCountEi', rowCount,
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
    'QVBarModelMapper::QVBarModelMapper(QObject *parent)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qvbarmodelmapper.html#QVBarModelMapper

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QVBarModelMapper::QVBarModelMapper(QObject *parent)
    self._noteCreation(QVBarModelMapper, lambda: Rituals.call(
        'ritual_ZN16QVBarModelMapperC1EP7QObject',
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
    Calls Qt's 'void QVBarModelMapper::seriesReplaced()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvbarmodelmapper.html#seriesReplaced
    """
    #  void QVBarModelMapper::seriesReplaced()
    self.uglySide.call('ritual_ZN16QVBarModelMapper14seriesReplacedEv')

  def modelReplaced(self) -> None:
    """
    Calls Qt's 'void QVBarModelMapper::modelReplaced()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvbarmodelmapper.html#modelReplaced
    """
    #  void QVBarModelMapper::modelReplaced()
    self.uglySide.call('ritual_ZN16QVBarModelMapper13modelReplacedEv')

  def firstBarSetColumnChanged(self) -> None:
    """
    Calls Qt's 'void QVBarModelMapper::firstBarSetColumnChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvbarmodelmapper.html#firstBarSetColumnChanged
    """
    #  void QVBarModelMapper::firstBarSetColumnChanged()
    self.uglySide.call(
        'ritual_ZN16QVBarModelMapper24firstBarSetColumnChangedEv',
    )

  def lastBarSetColumnChanged(self) -> None:
    """
    Calls Qt's 'void QVBarModelMapper::lastBarSetColumnChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvbarmodelmapper.html#lastBarSetColumnChanged
    """
    #  void QVBarModelMapper::lastBarSetColumnChanged()
    self.uglySide.call(
        'ritual_ZN16QVBarModelMapper23lastBarSetColumnChangedEv',
    )

  def firstRowChanged(self) -> None:
    """
    Calls Qt's 'void QVBarModelMapper::firstRowChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvbarmodelmapper.html#firstRowChanged
    """
    #  void QVBarModelMapper::firstRowChanged()
    self.uglySide.call('ritual_ZN16QVBarModelMapper15firstRowChangedEv')

  def rowCountChanged(self) -> None:
    """
    Calls Qt's 'void QVBarModelMapper::rowCountChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvbarmodelmapper.html#rowCountChanged
    """
    #  void QVBarModelMapper::rowCountChanged()
    self.uglySide.call('ritual_ZN16QVBarModelMapper15rowCountChangedEv')
