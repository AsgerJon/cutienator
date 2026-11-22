"""
QOperatingSystemVersionBase binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qoperatingsystemversion.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from . import QVersionNumber


class QOperatingSystemVersionBase(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QOperatingSystemVersionBase: a plain Python object
  standing in front of one C++ QOperatingSystemVersionBase.

  C++ hands a QOperatingSystemVersionBase around as a copy, so every C++
  QOperatingSystemVersionBase behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QOperatingSystemVersionBase that has a ritual and
  that Python can call so far, 9 names in all: 'current', 'name',
  'currentType', 'version', 'majorVersion', 'minorVersion', 'microVersion',
  'segmentCount', 'type'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QOperatingSystemVersionBase::~QOperatingSystemVersionBase()': the
    destructor: Python removes its C++ QOperatingSystemVersionBase by it, and
    has no other use for it.

  What has no ritual
  ------------------

  5 of the 17 functions Qt declares: 2 takes or gives a type that cannot be
  passed yet; 2 protected; 1 private.

  What to expect
  --------------

  - The C++ QOperatingSystemVersionBase is created at the first use, not by
    'QOperatingSystemVersionBase(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QOperatingSystemVersionBase back gives a copy the
    ritual made for Python, in a new cute QOperatingSystemVersionBase.
  """

  #  The enums Qt writes inside QOperatingSystemVersionBase, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class OSType(CuteNum):
    """
    The enum 'QOperatingSystemVersionBase::OSType' of Qt, with the 9 names Qt
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
  def current() -> QOperatingSystemVersionBase:
    """
    Calls Qt's 'QOperatingSystemVersionBase
    QOperatingSystemVersionBase::current()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoperatingsystemversionbase.html#current

    Returns
    -------

    QOperatingSystemVersionBase
      A new cute QOperatingSystemVersionBase around the copy Qt gave back.
      Python owns it.
    """
    #  QOperatingSystemVersionBase QOperatingSystemVersionBase::current()
    address = Rituals.call(
        'ritual_ZN27QOperatingSystemVersionBase7currentEv',
    )
    return QOperatingSystemVersionBase._cuteOwning(address)

  @staticmethod
  @overload(THIS)
  def name(osversion: QOperatingSystemVersionBase) -> str:
    """
    Calls Qt's 'QString
    QOperatingSystemVersionBase::name(QOperatingSystemVersionBase
    osversion)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoperatingsystemversionbase.html#name

    Parameters
    ----------

    osversion : QOperatingSystemVersionBase
      Passed on as a value: Qt reads the C++ QOperatingSystemVersionBase,
      which stays Python's own.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QOperatingSystemVersionBase::name(QOperatingSystemVersionBase
    #      osversion)
    return Rituals.call(
        'ritual_ZN27QOperatingSystemVersionBase4nameES_',
        CuteMixin._valueOf(osversion),
    )

  @overload()
  def name(self) -> str:
    """
    Calls Qt's 'QString QOperatingSystemVersionBase::name() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoperatingsystemversionbase.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QOperatingSystemVersionBase::name() const
    return self.uglySide.call(
        'ritual_ZNK27QOperatingSystemVersionBase4nameEv',
    )

  @staticmethod
  def currentType() -> OSType:
    """
    Calls Qt's 'OSType QOperatingSystemVersionBase::currentType()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoperatingsystemversionbase.html#currentType

    Returns
    -------

    OSType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'OSType(number)' gives.
    """
    #  OSType QOperatingSystemVersionBase::currentType()
    return QOperatingSystemVersionBase.OSType(Rituals.call(
        'ritual_ZN27QOperatingSystemVersionBase11currentTypeEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOperatingSystemVersionBase'

  #  Qt's '~QOperatingSystemVersionBase()'. Naming it makes this a value
  #  class: Python owns every C++ QOperatingSystemVersionBase behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN27QOperatingSystemVersionBaseD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def version(self) -> QVersionNumber:
    """
    Calls Qt's 'QVersionNumber QOperatingSystemVersionBase::version() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoperatingsystemversionbase.html#version

    Returns
    -------

    QVersionNumber
      A new cute QVersionNumber around the copy Qt gave back. Python owns it.
    """
    #  QVersionNumber QOperatingSystemVersionBase::version() const
    address = self.uglySide.call(
        'ritual_ZNK27QOperatingSystemVersionBase7versionEv',
    )
    from . import QVersionNumber
    return QVersionNumber._cuteOwning(address)

  def majorVersion(self) -> int:
    """
    Calls Qt's 'int QOperatingSystemVersionBase::majorVersion() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoperatingsystemversionbase.html#majorVersion
    """
    #  int QOperatingSystemVersionBase::majorVersion() const
    return self.uglySide.call(
        'ritual_ZNK27QOperatingSystemVersionBase12majorVersionEv',
    )

  def minorVersion(self) -> int:
    """
    Calls Qt's 'int QOperatingSystemVersionBase::minorVersion() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoperatingsystemversionbase.html#minorVersion
    """
    #  int QOperatingSystemVersionBase::minorVersion() const
    return self.uglySide.call(
        'ritual_ZNK27QOperatingSystemVersionBase12minorVersionEv',
    )

  def microVersion(self) -> int:
    """
    Calls Qt's 'int QOperatingSystemVersionBase::microVersion() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoperatingsystemversionbase.html#microVersion
    """
    #  int QOperatingSystemVersionBase::microVersion() const
    return self.uglySide.call(
        'ritual_ZNK27QOperatingSystemVersionBase12microVersionEv',
    )

  def segmentCount(self) -> int:
    """
    Calls Qt's 'int QOperatingSystemVersionBase::segmentCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoperatingsystemversionbase.html#segmentCount
    """
    #  int QOperatingSystemVersionBase::segmentCount() const
    return self.uglySide.call(
        'ritual_ZNK27QOperatingSystemVersionBase12segmentCountEv',
    )

  def type(self) -> OSType:
    """
    Calls Qt's 'OSType QOperatingSystemVersionBase::type() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoperatingsystemversionbase.html#type

    Returns
    -------

    OSType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'OSType(number)' gives.
    """
    #  OSType QOperatingSystemVersionBase::type() const
    return QOperatingSystemVersionBase.OSType(self.uglySide.call(
        'ritual_ZNK27QOperatingSystemVersionBase4typeEv',
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
    'QOperatingSystemVersionBase::QOperatingSystemVersionBase(OSType osType,
    int vmajor, int vminor, int vmicro)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qoperatingsystemversionbase.html

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
    #  QOperatingSystemVersionBase::QOperatingSystemVersionBase(OSType
    #      osType, int vmajor, int vminor, int vmicro)
    self._noteCreation(QOperatingSystemVersionBase, lambda: Rituals.call(
        'ritual_ZN27QOperatingSystemVersionBaseC1ENS_6OSTypeEiii',
        osType.value, vmajor, vminor, vmicro,
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
