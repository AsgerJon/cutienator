"""
Qt3DExtras::QSkyboxEntity binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DExtras/qskyboxentity.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DExtras

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSkyboxEntity(Qt3DCore.QEntity):
  """
  The cute side of Qt's Qt3DExtras::QSkyboxEntity: a plain Python object
  standing in front of one C++ Qt3DExtras::QSkyboxEntity.

  It is built on the cute 'Qt3DCore::QEntity', as Qt's
  Qt3DExtras::QSkyboxEntity is built on Qt's Qt3DCore::QEntity, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DExtras::QSkyboxEntity that has a ritual and that
  Python can call so far, 12 names in all: 'metaObject', 'tr', 'baseName',
  'extension', 'isGammaCorrectEnabled', 'setBaseName', 'setExtension',
  'setGammaCorrectEnabled', 'baseNameChanged', 'extensionChanged',
  'gammaCorrectEnabledChanged', 'd_func'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DExtras::QSkyboxEntity::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int Qt3DExtras::QSkyboxEntity::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DExtras::QSkyboxEntity::~QSkyboxEntity()': the destructor:
    Python never removes a C++ Qt3DExtras::QSkyboxEntity.
  - Qt's 'const QSkyboxEntityPrivate *Qt3DExtras::QSkyboxEntity::d_func()
    const': takes in Python what 'QSkyboxEntityPrivate
    *Qt3DExtras::QSkyboxEntity::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 19 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DExtras::QSkyboxEntity is created at the first use, not by
    'Qt3DExtras::QSkyboxEntity(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DExtras::QSkyboxEntity.
  - Qt tells when it has removed the C++ Qt3DExtras::QSkyboxEntity. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString Qt3DExtras::QSkyboxEntity::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dextras-qskyboxentity.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString Qt3DExtras::QSkyboxEntity::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN10Qt3DExtras13QSkyboxEntity2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DExtras::QSkyboxEntity'

  #  A C++ Qt3DExtras::QSkyboxEntity Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DExtras_QSkyboxEntity'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DExtras::QSkyboxEntity::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qskyboxentity.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DExtras::QSkyboxEntity::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras13QSkyboxEntity10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def baseName(self) -> str:
    """
    Calls Qt's 'QString Qt3DExtras::QSkyboxEntity::baseName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qskyboxentity.html#baseName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString Qt3DExtras::QSkyboxEntity::baseName() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DExtras13QSkyboxEntity8baseNameEv',
    )

  def extension(self) -> str:
    """
    Calls Qt's 'QString Qt3DExtras::QSkyboxEntity::extension() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qskyboxentity.html#extension

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString Qt3DExtras::QSkyboxEntity::extension() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DExtras13QSkyboxEntity9extensionEv',
    )

  def isGammaCorrectEnabled(self) -> bool:
    """
    Calls Qt's 'bool Qt3DExtras::QSkyboxEntity::isGammaCorrectEnabled()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qskyboxentity.html
    """
    #  bool Qt3DExtras::QSkyboxEntity::isGammaCorrectEnabled() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DExtras13QSkyboxEntity21isGammaCorrectEnabledEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setBaseName(self, path: str) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QSkyboxEntity::setBaseName(const QString
    &path)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qskyboxentity.html#setBaseName

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void Qt3DExtras::QSkyboxEntity::setBaseName(const QString &path)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras13QSkyboxEntity11setBaseNameERK7QString', path,
    )

  @overload(str)
  def setExtension(self, extension: str) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QSkyboxEntity::setExtension(const QString
    &extension)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qskyboxentity.html#setExtension

    Parameters
    ----------

    extension : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void Qt3DExtras::QSkyboxEntity::setExtension(const QString &extension)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras13QSkyboxEntity12setExtensionERK7QString',
        extension,
    )

  @overload(bool)
  def setGammaCorrectEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QSkyboxEntity::setGammaCorrectEnabled(bool
    enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qskyboxentity.html

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void Qt3DExtras::QSkyboxEntity::setGammaCorrectEnabled(bool enabled)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras13QSkyboxEntity22setGammaCorrectEnabledEb',
        enabled,
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

  @overload()
  @overload(Qt3DCore.QNode)
  @overload(NoneType)
  def __init__(self, parent: Optional[Qt3DCore.QNode] = None) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DExtras::QSkyboxEntity::QSkyboxEntity(Qt3DCore::QNode *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qskyboxentity.html#QSkyboxEntity

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DExtras::QSkyboxEntity::QSkyboxEntity(Qt3DCore::QNode *parent)
    self._noteCreation(QSkyboxEntity, lambda: Rituals.call(
        'ritual_ZN10Qt3DExtras13QSkyboxEntityC1EPN8Qt3DCore5QNodeE',
        self._addressOf(parent),
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

  @overload(str)
  def baseNameChanged(self, path: str) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QSkyboxEntity::baseNameChanged(const QString
    &path)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qskyboxentity.html#baseNameChanged

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void Qt3DExtras::QSkyboxEntity::baseNameChanged(const QString &path)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras13QSkyboxEntity15baseNameChangedERK7QString',
        path,
    )

  @overload(str)
  def extensionChanged(self, extension: str) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QSkyboxEntity::extensionChanged(const
    QString &extension)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qskyboxentity.html#extensionChanged

    Parameters
    ----------

    extension : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void Qt3DExtras::QSkyboxEntity::extensionChanged(const QString
    #      &extension)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras13QSkyboxEntity16extensionChangedERK7QString',
        extension,
    )

  @overload(bool)
  def gammaCorrectEnabledChanged(self, enabled: bool) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QSkyboxEntity::gammaCorrectEnabledChanged(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qskyboxentity.html

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void Qt3DExtras::QSkyboxEntity::gammaCorrectEnabledChanged(bool
    #      enabled)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras13QSkyboxEntity26gammaCorrectEnabledChangedEb',
        enabled,
    )

  def d_func(self) -> Optional[Qt3DExtras.QSkyboxEntityPrivate]:
    """
    Calls Qt's 'QSkyboxEntityPrivate *Qt3DExtras::QSkyboxEntity::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qskyboxentity.html#d_func

    Returns
    -------

    Optional[Qt3DExtras.QSkyboxEntityPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSkyboxEntityPrivate *Qt3DExtras::QSkyboxEntity::d_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DExtras13QSkyboxEntity6d_funcEv',
    )
    return Qt3DExtras.QSkyboxEntityPrivate._cuteAt(address)
