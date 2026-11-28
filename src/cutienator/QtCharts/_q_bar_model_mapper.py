"""
QBarModelMapper binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/qbarmodelmapper.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QAbstractItemModel, QMetaObject
  from . import QAbstractBarSeries, QBarModelMapperPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractBarSeries = WAIT['QAbstractBarSeries']
  QAbstractItemModel = WAIT['QAbstractItemModel']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QBarModelMapper(QObject):
  """
  The cute side of Qt's QBarModelMapper: a plain Python object standing in
  front of one C++ QBarModelMapper.

  It is built on the cute 'QObject', as Qt's QBarModelMapper is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QBarModelMapper that has a ritual and that Python
  can call so far, 17 names in all: 'metaObject', 'tr', 'model', 'setModel',
  'series', 'setSeries', 'first', 'setFirst', 'count', 'setCount',
  'firstBarSetSection', 'setFirstBarSetSection', 'lastBarSetSection',
  'setLastBarSetSection', 'orientation', 'setOrientation', 'd_func'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QBarModelMapper::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QBarModelMapper::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'const QBarModelMapperPrivate *QBarModelMapper::d_func() const':
    takes in Python what 'QBarModelMapperPrivate *QBarModelMapper::d_func()'
    takes.

  What has no ritual
  ------------------

  2 of the 23 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QBarModelMapper is created at the first use, not by
    'QBarModelMapper(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QBarModelMapper.
  - Qt tells when it has removed the C++ QBarModelMapper. Every call on the
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
    Calls Qt's 'QString QBarModelMapper::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarmodelmapper.html#tr

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
    #  QString QBarModelMapper::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN15QBarModelMapper2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QBarModelMapper'
  #  The part of Qt it is of, as another part has a class of its name too.
  __qt_part__ = 'QtCharts'

  #  A C++ QBarModelMapper Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QBarModelMapper'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QBarModelMapper::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbarmodelmapper.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QBarModelMapper::metaObject() const
    address = self.uglySide.call('ritual_ZNK15QBarModelMapper10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def model(self) -> Optional[QAbstractItemModel]:
    """
    Calls Qt's 'QAbstractItemModel *QBarModelMapper::model() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbarmodelmapper.html#model

    Returns
    -------

    Optional[QAbstractItemModel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractItemModel *QBarModelMapper::model() const
    address = self.uglySide.call('ritual_ZNK15QBarModelMapper5modelEv')
    from ..QtCore import QAbstractItemModel
    return QAbstractItemModel._cuteAt(address)

  def series(self) -> Optional[QAbstractBarSeries]:
    """
    Calls Qt's 'QAbstractBarSeries *QBarModelMapper::series() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbarmodelmapper.html#series

    Returns
    -------

    Optional[QAbstractBarSeries]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractBarSeries *QBarModelMapper::series() const
    address = self.uglySide.call('ritual_ZNK15QBarModelMapper6seriesEv')
    from . import QAbstractBarSeries
    return QAbstractBarSeries._cuteAt(address)

  def first(self) -> int:
    """
    Calls Qt's 'int QBarModelMapper::first() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbarmodelmapper.html#first
    """
    #  int QBarModelMapper::first() const
    return self.uglySide.call('ritual_ZNK15QBarModelMapper5firstEv')

  def count(self) -> int:
    """
    Calls Qt's 'int QBarModelMapper::count() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbarmodelmapper.html#count
    """
    #  int QBarModelMapper::count() const
    return self.uglySide.call('ritual_ZNK15QBarModelMapper5countEv')

  def firstBarSetSection(self) -> int:
    """
    Calls Qt's 'int QBarModelMapper::firstBarSetSection() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbarmodelmapper.html#firstBarSetSection
    """
    #  int QBarModelMapper::firstBarSetSection() const
    return self.uglySide.call(
        'ritual_ZNK15QBarModelMapper18firstBarSetSectionEv',
    )

  def lastBarSetSection(self) -> int:
    """
    Calls Qt's 'int QBarModelMapper::lastBarSetSection() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbarmodelmapper.html#lastBarSetSection
    """
    #  int QBarModelMapper::lastBarSetSection() const
    return self.uglySide.call(
        'ritual_ZNK15QBarModelMapper17lastBarSetSectionEv',
    )

  def orientation(self) -> Qt.Orientation:
    """
    Calls Qt's 'Qt::Orientation QBarModelMapper::orientation() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbarmodelmapper.html#orientation

    Returns
    -------

    Qt.Orientation
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.Orientation(number)'
      gives.
    """
    #  Qt::Orientation QBarModelMapper::orientation() const
    return Qt.Orientation(self.uglySide.call(
        'ritual_ZNK15QBarModelMapper11orientationEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAbstractItemModel)
  @overload(NoneType)
  def setModel(self, model: Optional[QAbstractItemModel]) -> None:
    """
    Calls Qt's 'void QBarModelMapper::setModel(QAbstractItemModel *model)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarmodelmapper.html#setModel

    Parameters
    ----------

    model : Optional[QAbstractItemModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QBarModelMapper::setModel(QAbstractItemModel *model)
    self.uglySide.call(
        'ritual_ZN15QBarModelMapper8setModelEP18QAbstractItemModel',
        self._addressOf(model),
    )

  @overload(QAbstractBarSeries)
  @overload(NoneType)
  def setSeries(self, series: Optional[QAbstractBarSeries]) -> None:
    """
    Calls Qt's 'void QBarModelMapper::setSeries(QAbstractBarSeries *series)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarmodelmapper.html#setSeries

    Parameters
    ----------

    series : Optional[QAbstractBarSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QBarModelMapper::setSeries(QAbstractBarSeries *series)
    self.uglySide.call(
        'ritual_ZN15QBarModelMapper9setSeriesEP18QAbstractBarSeries',
        self._addressOf(series),
    )

  @overload(int)
  def setFirst(self, first: int) -> None:
    """
    Calls Qt's 'void QBarModelMapper::setFirst(int first)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarmodelmapper.html#setFirst

    Parameters
    ----------

    first : int
      Passed on as it is.
    """
    #  void QBarModelMapper::setFirst(int first)
    self.uglySide.call('ritual_ZN15QBarModelMapper8setFirstEi', first)

  @overload(int)
  def setCount(self, count: int) -> None:
    """
    Calls Qt's 'void QBarModelMapper::setCount(int count)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarmodelmapper.html#setCount

    Parameters
    ----------

    count : int
      Passed on as it is.
    """
    #  void QBarModelMapper::setCount(int count)
    self.uglySide.call('ritual_ZN15QBarModelMapper8setCountEi', count)

  @overload(int)
  def setFirstBarSetSection(self, firstBarSetSection: int) -> None:
    """
    Calls Qt's 'void QBarModelMapper::setFirstBarSetSection(int
    firstBarSetSection)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbarmodelmapper.html#setFirstBarSetSection

    Parameters
    ----------

    firstBarSetSection : int
      Passed on as it is.
    """
    #  void QBarModelMapper::setFirstBarSetSection(int firstBarSetSection)
    self.uglySide.call(
        'ritual_ZN15QBarModelMapper21setFirstBarSetSectionEi',
        firstBarSetSection,
    )

  @overload(int)
  def setLastBarSetSection(self, lastBarSetSection: int) -> None:
    """
    Calls Qt's 'void QBarModelMapper::setLastBarSetSection(int
    lastBarSetSection)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbarmodelmapper.html#setLastBarSetSection

    Parameters
    ----------

    lastBarSetSection : int
      Passed on as it is.
    """
    #  void QBarModelMapper::setLastBarSetSection(int lastBarSetSection)
    self.uglySide.call(
        'ritual_ZN15QBarModelMapper20setLastBarSetSectionEi',
        lastBarSetSection,
    )

  @overload(Qt.Orientation)
  def setOrientation(self, orientation: Qt.Orientation) -> None:
    """
    Calls Qt's 'void QBarModelMapper::setOrientation(Qt::Orientation
    orientation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbarmodelmapper.html#setOrientation

    Parameters
    ----------

    orientation : Qt.Orientation
      Passed on as its number.
    """
    #  void QBarModelMapper::setOrientation(Qt::Orientation orientation)
    self.uglySide.call(
        'ritual_ZN15QBarModelMapper14setOrientationEN2Qt11OrientationE',
        orientation.value,
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
    Notes what was given, for Qt's 'QBarModelMapper::QBarModelMapper(QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qbarmodelmapper.html#QBarModelMapper

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QBarModelMapper::QBarModelMapper(QObject *parent)
    self._noteCreation(QBarModelMapper, lambda: Rituals.call(
        'ritual_ZN15QBarModelMapperC1EP7QObject',
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

  def d_func(self) -> Optional[QBarModelMapperPrivate]:
    """
    Calls Qt's 'QBarModelMapperPrivate *QBarModelMapper::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qbarmodelmapper.html#d_func

    Returns
    -------

    Optional[QBarModelMapperPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QBarModelMapperPrivate *QBarModelMapper::d_func()
    address = self.uglySide.call('ritual_ZN15QBarModelMapper6d_funcEv')
    from . import QBarModelMapperPrivate
    return QBarModelMapperPrivate._cuteAt(address)
