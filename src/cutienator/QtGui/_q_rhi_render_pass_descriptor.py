"""
QRhiRenderPassDescriptor binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/rhi/qrhi.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from . import QRhiResource

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QRhiNativeHandles

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QRhiRenderPassDescriptor(QRhiResource):
  """
  The cute side of Qt's QRhiRenderPassDescriptor: a plain Python object
  standing in front of one C++ QRhiRenderPassDescriptor.

  It is built on the cute 'QRhiResource', as Qt's QRhiRenderPassDescriptor is
  built on Qt's QRhiResource, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QRhiRenderPassDescriptor that has a ritual and that
  Python can call so far, 4 names in all: 'resourceType', 'isCompatible',
  'nativeHandles', 'newCompatibleRenderPassDescriptor'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QVector<quint32> QRhiRenderPassDescriptor::serializedFormat()
    const': gives a type Python has no way to take yet.

  What has no ritual
  ------------------

  1 of the 6 functions Qt declares: 1 the class is abstract, so C++ cannot
  make one, and the C++ class of ours does not fill in every function it
  leaves open.

  What to expect
  --------------

  - The C++ QRhiRenderPassDescriptor is created at the first use, not by
    'QRhiRenderPassDescriptor(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QRhiRenderPassDescriptor.
  - Each name of Qt's QRhiRenderPassDescriptor that has no cute function yet,
    '__init__', 'serializedFormat', holds a function that raises
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
  __qt_class__ = 'QRhiRenderPassDescriptor'

  #  A C++ QRhiRenderPassDescriptor Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QRhiRenderPassDescriptor'

  #  The functions Qt calls itself that QRhiRenderPassDescriptor is the first
  #  to declare and that cannot be handed to Python yet, each as Qt declares
  #  it. A class of a program that writes one of them anew is refused, since
  #  Qt would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'serializedFormat': (
          'QVector<quint32> QRhiRenderPassDescriptor::serializedFormat() '
          'const',
      ),
  }

  #  The functions Qt calls itself that QRhiRenderPassDescriptor is the first
  #  to declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'isCompatible': (
          ('_ZNK24QRhiRenderPassDescriptor12isCompatibleEPKS_',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtGui:QRhiRenderPassDescriptor'),
           )),
      ),
      'nativeHandles': (
          ('_ZN24QRhiRenderPassDescriptor13nativeHandlesEv',
           ('address', 'address', 'QtGui:QRhiNativeHandles'),
           ()),
      ),
      'newCompatibleRenderPassDescriptor': (
          ('_ZNK24QRhiRenderPassDescriptor33newCompatibleRenderPassDescript'
           'orEv',
           ('address', 'address', 'QtGui:QRhiRenderPassDescriptor'),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def resourceType(self) -> QRhiResource.Type:
    """
    Calls Qt's 'QRhiResource::Type QRhiRenderPassDescriptor::resourceType()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhirenderpassdescriptor.html#resourceType

    Returns
    -------

    QRhiResource.Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QRhiResource.Type(number)' gives.
    """
    #  QRhiResource::Type QRhiRenderPassDescriptor::resourceType() const
    ritual = 'ritual_ZNK24QRhiRenderPassDescriptor12resourceTypeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK24QRhiRenderPassDescriptor12resourceTypeEv'
    return QRhiResource.Type(self.uglySide.call(ritual))

  @overload(THIS)
  @overload(NoneType)
  def isCompatible(self, other: Optional[QRhiRenderPassDescriptor]) -> bool:
    """
    Calls Qt's 'bool QRhiRenderPassDescriptor::isCompatible(const
    QRhiRenderPassDescriptor *other) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhirenderpassdescriptor.html#isCompatible

    Parameters
    ----------

    other : Optional[QRhiRenderPassDescriptor]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QRhiRenderPassDescriptor::isCompatible(const
    #      QRhiRenderPassDescriptor *other) const
    return self.uglySide.call(
        'ritual_ZNK24QRhiRenderPassDescriptor12isCompatibleEPKS_',
        self._addressOf(other),
    )

  def newCompatibleRenderPassDescriptor(
      self,
  ) -> Optional[QRhiRenderPassDescriptor]:
    """
    Calls Qt's 'QRhiRenderPassDescriptor
    *QRhiRenderPassDescriptor::newCompatibleRenderPassDescriptor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhirenderpassdescriptor.html

    Returns
    -------

    Optional[QRhiRenderPassDescriptor]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiRenderPassDescriptor
    #      *QRhiRenderPassDescriptor::newCompatibleRenderPassDescriptor()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK24QRhiRenderPassDescriptor33newCompatibleRenderPassDescr'
        'iptorEv',
    )
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's
    'QRhiRenderPassDescriptor::QRhiRenderPassDescriptor(QRhiImplementation
    *rhi)': the class is abstract, so C++ cannot make one, and the C++ class
    of ours does not fill in every function it leaves open.
    """
    raise NotImplementedError(
        "'QRhiRenderPassDescriptor.__init__' has no cute function yet. Qt's "
        "'QRhiRenderPassDescriptor::QRhiRenderPassDescriptor(QRhiImplementat"
        "ion *rhi)': the class is abstract, so C++ cannot make one, and the "
        "C++ class of ours does not fill in every function it leaves open.")

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

  def nativeHandles(self) -> Optional[QRhiNativeHandles]:
    """
    Calls Qt's 'const QRhiNativeHandles
    *QRhiRenderPassDescriptor::nativeHandles()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhirenderpassdescriptor.html#nativeHandles

    Returns
    -------

    Optional[QRhiNativeHandles]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QRhiNativeHandles *QRhiRenderPassDescriptor::nativeHandles()
    ritual = 'ritual_ZN24QRhiRenderPassDescriptor13nativeHandlesEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN24QRhiRenderPassDescriptor13nativeHandlesEv'
    address = self.uglySide.call(ritual)
    from . import QRhiNativeHandles
    return QRhiNativeHandles._cuteAt(address)

  @staticmethod
  def serializedFormat(*__, **_) -> Never:
    """
    Qt's 'QVector<quint32> QRhiRenderPassDescriptor::serializedFormat()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QRhiRenderPassDescriptor.serializedFormat' has no cute function "
        "yet. Qt's 'QVector<quint32> "
        "QRhiRenderPassDescriptor::serializedFormat() const': gives a type "
        "Python has no way to take yet.")
