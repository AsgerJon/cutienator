"""
QGles2RenderPassDescriptor binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qrhigles2_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QGles2RenderPassDescriptor to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
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


class QGles2RenderPassDescriptor(QRhiRenderPassDescriptor):
  """
  The cute side of Qt's QGles2RenderPassDescriptor: a plain Python object
  standing in front of one C++ QGles2RenderPassDescriptor.

  It is built on the cute 'QRhiRenderPassDescriptor', as Qt's
  QGles2RenderPassDescriptor is built on Qt's QRhiRenderPassDescriptor, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QGles2RenderPassDescriptor that has a ritual and
  that Python can call so far, 3 names in all: 'destroy', 'isCompatible',
  'newCompatibleRenderPassDescriptor'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGles2RenderPassDescriptor::~QGles2RenderPassDescriptor()': the
    destructor: Python never removes a C++ QGles2RenderPassDescriptor.
  - Qt's 'QVector<quint32> QGles2RenderPassDescriptor::serializedFormat()
    const': gives a type Python has no way to take yet.

  What to expect
  --------------

  - The C++ QGles2RenderPassDescriptor is created at the first use, not by
    'QGles2RenderPassDescriptor(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGles2RenderPassDescriptor.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGles2RenderPassDescriptor'

  #  A C++ QGles2RenderPassDescriptor Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGles2RenderPassDescriptor'

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
    Calls Qt's 'bool QGles2RenderPassDescriptor::isCompatible(const
    QRhiRenderPassDescriptor *other) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgles2renderpassdescriptor.html#isCompatible

    Parameters
    ----------

    other : Optional[QRhiRenderPassDescriptor]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QGles2RenderPassDescriptor::isCompatible(const
    #      QRhiRenderPassDescriptor *other) const
    ritual = (
        'ritual_ZNK26QGles2RenderPassDescriptor12isCompatibleEPK24QRhiRende'
        'rPassDescriptor')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK26QGles2RenderPassDescriptor12isCompatibleEPK24QRh'
          'iRenderPassDescriptor')
    return self.uglySide.call(ritual, self._addressOf(other))

  def newCompatibleRenderPassDescriptor(
      self,
  ) -> Optional[QRhiRenderPassDescriptor]:
    """
    Calls Qt's 'QRhiRenderPassDescriptor
    *QGles2RenderPassDescriptor::newCompatibleRenderPassDescriptor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgles2renderpassdescriptor.html

    Returns
    -------

    Optional[QRhiRenderPassDescriptor]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiRenderPassDescriptor
    #      *QGles2RenderPassDescriptor::newCompatibleRenderPassDescriptor()
    #      const
    ritual = (
        'ritual_ZNK26QGles2RenderPassDescriptor33newCompatibleRenderPassDes'
        'criptorEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK26QGles2RenderPassDescriptor33newCompatibleRenderP'
          'assDescriptorEv')
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
    'QGles2RenderPassDescriptor::QGles2RenderPassDescriptor(
    QRhiImplementation *rhi)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgles2renderpassdescriptor.html

    Parameters
    ----------

    rhi : Optional[QRhiImplementation]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QGles2RenderPassDescriptor::QGles2RenderPassDescriptor(
    #      QRhiImplementation *rhi)
    self._noteCreation(QGles2RenderPassDescriptor, lambda: Rituals.call(
        'ritual_ZN26QGles2RenderPassDescriptorC1EP18QRhiImplementation',
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
    Calls Qt's 'void QGles2RenderPassDescriptor::destroy()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgles2renderpassdescriptor.html#destroy
    """
    #  void QGles2RenderPassDescriptor::destroy()
    ritual = 'ritual_ZN26QGles2RenderPassDescriptor7destroyEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN26QGles2RenderPassDescriptor7destroyEv'
    self.uglySide.call(ritual)
