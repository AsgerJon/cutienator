"""
QQuickIndicatorButton binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickindicatorbutton_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickIndicatorButton to be private: it declares the class in a
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
  from . import QQuickIndicatorButtonPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickItem = WAIT['QQuickItem']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickIndicatorButton(QObject):
  """
  The cute side of Qt's QQuickIndicatorButton: a plain Python object standing
  in front of one C++ QQuickIndicatorButton.

  It is built on the cute 'QObject', as Qt's QQuickIndicatorButton is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickIndicatorButton that has a ritual and that
  Python can call so far, 16 names in all: 'metaObject', 'tr', 'isPressed',
  'setPressed', 'indicator', 'setIndicator', 'isHovered', 'setHovered',
  'implicitIndicatorWidth', 'implicitIndicatorHeight', 'pressedChanged',
  'indicatorChanged', 'hoveredChanged', 'implicitIndicatorWidthChanged',
  'implicitIndicatorHeightChanged', 'd_func'. It can be made from Python, in
  1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickIndicatorButton::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickIndicatorButton::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickIndicatorButton::qt_qmlMarker_anonymous()': one of Qt's
    own inner workings.
  - Qt's 'QQuickIndicatorButton::~QQuickIndicatorButton()': the destructor:
    Python never removes a C++ QQuickIndicatorButton.
  - Qt's 'const QQuickIndicatorButtonPrivate *QQuickIndicatorButton::d_func()
    const': takes in Python what 'QQuickIndicatorButtonPrivate
    *QQuickIndicatorButton::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 26 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickIndicatorButton is created at the first use, not by
    'QQuickIndicatorButton(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickIndicatorButton.
  - Qt tells when it has removed the C++ QQuickIndicatorButton. Every call on
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
    Calls Qt's 'QString QQuickIndicatorButton::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickindicatorbutton.html#tr

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
    #  QString QQuickIndicatorButton::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN21QQuickIndicatorButton2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickIndicatorButton'

  #  A C++ QQuickIndicatorButton Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickIndicatorButton'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickIndicatorButton::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickindicatorbutton.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickIndicatorButton::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK21QQuickIndicatorButton10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isPressed(self) -> bool:
    """
    Calls Qt's 'bool QQuickIndicatorButton::isPressed() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickindicatorbutton.html#isPressed
    """
    #  bool QQuickIndicatorButton::isPressed() const
    return self.uglySide.call(
        'ritual_ZNK21QQuickIndicatorButton9isPressedEv',
    )

  def indicator(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickIndicatorButton::indicator() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickindicatorbutton.html#indicator

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickIndicatorButton::indicator() const
    address = self.uglySide.call(
        'ritual_ZNK21QQuickIndicatorButton9indicatorEv',
    )
    from ..QtQuick import QQuickItem
    return QQuickItem._cuteAt(address)

  def isHovered(self) -> bool:
    """
    Calls Qt's 'bool QQuickIndicatorButton::isHovered() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickindicatorbutton.html#isHovered
    """
    #  bool QQuickIndicatorButton::isHovered() const
    return self.uglySide.call(
        'ritual_ZNK21QQuickIndicatorButton9isHoveredEv',
    )

  def implicitIndicatorWidth(self) -> float:
    """
    Calls Qt's 'qreal QQuickIndicatorButton::implicitIndicatorWidth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickindicatorbutton.html#implicitIndicatorWidth
    """
    #  qreal QQuickIndicatorButton::implicitIndicatorWidth() const
    return self.uglySide.call(
        'ritual_ZNK21QQuickIndicatorButton22implicitIndicatorWidthEv',
    )

  def implicitIndicatorHeight(self) -> float:
    """
    Calls Qt's 'qreal QQuickIndicatorButton::implicitIndicatorHeight()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickindicatorbutton.html#implicitIndicatorHeight
    """
    #  qreal QQuickIndicatorButton::implicitIndicatorHeight() const
    return self.uglySide.call(
        'ritual_ZNK21QQuickIndicatorButton23implicitIndicatorHeightEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setPressed(self, pressed: bool) -> None:
    """
    Calls Qt's 'void QQuickIndicatorButton::setPressed(bool pressed)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickindicatorbutton.html#setPressed

    Parameters
    ----------

    pressed : bool
      Passed on as it is.
    """
    #  void QQuickIndicatorButton::setPressed(bool pressed)
    self.uglySide.call(
        'ritual_ZN21QQuickIndicatorButton10setPressedEb', pressed,
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def setIndicator(self, indicator: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickIndicatorButton::setIndicator(QQuickItem
    *indicator)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickindicatorbutton.html#setIndicator

    Parameters
    ----------

    indicator : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickIndicatorButton::setIndicator(QQuickItem *indicator)
    self.uglySide.call(
        'ritual_ZN21QQuickIndicatorButton12setIndicatorEP10QQuickItem',
        self._addressOf(indicator),
    )

  @overload(bool)
  def setHovered(self, hovered: bool) -> None:
    """
    Calls Qt's 'void QQuickIndicatorButton::setHovered(bool hovered)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickindicatorbutton.html#setHovered

    Parameters
    ----------

    hovered : bool
      Passed on as it is.
    """
    #  void QQuickIndicatorButton::setHovered(bool hovered)
    self.uglySide.call(
        'ritual_ZN21QQuickIndicatorButton10setHoveredEb', hovered,
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

  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject]) -> None:
    """
    Notes what was given, for Qt's
    'QQuickIndicatorButton::QQuickIndicatorButton(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickindicatorbutton.html#QQuickIndicatorButton

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQuickIndicatorButton::QQuickIndicatorButton(QObject *parent)
    self._noteCreation(QQuickIndicatorButton, lambda: Rituals.call(
        'ritual_ZN21QQuickIndicatorButtonC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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

  def pressedChanged(self) -> None:
    """
    Calls Qt's 'void QQuickIndicatorButton::pressedChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickindicatorbutton.html#pressedChanged
    """
    #  void QQuickIndicatorButton::pressedChanged()
    self.uglySide.call('ritual_ZN21QQuickIndicatorButton14pressedChangedEv')

  def indicatorChanged(self) -> None:
    """
    Calls Qt's 'void QQuickIndicatorButton::indicatorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickindicatorbutton.html#indicatorChanged
    """
    #  void QQuickIndicatorButton::indicatorChanged()
    self.uglySide.call(
        'ritual_ZN21QQuickIndicatorButton16indicatorChangedEv',
    )

  def hoveredChanged(self) -> None:
    """
    Calls Qt's 'void QQuickIndicatorButton::hoveredChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickindicatorbutton.html#hoveredChanged
    """
    #  void QQuickIndicatorButton::hoveredChanged()
    self.uglySide.call('ritual_ZN21QQuickIndicatorButton14hoveredChangedEv')

  def implicitIndicatorWidthChanged(self) -> None:
    """
    Calls Qt's 'void QQuickIndicatorButton::implicitIndicatorWidthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickindicatorbutton.html
    """
    #  void QQuickIndicatorButton::implicitIndicatorWidthChanged()
    self.uglySide.call(
        'ritual_ZN21QQuickIndicatorButton29implicitIndicatorWidthChangedEv',
    )

  def implicitIndicatorHeightChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuickIndicatorButton::implicitIndicatorHeightChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickindicatorbutton.html
    """
    #  void QQuickIndicatorButton::implicitIndicatorHeightChanged()
    self.uglySide.call(
        'ritual_ZN21QQuickIndicatorButton30implicitIndicatorHeightChangedEv',
    )

  def d_func(self) -> Optional[QQuickIndicatorButtonPrivate]:
    """
    Calls Qt's 'QQuickIndicatorButtonPrivate
    *QQuickIndicatorButton::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickindicatorbutton.html#d_func

    Returns
    -------

    Optional[QQuickIndicatorButtonPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickIndicatorButtonPrivate *QQuickIndicatorButton::d_func()
    address = self.uglySide.call('ritual_ZN21QQuickIndicatorButton6d_funcEv')
    from . import QQuickIndicatorButtonPrivate
    return QQuickIndicatorButtonPrivate._cuteAt(address)
