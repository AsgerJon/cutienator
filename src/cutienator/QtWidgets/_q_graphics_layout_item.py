"""
QGraphicsLayoutItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qgraphicslayoutitem.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..QtCore import Qt
from . import QSizePolicy

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QRectF, QSizeF
  from . import QGraphicsItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRectF = WAIT['QRectF']
  QSizeF = WAIT['QSizeF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGraphicsLayoutItem(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QGraphicsLayoutItem: a plain Python object standing
  in front of one C++ QGraphicsLayoutItem.

  What exists
  -----------

  Every function of Qt's QGraphicsLayoutItem that has a ritual and that
  Python can call so far, 31 names in all: 'setSizePolicy', 'sizePolicy',
  'setMinimumSize', 'minimumSize', 'setMinimumWidth', 'minimumWidth',
  'setMinimumHeight', 'minimumHeight', 'setPreferredSize', 'preferredSize',
  'setPreferredWidth', 'preferredWidth', 'setPreferredHeight',
  'preferredHeight', 'setMaximumSize', 'maximumSize', 'setMaximumWidth',
  'maximumWidth', 'setMaximumHeight', 'maximumHeight', 'setGeometry',
  'geometry', 'contentsRect', 'effectiveSizeHint', 'updateGeometry',
  'isEmpty', 'parentLayoutItem', 'setParentLayoutItem', 'isLayout',
  'graphicsItem', 'ownedByLayout'. None can be made from Python: one comes
  out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGraphicsLayoutItem::~QGraphicsLayoutItem()': the destructor:
    Python never removes a C++ QGraphicsLayoutItem.
  - Qt's 'void QGraphicsLayoutItem::getContentsMargins(qreal *left, qreal
    *top, qreal *right, qreal *bottom) const': takes a number to change where
    it is.

  What has no ritual
  ------------------

  8 of the 45 functions Qt declares: 4 protected; 3 private; 1 the class is
  abstract, so C++ cannot make one.

  What to expect
  --------------

  - The C++ QGraphicsLayoutItem is created at the first use, not by
    'QGraphicsLayoutItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGraphicsLayoutItem.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGraphicsLayoutItem'

  #  A C++ QGraphicsLayoutItem Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGraphicsLayoutItem'

  #  The functions Qt calls itself that QGraphicsLayoutItem is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'getContentsMargins': (
          'void QGraphicsLayoutItem::getContentsMargins(qreal *, qreal *, '
          'qreal *, qreal *) const',
      ),
  }

  #  The functions Qt calls itself that QGraphicsLayoutItem is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'setGeometry': (
          ('_ZN19QGraphicsLayoutItem11setGeometryERK6QRectF',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QRectF'),
           )),
      ),
      'updateGeometry': (
          ('_ZN19QGraphicsLayoutItem14updateGeometryEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'isEmpty': (
          ('_ZNK19QGraphicsLayoutItem7isEmptyEv',
           ('bool', 'number', ''),
           ()),
      ),
      'sizeHint': (
          ('_ZNK19QGraphicsLayoutItem8sizeHintEN2Qt8SizeHintERK6QSizeF',
           ('address', 'value', 'QtCore:QSizeF'),
           (
               ('int', 'enum', 'QtCore:Qt.SizeHint'),
               ('address', 'value', 'QtCore:QSizeF'),
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

  def sizePolicy(self) -> QSizePolicy:
    """
    Calls Qt's 'QSizePolicy QGraphicsLayoutItem::sizePolicy() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicslayoutitem.html#sizePolicy

    Returns
    -------

    QSizePolicy
      A new cute QSizePolicy around the copy Qt gave back. Python owns it.
    """
    #  QSizePolicy QGraphicsLayoutItem::sizePolicy() const
    address = self._callAs(
        'QGraphicsLayoutItem',
        'ritual_ZNK19QGraphicsLayoutItem10sizePolicyEv',
    )
    return QSizePolicy._cuteOwning(address)

  def minimumSize(self) -> QSizeF:
    """
    Calls Qt's 'QSizeF QGraphicsLayoutItem::minimumSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicslayoutitem.html#minimumSize

    Returns
    -------

    QSizeF
      A new cute QSizeF around the copy Qt gave back. Python owns it.
    """
    #  QSizeF QGraphicsLayoutItem::minimumSize() const
    address = self._callAs(
        'QGraphicsLayoutItem',
        'ritual_ZNK19QGraphicsLayoutItem11minimumSizeEv',
    )
    from ..QtCore import QSizeF
    return QSizeF._cuteOwning(address)

  def minimumWidth(self) -> float:
    """
    Calls Qt's 'qreal QGraphicsLayoutItem::minimumWidth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicslayoutitem.html#minimumWidth
    """
    #  qreal QGraphicsLayoutItem::minimumWidth() const
    return self._callAs(
        'QGraphicsLayoutItem',
        'ritual_ZNK19QGraphicsLayoutItem12minimumWidthEv',
    )

  def minimumHeight(self) -> float:
    """
    Calls Qt's 'qreal QGraphicsLayoutItem::minimumHeight() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicslayoutitem.html#minimumHeight
    """
    #  qreal QGraphicsLayoutItem::minimumHeight() const
    return self._callAs(
        'QGraphicsLayoutItem',
        'ritual_ZNK19QGraphicsLayoutItem13minimumHeightEv',
    )

  def preferredSize(self) -> QSizeF:
    """
    Calls Qt's 'QSizeF QGraphicsLayoutItem::preferredSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicslayoutitem.html#preferredSize

    Returns
    -------

    QSizeF
      A new cute QSizeF around the copy Qt gave back. Python owns it.
    """
    #  QSizeF QGraphicsLayoutItem::preferredSize() const
    address = self._callAs(
        'QGraphicsLayoutItem',
        'ritual_ZNK19QGraphicsLayoutItem13preferredSizeEv',
    )
    from ..QtCore import QSizeF
    return QSizeF._cuteOwning(address)

  def preferredWidth(self) -> float:
    """
    Calls Qt's 'qreal QGraphicsLayoutItem::preferredWidth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicslayoutitem.html#preferredWidth
    """
    #  qreal QGraphicsLayoutItem::preferredWidth() const
    return self._callAs(
        'QGraphicsLayoutItem',
        'ritual_ZNK19QGraphicsLayoutItem14preferredWidthEv',
    )

  def preferredHeight(self) -> float:
    """
    Calls Qt's 'qreal QGraphicsLayoutItem::preferredHeight() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicslayoutitem.html#preferredHeight
    """
    #  qreal QGraphicsLayoutItem::preferredHeight() const
    return self._callAs(
        'QGraphicsLayoutItem',
        'ritual_ZNK19QGraphicsLayoutItem15preferredHeightEv',
    )

  def maximumSize(self) -> QSizeF:
    """
    Calls Qt's 'QSizeF QGraphicsLayoutItem::maximumSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicslayoutitem.html#maximumSize

    Returns
    -------

    QSizeF
      A new cute QSizeF around the copy Qt gave back. Python owns it.
    """
    #  QSizeF QGraphicsLayoutItem::maximumSize() const
    address = self._callAs(
        'QGraphicsLayoutItem',
        'ritual_ZNK19QGraphicsLayoutItem11maximumSizeEv',
    )
    from ..QtCore import QSizeF
    return QSizeF._cuteOwning(address)

  def maximumWidth(self) -> float:
    """
    Calls Qt's 'qreal QGraphicsLayoutItem::maximumWidth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicslayoutitem.html#maximumWidth
    """
    #  qreal QGraphicsLayoutItem::maximumWidth() const
    return self._callAs(
        'QGraphicsLayoutItem',
        'ritual_ZNK19QGraphicsLayoutItem12maximumWidthEv',
    )

  def maximumHeight(self) -> float:
    """
    Calls Qt's 'qreal QGraphicsLayoutItem::maximumHeight() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicslayoutitem.html#maximumHeight
    """
    #  qreal QGraphicsLayoutItem::maximumHeight() const
    return self._callAs(
        'QGraphicsLayoutItem',
        'ritual_ZNK19QGraphicsLayoutItem13maximumHeightEv',
    )

  def geometry(self) -> QRectF:
    """
    Calls Qt's 'QRectF QGraphicsLayoutItem::geometry() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicslayoutitem.html#geometry

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QGraphicsLayoutItem::geometry() const
    address = self._callAs(
        'QGraphicsLayoutItem', 'ritual_ZNK19QGraphicsLayoutItem8geometryEv',
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def contentsRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QGraphicsLayoutItem::contentsRect() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicslayoutitem.html#contentsRect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QGraphicsLayoutItem::contentsRect() const
    address = self._callAs(
        'QGraphicsLayoutItem',
        'ritual_ZNK19QGraphicsLayoutItem12contentsRectEv',
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @overload(Qt.SizeHint)
  @overload(Qt.SizeHint, QSizeF)
  def effectiveSizeHint(
      self,
      which: Qt.SizeHint,
      constraint: Optional[QSizeF] = None,
  ) -> QSizeF:
    """
    Calls Qt's 'QSizeF QGraphicsLayoutItem::effectiveSizeHint(Qt::SizeHint
    which, const QSizeF &constraint) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicslayoutitem.html#effectiveSizeHint

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
    #  QSizeF QGraphicsLayoutItem::effectiveSizeHint(Qt::SizeHint which,
    #      const QSizeF &constraint) const
    if constraint is None:
      from ..QtCore import QSizeF
      constraint = QSizeF()
    address = self._callAs(
        'QGraphicsLayoutItem',
        'ritual_ZNK19QGraphicsLayoutItem17effectiveSizeHintEN2Qt8SizeHintER'
        'K6QSizeF',
        which.value, self._valueOf(constraint),
    )
    from ..QtCore import QSizeF
    return QSizeF._cuteOwning(address)

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QGraphicsLayoutItem::isEmpty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicslayoutitem.html#isEmpty
    """
    #  bool QGraphicsLayoutItem::isEmpty() const
    ritual = 'ritual_ZNK19QGraphicsLayoutItem7isEmptyEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QGraphicsLayoutItem7isEmptyEv'
    return self._callAs('QGraphicsLayoutItem', ritual)

  def parentLayoutItem(self) -> Optional[QGraphicsLayoutItem]:
    """
    Calls Qt's 'QGraphicsLayoutItem *QGraphicsLayoutItem::parentLayoutItem()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicslayoutitem.html#parentLayoutItem

    Returns
    -------

    Optional[QGraphicsLayoutItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphicsLayoutItem *QGraphicsLayoutItem::parentLayoutItem() const
    address = self._callAs(
        'QGraphicsLayoutItem',
        'ritual_ZNK19QGraphicsLayoutItem16parentLayoutItemEv',
    )
    return QGraphicsLayoutItem._cuteAt(address)

  def isLayout(self) -> bool:
    """
    Calls Qt's 'bool QGraphicsLayoutItem::isLayout() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicslayoutitem.html#isLayout
    """
    #  bool QGraphicsLayoutItem::isLayout() const
    return self._callAs(
        'QGraphicsLayoutItem', 'ritual_ZNK19QGraphicsLayoutItem8isLayoutEv',
    )

  def graphicsItem(self) -> Optional[QGraphicsItem]:
    """
    Calls Qt's 'QGraphicsItem *QGraphicsLayoutItem::graphicsItem() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicslayoutitem.html#graphicsItem

    Returns
    -------

    Optional[QGraphicsItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphicsItem *QGraphicsLayoutItem::graphicsItem() const
    address = self._callAs(
        'QGraphicsLayoutItem',
        'ritual_ZNK19QGraphicsLayoutItem12graphicsItemEv',
    )
    from . import QGraphicsItem
    return QGraphicsItem._cuteAt(address)

  def ownedByLayout(self) -> bool:
    """
    Calls Qt's 'bool QGraphicsLayoutItem::ownedByLayout() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicslayoutitem.html#ownedByLayout
    """
    #  bool QGraphicsLayoutItem::ownedByLayout() const
    return self._callAs(
        'QGraphicsLayoutItem',
        'ritual_ZNK19QGraphicsLayoutItem13ownedByLayoutEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QSizePolicy)
  def setSizePolicy(self, policy: QSizePolicy) -> None:
    """
    Calls Qt's 'void QGraphicsLayoutItem::setSizePolicy(const QSizePolicy
    &policy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicslayoutitem.html#setSizePolicy

    Parameters
    ----------

    policy : QSizePolicy
      Passed on as a value: Qt reads the C++ QSizePolicy, which stays
      Python's own.
    """
    #  void QGraphicsLayoutItem::setSizePolicy(const QSizePolicy &policy)
    self._callAs(
        'QGraphicsLayoutItem',
        'ritual_ZN19QGraphicsLayoutItem13setSizePolicyERK11QSizePolicy',
        self._valueOf(policy),
    )

  @overload(QSizePolicy.Policy, QSizePolicy.Policy)
  @overload(QSizePolicy.Policy, QSizePolicy.Policy, QSizePolicy.ControlType)
  def setSizePolicy(
      self,
      hPolicy: QSizePolicy.Policy,
      vPolicy: QSizePolicy.Policy,
      controlType: QSizePolicy.ControlType = (
          QSizePolicy.ControlType.DefaultType),
  ) -> None:
    """
    Calls Qt's 'void QGraphicsLayoutItem::setSizePolicy(QSizePolicy::Policy
    hPolicy, QSizePolicy::Policy vPolicy, QSizePolicy::ControlType
    controlType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicslayoutitem.html#setSizePolicy

    Parameters
    ----------

    hPolicy : QSizePolicy.Policy
      Passed on as its number.

    vPolicy : QSizePolicy.Policy
      Passed on as its number.

    controlType : QSizePolicy.ControlType
      Passed on as its number. May be left out, as in Qt: it is then
      QSizePolicy.ControlType.DefaultType.
    """
    #  void QGraphicsLayoutItem::setSizePolicy(QSizePolicy::Policy hPolicy,
    #      QSizePolicy::Policy vPolicy, QSizePolicy::ControlType controlType)
    self._callAs(
        'QGraphicsLayoutItem',
        'ritual_ZN19QGraphicsLayoutItem13setSizePolicyEN11QSizePolicy6Polic'
        'yES1_NS0_11ControlTypeE',
        hPolicy.value, vPolicy.value, controlType.value,
    )

  @overload(QSizeF)
  def setMinimumSize(self, size: QSizeF) -> None:
    """
    Calls Qt's 'void QGraphicsLayoutItem::setMinimumSize(const QSizeF
    &size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicslayoutitem.html#setMinimumSize

    Parameters
    ----------

    size : QSizeF
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own.
    """
    #  void QGraphicsLayoutItem::setMinimumSize(const QSizeF &size)
    self._callAs(
        'QGraphicsLayoutItem',
        'ritual_ZN19QGraphicsLayoutItem14setMinimumSizeERK6QSizeF',
        self._valueOf(size),
    )

  @overload(float, float)
  def setMinimumSize(self, w: float, h: float) -> None:
    """
    Calls Qt's 'void QGraphicsLayoutItem::setMinimumSize(qreal w, qreal h)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicslayoutitem.html#setMinimumSize

    Parameters
    ----------

    w : float
      Passed on as it is.

    h : float
      Passed on as it is.
    """
    #  void QGraphicsLayoutItem::setMinimumSize(qreal w, qreal h)
    self._callAs(
        'QGraphicsLayoutItem',
        'ritual_ZN19QGraphicsLayoutItem14setMinimumSizeEdd',
        w, h,
    )

  @overload(float)
  def setMinimumWidth(self, width: float) -> None:
    """
    Calls Qt's 'void QGraphicsLayoutItem::setMinimumWidth(qreal width)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicslayoutitem.html#setMinimumWidth

    Parameters
    ----------

    width : float
      Passed on as it is.
    """
    #  void QGraphicsLayoutItem::setMinimumWidth(qreal width)
    self._callAs(
        'QGraphicsLayoutItem',
        'ritual_ZN19QGraphicsLayoutItem15setMinimumWidthEd',
        width,
    )

  @overload(float)
  def setMinimumHeight(self, height: float) -> None:
    """
    Calls Qt's 'void QGraphicsLayoutItem::setMinimumHeight(qreal height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicslayoutitem.html#setMinimumHeight

    Parameters
    ----------

    height : float
      Passed on as it is.
    """
    #  void QGraphicsLayoutItem::setMinimumHeight(qreal height)
    self._callAs(
        'QGraphicsLayoutItem',
        'ritual_ZN19QGraphicsLayoutItem16setMinimumHeightEd',
        height,
    )

  @overload(QSizeF)
  def setPreferredSize(self, size: QSizeF) -> None:
    """
    Calls Qt's 'void QGraphicsLayoutItem::setPreferredSize(const QSizeF
    &size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicslayoutitem.html#setPreferredSize

    Parameters
    ----------

    size : QSizeF
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own.
    """
    #  void QGraphicsLayoutItem::setPreferredSize(const QSizeF &size)
    self._callAs(
        'QGraphicsLayoutItem',
        'ritual_ZN19QGraphicsLayoutItem16setPreferredSizeERK6QSizeF',
        self._valueOf(size),
    )

  @overload(float, float)
  def setPreferredSize(self, w: float, h: float) -> None:
    """
    Calls Qt's 'void QGraphicsLayoutItem::setPreferredSize(qreal w, qreal
    h)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicslayoutitem.html#setPreferredSize

    Parameters
    ----------

    w : float
      Passed on as it is.

    h : float
      Passed on as it is.
    """
    #  void QGraphicsLayoutItem::setPreferredSize(qreal w, qreal h)
    self._callAs(
        'QGraphicsLayoutItem',
        'ritual_ZN19QGraphicsLayoutItem16setPreferredSizeEdd',
        w, h,
    )

  @overload(float)
  def setPreferredWidth(self, width: float) -> None:
    """
    Calls Qt's 'void QGraphicsLayoutItem::setPreferredWidth(qreal width)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicslayoutitem.html#setPreferredWidth

    Parameters
    ----------

    width : float
      Passed on as it is.
    """
    #  void QGraphicsLayoutItem::setPreferredWidth(qreal width)
    self._callAs(
        'QGraphicsLayoutItem',
        'ritual_ZN19QGraphicsLayoutItem17setPreferredWidthEd',
        width,
    )

  @overload(float)
  def setPreferredHeight(self, height: float) -> None:
    """
    Calls Qt's 'void QGraphicsLayoutItem::setPreferredHeight(qreal height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicslayoutitem.html#setPreferredHeight

    Parameters
    ----------

    height : float
      Passed on as it is.
    """
    #  void QGraphicsLayoutItem::setPreferredHeight(qreal height)
    self._callAs(
        'QGraphicsLayoutItem',
        'ritual_ZN19QGraphicsLayoutItem18setPreferredHeightEd',
        height,
    )

  @overload(QSizeF)
  def setMaximumSize(self, size: QSizeF) -> None:
    """
    Calls Qt's 'void QGraphicsLayoutItem::setMaximumSize(const QSizeF
    &size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicslayoutitem.html#setMaximumSize

    Parameters
    ----------

    size : QSizeF
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own.
    """
    #  void QGraphicsLayoutItem::setMaximumSize(const QSizeF &size)
    self._callAs(
        'QGraphicsLayoutItem',
        'ritual_ZN19QGraphicsLayoutItem14setMaximumSizeERK6QSizeF',
        self._valueOf(size),
    )

  @overload(float, float)
  def setMaximumSize(self, w: float, h: float) -> None:
    """
    Calls Qt's 'void QGraphicsLayoutItem::setMaximumSize(qreal w, qreal h)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicslayoutitem.html#setMaximumSize

    Parameters
    ----------

    w : float
      Passed on as it is.

    h : float
      Passed on as it is.
    """
    #  void QGraphicsLayoutItem::setMaximumSize(qreal w, qreal h)
    self._callAs(
        'QGraphicsLayoutItem',
        'ritual_ZN19QGraphicsLayoutItem14setMaximumSizeEdd',
        w, h,
    )

  @overload(float)
  def setMaximumWidth(self, width: float) -> None:
    """
    Calls Qt's 'void QGraphicsLayoutItem::setMaximumWidth(qreal width)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicslayoutitem.html#setMaximumWidth

    Parameters
    ----------

    width : float
      Passed on as it is.
    """
    #  void QGraphicsLayoutItem::setMaximumWidth(qreal width)
    self._callAs(
        'QGraphicsLayoutItem',
        'ritual_ZN19QGraphicsLayoutItem15setMaximumWidthEd',
        width,
    )

  @overload(float)
  def setMaximumHeight(self, height: float) -> None:
    """
    Calls Qt's 'void QGraphicsLayoutItem::setMaximumHeight(qreal height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicslayoutitem.html#setMaximumHeight

    Parameters
    ----------

    height : float
      Passed on as it is.
    """
    #  void QGraphicsLayoutItem::setMaximumHeight(qreal height)
    self._callAs(
        'QGraphicsLayoutItem',
        'ritual_ZN19QGraphicsLayoutItem16setMaximumHeightEd',
        height,
    )

  @overload(QRectF)
  def setGeometry(self, rect: QRectF) -> None:
    """
    Calls Qt's 'void QGraphicsLayoutItem::setGeometry(const QRectF &rect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicslayoutitem.html#setGeometry

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QGraphicsLayoutItem::setGeometry(const QRectF &rect)
    ritual = 'ritual_ZN19QGraphicsLayoutItem11setGeometryERK6QRectF'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QGraphicsLayoutItem11setGeometryERK6QRectF'
    self._callAs('QGraphicsLayoutItem', ritual, self._valueOf(rect))

  @overload(THIS)
  @overload(NoneType)
  def setParentLayoutItem(
      self,
      parent: Optional[QGraphicsLayoutItem],
  ) -> None:
    """
    Calls Qt's 'void
    QGraphicsLayoutItem::setParentLayoutItem(QGraphicsLayoutItem *parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicslayoutitem.html#setParentLayoutItem

    Parameters
    ----------

    parent : Optional[QGraphicsLayoutItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsLayoutItem::setParentLayoutItem(QGraphicsLayoutItem
    #      *parent)
    self._callAs(
        'QGraphicsLayoutItem',
        'ritual_ZN19QGraphicsLayoutItem19setParentLayoutItemEPS_',
        self._addressOf(parent, 'QGraphicsLayoutItem'),
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

  def updateGeometry(self) -> None:
    """
    Calls Qt's 'void QGraphicsLayoutItem::updateGeometry()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicslayoutitem.html#updateGeometry
    """
    #  void QGraphicsLayoutItem::updateGeometry()
    ritual = 'ritual_ZN19QGraphicsLayoutItem14updateGeometryEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QGraphicsLayoutItem14updateGeometryEv'
    self._callAs('QGraphicsLayoutItem', ritual)
