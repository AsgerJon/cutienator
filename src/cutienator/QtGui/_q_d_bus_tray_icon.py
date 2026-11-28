"""
QDBusTrayIcon binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qdbustrayicon_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QDBusTrayIcon to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QPlatformSystemTrayIcon

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QRect, QTemporaryFile
  from . import QDBusPlatformMenu, QIcon, QPlatformMenu
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QIcon = WAIT['QIcon']
  QPlatformMenu = WAIT['QPlatformMenu']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDBusTrayIcon(QPlatformSystemTrayIcon):
  """
  The cute side of Qt's QDBusTrayIcon: a plain Python object standing in
  front of one C++ QDBusTrayIcon.

  It is built on the cute 'QPlatformSystemTrayIcon', as Qt's QDBusTrayIcon is
  built on Qt's QPlatformSystemTrayIcon, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QDBusTrayIcon that has a ritual and that Python can
  call so far, 34 names in all: 'metaObject', 'init', 'cleanup',
  'updateIcon', 'updateToolTip', 'updateMenu', 'createMenu', 'showMessage',
  'isSystemTrayAvailable', 'supportsMessages', 'geometry', 'category',
  'status', 'tooltip', 'iconName', 'icon', 'isRequestingAttention',
  'attentionTitle', 'attentionMessage', 'attentionIconName', 'attentionIcon',
  'instanceId', 'menu', 'categoryChanged', 'statusChanged', 'tooltipChanged',
  'iconChanged', 'attention', 'menuChanged', 'attentionTimerExpired',
  'actionInvoked', 'notificationClosed', 'watcherServiceRegistered',
  'tempIcon'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QDBusTrayIcon::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QDBusTrayIcon::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QDBusTrayIcon::~QDBusTrayIcon()': the destructor: Python never
    removes a C++ QDBusTrayIcon.

  What has no ritual
  ------------------

  6 of the 43 functions Qt declares: 2 not a gap; 2 leans on 'QDBusTrayIcon;
  1 Qt's library has no name for it, and its code in Qt's source does not
  compile apart from its file; 1 leans on 'QDBusMenuConnection.

  What to expect
  --------------

  - The C++ QDBusTrayIcon is created at the first use, not by
    'QDBusTrayIcon(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDBusTrayIcon.
  - Qt tells when it has removed the C++ QDBusTrayIcon. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QDBusTrayIcon that has no cute function yet,
    '__init__', 'dBusConnection', 'setStatus', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDBusTrayIcon'

  #  A C++ QDBusTrayIcon Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDBusTrayIcon'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QDBusTrayIcon::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdbustrayicon.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QDBusTrayIcon::metaObject() const
    address = self.uglySide.call('ritual_ZNK13QDBusTrayIcon10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def createMenu(self) -> Optional[QPlatformMenu]:
    """
    Calls Qt's 'QPlatformMenu *QDBusTrayIcon::createMenu() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdbustrayicon.html#createMenu

    Returns
    -------

    Optional[QPlatformMenu]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformMenu *QDBusTrayIcon::createMenu() const
    address = self.uglySide.call('ritual_ZNK13QDBusTrayIcon10createMenuEv')
    from . import QPlatformMenu
    return QPlatformMenu._cuteAt(address)

  def isSystemTrayAvailable(self) -> bool:
    """
    Calls Qt's 'bool QDBusTrayIcon::isSystemTrayAvailable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbustrayicon.html#isSystemTrayAvailable
    """
    #  bool QDBusTrayIcon::isSystemTrayAvailable() const
    return self.uglySide.call(
        'ritual_ZNK13QDBusTrayIcon21isSystemTrayAvailableEv',
    )

  def supportsMessages(self) -> bool:
    """
    Calls Qt's 'bool QDBusTrayIcon::supportsMessages() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbustrayicon.html#supportsMessages
    """
    #  bool QDBusTrayIcon::supportsMessages() const
    ritual = 'ritual_ZNK13QDBusTrayIcon16supportsMessagesEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13QDBusTrayIcon16supportsMessagesEv'
    return self.uglySide.call(ritual)

  def geometry(self) -> QRect:
    """
    Calls Qt's 'QRect QDBusTrayIcon::geometry() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdbustrayicon.html#geometry

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QDBusTrayIcon::geometry() const
    ritual = 'ritual_ZNK13QDBusTrayIcon8geometryEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13QDBusTrayIcon8geometryEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def category(self) -> str:
    """
    Calls Qt's 'QString QDBusTrayIcon::category() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdbustrayicon.html#category

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDBusTrayIcon::category() const
    return self.uglySide.call('ritual_ZNK13QDBusTrayIcon8categoryEv')

  def status(self) -> str:
    """
    Calls Qt's 'QString QDBusTrayIcon::status() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdbustrayicon.html#status

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDBusTrayIcon::status() const
    return self.uglySide.call('ritual_ZNK13QDBusTrayIcon6statusEv')

  def tooltip(self) -> str:
    """
    Calls Qt's 'QString QDBusTrayIcon::tooltip() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdbustrayicon.html#tooltip

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDBusTrayIcon::tooltip() const
    return self.uglySide.call('ritual_ZNK13QDBusTrayIcon7tooltipEv')

  def iconName(self) -> str:
    """
    Calls Qt's 'QString QDBusTrayIcon::iconName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdbustrayicon.html#iconName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDBusTrayIcon::iconName() const
    return self.uglySide.call('ritual_ZNK13QDBusTrayIcon8iconNameEv')

  def icon(self) -> QIcon:
    """
    Calls Qt's 'const QIcon &QDBusTrayIcon::icon() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdbustrayicon.html#icon

    Returns
    -------

    QIcon
      A new cute QIcon around the copy Qt gave back. Python owns it.
    """
    #  const QIcon &QDBusTrayIcon::icon() const
    address = self.uglySide.call('ritual_ZNK13QDBusTrayIcon4iconEv')
    from . import QIcon
    return QIcon._cuteOwning(address)

  def isRequestingAttention(self) -> bool:
    """
    Calls Qt's 'bool QDBusTrayIcon::isRequestingAttention() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbustrayicon.html#isRequestingAttention
    """
    #  bool QDBusTrayIcon::isRequestingAttention() const
    return self.uglySide.call(
        'ritual_ZNK13QDBusTrayIcon21isRequestingAttentionEv',
    )

  def attentionTitle(self) -> str:
    """
    Calls Qt's 'QString QDBusTrayIcon::attentionTitle() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdbustrayicon.html#attentionTitle

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDBusTrayIcon::attentionTitle() const
    return self.uglySide.call('ritual_ZNK13QDBusTrayIcon14attentionTitleEv')

  def attentionMessage(self) -> str:
    """
    Calls Qt's 'QString QDBusTrayIcon::attentionMessage() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbustrayicon.html#attentionMessage

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDBusTrayIcon::attentionMessage() const
    return self.uglySide.call(
        'ritual_ZNK13QDBusTrayIcon16attentionMessageEv',
    )

  def attentionIconName(self) -> str:
    """
    Calls Qt's 'QString QDBusTrayIcon::attentionIconName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbustrayicon.html#attentionIconName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDBusTrayIcon::attentionIconName() const
    return self.uglySide.call(
        'ritual_ZNK13QDBusTrayIcon17attentionIconNameEv',
    )

  def attentionIcon(self) -> QIcon:
    """
    Calls Qt's 'const QIcon &QDBusTrayIcon::attentionIcon() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdbustrayicon.html#attentionIcon

    Returns
    -------

    QIcon
      A new cute QIcon around the copy Qt gave back. Python owns it.
    """
    #  const QIcon &QDBusTrayIcon::attentionIcon() const
    address = self.uglySide.call(
        'ritual_ZNK13QDBusTrayIcon13attentionIconEv',
    )
    from . import QIcon
    return QIcon._cuteOwning(address)

  def instanceId(self) -> str:
    """
    Calls Qt's 'QString QDBusTrayIcon::instanceId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdbustrayicon.html#instanceId

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDBusTrayIcon::instanceId() const
    return self.uglySide.call('ritual_ZNK13QDBusTrayIcon10instanceIdEv')

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QDBusTrayIcon::QDBusTrayIcon()': Qt's library has no name for it,
    and its code in Qt's source does not compile apart from its file: use of
    undeclared identifier 'instanceCount'.
    """
    raise NotImplementedError(
        "'QDBusTrayIcon.__init__' has no cute function yet. Qt's "
        "'QDBusTrayIcon::QDBusTrayIcon()': Qt's library has no name for it, "
        "and its code in Qt's source does not compile apart from its file: "
        "use of undeclared identifier 'instanceCount'.")

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

  def init(self) -> None:
    """
    Calls Qt's 'void QDBusTrayIcon::init()'.

    Qt's own words: https://doc.qt.io/qt-6/qdbustrayicon.html#init
    """
    #  void QDBusTrayIcon::init()
    self.uglySide.call('ritual_ZN13QDBusTrayIcon4initEv')

  def cleanup(self) -> None:
    """
    Calls Qt's 'void QDBusTrayIcon::cleanup()'.

    Qt's own words: https://doc.qt.io/qt-6/qdbustrayicon.html#cleanup
    """
    #  void QDBusTrayIcon::cleanup()
    self.uglySide.call('ritual_ZN13QDBusTrayIcon7cleanupEv')

  @overload(QIcon)
  def updateIcon(self, icon: QIcon) -> None:
    """
    Calls Qt's 'void QDBusTrayIcon::updateIcon(const QIcon &icon)'.

    Qt's own words: https://doc.qt.io/qt-6/qdbustrayicon.html#updateIcon

    Parameters
    ----------

    icon : QIcon
      Passed on as a value: Qt reads the C++ QIcon, which stays Python's own.
    """
    #  void QDBusTrayIcon::updateIcon(const QIcon &icon)
    self.uglySide.call(
        'ritual_ZN13QDBusTrayIcon10updateIconERK5QIcon', self._valueOf(icon),
    )

  @overload(str)
  def updateToolTip(self, tooltip: str) -> None:
    """
    Calls Qt's 'void QDBusTrayIcon::updateToolTip(const QString &tooltip)'.

    Qt's own words: https://doc.qt.io/qt-6/qdbustrayicon.html#updateToolTip

    Parameters
    ----------

    tooltip : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDBusTrayIcon::updateToolTip(const QString &tooltip)
    self.uglySide.call(
        'ritual_ZN13QDBusTrayIcon13updateToolTipERK7QString', tooltip,
    )

  @overload(QPlatformMenu)
  @overload(NoneType)
  def updateMenu(self, menu: Optional[QPlatformMenu]) -> None:
    """
    Calls Qt's 'void QDBusTrayIcon::updateMenu(QPlatformMenu *menu)'.

    Qt's own words: https://doc.qt.io/qt-6/qdbustrayicon.html#updateMenu

    Parameters
    ----------

    menu : Optional[QPlatformMenu]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDBusTrayIcon::updateMenu(QPlatformMenu *menu)
    self.uglySide.call(
        'ritual_ZN13QDBusTrayIcon10updateMenuEP13QPlatformMenu',
        self._addressOf(menu),
    )

  @overload(str, str, QIcon, QPlatformSystemTrayIcon.MessageIcon, int)
  def showMessage(
      self,
      title: str,
      msg: str,
      icon: QIcon,
      iconType: QPlatformSystemTrayIcon.MessageIcon,
      msecs: int,
  ) -> None:
    """
    Calls Qt's 'void QDBusTrayIcon::showMessage(const QString &title, const
    QString &msg, const QIcon &icon, MessageIcon iconType, int msecs)'.

    Qt's own words: https://doc.qt.io/qt-6/qdbustrayicon.html#showMessage

    Parameters
    ----------

    title : str
      Passed on as it is: a QString is made of it for the call.

    msg : str
      Passed on as it is: a QString is made of it for the call.

    icon : QIcon
      Passed on as a value: Qt reads the C++ QIcon, which stays Python's own.

    iconType : QPlatformSystemTrayIcon.MessageIcon
      Passed on as its number.

    msecs : int
      Passed on as it is.
    """
    #  void QDBusTrayIcon::showMessage(const QString &title, const QString
    #      &msg, const QIcon &icon, MessageIcon iconType, int msecs)
    self.uglySide.call(
        'ritual_ZN13QDBusTrayIcon11showMessageERK7QStringS2_RK5QIconN23QPla'
        'tformSystemTrayIcon11MessageIconEi',
        title, msg, self._valueOf(icon), iconType.value, msecs,
    )

  def menu(self) -> Optional[QDBusPlatformMenu]:
    """
    Calls Qt's 'QDBusPlatformMenu *QDBusTrayIcon::menu()'.

    Qt's own words: https://doc.qt.io/qt-6/qdbustrayicon.html#menu

    Returns
    -------

    Optional[QDBusPlatformMenu]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDBusPlatformMenu *QDBusTrayIcon::menu()
    address = self.uglySide.call('ritual_ZN13QDBusTrayIcon4menuEv')
    from . import QDBusPlatformMenu
    return QDBusPlatformMenu._cuteAt(address)

  def categoryChanged(self) -> None:
    """
    Calls Qt's 'void QDBusTrayIcon::categoryChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qdbustrayicon.html#categoryChanged
    """
    #  void QDBusTrayIcon::categoryChanged()
    self.uglySide.call('ritual_ZN13QDBusTrayIcon15categoryChangedEv')

  @overload(str)
  def statusChanged(self, arg: str) -> None:
    """
    Calls Qt's 'void QDBusTrayIcon::statusChanged(QString arg)'.

    Qt's own words: https://doc.qt.io/qt-6/qdbustrayicon.html#statusChanged

    Parameters
    ----------

    arg : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDBusTrayIcon::statusChanged(QString arg)
    self.uglySide.call(
        'ritual_ZN13QDBusTrayIcon13statusChangedE7QString', arg,
    )

  def tooltipChanged(self) -> None:
    """
    Calls Qt's 'void QDBusTrayIcon::tooltipChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qdbustrayicon.html#tooltipChanged
    """
    #  void QDBusTrayIcon::tooltipChanged()
    self.uglySide.call('ritual_ZN13QDBusTrayIcon14tooltipChangedEv')

  def iconChanged(self) -> None:
    """
    Calls Qt's 'void QDBusTrayIcon::iconChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qdbustrayicon.html#iconChanged
    """
    #  void QDBusTrayIcon::iconChanged()
    self.uglySide.call('ritual_ZN13QDBusTrayIcon11iconChangedEv')

  def attention(self) -> None:
    """
    Calls Qt's 'void QDBusTrayIcon::attention()'.

    Qt's own words: https://doc.qt.io/qt-6/qdbustrayicon.html#attention
    """
    #  void QDBusTrayIcon::attention()
    self.uglySide.call('ritual_ZN13QDBusTrayIcon9attentionEv')

  def menuChanged(self) -> None:
    """
    Calls Qt's 'void QDBusTrayIcon::menuChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qdbustrayicon.html#menuChanged
    """
    #  void QDBusTrayIcon::menuChanged()
    self.uglySide.call('ritual_ZN13QDBusTrayIcon11menuChangedEv')

  def attentionTimerExpired(self) -> None:
    """
    Calls Qt's 'void QDBusTrayIcon::attentionTimerExpired()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbustrayicon.html#attentionTimerExpired
    """
    #  void QDBusTrayIcon::attentionTimerExpired()
    self.uglySide.call('ritual_ZN13QDBusTrayIcon21attentionTimerExpiredEv')

  @overload(int, str)
  def actionInvoked(self, id: int, action: str) -> None:
    """
    Calls Qt's 'void QDBusTrayIcon::actionInvoked(uint id, const QString
    &action)'.

    Qt's own words: https://doc.qt.io/qt-6/qdbustrayicon.html#actionInvoked

    Parameters
    ----------

    id : int
      Passed on as it is.

    action : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDBusTrayIcon::actionInvoked(uint id, const QString &action)
    self.uglySide.call(
        'ritual_ZN13QDBusTrayIcon13actionInvokedEjRK7QString', id, action,
    )

  @overload(int, int)
  def notificationClosed(self, id: int, reason: int) -> None:
    """
    Calls Qt's 'void QDBusTrayIcon::notificationClosed(uint id, uint
    reason)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbustrayicon.html#notificationClosed

    Parameters
    ----------

    id : int
      Passed on as it is.

    reason : int
      Passed on as it is.
    """
    #  void QDBusTrayIcon::notificationClosed(uint id, uint reason)
    self.uglySide.call(
        'ritual_ZN13QDBusTrayIcon18notificationClosedEjj', id, reason,
    )

  @overload(str)
  def watcherServiceRegistered(self, serviceName: str) -> None:
    """
    Calls Qt's 'void QDBusTrayIcon::watcherServiceRegistered(const QString
    &serviceName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbustrayicon.html#watcherServiceRegistered

    Parameters
    ----------

    serviceName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDBusTrayIcon::watcherServiceRegistered(const QString
    #      &serviceName)
    self.uglySide.call(
        'ritual_ZN13QDBusTrayIcon24watcherServiceRegisteredERK7QString',
        serviceName,
    )

  @overload(QIcon)
  def tempIcon(self, icon: QIcon) -> Optional[QTemporaryFile]:
    """
    Calls Qt's 'QTemporaryFile *QDBusTrayIcon::tempIcon(const QIcon &icon)'.

    Qt's own words: https://doc.qt.io/qt-6/qdbustrayicon.html#tempIcon

    Parameters
    ----------

    icon : QIcon
      Passed on as a value: Qt reads the C++ QIcon, which stays Python's own.

    Returns
    -------

    Optional[QTemporaryFile]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTemporaryFile *QDBusTrayIcon::tempIcon(const QIcon &icon)
    address = self.uglySide.call(
        'ritual_ZN13QDBusTrayIcon8tempIconERK5QIcon', self._valueOf(icon),
    )
    from ..QtCore import QTemporaryFile
    return QTemporaryFile._cuteAt(address)

  @staticmethod
  def dBusConnection(*__, **_) -> Never:
    """
    Qt's 'QDBusMenuConnection *QDBusTrayIcon::dBusConnection()': leans on
    'QDBusMenuConnection::QDBusMenuConnection(QObject*, QString const&)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QDBusTrayIcon.dBusConnection' has no cute function yet. Qt's "
        "'QDBusMenuConnection *QDBusTrayIcon::dBusConnection()': leans on "
        "'QDBusMenuConnection::QDBusMenuConnection(QObject*, QString "
        "const&)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def setStatus(*__, **_) -> Never:
    """
    Qt's 'void QDBusTrayIcon::setStatus(const QString &status)': leans on
    'QDBusTrayIcon::statusChanged(QString)', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDBusTrayIcon.setStatus' has no cute function yet. Qt's 'void "
        "QDBusTrayIcon::setStatus(const QString &status)': leans on "
        "'QDBusTrayIcon::statusChanged(QString)', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")
