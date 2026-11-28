"""
QSSGUserRenderPassManager binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssguserrenderpassmanager_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGUserRenderPassManager to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtGui import QRhiTexture
  from . import QSSGManagedRhiTexture, QSSGRenderUserPass
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRhiTexture = WAIT['QRhiTexture']
  QSSGManagedRhiTexture = WAIT['QSSGManagedRhiTexture']
  QSSGRenderUserPass = WAIT['QSSGRenderUserPass']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSSGUserRenderPassManager(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSSGUserRenderPassManager: a plain Python object
  standing in front of one C++ QSSGUserRenderPassManager.

  What exists
  -----------

  Every function of Qt's QSSGUserRenderPassManager that has a ritual and that
  Python can call so far, 12 names in all: 'scheduleUserPass',
  'unscheduleUserPass', 'updateUserPassOrder', 'scheduledUserPasses',
  'releaseAll', 'unregisterManagedTexture', 'registerManagedTexture',
  'maxUserPassSlots', 'acquireUserPassSlot', 'resetForFrame', 'derefTexture',
  'refTexture'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSSGUserRenderPassManager::QSSGUserRenderPassManager(Private a0)':
    names the enum 'QSSGUserRenderPassManager::Private', whose class cannot
    be named here.
  - Qt's 'QSSGUserRenderPassManager::~QSSGUserRenderPassManager()': the
    destructor: Python never removes a C++ QSSGUserRenderPassManager.
  - Qt's 'std::shared_ptr<QSSGUserRenderPassManager>
    QSSGUserRenderPassManager::create()': gives a type Python has no way to
    take yet.
  - Qt's 'QSSGRhiRenderableTextureV2Ptr
    QSSGUserRenderPassManager::getOrCreateRenderableTexture(const
    QSSGRenderUserPass &userPass)': takes a type Python has no way to hand
    over yet.
  - Qt's 'QSSGRhiRenderableTextureV2Ptr
    QSSGUserRenderPassManager::getUserPassTexureResult(const
    QSSGRenderUserPass &userPass) const': takes a type Python has no way to
    hand over yet.
  - Qt's 'bool QSSGUserRenderPassManager::derefTexture(const
    std::unique_ptr<QRhiTexture> &texture)': takes a type Python has no way
    to hand over yet.
  - Qt's 'void QSSGUserRenderPassManager::refTexture(const
    std::unique_ptr<QRhiTexture> &texture)': takes a type Python has no way
    to hand over yet.

  What has no ritual
  ------------------

  4 of the 23 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ QSSGUserRenderPassManager is created at the first use, not by
    'QSSGUserRenderPassManager(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSSGUserRenderPassManager.
  - Each name of Qt's QSSGUserRenderPassManager that has no cute function
    yet, '__init__', 'create', 'getOrCreateRenderableTexture',
    'getUserPassTexureResult', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def maxUserPassSlots() -> int:
    """
    Calls Qt's 'size_t QSSGUserRenderPassManager::maxUserPassSlots()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssguserrenderpassmanager.html#maxUserPassSlots
    """
    #  size_t QSSGUserRenderPassManager::maxUserPassSlots()
    return Rituals.call(
        'ritual_ZN25QSSGUserRenderPassManager16maxUserPassSlotsEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGUserRenderPassManager'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def scheduledUserPasses(self) -> QList[QSSGRenderUserPass]:
    """
    Calls Qt's 'const UserPassSet
    &QSSGUserRenderPassManager::scheduledUserPasses() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssguserrenderpassmanager.html#scheduledUserPasses

    Returns
    -------

    QList[QSSGRenderUserPass]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  const UserPassSet &QSSGUserRenderPassManager::scheduledUserPasses()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK25QSSGUserRenderPassManager19scheduledUserPassesEv',
    )
    from . import QSSGRenderUserPass
    return QList[QSSGRenderUserPass]._cuteOwning(address)

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
    Qt's 'QSSGUserRenderPassManager::QSSGUserRenderPassManager(Private a0)':
    names the enum 'QSSGUserRenderPassManager::Private', whose class cannot
    be named here.
    """
    raise NotImplementedError(
        "'QSSGUserRenderPassManager.__init__' has no cute function yet. "
        "Qt's 'QSSGUserRenderPassManager::QSSGUserRenderPassManager(Private "
        "a0)': names the enum 'QSSGUserRenderPassManager::Private', whose "
        "class cannot be named here.")

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

  @overload(QSSGRenderUserPass)
  @overload(NoneType)
  def scheduleUserPass(
      self,
      userPasses: Optional[QSSGRenderUserPass],
  ) -> None:
    """
    Calls Qt's 'void
    QSSGUserRenderPassManager::scheduleUserPass(QSSGRenderUserPass
    *userPasses)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssguserrenderpassmanager.html#scheduleUserPass

    Parameters
    ----------

    userPasses : Optional[QSSGRenderUserPass]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSSGUserRenderPassManager::scheduleUserPass(QSSGRenderUserPass
    #      *userPasses)
    self.uglySide.call(
        'ritual_ZN25QSSGUserRenderPassManager16scheduleUserPassEP18QSSGRend'
        'erUserPass',
        self._addressOf(userPasses),
    )

  @overload(QSSGRenderUserPass)
  @overload(NoneType)
  def unscheduleUserPass(
      self,
      userPasses: Optional[QSSGRenderUserPass],
  ) -> None:
    """
    Calls Qt's 'void QSSGUserRenderPassManager::unscheduleUserPass(const
    QSSGRenderUserPass *userPasses)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssguserrenderpassmanager.html#unscheduleUserPass

    Parameters
    ----------

    userPasses : Optional[QSSGRenderUserPass]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSSGUserRenderPassManager::unscheduleUserPass(const
    #      QSSGRenderUserPass *userPasses)
    self.uglySide.call(
        'ritual_ZN25QSSGUserRenderPassManager18unscheduleUserPassEPK18QSSGR'
        'enderUserPass',
        self._addressOf(userPasses),
    )

  @overload()
  @overload(bool)
  def updateUserPassOrder(self, forceUpdate: bool = False) -> None:
    """
    Calls Qt's 'void QSSGUserRenderPassManager::updateUserPassOrder(bool
    forceUpdate)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssguserrenderpassmanager.html#updateUserPassOrder

    Parameters
    ----------

    forceUpdate : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QSSGUserRenderPassManager::updateUserPassOrder(bool forceUpdate)
    self.uglySide.call(
        'ritual_ZN25QSSGUserRenderPassManager19updateUserPassOrderEb',
        forceUpdate,
    )

  def releaseAll(self) -> None:
    """
    Calls Qt's 'void QSSGUserRenderPassManager::releaseAll()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssguserrenderpassmanager.html#releaseAll
    """
    #  void QSSGUserRenderPassManager::releaseAll()
    self.uglySide.call('ritual_ZN25QSSGUserRenderPassManager10releaseAllEv')

  @overload(QSSGManagedRhiTexture)
  @overload(NoneType)
  def unregisterManagedTexture(
      self,
      textureWrapper: Optional[QSSGManagedRhiTexture],
  ) -> None:
    """
    Calls Qt's 'void
    QSSGUserRenderPassManager::unregisterManagedTexture(QSSGManagedRhiTexture
    *textureWrapper)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssguserrenderpassmanager.html

    Parameters
    ----------

    textureWrapper : Optional[QSSGManagedRhiTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSSGUserRenderPassManager::unregisterManagedTexture(
    #      QSSGManagedRhiTexture *textureWrapper)
    self.uglySide.call(
        'ritual_ZN25QSSGUserRenderPassManager24unregisterManagedTextureEP21'
        'QSSGManagedRhiTexture',
        self._addressOf(textureWrapper),
    )

  @overload(QSSGManagedRhiTexture)
  @overload(NoneType)
  def registerManagedTexture(
      self,
      textureWrapper: Optional[QSSGManagedRhiTexture],
  ) -> None:
    """
    Calls Qt's 'void
    QSSGUserRenderPassManager::registerManagedTexture(QSSGManagedRhiTexture
    *textureWrapper)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssguserrenderpassmanager.html

    Parameters
    ----------

    textureWrapper : Optional[QSSGManagedRhiTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSSGUserRenderPassManager::registerManagedTexture(
    #      QSSGManagedRhiTexture *textureWrapper)
    self.uglySide.call(
        'ritual_ZN25QSSGUserRenderPassManager22registerManagedTextureEP21QS'
        'SGManagedRhiTexture',
        self._addressOf(textureWrapper),
    )

  def acquireUserPassSlot(self) -> int:
    """
    Calls Qt's 'qsizetype QSSGUserRenderPassManager::acquireUserPassSlot()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssguserrenderpassmanager.html#acquireUserPassSlot
    """
    #  qsizetype QSSGUserRenderPassManager::acquireUserPassSlot()
    return self.uglySide.call(
        'ritual_ZN25QSSGUserRenderPassManager19acquireUserPassSlotEv',
    )

  def resetForFrame(self) -> None:
    """
    Calls Qt's 'void QSSGUserRenderPassManager::resetForFrame()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssguserrenderpassmanager.html#resetForFrame
    """
    #  void QSSGUserRenderPassManager::resetForFrame()
    self.uglySide.call(
        'ritual_ZN25QSSGUserRenderPassManager13resetForFrameEv',
    )

  @overload(QRhiTexture)
  @overload(NoneType)
  def derefTexture(self, texture: Optional[QRhiTexture]) -> bool:
    """
    Calls Qt's 'bool QSSGUserRenderPassManager::derefTexture(QRhiTexture
    *texture)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssguserrenderpassmanager.html#derefTexture

    Parameters
    ----------

    texture : Optional[QRhiTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QSSGUserRenderPassManager::derefTexture(QRhiTexture *texture)
    return self.uglySide.call(
        'ritual_ZN25QSSGUserRenderPassManager12derefTextureEP11QRhiTexture',
        self._addressOf(texture),
    )

  @overload(QRhiTexture)
  @overload(NoneType)
  def refTexture(self, texture: Optional[QRhiTexture]) -> None:
    """
    Calls Qt's 'void QSSGUserRenderPassManager::refTexture(QRhiTexture
    *texture)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssguserrenderpassmanager.html#refTexture

    Parameters
    ----------

    texture : Optional[QRhiTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSSGUserRenderPassManager::refTexture(QRhiTexture *texture)
    self.uglySide.call(
        'ritual_ZN25QSSGUserRenderPassManager10refTextureEP11QRhiTexture',
        self._addressOf(texture),
    )

  @staticmethod
  def create(*__, **_) -> Never:
    """
    Qt's 'std::shared_ptr<QSSGUserRenderPassManager>
    QSSGUserRenderPassManager::create()': gives a type Python has no way to
    take yet.
    """
    raise NotImplementedError(
        "'QSSGUserRenderPassManager.create' has no cute function yet. Qt's "
        "'std::shared_ptr<QSSGUserRenderPassManager> "
        "QSSGUserRenderPassManager::create()': gives a type Python has no "
        "way to take yet.")

  @staticmethod
  def getOrCreateRenderableTexture(*__, **_) -> Never:
    """
    Qt's 'QSSGRhiRenderableTextureV2Ptr
    QSSGUserRenderPassManager::getOrCreateRenderableTexture(const
    QSSGRenderUserPass &userPass)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QSSGUserRenderPassManager.getOrCreateRenderableTexture' has no "
        "cute function yet. Qt's 'QSSGRhiRenderableTextureV2Ptr "
        "QSSGUserRenderPassManager::getOrCreateRenderableTexture(const "
        "QSSGRenderUserPass &userPass)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def getUserPassTexureResult(*__, **_) -> Never:
    """
    Qt's 'QSSGRhiRenderableTextureV2Ptr
    QSSGUserRenderPassManager::getUserPassTexureResult(const
    QSSGRenderUserPass &userPass) const': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QSSGUserRenderPassManager.getUserPassTexureResult' has no cute "
        "function yet. Qt's 'QSSGRhiRenderableTextureV2Ptr "
        "QSSGUserRenderPassManager::getUserPassTexureResult(const "
        "QSSGRenderUserPass &userPass) const': takes a type Python has no "
        "way to hand over yet.")
