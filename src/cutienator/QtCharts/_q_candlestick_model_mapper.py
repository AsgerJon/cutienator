"""
QCandlestickModelMapper binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/qcandlestickmodelmapper.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QAbstractItemModel, QMetaObject
  from . import QCandlestickModelMapperPrivate, QCandlestickSeries
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractItemModel = WAIT['QAbstractItemModel']
  QCandlestickSeries = WAIT['QCandlestickSeries']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QCandlestickModelMapper(QObject):
  """
  The cute side of Qt's QCandlestickModelMapper: a plain Python object
  standing in front of one C++ QCandlestickModelMapper.

  It is built on the cute 'QObject', as Qt's QCandlestickModelMapper is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QCandlestickModelMapper that has a ritual and that
  Python can call so far, 24 names in all: 'metaObject', 'tr', 'setModel',
  'model', 'setSeries', 'series', 'orientation', 'modelReplaced',
  'seriesReplaced', 'setTimestamp', 'timestamp', 'setOpen', 'open',
  'setHigh', 'high', 'setLow', 'low', 'setClose', 'close',
  'setFirstSetSection', 'firstSetSection', 'setLastSetSection',
  'lastSetSection', 'd_func'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QCandlestickModelMapper::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QCandlestickModelMapper::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'const QCandlestickModelMapperPrivate
    *QCandlestickModelMapper::d_func() const': takes in Python what
    'QCandlestickModelMapperPrivate *QCandlestickModelMapper::d_func()'
    takes.

  What has no ritual
  ------------------

  2 of the 30 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QCandlestickModelMapper is created at the first use, not by
    'QCandlestickModelMapper(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QCandlestickModelMapper.
  - Qt tells when it has removed the C++ QCandlestickModelMapper. Every call
    on the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QCandlestickModelMapper::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qcandlestickmodelmapper.html#tr

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
    #  QString QCandlestickModelMapper::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN23QCandlestickModelMapper2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCandlestickModelMapper'

  #  A C++ QCandlestickModelMapper Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QCandlestickModelMapper'

  #  The functions Qt calls itself that QCandlestickModelMapper is the first
  #  to declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'orientation': (
          ('_ZNK23QCandlestickModelMapper11orientationEv',
           ('int', 'enum', 'QtCore:Qt.Orientation'),
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
    Calls Qt's 'const QMetaObject *QCandlestickModelMapper::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlestickmodelmapper.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QCandlestickModelMapper::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK23QCandlestickModelMapper10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def model(self) -> Optional[QAbstractItemModel]:
    """
    Calls Qt's 'QAbstractItemModel *QCandlestickModelMapper::model() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcandlestickmodelmapper.html#model

    Returns
    -------

    Optional[QAbstractItemModel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractItemModel *QCandlestickModelMapper::model() const
    address = self.uglySide.call(
        'ritual_ZNK23QCandlestickModelMapper5modelEv',
    )
    from ..QtCore import QAbstractItemModel
    return QAbstractItemModel._cuteAt(address)

  def series(self) -> Optional[QCandlestickSeries]:
    """
    Calls Qt's 'QCandlestickSeries *QCandlestickModelMapper::series() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlestickmodelmapper.html#series

    Returns
    -------

    Optional[QCandlestickSeries]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCandlestickSeries *QCandlestickModelMapper::series() const
    address = self.uglySide.call(
        'ritual_ZNK23QCandlestickModelMapper6seriesEv',
    )
    from . import QCandlestickSeries
    return QCandlestickSeries._cuteAt(address)

  def orientation(self) -> Qt.Orientation:
    """
    Calls Qt's 'Qt::Orientation QCandlestickModelMapper::orientation()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlestickmodelmapper.html#orientation

    Returns
    -------

    Qt.Orientation
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.Orientation(number)'
      gives.
    """
    #  Qt::Orientation QCandlestickModelMapper::orientation() const
    return Qt.Orientation(self.uglySide.call(
        'ritual_ZNK23QCandlestickModelMapper11orientationEv',
    ))

  def timestamp(self) -> int:
    """
    Calls Qt's 'int QCandlestickModelMapper::timestamp() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlestickmodelmapper.html#timestamp
    """
    #  int QCandlestickModelMapper::timestamp() const
    return self.uglySide.call(
        'ritual_ZNK23QCandlestickModelMapper9timestampEv',
    )

  def open(self) -> int:
    """
    Calls Qt's 'int QCandlestickModelMapper::open() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcandlestickmodelmapper.html#open
    """
    #  int QCandlestickModelMapper::open() const
    return self.uglySide.call('ritual_ZNK23QCandlestickModelMapper4openEv')

  def high(self) -> int:
    """
    Calls Qt's 'int QCandlestickModelMapper::high() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcandlestickmodelmapper.html#high
    """
    #  int QCandlestickModelMapper::high() const
    return self.uglySide.call('ritual_ZNK23QCandlestickModelMapper4highEv')

  def low(self) -> int:
    """
    Calls Qt's 'int QCandlestickModelMapper::low() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcandlestickmodelmapper.html#low
    """
    #  int QCandlestickModelMapper::low() const
    return self.uglySide.call('ritual_ZNK23QCandlestickModelMapper3lowEv')

  def close(self) -> int:
    """
    Calls Qt's 'int QCandlestickModelMapper::close() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcandlestickmodelmapper.html#close
    """
    #  int QCandlestickModelMapper::close() const
    return self.uglySide.call('ritual_ZNK23QCandlestickModelMapper5closeEv')

  def firstSetSection(self) -> int:
    """
    Calls Qt's 'int QCandlestickModelMapper::firstSetSection() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlestickmodelmapper.html#firstSetSection
    """
    #  int QCandlestickModelMapper::firstSetSection() const
    return self.uglySide.call(
        'ritual_ZNK23QCandlestickModelMapper15firstSetSectionEv',
    )

  def lastSetSection(self) -> int:
    """
    Calls Qt's 'int QCandlestickModelMapper::lastSetSection() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlestickmodelmapper.html#lastSetSection
    """
    #  int QCandlestickModelMapper::lastSetSection() const
    return self.uglySide.call(
        'ritual_ZNK23QCandlestickModelMapper14lastSetSectionEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAbstractItemModel)
  @overload(NoneType)
  def setModel(self, model: Optional[QAbstractItemModel]) -> None:
    """
    Calls Qt's 'void QCandlestickModelMapper::setModel(QAbstractItemModel
    *model)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlestickmodelmapper.html#setModel

    Parameters
    ----------

    model : Optional[QAbstractItemModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QCandlestickModelMapper::setModel(QAbstractItemModel *model)
    self.uglySide.call(
        'ritual_ZN23QCandlestickModelMapper8setModelEP18QAbstractItemModel',
        self._addressOf(model),
    )

  @overload(QCandlestickSeries)
  @overload(NoneType)
  def setSeries(self, series: Optional[QCandlestickSeries]) -> None:
    """
    Calls Qt's 'void QCandlestickModelMapper::setSeries(QCandlestickSeries
    *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlestickmodelmapper.html#setSeries

    Parameters
    ----------

    series : Optional[QCandlestickSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QCandlestickModelMapper::setSeries(QCandlestickSeries *series)
    self.uglySide.call(
        'ritual_ZN23QCandlestickModelMapper9setSeriesEP18QCandlestickSeries',
        self._addressOf(series),
    )

  @overload(int)
  def setTimestamp(self, timestamp: int) -> None:
    """
    Calls Qt's 'void QCandlestickModelMapper::setTimestamp(int timestamp)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlestickmodelmapper.html#setTimestamp

    Parameters
    ----------

    timestamp : int
      Passed on as it is.
    """
    #  void QCandlestickModelMapper::setTimestamp(int timestamp)
    self.uglySide.call(
        'ritual_ZN23QCandlestickModelMapper12setTimestampEi', timestamp,
    )

  @overload(int)
  def setOpen(self, open: int) -> None:
    """
    Calls Qt's 'void QCandlestickModelMapper::setOpen(int open)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlestickmodelmapper.html#setOpen

    Parameters
    ----------

    open : int
      Passed on as it is.
    """
    #  void QCandlestickModelMapper::setOpen(int open)
    self.uglySide.call('ritual_ZN23QCandlestickModelMapper7setOpenEi', open)

  @overload(int)
  def setHigh(self, high: int) -> None:
    """
    Calls Qt's 'void QCandlestickModelMapper::setHigh(int high)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlestickmodelmapper.html#setHigh

    Parameters
    ----------

    high : int
      Passed on as it is.
    """
    #  void QCandlestickModelMapper::setHigh(int high)
    self.uglySide.call('ritual_ZN23QCandlestickModelMapper7setHighEi', high)

  @overload(int)
  def setLow(self, low: int) -> None:
    """
    Calls Qt's 'void QCandlestickModelMapper::setLow(int low)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlestickmodelmapper.html#setLow

    Parameters
    ----------

    low : int
      Passed on as it is.
    """
    #  void QCandlestickModelMapper::setLow(int low)
    self.uglySide.call('ritual_ZN23QCandlestickModelMapper6setLowEi', low)

  @overload(int)
  def setClose(self, close: int) -> None:
    """
    Calls Qt's 'void QCandlestickModelMapper::setClose(int close)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlestickmodelmapper.html#setClose

    Parameters
    ----------

    close : int
      Passed on as it is.
    """
    #  void QCandlestickModelMapper::setClose(int close)
    self.uglySide.call(
        'ritual_ZN23QCandlestickModelMapper8setCloseEi', close,
    )

  @overload(int)
  def setFirstSetSection(self, firstSetSection: int) -> None:
    """
    Calls Qt's 'void QCandlestickModelMapper::setFirstSetSection(int
    firstSetSection)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlestickmodelmapper.html#setFirstSetSection

    Parameters
    ----------

    firstSetSection : int
      Passed on as it is.
    """
    #  void QCandlestickModelMapper::setFirstSetSection(int firstSetSection)
    self.uglySide.call(
        'ritual_ZN23QCandlestickModelMapper18setFirstSetSectionEi',
        firstSetSection,
    )

  @overload(int)
  def setLastSetSection(self, lastSetSection: int) -> None:
    """
    Calls Qt's 'void QCandlestickModelMapper::setLastSetSection(int
    lastSetSection)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlestickmodelmapper.html#setLastSetSection

    Parameters
    ----------

    lastSetSection : int
      Passed on as it is.
    """
    #  void QCandlestickModelMapper::setLastSetSection(int lastSetSection)
    self.uglySide.call(
        'ritual_ZN23QCandlestickModelMapper17setLastSetSectionEi',
        lastSetSection,
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
    'QCandlestickModelMapper::QCandlestickModelMapper(QObject *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlestickmodelmapper.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QCandlestickModelMapper::QCandlestickModelMapper(QObject *parent)
    self._noteCreation(QCandlestickModelMapper, lambda: Rituals.call(
        'ritual_ZN23QCandlestickModelMapperC1EP7QObject',
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

  def modelReplaced(self) -> None:
    """
    Calls Qt's 'void QCandlestickModelMapper::modelReplaced()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlestickmodelmapper.html#modelReplaced
    """
    #  void QCandlestickModelMapper::modelReplaced()
    self.uglySide.call('ritual_ZN23QCandlestickModelMapper13modelReplacedEv')

  def seriesReplaced(self) -> None:
    """
    Calls Qt's 'void QCandlestickModelMapper::seriesReplaced()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlestickmodelmapper.html#seriesReplaced
    """
    #  void QCandlestickModelMapper::seriesReplaced()
    self.uglySide.call(
        'ritual_ZN23QCandlestickModelMapper14seriesReplacedEv',
    )

  def d_func(self) -> Optional[QCandlestickModelMapperPrivate]:
    """
    Calls Qt's 'QCandlestickModelMapperPrivate
    *QCandlestickModelMapper::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlestickmodelmapper.html#d_func

    Returns
    -------

    Optional[QCandlestickModelMapperPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCandlestickModelMapperPrivate *QCandlestickModelMapper::d_func()
    address = self.uglySide.call(
        'ritual_ZN23QCandlestickModelMapper6d_funcEv',
    )
    from . import QCandlestickModelMapperPrivate
    return QCandlestickModelMapperPrivate._cuteAt(address)
