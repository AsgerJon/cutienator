"""
QConfFileSettingsPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qsettings_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QConfFileSettingsPrivate to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QList, QSettingsPrivate, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from . import QConfFile, QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVariant = WAIT['QVariant']


class QConfFileSettingsPrivate(QSettingsPrivate):
  """
  The cute side of Qt's QConfFileSettingsPrivate: a plain Python object
  standing in front of one C++ QConfFileSettingsPrivate.

  It is built on the cute 'QSettingsPrivate', as Qt's
  QConfFileSettingsPrivate is built on Qt's QSettingsPrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QConfFileSettingsPrivate that has a ritual and that
  Python can call so far, 10 names in all: 'remove', 'set', 'children',
  'clear', 'sync', 'flush', 'isWritable', 'fileName', 'getConfFiles',
  'initAccess'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'std::optional<QVariant> QConfFileSettingsPrivate::get(const QString
    &key) const': gives a type Python has no way to take yet.

  What has no ritual
  ------------------

  11 of the 22 functions Qt declares: 5 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 5 leans on
  'QSettingsPrivate; 1 leans on 'QConfFileSettingsPrivate.

  What to expect
  --------------

  - The C++ QConfFileSettingsPrivate is created at the first use, not by
    'QConfFileSettingsPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QConfFileSettingsPrivate.
  - Each name of Qt's QConfFileSettingsPrivate that has no cute function yet,
    '__init__', 'ensureAllSectionsParsed', 'ensureSectionParsed',
    'initFormat', 'readIniFile', 'readIniLine', 'readIniSection',
    'syncConfFile', 'writeIniFile', holds a function that raises
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
  __qt_class__ = 'QConfFileSettingsPrivate'

  #  A C++ QConfFileSettingsPrivate Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QConfFileSettingsPrivate'

  #  The functions Qt calls itself that QConfFileSettingsPrivate is the first
  #  to declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'initAccess': (
          ('_ZN24QConfFileSettingsPrivate10initAccessEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str, QSettingsPrivate.ChildSpec)
  def children(
      self,
      prefix: str,
      spec: QSettingsPrivate.ChildSpec,
  ) -> QStringList:
    """
    Calls Qt's 'QStringList QConfFileSettingsPrivate::children(const QString
    &prefix, ChildSpec spec) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qconffilesettingsprivate.html#children

    Parameters
    ----------

    prefix : str
      Passed on as it is: a QString is made of it for the call.

    spec : QSettingsPrivate.ChildSpec
      Passed on as its number.

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QConfFileSettingsPrivate::children(const QString &prefix,
    #      ChildSpec spec) const
    address = self.uglySide.call(
        'ritual_ZNK24QConfFileSettingsPrivate8childrenERK7QStringN16QSettin'
        'gsPrivate9ChildSpecE',
        prefix, spec.value,
    )
    return QStringList._cuteOwning(address)

  def isWritable(self) -> bool:
    """
    Calls Qt's 'bool QConfFileSettingsPrivate::isWritable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qconffilesettingsprivate.html#isWritable
    """
    #  bool QConfFileSettingsPrivate::isWritable() const
    ritual = 'ritual_ZNK24QConfFileSettingsPrivate10isWritableEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK24QConfFileSettingsPrivate10isWritableEv'
    return self.uglySide.call(ritual)

  def fileName(self) -> str:
    """
    Calls Qt's 'QString QConfFileSettingsPrivate::fileName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qconffilesettingsprivate.html#fileName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QConfFileSettingsPrivate::fileName() const
    ritual = 'ritual_ZNK24QConfFileSettingsPrivate8fileNameEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK24QConfFileSettingsPrivate8fileNameEv'
    return self.uglySide.call(ritual)

  def getConfFiles(self) -> QList[QConfFile]:
    """
    Calls Qt's 'const QList<QConfFile *>
    &QConfFileSettingsPrivate::getConfFiles() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qconffilesettingsprivate.html#getConfFiles

    Returns
    -------

    QList[QConfFile]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  const QList<QConfFile *> &QConfFileSettingsPrivate::getConfFiles()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK24QConfFileSettingsPrivate12getConfFilesEv',
    )
    from . import QConfFile
    return QList[QConfFile]._cuteOwning(address)

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
    - Qt's
      'QConfFileSettingsPrivate::QConfFileSettingsPrivate(QSettings::Format
      format, QSettings::Scope scope, const QString &organization, const
      QString &application)': Qt's library has no name for it, and its code
      in Qt's source does not compile apart from its file: unknown type name
      'Path'.
    - Qt's 'QConfFileSettingsPrivate::QConfFileSettingsPrivate(const QString
      &fileName, QSettings::Format format)': leans on
      'QSettingsPrivate::iniUnescapedStringList(QByteArrayView, QString&,
      QList<QString>&)', which Qt's source does not mark for use from outside
      Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QConfFileSettingsPrivate.__init__' has no cute function yet. Qt's "
        "'QConfFileSettingsPrivate::QConfFileSettingsPrivate(QSettings::Form"
        "at format, QSettings::Scope scope, const QString &organization, "
        "const QString &application)': Qt's library has no name for it, and "
        "its code in Qt's source does not compile apart from its file: "
        "unknown type name 'Path'. Qt's "
        "'QConfFileSettingsPrivate::QConfFileSettingsPrivate(const QString "
        "&fileName, QSettings::Format format)': leans on "
        "'QSettingsPrivate::iniUnescapedStringList(QByteArrayView, "
        "QString&, QList<QString>&)', which Qt's source does not mark for "
        "use from outside Qt and has no code for that could be taken.")

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

  @overload(str)
  def remove(self, key: str) -> None:
    """
    Calls Qt's 'void QConfFileSettingsPrivate::remove(const QString &key)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qconffilesettingsprivate.html#remove

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QConfFileSettingsPrivate::remove(const QString &key)
    self.uglySide.call(
        'ritual_ZN24QConfFileSettingsPrivate6removeERK7QString', key,
    )

  @overload(str, QVariant)
  def set(self, key: str, value: QVariant) -> None:
    """
    Calls Qt's 'void QConfFileSettingsPrivate::set(const QString &key, const
    QVariant &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qconffilesettingsprivate.html#set

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QConfFileSettingsPrivate::set(const QString &key, const QVariant
    #      &value)
    ritual = 'ritual_ZN24QConfFileSettingsPrivate3setERK7QStringRK8QVariant'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QConfFileSettingsPrivate3setERK7QStringRK8QVarian'
          't')
    self.uglySide.call(ritual, key, self._valueOf(value))

  def clear(self) -> None:
    """
    Calls Qt's 'void QConfFileSettingsPrivate::clear()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qconffilesettingsprivate.html#clear
    """
    #  void QConfFileSettingsPrivate::clear()
    self.uglySide.call('ritual_ZN24QConfFileSettingsPrivate5clearEv')

  def sync(self) -> None:
    """
    Calls Qt's 'void QConfFileSettingsPrivate::sync()'.

    Qt's own words: https://doc.qt.io/qt-6/qconffilesettingsprivate.html#sync
    """
    #  void QConfFileSettingsPrivate::sync()
    self.uglySide.call('ritual_ZN24QConfFileSettingsPrivate4syncEv')

  def flush(self) -> None:
    """
    Calls Qt's 'void QConfFileSettingsPrivate::flush()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qconffilesettingsprivate.html#flush
    """
    #  void QConfFileSettingsPrivate::flush()
    ritual = 'ritual_ZN24QConfFileSettingsPrivate5flushEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN24QConfFileSettingsPrivate5flushEv'
    self.uglySide.call(ritual)

  def initAccess(self) -> None:
    """
    Calls Qt's 'void QConfFileSettingsPrivate::initAccess()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qconffilesettingsprivate.html#initAccess
    """
    #  void QConfFileSettingsPrivate::initAccess()
    ritual = 'ritual_ZN24QConfFileSettingsPrivate10initAccessEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN24QConfFileSettingsPrivate10initAccessEv'
    self.uglySide.call(ritual)

  @staticmethod
  def ensureAllSectionsParsed(*__, **_) -> Never:
    """
    Qt's 'void QConfFileSettingsPrivate::ensureAllSectionsParsed(QConfFile
    *confFile) const': leans on
    'QSettingsPrivate::iniUnescapedStringList(QByteArrayView, QString&,
    QList<QString>&)', which Qt's source does not mark for use from outside
    Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QConfFileSettingsPrivate.ensureAllSectionsParsed' has no cute "
        "function yet. Qt's 'void "
        "QConfFileSettingsPrivate::ensureAllSectionsParsed(QConfFile "
        "*confFile) const': leans on "
        "'QSettingsPrivate::iniUnescapedStringList(QByteArrayView, "
        "QString&, QList<QString>&)', which Qt's source does not mark for "
        "use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def ensureSectionParsed(*__, **_) -> Never:
    """
    Qt's 'void QConfFileSettingsPrivate::ensureSectionParsed(QConfFile
    *confFile, const QSettingsKey &key) const': leans on
    'QSettingsPrivate::iniUnescapedStringList(QByteArrayView, QString&,
    QList<QString>&)', which Qt's source does not mark for use from outside
    Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QConfFileSettingsPrivate.ensureSectionParsed' has no cute "
        "function yet. Qt's 'void "
        "QConfFileSettingsPrivate::ensureSectionParsed(QConfFile *confFile, "
        "const QSettingsKey &key) const': leans on "
        "'QSettingsPrivate::iniUnescapedStringList(QByteArrayView, "
        "QString&, QList<QString>&)', which Qt's source does not mark for "
        "use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def initFormat(*__, **_) -> Never:
    """
    Qt's 'void QConfFileSettingsPrivate::initFormat()': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: use of undeclared identifier 'settingsGlobalMutex'.
    """
    raise NotImplementedError(
        "'QConfFileSettingsPrivate.initFormat' has no cute function yet. "
        "Qt's 'void QConfFileSettingsPrivate::initFormat()': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier "
        "'settingsGlobalMutex'.")

  @staticmethod
  def readIniFile(*__, **_) -> Never:
    """
    Qt's 'bool QConfFileSettingsPrivate::readIniFile(QByteArrayView data,
    UnparsedSettingsMap *unparsedIniSections)': leans on
    'QConfFileSettingsPrivate::readIniLine(QByteArrayView, long long&, long
    long&, long long&, long long&)', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QConfFileSettingsPrivate.readIniFile' has no cute function yet. "
        "Qt's 'bool QConfFileSettingsPrivate::readIniFile(QByteArrayView "
        "data, UnparsedSettingsMap *unparsedIniSections)': leans on "
        "'QConfFileSettingsPrivate::readIniLine(QByteArrayView, long long&, "
        "long long&, long long&, long long&)', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def readIniLine(*__, **_) -> Never:
    """
    Qt's 'bool QConfFileSettingsPrivate::readIniLine(QByteArrayView data,
    qsizetype &dataPos, qsizetype &lineStart, qsizetype &lineLen, qsizetype
    &equalsPos)': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: use of undeclared identifier
    'SettingsImpl'; did you mean 'QSettings::SettingsMap'?.
    """
    raise NotImplementedError(
        "'QConfFileSettingsPrivate.readIniLine' has no cute function yet. "
        "Qt's 'bool QConfFileSettingsPrivate::readIniLine(QByteArrayView "
        "data, qsizetype &dataPos, qsizetype &lineStart, qsizetype "
        "&lineLen, qsizetype &equalsPos)': Qt's library has no name for it, "
        "and its code in Qt's source does not compile apart from its file: "
        "use of undeclared identifier 'SettingsImpl'; did you mean "
        "'QSettings::SettingsMap'?.")

  @staticmethod
  def readIniSection(*__, **_) -> Never:
    """
    Qt's 'bool QConfFileSettingsPrivate::readIniSection(const QSettingsKey
    &section, QByteArrayView data, ParsedSettingsMap *settingsMap)': leans on
    'QSettingsPrivate::iniUnescapedStringList(QByteArrayView, QString&,
    QList<QString>&)', which Qt's source does not mark for use from outside
    Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QConfFileSettingsPrivate.readIniSection' has no cute function "
        "yet. Qt's 'bool QConfFileSettingsPrivate::readIniSection(const "
        "QSettingsKey &section, QByteArrayView data, ParsedSettingsMap "
        "*settingsMap)': leans on "
        "'QSettingsPrivate::iniUnescapedStringList(QByteArrayView, "
        "QString&, QList<QString>&)', which Qt's source does not mark for "
        "use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def syncConfFile(*__, **_) -> Never:
    """
    Qt's 'void QConfFileSettingsPrivate::syncConfFile(QConfFile *confFile)':
    leans on 'QSettingsPrivate::iniUnescapedStringList(QByteArrayView,
    QString&, QList<QString>&)', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QConfFileSettingsPrivate.syncConfFile' has no cute function yet. "
        "Qt's 'void QConfFileSettingsPrivate::syncConfFile(QConfFile "
        "*confFile)': leans on "
        "'QSettingsPrivate::iniUnescapedStringList(QByteArrayView, "
        "QString&, QList<QString>&)', which Qt's source does not mark for "
        "use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def writeIniFile(*__, **_) -> Never:
    """
    Qt's 'bool QConfFileSettingsPrivate::writeIniFile(QIODevice &device,
    const ParsedSettingsMap &map)': Qt's library has no name for it, and its
    code in Qt's source does not compile apart from its file: unknown type
    name 'IniMap'.
    """
    raise NotImplementedError(
        "'QConfFileSettingsPrivate.writeIniFile' has no cute function yet. "
        "Qt's 'bool QConfFileSettingsPrivate::writeIniFile(QIODevice "
        "&device, const ParsedSettingsMap &map)': Qt's library has no name "
        "for it, and its code in Qt's source does not compile apart from "
        "its file: unknown type name 'IniMap'.")
