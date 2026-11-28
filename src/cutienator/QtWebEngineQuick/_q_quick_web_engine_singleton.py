"""
QQuickWebEngineSingleton binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWebEngineQuick/6.12.0/QtWebEngineQuick/private/qquickwebenginesingleton_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickWebEngineSingleton to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtWebEngineCore import QWebEngineScript
  from . import QQuickWebEngineProfile, QQuickWebEngineSettings

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickWebEngineSingleton(QObject):
  """
  The cute side of Qt's QQuickWebEngineSingleton: a plain Python object
  standing in front of one C++ QQuickWebEngineSingleton.

  It is built on the cute 'QObject', as Qt's QQuickWebEngineSingleton is
  built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickWebEngineSingleton that has a ritual and that
  Python can call so far, 5 names in all: 'metaObject', 'tr', 'settings',
  'defaultProfile', 'script'. None can be made from Python: one comes out of
  a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickWebEngineSingleton::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QQuickWebEngineSingleton::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickWebEngineSingleton::qt_qmlMarker_singleton()': one of
    Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 10 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickWebEngineSingleton is created at the first use, not by
    'QQuickWebEngineSingleton(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickWebEngineSingleton.
  - Qt tells when it has removed the C++ QQuickWebEngineSingleton. Every call
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
    Calls Qt's 'QString QQuickWebEngineSingleton::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwebenginesingleton.html#tr

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
    #  QString QQuickWebEngineSingleton::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN24QQuickWebEngineSingleton2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickWebEngineSingleton'

  #  A C++ QQuickWebEngineSingleton Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickWebEngineSingleton'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickWebEngineSingleton::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesingleton.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickWebEngineSingleton::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK24QQuickWebEngineSingleton10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def settings(self) -> Optional[QQuickWebEngineSettings]:
    """
    Calls Qt's 'QQuickWebEngineSettings *QQuickWebEngineSingleton::settings()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesingleton.html#settings

    Returns
    -------

    Optional[QQuickWebEngineSettings]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickWebEngineSettings *QQuickWebEngineSingleton::settings() const
    address = self.uglySide.call(
        'ritual_ZNK24QQuickWebEngineSingleton8settingsEv',
    )
    from . import QQuickWebEngineSettings
    return QQuickWebEngineSettings._cuteAt(address)

  def defaultProfile(self) -> Optional[QQuickWebEngineProfile]:
    """
    Calls Qt's 'QQuickWebEngineProfile
    *QQuickWebEngineSingleton::defaultProfile() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesingleton.html#defaultProfile

    Returns
    -------

    Optional[QQuickWebEngineProfile]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickWebEngineProfile *QQuickWebEngineSingleton::defaultProfile()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK24QQuickWebEngineSingleton14defaultProfileEv',
    )
    from . import QQuickWebEngineProfile
    return QQuickWebEngineProfile._cuteAt(address)

  def script(self) -> QWebEngineScript:
    """
    Calls Qt's 'QWebEngineScript QQuickWebEngineSingleton::script() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesingleton.html#script

    Returns
    -------

    QWebEngineScript
      A new cute QWebEngineScript around the copy Qt gave back. Python owns
      it.
    """
    #  QWebEngineScript QQuickWebEngineSingleton::script() const
    address = self.uglySide.call(
        'ritual_ZNK24QQuickWebEngineSingleton6scriptEv',
    )
    from ..QtWebEngineCore import QWebEngineScript
    return QWebEngineScript._cuteOwning(address)

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
