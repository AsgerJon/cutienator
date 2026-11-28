"""
QQuickLabsPlatformSystemTrayIcon binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLabsPlatform/6.12.0/QtLabsPlatform/private/qquicklabsplatformsystemtrayicon_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickLabsPlatformSystemTrayIcon to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from ..QtGui import QPlatformSystemTrayIcon

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QQuickLabsPlatformIcon, QQuickLabsPlatformMenu
  from ..QtCore import QMetaObject, QRect


class QQuickLabsPlatformSystemTrayIcon(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickLabsPlatformSystemTrayIcon: a plain Python
  object standing in front of one C++ QQuickLabsPlatformSystemTrayIcon.

  What exists
  -----------

  Every function of Qt's QQuickLabsPlatformSystemTrayIcon that has a ritual
  and that Python can call so far, 24 names in all: 'metaObject',
  'qmlExtendedNamespace', 'handle', 'isAvailable', 'supportsMessages',
  'isVisible', 'tooltip', 'menu', 'geometry', 'icon', 'show', 'hide',
  'showMessage', 'activated', 'messageClicked', 'visibleChanged',
  'tooltipChanged', 'menuChanged', 'geometryChanged', 'iconChanged',
  'cleanup', 'classBegin', 'componentComplete', 'updateIcon'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickLabsPlatformSystemTrayIcon::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int QQuickLabsPlatformSystemTrayIcon::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void
    QQuickLabsPlatformSystemTrayIcon::qt_qmlMarker_extendedNamespace()': one
    of Qt's own inner workings.
  - Qt's
    'QQuickLabsPlatformSystemTrayIcon::~QQuickLabsPlatformSystemTrayIcon()':
    the destructor: Python never removes a C++
    QQuickLabsPlatformSystemTrayIcon.

  What has no ritual
  ------------------

  10 of the 38 functions Qt declares: 6 leans on
  'QQuickLabsPlatformSystemTrayIcon; 2 not a gap; 1 Qt's library has no name
  for it, and its code in Qt's source does not compile apart from its file; 1
  leans on 'QQuickLabsPlatformMenu.

  What to expect
  --------------

  - The C++ QQuickLabsPlatformSystemTrayIcon is created at the first use, not
    by 'QQuickLabsPlatformSystemTrayIcon(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickLabsPlatformSystemTrayIcon.
  - Qt tells when it has removed the C++ QQuickLabsPlatformSystemTrayIcon.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickLabsPlatformSystemTrayIcon that has no cute
    function yet, '__init__', 'iconLoader', 'init', 'setIcon', 'setMenu',
    'setTooltip', 'setVisible', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def qmlExtendedNamespace() -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *QQuickLabsPlatformSystemTrayIcon::qmlExtendedNamespace()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformsystemtrayicon.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject
    #      *QQuickLabsPlatformSystemTrayIcon::qmlExtendedNamespace()
    address = Rituals.call(
        'ritual_ZN32QQuickLabsPlatformSystemTrayIcon20qmlExtendedNamespaceE'
        'v',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickLabsPlatformSystemTrayIcon'

  #  A C++ QQuickLabsPlatformSystemTrayIcon Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickLabsPlatformSystemTrayIcon'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *QQuickLabsPlatformSystemTrayIcon::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformsystemtrayicon.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickLabsPlatformSystemTrayIcon::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK32QQuickLabsPlatformSystemTrayIcon10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def handle(self) -> Optional[QPlatformSystemTrayIcon]:
    """
    Calls Qt's 'QPlatformSystemTrayIcon
    *QQuickLabsPlatformSystemTrayIcon::handle() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformsystemtrayicon.html#handle

    Returns
    -------

    Optional[QPlatformSystemTrayIcon]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformSystemTrayIcon *QQuickLabsPlatformSystemTrayIcon::handle()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK32QQuickLabsPlatformSystemTrayIcon6handleEv',
    )
    return QPlatformSystemTrayIcon._cuteAt(address)

  def isAvailable(self) -> bool:
    """
    Calls Qt's 'bool QQuickLabsPlatformSystemTrayIcon::isAvailable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformsystemtrayicon.html#isAvailable
    """
    #  bool QQuickLabsPlatformSystemTrayIcon::isAvailable() const
    return self.uglySide.call(
        'ritual_ZNK32QQuickLabsPlatformSystemTrayIcon11isAvailableEv',
    )

  def supportsMessages(self) -> bool:
    """
    Calls Qt's 'bool QQuickLabsPlatformSystemTrayIcon::supportsMessages()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformsystemtrayicon.html
    """
    #  bool QQuickLabsPlatformSystemTrayIcon::supportsMessages() const
    return self.uglySide.call(
        'ritual_ZNK32QQuickLabsPlatformSystemTrayIcon16supportsMessagesEv',
    )

  def isVisible(self) -> bool:
    """
    Calls Qt's 'bool QQuickLabsPlatformSystemTrayIcon::isVisible() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformsystemtrayicon.html#isVisible
    """
    #  bool QQuickLabsPlatformSystemTrayIcon::isVisible() const
    return self.uglySide.call(
        'ritual_ZNK32QQuickLabsPlatformSystemTrayIcon9isVisibleEv',
    )

  def tooltip(self) -> str:
    """
    Calls Qt's 'QString QQuickLabsPlatformSystemTrayIcon::tooltip() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformsystemtrayicon.html#tooltip

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickLabsPlatformSystemTrayIcon::tooltip() const
    return self.uglySide.call(
        'ritual_ZNK32QQuickLabsPlatformSystemTrayIcon7tooltipEv',
    )

  def menu(self) -> Optional[QQuickLabsPlatformMenu]:
    """
    Calls Qt's 'QQuickLabsPlatformMenu
    *QQuickLabsPlatformSystemTrayIcon::menu() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformsystemtrayicon.html#menu

    Returns
    -------

    Optional[QQuickLabsPlatformMenu]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickLabsPlatformMenu *QQuickLabsPlatformSystemTrayIcon::menu() const
    address = self.uglySide.call(
        'ritual_ZNK32QQuickLabsPlatformSystemTrayIcon4menuEv',
    )
    from . import QQuickLabsPlatformMenu
    return QQuickLabsPlatformMenu._cuteAt(address)

  def geometry(self) -> QRect:
    """
    Calls Qt's 'QRect QQuickLabsPlatformSystemTrayIcon::geometry() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformsystemtrayicon.html#geometry

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QQuickLabsPlatformSystemTrayIcon::geometry() const
    address = self.uglySide.call(
        'ritual_ZNK32QQuickLabsPlatformSystemTrayIcon8geometryEv',
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def icon(self) -> QQuickLabsPlatformIcon:
    """
    Calls Qt's 'QQuickLabsPlatformIcon
    QQuickLabsPlatformSystemTrayIcon::icon() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformsystemtrayicon.html#icon

    Returns
    -------

    QQuickLabsPlatformIcon
      A new cute QQuickLabsPlatformIcon around the copy Qt gave back. Python
      owns it.
    """
    #  QQuickLabsPlatformIcon QQuickLabsPlatformSystemTrayIcon::icon() const
    address = self.uglySide.call(
        'ritual_ZNK32QQuickLabsPlatformSystemTrayIcon4iconEv',
    )
    from . import QQuickLabsPlatformIcon
    return QQuickLabsPlatformIcon._cuteOwning(address)

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
    Qt's 'QQuickLabsPlatformSystemTrayIcon::QQuickLabsPlatformSystemTrayIcon(
    QObject *parent)': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: use of undeclared identifier
    'QWidgetPlatform'.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformSystemTrayIcon.__init__' has no cute function "
        "yet. Qt's "
        "'QQuickLabsPlatformSystemTrayIcon::QQuickLabsPlatformSystemTrayIcon"
        "(QObject *parent)': Qt's library has no name for it, and its code "
        "in Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'QWidgetPlatform'.")

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

  def show(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformSystemTrayIcon::show()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformsystemtrayicon.html#show
    """
    #  void QQuickLabsPlatformSystemTrayIcon::show()
    self.uglySide.call('ritual_ZN32QQuickLabsPlatformSystemTrayIcon4showEv')

  def hide(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformSystemTrayIcon::hide()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformsystemtrayicon.html#hide
    """
    #  void QQuickLabsPlatformSystemTrayIcon::hide()
    self.uglySide.call('ritual_ZN32QQuickLabsPlatformSystemTrayIcon4hideEv')

  @overload(str, str)
  @overload(str, str, QPlatformSystemTrayIcon.MessageIcon)
  @overload(str, str, QPlatformSystemTrayIcon.MessageIcon, int)
  def showMessage(
      self,
      title: str,
      message: str,
      iconType: QPlatformSystemTrayIcon.MessageIcon = (
          QPlatformSystemTrayIcon.MessageIcon.Information),
      msecs: int = 10000,
  ) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformSystemTrayIcon::showMessage(const
    QString &title, const QString &message,
    QPlatformSystemTrayIcon::MessageIcon iconType, int msecs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformsystemtrayicon.html#showMessage

    Parameters
    ----------

    title : str
      Passed on as it is: a QString is made of it for the call.

    message : str
      Passed on as it is: a QString is made of it for the call.

    iconType : QPlatformSystemTrayIcon.MessageIcon
      Passed on as its number. May be left out, as in Qt: it is then
      QPlatformSystemTrayIcon.MessageIcon.Information.

    msecs : int
      Passed on as it is. May be left out, as in Qt: it is then 10000.
    """
    #  void QQuickLabsPlatformSystemTrayIcon::showMessage(const QString
    #      &title, const QString &message,
    #      QPlatformSystemTrayIcon::MessageIcon iconType, int msecs)
    self.uglySide.call(
        'ritual_ZN32QQuickLabsPlatformSystemTrayIcon11showMessageERK7QStrin'
        'gS2_N23QPlatformSystemTrayIcon11MessageIconEi',
        title, message, iconType.value, msecs,
    )

  @overload(QPlatformSystemTrayIcon.ActivationReason)
  def activated(
      self,
      reason: QPlatformSystemTrayIcon.ActivationReason,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickLabsPlatformSystemTrayIcon::activated(QPlatformSystemTrayIcon::
    ActivationReason reason)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformsystemtrayicon.html#activated

    Parameters
    ----------

    reason : QPlatformSystemTrayIcon.ActivationReason
      Passed on as its number.
    """
    #  void QQuickLabsPlatformSystemTrayIcon::activated(
    #      QPlatformSystemTrayIcon::ActivationReason reason)
    self.uglySide.call(
        'ritual_ZN32QQuickLabsPlatformSystemTrayIcon9activatedEN23QPlatform'
        'SystemTrayIcon16ActivationReasonE',
        reason.value,
    )

  def messageClicked(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformSystemTrayIcon::messageClicked()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformsystemtrayicon.html
    """
    #  void QQuickLabsPlatformSystemTrayIcon::messageClicked()
    self.uglySide.call(
        'ritual_ZN32QQuickLabsPlatformSystemTrayIcon14messageClickedEv',
    )

  def visibleChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformSystemTrayIcon::visibleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformsystemtrayicon.html
    """
    #  void QQuickLabsPlatformSystemTrayIcon::visibleChanged()
    self.uglySide.call(
        'ritual_ZN32QQuickLabsPlatformSystemTrayIcon14visibleChangedEv',
    )

  def tooltipChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformSystemTrayIcon::tooltipChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformsystemtrayicon.html
    """
    #  void QQuickLabsPlatformSystemTrayIcon::tooltipChanged()
    self.uglySide.call(
        'ritual_ZN32QQuickLabsPlatformSystemTrayIcon14tooltipChangedEv',
    )

  def menuChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformSystemTrayIcon::menuChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformsystemtrayicon.html#menuChanged
    """
    #  void QQuickLabsPlatformSystemTrayIcon::menuChanged()
    self.uglySide.call(
        'ritual_ZN32QQuickLabsPlatformSystemTrayIcon11menuChangedEv',
    )

  def geometryChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformSystemTrayIcon::geometryChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformsystemtrayicon.html
    """
    #  void QQuickLabsPlatformSystemTrayIcon::geometryChanged()
    self.uglySide.call(
        'ritual_ZN32QQuickLabsPlatformSystemTrayIcon15geometryChangedEv',
    )

  def iconChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformSystemTrayIcon::iconChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformsystemtrayicon.html#iconChanged
    """
    #  void QQuickLabsPlatformSystemTrayIcon::iconChanged()
    self.uglySide.call(
        'ritual_ZN32QQuickLabsPlatformSystemTrayIcon11iconChangedEv',
    )

  def cleanup(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformSystemTrayIcon::cleanup()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformsystemtrayicon.html#cleanup
    """
    #  void QQuickLabsPlatformSystemTrayIcon::cleanup()
    self.uglySide.call(
        'ritual_ZN32QQuickLabsPlatformSystemTrayIcon7cleanupEv',
    )

  def classBegin(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformSystemTrayIcon::classBegin()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformsystemtrayicon.html#classBegin
    """
    #  void QQuickLabsPlatformSystemTrayIcon::classBegin()
    ritual = 'ritual_ZN32QQuickLabsPlatformSystemTrayIcon10classBeginEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN32QQuickLabsPlatformSystemTrayIcon10classBeginEv')
    self.uglySide.call(ritual)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformSystemTrayIcon::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformsystemtrayicon.html
    """
    #  void QQuickLabsPlatformSystemTrayIcon::componentComplete()
    self.uglySide.call(
        'ritual_ZN32QQuickLabsPlatformSystemTrayIcon17componentCompleteEv',
    )

  def updateIcon(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformSystemTrayIcon::updateIcon()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformsystemtrayicon.html#updateIcon
    """
    #  void QQuickLabsPlatformSystemTrayIcon::updateIcon()
    self.uglySide.call(
        'ritual_ZN32QQuickLabsPlatformSystemTrayIcon10updateIconEv',
    )

  @staticmethod
  def iconLoader(*__, **_) -> Never:
    """
    Qt's 'QQuickLabsPlatformIconLoader
    *QQuickLabsPlatformSystemTrayIcon::iconLoader() const': leans on
    'QQuickLabsPlatformSystemTrayIcon::staticMetaObject', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformSystemTrayIcon.iconLoader' has no cute function "
        "yet. Qt's 'QQuickLabsPlatformIconLoader "
        "*QQuickLabsPlatformSystemTrayIcon::iconLoader() const': leans on "
        "'QQuickLabsPlatformSystemTrayIcon::staticMetaObject', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def init(*__, **_) -> Never:
    """
    Qt's 'void QQuickLabsPlatformSystemTrayIcon::init()': leans on
    'QQuickLabsPlatformMenu::create()', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformSystemTrayIcon.init' has no cute function yet. "
        "Qt's 'void QQuickLabsPlatformSystemTrayIcon::init()': leans on "
        "'QQuickLabsPlatformMenu::create()', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def setIcon(*__, **_) -> Never:
    """
    Qt's 'void QQuickLabsPlatformSystemTrayIcon::setIcon(const
    QQuickLabsPlatformIcon &icon)': leans on
    'QQuickLabsPlatformSystemTrayIcon::iconChanged()', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformSystemTrayIcon.setIcon' has no cute function "
        "yet. Qt's 'void QQuickLabsPlatformSystemTrayIcon::setIcon(const "
        "QQuickLabsPlatformIcon &icon)': leans on "
        "'QQuickLabsPlatformSystemTrayIcon::iconChanged()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def setMenu(*__, **_) -> Never:
    """
    Qt's 'void
    QQuickLabsPlatformSystemTrayIcon::setMenu(QQuickLabsPlatformMenu *menu)':
    leans on 'QQuickLabsPlatformSystemTrayIcon::menuChanged()', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformSystemTrayIcon.setMenu' has no cute function "
        "yet. Qt's 'void "
        "QQuickLabsPlatformSystemTrayIcon::setMenu(QQuickLabsPlatformMenu "
        "*menu)': leans on "
        "'QQuickLabsPlatformSystemTrayIcon::menuChanged()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def setTooltip(*__, **_) -> Never:
    """
    Qt's 'void QQuickLabsPlatformSystemTrayIcon::setTooltip(const QString
    &tooltip)': leans on
    'QQuickLabsPlatformSystemTrayIcon::tooltipChanged()', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformSystemTrayIcon.setTooltip' has no cute function "
        "yet. Qt's 'void QQuickLabsPlatformSystemTrayIcon::setTooltip(const "
        "QString &tooltip)': leans on "
        "'QQuickLabsPlatformSystemTrayIcon::tooltipChanged()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def setVisible(*__, **_) -> Never:
    """
    Qt's 'void QQuickLabsPlatformSystemTrayIcon::setVisible(bool visible)':
    leans on 'QQuickLabsPlatformSystemTrayIcon::visibleChanged()', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformSystemTrayIcon.setVisible' has no cute function "
        "yet. Qt's 'void QQuickLabsPlatformSystemTrayIcon::setVisible(bool "
        "visible)': leans on "
        "'QQuickLabsPlatformSystemTrayIcon::visibleChanged()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")
