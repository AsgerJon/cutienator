"""
QQuickGraphsSurfaceNode binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGraphs/6.12.0/QtGraphs/private/qquickgraphssurfacenode_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuickGraphsSurfaceNode to be private: it declares the class in a
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
  from . import QQuickGraphsSurface, QSurface3DSeries, QValue3DAxis
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPointF = WAIT['QPointF']
  QSurface3DSeries = WAIT['QtGraphs:QSurface3DSeries']
  QValue3DAxis = WAIT['QtGraphs:QValue3DAxis']
  QVector3D = WAIT['QVector3D']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickGraphsSurfaceNode(QQuickGraphsNode):
  """
  The cute side of Qt's QQuickGraphsSurfaceNode: a plain Python object
  standing in front of one C++ QQuickGraphsSurfaceNode.

  It is built on the cute 'QQuickGraphsNode', as Qt's QQuickGraphsSurfaceNode
  is built on Qt's QQuickGraphsNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickGraphsSurfaceNode that has a ritual and that
  Python can call so far, 25 names in all: 'metaObject', 'tr', 'axisX',
  'setAxisX', 'axisY', 'setAxisY', 'axisZ', 'setAxisZ', 'selectedSeries',
  'setSelectionMode', 'flipHorizontalGrid', 'setFlipHorizontalGrid',
  'surfaceSeriesList', 'addSeries', 'removeSeries', 'clearSelection',
  'doPicking', 'doRayPicking', 'componentComplete', 'axisXChanged',
  'axisYChanged', 'axisZChanged', 'selectedSeriesChanged',
  'flipHorizontalGridChanged', 'graphSurface'. It can be made from Python, in
  1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickGraphsSurfaceNode::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickGraphsSurfaceNode::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickGraphsSurfaceNode::~QQuickGraphsSurfaceNode()': the
    destructor: Python never removes a C++ QQuickGraphsSurfaceNode.
  - Qt's 'QQmlListProperty<QSurface3DSeries>
    QQuickGraphsSurfaceNode::seriesList()': gives a type Python has no way to
    take yet.
  - Qt's 'void QQuickGraphsSurfaceNode::appendSeriesFunc(
    QQmlListProperty<QSurface3DSeries> *list, QSurface3DSeries *series)':
    names 'QQmlListProperty<QSurface3DSeries>', which has no cute class yet.
  - Qt's 'qsizetype QQuickGraphsSurfaceNode::countSeriesFunc(
    QQmlListProperty<QSurface3DSeries> *list)': names
    'QQmlListProperty<QSurface3DSeries>', which has no cute class yet.
  - Qt's 'QSurface3DSeries
    *QQuickGraphsSurfaceNode::atSeriesFunc(QQmlListProperty<QSurface3DSeries>
    *list, qsizetype index)': names 'QQmlListProperty<QSurface3DSeries>',
    which has no cute class yet.
  - Qt's 'void QQuickGraphsSurfaceNode::clearSeriesFunc(
    QQmlListProperty<QSurface3DSeries> *list)': names
    'QQmlListProperty<QSurface3DSeries>', which has no cute class yet.
  - Qt's 'const QQuickGraphsSurface *QQuickGraphsSurfaceNode::graphSurface()
    const': takes in Python what 'QQuickGraphsSurface
    *QQuickGraphsSurfaceNode::graphSurface()' takes.

  What has no ritual
  ------------------

  2 of the 37 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickGraphsSurfaceNode is created at the first use, not by
    'QQuickGraphsSurfaceNode(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickGraphsSurfaceNode.
  - Qt tells when it has removed the C++ QQuickGraphsSurfaceNode. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickGraphsSurfaceNode that has no cute function yet,
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
    Calls Qt's 'QString QQuickGraphsSurfaceNode::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphssurfacenode.html#tr

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
    #  QString QQuickGraphsSurfaceNode::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN23QQuickGraphsSurfaceNode2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickGraphsSurfaceNode'

  #  A C++ QQuickGraphsSurfaceNode Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickGraphsSurfaceNode'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickGraphsSurfaceNode::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurfacenode.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickGraphsSurfaceNode::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK23QQuickGraphsSurfaceNode10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def axisX(self) -> Optional[QValue3DAxis]:
    """
    Calls Qt's 'QValue3DAxis *QQuickGraphsSurfaceNode::axisX() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphssurfacenode.html#axisX

    Returns
    -------

    Optional[QValue3DAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QValue3DAxis *QQuickGraphsSurfaceNode::axisX() const
    address = self.uglySide.call(
        'ritual_ZNK23QQuickGraphsSurfaceNode5axisXEv',
    )
    from . import QValue3DAxis
    return QValue3DAxis._cuteAt(address)

  def axisY(self) -> Optional[QValue3DAxis]:
    """
    Calls Qt's 'QValue3DAxis *QQuickGraphsSurfaceNode::axisY() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphssurfacenode.html#axisY

    Returns
    -------

    Optional[QValue3DAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QValue3DAxis *QQuickGraphsSurfaceNode::axisY() const
    address = self.uglySide.call(
        'ritual_ZNK23QQuickGraphsSurfaceNode5axisYEv',
    )
    from . import QValue3DAxis
    return QValue3DAxis._cuteAt(address)

  def axisZ(self) -> Optional[QValue3DAxis]:
    """
    Calls Qt's 'QValue3DAxis *QQuickGraphsSurfaceNode::axisZ() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphssurfacenode.html#axisZ

    Returns
    -------

    Optional[QValue3DAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QValue3DAxis *QQuickGraphsSurfaceNode::axisZ() const
    address = self.uglySide.call(
        'ritual_ZNK23QQuickGraphsSurfaceNode5axisZEv',
    )
    from . import QValue3DAxis
    return QValue3DAxis._cuteAt(address)

  def selectedSeries(self) -> Optional[QSurface3DSeries]:
    """
    Calls Qt's 'QSurface3DSeries *QQuickGraphsSurfaceNode::selectedSeries()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurfacenode.html#selectedSeries

    Returns
    -------

    Optional[QSurface3DSeries]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSurface3DSeries *QQuickGraphsSurfaceNode::selectedSeries() const
    address = self.uglySide.call(
        'ritual_ZNK23QQuickGraphsSurfaceNode14selectedSeriesEv',
    )
    from . import QSurface3DSeries
    return QSurface3DSeries._cuteAt(address)

  def flipHorizontalGrid(self) -> bool:
    """
    Calls Qt's 'bool QQuickGraphsSurfaceNode::flipHorizontalGrid() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurfacenode.html#flipHorizontalGrid
    """
    #  bool QQuickGraphsSurfaceNode::flipHorizontalGrid() const
    return self.uglySide.call(
        'ritual_ZNK23QQuickGraphsSurfaceNode18flipHorizontalGridEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QValue3DAxis)
  @overload(NoneType)
  def setAxisX(self, axis: Optional[QValue3DAxis]) -> None:
    """
    Calls Qt's 'void QQuickGraphsSurfaceNode::setAxisX(QValue3DAxis *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurfacenode.html#setAxisX

    Parameters
    ----------

    axis : Optional[QValue3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsSurfaceNode::setAxisX(QValue3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN23QQuickGraphsSurfaceNode8setAxisXEP12QValue3DAxis',
        self._addressOf(axis),
    )

  @overload(QValue3DAxis)
  @overload(NoneType)
  def setAxisY(self, axis: Optional[QValue3DAxis]) -> None:
    """
    Calls Qt's 'void QQuickGraphsSurfaceNode::setAxisY(QValue3DAxis *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurfacenode.html#setAxisY

    Parameters
    ----------

    axis : Optional[QValue3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsSurfaceNode::setAxisY(QValue3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN23QQuickGraphsSurfaceNode8setAxisYEP12QValue3DAxis',
        self._addressOf(axis),
    )

  @overload(QValue3DAxis)
  @overload(NoneType)
  def setAxisZ(self, axis: Optional[QValue3DAxis]) -> None:
    """
    Calls Qt's 'void QQuickGraphsSurfaceNode::setAxisZ(QValue3DAxis *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurfacenode.html#setAxisZ

    Parameters
    ----------

    axis : Optional[QValue3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsSurfaceNode::setAxisZ(QValue3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN23QQuickGraphsSurfaceNode8setAxisZEP12QValue3DAxis',
        self._addressOf(axis),
    )

  @overload(QtGraphs3D.SelectionFlags)
  def setSelectionMode(self, mode: QtGraphs3D.SelectionFlags) -> None:
    """
    Calls Qt's 'void
    QQuickGraphsSurfaceNode::setSelectionMode(QtGraphs3D::SelectionFlags
    mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurfacenode.html#setSelectionMode

    Parameters
    ----------

    mode : QtGraphs3D.SelectionFlags
      Passed on as its number.
    """
    #  void QQuickGraphsSurfaceNode::setSelectionMode(QtGraphs3D::
    #      SelectionFlags mode)
    ritual = (
        'ritual_ZN23QQuickGraphsSurfaceNode16setSelectionModeE6QFlagsIN10Qt'
        'Graphs3D13SelectionFlagEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN23QQuickGraphsSurfaceNode16setSelectionModeE6QFlags'
          'IN10QtGraphs3D13SelectionFlagEE')
    self.uglySide.call(ritual, mode.value)

  @overload(bool)
  def setFlipHorizontalGrid(self, flip: bool) -> None:
    """
    Calls Qt's 'void QQuickGraphsSurfaceNode::setFlipHorizontalGrid(bool
    flip)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurfacenode.html#setFlipHorizontalGrid

    Parameters
    ----------

    flip : bool
      Passed on as it is.
    """
    #  void QQuickGraphsSurfaceNode::setFlipHorizontalGrid(bool flip)
    self.uglySide.call(
        'ritual_ZN23QQuickGraphsSurfaceNode21setFlipHorizontalGridEb', flip,
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
  @overload(QQuick3DNode)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuick3DNode] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuickGraphsSurfaceNode::QQuickGraphsSurfaceNode(QQuick3DNode *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurfacenode.html

    Parameters
    ----------

    parent : Optional[QQuick3DNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickGraphsSurfaceNode::QQuickGraphsSurfaceNode(QQuick3DNode *parent)
    self._noteCreation(QQuickGraphsSurfaceNode, lambda: Rituals.call(
        'ritual_ZN23QQuickGraphsSurfaceNodeC1EP12QQuick3DNode',
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

  def surfaceSeriesList(self) -> QList[QSurface3DSeries]:
    """
    Calls Qt's 'QList<QSurface3DSeries *>
    QQuickGraphsSurfaceNode::surfaceSeriesList()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurfacenode.html#surfaceSeriesList

    Returns
    -------

    QList[QSurface3DSeries]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QSurface3DSeries *> QQuickGraphsSurfaceNode::surfaceSeriesList()
    address = self.uglySide.call(
        'ritual_ZN23QQuickGraphsSurfaceNode17surfaceSeriesListEv',
    )
    from . import QSurface3DSeries
    return QList[QSurface3DSeries]._cuteOwning(address)

  @overload(QSurface3DSeries)
  @overload(NoneType)
  def addSeries(self, series: Optional[QSurface3DSeries]) -> None:
    """
    Calls Qt's 'void QQuickGraphsSurfaceNode::addSeries(QSurface3DSeries
    *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurfacenode.html#addSeries

    Parameters
    ----------

    series : Optional[QSurface3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsSurfaceNode::addSeries(QSurface3DSeries *series)
    self.uglySide.call(
        'ritual_ZN23QQuickGraphsSurfaceNode9addSeriesEP16QSurface3DSeries',
        self._addressOf(series),
    )

  @overload(QSurface3DSeries)
  @overload(NoneType)
  def removeSeries(self, series: Optional[QSurface3DSeries]) -> None:
    """
    Calls Qt's 'void QQuickGraphsSurfaceNode::removeSeries(QSurface3DSeries
    *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurfacenode.html#removeSeries

    Parameters
    ----------

    series : Optional[QSurface3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsSurfaceNode::removeSeries(QSurface3DSeries *series)
    self.uglySide.call(
        'ritual_ZN23QQuickGraphsSurfaceNode12removeSeriesEP16QSurface3DSeri'
        'es',
        self._addressOf(series),
    )

  def clearSelection(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsSurfaceNode::clearSelection()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurfacenode.html#clearSelection
    """
    #  void QQuickGraphsSurfaceNode::clearSelection()
    ritual = 'ritual_ZN23QQuickGraphsSurfaceNode14clearSelectionEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN23QQuickGraphsSurfaceNode14clearSelectionEv'
    self.uglySide.call(ritual)

  @overload(QPointF)
  def doPicking(self, point: QPointF) -> bool:
    """
    Calls Qt's 'bool QQuickGraphsSurfaceNode::doPicking(QPointF point)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurfacenode.html#doPicking

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  bool QQuickGraphsSurfaceNode::doPicking(QPointF point)
    ritual = 'ritual_ZN23QQuickGraphsSurfaceNode9doPickingE7QPointF'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN23QQuickGraphsSurfaceNode9doPickingE7QPointF'
    return self.uglySide.call(ritual, self._valueOf(point, 'QPointF'))

  @overload(QVector3D, QVector3D)
  def doRayPicking(self, origin: QVector3D, direction: QVector3D) -> bool:
    """
    Calls Qt's 'bool QQuickGraphsSurfaceNode::doRayPicking(const QVector3D
    &origin, const QVector3D &direction)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurfacenode.html#doRayPicking

    Parameters
    ----------

    origin : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    direction : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  bool QQuickGraphsSurfaceNode::doRayPicking(const QVector3D &origin,
    #      const QVector3D &direction)
    ritual = (
        'ritual_ZN23QQuickGraphsSurfaceNode12doRayPickingERK9QVector3DS2_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN23QQuickGraphsSurfaceNode12doRayPickingERK9QVector3'
          'DS2_')
    return self.uglySide.call(
        ritual, self._valueOf(origin), self._valueOf(direction),
    )

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsSurfaceNode::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurfacenode.html#componentComplete
    """
    #  void QQuickGraphsSurfaceNode::componentComplete()
    ritual = 'ritual_ZN23QQuickGraphsSurfaceNode17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN23QQuickGraphsSurfaceNode17componentCompleteEv'
    self.uglySide.call(ritual)

  @overload(QValue3DAxis)
  @overload(NoneType)
  def axisXChanged(self, axis: Optional[QValue3DAxis]) -> None:
    """
    Calls Qt's 'void QQuickGraphsSurfaceNode::axisXChanged(QValue3DAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurfacenode.html#axisXChanged

    Parameters
    ----------

    axis : Optional[QValue3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsSurfaceNode::axisXChanged(QValue3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN23QQuickGraphsSurfaceNode12axisXChangedEP12QValue3DAxis',
        self._addressOf(axis),
    )

  @overload(QValue3DAxis)
  @overload(NoneType)
  def axisYChanged(self, axis: Optional[QValue3DAxis]) -> None:
    """
    Calls Qt's 'void QQuickGraphsSurfaceNode::axisYChanged(QValue3DAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurfacenode.html#axisYChanged

    Parameters
    ----------

    axis : Optional[QValue3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsSurfaceNode::axisYChanged(QValue3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN23QQuickGraphsSurfaceNode12axisYChangedEP12QValue3DAxis',
        self._addressOf(axis),
    )

  @overload(QValue3DAxis)
  @overload(NoneType)
  def axisZChanged(self, axis: Optional[QValue3DAxis]) -> None:
    """
    Calls Qt's 'void QQuickGraphsSurfaceNode::axisZChanged(QValue3DAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurfacenode.html#axisZChanged

    Parameters
    ----------

    axis : Optional[QValue3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsSurfaceNode::axisZChanged(QValue3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN23QQuickGraphsSurfaceNode12axisZChangedEP12QValue3DAxis',
        self._addressOf(axis),
    )

  @overload(QSurface3DSeries)
  @overload(NoneType)
  def selectedSeriesChanged(
      self,
      series: Optional[QSurface3DSeries],
  ) -> None:
    """
    Calls Qt's 'void
    QQuickGraphsSurfaceNode::selectedSeriesChanged(QSurface3DSeries
    *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurfacenode.html#selectedSeriesChanged

    Parameters
    ----------

    series : Optional[QSurface3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsSurfaceNode::selectedSeriesChanged(QSurface3DSeries
    #      *series)
    self.uglySide.call(
        'ritual_ZN23QQuickGraphsSurfaceNode21selectedSeriesChangedEP16QSurf'
        'ace3DSeries',
        self._addressOf(series),
    )

  @overload(bool)
  def flipHorizontalGridChanged(self, flip: bool) -> None:
    """
    Calls Qt's 'void QQuickGraphsSurfaceNode::flipHorizontalGridChanged(bool
    flip)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurfacenode.html

    Parameters
    ----------

    flip : bool
      Passed on as it is.
    """
    #  void QQuickGraphsSurfaceNode::flipHorizontalGridChanged(bool flip)
    self.uglySide.call(
        'ritual_ZN23QQuickGraphsSurfaceNode25flipHorizontalGridChangedEb',
        flip,
    )

  def graphSurface(self) -> Optional[QQuickGraphsSurface]:
    """
    Calls Qt's 'QQuickGraphsSurface
    *QQuickGraphsSurfaceNode::graphSurface()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurfacenode.html#graphSurface

    Returns
    -------

    Optional[QQuickGraphsSurface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickGraphsSurface *QQuickGraphsSurfaceNode::graphSurface()
    address = self.uglySide.call(
        'ritual_ZN23QQuickGraphsSurfaceNode12graphSurfaceEv',
    )
    from . import QQuickGraphsSurface
    return QQuickGraphsSurface._cuteAt(address)

  @staticmethod
  def appendSeriesFunc(*__, **_) -> Never:
    """
    Qt's 'void QQuickGraphsSurfaceNode::appendSeriesFunc(
    QQmlListProperty<QSurface3DSeries> *list, QSurface3DSeries *series)':
    names 'QQmlListProperty<QSurface3DSeries>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuickGraphsSurfaceNode.appendSeriesFunc' has no cute function "
        "yet. Qt's 'void "
        "QQuickGraphsSurfaceNode::appendSeriesFunc(QQmlListProperty<QSurface"
        "3DSeries> *list, QSurface3DSeries *series)': names "
        "'QQmlListProperty<QSurface3DSeries>', which has no cute class yet.")

  @staticmethod
  def atSeriesFunc(*__, **_) -> Never:
    """
    Qt's 'QSurface3DSeries
    *QQuickGraphsSurfaceNode::atSeriesFunc(QQmlListProperty<QSurface3DSeries>
    *list, qsizetype index)': names 'QQmlListProperty<QSurface3DSeries>',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuickGraphsSurfaceNode.atSeriesFunc' has no cute function yet. "
        "Qt's 'QSurface3DSeries "
        "*QQuickGraphsSurfaceNode::atSeriesFunc(QQmlListProperty<QSurface3DS"
        "eries> *list, qsizetype index)': names "
        "'QQmlListProperty<QSurface3DSeries>', which has no cute class yet.")

  @staticmethod
  def clearSeriesFunc(*__, **_) -> Never:
    """
    Qt's 'void QQuickGraphsSurfaceNode::clearSeriesFunc(
    QQmlListProperty<QSurface3DSeries> *list)': names
    'QQmlListProperty<QSurface3DSeries>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuickGraphsSurfaceNode.clearSeriesFunc' has no cute function "
        "yet. Qt's 'void "
        "QQuickGraphsSurfaceNode::clearSeriesFunc(QQmlListProperty<QSurface3"
        "DSeries> *list)': names 'QQmlListProperty<QSurface3DSeries>', "
        "which has no cute class yet.")

  @staticmethod
  def countSeriesFunc(*__, **_) -> Never:
    """
    Qt's 'qsizetype QQuickGraphsSurfaceNode::countSeriesFunc(
    QQmlListProperty<QSurface3DSeries> *list)': names
    'QQmlListProperty<QSurface3DSeries>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuickGraphsSurfaceNode.countSeriesFunc' has no cute function "
        "yet. Qt's 'qsizetype "
        "QQuickGraphsSurfaceNode::countSeriesFunc(QQmlListProperty<QSurface3"
        "DSeries> *list)': names 'QQmlListProperty<QSurface3DSeries>', "
        "which has no cute class yet.")
