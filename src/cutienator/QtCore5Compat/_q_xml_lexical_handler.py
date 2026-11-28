"""
QXmlLexicalHandler binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore5Compat/qxml.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute


class QXmlLexicalHandler(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QXmlLexicalHandler: a plain Python object standing in
  front of one C++ QXmlLexicalHandler.

  What exists
  -----------

  Every function of Qt's QXmlLexicalHandler that has a ritual and that Python
  can call so far, 8 names in all: 'startDTD', 'endDTD', 'startEntity',
  'endEntity', 'startCDATA', 'endCDATA', 'comment', 'errorString'. None can
  be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QXmlLexicalHandler::~QXmlLexicalHandler()': the destructor: Python
    never removes a C++ QXmlLexicalHandler.

  What to expect
  --------------

  - The C++ QXmlLexicalHandler is created at the first use, not by
    'QXmlLexicalHandler(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QXmlLexicalHandler.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QXmlLexicalHandler'

  #  A C++ QXmlLexicalHandler Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QXmlLexicalHandler'

  #  The functions Qt calls itself that QXmlLexicalHandler is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'startDTD': (
          ('_ZN18QXmlLexicalHandler8startDTDERK7QStringS2_S2_',
           ('bool', 'number', ''),
           (
               ('address', 'text', ''),
               ('address', 'text', ''),
               ('address', 'text', ''),
           )),
      ),
      'endDTD': (
          ('_ZN18QXmlLexicalHandler6endDTDEv',
           ('bool', 'number', ''),
           ()),
      ),
      'startEntity': (
          ('_ZN18QXmlLexicalHandler11startEntityERK7QString',
           ('bool', 'number', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'endEntity': (
          ('_ZN18QXmlLexicalHandler9endEntityERK7QString',
           ('bool', 'number', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'startCDATA': (
          ('_ZN18QXmlLexicalHandler10startCDATAEv',
           ('bool', 'number', ''),
           ()),
      ),
      'endCDATA': (
          ('_ZN18QXmlLexicalHandler8endCDATAEv',
           ('bool', 'number', ''),
           ()),
      ),
      'comment': (
          ('_ZN18QXmlLexicalHandler7commentERK7QString',
           ('bool', 'number', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'errorString': (
          ('_ZNK18QXmlLexicalHandler11errorStringEv',
           ('address', 'text', ''),
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

  def errorString(self) -> str:
    """
    Calls Qt's 'QString QXmlLexicalHandler::errorString() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmllexicalhandler.html#errorString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QXmlLexicalHandler::errorString() const
    return self._callAs(
        'QXmlLexicalHandler',
        'ritual_ZNK18QXmlLexicalHandler11errorStringEv',
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

  @overload(str, str, str)
  def startDTD(self, name: str, publicId: str, systemId: str) -> bool:
    """
    Calls Qt's 'bool QXmlLexicalHandler::startDTD(const QString &name, const
    QString &publicId, const QString &systemId)'.

    Qt's own words: https://doc.qt.io/qt-6/qxmllexicalhandler.html#startDTD

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    publicId : str
      Passed on as it is: a QString is made of it for the call.

    systemId : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QXmlLexicalHandler::startDTD(const QString &name, const QString
    #      &publicId, const QString &systemId)
    return self._callAs(
        'QXmlLexicalHandler',
        'ritual_ZN18QXmlLexicalHandler8startDTDERK7QStringS2_S2_',
        name, publicId, systemId,
    )

  def endDTD(self) -> bool:
    """
    Calls Qt's 'bool QXmlLexicalHandler::endDTD()'.

    Qt's own words: https://doc.qt.io/qt-6/qxmllexicalhandler.html#endDTD
    """
    #  bool QXmlLexicalHandler::endDTD()
    return self._callAs(
        'QXmlLexicalHandler', 'ritual_ZN18QXmlLexicalHandler6endDTDEv',
    )

  @overload(str)
  def startEntity(self, name: str) -> bool:
    """
    Calls Qt's 'bool QXmlLexicalHandler::startEntity(const QString &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmllexicalhandler.html#startEntity

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QXmlLexicalHandler::startEntity(const QString &name)
    return self._callAs(
        'QXmlLexicalHandler',
        'ritual_ZN18QXmlLexicalHandler11startEntityERK7QString',
        name,
    )

  @overload(str)
  def endEntity(self, name: str) -> bool:
    """
    Calls Qt's 'bool QXmlLexicalHandler::endEntity(const QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qxmllexicalhandler.html#endEntity

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QXmlLexicalHandler::endEntity(const QString &name)
    return self._callAs(
        'QXmlLexicalHandler',
        'ritual_ZN18QXmlLexicalHandler9endEntityERK7QString',
        name,
    )

  def startCDATA(self) -> bool:
    """
    Calls Qt's 'bool QXmlLexicalHandler::startCDATA()'.

    Qt's own words: https://doc.qt.io/qt-6/qxmllexicalhandler.html#startCDATA
    """
    #  bool QXmlLexicalHandler::startCDATA()
    return self._callAs(
        'QXmlLexicalHandler', 'ritual_ZN18QXmlLexicalHandler10startCDATAEv',
    )

  def endCDATA(self) -> bool:
    """
    Calls Qt's 'bool QXmlLexicalHandler::endCDATA()'.

    Qt's own words: https://doc.qt.io/qt-6/qxmllexicalhandler.html#endCDATA
    """
    #  bool QXmlLexicalHandler::endCDATA()
    return self._callAs(
        'QXmlLexicalHandler', 'ritual_ZN18QXmlLexicalHandler8endCDATAEv',
    )

  @overload(str)
  def comment(self, ch: str) -> bool:
    """
    Calls Qt's 'bool QXmlLexicalHandler::comment(const QString &ch)'.

    Qt's own words: https://doc.qt.io/qt-6/qxmllexicalhandler.html#comment

    Parameters
    ----------

    ch : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QXmlLexicalHandler::comment(const QString &ch)
    return self._callAs(
        'QXmlLexicalHandler',
        'ritual_ZN18QXmlLexicalHandler7commentERK7QString',
        ch,
    )
