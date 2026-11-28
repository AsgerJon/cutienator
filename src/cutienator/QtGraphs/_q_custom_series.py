"""
QCustomSeries binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGraphs/qcustomseries.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QMap, QObject
from . import QAbstractSeries

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject, QVariant
  from ..QtQml import QQmlComponent
  from ..QtQuick import QQuickItem
  from . import QCustomSeriesCanvasRenderer, QCustomSeriesData
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QCustomSeriesCanvasRenderer = WAIT['QCustomSeriesCanvasRenderer']
  QEvent = WAIT['QEvent']
  QQmlComponent = WAIT['QQmlComponent']
  QQuickItem = WAIT['QQuickItem']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QCustomSeries(QAbstractSeries):
  """
  The cute side of Qt's QCustomSeries: a plain Python object standing in
  front of one C++ QCustomSeries.

  It is built on the cute 'QAbstractSeries', as Qt's QCustomSeries is built
  on Qt's QAbstractSeries, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QCustomSeries that has a ritual and that Python can
  call so far, 17 names in all: 'metaObject', 'tr', 'type', 'dataItems',
  'delegate', 'setDelegate', 'setCustomSeriesPainter', 'mapX', 'mapY',
  'append', 'insert', 'remove', 'clear', 'delegateChanged',
  'componentComplete', 'updateDelegate', 'event'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QCustomSeries::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QCustomSeries::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QCustomSeries::~QCustomSeries()': the destructor: Python never
    removes a C++ QCustomSeries.
  - Qt's 'QCustomSeries::QCustomSeries(QCustomSeriesPrivate &dd, QObject
    *parent)': takes a type Python has no way to hand over yet.
  - Qt's 'QCustomSeriesPrivate *QCustomSeries::d_func()': gives
    'QCustomSeriesPrivate', which has no cute class yet.
  - Qt's 'const QCustomSeriesPrivate *QCustomSeries::d_func() const': gives
    'QCustomSeriesPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  6 of the 32 functions Qt declares: 4 forbidden; 2 not a gap.

  What to expect
  --------------

  - The C++ QCustomSeries is created at the first use, not by
    'QCustomSeries(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QCustomSeries.
  - Qt tells when it has removed the C++ QCustomSeries. Every call on the
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
    Calls Qt's 'QString QCustomSeries::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qcustomseries.html#tr

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
    #  QString QCustomSeries::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN13QCustomSeries2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCustomSeries'

  #  A C++ QCustomSeries Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QCustomSeries'

  #  The functions Qt calls itself that QCustomSeries is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'updateDelegate': (
          ('_ZN13QCustomSeries14updateDelegateEP10QQuickItemx',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
               ('long long', 'number', ''),
           )),
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
    Calls Qt's 'const QMetaObject *QCustomSeries::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcustomseries.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QCustomSeries::metaObject() const
    address = self.uglySide.call('ritual_ZNK13QCustomSeries10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def type(self) -> QAbstractSeries.SeriesType:
    """
    Calls Qt's 'QAbstractSeries::SeriesType QCustomSeries::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcustomseries.html#type

    Returns
    -------

    QAbstractSeries.SeriesType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QAbstractSeries.SeriesType(number)' gives.
    """
    #  QAbstractSeries::SeriesType QCustomSeries::type() const
    ritual = 'ritual_ZNK13QCustomSeries4typeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13QCustomSeries4typeEv'
    return QAbstractSeries.SeriesType(self.uglySide.call(ritual))

  def dataItems(self) -> QList[QCustomSeriesData]:
    """
    Calls Qt's 'QList<QCustomSeriesData *> QCustomSeries::dataItems() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcustomseries.html#dataItems

    Returns
    -------

    QList[QCustomSeriesData]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QCustomSeriesData *> QCustomSeries::dataItems() const
    address = self.uglySide.call('ritual_ZNK13QCustomSeries9dataItemsEv')
    from . import QCustomSeriesData
    return QList[QCustomSeriesData]._cuteOwning(address)

  def delegate(self) -> Optional[QQmlComponent]:
    """
    Calls Qt's 'QQmlComponent *QCustomSeries::delegate() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcustomseries.html#delegate

    Returns
    -------

    Optional[QQmlComponent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlComponent *QCustomSeries::delegate() const
    address = self.uglySide.call('ritual_ZNK13QCustomSeries8delegateEv')
    from ..QtQml import QQmlComponent
    return QQmlComponent._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQmlComponent)
  @overload(NoneType)
  def setDelegate(self, newDelegate: Optional[QQmlComponent]) -> None:
    """
    Calls Qt's 'void QCustomSeries::setDelegate(QQmlComponent *newDelegate)'.

    Qt's own words: https://doc.qt.io/qt-6/qcustomseries.html#setDelegate

    Parameters
    ----------

    newDelegate : Optional[QQmlComponent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QCustomSeries::setDelegate(QQmlComponent *newDelegate)
    self.uglySide.call(
        'ritual_ZN13QCustomSeries11setDelegateEP13QQmlComponent',
        self._addressOf(newDelegate),
    )

  @overload(QCustomSeriesCanvasRenderer)
  @overload(NoneType)
  def setCustomSeriesPainter(
      self,
      painter: Optional[QCustomSeriesCanvasRenderer],
  ) -> None:
    """
    Calls Qt's 'void
    QCustomSeries::setCustomSeriesPainter(QCustomSeriesCanvasRenderer
    *painter)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcustomseries.html#setCustomSeriesPainter

    Parameters
    ----------

    painter : Optional[QCustomSeriesCanvasRenderer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QCustomSeries::setCustomSeriesPainter(QCustomSeriesCanvasRenderer
    #      *painter)
    self.uglySide.call(
        'ritual_ZN13QCustomSeries22setCustomSeriesPainterEP27QCustomSeriesC'
        'anvasRenderer',
        self._addressOf(painter),
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
    Notes what was given, for Qt's 'QCustomSeries::QCustomSeries(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcustomseries.html#QCustomSeries

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QCustomSeries::QCustomSeries(QObject *parent)
    self._noteCreation(QCustomSeries, lambda: Rituals.call(
        'ritual_ZN13QCustomSeriesC1EP7QObject',
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

  @overload(float)
  def mapX(self, x: float) -> float:
    """
    Calls Qt's 'qreal QCustomSeries::mapX(qreal x)'.

    Qt's own words: https://doc.qt.io/qt-6/qcustomseries.html#mapX

    Parameters
    ----------

    x : float
      Passed on as it is.
    """
    #  qreal QCustomSeries::mapX(qreal x)
    return self.uglySide.call('ritual_ZN13QCustomSeries4mapXEd', x)

  @overload(float)
  def mapY(self, y: float) -> float:
    """
    Calls Qt's 'qreal QCustomSeries::mapY(qreal y)'.

    Qt's own words: https://doc.qt.io/qt-6/qcustomseries.html#mapY

    Parameters
    ----------

    y : float
      Passed on as it is.
    """
    #  qreal QCustomSeries::mapY(qreal y)
    return self.uglySide.call('ritual_ZN13QCustomSeries4mapYEd', y)

  @overload(QMap[str, QVariant])
  def append(self, data: QMap[str, QVariant]) -> None:
    """
    Calls Qt's 'void QCustomSeries::append(const QVariantMap &data)'.

    Qt's own words: https://doc.qt.io/qt-6/qcustomseries.html#append

    Parameters
    ----------

    data : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.
    """
    #  void QCustomSeries::append(const QVariantMap &data)
    self.uglySide.call(
        'ritual_ZN13QCustomSeries6appendERK4QMapI7QString8QVariantE',
        self._valueOf(data),
    )

  @overload()
  def append(self) -> None:
    """
    Calls Qt's 'void QCustomSeries::append()'.

    Qt's own words: https://doc.qt.io/qt-6/qcustomseries.html#append
    """
    #  void QCustomSeries::append()
    self.uglySide.call('ritual_ZN13QCustomSeries6appendEv')

  @overload(int, QMap[str, QVariant])
  def insert(self, index: int, data: QMap[str, QVariant]) -> None:
    """
    Calls Qt's 'void QCustomSeries::insert(qsizetype index, const QVariantMap
    &data)'.

    Qt's own words: https://doc.qt.io/qt-6/qcustomseries.html#insert

    Parameters
    ----------

    index : int
      Passed on as it is.

    data : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.
    """
    #  void QCustomSeries::insert(qsizetype index, const QVariantMap &data)
    self.uglySide.call(
        'ritual_ZN13QCustomSeries6insertExRK4QMapI7QString8QVariantE',
        index, self._valueOf(data),
    )

  @overload(int)
  def insert(self, index: int) -> None:
    """
    Calls Qt's 'void QCustomSeries::insert(qsizetype index)'.

    Qt's own words: https://doc.qt.io/qt-6/qcustomseries.html#insert

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QCustomSeries::insert(qsizetype index)
    self.uglySide.call('ritual_ZN13QCustomSeries6insertEx', index)

  @overload(int)
  def remove(self, index: int) -> None:
    """
    Calls Qt's 'void QCustomSeries::remove(qsizetype index)'.

    Qt's own words: https://doc.qt.io/qt-6/qcustomseries.html#remove

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QCustomSeries::remove(qsizetype index)
    self.uglySide.call('ritual_ZN13QCustomSeries6removeEx', index)

  def clear(self) -> None:
    """
    Calls Qt's 'void QCustomSeries::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qcustomseries.html#clear
    """
    #  void QCustomSeries::clear()
    self.uglySide.call('ritual_ZN13QCustomSeries5clearEv')

  def delegateChanged(self) -> None:
    """
    Calls Qt's 'void QCustomSeries::delegateChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qcustomseries.html#delegateChanged
    """
    #  void QCustomSeries::delegateChanged()
    self.uglySide.call('ritual_ZN13QCustomSeries15delegateChangedEv')

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QCustomSeries::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcustomseries.html#componentComplete
    """
    #  void QCustomSeries::componentComplete()
    ritual = 'ritual_ZN13QCustomSeries17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QCustomSeries17componentCompleteEv'
    self.uglySide.call(ritual)

  @overload(QQuickItem, int)
  @overload(NoneType, int)
  def updateDelegate(self, item: Optional[QQuickItem], index: int) -> None:
    """
    Calls Qt's 'void QCustomSeries::updateDelegate(QQuickItem *item,
    qsizetype index)'.

    Qt's own words: https://doc.qt.io/qt-6/qcustomseries.html#updateDelegate

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    index : int
      Passed on as it is.
    """
    #  void QCustomSeries::updateDelegate(QQuickItem *item, qsizetype index)
    ritual = 'ritual_ZN13QCustomSeries14updateDelegateEP10QQuickItemx'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QCustomSeries14updateDelegateEP10QQuickItemx'
    self.uglySide.call(ritual, self._addressOf(item), index)

  @overload(QEvent)
  @overload(NoneType)
  def event(self, event: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QCustomSeries::event(QEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qcustomseries.html#event

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QCustomSeries::event(QEvent *event)
    ritual = 'ritual_ZN13QCustomSeries5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QCustomSeries5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(event))
