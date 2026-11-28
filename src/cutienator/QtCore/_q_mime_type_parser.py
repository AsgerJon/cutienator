"""
QMimeTypeParser binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qmimetypeparser_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QMimeTypeParser to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QMimeTypeParserBase

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QMimeGlobPattern, QMimeMagicRuleMatcher, QMimeTypeXMLData
  from . import QString
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMimeGlobPattern = WAIT['QMimeGlobPattern']
  QMimeMagicRuleMatcher = WAIT['QMimeMagicRuleMatcher']
  QMimeTypeXMLData = WAIT['QMimeTypeXMLData']
  QString = WAIT['QString']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QMimeTypeParser(QMimeTypeParserBase):
  """
  The cute side of Qt's QMimeTypeParser: a plain Python object standing in
  front of one C++ QMimeTypeParser.

  It is built on the cute 'QMimeTypeParserBase', as Qt's QMimeTypeParser is
  built on Qt's QMimeTypeParserBase, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QMimeTypeParser that has a ritual and that Python
  can call so far, 4 names in all: 'process', 'processParent',
  'processAlias', 'processMagicMatcher'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QMimeTypeParser::QMimeTypeParser(QMimeXMLProvider &provider)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QMimeTypeParser::~QMimeTypeParser()': the destructor: Python never
    removes a C++ QMimeTypeParser.

  What to expect
  --------------

  - The C++ QMimeTypeParser is created at the first use, not by
    'QMimeTypeParser(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QMimeTypeParser.
  - Each name of Qt's QMimeTypeParser that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QMimeTypeParser'

  #  A C++ QMimeTypeParser Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QMimeTypeParser'

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QMimeTypeParser::QMimeTypeParser(QMimeXMLProvider &provider)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QMimeTypeParser.__init__' has no cute function yet. Qt's "
        "'QMimeTypeParser::QMimeTypeParser(QMimeXMLProvider &provider)': "
        "takes a type Python has no way to hand over yet.")

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

  @overload(QMimeTypeXMLData, QString)
  @overload(QMimeTypeXMLData, NoneType)
  def process(self, t: QMimeTypeXMLData, a1: Optional[QString]) -> bool:
    """
    Calls Qt's 'bool QMimeTypeParser::process(const QMimeTypeXMLData &t,
    QString *a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qmimetypeparser.html#process

    Parameters
    ----------

    t : QMimeTypeXMLData
      Passed on as a value: Qt reads the C++ QMimeTypeXMLData, which stays
      Python's own.

    a1 : Optional[QString]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QMimeTypeParser::process(const QMimeTypeXMLData &t, QString *a1)
    ritual = (
        'ritual_ZN15QMimeTypeParser7processERK16QMimeTypeXMLDataP7QString')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QMimeTypeParser7processERK16QMimeTypeXMLDataP7QSt'
          'ring')
    return self.uglySide.call(ritual, self._valueOf(t), self._addressOf(a1))

  @overload(QMimeGlobPattern, QString)
  @overload(QMimeGlobPattern, NoneType)
  def process(self, glob: QMimeGlobPattern, a1: Optional[QString]) -> bool:
    """
    Calls Qt's 'bool QMimeTypeParser::process(const QMimeGlobPattern &glob,
    QString *a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qmimetypeparser.html#process

    Parameters
    ----------

    glob : QMimeGlobPattern
      Passed on as a value: Qt reads the C++ QMimeGlobPattern, which stays
      Python's own.

    a1 : Optional[QString]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QMimeTypeParser::process(const QMimeGlobPattern &glob, QString
    #      *a1)
    ritual = (
        'ritual_ZN15QMimeTypeParser7processERK16QMimeGlobPatternP7QString')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QMimeTypeParser7processERK16QMimeGlobPatternP7QSt'
          'ring')
    return self.uglySide.call(
        ritual, self._valueOf(glob), self._addressOf(a1),
    )

  @overload(str, str)
  def processParent(self, child: str, parent: str) -> None:
    """
    Calls Qt's 'void QMimeTypeParser::processParent(const QString &child,
    const QString &parent)'.

    Qt's own words: https://doc.qt.io/qt-6/qmimetypeparser.html#processParent

    Parameters
    ----------

    child : str
      Passed on as it is: a QString is made of it for the call.

    parent : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QMimeTypeParser::processParent(const QString &child, const
    #      QString &parent)
    ritual = 'ritual_ZN15QMimeTypeParser13processParentERK7QStringS2_'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QMimeTypeParser13processParentERK7QStringS2_'
    self.uglySide.call(ritual, child, parent)

  @overload(str, str)
  def processAlias(self, alias: str, name: str) -> None:
    """
    Calls Qt's 'void QMimeTypeParser::processAlias(const QString &alias,
    const QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qmimetypeparser.html#processAlias

    Parameters
    ----------

    alias : str
      Passed on as it is: a QString is made of it for the call.

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QMimeTypeParser::processAlias(const QString &alias, const QString
    #      &name)
    ritual = 'ritual_ZN15QMimeTypeParser12processAliasERK7QStringS2_'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QMimeTypeParser12processAliasERK7QStringS2_'
    self.uglySide.call(ritual, alias, name)

  @overload(QMimeMagicRuleMatcher)
  def processMagicMatcher(self, matcher: QMimeMagicRuleMatcher) -> None:
    """
    Calls Qt's 'void QMimeTypeParser::processMagicMatcher(const
    QMimeMagicRuleMatcher &matcher)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmimetypeparser.html#processMagicMatcher

    Parameters
    ----------

    matcher : QMimeMagicRuleMatcher
      Passed on as a value: Qt reads the C++ QMimeMagicRuleMatcher, which
      stays Python's own.
    """
    #  void QMimeTypeParser::processMagicMatcher(const QMimeMagicRuleMatcher
    #      &matcher)
    ritual = (
        'ritual_ZN15QMimeTypeParser19processMagicMatcherERK21QMimeMagicRule'
        'Matcher')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QMimeTypeParser19processMagicMatcherERK21QMimeMag'
          'icRuleMatcher')
    self.uglySide.call(ritual, self._valueOf(matcher))
