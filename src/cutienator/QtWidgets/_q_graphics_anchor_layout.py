"""
QGraphicsAnchorLayout binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qgraphicsanchorlayout.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import Qt
from . import QGraphicsLayout, QGraphicsLayoutItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QRectF, QSizeF
  from . import QGraphicsAnchor
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRectF = WAIT['QRectF']
  QSizeF = WAIT['QSizeF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGraphicsAnchorLayout(QGraphicsLayout):
  """
  The cute side of Qt's QGraphicsAnchorLayout: a plain Python object standing
  in front of one C++ QGraphicsAnchorLayout.

  It is built on the cute 'QGraphicsLayout', as Qt's QGraphicsAnchorLayout is
  built on Qt's QGraphicsLayout, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QGraphicsAnchorLayout that has a ritual and that
  Python can call so far, 15 names in all: 'addAnchor', 'anchor',
  'addCornerAnchors', 'addAnchors', 'setHorizontalSpacing',
  'setVerticalSpacing', 'setSpacing', 'horizontalSpacing', 'verticalSpacing',
  'removeAt', 'setGeometry', 'count', 'itemAt', 'invalidate', 'sizeHint'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGraphicsAnchorLayout::~QGraphicsAnchorLayout()': the destructor:
    Python never removes a C++ QGraphicsAnchorLayout.

  What has no ritual
  ------------------

  4 of the 21 functions Qt declares: 2 forbidden; 2 private.

  What to expect
  --------------

  - The C++ QGraphicsAnchorLayout is created at the first use, not by
    'QGraphicsAnchorLayout(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGraphicsAnchorLayout.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGraphicsAnchorLayout'

  #  A C++ QGraphicsAnchorLayout Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGraphicsAnchorLayout'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def horizontalSpacing(self) -> float:
    """
    Calls Qt's 'qreal QGraphicsAnchorLayout::horizontalSpacing() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsanchorlayout.html#horizontalSpacing
    """
    #  qreal QGraphicsAnchorLayout::horizontalSpacing() const
    return self.uglySide.call(
        'ritual_ZNK21QGraphicsAnchorLayout17horizontalSpacingEv',
    )

  def verticalSpacing(self) -> float:
    """
    Calls Qt's 'qreal QGraphicsAnchorLayout::verticalSpacing() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsanchorlayout.html#verticalSpacing
    """
    #  qreal QGraphicsAnchorLayout::verticalSpacing() const
    return self.uglySide.call(
        'ritual_ZNK21QGraphicsAnchorLayout15verticalSpacingEv',
    )

  def count(self) -> int:
    """
    Calls Qt's 'int QGraphicsAnchorLayout::count() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsanchorlayout.html#count
    """
    #  int QGraphicsAnchorLayout::count() const
    ritual = 'ritual_ZNK21QGraphicsAnchorLayout5countEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QGraphicsAnchorLayout5countEv'
    return self.uglySide.call(ritual)

  @overload(int)
  def itemAt(self, index: int) -> Optional[QGraphicsLayoutItem]:
    """
    Calls Qt's 'QGraphicsLayoutItem *QGraphicsAnchorLayout::itemAt(int index)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsanchorlayout.html#itemAt

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[QGraphicsLayoutItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphicsLayoutItem *QGraphicsAnchorLayout::itemAt(int index) const
    ritual = 'ritual_ZNK21QGraphicsAnchorLayout6itemAtEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QGraphicsAnchorLayout6itemAtEi'
    address = self.uglySide.call(ritual, index)
    return QGraphicsLayoutItem._cuteAt(address)

  @overload(Qt.SizeHint)
  @overload(Qt.SizeHint, QSizeF)
  def sizeHint(
      self,
      which: Qt.SizeHint,
      constraint: Optional[QSizeF] = None,
  ) -> QSizeF:
    """
    Calls Qt's 'QSizeF QGraphicsAnchorLayout::sizeHint(Qt::SizeHint which,
    const QSizeF &constraint) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsanchorlayout.html#sizeHint

    Parameters
    ----------

    which : Qt.SizeHint
      Passed on as its number.

    constraint : Optional[QSizeF]
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own. May be left out, as in Qt: a new 'QSizeF()' is then passed on.

    Returns
    -------

    QSizeF
      A new cute QSizeF around the copy Qt gave back. Python owns it.
    """
    #  QSizeF QGraphicsAnchorLayout::sizeHint(Qt::SizeHint which, const
    #      QSizeF &constraint) const
    if constraint is None:
      from ..QtCore import QSizeF
      constraint = QSizeF()
    address = self.uglySide.call(
        'ritual_own_ZNK21QGraphicsAnchorLayout8sizeHintEN2Qt8SizeHintERK6QS'
        'izeF',
        which.value, self._valueOf(constraint),
    )
    from ..QtCore import QSizeF
    return QSizeF._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setHorizontalSpacing(self, spacing: float) -> None:
    """
    Calls Qt's 'void QGraphicsAnchorLayout::setHorizontalSpacing(qreal
    spacing)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsanchorlayout.html#setHorizontalSpacing

    Parameters
    ----------

    spacing : float
      Passed on as it is.
    """
    #  void QGraphicsAnchorLayout::setHorizontalSpacing(qreal spacing)
    self.uglySide.call(
        'ritual_ZN21QGraphicsAnchorLayout20setHorizontalSpacingEd', spacing,
    )

  @overload(float)
  def setVerticalSpacing(self, spacing: float) -> None:
    """
    Calls Qt's 'void QGraphicsAnchorLayout::setVerticalSpacing(qreal
    spacing)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsanchorlayout.html#setVerticalSpacing

    Parameters
    ----------

    spacing : float
      Passed on as it is.
    """
    #  void QGraphicsAnchorLayout::setVerticalSpacing(qreal spacing)
    self.uglySide.call(
        'ritual_ZN21QGraphicsAnchorLayout18setVerticalSpacingEd', spacing,
    )

  @overload(float)
  def setSpacing(self, spacing: float) -> None:
    """
    Calls Qt's 'void QGraphicsAnchorLayout::setSpacing(qreal spacing)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsanchorlayout.html#setSpacing

    Parameters
    ----------

    spacing : float
      Passed on as it is.
    """
    #  void QGraphicsAnchorLayout::setSpacing(qreal spacing)
    self.uglySide.call(
        'ritual_ZN21QGraphicsAnchorLayout10setSpacingEd', spacing,
    )

  @overload(QRectF)
  def setGeometry(self, rect: QRectF) -> None:
    """
    Calls Qt's 'void QGraphicsAnchorLayout::setGeometry(const QRectF &rect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsanchorlayout.html#setGeometry

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QGraphicsAnchorLayout::setGeometry(const QRectF &rect)
    ritual = 'ritual_ZN21QGraphicsAnchorLayout11setGeometryERK6QRectF'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QGraphicsAnchorLayout11setGeometryERK6QRectF'
    self.uglySide.call(ritual, self._valueOf(rect))

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
  @overload(QGraphicsLayoutItem)
  @overload(NoneType)
  def __init__(self, parent: Optional[QGraphicsLayoutItem] = None) -> None:
    """
    Notes what was given, for Qt's
    'QGraphicsAnchorLayout::QGraphicsAnchorLayout(QGraphicsLayoutItem
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsanchorlayout.html#QGraphicsAnchorLayout

    Parameters
    ----------

    parent : Optional[QGraphicsLayoutItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QGraphicsAnchorLayout::QGraphicsAnchorLayout(QGraphicsLayoutItem
    #      *parent)
    self._noteCreation(QGraphicsAnchorLayout, lambda: Rituals.call(
        'ritual_ZN21QGraphicsAnchorLayoutC1EP19QGraphicsLayoutItem',
        self._addressOf(parent, 'QGraphicsLayoutItem'),
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

  @overload(
      QGraphicsLayoutItem, Qt.AnchorPoint, QGraphicsLayoutItem,
      Qt.AnchorPoint,
  )
  @overload(QGraphicsLayoutItem, Qt.AnchorPoint, NoneType, Qt.AnchorPoint)
  @overload(NoneType, Qt.AnchorPoint, QGraphicsLayoutItem, Qt.AnchorPoint)
  @overload(NoneType, Qt.AnchorPoint, NoneType, Qt.AnchorPoint)
  def addAnchor(
      self,
      firstItem: Optional[QGraphicsLayoutItem],
      firstEdge: Qt.AnchorPoint,
      secondItem: Optional[QGraphicsLayoutItem],
      secondEdge: Qt.AnchorPoint,
  ) -> Optional[QGraphicsAnchor]:
    """
    Calls Qt's 'QGraphicsAnchor
    *QGraphicsAnchorLayout::addAnchor(QGraphicsLayoutItem *firstItem,
    Qt::AnchorPoint firstEdge, QGraphicsLayoutItem *secondItem,
    Qt::AnchorPoint secondEdge)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsanchorlayout.html#addAnchor

    Parameters
    ----------

    firstItem : Optional[QGraphicsLayoutItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    firstEdge : Qt.AnchorPoint
      Passed on as its number.

    secondItem : Optional[QGraphicsLayoutItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    secondEdge : Qt.AnchorPoint
      Passed on as its number.

    Returns
    -------

    Optional[QGraphicsAnchor]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphicsAnchor *QGraphicsAnchorLayout::addAnchor(QGraphicsLayoutItem
    #      *firstItem, Qt::AnchorPoint firstEdge, QGraphicsLayoutItem
    #      *secondItem, Qt::AnchorPoint secondEdge)
    address = self.uglySide.call(
        'ritual_ZN21QGraphicsAnchorLayout9addAnchorEP19QGraphicsLayoutItemN'
        '2Qt11AnchorPointES1_S3_',
        self._addressOf(firstItem, 'QGraphicsLayoutItem'), firstEdge.value,
        self._addressOf(secondItem, 'QGraphicsLayoutItem'), secondEdge.value,
    )
    from . import QGraphicsAnchor
    return QGraphicsAnchor._cuteAt(address)

  @overload(
      QGraphicsLayoutItem, Qt.AnchorPoint, QGraphicsLayoutItem,
      Qt.AnchorPoint,
  )
  @overload(QGraphicsLayoutItem, Qt.AnchorPoint, NoneType, Qt.AnchorPoint)
  @overload(NoneType, Qt.AnchorPoint, QGraphicsLayoutItem, Qt.AnchorPoint)
  @overload(NoneType, Qt.AnchorPoint, NoneType, Qt.AnchorPoint)
  def anchor(
      self,
      firstItem: Optional[QGraphicsLayoutItem],
      firstEdge: Qt.AnchorPoint,
      secondItem: Optional[QGraphicsLayoutItem],
      secondEdge: Qt.AnchorPoint,
  ) -> Optional[QGraphicsAnchor]:
    """
    Calls Qt's 'QGraphicsAnchor
    *QGraphicsAnchorLayout::anchor(QGraphicsLayoutItem *firstItem,
    Qt::AnchorPoint firstEdge, QGraphicsLayoutItem *secondItem,
    Qt::AnchorPoint secondEdge)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsanchorlayout.html#anchor

    Parameters
    ----------

    firstItem : Optional[QGraphicsLayoutItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    firstEdge : Qt.AnchorPoint
      Passed on as its number.

    secondItem : Optional[QGraphicsLayoutItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    secondEdge : Qt.AnchorPoint
      Passed on as its number.

    Returns
    -------

    Optional[QGraphicsAnchor]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphicsAnchor *QGraphicsAnchorLayout::anchor(QGraphicsLayoutItem
    #      *firstItem, Qt::AnchorPoint firstEdge, QGraphicsLayoutItem
    #      *secondItem, Qt::AnchorPoint secondEdge)
    address = self.uglySide.call(
        'ritual_ZN21QGraphicsAnchorLayout6anchorEP19QGraphicsLayoutItemN2Qt'
        '11AnchorPointES1_S3_',
        self._addressOf(firstItem, 'QGraphicsLayoutItem'), firstEdge.value,
        self._addressOf(secondItem, 'QGraphicsLayoutItem'), secondEdge.value,
    )
    from . import QGraphicsAnchor
    return QGraphicsAnchor._cuteAt(address)

  @overload(QGraphicsLayoutItem, Qt.Corner, QGraphicsLayoutItem, Qt.Corner)
  @overload(QGraphicsLayoutItem, Qt.Corner, NoneType, Qt.Corner)
  @overload(NoneType, Qt.Corner, QGraphicsLayoutItem, Qt.Corner)
  @overload(NoneType, Qt.Corner, NoneType, Qt.Corner)
  def addCornerAnchors(
      self,
      firstItem: Optional[QGraphicsLayoutItem],
      firstCorner: Qt.Corner,
      secondItem: Optional[QGraphicsLayoutItem],
      secondCorner: Qt.Corner,
  ) -> None:
    """
    Calls Qt's 'void
    QGraphicsAnchorLayout::addCornerAnchors(QGraphicsLayoutItem *firstItem,
    Qt::Corner firstCorner, QGraphicsLayoutItem *secondItem, Qt::Corner
    secondCorner)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsanchorlayout.html#addCornerAnchors

    Parameters
    ----------

    firstItem : Optional[QGraphicsLayoutItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    firstCorner : Qt.Corner
      Passed on as its number.

    secondItem : Optional[QGraphicsLayoutItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    secondCorner : Qt.Corner
      Passed on as its number.
    """
    #  void QGraphicsAnchorLayout::addCornerAnchors(QGraphicsLayoutItem
    #      *firstItem, Qt::Corner firstCorner, QGraphicsLayoutItem
    #      *secondItem, Qt::Corner secondCorner)
    self.uglySide.call(
        'ritual_ZN21QGraphicsAnchorLayout16addCornerAnchorsEP19QGraphicsLay'
        'outItemN2Qt6CornerES1_S3_',
        self._addressOf(firstItem, 'QGraphicsLayoutItem'), firstCorner.value,
        self._addressOf(secondItem, 'QGraphicsLayoutItem'),
        secondCorner.value,
    )

  @overload(QGraphicsLayoutItem, QGraphicsLayoutItem)
  @overload(QGraphicsLayoutItem, NoneType)
  @overload(NoneType, QGraphicsLayoutItem)
  @overload(NoneType, NoneType)
  @overload(QGraphicsLayoutItem, QGraphicsLayoutItem, Qt.Orientations)
  @overload(QGraphicsLayoutItem, NoneType, Qt.Orientations)
  @overload(NoneType, QGraphicsLayoutItem, Qt.Orientations)
  @overload(NoneType, NoneType, Qt.Orientations)
  def addAnchors(
      self,
      firstItem: Optional[QGraphicsLayoutItem],
      secondItem: Optional[QGraphicsLayoutItem],
      orientations: Qt.Orientations = (
          Qt.Orientations.Horizontal | Qt.Orientations.Vertical),
  ) -> None:
    """
    Calls Qt's 'void QGraphicsAnchorLayout::addAnchors(QGraphicsLayoutItem
    *firstItem, QGraphicsLayoutItem *secondItem, Qt::Orientations
    orientations)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsanchorlayout.html#addAnchors

    Parameters
    ----------

    firstItem : Optional[QGraphicsLayoutItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    secondItem : Optional[QGraphicsLayoutItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    orientations : Qt.Orientations
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.Orientations.Horizontal | Qt.Orientations.Vertical.
    """
    #  void QGraphicsAnchorLayout::addAnchors(QGraphicsLayoutItem *firstItem,
    #      QGraphicsLayoutItem *secondItem, Qt::Orientations orientations)
    self.uglySide.call(
        'ritual_ZN21QGraphicsAnchorLayout10addAnchorsEP19QGraphicsLayoutIte'
        'mS1_6QFlagsIN2Qt11OrientationEE',
        self._addressOf(firstItem, 'QGraphicsLayoutItem'),
        self._addressOf(secondItem, 'QGraphicsLayoutItem'),
        orientations.value,
    )

  @overload(int)
  def removeAt(self, index: int) -> None:
    """
    Calls Qt's 'void QGraphicsAnchorLayout::removeAt(int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsanchorlayout.html#removeAt

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QGraphicsAnchorLayout::removeAt(int index)
    ritual = 'ritual_ZN21QGraphicsAnchorLayout8removeAtEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QGraphicsAnchorLayout8removeAtEi'
    self.uglySide.call(ritual, index)

  def invalidate(self) -> None:
    """
    Calls Qt's 'void QGraphicsAnchorLayout::invalidate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsanchorlayout.html#invalidate
    """
    #  void QGraphicsAnchorLayout::invalidate()
    ritual = 'ritual_ZN21QGraphicsAnchorLayout10invalidateEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QGraphicsAnchorLayout10invalidateEv'
    self.uglySide.call(ritual)
