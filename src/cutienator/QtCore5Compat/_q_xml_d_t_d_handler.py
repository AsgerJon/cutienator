"""
QXmlDTDHandler binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore5Compat/qxml.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute


class QXmlDTDHandler(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QXmlDTDHandler: a plain Python object standing in
  front of one C++ QXmlDTDHandler.

  What exists
  -----------

  Every function of Qt's QXmlDTDHandler that has a ritual and that Python can
  call so far, 3 names in all: 'notationDecl', 'unparsedEntityDecl',
  'errorString'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QXmlDTDHandler::~QXmlDTDHandler()': the destructor: Python never
    removes a C++ QXmlDTDHandler.

  What to expect
  --------------

  - The C++ QXmlDTDHandler is created at the first use, not by
    'QXmlDTDHandler(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QXmlDTDHandler.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QXmlDTDHandler'

  #  A C++ QXmlDTDHandler Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QXmlDTDHandler'

  #  The functions Qt calls itself that QXmlDTDHandler is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'notationDecl': (
          ('_ZN14QXmlDTDHandler12notationDeclERK7QStringS2_S2_',
           ('bool', 'number', ''),
           (
               ('address', 'text', ''),
               ('address', 'text', ''),
               ('address', 'text', ''),
           )),
      ),
      'unparsedEntityDecl': (
          ('_ZN14QXmlDTDHandler18unparsedEntityDeclERK7QStringS2_S2_S2_',
           ('bool', 'number', ''),
           (
               ('address', 'text', ''),
               ('address', 'text', ''),
               ('address', 'text', ''),
               ('address', 'text', ''),
           )),
      ),
      'errorString': (
          ('_ZNK14QXmlDTDHandler11errorStringEv',
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
    Calls Qt's 'QString QXmlDTDHandler::errorString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qxmldtdhandler.html#errorString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QXmlDTDHandler::errorString() const
    return self._callAs(
        'QXmlDTDHandler', 'ritual_ZNK14QXmlDTDHandler11errorStringEv',
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
  def notationDecl(self, name: str, publicId: str, systemId: str) -> bool:
    """
    Calls Qt's 'bool QXmlDTDHandler::notationDecl(const QString &name, const
    QString &publicId, const QString &systemId)'.

    Qt's own words: https://doc.qt.io/qt-6/qxmldtdhandler.html#notationDecl

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    publicId : str
      Passed on as it is: a QString is made of it for the call.

    systemId : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QXmlDTDHandler::notationDecl(const QString &name, const QString
    #      &publicId, const QString &systemId)
    return self._callAs(
        'QXmlDTDHandler',
        'ritual_ZN14QXmlDTDHandler12notationDeclERK7QStringS2_S2_',
        name, publicId, systemId,
    )

  @overload(str, str, str, str)
  def unparsedEntityDecl(
      self,
      name: str,
      publicId: str,
      systemId: str,
      notationName: str,
  ) -> bool:
    """
    Calls Qt's 'bool QXmlDTDHandler::unparsedEntityDecl(const QString &name,
    const QString &publicId, const QString &systemId, const QString
    &notationName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmldtdhandler.html#unparsedEntityDecl

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    publicId : str
      Passed on as it is: a QString is made of it for the call.

    systemId : str
      Passed on as it is: a QString is made of it for the call.

    notationName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QXmlDTDHandler::unparsedEntityDecl(const QString &name, const
    #      QString &publicId, const QString &systemId, const QString
    #      &notationName)
    return self._callAs(
        'QXmlDTDHandler',
        'ritual_ZN14QXmlDTDHandler18unparsedEntityDeclERK7QStringS2_S2_S2_',
        name, publicId, systemId, notationName,
    )
