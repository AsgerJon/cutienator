"""
QQmlJS::Engine binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmljsengine_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QQmlJS::Engine to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from . import QQmlJS

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QChar
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QChar = WAIT['QChar']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Engine(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlJS::Engine: a plain Python object standing in
  front of one C++ QQmlJS::Engine.

  What exists
  -----------

  Every function of Qt's QQmlJS::Engine that has a ritual and that Python can
  call so far, 8 names in all: 'setCode', 'code', 'addComment', 'directives',
  'setDirectives', 'pool', 'midRef', 'newStringRef'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QList<SourceLocation> QQmlJS::Engine::comments() const': gives a
    type Python has no way to take yet.
  - Qt's 'const MemoryPool *QQmlJS::Engine::pool() const': takes in Python
    what 'MemoryPool *QQmlJS::Engine::pool()' takes.

  What has no ritual
  ------------------

  2 of the 13 functions Qt declares: 2 the compiler refuses its ritual as it
  would be written here.

  What to expect
  --------------

  - The C++ QQmlJS::Engine is created at the first use, not by
    'QQmlJS::Engine(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlJS::Engine.
  - Each name of Qt's QQmlJS::Engine that has no cute function yet,
    'comments', 'lexer', 'setLexer', holds a function that raises
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
  __qt_class__ = 'QQmlJS::Engine'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def code(self) -> str:
    """
    Calls Qt's 'const QString &QQmlJS::Engine::code() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-engine.html#code

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  const QString &QQmlJS::Engine::code() const
    return self.uglySide.call('ritual_ZNK6QQmlJS6Engine4codeEv')

  def directives(self) -> Optional[QQmlJS.Directives]:
    """
    Calls Qt's 'Directives *QQmlJS::Engine::directives() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-engine.html#directives

    Returns
    -------

    Optional[QQmlJS.Directives]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Directives *QQmlJS::Engine::directives() const
    address = self.uglySide.call('ritual_ZNK6QQmlJS6Engine10directivesEv')
    return QQmlJS.Directives._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setCode(self, code: str) -> None:
    """
    Calls Qt's 'void QQmlJS::Engine::setCode(const QString &code)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-engine.html#setCode

    Parameters
    ----------

    code : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlJS::Engine::setCode(const QString &code)
    self.uglySide.call('ritual_ZN6QQmlJS6Engine7setCodeERK7QString', code)

  @overload(WAIT['QQmlJS.Directives'])
  @overload(NoneType)
  def setDirectives(self, directives: Optional[QQmlJS.Directives]) -> None:
    """
    Calls Qt's 'void QQmlJS::Engine::setDirectives(Directives *directives)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-engine.html#setDirectives

    Parameters
    ----------

    directives : Optional[QQmlJS.Directives]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::Engine::setDirectives(Directives *directives)
    self.uglySide.call(
        'ritual_ZN6QQmlJS6Engine13setDirectivesEPNS_10DirectivesE',
        self._addressOf(directives),
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

  @overload(int, int, int, int)
  def addComment(self, pos: int, len: int, line: int, col: int) -> None:
    """
    Calls Qt's 'void QQmlJS::Engine::addComment(int pos, int len, int line,
    int col)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-engine.html#addComment

    Parameters
    ----------

    pos : int
      Passed on as it is.

    len : int
      Passed on as it is.

    line : int
      Passed on as it is.

    col : int
      Passed on as it is.
    """
    #  void QQmlJS::Engine::addComment(int pos, int len, int line, int col)
    self.uglySide.call(
        'ritual_ZN6QQmlJS6Engine10addCommentEiiii', pos, len, line, col,
    )

  def pool(self) -> Optional[QQmlJS.MemoryPool]:
    """
    Calls Qt's 'MemoryPool *QQmlJS::Engine::pool()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-engine.html#pool

    Returns
    -------

    Optional[QQmlJS.MemoryPool]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  MemoryPool *QQmlJS::Engine::pool()
    address = self.uglySide.call('ritual_ZN6QQmlJS6Engine4poolEv')
    return QQmlJS.MemoryPool._cuteAt(address)

  @overload(int, int)
  def midRef(self, position: int, size: int) -> str:
    """
    Calls Qt's 'QStringView QQmlJS::Engine::midRef(int position, int size)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-engine.html#midRef

    Parameters
    ----------

    position : int
      Passed on as it is.

    size : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QStringView QQmlJS::Engine::midRef(int position, int size)
    return self.uglySide.call(
        'ritual_ZN6QQmlJS6Engine6midRefEii', position, size,
    )

  @overload(str)
  def newStringRef(self, text: str) -> str:
    """
    Calls Qt's 'QStringView QQmlJS::Engine::newStringRef(const QString
    &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-engine.html#newStringRef

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QStringView QQmlJS::Engine::newStringRef(const QString &text)
    return self.uglySide.call(
        'ritual_ZN6QQmlJS6Engine12newStringRefERK7QString', text,
    )

  @overload(QChar, int)
  @overload(NoneType, int)
  def newStringRef(self, chars: Optional[QChar], size: int) -> str:
    """
    Calls Qt's 'QStringView QQmlJS::Engine::newStringRef(const QChar *chars,
    int size)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-engine.html#newStringRef

    Parameters
    ----------

    chars : Optional[QChar]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    size : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QStringView QQmlJS::Engine::newStringRef(const QChar *chars, int size)
    return self.uglySide.call(
        'ritual_ZN6QQmlJS6Engine12newStringRefEPK5QChari',
        self._addressOf(chars), size,
    )

  @staticmethod
  def comments(*__, **_) -> Never:
    """
    Qt's 'QList<SourceLocation> QQmlJS::Engine::comments() const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJS.Engine.comments' has no cute function yet. Qt's "
        "'QList<SourceLocation> QQmlJS::Engine::comments() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def lexer(*__, **_) -> Never:
    """
    Qt's 'Lexer *QQmlJS::Engine::lexer() const': the compiler refuses its
    ritual as it would be written here: unknown type name 'Lexer'; did you
    mean 'QQmlJS::Lexer'?.
    """
    raise NotImplementedError(
        "'QQmlJS.Engine.lexer' has no cute function yet. Qt's 'Lexer "
        "*QQmlJS::Engine::lexer() const': the compiler refuses its ritual "
        "as it would be written here: unknown type name 'Lexer'; did you "
        "mean 'QQmlJS::Lexer'?.")

  @staticmethod
  def setLexer(*__, **_) -> Never:
    """
    Qt's 'void QQmlJS::Engine::setLexer(Lexer *lexer)': the compiler refuses
    its ritual as it would be written here: unknown type name 'Lexer'; did
    you mean 'QQmlJS::Lexer'?.
    """
    raise NotImplementedError(
        "'QQmlJS.Engine.setLexer' has no cute function yet. Qt's 'void "
        "QQmlJS::Engine::setLexer(Lexer *lexer)': the compiler refuses its "
        "ritual as it would be written here: unknown type name 'Lexer'; did "
        "you mean 'QQmlJS::Lexer'?.")
