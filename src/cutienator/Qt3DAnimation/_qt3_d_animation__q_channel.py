"""
Qt3DAnimation::QChannel binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DAnimation/qchannel.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import Qt3DAnimation

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QChannel(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's Qt3DAnimation::QChannel: a plain Python object
  standing in front of one C++ Qt3DAnimation::QChannel.

  C++ hands a Qt3DAnimation::QChannel around as a copy, so every C++
  Qt3DAnimation::QChannel behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's Qt3DAnimation::QChannel that has a ritual and that
  Python can call so far, 11 names in all: 'setName', 'name',
  'setJointIndex', 'jointIndex', 'channelComponentCount',
  'appendChannelComponent', 'insertChannelComponent',
  'removeChannelComponent', 'clearChannelComponents', '__eq__', '__ne__'. It
  can be made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QChannel &Qt3DAnimation::QChannel::operator=(const QChannel &a0)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'Qt3DAnimation::QChannel::~QChannel()': the destructor: Python
    removes its C++ Qt3DAnimation::QChannel by it, and has no other use for
    it.
  - Qt's 'const_iterator Qt3DAnimation::QChannel::begin() const': gives
    'QChannelComponent', which has no cute class yet.
  - Qt's 'const_iterator Qt3DAnimation::QChannel::cbegin() const': gives
    'QChannelComponent', which has no cute class yet.
  - Qt's 'const_iterator Qt3DAnimation::QChannel::end() const': gives
    'QChannelComponent', which has no cute class yet.
  - Qt's 'const_iterator Qt3DAnimation::QChannel::cend() const': gives
    'QChannelComponent', which has no cute class yet.
  - Qt's 'const_reverse_iterator Qt3DAnimation::QChannel::rbegin() const':
    gives a type Python has no way to take yet.
  - Qt's 'const_reverse_iterator Qt3DAnimation::QChannel::crbegin() const':
    gives a type Python has no way to take yet.
  - Qt's 'const_reverse_iterator Qt3DAnimation::QChannel::rend() const':
    gives a type Python has no way to take yet.
  - Qt's 'const_reverse_iterator Qt3DAnimation::QChannel::crend() const':
    gives a type Python has no way to take yet.

  What to expect
  --------------

  - The C++ Qt3DAnimation::QChannel is created at the first use, not by
    'Qt3DAnimation::QChannel(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a Qt3DAnimation::QChannel back gives a copy the ritual
    made for Python, in a new cute Qt3DAnimation::QChannel.
  - Each name of Qt's Qt3DAnimation::QChannel that has no cute function yet,
    'begin', 'cbegin', 'cend', 'crbegin', 'crend', 'end', 'rbegin', 'rend',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DAnimation::QChannel'

  #  Qt's '~Qt3DAnimation::QChannel()'. Naming it makes this a value class:
  #  Python owns every C++ Qt3DAnimation::QChannel behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN13Qt3DAnimation8QChannelD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def name(self) -> str:
    """
    Calls Qt's 'QString Qt3DAnimation::QChannel::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3danimation-qchannel.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString Qt3DAnimation::QChannel::name() const
    return self.uglySide.call('ritual_ZNK13Qt3DAnimation8QChannel4nameEv')

  def jointIndex(self) -> int:
    """
    Calls Qt's 'int Qt3DAnimation::QChannel::jointIndex() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qchannel.html#jointIndex
    """
    #  int Qt3DAnimation::QChannel::jointIndex() const
    return self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation8QChannel10jointIndexEv',
    )

  def channelComponentCount(self) -> int:
    """
    Calls Qt's 'int Qt3DAnimation::QChannel::channelComponentCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qchannel.html#channelComponentCount
    """
    #  int Qt3DAnimation::QChannel::channelComponentCount() const
    return self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation8QChannel21channelComponentCountEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setName(self, name: str) -> None:
    """
    Calls Qt's 'void Qt3DAnimation::QChannel::setName(const QString &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qchannel.html#setName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void Qt3DAnimation::QChannel::setName(const QString &name)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation8QChannel7setNameERK7QString', name,
    )

  @overload(int)
  def setJointIndex(self, jointIndex: int) -> None:
    """
    Calls Qt's 'void Qt3DAnimation::QChannel::setJointIndex(int jointIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qchannel.html#setJointIndex

    Parameters
    ----------

    jointIndex : int
      Passed on as it is.
    """
    #  void Qt3DAnimation::QChannel::setJointIndex(int jointIndex)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation8QChannel13setJointIndexEi', jointIndex,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, a1: QChannel) -> bool:
    """
    Calls Qt's 'bool operator==(const QChannel &a0, const QChannel &a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qchannel.html#operator==

    Parameters
    ----------

    a1 : QChannel
      Passed on as a value: Qt reads the C++ Qt3DAnimation::QChannel, which
      stays Python's own.
    """
    #  bool operator==(const QChannel &a0, const QChannel &a1)
    return Rituals.call(
        'ritual_ZN13Qt3DAnimationeqERKNS_8QChannelES2_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(a1),
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
  def __ne__(self, a1: QChannel) -> bool:
    """
    Calls Qt's 'bool operator!=(const QChannel &a0, const QChannel &a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qchannel.html#operator!=

    Parameters
    ----------

    a1 : QChannel
      Passed on as a value: Qt reads the C++ Qt3DAnimation::QChannel, which
      stays Python's own.
    """
    #  bool operator!=(const QChannel &a0, const QChannel &a1)
    return Rituals.call(
        'ritual_ZN13Qt3DAnimationneERKNS_8QChannelES2_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(a1),
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
    Notes what was given, for Qt's 'Qt3DAnimation::QChannel::QChannel()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qchannel.html#QChannel
    """
    #  Qt3DAnimation::QChannel::QChannel()
    self._noteCreation(QChannel, lambda: Rituals.call(
        'ritual_ZN13Qt3DAnimation8QChannelC1Ev',
    ))

  @overload(str)
  def __init__(self, name: str) -> None:
    """
    Notes what was given, for Qt's 'Qt3DAnimation::QChannel::QChannel(const
    QString &name)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qchannel.html#QChannel

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  Qt3DAnimation::QChannel::QChannel(const QString &name)
    self._noteCreation(QChannel, lambda: Rituals.call(
        'ritual_ZN13Qt3DAnimation8QChannelC1ERK7QString', name,
    ))

  @overload(THIS)
  def __init__(self, a0: QChannel) -> None:
    """
    Notes what was given, for Qt's 'Qt3DAnimation::QChannel::QChannel(const
    QChannel &a0)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qchannel.html#QChannel

    Parameters
    ----------

    a0 : QChannel
      Passed on as a value: Qt reads the C++ Qt3DAnimation::QChannel, which
      stays Python's own.
    """
    #  Qt3DAnimation::QChannel::QChannel(const QChannel &a0)
    self._noteCreation(QChannel, lambda: Rituals.call(
        'ritual_ZN13Qt3DAnimation8QChannelC1ERKS0_', self._valueOf(a0),
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

  @overload(WAIT['Qt3DAnimation.QChannelComponent'])
  def appendChannelComponent(
      self,
      component: Qt3DAnimation.QChannelComponent,
  ) -> None:
    """
    Calls Qt's 'void Qt3DAnimation::QChannel::appendChannelComponent(const
    QChannelComponent &component)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qchannel.html#appendChannelComponent

    Parameters
    ----------

    component : Qt3DAnimation.QChannelComponent
      Passed on as a value: Qt reads the C++
      Qt3DAnimation::QChannelComponent, which stays Python's own.
    """
    #  void Qt3DAnimation::QChannel::appendChannelComponent(const
    #      QChannelComponent &component)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation8QChannel22appendChannelComponentERKNS_17Q'
        'ChannelComponentE',
        self._valueOf(component),
    )

  @overload(int, WAIT['Qt3DAnimation.QChannelComponent'])
  def insertChannelComponent(
      self,
      index: int,
      component: Qt3DAnimation.QChannelComponent,
  ) -> None:
    """
    Calls Qt's 'void Qt3DAnimation::QChannel::insertChannelComponent(int
    index, const QChannelComponent &component)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qchannel.html#insertChannelComponent

    Parameters
    ----------

    index : int
      Passed on as it is.

    component : Qt3DAnimation.QChannelComponent
      Passed on as a value: Qt reads the C++
      Qt3DAnimation::QChannelComponent, which stays Python's own.
    """
    #  void Qt3DAnimation::QChannel::insertChannelComponent(int index, const
    #      QChannelComponent &component)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation8QChannel22insertChannelComponentEiRKNS_17'
        'QChannelComponentE',
        index, self._valueOf(component),
    )

  @overload(int)
  def removeChannelComponent(self, index: int) -> None:
    """
    Calls Qt's 'void Qt3DAnimation::QChannel::removeChannelComponent(int
    index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qchannel.html#removeChannelComponent

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void Qt3DAnimation::QChannel::removeChannelComponent(int index)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation8QChannel22removeChannelComponentEi', index,
    )

  def clearChannelComponents(self) -> None:
    """
    Calls Qt's 'void Qt3DAnimation::QChannel::clearChannelComponents()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qchannel.html#clearChannelComponents
    """
    #  void Qt3DAnimation::QChannel::clearChannelComponents()
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation8QChannel22clearChannelComponentsEv',
    )

  @staticmethod
  def begin(*__, **_) -> Never:
    """
    Qt's 'const_iterator Qt3DAnimation::QChannel::begin() const': gives
    'QChannelComponent', which has no cute class yet.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.QChannel.begin' has no cute function yet. Qt's "
        "'const_iterator Qt3DAnimation::QChannel::begin() const': gives "
        "'QChannelComponent', which has no cute class yet.")

  @staticmethod
  def cbegin(*__, **_) -> Never:
    """
    Qt's 'const_iterator Qt3DAnimation::QChannel::cbegin() const': gives
    'QChannelComponent', which has no cute class yet.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.QChannel.cbegin' has no cute function yet. Qt's "
        "'const_iterator Qt3DAnimation::QChannel::cbegin() const': gives "
        "'QChannelComponent', which has no cute class yet.")

  @staticmethod
  def cend(*__, **_) -> Never:
    """
    Qt's 'const_iterator Qt3DAnimation::QChannel::cend() const': gives
    'QChannelComponent', which has no cute class yet.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.QChannel.cend' has no cute function yet. Qt's "
        "'const_iterator Qt3DAnimation::QChannel::cend() const': gives "
        "'QChannelComponent', which has no cute class yet.")

  @staticmethod
  def crbegin(*__, **_) -> Never:
    """
    Qt's 'const_reverse_iterator Qt3DAnimation::QChannel::crbegin() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.QChannel.crbegin' has no cute function yet. Qt's "
        "'const_reverse_iterator Qt3DAnimation::QChannel::crbegin() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def crend(*__, **_) -> Never:
    """
    Qt's 'const_reverse_iterator Qt3DAnimation::QChannel::crend() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.QChannel.crend' has no cute function yet. Qt's "
        "'const_reverse_iterator Qt3DAnimation::QChannel::crend() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def end(*__, **_) -> Never:
    """
    Qt's 'const_iterator Qt3DAnimation::QChannel::end() const': gives
    'QChannelComponent', which has no cute class yet.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.QChannel.end' has no cute function yet. Qt's "
        "'const_iterator Qt3DAnimation::QChannel::end() const': gives "
        "'QChannelComponent', which has no cute class yet.")

  @staticmethod
  def rbegin(*__, **_) -> Never:
    """
    Qt's 'const_reverse_iterator Qt3DAnimation::QChannel::rbegin() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.QChannel.rbegin' has no cute function yet. Qt's "
        "'const_reverse_iterator Qt3DAnimation::QChannel::rbegin() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def rend(*__, **_) -> Never:
    """
    Qt's 'const_reverse_iterator Qt3DAnimation::QChannel::rend() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.QChannel.rend' has no cute function yet. Qt's "
        "'const_reverse_iterator Qt3DAnimation::QChannel::rend() const': "
        "gives a type Python has no way to take yet.")
