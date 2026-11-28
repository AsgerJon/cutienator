"""
Qt3DRender::Render::Texture binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/texture_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means Qt3DRender::Render::Texture to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags, MetaCute, WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Texture(Qt3DRender.Render.BackendNode):
  """
  The cute side of Qt's Qt3DRender::Render::Texture: a plain Python object
  standing in front of one C++ Qt3DRender::Render::Texture.

  It is built on the cute 'Qt3DRender::Render::BackendNode', as Qt's
  Qt3DRender::Render::Texture is built on Qt's
  Qt3DRender::Render::BackendNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::Render::Texture that has a ritual and
  that Python can call so far, 10 names in all: 'addDirtyFlag', 'dirtyFlags',
  'unsetDirty', 'cleanup', 'addTextureDataUpdate', 'syncFromFrontEnd',
  'properties', 'parameters', 'sharedTextureId', 'isValid'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DRender::Render::Texture::~Texture()': the destructor: Python
    never removes a C++ Qt3DRender::Render::Texture.
  - Qt's 'std::vector<QTextureDataUpdate>
    Qt3DRender::Render::Texture::takePendingTextureDataUpdates()': gives a
    type Python has no way to take yet.
  - Qt's 'const Qt3DCore::QNodeIdVector
    Qt3DRender::Render::Texture::textureImageIds() const': gives a type
    Python has no way to take yet.
  - Qt's 'const QTextureGeneratorPtr
    &Qt3DRender::Render::Texture::dataGenerator() const': gives a type Python
    has no way to take yet.
  - Qt's 'void Qt3DRender::Render::Texture::setDataGenerator(const
    QTextureGeneratorPtr &generator)': takes a type Python has no way to hand
    over yet.

  What to expect
  --------------

  - The C++ Qt3DRender::Render::Texture is created at the first use, not by
    'Qt3DRender::Render::Texture(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::Render::Texture.
  - Each name of Qt's Qt3DRender::Render::Texture that has no cute function
    yet, 'dataGenerator', 'setDataGenerator',
    'takePendingTextureDataUpdates', 'textureImageIds', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside Qt3DRender::Render::Texture, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class DirtyFlag(CuteFlags):
    """
    The flags enum 'Qt3DRender::Render::Texture::DirtyFlag' of Qt, with the 7
    names Qt gives in it. Qt names the type of its combinations
    'Qt3DRender::Render::Texture::DirtyFlags'.
    """

    NotDirty = 0x0
    DirtyProperties = 0x1
    DirtyParameters = 0x2
    DirtyImageGenerators = 0x4
    DirtyDataGenerator = 0x8
    DirtySharedTextureId = 0x10
    DirtyPendingDataUpdates = 0x20

  DirtyFlags = DirtyFlag

  #  The classes Qt writes inside Qt3DRender::Render::Texture, each a class
  #  in here as in C++.

  class TextureUpdateInfo(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's Qt3DRender::Render::Texture::TextureUpdateInfo: a
    plain Python object standing in front of one C++
    Qt3DRender::Render::Texture::TextureUpdateInfo.

    C++ hands a Qt3DRender::Render::Texture::TextureUpdateInfo around as a
    copy, so every C++ Qt3DRender::Render::Texture::TextureUpdateInfo behind
    a cute one is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's Qt3DRender::Render::Texture::TextureUpdateInfo yet.
    None can be made from Python: one comes out of a function of another
    class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's
      'Qt3DRender::Render::Texture::TextureUpdateInfo::~TextureUpdateInfo()':
      the destructor: Python removes its C++
      Qt3DRender::Render::Texture::TextureUpdateInfo by it, and has no other
      use for it.

    What to expect
    --------------

    - The C++ Qt3DRender::Render::Texture::TextureUpdateInfo is created at
      the first use, not by
      'Qt3DRender::Render::Texture::TextureUpdateInfo(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a Qt3DRender::Render::Texture::TextureUpdateInfo back
      gives a copy the ritual made for Python, in a new cute
      Qt3DRender::Render::Texture::TextureUpdateInfo.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'Qt3DRender::Render::Texture::TextureUpdateInfo'

    #  Qt's '~Qt3DRender::Render::Texture::TextureUpdateInfo()'. Naming it
    #  makes this a value class: Python owns every C++
    #  Qt3DRender::Render::Texture::TextureUpdateInfo behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN10Qt3DRender6Render7Texture17TextureUpdateInfoD1Ev')

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::Render::Texture'

  #  A C++ Qt3DRender::Render::Texture Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_Render_Texture'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def properties(self) -> Qt3DRender.Render.TextureProperties:
    """
    Calls Qt's 'const TextureProperties
    &Qt3DRender::Render::Texture::properties() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-texture.html#properties

    Returns
    -------

    Qt3DRender.Render.TextureProperties
      A new cute Qt3DRender::Render::TextureProperties around the copy Qt
      gave back. Python owns it.
    """
    #  const TextureProperties &Qt3DRender::Render::Texture::properties()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render7Texture10propertiesEv',
    )
    return Qt3DRender.Render.TextureProperties._cuteOwning(address)

  def parameters(self) -> Qt3DRender.Render.TextureParameters:
    """
    Calls Qt's 'const TextureParameters
    &Qt3DRender::Render::Texture::parameters() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-texture.html#parameters

    Returns
    -------

    Qt3DRender.Render.TextureParameters
      A new cute Qt3DRender::Render::TextureParameters around the copy Qt
      gave back. Python owns it.
    """
    #  const TextureParameters &Qt3DRender::Render::Texture::parameters()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render7Texture10parametersEv',
    )
    return Qt3DRender.Render.TextureParameters._cuteOwning(address)

  def sharedTextureId(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::Render::Texture::sharedTextureId() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-texture.html#sharedTextureId
    """
    #  int Qt3DRender::Render::Texture::sharedTextureId() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render7Texture15sharedTextureIdEv',
    )

  @overload(WAIT['Qt3DRender.Render.TextureImageManager'])
  @overload(NoneType)
  def isValid(
      self,
      manager: Optional[Qt3DRender.Render.TextureImageManager],
  ) -> bool:
    """
    Calls Qt's 'bool Qt3DRender::Render::Texture::isValid(TextureImageManager
    *manager) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-texture.html#isValid

    Parameters
    ----------

    manager : Optional[Qt3DRender.Render.TextureImageManager]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool Qt3DRender::Render::Texture::isValid(TextureImageManager
    #      *manager) const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render7Texture7isValidEPNS0_19TextureImageM'
        'anagerE',
        self._addressOf(manager),
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'Qt3DRender::Render::Texture::Texture()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-texture.html#Texture
    """
    #  Qt3DRender::Render::Texture::Texture()
    self._noteCreation(Texture, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender6Render7TextureC1Ev',
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

  @overload(DirtyFlags)
  def addDirtyFlag(self, flags: DirtyFlags) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::Texture::addDirtyFlag(DirtyFlags
    flags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-texture.html#addDirtyFlag

    Parameters
    ----------

    flags : DirtyFlags
      Passed on as its number.
    """
    #  void Qt3DRender::Render::Texture::addDirtyFlag(DirtyFlags flags)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render7Texture12addDirtyFlagE6QFlagsINS1_9Di'
        'rtyFlagEE',
        flags.value,
    )

  def dirtyFlags(self) -> DirtyFlags:
    """
    Calls Qt's 'DirtyFlags Qt3DRender::Render::Texture::dirtyFlags()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-texture.html#dirtyFlags

    Returns
    -------

    DirtyFlags
      The value standing for the combination Qt gave back.
    """
    #  DirtyFlags Qt3DRender::Render::Texture::dirtyFlags()
    return Texture.DirtyFlags(self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render7Texture10dirtyFlagsEv',
    ))

  def unsetDirty(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::Texture::unsetDirty()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-texture.html#unsetDirty
    """
    #  void Qt3DRender::Render::Texture::unsetDirty()
    self.uglySide.call('ritual_ZN10Qt3DRender6Render7Texture10unsetDirtyEv')

  def cleanup(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::Texture::cleanup()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-texture.html#cleanup
    """
    #  void Qt3DRender::Render::Texture::cleanup()
    self.uglySide.call('ritual_ZN10Qt3DRender6Render7Texture7cleanupEv')

  @overload(WAIT['Qt3DRender.QTextureDataUpdate'])
  def addTextureDataUpdate(
      self,
      update: Qt3DRender.QTextureDataUpdate,
  ) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::Texture::addTextureDataUpdate(const
    QTextureDataUpdate &update)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-texture.html

    Parameters
    ----------

    update : Qt3DRender.QTextureDataUpdate
      Passed on as a value: Qt reads the C++ Qt3DRender::QTextureDataUpdate,
      which stays Python's own.
    """
    #  void Qt3DRender::Render::Texture::addTextureDataUpdate(const
    #      QTextureDataUpdate &update)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render7Texture20addTextureDataUpdateERKNS_18'
        'QTextureDataUpdateE',
        self._valueOf(update),
    )

  @overload(WAIT['Qt3DCore.QNode'], bool)
  @overload(NoneType, bool)
  def syncFromFrontEnd(
      self,
      frontEnd: Optional[Qt3DCore.QNode],
      firstTime: bool,
  ) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::Texture::syncFromFrontEnd(const
    Qt3DCore::QNode *frontEnd, bool firstTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-texture.html#syncFromFrontEnd

    Parameters
    ----------

    frontEnd : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    firstTime : bool
      Passed on as it is.
    """
    #  void Qt3DRender::Render::Texture::syncFromFrontEnd(const
    #      Qt3DCore::QNode *frontEnd, bool firstTime)
    ritual = (
        'ritual_ZN10Qt3DRender6Render7Texture16syncFromFrontEndEPKN8Qt3DCor'
        'e5QNodeEb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10Qt3DRender6Render7Texture16syncFromFrontEndEPKN8Q'
          't3DCore5QNodeEb')
    self.uglySide.call(ritual, self._addressOf(frontEnd), firstTime)

  @staticmethod
  def dataGenerator(*__, **_) -> Never:
    """
    Qt's 'const QTextureGeneratorPtr
    &Qt3DRender::Render::Texture::dataGenerator() const': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.Texture.dataGenerator' has no cute function "
        "yet. Qt's 'const QTextureGeneratorPtr "
        "&Qt3DRender::Render::Texture::dataGenerator() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def setDataGenerator(*__, **_) -> Never:
    """
    Qt's 'void Qt3DRender::Render::Texture::setDataGenerator(const
    QTextureGeneratorPtr &generator)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.Texture.setDataGenerator' has no cute function "
        "yet. Qt's 'void "
        "Qt3DRender::Render::Texture::setDataGenerator(const "
        "QTextureGeneratorPtr &generator)': takes a type Python has no way "
        "to hand over yet.")

  @staticmethod
  def takePendingTextureDataUpdates(*__, **_) -> Never:
    """
    Qt's 'std::vector<QTextureDataUpdate>
    Qt3DRender::Render::Texture::takePendingTextureDataUpdates()': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.Texture.takePendingTextureDataUpdates' has no "
        "cute function yet. Qt's 'std::vector<QTextureDataUpdate> "
        "Qt3DRender::Render::Texture::takePendingTextureDataUpdates()': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def textureImageIds(*__, **_) -> Never:
    """
    Qt's 'const Qt3DCore::QNodeIdVector
    Qt3DRender::Render::Texture::textureImageIds() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.Texture.textureImageIds' has no cute function "
        "yet. Qt's 'const Qt3DCore::QNodeIdVector "
        "Qt3DRender::Render::Texture::textureImageIds() const': gives a "
        "type Python has no way to take yet.")
