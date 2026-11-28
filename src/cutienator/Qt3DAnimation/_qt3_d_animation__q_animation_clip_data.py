"""
Qt3DAnimation::QAnimationClipData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DAnimation/qanimationclipdata.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import Qt3DAnimation

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QAnimationClipData(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's Qt3DAnimation::QAnimationClipData: a plain Python
  object standing in front of one C++ Qt3DAnimation::QAnimationClipData.

  C++ hands a Qt3DAnimation::QAnimationClipData around as a copy, so every
  C++ Qt3DAnimation::QAnimationClipData behind a cute one is Python's own: it
  is removed, by the ritual named in '__delete_ritual__', when the cute
  object goes.

  What exists
  -----------

  Every function of Qt's Qt3DAnimation::QAnimationClipData that has a ritual
  and that Python can call so far, 10 names in all: 'setName', 'name',
  'channelCount', 'appendChannel', 'insertChannel', 'removeChannel',
  'clearChannels', 'isValid', '__eq__', '__ne__'. It can be made from Python,
  in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QAnimationClipData
    &Qt3DAnimation::QAnimationClipData::operator=(const QAnimationClipData
    &a0)': assignment: Python binds a name and has no operator for it.
  - Qt's 'Qt3DAnimation::QAnimationClipData::~QAnimationClipData()': the
    destructor: Python removes its C++ Qt3DAnimation::QAnimationClipData by
    it, and has no other use for it.
  - Qt's 'const_iterator Qt3DAnimation::QAnimationClipData::begin() const':
    gives 'QChannel', which has no cute class yet.
  - Qt's 'const_iterator Qt3DAnimation::QAnimationClipData::cbegin() const':
    gives 'QChannel', which has no cute class yet.
  - Qt's 'const_iterator Qt3DAnimation::QAnimationClipData::end() const':
    gives 'QChannel', which has no cute class yet.
  - Qt's 'const_iterator Qt3DAnimation::QAnimationClipData::cend() const':
    gives 'QChannel', which has no cute class yet.
  - Qt's 'const_reverse_iterator Qt3DAnimation::QAnimationClipData::rbegin()
    const': gives a type Python has no way to take yet.
  - Qt's 'const_reverse_iterator Qt3DAnimation::QAnimationClipData::crbegin()
    const': gives a type Python has no way to take yet.
  - Qt's 'const_reverse_iterator Qt3DAnimation::QAnimationClipData::rend()
    const': gives a type Python has no way to take yet.
  - Qt's 'const_reverse_iterator Qt3DAnimation::QAnimationClipData::crend()
    const': gives a type Python has no way to take yet.

  What to expect
  --------------

  - The C++ Qt3DAnimation::QAnimationClipData is created at the first use,
    not by 'Qt3DAnimation::QAnimationClipData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a Qt3DAnimation::QAnimationClipData back gives a copy
    the ritual made for Python, in a new cute
    Qt3DAnimation::QAnimationClipData.
  - Each name of Qt's Qt3DAnimation::QAnimationClipData that has no cute
    function yet, 'begin', 'cbegin', 'cend', 'crbegin', 'crend', 'end',
    'rbegin', 'rend', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DAnimation::QAnimationClipData'

  #  Qt's '~Qt3DAnimation::QAnimationClipData()'. Naming it makes this a
  #  value class: Python owns every C++ Qt3DAnimation::QAnimationClipData
  #  behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN13Qt3DAnimation18QAnimationClipDataD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def name(self) -> str:
    """
    Calls Qt's 'QString Qt3DAnimation::QAnimationClipData::name() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qanimationclipdata.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString Qt3DAnimation::QAnimationClipData::name() const
    return self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation18QAnimationClipData4nameEv',
    )

  def channelCount(self) -> int:
    """
    Calls Qt's 'int Qt3DAnimation::QAnimationClipData::channelCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qanimationclipdata.html#channelCount
    """
    #  int Qt3DAnimation::QAnimationClipData::channelCount() const
    return self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation18QAnimationClipData12channelCountEv',
    )

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool Qt3DAnimation::QAnimationClipData::isValid() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qanimationclipdata.html#isValid
    """
    #  bool Qt3DAnimation::QAnimationClipData::isValid() const
    return self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation18QAnimationClipData7isValidEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setName(self, name: str) -> None:
    """
    Calls Qt's 'void Qt3DAnimation::QAnimationClipData::setName(const QString
    &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qanimationclipdata.html#setName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void Qt3DAnimation::QAnimationClipData::setName(const QString &name)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation18QAnimationClipData7setNameERK7QString',
        name,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, a1: QAnimationClipData) -> bool:
    """
    Calls Qt's 'bool operator==(const QAnimationClipData &a0, const
    QAnimationClipData &a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qanimationclipdata.html#operator==

    Parameters
    ----------

    a1 : QAnimationClipData
      Passed on as a value: Qt reads the C++
      Qt3DAnimation::QAnimationClipData, which stays Python's own.
    """
    #  bool operator==(const QAnimationClipData &a0, const QAnimationClipData
    #      &a1)
    return Rituals.call(
        'ritual_ZN13Qt3DAnimationeqERKNS_18QAnimationClipDataES2_',
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
  def __ne__(self, a1: QAnimationClipData) -> bool:
    """
    Calls Qt's 'bool operator!=(const QAnimationClipData &a0, const
    QAnimationClipData &a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qanimationclipdata.html#operator!=

    Parameters
    ----------

    a1 : QAnimationClipData
      Passed on as a value: Qt reads the C++
      Qt3DAnimation::QAnimationClipData, which stays Python's own.
    """
    #  bool operator!=(const QAnimationClipData &a0, const QAnimationClipData
    #      &a1)
    return Rituals.call(
        'ritual_ZN13Qt3DAnimationneERKNS_18QAnimationClipDataES2_',
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
    Notes what was given, for Qt's
    'Qt3DAnimation::QAnimationClipData::QAnimationClipData()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qanimationclipdata.html
    """
    #  Qt3DAnimation::QAnimationClipData::QAnimationClipData()
    self._noteCreation(QAnimationClipData, lambda: Rituals.call(
        'ritual_ZN13Qt3DAnimation18QAnimationClipDataC1Ev',
    ))

  @overload(THIS)
  def __init__(self, a0: QAnimationClipData) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DAnimation::QAnimationClipData::QAnimationClipData(const
    QAnimationClipData &a0)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qanimationclipdata.html

    Parameters
    ----------

    a0 : QAnimationClipData
      Passed on as a value: Qt reads the C++
      Qt3DAnimation::QAnimationClipData, which stays Python's own.
    """
    #  Qt3DAnimation::QAnimationClipData::QAnimationClipData(const
    #      QAnimationClipData &a0)
    self._noteCreation(QAnimationClipData, lambda: Rituals.call(
        'ritual_ZN13Qt3DAnimation18QAnimationClipDataC1ERKS0_',
        self._valueOf(a0),
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

  @overload(WAIT['Qt3DAnimation.QChannel'])
  def appendChannel(self, c: Qt3DAnimation.QChannel) -> None:
    """
    Calls Qt's 'void Qt3DAnimation::QAnimationClipData::appendChannel(const
    QChannel &c)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qanimationclipdata.html

    Parameters
    ----------

    c : Qt3DAnimation.QChannel
      Passed on as a value: Qt reads the C++ Qt3DAnimation::QChannel, which
      stays Python's own.
    """
    #  void Qt3DAnimation::QAnimationClipData::appendChannel(const QChannel
    #      &c)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation18QAnimationClipData13appendChannelERKNS_8'
        'QChannelE',
        self._valueOf(c),
    )

  @overload(int, WAIT['Qt3DAnimation.QChannel'])
  def insertChannel(self, index: int, c: Qt3DAnimation.QChannel) -> None:
    """
    Calls Qt's 'void Qt3DAnimation::QAnimationClipData::insertChannel(int
    index, const QChannel &c)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qanimationclipdata.html

    Parameters
    ----------

    index : int
      Passed on as it is.

    c : Qt3DAnimation.QChannel
      Passed on as a value: Qt reads the C++ Qt3DAnimation::QChannel, which
      stays Python's own.
    """
    #  void Qt3DAnimation::QAnimationClipData::insertChannel(int index, const
    #      QChannel &c)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation18QAnimationClipData13insertChannelEiRKNS_'
        '8QChannelE',
        index, self._valueOf(c),
    )

  @overload(int)
  def removeChannel(self, index: int) -> None:
    """
    Calls Qt's 'void Qt3DAnimation::QAnimationClipData::removeChannel(int
    index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qanimationclipdata.html

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void Qt3DAnimation::QAnimationClipData::removeChannel(int index)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation18QAnimationClipData13removeChannelEi',
        index,
    )

  def clearChannels(self) -> None:
    """
    Calls Qt's 'void Qt3DAnimation::QAnimationClipData::clearChannels()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qanimationclipdata.html
    """
    #  void Qt3DAnimation::QAnimationClipData::clearChannels()
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation18QAnimationClipData13clearChannelsEv',
    )

  @staticmethod
  def begin(*__, **_) -> Never:
    """
    Qt's 'const_iterator Qt3DAnimation::QAnimationClipData::begin() const':
    gives 'QChannel', which has no cute class yet.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.QAnimationClipData.begin' has no cute function yet. "
        "Qt's 'const_iterator Qt3DAnimation::QAnimationClipData::begin() "
        "const': gives 'QChannel', which has no cute class yet.")

  @staticmethod
  def cbegin(*__, **_) -> Never:
    """
    Qt's 'const_iterator Qt3DAnimation::QAnimationClipData::cbegin() const':
    gives 'QChannel', which has no cute class yet.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.QAnimationClipData.cbegin' has no cute function "
        "yet. Qt's 'const_iterator "
        "Qt3DAnimation::QAnimationClipData::cbegin() const': gives "
        "'QChannel', which has no cute class yet.")

  @staticmethod
  def cend(*__, **_) -> Never:
    """
    Qt's 'const_iterator Qt3DAnimation::QAnimationClipData::cend() const':
    gives 'QChannel', which has no cute class yet.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.QAnimationClipData.cend' has no cute function yet. "
        "Qt's 'const_iterator Qt3DAnimation::QAnimationClipData::cend() "
        "const': gives 'QChannel', which has no cute class yet.")

  @staticmethod
  def crbegin(*__, **_) -> Never:
    """
    Qt's 'const_reverse_iterator Qt3DAnimation::QAnimationClipData::crbegin()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.QAnimationClipData.crbegin' has no cute function "
        "yet. Qt's 'const_reverse_iterator "
        "Qt3DAnimation::QAnimationClipData::crbegin() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def crend(*__, **_) -> Never:
    """
    Qt's 'const_reverse_iterator Qt3DAnimation::QAnimationClipData::crend()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.QAnimationClipData.crend' has no cute function yet. "
        "Qt's 'const_reverse_iterator "
        "Qt3DAnimation::QAnimationClipData::crend() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def end(*__, **_) -> Never:
    """
    Qt's 'const_iterator Qt3DAnimation::QAnimationClipData::end() const':
    gives 'QChannel', which has no cute class yet.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.QAnimationClipData.end' has no cute function yet. "
        "Qt's 'const_iterator Qt3DAnimation::QAnimationClipData::end() "
        "const': gives 'QChannel', which has no cute class yet.")

  @staticmethod
  def rbegin(*__, **_) -> Never:
    """
    Qt's 'const_reverse_iterator Qt3DAnimation::QAnimationClipData::rbegin()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.QAnimationClipData.rbegin' has no cute function "
        "yet. Qt's 'const_reverse_iterator "
        "Qt3DAnimation::QAnimationClipData::rbegin() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def rend(*__, **_) -> Never:
    """
    Qt's 'const_reverse_iterator Qt3DAnimation::QAnimationClipData::rend()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.QAnimationClipData.rend' has no cute function yet. "
        "Qt's 'const_reverse_iterator "
        "Qt3DAnimation::QAnimationClipData::rend() const': gives a type "
        "Python has no way to take yet.")
