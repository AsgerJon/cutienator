"""
QQuickListView binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquicklistview_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQuickListView to be private: it declares the class in a header
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
  from . import QQuickListViewAttached, QQuickViewSection
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QKeyEvent = WAIT['QKeyEvent']
  QRectF = WAIT['QRectF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickListView(QQuickItemView):
  """
  The cute side of Qt's QQuickListView: a plain Python object standing in
  front of one C++ QQuickListView.

  It is built on the cute 'QQuickItemView', as Qt's QQuickListView is built
  on Qt's QQuickItemView, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickListView that has a ritual and that Python can
  call so far, 40 names in all: 'metaObject', 'tr', 'spacing', 'setSpacing',
  'orientation', 'setOrientation', 'sectionCriteria', 'currentSection',
  'setHighlightFollowsCurrentItem', 'highlightMoveVelocity',
  'setHighlightMoveVelocity', 'highlightResizeVelocity',
  'setHighlightResizeVelocity', 'highlightResizeDuration',
  'setHighlightResizeDuration', 'setHighlightMoveDuration', 'snapMode',
  'setSnapMode', 'headerPositioning', 'setHeaderPositioning',
  'footerPositioning', 'setFooterPositioning', 'qmlAttachedProperties',
  'incrementCurrentIndex', 'decrementCurrentIndex', 'spacingChanged',
  'orientationChanged', 'currentSectionChanged',
  'highlightMoveVelocityChanged', 'highlightResizeVelocityChanged',
  'highlightResizeDurationChanged', 'snapModeChanged',
  'headerPositioningChanged', 'footerPositioningChanged', 'viewportMoved',
  'keyPressEvent', 'geometryChange', 'initItem', 'maxYExtent', 'maxXExtent'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickListView::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQuickListView::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickListViewPrivate *QQuickListView::d_func()': gives
    'QQuickListViewPrivate', which has no cute class yet.
  - Qt's 'const QQuickListViewPrivate *QQuickListView::d_func() const': gives
    'QQuickListViewPrivate', which has no cute class yet.
  - Qt's 'void QQuickListView::qt_qmlMarker_attached()': one of Qt's own
    inner workings.
  - Qt's 'QQuickListView::~QQuickListView()': the destructor: Python never
    removes a C++ QQuickListView.

  What has no ritual
  ------------------

  2 of the 49 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickListView is created at the first use, not by
    'QQuickListView(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickListView.
  - Qt tells when it has removed the C++ QQuickListView. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QQuickListView, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class FooterPositioning(CuteNum):
    """
    The enum 'QQuickListView::FooterPositioning' of Qt, with the 3 names Qt
    gives in it.
    """

    InlineFooter = Kee[int](0)
    OverlayFooter = Kee[int](1)
    PullBackFooter = Kee[int](2)

  class HeaderPositioning(CuteNum):
    """
    The enum 'QQuickListView::HeaderPositioning' of Qt, with the 3 names Qt
    gives in it.
    """

    InlineHeader = Kee[int](0)
    OverlayHeader = Kee[int](1)
    PullBackHeader = Kee[int](2)

  class Orientation(CuteNum):
    """
    The enum 'QQuickListView::Orientation' of Qt, with the 2 names Qt gives
    in it.
    """

    Horizontal = Kee[int](1)
    Vertical = Kee[int](2)

  class SnapMode(CuteNum):
    """
    The enum 'QQuickListView::SnapMode' of Qt, with the 3 names Qt gives in
    it.
    """

    NoSnap = Kee[int](0)
    SnapToItem = Kee[int](1)
    SnapOneItem = Kee[int](2)

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
    Calls Qt's 'QString QQuickListView::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicklistview.html#tr

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
    #  QString QQuickListView::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN14QQuickListView2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  def qmlAttachedProperties(
      a0: Optional[QObject],
  ) -> Optional[QQuickListViewAttached]:
    """
    Calls Qt's 'QQuickListViewAttached
    *QQuickListView::qmlAttachedProperties(QObject *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklistview.html#qmlAttachedProperties

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickListViewAttached]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickListViewAttached *QQuickListView::qmlAttachedProperties(QObject
    #      *a0)
    address = Rituals.call(
        'ritual_ZN14QQuickListView21qmlAttachedPropertiesEP7QObject',
        CuteMixin._addressOf(a0, 'QObject'),
    )
    from . import QQuickListViewAttached
    return QQuickListViewAttached._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickListView'

  #  A C++ QQuickListView Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickListView'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickListView::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicklistview.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickListView::metaObject() const
    address = self.uglySide.call('ritual_ZNK14QQuickListView10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def spacing(self) -> float:
    """
    Calls Qt's 'qreal QQuickListView::spacing() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicklistview.html#spacing
    """
    #  qreal QQuickListView::spacing() const
    return self.uglySide.call('ritual_ZNK14QQuickListView7spacingEv')

  def orientation(self) -> Orientation:
    """
    Calls Qt's 'Orientation QQuickListView::orientation() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicklistview.html#orientation

    Returns
    -------

    Orientation
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Orientation(number)'
      gives.
    """
    #  Orientation QQuickListView::orientation() const
    return QQuickListView.Orientation(self.uglySide.call(
        'ritual_ZNK14QQuickListView11orientationEv',
    ))

  def currentSection(self) -> str:
    """
    Calls Qt's 'QString QQuickListView::currentSection() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicklistview.html#currentSection

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickListView::currentSection() const
    return self.uglySide.call('ritual_ZNK14QQuickListView14currentSectionEv')

  def highlightMoveVelocity(self) -> float:
    """
    Calls Qt's 'qreal QQuickListView::highlightMoveVelocity() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklistview.html#highlightMoveVelocity
    """
    #  qreal QQuickListView::highlightMoveVelocity() const
    return self.uglySide.call(
        'ritual_ZNK14QQuickListView21highlightMoveVelocityEv',
    )

  def highlightResizeVelocity(self) -> float:
    """
    Calls Qt's 'qreal QQuickListView::highlightResizeVelocity() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklistview.html#highlightResizeVelocity
    """
    #  qreal QQuickListView::highlightResizeVelocity() const
    return self.uglySide.call(
        'ritual_ZNK14QQuickListView23highlightResizeVelocityEv',
    )

  def highlightResizeDuration(self) -> int:
    """
    Calls Qt's 'int QQuickListView::highlightResizeDuration() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklistview.html#highlightResizeDuration
    """
    #  int QQuickListView::highlightResizeDuration() const
    return self.uglySide.call(
        'ritual_ZNK14QQuickListView23highlightResizeDurationEv',
    )

  def snapMode(self) -> SnapMode:
    """
    Calls Qt's 'SnapMode QQuickListView::snapMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicklistview.html#snapMode

    Returns
    -------

    SnapMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'SnapMode(number)' gives.
    """
    #  SnapMode QQuickListView::snapMode() const
    return QQuickListView.SnapMode(self.uglySide.call(
        'ritual_ZNK14QQuickListView8snapModeEv',
    ))

  def headerPositioning(self) -> HeaderPositioning:
    """
    Calls Qt's 'HeaderPositioning QQuickListView::headerPositioning() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklistview.html#headerPositioning

    Returns
    -------

    HeaderPositioning
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'HeaderPositioning(number)' gives.
    """
    #  HeaderPositioning QQuickListView::headerPositioning() const
    return QQuickListView.HeaderPositioning(self.uglySide.call(
        'ritual_ZNK14QQuickListView17headerPositioningEv',
    ))

  def footerPositioning(self) -> FooterPositioning:
    """
    Calls Qt's 'FooterPositioning QQuickListView::footerPositioning() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklistview.html#footerPositioning

    Returns
    -------

    FooterPositioning
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'FooterPositioning(number)' gives.
    """
    #  FooterPositioning QQuickListView::footerPositioning() const
    return QQuickListView.FooterPositioning(self.uglySide.call(
        'ritual_ZNK14QQuickListView17footerPositioningEv',
    ))

  def maxYExtent(self) -> float:
    """
    Calls Qt's 'qreal QQuickListView::maxYExtent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicklistview.html#maxYExtent
    """
    #  qreal QQuickListView::maxYExtent() const
    ritual = 'ritual_ZNK14QQuickListView10maxYExtentEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QQuickListView10maxYExtentEv'
    return self.uglySide.call(ritual)

  def maxXExtent(self) -> float:
    """
    Calls Qt's 'qreal QQuickListView::maxXExtent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicklistview.html#maxXExtent
    """
    #  qreal QQuickListView::maxXExtent() const
    ritual = 'ritual_ZNK14QQuickListView10maxXExtentEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QQuickListView10maxXExtentEv'
    return self.uglySide.call(ritual)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setSpacing(self, spacing: float) -> None:
    """
    Calls Qt's 'void QQuickListView::setSpacing(qreal spacing)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicklistview.html#setSpacing

    Parameters
    ----------

    spacing : float
      Passed on as it is.
    """
    #  void QQuickListView::setSpacing(qreal spacing)
    self.uglySide.call('ritual_ZN14QQuickListView10setSpacingEd', spacing)

  @overload(Orientation)
  def setOrientation(self, a0: Orientation) -> None:
    """
    Calls Qt's 'void QQuickListView::setOrientation(Orientation a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicklistview.html#setOrientation

    Parameters
    ----------

    a0 : Orientation
      Passed on as its number.
    """
    #  void QQuickListView::setOrientation(Orientation a0)
    self.uglySide.call(
        'ritual_ZN14QQuickListView14setOrientationENS_11OrientationE',
        a0.value,
    )

  @overload(bool)
  def setHighlightFollowsCurrentItem(self, a0: bool) -> None:
    """
    Calls Qt's 'void QQuickListView::setHighlightFollowsCurrentItem(bool
    a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklistview.html#setHighlightFollowsCurrentItem

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QQuickListView::setHighlightFollowsCurrentItem(bool a0)
    ritual = 'ritual_ZN14QQuickListView30setHighlightFollowsCurrentItemEb'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QQuickListView30setHighlightFollowsCurrentItemEb')
    self.uglySide.call(ritual, a0)

  @overload(float)
  def setHighlightMoveVelocity(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickListView::setHighlightMoveVelocity(qreal a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklistview.html#setHighlightMoveVelocity

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickListView::setHighlightMoveVelocity(qreal a0)
    self.uglySide.call(
        'ritual_ZN14QQuickListView24setHighlightMoveVelocityEd', a0,
    )

  @overload(float)
  def setHighlightResizeVelocity(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickListView::setHighlightResizeVelocity(qreal a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklistview.html#setHighlightResizeVelocity

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickListView::setHighlightResizeVelocity(qreal a0)
    self.uglySide.call(
        'ritual_ZN14QQuickListView26setHighlightResizeVelocityEd', a0,
    )

  @overload(int)
  def setHighlightResizeDuration(self, a0: int) -> None:
    """
    Calls Qt's 'void QQuickListView::setHighlightResizeDuration(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklistview.html#setHighlightResizeDuration

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQuickListView::setHighlightResizeDuration(int a0)
    self.uglySide.call(
        'ritual_ZN14QQuickListView26setHighlightResizeDurationEi', a0,
    )

  @overload(int)
  def setHighlightMoveDuration(self, a0: int) -> None:
    """
    Calls Qt's 'void QQuickListView::setHighlightMoveDuration(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklistview.html#setHighlightMoveDuration

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQuickListView::setHighlightMoveDuration(int a0)
    ritual = 'ritual_ZN14QQuickListView24setHighlightMoveDurationEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QQuickListView24setHighlightMoveDurationEi'
    self.uglySide.call(ritual, a0)

  @overload(SnapMode)
  def setSnapMode(self, mode: SnapMode) -> None:
    """
    Calls Qt's 'void QQuickListView::setSnapMode(SnapMode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicklistview.html#setSnapMode

    Parameters
    ----------

    mode : SnapMode
      Passed on as its number.
    """
    #  void QQuickListView::setSnapMode(SnapMode mode)
    self.uglySide.call(
        'ritual_ZN14QQuickListView11setSnapModeENS_8SnapModeE', mode.value,
    )

  @overload(HeaderPositioning)
  def setHeaderPositioning(self, positioning: HeaderPositioning) -> None:
    """
    Calls Qt's 'void QQuickListView::setHeaderPositioning(HeaderPositioning
    positioning)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklistview.html#setHeaderPositioning

    Parameters
    ----------

    positioning : HeaderPositioning
      Passed on as its number.
    """
    #  void QQuickListView::setHeaderPositioning(HeaderPositioning
    #      positioning)
    self.uglySide.call(
        'ritual_ZN14QQuickListView20setHeaderPositioningENS_17HeaderPositio'
        'ningE',
        positioning.value,
    )

  @overload(FooterPositioning)
  def setFooterPositioning(self, positioning: FooterPositioning) -> None:
    """
    Calls Qt's 'void QQuickListView::setFooterPositioning(FooterPositioning
    positioning)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklistview.html#setFooterPositioning

    Parameters
    ----------

    positioning : FooterPositioning
      Passed on as its number.
    """
    #  void QQuickListView::setFooterPositioning(FooterPositioning
    #      positioning)
    self.uglySide.call(
        'ritual_ZN14QQuickListView20setFooterPositioningENS_17FooterPositio'
        'ningE',
        positioning.value,
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
    Notes what was given, for Qt's 'QQuickListView::QQuickListView(QQuickItem
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qquicklistview.html#QQuickListView

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickListView::QQuickListView(QQuickItem *parent)
    self._noteCreation(QQuickListView, lambda: Rituals.call(
        'ritual_ZN14QQuickListViewC1EP10QQuickItem', self._addressOf(parent),
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

  def sectionCriteria(self) -> Optional[QQuickViewSection]:
    """
    Calls Qt's 'QQuickViewSection *QQuickListView::sectionCriteria()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklistview.html#sectionCriteria

    Returns
    -------

    Optional[QQuickViewSection]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickViewSection *QQuickListView::sectionCriteria()
    address = self.uglySide.call(
        'ritual_ZN14QQuickListView15sectionCriteriaEv',
    )
    from . import QQuickViewSection
    return QQuickViewSection._cuteAt(address)

  def incrementCurrentIndex(self) -> None:
    """
    Calls Qt's 'void QQuickListView::incrementCurrentIndex()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklistview.html#incrementCurrentIndex
    """
    #  void QQuickListView::incrementCurrentIndex()
    self.uglySide.call('ritual_ZN14QQuickListView21incrementCurrentIndexEv')

  def decrementCurrentIndex(self) -> None:
    """
    Calls Qt's 'void QQuickListView::decrementCurrentIndex()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklistview.html#decrementCurrentIndex
    """
    #  void QQuickListView::decrementCurrentIndex()
    self.uglySide.call('ritual_ZN14QQuickListView21decrementCurrentIndexEv')

  def spacingChanged(self) -> None:
    """
    Calls Qt's 'void QQuickListView::spacingChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicklistview.html#spacingChanged
    """
    #  void QQuickListView::spacingChanged()
    self.uglySide.call('ritual_ZN14QQuickListView14spacingChangedEv')

  def orientationChanged(self) -> None:
    """
    Calls Qt's 'void QQuickListView::orientationChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklistview.html#orientationChanged
    """
    #  void QQuickListView::orientationChanged()
    self.uglySide.call('ritual_ZN14QQuickListView18orientationChangedEv')

  def currentSectionChanged(self) -> None:
    """
    Calls Qt's 'void QQuickListView::currentSectionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklistview.html#currentSectionChanged
    """
    #  void QQuickListView::currentSectionChanged()
    self.uglySide.call('ritual_ZN14QQuickListView21currentSectionChangedEv')

  def highlightMoveVelocityChanged(self) -> None:
    """
    Calls Qt's 'void QQuickListView::highlightMoveVelocityChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklistview.html#highlightMoveVelocityChanged
    """
    #  void QQuickListView::highlightMoveVelocityChanged()
    self.uglySide.call(
        'ritual_ZN14QQuickListView28highlightMoveVelocityChangedEv',
    )

  def highlightResizeVelocityChanged(self) -> None:
    """
    Calls Qt's 'void QQuickListView::highlightResizeVelocityChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklistview.html#highlightResizeVelocityChanged
    """
    #  void QQuickListView::highlightResizeVelocityChanged()
    self.uglySide.call(
        'ritual_ZN14QQuickListView30highlightResizeVelocityChangedEv',
    )

  def highlightResizeDurationChanged(self) -> None:
    """
    Calls Qt's 'void QQuickListView::highlightResizeDurationChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklistview.html#highlightResizeDurationChanged
    """
    #  void QQuickListView::highlightResizeDurationChanged()
    self.uglySide.call(
        'ritual_ZN14QQuickListView30highlightResizeDurationChangedEv',
    )

  def snapModeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickListView::snapModeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklistview.html#snapModeChanged
    """
    #  void QQuickListView::snapModeChanged()
    self.uglySide.call('ritual_ZN14QQuickListView15snapModeChangedEv')

  def headerPositioningChanged(self) -> None:
    """
    Calls Qt's 'void QQuickListView::headerPositioningChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklistview.html#headerPositioningChanged
    """
    #  void QQuickListView::headerPositioningChanged()
    self.uglySide.call(
        'ritual_ZN14QQuickListView24headerPositioningChangedEv',
    )

  def footerPositioningChanged(self) -> None:
    """
    Calls Qt's 'void QQuickListView::footerPositioningChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklistview.html#footerPositioningChanged
    """
    #  void QQuickListView::footerPositioningChanged()
    self.uglySide.call(
        'ritual_ZN14QQuickListView24footerPositioningChangedEv',
    )

  @overload(Qt.Orientations)
  def viewportMoved(self, orient: Qt.Orientations) -> None:
    """
    Calls Qt's 'void QQuickListView::viewportMoved(Qt::Orientations orient)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicklistview.html#viewportMoved

    Parameters
    ----------

    orient : Qt.Orientations
      Passed on as its number.
    """
    #  void QQuickListView::viewportMoved(Qt::Orientations orient)
    ritual = (
        'ritual_ZN14QQuickListView13viewportMovedE6QFlagsIN2Qt11Orientation'
        'EE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QQuickListView13viewportMovedE6QFlagsIN2Qt11Orien'
          'tationEE')
    self.uglySide.call(ritual, orient.value)

  @overload(QKeyEvent)
  @overload(NoneType)
  def keyPressEvent(self, a0: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void QQuickListView::keyPressEvent(QKeyEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicklistview.html#keyPressEvent

    Parameters
    ----------

    a0 : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickListView::keyPressEvent(QKeyEvent *a0)
    ritual = 'ritual_ZN14QQuickListView13keyPressEventEP9QKeyEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QQuickListView13keyPressEventEP9QKeyEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QRectF, QRectF)
  def geometryChange(self, newGeometry: QRectF, oldGeometry: QRectF) -> None:
    """
    Calls Qt's 'void QQuickListView::geometryChange(const QRectF
    &newGeometry, const QRectF &oldGeometry)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicklistview.html#geometryChange

    Parameters
    ----------

    newGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    oldGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QQuickListView::geometryChange(const QRectF &newGeometry, const
    #      QRectF &oldGeometry)
    ritual = 'ritual_ZN14QQuickListView14geometryChangeERK6QRectFS2_'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QQuickListView14geometryChangeERK6QRectFS2_'
    self.uglySide.call(
        ritual, self._valueOf(newGeometry), self._valueOf(oldGeometry),
    )

  @overload(int, QObject)
  @overload(int, NoneType)
  def initItem(self, index: int, item: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QQuickListView::initItem(int index, QObject *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicklistview.html#initItem

    Parameters
    ----------

    index : int
      Passed on as it is.

    item : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickListView::initItem(int index, QObject *item)
    ritual = 'ritual_ZN14QQuickListView8initItemEiP7QObject'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QQuickListView8initItemEiP7QObject'
    self.uglySide.call(ritual, index, self._addressOf(item, 'QObject'))
