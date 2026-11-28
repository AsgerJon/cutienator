"""
QRhiTextureRenderTarget binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/rhi/qrhi.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteFlags, WAIT
from ..occult import Rituals
from . import QRhiRenderTarget, QRhiResource

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QRhiImplementation, QRhiRenderPassDescriptor
  from . import QRhiTextureRenderTargetDescription
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRhiImplementation = WAIT['QRhiImplementation']
  QRhiTextureRenderTargetDescription = WAIT['QRhiTextureRenderTargetDescription']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QRhiTextureRenderTarget(QRhiRenderTarget):
  """
  The cute side of Qt's QRhiTextureRenderTarget: a plain Python object
  standing in front of one C++ QRhiTextureRenderTarget.

  It is built on the cute 'QRhiRenderTarget', as Qt's QRhiTextureRenderTarget
  is built on Qt's QRhiRenderTarget, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QRhiTextureRenderTarget that has a ritual and that
  Python can call so far, 7 names in all: 'resourceType', 'description',
  'setDescription', 'flags', 'setFlags', 'newCompatibleRenderPassDescriptor',
  'create'. It can be made from Python, in 1 way; see '__init__'.

  What to expect
  --------------

  - The C++ QRhiTextureRenderTarget is created at the first use, not by
    'QRhiTextureRenderTarget(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QRhiTextureRenderTarget.
  """

  #  The enums Qt writes inside QRhiTextureRenderTarget, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class Flag(CuteFlags):
    """
    The flags enum 'QRhiTextureRenderTarget::Flag' of Qt, with the 3 names Qt
    gives in it. Qt names the type of its combinations
    'QRhiTextureRenderTarget::Flags'.
    """

    PreserveColorContents = 0x1
    PreserveDepthStencilContents = 0x2
    DoNotStoreDepthStencilContents = 0x4

  Flags = Flag

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QRhiTextureRenderTarget'

  #  A C++ QRhiTextureRenderTarget Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QRhiTextureRenderTarget'

  #  The functions Qt calls itself that QRhiTextureRenderTarget is the first
  #  to declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'newCompatibleRenderPassDescriptor': (
          ('_ZN23QRhiTextureRenderTarget33newCompatibleRenderPassDescriptor'
           'Ev',
           ('address', 'address', 'QtGui:QRhiRenderPassDescriptor'),
           ()),
      ),
      'create': (
          ('_ZN23QRhiTextureRenderTarget6createEv',
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
    Calls Qt's 'QRhiResource::Type QRhiTextureRenderTarget::resourceType()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhitexturerendertarget.html#resourceType

    Returns
    -------

    QRhiResource.Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QRhiResource.Type(number)' gives.
    """
    #  QRhiResource::Type QRhiTextureRenderTarget::resourceType() const
    ritual = 'ritual_ZNK23QRhiTextureRenderTarget12resourceTypeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK23QRhiTextureRenderTarget12resourceTypeEv'
    return QRhiResource.Type(self.uglySide.call(ritual))

  def description(self) -> QRhiTextureRenderTargetDescription:
    """
    Calls Qt's 'QRhiTextureRenderTargetDescription
    QRhiTextureRenderTarget::description() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhitexturerendertarget.html#description

    Returns
    -------

    QRhiTextureRenderTargetDescription
      A new cute QRhiTextureRenderTargetDescription around the copy Qt gave
      back. Python owns it.
    """
    #  QRhiTextureRenderTargetDescription
    #      QRhiTextureRenderTarget::description() const
    address = self.uglySide.call(
        'ritual_ZNK23QRhiTextureRenderTarget11descriptionEv',
    )
    from . import QRhiTextureRenderTargetDescription
    return QRhiTextureRenderTargetDescription._cuteOwning(address)

  def flags(self) -> Flags:
    """
    Calls Qt's 'Flags QRhiTextureRenderTarget::flags() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhitexturerendertarget.html#flags

    Returns
    -------

    Flags
      The value standing for the combination Qt gave back.
    """
    #  Flags QRhiTextureRenderTarget::flags() const
    return QRhiTextureRenderTarget.Flags(self.uglySide.call(
        'ritual_ZNK23QRhiTextureRenderTarget5flagsEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QRhiTextureRenderTargetDescription)
  def setDescription(self, desc: QRhiTextureRenderTargetDescription) -> None:
    """
    Calls Qt's 'void QRhiTextureRenderTarget::setDescription(const
    QRhiTextureRenderTargetDescription &desc)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhitexturerendertarget.html#setDescription

    Parameters
    ----------

    desc : QRhiTextureRenderTargetDescription
      Passed on as a value: Qt reads the C++
      QRhiTextureRenderTargetDescription, which stays Python's own.
    """
    #  void QRhiTextureRenderTarget::setDescription(const
    #      QRhiTextureRenderTargetDescription &desc)
    self.uglySide.call(
        'ritual_ZN23QRhiTextureRenderTarget14setDescriptionERK34QRhiTexture'
        'RenderTargetDescription',
        self._valueOf(desc),
    )

  @overload(Flags)
  def setFlags(self, f: Flags) -> None:
    """
    Calls Qt's 'void QRhiTextureRenderTarget::setFlags(Flags f)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhitexturerendertarget.html#setFlags

    Parameters
    ----------

    f : Flags
      Passed on as its number.
    """
    #  void QRhiTextureRenderTarget::setFlags(Flags f)
    self.uglySide.call(
        'ritual_ZN23QRhiTextureRenderTarget8setFlagsE6QFlagsINS_4FlagEE',
        f.value,
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

  @overload(QRhiImplementation, QRhiTextureRenderTargetDescription, Flags)
  @overload(NoneType, QRhiTextureRenderTargetDescription, Flags)
  def __init__(
      self,
      rhi: Optional[QRhiImplementation],
      desc_: QRhiTextureRenderTargetDescription,
      flags_: Flags,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QRhiTextureRenderTarget::QRhiTextureRenderTarget(QRhiImplementation
    *rhi, const QRhiTextureRenderTargetDescription &desc_, Flags flags_)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhitexturerendertarget.html

    Parameters
    ----------

    rhi : Optional[QRhiImplementation]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    desc_ : QRhiTextureRenderTargetDescription
      Passed on as a value: Qt reads the C++
      QRhiTextureRenderTargetDescription, which stays Python's own.

    flags_ : Flags
      Passed on as its number.
    """
    #  QRhiTextureRenderTarget::QRhiTextureRenderTarget(QRhiImplementation
    #      *rhi, const QRhiTextureRenderTargetDescription &desc_, Flags
    #      flags_)
    self._noteCreation(QRhiTextureRenderTarget, lambda: Rituals.call(
        'ritual_ZN23QRhiTextureRenderTargetC1EP18QRhiImplementationRK34QRhi'
        'TextureRenderTargetDescription6QFlagsINS_4FlagEE',
        self._addressOf(rhi), self._valueOf(desc_), flags_.value,
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

  def newCompatibleRenderPassDescriptor(
      self,
  ) -> Optional[QRhiRenderPassDescriptor]:
    """
    Calls Qt's 'QRhiRenderPassDescriptor
    *QRhiTextureRenderTarget::newCompatibleRenderPassDescriptor()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhitexturerendertarget.html

    Returns
    -------

    Optional[QRhiRenderPassDescriptor]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiRenderPassDescriptor
    #      *QRhiTextureRenderTarget::newCompatibleRenderPassDescriptor()
    address = self.uglySide.call(
        'ritual_ZN23QRhiTextureRenderTarget33newCompatibleRenderPassDescrip'
        'torEv',
    )
    from . import QRhiRenderPassDescriptor
    return QRhiRenderPassDescriptor._cuteAt(address)

  def create(self) -> bool:
    """
    Calls Qt's 'bool QRhiTextureRenderTarget::create()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhitexturerendertarget.html#create
    """
    #  bool QRhiTextureRenderTarget::create()
    return self.uglySide.call('ritual_ZN23QRhiTextureRenderTarget6createEv')
