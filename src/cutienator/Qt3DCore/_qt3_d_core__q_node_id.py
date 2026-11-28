"""
Qt3DCore::QNodeId binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DCore/qnodeid.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals


class QNodeId(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's Qt3DCore::QNodeId: a plain Python object standing in
  front of one C++ Qt3DCore::QNodeId.

  C++ hands a Qt3DCore::QNodeId around as a copy, so every C++
  Qt3DCore::QNodeId behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's Qt3DCore::QNodeId that has a ritual and that Python
  can call so far, 8 names in all: 'createId', 'isNull', '__eq__', '__ne__',
  '__lt__', '__gt__', 'id', '__bool__'. It can be made from Python, in 2
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DCore::QNodeId::~QNodeId()': the destructor: Python removes its
    C++ Qt3DCore::QNodeId by it, and has no other use for it.

  What to expect
  --------------

  - The C++ Qt3DCore::QNodeId is created at the first use, not by
    'Qt3DCore::QNodeId(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a Qt3DCore::QNodeId back gives a copy the ritual made
    for Python, in a new cute Qt3DCore::QNodeId.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def createId() -> QNodeId:
    """
    Calls Qt's 'QNodeId Qt3DCore::QNodeId::createId()'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qnodeid.html#createId

    Returns
    -------

    QNodeId
      A new cute Qt3DCore::QNodeId around the copy Qt gave back. Python owns
      it.
    """
    #  QNodeId Qt3DCore::QNodeId::createId()
    address = Rituals.call('ritual_ZN8Qt3DCore7QNodeId8createIdEv')
    return QNodeId._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DCore::QNodeId'

  #  Qt's '~Qt3DCore::QNodeId()'. Naming it makes this a value class: Python
  #  owns every C++ Qt3DCore::QNodeId behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN8Qt3DCore7QNodeIdD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool Qt3DCore::QNodeId::isNull() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qnodeid.html#isNull
    """
    #  bool Qt3DCore::QNodeId::isNull() const
    return self.uglySide.call('ritual_ZNK8Qt3DCore7QNodeId6isNullEv')

  def id(self) -> int:
    """
    Calls Qt's 'quint64 Qt3DCore::QNodeId::id() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qnodeid.html#id
    """
    #  quint64 Qt3DCore::QNodeId::id() const
    return self.uglySide.call('ritual_ZNK8Qt3DCore7QNodeId2idEv')

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
  def __eq__(self, other: QNodeId) -> bool:
    """
    Calls Qt's 'bool Qt3DCore::QNodeId::operator==(QNodeId other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qnodeid.html#operator==

    Parameters
    ----------

    other : QNodeId
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own.
    """
    #  bool Qt3DCore::QNodeId::operator==(QNodeId other) const
    return self.uglySide.call(
        'ritual_ZNK8Qt3DCore7QNodeIdeqES0_', self._valueOf(other),
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
  def __ne__(self, other: QNodeId) -> bool:
    """
    Calls Qt's 'bool Qt3DCore::QNodeId::operator!=(QNodeId other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qnodeid.html#operator!=

    Parameters
    ----------

    other : QNodeId
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own.
    """
    #  bool Qt3DCore::QNodeId::operator!=(QNodeId other) const
    return self.uglySide.call(
        'ritual_ZNK8Qt3DCore7QNodeIdneES0_', self._valueOf(other),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __lt__(self, other: QNodeId) -> bool:
    """
    Calls Qt's 'bool Qt3DCore::QNodeId::operator<(QNodeId other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qnodeid.html#operator<

    Parameters
    ----------

    other : QNodeId
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own.
    """
    #  bool Qt3DCore::QNodeId::operator<(QNodeId other) const
    return self.uglySide.call(
        'ritual_ZNK8Qt3DCore7QNodeIdltES0_', self._valueOf(other),
    )

  @overload.fallback
  def __lt__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __gt__(self, other: QNodeId) -> bool:
    """
    Calls Qt's 'bool Qt3DCore::QNodeId::operator>(QNodeId other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qnodeid.html#operator>

    Parameters
    ----------

    other : QNodeId
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own.
    """
    #  bool Qt3DCore::QNodeId::operator>(QNodeId other) const
    return self.uglySide.call(
        'ritual_ZNK8Qt3DCore7QNodeIdgtES0_', self._valueOf(other),
    )

  @overload.fallback
  def __gt__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  def __bool__(self) -> bool:
    """
    Calls Qt's 'bool Qt3DCore::QNodeId::operator bool() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qnodeid.html#operator bool
    """
    #  bool Qt3DCore::QNodeId::operator bool() const
    return self.uglySide.call('ritual_ZNK8Qt3DCore7QNodeIdcvbEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def __init__(self, i: int) -> None:
    """
    Notes what was given, for Qt's 'Qt3DCore::QNodeId::QNodeId(quint64 i)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qnodeid.html#QNodeId

    Parameters
    ----------

    i : int
      Passed on as it is.
    """
    #  Qt3DCore::QNodeId::QNodeId(quint64 i)
    self._noteCreation(QNodeId, lambda: Rituals.call(
        'ritual_ZN8Qt3DCore7QNodeIdC1Ey', i,
    ))

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'Qt3DCore::QNodeId::QNodeId()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qnodeid.html#QNodeId
    """
    #  Qt3DCore::QNodeId::QNodeId()
    self._noteCreation(QNodeId, lambda: Rituals.call(
        'ritual_ZN8Qt3DCore7QNodeIdC1Ev',
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
