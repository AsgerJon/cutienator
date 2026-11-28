"""
Qt3DAnimation::QChannelComponent binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DAnimation/qchannelcomponent.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import Qt3DAnimation

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QChannelComponent(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's Qt3DAnimation::QChannelComponent: a plain Python
  object standing in front of one C++ Qt3DAnimation::QChannelComponent.

  C++ hands a Qt3DAnimation::QChannelComponent around as a copy, so every C++
  Qt3DAnimation::QChannelComponent behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's Qt3DAnimation::QChannelComponent that has a ritual
  and that Python can call so far, 9 names in all: 'setName', 'name',
  'keyFrameCount', 'appendKeyFrame', 'insertKeyFrame', 'removeKeyFrame',
  'clearKeyFrames', '__eq__', '__ne__'. It can be made from Python, in 3
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QChannelComponent
    &Qt3DAnimation::QChannelComponent::operator=(const QChannelComponent
    &a0)': assignment: Python binds a name and has no operator for it.
  - Qt's 'Qt3DAnimation::QChannelComponent::~QChannelComponent()': the
    destructor: Python removes its C++ Qt3DAnimation::QChannelComponent by
    it, and has no other use for it.
  - Qt's 'const_iterator Qt3DAnimation::QChannelComponent::begin() const':
    gives 'QKeyFrame', which has no cute class yet.
  - Qt's 'const_iterator Qt3DAnimation::QChannelComponent::cbegin() const':
    gives 'QKeyFrame', which has no cute class yet.
  - Qt's 'const_iterator Qt3DAnimation::QChannelComponent::end() const':
    gives 'QKeyFrame', which has no cute class yet.
  - Qt's 'const_iterator Qt3DAnimation::QChannelComponent::cend() const':
    gives 'QKeyFrame', which has no cute class yet.
  - Qt's 'const_reverse_iterator Qt3DAnimation::QChannelComponent::rbegin()
    const': gives a type Python has no way to take yet.
  - Qt's 'const_reverse_iterator Qt3DAnimation::QChannelComponent::crbegin()
    const': gives a type Python has no way to take yet.
  - Qt's 'const_reverse_iterator Qt3DAnimation::QChannelComponent::rend()
    const': gives a type Python has no way to take yet.
  - Qt's 'const_reverse_iterator Qt3DAnimation::QChannelComponent::crend()
    const': gives a type Python has no way to take yet.

  What to expect
  --------------

  - The C++ Qt3DAnimation::QChannelComponent is created at the first use, not
    by 'Qt3DAnimation::QChannelComponent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a Qt3DAnimation::QChannelComponent back gives a copy
    the ritual made for Python, in a new cute
    Qt3DAnimation::QChannelComponent.
  - Each name of Qt's Qt3DAnimation::QChannelComponent that has no cute
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
  __qt_class__ = 'Qt3DAnimation::QChannelComponent'

  #  Qt's '~Qt3DAnimation::QChannelComponent()'. Naming it makes this a value
  #  class: Python owns every C++ Qt3DAnimation::QChannelComponent behind a
  #  cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN13Qt3DAnimation17QChannelComponentD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def name(self) -> str:
    """
    Calls Qt's 'QString Qt3DAnimation::QChannelComponent::name() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qchannelcomponent.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString Qt3DAnimation::QChannelComponent::name() const
    return self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation17QChannelComponent4nameEv',
    )

  def keyFrameCount(self) -> int:
    """
    Calls Qt's 'int Qt3DAnimation::QChannelComponent::keyFrameCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qchannelcomponent.html#keyFrameCount
    """
    #  int Qt3DAnimation::QChannelComponent::keyFrameCount() const
    return self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation17QChannelComponent13keyFrameCountEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setName(self, name: str) -> None:
    """
    Calls Qt's 'void Qt3DAnimation::QChannelComponent::setName(const QString
    &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qchannelcomponent.html#setName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void Qt3DAnimation::QChannelComponent::setName(const QString &name)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation17QChannelComponent7setNameERK7QString',
        name,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, a1: QChannelComponent) -> bool:
    """
    Calls Qt's 'bool operator==(const QChannelComponent &a0, const
    QChannelComponent &a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qchannelcomponent.html#operator==

    Parameters
    ----------

    a1 : QChannelComponent
      Passed on as a value: Qt reads the C++
      Qt3DAnimation::QChannelComponent, which stays Python's own.
    """
    #  bool operator==(const QChannelComponent &a0, const QChannelComponent
    #      &a1)
    return Rituals.call(
        'ritual_ZN13Qt3DAnimationeqERKNS_17QChannelComponentES2_',
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
  def __ne__(self, a1: QChannelComponent) -> bool:
    """
    Calls Qt's 'bool operator!=(const QChannelComponent &a0, const
    QChannelComponent &a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qchannelcomponent.html#operator!=

    Parameters
    ----------

    a1 : QChannelComponent
      Passed on as a value: Qt reads the C++
      Qt3DAnimation::QChannelComponent, which stays Python's own.
    """
    #  bool operator!=(const QChannelComponent &a0, const QChannelComponent
    #      &a1)
    return Rituals.call(
        'ritual_ZN13Qt3DAnimationneERKNS_17QChannelComponentES2_',
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
    'Qt3DAnimation::QChannelComponent::QChannelComponent()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qchannelcomponent.html
    """
    #  Qt3DAnimation::QChannelComponent::QChannelComponent()
    self._noteCreation(QChannelComponent, lambda: Rituals.call(
        'ritual_ZN13Qt3DAnimation17QChannelComponentC1Ev',
    ))

  @overload(str)
  def __init__(self, name: str) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DAnimation::QChannelComponent::QChannelComponent(const QString
    &name)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qchannelcomponent.html

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  Qt3DAnimation::QChannelComponent::QChannelComponent(const QString
    #      &name)
    self._noteCreation(QChannelComponent, lambda: Rituals.call(
        'ritual_ZN13Qt3DAnimation17QChannelComponentC1ERK7QString', name,
    ))

  @overload(THIS)
  def __init__(self, a0: QChannelComponent) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DAnimation::QChannelComponent::QChannelComponent(const
    QChannelComponent &a0)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qchannelcomponent.html

    Parameters
    ----------

    a0 : QChannelComponent
      Passed on as a value: Qt reads the C++
      Qt3DAnimation::QChannelComponent, which stays Python's own.
    """
    #  Qt3DAnimation::QChannelComponent::QChannelComponent(const
    #      QChannelComponent &a0)
    self._noteCreation(QChannelComponent, lambda: Rituals.call(
        'ritual_ZN13Qt3DAnimation17QChannelComponentC1ERKS0_',
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

  @overload(WAIT['Qt3DAnimation.QKeyFrame'])
  def appendKeyFrame(self, kf: Qt3DAnimation.QKeyFrame) -> None:
    """
    Calls Qt's 'void Qt3DAnimation::QChannelComponent::appendKeyFrame(const
    QKeyFrame &kf)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qchannelcomponent.html

    Parameters
    ----------

    kf : Qt3DAnimation.QKeyFrame
      Passed on as a value: Qt reads the C++ Qt3DAnimation::QKeyFrame, which
      stays Python's own.
    """
    #  void Qt3DAnimation::QChannelComponent::appendKeyFrame(const QKeyFrame
    #      &kf)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation17QChannelComponent14appendKeyFrameERKNS_9'
        'QKeyFrameE',
        self._valueOf(kf),
    )

  @overload(int, WAIT['Qt3DAnimation.QKeyFrame'])
  def insertKeyFrame(self, index: int, kf: Qt3DAnimation.QKeyFrame) -> None:
    """
    Calls Qt's 'void Qt3DAnimation::QChannelComponent::insertKeyFrame(int
    index, const QKeyFrame &kf)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qchannelcomponent.html

    Parameters
    ----------

    index : int
      Passed on as it is.

    kf : Qt3DAnimation.QKeyFrame
      Passed on as a value: Qt reads the C++ Qt3DAnimation::QKeyFrame, which
      stays Python's own.
    """
    #  void Qt3DAnimation::QChannelComponent::insertKeyFrame(int index, const
    #      QKeyFrame &kf)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation17QChannelComponent14insertKeyFrameEiRKNS_'
        '9QKeyFrameE',
        index, self._valueOf(kf),
    )

  @overload(int)
  def removeKeyFrame(self, index: int) -> None:
    """
    Calls Qt's 'void Qt3DAnimation::QChannelComponent::removeKeyFrame(int
    index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qchannelcomponent.html

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void Qt3DAnimation::QChannelComponent::removeKeyFrame(int index)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation17QChannelComponent14removeKeyFrameEi',
        index,
    )

  def clearKeyFrames(self) -> None:
    """
    Calls Qt's 'void Qt3DAnimation::QChannelComponent::clearKeyFrames()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qchannelcomponent.html
    """
    #  void Qt3DAnimation::QChannelComponent::clearKeyFrames()
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation17QChannelComponent14clearKeyFramesEv',
    )

  @staticmethod
  def begin(*__, **_) -> Never:
    """
    Qt's 'const_iterator Qt3DAnimation::QChannelComponent::begin() const':
    gives 'QKeyFrame', which has no cute class yet.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.QChannelComponent.begin' has no cute function yet. "
        "Qt's 'const_iterator Qt3DAnimation::QChannelComponent::begin() "
        "const': gives 'QKeyFrame', which has no cute class yet.")

  @staticmethod
  def cbegin(*__, **_) -> Never:
    """
    Qt's 'const_iterator Qt3DAnimation::QChannelComponent::cbegin() const':
    gives 'QKeyFrame', which has no cute class yet.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.QChannelComponent.cbegin' has no cute function yet. "
        "Qt's 'const_iterator Qt3DAnimation::QChannelComponent::cbegin() "
        "const': gives 'QKeyFrame', which has no cute class yet.")

  @staticmethod
  def cend(*__, **_) -> Never:
    """
    Qt's 'const_iterator Qt3DAnimation::QChannelComponent::cend() const':
    gives 'QKeyFrame', which has no cute class yet.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.QChannelComponent.cend' has no cute function yet. "
        "Qt's 'const_iterator Qt3DAnimation::QChannelComponent::cend() "
        "const': gives 'QKeyFrame', which has no cute class yet.")

  @staticmethod
  def crbegin(*__, **_) -> Never:
    """
    Qt's 'const_reverse_iterator Qt3DAnimation::QChannelComponent::crbegin()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.QChannelComponent.crbegin' has no cute function "
        "yet. Qt's 'const_reverse_iterator "
        "Qt3DAnimation::QChannelComponent::crbegin() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def crend(*__, **_) -> Never:
    """
    Qt's 'const_reverse_iterator Qt3DAnimation::QChannelComponent::crend()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.QChannelComponent.crend' has no cute function yet. "
        "Qt's 'const_reverse_iterator "
        "Qt3DAnimation::QChannelComponent::crend() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def end(*__, **_) -> Never:
    """
    Qt's 'const_iterator Qt3DAnimation::QChannelComponent::end() const':
    gives 'QKeyFrame', which has no cute class yet.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.QChannelComponent.end' has no cute function yet. "
        "Qt's 'const_iterator Qt3DAnimation::QChannelComponent::end() "
        "const': gives 'QKeyFrame', which has no cute class yet.")

  @staticmethod
  def rbegin(*__, **_) -> Never:
    """
    Qt's 'const_reverse_iterator Qt3DAnimation::QChannelComponent::rbegin()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.QChannelComponent.rbegin' has no cute function yet. "
        "Qt's 'const_reverse_iterator "
        "Qt3DAnimation::QChannelComponent::rbegin() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def rend(*__, **_) -> Never:
    """
    Qt's 'const_reverse_iterator Qt3DAnimation::QChannelComponent::rend()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.QChannelComponent.rend' has no cute function yet. "
        "Qt's 'const_reverse_iterator "
        "Qt3DAnimation::QChannelComponent::rend() const': gives a type "
        "Python has no way to take yet.")
