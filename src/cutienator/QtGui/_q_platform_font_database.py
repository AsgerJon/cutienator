"""
QPlatformFontDatabase binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/qpa/qplatformfontdatabase.h, Qt 6.12.0. Changes made
#  here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QStringList
from . import QFont, QFontDatabasePrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray
  from . import QFontEngine, QFontEngineMulti, QSupportedWritingSystems
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QFontEngine = WAIT['QFontEngine']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPlatformFontDatabase(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QPlatformFontDatabase: a plain Python object standing
  in front of one C++ QPlatformFontDatabase.

  C++ hands a QPlatformFontDatabase around as a copy, so every C++
  QPlatformFontDatabase behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QPlatformFontDatabase that has a ritual and that
  Python can call so far, 20 names in all: 'populateFontDatabase',
  'populateFamilyAliases', 'populateFamily', 'invalidate',
  'fallbacksForFamily', 'addApplicationFont', 'fontEngine',
  'fontEngineMulti', 'fontDir', 'defaultFont', 'isPrivateFontFamily',
  'resolveFontFamilyAlias', 'fontsAlwaysScalable',
  'supportsVariableApplicationFonts', 'supportsColrv0Fonts',
  'writingSystemsFromOS2Table', 'registerFontFamily',
  'registerAliasToFontFamily', 'repopulateFontDatabase', 'isFamilyPopulated'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPlatformFontDatabase::~QPlatformFontDatabase()': the destructor:
    Python removes its C++ QPlatformFontDatabase by it, and has no other use
    for it.
  - Qt's 'QFontEngine *QPlatformFontDatabase::fontEngine(const QFontDef
    &fontDef, void *handle)': names 'void', which has no cute class yet.
  - Qt's 'void QPlatformFontDatabase::releaseHandle(void *handle)': names
    'void', which has no cute class yet.
  - Qt's 'QList<int> QPlatformFontDatabase::standardSizes() const': gives a
    type Python has no way to take yet.
  - Qt's 'QSupportedWritingSystems
    QPlatformFontDatabase::writingSystemsFromTrueTypeBits(quint32
    *unicodeRange, quint32 *codePageRange)': takes a number to change where
    it is.
  - Qt's 'void QPlatformFontDatabase::registerFont(const QString &familyname,
    const QString &stylename, const QString &foundryname, QFont::Weight
    weight, QFont::Style style, QFont::Stretch stretch, bool antialiased,
    bool scalable, int pixelSize, bool fixedPitch, bool colorFont, const
    QSupportedWritingSystems &writingSystems, void *handle)': names 'void',
    which has no cute class yet.

  What to expect
  --------------

  - The C++ QPlatformFontDatabase is created at the first use, not by
    'QPlatformFontDatabase(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QPlatformFontDatabase back gives a copy the ritual
    made for Python, in a new cute QPlatformFontDatabase.
  - Each name of Qt's QPlatformFontDatabase that has no cute function yet,
    'registerFont', 'releaseHandle', 'standardSizes',
    'writingSystemsFromTrueTypeBits', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str, int)
  @overload(NoneType, int)
  def writingSystemsFromOS2Table(
      os2Table: Optional[str],
      length: int,
  ) -> QSupportedWritingSystems:
    """
    Calls Qt's 'QSupportedWritingSystems
    QPlatformFontDatabase::writingSystemsFromOS2Table(const char *os2Table,
    size_t length)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformfontdatabase.html

    Parameters
    ----------

    os2Table : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    length : int
      Passed on as it is.

    Returns
    -------

    QSupportedWritingSystems
      A new cute QSupportedWritingSystems around the copy Qt gave back.
      Python owns it.
    """
    #  QSupportedWritingSystems
    #      QPlatformFontDatabase::writingSystemsFromOS2Table(const char
    #      *os2Table, size_t length)
    address = Rituals.call(
        'ritual_ZN21QPlatformFontDatabase26writingSystemsFromOS2TableEPKcm',
        CuteMixin._bytesOf(os2Table), length,
    )
    from . import QSupportedWritingSystems
    return QSupportedWritingSystems._cuteOwning(address)

  @staticmethod
  @overload(str)
  def registerFontFamily(familyName: str) -> None:
    """
    Calls Qt's 'void QPlatformFontDatabase::registerFontFamily(const QString
    &familyName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformfontdatabase.html#registerFontFamily

    Parameters
    ----------

    familyName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QPlatformFontDatabase::registerFontFamily(const QString
    #      &familyName)
    Rituals.call(
        'ritual_ZN21QPlatformFontDatabase18registerFontFamilyERK7QString',
        familyName,
    )

  @staticmethod
  @overload(str, str)
  def registerAliasToFontFamily(familyName: str, alias: str) -> None:
    """
    Calls Qt's 'void QPlatformFontDatabase::registerAliasToFontFamily(const
    QString &familyName, const QString &alias)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformfontdatabase.html

    Parameters
    ----------

    familyName : str
      Passed on as it is: a QString is made of it for the call.

    alias : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QPlatformFontDatabase::registerAliasToFontFamily(const QString
    #      &familyName, const QString &alias)
    Rituals.call(
        'ritual_ZN21QPlatformFontDatabase25registerAliasToFontFamilyERK7QSt'
        'ringS2_',
        familyName, alias,
    )

  @staticmethod
  def repopulateFontDatabase() -> None:
    """
    Calls Qt's 'void QPlatformFontDatabase::repopulateFontDatabase()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformfontdatabase.html#repopulateFontDatabase
    """
    #  void QPlatformFontDatabase::repopulateFontDatabase()
    Rituals.call(
        'ritual_ZN21QPlatformFontDatabase22repopulateFontDatabaseEv',
    )

  @staticmethod
  @overload(str)
  def isFamilyPopulated(familyName: str) -> bool:
    """
    Calls Qt's 'bool QPlatformFontDatabase::isFamilyPopulated(const QString
    &familyName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformfontdatabase.html#isFamilyPopulated

    Parameters
    ----------

    familyName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QPlatformFontDatabase::isFamilyPopulated(const QString
    #      &familyName)
    return Rituals.call(
        'ritual_ZN21QPlatformFontDatabase17isFamilyPopulatedERK7QString',
        familyName,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPlatformFontDatabase'

  #  A C++ QPlatformFontDatabase Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPlatformFontDatabase'

  #  The functions Qt calls itself that QPlatformFontDatabase is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'fallbacksForFamily': (
          'QStringList QPlatformFontDatabase::fallbacksForFamily(const '
          'QString &, QFont::Style, QFont::StyleHint, '
          'QFontDatabasePrivate::ExtendedScript) const',
      ),
      'addApplicationFont': (
          'QStringList QPlatformFontDatabase::addApplicationFont(const '
          'QByteArray &, const QString &, '
          'QFontDatabasePrivate::ApplicationFont *)',
      ),
      'releaseHandle': (
          'void QPlatformFontDatabase::releaseHandle(void *)',
      ),
      'standardSizes': (
          'QList<int> QPlatformFontDatabase::standardSizes() const',
      ),
  }

  #  The functions Qt calls itself that QPlatformFontDatabase is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'populateFontDatabase': (
          ('_ZN21QPlatformFontDatabase20populateFontDatabaseEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'populateFamilyAliases': (
          ('_ZN21QPlatformFontDatabase21populateFamilyAliasesERK7QString',
           ('bool', 'number', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'populateFamily': (
          ('_ZN21QPlatformFontDatabase14populateFamilyERK7QString',
           ('nothing', 'nothing', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'invalidate': (
          ('_ZN21QPlatformFontDatabase10invalidateEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'fontEngine': (
          ('_ZN21QPlatformFontDatabase10fontEngineERK10QByteArraydN5QFont17'
           'HintingPreferenceE',
           ('address', 'address', 'QtGui:QFontEngine'),
           (
               ('address', 'value', 'QtCore:QByteArray'),
               ('double', 'number', ''),
               ('int', 'enum', 'QtGui:QFont.HintingPreference'),
           )),
      ),
      'fontEngineMulti': (
          ('_ZN21QPlatformFontDatabase15fontEngineMultiEP11QFontEngineN20QF'
           'ontDatabasePrivate14ExtendedScriptE',
           ('address', 'address', 'QtGui:QFontEngineMulti'),
           (
               ('address', 'address', 'QtGui:QFontEngine'),
               ('int', 'enum', 'QtGui:QFontDatabasePrivate.ExtendedScript'),
           )),
      ),
      'fontDir': (
          ('_ZNK21QPlatformFontDatabase7fontDirEv',
           ('address', 'text', ''),
           ()),
      ),
      'defaultFont': (
          ('_ZNK21QPlatformFontDatabase11defaultFontEv',
           ('address', 'value', 'QtGui:QFont'),
           ()),
      ),
      'isPrivateFontFamily': (
          ('_ZNK21QPlatformFontDatabase19isPrivateFontFamilyERK7QString',
           ('bool', 'number', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'resolveFontFamilyAlias': (
          ('_ZNK21QPlatformFontDatabase22resolveFontFamilyAliasERK7QString',
           ('address', 'text', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'fontsAlwaysScalable': (
          ('_ZNK21QPlatformFontDatabase19fontsAlwaysScalableEv',
           ('bool', 'number', ''),
           ()),
      ),
      'supportsVariableApplicationFonts': (
          ('_ZNK21QPlatformFontDatabase32supportsVariableApplicationFontsEv',
           ('bool', 'number', ''),
           ()),
      ),
      'supportsColrv0Fonts': (
          ('_ZNK21QPlatformFontDatabase19supportsColrv0FontsEv',
           ('bool', 'number', ''),
           ()),
      ),
  }

  #  Qt's '~QPlatformFontDatabase()'. Naming it makes this a value class:
  #  Python owns every C++ QPlatformFontDatabase behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN21QPlatformFontDatabaseD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(
      str, QFont.Style, QFont.StyleHint, QFontDatabasePrivate.ExtendedScript,
  )
  def fallbacksForFamily(
      self,
      family: str,
      style: QFont.Style,
      styleHint: QFont.StyleHint,
      script: QFontDatabasePrivate.ExtendedScript,
  ) -> QStringList:
    """
    Calls Qt's 'QStringList QPlatformFontDatabase::fallbacksForFamily(const
    QString &family, QFont::Style style, QFont::StyleHint styleHint,
    QFontDatabasePrivate::ExtendedScript script) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformfontdatabase.html#fallbacksForFamily

    Parameters
    ----------

    family : str
      Passed on as it is: a QString is made of it for the call.

    style : QFont.Style
      Passed on as its number.

    styleHint : QFont.StyleHint
      Passed on as its number.

    script : QFontDatabasePrivate.ExtendedScript
      Passed on as its number.

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QPlatformFontDatabase::fallbacksForFamily(const QString
    #      &family, QFont::Style style, QFont::StyleHint styleHint,
    #      QFontDatabasePrivate::ExtendedScript script) const
    address = self.uglySide.call(
        'ritual_ZNK21QPlatformFontDatabase18fallbacksForFamilyERK7QStringN5'
        'QFont5StyleENS3_9StyleHintEN20QFontDatabasePrivate14ExtendedScript'
        'E',
        family, style.value, styleHint.value, script.value,
    )
    return QStringList._cuteOwning(address)

  def fontDir(self) -> str:
    """
    Calls Qt's 'QString QPlatformFontDatabase::fontDir() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformfontdatabase.html#fontDir

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPlatformFontDatabase::fontDir() const
    ritual = 'ritual_ZNK21QPlatformFontDatabase7fontDirEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QPlatformFontDatabase7fontDirEv'
    return self.uglySide.call(ritual)

  def defaultFont(self) -> QFont:
    """
    Calls Qt's 'QFont QPlatformFontDatabase::defaultFont() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformfontdatabase.html#defaultFont

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QPlatformFontDatabase::defaultFont() const
    ritual = 'ritual_ZNK21QPlatformFontDatabase11defaultFontEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QPlatformFontDatabase11defaultFontEv'
    address = self.uglySide.call(ritual)
    return QFont._cuteOwning(address)

  @overload(str)
  def isPrivateFontFamily(self, family: str) -> bool:
    """
    Calls Qt's 'bool QPlatformFontDatabase::isPrivateFontFamily(const QString
    &family) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformfontdatabase.html#isPrivateFontFamily

    Parameters
    ----------

    family : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QPlatformFontDatabase::isPrivateFontFamily(const QString &family)
    #      const
    ritual = (
        'ritual_ZNK21QPlatformFontDatabase19isPrivateFontFamilyERK7QString')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK21QPlatformFontDatabase19isPrivateFontFamilyERK7QS'
          'tring')
    return self.uglySide.call(ritual, family)

  @overload(str)
  def resolveFontFamilyAlias(self, family: str) -> str:
    """
    Calls Qt's 'QString QPlatformFontDatabase::resolveFontFamilyAlias(const
    QString &family) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformfontdatabase.html#resolveFontFamilyAlias

    Parameters
    ----------

    family : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPlatformFontDatabase::resolveFontFamilyAlias(const QString
    #      &family) const
    ritual = (
        'ritual_ZNK21QPlatformFontDatabase22resolveFontFamilyAliasERK7QStri'
        'ng')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK21QPlatformFontDatabase22resolveFontFamilyAliasERK'
          '7QString')
    return self.uglySide.call(ritual, family)

  def fontsAlwaysScalable(self) -> bool:
    """
    Calls Qt's 'bool QPlatformFontDatabase::fontsAlwaysScalable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformfontdatabase.html#fontsAlwaysScalable
    """
    #  bool QPlatformFontDatabase::fontsAlwaysScalable() const
    ritual = 'ritual_ZNK21QPlatformFontDatabase19fontsAlwaysScalableEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QPlatformFontDatabase19fontsAlwaysScalableEv'
    return self.uglySide.call(ritual)

  def supportsVariableApplicationFonts(self) -> bool:
    """
    Calls Qt's 'bool
    QPlatformFontDatabase::supportsVariableApplicationFonts() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformfontdatabase.html
    """
    #  bool QPlatformFontDatabase::supportsVariableApplicationFonts() const
    ritual = (
        'ritual_ZNK21QPlatformFontDatabase32supportsVariableApplicationFont'
        'sEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK21QPlatformFontDatabase32supportsVariableApplicati'
          'onFontsEv')
    return self.uglySide.call(ritual)

  def supportsColrv0Fonts(self) -> bool:
    """
    Calls Qt's 'bool QPlatformFontDatabase::supportsColrv0Fonts() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformfontdatabase.html#supportsColrv0Fonts
    """
    #  bool QPlatformFontDatabase::supportsColrv0Fonts() const
    ritual = 'ritual_ZNK21QPlatformFontDatabase19supportsColrv0FontsEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QPlatformFontDatabase19supportsColrv0FontsEv'
    return self.uglySide.call(ritual)

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

  def populateFontDatabase(self) -> None:
    """
    Calls Qt's 'void QPlatformFontDatabase::populateFontDatabase()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformfontdatabase.html#populateFontDatabase
    """
    #  void QPlatformFontDatabase::populateFontDatabase()
    ritual = 'ritual_ZN21QPlatformFontDatabase20populateFontDatabaseEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QPlatformFontDatabase20populateFontDatabaseEv'
    self.uglySide.call(ritual)

  @overload(str)
  def populateFamilyAliases(self, missingFamily: str) -> bool:
    """
    Calls Qt's 'bool QPlatformFontDatabase::populateFamilyAliases(const
    QString &missingFamily)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformfontdatabase.html#populateFamilyAliases

    Parameters
    ----------

    missingFamily : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QPlatformFontDatabase::populateFamilyAliases(const QString
    #      &missingFamily)
    ritual = (
        'ritual_ZN21QPlatformFontDatabase21populateFamilyAliasesERK7QString')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QPlatformFontDatabase21populateFamilyAliasesERK7Q'
          'String')
    return self.uglySide.call(ritual, missingFamily)

  @overload(str)
  def populateFamily(self, familyName: str) -> None:
    """
    Calls Qt's 'void QPlatformFontDatabase::populateFamily(const QString
    &familyName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformfontdatabase.html#populateFamily

    Parameters
    ----------

    familyName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QPlatformFontDatabase::populateFamily(const QString &familyName)
    ritual = 'ritual_ZN21QPlatformFontDatabase14populateFamilyERK7QString'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QPlatformFontDatabase14populateFamilyERK7QString')
    self.uglySide.call(ritual, familyName)

  def invalidate(self) -> None:
    """
    Calls Qt's 'void QPlatformFontDatabase::invalidate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformfontdatabase.html#invalidate
    """
    #  void QPlatformFontDatabase::invalidate()
    ritual = 'ritual_ZN21QPlatformFontDatabase10invalidateEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QPlatformFontDatabase10invalidateEv'
    self.uglySide.call(ritual)

  @overload(QByteArray, str)
  @overload(QByteArray, str, QFontDatabasePrivate.ApplicationFont)
  @overload(QByteArray, str, NoneType)
  def addApplicationFont(
      self,
      fontData: QByteArray,
      fileName: str,
      font: Optional[QFontDatabasePrivate.ApplicationFont] = None,
  ) -> QStringList:
    """
    Calls Qt's 'QStringList QPlatformFontDatabase::addApplicationFont(const
    QByteArray &fontData, const QString &fileName,
    QFontDatabasePrivate::ApplicationFont *font)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformfontdatabase.html#addApplicationFont

    Parameters
    ----------

    fontData : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    fileName : str
      Passed on as it is: a QString is made of it for the call.

    font : Optional[QFontDatabasePrivate.ApplicationFont]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QPlatformFontDatabase::addApplicationFont(const QByteArray
    #      &fontData, const QString &fileName,
    #      QFontDatabasePrivate::ApplicationFont *font)
    address = self.uglySide.call(
        'ritual_ZN21QPlatformFontDatabase18addApplicationFontERK10QByteArra'
        'yRK7QStringPN20QFontDatabasePrivate15ApplicationFontE',
        self._valueOf(fontData), fileName, self._addressOf(font),
    )
    return QStringList._cuteOwning(address)

  @overload(QByteArray, float, QFont.HintingPreference)
  def fontEngine(
      self,
      fontData: QByteArray,
      pixelSize: float,
      hintingPreference: QFont.HintingPreference,
  ) -> Optional[QFontEngine]:
    """
    Calls Qt's 'QFontEngine *QPlatformFontDatabase::fontEngine(const
    QByteArray &fontData, qreal pixelSize, QFont::HintingPreference
    hintingPreference)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformfontdatabase.html#fontEngine

    Parameters
    ----------

    fontData : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    pixelSize : float
      Passed on as it is.

    hintingPreference : QFont.HintingPreference
      Passed on as its number.

    Returns
    -------

    Optional[QFontEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QFontEngine *QPlatformFontDatabase::fontEngine(const QByteArray
    #      &fontData, qreal pixelSize, QFont::HintingPreference
    #      hintingPreference)
    ritual = (
        'ritual_ZN21QPlatformFontDatabase10fontEngineERK10QByteArraydN5QFon'
        't17HintingPreferenceE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QPlatformFontDatabase10fontEngineERK10QByteArrayd'
          'N5QFont17HintingPreferenceE')
    address = self.uglySide.call(
        ritual, self._valueOf(fontData), pixelSize, hintingPreference.value,
    )
    from . import QFontEngine
    return QFontEngine._cuteAt(address)

  @overload(QFontEngine, QFontDatabasePrivate.ExtendedScript)
  @overload(NoneType, QFontDatabasePrivate.ExtendedScript)
  def fontEngineMulti(
      self,
      fontEngine: Optional[QFontEngine],
      script: QFontDatabasePrivate.ExtendedScript,
  ) -> Optional[QFontEngineMulti]:
    """
    Calls Qt's 'QFontEngineMulti
    *QPlatformFontDatabase::fontEngineMulti(QFontEngine *fontEngine,
    QFontDatabasePrivate::ExtendedScript script)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformfontdatabase.html#fontEngineMulti

    Parameters
    ----------

    fontEngine : Optional[QFontEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    script : QFontDatabasePrivate.ExtendedScript
      Passed on as its number.

    Returns
    -------

    Optional[QFontEngineMulti]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QFontEngineMulti *QPlatformFontDatabase::fontEngineMulti(QFontEngine
    #      *fontEngine, QFontDatabasePrivate::ExtendedScript script)
    ritual = (
        'ritual_ZN21QPlatformFontDatabase15fontEngineMultiEP11QFontEngineN2'
        '0QFontDatabasePrivate14ExtendedScriptE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QPlatformFontDatabase15fontEngineMultiEP11QFontEn'
          'gineN20QFontDatabasePrivate14ExtendedScriptE')
    address = self.uglySide.call(
        ritual, self._addressOf(fontEngine), script.value,
    )
    from . import QFontEngineMulti
    return QFontEngineMulti._cuteAt(address)

  @staticmethod
  def registerFont(*__, **_) -> Never:
    """
    Qt's 'void QPlatformFontDatabase::registerFont(const QString &familyname,
    const QString &stylename, const QString &foundryname, QFont::Weight
    weight, QFont::Style style, QFont::Stretch stretch, bool antialiased,
    bool scalable, int pixelSize, bool fixedPitch, bool colorFont, const
    QSupportedWritingSystems &writingSystems, void *handle)': names 'void',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QPlatformFontDatabase.registerFont' has no cute function yet. "
        "Qt's 'void QPlatformFontDatabase::registerFont(const QString "
        "&familyname, const QString &stylename, const QString &foundryname, "
        "QFont::Weight weight, QFont::Style style, QFont::Stretch stretch, "
        "bool antialiased, bool scalable, int pixelSize, bool fixedPitch, "
        "bool colorFont, const QSupportedWritingSystems &writingSystems, "
        "void *handle)': names 'void', which has no cute class yet.")

  @staticmethod
  def releaseHandle(*__, **_) -> Never:
    """
    Qt's 'void QPlatformFontDatabase::releaseHandle(void *handle)': names
    'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QPlatformFontDatabase.releaseHandle' has no cute function yet. "
        "Qt's 'void QPlatformFontDatabase::releaseHandle(void *handle)': "
        "names 'void', which has no cute class yet.")

  @staticmethod
  def standardSizes(*__, **_) -> Never:
    """
    Qt's 'QList<int> QPlatformFontDatabase::standardSizes() const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QPlatformFontDatabase.standardSizes' has no cute function yet. "
        "Qt's 'QList<int> QPlatformFontDatabase::standardSizes() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def writingSystemsFromTrueTypeBits(*__, **_) -> Never:
    """
    Qt's 'QSupportedWritingSystems
    QPlatformFontDatabase::writingSystemsFromTrueTypeBits(quint32
    *unicodeRange, quint32 *codePageRange)': takes a number to change where
    it is.
    """
    raise NotImplementedError(
        "'QPlatformFontDatabase.writingSystemsFromTrueTypeBits' has no cute "
        "function yet. Qt's 'QSupportedWritingSystems "
        "QPlatformFontDatabase::writingSystemsFromTrueTypeBits(quint32 "
        "*unicodeRange, quint32 *codePageRange)': takes a number to change "
        "where it is.")
