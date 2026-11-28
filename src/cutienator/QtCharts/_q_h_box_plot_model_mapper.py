"""
QHBoxPlotModelMapper binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/qhboxplotmodelmapper.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QBoxPlotModelMapper

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QAbstractItemModel, QMetaObject
  from . import QBoxPlotSeries
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractItemModel = WAIT['QAbstractItemModel']
  QBoxPlotSeries = WAIT['QBoxPlotSeries']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QHBoxPlotModelMapper(QBoxPlotModelMapper):
  """
  The cute side of Qt's QHBoxPlotModelMapper: a plain Python object standing
  in front of one C++ QHBoxPlotModelMapper.

  It is built on the cute 'QBoxPlotModelMapper', as Qt's QHBoxPlotModelMapper
  is built on Qt's QBoxPlotModelMapper, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QHBoxPlotModelMapper that has a ritual and that
  Python can call so far, 20 names in all: 'metaObject', 'tr', 'model',
  'setModel', 'series', 'setSeries', 'firstBoxSetRow', 'setFirstBoxSetRow',
  'lastBoxSetRow', 'setLastBoxSetRow', 'firstColumn', 'setFirstColumn',
  'columnCount', 'setColumnCount', 'seriesReplaced', 'modelReplaced',
  'firstBoxSetRowChanged', 'lastBoxSetRowChanged', 'firstColumnChanged',
  'columnCountChanged'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QHBoxPlotModelMapper::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QHBoxPlotModelMapper::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 25 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QHBoxPlotModelMapper is created at the first use, not by
    'QHBoxPlotModelMapper(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QHBoxPlotModelMapper.
  - Qt tells when it has removed the C++ QHBoxPlotModelMapper. Every call on
    the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QHBoxPlotModelMapper::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qhboxplotmodelmapper.html#tr

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
    #  QString QHBoxPlotModelMapper::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN20QHBoxPlotModelMapper2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QHBoxPlotModelMapper'

  #  A C++ QHBoxPlotModelMapper Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QHBoxPlotModelMapper'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QHBoxPlotModelMapper::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhboxplotmodelmapper.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QHBoxPlotModelMapper::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20QHBoxPlotModelMapper10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def model(self) -> Optional[QAbstractItemModel]:
    """
    Calls Qt's 'QAbstractItemModel *QHBoxPlotModelMapper::model() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhboxplotmodelmapper.html#model

    Returns
    -------

    Optional[QAbstractItemModel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractItemModel *QHBoxPlotModelMapper::model() const
    address = self.uglySide.call('ritual_ZNK20QHBoxPlotModelMapper5modelEv')
    from ..QtCore import QAbstractItemModel
    return QAbstractItemModel._cuteAt(address)

  def series(self) -> Optional[QBoxPlotSeries]:
    """
    Calls Qt's 'QBoxPlotSeries *QHBoxPlotModelMapper::series() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhboxplotmodelmapper.html#series

    Returns
    -------

    Optional[QBoxPlotSeries]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QBoxPlotSeries *QHBoxPlotModelMapper::series() const
    address = self.uglySide.call('ritual_ZNK20QHBoxPlotModelMapper6seriesEv')
    from . import QBoxPlotSeries
    return QBoxPlotSeries._cuteAt(address)

  def firstBoxSetRow(self) -> int:
    """
    Calls Qt's 'int QHBoxPlotModelMapper::firstBoxSetRow() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhboxplotmodelmapper.html#firstBoxSetRow
    """
    #  int QHBoxPlotModelMapper::firstBoxSetRow() const
    return self.uglySide.call(
        'ritual_ZNK20QHBoxPlotModelMapper14firstBoxSetRowEv',
    )

  def lastBoxSetRow(self) -> int:
    """
    Calls Qt's 'int QHBoxPlotModelMapper::lastBoxSetRow() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhboxplotmodelmapper.html#lastBoxSetRow
    """
    #  int QHBoxPlotModelMapper::lastBoxSetRow() const
    return self.uglySide.call(
        'ritual_ZNK20QHBoxPlotModelMapper13lastBoxSetRowEv',
    )

  def firstColumn(self) -> int:
    """
    Calls Qt's 'int QHBoxPlotModelMapper::firstColumn() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhboxplotmodelmapper.html#firstColumn
    """
    #  int QHBoxPlotModelMapper::firstColumn() const
    return self.uglySide.call(
        'ritual_ZNK20QHBoxPlotModelMapper11firstColumnEv',
    )

  def columnCount(self) -> int:
    """
    Calls Qt's 'int QHBoxPlotModelMapper::columnCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhboxplotmodelmapper.html#columnCount
    """
    #  int QHBoxPlotModelMapper::columnCount() const
    return self.uglySide.call(
        'ritual_ZNK20QHBoxPlotModelMapper11columnCountEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAbstractItemModel)
  @overload(NoneType)
  def setModel(self, model: Optional[QAbstractItemModel]) -> None:
    """
    Calls Qt's 'void QHBoxPlotModelMapper::setModel(QAbstractItemModel
    *model)'.

    Qt's own words: https://doc.qt.io/qt-6/qhboxplotmodelmapper.html#setModel

    Parameters
    ----------

    model : Optional[QAbstractItemModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QHBoxPlotModelMapper::setModel(QAbstractItemModel *model)
    self.uglySide.call(
        'ritual_ZN20QHBoxPlotModelMapper8setModelEP18QAbstractItemModel',
        self._addressOf(model),
    )

  @overload(QBoxPlotSeries)
  @overload(NoneType)
  def setSeries(self, series: Optional[QBoxPlotSeries]) -> None:
    """
    Calls Qt's 'void QHBoxPlotModelMapper::setSeries(QBoxPlotSeries
    *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhboxplotmodelmapper.html#setSeries

    Parameters
    ----------

    series : Optional[QBoxPlotSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QHBoxPlotModelMapper::setSeries(QBoxPlotSeries *series)
    self.uglySide.call(
        'ritual_ZN20QHBoxPlotModelMapper9setSeriesEP14QBoxPlotSeries',
        self._addressOf(series),
    )

  @overload(int)
  def setFirstBoxSetRow(self, firstBoxSetRow: int) -> None:
    """
    Calls Qt's 'void QHBoxPlotModelMapper::setFirstBoxSetRow(int
    firstBoxSetRow)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhboxplotmodelmapper.html#setFirstBoxSetRow

    Parameters
    ----------

    firstBoxSetRow : int
      Passed on as it is.
    """
    #  void QHBoxPlotModelMapper::setFirstBoxSetRow(int firstBoxSetRow)
    self.uglySide.call(
        'ritual_ZN20QHBoxPlotModelMapper17setFirstBoxSetRowEi',
        firstBoxSetRow,
    )

  @overload(int)
  def setLastBoxSetRow(self, lastBoxSetRow: int) -> None:
    """
    Calls Qt's 'void QHBoxPlotModelMapper::setLastBoxSetRow(int
    lastBoxSetRow)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhboxplotmodelmapper.html#setLastBoxSetRow

    Parameters
    ----------

    lastBoxSetRow : int
      Passed on as it is.
    """
    #  void QHBoxPlotModelMapper::setLastBoxSetRow(int lastBoxSetRow)
    self.uglySide.call(
        'ritual_ZN20QHBoxPlotModelMapper16setLastBoxSetRowEi', lastBoxSetRow,
    )

  @overload(int)
  def setFirstColumn(self, firstColumn: int) -> None:
    """
    Calls Qt's 'void QHBoxPlotModelMapper::setFirstColumn(int firstColumn)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhboxplotmodelmapper.html#setFirstColumn

    Parameters
    ----------

    firstColumn : int
      Passed on as it is.
    """
    #  void QHBoxPlotModelMapper::setFirstColumn(int firstColumn)
    self.uglySide.call(
        'ritual_ZN20QHBoxPlotModelMapper14setFirstColumnEi', firstColumn,
    )

  @overload(int)
  def setColumnCount(self, rowCount: int) -> None:
    """
    Calls Qt's 'void QHBoxPlotModelMapper::setColumnCount(int rowCount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhboxplotmodelmapper.html#setColumnCount

    Parameters
    ----------

    rowCount : int
      Passed on as it is.
    """
    #  void QHBoxPlotModelMapper::setColumnCount(int rowCount)
    self.uglySide.call(
        'ritual_ZN20QHBoxPlotModelMapper14setColumnCountEi', rowCount,
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
    'QHBoxPlotModelMapper::QHBoxPlotModelMapper(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qhboxplotmodelmapper.html#QHBoxPlotModelMapper

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QHBoxPlotModelMapper::QHBoxPlotModelMapper(QObject *parent)
    self._noteCreation(QHBoxPlotModelMapper, lambda: Rituals.call(
        'ritual_ZN20QHBoxPlotModelMapperC1EP7QObject',
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
    Calls Qt's 'void QHBoxPlotModelMapper::seriesReplaced()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhboxplotmodelmapper.html#seriesReplaced
    """
    #  void QHBoxPlotModelMapper::seriesReplaced()
    self.uglySide.call('ritual_ZN20QHBoxPlotModelMapper14seriesReplacedEv')

  def modelReplaced(self) -> None:
    """
    Calls Qt's 'void QHBoxPlotModelMapper::modelReplaced()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhboxplotmodelmapper.html#modelReplaced
    """
    #  void QHBoxPlotModelMapper::modelReplaced()
    self.uglySide.call('ritual_ZN20QHBoxPlotModelMapper13modelReplacedEv')

  def firstBoxSetRowChanged(self) -> None:
    """
    Calls Qt's 'void QHBoxPlotModelMapper::firstBoxSetRowChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhboxplotmodelmapper.html#firstBoxSetRowChanged
    """
    #  void QHBoxPlotModelMapper::firstBoxSetRowChanged()
    self.uglySide.call(
        'ritual_ZN20QHBoxPlotModelMapper21firstBoxSetRowChangedEv',
    )

  def lastBoxSetRowChanged(self) -> None:
    """
    Calls Qt's 'void QHBoxPlotModelMapper::lastBoxSetRowChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhboxplotmodelmapper.html#lastBoxSetRowChanged
    """
    #  void QHBoxPlotModelMapper::lastBoxSetRowChanged()
    self.uglySide.call(
        'ritual_ZN20QHBoxPlotModelMapper20lastBoxSetRowChangedEv',
    )

  def firstColumnChanged(self) -> None:
    """
    Calls Qt's 'void QHBoxPlotModelMapper::firstColumnChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhboxplotmodelmapper.html#firstColumnChanged
    """
    #  void QHBoxPlotModelMapper::firstColumnChanged()
    self.uglySide.call(
        'ritual_ZN20QHBoxPlotModelMapper18firstColumnChangedEv',
    )

  def columnCountChanged(self) -> None:
    """
    Calls Qt's 'void QHBoxPlotModelMapper::columnCountChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhboxplotmodelmapper.html#columnCountChanged
    """
    #  void QHBoxPlotModelMapper::columnCountChanged()
    self.uglySide.call(
        'ritual_ZN20QHBoxPlotModelMapper18columnCountChangedEv',
    )
