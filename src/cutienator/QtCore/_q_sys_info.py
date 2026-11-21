"""
QSysInfo binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qsysinfo.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from . import QByteArray


class QSysInfo(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSysInfo: a plain Python object standing in front of
  one C++ QSysInfo.

  C++ hands a QSysInfo around as a copy, so every C++ QSysInfo behind a cute
  one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSysInfo that has a ritual and that Python can call
  so far, 11 names in all: 'buildCpuArchitecture', 'currentCpuArchitecture',
  'buildAbi', 'kernelType', 'kernelVersion', 'productType', 'productVersion',
  'prettyProductName', 'machineHostName', 'machineUniqueId', 'bootUniqueId'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSysInfo::~QSysInfo()': the destructor: Python removes its C++
    QSysInfo by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QSysInfo is created at the first use, not by 'QSysInfo(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSysInfo back gives a copy the ritual made for
    Python, in a new cute QSysInfo.
  """

  #  The enums Qt writes inside QSysInfo, each a class in here as in C++, and
  #  the names Qt has for the combinations of its flags enums.

  class Endian(CuteNum):
    """The enum 'QSysInfo::Endian' of Qt, with the 3 names Qt gives in it."""

    BigEndian = Kee[int](0)
    LittleEndian = Kee[int](1)
    ByteOrder = Kee[int](1)

  class Sizes(CuteNum):
    """The enum 'QSysInfo::Sizes' of Qt, with the 1 names Qt gives in it."""

    WordSize = Kee[int](64)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def buildCpuArchitecture() -> str:
    """
    Calls Qt's 'QString QSysInfo::buildCpuArchitecture()'.

    Qt's own words: https://doc.qt.io/qt-6/qsysinfo.html#buildCpuArchitecture

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSysInfo::buildCpuArchitecture()
    return Rituals.call('ritual_ZN8QSysInfo20buildCpuArchitectureEv')

  @staticmethod
  def currentCpuArchitecture() -> str:
    """
    Calls Qt's 'QString QSysInfo::currentCpuArchitecture()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsysinfo.html#currentCpuArchitecture

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSysInfo::currentCpuArchitecture()
    return Rituals.call('ritual_ZN8QSysInfo22currentCpuArchitectureEv')

  @staticmethod
  def buildAbi() -> str:
    """
    Calls Qt's 'QString QSysInfo::buildAbi()'.

    Qt's own words: https://doc.qt.io/qt-6/qsysinfo.html#buildAbi

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSysInfo::buildAbi()
    return Rituals.call('ritual_ZN8QSysInfo8buildAbiEv')

  @staticmethod
  def kernelType() -> str:
    """
    Calls Qt's 'QString QSysInfo::kernelType()'.

    Qt's own words: https://doc.qt.io/qt-6/qsysinfo.html#kernelType

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSysInfo::kernelType()
    return Rituals.call('ritual_ZN8QSysInfo10kernelTypeEv')

  @staticmethod
  def kernelVersion() -> str:
    """
    Calls Qt's 'QString QSysInfo::kernelVersion()'.

    Qt's own words: https://doc.qt.io/qt-6/qsysinfo.html#kernelVersion

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSysInfo::kernelVersion()
    return Rituals.call('ritual_ZN8QSysInfo13kernelVersionEv')

  @staticmethod
  def productType() -> str:
    """
    Calls Qt's 'QString QSysInfo::productType()'.

    Qt's own words: https://doc.qt.io/qt-6/qsysinfo.html#productType

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSysInfo::productType()
    return Rituals.call('ritual_ZN8QSysInfo11productTypeEv')

  @staticmethod
  def productVersion() -> str:
    """
    Calls Qt's 'QString QSysInfo::productVersion()'.

    Qt's own words: https://doc.qt.io/qt-6/qsysinfo.html#productVersion

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSysInfo::productVersion()
    return Rituals.call('ritual_ZN8QSysInfo14productVersionEv')

  @staticmethod
  def prettyProductName() -> str:
    """
    Calls Qt's 'QString QSysInfo::prettyProductName()'.

    Qt's own words: https://doc.qt.io/qt-6/qsysinfo.html#prettyProductName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSysInfo::prettyProductName()
    return Rituals.call('ritual_ZN8QSysInfo17prettyProductNameEv')

  @staticmethod
  def machineHostName() -> str:
    """
    Calls Qt's 'QString QSysInfo::machineHostName()'.

    Qt's own words: https://doc.qt.io/qt-6/qsysinfo.html#machineHostName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSysInfo::machineHostName()
    return Rituals.call('ritual_ZN8QSysInfo15machineHostNameEv')

  @staticmethod
  def machineUniqueId() -> QByteArray:
    """
    Calls Qt's 'QByteArray QSysInfo::machineUniqueId()'.

    Qt's own words: https://doc.qt.io/qt-6/qsysinfo.html#machineUniqueId

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QSysInfo::machineUniqueId()
    address = Rituals.call('ritual_ZN8QSysInfo15machineUniqueIdEv')
    from . import QByteArray
    return QByteArray._cuteOwning(address)

  @staticmethod
  def bootUniqueId() -> QByteArray:
    """
    Calls Qt's 'QByteArray QSysInfo::bootUniqueId()'.

    Qt's own words: https://doc.qt.io/qt-6/qsysinfo.html#bootUniqueId

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QSysInfo::bootUniqueId()
    address = Rituals.call('ritual_ZN8QSysInfo12bootUniqueIdEv')
    from . import QByteArray
    return QByteArray._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSysInfo'

  #  Qt's '~QSysInfo()'. Naming it makes this a value class: Python owns
  #  every C++ QSysInfo behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN8QSysInfoD1Ev'

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
