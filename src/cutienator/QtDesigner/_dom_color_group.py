"""
DomColorGroup binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/ui4_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means DomColorGroup to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from . import DomColor, DomColorRole
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  DomColor = WAIT['DomColor']
  DomColorRole = WAIT['DomColorRole']


class DomColorGroup(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's DomColorGroup: a plain Python object standing in
  front of one C++ DomColorGroup.

  What exists
  -----------

  Every function of Qt's DomColorGroup that has a ritual and that Python can
  call so far, 4 names in all: 'elementColorRole', 'setElementColorRole',
  'elementColor', 'setElementColor'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'DomColorGroup::~DomColorGroup()': the destructor: Python never
    removes a C++ DomColorGroup.
  - Qt's 'void DomColorGroup::read(QXmlStreamReader &reader)': takes a type
    Python has no way to hand over yet.
  - Qt's 'void DomColorGroup::write(QXmlStreamWriter &writer, const QString
    &tagName) const': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 12 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ DomColorGroup is created at the first use, not by
    'DomColorGroup(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ DomColorGroup.
  - Each name of Qt's DomColorGroup that has no cute function yet, 'read',
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
  __qt_class__ = 'DomColorGroup'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def elementColorRole(self) -> QList[DomColorRole]:
    """
    Calls Qt's 'QList<DomColorRole *> DomColorGroup::elementColorRole()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domcolorgroup.html#elementColorRole

    Returns
    -------

    QList[DomColorRole]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<DomColorRole *> DomColorGroup::elementColorRole() const
    address = self.uglySide.call(
        'ritual_ZNK13DomColorGroup16elementColorRoleEv',
    )
    from . import DomColorRole
    return QList[DomColorRole]._cuteOwning(address)

  def elementColor(self) -> QList[DomColor]:
    """
    Calls Qt's 'QList<DomColor *> DomColorGroup::elementColor() const'.

    Qt's own words: https://doc.qt.io/qt-6/domcolorgroup.html#elementColor

    Returns
    -------

    QList[DomColor]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<DomColor *> DomColorGroup::elementColor() const
    address = self.uglySide.call('ritual_ZNK13DomColorGroup12elementColorEv')
    from . import DomColor
    return QList[DomColor]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QList[DomColorRole])
  def setElementColorRole(self, a: QList[DomColorRole]) -> None:
    """
    Calls Qt's 'void DomColorGroup::setElementColorRole(const
    QList<DomColorRole *> &a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/domcolorgroup.html#setElementColorRole

    Parameters
    ----------

    a : QList[DomColorRole]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void DomColorGroup::setElementColorRole(const QList<DomColorRole *>
    #      &a)
    self.uglySide.call(
        'ritual_ZN13DomColorGroup19setElementColorRoleERK5QListIP12DomColor'
        'RoleE',
        self._valueOf(a),
    )

  @overload(QList[DomColor])
  def setElementColor(self, a: QList[DomColor]) -> None:
    """
    Calls Qt's 'void DomColorGroup::setElementColor(const QList<DomColor *>
    &a)'.

    Qt's own words: https://doc.qt.io/qt-6/domcolorgroup.html#setElementColor

    Parameters
    ----------

    a : QList[DomColor]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void DomColorGroup::setElementColor(const QList<DomColor *> &a)
    self.uglySide.call(
        'ritual_ZN13DomColorGroup15setElementColorERK5QListIP8DomColorE',
        self._valueOf(a),
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
    Notes what was given, for Qt's 'DomColorGroup::DomColorGroup()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/domcolorgroup.html#DomColorGroup
    """
    #  DomColorGroup::DomColorGroup()
    self._noteCreation(DomColorGroup, lambda: Rituals.call(
        'ritual_ZN13DomColorGroupC1Ev',
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

  @staticmethod
  def read(*__, **_) -> Never:
    """
    Qt's 'void DomColorGroup::read(QXmlStreamReader &reader)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'DomColorGroup.read' has no cute function yet. Qt's 'void "
        "DomColorGroup::read(QXmlStreamReader &reader)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def write(*__, **_) -> Never:
    """
    Qt's 'void DomColorGroup::write(QXmlStreamWriter &writer, const QString
    &tagName) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'DomColorGroup.write' has no cute function yet. Qt's 'void "
        "DomColorGroup::write(QXmlStreamWriter &writer, const QString "
        "&tagName) const': takes a type Python has no way to hand over yet.")
