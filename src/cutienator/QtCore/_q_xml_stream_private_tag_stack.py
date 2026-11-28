"""
QXmlStreamPrivateTagStack binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qxmlstream_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QXmlStreamPrivateTagStack to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QtPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QXmlStreamPrivateTagStack(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QXmlStreamPrivateTagStack: a plain Python object
  standing in front of one C++ QXmlStreamPrivateTagStack.

  What exists
  -----------

  Every function of Qt's QXmlStreamPrivateTagStack that has a ritual and that
  Python can call so far, 2 names in all: 'addToStringStorage',
  'tagStack_pop'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Tag &QXmlStreamPrivateTagStack::tagStack_push()': gives a type
    Python has no way to take yet.

  What has no ritual
  ------------------

  4 of the 8 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ QXmlStreamPrivateTagStack is created at the first use, not by
    'QXmlStreamPrivateTagStack(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QXmlStreamPrivateTagStack.
  - Each name of Qt's QXmlStreamPrivateTagStack that has no cute function
    yet, 'tagStack_push', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  #  The classes Qt writes inside QXmlStreamPrivateTagStack, each a class in
  #  here as in C++.

  class NamespaceDeclaration(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QXmlStreamPrivateTagStack::NamespaceDeclaration: a
    plain Python object standing in front of one C++
    QXmlStreamPrivateTagStack::NamespaceDeclaration.

    C++ hands a QXmlStreamPrivateTagStack::NamespaceDeclaration around as a
    copy, so every C++ QXmlStreamPrivateTagStack::NamespaceDeclaration behind
    a cute one is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QXmlStreamPrivateTagStack::NamespaceDeclaration yet.
    None can be made from Python: one comes out of a function of another
    class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QXmlStreamPrivateTagStack::NamespaceDeclaration::
      ~NamespaceDeclaration()': the destructor: Python removes its C++
      QXmlStreamPrivateTagStack::NamespaceDeclaration by it, and has no other
      use for it.

    What to expect
    --------------

    - The C++ QXmlStreamPrivateTagStack::NamespaceDeclaration is created at
      the first use, not by
      'QXmlStreamPrivateTagStack::NamespaceDeclaration(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QXmlStreamPrivateTagStack::NamespaceDeclaration
      back gives a copy the ritual made for Python, in a new cute
      QXmlStreamPrivateTagStack::NamespaceDeclaration.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QXmlStreamPrivateTagStack::NamespaceDeclaration'

    #  Qt's '~QXmlStreamPrivateTagStack::NamespaceDeclaration()'. Naming it
    #  makes this a value class: Python owns every C++
    #  QXmlStreamPrivateTagStack::NamespaceDeclaration behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN25QXmlStreamPrivateTagStack20NamespaceDeclarationD1Ev')

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  class Tag(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QXmlStreamPrivateTagStack::Tag: a plain Python
    object standing in front of one C++ QXmlStreamPrivateTagStack::Tag.

    C++ hands a QXmlStreamPrivateTagStack::Tag around as a copy, so every C++
    QXmlStreamPrivateTagStack::Tag behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    No function of Qt's QXmlStreamPrivateTagStack::Tag yet. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QXmlStreamPrivateTagStack::Tag::~Tag()': the destructor: Python
      removes its C++ QXmlStreamPrivateTagStack::Tag by it, and has no other
      use for it.

    What to expect
    --------------

    - The C++ QXmlStreamPrivateTagStack::Tag is created at the first use, not
      by 'QXmlStreamPrivateTagStack::Tag(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QXmlStreamPrivateTagStack::Tag back gives a copy
      the ritual made for Python, in a new cute
      QXmlStreamPrivateTagStack::Tag.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QXmlStreamPrivateTagStack::Tag'

    #  Qt's '~QXmlStreamPrivateTagStack::Tag()'. Naming it makes this a value
    #  class: Python owns every C++ QXmlStreamPrivateTagStack::Tag behind a
    #  cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN25QXmlStreamPrivateTagStack3TagD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QXmlStreamPrivateTagStack'

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
    'QXmlStreamPrivateTagStack::QXmlStreamPrivateTagStack()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamprivatetagstack.html
    """
    #  QXmlStreamPrivateTagStack::QXmlStreamPrivateTagStack()
    self._noteCreation(QXmlStreamPrivateTagStack, lambda: Rituals.call(
        'ritual_ZN25QXmlStreamPrivateTagStackC1Ev',
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

  @overload(str)
  def addToStringStorage(self, s: str) -> QtPrivate.XmlStringRef:
    """
    Calls Qt's 'XmlStringRef
    QXmlStreamPrivateTagStack::addToStringStorage(QAnyStringView s)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamprivatetagstack.html#addToStringStorage

    Parameters
    ----------

    s : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QtPrivate.XmlStringRef
      A new cute QtPrivate::XmlStringRef around the copy Qt gave back. Python
      owns it.
    """
    #  XmlStringRef
    #      QXmlStreamPrivateTagStack::addToStringStorage(QAnyStringView s)
    address = self._callAs(
        'QXmlStreamPrivateTagStack',
        'ritual_ZN25QXmlStreamPrivateTagStack18addToStringStorageE14QAnyStr'
        'ingView',
        s,
    )
    return QtPrivate.XmlStringRef._cuteOwning(address)

  def tagStack_pop(self) -> Tag:
    """
    Calls Qt's 'Tag QXmlStreamPrivateTagStack::tagStack_pop()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamprivatetagstack.html#tagStack_pop

    Returns
    -------

    Tag
      A new cute QXmlStreamPrivateTagStack::Tag around the copy Qt gave back.
      Python owns it.
    """
    #  Tag QXmlStreamPrivateTagStack::tagStack_pop()
    address = self._callAs(
        'QXmlStreamPrivateTagStack',
        'ritual_ZN25QXmlStreamPrivateTagStack12tagStack_popEv',
    )
    return QXmlStreamPrivateTagStack.Tag._cuteOwning(address)

  @staticmethod
  def tagStack_push(*__, **_) -> Never:
    """
    Qt's 'Tag &QXmlStreamPrivateTagStack::tagStack_push()': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QXmlStreamPrivateTagStack.tagStack_push' has no cute function "
        "yet. Qt's 'Tag &QXmlStreamPrivateTagStack::tagStack_push()': gives "
        "a type Python has no way to take yet.")
