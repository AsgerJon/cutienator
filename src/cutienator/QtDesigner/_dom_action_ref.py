"""
DomActionRef binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/ui4_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means DomActionRef to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class DomActionRef(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's DomActionRef: a plain Python object standing in front
  of one C++ DomActionRef.

  What exists
  -----------

  Every function of Qt's DomActionRef that has a ritual and that Python can
  call so far, 4 names in all: 'hasAttributeName', 'attributeName',
  'setAttributeName', 'clearAttributeName'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'DomActionRef::~DomActionRef()': the destructor: Python never
    removes a C++ DomActionRef.
  - Qt's 'void DomActionRef::read(QXmlStreamReader &reader)': takes a type
    Python has no way to hand over yet.
  - Qt's 'void DomActionRef::write(QXmlStreamWriter &writer, const QString
    &tagName) const': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 12 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ DomActionRef is created at the first use, not by
    'DomActionRef(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ DomActionRef.
  - Each name of Qt's DomActionRef that has no cute function yet, 'read',
    'write', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'DomActionRef'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def hasAttributeName(self) -> bool:
    """
    Calls Qt's 'bool DomActionRef::hasAttributeName() const'.

    Qt's own words: https://doc.qt.io/qt-6/domactionref.html#hasAttributeName
    """
    #  bool DomActionRef::hasAttributeName() const
    return self.uglySide.call('ritual_ZNK12DomActionRef16hasAttributeNameEv')

  def attributeName(self) -> str:
    """
    Calls Qt's 'QString DomActionRef::attributeName() const'.

    Qt's own words: https://doc.qt.io/qt-6/domactionref.html#attributeName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString DomActionRef::attributeName() const
    return self.uglySide.call('ritual_ZNK12DomActionRef13attributeNameEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setAttributeName(self, a: str) -> None:
    """
    Calls Qt's 'void DomActionRef::setAttributeName(const QString &a)'.

    Qt's own words: https://doc.qt.io/qt-6/domactionref.html#setAttributeName

    Parameters
    ----------

    a : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void DomActionRef::setAttributeName(const QString &a)
    self.uglySide.call(
        'ritual_ZN12DomActionRef16setAttributeNameERK7QString', a,
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
    Notes what was given, for Qt's 'DomActionRef::DomActionRef()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/domactionref.html#DomActionRef
    """
    #  DomActionRef::DomActionRef()
    self._noteCreation(DomActionRef, lambda: Rituals.call(
        'ritual_ZN12DomActionRefC1Ev',
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
    Calls Qt's 'void DomActionRef::clearAttributeName()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domactionref.html#clearAttributeName
    """
    #  void DomActionRef::clearAttributeName()
    self.uglySide.call('ritual_ZN12DomActionRef18clearAttributeNameEv')

  @staticmethod
  def read(*__, **_) -> Never:
    """
    Qt's 'void DomActionRef::read(QXmlStreamReader &reader)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'DomActionRef.read' has no cute function yet. Qt's 'void "
        "DomActionRef::read(QXmlStreamReader &reader)': takes a type Python "
        "has no way to hand over yet.")

  @staticmethod
  def write(*__, **_) -> Never:
    """
    Qt's 'void DomActionRef::write(QXmlStreamWriter &writer, const QString
    &tagName) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'DomActionRef.write' has no cute function yet. Qt's 'void "
        "DomActionRef::write(QXmlStreamWriter &writer, const QString "
        "&tagName) const': takes a type Python has no way to hand over yet.")


#  Qt's 'QList<DomActionRef *>': the list of DomActionRef, which
#  'QList[DomActionRef]' gives. It is made here, so that there is one as soon
#  as there can be a DomActionRef.
QList.createKind(
    DomActionRef, 'address',
    make='ritual_list_make_DomActionRef_ptr',
    add='ritual_list_add_DomActionRef_ptr',
    size='ritual_list_size_DomActionRef_ptr',
    at='ritual_list_at_DomActionRef_ptr',
    drop='ritual_list_drop_DomActionRef_ptr',
)
