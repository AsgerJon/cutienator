"""
QBar3DSeriesPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGraphs/6.12.0/QtGraphs/private/qbar3dseries_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QBar3DSeriesPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QStringList
from . import QAbstract3DSeriesPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QPoint
  from ..QtGui import QColor
  from . import QAbstractDataProxy, QBar3DSeries, QCategory3DAxis
  from . import QQuickGraphsItem, QValue3DAxis
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractDataProxy = WAIT['QtGraphs:QAbstractDataProxy']
  QBar3DSeries = WAIT['QtGraphs:QBar3DSeries']
  QCategory3DAxis = WAIT['QtGraphs:QCategory3DAxis']
  QColor = WAIT['QColor']
  QPoint = WAIT['QPoint']
  QQuickGraphsItem = WAIT['QQuickGraphsItem']
  QValue3DAxis = WAIT['QtGraphs:QValue3DAxis']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QBar3DSeriesPrivate(QAbstract3DSeriesPrivate):
  """
  The cute side of Qt's QBar3DSeriesPrivate: a plain Python object standing
  in front of one C++ QBar3DSeriesPrivate.

  It is built on the cute 'QAbstract3DSeriesPrivate', as Qt's
  QBar3DSeriesPrivate is built on Qt's QAbstract3DSeriesPrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QBar3DSeriesPrivate that has a ritual and that
  Python can call so far, 21 names in all: 'q_func', 'get', 'setDataProxy',
  'connectGraphAndProxy', 'createItemLabel', 'setSelectedBar',
  'setRowColors', 'setValueColoringEnabled', 'clearRow', 'clearArray',
  'setRowLabels', 'setColumnLabels', 'setCustomRowLabels',
  'setCustomColumnLabels', 'fixRowLabels', 'setRowAxis', 'setValueAxis',
  'setColumnAxis', 'resetRowAxis', 'resetValueAxis', 'resetColumnAxis'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QBar3DSeries *QBar3DSeriesPrivate::q_func() const': takes in
    Python what 'QBar3DSeries *QBar3DSeriesPrivate::q_func()' takes.
  - Qt's 'QBar3DSeriesPrivate::~QBar3DSeriesPrivate()': the destructor:
    Python never removes a C++ QBar3DSeriesPrivate.
  - Qt's 'void QBar3DSeriesPrivate::setDataArray(const QBarDataArray
    &newDataArray)': takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QBar3DSeriesPrivate is created at the first use, not by
    'QBar3DSeriesPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QBar3DSeriesPrivate.
  - Each name of Qt's QBar3DSeriesPrivate that has no cute function yet,
    'setDataArray', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QBar3DSeries)
  @overload(NoneType)
  def get(item: Optional[QBar3DSeries]) -> Optional[QBar3DSeriesPrivate]:
    """
    Calls Qt's 'QBar3DSeriesPrivate *QBar3DSeriesPrivate::get(QBar3DSeries
    *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qbar3dseriesprivate.html#get

    Parameters
    ----------

    item : Optional[QBar3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QBar3DSeriesPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QBar3DSeriesPrivate *QBar3DSeriesPrivate::get(QBar3DSeries *item)
    address = Rituals.call(
        'ritual_ZN19QBar3DSeriesPrivate3getEP12QBar3DSeries',
        CuteMixin._addressOf(item),
    )
    return QBar3DSeriesPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QBar3DSeriesPrivate'
  #  The part of Qt it is of, as another part has a class of its name too.
  __qt_part__ = 'QtGraphs'

  #  A C++ QBar3DSeriesPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QBar3DSeriesPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAbstractDataProxy)
  @overload(NoneType)
  def setDataProxy(self, proxy: Optional[QAbstractDataProxy]) -> None:
    """
    Calls Qt's 'void QBar3DSeriesPrivate::setDataProxy(QAbstractDataProxy
    *proxy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbar3dseriesprivate.html#setDataProxy

    Parameters
    ----------

    proxy : Optional[QAbstractDataProxy]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QBar3DSeriesPrivate::setDataProxy(QAbstractDataProxy *proxy)
    ritual = (
        'ritual_ZN19QBar3DSeriesPrivate12setDataProxyEP18QAbstractDataProxy')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QBar3DSeriesPrivate12setDataProxyEP18QAbstractDat'
          'aProxy')
    self.uglySide.call(ritual, self._addressOf(proxy))

  @overload(QPoint)
  def setSelectedBar(self, position: QPoint) -> None:
    """
    Calls Qt's 'void QBar3DSeriesPrivate::setSelectedBar(QPoint position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbar3dseriesprivate.html#setSelectedBar

    Parameters
    ----------

    position : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QBar3DSeriesPrivate::setSelectedBar(QPoint position)
    self.uglySide.call(
        'ritual_ZN19QBar3DSeriesPrivate14setSelectedBarE6QPoint',
        self._valueOf(position),
    )

  @overload(QList[QColor])
  def setRowColors(self, colors: QList[QColor]) -> None:
    """
    Calls Qt's 'void QBar3DSeriesPrivate::setRowColors(const QList<QColor>
    &colors)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbar3dseriesprivate.html#setRowColors

    Parameters
    ----------

    colors : QList[QColor]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QBar3DSeriesPrivate::setRowColors(const QList<QColor> &colors)
    self.uglySide.call(
        'ritual_ZN19QBar3DSeriesPrivate12setRowColorsERK5QListI6QColorE',
        self._valueOf(colors),
    )

  @overload(bool)
  def setValueColoringEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QBar3DSeriesPrivate::setValueColoringEnabled(bool
    enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbar3dseriesprivate.html#setValueColoringEnabled

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QBar3DSeriesPrivate::setValueColoringEnabled(bool enabled)
    self.uglySide.call(
        'ritual_ZN19QBar3DSeriesPrivate23setValueColoringEnabledEb', enabled,
    )

  @overload(QStringList)
  def setRowLabels(self, labels: QStringList) -> None:
    """
    Calls Qt's 'void QBar3DSeriesPrivate::setRowLabels(const QStringList
    &labels)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbar3dseriesprivate.html#setRowLabels

    Parameters
    ----------

    labels : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QBar3DSeriesPrivate::setRowLabels(const QStringList &labels)
    self.uglySide.call(
        'ritual_ZN19QBar3DSeriesPrivate12setRowLabelsERK5QListI7QStringE',
        self._valueOf(labels),
    )

  @overload(QStringList)
  def setColumnLabels(self, labels: QStringList) -> None:
    """
    Calls Qt's 'void QBar3DSeriesPrivate::setColumnLabels(const QStringList
    &labels)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbar3dseriesprivate.html#setColumnLabels

    Parameters
    ----------

    labels : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QBar3DSeriesPrivate::setColumnLabels(const QStringList &labels)
    self.uglySide.call(
        'ritual_ZN19QBar3DSeriesPrivate15setColumnLabelsERK5QListI7QStringE',
        self._valueOf(labels),
    )

  @overload(QStringList)
  def setCustomRowLabels(self, labels: QStringList) -> None:
    """
    Calls Qt's 'void QBar3DSeriesPrivate::setCustomRowLabels(const
    QStringList &labels)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbar3dseriesprivate.html#setCustomRowLabels

    Parameters
    ----------

    labels : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QBar3DSeriesPrivate::setCustomRowLabels(const QStringList
    #      &labels)
    self.uglySide.call(
        'ritual_ZN19QBar3DSeriesPrivate18setCustomRowLabelsERK5QListI7QStri'
        'ngE',
        self._valueOf(labels),
    )

  @overload(QStringList)
  def setCustomColumnLabels(self, labels: QStringList) -> None:
    """
    Calls Qt's 'void QBar3DSeriesPrivate::setCustomColumnLabels(const
    QStringList &labels)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbar3dseriesprivate.html#setCustomColumnLabels

    Parameters
    ----------

    labels : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QBar3DSeriesPrivate::setCustomColumnLabels(const QStringList
    #      &labels)
    self.uglySide.call(
        'ritual_ZN19QBar3DSeriesPrivate21setCustomColumnLabelsERK5QListI7QS'
        'tringE',
        self._valueOf(labels),
    )

  @overload(QCategory3DAxis)
  @overload(NoneType)
  def setRowAxis(self, axis: Optional[QCategory3DAxis]) -> None:
    """
    Calls Qt's 'void QBar3DSeriesPrivate::setRowAxis(QCategory3DAxis *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbar3dseriesprivate.html#setRowAxis

    Parameters
    ----------

    axis : Optional[QCategory3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QBar3DSeriesPrivate::setRowAxis(QCategory3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN19QBar3DSeriesPrivate10setRowAxisEP15QCategory3DAxis',
        self._addressOf(axis),
    )

  @overload(QValue3DAxis)
  @overload(NoneType)
  def setValueAxis(self, axis: Optional[QValue3DAxis]) -> None:
    """
    Calls Qt's 'void QBar3DSeriesPrivate::setValueAxis(QValue3DAxis *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbar3dseriesprivate.html#setValueAxis

    Parameters
    ----------

    axis : Optional[QValue3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QBar3DSeriesPrivate::setValueAxis(QValue3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN19QBar3DSeriesPrivate12setValueAxisEP12QValue3DAxis',
        self._addressOf(axis),
    )

  @overload(QCategory3DAxis)
  @overload(NoneType)
  def setColumnAxis(self, axis: Optional[QCategory3DAxis]) -> None:
    """
    Calls Qt's 'void QBar3DSeriesPrivate::setColumnAxis(QCategory3DAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbar3dseriesprivate.html#setColumnAxis

    Parameters
    ----------

    axis : Optional[QCategory3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QBar3DSeriesPrivate::setColumnAxis(QCategory3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN19QBar3DSeriesPrivate13setColumnAxisEP15QCategory3DAxis',
        self._addressOf(axis),
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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QBar3DSeriesPrivate::QBar3DSeriesPrivate()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qbar3dseriesprivate.html#QBar3DSeriesPrivate
    """
    #  QBar3DSeriesPrivate::QBar3DSeriesPrivate()
    self._noteCreation(QBar3DSeriesPrivate, lambda: Rituals.call(
        'ritual_ZN19QBar3DSeriesPrivateC1Ev',
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

  def q_func(self) -> Optional[QBar3DSeries]:
    """
    Calls Qt's 'QBar3DSeries *QBar3DSeriesPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qbar3dseriesprivate.html#q_func

    Returns
    -------

    Optional[QBar3DSeries]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QBar3DSeries *QBar3DSeriesPrivate::q_func()
    address = self.uglySide.call('ritual_ZN19QBar3DSeriesPrivate6q_funcEv')
    from . import QBar3DSeries
    return QBar3DSeries._cuteAt(address)

  @overload(QQuickGraphsItem)
  @overload(NoneType)
  def connectGraphAndProxy(
      self,
      newGraph: Optional[QQuickGraphsItem],
  ) -> None:
    """
    Calls Qt's 'void
    QBar3DSeriesPrivate::connectGraphAndProxy(QQuickGraphsItem *newGraph)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbar3dseriesprivate.html#connectGraphAndProxy

    Parameters
    ----------

    newGraph : Optional[QQuickGraphsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QBar3DSeriesPrivate::connectGraphAndProxy(QQuickGraphsItem
    #      *newGraph)
    ritual = (
        'ritual_ZN19QBar3DSeriesPrivate20connectGraphAndProxyEP16QQuickGrap'
        'hsItem')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QBar3DSeriesPrivate20connectGraphAndProxyEP16QQui'
          'ckGraphsItem')
    self.uglySide.call(ritual, self._addressOf(newGraph))

  def createItemLabel(self) -> None:
    """
    Calls Qt's 'void QBar3DSeriesPrivate::createItemLabel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbar3dseriesprivate.html#createItemLabel
    """
    #  void QBar3DSeriesPrivate::createItemLabel()
    ritual = 'ritual_ZN19QBar3DSeriesPrivate15createItemLabelEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QBar3DSeriesPrivate15createItemLabelEv'
    self.uglySide.call(ritual)

  @overload(int)
  def clearRow(self, rowIndex: int) -> None:
    """
    Calls Qt's 'void QBar3DSeriesPrivate::clearRow(qsizetype rowIndex)'.

    Qt's own words: https://doc.qt.io/qt-6/qbar3dseriesprivate.html#clearRow

    Parameters
    ----------

    rowIndex : int
      Passed on as it is.
    """
    #  void QBar3DSeriesPrivate::clearRow(qsizetype rowIndex)
    self.uglySide.call('ritual_ZN19QBar3DSeriesPrivate8clearRowEx', rowIndex)

  def clearArray(self) -> None:
    """
    Calls Qt's 'void QBar3DSeriesPrivate::clearArray()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbar3dseriesprivate.html#clearArray
    """
    #  void QBar3DSeriesPrivate::clearArray()
    self.uglySide.call('ritual_ZN19QBar3DSeriesPrivate10clearArrayEv')

  @overload(int, int, QStringList, bool)
  def fixRowLabels(
      self,
      startIndex: int,
      count: int,
      newLabels: QStringList,
      isInsert: bool,
  ) -> None:
    """
    Calls Qt's 'void QBar3DSeriesPrivate::fixRowLabels(qsizetype startIndex,
    qsizetype count, const QStringList &newLabels, bool isInsert)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbar3dseriesprivate.html#fixRowLabels

    Parameters
    ----------

    startIndex : int
      Passed on as it is.

    count : int
      Passed on as it is.

    newLabels : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    isInsert : bool
      Passed on as it is.
    """
    #  void QBar3DSeriesPrivate::fixRowLabels(qsizetype startIndex, qsizetype
    #      count, const QStringList &newLabels, bool isInsert)
    self.uglySide.call(
        'ritual_ZN19QBar3DSeriesPrivate12fixRowLabelsExxRK5QListI7QStringEb',
        startIndex, count, self._valueOf(newLabels), isInsert,
    )

  def resetRowAxis(self) -> None:
    """
    Calls Qt's 'void QBar3DSeriesPrivate::resetRowAxis()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbar3dseriesprivate.html#resetRowAxis
    """
    #  void QBar3DSeriesPrivate::resetRowAxis()
    self.uglySide.call('ritual_ZN19QBar3DSeriesPrivate12resetRowAxisEv')

  def resetValueAxis(self) -> None:
    """
    Calls Qt's 'void QBar3DSeriesPrivate::resetValueAxis()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbar3dseriesprivate.html#resetValueAxis
    """
    #  void QBar3DSeriesPrivate::resetValueAxis()
    self.uglySide.call('ritual_ZN19QBar3DSeriesPrivate14resetValueAxisEv')

  def resetColumnAxis(self) -> None:
    """
    Calls Qt's 'void QBar3DSeriesPrivate::resetColumnAxis()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbar3dseriesprivate.html#resetColumnAxis
    """
    #  void QBar3DSeriesPrivate::resetColumnAxis()
    self.uglySide.call('ritual_ZN19QBar3DSeriesPrivate15resetColumnAxisEv')

  @staticmethod
  def setDataArray(*__, **_) -> Never:
    """
    Qt's 'void QBar3DSeriesPrivate::setDataArray(const QBarDataArray
    &newDataArray)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QBar3DSeriesPrivate.setDataArray' has no cute function yet. Qt's "
        "'void QBar3DSeriesPrivate::setDataArray(const QBarDataArray "
        "&newDataArray)': takes a type Python has no way to hand over yet.")
