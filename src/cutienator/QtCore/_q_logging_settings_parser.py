"""
QLoggingSettingsParser binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qloggingregistry_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QLoggingSettingsParser to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from . import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from . import QLoggingRule


class QLoggingSettingsParser(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QLoggingSettingsParser: a plain Python object
  standing in front of one C++ QLoggingSettingsParser.

  C++ hands a QLoggingSettingsParser around as a copy, so every C++
  QLoggingSettingsParser behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QLoggingSettingsParser that has a ritual and that
  Python can call so far, 3 names in all: 'setImplicitRulesSection',
  'setContent', 'rules'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QLoggingSettingsParser::setContent(FILE *stream)': names
    'FILE', which has no cute class yet.
  - Qt's 'QLoggingSettingsParser::~QLoggingSettingsParser()': the destructor:
    Python removes its C++ QLoggingSettingsParser by it, and has no other use
    for it.

  What has no ritual
  ------------------

  1 of the 6 functions Qt declares: 1 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QLoggingSettingsParser is created at the first use, not by
    'QLoggingSettingsParser(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QLoggingSettingsParser back gives a copy the ritual
    made for Python, in a new cute QLoggingSettingsParser.
  - Each name of Qt's QLoggingSettingsParser that has no cute function yet,
    'parseNextLine', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QLoggingSettingsParser'

  #  Qt's '~QLoggingSettingsParser()'. Naming it makes this a value class:
  #  Python owns every C++ QLoggingSettingsParser behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN22QLoggingSettingsParserD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def rules(self) -> QList[QLoggingRule]:
    """
    Calls Qt's 'QList<QLoggingRule> QLoggingSettingsParser::rules() const'.

    Qt's own words: https://doc.qt.io/qt-6/qloggingsettingsparser.html#rules

    Returns
    -------

    QList[QLoggingRule]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QLoggingRule> QLoggingSettingsParser::rules() const
    address = self.uglySide.call(
        'ritual_ZNK22QLoggingSettingsParser5rulesEv',
    )
    from . import QLoggingRule
    return QList[QLoggingRule]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setImplicitRulesSection(self, inRulesSection: bool) -> None:
    """
    Calls Qt's 'void QLoggingSettingsParser::setImplicitRulesSection(bool
    inRulesSection)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qloggingsettingsparser.html

    Parameters
    ----------

    inRulesSection : bool
      Passed on as it is.
    """
    #  void QLoggingSettingsParser::setImplicitRulesSection(bool
    #      inRulesSection)
    self.uglySide.call(
        'ritual_ZN22QLoggingSettingsParser23setImplicitRulesSectionEb',
        inRulesSection,
    )

  @overload(str, int)
  def setContent(self, content: str, separator: int) -> None:
    """
    Calls Qt's 'void QLoggingSettingsParser::setContent(QStringView content,
    char16_t separator)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qloggingsettingsparser.html#setContent

    Parameters
    ----------

    content : str
      Passed on as it is: a QString is made of it for the call.

    separator : int
      Passed on as it is.
    """
    #  void QLoggingSettingsParser::setContent(QStringView content, char16_t
    #      separator)
    self.uglySide.call(
        'ritual_ZN22QLoggingSettingsParser10setContentE11QStringViewDs',
        content, separator,
    )

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

  @staticmethod
  def parseNextLine(*__, **_) -> Never:
    """
    Qt's 'void QLoggingSettingsParser::parseNextLine(QStringView line)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'warnMsg'.
    """
    raise NotImplementedError(
        "'QLoggingSettingsParser.parseNextLine' has no cute function yet. "
        "Qt's 'void QLoggingSettingsParser::parseNextLine(QStringView "
        "line)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'warnMsg'.")
