"""
QSSGAssetImportManager binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DAssetImport/6.12.0/QtQuick3DAssetImport/private/qssgassetimportmanager_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGAssetImportManager to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QHash, QList, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QDir, QJsonObject, QMetaObject, QString
  from . import QSSGAssetImporterPluginInfo
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDir = WAIT['QDir']
  QJsonObject = WAIT['QJsonObject']
  QString = WAIT['QString']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSSGAssetImportManager(QObject):
  """
  The cute side of Qt's QSSGAssetImportManager: a plain Python object
  standing in front of one C++ QSSGAssetImportManager.

  It is built on the cute 'QObject', as Qt's QSSGAssetImportManager is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSSGAssetImportManager that has a ritual and that
  Python can call so far, 6 names in all: 'metaObject', 'tr', 'importFile',
  'getOptionsForFile', 'getAllOptions', 'getImporterPluginInfos'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QSSGAssetImportManager::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QSSGAssetImportManager::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QSSGAssetImportManager::~QSSGAssetImportManager()': the destructor:
    Python never removes a C++ QSSGAssetImportManager.
  - Qt's 'ImportState QSSGAssetImportManager::importFile(const QUrl &url,
    QSSGSceneDesc::Scene &scene, QString *error)': takes a type Python has no
    way to hand over yet.
  - Qt's 'ImportState QSSGAssetImportManager::importFile(const QUrl &url,
    QSSGSceneDesc::Scene &scene, const QJsonObject &options, QString
    *error)': takes a type Python has no way to hand over yet.
  - Qt's 'QHash<QString, QStringList>
    QSSGAssetImportManager::getSupportedExtensions() const': gives a type
    Python has no way to take yet.

  What has no ritual
  ------------------

  2 of the 16 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QSSGAssetImportManager is created at the first use, not by
    'QSSGAssetImportManager(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSSGAssetImportManager.
  - Qt tells when it has removed the C++ QSSGAssetImportManager. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QSSGAssetImportManager that has no cute function yet,
    'getSupportedExtensions', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QSSGAssetImportManager, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class ImportState(CuteNum, scoped=True):
    """
    The enum 'QSSGAssetImportManager::ImportState' of Qt, with the 3 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    Success = Kee[int](0)
    IoError = Kee[int](1)
    Unsupported = Kee[int](2)

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
    Calls Qt's 'QString QSSGAssetImportManager::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qssgassetimportmanager.html#tr

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
    #  QString QSSGAssetImportManager::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN22QSSGAssetImportManager2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGAssetImportManager'

  #  A C++ QSSGAssetImportManager Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSSGAssetImportManager'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QSSGAssetImportManager::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgassetimportmanager.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QSSGAssetImportManager::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK22QSSGAssetImportManager10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def getAllOptions(self) -> QHash[str, QJsonObject]:
    """
    Calls Qt's 'PluginOptionMaps QSSGAssetImportManager::getAllOptions()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgassetimportmanager.html#getAllOptions

    Returns
    -------

    QHash[str, QJsonObject]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  PluginOptionMaps QSSGAssetImportManager::getAllOptions() const
    address = self.uglySide.call(
        'ritual_ZNK22QSSGAssetImportManager13getAllOptionsEv',
    )
    from ..QtCore import QJsonObject
    return QHash[str, QJsonObject]._cuteOwning(address)

  def getImporterPluginInfos(self) -> QList[QSSGAssetImporterPluginInfo]:
    """
    Calls Qt's 'QList<QSSGAssetImporterPluginInfo>
    QSSGAssetImportManager::getImporterPluginInfos() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgassetimportmanager.html#getImporterPluginInfos

    Returns
    -------

    QList[QSSGAssetImporterPluginInfo]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QSSGAssetImporterPluginInfo>
    #      QSSGAssetImportManager::getImporterPluginInfos() const
    address = self.uglySide.call(
        'ritual_ZNK22QSSGAssetImportManager22getImporterPluginInfosEv',
    )
    from . import QSSGAssetImporterPluginInfo
    return QList[QSSGAssetImporterPluginInfo]._cuteOwning(address)

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

  @overload()
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QSSGAssetImportManager::QSSGAssetImportManager(QObject *parent)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgassetimportmanager.html#QSSGAssetImportManager

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QSSGAssetImportManager::QSSGAssetImportManager(QObject *parent)
    self._noteCreation(QSSGAssetImportManager, lambda: Rituals.call(
        'ritual_ZN22QSSGAssetImportManagerC1EP7QObject',
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

  @overload(str, QDir)
  @overload(str, QDir, QString)
  @overload(str, QDir, NoneType)
  def importFile(
      self,
      filename: str,
      outputPath: QDir,
      error: Optional[QString] = None,
  ) -> ImportState:
    """
    Calls Qt's 'ImportState QSSGAssetImportManager::importFile(const QString
    &filename, const QDir &outputPath, QString *error)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgassetimportmanager.html#importFile

    Parameters
    ----------

    filename : str
      Passed on as it is: a QString is made of it for the call.

    outputPath : QDir
      Passed on as a value: Qt reads the C++ QDir, which stays Python's own.

    error : Optional[QString]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    ImportState
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ImportState(number)'
      gives.
    """
    #  ImportState QSSGAssetImportManager::importFile(const QString
    #      &filename, const QDir &outputPath, QString *error)
    return QSSGAssetImportManager.ImportState(self.uglySide.call(
        'ritual_ZN22QSSGAssetImportManager10importFileERK7QStringRK4QDirPS0'
        '_',
        filename, self._valueOf(outputPath), self._addressOf(error),
    ))

  @overload(str, QDir, QJsonObject)
  @overload(str, QDir, QJsonObject, QString)
  @overload(str, QDir, QJsonObject, NoneType)
  def importFile(
      self,
      filename: str,
      outputPath: QDir,
      options: Optional[QJsonObject] = None,
      error: Optional[QString] = None,
  ) -> ImportState:
    """
    Calls Qt's 'ImportState QSSGAssetImportManager::importFile(const QString
    &filename, const QDir &outputPath, const QJsonObject &options, QString
    *error)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgassetimportmanager.html#importFile

    Parameters
    ----------

    filename : str
      Passed on as it is: a QString is made of it for the call.

    outputPath : QDir
      Passed on as a value: Qt reads the C++ QDir, which stays Python's own.

    options : Optional[QJsonObject]
      Passed on as a value: Qt reads the C++ QJsonObject, which stays
      Python's own. May be left out, as in Qt: a new 'QJsonObject()' is then
      passed on.

    error : Optional[QString]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    ImportState
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ImportState(number)'
      gives.
    """
    #  ImportState QSSGAssetImportManager::importFile(const QString
    #      &filename, const QDir &outputPath, const QJsonObject &options,
    #      QString *error)
    if options is None:
      from ..QtCore import QJsonObject
      options = QJsonObject()
    return QSSGAssetImportManager.ImportState(self.uglySide.call(
        'ritual_ZN22QSSGAssetImportManager10importFileERK7QStringRK4QDirRK1'
        '1QJsonObjectPS0_',
        filename, self._valueOf(outputPath), self._valueOf(options),
        self._addressOf(error),
    ))

  @overload(str)
  def getOptionsForFile(self, filename: str) -> QJsonObject:
    """
    Calls Qt's 'QJsonObject QSSGAssetImportManager::getOptionsForFile(const
    QString &filename)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgassetimportmanager.html#getOptionsForFile

    Parameters
    ----------

    filename : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QJsonObject
      A new cute QJsonObject around the copy Qt gave back. Python owns it.
    """
    #  QJsonObject QSSGAssetImportManager::getOptionsForFile(const QString
    #      &filename)
    address = self.uglySide.call(
        'ritual_ZN22QSSGAssetImportManager17getOptionsForFileERK7QString',
        filename,
    )
    from ..QtCore import QJsonObject
    return QJsonObject._cuteOwning(address)

  @staticmethod
  def getSupportedExtensions(*__, **_) -> Never:
    """
    Qt's 'QHash<QString, QStringList>
    QSSGAssetImportManager::getSupportedExtensions() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSSGAssetImportManager.getSupportedExtensions' has no cute "
        "function yet. Qt's 'QHash<QString, QStringList> "
        "QSSGAssetImportManager::getSupportedExtensions() const': gives a "
        "type Python has no way to take yet.")
