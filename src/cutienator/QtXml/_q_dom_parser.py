"""
QDomParser binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtXml/6.12.0/QtXml/private/qdomhelpers_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QDomParser to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QDomDocument

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QXmlStreamReader
  from . import QDomDocumentPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDomDocumentPrivate = WAIT['QDomDocumentPrivate']
  QXmlStreamReader = WAIT['QXmlStreamReader']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDomParser(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QDomParser: a plain Python object standing in front
  of one C++ QDomParser.

  C++ hands a QDomParser around as a copy, so every C++ QDomParser behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QDomParser that has a ritual and that Python can
  call so far, 2 names in all: 'tr', 'result'. It can be made from Python, in
  1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDomParser::~QDomParser()': the destructor: Python removes its C++
    QDomParser by it, and has no other use for it.

  What has no ritual
  ------------------

  4 of the 8 functions Qt declares: 4 leans on 'QDomNodePrivate.

  What to expect
  --------------

  - The C++ QDomParser is created at the first use, not by 'QDomParser(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QDomParser back gives a copy the ritual made for
    Python, in a new cute QDomParser.
  - Each name of Qt's QDomParser that has no cute function yet, 'parse',
    'parseBody', 'parseMarkupDecl', 'parseProlog', holds a function that
    raises 'NotImplementedError', and its docstring says why.
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
  def tr(
      sourceText: Optional[str],
      disambiguation: Optional[str] = None,
      n: int = -1,
  ) -> str:
    """
    Calls Qt's 'QString QDomParser::tr(const char *sourceText, const char
    *disambiguation, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qdomparser.html#tr

    Parameters
    ----------

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
    #  QString QDomParser::tr(const char *sourceText, const char
    #      *disambiguation, int n)
    return Rituals.call(
        'ritual_ZN10QDomParser2trEPKcS1_i',
        CuteMixin._bytesOf(sourceText), CuteMixin._bytesOf(disambiguation),
        n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDomParser'

  #  Qt's '~QDomParser()'. Naming it makes this a value class: Python owns
  #  every C++ QDomParser behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN10QDomParserD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def result(self) -> QDomDocument.ParseResult:
    """
    Calls Qt's 'QDomDocument::ParseResult QDomParser::result() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomparser.html#result

    Returns
    -------

    QDomDocument.ParseResult
      A new cute QDomDocument::ParseResult around the copy Qt gave back.
      Python owns it.
    """
    #  QDomDocument::ParseResult QDomParser::result() const
    address = self.uglySide.call('ritual_ZNK10QDomParser6resultEv')
    return QDomDocument.ParseResult._cuteOwning(address)

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

  @overload(QDomDocumentPrivate, QXmlStreamReader, QDomDocument.ParseOptions)
  @overload(QDomDocumentPrivate, NoneType, QDomDocument.ParseOptions)
  @overload(NoneType, QXmlStreamReader, QDomDocument.ParseOptions)
  @overload(NoneType, NoneType, QDomDocument.ParseOptions)
  def __init__(
      self,
      d: Optional[QDomDocumentPrivate],
      r: Optional[QXmlStreamReader],
      options: QDomDocument.ParseOptions,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QDomParser::QDomParser(QDomDocumentPrivate *d, QXmlStreamReader *r,
    QDomDocument::ParseOptions options)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdomparser.html#QDomParser

    Parameters
    ----------

    d : Optional[QDomDocumentPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    r : Optional[QXmlStreamReader]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    options : QDomDocument.ParseOptions
      Passed on as its number.
    """
    #  QDomParser::QDomParser(QDomDocumentPrivate *d, QXmlStreamReader *r,
    #      QDomDocument::ParseOptions options)
    self._noteCreation(QDomParser, lambda: Rituals.call(
        'ritual_ZN10QDomParserC1EP19QDomDocumentPrivateP16QXmlStreamReader6'
        'QFlagsIN12QDomDocument11ParseOptionEE',
        self._addressOf(d), self._addressOf(r), options.value,
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
  def parse(*__, **_) -> Never:
    """
    Qt's 'bool QDomParser::parse()': leans on
    'QDomNodePrivate::QDomNodePrivate(QDomDocumentPrivate*,
    QDomNodePrivate*)', which Qt's source does not mark for use from outside
    Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDomParser.parse' has no cute function yet. Qt's 'bool "
        "QDomParser::parse()': leans on "
        "'QDomNodePrivate::QDomNodePrivate(QDomDocumentPrivate*, "
        "QDomNodePrivate*)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

  @staticmethod
  def parseBody(*__, **_) -> Never:
    """
    Qt's 'bool QDomParser::parseBody()': leans on
    'QDomNodePrivate::QDomNodePrivate(QDomDocumentPrivate*,
    QDomNodePrivate*)', which Qt's source does not mark for use from outside
    Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDomParser.parseBody' has no cute function yet. Qt's 'bool "
        "QDomParser::parseBody()': leans on "
        "'QDomNodePrivate::QDomNodePrivate(QDomDocumentPrivate*, "
        "QDomNodePrivate*)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

  @staticmethod
  def parseMarkupDecl(*__, **_) -> Never:
    """
    Qt's 'bool QDomParser::parseMarkupDecl()': leans on
    'QDomNodePrivate::QDomNodePrivate(QDomDocumentPrivate*,
    QDomNodePrivate*)', which Qt's source does not mark for use from outside
    Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDomParser.parseMarkupDecl' has no cute function yet. Qt's 'bool "
        "QDomParser::parseMarkupDecl()': leans on "
        "'QDomNodePrivate::QDomNodePrivate(QDomDocumentPrivate*, "
        "QDomNodePrivate*)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

  @staticmethod
  def parseProlog(*__, **_) -> Never:
    """
    Qt's 'bool QDomParser::parseProlog()': leans on
    'QDomNodePrivate::QDomNodePrivate(QDomDocumentPrivate*,
    QDomNodePrivate*)', which Qt's source does not mark for use from outside
    Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDomParser.parseProlog' has no cute function yet. Qt's 'bool "
        "QDomParser::parseProlog()': leans on "
        "'QDomNodePrivate::QDomNodePrivate(QDomDocumentPrivate*, "
        "QDomNodePrivate*)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")
