"""
QVulkanDefaultInstance binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qvulkandefaultinstance_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QVulkanDefaultInstance to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QVulkanInstance


class QVulkanDefaultInstance(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QVulkanDefaultInstance: a plain Python object
  standing in front of one C++ QVulkanDefaultInstance.

  C++ hands a QVulkanDefaultInstance around as a copy, so every C++
  QVulkanDefaultInstance behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QVulkanDefaultInstance that has a ritual and that
  Python can call so far, 5 names in all: 'flags', 'setFlag', 'hasInstance',
  'instance', 'cleanup'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QVulkanDefaultInstance::~QVulkanDefaultInstance()': the destructor:
    Python removes its C++ QVulkanDefaultInstance by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QVulkanDefaultInstance is created at the first use, not by
    'QVulkanDefaultInstance(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QVulkanDefaultInstance back gives a copy the ritual
    made for Python, in a new cute QVulkanDefaultInstance.
  """

  #  The enums Qt writes inside QVulkanDefaultInstance, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class Flag(CuteFlags):
    """
    The flags enum 'QVulkanDefaultInstance::Flag' of Qt, with the 1 names Qt
    gives in it. Qt names the type of its combinations
    'QVulkanDefaultInstance::Flags'.
    """

    EnableValidation = 0x1

  Flags = Flag

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def flags() -> Flags:
    """
    Calls Qt's 'Flags QVulkanDefaultInstance::flags()'.

    Qt's own words: https://doc.qt.io/qt-6/qvulkandefaultinstance.html#flags

    Returns
    -------

    Flags
      The value standing for the combination Qt gave back.
    """
    #  Flags QVulkanDefaultInstance::flags()
    return QVulkanDefaultInstance.Flags(Rituals.call(
        'ritual_ZN22QVulkanDefaultInstance5flagsEv',
    ))

  @staticmethod
  @overload(Flag)
  @overload(Flag, bool)
  def setFlag(flag: Flag, on: bool = True) -> None:
    """
    Calls Qt's 'void QVulkanDefaultInstance::setFlag(Flag flag, bool on)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvulkandefaultinstance.html#setFlag

    Parameters
    ----------

    flag : Flag
      Passed on as its number.

    on : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QVulkanDefaultInstance::setFlag(Flag flag, bool on)
    Rituals.call(
        'ritual_ZN22QVulkanDefaultInstance7setFlagENS_4FlagEb',
        flag.value, on,
    )

  @staticmethod
  def hasInstance() -> bool:
    """
    Calls Qt's 'bool QVulkanDefaultInstance::hasInstance()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvulkandefaultinstance.html#hasInstance
    """
    #  bool QVulkanDefaultInstance::hasInstance()
    return Rituals.call('ritual_ZN22QVulkanDefaultInstance11hasInstanceEv')

  @staticmethod
  def instance() -> Optional[QVulkanInstance]:
    """
    Calls Qt's 'QVulkanInstance *QVulkanDefaultInstance::instance()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvulkandefaultinstance.html#instance

    Returns
    -------

    Optional[QVulkanInstance]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QVulkanInstance *QVulkanDefaultInstance::instance()
    address = Rituals.call('ritual_ZN22QVulkanDefaultInstance8instanceEv')
    from . import QVulkanInstance
    return QVulkanInstance._cuteAt(address)

  @staticmethod
  def cleanup() -> None:
    """
    Calls Qt's 'void QVulkanDefaultInstance::cleanup()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvulkandefaultinstance.html#cleanup
    """
    #  void QVulkanDefaultInstance::cleanup()
    Rituals.call('ritual_ZN22QVulkanDefaultInstance7cleanupEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QVulkanDefaultInstance'

  #  Qt's '~QVulkanDefaultInstance()'. Naming it makes this a value class:
  #  Python owns every C++ QVulkanDefaultInstance behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN22QVulkanDefaultInstanceD1Ev'

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
