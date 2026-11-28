"""
DomColorRole binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/ui4_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means DomColorRole to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import DomBrush
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  DomBrush = WAIT['DomBrush']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class DomColorRole(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's DomColorRole: a plain Python object standing in front
  of one C++ DomColorRole.

  What exists
  -----------

  Every function of Qt's DomColorRole that has a ritual and that Python can
  call so far, 9 names in all: 'hasAttributeRole', 'attributeRole',
  'setAttributeRole', 'clearAttributeRole', 'elementBrush',
  'takeElementBrush', 'setElementBrush', 'hasElementBrush',
  'clearElementBrush'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'DomColorRole::~DomColorRole()': the destructor: Python never
    removes a C++ DomColorRole.
  - Qt's 'void DomColorRole::read(QXmlStreamReader &reader)': takes a type
    Python has no way to hand over yet.
  - Qt's 'void DomColorRole::write(QXmlStreamWriter &writer, const QString
    &tagName) const': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 17 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ DomColorRole is created at the first use, not by
    'DomColorRole(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ DomColorRole.
  - Each name of Qt's DomColorRole that has no cute function yet, 'read',
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
  __qt_class__ = 'DomColorRole'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def hasAttributeRole(self) -> bool:
    """
    Calls Qt's 'bool DomColorRole::hasAttributeRole() const'.

    Qt's own words: https://doc.qt.io/qt-6/domcolorrole.html#hasAttributeRole
    """
    #  bool DomColorRole::hasAttributeRole() const
    return self.uglySide.call('ritual_ZNK12DomColorRole16hasAttributeRoleEv')

  def attributeRole(self) -> str:
    """
    Calls Qt's 'QString DomColorRole::attributeRole() const'.

    Qt's own words: https://doc.qt.io/qt-6/domcolorrole.html#attributeRole

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString DomColorRole::attributeRole() const
    return self.uglySide.call('ritual_ZNK12DomColorRole13attributeRoleEv')

  def elementBrush(self) -> Optional[DomBrush]:
    """
    Calls Qt's 'DomBrush *DomColorRole::elementBrush() const'.

    Qt's own words: https://doc.qt.io/qt-6/domcolorrole.html#elementBrush

    Returns
    -------

    Optional[DomBrush]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomBrush *DomColorRole::elementBrush() const
    address = self.uglySide.call('ritual_ZNK12DomColorRole12elementBrushEv')
    from . import DomBrush
    return DomBrush._cuteAt(address)

  def hasElementBrush(self) -> bool:
    """
    Calls Qt's 'bool DomColorRole::hasElementBrush() const'.

    Qt's own words: https://doc.qt.io/qt-6/domcolorrole.html#hasElementBrush
    """
    #  bool DomColorRole::hasElementBrush() const
    return self.uglySide.call('ritual_ZNK12DomColorRole15hasElementBrushEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setAttributeRole(self, a: str) -> None:
    """
    Calls Qt's 'void DomColorRole::setAttributeRole(const QString &a)'.

    Qt's own words: https://doc.qt.io/qt-6/domcolorrole.html#setAttributeRole

    Parameters
    ----------

    a : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void DomColorRole::setAttributeRole(const QString &a)
    self.uglySide.call(
        'ritual_ZN12DomColorRole16setAttributeRoleERK7QString', a,
    )

  @overload(DomBrush)
  @overload(NoneType)
  def setElementBrush(self, a: Optional[DomBrush]) -> None:
    """
    Calls Qt's 'void DomColorRole::setElementBrush(DomBrush *a)'.

    Qt's own words: https://doc.qt.io/qt-6/domcolorrole.html#setElementBrush

    Parameters
    ----------

    a : Optional[DomBrush]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DomColorRole::setElementBrush(DomBrush *a)
    self.uglySide.call(
        'ritual_ZN12DomColorRole15setElementBrushEP8DomBrush',
        self._addressOf(a),
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
    Notes what was given, for Qt's 'DomColorRole::DomColorRole()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/domcolorrole.html#DomColorRole
    """
    #  DomColorRole::DomColorRole()
    self._noteCreation(DomColorRole, lambda: Rituals.call(
        'ritual_ZN12DomColorRoleC1Ev',
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

  def clearAttributeRole(self) -> None:
    """
    Calls Qt's 'void DomColorRole::clearAttributeRole()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domcolorrole.html#clearAttributeRole
    """
    #  void DomColorRole::clearAttributeRole()
    self.uglySide.call('ritual_ZN12DomColorRole18clearAttributeRoleEv')

  def takeElementBrush(self) -> Optional[DomBrush]:
    """
    Calls Qt's 'DomBrush *DomColorRole::takeElementBrush()'.

    Qt's own words: https://doc.qt.io/qt-6/domcolorrole.html#takeElementBrush

    Returns
    -------

    Optional[DomBrush]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomBrush *DomColorRole::takeElementBrush()
    address = self.uglySide.call(
        'ritual_ZN12DomColorRole16takeElementBrushEv',
    )
    from . import DomBrush
    return DomBrush._cuteAt(address)

  def clearElementBrush(self) -> None:
    """
    Calls Qt's 'void DomColorRole::clearElementBrush()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domcolorrole.html#clearElementBrush
    """
    #  void DomColorRole::clearElementBrush()
    self.uglySide.call('ritual_ZN12DomColorRole17clearElementBrushEv')

  @staticmethod
  def read(*__, **_) -> Never:
    """
    Qt's 'void DomColorRole::read(QXmlStreamReader &reader)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'DomColorRole.read' has no cute function yet. Qt's 'void "
        "DomColorRole::read(QXmlStreamReader &reader)': takes a type Python "
        "has no way to hand over yet.")

  @staticmethod
  def write(*__, **_) -> Never:
    """
    Qt's 'void DomColorRole::write(QXmlStreamWriter &writer, const QString
    &tagName) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'DomColorRole.write' has no cute function yet. Qt's 'void "
        "DomColorRole::write(QXmlStreamWriter &writer, const QString "
        "&tagName) const': takes a type Python has no way to hand over yet.")


#  Qt's 'QList<DomColorRole *>': the list of DomColorRole, which
#  'QList[DomColorRole]' gives. It is made here, so that there is one as soon
#  as there can be a DomColorRole.
QList.createKind(
    DomColorRole, 'address',
    make='ritual_list_make_DomColorRole_ptr',
    add='ritual_list_add_DomColorRole_ptr',
    size='ritual_list_size_DomColorRole_ptr',
    at='ritual_list_at_DomColorRole_ptr',
    drop='ritual_list_drop_DomColorRole_ptr',
)
