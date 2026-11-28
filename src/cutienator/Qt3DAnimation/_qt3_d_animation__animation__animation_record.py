"""
Qt3DAnimation::Animation::AnimationRecord binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DAnimation/6.12.0/Qt3DAnimation/private/animationutils_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DAnimation::Animation::AnimationRecord to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QVariant

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class AnimationRecord(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's Qt3DAnimation::Animation::AnimationRecord: a plain
  Python object standing in front of one C++
  Qt3DAnimation::Animation::AnimationRecord.

  C++ hands a Qt3DAnimation::Animation::AnimationRecord around as a copy, so
  every C++ Qt3DAnimation::Animation::AnimationRecord behind a cute one is
  Python's own: it is removed, by the ritual named in '__delete_ritual__',
  when the cute object goes.

  What exists
  -----------

  No function of Qt's Qt3DAnimation::Animation::AnimationRecord yet. None can
  be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DAnimation::Animation::AnimationRecord::~AnimationRecord()': the
    destructor: Python removes its C++
    Qt3DAnimation::Animation::AnimationRecord by it, and has no other use for
    it.

  What to expect
  --------------

  - The C++ Qt3DAnimation::Animation::AnimationRecord is created at the first
    use, not by 'Qt3DAnimation::Animation::AnimationRecord(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a Qt3DAnimation::Animation::AnimationRecord back gives
    a copy the ritual made for Python, in a new cute
    Qt3DAnimation::Animation::AnimationRecord.
  """

  #  The classes Qt writes inside Qt3DAnimation::Animation::AnimationRecord,
  #  each a class in here as in C++.

  class TargetChange(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's
    Qt3DAnimation::Animation::AnimationRecord::TargetChange: a plain Python
    object standing in front of one C++
    Qt3DAnimation::Animation::AnimationRecord::TargetChange.

    C++ hands a Qt3DAnimation::Animation::AnimationRecord::TargetChange
    around as a copy, so every C++
    Qt3DAnimation::Animation::AnimationRecord::TargetChange behind a cute one
    is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's
    Qt3DAnimation::Animation::AnimationRecord::TargetChange yet. It can be
    made from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'Qt3DAnimation::Animation::AnimationRecord::TargetChange::
      ~TargetChange()': the destructor: Python removes its C++
      Qt3DAnimation::Animation::AnimationRecord::TargetChange by it, and has
      no other use for it.

    What to expect
    --------------

    - The C++ Qt3DAnimation::Animation::AnimationRecord::TargetChange is
      created at the first use, not by
      'Qt3DAnimation::Animation::AnimationRecord::TargetChange(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a
      Qt3DAnimation::Animation::AnimationRecord::TargetChange back gives a
      copy the ritual made for Python, in a new cute
      Qt3DAnimation::Animation::AnimationRecord::TargetChange.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QVariant = WAIT['QVariant']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'Qt3DAnimation::Animation::AnimationRecord::TargetChange'

    #  Qt's '~Qt3DAnimation::Animation::AnimationRecord::TargetChange()'.
    #  Naming it makes this a value class: Python owns every C++
    #  Qt3DAnimation::Animation::AnimationRecord::TargetChange behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN13Qt3DAnimation9Animation15AnimationRecord12TargetChangeD1Ev')

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

    @overload(WAIT['Qt3DCore.QNodeId'], str, QVariant)
    @overload(WAIT['Qt3DCore.QNodeId'], NoneType, QVariant)
    def __init__(
        self,
        id: Qt3DCore.QNodeId,
        name: Optional[str],
        v: QVariant,
    ) -> None:
      """
      Notes what was given, for Qt's
      'Qt3DAnimation::Animation::AnimationRecord::TargetChange::TargetChange(
      Qt3DCore::QNodeId id, const char *name, QVariant v)', which is called
      at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qt3danimation-animation-animationrecord-targetchange.html

      Parameters
      ----------

      id : Qt3DCore.QNodeId
        Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
        Python's own.

      name : Optional[str]
        Passed on as the bytes of the text. None is passed on as no text.

      v : QVariant
        Passed on as a value: Qt reads the C++ QVariant, which stays Python's
        own.
      """
      #  Qt3DAnimation::Animation::AnimationRecord::TargetChange::
      #      TargetChange(Qt3DCore::QNodeId id, const char *name, QVariant v)
      self._noteCreation(AnimationRecord.TargetChange, lambda: Rituals.call(
          'ritual_ZN13Qt3DAnimation9Animation15AnimationRecord12TargetChang'
          'eC1EN8Qt3DCore7QNodeIdEPKc8QVariant',
          self._valueOf(id), self._bytesOf(name), self._valueOf(v),
      ))

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
  __qt_class__ = 'Qt3DAnimation::Animation::AnimationRecord'

  #  Qt's '~Qt3DAnimation::Animation::AnimationRecord()'. Naming it makes
  #  this a value class: Python owns every C++
  #  Qt3DAnimation::Animation::AnimationRecord behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = (
      'ritual_ZN13Qt3DAnimation9Animation15AnimationRecordD1Ev')

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
