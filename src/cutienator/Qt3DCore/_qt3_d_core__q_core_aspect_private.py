"""
Qt3DCore::QCoreAspectPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DCore/6.12.0/Qt3DCore/private/qcoreaspect_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means Qt3DCore::QCoreAspectPrivate to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import Qt3DCore

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QCoreAspectPrivate(Qt3DCore.QAbstractAspectPrivate):
  """
  The cute side of Qt's Qt3DCore::QCoreAspectPrivate: a plain Python object
  standing in front of one C++ Qt3DCore::QCoreAspectPrivate.

  It is built on the cute 'Qt3DCore::QAbstractAspectPrivate', as Qt's
  Qt3DCore::QCoreAspectPrivate is built on Qt's
  Qt3DCore::QAbstractAspectPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DCore::QCoreAspectPrivate that has a ritual and
  that Python can call so far, 4 names in all: 'q_func', 'get', 'jobsDone',
  'frameDone'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DCore::QCoreAspectPrivate::~QCoreAspectPrivate()': the
    destructor: Python never removes a C++ Qt3DCore::QCoreAspectPrivate.
  - Qt's 'const QCoreAspect *Qt3DCore::QCoreAspectPrivate::q_func() const':
    takes in Python what 'QCoreAspect
    *Qt3DCore::QCoreAspectPrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ Qt3DCore::QCoreAspectPrivate is created at the first use, not by
    'Qt3DCore::QCoreAspectPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DCore::QCoreAspectPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(WAIT['Qt3DCore.QCoreAspect'])
  @overload(NoneType)
  def get(
      aspect: Optional[Qt3DCore.QCoreAspect],
  ) -> Optional[QCoreAspectPrivate]:
    """
    Calls Qt's 'QCoreAspectPrivate
    *Qt3DCore::QCoreAspectPrivate::get(QCoreAspect *aspect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qcoreaspectprivate.html#get

    Parameters
    ----------

    aspect : Optional[Qt3DCore.QCoreAspect]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QCoreAspectPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCoreAspectPrivate *Qt3DCore::QCoreAspectPrivate::get(QCoreAspect
    #      *aspect)
    address = Rituals.call(
        'ritual_ZN8Qt3DCore18QCoreAspectPrivate3getEPNS_11QCoreAspectE',
        CuteMixin._addressOf(aspect),
    )
    return QCoreAspectPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DCore::QCoreAspectPrivate'

  #  A C++ Qt3DCore::QCoreAspectPrivate Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DCore_QCoreAspectPrivate'

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
    'Qt3DCore::QCoreAspectPrivate::QCoreAspectPrivate()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qcoreaspectprivate.html
    """
    #  Qt3DCore::QCoreAspectPrivate::QCoreAspectPrivate()
    self._noteCreation(QCoreAspectPrivate, lambda: Rituals.call(
        'ritual_ZN8Qt3DCore18QCoreAspectPrivateC1Ev',
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

  def q_func(self) -> Optional[Qt3DCore.QCoreAspect]:
    """
    Calls Qt's 'QCoreAspect *Qt3DCore::QCoreAspectPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qcoreaspectprivate.html#q_func

    Returns
    -------

    Optional[Qt3DCore.QCoreAspect]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCoreAspect *Qt3DCore::QCoreAspectPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN8Qt3DCore18QCoreAspectPrivate6q_funcEv',
    )
    return Qt3DCore.QCoreAspect._cuteAt(address)

  def jobsDone(self) -> None:
    """
    Calls Qt's 'void Qt3DCore::QCoreAspectPrivate::jobsDone()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qcoreaspectprivate.html#jobsDone
    """
    #  void Qt3DCore::QCoreAspectPrivate::jobsDone()
    ritual = 'ritual_ZN8Qt3DCore18QCoreAspectPrivate8jobsDoneEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN8Qt3DCore18QCoreAspectPrivate8jobsDoneEv'
    self.uglySide.call(ritual)

  def frameDone(self) -> None:
    """
    Calls Qt's 'void Qt3DCore::QCoreAspectPrivate::frameDone()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qcoreaspectprivate.html#frameDone
    """
    #  void Qt3DCore::QCoreAspectPrivate::frameDone()
    ritual = 'ritual_ZN8Qt3DCore18QCoreAspectPrivate9frameDoneEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN8Qt3DCore18QCoreAspectPrivate9frameDoneEv'
    self.uglySide.call(ritual)
