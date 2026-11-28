"""
QRhiSampler binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/rhi/qrhi.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum, WAIT
from ..occult import Rituals
from . import QRhiResource

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


class QRhiSampler(QRhiResource):
  """
  The cute side of Qt's QRhiSampler: a plain Python object standing in front
  of one C++ QRhiSampler.

  It is built on the cute 'QRhiResource', as Qt's QRhiSampler is built on
  Qt's QRhiResource, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QRhiSampler that has a ritual and that Python can
  call so far, 16 names in all: 'resourceType', 'magFilter', 'setMagFilter',
  'minFilter', 'setMinFilter', 'mipmapMode', 'setMipmapMode', 'addressU',
  'setAddressU', 'addressV', 'setAddressV', 'addressW', 'setAddressW',
  'textureCompareOp', 'setTextureCompareOp', 'create'. It can be made from
  Python, in 1 way; see '__init__'.

  What to expect
  --------------

  - The C++ QRhiSampler is created at the first use, not by
    'QRhiSampler(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QRhiSampler.
  """

  #  The enums Qt writes inside QRhiSampler, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class AddressMode(CuteNum):
    """
    The enum 'QRhiSampler::AddressMode' of Qt, with the 3 names Qt gives in
    it.
    """

    Repeat = Kee[int](0)
    ClampToEdge = Kee[int](1)
    Mirror = Kee[int](2)

  class CompareOp(CuteNum):
    """
    The enum 'QRhiSampler::CompareOp' of Qt, with the 8 names Qt gives in it.
    """

    Never = Kee[int](0)
    Less = Kee[int](1)
    Equal = Kee[int](2)
    LessOrEqual = Kee[int](3)
    Greater = Kee[int](4)
    NotEqual = Kee[int](5)
    GreaterOrEqual = Kee[int](6)
    Always = Kee[int](7)

  class Filter(CuteNum):
    """
    The enum 'QRhiSampler::Filter' of Qt, with the 3 names Qt gives in it.
    """

    NULL = Kee[int](0)
    Nearest = Kee[int](1)
    Linear = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QRhiSampler'

  #  A C++ QRhiSampler Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QRhiSampler'

  #  The functions Qt calls itself that QRhiSampler is the first to declare.
  #  A class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'create': (
          ('_ZN11QRhiSampler6createEv',
           ('bool', 'number', ''),
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
    Calls Qt's 'QRhiResource::Type QRhiSampler::resourceType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhisampler.html#resourceType

    Returns
    -------

    QRhiResource.Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QRhiResource.Type(number)' gives.
    """
    #  QRhiResource::Type QRhiSampler::resourceType() const
    ritual = 'ritual_ZNK11QRhiSampler12resourceTypeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QRhiSampler12resourceTypeEv'
    return QRhiResource.Type(self.uglySide.call(ritual))

  def magFilter(self) -> Filter:
    """
    Calls Qt's 'Filter QRhiSampler::magFilter() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhisampler.html#magFilter

    Returns
    -------

    Filter
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Filter(number)' gives.
    """
    #  Filter QRhiSampler::magFilter() const
    return QRhiSampler.Filter(self.uglySide.call(
        'ritual_ZNK11QRhiSampler9magFilterEv',
    ))

  def minFilter(self) -> Filter:
    """
    Calls Qt's 'Filter QRhiSampler::minFilter() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhisampler.html#minFilter

    Returns
    -------

    Filter
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Filter(number)' gives.
    """
    #  Filter QRhiSampler::minFilter() const
    return QRhiSampler.Filter(self.uglySide.call(
        'ritual_ZNK11QRhiSampler9minFilterEv',
    ))

  def mipmapMode(self) -> Filter:
    """
    Calls Qt's 'Filter QRhiSampler::mipmapMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhisampler.html#mipmapMode

    Returns
    -------

    Filter
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Filter(number)' gives.
    """
    #  Filter QRhiSampler::mipmapMode() const
    return QRhiSampler.Filter(self.uglySide.call(
        'ritual_ZNK11QRhiSampler10mipmapModeEv',
    ))

  def addressU(self) -> AddressMode:
    """
    Calls Qt's 'AddressMode QRhiSampler::addressU() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhisampler.html#addressU

    Returns
    -------

    AddressMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'AddressMode(number)'
      gives.
    """
    #  AddressMode QRhiSampler::addressU() const
    return QRhiSampler.AddressMode(self.uglySide.call(
        'ritual_ZNK11QRhiSampler8addressUEv',
    ))

  def addressV(self) -> AddressMode:
    """
    Calls Qt's 'AddressMode QRhiSampler::addressV() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhisampler.html#addressV

    Returns
    -------

    AddressMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'AddressMode(number)'
      gives.
    """
    #  AddressMode QRhiSampler::addressV() const
    return QRhiSampler.AddressMode(self.uglySide.call(
        'ritual_ZNK11QRhiSampler8addressVEv',
    ))

  def addressW(self) -> AddressMode:
    """
    Calls Qt's 'AddressMode QRhiSampler::addressW() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhisampler.html#addressW

    Returns
    -------

    AddressMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'AddressMode(number)'
      gives.
    """
    #  AddressMode QRhiSampler::addressW() const
    return QRhiSampler.AddressMode(self.uglySide.call(
        'ritual_ZNK11QRhiSampler8addressWEv',
    ))

  def textureCompareOp(self) -> CompareOp:
    """
    Calls Qt's 'CompareOp QRhiSampler::textureCompareOp() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhisampler.html#textureCompareOp

    Returns
    -------

    CompareOp
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'CompareOp(number)' gives.
    """
    #  CompareOp QRhiSampler::textureCompareOp() const
    return QRhiSampler.CompareOp(self.uglySide.call(
        'ritual_ZNK11QRhiSampler16textureCompareOpEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Filter)
  def setMagFilter(self, f: Filter) -> None:
    """
    Calls Qt's 'void QRhiSampler::setMagFilter(Filter f)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhisampler.html#setMagFilter

    Parameters
    ----------

    f : Filter
      Passed on as its number.
    """
    #  void QRhiSampler::setMagFilter(Filter f)
    self.uglySide.call(
        'ritual_ZN11QRhiSampler12setMagFilterENS_6FilterE', f.value,
    )

  @overload(Filter)
  def setMinFilter(self, f: Filter) -> None:
    """
    Calls Qt's 'void QRhiSampler::setMinFilter(Filter f)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhisampler.html#setMinFilter

    Parameters
    ----------

    f : Filter
      Passed on as its number.
    """
    #  void QRhiSampler::setMinFilter(Filter f)
    self.uglySide.call(
        'ritual_ZN11QRhiSampler12setMinFilterENS_6FilterE', f.value,
    )

  @overload(Filter)
  def setMipmapMode(self, f: Filter) -> None:
    """
    Calls Qt's 'void QRhiSampler::setMipmapMode(Filter f)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhisampler.html#setMipmapMode

    Parameters
    ----------

    f : Filter
      Passed on as its number.
    """
    #  void QRhiSampler::setMipmapMode(Filter f)
    self.uglySide.call(
        'ritual_ZN11QRhiSampler13setMipmapModeENS_6FilterE', f.value,
    )

  @overload(AddressMode)
  def setAddressU(self, mode: AddressMode) -> None:
    """
    Calls Qt's 'void QRhiSampler::setAddressU(AddressMode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhisampler.html#setAddressU

    Parameters
    ----------

    mode : AddressMode
      Passed on as its number.
    """
    #  void QRhiSampler::setAddressU(AddressMode mode)
    self.uglySide.call(
        'ritual_ZN11QRhiSampler11setAddressUENS_11AddressModeE', mode.value,
    )

  @overload(AddressMode)
  def setAddressV(self, mode: AddressMode) -> None:
    """
    Calls Qt's 'void QRhiSampler::setAddressV(AddressMode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhisampler.html#setAddressV

    Parameters
    ----------

    mode : AddressMode
      Passed on as its number.
    """
    #  void QRhiSampler::setAddressV(AddressMode mode)
    self.uglySide.call(
        'ritual_ZN11QRhiSampler11setAddressVENS_11AddressModeE', mode.value,
    )

  @overload(AddressMode)
  def setAddressW(self, mode: AddressMode) -> None:
    """
    Calls Qt's 'void QRhiSampler::setAddressW(AddressMode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhisampler.html#setAddressW

    Parameters
    ----------

    mode : AddressMode
      Passed on as its number.
    """
    #  void QRhiSampler::setAddressW(AddressMode mode)
    self.uglySide.call(
        'ritual_ZN11QRhiSampler11setAddressWENS_11AddressModeE', mode.value,
    )

  @overload(CompareOp)
  def setTextureCompareOp(self, op: CompareOp) -> None:
    """
    Calls Qt's 'void QRhiSampler::setTextureCompareOp(CompareOp op)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhisampler.html#setTextureCompareOp

    Parameters
    ----------

    op : CompareOp
      Passed on as its number.
    """
    #  void QRhiSampler::setTextureCompareOp(CompareOp op)
    self.uglySide.call(
        'ritual_ZN11QRhiSampler19setTextureCompareOpENS_9CompareOpE',
        op.value,
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

  @overload(
      QRhiImplementation, Filter, Filter, Filter, AddressMode, AddressMode,
      AddressMode,
  )
  @overload(
      NoneType, Filter, Filter, Filter, AddressMode, AddressMode,
      AddressMode,
  )
  def __init__(
      self,
      rhi: Optional[QRhiImplementation],
      magFilter_: Filter,
      minFilter_: Filter,
      mipmapMode_: Filter,
      u_: AddressMode,
      v_: AddressMode,
      w_: AddressMode,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QRhiSampler::QRhiSampler(QRhiImplementation *rhi, Filter magFilter_,
    Filter minFilter_, Filter mipmapMode_, AddressMode u_, AddressMode v_,
    AddressMode w_)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qrhisampler.html#QRhiSampler

    Parameters
    ----------

    rhi : Optional[QRhiImplementation]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    magFilter_ : Filter
      Passed on as its number.

    minFilter_ : Filter
      Passed on as its number.

    mipmapMode_ : Filter
      Passed on as its number.

    u_ : AddressMode
      Passed on as its number.

    v_ : AddressMode
      Passed on as its number.

    w_ : AddressMode
      Passed on as its number.
    """
    #  QRhiSampler::QRhiSampler(QRhiImplementation *rhi, Filter magFilter_,
    #      Filter minFilter_, Filter mipmapMode_, AddressMode u_, AddressMode
    #      v_, AddressMode w_)
    self._noteCreation(QRhiSampler, lambda: Rituals.call(
        'ritual_ZN11QRhiSamplerC1EP18QRhiImplementationNS_6FilterES2_S2_NS_'
        '11AddressModeES3_S3_',
        self._addressOf(rhi), magFilter_.value, minFilter_.value,
        mipmapMode_.value, u_.value, v_.value, w_.value,
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

  def create(self) -> bool:
    """
    Calls Qt's 'bool QRhiSampler::create()'.

    Qt's own words: https://doc.qt.io/qt-6/qrhisampler.html#create
    """
    #  bool QRhiSampler::create()
    return self.uglySide.call('ritual_ZN11QRhiSampler6createEv')
