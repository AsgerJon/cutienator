"""
QQmlPluginImporter binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlpluginimporter_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQmlPluginImporter to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QQmlPluginImporter(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlPluginImporter: a plain Python object standing in
  front of one C++ QQmlPluginImporter.

  What exists
  -----------

  Every function of Qt's QQmlPluginImporter that has a ritual and that Python
  can call so far, 1 name in all: 'truncateToDirectory'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlPluginImporter::QQmlPluginImporter(const QString &uri,
    QTypeRevision version, const QQmlTypeLoaderQmldirContent *qmldir,
    QQmlTypeLoader *typeLoader, QList<QQmlError> *errors)': names
    'QList<QQmlError>', which has no cute class yet.
  - Qt's 'QQmlPluginImporter::~QQmlPluginImporter()': the destructor: Python
    never removes a C++ QQmlPluginImporter.

  What has no ritual
  ------------------

  11 of the 14 functions Qt declares: 5 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 4 forbidden;
  1 leans on 'lcQmlImport()', which Qt's source does not mark for use from
  outside Qt and has no code for that could be taken; 1 leans on 'QQmlThread.

  What to expect
  --------------

  - The C++ QQmlPluginImporter is created at the first use, not by
    'QQmlPluginImporter(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlPluginImporter.
  - Each name of Qt's QQmlPluginImporter that has no cute function yet,
    '__init__', 'finalizePlugin', 'importDynamicPlugin', 'importPlugins',
    'importStaticPlugin', 'plugins', 'removePlugin', 'resolvePlugin', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  def truncateToDirectory(qmldirFilePath: str) -> str:
    """
    Calls Qt's 'QString QQmlPluginImporter::truncateToDirectory(const QString
    &qmldirFilePath)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpluginimporter.html#truncateToDirectory

    Parameters
    ----------

    qmldirFilePath : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlPluginImporter::truncateToDirectory(const QString
    #      &qmldirFilePath)
    return Rituals.call(
        'ritual_ZN18QQmlPluginImporter19truncateToDirectoryERK7QString',
        qmldirFilePath,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlPluginImporter'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
    Qt's 'QQmlPluginImporter::QQmlPluginImporter(const QString &uri,
    QTypeRevision version, const QQmlTypeLoaderQmldirContent *qmldir,
    QQmlTypeLoader *typeLoader, QList<QQmlError> *errors)': names
    'QList<QQmlError>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQmlPluginImporter.__init__' has no cute function yet. Qt's "
        "'QQmlPluginImporter::QQmlPluginImporter(const QString &uri, "
        "QTypeRevision version, const QQmlTypeLoaderQmldirContent *qmldir, "
        "QQmlTypeLoader *typeLoader, QList<QQmlError> *errors)': names "
        "'QList<QQmlError>', which has no cute class yet.")

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

  @staticmethod
  def finalizePlugin(*__, **_) -> Never:
    """
    Qt's 'void QQmlPluginImporter::finalizePlugin(QObject *instance, const
    QString &path)': leans on 'QQmlThread::isThisThread() const', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QQmlPluginImporter.finalizePlugin' has no cute function yet. Qt's "
        "'void QQmlPluginImporter::finalizePlugin(QObject *instance, const "
        "QString &path)': leans on 'QQmlThread::isThisThread() const', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def importDynamicPlugin(*__, **_) -> Never:
    """
    Qt's 'QTypeRevision QQmlPluginImporter::importDynamicPlugin(const QString
    &filePath, const QString &pluginId, bool optional)': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: unknown type name 'QmlPlugin'.
    """
    raise NotImplementedError(
        "'QQmlPluginImporter.importDynamicPlugin' has no cute function yet. "
        "Qt's 'QTypeRevision QQmlPluginImporter::importDynamicPlugin(const "
        "QString &filePath, const QString &pluginId, bool optional)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: unknown type name 'QmlPlugin'.")

  @staticmethod
  def importPlugins(*__, **_) -> Never:
    """
    Qt's 'QTypeRevision QQmlPluginImporter::importPlugins()': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: use of undeclared identifier
    'staticQmlPluginsMatchingURI'.
    """
    raise NotImplementedError(
        "'QQmlPluginImporter.importPlugins' has no cute function yet. Qt's "
        "'QTypeRevision QQmlPluginImporter::importPlugins()': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier "
        "'staticQmlPluginsMatchingURI'.")

  @staticmethod
  def importStaticPlugin(*__, **_) -> Never:
    """
    Qt's 'QTypeRevision QQmlPluginImporter::importStaticPlugin(QObject
    *instance, const QString &pluginId)': Qt's library has no name for it,
    and its code in Qt's source does not compile apart from its file: unknown
    type name 'PluginMapPtr'.
    """
    raise NotImplementedError(
        "'QQmlPluginImporter.importStaticPlugin' has no cute function yet. "
        "Qt's 'QTypeRevision QQmlPluginImporter::importStaticPlugin(QObject "
        "*instance, const QString &pluginId)': Qt's library has no name for "
        "it, and its code in Qt's source does not compile apart from its "
        "file: unknown type name 'PluginMapPtr'.")

  @staticmethod
  def plugins(*__, **_) -> Never:
    """
    Qt's 'QStringList QQmlPluginImporter::plugins()': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: unknown type name 'PluginMapPtr'.
    """
    raise NotImplementedError(
        "'QQmlPluginImporter.plugins' has no cute function yet. Qt's "
        "'QStringList QQmlPluginImporter::plugins()': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: unknown type name 'PluginMapPtr'.")

  @staticmethod
  def removePlugin(*__, **_) -> Never:
    """
    Qt's 'bool QQmlPluginImporter::removePlugin(const QString &pluginId)':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: unknown type name 'PluginMapPtr'.
    """
    raise NotImplementedError(
        "'QQmlPluginImporter.removePlugin' has no cute function yet. Qt's "
        "'bool QQmlPluginImporter::removePlugin(const QString &pluginId)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: unknown type name 'PluginMapPtr'.")

  @staticmethod
  def resolvePlugin(*__, **_) -> Never:
    """
    Qt's 'QString QQmlPluginImporter::resolvePlugin(const QString
    &qmldirPluginPath, const QString &baseName)': leans on 'lcQmlImport()',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QQmlPluginImporter.resolvePlugin' has no cute function yet. Qt's "
        "'QString QQmlPluginImporter::resolvePlugin(const QString "
        "&qmldirPluginPath, const QString &baseName)': leans on "
        "'lcQmlImport()', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")
