"""
QTranslator binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qtranslator.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QLocale, QMetaObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QLocale = WAIT['QLocale']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QTranslator(QObject):
  """
  The cute side of Qt's QTranslator: a plain Python object standing in front
  of one C++ QTranslator.

  It is built on the cute 'QObject', as Qt's QTranslator is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QTranslator that has a ritual and that Python can
  call so far, 7 names in all: 'metaObject', 'tr', 'translate', 'isEmpty',
  'language', 'filePath', 'load'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QTranslator::~QTranslator()': the destructor: Python never removes
    a C++ QTranslator.

  What has no ritual
  ------------------

  9 of the 19 functions Qt declares: 3 takes or gives a type that cannot be
  passed yet; 3 private; 2 forbidden; 1 a template.

  What to expect
  --------------

  - The C++ QTranslator is created at the first use, not by
    'QTranslator(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QTranslator.
  - Qt tells when it has removed the C++ QTranslator. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

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
    Calls Qt's 'QString QTranslator::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qtranslator.html#tr

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
    #  QString QTranslator::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN11QTranslator2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTranslator'

  #  A C++ QTranslator Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QTranslator'

  #  The functions Qt calls itself that QTranslator is the first to declare
  #  and that cannot be handed to Python yet, each as Qt declares it. A class
  #  of a program that writes one of them anew is refused, since Qt would
  #  never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'translate': (
          'QString QTranslator::translate(const char *, const char *, '
          'const char *, int) const',
      ),
  }

  #  The functions Qt calls itself that QTranslator is the first to declare.
  #  A class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'isEmpty': (
          ('_ZNK11QTranslator7isEmptyEv',
           ('bool', 'number', ''),
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

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QTranslator::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtranslator.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QTranslator::metaObject() const
    address = self.uglySide.call('ritual_ZNK11QTranslator10metaObjectEv')
    from . import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, str)
  @overload(str, str, NoneType)
  @overload(str, NoneType, str)
  @overload(str, NoneType, NoneType)
  @overload(NoneType, str, str)
  @overload(NoneType, str, NoneType)
  @overload(NoneType, NoneType, str)
  @overload(NoneType, NoneType, NoneType)
  @overload(str, str, str, int)
  @overload(str, str, NoneType, int)
  @overload(str, NoneType, str, int)
  @overload(str, NoneType, NoneType, int)
  @overload(NoneType, str, str, int)
  @overload(NoneType, str, NoneType, int)
  @overload(NoneType, NoneType, str, int)
  @overload(NoneType, NoneType, NoneType, int)
  def translate(
      self,
      context: Optional[str],
      sourceText: Optional[str],
      disambiguation: Optional[str] = None,
      n: int = -1,
  ) -> str:
    """
    Calls Qt's 'QString QTranslator::translate(const char *context, const
    char *sourceText, const char *disambiguation, int n) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtranslator.html#translate

    Parameters
    ----------

    context : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    sourceText : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    disambiguation : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTranslator::translate(const char *context, const char
    #      *sourceText, const char *disambiguation, int n) const
    return self.uglySide.call(
        'ritual_ZNK11QTranslator9translateEPKcS1_S1_i',
        self._bytesOf(context), self._bytesOf(sourceText),
        self._bytesOf(disambiguation), n,
    )

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QTranslator::isEmpty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtranslator.html#isEmpty
    """
    #  bool QTranslator::isEmpty() const
    ritual = 'ritual_ZNK11QTranslator7isEmptyEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QTranslator7isEmptyEv'
    return self.uglySide.call(ritual)

  def language(self) -> str:
    """
    Calls Qt's 'QString QTranslator::language() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtranslator.html#language

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTranslator::language() const
    return self.uglySide.call('ritual_ZNK11QTranslator8languageEv')

  def filePath(self) -> str:
    """
    Calls Qt's 'QString QTranslator::filePath() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtranslator.html#filePath

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTranslator::filePath() const
    return self.uglySide.call('ritual_ZNK11QTranslator8filePathEv')

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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's 'QTranslator::QTranslator(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtranslator.html#QTranslator

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QTranslator::QTranslator(QObject *parent)
    self._noteCreation(QTranslator, lambda: Rituals.call(
        'ritual_ZN11QTranslatorC1EP7QObject', self._addressOf(parent),
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

  @overload(str)
  @overload(str, str)
  @overload(str, str, str)
  @overload(str, str, str, str)
  def load(
      self,
      filename: str,
      directory: str = '',
      search_delimiters: str = '',
      suffix: str = '',
  ) -> bool:
    """
    Calls Qt's 'bool QTranslator::load(const QString &filename, const QString
    &directory, const QString &search_delimiters, const QString &suffix)'.

    Qt's own words: https://doc.qt.io/qt-6/qtranslator.html#load

    Parameters
    ----------

    filename : str
      Passed on as it is: a QString is made of it for the call.

    directory : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    search_delimiters : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    suffix : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  bool QTranslator::load(const QString &filename, const QString
    #      &directory, const QString &search_delimiters, const QString
    #      &suffix)
    return self.uglySide.call(
        'ritual_ZN11QTranslator4loadERK7QStringS2_S2_S2_',
        filename, directory, search_delimiters, suffix,
    )

  @overload(QLocale, str)
  @overload(QLocale, str, str)
  @overload(QLocale, str, str, str)
  @overload(QLocale, str, str, str, str)
  def load(
      self,
      locale: QLocale,
      filename: str,
      prefix: str = '',
      directory: str = '',
      suffix: str = '',
  ) -> bool:
    """
    Calls Qt's 'bool QTranslator::load(const QLocale &locale, const QString
    &filename, const QString &prefix, const QString &directory, const QString
    &suffix)'.

    Qt's own words: https://doc.qt.io/qt-6/qtranslator.html#load

    Parameters
    ----------

    locale : QLocale
      Passed on as a value: Qt reads the C++ QLocale, which stays Python's
      own.

    filename : str
      Passed on as it is: a QString is made of it for the call.

    prefix : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    directory : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    suffix : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  bool QTranslator::load(const QLocale &locale, const QString &filename,
    #      const QString &prefix, const QString &directory, const QString
    #      &suffix)
    return self.uglySide.call(
        'ritual_ZN11QTranslator4loadERK7QLocaleRK7QStringS5_S5_S5_',
        self._valueOf(locale), filename, prefix, directory, suffix,
    )
