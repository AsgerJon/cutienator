"""
Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoaderPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DQuickExtras/6.12.0/Qt3DQuickExtras/private/quick3dlevelofdetailloader_p_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoaderPrivate to
#  be private: it declares the class in a header it calls private. cutienator
#  does not care. Qt hands objects of the class out all the same, and a class
#  we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DExtras

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional


class Quick3DLevelOfDetailLoaderPrivate(Qt3DCore.QEntityPrivate):
  """
  The cute side of Qt's
  Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoaderPrivate: a plain
  Python object standing in front of one C++
  Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoaderPrivate.

  It is built on the cute 'Qt3DCore::QEntityPrivate', as Qt's
  Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoaderPrivate is built on
  Qt's Qt3DCore::QEntityPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's
  Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoaderPrivate that has a
  ritual and that Python can call so far, 1 name in all: 'q_func'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const Quick3DLevelOfDetailLoader
    *Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoaderPrivate::q_func()
    const': takes in Python what 'Quick3DLevelOfDetailLoader
    *Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoaderPrivate::q_func()'
    takes.

  What to expect
  --------------

  - The C++ Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoaderPrivate is
    created at the first use, not by
    'Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoaderPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++
    Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoaderPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoaderPrivate'

  #  A C++ Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoaderPrivate
  #  Python makes is of a C++ class of ours, in which Python can take
  #  functions over. This ritual hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DExtras_Extras_Quick_Quick3DLevelOfDetailLoaderPrivate'

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
    'Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoaderPrivate::
    Quick3DLevelOfDetailLoaderPrivate()', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-extras-quick-quick3dlevelofdetailloaderprivate.html
    """
    #  Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoaderPrivate::
    #      Quick3DLevelOfDetailLoaderPrivate()
    self._noteCreation(
        Quick3DLevelOfDetailLoaderPrivate, lambda: Rituals.call(
            'ritual_ZN10Qt3DExtras6Extras5Quick33Quick3DLevelOfDetailLoader'
            'PrivateC1Ev',
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

  def q_func(
      self,
  ) -> Optional[Qt3DExtras.Extras.Quick.Quick3DLevelOfDetailLoader]:
    """
    Calls Qt's 'Quick3DLevelOfDetailLoader
    *Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoaderPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-extras-quick-quick3dlevelofdetailloaderprivate.html

    Returns
    -------

    Optional[Qt3DExtras.Extras.Quick.Quick3DLevelOfDetailLoader]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Quick3DLevelOfDetailLoader
    #      *Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoaderPrivate::
    #      q_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DExtras6Extras5Quick33Quick3DLevelOfDetailLoaderPriv'
        'ate6q_funcEv',
    )
    return Qt3DExtras.Extras.Quick.Quick3DLevelOfDetailLoader._cuteAt(address)
