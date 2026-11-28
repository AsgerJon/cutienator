"""
QQuickGridView binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickgridview_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQuickGridView to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObject
from . import QQuickItem, QQuickItemView

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QRectF
  from ..QtGui import QKeyEvent
  from . import QQuickGridViewAttached
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QKeyEvent = WAIT['QKeyEvent']
  QRectF = WAIT['QRectF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickGridView(QQuickItemView):
  """
  The cute side of Qt's QQuickGridView: a plain Python object standing in
  front of one C++ QQuickGridView.

  It is built on the cute 'QQuickItemView', as Qt's QQuickGridView is built
  on Qt's QQuickItemView, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickGridView that has a ritual and that Python can
  call so far, 26 names in all: 'metaObject', 'tr',
  'setHighlightFollowsCurrentItem', 'setHighlightMoveDuration', 'flow',
  'setFlow', 'cellWidth', 'setCellWidth', 'cellHeight', 'setCellHeight',
  'snapMode', 'setSnapMode', 'qmlAttachedProperties', 'moveCurrentIndexUp',
  'moveCurrentIndexDown', 'moveCurrentIndexLeft', 'moveCurrentIndexRight',
  'cellWidthChanged', 'cellHeightChanged', 'highlightMoveDurationChanged',
  'flowChanged', 'snapModeChanged', 'viewportMoved', 'keyPressEvent',
  'geometryChange', 'initItem'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickGridView::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQuickGridView::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickGridViewPrivate *QQuickGridView::d_func()': gives
    'QQuickGridViewPrivate', which has no cute class yet.
  - Qt's 'const QQuickGridViewPrivate *QQuickGridView::d_func() const': gives
    'QQuickGridViewPrivate', which has no cute class yet.
  - Qt's 'void QQuickGridView::qt_qmlMarker_attached()': one of Qt's own
    inner workings.

  What has no ritual
  ------------------

  2 of the 34 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickGridView is created at the first use, not by
    'QQuickGridView(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickGridView.
  - Qt tells when it has removed the C++ QQuickGridView. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QQuickGridView, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Flow(CuteNum):
    """
    The enum 'QQuickGridView::Flow' of Qt, with the 2 names Qt gives in it.
    """

    FlowLeftToRight = Kee[int](0)
    FlowTopToBottom = Kee[int](2)

  class SnapMode(CuteNum):
    """
    The enum 'QQuickGridView::SnapMode' of Qt, with the 3 names Qt gives in
    it.
    """

    NoSnap = Kee[int](0)
    SnapToRow = Kee[int](1)
    SnapOneRow = Kee[int](2)

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
    Calls Qt's 'QString QQuickGridView::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgridview.html#tr

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
    #  QString QQuickGridView::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN14QQuickGridView2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  def qmlAttachedProperties(
      a0: Optional[QObject],
  ) -> Optional[QQuickGridViewAttached]:
    """
    Calls Qt's 'QQuickGridViewAttached
    *QQuickGridView::qmlAttachedProperties(QObject *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgridview.html#qmlAttachedProperties

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickGridViewAttached]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickGridViewAttached *QQuickGridView::qmlAttachedProperties(QObject
    #      *a0)
    address = Rituals.call(
        'ritual_ZN14QQuickGridView21qmlAttachedPropertiesEP7QObject',
        CuteMixin._addressOf(a0, 'QObject'),
    )
    from . import QQuickGridViewAttached
    return QQuickGridViewAttached._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickGridView'

  #  A C++ QQuickGridView Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickGridView'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickGridView::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgridview.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickGridView::metaObject() const
    address = self.uglySide.call('ritual_ZNK14QQuickGridView10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def flow(self) -> Flow:
    """
    Calls Qt's 'Flow QQuickGridView::flow() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgridview.html#flow

    Returns
    -------

    Flow
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Flow(number)' gives.
    """
    #  Flow QQuickGridView::flow() const
    return QQuickGridView.Flow(self.uglySide.call(
        'ritual_ZNK14QQuickGridView4flowEv',
    ))

  def cellWidth(self) -> float:
    """
    Calls Qt's 'qreal QQuickGridView::cellWidth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgridview.html#cellWidth
    """
    #  qreal QQuickGridView::cellWidth() const
    return self.uglySide.call('ritual_ZNK14QQuickGridView9cellWidthEv')

  def cellHeight(self) -> float:
    """
    Calls Qt's 'qreal QQuickGridView::cellHeight() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgridview.html#cellHeight
    """
    #  qreal QQuickGridView::cellHeight() const
    return self.uglySide.call('ritual_ZNK14QQuickGridView10cellHeightEv')

  def snapMode(self) -> SnapMode:
    """
    Calls Qt's 'SnapMode QQuickGridView::snapMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgridview.html#snapMode

    Returns
    -------

    SnapMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'SnapMode(number)' gives.
    """
    #  SnapMode QQuickGridView::snapMode() const
    return QQuickGridView.SnapMode(self.uglySide.call(
        'ritual_ZNK14QQuickGridView8snapModeEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setHighlightFollowsCurrentItem(self, a0: bool) -> None:
    """
    Calls Qt's 'void QQuickGridView::setHighlightFollowsCurrentItem(bool
    a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgridview.html#setHighlightFollowsCurrentItem

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QQuickGridView::setHighlightFollowsCurrentItem(bool a0)
    ritual = 'ritual_ZN14QQuickGridView30setHighlightFollowsCurrentItemEb'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QQuickGridView30setHighlightFollowsCurrentItemEb')
    self.uglySide.call(ritual, a0)

  @overload(int)
  def setHighlightMoveDuration(self, a0: int) -> None:
    """
    Calls Qt's 'void QQuickGridView::setHighlightMoveDuration(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgridview.html#setHighlightMoveDuration

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQuickGridView::setHighlightMoveDuration(int a0)
    ritual = 'ritual_ZN14QQuickGridView24setHighlightMoveDurationEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QQuickGridView24setHighlightMoveDurationEi'
    self.uglySide.call(ritual, a0)

  @overload(Flow)
  def setFlow(self, a0: Flow) -> None:
    """
    Calls Qt's 'void QQuickGridView::setFlow(Flow a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgridview.html#setFlow

    Parameters
    ----------

    a0 : Flow
      Passed on as its number.
    """
    #  void QQuickGridView::setFlow(Flow a0)
    self.uglySide.call(
        'ritual_ZN14QQuickGridView7setFlowENS_4FlowE', a0.value,
    )

  @overload(float)
  def setCellWidth(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickGridView::setCellWidth(qreal a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgridview.html#setCellWidth

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickGridView::setCellWidth(qreal a0)
    self.uglySide.call('ritual_ZN14QQuickGridView12setCellWidthEd', a0)

  @overload(float)
  def setCellHeight(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickGridView::setCellHeight(qreal a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgridview.html#setCellHeight

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickGridView::setCellHeight(qreal a0)
    self.uglySide.call('ritual_ZN14QQuickGridView13setCellHeightEd', a0)

  @overload(SnapMode)
  def setSnapMode(self, mode: SnapMode) -> None:
    """
    Calls Qt's 'void QQuickGridView::setSnapMode(SnapMode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgridview.html#setSnapMode

    Parameters
    ----------

    mode : SnapMode
      Passed on as its number.
    """
    #  void QQuickGridView::setSnapMode(SnapMode mode)
    self.uglySide.call(
        'ritual_ZN14QQuickGridView11setSnapModeENS_8SnapModeE', mode.value,
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
  @overload(QQuickItem)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuickItem] = None) -> None:
    """
    Notes what was given, for Qt's 'QQuickGridView::QQuickGridView(QQuickItem
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qquickgridview.html#QQuickGridView

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickGridView::QQuickGridView(QQuickItem *parent)
    self._noteCreation(QQuickGridView, lambda: Rituals.call(
        'ritual_ZN14QQuickGridViewC1EP10QQuickItem', self._addressOf(parent),
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

  def moveCurrentIndexUp(self) -> None:
    """
    Calls Qt's 'void QQuickGridView::moveCurrentIndexUp()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgridview.html#moveCurrentIndexUp
    """
    #  void QQuickGridView::moveCurrentIndexUp()
    self.uglySide.call('ritual_ZN14QQuickGridView18moveCurrentIndexUpEv')

  def moveCurrentIndexDown(self) -> None:
    """
    Calls Qt's 'void QQuickGridView::moveCurrentIndexDown()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgridview.html#moveCurrentIndexDown
    """
    #  void QQuickGridView::moveCurrentIndexDown()
    self.uglySide.call('ritual_ZN14QQuickGridView20moveCurrentIndexDownEv')

  def moveCurrentIndexLeft(self) -> None:
    """
    Calls Qt's 'void QQuickGridView::moveCurrentIndexLeft()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgridview.html#moveCurrentIndexLeft
    """
    #  void QQuickGridView::moveCurrentIndexLeft()
    self.uglySide.call('ritual_ZN14QQuickGridView20moveCurrentIndexLeftEv')

  def moveCurrentIndexRight(self) -> None:
    """
    Calls Qt's 'void QQuickGridView::moveCurrentIndexRight()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgridview.html#moveCurrentIndexRight
    """
    #  void QQuickGridView::moveCurrentIndexRight()
    self.uglySide.call('ritual_ZN14QQuickGridView21moveCurrentIndexRightEv')

  def cellWidthChanged(self) -> None:
    """
    Calls Qt's 'void QQuickGridView::cellWidthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgridview.html#cellWidthChanged
    """
    #  void QQuickGridView::cellWidthChanged()
    self.uglySide.call('ritual_ZN14QQuickGridView16cellWidthChangedEv')

  def cellHeightChanged(self) -> None:
    """
    Calls Qt's 'void QQuickGridView::cellHeightChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgridview.html#cellHeightChanged
    """
    #  void QQuickGridView::cellHeightChanged()
    self.uglySide.call('ritual_ZN14QQuickGridView17cellHeightChangedEv')

  def highlightMoveDurationChanged(self) -> None:
    """
    Calls Qt's 'void QQuickGridView::highlightMoveDurationChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgridview.html#highlightMoveDurationChanged
    """
    #  void QQuickGridView::highlightMoveDurationChanged()
    self.uglySide.call(
        'ritual_ZN14QQuickGridView28highlightMoveDurationChangedEv',
    )

  def flowChanged(self) -> None:
    """
    Calls Qt's 'void QQuickGridView::flowChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgridview.html#flowChanged
    """
    #  void QQuickGridView::flowChanged()
    self.uglySide.call('ritual_ZN14QQuickGridView11flowChangedEv')

  def snapModeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickGridView::snapModeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgridview.html#snapModeChanged
    """
    #  void QQuickGridView::snapModeChanged()
    self.uglySide.call('ritual_ZN14QQuickGridView15snapModeChangedEv')

  @overload(Qt.Orientations)
  def viewportMoved(self, a0: Qt.Orientations) -> None:
    """
    Calls Qt's 'void QQuickGridView::viewportMoved(Qt::Orientations a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgridview.html#viewportMoved

    Parameters
    ----------

    a0 : Qt.Orientations
      Passed on as its number.
    """
    #  void QQuickGridView::viewportMoved(Qt::Orientations a0)
    ritual = (
        'ritual_ZN14QQuickGridView13viewportMovedE6QFlagsIN2Qt11Orientation'
        'EE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QQuickGridView13viewportMovedE6QFlagsIN2Qt11Orien'
          'tationEE')
    self.uglySide.call(ritual, a0.value)

  @overload(QKeyEvent)
  @overload(NoneType)
  def keyPressEvent(self, a0: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void QQuickGridView::keyPressEvent(QKeyEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgridview.html#keyPressEvent

    Parameters
    ----------

    a0 : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGridView::keyPressEvent(QKeyEvent *a0)
    ritual = 'ritual_ZN14QQuickGridView13keyPressEventEP9QKeyEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QQuickGridView13keyPressEventEP9QKeyEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QRectF, QRectF)
  def geometryChange(self, newGeometry: QRectF, oldGeometry: QRectF) -> None:
    """
    Calls Qt's 'void QQuickGridView::geometryChange(const QRectF
    &newGeometry, const QRectF &oldGeometry)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgridview.html#geometryChange

    Parameters
    ----------

    newGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    oldGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QQuickGridView::geometryChange(const QRectF &newGeometry, const
    #      QRectF &oldGeometry)
    ritual = 'ritual_ZN14QQuickGridView14geometryChangeERK6QRectFS2_'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QQuickGridView14geometryChangeERK6QRectFS2_'
    self.uglySide.call(
        ritual, self._valueOf(newGeometry), self._valueOf(oldGeometry),
    )

  @overload(int, QObject)
  @overload(int, NoneType)
  def initItem(self, index: int, item: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QQuickGridView::initItem(int index, QObject *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgridview.html#initItem

    Parameters
    ----------

    index : int
      Passed on as it is.

    item : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGridView::initItem(int index, QObject *item)
    ritual = 'ritual_ZN14QQuickGridView8initItemEiP7QObject'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QQuickGridView8initItemEiP7QObject'
    self.uglySide.call(ritual, index, self._addressOf(item, 'QObject'))
