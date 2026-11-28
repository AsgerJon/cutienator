"""
QQuickSwipeDelegate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickswipedelegate_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickSwipeDelegate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from ..QtGui import QAccessible
from ..QtQuick import QQuickItem
from . import QQuickItemDelegate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject, QRectF
  from ..QtGui import QFont, QMouseEvent, QTouchEvent
  from . import QQuickSwipe, QQuickSwipeDelegateAttached
  from . import QQuickSwipeDelegatePrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QMouseEvent = WAIT['QMouseEvent']
  QRectF = WAIT['QRectF']
  QTouchEvent = WAIT['QTouchEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickSwipeDelegate(QQuickItemDelegate):
  """
  The cute side of Qt's QQuickSwipeDelegate: a plain Python object standing
  in front of one C++ QQuickSwipeDelegate.

  It is built on the cute 'QQuickItemDelegate', as Qt's QQuickSwipeDelegate
  is built on Qt's QQuickItemDelegate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickSwipeDelegate that has a ritual and that
  Python can call so far, 15 names in all: 'metaObject', 'tr', 'swipe',
  'qmlAttachedProperties', 'childMouseEventFilter', 'mousePressEvent',
  'mouseMoveEvent', 'mouseReleaseEvent', 'mouseUngrabEvent', 'touchEvent',
  'componentComplete', 'geometryChange', 'defaultFont', 'accessibleRole',
  'd_func'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickSwipeDelegate::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickSwipeDelegate::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickSwipeDelegate::qt_qmlMarker_attached()': one of Qt's own
    inner workings.
  - Qt's 'const QQuickSwipeDelegatePrivate *QQuickSwipeDelegate::d_func()
    const': takes in Python what 'QQuickSwipeDelegatePrivate
    *QQuickSwipeDelegate::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 24 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickSwipeDelegate is created at the first use, not by
    'QQuickSwipeDelegate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickSwipeDelegate.
  - Qt tells when it has removed the C++ QQuickSwipeDelegate. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QQuickSwipeDelegate, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class Side(CuteNum):
    """
    The enum 'QQuickSwipeDelegate::Side' of Qt, with the 2 names Qt gives in
    it.
    """

    Left = Kee[int](1)
    Right = Kee[int](-1)

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
    Calls Qt's 'QString QQuickSwipeDelegate::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickswipedelegate.html#tr

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
    #  QString QQuickSwipeDelegate::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN19QQuickSwipeDelegate2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  def qmlAttachedProperties(
      object: Optional[QObject],
  ) -> Optional[QQuickSwipeDelegateAttached]:
    """
    Calls Qt's 'QQuickSwipeDelegateAttached
    *QQuickSwipeDelegate::qmlAttachedProperties(QObject *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickswipedelegate.html#qmlAttachedProperties

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickSwipeDelegateAttached]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickSwipeDelegateAttached
    #      *QQuickSwipeDelegate::qmlAttachedProperties(QObject *object)
    address = Rituals.call(
        'ritual_ZN19QQuickSwipeDelegate21qmlAttachedPropertiesEP7QObject',
        CuteMixin._addressOf(object, 'QObject'),
    )
    from . import QQuickSwipeDelegateAttached
    return QQuickSwipeDelegateAttached._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickSwipeDelegate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickSwipeDelegate::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickswipedelegate.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickSwipeDelegate::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickSwipeDelegate10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def swipe(self) -> Optional[QQuickSwipe]:
    """
    Calls Qt's 'QQuickSwipe *QQuickSwipeDelegate::swipe() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickswipedelegate.html#swipe

    Returns
    -------

    Optional[QQuickSwipe]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickSwipe *QQuickSwipeDelegate::swipe() const
    address = self.uglySide.call('ritual_ZNK19QQuickSwipeDelegate5swipeEv')
    from . import QQuickSwipe
    return QQuickSwipe._cuteAt(address)

  def defaultFont(self) -> QFont:
    """
    Calls Qt's 'QFont QQuickSwipeDelegate::defaultFont() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickswipedelegate.html#defaultFont

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QQuickSwipeDelegate::defaultFont() const
    ritual = 'ritual_ZNK19QQuickSwipeDelegate11defaultFontEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QQuickSwipeDelegate11defaultFontEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  def accessibleRole(self) -> QAccessible.Role:
    """
    Calls Qt's 'QAccessible::Role QQuickSwipeDelegate::accessibleRole()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickswipedelegate.html#accessibleRole

    Returns
    -------

    QAccessible.Role
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QAccessible.Role(number)'
      gives.
    """
    #  QAccessible::Role QQuickSwipeDelegate::accessibleRole() const
    ritual = 'ritual_ZNK19QQuickSwipeDelegate14accessibleRoleEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QQuickSwipeDelegate14accessibleRoleEv'
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

  @overload()
  @overload(QQuickItem)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuickItem] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuickSwipeDelegate::QQuickSwipeDelegate(QQuickItem *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickswipedelegate.html#QQuickSwipeDelegate

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickSwipeDelegate::QQuickSwipeDelegate(QQuickItem *parent)
    self._noteCreation(QQuickSwipeDelegate, lambda: Rituals.call(
        'ritual_ZN19QQuickSwipeDelegateC1EP10QQuickItem',
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
    Calls Qt's 'bool QQuickSwipeDelegate::childMouseEventFilter(QQuickItem
    *child, QEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickswipedelegate.html#childMouseEventFilter

    Parameters
    ----------

    child : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickSwipeDelegate::childMouseEventFilter(QQuickItem *child,
    #      QEvent *event)
    ritual = (
        'ritual_ZN19QQuickSwipeDelegate21childMouseEventFilterEP10QQuickIte'
        'mP6QEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQuickSwipeDelegate21childMouseEventFilterEP10QQu'
          'ickItemP6QEvent')
    return self.uglySide.call(
        ritual, self._addressOf(child), self._addressOf(event),
    )

  @overload(QMouseEvent)
  @overload(NoneType)
  def mousePressEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QQuickSwipeDelegate::mousePressEvent(QMouseEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickswipedelegate.html#mousePressEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickSwipeDelegate::mousePressEvent(QMouseEvent *event)
    ritual = 'ritual_ZN19QQuickSwipeDelegate15mousePressEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQuickSwipeDelegate15mousePressEventEP11QMouseEve'
          'nt')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseMoveEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QQuickSwipeDelegate::mouseMoveEvent(QMouseEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickswipedelegate.html#mouseMoveEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickSwipeDelegate::mouseMoveEvent(QMouseEvent *event)
    ritual = 'ritual_ZN19QQuickSwipeDelegate14mouseMoveEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQuickSwipeDelegate14mouseMoveEventEP11QMouseEven'
          't')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseReleaseEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QQuickSwipeDelegate::mouseReleaseEvent(QMouseEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickswipedelegate.html#mouseReleaseEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickSwipeDelegate::mouseReleaseEvent(QMouseEvent *event)
    ritual = (
        'ritual_ZN19QQuickSwipeDelegate17mouseReleaseEventEP11QMouseEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQuickSwipeDelegate17mouseReleaseEventEP11QMouseE'
          'vent')
    self.uglySide.call(ritual, self._addressOf(event))

  def mouseUngrabEvent(self) -> None:
    """
    Calls Qt's 'void QQuickSwipeDelegate::mouseUngrabEvent()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickswipedelegate.html#mouseUngrabEvent
    """
    #  void QQuickSwipeDelegate::mouseUngrabEvent()
    ritual = 'ritual_ZN19QQuickSwipeDelegate16mouseUngrabEventEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQuickSwipeDelegate16mouseUngrabEventEv'
    self.uglySide.call(ritual)

  @overload(QTouchEvent)
  @overload(NoneType)
  def touchEvent(self, event: Optional[QTouchEvent]) -> None:
    """
    Calls Qt's 'void QQuickSwipeDelegate::touchEvent(QTouchEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickswipedelegate.html#touchEvent

    Parameters
    ----------

    event : Optional[QTouchEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickSwipeDelegate::touchEvent(QTouchEvent *event)
    ritual = 'ritual_ZN19QQuickSwipeDelegate10touchEventEP11QTouchEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQuickSwipeDelegate10touchEventEP11QTouchEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickSwipeDelegate::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickswipedelegate.html#componentComplete
    """
    #  void QQuickSwipeDelegate::componentComplete()
    ritual = 'ritual_ZN19QQuickSwipeDelegate17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQuickSwipeDelegate17componentCompleteEv'
    self.uglySide.call(ritual)

  @overload(QRectF, QRectF)
  def geometryChange(self, newGeometry: QRectF, oldGeometry: QRectF) -> None:
    """
    Calls Qt's 'void QQuickSwipeDelegate::geometryChange(const QRectF
    &newGeometry, const QRectF &oldGeometry)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickswipedelegate.html#geometryChange

    Parameters
    ----------

    newGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    oldGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QQuickSwipeDelegate::geometryChange(const QRectF &newGeometry,
    #      const QRectF &oldGeometry)
    ritual = 'ritual_ZN19QQuickSwipeDelegate14geometryChangeERK6QRectFS2_'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQuickSwipeDelegate14geometryChangeERK6QRectFS2_')
    self.uglySide.call(
        ritual, self._valueOf(newGeometry), self._valueOf(oldGeometry),
    )

  def d_func(self) -> Optional[QQuickSwipeDelegatePrivate]:
    """
    Calls Qt's 'QQuickSwipeDelegatePrivate *QQuickSwipeDelegate::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickswipedelegate.html#d_func

    Returns
    -------

    Optional[QQuickSwipeDelegatePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickSwipeDelegatePrivate *QQuickSwipeDelegate::d_func()
    address = self.uglySide.call('ritual_ZN19QQuickSwipeDelegate6d_funcEv')
    from . import QQuickSwipeDelegatePrivate
    return QQuickSwipeDelegatePrivate._cuteAt(address)
