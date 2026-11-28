"""
QQuickItemView binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickitemview_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQuickItemView to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObject
from . import QQuickFlickable, QQuickItem
from ..QtQmlModels import QQmlDelegateModel

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QRectF, QVariant
  from ..QtQml import QQmlComponent
  from . import QQuickItemViewPrivate, QQuickTransition
  from ..QtQmlModels import QQmlChangeSet
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlChangeSet = WAIT['QQmlChangeSet']
  QQmlComponent = WAIT['QQmlComponent']
  QQuickTransition = WAIT['QQuickTransition']
  QRectF = WAIT['QRectF']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickItemView(QQuickFlickable):
  """
  The cute side of Qt's QQuickItemView: a plain Python object standing in
  front of one C++ QQuickItemView.

  It is built on the cute 'QQuickFlickable', as Qt's QQuickItemView is built
  on Qt's QQuickFlickable, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickItemView that has a ritual and that Python can
  call so far, 128 names in all: 'metaObject', 'tr', 'model', 'setModel',
  'delegate', 'setDelegate', 'count', 'currentIndex', 'setCurrentIndex',
  'currentItem', 'isWrapEnabled', 'setWrapEnabled', 'isKeyNavigationEnabled',
  'setKeyNavigationEnabled', 'cacheBuffer', 'setCacheBuffer',
  'displayMarginBeginning', 'setDisplayMarginBeginning', 'displayMarginEnd',
  'setDisplayMarginEnd', 'layoutDirection', 'setLayoutDirection',
  'effectiveLayoutDirection', 'verticalLayoutDirection',
  'setVerticalLayoutDirection', 'footer', 'setFooter', 'footerItem',
  'header', 'setHeader', 'headerItem', 'populateTransition',
  'setPopulateTransition', 'addTransition', 'setAddTransition',
  'addDisplacedTransition', 'setAddDisplacedTransition', 'moveTransition',
  'setMoveTransition', 'moveDisplacedTransition',
  'setMoveDisplacedTransition', 'removeTransition', 'setRemoveTransition',
  'removeDisplacedTransition', 'setRemoveDisplacedTransition',
  'displacedTransition', 'setDisplacedTransition', 'highlight',
  'setHighlight', 'highlightItem', 'highlightFollowsCurrentItem',
  'setHighlightFollowsCurrentItem', 'highlightRangeMode',
  'setHighlightRangeMode', 'preferredHighlightBegin',
  'setPreferredHighlightBegin', 'resetPreferredHighlightBegin',
  'preferredHighlightEnd', 'setPreferredHighlightEnd',
  'resetPreferredHighlightEnd', 'highlightMoveDuration',
  'setHighlightMoveDuration', 'reuseItems', 'setReuseItems',
  'positionViewAtIndex', 'indexAt', 'itemAt', 'itemAtIndex',
  'positionViewAtBeginning', 'positionViewAtEnd', 'forceLayout',
  'setContentX', 'setContentY', 'originX', 'originY', 'delegateModelAccess',
  'setDelegateModelAccess', 'modelChanged', 'delegateChanged',
  'countChanged', 'currentIndexChanged', 'currentItemChanged',
  'keyNavigationWrapsChanged', 'keyNavigationEnabledChanged',
  'cacheBufferChanged', 'displayMarginBeginningChanged',
  'displayMarginEndChanged', 'layoutDirectionChanged',
  'effectiveLayoutDirectionChanged', 'verticalLayoutDirectionChanged',
  'headerChanged', 'footerChanged', 'headerItemChanged', 'footerItemChanged',
  'populateTransitionChanged', 'addTransitionChanged',
  'addDisplacedTransitionChanged', 'moveTransitionChanged',
  'moveDisplacedTransitionChanged', 'removeTransitionChanged',
  'removeDisplacedTransitionChanged', 'displacedTransitionChanged',
  'highlightChanged', 'highlightItemChanged',
  'highlightFollowsCurrentItemChanged', 'highlightRangeModeChanged',
  'preferredHighlightBeginChanged', 'preferredHighlightEndChanged',
  'highlightMoveDurationChanged', 'reuseItemsChanged',
  'delegateModelAccessChanged', 'updatePolish', 'componentComplete',
  'geometryChange', 'minYExtent', 'maxYExtent', 'minXExtent', 'maxXExtent',
  'destroyRemoved', 'createdItem', 'initItem', 'modelUpdated',
  'destroyingItem', 'onItemPooled', 'onItemReused', 'animStopped',
  'trackedPositionChanged', 'd_func'. None can be made from Python: one comes
  out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickItemView::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQuickItemView::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickItemView::qt_qmlMarker_uncreatable()': one of Qt's own
    inner workings.
  - Qt's 'QQuickItemView::QQuickItemView(QQuickFlickablePrivate &dd,
    QQuickItem *parent)': takes a type Python has no way to hand over yet.
  - Qt's 'QQuickItemView::~QQuickItemView()': the destructor: Python never
    removes a C++ QQuickItemView.
  - Qt's 'const QQuickItemViewPrivate *QQuickItemView::d_func() const': takes
    in Python what 'QQuickItemViewPrivate *QQuickItemView::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 136 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickItemView is created at the first use, not by
    'QQuickItemView(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickItemView.
  - Qt tells when it has removed the C++ QQuickItemView. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickItemView that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The enums Qt writes inside QQuickItemView, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class HighlightRangeMode(CuteNum):
    """
    The enum 'QQuickItemView::HighlightRangeMode' of Qt, with the 3 names Qt
    gives in it.
    """

    NoHighlightRange = Kee[int](0)
    ApplyRange = Kee[int](1)
    StrictlyEnforceRange = Kee[int](2)

  class LayoutDirection(CuteNum):
    """
    The enum 'QQuickItemView::LayoutDirection' of Qt, with the 4 names Qt
    gives in it.
    """

    LeftToRight = Kee[int](0)
    RightToLeft = Kee[int](1)
    VerticalTopToBottom = Kee[int](2)
    VerticalBottomToTop = Kee[int](3)

  class PositionMode(CuteNum):
    """
    The enum 'QQuickItemView::PositionMode' of Qt, with the 6 names Qt gives
    in it.
    """

    Beginning = Kee[int](0)
    Center = Kee[int](1)
    End = Kee[int](2)
    Visible = Kee[int](3)
    Contain = Kee[int](4)
    SnapPosition = Kee[int](5)

  class VerticalLayoutDirection(CuteNum):
    """
    The enum 'QQuickItemView::VerticalLayoutDirection' of Qt, with the 2
    names Qt gives in it.
    """

    TopToBottom = Kee[int](2)
    BottomToTop = Kee[int](3)

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
    Calls Qt's 'QString QQuickItemView::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemview.html#tr

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
    #  QString QQuickItemView::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN14QQuickItemView2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickItemView'

  #  A C++ QQuickItemView Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickItemView'

  #  The functions Qt calls itself that QQuickItemView is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'setHighlightFollowsCurrentItem': (
          ('_ZN14QQuickItemView30setHighlightFollowsCurrentItemEb',
           ('nothing', 'nothing', ''),
           (
               ('bool', 'number', ''),
           )),
      ),
      'setHighlightMoveDuration': (
          ('_ZN14QQuickItemView24setHighlightMoveDurationEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'initItem': (
          ('_ZN14QQuickItemView8initItemEiP7QObject',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('address', 'address', 'QtCore:QObject'),
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
    Calls Qt's 'const QMetaObject *QQuickItemView::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemview.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickItemView::metaObject() const
    address = self.uglySide.call('ritual_ZNK14QQuickItemView10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def model(self) -> QVariant:
    """
    Calls Qt's 'QVariant QQuickItemView::model() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemview.html#model

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQuickItemView::model() const
    address = self.uglySide.call('ritual_ZNK14QQuickItemView5modelEv')
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def delegate(self) -> Optional[QQmlComponent]:
    """
    Calls Qt's 'QQmlComponent *QQuickItemView::delegate() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemview.html#delegate

    Returns
    -------

    Optional[QQmlComponent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlComponent *QQuickItemView::delegate() const
    address = self.uglySide.call('ritual_ZNK14QQuickItemView8delegateEv')
    from ..QtQml import QQmlComponent
    return QQmlComponent._cuteAt(address)

  def count(self) -> int:
    """
    Calls Qt's 'int QQuickItemView::count() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemview.html#count
    """
    #  int QQuickItemView::count() const
    return self.uglySide.call('ritual_ZNK14QQuickItemView5countEv')

  def currentIndex(self) -> int:
    """
    Calls Qt's 'int QQuickItemView::currentIndex() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemview.html#currentIndex
    """
    #  int QQuickItemView::currentIndex() const
    return self.uglySide.call('ritual_ZNK14QQuickItemView12currentIndexEv')

  def currentItem(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickItemView::currentItem() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemview.html#currentItem

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickItemView::currentItem() const
    address = self.uglySide.call('ritual_ZNK14QQuickItemView11currentItemEv')
    return QQuickItem._cuteAt(address)

  def isWrapEnabled(self) -> bool:
    """
    Calls Qt's 'bool QQuickItemView::isWrapEnabled() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemview.html#isWrapEnabled
    """
    #  bool QQuickItemView::isWrapEnabled() const
    return self.uglySide.call('ritual_ZNK14QQuickItemView13isWrapEnabledEv')

  def isKeyNavigationEnabled(self) -> bool:
    """
    Calls Qt's 'bool QQuickItemView::isKeyNavigationEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemview.html#isKeyNavigationEnabled
    """
    #  bool QQuickItemView::isKeyNavigationEnabled() const
    return self.uglySide.call(
        'ritual_ZNK14QQuickItemView22isKeyNavigationEnabledEv',
    )

  def cacheBuffer(self) -> int:
    """
    Calls Qt's 'int QQuickItemView::cacheBuffer() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemview.html#cacheBuffer
    """
    #  int QQuickItemView::cacheBuffer() const
    return self.uglySide.call('ritual_ZNK14QQuickItemView11cacheBufferEv')

  def displayMarginBeginning(self) -> int:
    """
    Calls Qt's 'int QQuickItemView::displayMarginBeginning() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemview.html#displayMarginBeginning
    """
    #  int QQuickItemView::displayMarginBeginning() const
    return self.uglySide.call(
        'ritual_ZNK14QQuickItemView22displayMarginBeginningEv',
    )

  def displayMarginEnd(self) -> int:
    """
    Calls Qt's 'int QQuickItemView::displayMarginEnd() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemview.html#displayMarginEnd
    """
    #  int QQuickItemView::displayMarginEnd() const
    return self.uglySide.call(
        'ritual_ZNK14QQuickItemView16displayMarginEndEv',
    )

  def layoutDirection(self) -> Qt.LayoutDirection:
    """
    Calls Qt's 'Qt::LayoutDirection QQuickItemView::layoutDirection() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemview.html#layoutDirection

    Returns
    -------

    Qt.LayoutDirection
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.LayoutDirection(number)' gives.
    """
    #  Qt::LayoutDirection QQuickItemView::layoutDirection() const
    return Qt.LayoutDirection(self.uglySide.call(
        'ritual_ZNK14QQuickItemView15layoutDirectionEv',
    ))

  def effectiveLayoutDirection(self) -> Qt.LayoutDirection:
    """
    Calls Qt's 'Qt::LayoutDirection
    QQuickItemView::effectiveLayoutDirection() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemview.html#effectiveLayoutDirection

    Returns
    -------

    Qt.LayoutDirection
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.LayoutDirection(number)' gives.
    """
    #  Qt::LayoutDirection QQuickItemView::effectiveLayoutDirection() const
    return Qt.LayoutDirection(self.uglySide.call(
        'ritual_ZNK14QQuickItemView24effectiveLayoutDirectionEv',
    ))

  def verticalLayoutDirection(self) -> VerticalLayoutDirection:
    """
    Calls Qt's 'VerticalLayoutDirection
    QQuickItemView::verticalLayoutDirection() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemview.html#verticalLayoutDirection

    Returns
    -------

    VerticalLayoutDirection
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'VerticalLayoutDirection(number)' gives.
    """
    #  VerticalLayoutDirection QQuickItemView::verticalLayoutDirection()
    #      const
    return QQuickItemView.VerticalLayoutDirection(self.uglySide.call(
        'ritual_ZNK14QQuickItemView23verticalLayoutDirectionEv',
    ))

  def footer(self) -> Optional[QQmlComponent]:
    """
    Calls Qt's 'QQmlComponent *QQuickItemView::footer() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemview.html#footer

    Returns
    -------

    Optional[QQmlComponent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlComponent *QQuickItemView::footer() const
    address = self.uglySide.call('ritual_ZNK14QQuickItemView6footerEv')
    from ..QtQml import QQmlComponent
    return QQmlComponent._cuteAt(address)

  def footerItem(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickItemView::footerItem() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemview.html#footerItem

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickItemView::footerItem() const
    address = self.uglySide.call('ritual_ZNK14QQuickItemView10footerItemEv')
    return QQuickItem._cuteAt(address)

  def header(self) -> Optional[QQmlComponent]:
    """
    Calls Qt's 'QQmlComponent *QQuickItemView::header() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemview.html#header

    Returns
    -------

    Optional[QQmlComponent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlComponent *QQuickItemView::header() const
    address = self.uglySide.call('ritual_ZNK14QQuickItemView6headerEv')
    from ..QtQml import QQmlComponent
    return QQmlComponent._cuteAt(address)

  def headerItem(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickItemView::headerItem() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemview.html#headerItem

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickItemView::headerItem() const
    address = self.uglySide.call('ritual_ZNK14QQuickItemView10headerItemEv')
    return QQuickItem._cuteAt(address)

  def populateTransition(self) -> Optional[QQuickTransition]:
    """
    Calls Qt's 'QQuickTransition *QQuickItemView::populateTransition()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemview.html#populateTransition

    Returns
    -------

    Optional[QQuickTransition]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickTransition *QQuickItemView::populateTransition() const
    address = self.uglySide.call(
        'ritual_ZNK14QQuickItemView18populateTransitionEv',
    )
    from . import QQuickTransition
    return QQuickTransition._cuteAt(address)

  def addTransition(self) -> Optional[QQuickTransition]:
    """
    Calls Qt's 'QQuickTransition *QQuickItemView::addTransition() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemview.html#addTransition

    Returns
    -------

    Optional[QQuickTransition]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickTransition *QQuickItemView::addTransition() const
    address = self.uglySide.call(
        'ritual_ZNK14QQuickItemView13addTransitionEv',
    )
    from . import QQuickTransition
    return QQuickTransition._cuteAt(address)

  def addDisplacedTransition(self) -> Optional[QQuickTransition]:
    """
    Calls Qt's 'QQuickTransition *QQuickItemView::addDisplacedTransition()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemview.html#addDisplacedTransition

    Returns
    -------

    Optional[QQuickTransition]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickTransition *QQuickItemView::addDisplacedTransition() const
    address = self.uglySide.call(
        'ritual_ZNK14QQuickItemView22addDisplacedTransitionEv',
    )
    from . import QQuickTransition
    return QQuickTransition._cuteAt(address)

  def moveTransition(self) -> Optional[QQuickTransition]:
    """
    Calls Qt's 'QQuickTransition *QQuickItemView::moveTransition() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemview.html#moveTransition

    Returns
    -------

    Optional[QQuickTransition]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickTransition *QQuickItemView::moveTransition() const
    address = self.uglySide.call(
        'ritual_ZNK14QQuickItemView14moveTransitionEv',
    )
    from . import QQuickTransition
    return QQuickTransition._cuteAt(address)

  def moveDisplacedTransition(self) -> Optional[QQuickTransition]:
    """
    Calls Qt's 'QQuickTransition *QQuickItemView::moveDisplacedTransition()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemview.html#moveDisplacedTransition

    Returns
    -------

    Optional[QQuickTransition]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickTransition *QQuickItemView::moveDisplacedTransition() const
    address = self.uglySide.call(
        'ritual_ZNK14QQuickItemView23moveDisplacedTransitionEv',
    )
    from . import QQuickTransition
    return QQuickTransition._cuteAt(address)

  def removeTransition(self) -> Optional[QQuickTransition]:
    """
    Calls Qt's 'QQuickTransition *QQuickItemView::removeTransition() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemview.html#removeTransition

    Returns
    -------

    Optional[QQuickTransition]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickTransition *QQuickItemView::removeTransition() const
    address = self.uglySide.call(
        'ritual_ZNK14QQuickItemView16removeTransitionEv',
    )
    from . import QQuickTransition
    return QQuickTransition._cuteAt(address)

  def removeDisplacedTransition(self) -> Optional[QQuickTransition]:
    """
    Calls Qt's 'QQuickTransition *QQuickItemView::removeDisplacedTransition()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemview.html#removeDisplacedTransition

    Returns
    -------

    Optional[QQuickTransition]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickTransition *QQuickItemView::removeDisplacedTransition() const
    address = self.uglySide.call(
        'ritual_ZNK14QQuickItemView25removeDisplacedTransitionEv',
    )
    from . import QQuickTransition
    return QQuickTransition._cuteAt(address)

  def displacedTransition(self) -> Optional[QQuickTransition]:
    """
    Calls Qt's 'QQuickTransition *QQuickItemView::displacedTransition()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemview.html#displacedTransition

    Returns
    -------

    Optional[QQuickTransition]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickTransition *QQuickItemView::displacedTransition() const
    address = self.uglySide.call(
        'ritual_ZNK14QQuickItemView19displacedTransitionEv',
    )
    from . import QQuickTransition
    return QQuickTransition._cuteAt(address)

  def highlight(self) -> Optional[QQmlComponent]:
    """
    Calls Qt's 'QQmlComponent *QQuickItemView::highlight() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemview.html#highlight

    Returns
    -------

    Optional[QQmlComponent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlComponent *QQuickItemView::highlight() const
    address = self.uglySide.call('ritual_ZNK14QQuickItemView9highlightEv')
    from ..QtQml import QQmlComponent
    return QQmlComponent._cuteAt(address)

  def highlightItem(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickItemView::highlightItem() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemview.html#highlightItem

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickItemView::highlightItem() const
    address = self.uglySide.call(
        'ritual_ZNK14QQuickItemView13highlightItemEv',
    )
    return QQuickItem._cuteAt(address)

  def highlightFollowsCurrentItem(self) -> bool:
    """
    Calls Qt's 'bool QQuickItemView::highlightFollowsCurrentItem() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemview.html#highlightFollowsCurrentItem
    """
    #  bool QQuickItemView::highlightFollowsCurrentItem() const
    return self.uglySide.call(
        'ritual_ZNK14QQuickItemView27highlightFollowsCurrentItemEv',
    )

  def highlightRangeMode(self) -> HighlightRangeMode:
    """
    Calls Qt's 'HighlightRangeMode QQuickItemView::highlightRangeMode()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemview.html#highlightRangeMode

    Returns
    -------

    HighlightRangeMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'HighlightRangeMode(number)' gives.
    """
    #  HighlightRangeMode QQuickItemView::highlightRangeMode() const
    return QQuickItemView.HighlightRangeMode(self.uglySide.call(
        'ritual_ZNK14QQuickItemView18highlightRangeModeEv',
    ))

  def preferredHighlightBegin(self) -> float:
    """
    Calls Qt's 'qreal QQuickItemView::preferredHighlightBegin() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemview.html#preferredHighlightBegin
    """
    #  qreal QQuickItemView::preferredHighlightBegin() const
    return self.uglySide.call(
        'ritual_ZNK14QQuickItemView23preferredHighlightBeginEv',
    )

  def preferredHighlightEnd(self) -> float:
    """
    Calls Qt's 'qreal QQuickItemView::preferredHighlightEnd() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemview.html#preferredHighlightEnd
    """
    #  qreal QQuickItemView::preferredHighlightEnd() const
    return self.uglySide.call(
        'ritual_ZNK14QQuickItemView21preferredHighlightEndEv',
    )

  def highlightMoveDuration(self) -> int:
    """
    Calls Qt's 'int QQuickItemView::highlightMoveDuration() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemview.html#highlightMoveDuration
    """
    #  int QQuickItemView::highlightMoveDuration() const
    return self.uglySide.call(
        'ritual_ZNK14QQuickItemView21highlightMoveDurationEv',
    )

  def reuseItems(self) -> bool:
    """
    Calls Qt's 'bool QQuickItemView::reuseItems() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemview.html#reuseItems
    """
    #  bool QQuickItemView::reuseItems() const
    return self.uglySide.call('ritual_ZNK14QQuickItemView10reuseItemsEv')

  @overload(float, float)
  def indexAt(self, x: float, y: float) -> int:
    """
    Calls Qt's 'int QQuickItemView::indexAt(qreal x, qreal y) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemview.html#indexAt

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  int QQuickItemView::indexAt(qreal x, qreal y) const
    return self.uglySide.call('ritual_ZNK14QQuickItemView7indexAtEdd', x, y)

  @overload(float, float)
  def itemAt(self, x: float, y: float) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickItemView::itemAt(qreal x, qreal y) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemview.html#itemAt

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickItemView::itemAt(qreal x, qreal y) const
    address = self.uglySide.call(
        'ritual_ZNK14QQuickItemView6itemAtEdd', x, y,
    )
    return QQuickItem._cuteAt(address)

  @overload(int)
  def itemAtIndex(self, index: int) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickItemView::itemAtIndex(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemview.html#itemAtIndex

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickItemView::itemAtIndex(int index) const
    address = self.uglySide.call(
        'ritual_ZNK14QQuickItemView11itemAtIndexEi', index,
    )
    return QQuickItem._cuteAt(address)

  def originX(self) -> float:
    """
    Calls Qt's 'qreal QQuickItemView::originX() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemview.html#originX
    """
    #  qreal QQuickItemView::originX() const
    ritual = 'ritual_ZNK14QQuickItemView7originXEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QQuickItemView7originXEv'
    return self.uglySide.call(ritual)

  def originY(self) -> float:
    """
    Calls Qt's 'qreal QQuickItemView::originY() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemview.html#originY
    """
    #  qreal QQuickItemView::originY() const
    ritual = 'ritual_ZNK14QQuickItemView7originYEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QQuickItemView7originYEv'
    return self.uglySide.call(ritual)

  def delegateModelAccess(self) -> QQmlDelegateModel.DelegateModelAccess:
    """
    Calls Qt's 'QQmlDelegateModel::DelegateModelAccess
    QQuickItemView::delegateModelAccess() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemview.html#delegateModelAccess

    Returns
    -------

    QQmlDelegateModel.DelegateModelAccess
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQmlDelegateModel.DelegateModelAccess(number)' gives.
    """
    #  QQmlDelegateModel::DelegateModelAccess
    #      QQuickItemView::delegateModelAccess() const
    return QQmlDelegateModel.DelegateModelAccess(self.uglySide.call(
        'ritual_ZNK14QQuickItemView19delegateModelAccessEv',
    ))

  def minYExtent(self) -> float:
    """
    Calls Qt's 'qreal QQuickItemView::minYExtent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemview.html#minYExtent
    """
    #  qreal QQuickItemView::minYExtent() const
    ritual = 'ritual_ZNK14QQuickItemView10minYExtentEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QQuickItemView10minYExtentEv'
    return self.uglySide.call(ritual)

  def maxYExtent(self) -> float:
    """
    Calls Qt's 'qreal QQuickItemView::maxYExtent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemview.html#maxYExtent
    """
    #  qreal QQuickItemView::maxYExtent() const
    ritual = 'ritual_ZNK14QQuickItemView10maxYExtentEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QQuickItemView10maxYExtentEv'
    return self.uglySide.call(ritual)

  def minXExtent(self) -> float:
    """
    Calls Qt's 'qreal QQuickItemView::minXExtent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemview.html#minXExtent
    """
    #  qreal QQuickItemView::minXExtent() const
    ritual = 'ritual_ZNK14QQuickItemView10minXExtentEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QQuickItemView10minXExtentEv'
    return self.uglySide.call(ritual)

  def maxXExtent(self) -> float:
    """
    Calls Qt's 'qreal QQuickItemView::maxXExtent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemview.html#maxXExtent
    """
    #  qreal QQuickItemView::maxXExtent() const
    ritual = 'ritual_ZNK14QQuickItemView10maxXExtentEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QQuickItemView10maxXExtentEv'
    return self.uglySide.call(ritual)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QVariant)
  def setModel(self, a0: QVariant) -> None:
    """
    Calls Qt's 'void QQuickItemView::setModel(const QVariant &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemview.html#setModel

    Parameters
    ----------

    a0 : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QQuickItemView::setModel(const QVariant &a0)
    self.uglySide.call(
        'ritual_ZN14QQuickItemView8setModelERK8QVariant', self._valueOf(a0),
    )

  @overload(QQmlComponent)
  @overload(NoneType)
  def setDelegate(self, a0: Optional[QQmlComponent]) -> None:
    """
    Calls Qt's 'void QQuickItemView::setDelegate(QQmlComponent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemview.html#setDelegate

    Parameters
    ----------

    a0 : Optional[QQmlComponent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItemView::setDelegate(QQmlComponent *a0)
    self.uglySide.call(
        'ritual_ZN14QQuickItemView11setDelegateEP13QQmlComponent',
        self._addressOf(a0),
    )

  @overload(int)
  def setCurrentIndex(self, idx: int) -> None:
    """
    Calls Qt's 'void QQuickItemView::setCurrentIndex(int idx)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemview.html#setCurrentIndex

    Parameters
    ----------

    idx : int
      Passed on as it is.
    """
    #  void QQuickItemView::setCurrentIndex(int idx)
    self.uglySide.call('ritual_ZN14QQuickItemView15setCurrentIndexEi', idx)

  @overload(bool)
  def setWrapEnabled(self, a0: bool) -> None:
    """
    Calls Qt's 'void QQuickItemView::setWrapEnabled(bool a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemview.html#setWrapEnabled

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QQuickItemView::setWrapEnabled(bool a0)
    self.uglySide.call('ritual_ZN14QQuickItemView14setWrapEnabledEb', a0)

  @overload(bool)
  def setKeyNavigationEnabled(self, a0: bool) -> None:
    """
    Calls Qt's 'void QQuickItemView::setKeyNavigationEnabled(bool a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemview.html#setKeyNavigationEnabled

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QQuickItemView::setKeyNavigationEnabled(bool a0)
    self.uglySide.call(
        'ritual_ZN14QQuickItemView23setKeyNavigationEnabledEb', a0,
    )

  @overload(int)
  def setCacheBuffer(self, a0: int) -> None:
    """
    Calls Qt's 'void QQuickItemView::setCacheBuffer(int a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemview.html#setCacheBuffer

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQuickItemView::setCacheBuffer(int a0)
    self.uglySide.call('ritual_ZN14QQuickItemView14setCacheBufferEi', a0)

  @overload(int)
  def setDisplayMarginBeginning(self, a0: int) -> None:
    """
    Calls Qt's 'void QQuickItemView::setDisplayMarginBeginning(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemview.html#setDisplayMarginBeginning

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQuickItemView::setDisplayMarginBeginning(int a0)
    self.uglySide.call(
        'ritual_ZN14QQuickItemView25setDisplayMarginBeginningEi', a0,
    )

  @overload(int)
  def setDisplayMarginEnd(self, a0: int) -> None:
    """
    Calls Qt's 'void QQuickItemView::setDisplayMarginEnd(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemview.html#setDisplayMarginEnd

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQuickItemView::setDisplayMarginEnd(int a0)
    self.uglySide.call(
        'ritual_ZN14QQuickItemView19setDisplayMarginEndEi', a0,
    )

  @overload(Qt.LayoutDirection)
  def setLayoutDirection(self, a0: Qt.LayoutDirection) -> None:
    """
    Calls Qt's 'void QQuickItemView::setLayoutDirection(Qt::LayoutDirection
    a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemview.html#setLayoutDirection

    Parameters
    ----------

    a0 : Qt.LayoutDirection
      Passed on as its number.
    """
    #  void QQuickItemView::setLayoutDirection(Qt::LayoutDirection a0)
    self.uglySide.call(
        'ritual_ZN14QQuickItemView18setLayoutDirectionEN2Qt15LayoutDirectio'
        'nE',
        a0.value,
    )

  @overload(VerticalLayoutDirection)
  def setVerticalLayoutDirection(
      self,
      layoutDirection: VerticalLayoutDirection,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickItemView::setVerticalLayoutDirection(VerticalLayoutDirection
    layoutDirection)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemview.html#setVerticalLayoutDirection

    Parameters
    ----------

    layoutDirection : VerticalLayoutDirection
      Passed on as its number.
    """
    #  void
    #      QQuickItemView::setVerticalLayoutDirection(VerticalLayoutDirection
    #      layoutDirection)
    self.uglySide.call(
        'ritual_ZN14QQuickItemView26setVerticalLayoutDirectionENS_23Vertica'
        'lLayoutDirectionE',
        layoutDirection.value,
    )

  @overload(QQmlComponent)
  @overload(NoneType)
  def setFooter(self, a0: Optional[QQmlComponent]) -> None:
    """
    Calls Qt's 'void QQuickItemView::setFooter(QQmlComponent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemview.html#setFooter

    Parameters
    ----------

    a0 : Optional[QQmlComponent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItemView::setFooter(QQmlComponent *a0)
    self.uglySide.call(
        'ritual_ZN14QQuickItemView9setFooterEP13QQmlComponent',
        self._addressOf(a0),
    )

  @overload(QQmlComponent)
  @overload(NoneType)
  def setHeader(self, a0: Optional[QQmlComponent]) -> None:
    """
    Calls Qt's 'void QQuickItemView::setHeader(QQmlComponent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemview.html#setHeader

    Parameters
    ----------

    a0 : Optional[QQmlComponent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItemView::setHeader(QQmlComponent *a0)
    self.uglySide.call(
        'ritual_ZN14QQuickItemView9setHeaderEP13QQmlComponent',
        self._addressOf(a0),
    )

  @overload(QQuickTransition)
  @overload(NoneType)
  def setPopulateTransition(
      self,
      transition: Optional[QQuickTransition],
  ) -> None:
    """
    Calls Qt's 'void QQuickItemView::setPopulateTransition(QQuickTransition
    *transition)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemview.html#setPopulateTransition

    Parameters
    ----------

    transition : Optional[QQuickTransition]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItemView::setPopulateTransition(QQuickTransition
    #      *transition)
    self.uglySide.call(
        'ritual_ZN14QQuickItemView21setPopulateTransitionEP16QQuickTransiti'
        'on',
        self._addressOf(transition),
    )

  @overload(QQuickTransition)
  @overload(NoneType)
  def setAddTransition(self, transition: Optional[QQuickTransition]) -> None:
    """
    Calls Qt's 'void QQuickItemView::setAddTransition(QQuickTransition
    *transition)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemview.html#setAddTransition

    Parameters
    ----------

    transition : Optional[QQuickTransition]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItemView::setAddTransition(QQuickTransition *transition)
    self.uglySide.call(
        'ritual_ZN14QQuickItemView16setAddTransitionEP16QQuickTransition',
        self._addressOf(transition),
    )

  @overload(QQuickTransition)
  @overload(NoneType)
  def setAddDisplacedTransition(
      self,
      transition: Optional[QQuickTransition],
  ) -> None:
    """
    Calls Qt's 'void
    QQuickItemView::setAddDisplacedTransition(QQuickTransition *transition)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemview.html#setAddDisplacedTransition

    Parameters
    ----------

    transition : Optional[QQuickTransition]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItemView::setAddDisplacedTransition(QQuickTransition
    #      *transition)
    self.uglySide.call(
        'ritual_ZN14QQuickItemView25setAddDisplacedTransitionEP16QQuickTran'
        'sition',
        self._addressOf(transition),
    )

  @overload(QQuickTransition)
  @overload(NoneType)
  def setMoveTransition(
      self,
      transition: Optional[QQuickTransition],
  ) -> None:
    """
    Calls Qt's 'void QQuickItemView::setMoveTransition(QQuickTransition
    *transition)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemview.html#setMoveTransition

    Parameters
    ----------

    transition : Optional[QQuickTransition]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItemView::setMoveTransition(QQuickTransition *transition)
    self.uglySide.call(
        'ritual_ZN14QQuickItemView17setMoveTransitionEP16QQuickTransition',
        self._addressOf(transition),
    )

  @overload(QQuickTransition)
  @overload(NoneType)
  def setMoveDisplacedTransition(
      self,
      transition: Optional[QQuickTransition],
  ) -> None:
    """
    Calls Qt's 'void
    QQuickItemView::setMoveDisplacedTransition(QQuickTransition
    *transition)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemview.html#setMoveDisplacedTransition

    Parameters
    ----------

    transition : Optional[QQuickTransition]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItemView::setMoveDisplacedTransition(QQuickTransition
    #      *transition)
    self.uglySide.call(
        'ritual_ZN14QQuickItemView26setMoveDisplacedTransitionEP16QQuickTra'
        'nsition',
        self._addressOf(transition),
    )

  @overload(QQuickTransition)
  @overload(NoneType)
  def setRemoveTransition(
      self,
      transition: Optional[QQuickTransition],
  ) -> None:
    """
    Calls Qt's 'void QQuickItemView::setRemoveTransition(QQuickTransition
    *transition)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemview.html#setRemoveTransition

    Parameters
    ----------

    transition : Optional[QQuickTransition]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItemView::setRemoveTransition(QQuickTransition *transition)
    self.uglySide.call(
        'ritual_ZN14QQuickItemView19setRemoveTransitionEP16QQuickTransition',
        self._addressOf(transition),
    )

  @overload(QQuickTransition)
  @overload(NoneType)
  def setRemoveDisplacedTransition(
      self,
      transition: Optional[QQuickTransition],
  ) -> None:
    """
    Calls Qt's 'void
    QQuickItemView::setRemoveDisplacedTransition(QQuickTransition
    *transition)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemview.html#setRemoveDisplacedTransition

    Parameters
    ----------

    transition : Optional[QQuickTransition]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItemView::setRemoveDisplacedTransition(QQuickTransition
    #      *transition)
    self.uglySide.call(
        'ritual_ZN14QQuickItemView28setRemoveDisplacedTransitionEP16QQuickT'
        'ransition',
        self._addressOf(transition),
    )

  @overload(QQuickTransition)
  @overload(NoneType)
  def setDisplacedTransition(
      self,
      transition: Optional[QQuickTransition],
  ) -> None:
    """
    Calls Qt's 'void QQuickItemView::setDisplacedTransition(QQuickTransition
    *transition)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemview.html#setDisplacedTransition

    Parameters
    ----------

    transition : Optional[QQuickTransition]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItemView::setDisplacedTransition(QQuickTransition
    #      *transition)
    self.uglySide.call(
        'ritual_ZN14QQuickItemView22setDisplacedTransitionEP16QQuickTransit'
        'ion',
        self._addressOf(transition),
    )

  @overload(QQmlComponent)
  @overload(NoneType)
  def setHighlight(self, a0: Optional[QQmlComponent]) -> None:
    """
    Calls Qt's 'void QQuickItemView::setHighlight(QQmlComponent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemview.html#setHighlight

    Parameters
    ----------

    a0 : Optional[QQmlComponent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItemView::setHighlight(QQmlComponent *a0)
    self.uglySide.call(
        'ritual_ZN14QQuickItemView12setHighlightEP13QQmlComponent',
        self._addressOf(a0),
    )

  @overload(bool)
  def setHighlightFollowsCurrentItem(self, a0: bool) -> None:
    """
    Calls Qt's 'void QQuickItemView::setHighlightFollowsCurrentItem(bool
    a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemview.html#setHighlightFollowsCurrentItem

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QQuickItemView::setHighlightFollowsCurrentItem(bool a0)
    ritual = 'ritual_ZN14QQuickItemView30setHighlightFollowsCurrentItemEb'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QQuickItemView30setHighlightFollowsCurrentItemEb')
    self.uglySide.call(ritual, a0)

  @overload(HighlightRangeMode)
  def setHighlightRangeMode(self, mode: HighlightRangeMode) -> None:
    """
    Calls Qt's 'void QQuickItemView::setHighlightRangeMode(HighlightRangeMode
    mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemview.html#setHighlightRangeMode

    Parameters
    ----------

    mode : HighlightRangeMode
      Passed on as its number.
    """
    #  void QQuickItemView::setHighlightRangeMode(HighlightRangeMode mode)
    self.uglySide.call(
        'ritual_ZN14QQuickItemView21setHighlightRangeModeENS_18HighlightRan'
        'geModeE',
        mode.value,
    )

  @overload(float)
  def setPreferredHighlightBegin(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickItemView::setPreferredHighlightBegin(qreal a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemview.html#setPreferredHighlightBegin

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickItemView::setPreferredHighlightBegin(qreal a0)
    self.uglySide.call(
        'ritual_ZN14QQuickItemView26setPreferredHighlightBeginEd', a0,
    )

  @overload(float)
  def setPreferredHighlightEnd(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickItemView::setPreferredHighlightEnd(qreal a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemview.html#setPreferredHighlightEnd

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickItemView::setPreferredHighlightEnd(qreal a0)
    self.uglySide.call(
        'ritual_ZN14QQuickItemView24setPreferredHighlightEndEd', a0,
    )

  @overload(int)
  def setHighlightMoveDuration(self, a0: int) -> None:
    """
    Calls Qt's 'void QQuickItemView::setHighlightMoveDuration(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemview.html#setHighlightMoveDuration

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQuickItemView::setHighlightMoveDuration(int a0)
    ritual = 'ritual_ZN14QQuickItemView24setHighlightMoveDurationEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QQuickItemView24setHighlightMoveDurationEi'
    self.uglySide.call(ritual, a0)

  @overload(bool)
  def setReuseItems(self, reuse: bool) -> None:
    """
    Calls Qt's 'void QQuickItemView::setReuseItems(bool reuse)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemview.html#setReuseItems

    Parameters
    ----------

    reuse : bool
      Passed on as it is.
    """
    #  void QQuickItemView::setReuseItems(bool reuse)
    self.uglySide.call('ritual_ZN14QQuickItemView13setReuseItemsEb', reuse)

  @overload(float)
  def setContentX(self, pos: float) -> None:
    """
    Calls Qt's 'void QQuickItemView::setContentX(qreal pos)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemview.html#setContentX

    Parameters
    ----------

    pos : float
      Passed on as it is.
    """
    #  void QQuickItemView::setContentX(qreal pos)
    ritual = 'ritual_ZN14QQuickItemView11setContentXEd'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QQuickItemView11setContentXEd'
    self.uglySide.call(ritual, pos)

  @overload(float)
  def setContentY(self, pos: float) -> None:
    """
    Calls Qt's 'void QQuickItemView::setContentY(qreal pos)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemview.html#setContentY

    Parameters
    ----------

    pos : float
      Passed on as it is.
    """
    #  void QQuickItemView::setContentY(qreal pos)
    ritual = 'ritual_ZN14QQuickItemView11setContentYEd'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QQuickItemView11setContentYEd'
    self.uglySide.call(ritual, pos)

  @overload(QQmlDelegateModel.DelegateModelAccess)
  def setDelegateModelAccess(
      self,
      delegateModelAccess: QQmlDelegateModel.DelegateModelAccess,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickItemView::setDelegateModelAccess(QQmlDelegateModel::
    DelegateModelAccess delegateModelAccess)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemview.html#setDelegateModelAccess

    Parameters
    ----------

    delegateModelAccess : QQmlDelegateModel.DelegateModelAccess
      Passed on as its number.
    """
    #  void QQuickItemView::setDelegateModelAccess(QQmlDelegateModel::
    #      DelegateModelAccess delegateModelAccess)
    self.uglySide.call(
        'ritual_ZN14QQuickItemView22setDelegateModelAccessEN17QQmlDelegateM'
        'odel19DelegateModelAccessE',
        delegateModelAccess.value,
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QQuickItemView::QQuickItemView(QQuickFlickablePrivate &dd,
    QQuickItem *parent)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuickItemView.__init__' has no cute function yet. Qt's "
        "'QQuickItemView::QQuickItemView(QQuickFlickablePrivate &dd, "
        "QQuickItem *parent)': takes a type Python has no way to hand over "
        "yet.")

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

  def resetPreferredHighlightBegin(self) -> None:
    """
    Calls Qt's 'void QQuickItemView::resetPreferredHighlightBegin()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemview.html#resetPreferredHighlightBegin
    """
    #  void QQuickItemView::resetPreferredHighlightBegin()
    self.uglySide.call(
        'ritual_ZN14QQuickItemView28resetPreferredHighlightBeginEv',
    )

  def resetPreferredHighlightEnd(self) -> None:
    """
    Calls Qt's 'void QQuickItemView::resetPreferredHighlightEnd()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemview.html#resetPreferredHighlightEnd
    """
    #  void QQuickItemView::resetPreferredHighlightEnd()
    self.uglySide.call(
        'ritual_ZN14QQuickItemView26resetPreferredHighlightEndEv',
    )

  @overload(int, int)
  def positionViewAtIndex(self, index: int, mode: int) -> None:
    """
    Calls Qt's 'void QQuickItemView::positionViewAtIndex(int index, int
    mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemview.html#positionViewAtIndex

    Parameters
    ----------

    index : int
      Passed on as it is.

    mode : int
      Passed on as it is.
    """
    #  void QQuickItemView::positionViewAtIndex(int index, int mode)
    self.uglySide.call(
        'ritual_ZN14QQuickItemView19positionViewAtIndexEii', index, mode,
    )

  def positionViewAtBeginning(self) -> None:
    """
    Calls Qt's 'void QQuickItemView::positionViewAtBeginning()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemview.html#positionViewAtBeginning
    """
    #  void QQuickItemView::positionViewAtBeginning()
    self.uglySide.call(
        'ritual_ZN14QQuickItemView23positionViewAtBeginningEv',
    )

  def positionViewAtEnd(self) -> None:
    """
    Calls Qt's 'void QQuickItemView::positionViewAtEnd()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemview.html#positionViewAtEnd
    """
    #  void QQuickItemView::positionViewAtEnd()
    self.uglySide.call('ritual_ZN14QQuickItemView17positionViewAtEndEv')

  def forceLayout(self) -> None:
    """
    Calls Qt's 'void QQuickItemView::forceLayout()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemview.html#forceLayout
    """
    #  void QQuickItemView::forceLayout()
    self.uglySide.call('ritual_ZN14QQuickItemView11forceLayoutEv')

  def modelChanged(self) -> None:
    """
    Calls Qt's 'void QQuickItemView::modelChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemview.html#modelChanged
    """
    #  void QQuickItemView::modelChanged()
    self.uglySide.call('ritual_ZN14QQuickItemView12modelChangedEv')

  def delegateChanged(self) -> None:
    """
    Calls Qt's 'void QQuickItemView::delegateChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemview.html#delegateChanged
    """
    #  void QQuickItemView::delegateChanged()
    self.uglySide.call('ritual_ZN14QQuickItemView15delegateChangedEv')

  def countChanged(self) -> None:
    """
    Calls Qt's 'void QQuickItemView::countChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemview.html#countChanged
    """
    #  void QQuickItemView::countChanged()
    self.uglySide.call('ritual_ZN14QQuickItemView12countChangedEv')

  def currentIndexChanged(self) -> None:
    """
    Calls Qt's 'void QQuickItemView::currentIndexChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemview.html#currentIndexChanged
    """
    #  void QQuickItemView::currentIndexChanged()
    self.uglySide.call('ritual_ZN14QQuickItemView19currentIndexChangedEv')

  def currentItemChanged(self) -> None:
    """
    Calls Qt's 'void QQuickItemView::currentItemChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemview.html#currentItemChanged
    """
    #  void QQuickItemView::currentItemChanged()
    self.uglySide.call('ritual_ZN14QQuickItemView18currentItemChangedEv')

  def keyNavigationWrapsChanged(self) -> None:
    """
    Calls Qt's 'void QQuickItemView::keyNavigationWrapsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemview.html#keyNavigationWrapsChanged
    """
    #  void QQuickItemView::keyNavigationWrapsChanged()
    self.uglySide.call(
        'ritual_ZN14QQuickItemView25keyNavigationWrapsChangedEv',
    )

  def keyNavigationEnabledChanged(self) -> None:
    """
    Calls Qt's 'void QQuickItemView::keyNavigationEnabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemview.html#keyNavigationEnabledChanged
    """
    #  void QQuickItemView::keyNavigationEnabledChanged()
    self.uglySide.call(
        'ritual_ZN14QQuickItemView27keyNavigationEnabledChangedEv',
    )

  def cacheBufferChanged(self) -> None:
    """
    Calls Qt's 'void QQuickItemView::cacheBufferChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemview.html#cacheBufferChanged
    """
    #  void QQuickItemView::cacheBufferChanged()
    self.uglySide.call('ritual_ZN14QQuickItemView18cacheBufferChangedEv')

  def displayMarginBeginningChanged(self) -> None:
    """
    Calls Qt's 'void QQuickItemView::displayMarginBeginningChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemview.html#displayMarginBeginningChanged
    """
    #  void QQuickItemView::displayMarginBeginningChanged()
    self.uglySide.call(
        'ritual_ZN14QQuickItemView29displayMarginBeginningChangedEv',
    )

  def displayMarginEndChanged(self) -> None:
    """
    Calls Qt's 'void QQuickItemView::displayMarginEndChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemview.html#displayMarginEndChanged
    """
    #  void QQuickItemView::displayMarginEndChanged()
    self.uglySide.call(
        'ritual_ZN14QQuickItemView23displayMarginEndChangedEv',
    )

  def layoutDirectionChanged(self) -> None:
    """
    Calls Qt's 'void QQuickItemView::layoutDirectionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemview.html#layoutDirectionChanged
    """
    #  void QQuickItemView::layoutDirectionChanged()
    self.uglySide.call('ritual_ZN14QQuickItemView22layoutDirectionChangedEv')

  def effectiveLayoutDirectionChanged(self) -> None:
    """
    Calls Qt's 'void QQuickItemView::effectiveLayoutDirectionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemview.html
    """
    #  void QQuickItemView::effectiveLayoutDirectionChanged()
    self.uglySide.call(
        'ritual_ZN14QQuickItemView31effectiveLayoutDirectionChangedEv',
    )

  def verticalLayoutDirectionChanged(self) -> None:
    """
    Calls Qt's 'void QQuickItemView::verticalLayoutDirectionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemview.html#verticalLayoutDirectionChanged
    """
    #  void QQuickItemView::verticalLayoutDirectionChanged()
    self.uglySide.call(
        'ritual_ZN14QQuickItemView30verticalLayoutDirectionChangedEv',
    )

  def headerChanged(self) -> None:
    """
    Calls Qt's 'void QQuickItemView::headerChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemview.html#headerChanged
    """
    #  void QQuickItemView::headerChanged()
    self.uglySide.call('ritual_ZN14QQuickItemView13headerChangedEv')

  def footerChanged(self) -> None:
    """
    Calls Qt's 'void QQuickItemView::footerChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemview.html#footerChanged
    """
    #  void QQuickItemView::footerChanged()
    self.uglySide.call('ritual_ZN14QQuickItemView13footerChangedEv')

  def headerItemChanged(self) -> None:
    """
    Calls Qt's 'void QQuickItemView::headerItemChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemview.html#headerItemChanged
    """
    #  void QQuickItemView::headerItemChanged()
    self.uglySide.call('ritual_ZN14QQuickItemView17headerItemChangedEv')

  def footerItemChanged(self) -> None:
    """
    Calls Qt's 'void QQuickItemView::footerItemChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemview.html#footerItemChanged
    """
    #  void QQuickItemView::footerItemChanged()
    self.uglySide.call('ritual_ZN14QQuickItemView17footerItemChangedEv')

  def populateTransitionChanged(self) -> None:
    """
    Calls Qt's 'void QQuickItemView::populateTransitionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemview.html#populateTransitionChanged
    """
    #  void QQuickItemView::populateTransitionChanged()
    self.uglySide.call(
        'ritual_ZN14QQuickItemView25populateTransitionChangedEv',
    )

  def addTransitionChanged(self) -> None:
    """
    Calls Qt's 'void QQuickItemView::addTransitionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemview.html#addTransitionChanged
    """
    #  void QQuickItemView::addTransitionChanged()
    self.uglySide.call('ritual_ZN14QQuickItemView20addTransitionChangedEv')

  def addDisplacedTransitionChanged(self) -> None:
    """
    Calls Qt's 'void QQuickItemView::addDisplacedTransitionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemview.html#addDisplacedTransitionChanged
    """
    #  void QQuickItemView::addDisplacedTransitionChanged()
    self.uglySide.call(
        'ritual_ZN14QQuickItemView29addDisplacedTransitionChangedEv',
    )

  def moveTransitionChanged(self) -> None:
    """
    Calls Qt's 'void QQuickItemView::moveTransitionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemview.html#moveTransitionChanged
    """
    #  void QQuickItemView::moveTransitionChanged()
    self.uglySide.call('ritual_ZN14QQuickItemView21moveTransitionChangedEv')

  def moveDisplacedTransitionChanged(self) -> None:
    """
    Calls Qt's 'void QQuickItemView::moveDisplacedTransitionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemview.html#moveDisplacedTransitionChanged
    """
    #  void QQuickItemView::moveDisplacedTransitionChanged()
    self.uglySide.call(
        'ritual_ZN14QQuickItemView30moveDisplacedTransitionChangedEv',
    )

  def removeTransitionChanged(self) -> None:
    """
    Calls Qt's 'void QQuickItemView::removeTransitionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemview.html#removeTransitionChanged
    """
    #  void QQuickItemView::removeTransitionChanged()
    self.uglySide.call(
        'ritual_ZN14QQuickItemView23removeTransitionChangedEv',
    )

  def removeDisplacedTransitionChanged(self) -> None:
    """
    Calls Qt's 'void QQuickItemView::removeDisplacedTransitionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemview.html
    """
    #  void QQuickItemView::removeDisplacedTransitionChanged()
    self.uglySide.call(
        'ritual_ZN14QQuickItemView32removeDisplacedTransitionChangedEv',
    )

  def displacedTransitionChanged(self) -> None:
    """
    Calls Qt's 'void QQuickItemView::displacedTransitionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemview.html#displacedTransitionChanged
    """
    #  void QQuickItemView::displacedTransitionChanged()
    self.uglySide.call(
        'ritual_ZN14QQuickItemView26displacedTransitionChangedEv',
    )

  def highlightChanged(self) -> None:
    """
    Calls Qt's 'void QQuickItemView::highlightChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemview.html#highlightChanged
    """
    #  void QQuickItemView::highlightChanged()
    self.uglySide.call('ritual_ZN14QQuickItemView16highlightChangedEv')

  def highlightItemChanged(self) -> None:
    """
    Calls Qt's 'void QQuickItemView::highlightItemChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemview.html#highlightItemChanged
    """
    #  void QQuickItemView::highlightItemChanged()
    self.uglySide.call('ritual_ZN14QQuickItemView20highlightItemChangedEv')

  def highlightFollowsCurrentItemChanged(self) -> None:
    """
    Calls Qt's 'void QQuickItemView::highlightFollowsCurrentItemChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemview.html
    """
    #  void QQuickItemView::highlightFollowsCurrentItemChanged()
    self.uglySide.call(
        'ritual_ZN14QQuickItemView34highlightFollowsCurrentItemChangedEv',
    )

  def highlightRangeModeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickItemView::highlightRangeModeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemview.html#highlightRangeModeChanged
    """
    #  void QQuickItemView::highlightRangeModeChanged()
    self.uglySide.call(
        'ritual_ZN14QQuickItemView25highlightRangeModeChangedEv',
    )

  def preferredHighlightBeginChanged(self) -> None:
    """
    Calls Qt's 'void QQuickItemView::preferredHighlightBeginChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemview.html#preferredHighlightBeginChanged
    """
    #  void QQuickItemView::preferredHighlightBeginChanged()
    self.uglySide.call(
        'ritual_ZN14QQuickItemView30preferredHighlightBeginChangedEv',
    )

  def preferredHighlightEndChanged(self) -> None:
    """
    Calls Qt's 'void QQuickItemView::preferredHighlightEndChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemview.html#preferredHighlightEndChanged
    """
    #  void QQuickItemView::preferredHighlightEndChanged()
    self.uglySide.call(
        'ritual_ZN14QQuickItemView28preferredHighlightEndChangedEv',
    )

  def highlightMoveDurationChanged(self) -> None:
    """
    Calls Qt's 'void QQuickItemView::highlightMoveDurationChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemview.html#highlightMoveDurationChanged
    """
    #  void QQuickItemView::highlightMoveDurationChanged()
    self.uglySide.call(
        'ritual_ZN14QQuickItemView28highlightMoveDurationChangedEv',
    )

  def reuseItemsChanged(self) -> None:
    """
    Calls Qt's 'void QQuickItemView::reuseItemsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemview.html#reuseItemsChanged
    """
    #  void QQuickItemView::reuseItemsChanged()
    self.uglySide.call('ritual_ZN14QQuickItemView17reuseItemsChangedEv')

  def delegateModelAccessChanged(self) -> None:
    """
    Calls Qt's 'void QQuickItemView::delegateModelAccessChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemview.html#delegateModelAccessChanged
    """
    #  void QQuickItemView::delegateModelAccessChanged()
    self.uglySide.call(
        'ritual_ZN14QQuickItemView26delegateModelAccessChangedEv',
    )

  def updatePolish(self) -> None:
    """
    Calls Qt's 'void QQuickItemView::updatePolish()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemview.html#updatePolish
    """
    #  void QQuickItemView::updatePolish()
    ritual = 'ritual_ZN14QQuickItemView12updatePolishEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QQuickItemView12updatePolishEv'
    self.uglySide.call(ritual)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickItemView::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemview.html#componentComplete
    """
    #  void QQuickItemView::componentComplete()
    ritual = 'ritual_ZN14QQuickItemView17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QQuickItemView17componentCompleteEv'
    self.uglySide.call(ritual)

  @overload(QRectF, QRectF)
  def geometryChange(self, newGeometry: QRectF, oldGeometry: QRectF) -> None:
    """
    Calls Qt's 'void QQuickItemView::geometryChange(const QRectF
    &newGeometry, const QRectF &oldGeometry)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemview.html#geometryChange

    Parameters
    ----------

    newGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    oldGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QQuickItemView::geometryChange(const QRectF &newGeometry, const
    #      QRectF &oldGeometry)
    ritual = 'ritual_ZN14QQuickItemView14geometryChangeERK6QRectFS2_'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QQuickItemView14geometryChangeERK6QRectFS2_'
    self.uglySide.call(
        ritual, self._valueOf(newGeometry), self._valueOf(oldGeometry),
    )

  def destroyRemoved(self) -> None:
    """
    Calls Qt's 'void QQuickItemView::destroyRemoved()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemview.html#destroyRemoved
    """
    #  void QQuickItemView::destroyRemoved()
    self.uglySide.call('ritual_ZN14QQuickItemView14destroyRemovedEv')

  @overload(int, QObject)
  @overload(int, NoneType)
  def createdItem(self, index: int, item: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QQuickItemView::createdItem(int index, QObject *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemview.html#createdItem

    Parameters
    ----------

    index : int
      Passed on as it is.

    item : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItemView::createdItem(int index, QObject *item)
    self.uglySide.call(
        'ritual_ZN14QQuickItemView11createdItemEiP7QObject',
        index, self._addressOf(item, 'QObject'),
    )

  @overload(int, QObject)
  @overload(int, NoneType)
  def initItem(self, index: int, item: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QQuickItemView::initItem(int index, QObject *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemview.html#initItem

    Parameters
    ----------

    index : int
      Passed on as it is.

    item : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItemView::initItem(int index, QObject *item)
    ritual = 'ritual_ZN14QQuickItemView8initItemEiP7QObject'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QQuickItemView8initItemEiP7QObject'
    self.uglySide.call(ritual, index, self._addressOf(item, 'QObject'))

  @overload(QQmlChangeSet, bool)
  def modelUpdated(self, changeSet: QQmlChangeSet, reset: bool) -> None:
    """
    Calls Qt's 'void QQuickItemView::modelUpdated(const QQmlChangeSet
    &changeSet, bool reset)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemview.html#modelUpdated

    Parameters
    ----------

    changeSet : QQmlChangeSet
      Passed on as a value: Qt reads the C++ QQmlChangeSet, which stays
      Python's own.

    reset : bool
      Passed on as it is.
    """
    #  void QQuickItemView::modelUpdated(const QQmlChangeSet &changeSet, bool
    #      reset)
    self.uglySide.call(
        'ritual_ZN14QQuickItemView12modelUpdatedERK13QQmlChangeSetb',
        self._valueOf(changeSet), reset,
    )

  @overload(QObject)
  @overload(NoneType)
  def destroyingItem(self, item: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QQuickItemView::destroyingItem(QObject *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemview.html#destroyingItem

    Parameters
    ----------

    item : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItemView::destroyingItem(QObject *item)
    self.uglySide.call(
        'ritual_ZN14QQuickItemView14destroyingItemEP7QObject',
        self._addressOf(item, 'QObject'),
    )

  @overload(int, QObject)
  @overload(int, NoneType)
  def onItemPooled(self, modelIndex: int, object: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QQuickItemView::onItemPooled(int modelIndex, QObject
    *object)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemview.html#onItemPooled

    Parameters
    ----------

    modelIndex : int
      Passed on as it is.

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItemView::onItemPooled(int modelIndex, QObject *object)
    self.uglySide.call(
        'ritual_ZN14QQuickItemView12onItemPooledEiP7QObject',
        modelIndex, self._addressOf(object, 'QObject'),
    )

  @overload(int, QObject)
  @overload(int, NoneType)
  def onItemReused(self, modelIndex: int, object: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QQuickItemView::onItemReused(int modelIndex, QObject
    *object)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemview.html#onItemReused

    Parameters
    ----------

    modelIndex : int
      Passed on as it is.

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItemView::onItemReused(int modelIndex, QObject *object)
    self.uglySide.call(
        'ritual_ZN14QQuickItemView12onItemReusedEiP7QObject',
        modelIndex, self._addressOf(object, 'QObject'),
    )

  def animStopped(self) -> None:
    """
    Calls Qt's 'void QQuickItemView::animStopped()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemview.html#animStopped
    """
    #  void QQuickItemView::animStopped()
    self.uglySide.call('ritual_ZN14QQuickItemView11animStoppedEv')

  def trackedPositionChanged(self) -> None:
    """
    Calls Qt's 'void QQuickItemView::trackedPositionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemview.html#trackedPositionChanged
    """
    #  void QQuickItemView::trackedPositionChanged()
    self.uglySide.call('ritual_ZN14QQuickItemView22trackedPositionChangedEv')

  def d_func(self) -> Optional[QQuickItemViewPrivate]:
    """
    Calls Qt's 'QQuickItemViewPrivate *QQuickItemView::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemview.html#d_func

    Returns
    -------

    Optional[QQuickItemViewPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItemViewPrivate *QQuickItemView::d_func()
    address = self.uglySide.call('ritual_ZN14QQuickItemView6d_funcEv')
    from . import QQuickItemViewPrivate
    return QQuickItemViewPrivate._cuteAt(address)
