"""
QQuick3DXrRuntimeInfo binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DXr/6.12.0/QtQuick3DXr/private/qquick3dxrruntimeinfo_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuick3DXrRuntimeInfo to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QQuick3DXrManager
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuick3DXrManager = WAIT['QQuick3DXrManager']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuick3DXrRuntimeInfo(QObject):
  """
  The cute side of Qt's QQuick3DXrRuntimeInfo: a plain Python object standing
  in front of one C++ QQuick3DXrRuntimeInfo.

  It is built on the cute 'QObject', as Qt's QQuick3DXrRuntimeInfo is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DXrRuntimeInfo that has a ritual and that
  Python can call so far, 6 names in all: 'metaObject', 'tr',
  'enabledExtensions', 'runtimeName', 'runtimeVersion', 'graphicsApiName'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DXrRuntimeInfo::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuick3DXrRuntimeInfo::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuick3DXrRuntimeInfo::qt_qmlMarker_uncreatable()': one of
    Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 12 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuick3DXrRuntimeInfo is created at the first use, not by
    'QQuick3DXrRuntimeInfo(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DXrRuntimeInfo.
  - Qt tells when it has removed the C++ QQuick3DXrRuntimeInfo. Every call on
    the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QQuick3DXrRuntimeInfo::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dxrruntimeinfo.html#tr

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
    #  QString QQuick3DXrRuntimeInfo::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN21QQuick3DXrRuntimeInfo2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DXrRuntimeInfo'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuick3DXrRuntimeInfo::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrruntimeinfo.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DXrRuntimeInfo::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK21QQuick3DXrRuntimeInfo10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def enabledExtensions(self) -> QStringList:
    """
    Calls Qt's 'QStringList QQuick3DXrRuntimeInfo::enabledExtensions()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrruntimeinfo.html#enabledExtensions

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QQuick3DXrRuntimeInfo::enabledExtensions() const
    address = self.uglySide.call(
        'ritual_ZNK21QQuick3DXrRuntimeInfo17enabledExtensionsEv',
    )
    return QStringList._cuteOwning(address)

  def runtimeName(self) -> str:
    """
    Calls Qt's 'QString QQuick3DXrRuntimeInfo::runtimeName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrruntimeinfo.html#runtimeName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuick3DXrRuntimeInfo::runtimeName() const
    return self.uglySide.call(
        'ritual_ZNK21QQuick3DXrRuntimeInfo11runtimeNameEv',
    )

  def runtimeVersion(self) -> str:
    """
    Calls Qt's 'QString QQuick3DXrRuntimeInfo::runtimeVersion() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrruntimeinfo.html#runtimeVersion

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuick3DXrRuntimeInfo::runtimeVersion() const
    return self.uglySide.call(
        'ritual_ZNK21QQuick3DXrRuntimeInfo14runtimeVersionEv',
    )

  def graphicsApiName(self) -> str:
    """
    Calls Qt's 'QString QQuick3DXrRuntimeInfo::graphicsApiName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrruntimeinfo.html#graphicsApiName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuick3DXrRuntimeInfo::graphicsApiName() const
    return self.uglySide.call(
        'ritual_ZNK21QQuick3DXrRuntimeInfo15graphicsApiNameEv',
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

  @overload(QQuick3DXrManager)
  @overload(NoneType)
  @overload(QQuick3DXrManager, QObject)
  @overload(QQuick3DXrManager, NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      manager: Optional[QQuick3DXrManager],
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQuick3DXrRuntimeInfo::QQuick3DXrRuntimeInfo(QQuick3DXrManager *manager,
    QObject *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrruntimeinfo.html#QQuick3DXrRuntimeInfo

    Parameters
    ----------

    manager : Optional[QQuick3DXrManager]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuick3DXrRuntimeInfo::QQuick3DXrRuntimeInfo(QQuick3DXrManager
    #      *manager, QObject *parent)
    self._noteCreation(QQuick3DXrRuntimeInfo, lambda: Rituals.call(
        'ritual_ZN21QQuick3DXrRuntimeInfoC1EP17QQuick3DXrManagerP7QObject',
        self._addressOf(manager), self._addressOf(parent, 'QObject'),
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
