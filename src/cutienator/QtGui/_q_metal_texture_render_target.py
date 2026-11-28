"""
QMetalTextureRenderTarget binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qrhimetal_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QMetalTextureRenderTarget to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from . import QRhiTextureRenderTarget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QSize
  from . import QRhiRenderPassDescriptor


class QMetalTextureRenderTarget(QRhiTextureRenderTarget):
  """
  The cute side of Qt's QMetalTextureRenderTarget: a plain Python object
  standing in front of one C++ QMetalTextureRenderTarget.

  It is built on the cute 'QRhiTextureRenderTarget', as Qt's
  QMetalTextureRenderTarget is built on Qt's QRhiTextureRenderTarget, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QMetalTextureRenderTarget that has a ritual and that
  Python can call so far, 6 names in all: 'destroy', 'pixelSize',
  'devicePixelRatio', 'sampleCount', 'newCompatibleRenderPassDescriptor',
  'create'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has no ritual
  ------------------

  2 of the 8 functions Qt declares: 2 cannot be called and cannot be called
  through the meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ QMetalTextureRenderTarget is created at the first use, not by
    'QMetalTextureRenderTarget(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QMetalTextureRenderTarget.
  - Each name of Qt's QMetalTextureRenderTarget that has no cute function
    yet, '__init__', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QMetalTextureRenderTarget'

  #  A C++ QMetalTextureRenderTarget Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QMetalTextureRenderTarget'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def pixelSize(self) -> QSize:
    """
    Calls Qt's 'QSize QMetalTextureRenderTarget::pixelSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaltexturerendertarget.html#pixelSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QMetalTextureRenderTarget::pixelSize() const
    address = self.uglySide.call(
        'ritual_ZNK25QMetalTextureRenderTarget9pixelSizeEv',
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def devicePixelRatio(self) -> float:
    """
    Calls Qt's 'float QMetalTextureRenderTarget::devicePixelRatio() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaltexturerendertarget.html#devicePixelRatio
    """
    #  float QMetalTextureRenderTarget::devicePixelRatio() const
    return self.uglySide.call(
        'ritual_ZNK25QMetalTextureRenderTarget16devicePixelRatioEv',
    )

  def sampleCount(self) -> int:
    """
    Calls Qt's 'int QMetalTextureRenderTarget::sampleCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaltexturerendertarget.html#sampleCount
    """
    #  int QMetalTextureRenderTarget::sampleCount() const
    return self.uglySide.call(
        'ritual_ZNK25QMetalTextureRenderTarget11sampleCountEv',
    )

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
    'QMetalTextureRenderTarget::QMetalTextureRenderTarget(QRhiImplementation
    *rhi, const QRhiTextureRenderTargetDescription &desc, Flags flags)':
    cannot be called and cannot be called through the meta-object and cannot
    be copied: no header file has its code, Qt's source does not mark it or
    its class for use from outside Qt or writes it 'inline' or nowhere, and
    it is no signal, slot or invokable function giving back nothing, of a
    class built on QObject, and Qt's source has no code for it that could be
    told from the rest.
    """
    raise NotImplementedError(
        "'QMetalTextureRenderTarget.__init__' has no cute function yet. "
        "Qt's "
        "'QMetalTextureRenderTarget::QMetalTextureRenderTarget(QRhiImplement"
        "ation *rhi, const QRhiTextureRenderTargetDescription &desc, Flags "
        "flags)': cannot be called and cannot be called through the "
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
    Calls Qt's 'void QMetalTextureRenderTarget::destroy()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaltexturerendertarget.html#destroy
    """
    #  void QMetalTextureRenderTarget::destroy()
    self.uglySide.call('ritual_ZN25QMetalTextureRenderTarget7destroyEv')

  def newCompatibleRenderPassDescriptor(
      self,
  ) -> Optional[QRhiRenderPassDescriptor]:
    """
    Calls Qt's 'QRhiRenderPassDescriptor
    *QMetalTextureRenderTarget::newCompatibleRenderPassDescriptor()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaltexturerendertarget.html

    Returns
    -------

    Optional[QRhiRenderPassDescriptor]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiRenderPassDescriptor
    #      *QMetalTextureRenderTarget::newCompatibleRenderPassDescriptor()
    address = self.uglySide.call(
        'ritual_ZN25QMetalTextureRenderTarget33newCompatibleRenderPassDescr'
        'iptorEv',
    )
    from . import QRhiRenderPassDescriptor
    return QRhiRenderPassDescriptor._cuteAt(address)

  def create(self) -> bool:
    """
    Calls Qt's 'bool QMetalTextureRenderTarget::create()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaltexturerendertarget.html#create
    """
    #  bool QMetalTextureRenderTarget::create()
    return self.uglySide.call(
        'ritual_ZN25QMetalTextureRenderTarget6createEv',
    )
