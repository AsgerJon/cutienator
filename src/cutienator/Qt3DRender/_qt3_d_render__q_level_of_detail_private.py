"""
Qt3DRender::QLevelOfDetailPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/qlevelofdetail_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DRender::QLevelOfDetailPrivate to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional


class QLevelOfDetailPrivate(Qt3DCore.QComponentPrivate):
  """
  The cute side of Qt's Qt3DRender::QLevelOfDetailPrivate: a plain Python
  object standing in front of one C++ Qt3DRender::QLevelOfDetailPrivate.

  It is built on the cute 'Qt3DCore::QComponentPrivate', as Qt's
  Qt3DRender::QLevelOfDetailPrivate is built on Qt's
  Qt3DCore::QComponentPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QLevelOfDetailPrivate that has a ritual
  and that Python can call so far, 2 names in all: 'q_func',
  'setCurrentIndex'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QLevelOfDetail *Qt3DRender::QLevelOfDetailPrivate::q_func()
    const': takes in Python what 'QLevelOfDetail
    *Qt3DRender::QLevelOfDetailPrivate::q_func()' takes.

  What has no ritual
  ------------------

  2 of the 6 functions Qt declares: 2 cannot be called and cannot be called
  through the meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ Qt3DRender::QLevelOfDetailPrivate is created at the first use,
    not by 'Qt3DRender::QLevelOfDetailPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::QLevelOfDetailPrivate.
  - Each name of Qt's Qt3DRender::QLevelOfDetailPrivate that has no cute
    function yet, '_q_centerChanged', '_q_radiusChanged', holds a function
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
  __qt_class__ = 'Qt3DRender::QLevelOfDetailPrivate'

  #  A C++ Qt3DRender::QLevelOfDetailPrivate Python makes is of a C++ class
  #  of ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_QLevelOfDetailPrivate'

  #  The functions Qt calls itself that Qt3DRender::QLevelOfDetailPrivate is
  #  the first to declare. A class of a program built on it can write one
  #  anew, and Qt then calls that. For each name: the key C++ knows the
  #  function by, what it gives, and what it takes.
  __virtual_functions__ = {
      'setCurrentIndex': (
          ('_ZN10Qt3DRender21QLevelOfDetailPrivate15setCurrentIndexEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
  }

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

  @overload(int)
  def setCurrentIndex(self, currentIndex: int) -> None:
    """
    Calls Qt's 'void Qt3DRender::QLevelOfDetailPrivate::setCurrentIndex(int
    currentIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qlevelofdetailprivate.html

    Parameters
    ----------

    currentIndex : int
      Passed on as it is.
    """
    #  void Qt3DRender::QLevelOfDetailPrivate::setCurrentIndex(int
    #      currentIndex)
    ritual = (
        'ritual_ZN10Qt3DRender21QLevelOfDetailPrivate15setCurrentIndexEi')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10Qt3DRender21QLevelOfDetailPrivate15setCurrentInde'
          'xEi')
    self.uglySide.call(ritual, currentIndex)

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
    'Qt3DRender::QLevelOfDetailPrivate::QLevelOfDetailPrivate()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qlevelofdetailprivate.html
    """
    #  Qt3DRender::QLevelOfDetailPrivate::QLevelOfDetailPrivate()
    self._noteCreation(QLevelOfDetailPrivate, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender21QLevelOfDetailPrivateC1Ev',
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

  def q_func(self) -> Optional[Qt3DRender.QLevelOfDetail]:
    """
    Calls Qt's 'QLevelOfDetail *Qt3DRender::QLevelOfDetailPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qlevelofdetailprivate.html#q_func

    Returns
    -------

    Optional[Qt3DRender.QLevelOfDetail]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLevelOfDetail *Qt3DRender::QLevelOfDetailPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender21QLevelOfDetailPrivate6q_funcEv',
    )
    return Qt3DRender.QLevelOfDetail._cuteAt(address)

  @staticmethod
  def _q_centerChanged(*__, **_) -> Never:
    """
    Qt's 'void Qt3DRender::QLevelOfDetailPrivate::_q_centerChanged(const
    QVector3D &center)': cannot be called and cannot be called through the
    meta-object and cannot be copied: no header file has its code, Qt's
    source does not mark it or its class for use from outside Qt or writes it
    'inline' or nowhere, and it is no signal, slot or invokable function
    giving back nothing, of a class built on QObject, and Qt's source has no
    code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'Qt3DRender.QLevelOfDetailPrivate._q_centerChanged' has no cute "
        "function yet. Qt's 'void "
        "Qt3DRender::QLevelOfDetailPrivate::_q_centerChanged(const "
        "QVector3D &center)': cannot be called and cannot be called through "
        "the meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def _q_radiusChanged(*__, **_) -> Never:
    """
    Qt's 'void Qt3DRender::QLevelOfDetailPrivate::_q_radiusChanged(float
    radius)': cannot be called and cannot be called through the meta-object
    and cannot be copied: no header file has its code, Qt's source does not
    mark it or its class for use from outside Qt or writes it 'inline' or
    nowhere, and it is no signal, slot or invokable function giving back
    nothing, of a class built on QObject, and Qt's source has no code for it
    that could be told from the rest.
    """
    raise NotImplementedError(
        "'Qt3DRender.QLevelOfDetailPrivate._q_radiusChanged' has no cute "
        "function yet. Qt's 'void "
        "Qt3DRender::QLevelOfDetailPrivate::_q_radiusChanged(float "
        "radius)': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")
