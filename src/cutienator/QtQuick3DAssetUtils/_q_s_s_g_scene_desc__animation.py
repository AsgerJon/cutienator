"""
QSSGSceneDesc::Animation binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DAssetUtils/6.12.0/QtQuick3DAssetUtils/private/qssgscenedesc_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGSceneDesc::Animation to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute
from ..QtCore import QMetaType

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QVariant


class Animation(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSSGSceneDesc::Animation: a plain Python object
  standing in front of one C++ QSSGSceneDesc::Animation.

  C++ hands a QSSGSceneDesc::Animation around as a copy, so every C++
  QSSGSceneDesc::Animation behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QSSGSceneDesc::Animation yet. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSSGSceneDesc::Animation::~Animation()': the destructor: Python
    removes its C++ QSSGSceneDesc::Animation by it, and has no other use for
    it.

  What to expect
  --------------

  - The C++ QSSGSceneDesc::Animation is created at the first use, not by
    'QSSGSceneDesc::Animation(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSSGSceneDesc::Animation back gives a copy the ritual
    made for Python, in a new cute QSSGSceneDesc::Animation.
  """

  #  The classes Qt writes inside QSSGSceneDesc::Animation, each a class in
  #  here as in C++.

  class Channel(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QSSGSceneDesc::Animation::Channel: a plain Python
    object standing in front of one C++ QSSGSceneDesc::Animation::Channel.

    C++ hands a QSSGSceneDesc::Animation::Channel around as a copy, so every
    C++ QSSGSceneDesc::Animation::Channel behind a cute one is Python's own:
    it is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    No function of Qt's QSSGSceneDesc::Animation::Channel yet. None can be
    made from Python: one comes out of a function of another class that gives
    one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QSSGSceneDesc::Animation::Channel::~Channel()': the destructor:
      Python removes its C++ QSSGSceneDesc::Animation::Channel by it, and has
      no other use for it.

    What to expect
    --------------

    - The C++ QSSGSceneDesc::Animation::Channel is created at the first use,
      not by 'QSSGSceneDesc::Animation::Channel(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QSSGSceneDesc::Animation::Channel back gives a copy
      the ritual made for Python, in a new cute
      QSSGSceneDesc::Animation::Channel.
    """

    #  The enums Qt writes inside QSSGSceneDesc::Animation::Channel, each a
    #  class in here as in C++, and the names Qt has for the combinations of
    #  its flags enums.

    class TargetProperty(CuteNum, scoped=True):
      """
      The enum 'QSSGSceneDesc::Animation::Channel::TargetProperty' of Qt,
      with the 5 names Qt gives in it. C++ keeps these names inside the enum,
      so the class that holds the enum does not have them.
      """

      Unknown = Kee[int](0)
      Position = Kee[int](1)
      Rotation = Kee[int](2)
      Scale = Kee[int](3)
      Weight = Kee[int](4)

    class TargetType(CuteNum, scoped=True):
      """
      The enum 'QSSGSceneDesc::Animation::Channel::TargetType' of Qt, with
      the 1 names Qt gives in it. C++ keeps these names inside the enum, so
      the class that holds the enum does not have them.
      """

      Property = Kee[int](0)

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QSSGSceneDesc::Animation::Channel'

    #  Qt's '~QSSGSceneDesc::Animation::Channel()'. Naming it makes this a
    #  value class: Python owns every C++ QSSGSceneDesc::Animation::Channel
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN13QSSGSceneDesc9Animation7ChannelD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  class KeyPosition(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QSSGSceneDesc::Animation::KeyPosition: a plain
    Python object standing in front of one C++
    QSSGSceneDesc::Animation::KeyPosition.

    C++ hands a QSSGSceneDesc::Animation::KeyPosition around as a copy, so
    every C++ QSSGSceneDesc::Animation::KeyPosition behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    Every function of Qt's QSSGSceneDesc::Animation::KeyPosition that has a
    ritual and that Python can call so far, 4 names in all: 'getValueType',
    'getKeyType', 'getValue', 'getValueQMetaType'. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QSSGSceneDesc::Animation::KeyPosition::~KeyPosition()': the
      destructor: Python removes its C++
      QSSGSceneDesc::Animation::KeyPosition by it, and has no other use for
      it.

    What to expect
    --------------

    - The C++ QSSGSceneDesc::Animation::KeyPosition is created at the first
      use, not by 'QSSGSceneDesc::Animation::KeyPosition(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QSSGSceneDesc::Animation::KeyPosition back gives a
      copy the ritual made for Python, in a new cute
      QSSGSceneDesc::Animation::KeyPosition.
    """

    #  The enums Qt writes inside QSSGSceneDesc::Animation::KeyPosition, each
    #  a class in here as in C++, and the names Qt has for the combinations
    #  of its flags enums.

    class KeyType(CuteNum, scoped=True):
      """
      The enum 'QSSGSceneDesc::Animation::KeyPosition::KeyType' of Qt, with
      the 2 names Qt gives in it. C++ keeps these names inside the enum, so
      the class that holds the enum does not have them.
      """

      Frame = Kee[int](256)
      Time = Kee[int](512)

    class ValueType(CuteNum, scoped=True):
      """
      The enum 'QSSGSceneDesc::Animation::KeyPosition::ValueType' of Qt, with
      the 5 names Qt gives in it. C++ keeps these names inside the enum, so
      the class that holds the enum does not have them.
      """

      Number = Kee[int](0)
      Vec2 = Kee[int](1)
      Vec3 = Kee[int](2)
      Vec4 = Kee[int](3)
      Quaternion = Kee[int](4)

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QSSGSceneDesc::Animation::KeyPosition'

    #  Qt's '~QSSGSceneDesc::Animation::KeyPosition()'. Naming it makes this
    #  a value class: Python owns every C++
    #  QSSGSceneDesc::Animation::KeyPosition behind a cute one, and removes
    #  it by this ritual.
    __delete_ritual__ = 'ritual_ZN13QSSGSceneDesc9Animation11KeyPositionD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def getValueType(self) -> ValueType:
      """
      Calls Qt's 'ValueType
      QSSGSceneDesc::Animation::KeyPosition::getValueType() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qssgscenedesc-animation-keyposition.html

      Returns
      -------

      ValueType
        The member standing for the number Qt gave back. For a number Qt
        gives no name it is the member without a name that
        'ValueType(number)' gives.
      """
      #  ValueType QSSGSceneDesc::Animation::KeyPosition::getValueType()
      #      const
      return Animation.KeyPosition.ValueType(self.uglySide.call(
          'ritual_ZNK13QSSGSceneDesc9Animation11KeyPosition12getValueTypeEv',
      ))

    def getKeyType(self) -> KeyType:
      """
      Calls Qt's 'KeyType QSSGSceneDesc::Animation::KeyPosition::getKeyType()
      const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qssgscenedesc-animation-keyposition.html

      Returns
      -------

      KeyType
        The member standing for the number Qt gave back. For a number Qt
        gives no name it is the member without a name that 'KeyType(number)'
        gives.
      """
      #  KeyType QSSGSceneDesc::Animation::KeyPosition::getKeyType() const
      return Animation.KeyPosition.KeyType(self.uglySide.call(
          'ritual_ZNK13QSSGSceneDesc9Animation11KeyPosition10getKeyTypeEv',
      ))

    def getValue(self) -> QVariant:
      """
      Calls Qt's 'QVariant QSSGSceneDesc::Animation::KeyPosition::getValue()
      const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qssgscenedesc-animation-keyposition.html

      Returns
      -------

      QVariant
        A new cute QVariant around the copy Qt gave back. Python owns it.
      """
      #  QVariant QSSGSceneDesc::Animation::KeyPosition::getValue() const
      address = self.uglySide.call(
          'ritual_ZNK13QSSGSceneDesc9Animation11KeyPosition8getValueEv',
      )
      from ..QtCore import QVariant
      return QVariant._cuteOwning(address)

    def getValueQMetaType(self) -> QMetaType.Type:
      """
      Calls Qt's 'QMetaType::Type
      QSSGSceneDesc::Animation::KeyPosition::getValueQMetaType() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qssgscenedesc-animation-keyposition.html

      Returns
      -------

      QMetaType.Type
        The member standing for the number Qt gave back. For a number Qt
        gives no name it is the member without a name that
        'QMetaType.Type(number)' gives.
      """
      #  QMetaType::Type
      #      QSSGSceneDesc::Animation::KeyPosition::getValueQMetaType() const
      return QMetaType.Type(self.uglySide.call(
          'ritual_ZNK13QSSGSceneDesc9Animation11KeyPosition17getValueQMetaT'
          'ypeEv',
      ))

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGSceneDesc::Animation'

  #  Qt's '~QSSGSceneDesc::Animation()'. Naming it makes this a value class:
  #  Python owns every C++ QSSGSceneDesc::Animation behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN13QSSGSceneDesc9AnimationD1Ev'

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
