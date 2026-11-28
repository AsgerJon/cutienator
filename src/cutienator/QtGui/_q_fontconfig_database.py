"""
QFontconfigDatabase binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qfontconfigdatabase_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QFontconfigDatabase to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QStringList
from . import QFont, QFontDatabasePrivate, QFreeTypeFontDatabase

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray
  from . import QFontEngine, QFontEngineMulti
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QFontEngine = WAIT['QFontEngine']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QFontconfigDatabase(QFreeTypeFontDatabase):
  """
  The cute side of Qt's QFontconfigDatabase: a plain Python object standing
  in front of one C++ QFontconfigDatabase.

  It is built on the cute 'QFreeTypeFontDatabase', as Qt's
  QFontconfigDatabase is built on Qt's QFreeTypeFontDatabase, and has
  everything that class has.

  C++ hands a QFontconfigDatabase around as a copy, so every C++
  QFontconfigDatabase behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QFontconfigDatabase that has a ritual and that
  Python can call so far, 9 names in all: 'populateFontDatabase',
  'invalidate', 'supportsVariableApplicationFonts', 'fontEngineMulti',
  'fontEngine', 'fallbacksForFamily', 'addApplicationFont',
  'resolveFontFamilyAlias', 'defaultFont'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QFontconfigDatabase::~QFontconfigDatabase()': the destructor:
    Python removes its C++ QFontconfigDatabase by it, and has no other use
    for it.
  - Qt's 'QFontEngine *QFontconfigDatabase::fontEngine(const QFontDef
    &fontDef, void *handle)': names 'void', which has no cute class yet.
  - Qt's 'void QFontconfigDatabase::setupFontEngine(QFontEngineFT *engine,
    const QFontDef &fontDef) const': names 'QFontEngineFT', which has no cute
    class yet.

  What to expect
  --------------

  - The C++ QFontconfigDatabase is created at the first use, not by
    'QFontconfigDatabase(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QFontconfigDatabase back gives a copy the ritual made
    for Python, in a new cute QFontconfigDatabase.
  - Each name of Qt's QFontconfigDatabase that has no cute function yet,
    'setupFontEngine', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QFontconfigDatabase'

  #  A C++ QFontconfigDatabase Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QFontconfigDatabase'

  #  Qt's '~QFontconfigDatabase()'. Naming it makes this a value class:
  #  Python owns every C++ QFontconfigDatabase behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = 'ritual_ZN19QFontconfigDatabaseD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def supportsVariableApplicationFonts(self) -> bool:
    """
    Calls Qt's 'bool QFontconfigDatabase::supportsVariableApplicationFonts()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontconfigdatabase.html
    """
    #  bool QFontconfigDatabase::supportsVariableApplicationFonts() const
    ritual = (
        'ritual_ZNK19QFontconfigDatabase32supportsVariableApplicationFontsE'
        'v')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK19QFontconfigDatabase32supportsVariableApplication'
          'FontsEv')
    return self.uglySide.call(ritual)

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
    Calls Qt's 'QStringList QFontconfigDatabase::fallbacksForFamily(const
    QString &family, QFont::Style style, QFont::StyleHint styleHint,
    QFontDatabasePrivate::ExtendedScript script) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontconfigdatabase.html#fallbacksForFamily

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
    #  QStringList QFontconfigDatabase::fallbacksForFamily(const QString
    #      &family, QFont::Style style, QFont::StyleHint styleHint,
    #      QFontDatabasePrivate::ExtendedScript script) const
    address = self.uglySide.call(
        'ritual_ZNK19QFontconfigDatabase18fallbacksForFamilyERK7QStringN5QF'
        'ont5StyleENS3_9StyleHintEN20QFontDatabasePrivate14ExtendedScriptE',
        family, style.value, styleHint.value, script.value,
    )
    return QStringList._cuteOwning(address)

  @overload(str)
  def resolveFontFamilyAlias(self, family: str) -> str:
    """
    Calls Qt's 'QString QFontconfigDatabase::resolveFontFamilyAlias(const
    QString &family) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontconfigdatabase.html#resolveFontFamilyAlias

    Parameters
    ----------

    family : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFontconfigDatabase::resolveFontFamilyAlias(const QString
    #      &family) const
    ritual = (
        'ritual_ZNK19QFontconfigDatabase22resolveFontFamilyAliasERK7QString')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK19QFontconfigDatabase22resolveFontFamilyAliasERK7Q'
          'String')
    return self.uglySide.call(ritual, family)

  def defaultFont(self) -> QFont:
    """
    Calls Qt's 'QFont QFontconfigDatabase::defaultFont() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontconfigdatabase.html#defaultFont

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QFontconfigDatabase::defaultFont() const
    ritual = 'ritual_ZNK19QFontconfigDatabase11defaultFontEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QFontconfigDatabase11defaultFontEv'
    address = self.uglySide.call(ritual)
    return QFont._cuteOwning(address)

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
    Calls Qt's 'void QFontconfigDatabase::populateFontDatabase()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontconfigdatabase.html#populateFontDatabase
    """
    #  void QFontconfigDatabase::populateFontDatabase()
    ritual = 'ritual_ZN19QFontconfigDatabase20populateFontDatabaseEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QFontconfigDatabase20populateFontDatabaseEv'
    self.uglySide.call(ritual)

  def invalidate(self) -> None:
    """
    Calls Qt's 'void QFontconfigDatabase::invalidate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontconfigdatabase.html#invalidate
    """
    #  void QFontconfigDatabase::invalidate()
    ritual = 'ritual_ZN19QFontconfigDatabase10invalidateEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QFontconfigDatabase10invalidateEv'
    self.uglySide.call(ritual)

  @overload(QFontEngine, QFontDatabasePrivate.ExtendedScript)
  @overload(NoneType, QFontDatabasePrivate.ExtendedScript)
  def fontEngineMulti(
      self,
      fontEngine: Optional[QFontEngine],
      script: QFontDatabasePrivate.ExtendedScript,
  ) -> Optional[QFontEngineMulti]:
    """
    Calls Qt's 'QFontEngineMulti
    *QFontconfigDatabase::fontEngineMulti(QFontEngine *fontEngine,
    QFontDatabasePrivate::ExtendedScript script)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontconfigdatabase.html#fontEngineMulti

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
    #  QFontEngineMulti *QFontconfigDatabase::fontEngineMulti(QFontEngine
    #      *fontEngine, QFontDatabasePrivate::ExtendedScript script)
    ritual = (
        'ritual_ZN19QFontconfigDatabase15fontEngineMultiEP11QFontEngineN20Q'
        'FontDatabasePrivate14ExtendedScriptE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QFontconfigDatabase15fontEngineMultiEP11QFontEngi'
          'neN20QFontDatabasePrivate14ExtendedScriptE')
    address = self.uglySide.call(
        ritual, self._addressOf(fontEngine), script.value,
    )
    from . import QFontEngineMulti
    return QFontEngineMulti._cuteAt(address)

  @overload(QByteArray, float, QFont.HintingPreference)
  def fontEngine(
      self,
      fontData: QByteArray,
      pixelSize: float,
      hintingPreference: QFont.HintingPreference,
  ) -> Optional[QFontEngine]:
    """
    Calls Qt's 'QFontEngine *QFontconfigDatabase::fontEngine(const QByteArray
    &fontData, qreal pixelSize, QFont::HintingPreference hintingPreference)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontconfigdatabase.html#fontEngine

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
    #  QFontEngine *QFontconfigDatabase::fontEngine(const QByteArray
    #      &fontData, qreal pixelSize, QFont::HintingPreference
    #      hintingPreference)
    ritual = (
        'ritual_ZN19QFontconfigDatabase10fontEngineERK10QByteArraydN5QFont1'
        '7HintingPreferenceE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QFontconfigDatabase10fontEngineERK10QByteArraydN5'
          'QFont17HintingPreferenceE')
    address = self.uglySide.call(
        ritual, self._valueOf(fontData), pixelSize, hintingPreference.value,
    )
    from . import QFontEngine
    return QFontEngine._cuteAt(address)

  @overload(QByteArray, str)
  @overload(QByteArray, str, QFontDatabasePrivate.ApplicationFont)
  @overload(QByteArray, str, NoneType)
  def addApplicationFont(
      self,
      fontData: QByteArray,
      fileName: str,
      applicationFont: Optional[QFontDatabasePrivate.ApplicationFont] = None,
  ) -> QStringList:
    """
    Calls Qt's 'QStringList QFontconfigDatabase::addApplicationFont(const
    QByteArray &fontData, const QString &fileName,
    QFontDatabasePrivate::ApplicationFont *applicationFont)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontconfigdatabase.html#addApplicationFont

    Parameters
    ----------

    fontData : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    fileName : str
      Passed on as it is: a QString is made of it for the call.

    applicationFont : Optional[QFontDatabasePrivate.ApplicationFont]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QFontconfigDatabase::addApplicationFont(const QByteArray
    #      &fontData, const QString &fileName,
    #      QFontDatabasePrivate::ApplicationFont *applicationFont)
    address = self.uglySide.call(
        'ritual_ZN19QFontconfigDatabase18addApplicationFontERK10QByteArrayR'
        'K7QStringPN20QFontDatabasePrivate15ApplicationFontE',
        self._valueOf(fontData), fileName, self._addressOf(applicationFont),
    )
    return QStringList._cuteOwning(address)

  @staticmethod
  def setupFontEngine(*__, **_) -> Never:
    """
    Qt's 'void QFontconfigDatabase::setupFontEngine(QFontEngineFT *engine,
    const QFontDef &fontDef) const': names 'QFontEngineFT', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QFontconfigDatabase.setupFontEngine' has no cute function yet. "
        "Qt's 'void QFontconfigDatabase::setupFontEngine(QFontEngineFT "
        "*engine, const QFontDef &fontDef) const': names 'QFontEngineFT', "
        "which has no cute class yet.")
