"""
QBar3DSeries binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGraphs/qbar3dseries.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject, QStringList
from . import QAbstract3DSeries

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QPoint
  from ..QtGui import QColor, QQuaternion
  from . import QBar3DSeriesPrivate, QBarDataProxy, QCategory3DAxis
  from . import QValue3DAxis
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QBarDataProxy = WAIT['QtGraphs:QBarDataProxy']
  QCategory3DAxis = WAIT['QtGraphs:QCategory3DAxis']
  QColor = WAIT['QColor']
  QPoint = WAIT['QPoint']
  QQuaternion = WAIT['QQuaternion']
  QValue3DAxis = WAIT['QtGraphs:QValue3DAxis']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QBar3DSeries(QAbstract3DSeries):
  """
  The cute side of Qt's QBar3DSeries: a plain Python object standing in front
  of one C++ QBar3DSeries.

  It is built on the cute 'QAbstract3DSeries', as Qt's QBar3DSeries is built
  on Qt's QAbstract3DSeries, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QBar3DSeries that has a ritual and that Python can
  call so far, 47 names in all: 'metaObject', 'tr', 'd_func', 'setDataProxy',
  'dataProxy', 'setSelectedBar', 'selectedBar', 'invalidSelectionPosition',
  'setMeshAngle', 'meshAngle', 'rowColors', 'setRowColors',
  'isValueColoringEnabled', 'setValueColoringEnabled', 'clearRow',
  'clearArray', 'rowLabels', 'setRowLabels', 'columnLabels',
  'setColumnLabels', 'customRowLabels', 'setCustomRowLabels',
  'customColumnLabels', 'setCustomColumnLabels', 'setRowAxis',
  'setValueAxis', 'setColumnAxis', 'rowAxis', 'valueAxis', 'columnAxis',
  'resetRowAxis', 'resetValueAxis', 'resetColumnAxis', 'dataProxyChanged',
  'selectedBarChanged', 'meshAngleChanged', 'rowColorsChanged',
  'rowLabelsChanged', 'columnLabelsChanged', 'valueColoringEnabledChanged',
  'customRowLabelsChanged', 'customColumnLabelsChanged', 'rowAxisChanged',
  'valueAxisChanged', 'columnAxisChanged', 'connectSignals',
  'handleMeshRotationChanged'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QBar3DSeries::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QBar3DSeries::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'const QBar3DSeriesPrivate *QBar3DSeries::d_func() const': takes in
    Python what 'QBar3DSeriesPrivate *QBar3DSeries::d_func()' takes.
  - Qt's 'void QBar3DSeries::qt_qmlMarker_uncreatable()': one of Qt's own
    inner workings.
  - Qt's 'QBar3DSeries::~QBar3DSeries()': the destructor: Python never
    removes a C++ QBar3DSeries.
  - Qt's 'void QBar3DSeries::setDataArray(const QBarDataArray
    &newDataArray)': takes a type Python has no way to hand over yet.
  - Qt's 'const QBarDataArray &QBar3DSeries::dataArray() const': gives a type
    Python has no way to take yet.
  - Qt's 'void QBar3DSeries::dataArrayChanged(const QBarDataArray &array)':
    takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  5 of the 62 functions Qt declares: 3 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QBar3DSeries is created at the first use, not by
    'QBar3DSeries(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QBar3DSeries.
  - Qt tells when it has removed the C++ QBar3DSeries. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's QBar3DSeries that has no cute function yet,
    'dataArray', 'dataArrayChanged', 'setDataArray', holds a function that
    raises 'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString QBar3DSeries::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qbar3dseries.html#tr

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
    #  QString QBar3DSeries::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN12QBar3DSeries2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def invalidSelectionPosition() -> QPoint:
    """
    Calls Qt's 'QPoint QBar3DSeries::invalidSelectionPosition()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbar3dseries.html#invalidSelectionPosition

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QBar3DSeries::invalidSelectionPosition()
    address = Rituals.call(
        'ritual_ZN12QBar3DSeries24invalidSelectionPositionEv',
    )
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QBar3DSeries'
  #  The part of Qt it is of, as another part has a class of its name too.
  __qt_part__ = 'QtGraphs'

  #  A C++ QBar3DSeries Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QBar3DSeries'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QBar3DSeries::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbar3dseries.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QBar3DSeries::metaObject() const
    address = self.uglySide.call('ritual_ZNK12QBar3DSeries10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def dataProxy(self) -> Optional[QBarDataProxy]:
    """
    Calls Qt's 'QBarDataProxy *QBar3DSeries::dataProxy() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbar3dseries.html#dataProxy

    Returns
    -------

    Optional[QBarDataProxy]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QBarDataProxy *QBar3DSeries::dataProxy() const
    address = self.uglySide.call('ritual_ZNK12QBar3DSeries9dataProxyEv')
    from . import QBarDataProxy
    return QBarDataProxy._cuteAt(address)

  def selectedBar(self) -> QPoint:
    """
    Calls Qt's 'QPoint QBar3DSeries::selectedBar() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbar3dseries.html#selectedBar

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QBar3DSeries::selectedBar() const
    address = self.uglySide.call('ritual_ZNK12QBar3DSeries11selectedBarEv')
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  def meshAngle(self) -> float:
    """
    Calls Qt's 'float QBar3DSeries::meshAngle() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbar3dseries.html#meshAngle
    """
    #  float QBar3DSeries::meshAngle() const
    return self.uglySide.call('ritual_ZNK12QBar3DSeries9meshAngleEv')

  def rowColors(self) -> QList[QColor]:
    """
    Calls Qt's 'QList<QColor> QBar3DSeries::rowColors() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbar3dseries.html#rowColors

    Returns
    -------

    QList[QColor]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QColor> QBar3DSeries::rowColors() const
    address = self.uglySide.call('ritual_ZNK12QBar3DSeries9rowColorsEv')
    from ..QtGui import QColor
    return QList[QColor]._cuteOwning(address)

  def isValueColoringEnabled(self) -> bool:
    """
    Calls Qt's 'bool QBar3DSeries::isValueColoringEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbar3dseries.html#isValueColoringEnabled
    """
    #  bool QBar3DSeries::isValueColoringEnabled() const
    return self.uglySide.call(
        'ritual_ZNK12QBar3DSeries22isValueColoringEnabledEv',
    )

  def rowLabels(self) -> QStringList:
    """
    Calls Qt's 'QStringList QBar3DSeries::rowLabels() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbar3dseries.html#rowLabels

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QBar3DSeries::rowLabels() const
    address = self.uglySide.call('ritual_ZNK12QBar3DSeries9rowLabelsEv')
    return QStringList._cuteOwning(address)

  def columnLabels(self) -> QStringList:
    """
    Calls Qt's 'QStringList QBar3DSeries::columnLabels() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbar3dseries.html#columnLabels

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QBar3DSeries::columnLabels() const
    address = self.uglySide.call('ritual_ZNK12QBar3DSeries12columnLabelsEv')
    return QStringList._cuteOwning(address)

  def customRowLabels(self) -> QStringList:
    """
    Calls Qt's 'QStringList QBar3DSeries::customRowLabels() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbar3dseries.html#customRowLabels

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QBar3DSeries::customRowLabels() const
    address = self.uglySide.call(
        'ritual_ZNK12QBar3DSeries15customRowLabelsEv',
    )
    return QStringList._cuteOwning(address)

  def customColumnLabels(self) -> QStringList:
    """
    Calls Qt's 'QStringList QBar3DSeries::customColumnLabels() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbar3dseries.html#customColumnLabels

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QBar3DSeries::customColumnLabels() const
    address = self.uglySide.call(
        'ritual_ZNK12QBar3DSeries18customColumnLabelsEv',
    )
    return QStringList._cuteOwning(address)

  def rowAxis(self) -> Optional[QCategory3DAxis]:
    """
    Calls Qt's 'QCategory3DAxis *QBar3DSeries::rowAxis() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbar3dseries.html#rowAxis

    Returns
    -------

    Optional[QCategory3DAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCategory3DAxis *QBar3DSeries::rowAxis() const
    address = self.uglySide.call('ritual_ZNK12QBar3DSeries7rowAxisEv')
    from . import QCategory3DAxis
    return QCategory3DAxis._cuteAt(address)

  def valueAxis(self) -> Optional[QValue3DAxis]:
    """
    Calls Qt's 'QValue3DAxis *QBar3DSeries::valueAxis() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbar3dseries.html#valueAxis

    Returns
    -------

    Optional[QValue3DAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QValue3DAxis *QBar3DSeries::valueAxis() const
    address = self.uglySide.call('ritual_ZNK12QBar3DSeries9valueAxisEv')
    from . import QValue3DAxis
    return QValue3DAxis._cuteAt(address)

  def columnAxis(self) -> Optional[QCategory3DAxis]:
    """
    Calls Qt's 'QCategory3DAxis *QBar3DSeries::columnAxis() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbar3dseries.html#columnAxis

    Returns
    -------

    Optional[QCategory3DAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCategory3DAxis *QBar3DSeries::columnAxis() const
    address = self.uglySide.call('ritual_ZNK12QBar3DSeries10columnAxisEv')
    from . import QCategory3DAxis
    return QCategory3DAxis._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QBarDataProxy)
  @overload(NoneType)
  def setDataProxy(self, proxy: Optional[QBarDataProxy]) -> None:
    """
    Calls Qt's 'void QBar3DSeries::setDataProxy(QBarDataProxy *proxy)'.

    Qt's own words: https://doc.qt.io/qt-6/qbar3dseries.html#setDataProxy

    Parameters
    ----------

    proxy : Optional[QBarDataProxy]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QBar3DSeries::setDataProxy(QBarDataProxy *proxy)
    self.uglySide.call(
        'ritual_ZN12QBar3DSeries12setDataProxyEP13QBarDataProxy',
        self._addressOf(proxy),
    )

  @overload(QPoint)
  def setSelectedBar(self, position: QPoint) -> None:
    """
    Calls Qt's 'void QBar3DSeries::setSelectedBar(QPoint position)'.

    Qt's own words: https://doc.qt.io/qt-6/qbar3dseries.html#setSelectedBar

    Parameters
    ----------

    position : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QBar3DSeries::setSelectedBar(QPoint position)
    self.uglySide.call(
        'ritual_ZN12QBar3DSeries14setSelectedBarE6QPoint',
        self._valueOf(position),
    )

  @overload(float)
  def setMeshAngle(self, angle: float) -> None:
    """
    Calls Qt's 'void QBar3DSeries::setMeshAngle(float angle)'.

    Qt's own words: https://doc.qt.io/qt-6/qbar3dseries.html#setMeshAngle

    Parameters
    ----------

    angle : float
      Passed on as it is.
    """
    #  void QBar3DSeries::setMeshAngle(float angle)
    self.uglySide.call('ritual_ZN12QBar3DSeries12setMeshAngleEf', angle)

  @overload(QList[QColor])
  def setRowColors(self, colors: QList[QColor]) -> None:
    """
    Calls Qt's 'void QBar3DSeries::setRowColors(const QList<QColor>
    &colors)'.

    Qt's own words: https://doc.qt.io/qt-6/qbar3dseries.html#setRowColors

    Parameters
    ----------

    colors : QList[QColor]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QBar3DSeries::setRowColors(const QList<QColor> &colors)
    self.uglySide.call(
        'ritual_ZN12QBar3DSeries12setRowColorsERK5QListI6QColorE',
        self._valueOf(colors),
    )

  @overload(bool)
  def setValueColoringEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QBar3DSeries::setValueColoringEnabled(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbar3dseries.html#setValueColoringEnabled

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QBar3DSeries::setValueColoringEnabled(bool enabled)
    self.uglySide.call(
        'ritual_ZN12QBar3DSeries23setValueColoringEnabledEb', enabled,
    )

  @overload(QStringList)
  def setRowLabels(self, labels: QStringList) -> None:
    """
    Calls Qt's 'void QBar3DSeries::setRowLabels(const QStringList &labels)'.

    Qt's own words: https://doc.qt.io/qt-6/qbar3dseries.html#setRowLabels

    Parameters
    ----------

    labels : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QBar3DSeries::setRowLabels(const QStringList &labels)
    self.uglySide.call(
        'ritual_ZN12QBar3DSeries12setRowLabelsERK5QListI7QStringE',
        self._valueOf(labels),
    )

  @overload(QStringList)
  def setColumnLabels(self, labels: QStringList) -> None:
    """
    Calls Qt's 'void QBar3DSeries::setColumnLabels(const QStringList
    &labels)'.

    Qt's own words: https://doc.qt.io/qt-6/qbar3dseries.html#setColumnLabels

    Parameters
    ----------

    labels : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QBar3DSeries::setColumnLabels(const QStringList &labels)
    self.uglySide.call(
        'ritual_ZN12QBar3DSeries15setColumnLabelsERK5QListI7QStringE',
        self._valueOf(labels),
    )

  @overload(QStringList)
  def setCustomRowLabels(self, labels: QStringList) -> None:
    """
    Calls Qt's 'void QBar3DSeries::setCustomRowLabels(const QStringList
    &labels)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbar3dseries.html#setCustomRowLabels

    Parameters
    ----------

    labels : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QBar3DSeries::setCustomRowLabels(const QStringList &labels)
    self.uglySide.call(
        'ritual_ZN12QBar3DSeries18setCustomRowLabelsERK5QListI7QStringE',
        self._valueOf(labels),
    )

  @overload(QStringList)
  def setCustomColumnLabels(self, labels: QStringList) -> None:
    """
    Calls Qt's 'void QBar3DSeries::setCustomColumnLabels(const QStringList
    &labels)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbar3dseries.html#setCustomColumnLabels

    Parameters
    ----------

    labels : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QBar3DSeries::setCustomColumnLabels(const QStringList &labels)
    self.uglySide.call(
        'ritual_ZN12QBar3DSeries21setCustomColumnLabelsERK5QListI7QStringE',
        self._valueOf(labels),
    )

  @overload(QCategory3DAxis)
  @overload(NoneType)
  def setRowAxis(self, axis: Optional[QCategory3DAxis]) -> None:
    """
    Calls Qt's 'void QBar3DSeries::setRowAxis(QCategory3DAxis *axis)'.

    Qt's own words: https://doc.qt.io/qt-6/qbar3dseries.html#setRowAxis

    Parameters
    ----------

    axis : Optional[QCategory3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QBar3DSeries::setRowAxis(QCategory3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN12QBar3DSeries10setRowAxisEP15QCategory3DAxis',
        self._addressOf(axis),
    )

  @overload(QValue3DAxis)
  @overload(NoneType)
  def setValueAxis(self, axis: Optional[QValue3DAxis]) -> None:
    """
    Calls Qt's 'void QBar3DSeries::setValueAxis(QValue3DAxis *axis)'.

    Qt's own words: https://doc.qt.io/qt-6/qbar3dseries.html#setValueAxis

    Parameters
    ----------

    axis : Optional[QValue3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QBar3DSeries::setValueAxis(QValue3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN12QBar3DSeries12setValueAxisEP12QValue3DAxis',
        self._addressOf(axis),
    )

  @overload(QCategory3DAxis)
  @overload(NoneType)
  def setColumnAxis(self, axis: Optional[QCategory3DAxis]) -> None:
    """
    Calls Qt's 'void QBar3DSeries::setColumnAxis(QCategory3DAxis *axis)'.

    Qt's own words: https://doc.qt.io/qt-6/qbar3dseries.html#setColumnAxis

    Parameters
    ----------

    axis : Optional[QCategory3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QBar3DSeries::setColumnAxis(QCategory3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN12QBar3DSeries13setColumnAxisEP15QCategory3DAxis',
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

  @overload(QBarDataProxy)
  @overload(QBarDataProxy, QObject)
  @overload(QBarDataProxy, NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      dataProxy: Optional[QBarDataProxy],
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QBar3DSeries::QBar3DSeries(QBarDataProxy
    *dataProxy, QObject *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qbar3dseries.html#QBar3DSeries

    Parameters
    ----------

    dataProxy : Optional[QBarDataProxy]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QBar3DSeries::QBar3DSeries(QBarDataProxy *dataProxy, QObject *parent)
    self._noteCreation(QBar3DSeries, lambda: Rituals.call(
        'ritual_ZN12QBar3DSeriesC1EP13QBarDataProxyP7QObject',
        self._addressOf(dataProxy), self._addressOf(parent, 'QObject'),
    ))

  @overload()
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's 'QBar3DSeries::QBar3DSeries(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qbar3dseries.html#QBar3DSeries

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QBar3DSeries::QBar3DSeries(QObject *parent)
    self._noteCreation(QBar3DSeries, lambda: Rituals.call(
        'ritual_ZN12QBar3DSeriesC1EP7QObject',
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

  def d_func(self) -> Optional[QBar3DSeriesPrivate]:
    """
    Calls Qt's 'QBar3DSeriesPrivate *QBar3DSeries::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qbar3dseries.html#d_func

    Returns
    -------

    Optional[QBar3DSeriesPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QBar3DSeriesPrivate *QBar3DSeries::d_func()
    address = self.uglySide.call('ritual_ZN12QBar3DSeries6d_funcEv')
    from . import QBar3DSeriesPrivate
    return QBar3DSeriesPrivate._cuteAt(address)

  @overload(int)
  def clearRow(self, rowIndex: int) -> None:
    """
    Calls Qt's 'void QBar3DSeries::clearRow(qsizetype rowIndex)'.

    Qt's own words: https://doc.qt.io/qt-6/qbar3dseries.html#clearRow

    Parameters
    ----------

    rowIndex : int
      Passed on as it is.
    """
    #  void QBar3DSeries::clearRow(qsizetype rowIndex)
    self.uglySide.call('ritual_ZN12QBar3DSeries8clearRowEx', rowIndex)

  def clearArray(self) -> None:
    """
    Calls Qt's 'void QBar3DSeries::clearArray()'.

    Qt's own words: https://doc.qt.io/qt-6/qbar3dseries.html#clearArray
    """
    #  void QBar3DSeries::clearArray()
    self.uglySide.call('ritual_ZN12QBar3DSeries10clearArrayEv')

  def resetRowAxis(self) -> None:
    """
    Calls Qt's 'void QBar3DSeries::resetRowAxis()'.

    Qt's own words: https://doc.qt.io/qt-6/qbar3dseries.html#resetRowAxis
    """
    #  void QBar3DSeries::resetRowAxis()
    self.uglySide.call('ritual_ZN12QBar3DSeries12resetRowAxisEv')

  def resetValueAxis(self) -> None:
    """
    Calls Qt's 'void QBar3DSeries::resetValueAxis()'.

    Qt's own words: https://doc.qt.io/qt-6/qbar3dseries.html#resetValueAxis
    """
    #  void QBar3DSeries::resetValueAxis()
    self.uglySide.call('ritual_ZN12QBar3DSeries14resetValueAxisEv')

  def resetColumnAxis(self) -> None:
    """
    Calls Qt's 'void QBar3DSeries::resetColumnAxis()'.

    Qt's own words: https://doc.qt.io/qt-6/qbar3dseries.html#resetColumnAxis
    """
    #  void QBar3DSeries::resetColumnAxis()
    self.uglySide.call('ritual_ZN12QBar3DSeries15resetColumnAxisEv')

  @overload(QBarDataProxy)
  @overload(NoneType)
  def dataProxyChanged(self, proxy: Optional[QBarDataProxy]) -> None:
    """
    Calls Qt's 'void QBar3DSeries::dataProxyChanged(QBarDataProxy *proxy)'.

    Qt's own words: https://doc.qt.io/qt-6/qbar3dseries.html#dataProxyChanged

    Parameters
    ----------

    proxy : Optional[QBarDataProxy]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QBar3DSeries::dataProxyChanged(QBarDataProxy *proxy)
    self.uglySide.call(
        'ritual_ZN12QBar3DSeries16dataProxyChangedEP13QBarDataProxy',
        self._addressOf(proxy),
    )

  @overload(QPoint)
  def selectedBarChanged(self, position: QPoint) -> None:
    """
    Calls Qt's 'void QBar3DSeries::selectedBarChanged(QPoint position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbar3dseries.html#selectedBarChanged

    Parameters
    ----------

    position : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QBar3DSeries::selectedBarChanged(QPoint position)
    self.uglySide.call(
        'ritual_ZN12QBar3DSeries18selectedBarChangedE6QPoint',
        self._valueOf(position),
    )

  @overload(float)
  def meshAngleChanged(self, angle: float) -> None:
    """
    Calls Qt's 'void QBar3DSeries::meshAngleChanged(float angle)'.

    Qt's own words: https://doc.qt.io/qt-6/qbar3dseries.html#meshAngleChanged

    Parameters
    ----------

    angle : float
      Passed on as it is.
    """
    #  void QBar3DSeries::meshAngleChanged(float angle)
    self.uglySide.call('ritual_ZN12QBar3DSeries16meshAngleChangedEf', angle)

  @overload(QList[QColor])
  def rowColorsChanged(self, rowcolors: QList[QColor]) -> None:
    """
    Calls Qt's 'void QBar3DSeries::rowColorsChanged(const QList<QColor>
    &rowcolors)'.

    Qt's own words: https://doc.qt.io/qt-6/qbar3dseries.html#rowColorsChanged

    Parameters
    ----------

    rowcolors : QList[QColor]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QBar3DSeries::rowColorsChanged(const QList<QColor> &rowcolors)
    self.uglySide.call(
        'ritual_ZN12QBar3DSeries16rowColorsChangedERK5QListI6QColorE',
        self._valueOf(rowcolors),
    )

  def rowLabelsChanged(self) -> None:
    """
    Calls Qt's 'void QBar3DSeries::rowLabelsChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qbar3dseries.html#rowLabelsChanged
    """
    #  void QBar3DSeries::rowLabelsChanged()
    self.uglySide.call('ritual_ZN12QBar3DSeries16rowLabelsChangedEv')

  def columnLabelsChanged(self) -> None:
    """
    Calls Qt's 'void QBar3DSeries::columnLabelsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbar3dseries.html#columnLabelsChanged
    """
    #  void QBar3DSeries::columnLabelsChanged()
    self.uglySide.call('ritual_ZN12QBar3DSeries19columnLabelsChangedEv')

  @overload(bool)
  def valueColoringEnabledChanged(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QBar3DSeries::valueColoringEnabledChanged(bool
    enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbar3dseries.html#valueColoringEnabledChanged

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QBar3DSeries::valueColoringEnabledChanged(bool enabled)
    self.uglySide.call(
        'ritual_ZN12QBar3DSeries27valueColoringEnabledChangedEb', enabled,
    )

  @overload(QStringList)
  def customRowLabelsChanged(self, newCustomRowLabels: QStringList) -> None:
    """
    Calls Qt's 'void QBar3DSeries::customRowLabelsChanged(const QStringList
    &newCustomRowLabels)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbar3dseries.html#customRowLabelsChanged

    Parameters
    ----------

    newCustomRowLabels : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QBar3DSeries::customRowLabelsChanged(const QStringList
    #      &newCustomRowLabels)
    self.uglySide.call(
        'ritual_ZN12QBar3DSeries22customRowLabelsChangedERK5QListI7QStringE',
        self._valueOf(newCustomRowLabels),
    )

  @overload(QStringList)
  def customColumnLabelsChanged(
      self,
      newCustomColumnLabels: QStringList,
  ) -> None:
    """
    Calls Qt's 'void QBar3DSeries::customColumnLabelsChanged(const
    QStringList &newCustomColumnLabels)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbar3dseries.html#customColumnLabelsChanged

    Parameters
    ----------

    newCustomColumnLabels : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QBar3DSeries::customColumnLabelsChanged(const QStringList
    #      &newCustomColumnLabels)
    self.uglySide.call(
        'ritual_ZN12QBar3DSeries25customColumnLabelsChangedERK5QListI7QStri'
        'ngE',
        self._valueOf(newCustomColumnLabels),
    )

  @overload(QCategory3DAxis)
  @overload(NoneType)
  def rowAxisChanged(self, axis: Optional[QCategory3DAxis]) -> None:
    """
    Calls Qt's 'void QBar3DSeries::rowAxisChanged(QCategory3DAxis *axis)'.

    Qt's own words: https://doc.qt.io/qt-6/qbar3dseries.html#rowAxisChanged

    Parameters
    ----------

    axis : Optional[QCategory3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QBar3DSeries::rowAxisChanged(QCategory3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN12QBar3DSeries14rowAxisChangedEP15QCategory3DAxis',
        self._addressOf(axis),
    )

  @overload(QValue3DAxis)
  @overload(NoneType)
  def valueAxisChanged(self, axis: Optional[QValue3DAxis]) -> None:
    """
    Calls Qt's 'void QBar3DSeries::valueAxisChanged(QValue3DAxis *axis)'.

    Qt's own words: https://doc.qt.io/qt-6/qbar3dseries.html#valueAxisChanged

    Parameters
    ----------

    axis : Optional[QValue3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QBar3DSeries::valueAxisChanged(QValue3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN12QBar3DSeries16valueAxisChangedEP12QValue3DAxis',
        self._addressOf(axis),
    )

  @overload(QCategory3DAxis)
  @overload(NoneType)
  def columnAxisChanged(self, axis: Optional[QCategory3DAxis]) -> None:
    """
    Calls Qt's 'void QBar3DSeries::columnAxisChanged(QCategory3DAxis *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbar3dseries.html#columnAxisChanged

    Parameters
    ----------

    axis : Optional[QCategory3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QBar3DSeries::columnAxisChanged(QCategory3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN12QBar3DSeries17columnAxisChangedEP15QCategory3DAxis',
        self._addressOf(axis),
    )

  def connectSignals(self) -> None:
    """
    Calls Qt's 'void QBar3DSeries::connectSignals()'.

    Qt's own words: https://doc.qt.io/qt-6/qbar3dseries.html#connectSignals
    """
    #  void QBar3DSeries::connectSignals()
    self.uglySide.call('ritual_ZN12QBar3DSeries14connectSignalsEv')

  @overload(QQuaternion)
  def handleMeshRotationChanged(self, rotation: QQuaternion) -> None:
    """
    Calls Qt's 'void QBar3DSeries::handleMeshRotationChanged(const
    QQuaternion &rotation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbar3dseries.html#handleMeshRotationChanged

    Parameters
    ----------

    rotation : QQuaternion
      Passed on as a value: Qt reads the C++ QQuaternion, which stays
      Python's own.
    """
    #  void QBar3DSeries::handleMeshRotationChanged(const QQuaternion
    #      &rotation)
    self.uglySide.call(
        'ritual_ZN12QBar3DSeries25handleMeshRotationChangedERK11QQuaternion',
        self._valueOf(rotation),
    )

  @staticmethod
  def dataArray(*__, **_) -> Never:
    """
    Qt's 'const QBarDataArray &QBar3DSeries::dataArray() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QBar3DSeries.dataArray' has no cute function yet. Qt's 'const "
        "QBarDataArray &QBar3DSeries::dataArray() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def dataArrayChanged(*__, **_) -> Never:
    """
    Qt's 'void QBar3DSeries::dataArrayChanged(const QBarDataArray &array)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QBar3DSeries.dataArrayChanged' has no cute function yet. Qt's "
        "'void QBar3DSeries::dataArrayChanged(const QBarDataArray &array)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def setDataArray(*__, **_) -> Never:
    """
    Qt's 'void QBar3DSeries::setDataArray(const QBarDataArray
    &newDataArray)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QBar3DSeries.setDataArray' has no cute function yet. Qt's 'void "
        "QBar3DSeries::setDataArray(const QBarDataArray &newDataArray)': "
        "takes a type Python has no way to hand over yet.")


#  Qt's 'QList<QBar3DSeries *>': the list of QBar3DSeries, which
#  'QList[QBar3DSeries]' gives. It is made here, so that there is one as soon
#  as there can be a QBar3DSeries.
QList.createKind(
    QBar3DSeries, 'address',
    make='ritual_list_make_QBar3DSeries_ptr',
    add='ritual_list_add_QBar3DSeries_ptr',
    size='ritual_list_size_QBar3DSeries_ptr',
    at='ritual_list_at_QBar3DSeries_ptr',
    drop='ritual_list_drop_QBar3DSeries_ptr',
)
