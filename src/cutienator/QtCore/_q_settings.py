"""
QSettings binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qsettings.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from . import QObject, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QEvent, QMetaObject, QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSettings(QObject):
  """
  The cute side of Qt's QSettings: a plain Python object standing in front of
  one C++ QSettings.

  It is built on the cute 'QObject', as Qt's QSettings is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSettings that has a ritual and that Python can call
  so far, 33 names in all: 'metaObject', 'tr', 'clear', 'sync', 'status',
  'isAtomicSyncRequired', 'setAtomicSyncRequired', 'beginGroup', 'endGroup',
  'group', 'beginReadArray', 'beginWriteArray', 'endArray', 'setArrayIndex',
  'allKeys', 'childKeys', 'childGroups', 'isWritable', 'setValue', 'value',
  'remove', 'contains', 'setFallbacksEnabled', 'fallbacksEnabled',
  'fileName', 'format', 'scope', 'organizationName', 'applicationName',
  'setDefaultFormat', 'defaultFormat', 'setPath', 'event'. It can be made
  from Python, in 6 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSettings::~QSettings()': the destructor: Python never removes a
    C++ QSettings.

  What has no ritual
  ------------------

  9 of the 50 functions Qt declares: 3 takes or gives a type that cannot be
  passed yet; 3 private; 2 forbidden; 1 a template.

  What to expect
  --------------

  - The C++ QSettings is created at the first use, not by 'QSettings(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSettings.
  - Qt tells when it has removed the C++ QSettings. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  #  The enums Qt writes inside QSettings, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class Format(CuteNum):
    """
    The enum 'QSettings::Format' of Qt, with the 19 names Qt gives in it.
    """

    NativeFormat = Kee[int](0)
    IniFormat = Kee[int](1)
    InvalidFormat = Kee[int](16)
    CustomFormat1 = Kee[int](17)
    CustomFormat2 = Kee[int](18)
    CustomFormat3 = Kee[int](19)
    CustomFormat4 = Kee[int](20)
    CustomFormat5 = Kee[int](21)
    CustomFormat6 = Kee[int](22)
    CustomFormat7 = Kee[int](23)
    CustomFormat8 = Kee[int](24)
    CustomFormat9 = Kee[int](25)
    CustomFormat10 = Kee[int](26)
    CustomFormat11 = Kee[int](27)
    CustomFormat12 = Kee[int](28)
    CustomFormat13 = Kee[int](29)
    CustomFormat14 = Kee[int](30)
    CustomFormat15 = Kee[int](31)
    CustomFormat16 = Kee[int](32)

  class Scope(CuteNum):
    """The enum 'QSettings::Scope' of Qt, with the 2 names Qt gives in it."""

    UserScope = Kee[int](0)
    SystemScope = Kee[int](1)

  class Status(CuteNum):
    """
    The enum 'QSettings::Status' of Qt, with the 3 names Qt gives in it.
    """

    NoError = Kee[int](0)
    AccessError = Kee[int](1)
    FormatError = Kee[int](2)

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
    Calls Qt's 'QString QSettings::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qsettings.html#tr

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
    #  QString QSettings::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN9QSettings2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(Format)
  def setDefaultFormat(format: Format) -> None:
    """
    Calls Qt's 'void QSettings::setDefaultFormat(Format format)'.

    Qt's own words: https://doc.qt.io/qt-6/qsettings.html#setDefaultFormat

    Parameters
    ----------

    format : Format
      Passed on as its number.
    """
    #  void QSettings::setDefaultFormat(Format format)
    Rituals.call(
        'ritual_ZN9QSettings16setDefaultFormatENS_6FormatE', format.value,
    )

  @staticmethod
  def defaultFormat() -> Format:
    """
    Calls Qt's 'Format QSettings::defaultFormat()'.

    Qt's own words: https://doc.qt.io/qt-6/qsettings.html#defaultFormat

    Returns
    -------

    Format
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Format(number)' gives.
    """
    #  Format QSettings::defaultFormat()
    return QSettings.Format(Rituals.call(
        'ritual_ZN9QSettings13defaultFormatEv',
    ))

  @staticmethod
  @overload(Format, Scope, str)
  def setPath(format: Format, scope: Scope, path: str) -> None:
    """
    Calls Qt's 'void QSettings::setPath(Format format, Scope scope, const
    QString &path)'.

    Qt's own words: https://doc.qt.io/qt-6/qsettings.html#setPath

    Parameters
    ----------

    format : Format
      Passed on as its number.

    scope : Scope
      Passed on as its number.

    path : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QSettings::setPath(Format format, Scope scope, const QString
    #      &path)
    Rituals.call(
        'ritual_ZN9QSettings7setPathENS_6FormatENS_5ScopeERK7QString',
        format.value, scope.value, path,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSettings'

  #  A C++ QSettings Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSettings'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QSettings::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsettings.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QSettings::metaObject() const
    address = self.uglySide.call('ritual_ZNK9QSettings10metaObjectEv')
    from . import QMetaObject
    return QMetaObject._cuteAt(address)

  def status(self) -> Status:
    """
    Calls Qt's 'Status QSettings::status() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsettings.html#status

    Returns
    -------

    Status
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Status(number)' gives.
    """
    #  Status QSettings::status() const
    return QSettings.Status(self.uglySide.call(
        'ritual_ZNK9QSettings6statusEv',
    ))

  def isAtomicSyncRequired(self) -> bool:
    """
    Calls Qt's 'bool QSettings::isAtomicSyncRequired() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsettings.html#isAtomicSyncRequired
    """
    #  bool QSettings::isAtomicSyncRequired() const
    return self.uglySide.call('ritual_ZNK9QSettings20isAtomicSyncRequiredEv')

  def group(self) -> str:
    """
    Calls Qt's 'QString QSettings::group() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsettings.html#group

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSettings::group() const
    return self.uglySide.call('ritual_ZNK9QSettings5groupEv')

  def allKeys(self) -> QStringList:
    """
    Calls Qt's 'QStringList QSettings::allKeys() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsettings.html#allKeys

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QSettings::allKeys() const
    address = self.uglySide.call('ritual_ZNK9QSettings7allKeysEv')
    return QStringList._cuteOwning(address)

  def childKeys(self) -> QStringList:
    """
    Calls Qt's 'QStringList QSettings::childKeys() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsettings.html#childKeys

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QSettings::childKeys() const
    address = self.uglySide.call('ritual_ZNK9QSettings9childKeysEv')
    return QStringList._cuteOwning(address)

  def childGroups(self) -> QStringList:
    """
    Calls Qt's 'QStringList QSettings::childGroups() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsettings.html#childGroups

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QSettings::childGroups() const
    address = self.uglySide.call('ritual_ZNK9QSettings11childGroupsEv')
    return QStringList._cuteOwning(address)

  def isWritable(self) -> bool:
    """
    Calls Qt's 'bool QSettings::isWritable() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsettings.html#isWritable
    """
    #  bool QSettings::isWritable() const
    return self.uglySide.call('ritual_ZNK9QSettings10isWritableEv')

  @overload(str, QVariant)
  def value(self, key: str, defaultValue: QVariant) -> QVariant:
    """
    Calls Qt's 'QVariant QSettings::value(QAnyStringView key, const QVariant
    &defaultValue) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsettings.html#value

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.

    defaultValue : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QSettings::value(QAnyStringView key, const QVariant
    #      &defaultValue) const
    address = self.uglySide.call(
        'ritual_ZNK9QSettings5valueE14QAnyStringViewRK8QVariant',
        key, self._valueOf(defaultValue),
    )
    from . import QVariant
    return QVariant._cuteOwning(address)

  @overload(str)
  def value(self, key: str) -> QVariant:
    """
    Calls Qt's 'QVariant QSettings::value(QAnyStringView key) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsettings.html#value

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QSettings::value(QAnyStringView key) const
    address = self.uglySide.call(
        'ritual_ZNK9QSettings5valueE14QAnyStringView', key,
    )
    from . import QVariant
    return QVariant._cuteOwning(address)

  @overload(str)
  def contains(self, key: str) -> bool:
    """
    Calls Qt's 'bool QSettings::contains(QAnyStringView key) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsettings.html#contains

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QSettings::contains(QAnyStringView key) const
    return self.uglySide.call(
        'ritual_ZNK9QSettings8containsE14QAnyStringView', key,
    )

  def fallbacksEnabled(self) -> bool:
    """
    Calls Qt's 'bool QSettings::fallbacksEnabled() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsettings.html#fallbacksEnabled
    """
    #  bool QSettings::fallbacksEnabled() const
    return self.uglySide.call('ritual_ZNK9QSettings16fallbacksEnabledEv')

  def fileName(self) -> str:
    """
    Calls Qt's 'QString QSettings::fileName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsettings.html#fileName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSettings::fileName() const
    return self.uglySide.call('ritual_ZNK9QSettings8fileNameEv')

  def format(self) -> Format:
    """
    Calls Qt's 'Format QSettings::format() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsettings.html#format

    Returns
    -------

    Format
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Format(number)' gives.
    """
    #  Format QSettings::format() const
    return QSettings.Format(self.uglySide.call(
        'ritual_ZNK9QSettings6formatEv',
    ))

  def scope(self) -> Scope:
    """
    Calls Qt's 'Scope QSettings::scope() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsettings.html#scope

    Returns
    -------

    Scope
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Scope(number)' gives.
    """
    #  Scope QSettings::scope() const
    return QSettings.Scope(self.uglySide.call(
        'ritual_ZNK9QSettings5scopeEv',
    ))

  def organizationName(self) -> str:
    """
    Calls Qt's 'QString QSettings::organizationName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsettings.html#organizationName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSettings::organizationName() const
    return self.uglySide.call('ritual_ZNK9QSettings16organizationNameEv')

  def applicationName(self) -> str:
    """
    Calls Qt's 'QString QSettings::applicationName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsettings.html#applicationName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSettings::applicationName() const
    return self.uglySide.call('ritual_ZNK9QSettings15applicationNameEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setAtomicSyncRequired(self, enable: bool) -> None:
    """
    Calls Qt's 'void QSettings::setAtomicSyncRequired(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsettings.html#setAtomicSyncRequired

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QSettings::setAtomicSyncRequired(bool enable)
    self.uglySide.call(
        'ritual_ZN9QSettings21setAtomicSyncRequiredEb', enable,
    )

  @overload(int)
  def setArrayIndex(self, i: int) -> None:
    """
    Calls Qt's 'void QSettings::setArrayIndex(int i)'.

    Qt's own words: https://doc.qt.io/qt-6/qsettings.html#setArrayIndex

    Parameters
    ----------

    i : int
      Passed on as it is.
    """
    #  void QSettings::setArrayIndex(int i)
    self.uglySide.call('ritual_ZN9QSettings13setArrayIndexEi', i)

  @overload(str, QVariant)
  def setValue(self, key: str, value: QVariant) -> None:
    """
    Calls Qt's 'void QSettings::setValue(QAnyStringView key, const QVariant
    &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qsettings.html#setValue

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QSettings::setValue(QAnyStringView key, const QVariant &value)
    self.uglySide.call(
        'ritual_ZN9QSettings8setValueE14QAnyStringViewRK8QVariant',
        key, self._valueOf(value),
    )

  @overload(bool)
  def setFallbacksEnabled(self, b: bool) -> None:
    """
    Calls Qt's 'void QSettings::setFallbacksEnabled(bool b)'.

    Qt's own words: https://doc.qt.io/qt-6/qsettings.html#setFallbacksEnabled

    Parameters
    ----------

    b : bool
      Passed on as it is.
    """
    #  void QSettings::setFallbacksEnabled(bool b)
    self.uglySide.call('ritual_ZN9QSettings19setFallbacksEnabledEb', b)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  @overload(str, str)
  @overload(str, str, QObject)
  @overload(str, str, NoneType)
  def __init__(
      self,
      organization: str,
      application: str = '',
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QSettings::QSettings(const QString
    &organization, const QString &application, QObject *parent)', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsettings.html#QSettings

    Parameters
    ----------

    organization : str
      Passed on as it is: a QString is made of it for the call.

    application : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QSettings::QSettings(const QString &organization, const QString
    #      &application, QObject *parent)
    self._noteCreation(QSettings, lambda: Rituals.call(
        'ritual_ZN9QSettingsC1ERK7QStringS2_P7QObject',
        organization, application, self._addressOf(parent),
    ))

  @overload(Scope, str)
  @overload(Scope, str, str)
  @overload(Scope, str, str, QObject)
  @overload(Scope, str, str, NoneType)
  def __init__(
      self,
      scope: Scope,
      organization: str,
      application: str = '',
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QSettings::QSettings(Scope scope, const
    QString &organization, const QString &application, QObject *parent)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsettings.html#QSettings

    Parameters
    ----------

    scope : Scope
      Passed on as its number.

    organization : str
      Passed on as it is: a QString is made of it for the call.

    application : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QSettings::QSettings(Scope scope, const QString &organization, const
    #      QString &application, QObject *parent)
    self._noteCreation(QSettings, lambda: Rituals.call(
        'ritual_ZN9QSettingsC1ENS_5ScopeERK7QStringS3_P7QObject',
        scope.value, organization, application, self._addressOf(parent),
    ))

  @overload(Format, Scope, str)
  @overload(Format, Scope, str, str)
  @overload(Format, Scope, str, str, QObject)
  @overload(Format, Scope, str, str, NoneType)
  def __init__(
      self,
      format: Format,
      scope: Scope,
      organization: str,
      application: str = '',
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QSettings::QSettings(Format format, Scope
    scope, const QString &organization, const QString &application, QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsettings.html#QSettings

    Parameters
    ----------

    format : Format
      Passed on as its number.

    scope : Scope
      Passed on as its number.

    organization : str
      Passed on as it is: a QString is made of it for the call.

    application : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QSettings::QSettings(Format format, Scope scope, const QString
    #      &organization, const QString &application, QObject *parent)
    self._noteCreation(QSettings, lambda: Rituals.call(
        'ritual_ZN9QSettingsC1ENS_6FormatENS_5ScopeERK7QStringS4_P7QObject',
        format.value, scope.value, organization, application,
        self._addressOf(parent),
    ))

  @overload(str, Format)
  @overload(str, Format, QObject)
  @overload(str, Format, NoneType)
  def __init__(
      self,
      fileName: str,
      format: Format,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QSettings::QSettings(const QString
    &fileName, Format format, QObject *parent)', which is called at the first
    use.

    Qt's own words: https://doc.qt.io/qt-6/qsettings.html#QSettings

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.

    format : Format
      Passed on as its number.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QSettings::QSettings(const QString &fileName, Format format, QObject
    #      *parent)
    self._noteCreation(QSettings, lambda: Rituals.call(
        'ritual_ZN9QSettingsC1ERK7QStringNS_6FormatEP7QObject',
        fileName, format.value, self._addressOf(parent),
    ))

  @overload()
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's 'QSettings::QSettings(QObject *parent)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsettings.html#QSettings

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QSettings::QSettings(QObject *parent)
    self._noteCreation(QSettings, lambda: Rituals.call(
        'ritual_ZN9QSettingsC1EP7QObject', self._addressOf(parent),
    ))

  @overload(Scope)
  @overload(Scope, QObject)
  @overload(Scope, NoneType)
  def __init__(self, scope: Scope, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's 'QSettings::QSettings(Scope scope, QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsettings.html#QSettings

    Parameters
    ----------

    scope : Scope
      Passed on as its number.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QSettings::QSettings(Scope scope, QObject *parent)
    self._noteCreation(QSettings, lambda: Rituals.call(
        'ritual_ZN9QSettingsC1ENS_5ScopeEP7QObject',
        scope.value, self._addressOf(parent),
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

  def clear(self) -> None:
    """
    Calls Qt's 'void QSettings::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qsettings.html#clear
    """
    #  void QSettings::clear()
    self.uglySide.call('ritual_ZN9QSettings5clearEv')

  def sync(self) -> None:
    """
    Calls Qt's 'void QSettings::sync()'.

    Qt's own words: https://doc.qt.io/qt-6/qsettings.html#sync
    """
    #  void QSettings::sync()
    self.uglySide.call('ritual_ZN9QSettings4syncEv')

  @overload(str)
  def beginGroup(self, prefix: str) -> None:
    """
    Calls Qt's 'void QSettings::beginGroup(QAnyStringView prefix)'.

    Qt's own words: https://doc.qt.io/qt-6/qsettings.html#beginGroup

    Parameters
    ----------

    prefix : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QSettings::beginGroup(QAnyStringView prefix)
    self.uglySide.call(
        'ritual_ZN9QSettings10beginGroupE14QAnyStringView', prefix,
    )

  def endGroup(self) -> None:
    """
    Calls Qt's 'void QSettings::endGroup()'.

    Qt's own words: https://doc.qt.io/qt-6/qsettings.html#endGroup
    """
    #  void QSettings::endGroup()
    self.uglySide.call('ritual_ZN9QSettings8endGroupEv')

  @overload(str)
  def beginReadArray(self, prefix: str) -> int:
    """
    Calls Qt's 'int QSettings::beginReadArray(QAnyStringView prefix)'.

    Qt's own words: https://doc.qt.io/qt-6/qsettings.html#beginReadArray

    Parameters
    ----------

    prefix : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  int QSettings::beginReadArray(QAnyStringView prefix)
    return self.uglySide.call(
        'ritual_ZN9QSettings14beginReadArrayE14QAnyStringView', prefix,
    )

  @overload(str)
  @overload(str, int)
  def beginWriteArray(self, prefix: str, size: int = -1) -> None:
    """
    Calls Qt's 'void QSettings::beginWriteArray(QAnyStringView prefix, int
    size)'.

    Qt's own words: https://doc.qt.io/qt-6/qsettings.html#beginWriteArray

    Parameters
    ----------

    prefix : str
      Passed on as it is: a QString is made of it for the call.

    size : int
      Passed on as it is. May be left out, as in Qt: it is then -1.
    """
    #  void QSettings::beginWriteArray(QAnyStringView prefix, int size)
    self.uglySide.call(
        'ritual_ZN9QSettings15beginWriteArrayE14QAnyStringViewi',
        prefix, size,
    )

  def endArray(self) -> None:
    """
    Calls Qt's 'void QSettings::endArray()'.

    Qt's own words: https://doc.qt.io/qt-6/qsettings.html#endArray
    """
    #  void QSettings::endArray()
    self.uglySide.call('ritual_ZN9QSettings8endArrayEv')

  @overload(str)
  def remove(self, key: str) -> None:
    """
    Calls Qt's 'void QSettings::remove(QAnyStringView key)'.

    Qt's own words: https://doc.qt.io/qt-6/qsettings.html#remove

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QSettings::remove(QAnyStringView key)
    self.uglySide.call('ritual_ZN9QSettings6removeE14QAnyStringView', key)

  @overload(QEvent)
  @overload(NoneType)
  def event(self, event: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QSettings::event(QEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qsettings.html#event

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QSettings::event(QEvent *event)
    return self.uglySide.call(
        'ritual_own_ZN9QSettings5eventEP6QEvent', self._addressOf(event),
    )
