"""
QWebEngineExtensionManager binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWebEngineCore/qwebengineextensionmanager.h, Qt 6.12.0. Changes made here
#  are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QEvent, QMetaObject
  from . import QWebEngineExtensionInfo
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QWebEngineExtensionInfo = WAIT['QWebEngineExtensionInfo']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWebEngineExtensionManager(QObject):
  """
  The cute side of Qt's QWebEngineExtensionManager: a plain Python object
  standing in front of one C++ QWebEngineExtensionManager.

  It is built on the cute 'QObject', as Qt's QWebEngineExtensionManager is
  built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QWebEngineExtensionManager that has a ritual and
  that Python can call so far, 14 names in all: 'metaObject', 'tr',
  'loadExtension', 'installExtension', 'unloadExtension',
  'uninstallExtension', 'setExtensionEnabled', 'installPath', 'extensions',
  'loadFinished', 'installFinished', 'unloadFinished', 'uninstallFinished',
  'event'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QWebEngineExtensionManager::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QWebEngineExtensionManager::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QWebEngineExtensionManager::~QWebEngineExtensionManager()': the
    destructor: Python never removes a C++ QWebEngineExtensionManager.
  - Qt's 'QWebEngineExtensionManager::QWebEngineExtensionManager(
    QtWebEngineCore::ExtensionManager *d)': names
    'QtWebEngineCore::ExtensionManager', which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 22 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QWebEngineExtensionManager is created at the first use, not by
    'QWebEngineExtensionManager(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWebEngineExtensionManager.
  - Qt tells when it has removed the C++ QWebEngineExtensionManager. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QWebEngineExtensionManager that has no cute function
    yet, '__init__', holds a function that raises 'NotImplementedError', and
    its docstring says why.
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
    Calls Qt's 'QString QWebEngineExtensionManager::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebengineextensionmanager.html#tr

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
    #  QString QWebEngineExtensionManager::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN26QWebEngineExtensionManager2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWebEngineExtensionManager'

  #  A C++ QWebEngineExtensionManager Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QWebEngineExtensionManager'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QWebEngineExtensionManager::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineextensionmanager.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QWebEngineExtensionManager::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK26QWebEngineExtensionManager10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def installPath(self) -> str:
    """
    Calls Qt's 'QString QWebEngineExtensionManager::installPath() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineextensionmanager.html#installPath

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWebEngineExtensionManager::installPath() const
    return self.uglySide.call(
        'ritual_ZNK26QWebEngineExtensionManager11installPathEv',
    )

  def extensions(self) -> QList[QWebEngineExtensionInfo]:
    """
    Calls Qt's 'QList<QWebEngineExtensionInfo>
    QWebEngineExtensionManager::extensions() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineextensionmanager.html#extensions

    Returns
    -------

    QList[QWebEngineExtensionInfo]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QWebEngineExtensionInfo>
    #      QWebEngineExtensionManager::extensions() const
    address = self.uglySide.call(
        'ritual_ZNK26QWebEngineExtensionManager10extensionsEv',
    )
    from . import QWebEngineExtensionInfo
    return QList[QWebEngineExtensionInfo]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QWebEngineExtensionInfo, bool)
  def setExtensionEnabled(
      self,
      extension: QWebEngineExtensionInfo,
      enabled: bool,
  ) -> None:
    """
    Calls Qt's 'void QWebEngineExtensionManager::setExtensionEnabled(const
    QWebEngineExtensionInfo &extension, bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineextensionmanager.html

    Parameters
    ----------

    extension : QWebEngineExtensionInfo
      Passed on as a value: Qt reads the C++ QWebEngineExtensionInfo, which
      stays Python's own.

    enabled : bool
      Passed on as it is.
    """
    #  void QWebEngineExtensionManager::setExtensionEnabled(const
    #      QWebEngineExtensionInfo &extension, bool enabled)
    self.uglySide.call(
        'ritual_ZN26QWebEngineExtensionManager19setExtensionEnabledERK23QWe'
        'bEngineExtensionInfob',
        self._valueOf(extension), enabled,
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
    Qt's 'QWebEngineExtensionManager::QWebEngineExtensionManager(
    QtWebEngineCore::ExtensionManager *d)': names
    'QtWebEngineCore::ExtensionManager', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QWebEngineExtensionManager.__init__' has no cute function yet. "
        "Qt's "
        "'QWebEngineExtensionManager::QWebEngineExtensionManager(QtWebEngine"
        "Core::ExtensionManager *d)': names "
        "'QtWebEngineCore::ExtensionManager', which has no cute class yet.")

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
  def loadExtension(self, path: str) -> None:
    """
    Calls Qt's 'void QWebEngineExtensionManager::loadExtension(const QString
    &path)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineextensionmanager.html#loadExtension

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWebEngineExtensionManager::loadExtension(const QString &path)
    self.uglySide.call(
        'ritual_ZN26QWebEngineExtensionManager13loadExtensionERK7QString',
        path,
    )

  @overload(str)
  def installExtension(self, path: str) -> None:
    """
    Calls Qt's 'void QWebEngineExtensionManager::installExtension(const
    QString &path)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineextensionmanager.html#installExtension

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWebEngineExtensionManager::installExtension(const QString &path)
    self.uglySide.call(
        'ritual_ZN26QWebEngineExtensionManager16installExtensionERK7QString',
        path,
    )

  @overload(QWebEngineExtensionInfo)
  def unloadExtension(self, extension: QWebEngineExtensionInfo) -> None:
    """
    Calls Qt's 'void QWebEngineExtensionManager::unloadExtension(const
    QWebEngineExtensionInfo &extension)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineextensionmanager.html#unloadExtension

    Parameters
    ----------

    extension : QWebEngineExtensionInfo
      Passed on as a value: Qt reads the C++ QWebEngineExtensionInfo, which
      stays Python's own.
    """
    #  void QWebEngineExtensionManager::unloadExtension(const
    #      QWebEngineExtensionInfo &extension)
    self.uglySide.call(
        'ritual_ZN26QWebEngineExtensionManager15unloadExtensionERK23QWebEng'
        'ineExtensionInfo',
        self._valueOf(extension),
    )

  @overload(QWebEngineExtensionInfo)
  def uninstallExtension(self, extension: QWebEngineExtensionInfo) -> None:
    """
    Calls Qt's 'void QWebEngineExtensionManager::uninstallExtension(const
    QWebEngineExtensionInfo &extension)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineextensionmanager.html#uninstallExtension

    Parameters
    ----------

    extension : QWebEngineExtensionInfo
      Passed on as a value: Qt reads the C++ QWebEngineExtensionInfo, which
      stays Python's own.
    """
    #  void QWebEngineExtensionManager::uninstallExtension(const
    #      QWebEngineExtensionInfo &extension)
    self.uglySide.call(
        'ritual_ZN26QWebEngineExtensionManager18uninstallExtensionERK23QWeb'
        'EngineExtensionInfo',
        self._valueOf(extension),
    )

  @overload(QWebEngineExtensionInfo)
  def loadFinished(self, extension: QWebEngineExtensionInfo) -> None:
    """
    Calls Qt's 'void QWebEngineExtensionManager::loadFinished(const
    QWebEngineExtensionInfo &extension)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineextensionmanager.html#loadFinished

    Parameters
    ----------

    extension : QWebEngineExtensionInfo
      Passed on as a value: Qt reads the C++ QWebEngineExtensionInfo, which
      stays Python's own.
    """
    #  void QWebEngineExtensionManager::loadFinished(const
    #      QWebEngineExtensionInfo &extension)
    self.uglySide.call(
        'ritual_ZN26QWebEngineExtensionManager12loadFinishedERK23QWebEngine'
        'ExtensionInfo',
        self._valueOf(extension),
    )

  @overload(QWebEngineExtensionInfo)
  def installFinished(self, extension: QWebEngineExtensionInfo) -> None:
    """
    Calls Qt's 'void QWebEngineExtensionManager::installFinished(const
    QWebEngineExtensionInfo &extension)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineextensionmanager.html#installFinished

    Parameters
    ----------

    extension : QWebEngineExtensionInfo
      Passed on as a value: Qt reads the C++ QWebEngineExtensionInfo, which
      stays Python's own.
    """
    #  void QWebEngineExtensionManager::installFinished(const
    #      QWebEngineExtensionInfo &extension)
    self.uglySide.call(
        'ritual_ZN26QWebEngineExtensionManager15installFinishedERK23QWebEng'
        'ineExtensionInfo',
        self._valueOf(extension),
    )

  @overload(QWebEngineExtensionInfo)
  def unloadFinished(self, extension: QWebEngineExtensionInfo) -> None:
    """
    Calls Qt's 'void QWebEngineExtensionManager::unloadFinished(const
    QWebEngineExtensionInfo &extension)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineextensionmanager.html#unloadFinished

    Parameters
    ----------

    extension : QWebEngineExtensionInfo
      Passed on as a value: Qt reads the C++ QWebEngineExtensionInfo, which
      stays Python's own.
    """
    #  void QWebEngineExtensionManager::unloadFinished(const
    #      QWebEngineExtensionInfo &extension)
    self.uglySide.call(
        'ritual_ZN26QWebEngineExtensionManager14unloadFinishedERK23QWebEngi'
        'neExtensionInfo',
        self._valueOf(extension),
    )

  @overload(QWebEngineExtensionInfo)
  def uninstallFinished(self, extension: QWebEngineExtensionInfo) -> None:
    """
    Calls Qt's 'void QWebEngineExtensionManager::uninstallFinished(const
    QWebEngineExtensionInfo &extension)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineextensionmanager.html#uninstallFinished

    Parameters
    ----------

    extension : QWebEngineExtensionInfo
      Passed on as a value: Qt reads the C++ QWebEngineExtensionInfo, which
      stays Python's own.
    """
    #  void QWebEngineExtensionManager::uninstallFinished(const
    #      QWebEngineExtensionInfo &extension)
    self.uglySide.call(
        'ritual_ZN26QWebEngineExtensionManager17uninstallFinishedERK23QWebE'
        'ngineExtensionInfo',
        self._valueOf(extension),
    )

  @overload(QEvent)
  @overload(NoneType)
  def event(self, e: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QWebEngineExtensionManager::event(QEvent *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineextensionmanager.html#event

    Parameters
    ----------

    e : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QWebEngineExtensionManager::event(QEvent *e)
    ritual = 'ritual_ZN26QWebEngineExtensionManager5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN26QWebEngineExtensionManager5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(e))
