"""
QMimeTypeParserBase binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qmimetypeparser_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QMimeTypeParserBase to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

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


class QMimeTypeParserBase(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QMimeTypeParserBase: a plain Python object standing
  in front of one C++ QMimeTypeParserBase.

  What exists
  -----------

  Every function of Qt's QMimeTypeParserBase that has a ritual and that
  Python can call so far, 4 names in all: 'process', 'processParent',
  'processAlias', 'processMagicMatcher'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QMimeTypeParserBase::~QMimeTypeParserBase()': the destructor:
    Python never removes a C++ QMimeTypeParserBase.
  - Qt's 'bool QMimeTypeParserBase::parseNumber(QStringView n, int *target,
    QString *errorMessage)': takes a number to change where it is.

  What has no ritual
  ------------------

  6 of the 14 functions Qt declares: 4 forbidden; 2 Qt's library has no name
  for it, and its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QMimeTypeParserBase is created at the first use, not by
    'QMimeTypeParserBase(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QMimeTypeParserBase.
  - Each name of Qt's QMimeTypeParserBase that has no cute function yet,
    'nextState', 'parse', 'parseNumber', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QMimeTypeParserBase'

  #  A C++ QMimeTypeParserBase Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QMimeTypeParserBase'

  #  The functions Qt calls itself that QMimeTypeParserBase is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'process': (
          ('_ZN19QMimeTypeParserBase7processERK16QMimeTypeXMLDataP7QString',
           ('bool', 'number', ''),
           (
               ('address', 'value', 'QtCore:QMimeTypeXMLData'),
               ('address', 'address', 'QtCore:QString'),
           )),
          ('_ZN19QMimeTypeParserBase7processERK16QMimeGlobPatternP7QString',
           ('bool', 'number', ''),
           (
               ('address', 'value', 'QtCore:QMimeGlobPattern'),
               ('address', 'address', 'QtCore:QString'),
           )),
      ),
      'processParent': (
          ('_ZN19QMimeTypeParserBase13processParentERK7QStringS2_',
           ('nothing', 'nothing', ''),
           (
               ('address', 'text', ''),
               ('address', 'text', ''),
           )),
      ),
      'processAlias': (
          ('_ZN19QMimeTypeParserBase12processAliasERK7QStringS2_',
           ('nothing', 'nothing', ''),
           (
               ('address', 'text', ''),
               ('address', 'text', ''),
           )),
      ),
      'processMagicMatcher': (
          ('_ZN19QMimeTypeParserBase19processMagicMatcherERK21QMimeMagicRul'
           'eMatcher',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QMimeMagicRuleMatcher'),
           )),
      ),
  }

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
    Notes what was given, for Qt's
    'QMimeTypeParserBase::QMimeTypeParserBase()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qmimetypeparserbase.html#QMimeTypeParserBase
    """
    #  QMimeTypeParserBase::QMimeTypeParserBase()
    self._noteCreation(QMimeTypeParserBase, lambda: Rituals.call(
        'ritual_ZN19QMimeTypeParserBaseC1Ev',
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

  @overload(QMimeTypeXMLData, QString)
  @overload(QMimeTypeXMLData, NoneType)
  def process(
      self,
      t: QMimeTypeXMLData,
      errorMessage: Optional[QString],
  ) -> bool:
    """
    Calls Qt's 'bool QMimeTypeParserBase::process(const QMimeTypeXMLData &t,
    QString *errorMessage)'.

    Qt's own words: https://doc.qt.io/qt-6/qmimetypeparserbase.html#process

    Parameters
    ----------

    t : QMimeTypeXMLData
      Passed on as a value: Qt reads the C++ QMimeTypeXMLData, which stays
      Python's own.

    errorMessage : Optional[QString]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QMimeTypeParserBase::process(const QMimeTypeXMLData &t, QString
    #      *errorMessage)
    return self.uglySide.call(
        'ritual_ZN19QMimeTypeParserBase7processERK16QMimeTypeXMLDataP7QStri'
        'ng',
        self._valueOf(t), self._addressOf(errorMessage),
    )

  @overload(QMimeGlobPattern, QString)
  @overload(QMimeGlobPattern, NoneType)
  def process(
      self,
      t: QMimeGlobPattern,
      errorMessage: Optional[QString],
  ) -> bool:
    """
    Calls Qt's 'bool QMimeTypeParserBase::process(const QMimeGlobPattern &t,
    QString *errorMessage)'.

    Qt's own words: https://doc.qt.io/qt-6/qmimetypeparserbase.html#process

    Parameters
    ----------

    t : QMimeGlobPattern
      Passed on as a value: Qt reads the C++ QMimeGlobPattern, which stays
      Python's own.

    errorMessage : Optional[QString]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QMimeTypeParserBase::process(const QMimeGlobPattern &t, QString
    #      *errorMessage)
    return self.uglySide.call(
        'ritual_ZN19QMimeTypeParserBase7processERK16QMimeGlobPatternP7QStri'
        'ng',
        self._valueOf(t), self._addressOf(errorMessage),
    )

  @overload(str, str)
  def processParent(self, child: str, parent: str) -> None:
    """
    Calls Qt's 'void QMimeTypeParserBase::processParent(const QString &child,
    const QString &parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmimetypeparserbase.html#processParent

    Parameters
    ----------

    child : str
      Passed on as it is: a QString is made of it for the call.

    parent : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QMimeTypeParserBase::processParent(const QString &child, const
    #      QString &parent)
    self.uglySide.call(
        'ritual_ZN19QMimeTypeParserBase13processParentERK7QStringS2_',
        child, parent,
    )

  @overload(str, str)
  def processAlias(self, alias: str, name: str) -> None:
    """
    Calls Qt's 'void QMimeTypeParserBase::processAlias(const QString &alias,
    const QString &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmimetypeparserbase.html#processAlias

    Parameters
    ----------

    alias : str
      Passed on as it is: a QString is made of it for the call.

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QMimeTypeParserBase::processAlias(const QString &alias, const
    #      QString &name)
    self.uglySide.call(
        'ritual_ZN19QMimeTypeParserBase12processAliasERK7QStringS2_',
        alias, name,
    )

  @overload(QMimeMagicRuleMatcher)
  def processMagicMatcher(self, matcher: QMimeMagicRuleMatcher) -> None:
    """
    Calls Qt's 'void QMimeTypeParserBase::processMagicMatcher(const
    QMimeMagicRuleMatcher &matcher)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmimetypeparserbase.html#processMagicMatcher

    Parameters
    ----------

    matcher : QMimeMagicRuleMatcher
      Passed on as a value: Qt reads the C++ QMimeMagicRuleMatcher, which
      stays Python's own.
    """
    #  void QMimeTypeParserBase::processMagicMatcher(const
    #      QMimeMagicRuleMatcher &matcher)
    self.uglySide.call(
        'ritual_ZN19QMimeTypeParserBase19processMagicMatcherERK21QMimeMagic'
        'RuleMatcher',
        self._valueOf(matcher),
    )

  @staticmethod
  def nextState(*__, **_) -> Never:
    """
    Qt's 'ParseState QMimeTypeParserBase::nextState(ParseState currentState,
    QStringView startElement)': Qt's library has no name for it, and its code
    in Qt's source does not compile apart from its file: use of undeclared
    identifier 'mimeTypeTagC'.
    """
    raise NotImplementedError(
        "'QMimeTypeParserBase.nextState' has no cute function yet. Qt's "
        "'ParseState QMimeTypeParserBase::nextState(ParseState "
        "currentState, QStringView startElement)': Qt's library has no name "
        "for it, and its code in Qt's source does not compile apart from "
        "its file: use of undeclared identifier 'mimeTypeTagC'.")

  @staticmethod
  def parse(*__, **_) -> Never:
    """
    Qt's 'bool QMimeTypeParserBase::parse(QIODevice *dev, const QString
    &fileName, QString *errorMessage)': Qt's library has no name for it, and
    its code in Qt's source does not compile apart from its file: use of
    undeclared identifier 'nameAttributeC'.
    """
    raise NotImplementedError(
        "'QMimeTypeParserBase.parse' has no cute function yet. Qt's 'bool "
        "QMimeTypeParserBase::parse(QIODevice *dev, const QString "
        "&fileName, QString *errorMessage)': Qt's library has no name for "
        "it, and its code in Qt's source does not compile apart from its "
        "file: use of undeclared identifier 'nameAttributeC'.")

  @staticmethod
  def parseNumber(*__, **_) -> Never:
    """
    Qt's 'bool QMimeTypeParserBase::parseNumber(QStringView n, int *target,
    QString *errorMessage)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QMimeTypeParserBase.parseNumber' has no cute function yet. Qt's "
        "'bool QMimeTypeParserBase::parseNumber(QStringView n, int *target, "
        "QString *errorMessage)': takes a number to change where it is.")
