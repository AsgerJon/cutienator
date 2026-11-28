"""
QOpcUaNodeCreationAttributesPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpcUa/6.12.0/QtOpcUa/private/qopcuanodecreationattributes_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QOpcUaNodeCreationAttributesPrivate to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum
from ..occult import Rituals
from ..QtCore import QSharedData


class QOpcUaNodeCreationAttributesPrivate(QSharedData):
  """
  The cute side of Qt's QOpcUaNodeCreationAttributesPrivate: a plain Python
  object standing in front of one C++ QOpcUaNodeCreationAttributesPrivate.

  It is built on the cute 'QSharedData', as Qt's
  QOpcUaNodeCreationAttributesPrivate is built on Qt's QSharedData, and has
  everything that class has.

  C++ hands a QOpcUaNodeCreationAttributesPrivate around as a copy, so every
  C++ QOpcUaNodeCreationAttributesPrivate behind a cute one is Python's own:
  it is removed, by the ritual named in '__delete_ritual__', when the cute
  object goes.

  What exists
  -----------

  Every function of Qt's QOpcUaNodeCreationAttributesPrivate that has a
  ritual and that Python can call so far, 2 names in all:
  'setAttributeInMask', 'attributeSet'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QOpcUaNodeCreationAttributesPrivate::
    ~QOpcUaNodeCreationAttributesPrivate()': the destructor: Python removes
    its C++ QOpcUaNodeCreationAttributesPrivate by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QOpcUaNodeCreationAttributesPrivate is created at the first use,
    not by 'QOpcUaNodeCreationAttributesPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QOpcUaNodeCreationAttributesPrivate back gives a copy
    the ritual made for Python, in a new cute
    QOpcUaNodeCreationAttributesPrivate.
  """

  #  The enums Qt writes inside QOpcUaNodeCreationAttributesPrivate, each a
  #  class in here as in C++, and the names Qt has for the combinations of
  #  its flags enums.

  class BitMask(CuteNum, scoped=True):
    """
    The enum 'QOpcUaNodeCreationAttributesPrivate::BitMask' of Qt, with the
    19 names Qt gives in it. C++ keeps these names inside the enum, so the
    class that holds the enum does not have them.
    """

    AccessLevel = Kee[int](0)
    ArrayDimensions = Kee[int](1)
    ContainsNoLoops = Kee[int](3)
    DataType = Kee[int](4)
    Description = Kee[int](5)
    DisplayName = Kee[int](6)
    EventNotifier = Kee[int](7)
    Executable = Kee[int](8)
    Historizing = Kee[int](9)
    InverseName = Kee[int](10)
    IsAbstract = Kee[int](11)
    MinimumSamplingInterval = Kee[int](12)
    Symmetric = Kee[int](15)
    UserAccessLevel = Kee[int](16)
    UserExecutable = Kee[int](17)
    UserWriteMask = Kee[int](18)
    ValueRank = Kee[int](19)
    WriteMask = Kee[int](20)
    Value = Kee[int](21)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpcUaNodeCreationAttributesPrivate'

  #  Qt's '~QOpcUaNodeCreationAttributesPrivate()'. Naming it makes this a
  #  value class: Python owns every C++ QOpcUaNodeCreationAttributesPrivate
  #  behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN35QOpcUaNodeCreationAttributesPrivateD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(BitMask)
  def attributeSet(self, attribute: BitMask) -> bool:
    """
    Calls Qt's 'bool QOpcUaNodeCreationAttributesPrivate::attributeSet(
    QOpcUaNodeCreationAttributesPrivate::BitMask attribute) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuanodecreationattributesprivate.html

    Parameters
    ----------

    attribute : BitMask
      Passed on as its number.
    """
    #  bool QOpcUaNodeCreationAttributesPrivate::attributeSet(
    #      QOpcUaNodeCreationAttributesPrivate::BitMask attribute) const
    return self.uglySide.call(
        'ritual_ZNK35QOpcUaNodeCreationAttributesPrivate12attributeSetENS_7'
        'BitMaskE',
        attribute.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(BitMask)
  def setAttributeInMask(self, attribute: BitMask) -> None:
    """
    Calls Qt's 'void QOpcUaNodeCreationAttributesPrivate::setAttributeInMask(
    QOpcUaNodeCreationAttributesPrivate::BitMask attribute)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuanodecreationattributesprivate.html

    Parameters
    ----------

    attribute : BitMask
      Passed on as its number.
    """
    #  void QOpcUaNodeCreationAttributesPrivate::setAttributeInMask(
    #      QOpcUaNodeCreationAttributesPrivate::BitMask attribute)
    self.uglySide.call(
        'ritual_ZN35QOpcUaNodeCreationAttributesPrivate18setAttributeInMask'
        'ENS_7BitMaskE',
        attribute.value,
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
    Notes what was given, for Qt's 'QOpcUaNodeCreationAttributesPrivate::
    QOpcUaNodeCreationAttributesPrivate()', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuanodecreationattributesprivate.html
    """
    #  QOpcUaNodeCreationAttributesPrivate::
    #      QOpcUaNodeCreationAttributesPrivate()
    self._noteCreation(
        QOpcUaNodeCreationAttributesPrivate, lambda: Rituals.call(
            'ritual_ZN35QOpcUaNodeCreationAttributesPrivateC1Ev',
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
