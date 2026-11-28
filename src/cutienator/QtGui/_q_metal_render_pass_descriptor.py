"""
QMetalRenderPassDescriptor binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qrhimetal_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QMetalRenderPassDescriptor to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from . import QRhiRenderPassDescriptor

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QMetalRenderPassDescriptor(QRhiRenderPassDescriptor):
  """
  The cute side of Qt's QMetalRenderPassDescriptor: a plain Python object
  standing in front of one C++ QMetalRenderPassDescriptor.

  It is built on the cute 'QRhiRenderPassDescriptor', as Qt's
  QMetalRenderPassDescriptor is built on Qt's QRhiRenderPassDescriptor, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QMetalRenderPassDescriptor that has a ritual and
  that Python can call so far, 3 names in all: 'destroy', 'isCompatible',
  'newCompatibleRenderPassDescriptor'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QVector<quint32> QMetalRenderPassDescriptor::serializedFormat()
    const': gives a type Python has no way to take yet.

  What has no ritual
  ------------------

  3 of the 7 functions Qt declares: 3 cannot be called and cannot be called
  through the meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ QMetalRenderPassDescriptor is created at the first use, not by
    'QMetalRenderPassDescriptor(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QMetalRenderPassDescriptor.
  - Each name of Qt's QMetalRenderPassDescriptor that has no cute function
    yet, '__init__', 'updateSerializedFormat', holds a function that raises
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
  __qt_class__ = 'QMetalRenderPassDescriptor'

  #  A C++ QMetalRenderPassDescriptor Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QMetalRenderPassDescriptor'

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
    Calls Qt's 'bool QMetalRenderPassDescriptor::isCompatible(const
    QRhiRenderPassDescriptor *other) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetalrenderpassdescriptor.html#isCompatible

    Parameters
    ----------

    other : Optional[QRhiRenderPassDescriptor]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QMetalRenderPassDescriptor::isCompatible(const
    #      QRhiRenderPassDescriptor *other) const
    return self.uglySide.call(
        'ritual_ZNK26QMetalRenderPassDescriptor12isCompatibleEPK24QRhiRende'
        'rPassDescriptor',
        self._addressOf(other),
    )

  def newCompatibleRenderPassDescriptor(
      self,
  ) -> Optional[QRhiRenderPassDescriptor]:
    """
    Calls Qt's 'QRhiRenderPassDescriptor
    *QMetalRenderPassDescriptor::newCompatibleRenderPassDescriptor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetalrenderpassdescriptor.html

    Returns
    -------

    Optional[QRhiRenderPassDescriptor]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiRenderPassDescriptor
    #      *QMetalRenderPassDescriptor::newCompatibleRenderPassDescriptor()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK26QMetalRenderPassDescriptor33newCompatibleRenderPassDes'
        'criptorEv',
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
    Qt's 'QMetalRenderPassDescriptor::QMetalRenderPassDescriptor(
    QRhiImplementation *rhi)': cannot be called and cannot be called through
    the meta-object and cannot be copied: no header file has its code, Qt's
    source does not mark it or its class for use from outside Qt or writes it
    'inline' or nowhere, and it is no signal, slot or invokable function
    giving back nothing, of a class built on QObject, and Qt's source has no
    code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QMetalRenderPassDescriptor.__init__' has no cute function yet. "
        "Qt's "
        "'QMetalRenderPassDescriptor::QMetalRenderPassDescriptor(QRhiImpleme"
        "ntation *rhi)': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

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
    Calls Qt's 'void QMetalRenderPassDescriptor::destroy()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetalrenderpassdescriptor.html#destroy
    """
    #  void QMetalRenderPassDescriptor::destroy()
    self.uglySide.call('ritual_ZN26QMetalRenderPassDescriptor7destroyEv')

  @staticmethod
  def updateSerializedFormat(*__, **_) -> Never:
    """
    Qt's 'void QMetalRenderPassDescriptor::updateSerializedFormat()': cannot
    be called and cannot be called through the meta-object and cannot be
    copied: no header file has its code, Qt's source does not mark it or its
    class for use from outside Qt or writes it 'inline' or nowhere, and it is
    no signal, slot or invokable function giving back nothing, of a class
    built on QObject, and Qt's source has no code for it that could be told
    from the rest.
    """
    raise NotImplementedError(
        "'QMetalRenderPassDescriptor.updateSerializedFormat' has no cute "
        "function yet. Qt's 'void "
        "QMetalRenderPassDescriptor::updateSerializedFormat()': cannot be "
        "called and cannot be called through the meta-object and cannot be "
        "copied: no header file has its code, Qt's source does not mark it "
        "or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")
