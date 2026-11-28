"""
Qt3DLogic::QLogicAspectPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DLogic/6.12.0/Qt3DLogic/private/qlogicaspect_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means Qt3DLogic::QLogicAspectPrivate to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import WAIT
from ..Qt3DCore import Qt3DCore
from . import Qt3DLogic

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional


class QLogicAspectPrivate(Qt3DCore.QAbstractAspectPrivate):
  """
  The cute side of Qt's Qt3DLogic::QLogicAspectPrivate: a plain Python object
  standing in front of one C++ Qt3DLogic::QLogicAspectPrivate.

  It is built on the cute 'Qt3DCore::QAbstractAspectPrivate', as Qt's
  Qt3DLogic::QLogicAspectPrivate is built on Qt's
  Qt3DCore::QAbstractAspectPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DLogic::QLogicAspectPrivate that has a ritual and
  that Python can call so far, 3 names in all: 'q_func',
  'onEngineAboutToShutdown', 'registerBackendTypes'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QLogicAspect *Qt3DLogic::QLogicAspectPrivate::q_func()
    const': takes in Python what 'QLogicAspect
    *Qt3DLogic::QLogicAspectPrivate::q_func()' takes.

  What has no ritual
  ------------------

  1 of the 5 functions Qt declares: 1 leans on 'vtable for Qt3DLogic.

  What to expect
  --------------

  - The C++ Qt3DLogic::QLogicAspectPrivate is created at the first use, not
    by 'Qt3DLogic::QLogicAspectPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DLogic::QLogicAspectPrivate.
  - Each name of Qt's Qt3DLogic::QLogicAspectPrivate that has no cute
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
  __qt_class__ = 'Qt3DLogic::QLogicAspectPrivate'

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
    Qt's 'Qt3DLogic::QLogicAspectPrivate::QLogicAspectPrivate()': leans on
    'vtable for Qt3DLogic::Logic::Executor', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'Qt3DLogic.QLogicAspectPrivate.__init__' has no cute function yet. "
        "Qt's 'Qt3DLogic::QLogicAspectPrivate::QLogicAspectPrivate()': "
        "leans on 'vtable for Qt3DLogic::Logic::Executor', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

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

  def q_func(self) -> Optional[Qt3DLogic.QLogicAspect]:
    """
    Calls Qt's 'QLogicAspect *Qt3DLogic::QLogicAspectPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dlogic-qlogicaspectprivate.html#q_func

    Returns
    -------

    Optional[Qt3DLogic.QLogicAspect]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLogicAspect *Qt3DLogic::QLogicAspectPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN9Qt3DLogic19QLogicAspectPrivate6q_funcEv',
    )
    return Qt3DLogic.QLogicAspect._cuteAt(address)

  def onEngineAboutToShutdown(self) -> None:
    """
    Calls Qt's 'void
    Qt3DLogic::QLogicAspectPrivate::onEngineAboutToShutdown()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dlogic-qlogicaspectprivate.html
    """
    #  void Qt3DLogic::QLogicAspectPrivate::onEngineAboutToShutdown()
    ritual = (
        'ritual_ZN9Qt3DLogic19QLogicAspectPrivate23onEngineAboutToShutdownE'
        'v')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN9Qt3DLogic19QLogicAspectPrivate23onEngineAboutToShu'
          'tdownEv')
    self.uglySide.call(ritual)

  def registerBackendTypes(self) -> None:
    """
    Calls Qt's 'void Qt3DLogic::QLogicAspectPrivate::registerBackendTypes()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dlogic-qlogicaspectprivate.html
    """
    #  void Qt3DLogic::QLogicAspectPrivate::registerBackendTypes()
    self.uglySide.call(
        'ritual_ZN9Qt3DLogic19QLogicAspectPrivate20registerBackendTypesEv',
    )
