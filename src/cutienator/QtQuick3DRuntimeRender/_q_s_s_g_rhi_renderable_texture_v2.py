"""
QSSGRhiRenderableTextureV2 binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrhicontext_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGRhiRenderableTextureV2 to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..QtGui import QRhiTextureRenderTarget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray
  from ..QtGui import QRhi, QRhiTextureRenderTargetDescription
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QRhi = WAIT['QRhi']
  QRhiTextureRenderTargetDescription = WAIT['QRhiTextureRenderTargetDescription']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSSGRhiRenderableTextureV2(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSSGRhiRenderableTextureV2: a plain Python object
  standing in front of one C++ QSSGRhiRenderableTextureV2.

  What exists
  -----------

  Every function of Qt's QSSGRhiRenderableTextureV2 that has a ritual and
  that Python can call so far, 8 names in all: 'setDescription', 'setName',
  'getName', 'colorAttachmentCount', 'isValid', 'resetRenderTarget', 'reset',
  'invalidate'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSSGRhiRenderableTextureV2::QSSGRhiRenderableTextureV2(const
    std::shared_ptr<QSSGUserRenderPassManager> &manager, Private a1)': takes
    a type Python has no way to hand over yet.
  - Qt's 'QSSGRhiRenderableTextureV2::~QSSGRhiRenderableTextureV2()': the
    destructor: Python never removes a C++ QSSGRhiRenderableTextureV2.
  - Qt's 'const QSSGManagedRhiTexturePtr
    &QSSGRhiRenderableTextureV2::getDepthTexture() const': gives a type
    Python has no way to take yet.
  - Qt's 'const std::unique_ptr<QRhiRenderBuffer>
    &QSSGRhiRenderableTextureV2::getDepthStencil() const': gives a type
    Python has no way to take yet.
  - Qt's 'const std::unique_ptr<QRhiRenderPassDescriptor>
    &QSSGRhiRenderableTextureV2::getRenderPassDescriptor() const': gives a
    type Python has no way to take yet.
  - Qt's 'const std::unique_ptr<QRhiTextureRenderTarget>
    &QSSGRhiRenderableTextureV2::getRenderTarget() const': gives a type
    Python has no way to take yet.
  - Qt's 'const QSSGManagedRhiTexturePtr
    &QSSGRhiRenderableTextureV2::getColorTexture(int index) const': gives a
    type Python has no way to take yet.

  What has no ritual
  ------------------

  1 of the 16 functions Qt declares: 1 cannot be called and cannot be called
  through the meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ QSSGRhiRenderableTextureV2 is created at the first use, not by
    'QSSGRhiRenderableTextureV2(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSSGRhiRenderableTextureV2.
  - Each name of Qt's QSSGRhiRenderableTextureV2 that has no cute function
    yet, '__init__', 'finialize', 'getColorTexture', 'getDepthStencil',
    'getDepthTexture', 'getRenderPassDescriptor', 'getRenderTarget', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGRhiRenderableTextureV2'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def getName(self) -> QByteArray:
    """
    Calls Qt's 'const QByteArray &QSSGRhiRenderableTextureV2::getName()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhirenderabletexturev2.html#getName

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  const QByteArray &QSSGRhiRenderableTextureV2::getName() const
    address = self.uglySide.call(
        'ritual_ZNK26QSSGRhiRenderableTextureV27getNameEv',
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def colorAttachmentCount(self) -> int:
    """
    Calls Qt's 'size_t QSSGRhiRenderableTextureV2::colorAttachmentCount()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhirenderabletexturev2.html
    """
    #  size_t QSSGRhiRenderableTextureV2::colorAttachmentCount() const
    return self.uglySide.call(
        'ritual_ZNK26QSSGRhiRenderableTextureV220colorAttachmentCountEv',
    )

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QSSGRhiRenderableTextureV2::isValid() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhirenderabletexturev2.html#isValid
    """
    #  bool QSSGRhiRenderableTextureV2::isValid() const
    return self.uglySide.call(
        'ritual_ZNK26QSSGRhiRenderableTextureV27isValidEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QRhi, QRhiTextureRenderTargetDescription)
  @overload(NoneType, QRhiTextureRenderTargetDescription)
  @overload(
      QRhi, QRhiTextureRenderTargetDescription,
      QRhiTextureRenderTarget.Flags,
  )
  @overload(
      NoneType, QRhiTextureRenderTargetDescription,
      QRhiTextureRenderTarget.Flags,
  )
  def setDescription(
      self,
      rhi: Optional[QRhi],
      rtDesc: QRhiTextureRenderTargetDescription,
      a2: QRhiTextureRenderTarget.Flags = QRhiTextureRenderTarget.Flags(),
  ) -> None:
    """
    Calls Qt's 'void QSSGRhiRenderableTextureV2::setDescription(QRhi *rhi,
    QRhiTextureRenderTargetDescription rtDesc, QRhiTextureRenderTarget::Flags
    a2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhirenderabletexturev2.html#setDescription

    Parameters
    ----------

    rhi : Optional[QRhi]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    rtDesc : QRhiTextureRenderTargetDescription
      Passed on as a value: Qt reads the C++
      QRhiTextureRenderTargetDescription, which stays Python's own.

    a2 : QRhiTextureRenderTarget.Flags
      Passed on as its number. May be left out, as in Qt: it is then
      QRhiTextureRenderTarget.Flags().
    """
    #  void QSSGRhiRenderableTextureV2::setDescription(QRhi *rhi,
    #      QRhiTextureRenderTargetDescription rtDesc,
    #      QRhiTextureRenderTarget::Flags a2)
    self.uglySide.call(
        'ritual_ZN26QSSGRhiRenderableTextureV214setDescriptionEP4QRhi34QRhi'
        'TextureRenderTargetDescription6QFlagsIN23QRhiTextureRenderTarget4F'
        'lagEE',
        self._addressOf(rhi), self._valueOf(rtDesc), a2.value,
    )

  @overload(QByteArray)
  def setName(self, name: QByteArray) -> None:
    """
    Calls Qt's 'void QSSGRhiRenderableTextureV2::setName(const QByteArray
    &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhirenderabletexturev2.html#setName

    Parameters
    ----------

    name : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QSSGRhiRenderableTextureV2::setName(const QByteArray &name)
    self.uglySide.call(
        'ritual_ZN26QSSGRhiRenderableTextureV27setNameERK10QByteArray',
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QSSGRhiRenderableTextureV2::QSSGRhiRenderableTextureV2(const
    std::shared_ptr<QSSGUserRenderPassManager> &manager, Private a1)': takes
    a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGRhiRenderableTextureV2.__init__' has no cute function yet. "
        "Qt's 'QSSGRhiRenderableTextureV2::QSSGRhiRenderableTextureV2(const "
        "std::shared_ptr<QSSGUserRenderPassManager> &manager, Private a1)': "
        "takes a type Python has no way to hand over yet.")

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

  def resetRenderTarget(self) -> None:
    """
    Calls Qt's 'void QSSGRhiRenderableTextureV2::resetRenderTarget()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhirenderabletexturev2.html#resetRenderTarget
    """
    #  void QSSGRhiRenderableTextureV2::resetRenderTarget()
    self.uglySide.call(
        'ritual_ZN26QSSGRhiRenderableTextureV217resetRenderTargetEv',
    )

  def reset(self) -> None:
    """
    Calls Qt's 'void QSSGRhiRenderableTextureV2::reset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhirenderabletexturev2.html#reset
    """
    #  void QSSGRhiRenderableTextureV2::reset()
    self.uglySide.call('ritual_ZN26QSSGRhiRenderableTextureV25resetEv')

  def invalidate(self) -> None:
    """
    Calls Qt's 'void QSSGRhiRenderableTextureV2::invalidate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhirenderabletexturev2.html#invalidate
    """
    #  void QSSGRhiRenderableTextureV2::invalidate()
    self.uglySide.call('ritual_ZN26QSSGRhiRenderableTextureV210invalidateEv')

  @staticmethod
  def finialize(*__, **_) -> Never:
    """
    Qt's 'void QSSGRhiRenderableTextureV2::finialize(QRhi *rhi)': cannot be
    called and cannot be called through the meta-object and cannot be copied:
    no header file has its code, Qt's source does not mark it or its class
    for use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QSSGRhiRenderableTextureV2.finialize' has no cute function yet. "
        "Qt's 'void QSSGRhiRenderableTextureV2::finialize(QRhi *rhi)': "
        "cannot be called and cannot be called through the meta-object and "
        "cannot be copied: no header file has its code, Qt's source does "
        "not mark it or its class for use from outside Qt or writes it "
        "'inline' or nowhere, and it is no signal, slot or invokable "
        "function giving back nothing, of a class built on QObject, and "
        "Qt's source has no code for it that could be told from the rest.")

  @staticmethod
  def getColorTexture(*__, **_) -> Never:
    """
    Qt's 'const QSSGManagedRhiTexturePtr
    &QSSGRhiRenderableTextureV2::getColorTexture(int index) const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSSGRhiRenderableTextureV2.getColorTexture' has no cute function "
        "yet. Qt's 'const QSSGManagedRhiTexturePtr "
        "&QSSGRhiRenderableTextureV2::getColorTexture(int index) const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def getDepthStencil(*__, **_) -> Never:
    """
    Qt's 'const std::unique_ptr<QRhiRenderBuffer>
    &QSSGRhiRenderableTextureV2::getDepthStencil() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSSGRhiRenderableTextureV2.getDepthStencil' has no cute function "
        "yet. Qt's 'const std::unique_ptr<QRhiRenderBuffer> "
        "&QSSGRhiRenderableTextureV2::getDepthStencil() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def getDepthTexture(*__, **_) -> Never:
    """
    Qt's 'const QSSGManagedRhiTexturePtr
    &QSSGRhiRenderableTextureV2::getDepthTexture() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSSGRhiRenderableTextureV2.getDepthTexture' has no cute function "
        "yet. Qt's 'const QSSGManagedRhiTexturePtr "
        "&QSSGRhiRenderableTextureV2::getDepthTexture() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def getRenderPassDescriptor(*__, **_) -> Never:
    """
    Qt's 'const std::unique_ptr<QRhiRenderPassDescriptor>
    &QSSGRhiRenderableTextureV2::getRenderPassDescriptor() const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSSGRhiRenderableTextureV2.getRenderPassDescriptor' has no cute "
        "function yet. Qt's 'const "
        "std::unique_ptr<QRhiRenderPassDescriptor> "
        "&QSSGRhiRenderableTextureV2::getRenderPassDescriptor() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def getRenderTarget(*__, **_) -> Never:
    """
    Qt's 'const std::unique_ptr<QRhiTextureRenderTarget>
    &QSSGRhiRenderableTextureV2::getRenderTarget() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSSGRhiRenderableTextureV2.getRenderTarget' has no cute function "
        "yet. Qt's 'const std::unique_ptr<QRhiTextureRenderTarget> "
        "&QSSGRhiRenderableTextureV2::getRenderTarget() const': gives a "
        "type Python has no way to take yet.")
