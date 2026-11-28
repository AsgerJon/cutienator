"""
QOpcUaConnectionSettings binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpcUa/qopcuaconnectionsettings.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from ..QtCore import QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QOpcUaConnectionSettings(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QOpcUaConnectionSettings: a plain Python object
  standing in front of one C++ QOpcUaConnectionSettings.

  C++ hands a QOpcUaConnectionSettings around as a copy, so every C++
  QOpcUaConnectionSettings behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QOpcUaConnectionSettings that has a ritual and that
  Python can call so far, 4 names in all: 'sessionLocaleIds',
  'setSessionLocaleIds', '__eq__', '__ne__'. It can be made from Python, in 2
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QOpcUaConnectionSettings &QOpcUaConnectionSettings::operator=(const
    QOpcUaConnectionSettings &rhs)': assignment: Python binds a name and has
    no operator for it.
  - Qt's 'QOpcUaConnectionSettings::QOpcUaConnectionSettings(
    QOpcUaConnectionSettings &&other)': takes a type Python has no way to
    hand over yet.
  - Qt's 'QOpcUaConnectionSettings
    &QOpcUaConnectionSettings::operator=(QOpcUaConnectionSettings &&other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QOpcUaConnectionSettings::~QOpcUaConnectionSettings()': the
    destructor: Python removes its C++ QOpcUaConnectionSettings by it, and
    has no other use for it.
  - Qt's 'void QOpcUaConnectionSettings::swap(QOpcUaConnectionSettings
    &other)': takes a type Python has no way to hand over yet.
  - Qt's 'std::chrono::milliseconds
    QOpcUaConnectionSettings::secureChannelLifeTime() const': gives a type
    Python has no way to take yet.
  - Qt's 'void
    QOpcUaConnectionSettings::setSecureChannelLifeTime(std::chrono::
    milliseconds lifeTime)': takes a type Python has no way to hand over yet.
  - Qt's 'std::chrono::milliseconds
    QOpcUaConnectionSettings::sessionTimeout() const': gives a type Python
    has no way to take yet.
  - Qt's 'void
    QOpcUaConnectionSettings::setSessionTimeout(std::chrono::milliseconds
    timeout)': takes a type Python has no way to hand over yet.
  - Qt's 'std::chrono::milliseconds
    QOpcUaConnectionSettings::requestTimeout() const': gives a type Python
    has no way to take yet.
  - Qt's 'void
    QOpcUaConnectionSettings::setRequestTimeout(std::chrono::milliseconds
    timeout)': takes a type Python has no way to hand over yet.
  - Qt's 'std::chrono::milliseconds
    QOpcUaConnectionSettings::connectTimeout() const': gives a type Python
    has no way to take yet.
  - Qt's 'void
    QOpcUaConnectionSettings::setConnectTimeout(std::chrono::milliseconds
    timeout)': takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QOpcUaConnectionSettings is created at the first use, not by
    'QOpcUaConnectionSettings(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QOpcUaConnectionSettings back gives a copy the ritual
    made for Python, in a new cute QOpcUaConnectionSettings.
  - Each name of Qt's QOpcUaConnectionSettings that has no cute function yet,
    'connectTimeout', 'requestTimeout', 'secureChannelLifeTime',
    'sessionTimeout', 'setConnectTimeout', 'setRequestTimeout',
    'setSecureChannelLifeTime', 'setSessionTimeout', 'swap', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpcUaConnectionSettings'

  #  Qt's '~QOpcUaConnectionSettings()'. Naming it makes this a value class:
  #  Python owns every C++ QOpcUaConnectionSettings behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN24QOpcUaConnectionSettingsD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def sessionLocaleIds(self) -> QStringList:
    """
    Calls Qt's 'QStringList QOpcUaConnectionSettings::sessionLocaleIds()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaconnectionsettings.html#sessionLocaleIds

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QOpcUaConnectionSettings::sessionLocaleIds() const
    address = self.uglySide.call(
        'ritual_ZNK24QOpcUaConnectionSettings16sessionLocaleIdsEv',
    )
    return QStringList._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QStringList)
  def setSessionLocaleIds(self, localeIds: QStringList) -> None:
    """
    Calls Qt's 'void QOpcUaConnectionSettings::setSessionLocaleIds(const
    QStringList &localeIds)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaconnectionsettings.html#setSessionLocaleIds

    Parameters
    ----------

    localeIds : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QOpcUaConnectionSettings::setSessionLocaleIds(const QStringList
    #      &localeIds)
    self.uglySide.call(
        'ritual_ZN24QOpcUaConnectionSettings19setSessionLocaleIdsERK5QListI'
        '7QStringE',
        self._valueOf(localeIds),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QOpcUaConnectionSettings) -> bool:
    """
    Calls Qt's 'bool operator==(const QOpcUaConnectionSettings &lhs, const
    QOpcUaConnectionSettings &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaconnectionsettings.html#operator==

    Parameters
    ----------

    rhs : QOpcUaConnectionSettings
      Passed on as a value: Qt reads the C++ QOpcUaConnectionSettings, which
      stays Python's own.
    """
    #  bool operator==(const QOpcUaConnectionSettings &lhs, const
    #      QOpcUaConnectionSettings &rhs)
    return Rituals.call(
        'ritual_ZeqRK24QOpcUaConnectionSettingsS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(self, rhs: QOpcUaConnectionSettings) -> bool:
    """
    Calls Qt's 'bool operator!=(const QOpcUaConnectionSettings &lhs, const
    QOpcUaConnectionSettings &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaconnectionsettings.html#operator!=

    Parameters
    ----------

    rhs : QOpcUaConnectionSettings
      Passed on as a value: Qt reads the C++ QOpcUaConnectionSettings, which
      stays Python's own.
    """
    #  bool operator!=(const QOpcUaConnectionSettings &lhs, const
    #      QOpcUaConnectionSettings &rhs)
    return Rituals.call(
        'ritual_ZneRK24QOpcUaConnectionSettingsS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QOpcUaConnectionSettings::QOpcUaConnectionSettings()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaconnectionsettings.html
    """
    #  QOpcUaConnectionSettings::QOpcUaConnectionSettings()
    self._noteCreation(QOpcUaConnectionSettings, lambda: Rituals.call(
        'ritual_ZN24QOpcUaConnectionSettingsC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QOpcUaConnectionSettings) -> None:
    """
    Notes what was given, for Qt's
    'QOpcUaConnectionSettings::QOpcUaConnectionSettings(const
    QOpcUaConnectionSettings &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaconnectionsettings.html

    Parameters
    ----------

    other : QOpcUaConnectionSettings
      Passed on as a value: Qt reads the C++ QOpcUaConnectionSettings, which
      stays Python's own.
    """
    #  QOpcUaConnectionSettings::QOpcUaConnectionSettings(const
    #      QOpcUaConnectionSettings &other)
    self._noteCreation(QOpcUaConnectionSettings, lambda: Rituals.call(
        'ritual_ZN24QOpcUaConnectionSettingsC1ERKS_', self._valueOf(other),
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

  @staticmethod
  def connectTimeout(*__, **_) -> Never:
    """
    Qt's 'std::chrono::milliseconds
    QOpcUaConnectionSettings::connectTimeout() const': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QOpcUaConnectionSettings.connectTimeout' has no cute function "
        "yet. Qt's 'std::chrono::milliseconds "
        "QOpcUaConnectionSettings::connectTimeout() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def requestTimeout(*__, **_) -> Never:
    """
    Qt's 'std::chrono::milliseconds
    QOpcUaConnectionSettings::requestTimeout() const': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QOpcUaConnectionSettings.requestTimeout' has no cute function "
        "yet. Qt's 'std::chrono::milliseconds "
        "QOpcUaConnectionSettings::requestTimeout() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def secureChannelLifeTime(*__, **_) -> Never:
    """
    Qt's 'std::chrono::milliseconds
    QOpcUaConnectionSettings::secureChannelLifeTime() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QOpcUaConnectionSettings.secureChannelLifeTime' has no cute "
        "function yet. Qt's 'std::chrono::milliseconds "
        "QOpcUaConnectionSettings::secureChannelLifeTime() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def sessionTimeout(*__, **_) -> Never:
    """
    Qt's 'std::chrono::milliseconds
    QOpcUaConnectionSettings::sessionTimeout() const': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QOpcUaConnectionSettings.sessionTimeout' has no cute function "
        "yet. Qt's 'std::chrono::milliseconds "
        "QOpcUaConnectionSettings::sessionTimeout() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def setConnectTimeout(*__, **_) -> Never:
    """
    Qt's 'void
    QOpcUaConnectionSettings::setConnectTimeout(std::chrono::milliseconds
    timeout)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QOpcUaConnectionSettings.setConnectTimeout' has no cute function "
        "yet. Qt's 'void "
        "QOpcUaConnectionSettings::setConnectTimeout(std::chrono::millisecon"
        "ds timeout)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def setRequestTimeout(*__, **_) -> Never:
    """
    Qt's 'void
    QOpcUaConnectionSettings::setRequestTimeout(std::chrono::milliseconds
    timeout)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QOpcUaConnectionSettings.setRequestTimeout' has no cute function "
        "yet. Qt's 'void "
        "QOpcUaConnectionSettings::setRequestTimeout(std::chrono::millisecon"
        "ds timeout)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def setSecureChannelLifeTime(*__, **_) -> Never:
    """
    Qt's 'void
    QOpcUaConnectionSettings::setSecureChannelLifeTime(std::chrono::
    milliseconds lifeTime)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QOpcUaConnectionSettings.setSecureChannelLifeTime' has no cute "
        "function yet. Qt's 'void "
        "QOpcUaConnectionSettings::setSecureChannelLifeTime(std::chrono::mil"
        "liseconds lifeTime)': takes a type Python has no way to hand over "
        "yet.")

  @staticmethod
  def setSessionTimeout(*__, **_) -> Never:
    """
    Qt's 'void
    QOpcUaConnectionSettings::setSessionTimeout(std::chrono::milliseconds
    timeout)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QOpcUaConnectionSettings.setSessionTimeout' has no cute function "
        "yet. Qt's 'void "
        "QOpcUaConnectionSettings::setSessionTimeout(std::chrono::millisecon"
        "ds timeout)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QOpcUaConnectionSettings::swap(QOpcUaConnectionSettings
    &other)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QOpcUaConnectionSettings.swap' has no cute function yet. Qt's "
        "'void QOpcUaConnectionSettings::swap(QOpcUaConnectionSettings "
        "&other)': takes a type Python has no way to hand over yet.")
