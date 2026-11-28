"""
DomStringPropertySpecification binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/ui4_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means DomStringPropertySpecification to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class DomStringPropertySpecification(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's DomStringPropertySpecification: a plain Python object
  standing in front of one C++ DomStringPropertySpecification.

  What exists
  -----------

  Every function of Qt's DomStringPropertySpecification that has a ritual and
  that Python can call so far, 12 names in all: 'hasAttributeName',
  'attributeName', 'setAttributeName', 'clearAttributeName',
  'hasAttributeType', 'attributeType', 'setAttributeType',
  'clearAttributeType', 'hasAttributeNotr', 'attributeNotr',
  'setAttributeNotr', 'clearAttributeNotr'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'DomStringPropertySpecification::~DomStringPropertySpecification()':
    the destructor: Python never removes a C++
    DomStringPropertySpecification.
  - Qt's 'void DomStringPropertySpecification::read(QXmlStreamReader
    &reader)': takes a type Python has no way to hand over yet.
  - Qt's 'void DomStringPropertySpecification::write(QXmlStreamWriter
    &writer, const QString &tagName) const': takes a type Python has no way
    to hand over yet.

  What has no ritual
  ------------------

  4 of the 20 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ DomStringPropertySpecification is created at the first use, not
    by 'DomStringPropertySpecification(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ DomStringPropertySpecification.
  - Each name of Qt's DomStringPropertySpecification that has no cute
    function yet, 'read', 'write', holds a function that raises
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
  __qt_class__ = 'DomStringPropertySpecification'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def hasAttributeName(self) -> bool:
    """
    Calls Qt's 'bool DomStringPropertySpecification::hasAttributeName()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domstringpropertyspecification.html
    """
    #  bool DomStringPropertySpecification::hasAttributeName() const
    return self.uglySide.call(
        'ritual_ZNK30DomStringPropertySpecification16hasAttributeNameEv',
    )

  def attributeName(self) -> str:
    """
    Calls Qt's 'QString DomStringPropertySpecification::attributeName()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domstringpropertyspecification.html#attributeName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString DomStringPropertySpecification::attributeName() const
    return self.uglySide.call(
        'ritual_ZNK30DomStringPropertySpecification13attributeNameEv',
    )

  def hasAttributeType(self) -> bool:
    """
    Calls Qt's 'bool DomStringPropertySpecification::hasAttributeType()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domstringpropertyspecification.html
    """
    #  bool DomStringPropertySpecification::hasAttributeType() const
    return self.uglySide.call(
        'ritual_ZNK30DomStringPropertySpecification16hasAttributeTypeEv',
    )

  def attributeType(self) -> str:
    """
    Calls Qt's 'QString DomStringPropertySpecification::attributeType()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domstringpropertyspecification.html#attributeType

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString DomStringPropertySpecification::attributeType() const
    return self.uglySide.call(
        'ritual_ZNK30DomStringPropertySpecification13attributeTypeEv',
    )

  def hasAttributeNotr(self) -> bool:
    """
    Calls Qt's 'bool DomStringPropertySpecification::hasAttributeNotr()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domstringpropertyspecification.html
    """
    #  bool DomStringPropertySpecification::hasAttributeNotr() const
    return self.uglySide.call(
        'ritual_ZNK30DomStringPropertySpecification16hasAttributeNotrEv',
    )

  def attributeNotr(self) -> str:
    """
    Calls Qt's 'QString DomStringPropertySpecification::attributeNotr()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domstringpropertyspecification.html#attributeNotr

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString DomStringPropertySpecification::attributeNotr() const
    return self.uglySide.call(
        'ritual_ZNK30DomStringPropertySpecification13attributeNotrEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setAttributeName(self, a: str) -> None:
    """
    Calls Qt's 'void DomStringPropertySpecification::setAttributeName(const
    QString &a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/domstringpropertyspecification.html

    Parameters
    ----------

    a : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void DomStringPropertySpecification::setAttributeName(const QString
    #      &a)
    self.uglySide.call(
        'ritual_ZN30DomStringPropertySpecification16setAttributeNameERK7QSt'
        'ring',
        a,
    )

  @overload(str)
  def setAttributeType(self, a: str) -> None:
    """
    Calls Qt's 'void DomStringPropertySpecification::setAttributeType(const
    QString &a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/domstringpropertyspecification.html

    Parameters
    ----------

    a : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void DomStringPropertySpecification::setAttributeType(const QString
    #      &a)
    self.uglySide.call(
        'ritual_ZN30DomStringPropertySpecification16setAttributeTypeERK7QSt'
        'ring',
        a,
    )

  @overload(str)
  def setAttributeNotr(self, a: str) -> None:
    """
    Calls Qt's 'void DomStringPropertySpecification::setAttributeNotr(const
    QString &a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/domstringpropertyspecification.html

    Parameters
    ----------

    a : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void DomStringPropertySpecification::setAttributeNotr(const QString
    #      &a)
    self.uglySide.call(
        'ritual_ZN30DomStringPropertySpecification16setAttributeNotrERK7QSt'
        'ring',
        a,
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'DomStringPropertySpecification::DomStringPropertySpecification()', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/domstringpropertyspecification.html
    """
    #  DomStringPropertySpecification::DomStringPropertySpecification()
    self._noteCreation(DomStringPropertySpecification, lambda: Rituals.call(
        'ritual_ZN30DomStringPropertySpecificationC1Ev',
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

  def clearAttributeName(self) -> None:
    """
    Calls Qt's 'void DomStringPropertySpecification::clearAttributeName()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domstringpropertyspecification.html
    """
    #  void DomStringPropertySpecification::clearAttributeName()
    self.uglySide.call(
        'ritual_ZN30DomStringPropertySpecification18clearAttributeNameEv',
    )

  def clearAttributeType(self) -> None:
    """
    Calls Qt's 'void DomStringPropertySpecification::clearAttributeType()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domstringpropertyspecification.html
    """
    #  void DomStringPropertySpecification::clearAttributeType()
    self.uglySide.call(
        'ritual_ZN30DomStringPropertySpecification18clearAttributeTypeEv',
    )

  def clearAttributeNotr(self) -> None:
    """
    Calls Qt's 'void DomStringPropertySpecification::clearAttributeNotr()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domstringpropertyspecification.html
    """
    #  void DomStringPropertySpecification::clearAttributeNotr()
    self.uglySide.call(
        'ritual_ZN30DomStringPropertySpecification18clearAttributeNotrEv',
    )

  @staticmethod
  def read(*__, **_) -> Never:
    """
    Qt's 'void DomStringPropertySpecification::read(QXmlStreamReader
    &reader)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'DomStringPropertySpecification.read' has no cute function yet. "
        "Qt's 'void DomStringPropertySpecification::read(QXmlStreamReader "
        "&reader)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def write(*__, **_) -> Never:
    """
    Qt's 'void DomStringPropertySpecification::write(QXmlStreamWriter
    &writer, const QString &tagName) const': takes a type Python has no way
    to hand over yet.
    """
    raise NotImplementedError(
        "'DomStringPropertySpecification.write' has no cute function yet. "
        "Qt's 'void DomStringPropertySpecification::write(QXmlStreamWriter "
        "&writer, const QString &tagName) const': takes a type Python has "
        "no way to hand over yet.")


#  Qt's 'QList<DomStringPropertySpecification *>': the list of
#  DomStringPropertySpecification, which
#  'QList[DomStringPropertySpecification]' gives. It is made here, so that
#  there is one as soon as there can be a DomStringPropertySpecification.
QList.createKind(
    DomStringPropertySpecification, 'address',
    make='ritual_list_make_DomStringPropertySpecification_ptr',
    add='ritual_list_add_DomStringPropertySpecification_ptr',
    size='ritual_list_size_DomStringPropertySpecification_ptr',
    at='ritual_list_at_DomStringPropertySpecification_ptr',
    drop='ritual_list_drop_DomStringPropertySpecification_ptr',
)
