"""
QUiLoader binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtUiTools/quiloader.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QDir, QIODevice, QMetaObject
  from ..QtGui import QAction, QActionGroup
  from ..QtWidgets import QLayout, QWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDir = WAIT['QDir']
  QIODevice = WAIT['QIODevice']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QUiLoader(QObject):
  """
  The cute side of Qt's QUiLoader: a plain Python object standing in front of
  one C++ QUiLoader.

  It is built on the cute 'QObject', as Qt's QUiLoader is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QUiLoader that has a ritual and that Python can call
  so far, 19 names in all: 'metaObject', 'tr', 'pluginPaths',
  'clearPluginPaths', 'addPluginPath', 'load', 'availableWidgets',
  'availableLayouts', 'createWidget', 'createLayout', 'createActionGroup',
  'createAction', 'setWorkingDirectory', 'workingDirectory',
  'setLanguageChangeEnabled', 'isLanguageChangeEnabled',
  'setTranslationEnabled', 'isTranslationEnabled', 'errorString'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QUiLoader::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QUiLoader::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QUiLoader::~QUiLoader()': the destructor: Python never removes a
    C++ QUiLoader.
  - Qt's 'QUiLoaderPrivate *QUiLoader::d_func()': gives 'QUiLoaderPrivate',
    which has no cute class yet.
  - Qt's 'const QUiLoaderPrivate *QUiLoader::d_func() const': gives
    'QUiLoaderPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  6 of the 31 functions Qt declares: 4 forbidden; 2 not a gap.

  What to expect
  --------------

  - The C++ QUiLoader is created at the first use, not by 'QUiLoader(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QUiLoader.
  - Qt tells when it has removed the C++ QUiLoader. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
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
    Calls Qt's 'QString QUiLoader::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/quiloader.html#tr

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
    #  QString QUiLoader::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN9QUiLoader2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QUiLoader'

  #  A C++ QUiLoader Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QUiLoader'

  #  The functions Qt calls itself that QUiLoader is the first to declare. A
  #  class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'createWidget': (
          ('_ZN9QUiLoader12createWidgetERK7QStringP7QWidgetS2_',
           ('address', 'address', 'QtWidgets:QWidget'),
           (
               ('address', 'text', ''),
               ('address', 'address', 'QtWidgets:QWidget'),
               ('address', 'text', ''),
           )),
      ),
      'createLayout': (
          ('_ZN9QUiLoader12createLayoutERK7QStringP7QObjectS2_',
           ('address', 'address', 'QtWidgets:QLayout'),
           (
               ('address', 'text', ''),
               ('address', 'address', 'QtCore:QObject'),
               ('address', 'text', ''),
           )),
      ),
      'createActionGroup': (
          ('_ZN9QUiLoader17createActionGroupEP7QObjectRK7QString',
           ('address', 'address', 'QtGui:QActionGroup'),
           (
               ('address', 'address', 'QtCore:QObject'),
               ('address', 'text', ''),
           )),
      ),
      'createAction': (
          ('_ZN9QUiLoader12createActionEP7QObjectRK7QString',
           ('address', 'address', 'QtGui:QAction'),
           (
               ('address', 'address', 'QtCore:QObject'),
               ('address', 'text', ''),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QUiLoader::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/quiloader.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QUiLoader::metaObject() const
    address = self.uglySide.call('ritual_ZNK9QUiLoader10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def pluginPaths(self) -> QStringList:
    """
    Calls Qt's 'QStringList QUiLoader::pluginPaths() const'.

    Qt's own words: https://doc.qt.io/qt-6/quiloader.html#pluginPaths

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QUiLoader::pluginPaths() const
    address = self.uglySide.call('ritual_ZNK9QUiLoader11pluginPathsEv')
    return QStringList._cuteOwning(address)

  def availableWidgets(self) -> QStringList:
    """
    Calls Qt's 'QStringList QUiLoader::availableWidgets() const'.

    Qt's own words: https://doc.qt.io/qt-6/quiloader.html#availableWidgets

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QUiLoader::availableWidgets() const
    address = self.uglySide.call('ritual_ZNK9QUiLoader16availableWidgetsEv')
    return QStringList._cuteOwning(address)

  def availableLayouts(self) -> QStringList:
    """
    Calls Qt's 'QStringList QUiLoader::availableLayouts() const'.

    Qt's own words: https://doc.qt.io/qt-6/quiloader.html#availableLayouts

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QUiLoader::availableLayouts() const
    address = self.uglySide.call('ritual_ZNK9QUiLoader16availableLayoutsEv')
    return QStringList._cuteOwning(address)

  def workingDirectory(self) -> QDir:
    """
    Calls Qt's 'QDir QUiLoader::workingDirectory() const'.

    Qt's own words: https://doc.qt.io/qt-6/quiloader.html#workingDirectory

    Returns
    -------

    QDir
      A new cute QDir around the copy Qt gave back. Python owns it.
    """
    #  QDir QUiLoader::workingDirectory() const
    address = self.uglySide.call('ritual_ZNK9QUiLoader16workingDirectoryEv')
    from ..QtCore import QDir
    return QDir._cuteOwning(address)

  def isLanguageChangeEnabled(self) -> bool:
    """
    Calls Qt's 'bool QUiLoader::isLanguageChangeEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/quiloader.html#isLanguageChangeEnabled
    """
    #  bool QUiLoader::isLanguageChangeEnabled() const
    return self.uglySide.call(
        'ritual_ZNK9QUiLoader23isLanguageChangeEnabledEv',
    )

  def isTranslationEnabled(self) -> bool:
    """
    Calls Qt's 'bool QUiLoader::isTranslationEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/quiloader.html#isTranslationEnabled
    """
    #  bool QUiLoader::isTranslationEnabled() const
    return self.uglySide.call('ritual_ZNK9QUiLoader20isTranslationEnabledEv')

  def errorString(self) -> str:
    """
    Calls Qt's 'QString QUiLoader::errorString() const'.

    Qt's own words: https://doc.qt.io/qt-6/quiloader.html#errorString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QUiLoader::errorString() const
    return self.uglySide.call('ritual_ZNK9QUiLoader11errorStringEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QDir)
  def setWorkingDirectory(self, dir: QDir) -> None:
    """
    Calls Qt's 'void QUiLoader::setWorkingDirectory(const QDir &dir)'.

    Qt's own words: https://doc.qt.io/qt-6/quiloader.html#setWorkingDirectory

    Parameters
    ----------

    dir : QDir
      Passed on as a value: Qt reads the C++ QDir, which stays Python's own.
    """
    #  void QUiLoader::setWorkingDirectory(const QDir &dir)
    self.uglySide.call(
        'ritual_ZN9QUiLoader19setWorkingDirectoryERK4QDir',
        self._valueOf(dir),
    )

  @overload(bool)
  def setLanguageChangeEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QUiLoader::setLanguageChangeEnabled(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/quiloader.html#setLanguageChangeEnabled

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QUiLoader::setLanguageChangeEnabled(bool enabled)
    self.uglySide.call(
        'ritual_ZN9QUiLoader24setLanguageChangeEnabledEb', enabled,
    )

  @overload(bool)
  def setTranslationEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QUiLoader::setTranslationEnabled(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/quiloader.html#setTranslationEnabled

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QUiLoader::setTranslationEnabled(bool enabled)
    self.uglySide.call(
        'ritual_ZN9QUiLoader21setTranslationEnabledEb', enabled,
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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's 'QUiLoader::QUiLoader(QObject *parent)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/quiloader.html#QUiLoader

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QUiLoader::QUiLoader(QObject *parent)
    self._noteCreation(QUiLoader, lambda: Rituals.call(
        'ritual_ZN9QUiLoaderC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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

  def clearPluginPaths(self) -> None:
    """
    Calls Qt's 'void QUiLoader::clearPluginPaths()'.

    Qt's own words: https://doc.qt.io/qt-6/quiloader.html#clearPluginPaths
    """
    #  void QUiLoader::clearPluginPaths()
    self.uglySide.call('ritual_ZN9QUiLoader16clearPluginPathsEv')

  @overload(str)
  def addPluginPath(self, path: str) -> None:
    """
    Calls Qt's 'void QUiLoader::addPluginPath(const QString &path)'.

    Qt's own words: https://doc.qt.io/qt-6/quiloader.html#addPluginPath

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QUiLoader::addPluginPath(const QString &path)
    self.uglySide.call('ritual_ZN9QUiLoader13addPluginPathERK7QString', path)

  @overload(QIODevice)
  @overload(NoneType)
  @overload(QIODevice, QWidget)
  @overload(QIODevice, NoneType)
  @overload(NoneType, QWidget)
  @overload(NoneType, NoneType)
  def load(
      self,
      device: Optional[QIODevice],
      parentWidget: Optional[QWidget] = None,
  ) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QUiLoader::load(QIODevice *device, QWidget
    *parentWidget)'.

    Qt's own words: https://doc.qt.io/qt-6/quiloader.html#load

    Parameters
    ----------

    device : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parentWidget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QUiLoader::load(QIODevice *device, QWidget *parentWidget)
    address = self.uglySide.call(
        'ritual_ZN9QUiLoader4loadEP9QIODeviceP7QWidget',
        self._addressOf(device), self._addressOf(parentWidget),
    )
    from ..QtWidgets import QWidget
    return QWidget._cuteAt(address)

  @overload(str)
  @overload(str, QWidget)
  @overload(str, NoneType)
  @overload(str, QWidget, str)
  @overload(str, NoneType, str)
  def createWidget(
      self,
      className: str,
      parent: Optional[QWidget] = None,
      name: str = '',
  ) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QUiLoader::createWidget(const QString &className,
    QWidget *parent, const QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/quiloader.html#createWidget

    Parameters
    ----------

    className : str
      Passed on as it is: a QString is made of it for the call.

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    name : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QUiLoader::createWidget(const QString &className, QWidget
    #      *parent, const QString &name)
    ritual = 'ritual_ZN9QUiLoader12createWidgetERK7QStringP7QWidgetS2_'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN9QUiLoader12createWidgetERK7QStringP7QWidgetS2_'
    address = self.uglySide.call(
        ritual, className, self._addressOf(parent), name,
    )
    from ..QtWidgets import QWidget
    return QWidget._cuteAt(address)

  @overload(str)
  @overload(str, QObject)
  @overload(str, NoneType)
  @overload(str, QObject, str)
  @overload(str, NoneType, str)
  def createLayout(
      self,
      className: str,
      parent: Optional[QObject] = None,
      name: str = '',
  ) -> Optional[QLayout]:
    """
    Calls Qt's 'QLayout *QUiLoader::createLayout(const QString &className,
    QObject *parent, const QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/quiloader.html#createLayout

    Parameters
    ----------

    className : str
      Passed on as it is: a QString is made of it for the call.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    name : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    Returns
    -------

    Optional[QLayout]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLayout *QUiLoader::createLayout(const QString &className, QObject
    #      *parent, const QString &name)
    ritual = 'ritual_ZN9QUiLoader12createLayoutERK7QStringP7QObjectS2_'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN9QUiLoader12createLayoutERK7QStringP7QObjectS2_'
    address = self.uglySide.call(
        ritual, className, self._addressOf(parent, 'QObject'), name,
    )
    from ..QtWidgets import QLayout
    return QLayout._cuteAt(address)

  @overload()
  @overload(QObject)
  @overload(NoneType)
  @overload(QObject, str)
  @overload(NoneType, str)
  def createActionGroup(
      self,
      parent: Optional[QObject] = None,
      name: str = '',
  ) -> Optional[QActionGroup]:
    """
    Calls Qt's 'QActionGroup *QUiLoader::createActionGroup(QObject *parent,
    const QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/quiloader.html#createActionGroup

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    name : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    Returns
    -------

    Optional[QActionGroup]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QActionGroup *QUiLoader::createActionGroup(QObject *parent, const
    #      QString &name)
    ritual = 'ritual_ZN9QUiLoader17createActionGroupEP7QObjectRK7QString'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN9QUiLoader17createActionGroupEP7QObjectRK7QString')
    address = self.uglySide.call(
        ritual, self._addressOf(parent, 'QObject'), name,
    )
    from ..QtGui import QActionGroup
    return QActionGroup._cuteAt(address)

  @overload()
  @overload(QObject)
  @overload(NoneType)
  @overload(QObject, str)
  @overload(NoneType, str)
  def createAction(
      self,
      parent: Optional[QObject] = None,
      name: str = '',
  ) -> Optional[QAction]:
    """
    Calls Qt's 'QAction *QUiLoader::createAction(QObject *parent, const
    QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/quiloader.html#createAction

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    name : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    Returns
    -------

    Optional[QAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAction *QUiLoader::createAction(QObject *parent, const QString &name)
    ritual = 'ritual_ZN9QUiLoader12createActionEP7QObjectRK7QString'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN9QUiLoader12createActionEP7QObjectRK7QString'
    address = self.uglySide.call(
        ritual, self._addressOf(parent, 'QObject'), name,
    )
    from ..QtGui import QAction
    return QAction._cuteAt(address)
