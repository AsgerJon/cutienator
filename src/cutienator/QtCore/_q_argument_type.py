"""
QArgumentType binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qmetaobject_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QArgumentType to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from . import QByteArrayView, QMetaType
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMetaType = WAIT['QMetaType']


class QArgumentType(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QArgumentType: a plain Python object standing in
  front of one C++ QArgumentType.

  C++ hands a QArgumentType around as a copy, so every C++ QArgumentType
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QArgumentType that has a ritual and that Python can
  call so far, 4 names in all: 'metaType', 'name', '__eq__', '__ne__'. It can
  be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QArgumentType::~QArgumentType()': the destructor: Python removes
    its C++ QArgumentType by it, and has no other use for it.

  What has no ritual
  ------------------

  1 of the 8 functions Qt declares: 1 leans on
  'qMetaTypeTypeInternal(QByteArrayView)', which Qt's source does not mark
  for use from outside Qt and has no code for that could be taken.

  What to expect
  --------------

  - The C++ QArgumentType is created at the first use, not by
    'QArgumentType(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QArgumentType back gives a copy the ritual made for
    Python, in a new cute QArgumentType.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QArgumentType'

  #  Qt's '~QArgumentType()'. Naming it makes this a value class: Python owns
  #  every C++ QArgumentType behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN13QArgumentTypeD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaType(self) -> QMetaType:
    """
    Calls Qt's 'QMetaType QArgumentType::metaType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qargumenttype.html#metaType

    Returns
    -------

    QMetaType
      A new cute QMetaType around the copy Qt gave back. Python owns it.
    """
    #  QMetaType QArgumentType::metaType() const
    address = self.uglySide.call('ritual_ZNK13QArgumentType8metaTypeEv')
    from . import QMetaType
    return QMetaType._cuteOwning(address)

  def name(self) -> QByteArrayView:
    """
    Calls Qt's 'QByteArrayView QArgumentType::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qargumenttype.html#name

    Returns
    -------

    QByteArrayView
      A new cute QByteArrayView around the copy Qt gave back. Python owns it.
    """
    #  QByteArrayView QArgumentType::name() const
    address = self.uglySide.call('ritual_ZNK13QArgumentType4nameEv')
    from . import QByteArrayView
    return QByteArrayView._cuteOwning(address)

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
  def __eq__(self, rhs: QArgumentType) -> bool:
    """
    Calls Qt's 'bool operator==(const QArgumentType &lhs, const QArgumentType
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qargumenttype.html#operator==

    Parameters
    ----------

    rhs : QArgumentType
      Passed on as a value: Qt reads the C++ QArgumentType, which stays
      Python's own.
    """
    #  bool operator==(const QArgumentType &lhs, const QArgumentType &rhs)
    return Rituals.call(
        'ritual_ZeqRK13QArgumentTypeS1_',
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
  def __ne__(self, rhs: QArgumentType) -> bool:
    """
    Calls Qt's 'bool operator!=(const QArgumentType &lhs, const QArgumentType
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qargumenttype.html#operator!=

    Parameters
    ----------

    rhs : QArgumentType
      Passed on as a value: Qt reads the C++ QArgumentType, which stays
      Python's own.
    """
    #  bool operator!=(const QArgumentType &lhs, const QArgumentType &rhs)
    return Rituals.call(
        'ritual_ZneRK13QArgumentTypeS1_',
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
    Notes what was given, for Qt's 'QArgumentType::QArgumentType()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qargumenttype.html#QArgumentType
    """
    #  QArgumentType::QArgumentType()
    self._noteCreation(QArgumentType, lambda: Rituals.call(
        'ritual_ZN13QArgumentTypeC1Ev',
    ))

  @overload(QMetaType)
  def __init__(self, metaType: QMetaType) -> None:
    """
    Notes what was given, for Qt's 'QArgumentType::QArgumentType(QMetaType
    metaType)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qargumenttype.html#QArgumentType

    Parameters
    ----------

    metaType : QMetaType
      Passed on as a value: Qt reads the C++ QMetaType, which stays Python's
      own.
    """
    #  QArgumentType::QArgumentType(QMetaType metaType)
    self._noteCreation(QArgumentType, lambda: Rituals.call(
        'ritual_ZN13QArgumentTypeC1E9QMetaType', self._valueOf(metaType),
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
