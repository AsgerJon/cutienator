"""
Qt3DAnimation::QAnimationAspectPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DAnimation/6.12.0/Qt3DAnimation/private/qanimationaspect_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means Qt3DAnimation::QAnimationAspectPrivate to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import WAIT
from ..Qt3DCore import Qt3DCore
from . import Qt3DAnimation

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional


class QAnimationAspectPrivate(Qt3DCore.QAbstractAspectPrivate):
  """
  The cute side of Qt's Qt3DAnimation::QAnimationAspectPrivate: a plain
  Python object standing in front of one C++
  Qt3DAnimation::QAnimationAspectPrivate.

  It is built on the cute 'Qt3DCore::QAbstractAspectPrivate', as Qt's
  Qt3DAnimation::QAnimationAspectPrivate is built on Qt's
  Qt3DCore::QAbstractAspectPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DAnimation::QAnimationAspectPrivate that has a
  ritual and that Python can call so far, 1 name in all: 'q_func'. None can
  be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QAnimationAspect
    *Qt3DAnimation::QAnimationAspectPrivate::q_func() const': takes in Python
    what 'QAnimationAspect *Qt3DAnimation::QAnimationAspectPrivate::q_func()'
    takes.

  What has no ritual
  ------------------

  1 of the 3 functions Qt declares: 1 leans on 'Qt3DAnimation.

  What to expect
  --------------

  - The C++ Qt3DAnimation::QAnimationAspectPrivate is created at the first
    use, not by 'Qt3DAnimation::QAnimationAspectPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DAnimation::QAnimationAspectPrivate.
  - Each name of Qt's Qt3DAnimation::QAnimationAspectPrivate that has no cute
    function yet, '__init__', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DAnimation::QAnimationAspectPrivate'

  #  A C++ Qt3DAnimation::QAnimationAspectPrivate Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DAnimation_QAnimationAspectPrivate'

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'Qt3DAnimation::QAnimationAspectPrivate::QAnimationAspectPrivate()':
    leans on
    'Qt3DAnimation::Animation::buildPropertyMappings(QList<Qt3DAnimation::
    Animation::ChannelMapping*> const&,
    QList<Qt3DAnimation::Animation::ChannelNameAndType> const&,
    QList<QList<long long> > const&, QList<QBitArray> const&)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.QAnimationAspectPrivate.__init__' has no cute "
        "function yet. Qt's "
        "'Qt3DAnimation::QAnimationAspectPrivate::QAnimationAspectPrivate()'"
        ": leans on "
        "'Qt3DAnimation::Animation::buildPropertyMappings(QList<Qt3DAnimatio"
        "n::Animation::ChannelMapping*> const&, "
        "QList<Qt3DAnimation::Animation::ChannelNameAndType> const&, "
        "QList<QList<long long> > const&, QList<QBitArray> const&)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

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

  def q_func(self) -> Optional[Qt3DAnimation.QAnimationAspect]:
    """
    Calls Qt's 'QAnimationAspect
    *Qt3DAnimation::QAnimationAspectPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qanimationaspectprivate.html#q_func

    Returns
    -------

    Optional[Qt3DAnimation.QAnimationAspect]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAnimationAspect *Qt3DAnimation::QAnimationAspectPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN13Qt3DAnimation23QAnimationAspectPrivate6q_funcEv',
    )
    return Qt3DAnimation.QAnimationAspect._cuteAt(address)
