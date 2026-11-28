"""
QXYModelMapper binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/qxymodelmapper.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QAbstractItemModel, QMetaObject
  from . import QXYModelMapperPrivate, QXYSeries
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractItemModel = WAIT['QAbstractItemModel']
  QXYSeries = WAIT['QtCharts:QXYSeries']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QXYModelMapper(QObject):
  """
  The cute side of Qt's QXYModelMapper: a plain Python object standing in
  front of one C++ QXYModelMapper.

  It is built on the cute 'QObject', as Qt's QXYModelMapper is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QXYModelMapper that has a ritual and that Python can
  call so far, 17 names in all: 'metaObject', 'tr', 'model', 'setModel',
  'series', 'setSeries', 'first', 'setFirst', 'count', 'setCount',
  'orientation', 'setOrientation', 'xSection', 'setXSection', 'ySection',
  'setYSection', 'd_func'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QXYModelMapper::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QXYModelMapper::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'const QXYModelMapperPrivate *QXYModelMapper::d_func() const': takes
    in Python what 'QXYModelMapperPrivate *QXYModelMapper::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 23 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QXYModelMapper is created at the first use, not by
    'QXYModelMapper(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QXYModelMapper.
  - Qt tells when it has removed the C++ QXYModelMapper. Every call on the
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
    Calls Qt's 'QString QXYModelMapper::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qxymodelmapper.html#tr

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
    #  QString QXYModelMapper::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN14QXYModelMapper2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QXYModelMapper'
  #  The part of Qt it is of, as another part has a class of its name too.
  __qt_part__ = 'QtCharts'

  #  A C++ QXYModelMapper Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QXYModelMapper'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QXYModelMapper::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qxymodelmapper.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QXYModelMapper::metaObject() const
    address = self.uglySide.call('ritual_ZNK14QXYModelMapper10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def model(self) -> Optional[QAbstractItemModel]:
    """
    Calls Qt's 'QAbstractItemModel *QXYModelMapper::model() const'.

    Qt's own words: https://doc.qt.io/qt-6/qxymodelmapper.html#model

    Returns
    -------

    Optional[QAbstractItemModel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractItemModel *QXYModelMapper::model() const
    address = self.uglySide.call('ritual_ZNK14QXYModelMapper5modelEv')
    from ..QtCore import QAbstractItemModel
    return QAbstractItemModel._cuteAt(address)

  def series(self) -> Optional[QXYSeries]:
    """
    Calls Qt's 'QXYSeries *QXYModelMapper::series() const'.

    Qt's own words: https://doc.qt.io/qt-6/qxymodelmapper.html#series

    Returns
    -------

    Optional[QXYSeries]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QXYSeries *QXYModelMapper::series() const
    address = self.uglySide.call('ritual_ZNK14QXYModelMapper6seriesEv')
    from . import QXYSeries
    return QXYSeries._cuteAt(address)

  def first(self) -> int:
    """
    Calls Qt's 'int QXYModelMapper::first() const'.

    Qt's own words: https://doc.qt.io/qt-6/qxymodelmapper.html#first
    """
    #  int QXYModelMapper::first() const
    return self.uglySide.call('ritual_ZNK14QXYModelMapper5firstEv')

  def count(self) -> int:
    """
    Calls Qt's 'int QXYModelMapper::count() const'.

    Qt's own words: https://doc.qt.io/qt-6/qxymodelmapper.html#count
    """
    #  int QXYModelMapper::count() const
    return self.uglySide.call('ritual_ZNK14QXYModelMapper5countEv')

  def orientation(self) -> Qt.Orientation:
    """
    Calls Qt's 'Qt::Orientation QXYModelMapper::orientation() const'.

    Qt's own words: https://doc.qt.io/qt-6/qxymodelmapper.html#orientation

    Returns
    -------

    Qt.Orientation
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.Orientation(number)'
      gives.
    """
    #  Qt::Orientation QXYModelMapper::orientation() const
    return Qt.Orientation(self.uglySide.call(
        'ritual_ZNK14QXYModelMapper11orientationEv',
    ))

  def xSection(self) -> int:
    """
    Calls Qt's 'int QXYModelMapper::xSection() const'.

    Qt's own words: https://doc.qt.io/qt-6/qxymodelmapper.html#xSection
    """
    #  int QXYModelMapper::xSection() const
    return self.uglySide.call('ritual_ZNK14QXYModelMapper8xSectionEv')

  def ySection(self) -> int:
    """
    Calls Qt's 'int QXYModelMapper::ySection() const'.

    Qt's own words: https://doc.qt.io/qt-6/qxymodelmapper.html#ySection
    """
    #  int QXYModelMapper::ySection() const
    return self.uglySide.call('ritual_ZNK14QXYModelMapper8ySectionEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAbstractItemModel)
  @overload(NoneType)
  def setModel(self, model: Optional[QAbstractItemModel]) -> None:
    """
    Calls Qt's 'void QXYModelMapper::setModel(QAbstractItemModel *model)'.

    Qt's own words: https://doc.qt.io/qt-6/qxymodelmapper.html#setModel

    Parameters
    ----------

    model : Optional[QAbstractItemModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QXYModelMapper::setModel(QAbstractItemModel *model)
    self.uglySide.call(
        'ritual_ZN14QXYModelMapper8setModelEP18QAbstractItemModel',
        self._addressOf(model),
    )

  @overload(QXYSeries)
  @overload(NoneType)
  def setSeries(self, series: Optional[QXYSeries]) -> None:
    """
    Calls Qt's 'void QXYModelMapper::setSeries(QXYSeries *series)'.

    Qt's own words: https://doc.qt.io/qt-6/qxymodelmapper.html#setSeries

    Parameters
    ----------

    series : Optional[QXYSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QXYModelMapper::setSeries(QXYSeries *series)
    self.uglySide.call(
        'ritual_ZN14QXYModelMapper9setSeriesEP9QXYSeries',
        self._addressOf(series),
    )

  @overload(int)
  def setFirst(self, first: int) -> None:
    """
    Calls Qt's 'void QXYModelMapper::setFirst(int first)'.

    Qt's own words: https://doc.qt.io/qt-6/qxymodelmapper.html#setFirst

    Parameters
    ----------

    first : int
      Passed on as it is.
    """
    #  void QXYModelMapper::setFirst(int first)
    self.uglySide.call('ritual_ZN14QXYModelMapper8setFirstEi', first)

  @overload(int)
  def setCount(self, count: int) -> None:
    """
    Calls Qt's 'void QXYModelMapper::setCount(int count)'.

    Qt's own words: https://doc.qt.io/qt-6/qxymodelmapper.html#setCount

    Parameters
    ----------

    count : int
      Passed on as it is.
    """
    #  void QXYModelMapper::setCount(int count)
    self.uglySide.call('ritual_ZN14QXYModelMapper8setCountEi', count)

  @overload(Qt.Orientation)
  def setOrientation(self, orientation: Qt.Orientation) -> None:
    """
    Calls Qt's 'void QXYModelMapper::setOrientation(Qt::Orientation
    orientation)'.

    Qt's own words: https://doc.qt.io/qt-6/qxymodelmapper.html#setOrientation

    Parameters
    ----------

    orientation : Qt.Orientation
      Passed on as its number.
    """
    #  void QXYModelMapper::setOrientation(Qt::Orientation orientation)
    self.uglySide.call(
        'ritual_ZN14QXYModelMapper14setOrientationEN2Qt11OrientationE',
        orientation.value,
    )

  @overload(int)
  def setXSection(self, xSection: int) -> None:
    """
    Calls Qt's 'void QXYModelMapper::setXSection(int xSection)'.

    Qt's own words: https://doc.qt.io/qt-6/qxymodelmapper.html#setXSection

    Parameters
    ----------

    xSection : int
      Passed on as it is.
    """
    #  void QXYModelMapper::setXSection(int xSection)
    self.uglySide.call('ritual_ZN14QXYModelMapper11setXSectionEi', xSection)

  @overload(int)
  def setYSection(self, ySection: int) -> None:
    """
    Calls Qt's 'void QXYModelMapper::setYSection(int ySection)'.

    Qt's own words: https://doc.qt.io/qt-6/qxymodelmapper.html#setYSection

    Parameters
    ----------

    ySection : int
      Passed on as it is.
    """
    #  void QXYModelMapper::setYSection(int ySection)
    self.uglySide.call('ritual_ZN14QXYModelMapper11setYSectionEi', ySection)

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
    Notes what was given, for Qt's 'QXYModelMapper::QXYModelMapper(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qxymodelmapper.html#QXYModelMapper

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QXYModelMapper::QXYModelMapper(QObject *parent)
    self._noteCreation(QXYModelMapper, lambda: Rituals.call(
        'ritual_ZN14QXYModelMapperC1EP7QObject',
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

  def d_func(self) -> Optional[QXYModelMapperPrivate]:
    """
    Calls Qt's 'QXYModelMapperPrivate *QXYModelMapper::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qxymodelmapper.html#d_func

    Returns
    -------

    Optional[QXYModelMapperPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QXYModelMapperPrivate *QXYModelMapper::d_func()
    address = self.uglySide.call('ritual_ZN14QXYModelMapper6d_funcEv')
    from . import QXYModelMapperPrivate
    return QXYModelMapperPrivate._cuteAt(address)
