"""
QRhiResource binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/rhi/qrhi.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray
  from . import QRhi, QRhiImplementation
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QRhiImplementation = WAIT['QRhiImplementation']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QRhiResource(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QRhiResource: a plain Python object standing in front
  of one C++ QRhiResource.

  What exists
  -----------

  Every function of Qt's QRhiResource that has a ritual and that Python can
  call so far, 7 names in all: 'resourceType', 'destroy', 'deleteLater',
  'name', 'setName', 'globalResourceId', 'rhi'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QRhiResource::~QRhiResource()': the destructor: Python never
    removes a C++ QRhiResource.

  What has no ritual
  ------------------

  2 of the 11 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QRhiResource is created at the first use, not by
    'QRhiResource(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QRhiResource.
  """

  #  The enums Qt writes inside QRhiResource, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class Type(CuteNum):
    """
    The enum 'QRhiResource::Type' of Qt, with the 13 names Qt gives in it.
    """

    Buffer = Kee[int](0)
    Texture = Kee[int](1)
    Sampler = Kee[int](2)
    RenderBuffer = Kee[int](3)
    RenderPassDescriptor = Kee[int](4)
    SwapChainRenderTarget = Kee[int](5)
    TextureRenderTarget = Kee[int](6)
    ShaderResourceBindings = Kee[int](7)
    GraphicsPipeline = Kee[int](8)
    SwapChain = Kee[int](9)
    ComputePipeline = Kee[int](10)
    CommandBuffer = Kee[int](11)
    ShadingRateMap = Kee[int](12)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QRhiResource'

  #  A C++ QRhiResource Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QRhiResource'

  #  The functions Qt calls itself that QRhiResource is the first to declare.
  #  A class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'resourceType': (
          ('_ZNK12QRhiResource12resourceTypeEv',
           ('int', 'enum', 'QtGui:QRhiResource.Type'),
           ()),
      ),
      'destroy': (
          ('_ZN12QRhiResource7destroyEv',
           ('nothing', 'nothing', ''),
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

  def resourceType(self) -> Type:
    """
    Calls Qt's 'Type QRhiResource::resourceType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhiresource.html#resourceType

    Returns
    -------

    Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Type(number)' gives.
    """
    #  Type QRhiResource::resourceType() const
    return QRhiResource.Type(self.uglySide.call(
        'ritual_ZNK12QRhiResource12resourceTypeEv',
    ))

  def name(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QRhiResource::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhiresource.html#name

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QRhiResource::name() const
    address = self.uglySide.call('ritual_ZNK12QRhiResource4nameEv')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def globalResourceId(self) -> int:
    """
    Calls Qt's 'quint64 QRhiResource::globalResourceId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhiresource.html#globalResourceId
    """
    #  quint64 QRhiResource::globalResourceId() const
    return self.uglySide.call('ritual_ZNK12QRhiResource16globalResourceIdEv')

  def rhi(self) -> Optional[QRhi]:
    """
    Calls Qt's 'QRhi *QRhiResource::rhi() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhiresource.html#rhi

    Returns
    -------

    Optional[QRhi]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhi *QRhiResource::rhi() const
    address = self.uglySide.call('ritual_ZNK12QRhiResource3rhiEv')
    from . import QRhi
    return QRhi._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QByteArray)
  def setName(self, name: QByteArray) -> None:
    """
    Calls Qt's 'void QRhiResource::setName(const QByteArray &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhiresource.html#setName

    Parameters
    ----------

    name : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QRhiResource::setName(const QByteArray &name)
    self.uglySide.call(
        'ritual_ZN12QRhiResource7setNameERK10QByteArray',
        self._valueOf(name),
    )

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
    'QRhiResource::QRhiResource(QRhiImplementation *rhi)', which is called at
    the first use.

    Qt's own words: https://doc.qt.io/qt-6/qrhiresource.html#QRhiResource

    Parameters
    ----------

    rhi : Optional[QRhiImplementation]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QRhiResource::QRhiResource(QRhiImplementation *rhi)
    self._noteCreation(QRhiResource, lambda: Rituals.call(
        'ritual_ZN12QRhiResourceC1EP18QRhiImplementation',
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
    Calls Qt's 'void QRhiResource::destroy()'.

    Qt's own words: https://doc.qt.io/qt-6/qrhiresource.html#destroy
    """
    #  void QRhiResource::destroy()
    self.uglySide.call('ritual_ZN12QRhiResource7destroyEv')

  def deleteLater(self) -> None:
    """
    Calls Qt's 'void QRhiResource::deleteLater()'.

    Qt's own words: https://doc.qt.io/qt-6/qrhiresource.html#deleteLater
    """
    #  void QRhiResource::deleteLater()
    self.uglySide.call('ritual_ZN12QRhiResource11deleteLaterEv')
