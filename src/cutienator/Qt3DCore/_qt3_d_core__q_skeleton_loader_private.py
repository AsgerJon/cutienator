"""
Qt3DCore::QSkeletonLoaderPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DCore/6.12.0/Qt3DCore/private/qskeletonloader_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means Qt3DCore::QSkeletonLoaderPrivate to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import Qt3DCore

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSkeletonLoaderPrivate(Qt3DCore.QAbstractSkeletonPrivate):
  """
  The cute side of Qt's Qt3DCore::QSkeletonLoaderPrivate: a plain Python
  object standing in front of one C++ Qt3DCore::QSkeletonLoaderPrivate.

  It is built on the cute 'Qt3DCore::QAbstractSkeletonPrivate', as Qt's
  Qt3DCore::QSkeletonLoaderPrivate is built on Qt's
  Qt3DCore::QAbstractSkeletonPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DCore::QSkeletonLoaderPrivate that has a ritual
  and that Python can call so far, 3 names in all: 'setStatus',
  'setRootJoint', 'q_func'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QSkeletonLoader *Qt3DCore::QSkeletonLoaderPrivate::q_func()
    const': takes in Python what 'QSkeletonLoader
    *Qt3DCore::QSkeletonLoaderPrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ Qt3DCore::QSkeletonLoaderPrivate is created at the first use, not
    by 'Qt3DCore::QSkeletonLoaderPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DCore::QSkeletonLoaderPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DCore::QSkeletonLoaderPrivate'

  #  A C++ Qt3DCore::QSkeletonLoaderPrivate Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DCore_QSkeletonLoaderPrivate'

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

  @overload(Qt3DCore.QSkeletonLoader.Status)
  def setStatus(self, status: Qt3DCore.QSkeletonLoader.Status) -> None:
    """
    Calls Qt's 'void
    Qt3DCore::QSkeletonLoaderPrivate::setStatus(QSkeletonLoader::Status
    status)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qskeletonloaderprivate.html#setStatus

    Parameters
    ----------

    status : Qt3DCore.QSkeletonLoader.Status
      Passed on as its number.
    """
    #  void Qt3DCore::QSkeletonLoaderPrivate::setStatus(QSkeletonLoader::
    #      Status status)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore22QSkeletonLoaderPrivate9setStatusENS_15QSkeleto'
        'nLoader6StatusE',
        status.value,
    )

  @overload(WAIT['Qt3DCore.QJoint'])
  @overload(NoneType)
  def setRootJoint(self, rootJoint: Optional[Qt3DCore.QJoint]) -> None:
    """
    Calls Qt's 'void Qt3DCore::QSkeletonLoaderPrivate::setRootJoint(QJoint
    *rootJoint)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qskeletonloaderprivate.html#setRootJoint

    Parameters
    ----------

    rootJoint : Optional[Qt3DCore.QJoint]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DCore::QSkeletonLoaderPrivate::setRootJoint(QJoint *rootJoint)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore22QSkeletonLoaderPrivate12setRootJointEPNS_6QJoi'
        'ntE',
        self._addressOf(rootJoint),
    )

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
    'Qt3DCore::QSkeletonLoaderPrivate::QSkeletonLoaderPrivate()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qskeletonloaderprivate.html
    """
    #  Qt3DCore::QSkeletonLoaderPrivate::QSkeletonLoaderPrivate()
    self._noteCreation(QSkeletonLoaderPrivate, lambda: Rituals.call(
        'ritual_ZN8Qt3DCore22QSkeletonLoaderPrivateC1Ev',
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

  def q_func(self) -> Optional[Qt3DCore.QSkeletonLoader]:
    """
    Calls Qt's 'QSkeletonLoader *Qt3DCore::QSkeletonLoaderPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qskeletonloaderprivate.html#q_func

    Returns
    -------

    Optional[Qt3DCore.QSkeletonLoader]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSkeletonLoader *Qt3DCore::QSkeletonLoaderPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN8Qt3DCore22QSkeletonLoaderPrivate6q_funcEv',
    )
    return Qt3DCore.QSkeletonLoader._cuteAt(address)
