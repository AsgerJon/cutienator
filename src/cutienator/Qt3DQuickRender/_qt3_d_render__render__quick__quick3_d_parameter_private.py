"""
Qt3DRender::Render::Quick::Quick3DParameterPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DQuickRender/6.12.0/Qt3DQuickRender/private/quick3dparameter_p_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means Qt3DRender::Render::Quick::Quick3DParameterPrivate to be private:
#  it declares the class in a header it calls private. cutienator does not
#  care. Qt hands objects of the class out all the same, and a class we are
#  handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..Qt3DRender import Qt3DRender
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVariant = WAIT['QVariant']


class Quick3DParameterPrivate(Qt3DRender.QParameterPrivate):
  """
  The cute side of Qt's Qt3DRender::Render::Quick::Quick3DParameterPrivate: a
  plain Python object standing in front of one C++
  Qt3DRender::Render::Quick::Quick3DParameterPrivate.

  It is built on the cute 'Qt3DRender::QParameterPrivate', as Qt's
  Qt3DRender::Render::Quick::Quick3DParameterPrivate is built on Qt's
  Qt3DRender::QParameterPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::Render::Quick::Quick3DParameterPrivate
  that has a ritual and that Python can call so far, 2 names in all:
  'q_func', 'setValue'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const Quick3DParameter
    *Qt3DRender::Render::Quick::Quick3DParameterPrivate::q_func() const':
    takes in Python what 'Quick3DParameter
    *Qt3DRender::Render::Quick::Quick3DParameterPrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ Qt3DRender::Render::Quick::Quick3DParameterPrivate is created at
    the first use, not by
    'Qt3DRender::Render::Quick::Quick3DParameterPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++
    Qt3DRender::Render::Quick::Quick3DParameterPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::Render::Quick::Quick3DParameterPrivate'

  #  A C++ Qt3DRender::Render::Quick::Quick3DParameterPrivate Python makes is
  #  of a C++ class of ours, in which Python can take functions over. This
  #  ritual hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_Render_Quick_Quick3DParameterPrivate'

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

  @overload(QVariant)
  def setValue(self, value: QVariant) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::Quick::Quick3DParameterPrivate::setValue(const
    QVariant &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-quick-quick3dparameterprivate.html

    Parameters
    ----------

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void
    #      Qt3DRender::Render::Quick::Quick3DParameterPrivate::setValue(const
    #      QVariant &value)
    ritual = (
        'ritual_ZN10Qt3DRender6Render5Quick23Quick3DParameterPrivate8setVal'
        'ueERK8QVariant')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10Qt3DRender6Render5Quick23Quick3DParameterPrivate8'
          'setValueERK8QVariant')
    self.uglySide.call(ritual, self._valueOf(value))

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
    'Qt3DRender::Render::Quick::Quick3DParameterPrivate::
    Quick3DParameterPrivate()', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-quick-quick3dparameterprivate.html
    """
    #  Qt3DRender::Render::Quick::Quick3DParameterPrivate::
    #      Quick3DParameterPrivate()
    self._noteCreation(Quick3DParameterPrivate, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender6Render5Quick23Quick3DParameterPrivateC1Ev',
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

  def q_func(self) -> Optional[Qt3DRender.Render.Quick.Quick3DParameter]:
    """
    Calls Qt's 'Quick3DParameter
    *Qt3DRender::Render::Quick::Quick3DParameterPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-quick-quick3dparameterprivate.html

    Returns
    -------

    Optional[Qt3DRender.Render.Quick.Quick3DParameter]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Quick3DParameter
    #      *Qt3DRender::Render::Quick::Quick3DParameterPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render5Quick23Quick3DParameterPrivate6q_func'
        'Ev',
    )
    return Qt3DRender.Render.Quick.Quick3DParameter._cuteAt(address)
