"""
QLocalePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qlocale_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QLocalePrivate to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QLocale

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QLocaleData
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QLocaleData = WAIT['QLocaleData']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QLocalePrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QLocalePrivate: a plain Python object standing in
  front of one C++ QLocalePrivate.

  What exists
  -----------

  Every function of Qt's QLocalePrivate that has a ritual and that Python can
  call so far, 4 names in all: 'languageId', 'territoryId', 'get',
  'measurementSystem'. It can be made from Python, in 1 way; see '__init__'.

  What has no ritual
  ------------------

  12 of the 17 functions Qt declares: 6 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 3 leans on
  'QLocalePrivate; 2 cannot be called and cannot be called through the
  meta-object and cannot be copied; 1 leans on 'QLocaleId.

  What to expect
  --------------

  - The C++ QLocalePrivate is created at the first use, not by
    'QLocalePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QLocalePrivate.
  - Each name of Qt's QLocalePrivate that has no cute function yet,
    'bcp47Name', 'codeToLanguage', 'codeToScript', 'codeToTerritory',
    'languageCode', 'languageToCode', 'scriptCode', 'scriptToCode',
    'territoryCode', 'territoryToCode', 'toLower', 'toUpper', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QLocale)
  def get(l: QLocale) -> Optional[QLocalePrivate]:
    """
    Calls Qt's 'const QLocalePrivate *QLocalePrivate::get(const QLocale &l)'.

    Qt's own words: https://doc.qt.io/qt-6/qlocaleprivate.html#get

    Parameters
    ----------

    l : QLocale
      Passed on as a value: Qt reads the C++ QLocale, which stays Python's
      own.

    Returns
    -------

    Optional[QLocalePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QLocalePrivate *QLocalePrivate::get(const QLocale &l)
    address = Rituals.call(
        'ritual_ZN14QLocalePrivate3getERK7QLocale', CuteMixin._valueOf(l),
    )
    return QLocalePrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QLocalePrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def languageId(self) -> int:
    """
    Calls Qt's 'quint16 QLocalePrivate::languageId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocaleprivate.html#languageId
    """
    #  quint16 QLocalePrivate::languageId() const
    return self.uglySide.call('ritual_ZNK14QLocalePrivate10languageIdEv')

  def territoryId(self) -> int:
    """
    Calls Qt's 'quint16 QLocalePrivate::territoryId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocaleprivate.html#territoryId
    """
    #  quint16 QLocalePrivate::territoryId() const
    return self.uglySide.call('ritual_ZNK14QLocalePrivate11territoryIdEv')

  def measurementSystem(self) -> QLocale.MeasurementSystem:
    """
    Calls Qt's 'QLocale::MeasurementSystem
    QLocalePrivate::measurementSystem() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlocaleprivate.html#measurementSystem

    Returns
    -------

    QLocale.MeasurementSystem
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QLocale.MeasurementSystem(number)' gives.
    """
    #  QLocale::MeasurementSystem QLocalePrivate::measurementSystem() const
    return QLocale.MeasurementSystem(self.uglySide.call(
        'ritual_ZNK14QLocalePrivate17measurementSystemEv',
    ))

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

  @overload(QLocaleData, int)
  @overload(NoneType, int)
  @overload(QLocaleData, int, QLocale.NumberOptions)
  @overload(NoneType, int, QLocale.NumberOptions)
  @overload(QLocaleData, int, QLocale.NumberOptions, int)
  @overload(NoneType, int, QLocale.NumberOptions, int)
  def __init__(
      self,
      data: Optional[QLocaleData],
      index: int,
      numberOptions: QLocale.NumberOptions = (
          QLocale.NumberOptions.DefaultNumberOptions),
      refs: int = 0,
  ) -> None:
    """
    Notes what was given, for Qt's 'QLocalePrivate::QLocalePrivate(const
    QLocaleData *data, qsizetype index, QLocale::NumberOptions numberOptions,
    int refs)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qlocaleprivate.html#QLocalePrivate

    Parameters
    ----------

    data : Optional[QLocaleData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    index : int
      Passed on as it is.

    numberOptions : QLocale.NumberOptions
      Passed on as its number. May be left out, as in Qt: it is then
      QLocale.NumberOptions.DefaultNumberOptions.

    refs : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  QLocalePrivate::QLocalePrivate(const QLocaleData *data, qsizetype
    #      index, QLocale::NumberOptions numberOptions, int refs)
    self._noteCreation(QLocalePrivate, lambda: Rituals.call(
        'ritual_ZN14QLocalePrivateC1EPK11QLocaleDatax6QFlagsIN7QLocale12Num'
        'berOptionEEi',
        self._addressOf(data), index, numberOptions.value, refs,
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
  def bcp47Name(*__, **_) -> Never:
    """
    Qt's 'QByteArray QLocalePrivate::bcp47Name(char separator) const': leans
    on 'QLocaleId::name(char) const', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QLocalePrivate.bcp47Name' has no cute function yet. Qt's "
        "'QByteArray QLocalePrivate::bcp47Name(char separator) const': "
        "leans on 'QLocaleId::name(char) const', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def codeToLanguage(*__, **_) -> Never:
    """
    Qt's 'QLocale::Language QLocalePrivate::codeToLanguage(QStringView code,
    QLocale::LanguageCodeTypes codeTypes)': Qt's library has no name for it,
    and its code in Qt's source does not compile apart from its file: unknown
    type name 'AlphaCode'.
    """
    raise NotImplementedError(
        "'QLocalePrivate.codeToLanguage' has no cute function yet. Qt's "
        "'QLocale::Language QLocalePrivate::codeToLanguage(QStringView "
        "code, QLocale::LanguageCodeTypes codeTypes)': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: unknown type name 'AlphaCode'.")

  @staticmethod
  def codeToScript(*__, **_) -> Never:
    """
    Qt's 'QLocale::Script QLocalePrivate::codeToScript(QStringView code)':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: use of undeclared identifier 'scriptIndex'.
    """
    raise NotImplementedError(
        "'QLocalePrivate.codeToScript' has no cute function yet. Qt's "
        "'QLocale::Script QLocalePrivate::codeToScript(QStringView code)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'scriptIndex'.")

  @staticmethod
  def codeToTerritory(*__, **_) -> Never:
    """
    Qt's 'QLocale::Territory QLocalePrivate::codeToTerritory(QStringView
    code)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'territory_code_list'.
    """
    raise NotImplementedError(
        "'QLocalePrivate.codeToTerritory' has no cute function yet. Qt's "
        "'QLocale::Territory QLocalePrivate::codeToTerritory(QStringView "
        "code)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'territory_code_list'.")

  @staticmethod
  def languageCode(*__, **_) -> Never:
    """
    Qt's 'std::array<char, 4>
    QLocalePrivate::languageCode(QLocale::LanguageCodeTypes codeTypes)
    const': leans on 'QLocalePrivate::languageToCode(QLocale::Language,
    QFlags<QLocale::LanguageCodeType>)', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QLocalePrivate.languageCode' has no cute function yet. Qt's "
        "'std::array<char, 4> "
        "QLocalePrivate::languageCode(QLocale::LanguageCodeTypes codeTypes) "
        "const': leans on "
        "'QLocalePrivate::languageToCode(QLocale::Language, "
        "QFlags<QLocale::LanguageCodeType>)', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def languageToCode(*__, **_) -> Never:
    """
    Qt's 'std::array<char, 4>
    QLocalePrivate::languageToCode(QLocale::Language language,
    QLocale::LanguageCodeTypes codeTypes)': Qt's library has no name for it,
    and its code in Qt's source does not compile apart from its file: unknown
    type name 'LanguageCodeEntry'.
    """
    raise NotImplementedError(
        "'QLocalePrivate.languageToCode' has no cute function yet. Qt's "
        "'std::array<char, 4> "
        "QLocalePrivate::languageToCode(QLocale::Language language, "
        "QLocale::LanguageCodeTypes codeTypes)': Qt's library has no name "
        "for it, and its code in Qt's source does not compile apart from "
        "its file: unknown type name 'LanguageCodeEntry'.")

  @staticmethod
  def scriptCode(*__, **_) -> Never:
    """
    Qt's 'QLatin1StringView QLocalePrivate::scriptCode() const': leans on
    'QLocalePrivate::scriptToCode(QLocale::Script)', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QLocalePrivate.scriptCode' has no cute function yet. Qt's "
        "'QLatin1StringView QLocalePrivate::scriptCode() const': leans on "
        "'QLocalePrivate::scriptToCode(QLocale::Script)', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def scriptToCode(*__, **_) -> Never:
    """
    Qt's 'QLatin1StringView QLocalePrivate::scriptToCode(QLocale::Script
    script)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: use of undeclared identifier
    'script_code_list'.
    """
    raise NotImplementedError(
        "'QLocalePrivate.scriptToCode' has no cute function yet. Qt's "
        "'QLatin1StringView QLocalePrivate::scriptToCode(QLocale::Script "
        "script)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'script_code_list'.")

  @staticmethod
  def territoryCode(*__, **_) -> Never:
    """
    Qt's 'QLatin1StringView QLocalePrivate::territoryCode() const': leans on
    'QLocalePrivate::territoryToCode(QLocale::Country)', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QLocalePrivate.territoryCode' has no cute function yet. Qt's "
        "'QLatin1StringView QLocalePrivate::territoryCode() const': leans "
        "on 'QLocalePrivate::territoryToCode(QLocale::Country)', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def territoryToCode(*__, **_) -> Never:
    """
    Qt's 'QLatin1StringView
    QLocalePrivate::territoryToCode(QLocale::Territory territory)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'territory_code_list'.
    """
    raise NotImplementedError(
        "'QLocalePrivate.territoryToCode' has no cute function yet. Qt's "
        "'QLatin1StringView "
        "QLocalePrivate::territoryToCode(QLocale::Territory territory)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'territory_code_list'.")

  @staticmethod
  def toLower(*__, **_) -> Never:
    """
    Qt's 'QString QLocalePrivate::toLower(const QString &str, bool *ok)
    const': cannot be called and cannot be called through the meta-object and
    cannot be copied: no header file has its code, Qt's source does not mark
    it or its class for use from outside Qt or writes it 'inline' or nowhere,
    and it is no signal, slot or invokable function giving back nothing, of a
    class built on QObject, and Qt's source has no code for it that could be
    told from the rest.
    """
    raise NotImplementedError(
        "'QLocalePrivate.toLower' has no cute function yet. Qt's 'QString "
        "QLocalePrivate::toLower(const QString &str, bool *ok) const': "
        "cannot be called and cannot be called through the meta-object and "
        "cannot be copied: no header file has its code, Qt's source does "
        "not mark it or its class for use from outside Qt or writes it "
        "'inline' or nowhere, and it is no signal, slot or invokable "
        "function giving back nothing, of a class built on QObject, and "
        "Qt's source has no code for it that could be told from the rest.")

  @staticmethod
  def toUpper(*__, **_) -> Never:
    """
    Qt's 'QString QLocalePrivate::toUpper(const QString &str, bool *ok)
    const': cannot be called and cannot be called through the meta-object and
    cannot be copied: no header file has its code, Qt's source does not mark
    it or its class for use from outside Qt or writes it 'inline' or nowhere,
    and it is no signal, slot or invokable function giving back nothing, of a
    class built on QObject, and Qt's source has no code for it that could be
    told from the rest.
    """
    raise NotImplementedError(
        "'QLocalePrivate.toUpper' has no cute function yet. Qt's 'QString "
        "QLocalePrivate::toUpper(const QString &str, bool *ok) const': "
        "cannot be called and cannot be called through the meta-object and "
        "cannot be copied: no header file has its code, Qt's source does "
        "not mark it or its class for use from outside Qt or writes it "
        "'inline' or nowhere, and it is no signal, slot or invokable "
        "function giving back nothing, of a class built on QObject, and "
        "Qt's source has no code for it that could be told from the rest.")
