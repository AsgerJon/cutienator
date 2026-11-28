"""
QSystemTrayIconPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qsystemtrayicon_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QSystemTrayIconPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QObjectPrivate
from ..QtGui import QPlatformSystemTrayIcon

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QMenu, QSystemTrayIcon
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMenu = WAIT['QMenu']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSystemTrayIconPrivate(QObjectPrivate):
  """
  The cute side of Qt's QSystemTrayIconPrivate: a plain Python object
  standing in front of one C++ QSystemTrayIconPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's QSystemTrayIconPrivate is
  built on Qt's QObjectPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSystemTrayIconPrivate that has a ritual and that
  Python can call so far, 4 names in all: 'q_func', '_q_emitActivated',
  'remove_sys_qpa', 'addPlatformMenu'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QSystemTrayIcon *QSystemTrayIconPrivate::q_func() const':
    takes in Python what 'QSystemTrayIcon *QSystemTrayIconPrivate::q_func()'
    takes.

  What has no ritual
  ------------------

  13 of the 18 functions Qt declares: 11 cannot be called and cannot be
  called through the meta-object and cannot be copied; 1 leans on
  'QSystemTrayIconPrivate; 1 leans on 'QBalloonTip.

  What to expect
  --------------

  - The C++ QSystemTrayIconPrivate is created at the first use, not by
    'QSystemTrayIconPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSystemTrayIconPrivate.
  - Each name of Qt's QSystemTrayIconPrivate that has no cute function yet,
    '__init__', 'destroyIcon', 'geometry_sys', 'install_sys',
    'install_sys_qpa', 'isSystemTrayAvailable_sys', 'remove_sys',
    'showMessage_sys', 'supportsMessages_sys', 'updateIcon_sys',
    'updateMenu_sys', 'updateToolTip_sys', holds a function that raises
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
  __qt_class__ = 'QSystemTrayIconPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
    Qt's 'QSystemTrayIconPrivate::QSystemTrayIconPrivate()': cannot be called
    and cannot be called through the meta-object and cannot be copied: no
    header file has its code, Qt's source does not mark it or its class for
    use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QSystemTrayIconPrivate.__init__' has no cute function yet. Qt's "
        "'QSystemTrayIconPrivate::QSystemTrayIconPrivate()': cannot be "
        "called and cannot be called through the meta-object and cannot be "
        "copied: no header file has its code, Qt's source does not mark it "
        "or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")

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

  def q_func(self) -> Optional[QSystemTrayIcon]:
    """
    Calls Qt's 'QSystemTrayIcon *QSystemTrayIconPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qsystemtrayiconprivate.html#q_func

    Returns
    -------

    Optional[QSystemTrayIcon]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSystemTrayIcon *QSystemTrayIconPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN22QSystemTrayIconPrivate6q_funcEv',
    )
    from . import QSystemTrayIcon
    return QSystemTrayIcon._cuteAt(address)

  @overload(QPlatformSystemTrayIcon.ActivationReason)
  def _q_emitActivated(
      self,
      reason: QPlatformSystemTrayIcon.ActivationReason,
  ) -> None:
    """
    Calls Qt's 'void
    QSystemTrayIconPrivate::_q_emitActivated(QPlatformSystemTrayIcon::
    ActivationReason reason)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsystemtrayiconprivate.html#_q_emitActivated

    Parameters
    ----------

    reason : QPlatformSystemTrayIcon.ActivationReason
      Passed on as its number.
    """
    #  void QSystemTrayIconPrivate::_q_emitActivated(
    #      QPlatformSystemTrayIcon::ActivationReason reason)
    self.uglySide.call(
        'ritual_ZN22QSystemTrayIconPrivate16_q_emitActivatedEN23QPlatformSy'
        'stemTrayIcon16ActivationReasonE',
        reason.value,
    )

  def remove_sys_qpa(self) -> None:
    """
    Calls Qt's 'void QSystemTrayIconPrivate::remove_sys_qpa()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsystemtrayiconprivate.html#remove_sys_qpa
    """
    #  void QSystemTrayIconPrivate::remove_sys_qpa()
    self.uglySide.call('ritual_ZN22QSystemTrayIconPrivate14remove_sys_qpaEv')

  @overload(QMenu)
  @overload(NoneType)
  def addPlatformMenu(self, menu: Optional[QMenu]) -> None:
    """
    Calls Qt's 'void QSystemTrayIconPrivate::addPlatformMenu(QMenu *menu)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsystemtrayiconprivate.html#addPlatformMenu

    Parameters
    ----------

    menu : Optional[QMenu]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSystemTrayIconPrivate::addPlatformMenu(QMenu *menu) const
    self.uglySide.call(
        'ritual_ZNK22QSystemTrayIconPrivate15addPlatformMenuEP5QMenu',
        self._addressOf(menu),
    )

  @staticmethod
  def destroyIcon(*__, **_) -> Never:
    """
    Qt's 'void QSystemTrayIconPrivate::destroyIcon()': leans on
    'QBalloonTip::hideBalloon()', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QSystemTrayIconPrivate.destroyIcon' has no cute function yet. "
        "Qt's 'void QSystemTrayIconPrivate::destroyIcon()': leans on "
        "'QBalloonTip::hideBalloon()', which Qt's source does not mark for "
        "use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def geometry_sys(*__, **_) -> Never:
    """
    Qt's 'QRect QSystemTrayIconPrivate::geometry_sys() const': cannot be
    called and cannot be called through the meta-object and cannot be copied:
    no header file has its code, Qt's source does not mark it or its class
    for use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QSystemTrayIconPrivate.geometry_sys' has no cute function yet. "
        "Qt's 'QRect QSystemTrayIconPrivate::geometry_sys() const': cannot "
        "be called and cannot be called through the meta-object and cannot "
        "be copied: no header file has its code, Qt's source does not mark "
        "it or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")

  @staticmethod
  def install_sys(*__, **_) -> Never:
    """
    Qt's 'void QSystemTrayIconPrivate::install_sys()': cannot be called and
    cannot be called through the meta-object and cannot be copied: no header
    file has its code, Qt's source does not mark it or its class for use from
    outside Qt or writes it 'inline' or nowhere, and it is no signal, slot or
    invokable function giving back nothing, of a class built on QObject, and
    Qt's source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QSystemTrayIconPrivate.install_sys' has no cute function yet. "
        "Qt's 'void QSystemTrayIconPrivate::install_sys()': cannot be "
        "called and cannot be called through the meta-object and cannot be "
        "copied: no header file has its code, Qt's source does not mark it "
        "or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")

  @staticmethod
  def install_sys_qpa(*__, **_) -> Never:
    """
    Qt's 'void QSystemTrayIconPrivate::install_sys_qpa()': leans on
    'QSystemTrayIconPrivate::updateIcon_sys()', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QSystemTrayIconPrivate.install_sys_qpa' has no cute function yet. "
        "Qt's 'void QSystemTrayIconPrivate::install_sys_qpa()': leans on "
        "'QSystemTrayIconPrivate::updateIcon_sys()', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def isSystemTrayAvailable_sys(*__, **_) -> Never:
    """
    Qt's 'bool QSystemTrayIconPrivate::isSystemTrayAvailable_sys()': cannot
    be called and cannot be called through the meta-object and cannot be
    copied: no header file has its code, Qt's source does not mark it or its
    class for use from outside Qt or writes it 'inline' or nowhere, and it is
    no signal, slot or invokable function giving back nothing, of a class
    built on QObject, and Qt's source has no code for it that could be told
    from the rest.
    """
    raise NotImplementedError(
        "'QSystemTrayIconPrivate.isSystemTrayAvailable_sys' has no cute "
        "function yet. Qt's 'bool "
        "QSystemTrayIconPrivate::isSystemTrayAvailable_sys()': cannot be "
        "called and cannot be called through the meta-object and cannot be "
        "copied: no header file has its code, Qt's source does not mark it "
        "or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")

  @staticmethod
  def remove_sys(*__, **_) -> Never:
    """
    Qt's 'void QSystemTrayIconPrivate::remove_sys()': cannot be called and
    cannot be called through the meta-object and cannot be copied: no header
    file has its code, Qt's source does not mark it or its class for use from
    outside Qt or writes it 'inline' or nowhere, and it is no signal, slot or
    invokable function giving back nothing, of a class built on QObject, and
    Qt's source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QSystemTrayIconPrivate.remove_sys' has no cute function yet. Qt's "
        "'void QSystemTrayIconPrivate::remove_sys()': cannot be called and "
        "cannot be called through the meta-object and cannot be copied: no "
        "header file has its code, Qt's source does not mark it or its "
        "class for use from outside Qt or writes it 'inline' or nowhere, "
        "and it is no signal, slot or invokable function giving back "
        "nothing, of a class built on QObject, and Qt's source has no code "
        "for it that could be told from the rest.")

  @staticmethod
  def showMessage_sys(*__, **_) -> Never:
    """
    Qt's 'void QSystemTrayIconPrivate::showMessage_sys(const QString &title,
    const QString &msg, const QIcon &icon, QSystemTrayIcon::MessageIcon
    msgIcon, int msecs)': cannot be called and cannot be called through the
    meta-object and cannot be copied: no header file has its code, Qt's
    source does not mark it or its class for use from outside Qt or writes it
    'inline' or nowhere, and it is no signal, slot or invokable function
    giving back nothing, of a class built on QObject, and Qt's source has no
    code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QSystemTrayIconPrivate.showMessage_sys' has no cute function yet. "
        "Qt's 'void QSystemTrayIconPrivate::showMessage_sys(const QString "
        "&title, const QString &msg, const QIcon &icon, "
        "QSystemTrayIcon::MessageIcon msgIcon, int msecs)': cannot be "
        "called and cannot be called through the meta-object and cannot be "
        "copied: no header file has its code, Qt's source does not mark it "
        "or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")

  @staticmethod
  def supportsMessages_sys(*__, **_) -> Never:
    """
    Qt's 'bool QSystemTrayIconPrivate::supportsMessages_sys()': cannot be
    called and cannot be called through the meta-object and cannot be copied:
    no header file has its code, Qt's source does not mark it or its class
    for use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QSystemTrayIconPrivate.supportsMessages_sys' has no cute function "
        "yet. Qt's 'bool QSystemTrayIconPrivate::supportsMessages_sys()': "
        "cannot be called and cannot be called through the meta-object and "
        "cannot be copied: no header file has its code, Qt's source does "
        "not mark it or its class for use from outside Qt or writes it "
        "'inline' or nowhere, and it is no signal, slot or invokable "
        "function giving back nothing, of a class built on QObject, and "
        "Qt's source has no code for it that could be told from the rest.")

  @staticmethod
  def updateIcon_sys(*__, **_) -> Never:
    """
    Qt's 'void QSystemTrayIconPrivate::updateIcon_sys()': cannot be called
    and cannot be called through the meta-object and cannot be copied: no
    header file has its code, Qt's source does not mark it or its class for
    use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QSystemTrayIconPrivate.updateIcon_sys' has no cute function yet. "
        "Qt's 'void QSystemTrayIconPrivate::updateIcon_sys()': cannot be "
        "called and cannot be called through the meta-object and cannot be "
        "copied: no header file has its code, Qt's source does not mark it "
        "or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")

  @staticmethod
  def updateMenu_sys(*__, **_) -> Never:
    """
    Qt's 'void QSystemTrayIconPrivate::updateMenu_sys()': cannot be called
    and cannot be called through the meta-object and cannot be copied: no
    header file has its code, Qt's source does not mark it or its class for
    use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QSystemTrayIconPrivate.updateMenu_sys' has no cute function yet. "
        "Qt's 'void QSystemTrayIconPrivate::updateMenu_sys()': cannot be "
        "called and cannot be called through the meta-object and cannot be "
        "copied: no header file has its code, Qt's source does not mark it "
        "or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")

  @staticmethod
  def updateToolTip_sys(*__, **_) -> Never:
    """
    Qt's 'void QSystemTrayIconPrivate::updateToolTip_sys()': cannot be called
    and cannot be called through the meta-object and cannot be copied: no
    header file has its code, Qt's source does not mark it or its class for
    use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QSystemTrayIconPrivate.updateToolTip_sys' has no cute function "
        "yet. Qt's 'void QSystemTrayIconPrivate::updateToolTip_sys()': "
        "cannot be called and cannot be called through the meta-object and "
        "cannot be copied: no header file has its code, Qt's source does "
        "not mark it or its class for use from outside Qt or writes it "
        "'inline' or nowhere, and it is no signal, slot or invokable "
        "function giving back nothing, of a class built on QObject, and "
        "Qt's source has no code for it that could be told from the rest.")
