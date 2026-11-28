"""
QBoxPlotSeries binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/qboxplotseries.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject
from . import QAbstractSeries

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QBrush, QPen
  from . import QBoxPlotSeriesPrivate, QBoxSet
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QBoxSet = WAIT['QBoxSet']
  QBrush = WAIT['QBrush']
  QPen = WAIT['QPen']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QBoxPlotSeries(QAbstractSeries):
  """
  The cute side of Qt's QBoxPlotSeries: a plain Python object standing in
  front of one C++ QBoxPlotSeries.

  It is built on the cute 'QAbstractSeries', as Qt's QBoxPlotSeries is built
  on Qt's QAbstractSeries, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QBoxPlotSeries that has a ritual and that Python can
  call so far, 31 names in all: 'metaObject', 'tr', 'append', 'remove',
  'take', 'insert', 'count', 'boxSets', 'clear', 'type',
  'setBoxOutlineVisible', 'boxOutlineVisible', 'setBoxWidth', 'boxWidth',
  'setBrush', 'brush', 'setPen', 'pen', 'clicked', 'hovered', 'pressed',
  'released', 'doubleClicked', 'countChanged', 'penChanged', 'brushChanged',
  'boxOutlineVisibilityChanged', 'boxWidthChanged', 'boxsetsAdded',
  'boxsetsRemoved', 'd_func'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QBoxPlotSeries::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QBoxPlotSeries::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QBoxPlotSeries::~QBoxPlotSeries()': the destructor: Python never
    removes a C++ QBoxPlotSeries.
  - Qt's 'const QBoxPlotSeriesPrivate *QBoxPlotSeries::d_func() const': takes
    in Python what 'QBoxPlotSeriesPrivate *QBoxPlotSeries::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 41 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QBoxPlotSeries is created at the first use, not by
    'QBoxPlotSeries(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QBoxPlotSeries.
  - Qt tells when it has removed the C++ QBoxPlotSeries. Every call on the
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
    Calls Qt's 'QString QBoxPlotSeries::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qboxplotseries.html#tr

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
    #  QString QBoxPlotSeries::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN14QBoxPlotSeries2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QBoxPlotSeries'

  #  A C++ QBoxPlotSeries Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QBoxPlotSeries'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QBoxPlotSeries::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qboxplotseries.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QBoxPlotSeries::metaObject() const
    address = self.uglySide.call('ritual_ZNK14QBoxPlotSeries10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def count(self) -> int:
    """
    Calls Qt's 'int QBoxPlotSeries::count() const'.

    Qt's own words: https://doc.qt.io/qt-6/qboxplotseries.html#count
    """
    #  int QBoxPlotSeries::count() const
    return self.uglySide.call('ritual_ZNK14QBoxPlotSeries5countEv')

  def boxSets(self) -> QList[QBoxSet]:
    """
    Calls Qt's 'QList<QBoxSet *> QBoxPlotSeries::boxSets() const'.

    Qt's own words: https://doc.qt.io/qt-6/qboxplotseries.html#boxSets

    Returns
    -------

    QList[QBoxSet]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QBoxSet *> QBoxPlotSeries::boxSets() const
    address = self.uglySide.call('ritual_ZNK14QBoxPlotSeries7boxSetsEv')
    from . import QBoxSet
    return QList[QBoxSet]._cuteOwning(address)

  def type(self) -> QAbstractSeries.SeriesType:
    """
    Calls Qt's 'QAbstractSeries::SeriesType QBoxPlotSeries::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qboxplotseries.html#type

    Returns
    -------

    QAbstractSeries.SeriesType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QAbstractSeries.SeriesType(number)' gives.
    """
    #  QAbstractSeries::SeriesType QBoxPlotSeries::type() const
    ritual = 'ritual_ZNK14QBoxPlotSeries4typeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QBoxPlotSeries4typeEv'
    return QAbstractSeries.SeriesType(self.uglySide.call(ritual))

  def brush(self) -> QBrush:
    """
    Calls Qt's 'QBrush QBoxPlotSeries::brush() const'.

    Qt's own words: https://doc.qt.io/qt-6/qboxplotseries.html#brush

    Returns
    -------

    QBrush
      A new cute QBrush around the copy Qt gave back. Python owns it.
    """
    #  QBrush QBoxPlotSeries::brush() const
    address = self.uglySide.call('ritual_ZNK14QBoxPlotSeries5brushEv')
    from ..QtGui import QBrush
    return QBrush._cuteOwning(address)

  def pen(self) -> QPen:
    """
    Calls Qt's 'QPen QBoxPlotSeries::pen() const'.

    Qt's own words: https://doc.qt.io/qt-6/qboxplotseries.html#pen

    Returns
    -------

    QPen
      A new cute QPen around the copy Qt gave back. Python owns it.
    """
    #  QPen QBoxPlotSeries::pen() const
    address = self.uglySide.call('ritual_ZNK14QBoxPlotSeries3penEv')
    from ..QtGui import QPen
    return QPen._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setBoxOutlineVisible(self, visible: bool) -> None:
    """
    Calls Qt's 'void QBoxPlotSeries::setBoxOutlineVisible(bool visible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qboxplotseries.html#setBoxOutlineVisible

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void QBoxPlotSeries::setBoxOutlineVisible(bool visible)
    self.uglySide.call(
        'ritual_ZN14QBoxPlotSeries20setBoxOutlineVisibleEb', visible,
    )

  @overload(float)
  def setBoxWidth(self, width: float) -> None:
    """
    Calls Qt's 'void QBoxPlotSeries::setBoxWidth(qreal width)'.

    Qt's own words: https://doc.qt.io/qt-6/qboxplotseries.html#setBoxWidth

    Parameters
    ----------

    width : float
      Passed on as it is.
    """
    #  void QBoxPlotSeries::setBoxWidth(qreal width)
    self.uglySide.call('ritual_ZN14QBoxPlotSeries11setBoxWidthEd', width)

  @overload(QBrush)
  def setBrush(self, brush: QBrush) -> None:
    """
    Calls Qt's 'void QBoxPlotSeries::setBrush(const QBrush &brush)'.

    Qt's own words: https://doc.qt.io/qt-6/qboxplotseries.html#setBrush

    Parameters
    ----------

    brush : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.
    """
    #  void QBoxPlotSeries::setBrush(const QBrush &brush)
    self.uglySide.call(
        'ritual_ZN14QBoxPlotSeries8setBrushERK6QBrush', self._valueOf(brush),
    )

  @overload(QPen)
  def setPen(self, pen: QPen) -> None:
    """
    Calls Qt's 'void QBoxPlotSeries::setPen(const QPen &pen)'.

    Qt's own words: https://doc.qt.io/qt-6/qboxplotseries.html#setPen

    Parameters
    ----------

    pen : QPen
      Passed on as a value: Qt reads the C++ QPen, which stays Python's own.
    """
    #  void QBoxPlotSeries::setPen(const QPen &pen)
    self.uglySide.call(
        'ritual_ZN14QBoxPlotSeries6setPenERK4QPen', self._valueOf(pen),
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
    Notes what was given, for Qt's 'QBoxPlotSeries::QBoxPlotSeries(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qboxplotseries.html#QBoxPlotSeries

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QBoxPlotSeries::QBoxPlotSeries(QObject *parent)
    self._noteCreation(QBoxPlotSeries, lambda: Rituals.call(
        'ritual_ZN14QBoxPlotSeriesC1EP7QObject',
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

  @overload(QBoxSet)
  @overload(NoneType)
  def append(self, box: Optional[QBoxSet]) -> bool:
    """
    Calls Qt's 'bool QBoxPlotSeries::append(QBoxSet *box)'.

    Qt's own words: https://doc.qt.io/qt-6/qboxplotseries.html#append

    Parameters
    ----------

    box : Optional[QBoxSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QBoxPlotSeries::append(QBoxSet *box)
    return self.uglySide.call(
        'ritual_ZN14QBoxPlotSeries6appendEP7QBoxSet', self._addressOf(box),
    )

  @overload(QList[QBoxSet])
  def append(self, boxes: QList[QBoxSet]) -> bool:
    """
    Calls Qt's 'bool QBoxPlotSeries::append(const QList<QBoxSet *> &boxes)'.

    Qt's own words: https://doc.qt.io/qt-6/qboxplotseries.html#append

    Parameters
    ----------

    boxes : QList[QBoxSet]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  bool QBoxPlotSeries::append(const QList<QBoxSet *> &boxes)
    return self.uglySide.call(
        'ritual_ZN14QBoxPlotSeries6appendERK5QListIP7QBoxSetE',
        self._valueOf(boxes),
    )

  @overload(QBoxSet)
  @overload(NoneType)
  def remove(self, box: Optional[QBoxSet]) -> bool:
    """
    Calls Qt's 'bool QBoxPlotSeries::remove(QBoxSet *box)'.

    Qt's own words: https://doc.qt.io/qt-6/qboxplotseries.html#remove

    Parameters
    ----------

    box : Optional[QBoxSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QBoxPlotSeries::remove(QBoxSet *box)
    return self.uglySide.call(
        'ritual_ZN14QBoxPlotSeries6removeEP7QBoxSet', self._addressOf(box),
    )

  @overload(QBoxSet)
  @overload(NoneType)
  def take(self, box: Optional[QBoxSet]) -> bool:
    """
    Calls Qt's 'bool QBoxPlotSeries::take(QBoxSet *box)'.

    Qt's own words: https://doc.qt.io/qt-6/qboxplotseries.html#take

    Parameters
    ----------

    box : Optional[QBoxSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QBoxPlotSeries::take(QBoxSet *box)
    return self.uglySide.call(
        'ritual_ZN14QBoxPlotSeries4takeEP7QBoxSet', self._addressOf(box),
    )

  @overload(int, QBoxSet)
  @overload(int, NoneType)
  def insert(self, index: int, box: Optional[QBoxSet]) -> bool:
    """
    Calls Qt's 'bool QBoxPlotSeries::insert(int index, QBoxSet *box)'.

    Qt's own words: https://doc.qt.io/qt-6/qboxplotseries.html#insert

    Parameters
    ----------

    index : int
      Passed on as it is.

    box : Optional[QBoxSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QBoxPlotSeries::insert(int index, QBoxSet *box)
    return self.uglySide.call(
        'ritual_ZN14QBoxPlotSeries6insertEiP7QBoxSet',
        index, self._addressOf(box),
    )

  def clear(self) -> None:
    """
    Calls Qt's 'void QBoxPlotSeries::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qboxplotseries.html#clear
    """
    #  void QBoxPlotSeries::clear()
    self.uglySide.call('ritual_ZN14QBoxPlotSeries5clearEv')

  def boxOutlineVisible(self) -> bool:
    """
    Calls Qt's 'bool QBoxPlotSeries::boxOutlineVisible()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qboxplotseries.html#boxOutlineVisible
    """
    #  bool QBoxPlotSeries::boxOutlineVisible()
    return self.uglySide.call(
        'ritual_ZN14QBoxPlotSeries17boxOutlineVisibleEv',
    )

  def boxWidth(self) -> float:
    """
    Calls Qt's 'qreal QBoxPlotSeries::boxWidth()'.

    Qt's own words: https://doc.qt.io/qt-6/qboxplotseries.html#boxWidth
    """
    #  qreal QBoxPlotSeries::boxWidth()
    return self.uglySide.call('ritual_ZN14QBoxPlotSeries8boxWidthEv')

  @overload(QBoxSet)
  @overload(NoneType)
  def clicked(self, boxset: Optional[QBoxSet]) -> None:
    """
    Calls Qt's 'void QBoxPlotSeries::clicked(QBoxSet *boxset)'.

    Qt's own words: https://doc.qt.io/qt-6/qboxplotseries.html#clicked

    Parameters
    ----------

    boxset : Optional[QBoxSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QBoxPlotSeries::clicked(QBoxSet *boxset)
    self.uglySide.call(
        'ritual_ZN14QBoxPlotSeries7clickedEP7QBoxSet',
        self._addressOf(boxset),
    )

  @overload(bool, QBoxSet)
  @overload(bool, NoneType)
  def hovered(self, status: bool, boxset: Optional[QBoxSet]) -> None:
    """
    Calls Qt's 'void QBoxPlotSeries::hovered(bool status, QBoxSet *boxset)'.

    Qt's own words: https://doc.qt.io/qt-6/qboxplotseries.html#hovered

    Parameters
    ----------

    status : bool
      Passed on as it is.

    boxset : Optional[QBoxSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QBoxPlotSeries::hovered(bool status, QBoxSet *boxset)
    self.uglySide.call(
        'ritual_ZN14QBoxPlotSeries7hoveredEbP7QBoxSet',
        status, self._addressOf(boxset),
    )

  @overload(QBoxSet)
  @overload(NoneType)
  def pressed(self, boxset: Optional[QBoxSet]) -> None:
    """
    Calls Qt's 'void QBoxPlotSeries::pressed(QBoxSet *boxset)'.

    Qt's own words: https://doc.qt.io/qt-6/qboxplotseries.html#pressed

    Parameters
    ----------

    boxset : Optional[QBoxSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QBoxPlotSeries::pressed(QBoxSet *boxset)
    self.uglySide.call(
        'ritual_ZN14QBoxPlotSeries7pressedEP7QBoxSet',
        self._addressOf(boxset),
    )

  @overload(QBoxSet)
  @overload(NoneType)
  def released(self, boxset: Optional[QBoxSet]) -> None:
    """
    Calls Qt's 'void QBoxPlotSeries::released(QBoxSet *boxset)'.

    Qt's own words: https://doc.qt.io/qt-6/qboxplotseries.html#released

    Parameters
    ----------

    boxset : Optional[QBoxSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QBoxPlotSeries::released(QBoxSet *boxset)
    self.uglySide.call(
        'ritual_ZN14QBoxPlotSeries8releasedEP7QBoxSet',
        self._addressOf(boxset),
    )

  @overload(QBoxSet)
  @overload(NoneType)
  def doubleClicked(self, boxset: Optional[QBoxSet]) -> None:
    """
    Calls Qt's 'void QBoxPlotSeries::doubleClicked(QBoxSet *boxset)'.

    Qt's own words: https://doc.qt.io/qt-6/qboxplotseries.html#doubleClicked

    Parameters
    ----------

    boxset : Optional[QBoxSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QBoxPlotSeries::doubleClicked(QBoxSet *boxset)
    self.uglySide.call(
        'ritual_ZN14QBoxPlotSeries13doubleClickedEP7QBoxSet',
        self._addressOf(boxset),
    )

  def countChanged(self) -> None:
    """
    Calls Qt's 'void QBoxPlotSeries::countChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qboxplotseries.html#countChanged
    """
    #  void QBoxPlotSeries::countChanged()
    self.uglySide.call('ritual_ZN14QBoxPlotSeries12countChangedEv')

  def penChanged(self) -> None:
    """
    Calls Qt's 'void QBoxPlotSeries::penChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qboxplotseries.html#penChanged
    """
    #  void QBoxPlotSeries::penChanged()
    self.uglySide.call('ritual_ZN14QBoxPlotSeries10penChangedEv')

  def brushChanged(self) -> None:
    """
    Calls Qt's 'void QBoxPlotSeries::brushChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qboxplotseries.html#brushChanged
    """
    #  void QBoxPlotSeries::brushChanged()
    self.uglySide.call('ritual_ZN14QBoxPlotSeries12brushChangedEv')

  def boxOutlineVisibilityChanged(self) -> None:
    """
    Calls Qt's 'void QBoxPlotSeries::boxOutlineVisibilityChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qboxplotseries.html#boxOutlineVisibilityChanged
    """
    #  void QBoxPlotSeries::boxOutlineVisibilityChanged()
    self.uglySide.call(
        'ritual_ZN14QBoxPlotSeries27boxOutlineVisibilityChangedEv',
    )

  def boxWidthChanged(self) -> None:
    """
    Calls Qt's 'void QBoxPlotSeries::boxWidthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qboxplotseries.html#boxWidthChanged
    """
    #  void QBoxPlotSeries::boxWidthChanged()
    self.uglySide.call('ritual_ZN14QBoxPlotSeries15boxWidthChangedEv')

  @overload(QList[QBoxSet])
  def boxsetsAdded(self, sets: QList[QBoxSet]) -> None:
    """
    Calls Qt's 'void QBoxPlotSeries::boxsetsAdded(const QList<QBoxSet *>
    &sets)'.

    Qt's own words: https://doc.qt.io/qt-6/qboxplotseries.html#boxsetsAdded

    Parameters
    ----------

    sets : QList[QBoxSet]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QBoxPlotSeries::boxsetsAdded(const QList<QBoxSet *> &sets)
    self.uglySide.call(
        'ritual_ZN14QBoxPlotSeries12boxsetsAddedERK5QListIP7QBoxSetE',
        self._valueOf(sets),
    )

  @overload(QList[QBoxSet])
  def boxsetsRemoved(self, sets: QList[QBoxSet]) -> None:
    """
    Calls Qt's 'void QBoxPlotSeries::boxsetsRemoved(const QList<QBoxSet *>
    &sets)'.

    Qt's own words: https://doc.qt.io/qt-6/qboxplotseries.html#boxsetsRemoved

    Parameters
    ----------

    sets : QList[QBoxSet]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QBoxPlotSeries::boxsetsRemoved(const QList<QBoxSet *> &sets)
    self.uglySide.call(
        'ritual_ZN14QBoxPlotSeries14boxsetsRemovedERK5QListIP7QBoxSetE',
        self._valueOf(sets),
    )

  def d_func(self) -> Optional[QBoxPlotSeriesPrivate]:
    """
    Calls Qt's 'QBoxPlotSeriesPrivate *QBoxPlotSeries::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qboxplotseries.html#d_func

    Returns
    -------

    Optional[QBoxPlotSeriesPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QBoxPlotSeriesPrivate *QBoxPlotSeries::d_func()
    address = self.uglySide.call('ritual_ZN14QBoxPlotSeries6d_funcEv')
    from . import QBoxPlotSeriesPrivate
    return QBoxPlotSeriesPrivate._cuteAt(address)
