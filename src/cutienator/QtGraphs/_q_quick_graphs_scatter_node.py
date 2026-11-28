"""
QQuickGraphsScatterNode binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGraphs/6.12.0/QtGraphs/private/qquickgraphsscatternode_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuickGraphsScatterNode to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList
from . import QtGraphs3D, QQuickGraphsNode
from ..QtQuick3D import QQuick3DNode

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QPointF
  from ..QtGui import QVector3D
  from . import QQuickGraphsScatter, QScatter3DSeries, QValue3DAxis
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPointF = WAIT['QPointF']
  QScatter3DSeries = WAIT['QtGraphs:QScatter3DSeries']
  QValue3DAxis = WAIT['QtGraphs:QValue3DAxis']
  QVector3D = WAIT['QVector3D']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickGraphsScatterNode(QQuickGraphsNode):
  """
  The cute side of Qt's QQuickGraphsScatterNode: a plain Python object
  standing in front of one C++ QQuickGraphsScatterNode.

  It is built on the cute 'QQuickGraphsNode', as Qt's QQuickGraphsScatterNode
  is built on Qt's QQuickGraphsNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickGraphsScatterNode that has a ritual and that
  Python can call so far, 22 names in all: 'metaObject', 'tr', 'axisX',
  'setAxisX', 'axisY', 'setAxisY', 'axisZ', 'setAxisZ', 'selectedSeries',
  'setSelectionMode', 'scatterSeriesList', 'addSeries', 'removeSeries',
  'clearSelection', 'doPicking', 'doRayPicking', 'componentComplete',
  'axisXChanged', 'axisYChanged', 'axisZChanged', 'selectedSeriesChanged',
  'graphScatter'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickGraphsScatterNode::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickGraphsScatterNode::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickGraphsScatterNode::~QQuickGraphsScatterNode()': the
    destructor: Python never removes a C++ QQuickGraphsScatterNode.
  - Qt's 'QQmlListProperty<QScatter3DSeries>
    QQuickGraphsScatterNode::seriesList()': gives a type Python has no way to
    take yet.
  - Qt's 'void QQuickGraphsScatterNode::appendSeriesFunc(
    QQmlListProperty<QScatter3DSeries> *list, QScatter3DSeries *series)':
    names 'QQmlListProperty<QScatter3DSeries>', which has no cute class yet.
  - Qt's 'qsizetype QQuickGraphsScatterNode::countSeriesFunc(
    QQmlListProperty<QScatter3DSeries> *list)': names
    'QQmlListProperty<QScatter3DSeries>', which has no cute class yet.
  - Qt's 'QScatter3DSeries
    *QQuickGraphsScatterNode::atSeriesFunc(QQmlListProperty<QScatter3DSeries>
    *list, qsizetype index)': names 'QQmlListProperty<QScatter3DSeries>',
    which has no cute class yet.
  - Qt's 'void QQuickGraphsScatterNode::clearSeriesFunc(
    QQmlListProperty<QScatter3DSeries> *list)': names
    'QQmlListProperty<QScatter3DSeries>', which has no cute class yet.
  - Qt's 'const QQuickGraphsScatter *QQuickGraphsScatterNode::graphScatter()
    const': takes in Python what 'QQuickGraphsScatter
    *QQuickGraphsScatterNode::graphScatter()' takes.

  What has no ritual
  ------------------

  2 of the 34 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickGraphsScatterNode is created at the first use, not by
    'QQuickGraphsScatterNode(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickGraphsScatterNode.
  - Qt tells when it has removed the C++ QQuickGraphsScatterNode. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickGraphsScatterNode that has no cute function yet,
    'appendSeriesFunc', 'atSeriesFunc', 'clearSeriesFunc', 'countSeriesFunc',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
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
    Calls Qt's 'QString QQuickGraphsScatterNode::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsscatternode.html#tr

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
    #  QString QQuickGraphsScatterNode::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN23QQuickGraphsScatterNode2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickGraphsScatterNode'

  #  A C++ QQuickGraphsScatterNode Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickGraphsScatterNode'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickGraphsScatterNode::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsscatternode.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickGraphsScatterNode::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK23QQuickGraphsScatterNode10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def axisX(self) -> Optional[QValue3DAxis]:
    """
    Calls Qt's 'QValue3DAxis *QQuickGraphsScatterNode::axisX() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsscatternode.html#axisX

    Returns
    -------

    Optional[QValue3DAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QValue3DAxis *QQuickGraphsScatterNode::axisX() const
    address = self.uglySide.call(
        'ritual_ZNK23QQuickGraphsScatterNode5axisXEv',
    )
    from . import QValue3DAxis
    return QValue3DAxis._cuteAt(address)

  def axisY(self) -> Optional[QValue3DAxis]:
    """
    Calls Qt's 'QValue3DAxis *QQuickGraphsScatterNode::axisY() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsscatternode.html#axisY

    Returns
    -------

    Optional[QValue3DAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QValue3DAxis *QQuickGraphsScatterNode::axisY() const
    address = self.uglySide.call(
        'ritual_ZNK23QQuickGraphsScatterNode5axisYEv',
    )
    from . import QValue3DAxis
    return QValue3DAxis._cuteAt(address)

  def axisZ(self) -> Optional[QValue3DAxis]:
    """
    Calls Qt's 'QValue3DAxis *QQuickGraphsScatterNode::axisZ() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsscatternode.html#axisZ

    Returns
    -------

    Optional[QValue3DAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QValue3DAxis *QQuickGraphsScatterNode::axisZ() const
    address = self.uglySide.call(
        'ritual_ZNK23QQuickGraphsScatterNode5axisZEv',
    )
    from . import QValue3DAxis
    return QValue3DAxis._cuteAt(address)

  def selectedSeries(self) -> Optional[QScatter3DSeries]:
    """
    Calls Qt's 'QScatter3DSeries *QQuickGraphsScatterNode::selectedSeries()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsscatternode.html#selectedSeries

    Returns
    -------

    Optional[QScatter3DSeries]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QScatter3DSeries *QQuickGraphsScatterNode::selectedSeries() const
    address = self.uglySide.call(
        'ritual_ZNK23QQuickGraphsScatterNode14selectedSeriesEv',
    )
    from . import QScatter3DSeries
    return QScatter3DSeries._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QValue3DAxis)
  @overload(NoneType)
  def setAxisX(self, axis: Optional[QValue3DAxis]) -> None:
    """
    Calls Qt's 'void QQuickGraphsScatterNode::setAxisX(QValue3DAxis *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsscatternode.html#setAxisX

    Parameters
    ----------

    axis : Optional[QValue3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsScatterNode::setAxisX(QValue3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN23QQuickGraphsScatterNode8setAxisXEP12QValue3DAxis',
        self._addressOf(axis),
    )

  @overload(QValue3DAxis)
  @overload(NoneType)
  def setAxisY(self, axis: Optional[QValue3DAxis]) -> None:
    """
    Calls Qt's 'void QQuickGraphsScatterNode::setAxisY(QValue3DAxis *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsscatternode.html#setAxisY

    Parameters
    ----------

    axis : Optional[QValue3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsScatterNode::setAxisY(QValue3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN23QQuickGraphsScatterNode8setAxisYEP12QValue3DAxis',
        self._addressOf(axis),
    )

  @overload(QValue3DAxis)
  @overload(NoneType)
  def setAxisZ(self, axis: Optional[QValue3DAxis]) -> None:
    """
    Calls Qt's 'void QQuickGraphsScatterNode::setAxisZ(QValue3DAxis *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsscatternode.html#setAxisZ

    Parameters
    ----------

    axis : Optional[QValue3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsScatterNode::setAxisZ(QValue3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN23QQuickGraphsScatterNode8setAxisZEP12QValue3DAxis',
        self._addressOf(axis),
    )

  @overload(QtGraphs3D.SelectionFlags)
  def setSelectionMode(self, mode: QtGraphs3D.SelectionFlags) -> None:
    """
    Calls Qt's 'void
    QQuickGraphsScatterNode::setSelectionMode(QtGraphs3D::SelectionFlags
    mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsscatternode.html#setSelectionMode

    Parameters
    ----------

    mode : QtGraphs3D.SelectionFlags
      Passed on as its number.
    """
    #  void QQuickGraphsScatterNode::setSelectionMode(QtGraphs3D::
    #      SelectionFlags mode)
    ritual = (
        'ritual_ZN23QQuickGraphsScatterNode16setSelectionModeE6QFlagsIN10Qt'
        'Graphs3D13SelectionFlagEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN23QQuickGraphsScatterNode16setSelectionModeE6QFlags'
          'IN10QtGraphs3D13SelectionFlagEE')
    self.uglySide.call(ritual, mode.value)

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
  @overload(QQuick3DNode)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuick3DNode] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuickGraphsScatterNode::QQuickGraphsScatterNode(QQuick3DNode *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsscatternode.html

    Parameters
    ----------

    parent : Optional[QQuick3DNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickGraphsScatterNode::QQuickGraphsScatterNode(QQuick3DNode *parent)
    self._noteCreation(QQuickGraphsScatterNode, lambda: Rituals.call(
        'ritual_ZN23QQuickGraphsScatterNodeC1EP12QQuick3DNode',
        self._addressOf(parent),
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

  def scatterSeriesList(self) -> QList[QScatter3DSeries]:
    """
    Calls Qt's 'QList<QScatter3DSeries *>
    QQuickGraphsScatterNode::scatterSeriesList()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsscatternode.html#scatterSeriesList

    Returns
    -------

    QList[QScatter3DSeries]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QScatter3DSeries *> QQuickGraphsScatterNode::scatterSeriesList()
    address = self.uglySide.call(
        'ritual_ZN23QQuickGraphsScatterNode17scatterSeriesListEv',
    )
    from . import QScatter3DSeries
    return QList[QScatter3DSeries]._cuteOwning(address)

  @overload(QScatter3DSeries)
  @overload(NoneType)
  def addSeries(self, series: Optional[QScatter3DSeries]) -> None:
    """
    Calls Qt's 'void QQuickGraphsScatterNode::addSeries(QScatter3DSeries
    *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsscatternode.html#addSeries

    Parameters
    ----------

    series : Optional[QScatter3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsScatterNode::addSeries(QScatter3DSeries *series)
    self.uglySide.call(
        'ritual_ZN23QQuickGraphsScatterNode9addSeriesEP16QScatter3DSeries',
        self._addressOf(series),
    )

  @overload(QScatter3DSeries)
  @overload(NoneType)
  def removeSeries(self, series: Optional[QScatter3DSeries]) -> None:
    """
    Calls Qt's 'void QQuickGraphsScatterNode::removeSeries(QScatter3DSeries
    *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsscatternode.html#removeSeries

    Parameters
    ----------

    series : Optional[QScatter3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsScatterNode::removeSeries(QScatter3DSeries *series)
    self.uglySide.call(
        'ritual_ZN23QQuickGraphsScatterNode12removeSeriesEP16QScatter3DSeri'
        'es',
        self._addressOf(series),
    )

  def clearSelection(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsScatterNode::clearSelection()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsscatternode.html#clearSelection
    """
    #  void QQuickGraphsScatterNode::clearSelection()
    ritual = 'ritual_ZN23QQuickGraphsScatterNode14clearSelectionEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN23QQuickGraphsScatterNode14clearSelectionEv'
    self.uglySide.call(ritual)

  @overload(QPointF)
  def doPicking(self, point: QPointF) -> bool:
    """
    Calls Qt's 'bool QQuickGraphsScatterNode::doPicking(QPointF point)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsscatternode.html#doPicking

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  bool QQuickGraphsScatterNode::doPicking(QPointF point)
    ritual = 'ritual_ZN23QQuickGraphsScatterNode9doPickingE7QPointF'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN23QQuickGraphsScatterNode9doPickingE7QPointF'
    return self.uglySide.call(ritual, self._valueOf(point, 'QPointF'))

  @overload(QVector3D, QVector3D)
  def doRayPicking(self, origin: QVector3D, direction: QVector3D) -> bool:
    """
    Calls Qt's 'bool QQuickGraphsScatterNode::doRayPicking(const QVector3D
    &origin, const QVector3D &direction)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsscatternode.html#doRayPicking

    Parameters
    ----------

    origin : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    direction : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  bool QQuickGraphsScatterNode::doRayPicking(const QVector3D &origin,
    #      const QVector3D &direction)
    ritual = (
        'ritual_ZN23QQuickGraphsScatterNode12doRayPickingERK9QVector3DS2_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN23QQuickGraphsScatterNode12doRayPickingERK9QVector3'
          'DS2_')
    return self.uglySide.call(
        ritual, self._valueOf(origin), self._valueOf(direction),
    )

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsScatterNode::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsscatternode.html#componentComplete
    """
    #  void QQuickGraphsScatterNode::componentComplete()
    ritual = 'ritual_ZN23QQuickGraphsScatterNode17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN23QQuickGraphsScatterNode17componentCompleteEv'
    self.uglySide.call(ritual)

  @overload(QValue3DAxis)
  @overload(NoneType)
  def axisXChanged(self, axis: Optional[QValue3DAxis]) -> None:
    """
    Calls Qt's 'void QQuickGraphsScatterNode::axisXChanged(QValue3DAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsscatternode.html#axisXChanged

    Parameters
    ----------

    axis : Optional[QValue3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsScatterNode::axisXChanged(QValue3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN23QQuickGraphsScatterNode12axisXChangedEP12QValue3DAxis',
        self._addressOf(axis),
    )

  @overload(QValue3DAxis)
  @overload(NoneType)
  def axisYChanged(self, axis: Optional[QValue3DAxis]) -> None:
    """
    Calls Qt's 'void QQuickGraphsScatterNode::axisYChanged(QValue3DAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsscatternode.html#axisYChanged

    Parameters
    ----------

    axis : Optional[QValue3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsScatterNode::axisYChanged(QValue3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN23QQuickGraphsScatterNode12axisYChangedEP12QValue3DAxis',
        self._addressOf(axis),
    )

  @overload(QValue3DAxis)
  @overload(NoneType)
  def axisZChanged(self, axis: Optional[QValue3DAxis]) -> None:
    """
    Calls Qt's 'void QQuickGraphsScatterNode::axisZChanged(QValue3DAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsscatternode.html#axisZChanged

    Parameters
    ----------

    axis : Optional[QValue3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsScatterNode::axisZChanged(QValue3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN23QQuickGraphsScatterNode12axisZChangedEP12QValue3DAxis',
        self._addressOf(axis),
    )

  @overload(QScatter3DSeries)
  @overload(NoneType)
  def selectedSeriesChanged(
      self,
      series: Optional[QScatter3DSeries],
  ) -> None:
    """
    Calls Qt's 'void
    QQuickGraphsScatterNode::selectedSeriesChanged(QScatter3DSeries
    *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsscatternode.html#selectedSeriesChanged

    Parameters
    ----------

    series : Optional[QScatter3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsScatterNode::selectedSeriesChanged(QScatter3DSeries
    #      *series)
    self.uglySide.call(
        'ritual_ZN23QQuickGraphsScatterNode21selectedSeriesChangedEP16QScat'
        'ter3DSeries',
        self._addressOf(series),
    )

  def graphScatter(self) -> Optional[QQuickGraphsScatter]:
    """
    Calls Qt's 'QQuickGraphsScatter
    *QQuickGraphsScatterNode::graphScatter()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsscatternode.html#graphScatter

    Returns
    -------

    Optional[QQuickGraphsScatter]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickGraphsScatter *QQuickGraphsScatterNode::graphScatter()
    address = self.uglySide.call(
        'ritual_ZN23QQuickGraphsScatterNode12graphScatterEv',
    )
    from . import QQuickGraphsScatter
    return QQuickGraphsScatter._cuteAt(address)

  @staticmethod
  def appendSeriesFunc(*__, **_) -> Never:
    """
    Qt's 'void QQuickGraphsScatterNode::appendSeriesFunc(
    QQmlListProperty<QScatter3DSeries> *list, QScatter3DSeries *series)':
    names 'QQmlListProperty<QScatter3DSeries>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuickGraphsScatterNode.appendSeriesFunc' has no cute function "
        "yet. Qt's 'void "
        "QQuickGraphsScatterNode::appendSeriesFunc(QQmlListProperty<QScatter"
        "3DSeries> *list, QScatter3DSeries *series)': names "
        "'QQmlListProperty<QScatter3DSeries>', which has no cute class yet.")

  @staticmethod
  def atSeriesFunc(*__, **_) -> Never:
    """
    Qt's 'QScatter3DSeries
    *QQuickGraphsScatterNode::atSeriesFunc(QQmlListProperty<QScatter3DSeries>
    *list, qsizetype index)': names 'QQmlListProperty<QScatter3DSeries>',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuickGraphsScatterNode.atSeriesFunc' has no cute function yet. "
        "Qt's 'QScatter3DSeries "
        "*QQuickGraphsScatterNode::atSeriesFunc(QQmlListProperty<QScatter3DS"
        "eries> *list, qsizetype index)': names "
        "'QQmlListProperty<QScatter3DSeries>', which has no cute class yet.")

  @staticmethod
  def clearSeriesFunc(*__, **_) -> Never:
    """
    Qt's 'void QQuickGraphsScatterNode::clearSeriesFunc(
    QQmlListProperty<QScatter3DSeries> *list)': names
    'QQmlListProperty<QScatter3DSeries>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuickGraphsScatterNode.clearSeriesFunc' has no cute function "
        "yet. Qt's 'void "
        "QQuickGraphsScatterNode::clearSeriesFunc(QQmlListProperty<QScatter3"
        "DSeries> *list)': names 'QQmlListProperty<QScatter3DSeries>', "
        "which has no cute class yet.")

  @staticmethod
  def countSeriesFunc(*__, **_) -> Never:
    """
    Qt's 'qsizetype QQuickGraphsScatterNode::countSeriesFunc(
    QQmlListProperty<QScatter3DSeries> *list)': names
    'QQmlListProperty<QScatter3DSeries>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuickGraphsScatterNode.countSeriesFunc' has no cute function "
        "yet. Qt's 'qsizetype "
        "QQuickGraphsScatterNode::countSeriesFunc(QQmlListProperty<QScatter3"
        "DSeries> *list)': names 'QQmlListProperty<QScatter3DSeries>', "
        "which has no cute class yet.")
