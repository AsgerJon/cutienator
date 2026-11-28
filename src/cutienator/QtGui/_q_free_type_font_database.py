"""
QFreeTypeFontDatabase binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qfreetypefontdatabase_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QFreeTypeFontDatabase to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QStringList
from . import QFont, QFontDatabasePrivate, QPlatformFontDatabase

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray
  from . import QFontEngine
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QFreeTypeFontDatabase(QPlatformFontDatabase):
  """
  The cute side of Qt's QFreeTypeFontDatabase: a plain Python object standing
  in front of one C++ QFreeTypeFontDatabase.

  It is built on the cute 'QPlatformFontDatabase', as Qt's
  QFreeTypeFontDatabase is built on Qt's QPlatformFontDatabase, and has
  everything that class has.

  C++ hands a QFreeTypeFontDatabase around as a copy, so every C++
  QFreeTypeFontDatabase behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QFreeTypeFontDatabase that has a ritual and that
  Python can call so far, 6 names in all: 'populateFontDatabase',
  'fontEngine', 'addApplicationFont', 'supportsVariableApplicationFonts',
  'supportsColrv0Fonts', 'addTTFile'. None can be made from Python: one comes
  out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QFontEngine *QFreeTypeFontDatabase::fontEngine(const QFontDef
    &fontDef, void *handle)': names 'void', which has no cute class yet.
  - Qt's 'void QFreeTypeFontDatabase::releaseHandle(void *handle)': names
    'void', which has no cute class yet.
  - Qt's 'void QFreeTypeFontDatabase::addNamedInstancesForFace(void *face,
    int faceIndex, const QString &family, const QString &styleName,
    QFont::Weight weight, QFont::Stretch stretch, QFont::Style style, bool
    fixedPitch, bool isColor, const QSupportedWritingSystems &writingSystems,
    const QByteArray &fileName, const QByteArray &fontData)': names 'void',
    which has no cute class yet.
  - Qt's 'QFreeTypeFontDatabase::~QFreeTypeFontDatabase()': the destructor:
    Python removes its C++ QFreeTypeFontDatabase by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QFreeTypeFontDatabase is created at the first use, not by
    'QFreeTypeFontDatabase(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QFreeTypeFontDatabase back gives a copy the ritual
    made for Python, in a new cute QFreeTypeFontDatabase.
  - Each name of Qt's QFreeTypeFontDatabase that has no cute function yet,
    'addNamedInstancesForFace', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QByteArray, QByteArray)
  @overload(QByteArray, QByteArray, QFontDatabasePrivate.ApplicationFont)
  @overload(QByteArray, QByteArray, NoneType)
  def addTTFile(
      fontData: QByteArray,
      file: QByteArray,
      applicationFont: Optional[QFontDatabasePrivate.ApplicationFont] = None,
  ) -> QStringList:
    """
    Calls Qt's 'QStringList QFreeTypeFontDatabase::addTTFile(const QByteArray
    &fontData, const QByteArray &file, QFontDatabasePrivate::ApplicationFont
    *applicationFont)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfreetypefontdatabase.html#addTTFile

    Parameters
    ----------

    fontData : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    file : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    applicationFont : Optional[QFontDatabasePrivate.ApplicationFont]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QFreeTypeFontDatabase::addTTFile(const QByteArray
    #      &fontData, const QByteArray &file,
    #      QFontDatabasePrivate::ApplicationFont *applicationFont)
    address = Rituals.call(
        'ritual_ZN21QFreeTypeFontDatabase9addTTFileERK10QByteArrayS2_PN20QF'
        'ontDatabasePrivate15ApplicationFontE',
        CuteMixin._valueOf(fontData), CuteMixin._valueOf(file),
        CuteMixin._addressOf(applicationFont),
    )
    return QStringList._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QFreeTypeFontDatabase'

  #  A C++ QFreeTypeFontDatabase Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QFreeTypeFontDatabase'

  #  Qt's '~QFreeTypeFontDatabase()'. Naming it makes this a value class:
  #  Python owns every C++ QFreeTypeFontDatabase behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN21QFreeTypeFontDatabaseD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def supportsVariableApplicationFonts(self) -> bool:
    """
    Calls Qt's 'bool
    QFreeTypeFontDatabase::supportsVariableApplicationFonts() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfreetypefontdatabase.html
    """
    #  bool QFreeTypeFontDatabase::supportsVariableApplicationFonts() const
    ritual = (
        'ritual_ZNK21QFreeTypeFontDatabase32supportsVariableApplicationFont'
        'sEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK21QFreeTypeFontDatabase32supportsVariableApplicati'
          'onFontsEv')
    return self.uglySide.call(ritual)

  def supportsColrv0Fonts(self) -> bool:
    """
    Calls Qt's 'bool QFreeTypeFontDatabase::supportsColrv0Fonts() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfreetypefontdatabase.html#supportsColrv0Fonts
    """
    #  bool QFreeTypeFontDatabase::supportsColrv0Fonts() const
    ritual = 'ritual_ZNK21QFreeTypeFontDatabase19supportsColrv0FontsEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QFreeTypeFontDatabase19supportsColrv0FontsEv'
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
    Calls Qt's 'void QFreeTypeFontDatabase::populateFontDatabase()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfreetypefontdatabase.html#populateFontDatabase
    """
    #  void QFreeTypeFontDatabase::populateFontDatabase()
    ritual = 'ritual_ZN21QFreeTypeFontDatabase20populateFontDatabaseEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QFreeTypeFontDatabase20populateFontDatabaseEv'
    self.uglySide.call(ritual)

  @overload(QByteArray, float, QFont.HintingPreference)
  def fontEngine(
      self,
      fontData: QByteArray,
      pixelSize: float,
      hintingPreference: QFont.HintingPreference,
  ) -> Optional[QFontEngine]:
    """
    Calls Qt's 'QFontEngine *QFreeTypeFontDatabase::fontEngine(const
    QByteArray &fontData, qreal pixelSize, QFont::HintingPreference
    hintingPreference)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfreetypefontdatabase.html#fontEngine

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
    #  QFontEngine *QFreeTypeFontDatabase::fontEngine(const QByteArray
    #      &fontData, qreal pixelSize, QFont::HintingPreference
    #      hintingPreference)
    ritual = (
        'ritual_ZN21QFreeTypeFontDatabase10fontEngineERK10QByteArraydN5QFon'
        't17HintingPreferenceE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QFreeTypeFontDatabase10fontEngineERK10QByteArrayd'
          'N5QFont17HintingPreferenceE')
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
    Calls Qt's 'QStringList QFreeTypeFontDatabase::addApplicationFont(const
    QByteArray &fontData, const QString &fileName,
    QFontDatabasePrivate::ApplicationFont *applicationFont)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfreetypefontdatabase.html#addApplicationFont

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
    #  QStringList QFreeTypeFontDatabase::addApplicationFont(const QByteArray
    #      &fontData, const QString &fileName,
    #      QFontDatabasePrivate::ApplicationFont *applicationFont)
    address = self.uglySide.call(
        'ritual_ZN21QFreeTypeFontDatabase18addApplicationFontERK10QByteArra'
        'yRK7QStringPN20QFontDatabasePrivate15ApplicationFontE',
        self._valueOf(fontData), fileName, self._addressOf(applicationFont),
    )
    return QStringList._cuteOwning(address)

  @staticmethod
  def addNamedInstancesForFace(*__, **_) -> Never:
    """
    Qt's 'void QFreeTypeFontDatabase::addNamedInstancesForFace(void *face,
    int faceIndex, const QString &family, const QString &styleName,
    QFont::Weight weight, QFont::Stretch stretch, QFont::Style style, bool
    fixedPitch, bool isColor, const QSupportedWritingSystems &writingSystems,
    const QByteArray &fileName, const QByteArray &fontData)': names 'void',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QFreeTypeFontDatabase.addNamedInstancesForFace' has no cute "
        "function yet. Qt's 'void "
        "QFreeTypeFontDatabase::addNamedInstancesForFace(void *face, int "
        "faceIndex, const QString &family, const QString &styleName, "
        "QFont::Weight weight, QFont::Stretch stretch, QFont::Style style, "
        "bool fixedPitch, bool isColor, const QSupportedWritingSystems "
        "&writingSystems, const QByteArray &fileName, const QByteArray "
        "&fontData)': names 'void', which has no cute class yet.")
