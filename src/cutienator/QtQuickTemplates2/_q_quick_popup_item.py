"""
QQuickPopupItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickpopupitem_p_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickPopupItem to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtGui import QAccessible
from ..QtQuick import QQuickItem
from . import QQuickPage

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QLocale, QMarginsF, QMetaObject, QRectF
  from ..QtCore import QSizeF
  from ..QtGui import QDragEnterEvent, QDragLeaveEvent, QDragMoveEvent
  from ..QtGui import QDropEvent, QFocusEvent, QFont, QKeyEvent, QMouseEvent
  from ..QtGui import QTouchEvent, QWheelEvent
  from . import QQuickPopup, QQuickPopupItemPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDragEnterEvent = WAIT['QDragEnterEvent']
  QDragLeaveEvent = WAIT['QDragLeaveEvent']
  QDragMoveEvent = WAIT['QDragMoveEvent']
  QDropEvent = WAIT['QDropEvent']
  QEvent = WAIT['QEvent']
  QFocusEvent = WAIT['QFocusEvent']
  QFont = WAIT['QFont']
  QKeyEvent = WAIT['QKeyEvent']
  QLocale = WAIT['QLocale']
  QMarginsF = WAIT['QMarginsF']
  QMouseEvent = WAIT['QMouseEvent']
  QQuickPopup = WAIT['QQuickPopup']
  QRectF = WAIT['QRectF']
  QSizeF = WAIT['QSizeF']
  QTouchEvent = WAIT['QTouchEvent']
  QWheelEvent = WAIT['QWheelEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickPopupItem(QQuickPage):
  """
  The cute side of Qt's QQuickPopupItem: a plain Python object standing in
  front of one C++ QQuickPopupItem.

  It is built on the cute 'QQuickPage', as Qt's QQuickPopupItem is built on
  Qt's QQuickPage, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickPopupItem that has a ritual and that Python
  can call so far, 35 names in all: 'metaObject', 'tr', 'updatePolish',
  'childMouseEventFilter', 'focusInEvent', 'focusOutEvent', 'keyPressEvent',
  'keyReleaseEvent', 'mousePressEvent', 'mouseMoveEvent',
  'mouseReleaseEvent', 'mouseDoubleClickEvent', 'mouseUngrabEvent',
  'touchEvent', 'touchUngrabEvent', 'wheelEvent', 'dragEnterEvent',
  'dragMoveEvent', 'dragLeaveEvent', 'dropEvent', 'contentItemChange',
  'contentSizeChange', 'fontChange', 'geometryChange', 'localeChange',
  'mirrorChange', 'itemChange', 'paddingChange', 'insetChange',
  'spacingChange', 'enabledChange', 'defaultFont', 'accessibleRole',
  'accessibilityActiveChanged', 'd_func'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickPopupItem::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickPopupItem::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'const QQuickPopupItemPrivate *QQuickPopupItem::d_func() const':
    takes in Python what 'QQuickPopupItemPrivate *QQuickPopupItem::d_func()'
    takes.

  What has no ritual
  ------------------

  4 of the 43 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickPopupItem is created at the first use, not by
    'QQuickPopupItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickPopupItem.
  - Qt tells when it has removed the C++ QQuickPopupItem. Every call on the
    cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QQuickPopupItem::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopupitem.html#tr

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
    #  QString QQuickPopupItem::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN15QQuickPopupItem2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickPopupItem'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickPopupItem::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopupitem.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickPopupItem::metaObject() const
    address = self.uglySide.call('ritual_ZNK15QQuickPopupItem10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def defaultFont(self) -> QFont:
    """
    Calls Qt's 'QFont QQuickPopupItem::defaultFont() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopupitem.html#defaultFont

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QQuickPopupItem::defaultFont() const
    ritual = 'ritual_ZNK15QQuickPopupItem11defaultFontEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QQuickPopupItem11defaultFontEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  def accessibleRole(self) -> QAccessible.Role:
    """
    Calls Qt's 'QAccessible::Role QQuickPopupItem::accessibleRole() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopupitem.html#accessibleRole

    Returns
    -------

    QAccessible.Role
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QAccessible.Role(number)'
      gives.
    """
    #  QAccessible::Role QQuickPopupItem::accessibleRole() const
    ritual = 'ritual_ZNK15QQuickPopupItem14accessibleRoleEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QQuickPopupItem14accessibleRoleEv'
    return QAccessible.Role(self.uglySide.call(ritual))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuickPopup)
  @overload(NoneType)
  def __init__(self, popup: Optional[QQuickPopup]) -> None:
    """
    Notes what was given, for Qt's
    'QQuickPopupItem::QQuickPopupItem(QQuickPopup *popup)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopupitem.html#QQuickPopupItem

    Parameters
    ----------

    popup : Optional[QQuickPopup]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQuickPopupItem::QQuickPopupItem(QQuickPopup *popup)
    self._noteCreation(QQuickPopupItem, lambda: Rituals.call(
        'ritual_ZN15QQuickPopupItemC1EP11QQuickPopup',
        self._addressOf(popup),
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

  def updatePolish(self) -> None:
    """
    Calls Qt's 'void QQuickPopupItem::updatePolish()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopupitem.html#updatePolish
    """
    #  void QQuickPopupItem::updatePolish()
    ritual = 'ritual_ZN15QQuickPopupItem12updatePolishEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQuickPopupItem12updatePolishEv'
    self.uglySide.call(ritual)

  @overload(QQuickItem, QEvent)
  @overload(QQuickItem, NoneType)
  @overload(NoneType, QEvent)
  @overload(NoneType, NoneType)
  def childMouseEventFilter(
      self,
      child: Optional[QQuickItem],
      event: Optional[QEvent],
  ) -> bool:
    """
    Calls Qt's 'bool QQuickPopupItem::childMouseEventFilter(QQuickItem
    *child, QEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopupitem.html#childMouseEventFilter

    Parameters
    ----------

    child : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickPopupItem::childMouseEventFilter(QQuickItem *child, QEvent
    #      *event)
    ritual = (
        'ritual_ZN15QQuickPopupItem21childMouseEventFilterEP10QQuickItemP6Q'
        'Event')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QQuickPopupItem21childMouseEventFilterEP10QQuickI'
          'temP6QEvent')
    return self.uglySide.call(
        ritual, self._addressOf(child), self._addressOf(event),
    )

  @overload(QFocusEvent)
  @overload(NoneType)
  def focusInEvent(self, event: Optional[QFocusEvent]) -> None:
    """
    Calls Qt's 'void QQuickPopupItem::focusInEvent(QFocusEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopupitem.html#focusInEvent

    Parameters
    ----------

    event : Optional[QFocusEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPopupItem::focusInEvent(QFocusEvent *event)
    ritual = 'ritual_ZN15QQuickPopupItem12focusInEventEP11QFocusEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQuickPopupItem12focusInEventEP11QFocusEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QFocusEvent)
  @overload(NoneType)
  def focusOutEvent(self, event: Optional[QFocusEvent]) -> None:
    """
    Calls Qt's 'void QQuickPopupItem::focusOutEvent(QFocusEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopupitem.html#focusOutEvent

    Parameters
    ----------

    event : Optional[QFocusEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPopupItem::focusOutEvent(QFocusEvent *event)
    ritual = 'ritual_ZN15QQuickPopupItem13focusOutEventEP11QFocusEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQuickPopupItem13focusOutEventEP11QFocusEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QKeyEvent)
  @overload(NoneType)
  def keyPressEvent(self, event: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void QQuickPopupItem::keyPressEvent(QKeyEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopupitem.html#keyPressEvent

    Parameters
    ----------

    event : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPopupItem::keyPressEvent(QKeyEvent *event)
    ritual = 'ritual_ZN15QQuickPopupItem13keyPressEventEP9QKeyEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQuickPopupItem13keyPressEventEP9QKeyEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QKeyEvent)
  @overload(NoneType)
  def keyReleaseEvent(self, event: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void QQuickPopupItem::keyReleaseEvent(QKeyEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopupitem.html#keyReleaseEvent

    Parameters
    ----------

    event : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPopupItem::keyReleaseEvent(QKeyEvent *event)
    ritual = 'ritual_ZN15QQuickPopupItem15keyReleaseEventEP9QKeyEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQuickPopupItem15keyReleaseEventEP9QKeyEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mousePressEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QQuickPopupItem::mousePressEvent(QMouseEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopupitem.html#mousePressEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPopupItem::mousePressEvent(QMouseEvent *event)
    ritual = 'ritual_ZN15QQuickPopupItem15mousePressEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QQuickPopupItem15mousePressEventEP11QMouseEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseMoveEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QQuickPopupItem::mouseMoveEvent(QMouseEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopupitem.html#mouseMoveEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPopupItem::mouseMoveEvent(QMouseEvent *event)
    ritual = 'ritual_ZN15QQuickPopupItem14mouseMoveEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QQuickPopupItem14mouseMoveEventEP11QMouseEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseReleaseEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QQuickPopupItem::mouseReleaseEvent(QMouseEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopupitem.html#mouseReleaseEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPopupItem::mouseReleaseEvent(QMouseEvent *event)
    ritual = 'ritual_ZN15QQuickPopupItem17mouseReleaseEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QQuickPopupItem17mouseReleaseEventEP11QMouseEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseDoubleClickEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QQuickPopupItem::mouseDoubleClickEvent(QMouseEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopupitem.html#mouseDoubleClickEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPopupItem::mouseDoubleClickEvent(QMouseEvent *event)
    ritual = (
        'ritual_ZN15QQuickPopupItem21mouseDoubleClickEventEP11QMouseEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QQuickPopupItem21mouseDoubleClickEventEP11QMouseE'
          'vent')
    self.uglySide.call(ritual, self._addressOf(event))

  def mouseUngrabEvent(self) -> None:
    """
    Calls Qt's 'void QQuickPopupItem::mouseUngrabEvent()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopupitem.html#mouseUngrabEvent
    """
    #  void QQuickPopupItem::mouseUngrabEvent()
    ritual = 'ritual_ZN15QQuickPopupItem16mouseUngrabEventEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQuickPopupItem16mouseUngrabEventEv'
    self.uglySide.call(ritual)

  @overload(QTouchEvent)
  @overload(NoneType)
  def touchEvent(self, event: Optional[QTouchEvent]) -> None:
    """
    Calls Qt's 'void QQuickPopupItem::touchEvent(QTouchEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopupitem.html#touchEvent

    Parameters
    ----------

    event : Optional[QTouchEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPopupItem::touchEvent(QTouchEvent *event)
    ritual = 'ritual_ZN15QQuickPopupItem10touchEventEP11QTouchEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQuickPopupItem10touchEventEP11QTouchEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  def touchUngrabEvent(self) -> None:
    """
    Calls Qt's 'void QQuickPopupItem::touchUngrabEvent()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopupitem.html#touchUngrabEvent
    """
    #  void QQuickPopupItem::touchUngrabEvent()
    ritual = 'ritual_ZN15QQuickPopupItem16touchUngrabEventEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQuickPopupItem16touchUngrabEventEv'
    self.uglySide.call(ritual)

  @overload(QWheelEvent)
  @overload(NoneType)
  def wheelEvent(self, event: Optional[QWheelEvent]) -> None:
    """
    Calls Qt's 'void QQuickPopupItem::wheelEvent(QWheelEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopupitem.html#wheelEvent

    Parameters
    ----------

    event : Optional[QWheelEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPopupItem::wheelEvent(QWheelEvent *event)
    ritual = 'ritual_ZN15QQuickPopupItem10wheelEventEP11QWheelEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQuickPopupItem10wheelEventEP11QWheelEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QDragEnterEvent)
  @overload(NoneType)
  def dragEnterEvent(self, event: Optional[QDragEnterEvent]) -> None:
    """
    Calls Qt's 'void QQuickPopupItem::dragEnterEvent(QDragEnterEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopupitem.html#dragEnterEvent

    Parameters
    ----------

    event : Optional[QDragEnterEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPopupItem::dragEnterEvent(QDragEnterEvent *event)
    ritual = 'ritual_ZN15QQuickPopupItem14dragEnterEventEP15QDragEnterEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QQuickPopupItem14dragEnterEventEP15QDragEnterEven'
          't')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QDragMoveEvent)
  @overload(NoneType)
  def dragMoveEvent(self, event: Optional[QDragMoveEvent]) -> None:
    """
    Calls Qt's 'void QQuickPopupItem::dragMoveEvent(QDragMoveEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopupitem.html#dragMoveEvent

    Parameters
    ----------

    event : Optional[QDragMoveEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPopupItem::dragMoveEvent(QDragMoveEvent *event)
    ritual = 'ritual_ZN15QQuickPopupItem13dragMoveEventEP14QDragMoveEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QQuickPopupItem13dragMoveEventEP14QDragMoveEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QDragLeaveEvent)
  @overload(NoneType)
  def dragLeaveEvent(self, event: Optional[QDragLeaveEvent]) -> None:
    """
    Calls Qt's 'void QQuickPopupItem::dragLeaveEvent(QDragLeaveEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopupitem.html#dragLeaveEvent

    Parameters
    ----------

    event : Optional[QDragLeaveEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPopupItem::dragLeaveEvent(QDragLeaveEvent *event)
    ritual = 'ritual_ZN15QQuickPopupItem14dragLeaveEventEP15QDragLeaveEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QQuickPopupItem14dragLeaveEventEP15QDragLeaveEven'
          't')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QDropEvent)
  @overload(NoneType)
  def dropEvent(self, event: Optional[QDropEvent]) -> None:
    """
    Calls Qt's 'void QQuickPopupItem::dropEvent(QDropEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopupitem.html#dropEvent

    Parameters
    ----------

    event : Optional[QDropEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPopupItem::dropEvent(QDropEvent *event)
    ritual = 'ritual_ZN15QQuickPopupItem9dropEventEP10QDropEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQuickPopupItem9dropEventEP10QDropEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QQuickItem, QQuickItem)
  @overload(QQuickItem, NoneType)
  @overload(NoneType, QQuickItem)
  @overload(NoneType, NoneType)
  def contentItemChange(
      self,
      newItem: Optional[QQuickItem],
      oldItem: Optional[QQuickItem],
  ) -> None:
    """
    Calls Qt's 'void QQuickPopupItem::contentItemChange(QQuickItem *newItem,
    QQuickItem *oldItem)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopupitem.html#contentItemChange

    Parameters
    ----------

    newItem : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    oldItem : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPopupItem::contentItemChange(QQuickItem *newItem,
    #      QQuickItem *oldItem)
    ritual = 'ritual_ZN15QQuickPopupItem17contentItemChangeEP10QQuickItemS1_'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QQuickPopupItem17contentItemChangeEP10QQuickItemS'
          '1_')
    self.uglySide.call(
        ritual, self._addressOf(newItem), self._addressOf(oldItem),
    )

  @overload(QSizeF, QSizeF)
  def contentSizeChange(self, newSize: QSizeF, oldSize: QSizeF) -> None:
    """
    Calls Qt's 'void QQuickPopupItem::contentSizeChange(const QSizeF
    &newSize, const QSizeF &oldSize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopupitem.html#contentSizeChange

    Parameters
    ----------

    newSize : QSizeF
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own.

    oldSize : QSizeF
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own.
    """
    #  void QQuickPopupItem::contentSizeChange(const QSizeF &newSize, const
    #      QSizeF &oldSize)
    ritual = 'ritual_ZN15QQuickPopupItem17contentSizeChangeERK6QSizeFS2_'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QQuickPopupItem17contentSizeChangeERK6QSizeFS2_')
    self.uglySide.call(
        ritual, self._valueOf(newSize), self._valueOf(oldSize),
    )

  @overload(QFont, QFont)
  def fontChange(self, newFont: QFont, oldFont: QFont) -> None:
    """
    Calls Qt's 'void QQuickPopupItem::fontChange(const QFont &newFont, const
    QFont &oldFont)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopupitem.html#fontChange

    Parameters
    ----------

    newFont : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.

    oldFont : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QQuickPopupItem::fontChange(const QFont &newFont, const QFont
    #      &oldFont)
    ritual = 'ritual_ZN15QQuickPopupItem10fontChangeERK5QFontS2_'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQuickPopupItem10fontChangeERK5QFontS2_'
    self.uglySide.call(
        ritual, self._valueOf(newFont), self._valueOf(oldFont),
    )

  @overload(QRectF, QRectF)
  def geometryChange(self, newGeometry: QRectF, oldGeometry: QRectF) -> None:
    """
    Calls Qt's 'void QQuickPopupItem::geometryChange(const QRectF
    &newGeometry, const QRectF &oldGeometry)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopupitem.html#geometryChange

    Parameters
    ----------

    newGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    oldGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QQuickPopupItem::geometryChange(const QRectF &newGeometry, const
    #      QRectF &oldGeometry)
    ritual = 'ritual_ZN15QQuickPopupItem14geometryChangeERK6QRectFS2_'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQuickPopupItem14geometryChangeERK6QRectFS2_'
    self.uglySide.call(
        ritual, self._valueOf(newGeometry), self._valueOf(oldGeometry),
    )

  @overload(QLocale, QLocale)
  def localeChange(self, newLocale: QLocale, oldLocale: QLocale) -> None:
    """
    Calls Qt's 'void QQuickPopupItem::localeChange(const QLocale &newLocale,
    const QLocale &oldLocale)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopupitem.html#localeChange

    Parameters
    ----------

    newLocale : QLocale
      Passed on as a value: Qt reads the C++ QLocale, which stays Python's
      own.

    oldLocale : QLocale
      Passed on as a value: Qt reads the C++ QLocale, which stays Python's
      own.
    """
    #  void QQuickPopupItem::localeChange(const QLocale &newLocale, const
    #      QLocale &oldLocale)
    ritual = 'ritual_ZN15QQuickPopupItem12localeChangeERK7QLocaleS2_'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQuickPopupItem12localeChangeERK7QLocaleS2_'
    self.uglySide.call(
        ritual, self._valueOf(newLocale), self._valueOf(oldLocale),
    )

  def mirrorChange(self) -> None:
    """
    Calls Qt's 'void QQuickPopupItem::mirrorChange()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopupitem.html#mirrorChange
    """
    #  void QQuickPopupItem::mirrorChange()
    ritual = 'ritual_ZN15QQuickPopupItem12mirrorChangeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQuickPopupItem12mirrorChangeEv'
    self.uglySide.call(ritual)

  @overload(QQuickItem.ItemChange, QQuickItem.ItemChangeData)
  def itemChange(
      self,
      change: QQuickItem.ItemChange,
      data: QQuickItem.ItemChangeData,
  ) -> None:
    """
    Calls Qt's 'void QQuickPopupItem::itemChange(ItemChange change, const
    ItemChangeData &data)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopupitem.html#itemChange

    Parameters
    ----------

    change : QQuickItem.ItemChange
      Passed on as its number.

    data : QQuickItem.ItemChangeData
      Passed on as a value: Qt reads the C++ QQuickItem::ItemChangeData,
      which stays Python's own.
    """
    #  void QQuickPopupItem::itemChange(ItemChange change, const
    #      ItemChangeData &data)
    ritual = (
        'ritual_ZN15QQuickPopupItem10itemChangeEN10QQuickItem10ItemChangeER'
        'KNS0_14ItemChangeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QQuickPopupItem10itemChangeEN10QQuickItem10ItemCh'
          'angeERKNS0_14ItemChangeDataE')
    self.uglySide.call(ritual, change.value, self._valueOf(data))

  @overload(QMarginsF, QMarginsF)
  def paddingChange(
      self,
      newPadding: QMarginsF,
      oldPadding: QMarginsF,
  ) -> None:
    """
    Calls Qt's 'void QQuickPopupItem::paddingChange(const QMarginsF
    &newPadding, const QMarginsF &oldPadding)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopupitem.html#paddingChange

    Parameters
    ----------

    newPadding : QMarginsF
      Passed on as a value: Qt reads the C++ QMarginsF, which stays Python's
      own.

    oldPadding : QMarginsF
      Passed on as a value: Qt reads the C++ QMarginsF, which stays Python's
      own.
    """
    #  void QQuickPopupItem::paddingChange(const QMarginsF &newPadding, const
    #      QMarginsF &oldPadding)
    ritual = 'ritual_ZN15QQuickPopupItem13paddingChangeERK9QMarginsFS2_'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QQuickPopupItem13paddingChangeERK9QMarginsFS2_')
    self.uglySide.call(
        ritual, self._valueOf(newPadding), self._valueOf(oldPadding),
    )

  @overload(QMarginsF, QMarginsF)
  def insetChange(self, newInset: QMarginsF, oldInset: QMarginsF) -> None:
    """
    Calls Qt's 'void QQuickPopupItem::insetChange(const QMarginsF &newInset,
    const QMarginsF &oldInset)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopupitem.html#insetChange

    Parameters
    ----------

    newInset : QMarginsF
      Passed on as a value: Qt reads the C++ QMarginsF, which stays Python's
      own.

    oldInset : QMarginsF
      Passed on as a value: Qt reads the C++ QMarginsF, which stays Python's
      own.
    """
    #  void QQuickPopupItem::insetChange(const QMarginsF &newInset, const
    #      QMarginsF &oldInset)
    ritual = 'ritual_ZN15QQuickPopupItem11insetChangeERK9QMarginsFS2_'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQuickPopupItem11insetChangeERK9QMarginsFS2_'
    self.uglySide.call(
        ritual, self._valueOf(newInset), self._valueOf(oldInset),
    )

  @overload(float, float)
  def spacingChange(self, newSpacing: float, oldSpacing: float) -> None:
    """
    Calls Qt's 'void QQuickPopupItem::spacingChange(qreal newSpacing, qreal
    oldSpacing)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopupitem.html#spacingChange

    Parameters
    ----------

    newSpacing : float
      Passed on as it is.

    oldSpacing : float
      Passed on as it is.
    """
    #  void QQuickPopupItem::spacingChange(qreal newSpacing, qreal
    #      oldSpacing)
    ritual = 'ritual_ZN15QQuickPopupItem13spacingChangeEdd'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQuickPopupItem13spacingChangeEdd'
    self.uglySide.call(ritual, newSpacing, oldSpacing)

  def enabledChange(self) -> None:
    """
    Calls Qt's 'void QQuickPopupItem::enabledChange()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopupitem.html#enabledChange
    """
    #  void QQuickPopupItem::enabledChange()
    ritual = 'ritual_ZN15QQuickPopupItem13enabledChangeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQuickPopupItem13enabledChangeEv'
    self.uglySide.call(ritual)

  @overload(bool)
  def accessibilityActiveChanged(self, active: bool) -> None:
    """
    Calls Qt's 'void QQuickPopupItem::accessibilityActiveChanged(bool
    active)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopupitem.html#accessibilityActiveChanged

    Parameters
    ----------

    active : bool
      Passed on as it is.
    """
    #  void QQuickPopupItem::accessibilityActiveChanged(bool active)
    ritual = 'ritual_ZN15QQuickPopupItem26accessibilityActiveChangedEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQuickPopupItem26accessibilityActiveChangedEb'
    self.uglySide.call(ritual, active)

  def d_func(self) -> Optional[QQuickPopupItemPrivate]:
    """
    Calls Qt's 'QQuickPopupItemPrivate *QQuickPopupItem::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopupitem.html#d_func

    Returns
    -------

    Optional[QQuickPopupItemPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickPopupItemPrivate *QQuickPopupItem::d_func()
    address = self.uglySide.call('ritual_ZN15QQuickPopupItem6d_funcEv')
    from . import QQuickPopupItemPrivate
    return QQuickPopupItemPrivate._cuteAt(address)
