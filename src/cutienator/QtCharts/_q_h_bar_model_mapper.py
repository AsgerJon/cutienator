"""
QHBarModelMapper binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/qhbarmodelmapper.h, Qt 6.12.0. Changes made here are lost.
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


class QHBarModelMapper(QBarModelMapper):
  """
  The cute side of Qt's QHBarModelMapper: a plain Python object standing in
  front of one C++ QHBarModelMapper.

  It is built on the cute 'QBarModelMapper', as Qt's QHBarModelMapper is
  built on Qt's QBarModelMapper, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QHBarModelMapper that has a ritual and that Python
  can call so far, 20 names in all: 'metaObject', 'tr', 'model', 'setModel',
  'series', 'setSeries', 'firstBarSetRow', 'setFirstBarSetRow',
  'lastBarSetRow', 'setLastBarSetRow', 'firstColumn', 'setFirstColumn',
  'columnCount', 'setColumnCount', 'seriesReplaced', 'modelReplaced',
  'firstBarSetRowChanged', 'lastBarSetRowChanged', 'firstColumnChanged',
  'columnCountChanged'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QHBarModelMapper::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QHBarModelMapper::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 25 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QHBarModelMapper is created at the first use, not by
    'QHBarModelMapper(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QHBarModelMapper.
  - Qt tells when it has removed the C++ QHBarModelMapper. Every call on the
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
    Calls Qt's 'QString QHBarModelMapper::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qhbarmodelmapper.html#tr

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
    #  QString QHBarModelMapper::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN16QHBarModelMapper2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QHBarModelMapper'

  #  A C++ QHBarModelMapper Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QHBarModelMapper'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QHBarModelMapper::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhbarmodelmapper.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QHBarModelMapper::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QHBarModelMapper10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def model(self) -> Optional[QAbstractItemModel]:
    """
    Calls Qt's 'QAbstractItemModel *QHBarModelMapper::model() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhbarmodelmapper.html#model

    Returns
    -------

    Optional[QAbstractItemModel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractItemModel *QHBarModelMapper::model() const
    address = self.uglySide.call('ritual_ZNK16QHBarModelMapper5modelEv')
    from ..QtCore import QAbstractItemModel
    return QAbstractItemModel._cuteAt(address)

  def series(self) -> Optional[QAbstractBarSeries]:
    """
    Calls Qt's 'QAbstractBarSeries *QHBarModelMapper::series() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhbarmodelmapper.html#series

    Returns
    -------

    Optional[QAbstractBarSeries]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractBarSeries *QHBarModelMapper::series() const
    address = self.uglySide.call('ritual_ZNK16QHBarModelMapper6seriesEv')
    from . import QAbstractBarSeries
    return QAbstractBarSeries._cuteAt(address)

  def firstBarSetRow(self) -> int:
    """
    Calls Qt's 'int QHBarModelMapper::firstBarSetRow() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhbarmodelmapper.html#firstBarSetRow
    """
    #  int QHBarModelMapper::firstBarSetRow() const
    return self.uglySide.call(
        'ritual_ZNK16QHBarModelMapper14firstBarSetRowEv',
    )

  def lastBarSetRow(self) -> int:
    """
    Calls Qt's 'int QHBarModelMapper::lastBarSetRow() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhbarmodelmapper.html#lastBarSetRow
    """
    #  int QHBarModelMapper::lastBarSetRow() const
    return self.uglySide.call(
        'ritual_ZNK16QHBarModelMapper13lastBarSetRowEv',
    )

  def firstColumn(self) -> int:
    """
    Calls Qt's 'int QHBarModelMapper::firstColumn() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhbarmodelmapper.html#firstColumn
    """
    #  int QHBarModelMapper::firstColumn() const
    return self.uglySide.call('ritual_ZNK16QHBarModelMapper11firstColumnEv')

  def columnCount(self) -> int:
    """
    Calls Qt's 'int QHBarModelMapper::columnCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhbarmodelmapper.html#columnCount
    """
    #  int QHBarModelMapper::columnCount() const
    return self.uglySide.call('ritual_ZNK16QHBarModelMapper11columnCountEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAbstractItemModel)
  @overload(NoneType)
  def setModel(self, model: Optional[QAbstractItemModel]) -> None:
    """
    Calls Qt's 'void QHBarModelMapper::setModel(QAbstractItemModel *model)'.

    Qt's own words: https://doc.qt.io/qt-6/qhbarmodelmapper.html#setModel

    Parameters
    ----------

    model : Optional[QAbstractItemModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QHBarModelMapper::setModel(QAbstractItemModel *model)
    self.uglySide.call(
        'ritual_ZN16QHBarModelMapper8setModelEP18QAbstractItemModel',
        self._addressOf(model),
    )

  @overload(QAbstractBarSeries)
  @overload(NoneType)
  def setSeries(self, series: Optional[QAbstractBarSeries]) -> None:
    """
    Calls Qt's 'void QHBarModelMapper::setSeries(QAbstractBarSeries
    *series)'.

    Qt's own words: https://doc.qt.io/qt-6/qhbarmodelmapper.html#setSeries

    Parameters
    ----------

    series : Optional[QAbstractBarSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QHBarModelMapper::setSeries(QAbstractBarSeries *series)
    self.uglySide.call(
        'ritual_ZN16QHBarModelMapper9setSeriesEP18QAbstractBarSeries',
        self._addressOf(series),
    )

  @overload(int)
  def setFirstBarSetRow(self, firstBarSetRow: int) -> None:
    """
    Calls Qt's 'void QHBarModelMapper::setFirstBarSetRow(int
    firstBarSetRow)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhbarmodelmapper.html#setFirstBarSetRow

    Parameters
    ----------

    firstBarSetRow : int
      Passed on as it is.
    """
    #  void QHBarModelMapper::setFirstBarSetRow(int firstBarSetRow)
    self.uglySide.call(
        'ritual_ZN16QHBarModelMapper17setFirstBarSetRowEi', firstBarSetRow,
    )

  @overload(int)
  def setLastBarSetRow(self, lastBarSetRow: int) -> None:
    """
    Calls Qt's 'void QHBarModelMapper::setLastBarSetRow(int lastBarSetRow)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhbarmodelmapper.html#setLastBarSetRow

    Parameters
    ----------

    lastBarSetRow : int
      Passed on as it is.
    """
    #  void QHBarModelMapper::setLastBarSetRow(int lastBarSetRow)
    self.uglySide.call(
        'ritual_ZN16QHBarModelMapper16setLastBarSetRowEi', lastBarSetRow,
    )

  @overload(int)
  def setFirstColumn(self, firstColumn: int) -> None:
    """
    Calls Qt's 'void QHBarModelMapper::setFirstColumn(int firstColumn)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhbarmodelmapper.html#setFirstColumn

    Parameters
    ----------

    firstColumn : int
      Passed on as it is.
    """
    #  void QHBarModelMapper::setFirstColumn(int firstColumn)
    self.uglySide.call(
        'ritual_ZN16QHBarModelMapper14setFirstColumnEi', firstColumn,
    )

  @overload(int)
  def setColumnCount(self, columnCount: int) -> None:
    """
    Calls Qt's 'void QHBarModelMapper::setColumnCount(int columnCount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhbarmodelmapper.html#setColumnCount

    Parameters
    ----------

    columnCount : int
      Passed on as it is.
    """
    #  void QHBarModelMapper::setColumnCount(int columnCount)
    self.uglySide.call(
        'ritual_ZN16QHBarModelMapper14setColumnCountEi', columnCount,
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
    'QHBarModelMapper::QHBarModelMapper(QObject *parent)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qhbarmodelmapper.html#QHBarModelMapper

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QHBarModelMapper::QHBarModelMapper(QObject *parent)
    self._noteCreation(QHBarModelMapper, lambda: Rituals.call(
        'ritual_ZN16QHBarModelMapperC1EP7QObject',
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
    Calls Qt's 'void QHBarModelMapper::seriesReplaced()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhbarmodelmapper.html#seriesReplaced
    """
    #  void QHBarModelMapper::seriesReplaced()
    self.uglySide.call('ritual_ZN16QHBarModelMapper14seriesReplacedEv')

  def modelReplaced(self) -> None:
    """
    Calls Qt's 'void QHBarModelMapper::modelReplaced()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhbarmodelmapper.html#modelReplaced
    """
    #  void QHBarModelMapper::modelReplaced()
    self.uglySide.call('ritual_ZN16QHBarModelMapper13modelReplacedEv')

  def firstBarSetRowChanged(self) -> None:
    """
    Calls Qt's 'void QHBarModelMapper::firstBarSetRowChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhbarmodelmapper.html#firstBarSetRowChanged
    """
    #  void QHBarModelMapper::firstBarSetRowChanged()
    self.uglySide.call(
        'ritual_ZN16QHBarModelMapper21firstBarSetRowChangedEv',
    )

  def lastBarSetRowChanged(self) -> None:
    """
    Calls Qt's 'void QHBarModelMapper::lastBarSetRowChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhbarmodelmapper.html#lastBarSetRowChanged
    """
    #  void QHBarModelMapper::lastBarSetRowChanged()
    self.uglySide.call('ritual_ZN16QHBarModelMapper20lastBarSetRowChangedEv')

  def firstColumnChanged(self) -> None:
    """
    Calls Qt's 'void QHBarModelMapper::firstColumnChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhbarmodelmapper.html#firstColumnChanged
    """
    #  void QHBarModelMapper::firstColumnChanged()
    self.uglySide.call('ritual_ZN16QHBarModelMapper18firstColumnChangedEv')

  def columnCountChanged(self) -> None:
    """
    Calls Qt's 'void QHBarModelMapper::columnCountChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhbarmodelmapper.html#columnCountChanged
    """
    #  void QHBarModelMapper::columnCountChanged()
    self.uglySide.call('ritual_ZN16QHBarModelMapper18columnCountChangedEv')
