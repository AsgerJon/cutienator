"""
QOperatingSystemVersion binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qoperatingsystemversion.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum
from ..occult import Rituals
from . import QOperatingSystemVersionBase, QOperatingSystemVersionUnexported


class QOperatingSystemVersion(QOperatingSystemVersionUnexported):
  """
  The cute side of Qt's QOperatingSystemVersion: a plain Python object
  standing in front of one C++ QOperatingSystemVersion.

  It is built on the cute 'QOperatingSystemVersionUnexported', as Qt's
  QOperatingSystemVersion is built on Qt's QOperatingSystemVersionUnexported,
  and has everything that class has.

  C++ hands a QOperatingSystemVersion around as a copy, so every C++
  QOperatingSystemVersion behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QOperatingSystemVersion that has a ritual and that
  Python can call so far, 3 names in all: 'current', 'currentType', 'type'.
  It can be made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QOperatingSystemVersion::~QOperatingSystemVersion()': the
    destructor: Python removes its C++ QOperatingSystemVersion by it, and has
    no other use for it.

  What has no ritual
  ------------------

  1 of the 8 functions Qt declares: 1 takes or gives a type that cannot be
  passed yet.

  What to expect
  --------------

  - The C++ QOperatingSystemVersion is created at the first use, not by
    'QOperatingSystemVersion(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QOperatingSystemVersion back gives a copy the ritual
    made for Python, in a new cute QOperatingSystemVersion.
  """

  #  The enums Qt writes inside QOperatingSystemVersion, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class OSType(CuteNum):
    """
    The enum 'QOperatingSystemVersion::OSType' of Qt, with the 9 names Qt
    gives in it.
    """

    Unknown = Kee[int](0)
    Windows = Kee[int](1)
    MacOS = Kee[int](2)
    IOS = Kee[int](3)
    TvOS = Kee[int](4)
    WatchOS = Kee[int](5)
    Android = Kee[int](6)
    VisionOS = Kee[int](7)
    HarmonyOS = Kee[int](8)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def current() -> QOperatingSystemVersion:
    """
    Calls Qt's 'QOperatingSystemVersion QOperatingSystemVersion::current()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoperatingsystemversion.html#current

    Returns
    -------

    QOperatingSystemVersion
      A new cute QOperatingSystemVersion around the copy Qt gave back. Python
      owns it.
    """
    #  QOperatingSystemVersion QOperatingSystemVersion::current()
    address = Rituals.call('ritual_ZN23QOperatingSystemVersion7currentEv')
    return QOperatingSystemVersion._cuteOwning(address)

  @staticmethod
  def currentType() -> OSType:
    """
    Calls Qt's 'OSType QOperatingSystemVersion::currentType()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoperatingsystemversion.html#currentType

    Returns
    -------

    OSType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'OSType(number)' gives.
    """
    #  OSType QOperatingSystemVersion::currentType()
    return QOperatingSystemVersion.OSType(Rituals.call(
        'ritual_ZN23QOperatingSystemVersion11currentTypeEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOperatingSystemVersion'

  #  Qt's '~QOperatingSystemVersion()'. Naming it makes this a value class:
  #  Python owns every C++ QOperatingSystemVersion behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN23QOperatingSystemVersionD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def type(self) -> OSType:
    """
    Calls Qt's 'OSType QOperatingSystemVersion::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qoperatingsystemversion.html#type

    Returns
    -------

    OSType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'OSType(number)' gives.
    """
    #  OSType QOperatingSystemVersion::type() const
    return QOperatingSystemVersion.OSType(self.uglySide.call(
        'ritual_ZNK23QOperatingSystemVersion4typeEv',
    ))

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

  @overload(QOperatingSystemVersionBase)
  def __init__(self, osversion: QOperatingSystemVersionBase) -> None:
    """
    Notes what was given, for Qt's
    'QOperatingSystemVersion::QOperatingSystemVersion(const
    QOperatingSystemVersionBase &osversion)', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qoperatingsystemversion.html

    Parameters
    ----------

    osversion : QOperatingSystemVersionBase
      Passed on as a value: Qt reads the C++ QOperatingSystemVersionBase,
      which stays Python's own.
    """
    #  QOperatingSystemVersion::QOperatingSystemVersion(const
    #      QOperatingSystemVersionBase &osversion)
    self._noteCreation(QOperatingSystemVersion, lambda: Rituals.call(
        'ritual_ZN23QOperatingSystemVersionC1ERK27QOperatingSystemVersionBa'
        'se',
        self._valueOf(osversion),
    ))

  @overload(OSType, int)
  @overload(OSType, int, int)
  @overload(OSType, int, int, int)
  def __init__(
      self,
      osType: OSType,
      vmajor: int,
      vminor: int = -1,
      vmicro: int = -1,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QOperatingSystemVersion::QOperatingSystemVersion(OSType osType, int
    vmajor, int vminor, int vmicro)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qoperatingsystemversion.html

    Parameters
    ----------

    osType : OSType
      Passed on as its number.

    vmajor : int
      Passed on as it is.

    vminor : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    vmicro : int
      Passed on as it is. May be left out, as in Qt: it is then -1.
    """
    #  QOperatingSystemVersion::QOperatingSystemVersion(OSType osType, int
    #      vmajor, int vminor, int vmicro)
    self._noteCreation(QOperatingSystemVersion, lambda: Rituals.call(
        'ritual_ZN23QOperatingSystemVersionC1ENS_6OSTypeEiii',
        osType.value, vmajor, vminor, vmicro,
    ))

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QOperatingSystemVersion::QOperatingSystemVersion()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qoperatingsystemversion.html
    """
    #  QOperatingSystemVersion::QOperatingSystemVersion()
    self._noteCreation(QOperatingSystemVersion, lambda: Rituals.call(
        'ritual_ZN23QOperatingSystemVersionC1Ev',
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
