"""
QQuickScrollBarPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickscrollbar_p_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickScrollBarPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QQuickControlPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QPointF
  from ..QtQuick import QQuickItem
  from . import QQuickScrollBar
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPointF = WAIT['QPointF']
  QQuickItem = WAIT['QQuickItem']
  QQuickScrollBar = WAIT['QQuickScrollBar']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickScrollBarPrivate(QQuickControlPrivate):
  """
  The cute side of Qt's QQuickScrollBarPrivate: a plain Python object
  standing in front of one C++ QQuickScrollBarPrivate.

  It is built on the cute 'QQuickControlPrivate', as Qt's
  QQuickScrollBarPrivate is built on Qt's QQuickControlPrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickScrollBarPrivate that has a ritual and that
  Python can call so far, 17 names in all: 'q_func', 'get', 'visualArea',
  'logicalPosition', 'setPosition', 'snapPosition', 'positionAt',
  'setInteractive', 'updateActive', 'resizeContent',
  'itemImplicitWidthChanged', 'itemImplicitHeightChanged', 'handlePress',
  'handleMove', 'handleRelease', 'handleUngrab', 'visualAreaChange'. None can
  be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuickScrollBar *QQuickScrollBarPrivate::q_func() const':
    takes in Python what 'QQuickScrollBar *QQuickScrollBarPrivate::q_func()'
    takes.
  - Qt's 'void QQuickScrollBarPrivate::updateHover(const QPointF &pos,
    std::optional<bool> newHoverState)': takes a type Python has no way to
    hand over yet.

  What to expect
  --------------

  - The C++ QQuickScrollBarPrivate is created at the first use, not by
    'QQuickScrollBarPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickScrollBarPrivate.
  - Each name of Qt's QQuickScrollBarPrivate that has no cute function yet,
    'updateHover', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  #  The classes Qt writes inside QQuickScrollBarPrivate, each a class in
  #  here as in C++.

  class VisualArea(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQuickScrollBarPrivate::VisualArea: a plain Python
    object standing in front of one C++ QQuickScrollBarPrivate::VisualArea.

    C++ hands a QQuickScrollBarPrivate::VisualArea around as a copy, so every
    C++ QQuickScrollBarPrivate::VisualArea behind a cute one is Python's own:
    it is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    No function of Qt's QQuickScrollBarPrivate::VisualArea yet. It can be
    made from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQuickScrollBarPrivate::VisualArea::~VisualArea()': the
      destructor: Python removes its C++ QQuickScrollBarPrivate::VisualArea
      by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QQuickScrollBarPrivate::VisualArea is created at the first use,
      not by 'QQuickScrollBarPrivate::VisualArea(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQuickScrollBarPrivate::VisualArea back gives a
      copy the ritual made for Python, in a new cute
      QQuickScrollBarPrivate::VisualArea.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQuickScrollBarPrivate::VisualArea'

    #  Qt's '~QQuickScrollBarPrivate::VisualArea()'. Naming it makes this a
    #  value class: Python owns every C++ QQuickScrollBarPrivate::VisualArea
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN22QQuickScrollBarPrivate10VisualAreaD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload(float, float)
    def __init__(self, pos: float, sz: float) -> None:
      """
      Notes what was given, for Qt's
      'QQuickScrollBarPrivate::VisualArea::VisualArea(qreal pos, qreal sz)',
      which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qquickscrollbarprivate-visualarea.html

      Parameters
      ----------

      pos : float
        Passed on as it is.

      sz : float
        Passed on as it is.
      """
      #  QQuickScrollBarPrivate::VisualArea::VisualArea(qreal pos, qreal sz)
      self._noteCreation(
          QQuickScrollBarPrivate.VisualArea, lambda: Rituals.call(
              'ritual_ZN22QQuickScrollBarPrivate10VisualAreaC1Edd', pos, sz,
          ))

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QQuickScrollBar)
  @overload(NoneType)
  def get(
      bar: Optional[QQuickScrollBar],
  ) -> Optional[QQuickScrollBarPrivate]:
    """
    Calls Qt's 'QQuickScrollBarPrivate
    *QQuickScrollBarPrivate::get(QQuickScrollBar *bar)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickscrollbarprivate.html#get

    Parameters
    ----------

    bar : Optional[QQuickScrollBar]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickScrollBarPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickScrollBarPrivate *QQuickScrollBarPrivate::get(QQuickScrollBar
    #      *bar)
    address = Rituals.call(
        'ritual_ZN22QQuickScrollBarPrivate3getEP15QQuickScrollBar',
        CuteMixin._addressOf(bar),
    )
    return QQuickScrollBarPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickScrollBarPrivate'

  #  A C++ QQuickScrollBarPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickScrollBarPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def visualArea(self) -> VisualArea:
    """
    Calls Qt's 'VisualArea QQuickScrollBarPrivate::visualArea() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscrollbarprivate.html#visualArea

    Returns
    -------

    VisualArea
      A new cute QQuickScrollBarPrivate::VisualArea around the copy Qt gave
      back. Python owns it.
    """
    #  VisualArea QQuickScrollBarPrivate::visualArea() const
    address = self.uglySide.call(
        'ritual_ZNK22QQuickScrollBarPrivate10visualAreaEv',
    )
    return QQuickScrollBarPrivate.VisualArea._cuteOwning(address)

  @overload(float)
  def logicalPosition(self, position: float) -> float:
    """
    Calls Qt's 'qreal QQuickScrollBarPrivate::logicalPosition(qreal position)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscrollbarprivate.html#logicalPosition

    Parameters
    ----------

    position : float
      Passed on as it is.
    """
    #  qreal QQuickScrollBarPrivate::logicalPosition(qreal position) const
    return self.uglySide.call(
        'ritual_ZNK22QQuickScrollBarPrivate15logicalPositionEd', position,
    )

  @overload(float)
  def snapPosition(self, position: float) -> float:
    """
    Calls Qt's 'qreal QQuickScrollBarPrivate::snapPosition(qreal position)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscrollbarprivate.html#snapPosition

    Parameters
    ----------

    position : float
      Passed on as it is.
    """
    #  qreal QQuickScrollBarPrivate::snapPosition(qreal position) const
    return self.uglySide.call(
        'ritual_ZNK22QQuickScrollBarPrivate12snapPositionEd', position,
    )

  @overload(QPointF)
  def positionAt(self, point: QPointF) -> float:
    """
    Calls Qt's 'qreal QQuickScrollBarPrivate::positionAt(const QPointF
    &point) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscrollbarprivate.html#positionAt

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  qreal QQuickScrollBarPrivate::positionAt(const QPointF &point) const
    return self.uglySide.call(
        'ritual_ZNK22QQuickScrollBarPrivate10positionAtERK7QPointF',
        self._valueOf(point, 'QPointF'),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  @overload(float, bool)
  def setPosition(
      self,
      position: float,
      notifyVisualChange: bool = True,
  ) -> None:
    """
    Calls Qt's 'void QQuickScrollBarPrivate::setPosition(qreal position, bool
    notifyVisualChange)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscrollbarprivate.html#setPosition

    Parameters
    ----------

    position : float
      Passed on as it is.

    notifyVisualChange : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QQuickScrollBarPrivate::setPosition(qreal position, bool
    #      notifyVisualChange)
    self.uglySide.call(
        'ritual_ZN22QQuickScrollBarPrivate11setPositionEdb',
        position, notifyVisualChange,
    )

  @overload(bool)
  def setInteractive(self, interactive: bool) -> None:
    """
    Calls Qt's 'void QQuickScrollBarPrivate::setInteractive(bool
    interactive)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscrollbarprivate.html#setInteractive

    Parameters
    ----------

    interactive : bool
      Passed on as it is.
    """
    #  void QQuickScrollBarPrivate::setInteractive(bool interactive)
    self.uglySide.call(
        'ritual_ZN22QQuickScrollBarPrivate14setInteractiveEb', interactive,
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

  def q_func(self) -> Optional[QQuickScrollBar]:
    """
    Calls Qt's 'QQuickScrollBar *QQuickScrollBarPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickscrollbarprivate.html#q_func

    Returns
    -------

    Optional[QQuickScrollBar]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickScrollBar *QQuickScrollBarPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN22QQuickScrollBarPrivate6q_funcEv',
    )
    from . import QQuickScrollBar
    return QQuickScrollBar._cuteAt(address)

  def updateActive(self) -> None:
    """
    Calls Qt's 'void QQuickScrollBarPrivate::updateActive()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscrollbarprivate.html#updateActive
    """
    #  void QQuickScrollBarPrivate::updateActive()
    self.uglySide.call('ritual_ZN22QQuickScrollBarPrivate12updateActiveEv')

  def resizeContent(self) -> None:
    """
    Calls Qt's 'void QQuickScrollBarPrivate::resizeContent()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscrollbarprivate.html#resizeContent
    """
    #  void QQuickScrollBarPrivate::resizeContent()
    ritual = 'ritual_ZN22QQuickScrollBarPrivate13resizeContentEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QQuickScrollBarPrivate13resizeContentEv'
    self.uglySide.call(ritual)

  @overload(QQuickItem)
  @overload(NoneType)
  def itemImplicitWidthChanged(self, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void
    QQuickScrollBarPrivate::itemImplicitWidthChanged(QQuickItem *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscrollbarprivate.html

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickScrollBarPrivate::itemImplicitWidthChanged(QQuickItem
    #      *item)
    ritual = (
        'ritual_ZN22QQuickScrollBarPrivate24itemImplicitWidthChangedEP10QQu'
        'ickItem')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QQuickScrollBarPrivate24itemImplicitWidthChangedE'
          'P10QQuickItem')
    self.uglySide.call(ritual, self._addressOf(item))

  @overload(QQuickItem)
  @overload(NoneType)
  def itemImplicitHeightChanged(self, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void
    QQuickScrollBarPrivate::itemImplicitHeightChanged(QQuickItem *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscrollbarprivate.html

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickScrollBarPrivate::itemImplicitHeightChanged(QQuickItem
    #      *item)
    ritual = (
        'ritual_ZN22QQuickScrollBarPrivate25itemImplicitHeightChangedEP10QQ'
        'uickItem')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QQuickScrollBarPrivate25itemImplicitHeightChanged'
          'EP10QQuickItem')
    self.uglySide.call(ritual, self._addressOf(item))

  @overload(QPointF, int)
  def handlePress(self, point: QPointF, timestamp: int) -> bool:
    """
    Calls Qt's 'bool QQuickScrollBarPrivate::handlePress(const QPointF
    &point, ulong timestamp)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscrollbarprivate.html#handlePress

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    timestamp : int
      Passed on as it is.
    """
    #  bool QQuickScrollBarPrivate::handlePress(const QPointF &point, ulong
    #      timestamp)
    ritual = 'ritual_ZN22QQuickScrollBarPrivate11handlePressERK7QPointFm'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QQuickScrollBarPrivate11handlePressERK7QPointFm')
    return self.uglySide.call(
        ritual, self._valueOf(point, 'QPointF'), timestamp,
    )

  @overload(QPointF, int)
  def handleMove(self, point: QPointF, timestamp: int) -> bool:
    """
    Calls Qt's 'bool QQuickScrollBarPrivate::handleMove(const QPointF &point,
    ulong timestamp)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscrollbarprivate.html#handleMove

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    timestamp : int
      Passed on as it is.
    """
    #  bool QQuickScrollBarPrivate::handleMove(const QPointF &point, ulong
    #      timestamp)
    ritual = 'ritual_ZN22QQuickScrollBarPrivate10handleMoveERK7QPointFm'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QQuickScrollBarPrivate10handleMoveERK7QPointFm')
    return self.uglySide.call(
        ritual, self._valueOf(point, 'QPointF'), timestamp,
    )

  @overload(QPointF, int)
  def handleRelease(self, point: QPointF, timestamp: int) -> bool:
    """
    Calls Qt's 'bool QQuickScrollBarPrivate::handleRelease(const QPointF
    &point, ulong timestamp)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscrollbarprivate.html#handleRelease

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    timestamp : int
      Passed on as it is.
    """
    #  bool QQuickScrollBarPrivate::handleRelease(const QPointF &point, ulong
    #      timestamp)
    ritual = 'ritual_ZN22QQuickScrollBarPrivate13handleReleaseERK7QPointFm'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QQuickScrollBarPrivate13handleReleaseERK7QPointFm')
    return self.uglySide.call(
        ritual, self._valueOf(point, 'QPointF'), timestamp,
    )

  def handleUngrab(self) -> None:
    """
    Calls Qt's 'void QQuickScrollBarPrivate::handleUngrab()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscrollbarprivate.html#handleUngrab
    """
    #  void QQuickScrollBarPrivate::handleUngrab()
    ritual = 'ritual_ZN22QQuickScrollBarPrivate12handleUngrabEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QQuickScrollBarPrivate12handleUngrabEv'
    self.uglySide.call(ritual)

  @overload(VisualArea, VisualArea)
  def visualAreaChange(
      self,
      newVisualArea: VisualArea,
      oldVisualArea: VisualArea,
  ) -> None:
    """
    Calls Qt's 'void QQuickScrollBarPrivate::visualAreaChange(const
    VisualArea &newVisualArea, const VisualArea &oldVisualArea)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscrollbarprivate.html#visualAreaChange

    Parameters
    ----------

    newVisualArea : VisualArea
      Passed on as a value: Qt reads the C++
      QQuickScrollBarPrivate::VisualArea, which stays Python's own.

    oldVisualArea : VisualArea
      Passed on as a value: Qt reads the C++
      QQuickScrollBarPrivate::VisualArea, which stays Python's own.
    """
    #  void QQuickScrollBarPrivate::visualAreaChange(const VisualArea
    #      &newVisualArea, const VisualArea &oldVisualArea)
    self.uglySide.call(
        'ritual_ZN22QQuickScrollBarPrivate16visualAreaChangeERKNS_10VisualA'
        'reaES2_',
        self._valueOf(newVisualArea), self._valueOf(oldVisualArea),
    )

  @staticmethod
  def updateHover(*__, **_) -> Never:
    """
    Qt's 'void QQuickScrollBarPrivate::updateHover(const QPointF &pos,
    std::optional<bool> newHoverState)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QQuickScrollBarPrivate.updateHover' has no cute function yet. "
        "Qt's 'void QQuickScrollBarPrivate::updateHover(const QPointF &pos, "
        "std::optional<bool> newHoverState)': takes a type Python has no "
        "way to hand over yet.")
