"""
Qt3DAnimation::QChannelMappingPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DAnimation/6.12.0/Qt3DAnimation/private/qchannelmapping_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DAnimation::QChannelMappingPrivate to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import Qt3DAnimation

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional


class QChannelMappingPrivate(Qt3DAnimation.QAbstractChannelMappingPrivate):
  """
  The cute side of Qt's Qt3DAnimation::QChannelMappingPrivate: a plain Python
  object standing in front of one C++ Qt3DAnimation::QChannelMappingPrivate.

  It is built on the cute 'Qt3DAnimation::QAbstractChannelMappingPrivate', as
  Qt's Qt3DAnimation::QChannelMappingPrivate is built on Qt's
  Qt3DAnimation::QAbstractChannelMappingPrivate, and has everything that
  class has.

  What exists
  -----------

  Every function of Qt's Qt3DAnimation::QChannelMappingPrivate that has a
  ritual and that Python can call so far, 1 name in all: 'q_func'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QChannelMapping
    *Qt3DAnimation::QChannelMappingPrivate::q_func() const': takes in Python
    what 'QChannelMapping *Qt3DAnimation::QChannelMappingPrivate::q_func()'
    takes.

  What has no ritual
  ------------------

  1 of the 4 functions Qt declares: 1 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ Qt3DAnimation::QChannelMappingPrivate is created at the first
    use, not by 'Qt3DAnimation::QChannelMappingPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DAnimation::QChannelMappingPrivate.
  - Each name of Qt's Qt3DAnimation::QChannelMappingPrivate that has no cute
    function yet, 'updatePropertyNameTypeAndComponentCount', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DAnimation::QChannelMappingPrivate'

  #  A C++ Qt3DAnimation::QChannelMappingPrivate Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DAnimation_QChannelMappingPrivate'

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DAnimation::QChannelMappingPrivate::QChannelMappingPrivate()', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qchannelmappingprivate.html
    """
    #  Qt3DAnimation::QChannelMappingPrivate::QChannelMappingPrivate()
    self._noteCreation(QChannelMappingPrivate, lambda: Rituals.call(
        'ritual_ZN13Qt3DAnimation22QChannelMappingPrivateC1Ev',
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

  def q_func(self) -> Optional[Qt3DAnimation.QChannelMapping]:
    """
    Calls Qt's 'QChannelMapping
    *Qt3DAnimation::QChannelMappingPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qchannelmappingprivate.html#q_func

    Returns
    -------

    Optional[Qt3DAnimation.QChannelMapping]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QChannelMapping *Qt3DAnimation::QChannelMappingPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN13Qt3DAnimation22QChannelMappingPrivate6q_funcEv',
    )
    return Qt3DAnimation.QChannelMapping._cuteAt(address)

  @staticmethod
  def updatePropertyNameTypeAndComponentCount(*__, **_) -> Never:
    """
    Qt's 'void Qt3DAnimation::QChannelMappingPrivate::
    updatePropertyNameTypeAndComponentCount()': Qt's library has no name for
    it, and its code in Qt's source does not compile apart from its file: use
    of undeclared identifier 'componentCountForType'.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.QChannelMappingPrivate.updatePropertyNameTypeAndComp"
        "onentCount' has no cute function yet. Qt's 'void "
        "Qt3DAnimation::QChannelMappingPrivate::updatePropertyNameTypeAndCom"
        "ponentCount()': Qt's library has no name for it, and its code in "
        "Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'componentCountForType'.")
