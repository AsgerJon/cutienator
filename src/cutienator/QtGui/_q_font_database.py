"""
QFontDatabase binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qfontdatabase.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QCharScript
from . import QFontDatabaseSystemFont, QFontDatabaseWritingSystem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QByteArray, QChar
  from . import QFont, QFontInfo
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QFont = WAIT['QFont']
  QFontInfo = WAIT['QFontInfo']


class QFontDatabase(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QFontDatabase: a plain Python object standing in
  front of one C++ QFontDatabase.

  C++ hands a QFontDatabase around as a copy, so every C++ QFontDatabase
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QFontDatabase that has a ritual and that Python can
  call so far, 22 names in all: 'styleString', 'font', 'isBitmapScalable',
  'isSmoothlyScalable', 'isScalable', 'isFixedPitch', 'italic', 'bold',
  'weight', 'hasFamily', 'isPrivateFamily', 'writingSystemName',
  'writingSystemSample', 'addApplicationFont', 'addApplicationFontFromData',
  'removeApplicationFont', 'removeAllApplicationFonts',
  'addApplicationFallbackFontFamily', 'removeApplicationFallbackFontFamily',
  'addApplicationEmojiFontFamily', 'removeApplicationEmojiFontFamily',
  'systemFont'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QFontDatabase::~QFontDatabase()': the destructor: Python removes
    its C++ QFontDatabase by it, and has no other use for it.

  What has no ritual
  ------------------

  15 of the 40 functions Qt declares: 12 takes or gives a type that cannot be
  passed yet; 1 declared and nowhere to be found; 1 a template; 1 private.

  What to expect
  --------------

  - The C++ QFontDatabase is created at the first use, not by
    'QFontDatabase(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QFontDatabase back gives a copy the ritual made for
    Python, in a new cute QFontDatabase.
  """

  #  The enums Qt writes inside QFontDatabase, and the names Qt has for the
  #  combinations of its flags enums.
  SystemFont = QFontDatabaseSystemFont
  WritingSystem = QFontDatabaseWritingSystem

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QFont)
  def styleString(font: QFont) -> str:
    """
    Calls Qt's 'QString QFontDatabase::styleString(const QFont &font)'.

    Qt's own words: https://doc.qt.io/qt-6/qfontdatabase.html#styleString

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFontDatabase::styleString(const QFont &font)
    return Rituals.call(
        'ritual_ZN13QFontDatabase11styleStringERK5QFont',
        CuteMixin._valueOf(font),
    )

  @staticmethod
  @overload(QFontInfo)
  def styleString(fontInfo: QFontInfo) -> str:
    """
    Calls Qt's 'QString QFontDatabase::styleString(const QFontInfo
    &fontInfo)'.

    Qt's own words: https://doc.qt.io/qt-6/qfontdatabase.html#styleString

    Parameters
    ----------

    fontInfo : QFontInfo
      Passed on as a value: Qt reads the C++ QFontInfo, which stays Python's
      own.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFontDatabase::styleString(const QFontInfo &fontInfo)
    return Rituals.call(
        'ritual_ZN13QFontDatabase11styleStringERK9QFontInfo',
        CuteMixin._valueOf(fontInfo),
    )

  @staticmethod
  @overload(str, str, int)
  def font(family: str, style: str, pointSize: int) -> QFont:
    """
    Calls Qt's 'QFont QFontDatabase::font(const QString &family, const
    QString &style, int pointSize)'.

    Qt's own words: https://doc.qt.io/qt-6/qfontdatabase.html#font

    Parameters
    ----------

    family : str
      Passed on as it is: a QString is made of it for the call.

    style : str
      Passed on as it is: a QString is made of it for the call.

    pointSize : int
      Passed on as it is.

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QFontDatabase::font(const QString &family, const QString &style,
    #      int pointSize)
    address = Rituals.call(
        'ritual_ZN13QFontDatabase4fontERK7QStringS2_i',
        family, style, pointSize,
    )
    from . import QFont
    return QFont._cuteOwning(address)

  @staticmethod
  @overload(str)
  @overload(str, str)
  def isBitmapScalable(family: str, style: str = '') -> bool:
    """
    Calls Qt's 'bool QFontDatabase::isBitmapScalable(const QString &family,
    const QString &style)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontdatabase.html#isBitmapScalable

    Parameters
    ----------

    family : str
      Passed on as it is: a QString is made of it for the call.

    style : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  bool QFontDatabase::isBitmapScalable(const QString &family, const
    #      QString &style)
    return Rituals.call(
        'ritual_ZN13QFontDatabase16isBitmapScalableERK7QStringS2_',
        family, style,
    )

  @staticmethod
  @overload(str)
  @overload(str, str)
  def isSmoothlyScalable(family: str, style: str = '') -> bool:
    """
    Calls Qt's 'bool QFontDatabase::isSmoothlyScalable(const QString &family,
    const QString &style)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontdatabase.html#isSmoothlyScalable

    Parameters
    ----------

    family : str
      Passed on as it is: a QString is made of it for the call.

    style : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  bool QFontDatabase::isSmoothlyScalable(const QString &family, const
    #      QString &style)
    return Rituals.call(
        'ritual_ZN13QFontDatabase18isSmoothlyScalableERK7QStringS2_',
        family, style,
    )

  @staticmethod
  @overload(str)
  @overload(str, str)
  def isScalable(family: str, style: str = '') -> bool:
    """
    Calls Qt's 'bool QFontDatabase::isScalable(const QString &family, const
    QString &style)'.

    Qt's own words: https://doc.qt.io/qt-6/qfontdatabase.html#isScalable

    Parameters
    ----------

    family : str
      Passed on as it is: a QString is made of it for the call.

    style : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  bool QFontDatabase::isScalable(const QString &family, const QString
    #      &style)
    return Rituals.call(
        'ritual_ZN13QFontDatabase10isScalableERK7QStringS2_', family, style,
    )

  @staticmethod
  @overload(str)
  @overload(str, str)
  def isFixedPitch(family: str, style: str = '') -> bool:
    """
    Calls Qt's 'bool QFontDatabase::isFixedPitch(const QString &family, const
    QString &style)'.

    Qt's own words: https://doc.qt.io/qt-6/qfontdatabase.html#isFixedPitch

    Parameters
    ----------

    family : str
      Passed on as it is: a QString is made of it for the call.

    style : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  bool QFontDatabase::isFixedPitch(const QString &family, const QString
    #      &style)
    return Rituals.call(
        'ritual_ZN13QFontDatabase12isFixedPitchERK7QStringS2_',
        family, style,
    )

  @staticmethod
  @overload(str, str)
  def italic(family: str, style: str) -> bool:
    """
    Calls Qt's 'bool QFontDatabase::italic(const QString &family, const
    QString &style)'.

    Qt's own words: https://doc.qt.io/qt-6/qfontdatabase.html#italic

    Parameters
    ----------

    family : str
      Passed on as it is: a QString is made of it for the call.

    style : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QFontDatabase::italic(const QString &family, const QString
    #      &style)
    return Rituals.call(
        'ritual_ZN13QFontDatabase6italicERK7QStringS2_', family, style,
    )

  @staticmethod
  @overload(str, str)
  def bold(family: str, style: str) -> bool:
    """
    Calls Qt's 'bool QFontDatabase::bold(const QString &family, const QString
    &style)'.

    Qt's own words: https://doc.qt.io/qt-6/qfontdatabase.html#bold

    Parameters
    ----------

    family : str
      Passed on as it is: a QString is made of it for the call.

    style : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QFontDatabase::bold(const QString &family, const QString &style)
    return Rituals.call(
        'ritual_ZN13QFontDatabase4boldERK7QStringS2_', family, style,
    )

  @staticmethod
  @overload(str, str)
  def weight(family: str, style: str) -> int:
    """
    Calls Qt's 'int QFontDatabase::weight(const QString &family, const
    QString &style)'.

    Qt's own words: https://doc.qt.io/qt-6/qfontdatabase.html#weight

    Parameters
    ----------

    family : str
      Passed on as it is: a QString is made of it for the call.

    style : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  int QFontDatabase::weight(const QString &family, const QString &style)
    return Rituals.call(
        'ritual_ZN13QFontDatabase6weightERK7QStringS2_', family, style,
    )

  @staticmethod
  @overload(str)
  def hasFamily(family: str) -> bool:
    """
    Calls Qt's 'bool QFontDatabase::hasFamily(const QString &family)'.

    Qt's own words: https://doc.qt.io/qt-6/qfontdatabase.html#hasFamily

    Parameters
    ----------

    family : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QFontDatabase::hasFamily(const QString &family)
    return Rituals.call(
        'ritual_ZN13QFontDatabase9hasFamilyERK7QString', family,
    )

  @staticmethod
  @overload(str)
  def isPrivateFamily(family: str) -> bool:
    """
    Calls Qt's 'bool QFontDatabase::isPrivateFamily(const QString &family)'.

    Qt's own words: https://doc.qt.io/qt-6/qfontdatabase.html#isPrivateFamily

    Parameters
    ----------

    family : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QFontDatabase::isPrivateFamily(const QString &family)
    return Rituals.call(
        'ritual_ZN13QFontDatabase15isPrivateFamilyERK7QString', family,
    )

  @staticmethod
  @overload(WritingSystem)
  def writingSystemName(writingSystem: WritingSystem) -> str:
    """
    Calls Qt's 'QString QFontDatabase::writingSystemName(WritingSystem
    writingSystem)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontdatabase.html#writingSystemName

    Parameters
    ----------

    writingSystem : WritingSystem
      Passed on as its number.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFontDatabase::writingSystemName(WritingSystem writingSystem)
    return Rituals.call(
        'ritual_ZN13QFontDatabase17writingSystemNameENS_13WritingSystemE',
        writingSystem.value,
    )

  @staticmethod
  @overload(WritingSystem)
  def writingSystemSample(writingSystem: WritingSystem) -> str:
    """
    Calls Qt's 'QString QFontDatabase::writingSystemSample(WritingSystem
    writingSystem)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontdatabase.html#writingSystemSample

    Parameters
    ----------

    writingSystem : WritingSystem
      Passed on as its number.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFontDatabase::writingSystemSample(WritingSystem
    #      writingSystem)
    return Rituals.call(
        'ritual_ZN13QFontDatabase19writingSystemSampleENS_13WritingSystemE',
        writingSystem.value,
    )

  @staticmethod
  @overload(str)
  def addApplicationFont(fileName: str) -> int:
    """
    Calls Qt's 'int QFontDatabase::addApplicationFont(const QString
    &fileName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontdatabase.html#addApplicationFont

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  int QFontDatabase::addApplicationFont(const QString &fileName)
    return Rituals.call(
        'ritual_ZN13QFontDatabase18addApplicationFontERK7QString', fileName,
    )

  @staticmethod
  @overload(QByteArray)
  def addApplicationFontFromData(fontData: QByteArray) -> int:
    """
    Calls Qt's 'int QFontDatabase::addApplicationFontFromData(const
    QByteArray &fontData)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontdatabase.html#addApplicationFontFromData

    Parameters
    ----------

    fontData : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  int QFontDatabase::addApplicationFontFromData(const QByteArray
    #      &fontData)
    return Rituals.call(
        'ritual_ZN13QFontDatabase26addApplicationFontFromDataERK10QByteArra'
        'y',
        CuteMixin._valueOf(fontData),
    )

  @staticmethod
  @overload(int)
  def removeApplicationFont(id: int) -> bool:
    """
    Calls Qt's 'bool QFontDatabase::removeApplicationFont(int id)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontdatabase.html#removeApplicationFont

    Parameters
    ----------

    id : int
      Passed on as it is.
    """
    #  bool QFontDatabase::removeApplicationFont(int id)
    return Rituals.call(
        'ritual_ZN13QFontDatabase21removeApplicationFontEi', id,
    )

  @staticmethod
  def removeAllApplicationFonts() -> bool:
    """
    Calls Qt's 'bool QFontDatabase::removeAllApplicationFonts()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontdatabase.html#removeAllApplicationFonts
    """
    #  bool QFontDatabase::removeAllApplicationFonts()
    return Rituals.call(
        'ritual_ZN13QFontDatabase25removeAllApplicationFontsEv',
    )

  @staticmethod
  @overload(QCharScript, str)
  def addApplicationFallbackFontFamily(
      script: QChar.Script,
      familyName: str,
  ) -> None:
    """
    Calls Qt's 'void
    QFontDatabase::addApplicationFallbackFontFamily(QChar::Script script,
    const QString &familyName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontdatabase.html

    Parameters
    ----------

    script : QChar.Script
      Passed on as its number.

    familyName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QFontDatabase::addApplicationFallbackFontFamily(QChar::Script
    #      script, const QString &familyName)
    Rituals.call(
        'ritual_ZN13QFontDatabase32addApplicationFallbackFontFamilyEN5QChar'
        '6ScriptERK7QString',
        script.value, familyName,
    )

  @staticmethod
  @overload(QCharScript, str)
  def removeApplicationFallbackFontFamily(
      script: QChar.Script,
      familyName: str,
  ) -> bool:
    """
    Calls Qt's 'bool
    QFontDatabase::removeApplicationFallbackFontFamily(QChar::Script script,
    const QString &familyName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontdatabase.html

    Parameters
    ----------

    script : QChar.Script
      Passed on as its number.

    familyName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QFontDatabase::removeApplicationFallbackFontFamily(QChar::Script
    #      script, const QString &familyName)
    return Rituals.call(
        'ritual_ZN13QFontDatabase35removeApplicationFallbackFontFamilyEN5QC'
        'har6ScriptERK7QString',
        script.value, familyName,
    )

  @staticmethod
  @overload(str)
  def addApplicationEmojiFontFamily(familyName: str) -> None:
    """
    Calls Qt's 'void QFontDatabase::addApplicationEmojiFontFamily(const
    QString &familyName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontdatabase.html#addApplicationEmojiFontFamily

    Parameters
    ----------

    familyName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QFontDatabase::addApplicationEmojiFontFamily(const QString
    #      &familyName)
    Rituals.call(
        'ritual_ZN13QFontDatabase29addApplicationEmojiFontFamilyERK7QString',
        familyName,
    )

  @staticmethod
  @overload(str)
  def removeApplicationEmojiFontFamily(familyName: str) -> bool:
    """
    Calls Qt's 'bool QFontDatabase::removeApplicationEmojiFontFamily(const
    QString &familyName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontdatabase.html

    Parameters
    ----------

    familyName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QFontDatabase::removeApplicationEmojiFontFamily(const QString
    #      &familyName)
    return Rituals.call(
        'ritual_ZN13QFontDatabase32removeApplicationEmojiFontFamilyERK7QStr'
        'ing',
        familyName,
    )

  @staticmethod
  @overload(SystemFont)
  def systemFont(type: SystemFont) -> QFont:
    """
    Calls Qt's 'QFont QFontDatabase::systemFont(SystemFont type)'.

    Qt's own words: https://doc.qt.io/qt-6/qfontdatabase.html#systemFont

    Parameters
    ----------

    type : SystemFont
      Passed on as its number.

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QFontDatabase::systemFont(SystemFont type)
    address = Rituals.call(
        'ritual_ZN13QFontDatabase10systemFontENS_10SystemFontE', type.value,
    )
    from . import QFont
    return QFont._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QFontDatabase'

  #  Qt's '~QFontDatabase()'. Naming it makes this a value class: Python owns
  #  every C++ QFontDatabase behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN13QFontDatabaseD1Ev'

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QFontDatabase::QFontDatabase()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qfontdatabase.html#QFontDatabase
    """
    #  QFontDatabase::QFontDatabase()
    self._noteCreation(QFontDatabase, lambda: Rituals.call(
        'ritual_ZN13QFontDatabaseC1Ev',
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
