"""
QScatter3DSeriesPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGraphs/6.12.0/QtGraphs/private/qscatter3dseries_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QScatter3DSeriesPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QList
from . import QAbstract3DSeriesPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtGui import QVector3D
  from . import QAbstractDataProxy, QQuickGraphsItem, QScatter3DSeries
  from . import QScatterDataItem, QValue3DAxis
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractDataProxy = WAIT['QtGraphs:QAbstractDataProxy']
  QQuickGraphsItem = WAIT['QQuickGraphsItem']
  QScatterDataItem = WAIT['QtGraphs:QScatterDataItem']
  QValue3DAxis = WAIT['QtGraphs:QValue3DAxis']
  QVector3D = WAIT['QVector3D']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QScatter3DSeriesPrivate(QAbstract3DSeriesPrivate):
  """
  The cute side of Qt's QScatter3DSeriesPrivate: a plain Python object
  standing in front of one C++ QScatter3DSeriesPrivate.

  It is built on the cute 'QAbstract3DSeriesPrivate', as Qt's
  QScatter3DSeriesPrivate is built on Qt's QAbstract3DSeriesPrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QScatter3DSeriesPrivate that has a ritual and that
  Python can call so far, 16 names in all: 'q_func', 'setDataProxy',
  'connectGraphAndProxy', 'createItemLabel', 'setSelectedItem',
  'setItemSize', 'setDataArray', 'clearArray', 'setScaleArray',
  'clearScaleArray', 'setAxisX', 'setAxisY', 'setAxisZ', 'resetAxisX',
  'resetAxisY', 'resetAxisZ'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QScatter3DSeries *QScatter3DSeriesPrivate::q_func() const':
    takes in Python what 'QScatter3DSeries
    *QScatter3DSeriesPrivate::q_func()' takes.
  - Qt's 'QScatter3DSeriesPrivate::~QScatter3DSeriesPrivate()': the
    destructor: Python never removes a C++ QScatter3DSeriesPrivate.

  What to expect
  --------------

  - The C++ QScatter3DSeriesPrivate is created at the first use, not by
    'QScatter3DSeriesPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QScatter3DSeriesPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QScatter3DSeriesPrivate'
  #  The part of Qt it is of, as another part has a class of its name too.
  __qt_part__ = 'QtGraphs'

  #  A C++ QScatter3DSeriesPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QScatter3DSeriesPrivate'

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
    Calls Qt's 'void QScatter3DSeriesPrivate::setDataProxy(QAbstractDataProxy
    *proxy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscatter3dseriesprivate.html#setDataProxy

    Parameters
    ----------

    proxy : Optional[QAbstractDataProxy]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QScatter3DSeriesPrivate::setDataProxy(QAbstractDataProxy *proxy)
    ritual = (
        'ritual_ZN23QScatter3DSeriesPrivate12setDataProxyEP18QAbstractDataP'
        'roxy')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN23QScatter3DSeriesPrivate12setDataProxyEP18QAbstrac'
          'tDataProxy')
    self.uglySide.call(ritual, self._addressOf(proxy))

  @overload(int)
  def setSelectedItem(self, index: int) -> None:
    """
    Calls Qt's 'void QScatter3DSeriesPrivate::setSelectedItem(qsizetype
    index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscatter3dseriesprivate.html#setSelectedItem

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QScatter3DSeriesPrivate::setSelectedItem(qsizetype index)
    self.uglySide.call(
        'ritual_ZN23QScatter3DSeriesPrivate15setSelectedItemEx', index,
    )

  @overload(float)
  def setItemSize(self, size: float) -> None:
    """
    Calls Qt's 'void QScatter3DSeriesPrivate::setItemSize(float size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscatter3dseriesprivate.html#setItemSize

    Parameters
    ----------

    size : float
      Passed on as it is.
    """
    #  void QScatter3DSeriesPrivate::setItemSize(float size)
    self.uglySide.call(
        'ritual_ZN23QScatter3DSeriesPrivate11setItemSizeEf', size,
    )

  @overload(QList[QScatterDataItem])
  def setDataArray(self, newDataArray: QList[QScatterDataItem]) -> None:
    """
    Calls Qt's 'void QScatter3DSeriesPrivate::setDataArray(const
    QScatterDataArray &newDataArray)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscatter3dseriesprivate.html#setDataArray

    Parameters
    ----------

    newDataArray : QList[QScatterDataItem]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QScatter3DSeriesPrivate::setDataArray(const QScatterDataArray
    #      &newDataArray)
    self.uglySide.call(
        'ritual_ZN23QScatter3DSeriesPrivate12setDataArrayERK5QListI16QScatt'
        'erDataItemE',
        self._valueOf(newDataArray),
    )

  @overload(QList[QVector3D])
  def setScaleArray(self, newScaleArray: QList[QVector3D]) -> None:
    """
    Calls Qt's 'void QScatter3DSeriesPrivate::setScaleArray(const
    QList<QVector3D> &newScaleArray)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscatter3dseriesprivate.html#setScaleArray

    Parameters
    ----------

    newScaleArray : QList[QVector3D]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QScatter3DSeriesPrivate::setScaleArray(const QList<QVector3D>
    #      &newScaleArray)
    self.uglySide.call(
        'ritual_ZN23QScatter3DSeriesPrivate13setScaleArrayERK5QListI9QVecto'
        'r3DE',
        self._valueOf(newScaleArray),
    )

  @overload(QValue3DAxis)
  @overload(NoneType)
  def setAxisX(self, axis: Optional[QValue3DAxis]) -> None:
    """
    Calls Qt's 'void QScatter3DSeriesPrivate::setAxisX(QValue3DAxis *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscatter3dseriesprivate.html#setAxisX

    Parameters
    ----------

    axis : Optional[QValue3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QScatter3DSeriesPrivate::setAxisX(QValue3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN23QScatter3DSeriesPrivate8setAxisXEP12QValue3DAxis',
        self._addressOf(axis),
    )

  @overload(QValue3DAxis)
  @overload(NoneType)
  def setAxisY(self, axis: Optional[QValue3DAxis]) -> None:
    """
    Calls Qt's 'void QScatter3DSeriesPrivate::setAxisY(QValue3DAxis *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscatter3dseriesprivate.html#setAxisY

    Parameters
    ----------

    axis : Optional[QValue3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QScatter3DSeriesPrivate::setAxisY(QValue3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN23QScatter3DSeriesPrivate8setAxisYEP12QValue3DAxis',
        self._addressOf(axis),
    )

  @overload(QValue3DAxis)
  @overload(NoneType)
  def setAxisZ(self, axis: Optional[QValue3DAxis]) -> None:
    """
    Calls Qt's 'void QScatter3DSeriesPrivate::setAxisZ(QValue3DAxis *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscatter3dseriesprivate.html#setAxisZ

    Parameters
    ----------

    axis : Optional[QValue3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QScatter3DSeriesPrivate::setAxisZ(QValue3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN23QScatter3DSeriesPrivate8setAxisZEP12QValue3DAxis',
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
    'QScatter3DSeriesPrivate::QScatter3DSeriesPrivate()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qscatter3dseriesprivate.html
    """
    #  QScatter3DSeriesPrivate::QScatter3DSeriesPrivate()
    self._noteCreation(QScatter3DSeriesPrivate, lambda: Rituals.call(
        'ritual_ZN23QScatter3DSeriesPrivateC1Ev',
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

  def q_func(self) -> Optional[QScatter3DSeries]:
    """
    Calls Qt's 'QScatter3DSeries *QScatter3DSeriesPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscatter3dseriesprivate.html#q_func

    Returns
    -------

    Optional[QScatter3DSeries]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QScatter3DSeries *QScatter3DSeriesPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN23QScatter3DSeriesPrivate6q_funcEv',
    )
    from . import QScatter3DSeries
    return QScatter3DSeries._cuteAt(address)

  @overload(QQuickGraphsItem)
  @overload(NoneType)
  def connectGraphAndProxy(
      self,
      newGraph: Optional[QQuickGraphsItem],
  ) -> None:
    """
    Calls Qt's 'void
    QScatter3DSeriesPrivate::connectGraphAndProxy(QQuickGraphsItem
    *newGraph)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscatter3dseriesprivate.html#connectGraphAndProxy

    Parameters
    ----------

    newGraph : Optional[QQuickGraphsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QScatter3DSeriesPrivate::connectGraphAndProxy(QQuickGraphsItem
    #      *newGraph)
    ritual = (
        'ritual_ZN23QScatter3DSeriesPrivate20connectGraphAndProxyEP16QQuick'
        'GraphsItem')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN23QScatter3DSeriesPrivate20connectGraphAndProxyEP16'
          'QQuickGraphsItem')
    self.uglySide.call(ritual, self._addressOf(newGraph))

  def createItemLabel(self) -> None:
    """
    Calls Qt's 'void QScatter3DSeriesPrivate::createItemLabel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscatter3dseriesprivate.html#createItemLabel
    """
    #  void QScatter3DSeriesPrivate::createItemLabel()
    ritual = 'ritual_ZN23QScatter3DSeriesPrivate15createItemLabelEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN23QScatter3DSeriesPrivate15createItemLabelEv'
    self.uglySide.call(ritual)

  def clearArray(self) -> None:
    """
    Calls Qt's 'void QScatter3DSeriesPrivate::clearArray()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscatter3dseriesprivate.html#clearArray
    """
    #  void QScatter3DSeriesPrivate::clearArray()
    self.uglySide.call('ritual_ZN23QScatter3DSeriesPrivate10clearArrayEv')

  def clearScaleArray(self) -> None:
    """
    Calls Qt's 'void QScatter3DSeriesPrivate::clearScaleArray()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscatter3dseriesprivate.html#clearScaleArray
    """
    #  void QScatter3DSeriesPrivate::clearScaleArray()
    self.uglySide.call(
        'ritual_ZN23QScatter3DSeriesPrivate15clearScaleArrayEv',
    )

  def resetAxisX(self) -> None:
    """
    Calls Qt's 'void QScatter3DSeriesPrivate::resetAxisX()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscatter3dseriesprivate.html#resetAxisX
    """
    #  void QScatter3DSeriesPrivate::resetAxisX()
    self.uglySide.call('ritual_ZN23QScatter3DSeriesPrivate10resetAxisXEv')

  def resetAxisY(self) -> None:
    """
    Calls Qt's 'void QScatter3DSeriesPrivate::resetAxisY()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscatter3dseriesprivate.html#resetAxisY
    """
    #  void QScatter3DSeriesPrivate::resetAxisY()
    self.uglySide.call('ritual_ZN23QScatter3DSeriesPrivate10resetAxisYEv')

  def resetAxisZ(self) -> None:
    """
    Calls Qt's 'void QScatter3DSeriesPrivate::resetAxisZ()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscatter3dseriesprivate.html#resetAxisZ
    """
    #  void QScatter3DSeriesPrivate::resetAxisZ()
    self.uglySide.call('ritual_ZN23QScatter3DSeriesPrivate10resetAxisZEv')
