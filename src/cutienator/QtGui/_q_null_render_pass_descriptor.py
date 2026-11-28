"""
QNullRenderPassDescriptor binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qrhinull_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QNullRenderPassDescriptor to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QRhiRenderPassDescriptor

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


class QNullRenderPassDescriptor(QRhiRenderPassDescriptor):
  """
  The cute side of Qt's QNullRenderPassDescriptor: a plain Python object
  standing in front of one C++ QNullRenderPassDescriptor.

  It is built on the cute 'QRhiRenderPassDescriptor', as Qt's
  QNullRenderPassDescriptor is built on Qt's QRhiRenderPassDescriptor, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QNullRenderPassDescriptor that has a ritual and that
  Python can call so far, 3 names in all: 'destroy', 'isCompatible',
  'newCompatibleRenderPassDescriptor'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QNullRenderPassDescriptor::~QNullRenderPassDescriptor()': the
    destructor: Python never removes a C++ QNullRenderPassDescriptor.
  - Qt's 'QVector<quint32> QNullRenderPassDescriptor::serializedFormat()
    const': gives a type Python has no way to take yet.

  What to expect
  --------------

  - The C++ QNullRenderPassDescriptor is created at the first use, not by
    'QNullRenderPassDescriptor(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QNullRenderPassDescriptor.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QNullRenderPassDescriptor'

  #  A C++ QNullRenderPassDescriptor Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QNullRenderPassDescriptor'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QRhiRenderPassDescriptor)
  @overload(NoneType)
  def isCompatible(self, other: Optional[QRhiRenderPassDescriptor]) -> bool:
    """
    Calls Qt's 'bool QNullRenderPassDescriptor::isCompatible(const
    QRhiRenderPassDescriptor *other) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnullrenderpassdescriptor.html#isCompatible

    Parameters
    ----------

    other : Optional[QRhiRenderPassDescriptor]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QNullRenderPassDescriptor::isCompatible(const
    #      QRhiRenderPassDescriptor *other) const
    ritual = (
        'ritual_ZNK25QNullRenderPassDescriptor12isCompatibleEPK24QRhiRender'
        'PassDescriptor')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK25QNullRenderPassDescriptor12isCompatibleEPK24QRhi'
          'RenderPassDescriptor')
    return self.uglySide.call(ritual, self._addressOf(other))

  def newCompatibleRenderPassDescriptor(
      self,
  ) -> Optional[QRhiRenderPassDescriptor]:
    """
    Calls Qt's 'QRhiRenderPassDescriptor
    *QNullRenderPassDescriptor::newCompatibleRenderPassDescriptor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnullrenderpassdescriptor.html

    Returns
    -------

    Optional[QRhiRenderPassDescriptor]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiRenderPassDescriptor
    #      *QNullRenderPassDescriptor::newCompatibleRenderPassDescriptor()
    #      const
    ritual = (
        'ritual_ZNK25QNullRenderPassDescriptor33newCompatibleRenderPassDesc'
        'riptorEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK25QNullRenderPassDescriptor33newCompatibleRenderPa'
          'ssDescriptorEv')
    address = self.uglySide.call(ritual)
    return QRhiRenderPassDescriptor._cuteAt(address)

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
    'QNullRenderPassDescriptor::QNullRenderPassDescriptor(QRhiImplementation
    *rhi)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qnullrenderpassdescriptor.html

    Parameters
    ----------

    rhi : Optional[QRhiImplementation]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QNullRenderPassDescriptor::QNullRenderPassDescriptor(
    #      QRhiImplementation *rhi)
    self._noteCreation(QNullRenderPassDescriptor, lambda: Rituals.call(
        'ritual_ZN25QNullRenderPassDescriptorC1EP18QRhiImplementation',
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
    Calls Qt's 'void QNullRenderPassDescriptor::destroy()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnullrenderpassdescriptor.html#destroy
    """
    #  void QNullRenderPassDescriptor::destroy()
    ritual = 'ritual_ZN25QNullRenderPassDescriptor7destroyEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN25QNullRenderPassDescriptor7destroyEv'
    self.uglySide.call(ritual)
