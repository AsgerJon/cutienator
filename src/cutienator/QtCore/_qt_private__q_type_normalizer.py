"""
QtPrivate::QTypeNormalizer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qmetatype.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QTypeNormalizer(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QtPrivate::QTypeNormalizer: a plain Python object
  standing in front of one C++ QtPrivate::QTypeNormalizer.

  C++ hands a QtPrivate::QTypeNormalizer around as a copy, so every C++
  QtPrivate::QTypeNormalizer behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QtPrivate::QTypeNormalizer that has a ritual and
  that Python can call so far, 6 names in all: 'starts_with_token',
  'skipString', 'skipTemplate', 'appendStr', 'normalizeTypeFromSignature',
  'normalizeType'. None can be made from Python: one comes out of a function
  of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'bool QtPrivate::QTypeNormalizer::is_ident_char(char s)': takes a
    single letter as C has it.
  - Qt's 'bool QtPrivate::QTypeNormalizer::is_space(char s)': takes a single
    letter as C has it.
  - Qt's 'bool QtPrivate::QTypeNormalizer::is_number(char s)': takes a single
    letter as C has it.
  - Qt's 'void QtPrivate::QTypeNormalizer::append(char x)': takes a single
    letter as C has it.
  - Qt's 'void QtPrivate::QTypeNormalizer::replaceLast(char x)': takes a
    single letter as C has it.
  - Qt's 'QtPrivate::QTypeNormalizer::~QTypeNormalizer()': the destructor:
    Python removes its C++ QtPrivate::QTypeNormalizer by it, and has no other
    use for it.

  What has no ritual
  ------------------

  4 of the 16 functions Qt declares: 4 takes or gives a type that cannot be
  passed yet.

  What to expect
  --------------

  - The C++ QtPrivate::QTypeNormalizer is created at the first use, not by
    'QtPrivate::QTypeNormalizer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QtPrivate::QTypeNormalizer back gives a copy the
    ritual made for Python, in a new cute QtPrivate::QTypeNormalizer.
  - Each name of Qt's QtPrivate::QTypeNormalizer that has no cute function
    yet, 'append', 'is_ident_char', 'is_number', 'is_space',
    'normalizeIntegerTypes', 'replaceLast', 'skipQtNamespace',
    'skipStructClassOrEnum', 'skipToken', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str, str, str)
  @overload(str, str, NoneType)
  @overload(str, NoneType, str)
  @overload(str, NoneType, NoneType)
  @overload(NoneType, str, str)
  @overload(NoneType, str, NoneType)
  @overload(NoneType, NoneType, str)
  @overload(NoneType, NoneType, NoneType)
  @overload(str, str, str, bool)
  @overload(str, str, NoneType, bool)
  @overload(str, NoneType, str, bool)
  @overload(str, NoneType, NoneType, bool)
  @overload(NoneType, str, str, bool)
  @overload(NoneType, str, NoneType, bool)
  @overload(NoneType, NoneType, str, bool)
  @overload(NoneType, NoneType, NoneType, bool)
  def starts_with_token(
      b: Optional[str],
      e: Optional[str],
      token: Optional[str],
      msvcKw: bool = False,
  ) -> bool:
    """
    Calls Qt's 'bool QtPrivate::QTypeNormalizer::starts_with_token(const char
    *b, const char *e, const char *token, bool msvcKw)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-qtypenormalizer.html#starts_with_token

    Parameters
    ----------

    b : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    e : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    token : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    msvcKw : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  bool QtPrivate::QTypeNormalizer::starts_with_token(const char *b,
    #      const char *e, const char *token, bool msvcKw)
    return Rituals.call(
        'ritual_ZN9QtPrivate15QTypeNormalizer17starts_with_tokenEPKcS2_S2_b',
        CuteMixin._bytesOf(b), CuteMixin._bytesOf(e),
        CuteMixin._bytesOf(token), msvcKw,
    )

  @staticmethod
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  def skipString(x: Optional[str], e: Optional[str]) -> Optional[str]:
    """
    Calls Qt's 'const char *QtPrivate::QTypeNormalizer::skipString(const char
    *x, const char *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-qtypenormalizer.html#skipString

    Parameters
    ----------

    x : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    e : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    Returns
    -------

    Optional[str]
      The text Qt gave back. None when Qt gave back no text.
    """
    #  const char *QtPrivate::QTypeNormalizer::skipString(const char *x,
    #      const char *e)
    chars = Rituals.call(
        'ritual_ZN9QtPrivate15QTypeNormalizer10skipStringEPKcS2_',
        CuteMixin._bytesOf(x), CuteMixin._bytesOf(e),
    )
    return None if chars is None else chars.decode()

  @staticmethod
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, bool)
  @overload(str, NoneType, bool)
  @overload(NoneType, str, bool)
  @overload(NoneType, NoneType, bool)
  def skipTemplate(
      x: Optional[str],
      e: Optional[str],
      stopAtComa: bool = False,
  ) -> Optional[str]:
    """
    Calls Qt's 'const char *QtPrivate::QTypeNormalizer::skipTemplate(const
    char *x, const char *e, bool stopAtComa)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-qtypenormalizer.html#skipTemplate

    Parameters
    ----------

    x : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    e : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    stopAtComa : bool
      Passed on as it is. May be left out, as in Qt: it is then False.

    Returns
    -------

    Optional[str]
      The text Qt gave back. None when Qt gave back no text.
    """
    #  const char *QtPrivate::QTypeNormalizer::skipTemplate(const char *x,
    #      const char *e, bool stopAtComa)
    chars = Rituals.call(
        'ritual_ZN9QtPrivate15QTypeNormalizer12skipTemplateEPKcS2_b',
        CuteMixin._bytesOf(x), CuteMixin._bytesOf(e), stopAtComa,
    )
    return None if chars is None else chars.decode()

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtPrivate::QTypeNormalizer'

  #  Qt's '~QtPrivate::QTypeNormalizer()'. Naming it makes this a value
  #  class: Python owns every C++ QtPrivate::QTypeNormalizer behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN9QtPrivate15QTypeNormalizerD1Ev'

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
  @overload(NoneType)
  def appendStr(self, x: Optional[str]) -> None:
    """
    Calls Qt's 'void QtPrivate::QTypeNormalizer::appendStr(const char *x)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-qtypenormalizer.html#appendStr

    Parameters
    ----------

    x : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  void QtPrivate::QTypeNormalizer::appendStr(const char *x)
    self.uglySide.call(
        'ritual_ZN9QtPrivate15QTypeNormalizer9appendStrEPKc',
        self._bytesOf(x),
    )

  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  def normalizeTypeFromSignature(
      self,
      begin: Optional[str],
      end: Optional[str],
  ) -> int:
    """
    Calls Qt's 'int
    QtPrivate::QTypeNormalizer::normalizeTypeFromSignature(const char *begin,
    const char *end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-qtypenormalizer.html

    Parameters
    ----------

    begin : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    end : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  int QtPrivate::QTypeNormalizer::normalizeTypeFromSignature(const char
    #      *begin, const char *end)
    return self.uglySide.call(
        'ritual_ZN9QtPrivate15QTypeNormalizer26normalizeTypeFromSignatureEP'
        'KcS2_',
        self._bytesOf(begin), self._bytesOf(end),
    )

  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, bool)
  @overload(str, NoneType, bool)
  @overload(NoneType, str, bool)
  @overload(NoneType, NoneType, bool)
  def normalizeType(
      self,
      begin: Optional[str],
      end: Optional[str],
      adjustConst: bool = True,
  ) -> int:
    """
    Calls Qt's 'int QtPrivate::QTypeNormalizer::normalizeType(const char
    *begin, const char *end, bool adjustConst)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-qtypenormalizer.html#normalizeType

    Parameters
    ----------

    begin : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    end : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    adjustConst : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  int QtPrivate::QTypeNormalizer::normalizeType(const char *begin, const
    #      char *end, bool adjustConst)
    return self.uglySide.call(
        'ritual_ZN9QtPrivate15QTypeNormalizer13normalizeTypeEPKcS2_b',
        self._bytesOf(begin), self._bytesOf(end), adjustConst,
    )

  @staticmethod
  def append(*__, **_) -> Never:
    """
    Qt's 'void QtPrivate::QTypeNormalizer::append(char x)': takes a single
    letter as C has it.
    """
    raise NotImplementedError(
        "'QtPrivate.QTypeNormalizer.append' has no cute function yet. Qt's "
        "'void QtPrivate::QTypeNormalizer::append(char x)': takes a single "
        "letter as C has it.")

  @staticmethod
  def is_ident_char(*__, **_) -> Never:
    """
    Qt's 'bool QtPrivate::QTypeNormalizer::is_ident_char(char s)': takes a
    single letter as C has it.
    """
    raise NotImplementedError(
        "'QtPrivate.QTypeNormalizer.is_ident_char' has no cute function "
        "yet. Qt's 'bool QtPrivate::QTypeNormalizer::is_ident_char(char "
        "s)': takes a single letter as C has it.")

  @staticmethod
  def is_number(*__, **_) -> Never:
    """
    Qt's 'bool QtPrivate::QTypeNormalizer::is_number(char s)': takes a single
    letter as C has it.
    """
    raise NotImplementedError(
        "'QtPrivate.QTypeNormalizer.is_number' has no cute function yet. "
        "Qt's 'bool QtPrivate::QTypeNormalizer::is_number(char s)': takes a "
        "single letter as C has it.")

  @staticmethod
  def is_space(*__, **_) -> Never:
    """
    Qt's 'bool QtPrivate::QTypeNormalizer::is_space(char s)': takes a single
    letter as C has it.
    """
    raise NotImplementedError(
        "'QtPrivate.QTypeNormalizer.is_space' has no cute function yet. "
        "Qt's 'bool QtPrivate::QTypeNormalizer::is_space(char s)': takes a "
        "single letter as C has it.")

  @staticmethod
  def normalizeIntegerTypes(*__, **_) -> Never:
    """
    Qt's 'void QtPrivate::QTypeNormalizer::normalizeIntegerTypes(const char
    *&begin, const char *end)': takes or gives a type that cannot be passed
    yet: const char *&.
    """
    raise NotImplementedError(
        "'QtPrivate.QTypeNormalizer.normalizeIntegerTypes' has no cute "
        "function yet. Qt's 'void "
        "QtPrivate::QTypeNormalizer::normalizeIntegerTypes(const char "
        "*&begin, const char *end)': takes or gives a type that cannot be "
        "passed yet: const char *&.")

  @staticmethod
  def replaceLast(*__, **_) -> Never:
    """
    Qt's 'void QtPrivate::QTypeNormalizer::replaceLast(char x)': takes a
    single letter as C has it.
    """
    raise NotImplementedError(
        "'QtPrivate.QTypeNormalizer.replaceLast' has no cute function yet. "
        "Qt's 'void QtPrivate::QTypeNormalizer::replaceLast(char x)': takes "
        "a single letter as C has it.")

  @staticmethod
  def skipQtNamespace(*__, **_) -> Never:
    """
    Qt's 'void QtPrivate::QTypeNormalizer::skipQtNamespace(const char
    *&begin, const char *end)': takes or gives a type that cannot be passed
    yet: const char *&.
    """
    raise NotImplementedError(
        "'QtPrivate.QTypeNormalizer.skipQtNamespace' has no cute function "
        "yet. Qt's 'void QtPrivate::QTypeNormalizer::skipQtNamespace(const "
        "char *&begin, const char *end)': takes or gives a type that cannot "
        "be passed yet: const char *&.")

  @staticmethod
  def skipStructClassOrEnum(*__, **_) -> Never:
    """
    Qt's 'void QtPrivate::QTypeNormalizer::skipStructClassOrEnum(const char
    *&begin, const char *end)': takes or gives a type that cannot be passed
    yet: const char *&.
    """
    raise NotImplementedError(
        "'QtPrivate.QTypeNormalizer.skipStructClassOrEnum' has no cute "
        "function yet. Qt's 'void "
        "QtPrivate::QTypeNormalizer::skipStructClassOrEnum(const char "
        "*&begin, const char *end)': takes or gives a type that cannot be "
        "passed yet: const char *&.")

  @staticmethod
  def skipToken(*__, **_) -> Never:
    """
    Qt's 'bool QtPrivate::QTypeNormalizer::skipToken(const char *&x, const
    char *e, const char *token, bool msvcKw)': takes or gives a type that
    cannot be passed yet: const char *&.
    """
    raise NotImplementedError(
        "'QtPrivate.QTypeNormalizer.skipToken' has no cute function yet. "
        "Qt's 'bool QtPrivate::QTypeNormalizer::skipToken(const char *&x, "
        "const char *e, const char *token, bool msvcKw)': takes or gives a "
        "type that cannot be passed yet: const char *&.")
