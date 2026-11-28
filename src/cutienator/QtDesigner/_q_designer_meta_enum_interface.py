"""
QDesignerMetaEnumInterface binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/abstractintrospection_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QDesignerMetaEnumInterface to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals


class QDesignerMetaEnumInterface(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QDesignerMetaEnumInterface: a plain Python object
  standing in front of one C++ QDesignerMetaEnumInterface.

  What exists
  -----------

  Every function of Qt's QDesignerMetaEnumInterface that has a ritual and
  that Python can call so far, 12 names in all: 'isFlag', 'key', 'keyCount',
  'keyToValue', 'keysToValue', 'name', 'enumName', 'scope', 'separator',
  'value', 'valueToKey', 'valueToKeys'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDesignerMetaEnumInterface::~QDesignerMetaEnumInterface()': the
    destructor: Python never removes a C++ QDesignerMetaEnumInterface.

  What has no ritual
  ------------------

  4 of the 18 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ QDesignerMetaEnumInterface is created at the first use, not by
    'QDesignerMetaEnumInterface(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDesignerMetaEnumInterface.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDesignerMetaEnumInterface'

  #  A C++ QDesignerMetaEnumInterface Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDesignerMetaEnumInterface'

  #  The functions Qt calls itself that QDesignerMetaEnumInterface is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'isFlag': (
          ('_ZNK26QDesignerMetaEnumInterface6isFlagEv',
           ('bool', 'number', ''),
           ()),
      ),
      'key': (
          ('_ZNK26QDesignerMetaEnumInterface3keyEi',
           ('address', 'text', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'keyCount': (
          ('_ZNK26QDesignerMetaEnumInterface8keyCountEv',
           ('int', 'number', ''),
           ()),
      ),
      'keyToValue': (
          ('_ZNK26QDesignerMetaEnumInterface10keyToValueERK7QString',
           ('int', 'number', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'keysToValue': (
          ('_ZNK26QDesignerMetaEnumInterface11keysToValueERK7QString',
           ('int', 'number', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'name': (
          ('_ZNK26QDesignerMetaEnumInterface4nameEv',
           ('address', 'text', ''),
           ()),
      ),
      'enumName': (
          ('_ZNK26QDesignerMetaEnumInterface8enumNameEv',
           ('address', 'text', ''),
           ()),
      ),
      'scope': (
          ('_ZNK26QDesignerMetaEnumInterface5scopeEv',
           ('address', 'text', ''),
           ()),
      ),
      'separator': (
          ('_ZNK26QDesignerMetaEnumInterface9separatorEv',
           ('address', 'text', ''),
           ()),
      ),
      'value': (
          ('_ZNK26QDesignerMetaEnumInterface5valueEi',
           ('int', 'number', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'valueToKey': (
          ('_ZNK26QDesignerMetaEnumInterface10valueToKeyEi',
           ('address', 'text', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'valueToKeys': (
          ('_ZNK26QDesignerMetaEnumInterface11valueToKeysEi',
           ('address', 'text', ''),
           (
               ('int', 'number', ''),
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

  def isFlag(self) -> bool:
    """
    Calls Qt's 'bool QDesignerMetaEnumInterface::isFlag() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermetaenuminterface.html#isFlag
    """
    #  bool QDesignerMetaEnumInterface::isFlag() const
    return self.uglySide.call(
        'ritual_ZNK26QDesignerMetaEnumInterface6isFlagEv',
    )

  @overload(int)
  def key(self, index: int) -> str:
    """
    Calls Qt's 'QString QDesignerMetaEnumInterface::key(int index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermetaenuminterface.html#key

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDesignerMetaEnumInterface::key(int index) const
    return self.uglySide.call(
        'ritual_ZNK26QDesignerMetaEnumInterface3keyEi', index,
    )

  def keyCount(self) -> int:
    """
    Calls Qt's 'int QDesignerMetaEnumInterface::keyCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermetaenuminterface.html#keyCount
    """
    #  int QDesignerMetaEnumInterface::keyCount() const
    return self.uglySide.call(
        'ritual_ZNK26QDesignerMetaEnumInterface8keyCountEv',
    )

  @overload(str)
  def keyToValue(self, key: str) -> int:
    """
    Calls Qt's 'int QDesignerMetaEnumInterface::keyToValue(const QString
    &key) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermetaenuminterface.html#keyToValue

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  int QDesignerMetaEnumInterface::keyToValue(const QString &key) const
    return self.uglySide.call(
        'ritual_ZNK26QDesignerMetaEnumInterface10keyToValueERK7QString', key,
    )

  @overload(str)
  def keysToValue(self, keys: str) -> int:
    """
    Calls Qt's 'int QDesignerMetaEnumInterface::keysToValue(const QString
    &keys) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermetaenuminterface.html#keysToValue

    Parameters
    ----------

    keys : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  int QDesignerMetaEnumInterface::keysToValue(const QString &keys) const
    return self.uglySide.call(
        'ritual_ZNK26QDesignerMetaEnumInterface11keysToValueERK7QString',
        keys,
    )

  def name(self) -> str:
    """
    Calls Qt's 'QString QDesignerMetaEnumInterface::name() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermetaenuminterface.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDesignerMetaEnumInterface::name() const
    return self.uglySide.call(
        'ritual_ZNK26QDesignerMetaEnumInterface4nameEv',
    )

  def enumName(self) -> str:
    """
    Calls Qt's 'QString QDesignerMetaEnumInterface::enumName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermetaenuminterface.html#enumName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDesignerMetaEnumInterface::enumName() const
    return self.uglySide.call(
        'ritual_ZNK26QDesignerMetaEnumInterface8enumNameEv',
    )

  def scope(self) -> str:
    """
    Calls Qt's 'QString QDesignerMetaEnumInterface::scope() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermetaenuminterface.html#scope

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDesignerMetaEnumInterface::scope() const
    return self.uglySide.call(
        'ritual_ZNK26QDesignerMetaEnumInterface5scopeEv',
    )

  def separator(self) -> str:
    """
    Calls Qt's 'QString QDesignerMetaEnumInterface::separator() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermetaenuminterface.html#separator

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDesignerMetaEnumInterface::separator() const
    return self.uglySide.call(
        'ritual_ZNK26QDesignerMetaEnumInterface9separatorEv',
    )

  @overload(int)
  def value(self, index: int) -> int:
    """
    Calls Qt's 'int QDesignerMetaEnumInterface::value(int index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermetaenuminterface.html#value

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  int QDesignerMetaEnumInterface::value(int index) const
    return self.uglySide.call(
        'ritual_ZNK26QDesignerMetaEnumInterface5valueEi', index,
    )

  @overload(int)
  def valueToKey(self, value: int) -> str:
    """
    Calls Qt's 'QString QDesignerMetaEnumInterface::valueToKey(int value)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermetaenuminterface.html#valueToKey

    Parameters
    ----------

    value : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDesignerMetaEnumInterface::valueToKey(int value) const
    return self.uglySide.call(
        'ritual_ZNK26QDesignerMetaEnumInterface10valueToKeyEi', value,
    )

  @overload(int)
  def valueToKeys(self, value: int) -> str:
    """
    Calls Qt's 'QString QDesignerMetaEnumInterface::valueToKeys(int value)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermetaenuminterface.html#valueToKeys

    Parameters
    ----------

    value : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDesignerMetaEnumInterface::valueToKeys(int value) const
    return self.uglySide.call(
        'ritual_ZNK26QDesignerMetaEnumInterface11valueToKeysEi', value,
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QDesignerMetaEnumInterface::QDesignerMetaEnumInterface()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermetaenuminterface.html
    """
    #  QDesignerMetaEnumInterface::QDesignerMetaEnumInterface()
    self._noteCreation(QDesignerMetaEnumInterface, lambda: Rituals.call(
        'ritual_ZN26QDesignerMetaEnumInterfaceC1Ev',
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
