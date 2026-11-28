"""
QDesignerPluginManager binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/pluginmanager_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QDesignerPluginManager to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtUiPlugin import QDesignerCustomWidgetInterface
  from . import QDesignerCustomWidgetData, QDesignerFormEditorInterface
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDesignerCustomWidgetInterface = WAIT['QDesignerCustomWidgetInterface']
  QDesignerFormEditorInterface = WAIT['QDesignerFormEditorInterface']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDesignerPluginManager(QObject):
  """
  The cute side of Qt's QDesignerPluginManager: a plain Python object
  standing in front of one C++ QDesignerPluginManager.

  It is built on the cute 'QObject', as Qt's QDesignerPluginManager is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QDesignerPluginManager that has a ritual and that
  Python can call so far, 22 names in all: 'metaObject', 'tr', 'core',
  'instance', 'registeredPlugins', 'findPlugins', 'pluginPaths',
  'setPluginPaths', 'disabledPlugins', 'setDisabledPlugins', 'failedPlugins',
  'failureReason', 'instances', 'registeredCustomWidgets',
  'customWidgetData', 'registerNewPlugins', 'defaultPluginPaths',
  'syncSettings', 'ensureInitialized', 'updateRegisteredPlugins',
  'registerPath', 'registerPlugin'. It can be made from Python, in 2 ways;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QDesignerPluginManager::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QDesignerPluginManager::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QDesignerPluginManager::~QDesignerPluginManager()': the destructor:
    Python never removes a C++ QDesignerPluginManager.

  What has no ritual
  ------------------

  2 of the 30 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QDesignerPluginManager is created at the first use, not by
    'QDesignerPluginManager(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDesignerPluginManager.
  - Qt tells when it has removed the C++ QDesignerPluginManager. Every call
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
    Calls Qt's 'QString QDesignerPluginManager::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qdesignerpluginmanager.html#tr

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
    #  QString QDesignerPluginManager::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN22QDesignerPluginManager2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def defaultPluginPaths() -> QStringList:
    """
    Calls Qt's 'QStringList QDesignerPluginManager::defaultPluginPaths()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerpluginmanager.html#defaultPluginPaths

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QDesignerPluginManager::defaultPluginPaths()
    address = Rituals.call(
        'ritual_ZN22QDesignerPluginManager18defaultPluginPathsEv',
    )
    return QStringList._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDesignerPluginManager'

  #  A C++ QDesignerPluginManager Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDesignerPluginManager'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QDesignerPluginManager::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerpluginmanager.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QDesignerPluginManager::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK22QDesignerPluginManager10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def core(self) -> Optional[QDesignerFormEditorInterface]:
    """
    Calls Qt's 'QDesignerFormEditorInterface *QDesignerPluginManager::core()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qdesignerpluginmanager.html#core

    Returns
    -------

    Optional[QDesignerFormEditorInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDesignerFormEditorInterface *QDesignerPluginManager::core() const
    address = self.uglySide.call('ritual_ZNK22QDesignerPluginManager4coreEv')
    from . import QDesignerFormEditorInterface
    return QDesignerFormEditorInterface._cuteAt(address)

  @overload(str)
  def instance(self, plugin: str) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QDesignerPluginManager::instance(const QString
    &plugin) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerpluginmanager.html#instance

    Parameters
    ----------

    plugin : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QDesignerPluginManager::instance(const QString &plugin) const
    address = self.uglySide.call(
        'ritual_ZNK22QDesignerPluginManager8instanceERK7QString', plugin,
    )
    return QObject._cuteAt(address)

  def registeredPlugins(self) -> QStringList:
    """
    Calls Qt's 'QStringList QDesignerPluginManager::registeredPlugins()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerpluginmanager.html#registeredPlugins

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QDesignerPluginManager::registeredPlugins() const
    address = self.uglySide.call(
        'ritual_ZNK22QDesignerPluginManager17registeredPluginsEv',
    )
    return QStringList._cuteOwning(address)

  def pluginPaths(self) -> QStringList:
    """
    Calls Qt's 'QStringList QDesignerPluginManager::pluginPaths() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerpluginmanager.html#pluginPaths

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QDesignerPluginManager::pluginPaths() const
    address = self.uglySide.call(
        'ritual_ZNK22QDesignerPluginManager11pluginPathsEv',
    )
    return QStringList._cuteOwning(address)

  def disabledPlugins(self) -> QStringList:
    """
    Calls Qt's 'QStringList QDesignerPluginManager::disabledPlugins() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerpluginmanager.html#disabledPlugins

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QDesignerPluginManager::disabledPlugins() const
    address = self.uglySide.call(
        'ritual_ZNK22QDesignerPluginManager15disabledPluginsEv',
    )
    return QStringList._cuteOwning(address)

  def failedPlugins(self) -> QStringList:
    """
    Calls Qt's 'QStringList QDesignerPluginManager::failedPlugins() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerpluginmanager.html#failedPlugins

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QDesignerPluginManager::failedPlugins() const
    address = self.uglySide.call(
        'ritual_ZNK22QDesignerPluginManager13failedPluginsEv',
    )
    return QStringList._cuteOwning(address)

  @overload(str)
  def failureReason(self, pluginName: str) -> str:
    """
    Calls Qt's 'QString QDesignerPluginManager::failureReason(const QString
    &pluginName) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerpluginmanager.html#failureReason

    Parameters
    ----------

    pluginName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDesignerPluginManager::failureReason(const QString
    #      &pluginName) const
    return self.uglySide.call(
        'ritual_ZNK22QDesignerPluginManager13failureReasonERK7QString',
        pluginName,
    )

  def instances(self) -> QList[QObject]:
    """
    Calls Qt's 'QObjectList QDesignerPluginManager::instances() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerpluginmanager.html#instances

    Returns
    -------

    QList[QObject]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QObjectList QDesignerPluginManager::instances() const
    address = self.uglySide.call(
        'ritual_ZNK22QDesignerPluginManager9instancesEv',
    )
    return QList[QObject]._cuteOwning(address)

  def registeredCustomWidgets(self) -> QList[QDesignerCustomWidgetInterface]:
    """
    Calls Qt's 'CustomWidgetList
    QDesignerPluginManager::registeredCustomWidgets() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerpluginmanager.html

    Returns
    -------

    QList[QDesignerCustomWidgetInterface]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  CustomWidgetList QDesignerPluginManager::registeredCustomWidgets()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK22QDesignerPluginManager23registeredCustomWidgetsEv',
    )
    from ..QtUiPlugin import QDesignerCustomWidgetInterface
    return QList[QDesignerCustomWidgetInterface]._cuteOwning(address)

  @overload(QDesignerCustomWidgetInterface)
  @overload(NoneType)
  def customWidgetData(
      self,
      w: Optional[QDesignerCustomWidgetInterface],
  ) -> QDesignerCustomWidgetData:
    """
    Calls Qt's 'QDesignerCustomWidgetData
    QDesignerPluginManager::customWidgetData(QDesignerCustomWidgetInterface
    *w) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerpluginmanager.html#customWidgetData

    Parameters
    ----------

    w : Optional[QDesignerCustomWidgetInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QDesignerCustomWidgetData
      A new cute QDesignerCustomWidgetData around the copy Qt gave back.
      Python owns it.
    """
    #  QDesignerCustomWidgetData QDesignerPluginManager::customWidgetData(
    #      QDesignerCustomWidgetInterface *w) const
    address = self.uglySide.call(
        'ritual_ZNK22QDesignerPluginManager16customWidgetDataEP30QDesignerC'
        'ustomWidgetInterface',
        self._addressOf(w),
    )
    from . import QDesignerCustomWidgetData
    return QDesignerCustomWidgetData._cuteOwning(address)

  @overload(str)
  def customWidgetData(self, className: str) -> QDesignerCustomWidgetData:
    """
    Calls Qt's 'QDesignerCustomWidgetData
    QDesignerPluginManager::customWidgetData(const QString &className)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerpluginmanager.html#customWidgetData

    Parameters
    ----------

    className : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QDesignerCustomWidgetData
      A new cute QDesignerCustomWidgetData around the copy Qt gave back.
      Python owns it.
    """
    #  QDesignerCustomWidgetData
    #      QDesignerPluginManager::customWidgetData(const QString &className)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK22QDesignerPluginManager16customWidgetDataERK7QString',
        className,
    )
    from . import QDesignerCustomWidgetData
    return QDesignerCustomWidgetData._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QStringList)
  def setPluginPaths(self, plugin_paths: QStringList) -> None:
    """
    Calls Qt's 'void QDesignerPluginManager::setPluginPaths(const QStringList
    &plugin_paths)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerpluginmanager.html#setPluginPaths

    Parameters
    ----------

    plugin_paths : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QDesignerPluginManager::setPluginPaths(const QStringList
    #      &plugin_paths)
    self.uglySide.call(
        'ritual_ZN22QDesignerPluginManager14setPluginPathsERK5QListI7QStrin'
        'gE',
        self._valueOf(plugin_paths),
    )

  @overload(QStringList)
  def setDisabledPlugins(self, disabled_plugins: QStringList) -> None:
    """
    Calls Qt's 'void QDesignerPluginManager::setDisabledPlugins(const
    QStringList &disabled_plugins)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerpluginmanager.html#setDisabledPlugins

    Parameters
    ----------

    disabled_plugins : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QDesignerPluginManager::setDisabledPlugins(const QStringList
    #      &disabled_plugins)
    self.uglySide.call(
        'ritual_ZN22QDesignerPluginManager18setDisabledPluginsERK5QListI7QS'
        'tringE',
        self._valueOf(disabled_plugins),
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

  @overload(QDesignerFormEditorInterface)
  @overload(NoneType)
  def __init__(self, core: Optional[QDesignerFormEditorInterface]) -> None:
    """
    Notes what was given, for Qt's
    'QDesignerPluginManager::QDesignerPluginManager(
    QDesignerFormEditorInterface *core)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerpluginmanager.html#QDesignerPluginManager

    Parameters
    ----------

    core : Optional[QDesignerFormEditorInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QDesignerPluginManager::QDesignerPluginManager(
    #      QDesignerFormEditorInterface *core)
    self._noteCreation(QDesignerPluginManager, lambda: Rituals.call(
        'ritual_ZN22QDesignerPluginManagerC1EP28QDesignerFormEditorInterfac'
        'e',
        self._addressOf(core),
    ))

  @overload(QStringList, QDesignerFormEditorInterface)
  @overload(QStringList, NoneType)
  def __init__(
      self,
      pluginPaths: QStringList,
      core: Optional[QDesignerFormEditorInterface],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QDesignerPluginManager::QDesignerPluginManager(const QStringList
    &pluginPaths, QDesignerFormEditorInterface *core)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerpluginmanager.html#QDesignerPluginManager

    Parameters
    ----------

    pluginPaths : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    core : Optional[QDesignerFormEditorInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QDesignerPluginManager::QDesignerPluginManager(const QStringList
    #      &pluginPaths, QDesignerFormEditorInterface *core)
    self._noteCreation(QDesignerPluginManager, lambda: Rituals.call(
        'ritual_ZN22QDesignerPluginManagerC1ERK5QListI7QStringEP28QDesigner'
        'FormEditorInterface',
        self._valueOf(pluginPaths), self._addressOf(core),
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
  def findPlugins(self, path: str) -> QStringList:
    """
    Calls Qt's 'QStringList QDesignerPluginManager::findPlugins(const QString
    &path)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerpluginmanager.html#findPlugins

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QDesignerPluginManager::findPlugins(const QString &path)
    address = self.uglySide.call(
        'ritual_ZN22QDesignerPluginManager11findPluginsERK7QString', path,
    )
    return QStringList._cuteOwning(address)

  def registerNewPlugins(self) -> bool:
    """
    Calls Qt's 'bool QDesignerPluginManager::registerNewPlugins()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerpluginmanager.html#registerNewPlugins
    """
    #  bool QDesignerPluginManager::registerNewPlugins()
    return self.uglySide.call(
        'ritual_ZN22QDesignerPluginManager18registerNewPluginsEv',
    )

  def syncSettings(self) -> bool:
    """
    Calls Qt's 'bool QDesignerPluginManager::syncSettings()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerpluginmanager.html#syncSettings
    """
    #  bool QDesignerPluginManager::syncSettings()
    return self.uglySide.call(
        'ritual_ZN22QDesignerPluginManager12syncSettingsEv',
    )

  def ensureInitialized(self) -> None:
    """
    Calls Qt's 'void QDesignerPluginManager::ensureInitialized()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerpluginmanager.html#ensureInitialized
    """
    #  void QDesignerPluginManager::ensureInitialized()
    self.uglySide.call(
        'ritual_ZN22QDesignerPluginManager17ensureInitializedEv',
    )

  def updateRegisteredPlugins(self) -> None:
    """
    Calls Qt's 'void QDesignerPluginManager::updateRegisteredPlugins()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerpluginmanager.html
    """
    #  void QDesignerPluginManager::updateRegisteredPlugins()
    self.uglySide.call(
        'ritual_ZN22QDesignerPluginManager23updateRegisteredPluginsEv',
    )

  @overload(str)
  def registerPath(self, path: str) -> None:
    """
    Calls Qt's 'void QDesignerPluginManager::registerPath(const QString
    &path)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerpluginmanager.html#registerPath

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDesignerPluginManager::registerPath(const QString &path)
    self.uglySide.call(
        'ritual_ZN22QDesignerPluginManager12registerPathERK7QString', path,
    )

  @overload(str)
  def registerPlugin(self, plugin: str) -> None:
    """
    Calls Qt's 'void QDesignerPluginManager::registerPlugin(const QString
    &plugin)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerpluginmanager.html#registerPlugin

    Parameters
    ----------

    plugin : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDesignerPluginManager::registerPlugin(const QString &plugin)
    self.uglySide.call(
        'ritual_ZN22QDesignerPluginManager14registerPluginERK7QString',
        plugin,
    )
