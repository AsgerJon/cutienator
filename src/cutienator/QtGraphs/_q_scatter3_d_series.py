"""
QScatter3DSeries binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGraphs/qscatter3dseries.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject
from . import QAbstract3DSeries

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QVector3D
  from . import QScatter3DSeriesPrivate, QScatterDataItem, QScatterDataProxy
  from . import QValue3DAxis
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QScatterDataItem = WAIT['QtGraphs:QScatterDataItem']
  QScatterDataProxy = WAIT['QtGraphs:QScatterDataProxy']
  QValue3DAxis = WAIT['QtGraphs:QValue3DAxis']
  QVector3D = WAIT['QVector3D']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QScatter3DSeries(QAbstract3DSeries):
  """
  The cute side of Qt's QScatter3DSeries: a plain Python object standing in
  front of one C++ QScatter3DSeries.

  It is built on the cute 'QAbstract3DSeries', as Qt's QScatter3DSeries is
  built on Qt's QAbstract3DSeries, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QScatter3DSeries that has a ritual and that Python
  can call so far, 33 names in all: 'metaObject', 'tr', 'd_func',
  'setDataProxy', 'dataProxy', 'setSelectedItem', 'selectedItem',
  'invalidSelectionIndex', 'setItemSize', 'itemSize', 'setDataArray',
  'clearArray', 'dataArray', 'setScaleArray', 'clearScaleArray',
  'scaleArray', 'setAxisX', 'setAxisY', 'setAxisZ', 'axisX', 'axisY',
  'axisZ', 'resetAxisX', 'resetAxisY', 'resetAxisZ', 'dataProxyChanged',
  'selectedItemChanged', 'itemSizeChanged', 'dataArrayChanged',
  'scaleArrayChanged', 'axisXChanged', 'axisYChanged', 'axisZChanged'. It can
  be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QScatter3DSeries::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QScatter3DSeries::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'const QScatter3DSeriesPrivate *QScatter3DSeries::d_func() const':
    takes in Python what 'QScatter3DSeriesPrivate
    *QScatter3DSeries::d_func()' takes.
  - Qt's 'void QScatter3DSeries::qt_qmlMarker_uncreatable()': one of Qt's own
    inner workings.
  - Qt's 'QScatter3DSeries::~QScatter3DSeries()': the destructor: Python
    never removes a C++ QScatter3DSeries.
  - Qt's 'QScatter3DSeries::QScatter3DSeries(QScatter3DSeriesPrivate &d,
    QObject *parent)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  6 of the 47 functions Qt declares: 4 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QScatter3DSeries is created at the first use, not by
    'QScatter3DSeries(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QScatter3DSeries.
  - Qt tells when it has removed the C++ QScatter3DSeries. Every call on the
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
    Calls Qt's 'QString QScatter3DSeries::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qscatter3dseries.html#tr

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
    #  QString QScatter3DSeries::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN16QScatter3DSeries2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def invalidSelectionIndex() -> int:
    """
    Calls Qt's 'qsizetype QScatter3DSeries::invalidSelectionIndex()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscatter3dseries.html#invalidSelectionIndex
    """
    #  qsizetype QScatter3DSeries::invalidSelectionIndex()
    return Rituals.call(
        'ritual_ZN16QScatter3DSeries21invalidSelectionIndexEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QScatter3DSeries'
  #  The part of Qt it is of, as another part has a class of its name too.
  __qt_part__ = 'QtGraphs'

  #  A C++ QScatter3DSeries Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QScatter3DSeries'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QScatter3DSeries::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscatter3dseries.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QScatter3DSeries::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QScatter3DSeries10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def dataProxy(self) -> Optional[QScatterDataProxy]:
    """
    Calls Qt's 'QScatterDataProxy *QScatter3DSeries::dataProxy() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscatter3dseries.html#dataProxy

    Returns
    -------

    Optional[QScatterDataProxy]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QScatterDataProxy *QScatter3DSeries::dataProxy() const
    address = self.uglySide.call('ritual_ZNK16QScatter3DSeries9dataProxyEv')
    from . import QScatterDataProxy
    return QScatterDataProxy._cuteAt(address)

  def selectedItem(self) -> int:
    """
    Calls Qt's 'qsizetype QScatter3DSeries::selectedItem() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscatter3dseries.html#selectedItem
    """
    #  qsizetype QScatter3DSeries::selectedItem() const
    return self.uglySide.call('ritual_ZNK16QScatter3DSeries12selectedItemEv')

  def itemSize(self) -> float:
    """
    Calls Qt's 'float QScatter3DSeries::itemSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscatter3dseries.html#itemSize
    """
    #  float QScatter3DSeries::itemSize() const
    return self.uglySide.call('ritual_ZNK16QScatter3DSeries8itemSizeEv')

  def dataArray(self) -> QList[QScatterDataItem]:
    """
    Calls Qt's 'const QScatterDataArray &QScatter3DSeries::dataArray()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qscatter3dseries.html#dataArray

    Returns
    -------

    QList[QScatterDataItem]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  const QScatterDataArray &QScatter3DSeries::dataArray() const
    address = self.uglySide.call('ritual_ZNKR16QScatter3DSeries9dataArrayEv')
    from . import QScatterDataItem
    return QList[QScatterDataItem]._cuteOwning(address)

  def scaleArray(self) -> QList[QVector3D]:
    """
    Calls Qt's 'const QList<QVector3D> &QScatter3DSeries::scaleArray()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qscatter3dseries.html#scaleArray

    Returns
    -------

    QList[QVector3D]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  const QList<QVector3D> &QScatter3DSeries::scaleArray() const
    address = self.uglySide.call(
        'ritual_ZNKR16QScatter3DSeries10scaleArrayEv',
    )
    from ..QtGui import QVector3D
    return QList[QVector3D]._cuteOwning(address)

  def axisX(self) -> Optional[QValue3DAxis]:
    """
    Calls Qt's 'QValue3DAxis *QScatter3DSeries::axisX() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscatter3dseries.html#axisX

    Returns
    -------

    Optional[QValue3DAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QValue3DAxis *QScatter3DSeries::axisX() const
    address = self.uglySide.call('ritual_ZNK16QScatter3DSeries5axisXEv')
    from . import QValue3DAxis
    return QValue3DAxis._cuteAt(address)

  def axisY(self) -> Optional[QValue3DAxis]:
    """
    Calls Qt's 'QValue3DAxis *QScatter3DSeries::axisY() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscatter3dseries.html#axisY

    Returns
    -------

    Optional[QValue3DAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QValue3DAxis *QScatter3DSeries::axisY() const
    address = self.uglySide.call('ritual_ZNK16QScatter3DSeries5axisYEv')
    from . import QValue3DAxis
    return QValue3DAxis._cuteAt(address)

  def axisZ(self) -> Optional[QValue3DAxis]:
    """
    Calls Qt's 'QValue3DAxis *QScatter3DSeries::axisZ() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscatter3dseries.html#axisZ

    Returns
    -------

    Optional[QValue3DAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QValue3DAxis *QScatter3DSeries::axisZ() const
    address = self.uglySide.call('ritual_ZNK16QScatter3DSeries5axisZEv')
    from . import QValue3DAxis
    return QValue3DAxis._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QScatterDataProxy)
  @overload(NoneType)
  def setDataProxy(self, proxy: Optional[QScatterDataProxy]) -> None:
    """
    Calls Qt's 'void QScatter3DSeries::setDataProxy(QScatterDataProxy
    *proxy)'.

    Qt's own words: https://doc.qt.io/qt-6/qscatter3dseries.html#setDataProxy

    Parameters
    ----------

    proxy : Optional[QScatterDataProxy]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QScatter3DSeries::setDataProxy(QScatterDataProxy *proxy)
    self.uglySide.call(
        'ritual_ZN16QScatter3DSeries12setDataProxyEP17QScatterDataProxy',
        self._addressOf(proxy),
    )

  @overload(int)
  def setSelectedItem(self, index: int) -> None:
    """
    Calls Qt's 'void QScatter3DSeries::setSelectedItem(qsizetype index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscatter3dseries.html#setSelectedItem

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QScatter3DSeries::setSelectedItem(qsizetype index)
    self.uglySide.call(
        'ritual_ZN16QScatter3DSeries15setSelectedItemEx', index,
    )

  @overload(float)
  def setItemSize(self, size: float) -> None:
    """
    Calls Qt's 'void QScatter3DSeries::setItemSize(float size)'.

    Qt's own words: https://doc.qt.io/qt-6/qscatter3dseries.html#setItemSize

    Parameters
    ----------

    size : float
      Passed on as it is.
    """
    #  void QScatter3DSeries::setItemSize(float size)
    self.uglySide.call('ritual_ZN16QScatter3DSeries11setItemSizeEf', size)

  @overload(QList[QScatterDataItem])
  def setDataArray(self, newDataArray: QList[QScatterDataItem]) -> None:
    """
    Calls Qt's 'void QScatter3DSeries::setDataArray(const QScatterDataArray
    &newDataArray)'.

    Qt's own words: https://doc.qt.io/qt-6/qscatter3dseries.html#setDataArray

    Parameters
    ----------

    newDataArray : QList[QScatterDataItem]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QScatter3DSeries::setDataArray(const QScatterDataArray
    #      &newDataArray)
    self.uglySide.call(
        'ritual_ZN16QScatter3DSeries12setDataArrayERK5QListI16QScatterDataI'
        'temE',
        self._valueOf(newDataArray),
    )

  @overload(QList[QVector3D])
  def setScaleArray(self, newScaleArray: QList[QVector3D]) -> None:
    """
    Calls Qt's 'void QScatter3DSeries::setScaleArray(const QList<QVector3D>
    &newScaleArray)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscatter3dseries.html#setScaleArray

    Parameters
    ----------

    newScaleArray : QList[QVector3D]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QScatter3DSeries::setScaleArray(const QList<QVector3D>
    #      &newScaleArray)
    self.uglySide.call(
        'ritual_ZN16QScatter3DSeries13setScaleArrayERK5QListI9QVector3DE',
        self._valueOf(newScaleArray),
    )

  @overload(QValue3DAxis)
  @overload(NoneType)
  def setAxisX(self, axis: Optional[QValue3DAxis]) -> None:
    """
    Calls Qt's 'void QScatter3DSeries::setAxisX(QValue3DAxis *axis)'.

    Qt's own words: https://doc.qt.io/qt-6/qscatter3dseries.html#setAxisX

    Parameters
    ----------

    axis : Optional[QValue3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QScatter3DSeries::setAxisX(QValue3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN16QScatter3DSeries8setAxisXEP12QValue3DAxis',
        self._addressOf(axis),
    )

  @overload(QValue3DAxis)
  @overload(NoneType)
  def setAxisY(self, axis: Optional[QValue3DAxis]) -> None:
    """
    Calls Qt's 'void QScatter3DSeries::setAxisY(QValue3DAxis *axis)'.

    Qt's own words: https://doc.qt.io/qt-6/qscatter3dseries.html#setAxisY

    Parameters
    ----------

    axis : Optional[QValue3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QScatter3DSeries::setAxisY(QValue3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN16QScatter3DSeries8setAxisYEP12QValue3DAxis',
        self._addressOf(axis),
    )

  @overload(QValue3DAxis)
  @overload(NoneType)
  def setAxisZ(self, axis: Optional[QValue3DAxis]) -> None:
    """
    Calls Qt's 'void QScatter3DSeries::setAxisZ(QValue3DAxis *axis)'.

    Qt's own words: https://doc.qt.io/qt-6/qscatter3dseries.html#setAxisZ

    Parameters
    ----------

    axis : Optional[QValue3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QScatter3DSeries::setAxisZ(QValue3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN16QScatter3DSeries8setAxisZEP12QValue3DAxis',
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

  @overload(QScatterDataProxy)
  @overload(QScatterDataProxy, QObject)
  @overload(QScatterDataProxy, NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      dataProxy: Optional[QScatterDataProxy],
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QScatter3DSeries::QScatter3DSeries(QScatterDataProxy *dataProxy, QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qscatter3dseries.html#QScatter3DSeries

    Parameters
    ----------

    dataProxy : Optional[QScatterDataProxy]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QScatter3DSeries::QScatter3DSeries(QScatterDataProxy *dataProxy,
    #      QObject *parent)
    self._noteCreation(QScatter3DSeries, lambda: Rituals.call(
        'ritual_ZN16QScatter3DSeriesC1EP17QScatterDataProxyP7QObject',
        self._addressOf(dataProxy), self._addressOf(parent, 'QObject'),
    ))

  @overload()
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QScatter3DSeries::QScatter3DSeries(QObject *parent)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qscatter3dseries.html#QScatter3DSeries

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QScatter3DSeries::QScatter3DSeries(QObject *parent)
    self._noteCreation(QScatter3DSeries, lambda: Rituals.call(
        'ritual_ZN16QScatter3DSeriesC1EP7QObject',
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

  def d_func(self) -> Optional[QScatter3DSeriesPrivate]:
    """
    Calls Qt's 'QScatter3DSeriesPrivate *QScatter3DSeries::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qscatter3dseries.html#d_func

    Returns
    -------

    Optional[QScatter3DSeriesPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QScatter3DSeriesPrivate *QScatter3DSeries::d_func()
    address = self.uglySide.call('ritual_ZN16QScatter3DSeries6d_funcEv')
    from . import QScatter3DSeriesPrivate
    return QScatter3DSeriesPrivate._cuteAt(address)

  def clearArray(self) -> None:
    """
    Calls Qt's 'void QScatter3DSeries::clearArray()'.

    Qt's own words: https://doc.qt.io/qt-6/qscatter3dseries.html#clearArray
    """
    #  void QScatter3DSeries::clearArray()
    self.uglySide.call('ritual_ZN16QScatter3DSeries10clearArrayEv')

  def clearScaleArray(self) -> None:
    """
    Calls Qt's 'void QScatter3DSeries::clearScaleArray()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscatter3dseries.html#clearScaleArray
    """
    #  void QScatter3DSeries::clearScaleArray()
    self.uglySide.call('ritual_ZN16QScatter3DSeries15clearScaleArrayEv')

  def resetAxisX(self) -> None:
    """
    Calls Qt's 'void QScatter3DSeries::resetAxisX()'.

    Qt's own words: https://doc.qt.io/qt-6/qscatter3dseries.html#resetAxisX
    """
    #  void QScatter3DSeries::resetAxisX()
    self.uglySide.call('ritual_ZN16QScatter3DSeries10resetAxisXEv')

  def resetAxisY(self) -> None:
    """
    Calls Qt's 'void QScatter3DSeries::resetAxisY()'.

    Qt's own words: https://doc.qt.io/qt-6/qscatter3dseries.html#resetAxisY
    """
    #  void QScatter3DSeries::resetAxisY()
    self.uglySide.call('ritual_ZN16QScatter3DSeries10resetAxisYEv')

  def resetAxisZ(self) -> None:
    """
    Calls Qt's 'void QScatter3DSeries::resetAxisZ()'.

    Qt's own words: https://doc.qt.io/qt-6/qscatter3dseries.html#resetAxisZ
    """
    #  void QScatter3DSeries::resetAxisZ()
    self.uglySide.call('ritual_ZN16QScatter3DSeries10resetAxisZEv')

  @overload(QScatterDataProxy)
  @overload(NoneType)
  def dataProxyChanged(self, proxy: Optional[QScatterDataProxy]) -> None:
    """
    Calls Qt's 'void QScatter3DSeries::dataProxyChanged(QScatterDataProxy
    *proxy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscatter3dseries.html#dataProxyChanged

    Parameters
    ----------

    proxy : Optional[QScatterDataProxy]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QScatter3DSeries::dataProxyChanged(QScatterDataProxy *proxy)
    self.uglySide.call(
        'ritual_ZN16QScatter3DSeries16dataProxyChangedEP17QScatterDataProxy',
        self._addressOf(proxy),
    )

  @overload(int)
  def selectedItemChanged(self, index: int) -> None:
    """
    Calls Qt's 'void QScatter3DSeries::selectedItemChanged(qsizetype index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscatter3dseries.html#selectedItemChanged

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QScatter3DSeries::selectedItemChanged(qsizetype index)
    self.uglySide.call(
        'ritual_ZN16QScatter3DSeries19selectedItemChangedEx', index,
    )

  @overload(float)
  def itemSizeChanged(self, size: float) -> None:
    """
    Calls Qt's 'void QScatter3DSeries::itemSizeChanged(float size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscatter3dseries.html#itemSizeChanged

    Parameters
    ----------

    size : float
      Passed on as it is.
    """
    #  void QScatter3DSeries::itemSizeChanged(float size)
    self.uglySide.call(
        'ritual_ZN16QScatter3DSeries15itemSizeChangedEf', size,
    )

  @overload(QList[QScatterDataItem])
  def dataArrayChanged(self, array: QList[QScatterDataItem]) -> None:
    """
    Calls Qt's 'void QScatter3DSeries::dataArrayChanged(const
    QScatterDataArray &array)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscatter3dseries.html#dataArrayChanged

    Parameters
    ----------

    array : QList[QScatterDataItem]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QScatter3DSeries::dataArrayChanged(const QScatterDataArray
    #      &array)
    self.uglySide.call(
        'ritual_ZN16QScatter3DSeries16dataArrayChangedERK5QListI16QScatterD'
        'ataItemE',
        self._valueOf(array),
    )

  @overload(QList[QVector3D])
  def scaleArrayChanged(self, scaleArray: QList[QVector3D]) -> None:
    """
    Calls Qt's 'void QScatter3DSeries::scaleArrayChanged(const
    QList<QVector3D> &scaleArray)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscatter3dseries.html#scaleArrayChanged

    Parameters
    ----------

    scaleArray : QList[QVector3D]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QScatter3DSeries::scaleArrayChanged(const QList<QVector3D>
    #      &scaleArray)
    self.uglySide.call(
        'ritual_ZN16QScatter3DSeries17scaleArrayChangedERK5QListI9QVector3D'
        'E',
        self._valueOf(scaleArray),
    )

  @overload(QValue3DAxis)
  @overload(NoneType)
  def axisXChanged(self, axis: Optional[QValue3DAxis]) -> None:
    """
    Calls Qt's 'void QScatter3DSeries::axisXChanged(QValue3DAxis *axis)'.

    Qt's own words: https://doc.qt.io/qt-6/qscatter3dseries.html#axisXChanged

    Parameters
    ----------

    axis : Optional[QValue3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QScatter3DSeries::axisXChanged(QValue3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN16QScatter3DSeries12axisXChangedEP12QValue3DAxis',
        self._addressOf(axis),
    )

  @overload(QValue3DAxis)
  @overload(NoneType)
  def axisYChanged(self, axis: Optional[QValue3DAxis]) -> None:
    """
    Calls Qt's 'void QScatter3DSeries::axisYChanged(QValue3DAxis *axis)'.

    Qt's own words: https://doc.qt.io/qt-6/qscatter3dseries.html#axisYChanged

    Parameters
    ----------

    axis : Optional[QValue3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QScatter3DSeries::axisYChanged(QValue3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN16QScatter3DSeries12axisYChangedEP12QValue3DAxis',
        self._addressOf(axis),
    )

  @overload(QValue3DAxis)
  @overload(NoneType)
  def axisZChanged(self, axis: Optional[QValue3DAxis]) -> None:
    """
    Calls Qt's 'void QScatter3DSeries::axisZChanged(QValue3DAxis *axis)'.

    Qt's own words: https://doc.qt.io/qt-6/qscatter3dseries.html#axisZChanged

    Parameters
    ----------

    axis : Optional[QValue3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QScatter3DSeries::axisZChanged(QValue3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN16QScatter3DSeries12axisZChangedEP12QValue3DAxis',
        self._addressOf(axis),
    )


#  Qt's 'QList<QScatter3DSeries *>': the list of QScatter3DSeries, which
#  'QList[QScatter3DSeries]' gives. It is made here, so that there is one as
#  soon as there can be a QScatter3DSeries.
QList.createKind(
    QScatter3DSeries, 'address',
    make='ritual_list_make_QScatter3DSeries_ptr',
    add='ritual_list_add_QScatter3DSeries_ptr',
    size='ritual_list_size_QScatter3DSeries_ptr',
    at='ritual_list_at_QScatter3DSeries_ptr',
    drop='ritual_list_drop_QScatter3DSeries_ptr',
)
