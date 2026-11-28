"""
Qt3DCore::Quick::QQmlAspectEnginePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DQuick/6.12.0/Qt3DQuick/private/qqmlaspectengine_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DCore::Quick::QQmlAspectEnginePrivate to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QObjectPrivate
from . import Qt3DCore

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional


class QQmlAspectEnginePrivate(QObjectPrivate):
  """
  The cute side of Qt's Qt3DCore::Quick::QQmlAspectEnginePrivate: a plain
  Python object standing in front of one C++
  Qt3DCore::Quick::QQmlAspectEnginePrivate.

  It is built on the cute 'QObjectPrivate', as Qt's
  Qt3DCore::Quick::QQmlAspectEnginePrivate is built on Qt's QObjectPrivate,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DCore::Quick::QQmlAspectEnginePrivate that has a
  ritual and that Python can call so far, 2 names in all: 'q_func',
  '_q_continueExecute'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQmlAspectEngine
    *Qt3DCore::Quick::QQmlAspectEnginePrivate::q_func() const': takes in
    Python what 'QQmlAspectEngine
    *Qt3DCore::Quick::QQmlAspectEnginePrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ Qt3DCore::Quick::QQmlAspectEnginePrivate is created at the first
    use, not by 'Qt3DCore::Quick::QQmlAspectEnginePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DCore::Quick::QQmlAspectEnginePrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DCore::Quick::QQmlAspectEnginePrivate'

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
    'Qt3DCore::Quick::QQmlAspectEnginePrivate::QQmlAspectEnginePrivate()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qqmlaspectengineprivate.html
    """
    #  Qt3DCore::Quick::QQmlAspectEnginePrivate::QQmlAspectEnginePrivate()
    self._noteCreation(QQmlAspectEnginePrivate, lambda: Rituals.call(
        'ritual_ZN8Qt3DCore5Quick23QQmlAspectEnginePrivateC1Ev',
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

  def q_func(self) -> Optional[Qt3DCore.Quick.QQmlAspectEngine]:
    """
    Calls Qt's 'QQmlAspectEngine
    *Qt3DCore::Quick::QQmlAspectEnginePrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qqmlaspectengineprivate.html#q_func

    Returns
    -------

    Optional[Qt3DCore.Quick.QQmlAspectEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlAspectEngine *Qt3DCore::Quick::QQmlAspectEnginePrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN8Qt3DCore5Quick23QQmlAspectEnginePrivate6q_funcEv',
    )
    return Qt3DCore.Quick.QQmlAspectEngine._cuteAt(address)

  def _q_continueExecute(self) -> None:
    """
    Calls Qt's 'void
    Qt3DCore::Quick::QQmlAspectEnginePrivate::_q_continueExecute()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qqmlaspectengineprivate.html
    """
    #  void Qt3DCore::Quick::QQmlAspectEnginePrivate::_q_continueExecute()
    self.uglySide.call(
        'ritual_ZN8Qt3DCore5Quick23QQmlAspectEnginePrivate18_q_continueExec'
        'uteEv',
    )
