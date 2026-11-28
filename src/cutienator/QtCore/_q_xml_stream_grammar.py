"""
QXmlStreamGrammar binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qxmlstreamgrammar_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QXmlStreamGrammar to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QXmlStreamGrammar(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QXmlStreamGrammar: a plain Python object standing in
  front of one C++ QXmlStreamGrammar.

  C++ hands a QXmlStreamGrammar around as a copy, so every C++
  QXmlStreamGrammar behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QXmlStreamGrammar yet. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QXmlStreamGrammar::~QXmlStreamGrammar()': the destructor: Python
    removes its C++ QXmlStreamGrammar by it, and has no other use for it.

  What has no ritual
  ------------------

  2 of the 3 functions Qt declares: 2 leans on 'QXmlStreamGrammar.

  What to expect
  --------------

  - The C++ QXmlStreamGrammar is created at the first use, not by
    'QXmlStreamGrammar(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QXmlStreamGrammar back gives a copy the ritual made
    for Python, in a new cute QXmlStreamGrammar.
  - Each name of Qt's QXmlStreamGrammar that has no cute function yet,
    'nt_action', 't_action', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QXmlStreamGrammar, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class VariousConstants(CuteNum):
    """
    The enum 'QXmlStreamGrammar::VariousConstants' of Qt, with the 65 names
    Qt gives in it.
    """

    EOF_SYMBOL = Kee[int](0)
    AMPERSAND = Kee[int](5)
    ANY = Kee[int](41)
    ATTLIST = Kee[int](31)
    BANG = Kee[int](25)
    CDATA = Kee[int](47)
    CDATA_START = Kee[int](28)
    COLON = Kee[int](17)
    COMMA = Kee[int](19)
    DASH = Kee[int](20)
    DBLQUOTE = Kee[int](8)
    DIGIT = Kee[int](27)
    DOCTYPE = Kee[int](29)
    DOT = Kee[int](23)
    ELEMENT = Kee[int](30)
    EMPTY = Kee[int](40)
    ENTITIES = Kee[int](51)
    ENTITY = Kee[int](32)
    ENTITY_DONE = Kee[int](45)
    EQ = Kee[int](14)
    FIXED = Kee[int](39)
    HASH = Kee[int](6)
    ID = Kee[int](48)
    IDREF = Kee[int](49)
    IDREFS = Kee[int](50)
    IMPLIED = Kee[int](38)
    LANGLE = Kee[int](3)
    LBRACK = Kee[int](9)
    LETTER = Kee[int](26)
    LPAREN = Kee[int](11)
    NDATA = Kee[int](36)
    NMTOKEN = Kee[int](52)
    NMTOKENS = Kee[int](53)
    NOTATION = Kee[int](33)
    NOTOKEN = Kee[int](1)
    PARSE_ENTITY = Kee[int](44)
    PCDATA = Kee[int](42)
    PERCENT = Kee[int](15)
    PIPE = Kee[int](13)
    PLUS = Kee[int](21)
    PUBLIC = Kee[int](35)
    QUESTIONMARK = Kee[int](24)
    QUOTE = Kee[int](7)
    RANGLE = Kee[int](4)
    RBRACK = Kee[int](10)
    REQUIRED = Kee[int](37)
    RPAREN = Kee[int](12)
    SEMICOLON = Kee[int](18)
    SHIFT_THERE = Kee[int](56)
    SLASH = Kee[int](16)
    SPACE = Kee[int](2)
    STAR = Kee[int](22)
    SYSTEM = Kee[int](34)
    UNRESOLVED_ENTITY = Kee[int](46)
    VERSION = Kee[int](55)
    XML = Kee[int](54)
    XML_ERROR = Kee[int](43)
    ACCEPT_STATE = Kee[int](416)
    RULE_COUNT = Kee[int](270)
    STATE_COUNT = Kee[int](427)
    TERMINAL_COUNT = Kee[int](57)
    NON_TERMINAL_COUNT = Kee[int](84)
    GOTO_INDEX_OFFSET = Kee[int](427)
    GOTO_INFO_OFFSET = Kee[int](1030)
    GOTO_CHECK_OFFSET = Kee[int](1030)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QXmlStreamGrammar'

  #  Qt's '~QXmlStreamGrammar()'. Naming it makes this a value class: Python
  #  owns every C++ QXmlStreamGrammar behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN17QXmlStreamGrammarD1Ev'

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

  @staticmethod
  def nt_action(*__, **_) -> Never:
    """
    Qt's 'int QXmlStreamGrammar::nt_action(int state, int nt)': leans on
    'QXmlStreamGrammar::action_info', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QXmlStreamGrammar.nt_action' has no cute function yet. Qt's 'int "
        "QXmlStreamGrammar::nt_action(int state, int nt)': leans on "
        "'QXmlStreamGrammar::action_info', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def t_action(*__, **_) -> Never:
    """
    Qt's 'int QXmlStreamGrammar::t_action(int state, int token)': leans on
    'QXmlStreamGrammar::action_info', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QXmlStreamGrammar.t_action' has no cute function yet. Qt's 'int "
        "QXmlStreamGrammar::t_action(int state, int token)': leans on "
        "'QXmlStreamGrammar::action_info', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")
