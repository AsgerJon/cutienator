"""
QQuick3DBakedLightmap binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dbakedlightmap_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuick3DBakedLightmap to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuick3DBakedLightmap(QObject):
  """
  The cute side of Qt's QQuick3DBakedLightmap: a plain Python object standing
  in front of one C++ QQuick3DBakedLightmap.

  It is built on the cute 'QObject', as Qt's QQuick3DBakedLightmap is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DBakedLightmap that has a ritual and that
  Python can call so far, 12 names in all: 'metaObject', 'tr', 'isEnabled',
  'key', 'loadPrefix', 'setEnabled', 'setKey', 'setLoadPrefix', 'changed',
  'enabledChanged', 'keyChanged', 'loadPrefixChanged'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DBakedLightmap::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuick3DBakedLightmap::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 16 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuick3DBakedLightmap is created at the first use, not by
    'QQuick3DBakedLightmap(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DBakedLightmap.
  - Qt tells when it has removed the C++ QQuick3DBakedLightmap. Every call on
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
    Calls Qt's 'QString QQuick3DBakedLightmap::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dbakedlightmap.html#tr

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
    #  QString QQuick3DBakedLightmap::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN21QQuick3DBakedLightmap2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DBakedLightmap'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuick3DBakedLightmap::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dbakedlightmap.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DBakedLightmap::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK21QQuick3DBakedLightmap10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isEnabled(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DBakedLightmap::isEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dbakedlightmap.html#isEnabled
    """
    #  bool QQuick3DBakedLightmap::isEnabled() const
    return self.uglySide.call(
        'ritual_ZNK21QQuick3DBakedLightmap9isEnabledEv',
    )

  def key(self) -> str:
    """
    Calls Qt's 'QString QQuick3DBakedLightmap::key() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dbakedlightmap.html#key

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuick3DBakedLightmap::key() const
    return self.uglySide.call('ritual_ZNK21QQuick3DBakedLightmap3keyEv')

  def loadPrefix(self) -> str:
    """
    Calls Qt's 'QString QQuick3DBakedLightmap::loadPrefix() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dbakedlightmap.html#loadPrefix

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuick3DBakedLightmap::loadPrefix() const
    return self.uglySide.call(
        'ritual_ZNK21QQuick3DBakedLightmap10loadPrefixEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QQuick3DBakedLightmap::setEnabled(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dbakedlightmap.html#setEnabled

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QQuick3DBakedLightmap::setEnabled(bool enabled)
    self.uglySide.call(
        'ritual_ZN21QQuick3DBakedLightmap10setEnabledEb', enabled,
    )

  @overload(str)
  def setKey(self, key: str) -> None:
    """
    Calls Qt's 'void QQuick3DBakedLightmap::setKey(const QString &key)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dbakedlightmap.html#setKey

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuick3DBakedLightmap::setKey(const QString &key)
    self.uglySide.call(
        'ritual_ZN21QQuick3DBakedLightmap6setKeyERK7QString', key,
    )

  @overload(str)
  def setLoadPrefix(self, loadPrefix: str) -> None:
    """
    Calls Qt's 'void QQuick3DBakedLightmap::setLoadPrefix(const QString
    &loadPrefix)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dbakedlightmap.html#setLoadPrefix

    Parameters
    ----------

    loadPrefix : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuick3DBakedLightmap::setLoadPrefix(const QString &loadPrefix)
    self.uglySide.call(
        'ritual_ZN21QQuick3DBakedLightmap13setLoadPrefixERK7QString',
        loadPrefix,
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

  def changed(self) -> None:
    """
    Calls Qt's 'void QQuick3DBakedLightmap::changed()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dbakedlightmap.html#changed
    """
    #  void QQuick3DBakedLightmap::changed()
    self.uglySide.call('ritual_ZN21QQuick3DBakedLightmap7changedEv')

  def enabledChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DBakedLightmap::enabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dbakedlightmap.html#enabledChanged
    """
    #  void QQuick3DBakedLightmap::enabledChanged()
    self.uglySide.call('ritual_ZN21QQuick3DBakedLightmap14enabledChangedEv')

  def keyChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DBakedLightmap::keyChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dbakedlightmap.html#keyChanged
    """
    #  void QQuick3DBakedLightmap::keyChanged()
    self.uglySide.call('ritual_ZN21QQuick3DBakedLightmap10keyChangedEv')

  def loadPrefixChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DBakedLightmap::loadPrefixChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dbakedlightmap.html#loadPrefixChanged
    """
    #  void QQuick3DBakedLightmap::loadPrefixChanged()
    self.uglySide.call(
        'ritual_ZN21QQuick3DBakedLightmap17loadPrefixChangedEv',
    )
