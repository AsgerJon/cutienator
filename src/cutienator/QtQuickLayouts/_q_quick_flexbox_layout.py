"""
QQuickFlexboxLayout binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickLayouts/6.12.0/QtQuickLayouts/private/qquickflexboxlayout_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuickFlexboxLayout to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObject
from . import QQuickLayout
from ..QtQuick import QQuickItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QSizeF
  from . import QQuickFlexboxLayoutAttached
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSizeF = WAIT['QSizeF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickFlexboxLayout(QQuickLayout):
  """
  The cute side of Qt's QQuickFlexboxLayout: a plain Python object standing
  in front of one C++ QQuickFlexboxLayout.

  It is built on the cute 'QQuickLayout', as Qt's QQuickFlexboxLayout is
  built on Qt's QQuickLayout, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickFlexboxLayout that has a ritual and that
  Python can call so far, 45 names in all: 'metaObject', 'tr', 'direction',
  'setDirection', 'wrap', 'setWrap', 'alignItems', 'setAlignItems',
  'justifyContent', 'setJustifyContent', 'alignContent', 'setAlignContent',
  'gap', 'setGap', 'resetGap', 'rowGap', 'setRowGap', 'resetRowGap',
  'columnGap', 'setColumnGap', 'resetColumnGap', 'componentComplete',
  'sizeHint', 'setAlignment', 'setStretchFactor', 'invalidate',
  'updateLayoutItems', 'rearrange', 'itemAt', 'itemCount',
  'itemSiblingOrderChanged', 'itemVisibilityChanged',
  'qmlAttachedProperties', 'isGapBitSet', 'checkAnchors', 'countChanged',
  'directionChanged', 'wrapChanged', 'alignItemsChanged',
  'alignContentChanged', 'justifyContentChanged', 'gapChanged',
  'rowGapChanged', 'columnGapChanged', 'childItemsChanged'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickFlexboxLayout::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickFlexboxLayout::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickFlexboxLayout::qt_qmlMarker_attached()': one of Qt's own
    inner workings.
  - Qt's 'QQuickFlexboxLayout::~QQuickFlexboxLayout()': the destructor:
    Python never removes a C++ QQuickFlexboxLayout.
  - Qt's 'QQuickFlexboxLayoutPrivate *QQuickFlexboxLayout::d_func()': gives
    'QQuickFlexboxLayoutPrivate', which has no cute class yet.
  - Qt's 'const QQuickFlexboxLayoutPrivate *QQuickFlexboxLayout::d_func()
    const': gives 'QQuickFlexboxLayoutPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  2 of the 54 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickFlexboxLayout is created at the first use, not by
    'QQuickFlexboxLayout(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickFlexboxLayout.
  - Qt tells when it has removed the C++ QQuickFlexboxLayout. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QQuickFlexboxLayout, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class FlexboxAlignment(CuteNum):
    """
    The enum 'QQuickFlexboxLayout::FlexboxAlignment' of Qt, with the 9 names
    Qt gives in it.
    """

    AlignAuto = Kee[int](0)
    AlignStart = Kee[int](1)
    AlignCenter = Kee[int](2)
    AlignEnd = Kee[int](3)
    AlignStretch = Kee[int](4)
    AlignBaseline = Kee[int](5)
    AlignSpaceBetween = Kee[int](6)
    AlignSpaceAround = Kee[int](7)
    AlignSpaceEvenly = Kee[int](8)

  class FlexboxDirection(CuteNum):
    """
    The enum 'QQuickFlexboxLayout::FlexboxDirection' of Qt, with the 4 names
    Qt gives in it.
    """

    Column = Kee[int](0)
    ColumnReverse = Kee[int](1)
    Row = Kee[int](2)
    RowReverse = Kee[int](3)

  class FlexboxEdge(CuteNum):
    """
    The enum 'QQuickFlexboxLayout::FlexboxEdge' of Qt, with the 6 names Qt
    gives in it.
    """

    EdgeLeft = Kee[int](0)
    EdgeRight = Kee[int](1)
    EdgeTop = Kee[int](2)
    EdgeBottom = Kee[int](3)
    EdgeAll = Kee[int](4)
    EdgeMax = Kee[int](5)

  class FlexboxGap(CuteNum):
    """
    The enum 'QQuickFlexboxLayout::FlexboxGap' of Qt, with the 4 names Qt
    gives in it.
    """

    GapRow = Kee[int](0)
    GapColumn = Kee[int](1)
    GapAll = Kee[int](2)
    GapMax = Kee[int](3)

  class FlexboxJustify(CuteNum):
    """
    The enum 'QQuickFlexboxLayout::FlexboxJustify' of Qt, with the 6 names Qt
    gives in it.
    """

    JustifyStart = Kee[int](0)
    JustifyCenter = Kee[int](1)
    JustifyEnd = Kee[int](2)
    JustifySpaceBetween = Kee[int](3)
    JustifySpaceAround = Kee[int](4)
    JustifySpaceEvenly = Kee[int](5)

  class FlexboxWrap(CuteNum):
    """
    The enum 'QQuickFlexboxLayout::FlexboxWrap' of Qt, with the 3 names Qt
    gives in it.
    """

    NoWrap = Kee[int](0)
    Wrap = Kee[int](1)
    WrapReverse = Kee[int](2)

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
    Calls Qt's 'QString QQuickFlexboxLayout::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickflexboxlayout.html#tr

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
    #  QString QQuickFlexboxLayout::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN19QQuickFlexboxLayout2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  def qmlAttachedProperties(
      object: Optional[QObject],
  ) -> Optional[QQuickFlexboxLayoutAttached]:
    """
    Calls Qt's 'QQuickFlexboxLayoutAttached
    *QQuickFlexboxLayout::qmlAttachedProperties(QObject *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflexboxlayout.html#qmlAttachedProperties

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickFlexboxLayoutAttached]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickFlexboxLayoutAttached
    #      *QQuickFlexboxLayout::qmlAttachedProperties(QObject *object)
    address = Rituals.call(
        'ritual_ZN19QQuickFlexboxLayout21qmlAttachedPropertiesEP7QObject',
        CuteMixin._addressOf(object, 'QObject'),
    )
    from . import QQuickFlexboxLayoutAttached
    return QQuickFlexboxLayoutAttached._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickFlexboxLayout'

  #  A C++ QQuickFlexboxLayout Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickFlexboxLayout'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickFlexboxLayout::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflexboxlayout.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickFlexboxLayout::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickFlexboxLayout10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def direction(self) -> FlexboxDirection:
    """
    Calls Qt's 'FlexboxDirection QQuickFlexboxLayout::direction() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickflexboxlayout.html#direction

    Returns
    -------

    FlexboxDirection
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'FlexboxDirection(number)'
      gives.
    """
    #  FlexboxDirection QQuickFlexboxLayout::direction() const
    return QQuickFlexboxLayout.FlexboxDirection(self.uglySide.call(
        'ritual_ZNK19QQuickFlexboxLayout9directionEv',
    ))

  def wrap(self) -> FlexboxWrap:
    """
    Calls Qt's 'FlexboxWrap QQuickFlexboxLayout::wrap() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickflexboxlayout.html#wrap

    Returns
    -------

    FlexboxWrap
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'FlexboxWrap(number)'
      gives.
    """
    #  FlexboxWrap QQuickFlexboxLayout::wrap() const
    return QQuickFlexboxLayout.FlexboxWrap(self.uglySide.call(
        'ritual_ZNK19QQuickFlexboxLayout4wrapEv',
    ))

  def alignItems(self) -> FlexboxAlignment:
    """
    Calls Qt's 'FlexboxAlignment QQuickFlexboxLayout::alignItems() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflexboxlayout.html#alignItems

    Returns
    -------

    FlexboxAlignment
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'FlexboxAlignment(number)'
      gives.
    """
    #  FlexboxAlignment QQuickFlexboxLayout::alignItems() const
    return QQuickFlexboxLayout.FlexboxAlignment(self.uglySide.call(
        'ritual_ZNK19QQuickFlexboxLayout10alignItemsEv',
    ))

  def justifyContent(self) -> FlexboxJustify:
    """
    Calls Qt's 'FlexboxJustify QQuickFlexboxLayout::justifyContent() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflexboxlayout.html#justifyContent

    Returns
    -------

    FlexboxJustify
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'FlexboxJustify(number)'
      gives.
    """
    #  FlexboxJustify QQuickFlexboxLayout::justifyContent() const
    return QQuickFlexboxLayout.FlexboxJustify(self.uglySide.call(
        'ritual_ZNK19QQuickFlexboxLayout14justifyContentEv',
    ))

  def alignContent(self) -> FlexboxAlignment:
    """
    Calls Qt's 'FlexboxAlignment QQuickFlexboxLayout::alignContent() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflexboxlayout.html#alignContent

    Returns
    -------

    FlexboxAlignment
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'FlexboxAlignment(number)'
      gives.
    """
    #  FlexboxAlignment QQuickFlexboxLayout::alignContent() const
    return QQuickFlexboxLayout.FlexboxAlignment(self.uglySide.call(
        'ritual_ZNK19QQuickFlexboxLayout12alignContentEv',
    ))

  def gap(self) -> float:
    """
    Calls Qt's 'qreal QQuickFlexboxLayout::gap() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickflexboxlayout.html#gap
    """
    #  qreal QQuickFlexboxLayout::gap() const
    return self.uglySide.call('ritual_ZNK19QQuickFlexboxLayout3gapEv')

  def rowGap(self) -> float:
    """
    Calls Qt's 'qreal QQuickFlexboxLayout::rowGap() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickflexboxlayout.html#rowGap
    """
    #  qreal QQuickFlexboxLayout::rowGap() const
    return self.uglySide.call('ritual_ZNK19QQuickFlexboxLayout6rowGapEv')

  def columnGap(self) -> float:
    """
    Calls Qt's 'qreal QQuickFlexboxLayout::columnGap() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickflexboxlayout.html#columnGap
    """
    #  qreal QQuickFlexboxLayout::columnGap() const
    return self.uglySide.call('ritual_ZNK19QQuickFlexboxLayout9columnGapEv')

  @overload(Qt.SizeHint)
  def sizeHint(self, whichSizeHint: Qt.SizeHint) -> QSizeF:
    """
    Calls Qt's 'QSizeF QQuickFlexboxLayout::sizeHint(Qt::SizeHint
    whichSizeHint) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickflexboxlayout.html#sizeHint

    Parameters
    ----------

    whichSizeHint : Qt.SizeHint
      Passed on as its number.

    Returns
    -------

    QSizeF
      A new cute QSizeF around the copy Qt gave back. Python owns it.
    """
    #  QSizeF QQuickFlexboxLayout::sizeHint(Qt::SizeHint whichSizeHint) const
    ritual = 'ritual_ZNK19QQuickFlexboxLayout8sizeHintEN2Qt8SizeHintE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QQuickFlexboxLayout8sizeHintEN2Qt8SizeHintE'
    address = self.uglySide.call(ritual, whichSizeHint.value)
    from ..QtCore import QSizeF
    return QSizeF._cuteOwning(address)

  @overload(int)
  def itemAt(self, index: int) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickFlexboxLayout::itemAt(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickflexboxlayout.html#itemAt

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
    #  QQuickItem *QQuickFlexboxLayout::itemAt(int index) const
    ritual = 'ritual_ZNK19QQuickFlexboxLayout6itemAtEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QQuickFlexboxLayout6itemAtEi'
    address = self.uglySide.call(ritual, index)
    return QQuickItem._cuteAt(address)

  def itemCount(self) -> int:
    """
    Calls Qt's 'int QQuickFlexboxLayout::itemCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickflexboxlayout.html#itemCount
    """
    #  int QQuickFlexboxLayout::itemCount() const
    ritual = 'ritual_ZNK19QQuickFlexboxLayout9itemCountEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QQuickFlexboxLayout9itemCountEv'
    return self.uglySide.call(ritual)

  @overload(FlexboxGap)
  def isGapBitSet(self, gap: FlexboxGap) -> bool:
    """
    Calls Qt's 'bool
    QQuickFlexboxLayout::isGapBitSet(QQuickFlexboxLayout::FlexboxGap gap)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflexboxlayout.html#isGapBitSet

    Parameters
    ----------

    gap : FlexboxGap
      Passed on as its number.
    """
    #  bool QQuickFlexboxLayout::isGapBitSet(QQuickFlexboxLayout::FlexboxGap
    #      gap) const
    return self.uglySide.call(
        'ritual_ZNK19QQuickFlexboxLayout11isGapBitSetENS_10FlexboxGapE',
        gap.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(FlexboxDirection)
  def setDirection(self, a0: FlexboxDirection) -> None:
    """
    Calls Qt's 'void QQuickFlexboxLayout::setDirection(FlexboxDirection a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflexboxlayout.html#setDirection

    Parameters
    ----------

    a0 : FlexboxDirection
      Passed on as its number.
    """
    #  void QQuickFlexboxLayout::setDirection(FlexboxDirection a0)
    self.uglySide.call(
        'ritual_ZN19QQuickFlexboxLayout12setDirectionENS_16FlexboxDirection'
        'E',
        a0.value,
    )

  @overload(FlexboxWrap)
  def setWrap(self, a0: FlexboxWrap) -> None:
    """
    Calls Qt's 'void QQuickFlexboxLayout::setWrap(FlexboxWrap a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickflexboxlayout.html#setWrap

    Parameters
    ----------

    a0 : FlexboxWrap
      Passed on as its number.
    """
    #  void QQuickFlexboxLayout::setWrap(FlexboxWrap a0)
    self.uglySide.call(
        'ritual_ZN19QQuickFlexboxLayout7setWrapENS_11FlexboxWrapE', a0.value,
    )

  @overload(FlexboxAlignment)
  def setAlignItems(self, a0: FlexboxAlignment) -> None:
    """
    Calls Qt's 'void QQuickFlexboxLayout::setAlignItems(FlexboxAlignment
    a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflexboxlayout.html#setAlignItems

    Parameters
    ----------

    a0 : FlexboxAlignment
      Passed on as its number.
    """
    #  void QQuickFlexboxLayout::setAlignItems(FlexboxAlignment a0)
    self.uglySide.call(
        'ritual_ZN19QQuickFlexboxLayout13setAlignItemsENS_16FlexboxAlignmen'
        'tE',
        a0.value,
    )

  @overload(FlexboxJustify)
  def setJustifyContent(self, a0: FlexboxJustify) -> None:
    """
    Calls Qt's 'void QQuickFlexboxLayout::setJustifyContent(FlexboxJustify
    a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflexboxlayout.html#setJustifyContent

    Parameters
    ----------

    a0 : FlexboxJustify
      Passed on as its number.
    """
    #  void QQuickFlexboxLayout::setJustifyContent(FlexboxJustify a0)
    self.uglySide.call(
        'ritual_ZN19QQuickFlexboxLayout17setJustifyContentENS_14FlexboxJust'
        'ifyE',
        a0.value,
    )

  @overload(FlexboxAlignment)
  def setAlignContent(self, a0: FlexboxAlignment) -> None:
    """
    Calls Qt's 'void QQuickFlexboxLayout::setAlignContent(FlexboxAlignment
    a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflexboxlayout.html#setAlignContent

    Parameters
    ----------

    a0 : FlexboxAlignment
      Passed on as its number.
    """
    #  void QQuickFlexboxLayout::setAlignContent(FlexboxAlignment a0)
    self.uglySide.call(
        'ritual_ZN19QQuickFlexboxLayout15setAlignContentENS_16FlexboxAlignm'
        'entE',
        a0.value,
    )

  @overload(float)
  def setGap(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickFlexboxLayout::setGap(qreal a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickflexboxlayout.html#setGap

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickFlexboxLayout::setGap(qreal a0)
    self.uglySide.call('ritual_ZN19QQuickFlexboxLayout6setGapEd', a0)

  @overload(float)
  def setRowGap(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickFlexboxLayout::setRowGap(qreal a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickflexboxlayout.html#setRowGap

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickFlexboxLayout::setRowGap(qreal a0)
    self.uglySide.call('ritual_ZN19QQuickFlexboxLayout9setRowGapEd', a0)

  @overload(float)
  def setColumnGap(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickFlexboxLayout::setColumnGap(qreal a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflexboxlayout.html#setColumnGap

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickFlexboxLayout::setColumnGap(qreal a0)
    self.uglySide.call('ritual_ZN19QQuickFlexboxLayout12setColumnGapEd', a0)

  @overload(QQuickItem, Qt.Alignment)
  @overload(NoneType, Qt.Alignment)
  def setAlignment(self, a0: Optional[QQuickItem], a1: Qt.Alignment) -> None:
    """
    Calls Qt's 'void QQuickFlexboxLayout::setAlignment(QQuickItem *a0,
    Qt::Alignment a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflexboxlayout.html#setAlignment

    Parameters
    ----------

    a0 : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : Qt.Alignment
      Passed on as its number.
    """
    #  void QQuickFlexboxLayout::setAlignment(QQuickItem *a0, Qt::Alignment
    #      a1)
    ritual = (
        'ritual_ZN19QQuickFlexboxLayout12setAlignmentEP10QQuickItem6QFlagsI'
        'N2Qt13AlignmentFlagEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQuickFlexboxLayout12setAlignmentEP10QQuickItem6Q'
          'FlagsIN2Qt13AlignmentFlagEE')
    self.uglySide.call(ritual, self._addressOf(a0), a1.value)

  @overload(QQuickItem, int, Qt.Orientation)
  @overload(NoneType, int, Qt.Orientation)
  def setStretchFactor(
      self,
      a0: Optional[QQuickItem],
      a1: int,
      a2: Qt.Orientation,
  ) -> None:
    """
    Calls Qt's 'void QQuickFlexboxLayout::setStretchFactor(QQuickItem *a0,
    int a1, Qt::Orientation a2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflexboxlayout.html#setStretchFactor

    Parameters
    ----------

    a0 : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : int
      Passed on as it is.

    a2 : Qt.Orientation
      Passed on as its number.
    """
    #  void QQuickFlexboxLayout::setStretchFactor(QQuickItem *a0, int a1,
    #      Qt::Orientation a2)
    ritual = (
        'ritual_ZN19QQuickFlexboxLayout16setStretchFactorEP10QQuickItemiN2Q'
        't11OrientationE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQuickFlexboxLayout16setStretchFactorEP10QQuickIt'
          'emiN2Qt11OrientationE')
    self.uglySide.call(ritual, self._addressOf(a0), a1, a2.value)

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
    Notes what was given, for Qt's
    'QQuickFlexboxLayout::QQuickFlexboxLayout(QQuickItem *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflexboxlayout.html#QQuickFlexboxLayout

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickFlexboxLayout::QQuickFlexboxLayout(QQuickItem *parent)
    self._noteCreation(QQuickFlexboxLayout, lambda: Rituals.call(
        'ritual_ZN19QQuickFlexboxLayoutC1EP10QQuickItem',
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

  def resetGap(self) -> None:
    """
    Calls Qt's 'void QQuickFlexboxLayout::resetGap()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickflexboxlayout.html#resetGap
    """
    #  void QQuickFlexboxLayout::resetGap()
    self.uglySide.call('ritual_ZN19QQuickFlexboxLayout8resetGapEv')

  def resetRowGap(self) -> None:
    """
    Calls Qt's 'void QQuickFlexboxLayout::resetRowGap()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflexboxlayout.html#resetRowGap
    """
    #  void QQuickFlexboxLayout::resetRowGap()
    self.uglySide.call('ritual_ZN19QQuickFlexboxLayout11resetRowGapEv')

  def resetColumnGap(self) -> None:
    """
    Calls Qt's 'void QQuickFlexboxLayout::resetColumnGap()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflexboxlayout.html#resetColumnGap
    """
    #  void QQuickFlexboxLayout::resetColumnGap()
    self.uglySide.call('ritual_ZN19QQuickFlexboxLayout14resetColumnGapEv')

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickFlexboxLayout::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflexboxlayout.html#componentComplete
    """
    #  void QQuickFlexboxLayout::componentComplete()
    ritual = 'ritual_ZN19QQuickFlexboxLayout17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQuickFlexboxLayout17componentCompleteEv'
    self.uglySide.call(ritual)

  @overload()
  @overload(QQuickItem)
  @overload(NoneType)
  def invalidate(self, childItem: Optional[QQuickItem] = None) -> None:
    """
    Calls Qt's 'void QQuickFlexboxLayout::invalidate(QQuickItem *childItem)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflexboxlayout.html#invalidate

    Parameters
    ----------

    childItem : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  void QQuickFlexboxLayout::invalidate(QQuickItem *childItem)
    ritual = 'ritual_ZN19QQuickFlexboxLayout10invalidateEP10QQuickItem'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQuickFlexboxLayout10invalidateEP10QQuickItem'
    self.uglySide.call(ritual, self._addressOf(childItem))

  def updateLayoutItems(self) -> None:
    """
    Calls Qt's 'void QQuickFlexboxLayout::updateLayoutItems()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflexboxlayout.html#updateLayoutItems
    """
    #  void QQuickFlexboxLayout::updateLayoutItems()
    ritual = 'ritual_ZN19QQuickFlexboxLayout17updateLayoutItemsEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQuickFlexboxLayout17updateLayoutItemsEv'
    self.uglySide.call(ritual)

  @overload(QSizeF)
  def rearrange(self, a0: QSizeF) -> None:
    """
    Calls Qt's 'void QQuickFlexboxLayout::rearrange(const QSizeF &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickflexboxlayout.html#rearrange

    Parameters
    ----------

    a0 : QSizeF
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own.
    """
    #  void QQuickFlexboxLayout::rearrange(const QSizeF &a0)
    ritual = 'ritual_ZN19QQuickFlexboxLayout9rearrangeERK6QSizeF'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQuickFlexboxLayout9rearrangeERK6QSizeF'
    self.uglySide.call(ritual, self._valueOf(a0))

  @overload(QQuickItem)
  @overload(NoneType)
  def itemSiblingOrderChanged(self, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickFlexboxLayout::itemSiblingOrderChanged(QQuickItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflexboxlayout.html#itemSiblingOrderChanged

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickFlexboxLayout::itemSiblingOrderChanged(QQuickItem *item)
    ritual = (
        'ritual_ZN19QQuickFlexboxLayout23itemSiblingOrderChangedEP10QQuickI'
        'tem')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQuickFlexboxLayout23itemSiblingOrderChangedEP10Q'
          'QuickItem')
    self.uglySide.call(ritual, self._addressOf(item))

  @overload(QQuickItem)
  @overload(NoneType)
  def itemVisibilityChanged(self, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickFlexboxLayout::itemVisibilityChanged(QQuickItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflexboxlayout.html#itemVisibilityChanged

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickFlexboxLayout::itemVisibilityChanged(QQuickItem *item)
    ritual = (
        'ritual_ZN19QQuickFlexboxLayout21itemVisibilityChangedEP10QQuickIte'
        'm')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQuickFlexboxLayout21itemVisibilityChangedEP10QQu'
          'ickItem')
    self.uglySide.call(ritual, self._addressOf(item))

  @overload(QQuickItem)
  @overload(NoneType)
  def checkAnchors(self, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickFlexboxLayout::checkAnchors(QQuickItem *item)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflexboxlayout.html#checkAnchors

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickFlexboxLayout::checkAnchors(QQuickItem *item) const
    self.uglySide.call(
        'ritual_ZNK19QQuickFlexboxLayout12checkAnchorsEP10QQuickItem',
        self._addressOf(item),
    )

  def countChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFlexboxLayout::countChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflexboxlayout.html#countChanged
    """
    #  void QQuickFlexboxLayout::countChanged()
    self.uglySide.call('ritual_ZN19QQuickFlexboxLayout12countChangedEv')

  def directionChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFlexboxLayout::directionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflexboxlayout.html#directionChanged
    """
    #  void QQuickFlexboxLayout::directionChanged()
    self.uglySide.call('ritual_ZN19QQuickFlexboxLayout16directionChangedEv')

  def wrapChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFlexboxLayout::wrapChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflexboxlayout.html#wrapChanged
    """
    #  void QQuickFlexboxLayout::wrapChanged()
    self.uglySide.call('ritual_ZN19QQuickFlexboxLayout11wrapChangedEv')

  def alignItemsChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFlexboxLayout::alignItemsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflexboxlayout.html#alignItemsChanged
    """
    #  void QQuickFlexboxLayout::alignItemsChanged()
    self.uglySide.call('ritual_ZN19QQuickFlexboxLayout17alignItemsChangedEv')

  def alignContentChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFlexboxLayout::alignContentChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflexboxlayout.html#alignContentChanged
    """
    #  void QQuickFlexboxLayout::alignContentChanged()
    self.uglySide.call(
        'ritual_ZN19QQuickFlexboxLayout19alignContentChangedEv',
    )

  def justifyContentChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFlexboxLayout::justifyContentChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflexboxlayout.html#justifyContentChanged
    """
    #  void QQuickFlexboxLayout::justifyContentChanged()
    self.uglySide.call(
        'ritual_ZN19QQuickFlexboxLayout21justifyContentChangedEv',
    )

  def gapChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFlexboxLayout::gapChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflexboxlayout.html#gapChanged
    """
    #  void QQuickFlexboxLayout::gapChanged()
    self.uglySide.call('ritual_ZN19QQuickFlexboxLayout10gapChangedEv')

  def rowGapChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFlexboxLayout::rowGapChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflexboxlayout.html#rowGapChanged
    """
    #  void QQuickFlexboxLayout::rowGapChanged()
    self.uglySide.call('ritual_ZN19QQuickFlexboxLayout13rowGapChangedEv')

  def columnGapChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFlexboxLayout::columnGapChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflexboxlayout.html#columnGapChanged
    """
    #  void QQuickFlexboxLayout::columnGapChanged()
    self.uglySide.call('ritual_ZN19QQuickFlexboxLayout16columnGapChangedEv')

  def childItemsChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFlexboxLayout::childItemsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflexboxlayout.html#childItemsChanged
    """
    #  void QQuickFlexboxLayout::childItemsChanged()
    self.uglySide.call('ritual_ZN19QQuickFlexboxLayout17childItemsChangedEv')
