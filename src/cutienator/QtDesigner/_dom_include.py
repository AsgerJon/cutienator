"""
DomInclude binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/ui4_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means DomInclude to be private: it declares the class in a header it
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


class DomInclude(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's DomInclude: a plain Python object standing in front
  of one C++ DomInclude.

  What exists
  -----------

  Every function of Qt's DomInclude that has a ritual and that Python can
  call so far, 10 names in all: 'text', 'setText', 'hasAttributeLocation',
  'attributeLocation', 'setAttributeLocation', 'clearAttributeLocation',
  'hasAttributeImpldecl', 'attributeImpldecl', 'setAttributeImpldecl',
  'clearAttributeImpldecl'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'DomInclude::~DomInclude()': the destructor: Python never removes a
    C++ DomInclude.
  - Qt's 'void DomInclude::read(QXmlStreamReader &reader)': takes a type
    Python has no way to hand over yet.
  - Qt's 'void DomInclude::write(QXmlStreamWriter &writer, const QString
    &tagName) const': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 18 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ DomInclude is created at the first use, not by 'DomInclude(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ DomInclude.
  - Each name of Qt's DomInclude that has no cute function yet, 'read',
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
  __qt_class__ = 'DomInclude'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def text(self) -> str:
    """
    Calls Qt's 'QString DomInclude::text() const'.

    Qt's own words: https://doc.qt.io/qt-6/dominclude.html#text

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString DomInclude::text() const
    return self.uglySide.call('ritual_ZNK10DomInclude4textEv')

  def hasAttributeLocation(self) -> bool:
    """
    Calls Qt's 'bool DomInclude::hasAttributeLocation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/dominclude.html#hasAttributeLocation
    """
    #  bool DomInclude::hasAttributeLocation() const
    return self.uglySide.call(
        'ritual_ZNK10DomInclude20hasAttributeLocationEv',
    )

  def attributeLocation(self) -> str:
    """
    Calls Qt's 'QString DomInclude::attributeLocation() const'.

    Qt's own words: https://doc.qt.io/qt-6/dominclude.html#attributeLocation

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString DomInclude::attributeLocation() const
    return self.uglySide.call('ritual_ZNK10DomInclude17attributeLocationEv')

  def hasAttributeImpldecl(self) -> bool:
    """
    Calls Qt's 'bool DomInclude::hasAttributeImpldecl() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/dominclude.html#hasAttributeImpldecl
    """
    #  bool DomInclude::hasAttributeImpldecl() const
    return self.uglySide.call(
        'ritual_ZNK10DomInclude20hasAttributeImpldeclEv',
    )

  def attributeImpldecl(self) -> str:
    """
    Calls Qt's 'QString DomInclude::attributeImpldecl() const'.

    Qt's own words: https://doc.qt.io/qt-6/dominclude.html#attributeImpldecl

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString DomInclude::attributeImpldecl() const
    return self.uglySide.call('ritual_ZNK10DomInclude17attributeImpldeclEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setText(self, s: str) -> None:
    """
    Calls Qt's 'void DomInclude::setText(const QString &s)'.

    Qt's own words: https://doc.qt.io/qt-6/dominclude.html#setText

    Parameters
    ----------

    s : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void DomInclude::setText(const QString &s)
    self.uglySide.call('ritual_ZN10DomInclude7setTextERK7QString', s)

  @overload(str)
  def setAttributeLocation(self, a: str) -> None:
    """
    Calls Qt's 'void DomInclude::setAttributeLocation(const QString &a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/dominclude.html#setAttributeLocation

    Parameters
    ----------

    a : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void DomInclude::setAttributeLocation(const QString &a)
    self.uglySide.call(
        'ritual_ZN10DomInclude20setAttributeLocationERK7QString', a,
    )

  @overload(str)
  def setAttributeImpldecl(self, a: str) -> None:
    """
    Calls Qt's 'void DomInclude::setAttributeImpldecl(const QString &a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/dominclude.html#setAttributeImpldecl

    Parameters
    ----------

    a : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void DomInclude::setAttributeImpldecl(const QString &a)
    self.uglySide.call(
        'ritual_ZN10DomInclude20setAttributeImpldeclERK7QString', a,
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
    Notes what was given, for Qt's 'DomInclude::DomInclude()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/dominclude.html#DomInclude
    """
    #  DomInclude::DomInclude()
    self._noteCreation(DomInclude, lambda: Rituals.call(
        'ritual_ZN10DomIncludeC1Ev',
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
    Calls Qt's 'void DomInclude::clearAttributeLocation()'.

    Qt's own words:
    https://doc.qt.io/qt-6/dominclude.html#clearAttributeLocation
    """
    #  void DomInclude::clearAttributeLocation()
    self.uglySide.call('ritual_ZN10DomInclude22clearAttributeLocationEv')

  def clearAttributeImpldecl(self) -> None:
    """
    Calls Qt's 'void DomInclude::clearAttributeImpldecl()'.

    Qt's own words:
    https://doc.qt.io/qt-6/dominclude.html#clearAttributeImpldecl
    """
    #  void DomInclude::clearAttributeImpldecl()
    self.uglySide.call('ritual_ZN10DomInclude22clearAttributeImpldeclEv')

  @staticmethod
  def read(*__, **_) -> Never:
    """
    Qt's 'void DomInclude::read(QXmlStreamReader &reader)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'DomInclude.read' has no cute function yet. Qt's 'void "
        "DomInclude::read(QXmlStreamReader &reader)': takes a type Python "
        "has no way to hand over yet.")

  @staticmethod
  def write(*__, **_) -> Never:
    """
    Qt's 'void DomInclude::write(QXmlStreamWriter &writer, const QString
    &tagName) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'DomInclude.write' has no cute function yet. Qt's 'void "
        "DomInclude::write(QXmlStreamWriter &writer, const QString "
        "&tagName) const': takes a type Python has no way to hand over yet.")


#  Qt's 'QList<DomInclude *>': the list of DomInclude, which
#  'QList[DomInclude]' gives. It is made here, so that there is one as soon
#  as there can be a DomInclude.
QList.createKind(
    DomInclude, 'address',
    make='ritual_list_make_DomInclude_ptr',
    add='ritual_list_add_DomInclude_ptr',
    size='ritual_list_size_DomInclude_ptr',
    at='ritual_list_at_DomInclude_ptr',
    drop='ritual_list_drop_DomInclude_ptr',
)
