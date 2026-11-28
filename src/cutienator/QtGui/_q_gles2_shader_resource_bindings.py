"""
QGles2ShaderResourceBindings binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qrhigles2_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QGles2ShaderResourceBindings to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QRhiShaderResourceBindings

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QRhiImplementation
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRhiImplementation = WAIT['QRhiImplementation']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGles2ShaderResourceBindings(QRhiShaderResourceBindings):
  """
  The cute side of Qt's QGles2ShaderResourceBindings: a plain Python object
  standing in front of one C++ QGles2ShaderResourceBindings.

  It is built on the cute 'QRhiShaderResourceBindings', as Qt's
  QGles2ShaderResourceBindings is built on Qt's QRhiShaderResourceBindings,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's QGles2ShaderResourceBindings that has a ritual and
  that Python can call so far, 3 names in all: 'destroy', 'create',
  'updateResources'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGles2ShaderResourceBindings::~QGles2ShaderResourceBindings()': the
    destructor: Python never removes a C++ QGles2ShaderResourceBindings.

  What to expect
  --------------

  - The C++ QGles2ShaderResourceBindings is created at the first use, not by
    'QGles2ShaderResourceBindings(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGles2ShaderResourceBindings.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGles2ShaderResourceBindings'

  #  A C++ QGles2ShaderResourceBindings Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGles2ShaderResourceBindings'

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

  @overload(QRhiImplementation)
  @overload(NoneType)
  def __init__(self, rhi: Optional[QRhiImplementation]) -> None:
    """
    Notes what was given, for Qt's
    'QGles2ShaderResourceBindings::QGles2ShaderResourceBindings(
    QRhiImplementation *rhi)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgles2shaderresourcebindings.html

    Parameters
    ----------

    rhi : Optional[QRhiImplementation]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QGles2ShaderResourceBindings::QGles2ShaderResourceBindings(
    #      QRhiImplementation *rhi)
    self._noteCreation(QGles2ShaderResourceBindings, lambda: Rituals.call(
        'ritual_ZN28QGles2ShaderResourceBindingsC1EP18QRhiImplementation',
        self._addressOf(rhi),
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

  def destroy(self) -> None:
    """
    Calls Qt's 'void QGles2ShaderResourceBindings::destroy()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgles2shaderresourcebindings.html#destroy
    """
    #  void QGles2ShaderResourceBindings::destroy()
    ritual = 'ritual_ZN28QGles2ShaderResourceBindings7destroyEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN28QGles2ShaderResourceBindings7destroyEv'
    self.uglySide.call(ritual)

  def create(self) -> bool:
    """
    Calls Qt's 'bool QGles2ShaderResourceBindings::create()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgles2shaderresourcebindings.html#create
    """
    #  bool QGles2ShaderResourceBindings::create()
    ritual = 'ritual_ZN28QGles2ShaderResourceBindings6createEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN28QGles2ShaderResourceBindings6createEv'
    return self.uglySide.call(ritual)

  @overload(QRhiShaderResourceBindings.UpdateFlags)
  def updateResources(
      self,
      flags: QRhiShaderResourceBindings.UpdateFlags,
  ) -> None:
    """
    Calls Qt's 'void
    QGles2ShaderResourceBindings::updateResources(UpdateFlags flags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgles2shaderresourcebindings.html#updateResources

    Parameters
    ----------

    flags : QRhiShaderResourceBindings.UpdateFlags
      Passed on as its number.
    """
    #  void QGles2ShaderResourceBindings::updateResources(UpdateFlags flags)
    ritual = (
        'ritual_ZN28QGles2ShaderResourceBindings15updateResourcesE6QFlagsIN'
        '26QRhiShaderResourceBindings10UpdateFlagEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN28QGles2ShaderResourceBindings15updateResourcesE6QF'
          'lagsIN26QRhiShaderResourceBindings10UpdateFlagEE')
    self.uglySide.call(ritual, flags.value)
