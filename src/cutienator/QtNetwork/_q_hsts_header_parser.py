"""
QHstsHeaderParser binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/6.12.0/QtNetwork/private/qhsts_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QHstsHeaderParser to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QByteArray, QDateTime
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']


class QHstsHeaderParser(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QHstsHeaderParser: a plain Python object standing in
  front of one C++ QHstsHeaderParser.

  C++ hands a QHstsHeaderParser around as a copy, so every C++
  QHstsHeaderParser behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QHstsHeaderParser that has a ritual and that Python
  can call so far, 3 names in all: 'expirationDate', 'includeSubDomains',
  'processDirective'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QHstsHeaderParser::~QHstsHeaderParser()': the destructor: Python
    removes its C++ QHstsHeaderParser by it, and has no other use for it.

  What has no ritual
  ------------------

  4 of the 8 functions Qt declares: 2 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 2 leans on
  'QHstsHeaderParser.

  What to expect
  --------------

  - The C++ QHstsHeaderParser is created at the first use, not by
    'QHstsHeaderParser(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QHstsHeaderParser back gives a copy the ritual made
    for Python, in a new cute QHstsHeaderParser.
  - Each name of Qt's QHstsHeaderParser that has no cute function yet,
    'nextToken', 'parse', 'parseDirective', 'parseSTSHeader', holds a
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
  __qt_class__ = 'QHstsHeaderParser'

  #  Qt's '~QHstsHeaderParser()'. Naming it makes this a value class: Python
  #  owns every C++ QHstsHeaderParser behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN17QHstsHeaderParserD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def expirationDate(self) -> QDateTime:
    """
    Calls Qt's 'QDateTime QHstsHeaderParser::expirationDate() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhstsheaderparser.html#expirationDate

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QHstsHeaderParser::expirationDate() const
    address = self.uglySide.call(
        'ritual_ZNK17QHstsHeaderParser14expirationDateEv',
    )
    from ..QtCore import QDateTime
    return QDateTime._cuteOwning(address)

  def includeSubDomains(self) -> bool:
    """
    Calls Qt's 'bool QHstsHeaderParser::includeSubDomains() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhstsheaderparser.html#includeSubDomains
    """
    #  bool QHstsHeaderParser::includeSubDomains() const
    return self.uglySide.call(
        'ritual_ZNK17QHstsHeaderParser17includeSubDomainsEv',
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

  @overload(QByteArray, QByteArray)
  def processDirective(self, name: QByteArray, value: QByteArray) -> bool:
    """
    Calls Qt's 'bool QHstsHeaderParser::processDirective(const QByteArray
    &name, const QByteArray &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhstsheaderparser.html#processDirective

    Parameters
    ----------

    name : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    value : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  bool QHstsHeaderParser::processDirective(const QByteArray &name, const
    #      QByteArray &value)
    return self.uglySide.call(
        'ritual_ZN17QHstsHeaderParser16processDirectiveERK10QByteArrayS2_',
        self._valueOf(name), self._valueOf(value),
    )

  @staticmethod
  def nextToken(*__, **_) -> Never:
    """
    Qt's 'bool QHstsHeaderParser::nextToken()': Qt's library has no name for
    it, and its code in Qt's source does not compile apart from its file: use
    of undeclared identifier 'isTOKEN'.
    """
    raise NotImplementedError(
        "'QHstsHeaderParser.nextToken' has no cute function yet. Qt's 'bool "
        "QHstsHeaderParser::nextToken()': Qt's library has no name for it, "
        "and its code in Qt's source does not compile apart from its file: "
        "use of undeclared identifier 'isTOKEN'.")

  @staticmethod
  def parse(*__, **_) -> Never:
    """
    Qt's 'bool QHstsHeaderParser::parse(const QHttpHeaders &headers)': leans
    on 'QHstsHeaderParser::parseDirective()', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QHstsHeaderParser.parse' has no cute function yet. Qt's 'bool "
        "QHstsHeaderParser::parse(const QHttpHeaders &headers)': leans on "
        "'QHstsHeaderParser::parseDirective()', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def parseDirective(*__, **_) -> Never:
    """
    Qt's 'bool QHstsHeaderParser::parseDirective()': Qt's library has no name
    for it, and its code in Qt's source does not compile apart from its file:
    use of undeclared identifier 'isTOKEN'.
    """
    raise NotImplementedError(
        "'QHstsHeaderParser.parseDirective' has no cute function yet. Qt's "
        "'bool QHstsHeaderParser::parseDirective()': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier 'isTOKEN'.")

  @staticmethod
  def parseSTSHeader(*__, **_) -> Never:
    """
    Qt's 'bool QHstsHeaderParser::parseSTSHeader()': leans on
    'QHstsHeaderParser::parseDirective()', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QHstsHeaderParser.parseSTSHeader' has no cute function yet. Qt's "
        "'bool QHstsHeaderParser::parseSTSHeader()': leans on "
        "'QHstsHeaderParser::parseDirective()', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")
