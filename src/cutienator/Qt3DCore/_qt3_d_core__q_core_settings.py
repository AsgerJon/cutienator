"""
Qt3DCore::QCoreSettings binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DCore/qcoresettings.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import Qt3DCore

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QCoreSettings(Qt3DCore.QComponent):
  """
  The cute side of Qt's Qt3DCore::QCoreSettings: a plain Python object
  standing in front of one C++ Qt3DCore::QCoreSettings.

  It is built on the cute 'Qt3DCore::QComponent', as Qt's
  Qt3DCore::QCoreSettings is built on Qt's Qt3DCore::QComponent, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DCore::QCoreSettings that has a ritual and that
  Python can call so far, 6 names in all: 'metaObject', 'tr',
  'boundingVolumesEnabled', 'setBoundingVolumesEnabled',
  'boundingVolumesEnabledChanged', 'd_func'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DCore::QCoreSettings::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int Qt3DCore::QCoreSettings::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DCore::QCoreSettings::~QCoreSettings()': the destructor: Python
    never removes a C++ Qt3DCore::QCoreSettings.
  - Qt's 'const QCoreSettingsPrivate *Qt3DCore::QCoreSettings::d_func()
    const': takes in Python what 'QCoreSettingsPrivate
    *Qt3DCore::QCoreSettings::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 13 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DCore::QCoreSettings is created at the first use, not by
    'Qt3DCore::QCoreSettings(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DCore::QCoreSettings.
  - Qt tells when it has removed the C++ Qt3DCore::QCoreSettings. Every call
    on the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString Qt3DCore::QCoreSettings::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qcoresettings.html#tr

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
    #  QString Qt3DCore::QCoreSettings::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN8Qt3DCore13QCoreSettings2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DCore::QCoreSettings'

  #  A C++ Qt3DCore::QCoreSettings Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DCore_QCoreSettings'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DCore::QCoreSettings::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qcoresettings.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DCore::QCoreSettings::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore13QCoreSettings10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def boundingVolumesEnabled(self) -> bool:
    """
    Calls Qt's 'bool Qt3DCore::QCoreSettings::boundingVolumesEnabled()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qcoresettings.html#boundingVolumesEnabled
    """
    #  bool Qt3DCore::QCoreSettings::boundingVolumesEnabled() const
    return self.uglySide.call(
        'ritual_ZNK8Qt3DCore13QCoreSettings22boundingVolumesEnabledEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setBoundingVolumesEnabled(self, boundingVolumesEnabled: bool) -> None:
    """
    Calls Qt's 'void Qt3DCore::QCoreSettings::setBoundingVolumesEnabled(bool
    boundingVolumesEnabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qcoresettings.html

    Parameters
    ----------

    boundingVolumesEnabled : bool
      Passed on as it is.
    """
    #  void Qt3DCore::QCoreSettings::setBoundingVolumesEnabled(bool
    #      boundingVolumesEnabled)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore13QCoreSettings25setBoundingVolumesEnabledEb',
        boundingVolumesEnabled,
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
    'Qt3DCore::QCoreSettings::QCoreSettings(Qt3DCore::QNode *parent)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qcoresettings.html#QCoreSettings

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DCore::QCoreSettings::QCoreSettings(Qt3DCore::QNode *parent)
    self._noteCreation(QCoreSettings, lambda: Rituals.call(
        'ritual_ZN8Qt3DCore13QCoreSettingsC1EPNS_5QNodeE',
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

  @overload(bool)
  def boundingVolumesEnabledChanged(
      self,
      boundingVolumesEnabled: bool,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DCore::QCoreSettings::boundingVolumesEnabledChanged(bool
    boundingVolumesEnabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qcoresettings.html

    Parameters
    ----------

    boundingVolumesEnabled : bool
      Passed on as it is.
    """
    #  void Qt3DCore::QCoreSettings::boundingVolumesEnabledChanged(bool
    #      boundingVolumesEnabled)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore13QCoreSettings29boundingVolumesEnabledChangedEb',
        boundingVolumesEnabled,
    )

  def d_func(self) -> Optional[Qt3DCore.QCoreSettingsPrivate]:
    """
    Calls Qt's 'QCoreSettingsPrivate *Qt3DCore::QCoreSettings::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qcoresettings.html#d_func

    Returns
    -------

    Optional[Qt3DCore.QCoreSettingsPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCoreSettingsPrivate *Qt3DCore::QCoreSettings::d_func()
    address = self.uglySide.call(
        'ritual_ZN8Qt3DCore13QCoreSettings6d_funcEv',
    )
    return Qt3DCore.QCoreSettingsPrivate._cuteAt(address)
