"""
QVkRenderPassDescriptor binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qrhivulkan_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QVkRenderPassDescriptor to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from . import QRhiRenderPassDescriptor

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QRhiNativeHandles

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QVkRenderPassDescriptor(QRhiRenderPassDescriptor):
  """
  The cute side of Qt's QVkRenderPassDescriptor: a plain Python object
  standing in front of one C++ QVkRenderPassDescriptor.

  It is built on the cute 'QRhiRenderPassDescriptor', as Qt's
  QVkRenderPassDescriptor is built on Qt's QRhiRenderPassDescriptor, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QVkRenderPassDescriptor that has a ritual and that
  Python can call so far, 5 names in all: 'destroy', 'isCompatible',
  'newCompatibleRenderPassDescriptor', 'nativeHandles',
  'updateSerializedFormat'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QVkRenderPassDescriptor::~QVkRenderPassDescriptor()': the
    destructor: Python never removes a C++ QVkRenderPassDescriptor.
  - Qt's 'QVector<quint32> QVkRenderPassDescriptor::serializedFormat()
    const': gives a type Python has no way to take yet.

  What has no ritual
  ------------------

  1 of the 8 functions Qt declares: 1 leans on 'QVkRenderPassDescriptor.

  What to expect
  --------------

  - The C++ QVkRenderPassDescriptor is created at the first use, not by
    'QVkRenderPassDescriptor(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QVkRenderPassDescriptor.
  - Each name of Qt's QVkRenderPassDescriptor that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QVkRenderPassDescriptor'

  #  A C++ QVkRenderPassDescriptor Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QVkRenderPassDescriptor'

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
    Calls Qt's 'bool QVkRenderPassDescriptor::isCompatible(const
    QRhiRenderPassDescriptor *other) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvkrenderpassdescriptor.html#isCompatible

    Parameters
    ----------

    other : Optional[QRhiRenderPassDescriptor]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QVkRenderPassDescriptor::isCompatible(const
    #      QRhiRenderPassDescriptor *other) const
    return self.uglySide.call(
        'ritual_ZNK23QVkRenderPassDescriptor12isCompatibleEPK24QRhiRenderPa'
        'ssDescriptor',
        self._addressOf(other),
    )

  def newCompatibleRenderPassDescriptor(
      self,
  ) -> Optional[QRhiRenderPassDescriptor]:
    """
    Calls Qt's 'QRhiRenderPassDescriptor
    *QVkRenderPassDescriptor::newCompatibleRenderPassDescriptor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvkrenderpassdescriptor.html

    Returns
    -------

    Optional[QRhiRenderPassDescriptor]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiRenderPassDescriptor
    #      *QVkRenderPassDescriptor::newCompatibleRenderPassDescriptor()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK23QVkRenderPassDescriptor33newCompatibleRenderPassDescri'
        'ptorEv',
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
    Qt's 'QVkRenderPassDescriptor::QVkRenderPassDescriptor(QRhiImplementation
    *rhi)': leans on
    'QVkRenderPassDescriptor::isCompatible(QRhiRenderPassDescriptor const*)
    const', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QVkRenderPassDescriptor.__init__' has no cute function yet. Qt's "
        "'QVkRenderPassDescriptor::QVkRenderPassDescriptor(QRhiImplementatio"
        "n *rhi)': leans on "
        "'QVkRenderPassDescriptor::isCompatible(QRhiRenderPassDescriptor "
        "const*) const', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

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
    Calls Qt's 'void QVkRenderPassDescriptor::destroy()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvkrenderpassdescriptor.html#destroy
    """
    #  void QVkRenderPassDescriptor::destroy()
    ritual = 'ritual_ZN23QVkRenderPassDescriptor7destroyEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN23QVkRenderPassDescriptor7destroyEv'
    self.uglySide.call(ritual)

  def nativeHandles(self) -> Optional[QRhiNativeHandles]:
    """
    Calls Qt's 'const QRhiNativeHandles
    *QVkRenderPassDescriptor::nativeHandles()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvkrenderpassdescriptor.html#nativeHandles

    Returns
    -------

    Optional[QRhiNativeHandles]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QRhiNativeHandles *QVkRenderPassDescriptor::nativeHandles()
    ritual = 'ritual_ZN23QVkRenderPassDescriptor13nativeHandlesEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN23QVkRenderPassDescriptor13nativeHandlesEv'
    address = self.uglySide.call(ritual)
    from . import QRhiNativeHandles
    return QRhiNativeHandles._cuteAt(address)

  def updateSerializedFormat(self) -> None:
    """
    Calls Qt's 'void QVkRenderPassDescriptor::updateSerializedFormat()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvkrenderpassdescriptor.html
    """
    #  void QVkRenderPassDescriptor::updateSerializedFormat()
    self.uglySide.call(
        'ritual_ZN23QVkRenderPassDescriptor22updateSerializedFormatEv',
    )
