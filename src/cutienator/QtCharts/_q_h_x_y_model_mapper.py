"""
QHXYModelMapper binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/qhxymodelmapper.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QXYModelMapper

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QAbstractItemModel, QMetaObject
  from . import QXYSeries
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractItemModel = WAIT['QAbstractItemModel']
  QXYSeries = WAIT['QtCharts:QXYSeries']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QHXYModelMapper(QXYModelMapper):
  """
  The cute side of Qt's QHXYModelMapper: a plain Python object standing in
  front of one C++ QHXYModelMapper.

  It is built on the cute 'QXYModelMapper', as Qt's QHXYModelMapper is built
  on Qt's QXYModelMapper, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QHXYModelMapper that has a ritual and that Python
  can call so far, 20 names in all: 'metaObject', 'tr', 'model', 'setModel',
  'series', 'setSeries', 'xRow', 'setXRow', 'yRow', 'setYRow', 'firstColumn',
  'setFirstColumn', 'columnCount', 'setColumnCount', 'seriesReplaced',
  'modelReplaced', 'xRowChanged', 'yRowChanged', 'firstColumnChanged',
  'columnCountChanged'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QHXYModelMapper::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QHXYModelMapper::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 25 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QHXYModelMapper is created at the first use, not by
    'QHXYModelMapper(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QHXYModelMapper.
  - Qt tells when it has removed the C++ QHXYModelMapper. Every call on the
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
    Calls Qt's 'QString QHXYModelMapper::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qhxymodelmapper.html#tr

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
    #  QString QHXYModelMapper::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN15QHXYModelMapper2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QHXYModelMapper'

  #  A C++ QHXYModelMapper Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QHXYModelMapper'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QHXYModelMapper::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhxymodelmapper.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QHXYModelMapper::metaObject() const
    address = self.uglySide.call('ritual_ZNK15QHXYModelMapper10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def model(self) -> Optional[QAbstractItemModel]:
    """
    Calls Qt's 'QAbstractItemModel *QHXYModelMapper::model() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhxymodelmapper.html#model

    Returns
    -------

    Optional[QAbstractItemModel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractItemModel *QHXYModelMapper::model() const
    address = self.uglySide.call('ritual_ZNK15QHXYModelMapper5modelEv')
    from ..QtCore import QAbstractItemModel
    return QAbstractItemModel._cuteAt(address)

  def series(self) -> Optional[QXYSeries]:
    """
    Calls Qt's 'QXYSeries *QHXYModelMapper::series() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhxymodelmapper.html#series

    Returns
    -------

    Optional[QXYSeries]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QXYSeries *QHXYModelMapper::series() const
    address = self.uglySide.call('ritual_ZNK15QHXYModelMapper6seriesEv')
    from . import QXYSeries
    return QXYSeries._cuteAt(address)

  def xRow(self) -> int:
    """
    Calls Qt's 'int QHXYModelMapper::xRow() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhxymodelmapper.html#xRow
    """
    #  int QHXYModelMapper::xRow() const
    return self.uglySide.call('ritual_ZNK15QHXYModelMapper4xRowEv')

  def yRow(self) -> int:
    """
    Calls Qt's 'int QHXYModelMapper::yRow() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhxymodelmapper.html#yRow
    """
    #  int QHXYModelMapper::yRow() const
    return self.uglySide.call('ritual_ZNK15QHXYModelMapper4yRowEv')

  def firstColumn(self) -> int:
    """
    Calls Qt's 'int QHXYModelMapper::firstColumn() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhxymodelmapper.html#firstColumn
    """
    #  int QHXYModelMapper::firstColumn() const
    return self.uglySide.call('ritual_ZNK15QHXYModelMapper11firstColumnEv')

  def columnCount(self) -> int:
    """
    Calls Qt's 'int QHXYModelMapper::columnCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhxymodelmapper.html#columnCount
    """
    #  int QHXYModelMapper::columnCount() const
    return self.uglySide.call('ritual_ZNK15QHXYModelMapper11columnCountEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAbstractItemModel)
  @overload(NoneType)
  def setModel(self, model: Optional[QAbstractItemModel]) -> None:
    """
    Calls Qt's 'void QHXYModelMapper::setModel(QAbstractItemModel *model)'.

    Qt's own words: https://doc.qt.io/qt-6/qhxymodelmapper.html#setModel

    Parameters
    ----------

    model : Optional[QAbstractItemModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QHXYModelMapper::setModel(QAbstractItemModel *model)
    self.uglySide.call(
        'ritual_ZN15QHXYModelMapper8setModelEP18QAbstractItemModel',
        self._addressOf(model),
    )

  @overload(QXYSeries)
  @overload(NoneType)
  def setSeries(self, series: Optional[QXYSeries]) -> None:
    """
    Calls Qt's 'void QHXYModelMapper::setSeries(QXYSeries *series)'.

    Qt's own words: https://doc.qt.io/qt-6/qhxymodelmapper.html#setSeries

    Parameters
    ----------

    series : Optional[QXYSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QHXYModelMapper::setSeries(QXYSeries *series)
    self.uglySide.call(
        'ritual_ZN15QHXYModelMapper9setSeriesEP9QXYSeries',
        self._addressOf(series),
    )

  @overload(int)
  def setXRow(self, xRow: int) -> None:
    """
    Calls Qt's 'void QHXYModelMapper::setXRow(int xRow)'.

    Qt's own words: https://doc.qt.io/qt-6/qhxymodelmapper.html#setXRow

    Parameters
    ----------

    xRow : int
      Passed on as it is.
    """
    #  void QHXYModelMapper::setXRow(int xRow)
    self.uglySide.call('ritual_ZN15QHXYModelMapper7setXRowEi', xRow)

  @overload(int)
  def setYRow(self, yRow: int) -> None:
    """
    Calls Qt's 'void QHXYModelMapper::setYRow(int yRow)'.

    Qt's own words: https://doc.qt.io/qt-6/qhxymodelmapper.html#setYRow

    Parameters
    ----------

    yRow : int
      Passed on as it is.
    """
    #  void QHXYModelMapper::setYRow(int yRow)
    self.uglySide.call('ritual_ZN15QHXYModelMapper7setYRowEi', yRow)

  @overload(int)
  def setFirstColumn(self, firstColumn: int) -> None:
    """
    Calls Qt's 'void QHXYModelMapper::setFirstColumn(int firstColumn)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhxymodelmapper.html#setFirstColumn

    Parameters
    ----------

    firstColumn : int
      Passed on as it is.
    """
    #  void QHXYModelMapper::setFirstColumn(int firstColumn)
    self.uglySide.call(
        'ritual_ZN15QHXYModelMapper14setFirstColumnEi', firstColumn,
    )

  @overload(int)
  def setColumnCount(self, columnCount: int) -> None:
    """
    Calls Qt's 'void QHXYModelMapper::setColumnCount(int columnCount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhxymodelmapper.html#setColumnCount

    Parameters
    ----------

    columnCount : int
      Passed on as it is.
    """
    #  void QHXYModelMapper::setColumnCount(int columnCount)
    self.uglySide.call(
        'ritual_ZN15QHXYModelMapper14setColumnCountEi', columnCount,
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
    Notes what was given, for Qt's 'QHXYModelMapper::QHXYModelMapper(QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qhxymodelmapper.html#QHXYModelMapper

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QHXYModelMapper::QHXYModelMapper(QObject *parent)
    self._noteCreation(QHXYModelMapper, lambda: Rituals.call(
        'ritual_ZN15QHXYModelMapperC1EP7QObject',
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
    Calls Qt's 'void QHXYModelMapper::seriesReplaced()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhxymodelmapper.html#seriesReplaced
    """
    #  void QHXYModelMapper::seriesReplaced()
    self.uglySide.call('ritual_ZN15QHXYModelMapper14seriesReplacedEv')

  def modelReplaced(self) -> None:
    """
    Calls Qt's 'void QHXYModelMapper::modelReplaced()'.

    Qt's own words: https://doc.qt.io/qt-6/qhxymodelmapper.html#modelReplaced
    """
    #  void QHXYModelMapper::modelReplaced()
    self.uglySide.call('ritual_ZN15QHXYModelMapper13modelReplacedEv')

  def xRowChanged(self) -> None:
    """
    Calls Qt's 'void QHXYModelMapper::xRowChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qhxymodelmapper.html#xRowChanged
    """
    #  void QHXYModelMapper::xRowChanged()
    self.uglySide.call('ritual_ZN15QHXYModelMapper11xRowChangedEv')

  def yRowChanged(self) -> None:
    """
    Calls Qt's 'void QHXYModelMapper::yRowChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qhxymodelmapper.html#yRowChanged
    """
    #  void QHXYModelMapper::yRowChanged()
    self.uglySide.call('ritual_ZN15QHXYModelMapper11yRowChangedEv')

  def firstColumnChanged(self) -> None:
    """
    Calls Qt's 'void QHXYModelMapper::firstColumnChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhxymodelmapper.html#firstColumnChanged
    """
    #  void QHXYModelMapper::firstColumnChanged()
    self.uglySide.call('ritual_ZN15QHXYModelMapper18firstColumnChangedEv')

  def columnCountChanged(self) -> None:
    """
    Calls Qt's 'void QHXYModelMapper::columnCountChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhxymodelmapper.html#columnCountChanged
    """
    #  void QHXYModelMapper::columnCountChanged()
    self.uglySide.call('ritual_ZN15QHXYModelMapper18columnCountChangedEv')
