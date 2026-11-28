"""
QLocaleId binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qlocale_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QLocaleId to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QLocaleId(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QLocaleId: a plain Python object standing in front of
  one C++ QLocaleId.

  C++ hands a QLocaleId around as a copy, so every C++ QLocaleId behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QLocaleId that has a ritual and that Python can call
  so far, 6 names in all: '__eq__', '__ne__', 'isValid', 'matchesAll',
  'acceptLanguage', 'acceptScriptTerritory'. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QLocaleId::~QLocaleId()': the destructor: Python removes its C++
    QLocaleId by it, and has no other use for it.

  What has no ritual
  ------------------

  4 of the 11 functions Qt declares: 2 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 1 leans on
  'qt_splitLocaleName(QStringView, QStringView*, QStringView*,
  QStringView*)', which Qt's source does not mark for use from outside Qt and
  has no code for that could be taken; 1 leans on 'QLocaleId.

  What to expect
  --------------

  - The C++ QLocaleId is created at the first use, not by 'QLocaleId(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QLocaleId back gives a copy the ritual made for
    Python, in a new cute QLocaleId.
  - Each name of Qt's QLocaleId that has no cute function yet, 'fromName',
    'name', 'withLikelySubtagsAdded', 'withLikelySubtagsRemoved', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QLocaleId'

  #  Qt's '~QLocaleId()'. Naming it makes this a value class: Python owns
  #  every C++ QLocaleId behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN9QLocaleIdD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QLocaleId::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocaleid.html#isValid
    """
    #  bool QLocaleId::isValid() const
    return self.uglySide.call('ritual_ZNK9QLocaleId7isValidEv')

  def matchesAll(self) -> bool:
    """
    Calls Qt's 'bool QLocaleId::matchesAll() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocaleid.html#matchesAll
    """
    #  bool QLocaleId::matchesAll() const
    return self.uglySide.call('ritual_ZNK9QLocaleId10matchesAllEv')

  @overload(int)
  def acceptLanguage(self, lang: int) -> bool:
    """
    Calls Qt's 'bool QLocaleId::acceptLanguage(quint16 lang) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocaleid.html#acceptLanguage

    Parameters
    ----------

    lang : int
      Passed on as it is.
    """
    #  bool QLocaleId::acceptLanguage(quint16 lang) const
    return self.uglySide.call('ritual_ZNK9QLocaleId14acceptLanguageEt', lang)

  @overload(THIS)
  def acceptScriptTerritory(self, other: QLocaleId) -> bool:
    """
    Calls Qt's 'bool QLocaleId::acceptScriptTerritory(QLocaleId other)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlocaleid.html#acceptScriptTerritory

    Parameters
    ----------

    other : QLocaleId
      Passed on as a value: Qt reads the C++ QLocaleId, which stays Python's
      own.
    """
    #  bool QLocaleId::acceptScriptTerritory(QLocaleId other) const
    return self.uglySide.call(
        'ritual_ZNK9QLocaleId21acceptScriptTerritoryES_',
        self._valueOf(other),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, other: QLocaleId) -> bool:
    """
    Calls Qt's 'bool QLocaleId::operator==(QLocaleId other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocaleid.html#operator==

    Parameters
    ----------

    other : QLocaleId
      Passed on as a value: Qt reads the C++ QLocaleId, which stays Python's
      own.
    """
    #  bool QLocaleId::operator==(QLocaleId other) const
    return self.uglySide.call(
        'ritual_ZNK9QLocaleIdeqES_', self._valueOf(other),
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
  def __ne__(self, other: QLocaleId) -> bool:
    """
    Calls Qt's 'bool QLocaleId::operator!=(QLocaleId other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocaleid.html#operator!=

    Parameters
    ----------

    other : QLocaleId
      Passed on as a value: Qt reads the C++ QLocaleId, which stays Python's
      own.
    """
    #  bool QLocaleId::operator!=(QLocaleId other) const
    return self.uglySide.call(
        'ritual_ZNK9QLocaleIdneES_', self._valueOf(other),
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
  def fromName(*__, **_) -> Never:
    """
    Qt's 'QLocaleId QLocaleId::fromName(QStringView name)': leans on
    'qt_splitLocaleName(QStringView, QStringView*, QStringView*,
    QStringView*)', which Qt's source does not mark for use from outside Qt
    and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QLocaleId.fromName' has no cute function yet. Qt's 'QLocaleId "
        "QLocaleId::fromName(QStringView name)': leans on "
        "'qt_splitLocaleName(QStringView, QStringView*, QStringView*, "
        "QStringView*)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

  @staticmethod
  def name(*__, **_) -> Never:
    """
    Qt's 'QByteArray QLocaleId::name(char separator) const': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: unknown type name 'LanguageCodeEntry'.
    """
    raise NotImplementedError(
        "'QLocaleId.name' has no cute function yet. Qt's 'QByteArray "
        "QLocaleId::name(char separator) const': Qt's library has no name "
        "for it, and its code in Qt's source does not compile apart from "
        "its file: unknown type name 'LanguageCodeEntry'.")

  @staticmethod
  def withLikelySubtagsAdded(*__, **_) -> Never:
    """
    Qt's 'QLocaleId QLocaleId::withLikelySubtagsAdded() const': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: use of undeclared identifier 'likely_subtags'.
    """
    raise NotImplementedError(
        "'QLocaleId.withLikelySubtagsAdded' has no cute function yet. Qt's "
        "'QLocaleId QLocaleId::withLikelySubtagsAdded() const': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'likely_subtags'.")

  @staticmethod
  def withLikelySubtagsRemoved(*__, **_) -> Never:
    """
    Qt's 'QLocaleId QLocaleId::withLikelySubtagsRemoved() const': leans on
    'QLocaleId::withLikelySubtagsAdded() const', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QLocaleId.withLikelySubtagsRemoved' has no cute function yet. "
        "Qt's 'QLocaleId QLocaleId::withLikelySubtagsRemoved() const': "
        "leans on 'QLocaleId::withLikelySubtagsAdded() const', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")
