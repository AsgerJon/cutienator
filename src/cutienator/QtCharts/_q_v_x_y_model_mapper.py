"""
QVXYModelMapper binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/qvxymodelmapper.h, Qt 6.12.0. Changes made here are lost.
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


class QVXYModelMapper(QXYModelMapper):
  """
  The cute side of Qt's QVXYModelMapper: a plain Python object standing in
  front of one C++ QVXYModelMapper.

  It is built on the cute 'QXYModelMapper', as Qt's QVXYModelMapper is built
  on Qt's QXYModelMapper, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QVXYModelMapper that has a ritual and that Python
  can call so far, 20 names in all: 'metaObject', 'tr', 'model', 'setModel',
  'series', 'setSeries', 'xColumn', 'setXColumn', 'yColumn', 'setYColumn',
  'firstRow', 'setFirstRow', 'rowCount', 'setRowCount', 'seriesReplaced',
  'modelReplaced', 'xColumnChanged', 'yColumnChanged', 'firstRowChanged',
  'rowCountChanged'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QVXYModelMapper::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QVXYModelMapper::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 25 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QVXYModelMapper is created at the first use, not by
    'QVXYModelMapper(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QVXYModelMapper.
  - Qt tells when it has removed the C++ QVXYModelMapper. Every call on the
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
    Calls Qt's 'QString QVXYModelMapper::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qvxymodelmapper.html#tr

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
    #  QString QVXYModelMapper::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN15QVXYModelMapper2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QVXYModelMapper'

  #  A C++ QVXYModelMapper Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QVXYModelMapper'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QVXYModelMapper::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvxymodelmapper.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QVXYModelMapper::metaObject() const
    address = self.uglySide.call('ritual_ZNK15QVXYModelMapper10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def model(self) -> Optional[QAbstractItemModel]:
    """
    Calls Qt's 'QAbstractItemModel *QVXYModelMapper::model() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvxymodelmapper.html#model

    Returns
    -------

    Optional[QAbstractItemModel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractItemModel *QVXYModelMapper::model() const
    address = self.uglySide.call('ritual_ZNK15QVXYModelMapper5modelEv')
    from ..QtCore import QAbstractItemModel
    return QAbstractItemModel._cuteAt(address)

  def series(self) -> Optional[QXYSeries]:
    """
    Calls Qt's 'QXYSeries *QVXYModelMapper::series() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvxymodelmapper.html#series

    Returns
    -------

    Optional[QXYSeries]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QXYSeries *QVXYModelMapper::series() const
    address = self.uglySide.call('ritual_ZNK15QVXYModelMapper6seriesEv')
    from . import QXYSeries
    return QXYSeries._cuteAt(address)

  def xColumn(self) -> int:
    """
    Calls Qt's 'int QVXYModelMapper::xColumn() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvxymodelmapper.html#xColumn
    """
    #  int QVXYModelMapper::xColumn() const
    return self.uglySide.call('ritual_ZNK15QVXYModelMapper7xColumnEv')

  def yColumn(self) -> int:
    """
    Calls Qt's 'int QVXYModelMapper::yColumn() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvxymodelmapper.html#yColumn
    """
    #  int QVXYModelMapper::yColumn() const
    return self.uglySide.call('ritual_ZNK15QVXYModelMapper7yColumnEv')

  def firstRow(self) -> int:
    """
    Calls Qt's 'int QVXYModelMapper::firstRow() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvxymodelmapper.html#firstRow
    """
    #  int QVXYModelMapper::firstRow() const
    return self.uglySide.call('ritual_ZNK15QVXYModelMapper8firstRowEv')

  def rowCount(self) -> int:
    """
    Calls Qt's 'int QVXYModelMapper::rowCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvxymodelmapper.html#rowCount
    """
    #  int QVXYModelMapper::rowCount() const
    return self.uglySide.call('ritual_ZNK15QVXYModelMapper8rowCountEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAbstractItemModel)
  @overload(NoneType)
  def setModel(self, model: Optional[QAbstractItemModel]) -> None:
    """
    Calls Qt's 'void QVXYModelMapper::setModel(QAbstractItemModel *model)'.

    Qt's own words: https://doc.qt.io/qt-6/qvxymodelmapper.html#setModel

    Parameters
    ----------

    model : Optional[QAbstractItemModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QVXYModelMapper::setModel(QAbstractItemModel *model)
    self.uglySide.call(
        'ritual_ZN15QVXYModelMapper8setModelEP18QAbstractItemModel',
        self._addressOf(model),
    )

  @overload(QXYSeries)
  @overload(NoneType)
  def setSeries(self, series: Optional[QXYSeries]) -> None:
    """
    Calls Qt's 'void QVXYModelMapper::setSeries(QXYSeries *series)'.

    Qt's own words: https://doc.qt.io/qt-6/qvxymodelmapper.html#setSeries

    Parameters
    ----------

    series : Optional[QXYSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QVXYModelMapper::setSeries(QXYSeries *series)
    self.uglySide.call(
        'ritual_ZN15QVXYModelMapper9setSeriesEP9QXYSeries',
        self._addressOf(series),
    )

  @overload(int)
  def setXColumn(self, xColumn: int) -> None:
    """
    Calls Qt's 'void QVXYModelMapper::setXColumn(int xColumn)'.

    Qt's own words: https://doc.qt.io/qt-6/qvxymodelmapper.html#setXColumn

    Parameters
    ----------

    xColumn : int
      Passed on as it is.
    """
    #  void QVXYModelMapper::setXColumn(int xColumn)
    self.uglySide.call('ritual_ZN15QVXYModelMapper10setXColumnEi', xColumn)

  @overload(int)
  def setYColumn(self, yColumn: int) -> None:
    """
    Calls Qt's 'void QVXYModelMapper::setYColumn(int yColumn)'.

    Qt's own words: https://doc.qt.io/qt-6/qvxymodelmapper.html#setYColumn

    Parameters
    ----------

    yColumn : int
      Passed on as it is.
    """
    #  void QVXYModelMapper::setYColumn(int yColumn)
    self.uglySide.call('ritual_ZN15QVXYModelMapper10setYColumnEi', yColumn)

  @overload(int)
  def setFirstRow(self, firstRow: int) -> None:
    """
    Calls Qt's 'void QVXYModelMapper::setFirstRow(int firstRow)'.

    Qt's own words: https://doc.qt.io/qt-6/qvxymodelmapper.html#setFirstRow

    Parameters
    ----------

    firstRow : int
      Passed on as it is.
    """
    #  void QVXYModelMapper::setFirstRow(int firstRow)
    self.uglySide.call('ritual_ZN15QVXYModelMapper11setFirstRowEi', firstRow)

  @overload(int)
  def setRowCount(self, rowCount: int) -> None:
    """
    Calls Qt's 'void QVXYModelMapper::setRowCount(int rowCount)'.

    Qt's own words: https://doc.qt.io/qt-6/qvxymodelmapper.html#setRowCount

    Parameters
    ----------

    rowCount : int
      Passed on as it is.
    """
    #  void QVXYModelMapper::setRowCount(int rowCount)
    self.uglySide.call('ritual_ZN15QVXYModelMapper11setRowCountEi', rowCount)

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
    Notes what was given, for Qt's 'QVXYModelMapper::QVXYModelMapper(QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qvxymodelmapper.html#QVXYModelMapper

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QVXYModelMapper::QVXYModelMapper(QObject *parent)
    self._noteCreation(QVXYModelMapper, lambda: Rituals.call(
        'ritual_ZN15QVXYModelMapperC1EP7QObject',
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
    Calls Qt's 'void QVXYModelMapper::seriesReplaced()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvxymodelmapper.html#seriesReplaced
    """
    #  void QVXYModelMapper::seriesReplaced()
    self.uglySide.call('ritual_ZN15QVXYModelMapper14seriesReplacedEv')

  def modelReplaced(self) -> None:
    """
    Calls Qt's 'void QVXYModelMapper::modelReplaced()'.

    Qt's own words: https://doc.qt.io/qt-6/qvxymodelmapper.html#modelReplaced
    """
    #  void QVXYModelMapper::modelReplaced()
    self.uglySide.call('ritual_ZN15QVXYModelMapper13modelReplacedEv')

  def xColumnChanged(self) -> None:
    """
    Calls Qt's 'void QVXYModelMapper::xColumnChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvxymodelmapper.html#xColumnChanged
    """
    #  void QVXYModelMapper::xColumnChanged()
    self.uglySide.call('ritual_ZN15QVXYModelMapper14xColumnChangedEv')

  def yColumnChanged(self) -> None:
    """
    Calls Qt's 'void QVXYModelMapper::yColumnChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvxymodelmapper.html#yColumnChanged
    """
    #  void QVXYModelMapper::yColumnChanged()
    self.uglySide.call('ritual_ZN15QVXYModelMapper14yColumnChangedEv')

  def firstRowChanged(self) -> None:
    """
    Calls Qt's 'void QVXYModelMapper::firstRowChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvxymodelmapper.html#firstRowChanged
    """
    #  void QVXYModelMapper::firstRowChanged()
    self.uglySide.call('ritual_ZN15QVXYModelMapper15firstRowChangedEv')

  def rowCountChanged(self) -> None:
    """
    Calls Qt's 'void QVXYModelMapper::rowCountChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvxymodelmapper.html#rowCountChanged
    """
    #  void QVXYModelMapper::rowCountChanged()
    self.uglySide.call('ritual_ZN15QVXYModelMapper15rowCountChangedEv')
