"""
RequiredPropertiesAndTarget binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlobjectcreator_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means RequiredPropertiesAndTarget to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import RequiredProperties

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class RequiredPropertiesAndTarget(RequiredProperties):
  """
  The cute side of Qt's RequiredPropertiesAndTarget: a plain Python object
  standing in front of one C++ RequiredPropertiesAndTarget.

  It is built on the cute 'RequiredProperties', as Qt's
  RequiredPropertiesAndTarget is built on Qt's RequiredProperties, and has
  everything that class has.

  C++ hands a RequiredPropertiesAndTarget around as a copy, so every C++
  RequiredPropertiesAndTarget behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  No function of Qt's RequiredPropertiesAndTarget yet. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'RequiredPropertiesAndTarget::RequiredPropertiesAndTarget(
    RequiredPropertiesAndTarget &&a0)': takes a type Python has no way to
    hand over yet.
  - Qt's 'RequiredPropertiesAndTarget
    &RequiredPropertiesAndTarget::operator=(const RequiredPropertiesAndTarget
    &a0)': assignment: Python binds a name and has no operator for it.
  - Qt's 'RequiredPropertiesAndTarget
    &RequiredPropertiesAndTarget::operator=(RequiredPropertiesAndTarget
    &&a0)': assignment: Python binds a name and has no operator for it.
  - Qt's 'RequiredPropertiesAndTarget::~RequiredPropertiesAndTarget()': the
    destructor: Python removes its C++ RequiredPropertiesAndTarget by it, and
    has no other use for it.

  What to expect
  --------------

  - The C++ RequiredPropertiesAndTarget is created at the first use, not by
    'RequiredPropertiesAndTarget(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a RequiredPropertiesAndTarget back gives a copy the
    ritual made for Python, in a new cute RequiredPropertiesAndTarget.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'RequiredPropertiesAndTarget'

  #  Qt's '~RequiredPropertiesAndTarget()'. Naming it makes this a value
  #  class: Python owns every C++ RequiredPropertiesAndTarget behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN27RequiredPropertiesAndTargetD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QObject)
  @overload(NoneType)
  def __init__(self, target: Optional[QObject]) -> None:
    """
    Notes what was given, for Qt's
    'RequiredPropertiesAndTarget::RequiredPropertiesAndTarget(QObject
    *target)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/requiredpropertiesandtarget.html

    Parameters
    ----------

    target : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  RequiredPropertiesAndTarget::RequiredPropertiesAndTarget(QObject
    #      *target)
    self._noteCreation(RequiredPropertiesAndTarget, lambda: Rituals.call(
        'ritual_ZN27RequiredPropertiesAndTargetC1EP7QObject',
        self._addressOf(target, 'QObject'),
    ))

  @overload(THIS)
  def __init__(self, a0: RequiredPropertiesAndTarget) -> None:
    """
    Notes what was given, for Qt's
    'RequiredPropertiesAndTarget::RequiredPropertiesAndTarget(const
    RequiredPropertiesAndTarget &a0)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/requiredpropertiesandtarget.html

    Parameters
    ----------

    a0 : RequiredPropertiesAndTarget
      Passed on as a value: Qt reads the C++ RequiredPropertiesAndTarget,
      which stays Python's own.
    """
    #  RequiredPropertiesAndTarget::RequiredPropertiesAndTarget(const
    #      RequiredPropertiesAndTarget &a0)
    self._noteCreation(RequiredPropertiesAndTarget, lambda: Rituals.call(
        'ritual_ZN27RequiredPropertiesAndTargetC1ERKS_', self._valueOf(a0),
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
