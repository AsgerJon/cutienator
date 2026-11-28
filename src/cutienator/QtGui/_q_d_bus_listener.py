"""
QDBusListener binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qdbuslistener_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QDBusListener to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum, WAIT
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QVariant
  from ..QtDBus import QDBusVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDBusVariant = WAIT['QDBusVariant']
  QVariant = WAIT['QVariant']


class QDBusListener(QObject):
  """
  The cute side of Qt's QDBusListener: a plain Python object standing in
  front of one C++ QDBusListener.

  It is built on the cute 'QObject', as Qt's QDBusListener is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QDBusListener that has a ritual and that Python can
  call so far, 3 names in all: 'metaObject', 'onSettingChanged',
  'settingChanged'. None can be made from Python: one comes out of a function
  of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QDBusListener::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QDBusListener::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'std::optional<ChangeSignal> QDBusListener::findSignal(const QString
    &location, const QString &key) const': gives a type Python has no way to
    take yet.

  What has no ritual
  ------------------

  9 of the 15 functions Qt declares: 3 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 2 not a gap;
  2 leans on 'QDBusListener; 2 leans on 'vtable for QDBusListener', which
  Qt's source does not mark for use from outside Qt and has no code for that
  could be taken.

  What to expect
  --------------

  - The C++ QDBusListener is created at the first use, not by
    'QDBusListener(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDBusListener.
  - Qt tells when it has removed the C++ QDBusListener. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QDBusListener that has no cute function yet,
    '__init__', 'findSignal', 'init', 'loadJson', 'populateSignalMap',
    'saveJson', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The enums Qt writes inside QDBusListener, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Provider(CuteNum, scoped=True):
    """
    The enum 'QDBusListener::Provider' of Qt, with the 3 names Qt gives in
    it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    Kde = Kee[int](0)
    Gtk = Kee[int](1)
    Gnome = Kee[int](2)

  class Setting(CuteNum, scoped=True):
    """
    The enum 'QDBusListener::Setting' of Qt, with the 5 names Qt gives in it.
    C++ keeps these names inside the enum, so the class that holds the enum
    does not have them.
    """

    Theme = Kee[int](0)
    ApplicationStyle = Kee[int](1)
    ColorScheme = Kee[int](2)
    Contrast = Kee[int](3)
    Motion = Kee[int](4)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDBusListener'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QDBusListener::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdbuslistener.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QDBusListener::metaObject() const
    address = self.uglySide.call('ritual_ZNK13QDBusListener10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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
    - Qt's 'QDBusListener::QDBusListener()': leans on 'vtable for
      QDBusListener', which Qt's source does not mark for use from outside Qt
      and has no code for that could be taken.
    - Qt's 'QDBusListener::QDBusListener(const QString &service, const
      QString &path, const QString &interface, const QString &signal)': leans
      on 'vtable for QDBusListener', which Qt's source does not mark for use
      from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDBusListener.__init__' has no cute function yet. Qt's "
        "'QDBusListener::QDBusListener()': leans on 'vtable for "
        "QDBusListener', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken. Qt's "
        "'QDBusListener::QDBusListener(const QString &service, const "
        "QString &path, const QString &interface, const QString &signal)': "
        "leans on 'vtable for QDBusListener', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

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

  @overload(str, str, QDBusVariant)
  def onSettingChanged(
      self,
      location: str,
      key: str,
      value: QDBusVariant,
  ) -> None:
    """
    Calls Qt's 'void QDBusListener::onSettingChanged(const QString &location,
    const QString &key, const QDBusVariant &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbuslistener.html#onSettingChanged

    Parameters
    ----------

    location : str
      Passed on as it is: a QString is made of it for the call.

    key : str
      Passed on as it is: a QString is made of it for the call.

    value : QDBusVariant
      Passed on as a value: Qt reads the C++ QDBusVariant, which stays
      Python's own.
    """
    #  void QDBusListener::onSettingChanged(const QString &location, const
    #      QString &key, const QDBusVariant &value)
    self.uglySide.call(
        'ritual_ZN13QDBusListener16onSettingChangedERK7QStringS2_RK12QDBusV'
        'ariant',
        location, key, self._valueOf(value),
    )

  @overload(Provider, Setting, QVariant)
  def settingChanged(
      self,
      provider: Provider,
      setting: Setting,
      value: QVariant,
  ) -> None:
    """
    Calls Qt's 'void QDBusListener::settingChanged(QDBusListener::Provider
    provider, QDBusListener::Setting setting, const QVariant &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qdbuslistener.html#settingChanged

    Parameters
    ----------

    provider : Provider
      Passed on as its number.

    setting : Setting
      Passed on as its number.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QDBusListener::settingChanged(QDBusListener::Provider provider,
    #      QDBusListener::Setting setting, const QVariant &value)
    self.uglySide.call(
        'ritual_ZN13QDBusListener14settingChangedENS_8ProviderENS_7SettingE'
        'RK8QVariant',
        provider.value, setting.value, self._valueOf(value),
    )

  @staticmethod
  def findSignal(*__, **_) -> Never:
    """
    Qt's 'std::optional<ChangeSignal> QDBusListener::findSignal(const QString
    &location, const QString &key) const': gives a type Python has no way to
    take yet.
    """
    raise NotImplementedError(
        "'QDBusListener.findSignal' has no cute function yet. Qt's "
        "'std::optional<ChangeSignal> QDBusListener::findSignal(const "
        "QString &location, const QString &key) const': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def init(*__, **_) -> Never:
    """
    Qt's 'void QDBusListener::init(const QString &service, const QString
    &path, const QString &interface, const QString &signal)': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: use of undeclared identifier 'lcQpaThemeDBus'.
    """
    raise NotImplementedError(
        "'QDBusListener.init' has no cute function yet. Qt's 'void "
        "QDBusListener::init(const QString &service, const QString &path, "
        "const QString &interface, const QString &signal)': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier 'lcQpaThemeDBus'."
    )

  @staticmethod
  def loadJson(*__, **_) -> Never:
    """
    Qt's 'void QDBusListener::loadJson(const QString &fileName)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'lcQpaThemeDBus'.
    """
    raise NotImplementedError(
        "'QDBusListener.loadJson' has no cute function yet. Qt's 'void "
        "QDBusListener::loadJson(const QString &fileName)': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier 'lcQpaThemeDBus'."
    )

  @staticmethod
  def populateSignalMap(*__, **_) -> Never:
    """
    Qt's 'void QDBusListener::populateSignalMap()': leans on
    'QDBusListener::loadJson(QString const&)', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDBusListener.populateSignalMap' has no cute function yet. Qt's "
        "'void QDBusListener::populateSignalMap()': leans on "
        "'QDBusListener::loadJson(QString const&)', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def saveJson(*__, **_) -> Never:
    """
    Qt's 'void QDBusListener::saveJson(const QString &fileName) const': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'lcQpaThemeDBus'.
    """
    raise NotImplementedError(
        "'QDBusListener.saveJson' has no cute function yet. Qt's 'void "
        "QDBusListener::saveJson(const QString &fileName) const': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'lcQpaThemeDBus'.")
