"""
QQuickRangeSliderNode binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickrangeslider_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickRangeSliderNode to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtQuick import QQuickItem
  from . import QQuickRangeSlider
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickItem = WAIT['QQuickItem']
  QQuickRangeSlider = WAIT['QQuickRangeSlider']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickRangeSliderNode(QObject):
  """
  The cute side of Qt's QQuickRangeSliderNode: a plain Python object standing
  in front of one C++ QQuickRangeSliderNode.

  It is built on the cute 'QObject', as Qt's QQuickRangeSliderNode is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickRangeSliderNode that has a ritual and that
  Python can call so far, 26 names in all: 'metaObject', 'tr', 'value',
  'setValue', 'position', 'visualPosition', 'handle', 'setHandle',
  'isPressed', 'setPressed', 'isHovered', 'setHovered',
  'implicitHandleWidth', 'implicitHandleHeight', 'increase', 'decrease',
  'valueChanged', 'positionChanged', 'visualPositionChanged',
  'handleChanged', 'pressedChanged', 'hoveredChanged', 'moved',
  'implicitHandleWidthChanged', 'implicitHandleHeightChanged',
  'updateHandleCrossing'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickRangeSliderNode::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickRangeSliderNode::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickRangeSliderNode::qt_qmlMarker_anonymous()': one of Qt's
    own inner workings.
  - Qt's 'QQuickRangeSliderNode::~QQuickRangeSliderNode()': the destructor:
    Python never removes a C++ QQuickRangeSliderNode.
  - Qt's 'QQuickRangeSliderNodePrivate *QQuickRangeSliderNode::d_func()':
    gives 'QQuickRangeSliderNodePrivate', which has no cute class yet.
  - Qt's 'const QQuickRangeSliderNodePrivate *QQuickRangeSliderNode::d_func()
    const': gives 'QQuickRangeSliderNodePrivate', which has no cute class
    yet.

  What has no ritual
  ------------------

  4 of the 37 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickRangeSliderNode is created at the first use, not by
    'QQuickRangeSliderNode(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickRangeSliderNode.
  - Qt tells when it has removed the C++ QQuickRangeSliderNode. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString QQuickRangeSliderNode::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrangeslidernode.html#tr

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
    #  QString QQuickRangeSliderNode::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN21QQuickRangeSliderNode2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickRangeSliderNode'

  #  A C++ QQuickRangeSliderNode Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickRangeSliderNode'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickRangeSliderNode::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrangeslidernode.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickRangeSliderNode::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK21QQuickRangeSliderNode10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def value(self) -> float:
    """
    Calls Qt's 'qreal QQuickRangeSliderNode::value() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrangeslidernode.html#value
    """
    #  qreal QQuickRangeSliderNode::value() const
    return self.uglySide.call('ritual_ZNK21QQuickRangeSliderNode5valueEv')

  def position(self) -> float:
    """
    Calls Qt's 'qreal QQuickRangeSliderNode::position() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrangeslidernode.html#position
    """
    #  qreal QQuickRangeSliderNode::position() const
    return self.uglySide.call('ritual_ZNK21QQuickRangeSliderNode8positionEv')

  def visualPosition(self) -> float:
    """
    Calls Qt's 'qreal QQuickRangeSliderNode::visualPosition() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrangeslidernode.html#visualPosition
    """
    #  qreal QQuickRangeSliderNode::visualPosition() const
    return self.uglySide.call(
        'ritual_ZNK21QQuickRangeSliderNode14visualPositionEv',
    )

  def handle(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickRangeSliderNode::handle() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrangeslidernode.html#handle

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickRangeSliderNode::handle() const
    address = self.uglySide.call(
        'ritual_ZNK21QQuickRangeSliderNode6handleEv',
    )
    from ..QtQuick import QQuickItem
    return QQuickItem._cuteAt(address)

  def isPressed(self) -> bool:
    """
    Calls Qt's 'bool QQuickRangeSliderNode::isPressed() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrangeslidernode.html#isPressed
    """
    #  bool QQuickRangeSliderNode::isPressed() const
    return self.uglySide.call(
        'ritual_ZNK21QQuickRangeSliderNode9isPressedEv',
    )

  def isHovered(self) -> bool:
    """
    Calls Qt's 'bool QQuickRangeSliderNode::isHovered() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrangeslidernode.html#isHovered
    """
    #  bool QQuickRangeSliderNode::isHovered() const
    return self.uglySide.call(
        'ritual_ZNK21QQuickRangeSliderNode9isHoveredEv',
    )

  def implicitHandleWidth(self) -> float:
    """
    Calls Qt's 'qreal QQuickRangeSliderNode::implicitHandleWidth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrangeslidernode.html#implicitHandleWidth
    """
    #  qreal QQuickRangeSliderNode::implicitHandleWidth() const
    return self.uglySide.call(
        'ritual_ZNK21QQuickRangeSliderNode19implicitHandleWidthEv',
    )

  def implicitHandleHeight(self) -> float:
    """
    Calls Qt's 'qreal QQuickRangeSliderNode::implicitHandleHeight() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrangeslidernode.html#implicitHandleHeight
    """
    #  qreal QQuickRangeSliderNode::implicitHandleHeight() const
    return self.uglySide.call(
        'ritual_ZNK21QQuickRangeSliderNode20implicitHandleHeightEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setValue(self, value: float) -> None:
    """
    Calls Qt's 'void QQuickRangeSliderNode::setValue(qreal value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrangeslidernode.html#setValue

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void QQuickRangeSliderNode::setValue(qreal value)
    self.uglySide.call('ritual_ZN21QQuickRangeSliderNode8setValueEd', value)

  @overload(QQuickItem)
  @overload(NoneType)
  def setHandle(self, handle: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickRangeSliderNode::setHandle(QQuickItem *handle)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrangeslidernode.html#setHandle

    Parameters
    ----------

    handle : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickRangeSliderNode::setHandle(QQuickItem *handle)
    self.uglySide.call(
        'ritual_ZN21QQuickRangeSliderNode9setHandleEP10QQuickItem',
        self._addressOf(handle),
    )

  @overload(bool)
  def setPressed(self, pressed: bool) -> None:
    """
    Calls Qt's 'void QQuickRangeSliderNode::setPressed(bool pressed)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrangeslidernode.html#setPressed

    Parameters
    ----------

    pressed : bool
      Passed on as it is.
    """
    #  void QQuickRangeSliderNode::setPressed(bool pressed)
    self.uglySide.call(
        'ritual_ZN21QQuickRangeSliderNode10setPressedEb', pressed,
    )

  @overload(bool)
  def setHovered(self, hovered: bool) -> None:
    """
    Calls Qt's 'void QQuickRangeSliderNode::setHovered(bool hovered)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrangeslidernode.html#setHovered

    Parameters
    ----------

    hovered : bool
      Passed on as it is.
    """
    #  void QQuickRangeSliderNode::setHovered(bool hovered)
    self.uglySide.call(
        'ritual_ZN21QQuickRangeSliderNode10setHoveredEb', hovered,
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

  @overload(float, QQuickRangeSlider)
  @overload(float, NoneType)
  def __init__(
      self,
      value: float,
      slider: Optional[QQuickRangeSlider],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQuickRangeSliderNode::QQuickRangeSliderNode(qreal value,
    QQuickRangeSlider *slider)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrangeslidernode.html#QQuickRangeSliderNode

    Parameters
    ----------

    value : float
      Passed on as it is.

    slider : Optional[QQuickRangeSlider]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQuickRangeSliderNode::QQuickRangeSliderNode(qreal value,
    #      QQuickRangeSlider *slider)
    self._noteCreation(QQuickRangeSliderNode, lambda: Rituals.call(
        'ritual_ZN21QQuickRangeSliderNodeC1EdP17QQuickRangeSlider',
        value, self._addressOf(slider),
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

  def increase(self) -> None:
    """
    Calls Qt's 'void QQuickRangeSliderNode::increase()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrangeslidernode.html#increase
    """
    #  void QQuickRangeSliderNode::increase()
    self.uglySide.call('ritual_ZN21QQuickRangeSliderNode8increaseEv')

  def decrease(self) -> None:
    """
    Calls Qt's 'void QQuickRangeSliderNode::decrease()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrangeslidernode.html#decrease
    """
    #  void QQuickRangeSliderNode::decrease()
    self.uglySide.call('ritual_ZN21QQuickRangeSliderNode8decreaseEv')

  def valueChanged(self) -> None:
    """
    Calls Qt's 'void QQuickRangeSliderNode::valueChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrangeslidernode.html#valueChanged
    """
    #  void QQuickRangeSliderNode::valueChanged()
    self.uglySide.call('ritual_ZN21QQuickRangeSliderNode12valueChangedEv')

  def positionChanged(self) -> None:
    """
    Calls Qt's 'void QQuickRangeSliderNode::positionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrangeslidernode.html#positionChanged
    """
    #  void QQuickRangeSliderNode::positionChanged()
    self.uglySide.call('ritual_ZN21QQuickRangeSliderNode15positionChangedEv')

  def visualPositionChanged(self) -> None:
    """
    Calls Qt's 'void QQuickRangeSliderNode::visualPositionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrangeslidernode.html#visualPositionChanged
    """
    #  void QQuickRangeSliderNode::visualPositionChanged()
    self.uglySide.call(
        'ritual_ZN21QQuickRangeSliderNode21visualPositionChangedEv',
    )

  def handleChanged(self) -> None:
    """
    Calls Qt's 'void QQuickRangeSliderNode::handleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrangeslidernode.html#handleChanged
    """
    #  void QQuickRangeSliderNode::handleChanged()
    self.uglySide.call('ritual_ZN21QQuickRangeSliderNode13handleChangedEv')

  def pressedChanged(self) -> None:
    """
    Calls Qt's 'void QQuickRangeSliderNode::pressedChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrangeslidernode.html#pressedChanged
    """
    #  void QQuickRangeSliderNode::pressedChanged()
    self.uglySide.call('ritual_ZN21QQuickRangeSliderNode14pressedChangedEv')

  def hoveredChanged(self) -> None:
    """
    Calls Qt's 'void QQuickRangeSliderNode::hoveredChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrangeslidernode.html#hoveredChanged
    """
    #  void QQuickRangeSliderNode::hoveredChanged()
    self.uglySide.call('ritual_ZN21QQuickRangeSliderNode14hoveredChangedEv')

  def moved(self) -> None:
    """
    Calls Qt's 'void QQuickRangeSliderNode::moved()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrangeslidernode.html#moved
    """
    #  void QQuickRangeSliderNode::moved()
    self.uglySide.call('ritual_ZN21QQuickRangeSliderNode5movedEv')

  def implicitHandleWidthChanged(self) -> None:
    """
    Calls Qt's 'void QQuickRangeSliderNode::implicitHandleWidthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrangeslidernode.html
    """
    #  void QQuickRangeSliderNode::implicitHandleWidthChanged()
    self.uglySide.call(
        'ritual_ZN21QQuickRangeSliderNode26implicitHandleWidthChangedEv',
    )

  def implicitHandleHeightChanged(self) -> None:
    """
    Calls Qt's 'void QQuickRangeSliderNode::implicitHandleHeightChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrangeslidernode.html
    """
    #  void QQuickRangeSliderNode::implicitHandleHeightChanged()
    self.uglySide.call(
        'ritual_ZN21QQuickRangeSliderNode27implicitHandleHeightChangedEv',
    )

  def updateHandleCrossing(self) -> None:
    """
    Calls Qt's 'void QQuickRangeSliderNode::updateHandleCrossing()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrangeslidernode.html#updateHandleCrossing
    """
    #  void QQuickRangeSliderNode::updateHandleCrossing()
    self.uglySide.call(
        'ritual_ZN21QQuickRangeSliderNode20updateHandleCrossingEv',
    )
