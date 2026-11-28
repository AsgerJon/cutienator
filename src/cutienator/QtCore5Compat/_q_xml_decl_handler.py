"""
QXmlDeclHandler binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore5Compat/qxml.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute


class QXmlDeclHandler(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QXmlDeclHandler: a plain Python object standing in
  front of one C++ QXmlDeclHandler.

  What exists
  -----------

  Every function of Qt's QXmlDeclHandler that has a ritual and that Python
  can call so far, 4 names in all: 'attributeDecl', 'internalEntityDecl',
  'externalEntityDecl', 'errorString'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QXmlDeclHandler::~QXmlDeclHandler()': the destructor: Python never
    removes a C++ QXmlDeclHandler.

  What to expect
  --------------

  - The C++ QXmlDeclHandler is created at the first use, not by
    'QXmlDeclHandler(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QXmlDeclHandler.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QXmlDeclHandler'

  #  A C++ QXmlDeclHandler Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QXmlDeclHandler'

  #  The functions Qt calls itself that QXmlDeclHandler is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'attributeDecl': (
          ('_ZN15QXmlDeclHandler13attributeDeclERK7QStringS2_S2_S2_S2_',
           ('bool', 'number', ''),
           (
               ('address', 'text', ''),
               ('address', 'text', ''),
               ('address', 'text', ''),
               ('address', 'text', ''),
               ('address', 'text', ''),
           )),
      ),
      'internalEntityDecl': (
          ('_ZN15QXmlDeclHandler18internalEntityDeclERK7QStringS2_',
           ('bool', 'number', ''),
           (
               ('address', 'text', ''),
               ('address', 'text', ''),
           )),
      ),
      'externalEntityDecl': (
          ('_ZN15QXmlDeclHandler18externalEntityDeclERK7QStringS2_S2_',
           ('bool', 'number', ''),
           (
               ('address', 'text', ''),
               ('address', 'text', ''),
               ('address', 'text', ''),
           )),
      ),
      'errorString': (
          ('_ZNK15QXmlDeclHandler11errorStringEv',
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
    Calls Qt's 'QString QXmlDeclHandler::errorString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qxmldeclhandler.html#errorString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QXmlDeclHandler::errorString() const
    return self._callAs(
        'QXmlDeclHandler', 'ritual_ZNK15QXmlDeclHandler11errorStringEv',
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

  @overload(str, str, str, str, str)
  def attributeDecl(
      self,
      eName: str,
      aName: str,
      type: str,
      valueDefault: str,
      value: str,
  ) -> bool:
    """
    Calls Qt's 'bool QXmlDeclHandler::attributeDecl(const QString &eName,
    const QString &aName, const QString &type, const QString &valueDefault,
    const QString &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qxmldeclhandler.html#attributeDecl

    Parameters
    ----------

    eName : str
      Passed on as it is: a QString is made of it for the call.

    aName : str
      Passed on as it is: a QString is made of it for the call.

    type : str
      Passed on as it is: a QString is made of it for the call.

    valueDefault : str
      Passed on as it is: a QString is made of it for the call.

    value : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QXmlDeclHandler::attributeDecl(const QString &eName, const
    #      QString &aName, const QString &type, const QString &valueDefault,
    #      const QString &value)
    return self._callAs(
        'QXmlDeclHandler',
        'ritual_ZN15QXmlDeclHandler13attributeDeclERK7QStringS2_S2_S2_S2_',
        eName, aName, type, valueDefault, value,
    )

  @overload(str, str)
  def internalEntityDecl(self, name: str, value: str) -> bool:
    """
    Calls Qt's 'bool QXmlDeclHandler::internalEntityDecl(const QString &name,
    const QString &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmldeclhandler.html#internalEntityDecl

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    value : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QXmlDeclHandler::internalEntityDecl(const QString &name, const
    #      QString &value)
    return self._callAs(
        'QXmlDeclHandler',
        'ritual_ZN15QXmlDeclHandler18internalEntityDeclERK7QStringS2_',
        name, value,
    )

  @overload(str, str, str)
  def externalEntityDecl(
      self,
      name: str,
      publicId: str,
      systemId: str,
  ) -> bool:
    """
    Calls Qt's 'bool QXmlDeclHandler::externalEntityDecl(const QString &name,
    const QString &publicId, const QString &systemId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmldeclhandler.html#externalEntityDecl

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    publicId : str
      Passed on as it is: a QString is made of it for the call.

    systemId : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QXmlDeclHandler::externalEntityDecl(const QString &name, const
    #      QString &publicId, const QString &systemId)
    return self._callAs(
        'QXmlDeclHandler',
        'ritual_ZN15QXmlDeclHandler18externalEntityDeclERK7QStringS2_S2_',
        name, publicId, systemId,
    )
