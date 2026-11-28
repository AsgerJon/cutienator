"""
QBoxPlotModelMapper binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/qboxplotmodelmapper.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QAbstractItemModel, QMetaObject
  from . import QBoxPlotModelMapperPrivate, QBoxPlotSeries
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractItemModel = WAIT['QAbstractItemModel']
  QBoxPlotSeries = WAIT['QBoxPlotSeries']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QBoxPlotModelMapper(QObject):
  """
  The cute side of Qt's QBoxPlotModelMapper: a plain Python object standing
  in front of one C++ QBoxPlotModelMapper.

  It is built on the cute 'QObject', as Qt's QBoxPlotModelMapper is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QBoxPlotModelMapper that has a ritual and that
  Python can call so far, 17 names in all: 'metaObject', 'tr', 'model',
  'setModel', 'series', 'setSeries', 'first', 'setFirst', 'count',
  'setCount', 'firstBoxSetSection', 'setFirstBoxSetSection',
  'lastBoxSetSection', 'setLastBoxSetSection', 'orientation',
  'setOrientation', 'd_func'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QBoxPlotModelMapper::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QBoxPlotModelMapper::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'const QBoxPlotModelMapperPrivate *QBoxPlotModelMapper::d_func()
    const': takes in Python what 'QBoxPlotModelMapperPrivate
    *QBoxPlotModelMapper::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 23 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QBoxPlotModelMapper is created at the first use, not by
    'QBoxPlotModelMapper(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QBoxPlotModelMapper.
  - Qt tells when it has removed the C++ QBoxPlotModelMapper. Every call on
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
    Calls Qt's 'QString QBoxPlotModelMapper::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qboxplotmodelmapper.html#tr

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
    #  QString QBoxPlotModelMapper::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN19QBoxPlotModelMapper2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QBoxPlotModelMapper'

  #  A C++ QBoxPlotModelMapper Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QBoxPlotModelMapper'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QBoxPlotModelMapper::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qboxplotmodelmapper.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QBoxPlotModelMapper::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK19QBoxPlotModelMapper10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def model(self) -> Optional[QAbstractItemModel]:
    """
    Calls Qt's 'QAbstractItemModel *QBoxPlotModelMapper::model() const'.

    Qt's own words: https://doc.qt.io/qt-6/qboxplotmodelmapper.html#model

    Returns
    -------

    Optional[QAbstractItemModel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractItemModel *QBoxPlotModelMapper::model() const
    address = self.uglySide.call('ritual_ZNK19QBoxPlotModelMapper5modelEv')
    from ..QtCore import QAbstractItemModel
    return QAbstractItemModel._cuteAt(address)

  def series(self) -> Optional[QBoxPlotSeries]:
    """
    Calls Qt's 'QBoxPlotSeries *QBoxPlotModelMapper::series() const'.

    Qt's own words: https://doc.qt.io/qt-6/qboxplotmodelmapper.html#series

    Returns
    -------

    Optional[QBoxPlotSeries]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QBoxPlotSeries *QBoxPlotModelMapper::series() const
    address = self.uglySide.call('ritual_ZNK19QBoxPlotModelMapper6seriesEv')
    from . import QBoxPlotSeries
    return QBoxPlotSeries._cuteAt(address)

  def first(self) -> int:
    """
    Calls Qt's 'int QBoxPlotModelMapper::first() const'.

    Qt's own words: https://doc.qt.io/qt-6/qboxplotmodelmapper.html#first
    """
    #  int QBoxPlotModelMapper::first() const
    return self.uglySide.call('ritual_ZNK19QBoxPlotModelMapper5firstEv')

  def count(self) -> int:
    """
    Calls Qt's 'int QBoxPlotModelMapper::count() const'.

    Qt's own words: https://doc.qt.io/qt-6/qboxplotmodelmapper.html#count
    """
    #  int QBoxPlotModelMapper::count() const
    return self.uglySide.call('ritual_ZNK19QBoxPlotModelMapper5countEv')

  def firstBoxSetSection(self) -> int:
    """
    Calls Qt's 'int QBoxPlotModelMapper::firstBoxSetSection() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qboxplotmodelmapper.html#firstBoxSetSection
    """
    #  int QBoxPlotModelMapper::firstBoxSetSection() const
    return self.uglySide.call(
        'ritual_ZNK19QBoxPlotModelMapper18firstBoxSetSectionEv',
    )

  def lastBoxSetSection(self) -> int:
    """
    Calls Qt's 'int QBoxPlotModelMapper::lastBoxSetSection() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qboxplotmodelmapper.html#lastBoxSetSection
    """
    #  int QBoxPlotModelMapper::lastBoxSetSection() const
    return self.uglySide.call(
        'ritual_ZNK19QBoxPlotModelMapper17lastBoxSetSectionEv',
    )

  def orientation(self) -> Qt.Orientation:
    """
    Calls Qt's 'Qt::Orientation QBoxPlotModelMapper::orientation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qboxplotmodelmapper.html#orientation

    Returns
    -------

    Qt.Orientation
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.Orientation(number)'
      gives.
    """
    #  Qt::Orientation QBoxPlotModelMapper::orientation() const
    return Qt.Orientation(self.uglySide.call(
        'ritual_ZNK19QBoxPlotModelMapper11orientationEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAbstractItemModel)
  @overload(NoneType)
  def setModel(self, model: Optional[QAbstractItemModel]) -> None:
    """
    Calls Qt's 'void QBoxPlotModelMapper::setModel(QAbstractItemModel
    *model)'.

    Qt's own words: https://doc.qt.io/qt-6/qboxplotmodelmapper.html#setModel

    Parameters
    ----------

    model : Optional[QAbstractItemModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QBoxPlotModelMapper::setModel(QAbstractItemModel *model)
    self.uglySide.call(
        'ritual_ZN19QBoxPlotModelMapper8setModelEP18QAbstractItemModel',
        self._addressOf(model),
    )

  @overload(QBoxPlotSeries)
  @overload(NoneType)
  def setSeries(self, series: Optional[QBoxPlotSeries]) -> None:
    """
    Calls Qt's 'void QBoxPlotModelMapper::setSeries(QBoxPlotSeries *series)'.

    Qt's own words: https://doc.qt.io/qt-6/qboxplotmodelmapper.html#setSeries

    Parameters
    ----------

    series : Optional[QBoxPlotSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QBoxPlotModelMapper::setSeries(QBoxPlotSeries *series)
    self.uglySide.call(
        'ritual_ZN19QBoxPlotModelMapper9setSeriesEP14QBoxPlotSeries',
        self._addressOf(series),
    )

  @overload(int)
  def setFirst(self, first: int) -> None:
    """
    Calls Qt's 'void QBoxPlotModelMapper::setFirst(int first)'.

    Qt's own words: https://doc.qt.io/qt-6/qboxplotmodelmapper.html#setFirst

    Parameters
    ----------

    first : int
      Passed on as it is.
    """
    #  void QBoxPlotModelMapper::setFirst(int first)
    self.uglySide.call('ritual_ZN19QBoxPlotModelMapper8setFirstEi', first)

  @overload(int)
  def setCount(self, count: int) -> None:
    """
    Calls Qt's 'void QBoxPlotModelMapper::setCount(int count)'.

    Qt's own words: https://doc.qt.io/qt-6/qboxplotmodelmapper.html#setCount

    Parameters
    ----------

    count : int
      Passed on as it is.
    """
    #  void QBoxPlotModelMapper::setCount(int count)
    self.uglySide.call('ritual_ZN19QBoxPlotModelMapper8setCountEi', count)

  @overload(int)
  def setFirstBoxSetSection(self, firstBoxSetSection: int) -> None:
    """
    Calls Qt's 'void QBoxPlotModelMapper::setFirstBoxSetSection(int
    firstBoxSetSection)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qboxplotmodelmapper.html#setFirstBoxSetSection

    Parameters
    ----------

    firstBoxSetSection : int
      Passed on as it is.
    """
    #  void QBoxPlotModelMapper::setFirstBoxSetSection(int
    #      firstBoxSetSection)
    self.uglySide.call(
        'ritual_ZN19QBoxPlotModelMapper21setFirstBoxSetSectionEi',
        firstBoxSetSection,
    )

  @overload(int)
  def setLastBoxSetSection(self, lastBoxSetSection: int) -> None:
    """
    Calls Qt's 'void QBoxPlotModelMapper::setLastBoxSetSection(int
    lastBoxSetSection)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qboxplotmodelmapper.html#setLastBoxSetSection

    Parameters
    ----------

    lastBoxSetSection : int
      Passed on as it is.
    """
    #  void QBoxPlotModelMapper::setLastBoxSetSection(int lastBoxSetSection)
    self.uglySide.call(
        'ritual_ZN19QBoxPlotModelMapper20setLastBoxSetSectionEi',
        lastBoxSetSection,
    )

  @overload(Qt.Orientation)
  def setOrientation(self, orientation: Qt.Orientation) -> None:
    """
    Calls Qt's 'void QBoxPlotModelMapper::setOrientation(Qt::Orientation
    orientation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qboxplotmodelmapper.html#setOrientation

    Parameters
    ----------

    orientation : Qt.Orientation
      Passed on as its number.
    """
    #  void QBoxPlotModelMapper::setOrientation(Qt::Orientation orientation)
    self.uglySide.call(
        'ritual_ZN19QBoxPlotModelMapper14setOrientationEN2Qt11OrientationE',
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
    Notes what was given, for Qt's
    'QBoxPlotModelMapper::QBoxPlotModelMapper(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qboxplotmodelmapper.html#QBoxPlotModelMapper

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QBoxPlotModelMapper::QBoxPlotModelMapper(QObject *parent)
    self._noteCreation(QBoxPlotModelMapper, lambda: Rituals.call(
        'ritual_ZN19QBoxPlotModelMapperC1EP7QObject',
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

  def d_func(self) -> Optional[QBoxPlotModelMapperPrivate]:
    """
    Calls Qt's 'QBoxPlotModelMapperPrivate *QBoxPlotModelMapper::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qboxplotmodelmapper.html#d_func

    Returns
    -------

    Optional[QBoxPlotModelMapperPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QBoxPlotModelMapperPrivate *QBoxPlotModelMapper::d_func()
    address = self.uglySide.call('ritual_ZN19QBoxPlotModelMapper6d_funcEv')
    from . import QBoxPlotModelMapperPrivate
    return QBoxPlotModelMapperPrivate._cuteAt(address)
