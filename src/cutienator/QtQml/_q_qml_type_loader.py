"""
QQmlTypeLoader binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmltypeloader_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQmlTypeLoader to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList, QStringList
from . import QQmlAbstractUrlInterceptor, QQmlImports, QQmlMetaType, QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QObject, QString, QUrl
  from . import QQmlEngineExtensionInterface, QQmlExtensionInterface
  from . import QQmlNetworkAccessManagerFactory, QQmlProfiler
  from . import QQmlTypeLoaderQmldirContent, QQmlTypeLoaderThread
  from ..QtNetwork import QNetworkAccessManager, QNetworkReply
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QNetworkReply = WAIT['QNetworkReply']
  QObject = WAIT['QObject']
  QQmlEngineExtensionInterface = WAIT['QQmlEngineExtensionInterface']
  QQmlExtensionInterface = WAIT['QQmlExtensionInterface']
  QQmlNetworkAccessManagerFactory = WAIT['QQmlNetworkAccessManagerFactory']
  QQmlProfiler = WAIT['QQmlProfiler']
  QString = WAIT['QString']
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlTypeLoader(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlTypeLoader: a plain Python object standing in
  front of one C++ QQmlTypeLoader.

  What exists
  -----------

  Every function of Qt's QQmlTypeLoader that has a ritual and that Python can
  call so far, 43 names in all: 'tr', 'sanitizeUNCPath', 'cleanFilePath',
  'fileExists', 'directoryExists', 'qmldirContent', 'setQmldirContent',
  'clearCache', 'trimCache', 'removeFromCache', 'isTypeLoaded',
  'isScriptLoaded', 'initializeEngine', 'invalidate', 'addUrlInterceptor',
  'removeUrlInterceptor', 'urlInterceptors', 'interceptUrl',
  'hasUrlInterceptors', 'profiler', 'setProfiler', 'importPathList',
  'setImportPathList', 'addImportPath', 'pluginPathList',
  'setPluginPathList', 'addPluginPath', 'setNetworkAccessManagerFactory',
  'createNetworkAccessManager', 'writeCacheFile', 'readCacheFile',
  'isDebugging', 'urlsForModule', 'isResource', 'thread', 'engine',
  'startThread', 'shutdownThread', 'ensureThread', 'networkReplyFinished',
  'networkReplyProgress', 'clearQmldirInfo', 'aotCacheMode'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlTypeLoader::~QQmlTypeLoader()': the destructor: Python never
    removes a C++ QQmlTypeLoader.
  - Qt's 'QQmlRefPointer<QV4::CompiledData::CompilationUnit>
    QQmlTypeLoader::injectModule(const QUrl &relativeUrl, const
    QV4::CompiledData::Unit *unit)': gives a type Python has no way to take
    yet.
  - Qt's 'void QQmlTypeLoader::loadWithStaticData(const QQmlDataBlob::Ptr
    &blob, const QByteArray &data, Mode mode)': takes a type Python has no
    way to hand over yet.
  - Qt's 'void QQmlTypeLoader::drop(const QQmlDataBlob::Ptr &blob)': takes a
    type Python has no way to hand over yet.
  - Qt's 'QQmlNetworkAccessManagerFactoryPtrConst
    QQmlTypeLoader::networkAccessManagerFactory() const': gives a type Python
    has no way to take yet.
  - Qt's 'void QQmlTypeLoader::trimCache(const QQmlTypeLoaderSharedDataPtr
    &data)': takes a type Python has no way to hand over yet.
  - Qt's 'void QQmlTypeLoader::loadThread(const QQmlDataBlob::Ptr &a0)':
    takes a type Python has no way to hand over yet.
  - Qt's 'void QQmlTypeLoader::loadWithStaticDataThread(const
    QQmlDataBlob::Ptr &a0, const QByteArray &a1)': takes a type Python has no
    way to hand over yet.
  - Qt's 'void QQmlTypeLoader::loadWithCachedUnitThread(const
    QQmlDataBlob::Ptr &blob, const QQmlPrivate::CachedQmlUnit *unit)': takes
    a type Python has no way to hand over yet.
  - Qt's 'void QQmlTypeLoader::setData(const QQmlDataBlob::Ptr &a0, const
    QByteArray &a1, DataOrigin a2)': takes a type Python has no way to hand
    over yet.
  - Qt's 'void QQmlTypeLoader::setData(const QQmlDataBlob::Ptr &a0, const
    QString &fileName, bool exists)': takes a type Python has no way to hand
    over yet.
  - Qt's 'void QQmlTypeLoader::setData(const QQmlDataBlob::Ptr &a0, const
    QQmlDataBlob::SourceCodeData &a1)': takes a type Python has no way to
    hand over yet.
  - Qt's 'void QQmlTypeLoader::setCachedUnit(const QQmlDataBlob::Ptr &blob,
    const QQmlPrivate::CachedQmlUnit *unit)': takes a type Python has no way
    to hand over yet.
  - Qt's 'QStringList QQmlTypeLoader::importPathList(PathType type) const':
    names the enum 'QQmlTypeLoader::PathType', whose class cannot be named
    here.
  - Qt's 'LocalQmldirResult
    QQmlTypeLoader::locateLocalQmldir(QQmlTypeLoader::Blob *blob, const
    QQmlTypeLoader::Blob::PendingImportPtr &import, QList<QQmlError>
    *errors)': takes a type Python has no way to hand over yet.
  - Qt's 'void QQmlTypeLoader::load(const QQmlDataBlob::Ptr &blob, Mode
    mode)': takes a type Python has no way to hand over yet.
  - Qt's 'void QQmlTypeLoader::loadWithCachedUnit(const QQmlDataBlob::Ptr
    &blob, const QQmlPrivate::CachedQmlUnit *unit, Mode mode)': takes a type
    Python has no way to hand over yet.
  - Qt's 'void QQmlTypeLoader::updateTypeCacheTrimThreshold(const
    QQmlTypeLoaderSharedDataPtr &data)': takes a type Python has no way to
    hand over yet.

  What has no ritual
  ------------------

  15 of the 79 functions Qt declares: 6 a template; 5 the compiler refuses
  its ritual as it would be written here; 4 leans on 'QQmlThread.

  What to expect
  --------------

  - The C++ QQmlTypeLoader is created at the first use, not by
    'QQmlTypeLoader(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlTypeLoader.
  - Each name of Qt's QQmlTypeLoader that has no cute function yet,
    'addTypeReferenceChecksumsToHash', 'doLoad', 'drop', 'finalizeBlob',
    'get', 'getQmldir', 'getScript', 'getType', 'hashDependencies',
    'injectModule', 'isModulePluginProcessingDone', 'isPluginInitialized',
    'load', 'loadThread', 'loadWithCachedUnit', 'loadWithCachedUnitThread',
    'loadWithStaticData', 'loadWithStaticDataThread', 'locateLocalQmldir',
    'networkAccessManagerFactory', 'setCachedUnit', 'setData',
    'setModulePluginProcessingDone', 'setPluginInitialized',
    'updateTypeCacheTrimThreshold', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QQmlTypeLoader, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class AddPathMode(CuteNum):
    """
    The enum 'QQmlTypeLoader::AddPathMode' of Qt, with the 2 names Qt gives
    in it.
    """

    PrependPath = Kee[int](0)
    AppendPath = Kee[int](1)

  class Mode(CuteNum):
    """
    The enum 'QQmlTypeLoader::Mode' of Qt, with the 3 names Qt gives in it.
    """

    PreferSynchronous = Kee[int](0)
    Asynchronous = Kee[int](1)
    Synchronous = Kee[int](2)

  #  The classes Qt writes inside QQmlTypeLoader, each a class in here as in
  #  C++.

  class Blob(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQmlTypeLoader::Blob: a plain Python object
    standing in front of one C++ QQmlTypeLoader::Blob.

    What exists
    -----------

    Every function of Qt's QQmlTypeLoader::Blob that has a ritual and that
    Python can call so far, 3 names in all: 'imports', 'setCachedUnitStatus',
    'stringAt'. None can be made from Python: one comes out of a function of
    another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQmlTypeLoader::Blob::~Blob()': the destructor: Python never
      removes a C++ QQmlTypeLoader::Blob.
    - Qt's 'void QQmlTypeLoader::Blob::importQmldirScripts(const
      PendingImportPtr &import, const QQmlTypeLoaderQmldirContent &qmldir,
      const QUrl &qmldirUrl)': takes a type Python has no way to hand over
      yet.
    - Qt's 'bool QQmlTypeLoader::Blob::handleLocalQmldirForImport(const
      PendingImportPtr &import, const QString &qmldirFilePath, const QString
      &qmldirUrl, QList<QQmlError> *errors)': takes a type Python has no way
      to hand over yet.
    - Qt's 'bool QQmlTypeLoader::Blob::addImport(const
      QV4::CompiledData::Import *import, QQmlImports::ImportFlags a1,
      QList<QQmlError> *errors)': names 'QList<QQmlError>', which has no cute
      class yet.
    - Qt's 'bool QQmlTypeLoader::Blob::addImport(const PendingImportPtr
      &import, QList<QQmlError> *errors)': takes a type Python has no way to
      hand over yet.
    - Qt's 'bool QQmlTypeLoader::Blob::fetchQmldir(const QUrl &url, const
      PendingImportPtr &import, int priority, QList<QQmlError> *errors)':
      takes a type Python has no way to hand over yet.
    - Qt's 'bool QQmlTypeLoader::Blob::updateQmldir(const
      QQmlRefPointer<QQmlQmldirData> &data, const PendingImportPtr &import,
      QList<QQmlError> *errors)': takes a type Python has no way to hand over
      yet.
    - Qt's 'bool QQmlTypeLoader::Blob::addScriptImport(const PendingImportPtr
      &import)': takes a type Python has no way to hand over yet.
    - Qt's 'bool QQmlTypeLoader::Blob::addFileImport(const PendingImportPtr
      &import, QList<QQmlError> *errors)': takes a type Python has no way to
      hand over yet.
    - Qt's 'bool QQmlTypeLoader::Blob::addLibraryImport(const
      PendingImportPtr &import, QList<QQmlError> *errors)': takes a type
      Python has no way to hand over yet.
    - Qt's 'bool QQmlTypeLoader::Blob::qmldirDataAvailable(const
      QQmlRefPointer<QQmlQmldirData> &a0, QList<QQmlError> *a1)': takes a
      type Python has no way to hand over yet.
    - Qt's 'void QQmlTypeLoader::Blob::scriptImported(const
      QQmlRefPointer<QQmlScriptBlob> &a0, const QV4::CompiledData::Location
      &a1, const QString &a2, const QString &a3)': takes a type Python has no
      way to hand over yet.
    - Qt's 'void QQmlTypeLoader::Blob::dependencyComplete(const
      QQmlDataBlob::Ptr &a0)': takes a type Python has no way to hand over
      yet.
    - Qt's 'bool QQmlTypeLoader::Blob::loadImportDependencies(const
      PendingImportPtr &currentImport, const QString &qmldirUri,
      QQmlImports::ImportFlags flags, QList<QQmlError> *errors)': takes a
      type Python has no way to hand over yet.
    - Qt's 'bool QQmlTypeLoader::Blob::registerPendingTypes(const
      PendingImportPtr &import)': takes a type Python has no way to hand over
      yet.
    - Qt's 'bool QQmlTypeLoader::Blob::loadDependentImports(const
      QList<QQmlDirParser::Import> &imports, const QString &qualifier,
      QTypeRevision version, quint8 precedence, QQmlImports::ImportFlags
      flags, QList<QQmlError> *errors)': takes a type Python has no way to
      hand over yet.

    What has no ritual
    ------------------

    1 of the 20 functions Qt declares: 1 leans on 'QQmlThread.

    What to expect
    --------------

    - The C++ QQmlTypeLoader::Blob is created at the first use, not by
      'QQmlTypeLoader::Blob(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - Python never removes the C++ QQmlTypeLoader::Blob.
    - Each name of Qt's QQmlTypeLoader::Blob that has no cute function yet,
      '__init__', 'addFileImport', 'addImport', 'addLibraryImport',
      'addScriptImport', 'fetchQmldir', 'handleLocalQmldirForImport',
      'importQmldirScripts', 'loadDependentImports',
      'loadImportDependencies', 'qmldirDataAvailable',
      'registerPendingTypes', 'scriptImported', 'updateQmldir', holds a
      function that raises 'NotImplementedError', and its docstring says why.
    """

    #  The classes Qt writes inside QQmlTypeLoader::Blob, each a class in
    #  here as in C++.

    class PendingImport(CuteMixin, metaclass=MetaCute):
      """
      The cute side of Qt's QQmlTypeLoader::Blob::PendingImport: a plain
      Python object standing in front of one C++
      QQmlTypeLoader::Blob::PendingImport.

      C++ hands a QQmlTypeLoader::Blob::PendingImport around as a copy, so
      every C++ QQmlTypeLoader::Blob::PendingImport behind a cute one is
      Python's own: it is removed, by the ritual named in
      '__delete_ritual__', when the cute object goes.

      What exists
      -----------

      No function of Qt's QQmlTypeLoader::Blob::PendingImport yet. It can be
      made from Python, in 1 way; see '__init__'.

      What has a ritual and is left out, and why
      ------------------------------------------

      - Qt's 'QQmlTypeLoader::Blob::PendingImport::PendingImport(const
        QQmlRefPointer<Blob> &blob, const QV4::CompiledData::Import *import,
        QQmlImports::ImportFlags flags)': takes a type Python has no way to
        hand over yet.
      - Qt's 'QQmlTypeLoader::Blob::PendingImport::~PendingImport()': the
        destructor: Python removes its C++
        QQmlTypeLoader::Blob::PendingImport by it, and has no other use for
        it.

      What to expect
      --------------

      - The C++ QQmlTypeLoader::Blob::PendingImport is created at the first
        use, not by 'QQmlTypeLoader::Blob::PendingImport(...)'.
      - A wrong argument is refused in Python, with 'DispatchException', and
        never reaches C++.
      - None is taken wherever Qt takes an object by its address, or text as
        C has it, and is passed on as nothing. Whether Qt can do with nothing
        there is as in C++.
      - A function giving a QQmlTypeLoader::Blob::PendingImport back gives a
        copy the ritual made for Python, in a new cute
        QQmlTypeLoader::Blob::PendingImport.
      """

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      #  Class Variables
      #  The class of Qt this class stands for.
      __qt_class__ = 'QQmlTypeLoader::Blob::PendingImport'

      #  Qt's '~QQmlTypeLoader::Blob::PendingImport()'. Naming it makes this
      #  a value class: Python owns every C++
      #  QQmlTypeLoader::Blob::PendingImport behind a cute one, and removes
      #  it by this ritual.
      __delete_ritual__ = 'ritual_ZN14QQmlTypeLoader4Blob13PendingImportD1Ev'

      #  Fallback Variables

      #  Private Variables

      #  Public Variables

      #  Virtual Variables

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      @overload()
      def __init__(self) -> None:
        """
        Notes what was given, for Qt's
        'QQmlTypeLoader::Blob::PendingImport::PendingImport()', which is
        called at the first use.

        Qt's own words:
        https://doc.qt.io/qt-6/qqmltypeloader-blob-pendingimport.html
        """
        #  QQmlTypeLoader::Blob::PendingImport::PendingImport()
        self._noteCreation(
            QQmlTypeLoader.Blob.PendingImport, lambda: Rituals.call(
                'ritual_ZN14QQmlTypeLoader4Blob13PendingImportC1Ev',
            ))

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQmlTypeLoader::Blob'

    #  A C++ QQmlTypeLoader::Blob Python makes is of a C++ class of ours, in
    #  which Python can take functions over. This ritual hands one over; see
    #  'CuteMixin._takeOver'.
    __take_ritual__ = 'ritual_take_QQmlTypeLoader_Blob'

    #  The functions Qt calls itself that QQmlTypeLoader::Blob is the first
    #  to declare and that cannot be handed to Python yet, each as Qt
    #  declares it. A class of a program that writes one of them anew is
    #  refused, since Qt would never call what it wrote; see
    #  'CuteMixin._refuseLeftOut'.
    __virtual_left_out__ = {
        'qmldirDataAvailable': (
            'bool QQmlTypeLoader::Blob::qmldirDataAvailable(const '
            'QQmlRefPointer<QQmlQmldirData> &, QList<QQmlError> *)',
        ),
        'scriptImported': (
            'void QQmlTypeLoader::Blob::scriptImported(const '
            'QQmlRefPointer<QQmlScriptBlob> &, const '
            'QV4::CompiledData::Location &, const QString &, const QString '
            '&)',
        ),
    }

    #  The functions Qt calls itself that QQmlTypeLoader::Blob is the first
    #  to declare. A class of a program built on it can write one anew, and
    #  Qt then calls that. For each name: the key C++ knows the function by,
    #  what it gives, and what it takes.
    __virtual_functions__ = {
        'stringAt': (
            ('_ZNK14QQmlTypeLoader4Blob8stringAtEi',
             ('address', 'text', ''),
             (
                 ('int', 'number', ''),
             )),
        ),
    }

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def imports(self) -> Optional[QQmlImports]:
      """
      Calls Qt's 'const QQmlImports *QQmlTypeLoader::Blob::imports() const'.

      Qt's own words: https://doc.qt.io/qt-6/qqmltypeloader-blob.html#imports

      Returns
      -------

      Optional[QQmlImports]
        The cute object standing for what Qt gave back. None when Qt gave
        back no object.
      """
      #  const QQmlImports *QQmlTypeLoader::Blob::imports() const
      address = self.uglySide.call(
          'ritual_ZNK14QQmlTypeLoader4Blob7importsEv',
      )
      return QQmlImports._cuteAt(address)

    @overload(int)
    def stringAt(self, a0: int) -> str:
      """
      Calls Qt's 'QString QQmlTypeLoader::Blob::stringAt(int a0) const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmltypeloader-blob.html#stringAt

      Parameters
      ----------

      a0 : int
        Passed on as it is.

      Returns
      -------

      str
        The text Qt gave back.
      """
      #  QString QQmlTypeLoader::Blob::stringAt(int a0) const
      ritual = 'ritual_ZNK14QQmlTypeLoader4Blob8stringAtEi'
      if self.uglySide.isOurs():
        ritual = 'ritual_own_ZNK14QQmlTypeLoader4Blob8stringAtEi'
      return self.uglySide.call(ritual, a0)

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload(QQmlMetaType.CachedUnitLookupError)
    def setCachedUnitStatus(
        self,
        status: QQmlMetaType.CachedUnitLookupError,
    ) -> None:
      """
      Calls Qt's 'void
      QQmlTypeLoader::Blob::setCachedUnitStatus(QQmlMetaType::
      CachedUnitLookupError status)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmltypeloader-blob.html#setCachedUnitStatus

      Parameters
      ----------

      status : QQmlMetaType.CachedUnitLookupError
        Passed on as its number.
      """
      #  void QQmlTypeLoader::Blob::setCachedUnitStatus(QQmlMetaType::
      #      CachedUnitLookupError status)
      self.uglySide.call(
          'ritual_ZN14QQmlTypeLoader4Blob19setCachedUnitStatusEN12QQmlMetaT'
          'ype21CachedUnitLookupErrorE',
          status.value,
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    def __init__(*__, **_) -> Never:
      """
      Qt's 'QQmlTypeLoader::Blob::Blob(const QUrl &url, QQmlDataBlob::Type
      type, QQmlTypeLoader *loader)': leans on 'QQmlThread::isThisThread()
      const', which Qt's source does not mark for use from outside Qt and has
      no code for that could be taken.
      """
      raise NotImplementedError(
          "'QQmlTypeLoader.Blob.__init__' has no cute function yet. Qt's "
          "'QQmlTypeLoader::Blob::Blob(const QUrl &url, QQmlDataBlob::Type "
          "type, QQmlTypeLoader *loader)': leans on "
          "'QQmlThread::isThisThread() const', which Qt's source does not "
          "mark for use from outside Qt and has no code for that could be "
          "taken.")

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    def addFileImport(*__, **_) -> Never:
      """
      Qt's 'bool QQmlTypeLoader::Blob::addFileImport(const PendingImportPtr
      &import, QList<QQmlError> *errors)': takes a type Python has no way to
      hand over yet.
      """
      raise NotImplementedError(
          "'QQmlTypeLoader.Blob.addFileImport' has no cute function yet. "
          "Qt's 'bool QQmlTypeLoader::Blob::addFileImport(const "
          "PendingImportPtr &import, QList<QQmlError> *errors)': takes a "
          "type Python has no way to hand over yet.")

    @staticmethod
    def addImport(*__, **_) -> Never:
      """
      - Qt's 'bool QQmlTypeLoader::Blob::addImport(const
        QV4::CompiledData::Import *import, QQmlImports::ImportFlags a1,
        QList<QQmlError> *errors)': names 'QList<QQmlError>', which has no
        cute class yet.
      - Qt's 'bool QQmlTypeLoader::Blob::addImport(const PendingImportPtr
        &import, QList<QQmlError> *errors)': takes a type Python has no way
        to hand over yet.
      """
      raise NotImplementedError(
          "'QQmlTypeLoader.Blob.addImport' has no cute function yet. Qt's "
          "'bool QQmlTypeLoader::Blob::addImport(const "
          "QV4::CompiledData::Import *import, QQmlImports::ImportFlags a1, "
          "QList<QQmlError> *errors)': names 'QList<QQmlError>', which has "
          "no cute class yet. Qt's 'bool "
          "QQmlTypeLoader::Blob::addImport(const PendingImportPtr &import, "
          "QList<QQmlError> *errors)': takes a type Python has no way to "
          "hand over yet.")

    @staticmethod
    def addLibraryImport(*__, **_) -> Never:
      """
      Qt's 'bool QQmlTypeLoader::Blob::addLibraryImport(const
      PendingImportPtr &import, QList<QQmlError> *errors)': takes a type
      Python has no way to hand over yet.
      """
      raise NotImplementedError(
          "'QQmlTypeLoader.Blob.addLibraryImport' has no cute function yet. "
          "Qt's 'bool QQmlTypeLoader::Blob::addLibraryImport(const "
          "PendingImportPtr &import, QList<QQmlError> *errors)': takes a "
          "type Python has no way to hand over yet.")

    @staticmethod
    def addScriptImport(*__, **_) -> Never:
      """
      Qt's 'bool QQmlTypeLoader::Blob::addScriptImport(const PendingImportPtr
      &import)': takes a type Python has no way to hand over yet.
      """
      raise NotImplementedError(
          "'QQmlTypeLoader.Blob.addScriptImport' has no cute function yet. "
          "Qt's 'bool QQmlTypeLoader::Blob::addScriptImport(const "
          "PendingImportPtr &import)': takes a type Python has no way to "
          "hand over yet.")

    @staticmethod
    def fetchQmldir(*__, **_) -> Never:
      """
      Qt's 'bool QQmlTypeLoader::Blob::fetchQmldir(const QUrl &url, const
      PendingImportPtr &import, int priority, QList<QQmlError> *errors)':
      takes a type Python has no way to hand over yet.
      """
      raise NotImplementedError(
          "'QQmlTypeLoader.Blob.fetchQmldir' has no cute function yet. Qt's "
          "'bool QQmlTypeLoader::Blob::fetchQmldir(const QUrl &url, const "
          "PendingImportPtr &import, int priority, QList<QQmlError> "
          "*errors)': takes a type Python has no way to hand over yet.")

    @staticmethod
    def handleLocalQmldirForImport(*__, **_) -> Never:
      """
      Qt's 'bool QQmlTypeLoader::Blob::handleLocalQmldirForImport(const
      PendingImportPtr &import, const QString &qmldirFilePath, const QString
      &qmldirUrl, QList<QQmlError> *errors)': takes a type Python has no way
      to hand over yet.
      """
      raise NotImplementedError(
          "'QQmlTypeLoader.Blob.handleLocalQmldirForImport' has no cute "
          "function yet. Qt's 'bool "
          "QQmlTypeLoader::Blob::handleLocalQmldirForImport(const "
          "PendingImportPtr &import, const QString &qmldirFilePath, const "
          "QString &qmldirUrl, QList<QQmlError> *errors)': takes a type "
          "Python has no way to hand over yet.")

    @staticmethod
    def importQmldirScripts(*__, **_) -> Never:
      """
      Qt's 'void QQmlTypeLoader::Blob::importQmldirScripts(const
      PendingImportPtr &import, const QQmlTypeLoaderQmldirContent &qmldir,
      const QUrl &qmldirUrl)': takes a type Python has no way to hand over
      yet.
      """
      raise NotImplementedError(
          "'QQmlTypeLoader.Blob.importQmldirScripts' has no cute function "
          "yet. Qt's 'void QQmlTypeLoader::Blob::importQmldirScripts(const "
          "PendingImportPtr &import, const QQmlTypeLoaderQmldirContent "
          "&qmldir, const QUrl &qmldirUrl)': takes a type Python has no way "
          "to hand over yet.")

    @staticmethod
    def loadDependentImports(*__, **_) -> Never:
      """
      Qt's 'bool QQmlTypeLoader::Blob::loadDependentImports(const
      QList<QQmlDirParser::Import> &imports, const QString &qualifier,
      QTypeRevision version, quint8 precedence, QQmlImports::ImportFlags
      flags, QList<QQmlError> *errors)': takes a type Python has no way to
      hand over yet.
      """
      raise NotImplementedError(
          "'QQmlTypeLoader.Blob.loadDependentImports' has no cute function "
          "yet. Qt's 'bool QQmlTypeLoader::Blob::loadDependentImports(const "
          "QList<QQmlDirParser::Import> &imports, const QString &qualifier, "
          "QTypeRevision version, quint8 precedence, "
          "QQmlImports::ImportFlags flags, QList<QQmlError> *errors)': "
          "takes a type Python has no way to hand over yet.")

    @staticmethod
    def loadImportDependencies(*__, **_) -> Never:
      """
      Qt's 'bool QQmlTypeLoader::Blob::loadImportDependencies(const
      PendingImportPtr &currentImport, const QString &qmldirUri,
      QQmlImports::ImportFlags flags, QList<QQmlError> *errors)': takes a
      type Python has no way to hand over yet.
      """
      raise NotImplementedError(
          "'QQmlTypeLoader.Blob.loadImportDependencies' has no cute "
          "function yet. Qt's 'bool "
          "QQmlTypeLoader::Blob::loadImportDependencies(const "
          "PendingImportPtr &currentImport, const QString &qmldirUri, "
          "QQmlImports::ImportFlags flags, QList<QQmlError> *errors)': "
          "takes a type Python has no way to hand over yet.")

    @staticmethod
    def qmldirDataAvailable(*__, **_) -> Never:
      """
      Qt's 'bool QQmlTypeLoader::Blob::qmldirDataAvailable(const
      QQmlRefPointer<QQmlQmldirData> &a0, QList<QQmlError> *a1)': takes a
      type Python has no way to hand over yet.
      """
      raise NotImplementedError(
          "'QQmlTypeLoader.Blob.qmldirDataAvailable' has no cute function "
          "yet. Qt's 'bool QQmlTypeLoader::Blob::qmldirDataAvailable(const "
          "QQmlRefPointer<QQmlQmldirData> &a0, QList<QQmlError> *a1)': "
          "takes a type Python has no way to hand over yet.")

    @staticmethod
    def registerPendingTypes(*__, **_) -> Never:
      """
      Qt's 'bool QQmlTypeLoader::Blob::registerPendingTypes(const
      PendingImportPtr &import)': takes a type Python has no way to hand over
      yet.
      """
      raise NotImplementedError(
          "'QQmlTypeLoader.Blob.registerPendingTypes' has no cute function "
          "yet. Qt's 'bool QQmlTypeLoader::Blob::registerPendingTypes(const "
          "PendingImportPtr &import)': takes a type Python has no way to "
          "hand over yet.")

    @staticmethod
    def scriptImported(*__, **_) -> Never:
      """
      Qt's 'void QQmlTypeLoader::Blob::scriptImported(const
      QQmlRefPointer<QQmlScriptBlob> &a0, const QV4::CompiledData::Location
      &a1, const QString &a2, const QString &a3)': takes a type Python has no
      way to hand over yet.
      """
      raise NotImplementedError(
          "'QQmlTypeLoader.Blob.scriptImported' has no cute function yet. "
          "Qt's 'void QQmlTypeLoader::Blob::scriptImported(const "
          "QQmlRefPointer<QQmlScriptBlob> &a0, const "
          "QV4::CompiledData::Location &a1, const QString &a2, const "
          "QString &a3)': takes a type Python has no way to hand over yet.")

    @staticmethod
    def updateQmldir(*__, **_) -> Never:
      """
      Qt's 'bool QQmlTypeLoader::Blob::updateQmldir(const
      QQmlRefPointer<QQmlQmldirData> &data, const PendingImportPtr &import,
      QList<QQmlError> *errors)': takes a type Python has no way to hand over
      yet.
      """
      raise NotImplementedError(
          "'QQmlTypeLoader.Blob.updateQmldir' has no cute function yet. "
          "Qt's 'bool QQmlTypeLoader::Blob::updateQmldir(const "
          "QQmlRefPointer<QQmlQmldirData> &data, const PendingImportPtr "
          "&import, QList<QQmlError> *errors)': takes a type Python has no "
          "way to hand over yet.")

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
  def tr(
      sourceText: Optional[str],
      disambiguation: Optional[str] = None,
      n: int = -1,
  ) -> str:
    """
    Calls Qt's 'QString QQmlTypeLoader::tr(const char *sourceText, const char
    *disambiguation, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltypeloader.html#tr

    Parameters
    ----------

    sourceText : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    disambiguation : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlTypeLoader::tr(const char *sourceText, const char
    #      *disambiguation, int n)
    return Rituals.call(
        'ritual_ZN14QQmlTypeLoader2trEPKcS1_i',
        CuteMixin._bytesOf(sourceText), CuteMixin._bytesOf(disambiguation),
        n,
    )

  @staticmethod
  @overload(QString)
  @overload(NoneType)
  def sanitizeUNCPath(path: Optional[QString]) -> None:
    """
    Calls Qt's 'void QQmlTypeLoader::sanitizeUNCPath(QString *path)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltypeloader.html#sanitizeUNCPath

    Parameters
    ----------

    path : Optional[QString]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlTypeLoader::sanitizeUNCPath(QString *path)
    Rituals.call(
        'ritual_ZN14QQmlTypeLoader15sanitizeUNCPathEP7QString',
        CuteMixin._addressOf(path),
    )

  @staticmethod
  @overload(str)
  def isResource(path: str) -> bool:
    """
    Calls Qt's 'bool QQmlTypeLoader::isResource(const QString &path)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltypeloader.html#isResource

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QQmlTypeLoader::isResource(const QString &path)
    return Rituals.call(
        'ritual_ZN14QQmlTypeLoader10isResourceERK7QString', path,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlTypeLoader'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def cleanFilePath(self, path: str) -> str:
    """
    Calls Qt's 'QString QQmlTypeLoader::cleanFilePath(const QString &path)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltypeloader.html#cleanFilePath

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlTypeLoader::cleanFilePath(const QString &path) const
    return self.uglySide.call(
        'ritual_ZNK14QQmlTypeLoader13cleanFilePathERK7QString', path,
    )

  @overload(str)
  def fileExists(self, filePath: str) -> bool:
    """
    Calls Qt's 'bool QQmlTypeLoader::fileExists(const QString &filePath)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltypeloader.html#fileExists

    Parameters
    ----------

    filePath : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QQmlTypeLoader::fileExists(const QString &filePath) const
    return self.uglySide.call(
        'ritual_ZNK14QQmlTypeLoader10fileExistsERK7QString', filePath,
    )

  @overload(str, str)
  def fileExists(self, dirPath: str, file: str) -> bool:
    """
    Calls Qt's 'bool QQmlTypeLoader::fileExists(const QString &dirPath, const
    QString &file) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltypeloader.html#fileExists

    Parameters
    ----------

    dirPath : str
      Passed on as it is: a QString is made of it for the call.

    file : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QQmlTypeLoader::fileExists(const QString &dirPath, const QString
    #      &file) const
    return self.uglySide.call(
        'ritual_ZNK14QQmlTypeLoader10fileExistsERK7QStringS2_',
        dirPath, file,
    )

  @overload(QUrl)
  def isTypeLoaded(self, url: QUrl) -> bool:
    """
    Calls Qt's 'bool QQmlTypeLoader::isTypeLoaded(const QUrl &url) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltypeloader.html#isTypeLoaded

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  bool QQmlTypeLoader::isTypeLoaded(const QUrl &url) const
    return self.uglySide.call(
        'ritual_ZNK14QQmlTypeLoader12isTypeLoadedERK4QUrl',
        self._valueOf(url),
    )

  @overload(QUrl)
  def isScriptLoaded(self, url: QUrl) -> bool:
    """
    Calls Qt's 'bool QQmlTypeLoader::isScriptLoaded(const QUrl &url) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltypeloader.html#isScriptLoaded

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  bool QQmlTypeLoader::isScriptLoaded(const QUrl &url) const
    return self.uglySide.call(
        'ritual_ZNK14QQmlTypeLoader14isScriptLoadedERK4QUrl',
        self._valueOf(url),
    )

  def urlInterceptors(self) -> QList[QQmlAbstractUrlInterceptor]:
    """
    Calls Qt's 'QList<QQmlAbstractUrlInterceptor *>
    QQmlTypeLoader::urlInterceptors() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltypeloader.html#urlInterceptors

    Returns
    -------

    QList[QQmlAbstractUrlInterceptor]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QQmlAbstractUrlInterceptor *> QQmlTypeLoader::urlInterceptors()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK14QQmlTypeLoader15urlInterceptorsEv',
    )
    return QList[QQmlAbstractUrlInterceptor]._cuteOwning(address)

  @overload(QUrl, QQmlAbstractUrlInterceptor.DataType)
  def interceptUrl(
      self,
      url: QUrl,
      type: QQmlAbstractUrlInterceptor.DataType,
  ) -> QUrl:
    """
    Calls Qt's 'QUrl QQmlTypeLoader::interceptUrl(const QUrl &url,
    QQmlAbstractUrlInterceptor::DataType type) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltypeloader.html#interceptUrl

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    type : QQmlAbstractUrlInterceptor.DataType
      Passed on as its number.

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQmlTypeLoader::interceptUrl(const QUrl &url,
    #      QQmlAbstractUrlInterceptor::DataType type) const
    address = self.uglySide.call(
        'ritual_ZNK14QQmlTypeLoader12interceptUrlERK4QUrlN26QQmlAbstractUrl'
        'Interceptor8DataTypeE',
        self._valueOf(url), type.value,
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def hasUrlInterceptors(self) -> bool:
    """
    Calls Qt's 'bool QQmlTypeLoader::hasUrlInterceptors() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltypeloader.html#hasUrlInterceptors
    """
    #  bool QQmlTypeLoader::hasUrlInterceptors() const
    return self.uglySide.call(
        'ritual_ZNK14QQmlTypeLoader18hasUrlInterceptorsEv',
    )

  def profiler(self) -> Optional[QQmlProfiler]:
    """
    Calls Qt's 'QQmlProfiler *QQmlTypeLoader::profiler() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltypeloader.html#profiler

    Returns
    -------

    Optional[QQmlProfiler]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlProfiler *QQmlTypeLoader::profiler() const
    address = self.uglySide.call('ritual_ZNK14QQmlTypeLoader8profilerEv')
    from . import QQmlProfiler
    return QQmlProfiler._cuteAt(address)

  def importPathList(self) -> QStringList:
    """
    Calls Qt's 'QStringList QQmlTypeLoader::importPathList() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltypeloader.html#importPathList

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QQmlTypeLoader::importPathList() const
    address = self.uglySide.call(
        'ritual_ZNK14QQmlTypeLoader14importPathListEv',
    )
    return QStringList._cuteOwning(address)

  def pluginPathList(self) -> QStringList:
    """
    Calls Qt's 'QStringList QQmlTypeLoader::pluginPathList() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltypeloader.html#pluginPathList

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QQmlTypeLoader::pluginPathList() const
    address = self.uglySide.call(
        'ritual_ZNK14QQmlTypeLoader14pluginPathListEv',
    )
    return QStringList._cuteOwning(address)

  @overload(QObject)
  @overload(NoneType)
  def createNetworkAccessManager(
      self,
      parent: Optional[QObject],
  ) -> Optional[QNetworkAccessManager]:
    """
    Calls Qt's 'QNetworkAccessManager
    *QQmlTypeLoader::createNetworkAccessManager(QObject *parent) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltypeloader.html#createNetworkAccessManager

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QNetworkAccessManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNetworkAccessManager
    #      *QQmlTypeLoader::createNetworkAccessManager(QObject *parent) const
    address = self.uglySide.call(
        'ritual_ZNK14QQmlTypeLoader26createNetworkAccessManagerEP7QObject',
        self._addressOf(parent, 'QObject'),
    )
    from ..QtNetwork import QNetworkAccessManager
    return QNetworkAccessManager._cuteAt(address)

  @overload(str)
  def urlsForModule(self, module: str) -> QStringList:
    """
    Calls Qt's 'QStringList QQmlTypeLoader::urlsForModule(const QString
    &module) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltypeloader.html#urlsForModule

    Parameters
    ----------

    module : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QQmlTypeLoader::urlsForModule(const QString &module) const
    address = self.uglySide.call(
        'ritual_ZNK14QQmlTypeLoader13urlsForModuleERK7QString', module,
    )
    return QStringList._cuteOwning(address)

  def thread(self) -> Optional[QQmlTypeLoaderThread]:
    """
    Calls Qt's 'QQmlTypeLoaderThread *QQmlTypeLoader::thread() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltypeloader.html#thread

    Returns
    -------

    Optional[QQmlTypeLoaderThread]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlTypeLoaderThread *QQmlTypeLoader::thread() const
    address = self.uglySide.call('ritual_ZNK14QQmlTypeLoader6threadEv')
    from . import QQmlTypeLoaderThread
    return QQmlTypeLoaderThread._cuteAt(address)

  def engine(self) -> Optional[QV4.ExecutionEngine]:
    """
    Calls Qt's 'QV4::ExecutionEngine *QQmlTypeLoader::engine() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltypeloader.html#engine

    Returns
    -------

    Optional[QV4.ExecutionEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::ExecutionEngine *QQmlTypeLoader::engine() const
    address = self.uglySide.call('ritual_ZNK14QQmlTypeLoader6engineEv')
    return QV4.ExecutionEngine._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str, str)
  def setQmldirContent(self, filePath: str, content: str) -> None:
    """
    Calls Qt's 'void QQmlTypeLoader::setQmldirContent(const QString
    &filePath, const QString &content)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltypeloader.html#setQmldirContent

    Parameters
    ----------

    filePath : str
      Passed on as it is: a QString is made of it for the call.

    content : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlTypeLoader::setQmldirContent(const QString &filePath, const
    #      QString &content)
    self.uglySide.call(
        'ritual_ZN14QQmlTypeLoader16setQmldirContentERK7QStringS2_',
        filePath, content,
    )

  @overload(QQmlProfiler)
  @overload(NoneType)
  def setProfiler(self, profiler: Optional[QQmlProfiler]) -> None:
    """
    Calls Qt's 'void QQmlTypeLoader::setProfiler(QQmlProfiler *profiler)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltypeloader.html#setProfiler

    Parameters
    ----------

    profiler : Optional[QQmlProfiler]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlTypeLoader::setProfiler(QQmlProfiler *profiler)
    self.uglySide.call(
        'ritual_ZN14QQmlTypeLoader11setProfilerEP12QQmlProfiler',
        self._addressOf(profiler),
    )

  @overload(QStringList)
  def setImportPathList(self, paths: QStringList) -> None:
    """
    Calls Qt's 'void QQmlTypeLoader::setImportPathList(const QStringList
    &paths)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltypeloader.html#setImportPathList

    Parameters
    ----------

    paths : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QQmlTypeLoader::setImportPathList(const QStringList &paths)
    self.uglySide.call(
        'ritual_ZN14QQmlTypeLoader17setImportPathListERK5QListI7QStringE',
        self._valueOf(paths),
    )

  @overload(QStringList)
  def setPluginPathList(self, paths: QStringList) -> None:
    """
    Calls Qt's 'void QQmlTypeLoader::setPluginPathList(const QStringList
    &paths)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltypeloader.html#setPluginPathList

    Parameters
    ----------

    paths : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QQmlTypeLoader::setPluginPathList(const QStringList &paths)
    self.uglySide.call(
        'ritual_ZN14QQmlTypeLoader17setPluginPathListERK5QListI7QStringE',
        self._valueOf(paths),
    )

  @overload(QQmlNetworkAccessManagerFactory)
  @overload(NoneType)
  def setNetworkAccessManagerFactory(
      self,
      factory: Optional[QQmlNetworkAccessManagerFactory],
  ) -> None:
    """
    Calls Qt's 'void QQmlTypeLoader::setNetworkAccessManagerFactory(
    QQmlNetworkAccessManagerFactory *factory)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltypeloader.html#setNetworkAccessManagerFactory

    Parameters
    ----------

    factory : Optional[QQmlNetworkAccessManagerFactory]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlTypeLoader::setNetworkAccessManagerFactory(
    #      QQmlNetworkAccessManagerFactory *factory)
    self.uglySide.call(
        'ritual_ZN14QQmlTypeLoader30setNetworkAccessManagerFactoryEP31QQmlN'
        'etworkAccessManagerFactory',
        self._addressOf(factory),
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

  @overload(WAIT['QV4.ExecutionEngine'])
  @overload(NoneType)
  def __init__(self, engine: Optional[QV4.ExecutionEngine]) -> None:
    """
    Notes what was given, for Qt's
    'QQmlTypeLoader::QQmlTypeLoader(QV4::ExecutionEngine *engine)', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qqmltypeloader.html#QQmlTypeLoader

    Parameters
    ----------

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQmlTypeLoader::QQmlTypeLoader(QV4::ExecutionEngine *engine)
    self._noteCreation(QQmlTypeLoader, lambda: Rituals.call(
        'ritual_ZN14QQmlTypeLoaderC1EPN3QV415ExecutionEngineE',
        self._addressOf(engine),
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
  def directoryExists(self, path: str) -> bool:
    """
    Calls Qt's 'bool QQmlTypeLoader::directoryExists(const QString &path)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltypeloader.html#directoryExists

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QQmlTypeLoader::directoryExists(const QString &path)
    return self.uglySide.call(
        'ritual_ZN14QQmlTypeLoader15directoryExistsERK7QString', path,
    )

  @overload(str)
  def qmldirContent(self, filePath: str) -> QQmlTypeLoaderQmldirContent:
    """
    Calls Qt's 'const QQmlTypeLoaderQmldirContent
    QQmlTypeLoader::qmldirContent(const QString &filePath)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltypeloader.html#qmldirContent

    Parameters
    ----------

    filePath : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QQmlTypeLoaderQmldirContent
      A new cute QQmlTypeLoaderQmldirContent around the copy Qt gave back.
      Python owns it.
    """
    #  const QQmlTypeLoaderQmldirContent QQmlTypeLoader::qmldirContent(const
    #      QString &filePath)
    address = self.uglySide.call(
        'ritual_ZN14QQmlTypeLoader13qmldirContentERK7QString', filePath,
    )
    from . import QQmlTypeLoaderQmldirContent
    return QQmlTypeLoaderQmldirContent._cuteOwning(address)

  def clearCache(self) -> None:
    """
    Calls Qt's 'void QQmlTypeLoader::clearCache()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltypeloader.html#clearCache
    """
    #  void QQmlTypeLoader::clearCache()
    self.uglySide.call('ritual_ZN14QQmlTypeLoader10clearCacheEv')

  def trimCache(self) -> None:
    """
    Calls Qt's 'void QQmlTypeLoader::trimCache()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltypeloader.html#trimCache
    """
    #  void QQmlTypeLoader::trimCache()
    self.uglySide.call('ritual_ZN14QQmlTypeLoader9trimCacheEv')

  @overload(QUrl)
  def removeFromCache(self, url: QUrl) -> bool:
    """
    Calls Qt's 'bool QQmlTypeLoader::removeFromCache(const QUrl &url)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltypeloader.html#removeFromCache

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  bool QQmlTypeLoader::removeFromCache(const QUrl &url)
    return self.uglySide.call(
        'ritual_ZN14QQmlTypeLoader15removeFromCacheERK4QUrl',
        self._valueOf(url),
    )

  @overload(QQmlEngineExtensionInterface, str)
  @overload(QQmlEngineExtensionInterface, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  def initializeEngine(
      self,
      a0: Optional[QQmlEngineExtensionInterface],
      a1: Optional[str],
  ) -> None:
    """
    Calls Qt's 'void
    QQmlTypeLoader::initializeEngine(QQmlEngineExtensionInterface *a0, const
    char *a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltypeloader.html#initializeEngine

    Parameters
    ----------

    a0 : Optional[QQmlEngineExtensionInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  void QQmlTypeLoader::initializeEngine(QQmlEngineExtensionInterface
    #      *a0, const char *a1)
    self.uglySide.call(
        'ritual_ZN14QQmlTypeLoader16initializeEngineEP28QQmlEngineExtension'
        'InterfacePKc',
        self._addressOf(a0, 'QQmlEngineExtensionInterface'),
        self._bytesOf(a1),
    )

  @overload(QQmlExtensionInterface, str)
  @overload(QQmlExtensionInterface, NoneType)
  def initializeEngine(
      self,
      a0: Optional[QQmlExtensionInterface],
      a1: Optional[str],
  ) -> None:
    """
    Calls Qt's 'void QQmlTypeLoader::initializeEngine(QQmlExtensionInterface
    *a0, const char *a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltypeloader.html#initializeEngine

    Parameters
    ----------

    a0 : Optional[QQmlExtensionInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  void QQmlTypeLoader::initializeEngine(QQmlExtensionInterface *a0,
    #      const char *a1)
    self.uglySide.call(
        'ritual_ZN14QQmlTypeLoader16initializeEngineEP22QQmlExtensionInterf'
        'acePKc',
        self._addressOf(a0, 'QQmlExtensionInterface'), self._bytesOf(a1),
    )

  def invalidate(self) -> None:
    """
    Calls Qt's 'void QQmlTypeLoader::invalidate()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltypeloader.html#invalidate
    """
    #  void QQmlTypeLoader::invalidate()
    self.uglySide.call('ritual_ZN14QQmlTypeLoader10invalidateEv')

  @overload(QQmlAbstractUrlInterceptor)
  @overload(NoneType)
  def addUrlInterceptor(
      self,
      urlInterceptor: Optional[QQmlAbstractUrlInterceptor],
  ) -> None:
    """
    Calls Qt's 'void
    QQmlTypeLoader::addUrlInterceptor(QQmlAbstractUrlInterceptor
    *urlInterceptor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltypeloader.html#addUrlInterceptor

    Parameters
    ----------

    urlInterceptor : Optional[QQmlAbstractUrlInterceptor]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlTypeLoader::addUrlInterceptor(QQmlAbstractUrlInterceptor
    #      *urlInterceptor)
    self.uglySide.call(
        'ritual_ZN14QQmlTypeLoader17addUrlInterceptorEP26QQmlAbstractUrlInt'
        'erceptor',
        self._addressOf(urlInterceptor),
    )

  @overload(QQmlAbstractUrlInterceptor)
  @overload(NoneType)
  def removeUrlInterceptor(
      self,
      urlInterceptor: Optional[QQmlAbstractUrlInterceptor],
  ) -> None:
    """
    Calls Qt's 'void
    QQmlTypeLoader::removeUrlInterceptor(QQmlAbstractUrlInterceptor
    *urlInterceptor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltypeloader.html#removeUrlInterceptor

    Parameters
    ----------

    urlInterceptor : Optional[QQmlAbstractUrlInterceptor]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlTypeLoader::removeUrlInterceptor(QQmlAbstractUrlInterceptor
    #      *urlInterceptor)
    self.uglySide.call(
        'ritual_ZN14QQmlTypeLoader20removeUrlInterceptorEP26QQmlAbstractUrl'
        'Interceptor',
        self._addressOf(urlInterceptor),
    )

  @overload(str, AddPathMode)
  def addImportPath(self, dir: str, mode: AddPathMode) -> None:
    """
    Calls Qt's 'void QQmlTypeLoader::addImportPath(const QString &dir,
    AddPathMode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltypeloader.html#addImportPath

    Parameters
    ----------

    dir : str
      Passed on as it is: a QString is made of it for the call.

    mode : AddPathMode
      Passed on as its number.
    """
    #  void QQmlTypeLoader::addImportPath(const QString &dir, AddPathMode
    #      mode)
    self.uglySide.call(
        'ritual_ZN14QQmlTypeLoader13addImportPathERK7QStringNS_11AddPathMod'
        'eE',
        dir, mode.value,
    )

  @overload(str, AddPathMode)
  def addPluginPath(self, path: str, mode: AddPathMode) -> None:
    """
    Calls Qt's 'void QQmlTypeLoader::addPluginPath(const QString &path,
    AddPathMode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltypeloader.html#addPluginPath

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.

    mode : AddPathMode
      Passed on as its number.
    """
    #  void QQmlTypeLoader::addPluginPath(const QString &path, AddPathMode
    #      mode)
    self.uglySide.call(
        'ritual_ZN14QQmlTypeLoader13addPluginPathERK7QStringNS_11AddPathMod'
        'eE',
        path, mode.value,
    )

  def writeCacheFile(self) -> bool:
    """
    Calls Qt's 'bool QQmlTypeLoader::writeCacheFile()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltypeloader.html#writeCacheFile
    """
    #  bool QQmlTypeLoader::writeCacheFile()
    return self.uglySide.call('ritual_ZN14QQmlTypeLoader14writeCacheFileEv')

  def readCacheFile(self) -> bool:
    """
    Calls Qt's 'bool QQmlTypeLoader::readCacheFile()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltypeloader.html#readCacheFile
    """
    #  bool QQmlTypeLoader::readCacheFile()
    return self.uglySide.call('ritual_ZN14QQmlTypeLoader13readCacheFileEv')

  def isDebugging(self) -> bool:
    """
    Calls Qt's 'bool QQmlTypeLoader::isDebugging()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltypeloader.html#isDebugging
    """
    #  bool QQmlTypeLoader::isDebugging()
    return self.uglySide.call('ritual_ZN14QQmlTypeLoader11isDebuggingEv')

  def startThread(self) -> None:
    """
    Calls Qt's 'void QQmlTypeLoader::startThread()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltypeloader.html#startThread
    """
    #  void QQmlTypeLoader::startThread()
    self.uglySide.call('ritual_ZN14QQmlTypeLoader11startThreadEv')

  def shutdownThread(self) -> None:
    """
    Calls Qt's 'void QQmlTypeLoader::shutdownThread()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltypeloader.html#shutdownThread
    """
    #  void QQmlTypeLoader::shutdownThread()
    self.uglySide.call('ritual_ZN14QQmlTypeLoader14shutdownThreadEv')

  def ensureThread(self) -> Optional[QQmlTypeLoaderThread]:
    """
    Calls Qt's 'QQmlTypeLoaderThread *QQmlTypeLoader::ensureThread()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltypeloader.html#ensureThread

    Returns
    -------

    Optional[QQmlTypeLoaderThread]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlTypeLoaderThread *QQmlTypeLoader::ensureThread()
    address = self.uglySide.call('ritual_ZN14QQmlTypeLoader12ensureThreadEv')
    from . import QQmlTypeLoaderThread
    return QQmlTypeLoaderThread._cuteAt(address)

  @overload(QNetworkReply)
  @overload(NoneType)
  def networkReplyFinished(self, a0: Optional[QNetworkReply]) -> None:
    """
    Calls Qt's 'void QQmlTypeLoader::networkReplyFinished(QNetworkReply
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltypeloader.html#networkReplyFinished

    Parameters
    ----------

    a0 : Optional[QNetworkReply]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlTypeLoader::networkReplyFinished(QNetworkReply *a0)
    self.uglySide.call(
        'ritual_ZN14QQmlTypeLoader20networkReplyFinishedEP13QNetworkReply',
        self._addressOf(a0),
    )

  @overload(QNetworkReply, int, int)
  @overload(NoneType, int, int)
  def networkReplyProgress(
      self,
      a0: Optional[QNetworkReply],
      a1: int,
      a2: int,
  ) -> None:
    """
    Calls Qt's 'void QQmlTypeLoader::networkReplyProgress(QNetworkReply *a0,
    qint64 a1, qint64 a2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltypeloader.html#networkReplyProgress

    Parameters
    ----------

    a0 : Optional[QNetworkReply]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : int
      Passed on as it is.

    a2 : int
      Passed on as it is.
    """
    #  void QQmlTypeLoader::networkReplyProgress(QNetworkReply *a0, qint64
    #      a1, qint64 a2)
    self.uglySide.call(
        'ritual_ZN14QQmlTypeLoader20networkReplyProgressEP13QNetworkReplyxx',
        self._addressOf(a0), a1, a2,
    )

  def clearQmldirInfo(self) -> None:
    """
    Calls Qt's 'void QQmlTypeLoader::clearQmldirInfo()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltypeloader.html#clearQmldirInfo
    """
    #  void QQmlTypeLoader::clearQmldirInfo()
    self.uglySide.call('ritual_ZN14QQmlTypeLoader15clearQmldirInfoEv')

  def aotCacheMode(self) -> QQmlMetaType.CacheMode:
    """
    Calls Qt's 'QQmlMetaType::CacheMode QQmlTypeLoader::aotCacheMode()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltypeloader.html#aotCacheMode

    Returns
    -------

    QQmlMetaType.CacheMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQmlMetaType.CacheMode(number)' gives.
    """
    #  QQmlMetaType::CacheMode QQmlTypeLoader::aotCacheMode()
    return QQmlMetaType.CacheMode(self.uglySide.call(
        'ritual_ZN14QQmlTypeLoader12aotCacheModeEv',
    ))

  @staticmethod
  def addTypeReferenceChecksumsToHash(*__, **_) -> Never:
    """
    Qt's 'QQmlTypeLoader::addTypeReferenceChecksumsToHash': a template: a
    pattern and no single function.
    """
    raise NotImplementedError(
        "'QQmlTypeLoader.addTypeReferenceChecksumsToHash' has no cute "
        "function yet. Qt's "
        "'QQmlTypeLoader::addTypeReferenceChecksumsToHash': a template: a "
        "pattern and no single function.")

  @staticmethod
  def doLoad(*__, **_) -> Never:
    """
    Qt's 'QQmlTypeLoader::doLoad': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QQmlTypeLoader.doLoad' has no cute function yet. Qt's "
        "'QQmlTypeLoader::doLoad': a template: a pattern and no single "
        "function.")

  @staticmethod
  def drop(*__, **_) -> Never:
    """
    Qt's 'void QQmlTypeLoader::drop(const QQmlDataBlob::Ptr &blob)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlTypeLoader.drop' has no cute function yet. Qt's 'void "
        "QQmlTypeLoader::drop(const QQmlDataBlob::Ptr &blob)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def finalizeBlob(*__, **_) -> Never:
    """
    Qt's 'QQmlTypeLoader::finalizeBlob': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QQmlTypeLoader.finalizeBlob' has no cute function yet. Qt's "
        "'QQmlTypeLoader::finalizeBlob': a template: a pattern and no "
        "single function.")

  @staticmethod
  def get(*__, **_) -> Never:
    """
    Qt's 'QQmlTypeLoader::get': a template: a pattern and no single function.
    """
    raise NotImplementedError(
        "'QQmlTypeLoader.get' has no cute function yet. Qt's "
        "'QQmlTypeLoader::get': a template: a pattern and no single "
        "function.")

  @staticmethod
  def getQmldir(*__, **_) -> Never:
    """
    Qt's 'QQmlRefPointer<QQmlQmldirData> QQmlTypeLoader::getQmldir(const QUrl
    &a0)': the compiler refuses its ritual as it would be written here:
    member access into incomplete type 'QQmlQmldirData'.
    """
    raise NotImplementedError(
        "'QQmlTypeLoader.getQmldir' has no cute function yet. Qt's "
        "'QQmlRefPointer<QQmlQmldirData> QQmlTypeLoader::getQmldir(const "
        "QUrl &a0)': the compiler refuses its ritual as it would be written "
        "here: member access into incomplete type 'QQmlQmldirData'.")

  @staticmethod
  def getScript(*__, **_) -> Never:
    """
    - Qt's 'QQmlRefPointer<QQmlScriptBlob> QQmlTypeLoader::getScript(const
      QUrl &unNormalizedUrl, Mode mode)': the compiler refuses its ritual as
      it would be written here: member access into incomplete type
      'QQmlScriptBlob'.
    - Qt's 'QQmlRefPointer<QQmlScriptBlob> QQmlTypeLoader::getScript(const
      QUrl &unNormalizedUrl, const QUrl &relativeUrl)': the compiler refuses
      its ritual as it would be written here: member access into incomplete
      type 'QQmlScriptBlob'.
    """
    raise NotImplementedError(
        "'QQmlTypeLoader.getScript' has no cute function yet. Qt's "
        "'QQmlRefPointer<QQmlScriptBlob> QQmlTypeLoader::getScript(const "
        "QUrl &unNormalizedUrl, Mode mode)': the compiler refuses its "
        "ritual as it would be written here: member access into incomplete "
        "type 'QQmlScriptBlob'. Qt's 'QQmlRefPointer<QQmlScriptBlob> "
        "QQmlTypeLoader::getScript(const QUrl &unNormalizedUrl, const QUrl "
        "&relativeUrl)': the compiler refuses its ritual as it would be "
        "written here: member access into incomplete type 'QQmlScriptBlob'.")

  @staticmethod
  def getType(*__, **_) -> Never:
    """
    - Qt's 'QQmlRefPointer<QQmlTypeData> QQmlTypeLoader::getType(const QUrl
      &unNormalizedUrl, Mode mode)': the compiler refuses its ritual as it
      would be written here: member access into incomplete type
      'QQmlTypeData'.
    - Qt's 'QQmlRefPointer<QQmlTypeData> QQmlTypeLoader::getType(const
      QByteArray &data, const QUrl &url, Mode mode)': the compiler refuses
      its ritual as it would be written here: member access into incomplete
      type 'QQmlTypeData'.
    """
    raise NotImplementedError(
        "'QQmlTypeLoader.getType' has no cute function yet. Qt's "
        "'QQmlRefPointer<QQmlTypeData> QQmlTypeLoader::getType(const QUrl "
        "&unNormalizedUrl, Mode mode)': the compiler refuses its ritual as "
        "it would be written here: member access into incomplete type "
        "'QQmlTypeData'. Qt's 'QQmlRefPointer<QQmlTypeData> "
        "QQmlTypeLoader::getType(const QByteArray &data, const QUrl &url, "
        "Mode mode)': the compiler refuses its ritual as it would be "
        "written here: member access into incomplete type 'QQmlTypeData'.")

  @staticmethod
  def hashDependencies(*__, **_) -> Never:
    """
    Qt's 'QQmlTypeLoader::hashDependencies': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'QQmlTypeLoader.hashDependencies' has no cute function yet. Qt's "
        "'QQmlTypeLoader::hashDependencies': a template: a pattern and no "
        "single function.")

  @staticmethod
  def injectModule(*__, **_) -> Never:
    """
    Qt's 'QQmlRefPointer<QV4::CompiledData::CompilationUnit>
    QQmlTypeLoader::injectModule(const QUrl &relativeUrl, const
    QV4::CompiledData::Unit *unit)': gives a type Python has no way to take
    yet.
    """
    raise NotImplementedError(
        "'QQmlTypeLoader.injectModule' has no cute function yet. Qt's "
        "'QQmlRefPointer<QV4::CompiledData::CompilationUnit> "
        "QQmlTypeLoader::injectModule(const QUrl &relativeUrl, const "
        "QV4::CompiledData::Unit *unit)': gives a type Python has no way to "
        "take yet.")

  @staticmethod
  def isModulePluginProcessingDone(*__, **_) -> Never:
    """
    Qt's 'bool QQmlTypeLoader::isModulePluginProcessingDone(const QString
    &module)': leans on 'QQmlThread::isThisThread() const', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QQmlTypeLoader.isModulePluginProcessingDone' has no cute function "
        "yet. Qt's 'bool QQmlTypeLoader::isModulePluginProcessingDone(const "
        "QString &module)': leans on 'QQmlThread::isThisThread() const', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def isPluginInitialized(*__, **_) -> Never:
    """
    Qt's 'bool QQmlTypeLoader::isPluginInitialized(const QString &plugin)
    const': leans on 'QQmlThread::isThisThread() const', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QQmlTypeLoader.isPluginInitialized' has no cute function yet. "
        "Qt's 'bool QQmlTypeLoader::isPluginInitialized(const QString "
        "&plugin) const': leans on 'QQmlThread::isThisThread() const', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def load(*__, **_) -> Never:
    """
    Qt's 'void QQmlTypeLoader::load(const QQmlDataBlob::Ptr &blob, Mode
    mode)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlTypeLoader.load' has no cute function yet. Qt's 'void "
        "QQmlTypeLoader::load(const QQmlDataBlob::Ptr &blob, Mode mode)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def loadThread(*__, **_) -> Never:
    """
    Qt's 'void QQmlTypeLoader::loadThread(const QQmlDataBlob::Ptr &a0)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlTypeLoader.loadThread' has no cute function yet. Qt's 'void "
        "QQmlTypeLoader::loadThread(const QQmlDataBlob::Ptr &a0)': takes a "
        "type Python has no way to hand over yet.")

  @staticmethod
  def loadWithCachedUnit(*__, **_) -> Never:
    """
    Qt's 'void QQmlTypeLoader::loadWithCachedUnit(const QQmlDataBlob::Ptr
    &blob, const QQmlPrivate::CachedQmlUnit *unit, Mode mode)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlTypeLoader.loadWithCachedUnit' has no cute function yet. Qt's "
        "'void QQmlTypeLoader::loadWithCachedUnit(const QQmlDataBlob::Ptr "
        "&blob, const QQmlPrivate::CachedQmlUnit *unit, Mode mode)': takes "
        "a type Python has no way to hand over yet.")

  @staticmethod
  def loadWithCachedUnitThread(*__, **_) -> Never:
    """
    Qt's 'void QQmlTypeLoader::loadWithCachedUnitThread(const
    QQmlDataBlob::Ptr &blob, const QQmlPrivate::CachedQmlUnit *unit)': takes
    a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlTypeLoader.loadWithCachedUnitThread' has no cute function "
        "yet. Qt's 'void QQmlTypeLoader::loadWithCachedUnitThread(const "
        "QQmlDataBlob::Ptr &blob, const QQmlPrivate::CachedQmlUnit *unit)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def loadWithStaticData(*__, **_) -> Never:
    """
    Qt's 'void QQmlTypeLoader::loadWithStaticData(const QQmlDataBlob::Ptr
    &blob, const QByteArray &data, Mode mode)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlTypeLoader.loadWithStaticData' has no cute function yet. Qt's "
        "'void QQmlTypeLoader::loadWithStaticData(const QQmlDataBlob::Ptr "
        "&blob, const QByteArray &data, Mode mode)': takes a type Python "
        "has no way to hand over yet.")

  @staticmethod
  def loadWithStaticDataThread(*__, **_) -> Never:
    """
    Qt's 'void QQmlTypeLoader::loadWithStaticDataThread(const
    QQmlDataBlob::Ptr &a0, const QByteArray &a1)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlTypeLoader.loadWithStaticDataThread' has no cute function "
        "yet. Qt's 'void QQmlTypeLoader::loadWithStaticDataThread(const "
        "QQmlDataBlob::Ptr &a0, const QByteArray &a1)': takes a type Python "
        "has no way to hand over yet.")

  @staticmethod
  def locateLocalQmldir(*__, **_) -> Never:
    """
    Qt's 'LocalQmldirResult
    QQmlTypeLoader::locateLocalQmldir(QQmlTypeLoader::Blob *blob, const
    QQmlTypeLoader::Blob::PendingImportPtr &import, QList<QQmlError>
    *errors)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlTypeLoader.locateLocalQmldir' has no cute function yet. Qt's "
        "'LocalQmldirResult "
        "QQmlTypeLoader::locateLocalQmldir(QQmlTypeLoader::Blob *blob, "
        "const QQmlTypeLoader::Blob::PendingImportPtr &import, "
        "QList<QQmlError> *errors)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def networkAccessManagerFactory(*__, **_) -> Never:
    """
    Qt's 'QQmlNetworkAccessManagerFactoryPtrConst
    QQmlTypeLoader::networkAccessManagerFactory() const': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlTypeLoader.networkAccessManagerFactory' has no cute function "
        "yet. Qt's 'QQmlNetworkAccessManagerFactoryPtrConst "
        "QQmlTypeLoader::networkAccessManagerFactory() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def setCachedUnit(*__, **_) -> Never:
    """
    Qt's 'void QQmlTypeLoader::setCachedUnit(const QQmlDataBlob::Ptr &blob,
    const QQmlPrivate::CachedQmlUnit *unit)': takes a type Python has no way
    to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlTypeLoader.setCachedUnit' has no cute function yet. Qt's "
        "'void QQmlTypeLoader::setCachedUnit(const QQmlDataBlob::Ptr &blob, "
        "const QQmlPrivate::CachedQmlUnit *unit)': takes a type Python has "
        "no way to hand over yet.")

  @staticmethod
  def setData(*__, **_) -> Never:
    """
    - Qt's 'void QQmlTypeLoader::setData(const QQmlDataBlob::Ptr &a0, const
      QByteArray &a1, DataOrigin a2)': takes a type Python has no way to hand
      over yet.
    - Qt's 'void QQmlTypeLoader::setData(const QQmlDataBlob::Ptr &a0, const
      QString &fileName, bool exists)': takes a type Python has no way to
      hand over yet.
    - Qt's 'void QQmlTypeLoader::setData(const QQmlDataBlob::Ptr &a0, const
      QQmlDataBlob::SourceCodeData &a1)': takes a type Python has no way to
      hand over yet.
    """
    raise NotImplementedError(
        "'QQmlTypeLoader.setData' has no cute function yet. Qt's 'void "
        "QQmlTypeLoader::setData(const QQmlDataBlob::Ptr &a0, const "
        "QByteArray &a1, DataOrigin a2)': takes a type Python has no way to "
        "hand over yet. Qt's 'void QQmlTypeLoader::setData(const "
        "QQmlDataBlob::Ptr &a0, const QString &fileName, bool exists)': "
        "takes a type Python has no way to hand over yet. Qt's 'void "
        "QQmlTypeLoader::setData(const QQmlDataBlob::Ptr &a0, const "
        "QQmlDataBlob::SourceCodeData &a1)': takes a type Python has no way "
        "to hand over yet.")

  @staticmethod
  def setModulePluginProcessingDone(*__, **_) -> Never:
    """
    Qt's 'void QQmlTypeLoader::setModulePluginProcessingDone(const QString
    &module)': leans on 'QQmlThread::isThisThread() const', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QQmlTypeLoader.setModulePluginProcessingDone' has no cute "
        "function yet. Qt's 'void "
        "QQmlTypeLoader::setModulePluginProcessingDone(const QString "
        "&module)': leans on 'QQmlThread::isThisThread() const', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def setPluginInitialized(*__, **_) -> Never:
    """
    Qt's 'void QQmlTypeLoader::setPluginInitialized(const QString &plugin)':
    leans on 'QQmlThread::isThisThread() const', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQmlTypeLoader.setPluginInitialized' has no cute function yet. "
        "Qt's 'void QQmlTypeLoader::setPluginInitialized(const QString "
        "&plugin)': leans on 'QQmlThread::isThisThread() const', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def updateTypeCacheTrimThreshold(*__, **_) -> Never:
    """
    Qt's 'void QQmlTypeLoader::updateTypeCacheTrimThreshold(const
    QQmlTypeLoaderSharedDataPtr &data)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QQmlTypeLoader.updateTypeCacheTrimThreshold' has no cute function "
        "yet. Qt's 'void QQmlTypeLoader::updateTypeCacheTrimThreshold(const "
        "QQmlTypeLoaderSharedDataPtr &data)': takes a type Python has no "
        "way to hand over yet.")
