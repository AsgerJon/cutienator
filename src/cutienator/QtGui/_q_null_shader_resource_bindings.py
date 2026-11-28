"""
QNullShaderResourceBindings binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qrhinull_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QNullShaderResourceBindings to be private: it declares the class
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


class QNullShaderResourceBindings(QRhiShaderResourceBindings):
  """
  The cute side of Qt's QNullShaderResourceBindings: a plain Python object
  standing in front of one C++ QNullShaderResourceBindings.

  It is built on the cute 'QRhiShaderResourceBindings', as Qt's
  QNullShaderResourceBindings is built on Qt's QRhiShaderResourceBindings,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's QNullShaderResourceBindings that has a ritual and
  that Python can call so far, 3 names in all: 'destroy', 'create',
  'updateResources'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QNullShaderResourceBindings::~QNullShaderResourceBindings()': the
    destructor: Python never removes a C++ QNullShaderResourceBindings.

  What to expect
  --------------

  - The C++ QNullShaderResourceBindings is created at the first use, not by
    'QNullShaderResourceBindings(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QNullShaderResourceBindings.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QNullShaderResourceBindings'

  #  A C++ QNullShaderResourceBindings Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QNullShaderResourceBindings'

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
    'QNullShaderResourceBindings::QNullShaderResourceBindings(
    QRhiImplementation *rhi)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qnullshaderresourcebindings.html

    Parameters
    ----------

    rhi : Optional[QRhiImplementation]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QNullShaderResourceBindings::QNullShaderResourceBindings(
    #      QRhiImplementation *rhi)
    self._noteCreation(QNullShaderResourceBindings, lambda: Rituals.call(
        'ritual_ZN27QNullShaderResourceBindingsC1EP18QRhiImplementation',
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
    Calls Qt's 'void QNullShaderResourceBindings::destroy()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnullshaderresourcebindings.html#destroy
    """
    #  void QNullShaderResourceBindings::destroy()
    ritual = 'ritual_ZN27QNullShaderResourceBindings7destroyEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN27QNullShaderResourceBindings7destroyEv'
    self.uglySide.call(ritual)

  def create(self) -> bool:
    """
    Calls Qt's 'bool QNullShaderResourceBindings::create()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnullshaderresourcebindings.html#create
    """
    #  bool QNullShaderResourceBindings::create()
    ritual = 'ritual_ZN27QNullShaderResourceBindings6createEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN27QNullShaderResourceBindings6createEv'
    return self.uglySide.call(ritual)

  @overload(QRhiShaderResourceBindings.UpdateFlags)
  def updateResources(
      self,
      flags: QRhiShaderResourceBindings.UpdateFlags,
  ) -> None:
    """
    Calls Qt's 'void QNullShaderResourceBindings::updateResources(UpdateFlags
    flags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnullshaderresourcebindings.html#updateResources

    Parameters
    ----------

    flags : QRhiShaderResourceBindings.UpdateFlags
      Passed on as its number.
    """
    #  void QNullShaderResourceBindings::updateResources(UpdateFlags flags)
    ritual = (
        'ritual_ZN27QNullShaderResourceBindings15updateResourcesE6QFlagsIN2'
        '6QRhiShaderResourceBindings10UpdateFlagEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN27QNullShaderResourceBindings15updateResourcesE6QFl'
          'agsIN26QRhiShaderResourceBindings10UpdateFlagEE')
    self.uglySide.call(ritual, flags.value)
