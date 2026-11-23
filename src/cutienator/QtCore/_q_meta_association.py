"""
QMetaAssociation binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qmetacontainer.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..occult import Rituals
from . import QMetaContainer

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from . import QMetaType


class QMetaAssociation(QMetaContainer):
  """
  The cute side of Qt's QMetaAssociation: a plain Python object standing in
  front of one C++ QMetaAssociation.

  It is built on the cute 'QMetaContainer', as Qt's QMetaAssociation is built
  on Qt's QMetaContainer, and has everything that class has.

  C++ hands a QMetaAssociation around as a copy, so every C++
  QMetaAssociation behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QMetaAssociation that has a ritual and that Python
  can call so far, 16 names in all: 'keyMetaType', 'mappedMetaType',
  'canInsertKey', 'canRemoveKey', 'canContainsKey', 'canGetMappedAtKey',
  'canSetMappedAtKey', 'canGetKeyAtIterator', 'canGetKeyAtConstIterator',
  'canGetMappedAtIterator', 'canGetMappedAtConstIterator',
  'canSetMappedAtIterator', 'canCreateIteratorAtKey',
  'canCreateConstIteratorAtKey', '__eq__', '__ne__'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QMetaAssociation::~QMetaAssociation()': the destructor: Python
    removes its C++ QMetaAssociation by it, and has no other use for it.

  What has no ritual
  ------------------

  16 of the 34 functions Qt declares: 15 takes or gives a type that cannot be
  passed yet; 1 a template.

  What to expect
  --------------

  - The C++ QMetaAssociation is created at the first use, not by
    'QMetaAssociation(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QMetaAssociation back gives a copy the ritual made
    for Python, in a new cute QMetaAssociation.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QMetaAssociation'

  #  Qt's '~QMetaAssociation()'. Naming it makes this a value class: Python
  #  owns every C++ QMetaAssociation behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN16QMetaAssociationD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def keyMetaType(self) -> QMetaType:
    """
    Calls Qt's 'QMetaType QMetaAssociation::keyMetaType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaassociation.html#keyMetaType

    Returns
    -------

    QMetaType
      A new cute QMetaType around the copy Qt gave back. Python owns it.
    """
    #  QMetaType QMetaAssociation::keyMetaType() const
    address = self.uglySide.call(
        'ritual_ZNK16QMetaAssociation11keyMetaTypeEv',
    )
    from . import QMetaType
    return QMetaType._cuteOwning(address)

  def mappedMetaType(self) -> QMetaType:
    """
    Calls Qt's 'QMetaType QMetaAssociation::mappedMetaType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaassociation.html#mappedMetaType

    Returns
    -------

    QMetaType
      A new cute QMetaType around the copy Qt gave back. Python owns it.
    """
    #  QMetaType QMetaAssociation::mappedMetaType() const
    address = self.uglySide.call(
        'ritual_ZNK16QMetaAssociation14mappedMetaTypeEv',
    )
    from . import QMetaType
    return QMetaType._cuteOwning(address)

  def canInsertKey(self) -> bool:
    """
    Calls Qt's 'bool QMetaAssociation::canInsertKey() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaassociation.html#canInsertKey
    """
    #  bool QMetaAssociation::canInsertKey() const
    return self.uglySide.call('ritual_ZNK16QMetaAssociation12canInsertKeyEv')

  def canRemoveKey(self) -> bool:
    """
    Calls Qt's 'bool QMetaAssociation::canRemoveKey() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaassociation.html#canRemoveKey
    """
    #  bool QMetaAssociation::canRemoveKey() const
    return self.uglySide.call('ritual_ZNK16QMetaAssociation12canRemoveKeyEv')

  def canContainsKey(self) -> bool:
    """
    Calls Qt's 'bool QMetaAssociation::canContainsKey() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaassociation.html#canContainsKey
    """
    #  bool QMetaAssociation::canContainsKey() const
    return self.uglySide.call(
        'ritual_ZNK16QMetaAssociation14canContainsKeyEv',
    )

  def canGetMappedAtKey(self) -> bool:
    """
    Calls Qt's 'bool QMetaAssociation::canGetMappedAtKey() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaassociation.html#canGetMappedAtKey
    """
    #  bool QMetaAssociation::canGetMappedAtKey() const
    return self.uglySide.call(
        'ritual_ZNK16QMetaAssociation17canGetMappedAtKeyEv',
    )

  def canSetMappedAtKey(self) -> bool:
    """
    Calls Qt's 'bool QMetaAssociation::canSetMappedAtKey() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaassociation.html#canSetMappedAtKey
    """
    #  bool QMetaAssociation::canSetMappedAtKey() const
    return self.uglySide.call(
        'ritual_ZNK16QMetaAssociation17canSetMappedAtKeyEv',
    )

  def canGetKeyAtIterator(self) -> bool:
    """
    Calls Qt's 'bool QMetaAssociation::canGetKeyAtIterator() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaassociation.html#canGetKeyAtIterator
    """
    #  bool QMetaAssociation::canGetKeyAtIterator() const
    return self.uglySide.call(
        'ritual_ZNK16QMetaAssociation19canGetKeyAtIteratorEv',
    )

  def canGetKeyAtConstIterator(self) -> bool:
    """
    Calls Qt's 'bool QMetaAssociation::canGetKeyAtConstIterator() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaassociation.html#canGetKeyAtConstIterator
    """
    #  bool QMetaAssociation::canGetKeyAtConstIterator() const
    return self.uglySide.call(
        'ritual_ZNK16QMetaAssociation24canGetKeyAtConstIteratorEv',
    )

  def canGetMappedAtIterator(self) -> bool:
    """
    Calls Qt's 'bool QMetaAssociation::canGetMappedAtIterator() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaassociation.html#canGetMappedAtIterator
    """
    #  bool QMetaAssociation::canGetMappedAtIterator() const
    return self.uglySide.call(
        'ritual_ZNK16QMetaAssociation22canGetMappedAtIteratorEv',
    )

  def canGetMappedAtConstIterator(self) -> bool:
    """
    Calls Qt's 'bool QMetaAssociation::canGetMappedAtConstIterator() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaassociation.html#canGetMappedAtConstIterator
    """
    #  bool QMetaAssociation::canGetMappedAtConstIterator() const
    return self.uglySide.call(
        'ritual_ZNK16QMetaAssociation27canGetMappedAtConstIteratorEv',
    )

  def canSetMappedAtIterator(self) -> bool:
    """
    Calls Qt's 'bool QMetaAssociation::canSetMappedAtIterator() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaassociation.html#canSetMappedAtIterator
    """
    #  bool QMetaAssociation::canSetMappedAtIterator() const
    return self.uglySide.call(
        'ritual_ZNK16QMetaAssociation22canSetMappedAtIteratorEv',
    )

  def canCreateIteratorAtKey(self) -> bool:
    """
    Calls Qt's 'bool QMetaAssociation::canCreateIteratorAtKey() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaassociation.html#canCreateIteratorAtKey
    """
    #  bool QMetaAssociation::canCreateIteratorAtKey() const
    return self.uglySide.call(
        'ritual_ZNK16QMetaAssociation22canCreateIteratorAtKeyEv',
    )

  def canCreateConstIteratorAtKey(self) -> bool:
    """
    Calls Qt's 'bool QMetaAssociation::canCreateConstIteratorAtKey() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaassociation.html#canCreateConstIteratorAtKey
    """
    #  bool QMetaAssociation::canCreateConstIteratorAtKey() const
    return self.uglySide.call(
        'ritual_ZNK16QMetaAssociation27canCreateConstIteratorAtKeyEv',
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

  @overload(THIS)
  def __eq__(self, rhs: QMetaAssociation) -> bool:
    """
    Calls Qt's 'bool operator==(const QMetaAssociation &lhs, const
    QMetaAssociation &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaassociation.html#operator==

    Parameters
    ----------

    rhs : QMetaAssociation
      Passed on as a value: Qt reads the C++ QMetaAssociation, which stays
      Python's own.
    """
    #  bool operator==(const QMetaAssociation &lhs, const QMetaAssociation
    #      &rhs)
    return Rituals.call(
        'ritual_ZeqRK16QMetaAssociationS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(self, rhs: QMetaAssociation) -> bool:
    """
    Calls Qt's 'bool operator!=(const QMetaAssociation &lhs, const
    QMetaAssociation &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaassociation.html#operator!=

    Parameters
    ----------

    rhs : QMetaAssociation
      Passed on as a value: Qt reads the C++ QMetaAssociation, which stays
      Python's own.
    """
    #  bool operator!=(const QMetaAssociation &lhs, const QMetaAssociation
    #      &rhs)
    return Rituals.call(
        'ritual_ZneRK16QMetaAssociationS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QMetaAssociation::QMetaAssociation()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaassociation.html#QMetaAssociation
    """
    #  QMetaAssociation::QMetaAssociation()
    self._noteCreation(QMetaAssociation, lambda: Rituals.call(
        'ritual_ZN16QMetaAssociationC1Ev',
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
