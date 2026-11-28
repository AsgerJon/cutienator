"""
QQuickToolTip binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquicktooltip_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuickToolTip to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from ..QtGui import QAccessible
from ..QtQuick import QQuickItem
from . import QQuickPopup

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QTimerEvent
  from ..QtGui import QFont
  from . import QQuickToolTipAttached
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QTimerEvent = WAIT['QTimerEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickToolTip(QQuickPopup):
  """
  The cute side of Qt's QQuickToolTip: a plain Python object standing in
  front of one C++ QQuickToolTip.

  It is built on the cute 'QQuickPopup', as Qt's QQuickToolTip is built on
  Qt's QQuickPopup, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickToolTip that has a ritual and that Python can
  call so far, 20 names in all: 'metaObject', 'tr', 'text', 'setText',
  'delay', 'setDelay', 'timeout', 'setTimeout', 'setVisible',
  'qmlAttachedProperties', 'textChanged', 'delayChanged', 'timeoutChanged',
  'show', 'hide', 'defaultFont', 'itemChange', 'timerEvent',
  'accessibleRole', 'accessibilityActiveChanged'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickToolTip::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQuickToolTip::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickToolTip::qt_qmlMarker_attached()': one of Qt's own inner
    workings.
  - Qt's 'QQuickToolTipPrivate *QQuickToolTip::d_func()': gives
    'QQuickToolTipPrivate', which has no cute class yet.
  - Qt's 'const QQuickToolTipPrivate *QQuickToolTip::d_func() const': gives
    'QQuickToolTipPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 30 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickToolTip is created at the first use, not by
    'QQuickToolTip(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickToolTip.
  - Qt tells when it has removed the C++ QQuickToolTip. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QQuickToolTip, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Policy(CuteNum):
    """
    The enum 'QQuickToolTip::Policy' of Qt, with the 2 names Qt gives in it.
    """

    Automatic = Kee[int](0)
    Manual = Kee[int](1)

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
    Calls Qt's 'QString QQuickToolTip::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktooltip.html#tr

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
    #  QString QQuickToolTip::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN13QQuickToolTip2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  def qmlAttachedProperties(
      object: Optional[QObject],
  ) -> Optional[QQuickToolTipAttached]:
    """
    Calls Qt's 'QQuickToolTipAttached
    *QQuickToolTip::qmlAttachedProperties(QObject *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktooltip.html#qmlAttachedProperties

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickToolTipAttached]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickToolTipAttached *QQuickToolTip::qmlAttachedProperties(QObject
    #      *object)
    address = Rituals.call(
        'ritual_ZN13QQuickToolTip21qmlAttachedPropertiesEP7QObject',
        CuteMixin._addressOf(object, 'QObject'),
    )
    from . import QQuickToolTipAttached
    return QQuickToolTipAttached._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickToolTip'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickToolTip::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktooltip.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickToolTip::metaObject() const
    address = self.uglySide.call('ritual_ZNK13QQuickToolTip10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def text(self) -> str:
    """
    Calls Qt's 'QString QQuickToolTip::text() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktooltip.html#text

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickToolTip::text() const
    return self.uglySide.call('ritual_ZNK13QQuickToolTip4textEv')

  def delay(self) -> int:
    """
    Calls Qt's 'int QQuickToolTip::delay() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktooltip.html#delay
    """
    #  int QQuickToolTip::delay() const
    return self.uglySide.call('ritual_ZNK13QQuickToolTip5delayEv')

  def timeout(self) -> int:
    """
    Calls Qt's 'int QQuickToolTip::timeout() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktooltip.html#timeout
    """
    #  int QQuickToolTip::timeout() const
    return self.uglySide.call('ritual_ZNK13QQuickToolTip7timeoutEv')

  def defaultFont(self) -> QFont:
    """
    Calls Qt's 'QFont QQuickToolTip::defaultFont() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktooltip.html#defaultFont

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QQuickToolTip::defaultFont() const
    ritual = 'ritual_ZNK13QQuickToolTip11defaultFontEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13QQuickToolTip11defaultFontEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  def accessibleRole(self) -> QAccessible.Role:
    """
    Calls Qt's 'QAccessible::Role QQuickToolTip::accessibleRole() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktooltip.html#accessibleRole

    Returns
    -------

    QAccessible.Role
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QAccessible.Role(number)'
      gives.
    """
    #  QAccessible::Role QQuickToolTip::accessibleRole() const
    ritual = 'ritual_ZNK13QQuickToolTip14accessibleRoleEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13QQuickToolTip14accessibleRoleEv'
    return QAccessible.Role(self.uglySide.call(ritual))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setText(self, text: str) -> None:
    """
    Calls Qt's 'void QQuickToolTip::setText(const QString &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktooltip.html#setText

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickToolTip::setText(const QString &text)
    self.uglySide.call('ritual_ZN13QQuickToolTip7setTextERK7QString', text)

  @overload(int)
  def setDelay(self, delay: int) -> None:
    """
    Calls Qt's 'void QQuickToolTip::setDelay(int delay)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktooltip.html#setDelay

    Parameters
    ----------

    delay : int
      Passed on as it is.
    """
    #  void QQuickToolTip::setDelay(int delay)
    self.uglySide.call('ritual_ZN13QQuickToolTip8setDelayEi', delay)

  @overload(int)
  def setTimeout(self, timeout: int) -> None:
    """
    Calls Qt's 'void QQuickToolTip::setTimeout(int timeout)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktooltip.html#setTimeout

    Parameters
    ----------

    timeout : int
      Passed on as it is.
    """
    #  void QQuickToolTip::setTimeout(int timeout)
    self.uglySide.call('ritual_ZN13QQuickToolTip10setTimeoutEi', timeout)

  @overload(bool)
  def setVisible(self, visible: bool) -> None:
    """
    Calls Qt's 'void QQuickToolTip::setVisible(bool visible)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktooltip.html#setVisible

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void QQuickToolTip::setVisible(bool visible)
    ritual = 'ritual_ZN13QQuickToolTip10setVisibleEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QQuickToolTip10setVisibleEb'
    self.uglySide.call(ritual, visible)

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
    Notes what was given, for Qt's 'QQuickToolTip::QQuickToolTip(QQuickItem
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qquicktooltip.html#QQuickToolTip

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickToolTip::QQuickToolTip(QQuickItem *parent)
    self._noteCreation(QQuickToolTip, lambda: Rituals.call(
        'ritual_ZN13QQuickToolTipC1EP10QQuickItem', self._addressOf(parent),
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

  def textChanged(self) -> None:
    """
    Calls Qt's 'void QQuickToolTip::textChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktooltip.html#textChanged
    """
    #  void QQuickToolTip::textChanged()
    self.uglySide.call('ritual_ZN13QQuickToolTip11textChangedEv')

  def delayChanged(self) -> None:
    """
    Calls Qt's 'void QQuickToolTip::delayChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktooltip.html#delayChanged
    """
    #  void QQuickToolTip::delayChanged()
    self.uglySide.call('ritual_ZN13QQuickToolTip12delayChangedEv')

  def timeoutChanged(self) -> None:
    """
    Calls Qt's 'void QQuickToolTip::timeoutChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktooltip.html#timeoutChanged
    """
    #  void QQuickToolTip::timeoutChanged()
    self.uglySide.call('ritual_ZN13QQuickToolTip14timeoutChangedEv')

  @overload(str)
  @overload(str, int)
  def show(self, text: str, ms: int = -1) -> None:
    """
    Calls Qt's 'void QQuickToolTip::show(const QString &text, int ms)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktooltip.html#show

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.

    ms : int
      Passed on as it is. May be left out, as in Qt: it is then -1.
    """
    #  void QQuickToolTip::show(const QString &text, int ms)
    self.uglySide.call('ritual_ZN13QQuickToolTip4showERK7QStringi', text, ms)

  def hide(self) -> None:
    """
    Calls Qt's 'void QQuickToolTip::hide()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktooltip.html#hide
    """
    #  void QQuickToolTip::hide()
    self.uglySide.call('ritual_ZN13QQuickToolTip4hideEv')

  @overload(QQuickItem.ItemChange, QQuickItem.ItemChangeData)
  def itemChange(
      self,
      change: QQuickItem.ItemChange,
      data: QQuickItem.ItemChangeData,
  ) -> None:
    """
    Calls Qt's 'void QQuickToolTip::itemChange(QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData &data)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktooltip.html#itemChange

    Parameters
    ----------

    change : QQuickItem.ItemChange
      Passed on as its number.

    data : QQuickItem.ItemChangeData
      Passed on as a value: Qt reads the C++ QQuickItem::ItemChangeData,
      which stays Python's own.
    """
    #  void QQuickToolTip::itemChange(QQuickItem::ItemChange change, const
    #      QQuickItem::ItemChangeData &data)
    ritual = (
        'ritual_ZN13QQuickToolTip10itemChangeEN10QQuickItem10ItemChangeERKN'
        'S0_14ItemChangeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN13QQuickToolTip10itemChangeEN10QQuickItem10ItemChan'
          'geERKNS0_14ItemChangeDataE')
    self.uglySide.call(ritual, change.value, self._valueOf(data))

  @overload(QTimerEvent)
  @overload(NoneType)
  def timerEvent(self, event: Optional[QTimerEvent]) -> None:
    """
    Calls Qt's 'void QQuickToolTip::timerEvent(QTimerEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktooltip.html#timerEvent

    Parameters
    ----------

    event : Optional[QTimerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickToolTip::timerEvent(QTimerEvent *event)
    ritual = 'ritual_ZN13QQuickToolTip10timerEventEP11QTimerEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QQuickToolTip10timerEventEP11QTimerEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(bool)
  def accessibilityActiveChanged(self, active: bool) -> None:
    """
    Calls Qt's 'void QQuickToolTip::accessibilityActiveChanged(bool active)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktooltip.html#accessibilityActiveChanged

    Parameters
    ----------

    active : bool
      Passed on as it is.
    """
    #  void QQuickToolTip::accessibilityActiveChanged(bool active)
    ritual = 'ritual_ZN13QQuickToolTip26accessibilityActiveChangedEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QQuickToolTip26accessibilityActiveChangedEb'
    self.uglySide.call(ritual, active)
