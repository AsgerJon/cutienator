"""
QQuickAnchors binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickanchors_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQuickAnchors to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QQuickAnchorLine, QQuickAnchorsPrivate, QQuickItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickAnchorLine = WAIT['QQuickAnchorLine']
  QQuickItem = WAIT['QQuickItem']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickAnchors(QObject):
  """
  The cute side of Qt's QQuickAnchors: a plain Python object standing in
  front of one C++ QQuickAnchors.

  It is built on the cute 'QObject', as Qt's QQuickAnchors is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickAnchors that has a ritual and that Python can
  call so far, 75 names in all: 'metaObject', 'tr', 'left', 'setLeft',
  'resetLeft', 'right', 'setRight', 'resetRight', 'horizontalCenter',
  'setHorizontalCenter', 'resetHorizontalCenter', 'top', 'setTop',
  'resetTop', 'bottom', 'setBottom', 'resetBottom', 'verticalCenter',
  'setVerticalCenter', 'resetVerticalCenter', 'baseline', 'setBaseline',
  'resetBaseline', 'leftMargin', 'setLeftMargin', 'resetLeftMargin',
  'rightMargin', 'setRightMargin', 'resetRightMargin',
  'horizontalCenterOffset', 'setHorizontalCenterOffset', 'topMargin',
  'setTopMargin', 'resetTopMargin', 'bottomMargin', 'setBottomMargin',
  'resetBottomMargin', 'margins', 'setMargins', 'verticalCenterOffset',
  'setVerticalCenterOffset', 'baselineOffset', 'setBaselineOffset', 'fill',
  'setFill', 'resetFill', 'centerIn', 'setCenterIn', 'resetCenterIn',
  'usedAnchors', 'activeDirections', 'mirrored', 'alignWhenCentered',
  'setAlignWhenCentered', 'classBegin', 'componentComplete', 'leftChanged',
  'rightChanged', 'topChanged', 'bottomChanged', 'verticalCenterChanged',
  'horizontalCenterChanged', 'baselineChanged', 'fillChanged',
  'centerInChanged', 'leftMarginChanged', 'rightMarginChanged',
  'topMarginChanged', 'bottomMarginChanged', 'marginsChanged',
  'verticalCenterOffsetChanged', 'horizontalCenterOffsetChanged',
  'baselineOffsetChanged', 'centerAlignedChanged', 'd_func'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickAnchors::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQuickAnchors::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickAnchors::qt_qmlMarker_anonymous()': one of Qt's own
    inner workings.
  - Qt's 'QQuickAnchors::~QQuickAnchors()': the destructor: Python never
    removes a C++ QQuickAnchors.
  - Qt's 'const QQuickAnchorsPrivate *QQuickAnchors::d_func() const': takes
    in Python what 'QQuickAnchorsPrivate *QQuickAnchors::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 85 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickAnchors is created at the first use, not by
    'QQuickAnchors(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickAnchors.
  - Qt tells when it has removed the C++ QQuickAnchors. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QQuickAnchors, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Anchor(CuteFlags, number='unsigned int'):
    """
    The flags enum 'QQuickAnchors::Anchor' of Qt, with the 10 names Qt gives
    in it. Qt names the type of its combinations 'QQuickAnchors::Anchors'.
    """

    InvalidAnchor = 0x0
    LeftAnchor = 0x1
    RightAnchor = 0x2
    TopAnchor = 0x4
    BottomAnchor = 0x8
    HCenterAnchor = 0x10
    VCenterAnchor = 0x20
    BaselineAnchor = 0x40
    Horizontal_Mask = 0x13
    Vertical_Mask = 0x6c

  Anchors = Anchor

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
    Calls Qt's 'QString QQuickAnchors::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanchors.html#tr

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
    #  QString QQuickAnchors::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN13QQuickAnchors2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickAnchors'

  #  A C++ QQuickAnchors Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickAnchors'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickAnchors::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanchors.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickAnchors::metaObject() const
    address = self.uglySide.call('ritual_ZNK13QQuickAnchors10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def left(self) -> QQuickAnchorLine:
    """
    Calls Qt's 'QQuickAnchorLine QQuickAnchors::left() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanchors.html#left

    Returns
    -------

    QQuickAnchorLine
      A new cute QQuickAnchorLine around the copy Qt gave back. Python owns
      it.
    """
    #  QQuickAnchorLine QQuickAnchors::left() const
    address = self.uglySide.call('ritual_ZNK13QQuickAnchors4leftEv')
    from . import QQuickAnchorLine
    return QQuickAnchorLine._cuteOwning(address)

  def right(self) -> QQuickAnchorLine:
    """
    Calls Qt's 'QQuickAnchorLine QQuickAnchors::right() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanchors.html#right

    Returns
    -------

    QQuickAnchorLine
      A new cute QQuickAnchorLine around the copy Qt gave back. Python owns
      it.
    """
    #  QQuickAnchorLine QQuickAnchors::right() const
    address = self.uglySide.call('ritual_ZNK13QQuickAnchors5rightEv')
    from . import QQuickAnchorLine
    return QQuickAnchorLine._cuteOwning(address)

  def horizontalCenter(self) -> QQuickAnchorLine:
    """
    Calls Qt's 'QQuickAnchorLine QQuickAnchors::horizontalCenter() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanchors.html#horizontalCenter

    Returns
    -------

    QQuickAnchorLine
      A new cute QQuickAnchorLine around the copy Qt gave back. Python owns
      it.
    """
    #  QQuickAnchorLine QQuickAnchors::horizontalCenter() const
    address = self.uglySide.call(
        'ritual_ZNK13QQuickAnchors16horizontalCenterEv',
    )
    from . import QQuickAnchorLine
    return QQuickAnchorLine._cuteOwning(address)

  def top(self) -> QQuickAnchorLine:
    """
    Calls Qt's 'QQuickAnchorLine QQuickAnchors::top() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanchors.html#top

    Returns
    -------

    QQuickAnchorLine
      A new cute QQuickAnchorLine around the copy Qt gave back. Python owns
      it.
    """
    #  QQuickAnchorLine QQuickAnchors::top() const
    address = self.uglySide.call('ritual_ZNK13QQuickAnchors3topEv')
    from . import QQuickAnchorLine
    return QQuickAnchorLine._cuteOwning(address)

  def bottom(self) -> QQuickAnchorLine:
    """
    Calls Qt's 'QQuickAnchorLine QQuickAnchors::bottom() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanchors.html#bottom

    Returns
    -------

    QQuickAnchorLine
      A new cute QQuickAnchorLine around the copy Qt gave back. Python owns
      it.
    """
    #  QQuickAnchorLine QQuickAnchors::bottom() const
    address = self.uglySide.call('ritual_ZNK13QQuickAnchors6bottomEv')
    from . import QQuickAnchorLine
    return QQuickAnchorLine._cuteOwning(address)

  def verticalCenter(self) -> QQuickAnchorLine:
    """
    Calls Qt's 'QQuickAnchorLine QQuickAnchors::verticalCenter() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanchors.html#verticalCenter

    Returns
    -------

    QQuickAnchorLine
      A new cute QQuickAnchorLine around the copy Qt gave back. Python owns
      it.
    """
    #  QQuickAnchorLine QQuickAnchors::verticalCenter() const
    address = self.uglySide.call(
        'ritual_ZNK13QQuickAnchors14verticalCenterEv',
    )
    from . import QQuickAnchorLine
    return QQuickAnchorLine._cuteOwning(address)

  def baseline(self) -> QQuickAnchorLine:
    """
    Calls Qt's 'QQuickAnchorLine QQuickAnchors::baseline() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanchors.html#baseline

    Returns
    -------

    QQuickAnchorLine
      A new cute QQuickAnchorLine around the copy Qt gave back. Python owns
      it.
    """
    #  QQuickAnchorLine QQuickAnchors::baseline() const
    address = self.uglySide.call('ritual_ZNK13QQuickAnchors8baselineEv')
    from . import QQuickAnchorLine
    return QQuickAnchorLine._cuteOwning(address)

  def leftMargin(self) -> float:
    """
    Calls Qt's 'qreal QQuickAnchors::leftMargin() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanchors.html#leftMargin
    """
    #  qreal QQuickAnchors::leftMargin() const
    return self.uglySide.call('ritual_ZNK13QQuickAnchors10leftMarginEv')

  def rightMargin(self) -> float:
    """
    Calls Qt's 'qreal QQuickAnchors::rightMargin() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanchors.html#rightMargin
    """
    #  qreal QQuickAnchors::rightMargin() const
    return self.uglySide.call('ritual_ZNK13QQuickAnchors11rightMarginEv')

  def horizontalCenterOffset(self) -> float:
    """
    Calls Qt's 'qreal QQuickAnchors::horizontalCenterOffset() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanchors.html#horizontalCenterOffset
    """
    #  qreal QQuickAnchors::horizontalCenterOffset() const
    return self.uglySide.call(
        'ritual_ZNK13QQuickAnchors22horizontalCenterOffsetEv',
    )

  def topMargin(self) -> float:
    """
    Calls Qt's 'qreal QQuickAnchors::topMargin() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanchors.html#topMargin
    """
    #  qreal QQuickAnchors::topMargin() const
    return self.uglySide.call('ritual_ZNK13QQuickAnchors9topMarginEv')

  def bottomMargin(self) -> float:
    """
    Calls Qt's 'qreal QQuickAnchors::bottomMargin() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanchors.html#bottomMargin
    """
    #  qreal QQuickAnchors::bottomMargin() const
    return self.uglySide.call('ritual_ZNK13QQuickAnchors12bottomMarginEv')

  def margins(self) -> float:
    """
    Calls Qt's 'qreal QQuickAnchors::margins() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanchors.html#margins
    """
    #  qreal QQuickAnchors::margins() const
    return self.uglySide.call('ritual_ZNK13QQuickAnchors7marginsEv')

  def verticalCenterOffset(self) -> float:
    """
    Calls Qt's 'qreal QQuickAnchors::verticalCenterOffset() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanchors.html#verticalCenterOffset
    """
    #  qreal QQuickAnchors::verticalCenterOffset() const
    return self.uglySide.call(
        'ritual_ZNK13QQuickAnchors20verticalCenterOffsetEv',
    )

  def baselineOffset(self) -> float:
    """
    Calls Qt's 'qreal QQuickAnchors::baselineOffset() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanchors.html#baselineOffset
    """
    #  qreal QQuickAnchors::baselineOffset() const
    return self.uglySide.call('ritual_ZNK13QQuickAnchors14baselineOffsetEv')

  def fill(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickAnchors::fill() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanchors.html#fill

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickAnchors::fill() const
    address = self.uglySide.call('ritual_ZNK13QQuickAnchors4fillEv')
    from . import QQuickItem
    return QQuickItem._cuteAt(address)

  def centerIn(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickAnchors::centerIn() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanchors.html#centerIn

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickAnchors::centerIn() const
    address = self.uglySide.call('ritual_ZNK13QQuickAnchors8centerInEv')
    from . import QQuickItem
    return QQuickItem._cuteAt(address)

  def usedAnchors(self) -> Anchors:
    """
    Calls Qt's 'Anchors QQuickAnchors::usedAnchors() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanchors.html#usedAnchors

    Returns
    -------

    Anchors
      The value standing for the combination Qt gave back.
    """
    #  Anchors QQuickAnchors::usedAnchors() const
    return QQuickAnchors.Anchors(self.uglySide.call(
        'ritual_ZNK13QQuickAnchors11usedAnchorsEv',
    ))

  def activeDirections(self) -> Qt.Orientations:
    """
    Calls Qt's 'Qt::Orientations QQuickAnchors::activeDirections() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanchors.html#activeDirections

    Returns
    -------

    Qt.Orientations
      The value standing for the combination Qt gave back.
    """
    #  Qt::Orientations QQuickAnchors::activeDirections() const
    return Qt.Orientations(self.uglySide.call(
        'ritual_ZNK13QQuickAnchors16activeDirectionsEv',
    ))

  def alignWhenCentered(self) -> bool:
    """
    Calls Qt's 'bool QQuickAnchors::alignWhenCentered() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanchors.html#alignWhenCentered
    """
    #  bool QQuickAnchors::alignWhenCentered() const
    return self.uglySide.call(
        'ritual_ZNK13QQuickAnchors17alignWhenCenteredEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuickAnchorLine)
  def setLeft(self, edge: QQuickAnchorLine) -> None:
    """
    Calls Qt's 'void QQuickAnchors::setLeft(const QQuickAnchorLine &edge)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanchors.html#setLeft

    Parameters
    ----------

    edge : QQuickAnchorLine
      Passed on as a value: Qt reads the C++ QQuickAnchorLine, which stays
      Python's own.
    """
    #  void QQuickAnchors::setLeft(const QQuickAnchorLine &edge)
    self.uglySide.call(
        'ritual_ZN13QQuickAnchors7setLeftERK16QQuickAnchorLine',
        self._valueOf(edge),
    )

  @overload(QQuickAnchorLine)
  def setRight(self, edge: QQuickAnchorLine) -> None:
    """
    Calls Qt's 'void QQuickAnchors::setRight(const QQuickAnchorLine &edge)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanchors.html#setRight

    Parameters
    ----------

    edge : QQuickAnchorLine
      Passed on as a value: Qt reads the C++ QQuickAnchorLine, which stays
      Python's own.
    """
    #  void QQuickAnchors::setRight(const QQuickAnchorLine &edge)
    self.uglySide.call(
        'ritual_ZN13QQuickAnchors8setRightERK16QQuickAnchorLine',
        self._valueOf(edge),
    )

  @overload(QQuickAnchorLine)
  def setHorizontalCenter(self, edge: QQuickAnchorLine) -> None:
    """
    Calls Qt's 'void QQuickAnchors::setHorizontalCenter(const
    QQuickAnchorLine &edge)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanchors.html#setHorizontalCenter

    Parameters
    ----------

    edge : QQuickAnchorLine
      Passed on as a value: Qt reads the C++ QQuickAnchorLine, which stays
      Python's own.
    """
    #  void QQuickAnchors::setHorizontalCenter(const QQuickAnchorLine &edge)
    self.uglySide.call(
        'ritual_ZN13QQuickAnchors19setHorizontalCenterERK16QQuickAnchorLine',
        self._valueOf(edge),
    )

  @overload(QQuickAnchorLine)
  def setTop(self, edge: QQuickAnchorLine) -> None:
    """
    Calls Qt's 'void QQuickAnchors::setTop(const QQuickAnchorLine &edge)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanchors.html#setTop

    Parameters
    ----------

    edge : QQuickAnchorLine
      Passed on as a value: Qt reads the C++ QQuickAnchorLine, which stays
      Python's own.
    """
    #  void QQuickAnchors::setTop(const QQuickAnchorLine &edge)
    self.uglySide.call(
        'ritual_ZN13QQuickAnchors6setTopERK16QQuickAnchorLine',
        self._valueOf(edge),
    )

  @overload(QQuickAnchorLine)
  def setBottom(self, edge: QQuickAnchorLine) -> None:
    """
    Calls Qt's 'void QQuickAnchors::setBottom(const QQuickAnchorLine &edge)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanchors.html#setBottom

    Parameters
    ----------

    edge : QQuickAnchorLine
      Passed on as a value: Qt reads the C++ QQuickAnchorLine, which stays
      Python's own.
    """
    #  void QQuickAnchors::setBottom(const QQuickAnchorLine &edge)
    self.uglySide.call(
        'ritual_ZN13QQuickAnchors9setBottomERK16QQuickAnchorLine',
        self._valueOf(edge),
    )

  @overload(QQuickAnchorLine)
  def setVerticalCenter(self, edge: QQuickAnchorLine) -> None:
    """
    Calls Qt's 'void QQuickAnchors::setVerticalCenter(const QQuickAnchorLine
    &edge)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanchors.html#setVerticalCenter

    Parameters
    ----------

    edge : QQuickAnchorLine
      Passed on as a value: Qt reads the C++ QQuickAnchorLine, which stays
      Python's own.
    """
    #  void QQuickAnchors::setVerticalCenter(const QQuickAnchorLine &edge)
    self.uglySide.call(
        'ritual_ZN13QQuickAnchors17setVerticalCenterERK16QQuickAnchorLine',
        self._valueOf(edge),
    )

  @overload(QQuickAnchorLine)
  def setBaseline(self, edge: QQuickAnchorLine) -> None:
    """
    Calls Qt's 'void QQuickAnchors::setBaseline(const QQuickAnchorLine
    &edge)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanchors.html#setBaseline

    Parameters
    ----------

    edge : QQuickAnchorLine
      Passed on as a value: Qt reads the C++ QQuickAnchorLine, which stays
      Python's own.
    """
    #  void QQuickAnchors::setBaseline(const QQuickAnchorLine &edge)
    self.uglySide.call(
        'ritual_ZN13QQuickAnchors11setBaselineERK16QQuickAnchorLine',
        self._valueOf(edge),
    )

  @overload(float)
  def setLeftMargin(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickAnchors::setLeftMargin(qreal a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanchors.html#setLeftMargin

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickAnchors::setLeftMargin(qreal a0)
    self.uglySide.call('ritual_ZN13QQuickAnchors13setLeftMarginEd', a0)

  @overload(float)
  def setRightMargin(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickAnchors::setRightMargin(qreal a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanchors.html#setRightMargin

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickAnchors::setRightMargin(qreal a0)
    self.uglySide.call('ritual_ZN13QQuickAnchors14setRightMarginEd', a0)

  @overload(float)
  def setHorizontalCenterOffset(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickAnchors::setHorizontalCenterOffset(qreal a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanchors.html#setHorizontalCenterOffset

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickAnchors::setHorizontalCenterOffset(qreal a0)
    self.uglySide.call(
        'ritual_ZN13QQuickAnchors25setHorizontalCenterOffsetEd', a0,
    )

  @overload(float)
  def setTopMargin(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickAnchors::setTopMargin(qreal a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanchors.html#setTopMargin

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickAnchors::setTopMargin(qreal a0)
    self.uglySide.call('ritual_ZN13QQuickAnchors12setTopMarginEd', a0)

  @overload(float)
  def setBottomMargin(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickAnchors::setBottomMargin(qreal a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanchors.html#setBottomMargin

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickAnchors::setBottomMargin(qreal a0)
    self.uglySide.call('ritual_ZN13QQuickAnchors15setBottomMarginEd', a0)

  @overload(float)
  def setMargins(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickAnchors::setMargins(qreal a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanchors.html#setMargins

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickAnchors::setMargins(qreal a0)
    self.uglySide.call('ritual_ZN13QQuickAnchors10setMarginsEd', a0)

  @overload(float)
  def setVerticalCenterOffset(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickAnchors::setVerticalCenterOffset(qreal a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanchors.html#setVerticalCenterOffset

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickAnchors::setVerticalCenterOffset(qreal a0)
    self.uglySide.call(
        'ritual_ZN13QQuickAnchors23setVerticalCenterOffsetEd', a0,
    )

  @overload(float)
  def setBaselineOffset(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickAnchors::setBaselineOffset(qreal a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanchors.html#setBaselineOffset

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickAnchors::setBaselineOffset(qreal a0)
    self.uglySide.call('ritual_ZN13QQuickAnchors17setBaselineOffsetEd', a0)

  @overload(QQuickItem)
  @overload(NoneType)
  def setFill(self, a0: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickAnchors::setFill(QQuickItem *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanchors.html#setFill

    Parameters
    ----------

    a0 : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickAnchors::setFill(QQuickItem *a0)
    self.uglySide.call(
        'ritual_ZN13QQuickAnchors7setFillEP10QQuickItem',
        self._addressOf(a0),
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def setCenterIn(self, a0: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickAnchors::setCenterIn(QQuickItem *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanchors.html#setCenterIn

    Parameters
    ----------

    a0 : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickAnchors::setCenterIn(QQuickItem *a0)
    self.uglySide.call(
        'ritual_ZN13QQuickAnchors11setCenterInEP10QQuickItem',
        self._addressOf(a0),
    )

  @overload(bool)
  def setAlignWhenCentered(self, a0: bool) -> None:
    """
    Calls Qt's 'void QQuickAnchors::setAlignWhenCentered(bool a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanchors.html#setAlignWhenCentered

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QQuickAnchors::setAlignWhenCentered(bool a0)
    self.uglySide.call(
        'ritual_ZN13QQuickAnchors20setAlignWhenCenteredEb', a0,
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

  @overload(QQuickItem)
  @overload(NoneType)
  @overload(QQuickItem, QObject)
  @overload(QQuickItem, NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      item: Optional[QQuickItem],
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QQuickAnchors::QQuickAnchors(QQuickItem
    *item, QObject *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qquickanchors.html#QQuickAnchors

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickAnchors::QQuickAnchors(QQuickItem *item, QObject *parent)
    self._noteCreation(QQuickAnchors, lambda: Rituals.call(
        'ritual_ZN13QQuickAnchorsC1EP10QQuickItemP7QObject',
        self._addressOf(item), self._addressOf(parent, 'QObject'),
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

  def resetLeft(self) -> None:
    """
    Calls Qt's 'void QQuickAnchors::resetLeft()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanchors.html#resetLeft
    """
    #  void QQuickAnchors::resetLeft()
    self.uglySide.call('ritual_ZN13QQuickAnchors9resetLeftEv')

  def resetRight(self) -> None:
    """
    Calls Qt's 'void QQuickAnchors::resetRight()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanchors.html#resetRight
    """
    #  void QQuickAnchors::resetRight()
    self.uglySide.call('ritual_ZN13QQuickAnchors10resetRightEv')

  def resetHorizontalCenter(self) -> None:
    """
    Calls Qt's 'void QQuickAnchors::resetHorizontalCenter()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanchors.html#resetHorizontalCenter
    """
    #  void QQuickAnchors::resetHorizontalCenter()
    self.uglySide.call('ritual_ZN13QQuickAnchors21resetHorizontalCenterEv')

  def resetTop(self) -> None:
    """
    Calls Qt's 'void QQuickAnchors::resetTop()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanchors.html#resetTop
    """
    #  void QQuickAnchors::resetTop()
    self.uglySide.call('ritual_ZN13QQuickAnchors8resetTopEv')

  def resetBottom(self) -> None:
    """
    Calls Qt's 'void QQuickAnchors::resetBottom()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanchors.html#resetBottom
    """
    #  void QQuickAnchors::resetBottom()
    self.uglySide.call('ritual_ZN13QQuickAnchors11resetBottomEv')

  def resetVerticalCenter(self) -> None:
    """
    Calls Qt's 'void QQuickAnchors::resetVerticalCenter()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanchors.html#resetVerticalCenter
    """
    #  void QQuickAnchors::resetVerticalCenter()
    self.uglySide.call('ritual_ZN13QQuickAnchors19resetVerticalCenterEv')

  def resetBaseline(self) -> None:
    """
    Calls Qt's 'void QQuickAnchors::resetBaseline()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanchors.html#resetBaseline
    """
    #  void QQuickAnchors::resetBaseline()
    self.uglySide.call('ritual_ZN13QQuickAnchors13resetBaselineEv')

  def resetLeftMargin(self) -> None:
    """
    Calls Qt's 'void QQuickAnchors::resetLeftMargin()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanchors.html#resetLeftMargin
    """
    #  void QQuickAnchors::resetLeftMargin()
    self.uglySide.call('ritual_ZN13QQuickAnchors15resetLeftMarginEv')

  def resetRightMargin(self) -> None:
    """
    Calls Qt's 'void QQuickAnchors::resetRightMargin()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanchors.html#resetRightMargin
    """
    #  void QQuickAnchors::resetRightMargin()
    self.uglySide.call('ritual_ZN13QQuickAnchors16resetRightMarginEv')

  def resetTopMargin(self) -> None:
    """
    Calls Qt's 'void QQuickAnchors::resetTopMargin()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanchors.html#resetTopMargin
    """
    #  void QQuickAnchors::resetTopMargin()
    self.uglySide.call('ritual_ZN13QQuickAnchors14resetTopMarginEv')

  def resetBottomMargin(self) -> None:
    """
    Calls Qt's 'void QQuickAnchors::resetBottomMargin()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanchors.html#resetBottomMargin
    """
    #  void QQuickAnchors::resetBottomMargin()
    self.uglySide.call('ritual_ZN13QQuickAnchors17resetBottomMarginEv')

  def resetFill(self) -> None:
    """
    Calls Qt's 'void QQuickAnchors::resetFill()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanchors.html#resetFill
    """
    #  void QQuickAnchors::resetFill()
    self.uglySide.call('ritual_ZN13QQuickAnchors9resetFillEv')

  def resetCenterIn(self) -> None:
    """
    Calls Qt's 'void QQuickAnchors::resetCenterIn()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanchors.html#resetCenterIn
    """
    #  void QQuickAnchors::resetCenterIn()
    self.uglySide.call('ritual_ZN13QQuickAnchors13resetCenterInEv')

  def mirrored(self) -> bool:
    """
    Calls Qt's 'bool QQuickAnchors::mirrored()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanchors.html#mirrored
    """
    #  bool QQuickAnchors::mirrored()
    return self.uglySide.call('ritual_ZN13QQuickAnchors8mirroredEv')

  def classBegin(self) -> None:
    """
    Calls Qt's 'void QQuickAnchors::classBegin()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanchors.html#classBegin
    """
    #  void QQuickAnchors::classBegin()
    self.uglySide.call('ritual_ZN13QQuickAnchors10classBeginEv')

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickAnchors::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanchors.html#componentComplete
    """
    #  void QQuickAnchors::componentComplete()
    self.uglySide.call('ritual_ZN13QQuickAnchors17componentCompleteEv')

  def leftChanged(self) -> None:
    """
    Calls Qt's 'void QQuickAnchors::leftChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanchors.html#leftChanged
    """
    #  void QQuickAnchors::leftChanged()
    self.uglySide.call('ritual_ZN13QQuickAnchors11leftChangedEv')

  def rightChanged(self) -> None:
    """
    Calls Qt's 'void QQuickAnchors::rightChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanchors.html#rightChanged
    """
    #  void QQuickAnchors::rightChanged()
    self.uglySide.call('ritual_ZN13QQuickAnchors12rightChangedEv')

  def topChanged(self) -> None:
    """
    Calls Qt's 'void QQuickAnchors::topChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanchors.html#topChanged
    """
    #  void QQuickAnchors::topChanged()
    self.uglySide.call('ritual_ZN13QQuickAnchors10topChangedEv')

  def bottomChanged(self) -> None:
    """
    Calls Qt's 'void QQuickAnchors::bottomChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanchors.html#bottomChanged
    """
    #  void QQuickAnchors::bottomChanged()
    self.uglySide.call('ritual_ZN13QQuickAnchors13bottomChangedEv')

  def verticalCenterChanged(self) -> None:
    """
    Calls Qt's 'void QQuickAnchors::verticalCenterChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanchors.html#verticalCenterChanged
    """
    #  void QQuickAnchors::verticalCenterChanged()
    self.uglySide.call('ritual_ZN13QQuickAnchors21verticalCenterChangedEv')

  def horizontalCenterChanged(self) -> None:
    """
    Calls Qt's 'void QQuickAnchors::horizontalCenterChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanchors.html#horizontalCenterChanged
    """
    #  void QQuickAnchors::horizontalCenterChanged()
    self.uglySide.call('ritual_ZN13QQuickAnchors23horizontalCenterChangedEv')

  def baselineChanged(self) -> None:
    """
    Calls Qt's 'void QQuickAnchors::baselineChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanchors.html#baselineChanged
    """
    #  void QQuickAnchors::baselineChanged()
    self.uglySide.call('ritual_ZN13QQuickAnchors15baselineChangedEv')

  def fillChanged(self) -> None:
    """
    Calls Qt's 'void QQuickAnchors::fillChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanchors.html#fillChanged
    """
    #  void QQuickAnchors::fillChanged()
    self.uglySide.call('ritual_ZN13QQuickAnchors11fillChangedEv')

  def centerInChanged(self) -> None:
    """
    Calls Qt's 'void QQuickAnchors::centerInChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanchors.html#centerInChanged
    """
    #  void QQuickAnchors::centerInChanged()
    self.uglySide.call('ritual_ZN13QQuickAnchors15centerInChangedEv')

  def leftMarginChanged(self) -> None:
    """
    Calls Qt's 'void QQuickAnchors::leftMarginChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanchors.html#leftMarginChanged
    """
    #  void QQuickAnchors::leftMarginChanged()
    self.uglySide.call('ritual_ZN13QQuickAnchors17leftMarginChangedEv')

  def rightMarginChanged(self) -> None:
    """
    Calls Qt's 'void QQuickAnchors::rightMarginChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanchors.html#rightMarginChanged
    """
    #  void QQuickAnchors::rightMarginChanged()
    self.uglySide.call('ritual_ZN13QQuickAnchors18rightMarginChangedEv')

  def topMarginChanged(self) -> None:
    """
    Calls Qt's 'void QQuickAnchors::topMarginChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanchors.html#topMarginChanged
    """
    #  void QQuickAnchors::topMarginChanged()
    self.uglySide.call('ritual_ZN13QQuickAnchors16topMarginChangedEv')

  def bottomMarginChanged(self) -> None:
    """
    Calls Qt's 'void QQuickAnchors::bottomMarginChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanchors.html#bottomMarginChanged
    """
    #  void QQuickAnchors::bottomMarginChanged()
    self.uglySide.call('ritual_ZN13QQuickAnchors19bottomMarginChangedEv')

  def marginsChanged(self) -> None:
    """
    Calls Qt's 'void QQuickAnchors::marginsChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanchors.html#marginsChanged
    """
    #  void QQuickAnchors::marginsChanged()
    self.uglySide.call('ritual_ZN13QQuickAnchors14marginsChangedEv')

  def verticalCenterOffsetChanged(self) -> None:
    """
    Calls Qt's 'void QQuickAnchors::verticalCenterOffsetChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanchors.html#verticalCenterOffsetChanged
    """
    #  void QQuickAnchors::verticalCenterOffsetChanged()
    self.uglySide.call(
        'ritual_ZN13QQuickAnchors27verticalCenterOffsetChangedEv',
    )

  def horizontalCenterOffsetChanged(self) -> None:
    """
    Calls Qt's 'void QQuickAnchors::horizontalCenterOffsetChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanchors.html#horizontalCenterOffsetChanged
    """
    #  void QQuickAnchors::horizontalCenterOffsetChanged()
    self.uglySide.call(
        'ritual_ZN13QQuickAnchors29horizontalCenterOffsetChangedEv',
    )

  def baselineOffsetChanged(self) -> None:
    """
    Calls Qt's 'void QQuickAnchors::baselineOffsetChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanchors.html#baselineOffsetChanged
    """
    #  void QQuickAnchors::baselineOffsetChanged()
    self.uglySide.call('ritual_ZN13QQuickAnchors21baselineOffsetChangedEv')

  def centerAlignedChanged(self) -> None:
    """
    Calls Qt's 'void QQuickAnchors::centerAlignedChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanchors.html#centerAlignedChanged
    """
    #  void QQuickAnchors::centerAlignedChanged()
    self.uglySide.call('ritual_ZN13QQuickAnchors20centerAlignedChangedEv')

  def d_func(self) -> Optional[QQuickAnchorsPrivate]:
    """
    Calls Qt's 'QQuickAnchorsPrivate *QQuickAnchors::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanchors.html#d_func

    Returns
    -------

    Optional[QQuickAnchorsPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickAnchorsPrivate *QQuickAnchors::d_func()
    address = self.uglySide.call('ritual_ZN13QQuickAnchors6d_funcEv')
    from . import QQuickAnchorsPrivate
    return QQuickAnchorsPrivate._cuteAt(address)
