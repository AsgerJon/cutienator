"""
DomResource binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/ui4_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means DomResource to be private: it declares the class in a header it
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


class DomResource(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's DomResource: a plain Python object standing in front
  of one C++ DomResource.

  What exists
  -----------

  Every function of Qt's DomResource that has a ritual and that Python can
  call so far, 4 names in all: 'hasAttributeLocation', 'attributeLocation',
  'setAttributeLocation', 'clearAttributeLocation'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'DomResource::~DomResource()': the destructor: Python never removes
    a C++ DomResource.
  - Qt's 'void DomResource::read(QXmlStreamReader &reader)': takes a type
    Python has no way to hand over yet.
  - Qt's 'void DomResource::write(QXmlStreamWriter &writer, const QString
    &tagName) const': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 12 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ DomResource is created at the first use, not by
    'DomResource(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ DomResource.
  - Each name of Qt's DomResource that has no cute function yet, 'read',
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
  __qt_class__ = 'DomResource'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def hasAttributeLocation(self) -> bool:
    """
    Calls Qt's 'bool DomResource::hasAttributeLocation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domresource.html#hasAttributeLocation
    """
    #  bool DomResource::hasAttributeLocation() const
    return self.uglySide.call(
        'ritual_ZNK11DomResource20hasAttributeLocationEv',
    )

  def attributeLocation(self) -> str:
    """
    Calls Qt's 'QString DomResource::attributeLocation() const'.

    Qt's own words: https://doc.qt.io/qt-6/domresource.html#attributeLocation

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString DomResource::attributeLocation() const
    return self.uglySide.call('ritual_ZNK11DomResource17attributeLocationEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setAttributeLocation(self, a: str) -> None:
    """
    Calls Qt's 'void DomResource::setAttributeLocation(const QString &a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/domresource.html#setAttributeLocation

    Parameters
    ----------

    a : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void DomResource::setAttributeLocation(const QString &a)
    self.uglySide.call(
        'ritual_ZN11DomResource20setAttributeLocationERK7QString', a,
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
    Notes what was given, for Qt's 'DomResource::DomResource()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/domresource.html#DomResource
    """
    #  DomResource::DomResource()
    self._noteCreation(DomResource, lambda: Rituals.call(
        'ritual_ZN11DomResourceC1Ev',
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

  def clearAttributeLocation(self) -> None:
    """
    Calls Qt's 'void DomResource::clearAttributeLocation()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domresource.html#clearAttributeLocation
    """
    #  void DomResource::clearAttributeLocation()
    self.uglySide.call('ritual_ZN11DomResource22clearAttributeLocationEv')

  @staticmethod
  def read(*__, **_) -> Never:
    """
    Qt's 'void DomResource::read(QXmlStreamReader &reader)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'DomResource.read' has no cute function yet. Qt's 'void "
        "DomResource::read(QXmlStreamReader &reader)': takes a type Python "
        "has no way to hand over yet.")

  @staticmethod
  def write(*__, **_) -> Never:
    """
    Qt's 'void DomResource::write(QXmlStreamWriter &writer, const QString
    &tagName) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'DomResource.write' has no cute function yet. Qt's 'void "
        "DomResource::write(QXmlStreamWriter &writer, const QString "
        "&tagName) const': takes a type Python has no way to hand over yet.")


#  Qt's 'QList<DomResource *>': the list of DomResource, which
#  'QList[DomResource]' gives. It is made here, so that there is one as soon
#  as there can be a DomResource.
QList.createKind(
    DomResource, 'address',
    make='ritual_list_make_DomResource_ptr',
    add='ritual_list_add_DomResource_ptr',
    size='ritual_list_size_DomResource_ptr',
    at='ritual_list_at_DomResource_ptr',
    drop='ritual_list_drop_DomResource_ptr',
)
