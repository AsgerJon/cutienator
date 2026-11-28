"""
QXmlSimpleReaderPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore5Compat/6.12.0/QtCore5Compat/private/qxml_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QXmlSimpleReaderPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QString
  from . import QXmlInputSource, QXmlSimpleReader
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QString = WAIT['QString']
  QXmlInputSource = WAIT['QXmlInputSource']
  QXmlSimpleReader = WAIT['QXmlSimpleReader']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QXmlSimpleReaderPrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QXmlSimpleReaderPrivate: a plain Python object
  standing in front of one C++ QXmlSimpleReaderPrivate.

  What exists
  -----------

  Every function of Qt's QXmlSimpleReaderPrivate that has a ritual and that
  Python can call so far, 21 names in all: 'initIncrementalParsing',
  'string', 'stringClear', 'stringAddC', 'nameClear', 'nameAddC', 'refClear',
  'refAddC', 'next', 'atEnd', 'init', 'initData', 'entityExist',
  'processElementEmptyTag', 'processElementAttribute', 'processReference',
  'insertXmlRef', 'reportEndEntities', 'reportParseError',
  'isExpandedEntityValueTooLarge', 'q_func'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QXmlSimpleReaderPrivate::~QXmlSimpleReaderPrivate()': the
    destructor: Python never removes a C++ QXmlSimpleReaderPrivate.
  - Qt's 'const QXmlSimpleReader *QXmlSimpleReaderPrivate::q_func() const':
    takes in Python what 'QXmlSimpleReader
    *QXmlSimpleReaderPrivate::q_func()' takes.

  What has no ritual
  ------------------

  41 of the 65 functions Qt declares: 29 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 8 leans on
  'QXmlSimpleReaderPrivate; 4 takes or gives a type that cannot be passed
  yet.

  What to expect
  --------------

  - The C++ QXmlSimpleReaderPrivate is created at the first use, not by
    'QXmlSimpleReaderPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QXmlSimpleReaderPrivate.
  - Each name of Qt's QXmlSimpleReaderPrivate that has no cute function yet,
    'eat_ws', 'name', 'next_eat_ws', 'parseAttType', 'parseAttValue',
    'parseAttlistDecl', 'parseAttribute', 'parseBeginOrContinue',
    'parseChoiceSeq', 'parseChoiceSeqFrame', 'parseComment', 'parseContent',
    'parseContentFrame', 'parseDoctype', 'parseElement', 'parseElementDecl',
    'parseElementFrame', 'parseEntityDecl', 'parseEntityValue',
    'parseExternalID', 'parseFailed', 'parseMarkupdecl', 'parseMisc',
    'parseName', 'parseNestedFrames', 'parseNmtoken', 'parseNotationDecl',
    'parsePEReference', 'parsePI', 'parseProlog', 'parseReference',
    'parseString', 'processElementETagBegin2', 'pushParseState', 'ref',
    'resumeSuspendedCall', 'tryUnwindParseStack', 'unexpectedEof', holds a
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
  __qt_class__ = 'QXmlSimpleReaderPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def entityExist(self, a0: str) -> bool:
    """
    Calls Qt's 'bool QXmlSimpleReaderPrivate::entityExist(const QString &a0)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlsimplereaderprivate.html#entityExist

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QXmlSimpleReaderPrivate::entityExist(const QString &a0) const
    return self.uglySide.call(
        'ritual_ZNK23QXmlSimpleReaderPrivate11entityExistERK7QString', a0,
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

  @overload(QXmlSimpleReader)
  @overload(NoneType)
  def __init__(self, reader: Optional[QXmlSimpleReader]) -> None:
    """
    Notes what was given, for Qt's
    'QXmlSimpleReaderPrivate::QXmlSimpleReaderPrivate(QXmlSimpleReader
    *reader)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlsimplereaderprivate.html

    Parameters
    ----------

    reader : Optional[QXmlSimpleReader]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QXmlSimpleReaderPrivate::QXmlSimpleReaderPrivate(QXmlSimpleReader
    #      *reader)
    self._noteCreation(QXmlSimpleReaderPrivate, lambda: Rituals.call(
        'ritual_ZN23QXmlSimpleReaderPrivateC1EP16QXmlSimpleReader',
        self._addressOf(reader),
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

  def initIncrementalParsing(self) -> None:
    """
    Calls Qt's 'void QXmlSimpleReaderPrivate::initIncrementalParsing()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlsimplereaderprivate.html
    """
    #  void QXmlSimpleReaderPrivate::initIncrementalParsing()
    self.uglySide.call(
        'ritual_ZN23QXmlSimpleReaderPrivate22initIncrementalParsingEv',
    )

  def string(self) -> str:
    """
    Calls Qt's 'const QString &QXmlSimpleReaderPrivate::string()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlsimplereaderprivate.html#string

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  const QString &QXmlSimpleReaderPrivate::string()
    return self.uglySide.call('ritual_ZN23QXmlSimpleReaderPrivate6stringEv')

  def stringClear(self) -> None:
    """
    Calls Qt's 'void QXmlSimpleReaderPrivate::stringClear()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlsimplereaderprivate.html#stringClear
    """
    #  void QXmlSimpleReaderPrivate::stringClear()
    self.uglySide.call('ritual_ZN23QXmlSimpleReaderPrivate11stringClearEv')

  def stringAddC(self) -> None:
    """
    Calls Qt's 'void QXmlSimpleReaderPrivate::stringAddC()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlsimplereaderprivate.html#stringAddC
    """
    #  void QXmlSimpleReaderPrivate::stringAddC()
    self.uglySide.call('ritual_ZN23QXmlSimpleReaderPrivate10stringAddCEv')

  def nameClear(self) -> None:
    """
    Calls Qt's 'void QXmlSimpleReaderPrivate::nameClear()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlsimplereaderprivate.html#nameClear
    """
    #  void QXmlSimpleReaderPrivate::nameClear()
    self.uglySide.call('ritual_ZN23QXmlSimpleReaderPrivate9nameClearEv')

  def nameAddC(self) -> None:
    """
    Calls Qt's 'void QXmlSimpleReaderPrivate::nameAddC()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlsimplereaderprivate.html#nameAddC
    """
    #  void QXmlSimpleReaderPrivate::nameAddC()
    self.uglySide.call('ritual_ZN23QXmlSimpleReaderPrivate8nameAddCEv')

  def refClear(self) -> None:
    """
    Calls Qt's 'void QXmlSimpleReaderPrivate::refClear()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlsimplereaderprivate.html#refClear
    """
    #  void QXmlSimpleReaderPrivate::refClear()
    self.uglySide.call('ritual_ZN23QXmlSimpleReaderPrivate8refClearEv')

  def refAddC(self) -> None:
    """
    Calls Qt's 'void QXmlSimpleReaderPrivate::refAddC()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlsimplereaderprivate.html#refAddC
    """
    #  void QXmlSimpleReaderPrivate::refAddC()
    self.uglySide.call('ritual_ZN23QXmlSimpleReaderPrivate7refAddCEv')

  def next(self) -> None:
    """
    Calls Qt's 'void QXmlSimpleReaderPrivate::next()'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlsimplereaderprivate.html#next
    """
    #  void QXmlSimpleReaderPrivate::next()
    self.uglySide.call('ritual_ZN23QXmlSimpleReaderPrivate4nextEv')

  def atEnd(self) -> bool:
    """
    Calls Qt's 'bool QXmlSimpleReaderPrivate::atEnd()'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlsimplereaderprivate.html#atEnd
    """
    #  bool QXmlSimpleReaderPrivate::atEnd()
    return self.uglySide.call('ritual_ZN23QXmlSimpleReaderPrivate5atEndEv')

  @overload(QXmlInputSource)
  @overload(NoneType)
  def init(self, i: Optional[QXmlInputSource]) -> None:
    """
    Calls Qt's 'void QXmlSimpleReaderPrivate::init(const QXmlInputSource
    *i)'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlsimplereaderprivate.html#init

    Parameters
    ----------

    i : Optional[QXmlInputSource]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QXmlSimpleReaderPrivate::init(const QXmlInputSource *i)
    self.uglySide.call(
        'ritual_ZN23QXmlSimpleReaderPrivate4initEPK15QXmlInputSource',
        self._addressOf(i),
    )

  def initData(self) -> None:
    """
    Calls Qt's 'void QXmlSimpleReaderPrivate::initData()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlsimplereaderprivate.html#initData
    """
    #  void QXmlSimpleReaderPrivate::initData()
    self.uglySide.call('ritual_ZN23QXmlSimpleReaderPrivate8initDataEv')

  def processElementEmptyTag(self) -> bool:
    """
    Calls Qt's 'bool QXmlSimpleReaderPrivate::processElementEmptyTag()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlsimplereaderprivate.html
    """
    #  bool QXmlSimpleReaderPrivate::processElementEmptyTag()
    return self.uglySide.call(
        'ritual_ZN23QXmlSimpleReaderPrivate22processElementEmptyTagEv',
    )

  def processElementAttribute(self) -> bool:
    """
    Calls Qt's 'bool QXmlSimpleReaderPrivate::processElementAttribute()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlsimplereaderprivate.html
    """
    #  bool QXmlSimpleReaderPrivate::processElementAttribute()
    return self.uglySide.call(
        'ritual_ZN23QXmlSimpleReaderPrivate23processElementAttributeEv',
    )

  def processReference(self) -> bool:
    """
    Calls Qt's 'bool QXmlSimpleReaderPrivate::processReference()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlsimplereaderprivate.html#processReference
    """
    #  bool QXmlSimpleReaderPrivate::processReference()
    return self.uglySide.call(
        'ritual_ZN23QXmlSimpleReaderPrivate16processReferenceEv',
    )

  @overload(str, str, bool)
  def insertXmlRef(self, a0: str, a1: str, a2: bool) -> bool:
    """
    Calls Qt's 'bool QXmlSimpleReaderPrivate::insertXmlRef(const QString &a0,
    const QString &a1, bool a2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlsimplereaderprivate.html#insertXmlRef

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.

    a1 : str
      Passed on as it is: a QString is made of it for the call.

    a2 : bool
      Passed on as it is.
    """
    #  bool QXmlSimpleReaderPrivate::insertXmlRef(const QString &a0, const
    #      QString &a1, bool a2)
    return self.uglySide.call(
        'ritual_ZN23QXmlSimpleReaderPrivate12insertXmlRefERK7QStringS2_b',
        a0, a1, a2,
    )

  def reportEndEntities(self) -> bool:
    """
    Calls Qt's 'bool QXmlSimpleReaderPrivate::reportEndEntities()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlsimplereaderprivate.html#reportEndEntities
    """
    #  bool QXmlSimpleReaderPrivate::reportEndEntities()
    return self.uglySide.call(
        'ritual_ZN23QXmlSimpleReaderPrivate17reportEndEntitiesEv',
    )

  @overload(str)
  def reportParseError(self, error: str) -> None:
    """
    Calls Qt's 'void QXmlSimpleReaderPrivate::reportParseError(const QString
    &error)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlsimplereaderprivate.html#reportParseError

    Parameters
    ----------

    error : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QXmlSimpleReaderPrivate::reportParseError(const QString &error)
    self.uglySide.call(
        'ritual_ZN23QXmlSimpleReaderPrivate16reportParseErrorERK7QString',
        error,
    )

  @overload(QString)
  @overload(NoneType)
  def isExpandedEntityValueTooLarge(
      self,
      errorMessage: Optional[QString],
  ) -> bool:
    """
    Calls Qt's 'bool
    QXmlSimpleReaderPrivate::isExpandedEntityValueTooLarge(QString
    *errorMessage)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlsimplereaderprivate.html

    Parameters
    ----------

    errorMessage : Optional[QString]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QXmlSimpleReaderPrivate::isExpandedEntityValueTooLarge(QString
    #      *errorMessage)
    return self.uglySide.call(
        'ritual_ZN23QXmlSimpleReaderPrivate29isExpandedEntityValueTooLargeE'
        'P7QString',
        self._addressOf(errorMessage),
    )

  def q_func(self) -> Optional[QXmlSimpleReader]:
    """
    Calls Qt's 'QXmlSimpleReader *QXmlSimpleReaderPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlsimplereaderprivate.html#q_func

    Returns
    -------

    Optional[QXmlSimpleReader]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QXmlSimpleReader *QXmlSimpleReaderPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN23QXmlSimpleReaderPrivate6q_funcEv',
    )
    from . import QXmlSimpleReader
    return QXmlSimpleReader._cuteAt(address)

  @staticmethod
  def eat_ws(*__, **_) -> Never:
    """
    Qt's 'bool QXmlSimpleReaderPrivate::eat_ws()': leans on
    'QXmlSimpleReaderPrivate::unexpectedEof(bool
    (QXmlSimpleReaderPrivate::*)(), int)', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QXmlSimpleReaderPrivate.eat_ws' has no cute function yet. Qt's "
        "'bool QXmlSimpleReaderPrivate::eat_ws()': leans on "
        "'QXmlSimpleReaderPrivate::unexpectedEof(bool "
        "(QXmlSimpleReaderPrivate::*)(), int)', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def name(*__, **_) -> Never:
    """
    Qt's 'const QString &QXmlSimpleReaderPrivate::name()': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: use of undeclared identifier 'updateValue'.
    """
    raise NotImplementedError(
        "'QXmlSimpleReaderPrivate.name' has no cute function yet. Qt's "
        "'const QString &QXmlSimpleReaderPrivate::name()': Qt's library has "
        "no name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier 'updateValue'.")

  @staticmethod
  def next_eat_ws(*__, **_) -> Never:
    """
    Qt's 'bool QXmlSimpleReaderPrivate::next_eat_ws()': leans on
    'QXmlSimpleReaderPrivate::unexpectedEof(bool
    (QXmlSimpleReaderPrivate::*)(), int)', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QXmlSimpleReaderPrivate.next_eat_ws' has no cute function yet. "
        "Qt's 'bool QXmlSimpleReaderPrivate::next_eat_ws()': leans on "
        "'QXmlSimpleReaderPrivate::unexpectedEof(bool "
        "(QXmlSimpleReaderPrivate::*)(), int)', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def parseAttType(*__, **_) -> Never:
    """
    Qt's 'bool QXmlSimpleReaderPrivate::parseAttType()': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: use of undeclared identifier 'ItemInitState'.
    """
    raise NotImplementedError(
        "'QXmlSimpleReaderPrivate.parseAttType' has no cute function yet. "
        "Qt's 'bool QXmlSimpleReaderPrivate::parseAttType()': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier 'ItemInitState'.")

  @staticmethod
  def parseAttValue(*__, **_) -> Never:
    """
    Qt's 'bool QXmlSimpleReaderPrivate::parseAttValue()': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: use of undeclared identifier 'ItemInitState'.
    """
    raise NotImplementedError(
        "'QXmlSimpleReaderPrivate.parseAttValue' has no cute function yet. "
        "Qt's 'bool QXmlSimpleReaderPrivate::parseAttValue()': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier 'ItemInitState'.")

  @staticmethod
  def parseAttlistDecl(*__, **_) -> Never:
    """
    Qt's 'bool QXmlSimpleReaderPrivate::parseAttlistDecl()': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: use of undeclared identifier 'ItemInitState'.
    """
    raise NotImplementedError(
        "'QXmlSimpleReaderPrivate.parseAttlistDecl' has no cute function "
        "yet. Qt's 'bool QXmlSimpleReaderPrivate::parseAttlistDecl()': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'ItemInitState'.")

  @staticmethod
  def parseAttribute(*__, **_) -> Never:
    """
    Qt's 'bool QXmlSimpleReaderPrivate::parseAttribute()': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: use of undeclared identifier 'ItemInitState'.
    """
    raise NotImplementedError(
        "'QXmlSimpleReaderPrivate.parseAttribute' has no cute function yet. "
        "Qt's 'bool QXmlSimpleReaderPrivate::parseAttribute()': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'ItemInitState'.")

  @staticmethod
  def parseBeginOrContinue(*__, **_) -> Never:
    """
    Qt's 'bool QXmlSimpleReaderPrivate::parseBeginOrContinue(int state, bool
    incremental)': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: use of undeclared identifier
    'clear'.
    """
    raise NotImplementedError(
        "'QXmlSimpleReaderPrivate.parseBeginOrContinue' has no cute "
        "function yet. Qt's 'bool "
        "QXmlSimpleReaderPrivate::parseBeginOrContinue(int state, bool "
        "incremental)': Qt's library has no name for it, and its code in "
        "Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'clear'.")

  @staticmethod
  def parseChoiceSeq(*__, **_) -> Never:
    """
    Qt's 'bool QXmlSimpleReaderPrivate::parseChoiceSeq()': leans on
    'QXmlSimpleReaderPrivate::unexpectedEof(bool
    (QXmlSimpleReaderPrivate::*)(), int)', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QXmlSimpleReaderPrivate.parseChoiceSeq' has no cute function yet. "
        "Qt's 'bool QXmlSimpleReaderPrivate::parseChoiceSeq()': leans on "
        "'QXmlSimpleReaderPrivate::unexpectedEof(bool "
        "(QXmlSimpleReaderPrivate::*)(), int)', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def parseChoiceSeqFrame(*__, **_) -> Never:
    """
    Qt's 'FrameParseResult QXmlSimpleReaderPrivate::parseChoiceSeqFrame(int
    &state)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: use of undeclared identifier
    'ItemInitState'.
    """
    raise NotImplementedError(
        "'QXmlSimpleReaderPrivate.parseChoiceSeqFrame' has no cute function "
        "yet. Qt's 'FrameParseResult "
        "QXmlSimpleReaderPrivate::parseChoiceSeqFrame(int &state)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'ItemInitState'.")

  @staticmethod
  def parseComment(*__, **_) -> Never:
    """
    Qt's 'bool QXmlSimpleReaderPrivate::parseComment()': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: use of undeclared identifier 'ItemInitState'.
    """
    raise NotImplementedError(
        "'QXmlSimpleReaderPrivate.parseComment' has no cute function yet. "
        "Qt's 'bool QXmlSimpleReaderPrivate::parseComment()': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier 'ItemInitState'.")

  @staticmethod
  def parseContent(*__, **_) -> Never:
    """
    Qt's 'bool QXmlSimpleReaderPrivate::parseContent()': leans on
    'QXmlSimpleReaderPrivate::unexpectedEof(bool
    (QXmlSimpleReaderPrivate::*)(), int)', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QXmlSimpleReaderPrivate.parseContent' has no cute function yet. "
        "Qt's 'bool QXmlSimpleReaderPrivate::parseContent()': leans on "
        "'QXmlSimpleReaderPrivate::unexpectedEof(bool "
        "(QXmlSimpleReaderPrivate::*)(), int)', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def parseContentFrame(*__, **_) -> Never:
    """
    Qt's 'FrameParseResult QXmlSimpleReaderPrivate::parseContentFrame(int
    &state)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: use of undeclared identifier
    'ItemInitState'.
    """
    raise NotImplementedError(
        "'QXmlSimpleReaderPrivate.parseContentFrame' has no cute function "
        "yet. Qt's 'FrameParseResult "
        "QXmlSimpleReaderPrivate::parseContentFrame(int &state)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'ItemInitState'.")

  @staticmethod
  def parseDoctype(*__, **_) -> Never:
    """
    Qt's 'bool QXmlSimpleReaderPrivate::parseDoctype()': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: use of undeclared identifier 'ItemInitState'.
    """
    raise NotImplementedError(
        "'QXmlSimpleReaderPrivate.parseDoctype' has no cute function yet. "
        "Qt's 'bool QXmlSimpleReaderPrivate::parseDoctype()': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier 'ItemInitState'.")

  @staticmethod
  def parseElement(*__, **_) -> Never:
    """
    Qt's 'bool QXmlSimpleReaderPrivate::parseElement()': leans on
    'QXmlSimpleReaderPrivate::unexpectedEof(bool
    (QXmlSimpleReaderPrivate::*)(), int)', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QXmlSimpleReaderPrivate.parseElement' has no cute function yet. "
        "Qt's 'bool QXmlSimpleReaderPrivate::parseElement()': leans on "
        "'QXmlSimpleReaderPrivate::unexpectedEof(bool "
        "(QXmlSimpleReaderPrivate::*)(), int)', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def parseElementDecl(*__, **_) -> Never:
    """
    Qt's 'bool QXmlSimpleReaderPrivate::parseElementDecl()': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: use of undeclared identifier 'ItemInitState'.
    """
    raise NotImplementedError(
        "'QXmlSimpleReaderPrivate.parseElementDecl' has no cute function "
        "yet. Qt's 'bool QXmlSimpleReaderPrivate::parseElementDecl()': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'ItemInitState'.")

  @staticmethod
  def parseElementFrame(*__, **_) -> Never:
    """
    Qt's 'FrameParseResult QXmlSimpleReaderPrivate::parseElementFrame(int
    &state)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: use of undeclared identifier
    'ItemInitState'.
    """
    raise NotImplementedError(
        "'QXmlSimpleReaderPrivate.parseElementFrame' has no cute function "
        "yet. Qt's 'FrameParseResult "
        "QXmlSimpleReaderPrivate::parseElementFrame(int &state)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'ItemInitState'.")

  @staticmethod
  def parseEntityDecl(*__, **_) -> Never:
    """
    Qt's 'bool QXmlSimpleReaderPrivate::parseEntityDecl()': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: use of undeclared identifier 'ItemInitState'.
    """
    raise NotImplementedError(
        "'QXmlSimpleReaderPrivate.parseEntityDecl' has no cute function "
        "yet. Qt's 'bool QXmlSimpleReaderPrivate::parseEntityDecl()': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'ItemInitState'.")

  @staticmethod
  def parseEntityValue(*__, **_) -> Never:
    """
    Qt's 'bool QXmlSimpleReaderPrivate::parseEntityValue()': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: use of undeclared identifier 'ItemInitState'.
    """
    raise NotImplementedError(
        "'QXmlSimpleReaderPrivate.parseEntityValue' has no cute function "
        "yet. Qt's 'bool QXmlSimpleReaderPrivate::parseEntityValue()': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'ItemInitState'.")

  @staticmethod
  def parseExternalID(*__, **_) -> Never:
    """
    Qt's 'bool QXmlSimpleReaderPrivate::parseExternalID()': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: use of undeclared identifier 'ItemInitState'.
    """
    raise NotImplementedError(
        "'QXmlSimpleReaderPrivate.parseExternalID' has no cute function "
        "yet. Qt's 'bool QXmlSimpleReaderPrivate::parseExternalID()': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'ItemInitState'.")

  @staticmethod
  def parseFailed(*__, **_) -> Never:
    """
    Qt's 'void QXmlSimpleReaderPrivate::parseFailed(ParseFunction where, int
    state)': takes or gives a type that cannot be passed yet: bool
    (QXmlSimpleReaderPrivate::*)().
    """
    raise NotImplementedError(
        "'QXmlSimpleReaderPrivate.parseFailed' has no cute function yet. "
        "Qt's 'void QXmlSimpleReaderPrivate::parseFailed(ParseFunction "
        "where, int state)': takes or gives a type that cannot be passed "
        "yet: bool (QXmlSimpleReaderPrivate::*)().")

  @staticmethod
  def parseMarkupdecl(*__, **_) -> Never:
    """
    Qt's 'bool QXmlSimpleReaderPrivate::parseMarkupdecl()': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: use of undeclared identifier 'ItemInitState'.
    """
    raise NotImplementedError(
        "'QXmlSimpleReaderPrivate.parseMarkupdecl' has no cute function "
        "yet. Qt's 'bool QXmlSimpleReaderPrivate::parseMarkupdecl()': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'ItemInitState'.")

  @staticmethod
  def parseMisc(*__, **_) -> Never:
    """
    Qt's 'bool QXmlSimpleReaderPrivate::parseMisc()': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: use of undeclared identifier 'ItemInitState'.
    """
    raise NotImplementedError(
        "'QXmlSimpleReaderPrivate.parseMisc' has no cute function yet. Qt's "
        "'bool QXmlSimpleReaderPrivate::parseMisc()': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier 'ItemInitState'.")

  @staticmethod
  def parseName(*__, **_) -> Never:
    """
    Qt's 'bool QXmlSimpleReaderPrivate::parseName()': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: use of undeclared identifier 'ItemInitState'.
    """
    raise NotImplementedError(
        "'QXmlSimpleReaderPrivate.parseName' has no cute function yet. Qt's "
        "'bool QXmlSimpleReaderPrivate::parseName()': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier 'ItemInitState'.")

  @staticmethod
  def parseNestedFrames(*__, **_) -> Never:
    """
    Qt's 'bool QXmlSimpleReaderPrivate::parseNestedFrames(FrameType
    outermost)': leans on 'QXmlSimpleReaderPrivate::unexpectedEof(bool
    (QXmlSimpleReaderPrivate::*)(), int)', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QXmlSimpleReaderPrivate.parseNestedFrames' has no cute function "
        "yet. Qt's 'bool "
        "QXmlSimpleReaderPrivate::parseNestedFrames(FrameType outermost)': "
        "leans on 'QXmlSimpleReaderPrivate::unexpectedEof(bool "
        "(QXmlSimpleReaderPrivate::*)(), int)', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def parseNmtoken(*__, **_) -> Never:
    """
    Qt's 'bool QXmlSimpleReaderPrivate::parseNmtoken()': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: use of undeclared identifier 'ItemInitState'.
    """
    raise NotImplementedError(
        "'QXmlSimpleReaderPrivate.parseNmtoken' has no cute function yet. "
        "Qt's 'bool QXmlSimpleReaderPrivate::parseNmtoken()': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier 'ItemInitState'.")

  @staticmethod
  def parseNotationDecl(*__, **_) -> Never:
    """
    Qt's 'bool QXmlSimpleReaderPrivate::parseNotationDecl()': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: use of undeclared identifier 'ItemInitState'.
    """
    raise NotImplementedError(
        "'QXmlSimpleReaderPrivate.parseNotationDecl' has no cute function "
        "yet. Qt's 'bool QXmlSimpleReaderPrivate::parseNotationDecl()': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'ItemInitState'.")

  @staticmethod
  def parsePEReference(*__, **_) -> Never:
    """
    Qt's 'bool QXmlSimpleReaderPrivate::parsePEReference()': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: use of undeclared identifier 'ItemInitState'.
    """
    raise NotImplementedError(
        "'QXmlSimpleReaderPrivate.parsePEReference' has no cute function "
        "yet. Qt's 'bool QXmlSimpleReaderPrivate::parsePEReference()': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'ItemInitState'.")

  @staticmethod
  def parsePI(*__, **_) -> Never:
    """
    Qt's 'bool QXmlSimpleReaderPrivate::parsePI()': Qt's library has no name
    for it, and its code in Qt's source does not compile apart from its file:
    use of undeclared identifier 'ItemInitState'.
    """
    raise NotImplementedError(
        "'QXmlSimpleReaderPrivate.parsePI' has no cute function yet. Qt's "
        "'bool QXmlSimpleReaderPrivate::parsePI()': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier 'ItemInitState'.")

  @staticmethod
  def parseProlog(*__, **_) -> Never:
    """
    Qt's 'bool QXmlSimpleReaderPrivate::parseProlog()': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: use of undeclared identifier 'ItemInitState'.
    """
    raise NotImplementedError(
        "'QXmlSimpleReaderPrivate.parseProlog' has no cute function yet. "
        "Qt's 'bool QXmlSimpleReaderPrivate::parseProlog()': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier 'ItemInitState'.")

  @staticmethod
  def parseReference(*__, **_) -> Never:
    """
    Qt's 'bool QXmlSimpleReaderPrivate::parseReference()': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: use of undeclared identifier 'ItemInitState'.
    """
    raise NotImplementedError(
        "'QXmlSimpleReaderPrivate.parseReference' has no cute function yet. "
        "Qt's 'bool QXmlSimpleReaderPrivate::parseReference()': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'ItemInitState'.")

  @staticmethod
  def parseString(*__, **_) -> Never:
    """
    Qt's 'bool QXmlSimpleReaderPrivate::parseString()': leans on
    'QXmlSimpleReaderPrivate::unexpectedEof(bool
    (QXmlSimpleReaderPrivate::*)(), int)', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QXmlSimpleReaderPrivate.parseString' has no cute function yet. "
        "Qt's 'bool QXmlSimpleReaderPrivate::parseString()': leans on "
        "'QXmlSimpleReaderPrivate::unexpectedEof(bool "
        "(QXmlSimpleReaderPrivate::*)(), int)', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def processElementETagBegin2(*__, **_) -> Never:
    """
    Qt's 'bool QXmlSimpleReaderPrivate::processElementETagBegin2()': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'prefixesAfter'.
    """
    raise NotImplementedError(
        "'QXmlSimpleReaderPrivate.processElementETagBegin2' has no cute "
        "function yet. Qt's 'bool "
        "QXmlSimpleReaderPrivate::processElementETagBegin2()': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier 'prefixesAfter'.")

  @staticmethod
  def pushParseState(*__, **_) -> Never:
    """
    Qt's 'void QXmlSimpleReaderPrivate::pushParseState(ParseFunction
    function, int state)': takes or gives a type that cannot be passed yet:
    bool (QXmlSimpleReaderPrivate::*)().
    """
    raise NotImplementedError(
        "'QXmlSimpleReaderPrivate.pushParseState' has no cute function yet. "
        "Qt's 'void QXmlSimpleReaderPrivate::pushParseState(ParseFunction "
        "function, int state)': takes or gives a type that cannot be passed "
        "yet: bool (QXmlSimpleReaderPrivate::*)().")

  @staticmethod
  def ref(*__, **_) -> Never:
    """
    Qt's 'const QString &QXmlSimpleReaderPrivate::ref()': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: use of undeclared identifier 'updateValue'.
    """
    raise NotImplementedError(
        "'QXmlSimpleReaderPrivate.ref' has no cute function yet. Qt's "
        "'const QString &QXmlSimpleReaderPrivate::ref()': Qt's library has "
        "no name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier 'updateValue'.")

  @staticmethod
  def resumeSuspendedCall(*__, **_) -> Never:
    """
    Qt's 'bool QXmlSimpleReaderPrivate::resumeSuspendedCall()': leans on
    'QXmlSimpleReaderPrivate::unexpectedEof(bool
    (QXmlSimpleReaderPrivate::*)(), int)', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QXmlSimpleReaderPrivate.resumeSuspendedCall' has no cute function "
        "yet. Qt's 'bool QXmlSimpleReaderPrivate::resumeSuspendedCall()': "
        "leans on 'QXmlSimpleReaderPrivate::unexpectedEof(bool "
        "(QXmlSimpleReaderPrivate::*)(), int)', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def tryUnwindParseStack(*__, **_) -> Never:
    """
    Qt's 'int
    QXmlSimpleReaderPrivate::tryUnwindParseStack(ParseState::ParseFunction
    func)': takes or gives a type that cannot be passed yet: bool
    (QXmlSimpleReaderPrivate::*)().
    """
    raise NotImplementedError(
        "'QXmlSimpleReaderPrivate.tryUnwindParseStack' has no cute function "
        "yet. Qt's 'int "
        "QXmlSimpleReaderPrivate::tryUnwindParseStack(ParseState::ParseFunct"
        "ion func)': takes or gives a type that cannot be passed yet: bool "
        "(QXmlSimpleReaderPrivate::*)().")

  @staticmethod
  def unexpectedEof(*__, **_) -> Never:
    """
    Qt's 'void QXmlSimpleReaderPrivate::unexpectedEof(ParseFunction where,
    int state)': takes or gives a type that cannot be passed yet: bool
    (QXmlSimpleReaderPrivate::*)().
    """
    raise NotImplementedError(
        "'QXmlSimpleReaderPrivate.unexpectedEof' has no cute function yet. "
        "Qt's 'void QXmlSimpleReaderPrivate::unexpectedEof(ParseFunction "
        "where, int state)': takes or gives a type that cannot be passed "
        "yet: bool (QXmlSimpleReaderPrivate::*)().")
