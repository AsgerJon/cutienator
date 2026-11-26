//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlscriptblob_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlscriptblob_p.h>
#include <QtQml/6.12.0/QtQml/private/qqmldatablob_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4compileddata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qqmlengine_p.h>
#include <QtQml/private/qqmlirbuilder_p.h>
#include <QtQml/private/qqmlscriptblob_p.h>
#include <QtQml/private/qqmlsourcecoordinate_p.h>
#include <QtQml/private/qqmlcontextdata_p.h>
#include <QtQml/private/qv4runtimecodegen_p.h>
#include <QtQml/private/qv4script_p.h>
#include <QtCore/qloggingcategory.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/qml/qqmlscriptblob.cpp, line 29, as _ZN14QQmlScriptBlob12dataReceivedERKN12QQmlDataBlob14SourceCodeDataE
inline void QQmlScriptBlob::dataReceived(const SourceCodeData &data)
{
    assertTypeLoaderThread();

    const bool isCacheable = data.isCacheable();

    if (isCacheable && m_typeLoader->readCacheFile()) {
        auto unit = QQml::makeRefPointer<QV4::CompiledData::CompilationUnit>();
        QString error;
        const auto sourceChecksum = [&data]() { return data.checksum(); };
        if (unit->loadFromDisk(url(), data.sourceTimeStamp(), sourceChecksum, &error)) {
            initializeFromCompilationUnit(std::move(unit));
            return;
        } else {
            qCDebug(DBG_DISK_CACHE())
                    << "Error loading" << urlString() << "from disk cache:" << error;
        }
    }

    if (!data.exists()) {
        if (m_cachedUnitStatus == QQmlMetaType::CachedUnitLookupError::VersionMismatch)
            setError(QQmlTypeLoader::tr("File was compiled ahead of time with an incompatible version of Qt and the original file cannot be found. Please recompile"));
        else
            setError(QQmlTypeLoader::tr("No such file or directory"));
        return;
    }

    QString error;
    QString source = data.readAll(&error);
    if (!error.isEmpty()) {
        setError(error);
        return;
    }

    QQmlRefPointer<QV4::CompiledData::CompilationUnit> unit;

    if (m_isModule) {
        QList<QQmlJS::DiagnosticMessage> diagnostics;
        unit = QV4::Compiler::Codegen::compileModule(
                m_typeLoader->isDebugging(), urlString(), source, data.sourceTimeStamp(),
                &diagnostics);
        QList<QQmlError> errors = QQmlEnginePrivate::qmlErrorFromDiagnostics(urlString(), diagnostics);
        if (!errors.isEmpty()) {
            setError(errors);
            return;
        }
    } else {
        QmlIR::Document irUnit(urlString(), finalUrlString(), m_typeLoader->isDebugging());

        irUnit.jsModule.sourceTimeStamp = data.sourceTimeStamp();

        QmlIR::ScriptDirectivesCollector collector(&irUnit);
        irUnit.jsParserEngine.setDirectives(&collector);

        QList<QQmlError> errors;
        const QString fragment = finalUrl().fragment();
        irUnit.javaScriptCompilationUnit = QV4::Script::precompile(
                     &irUnit.jsModule, &irUnit.jsParserEngine, &irUnit.jsGenerator, urlString(),
                     source, &errors, fragment == QLatin1String("global")
                        ? QV4::Compiler::ContextType::Global
                        : QV4::Compiler::ContextType::ScriptImportedByQML,
                     fragment == QLatin1String("include")
                        ? QV4::Script::InheritContext::Yes
                        : QV4::Script::InheritContext::No);

        source.clear();
        if (!errors.isEmpty()) {
            setError(errors);
            return;
        }

        QmlIR::QmlUnitGenerator qmlGenerator;
        qmlGenerator.generate(irUnit);
        unit = std::move(irUnit.javaScriptCompilationUnit);
    }

    if (isCacheable && m_typeLoader->writeCacheFile()) {
        QString errorString;
        const auto sourceChecksum = [&data]() { return data.checksum(); };
        if (unit->saveToDisk(url(), sourceChecksum, &errorString)) {
            QString error;
            if (!unit->loadFromDisk(url(), data.sourceTimeStamp(), sourceChecksum, &error)) {
                // log but ignore error, keep using the in-memory compilation unit.
                qCDebug(DBG_DISK_CACHE()) << "Error re-loading cached version of"
                                          << unit->fileName() << "from disk:" << errorString;
            }
        } else {
            qCDebug(DBG_DISK_CACHE()) << "Error saving cached version of"
                                      << unit->fileName() << "to disk:" << errorString;
        }
    }

    initializeFromCompilationUnit(std::move(unit));
}

//  from ../qtdeclarative/src/qml/qml/qqmlscriptblob.cpp, line 196, as _ZN14QQmlScriptBlob14scriptImportedERK14QQmlRefPointerIS_ERKN3QV412CompiledData8LocationERK7QStringSB_
inline void QQmlScriptBlob::scriptImported(const QQmlRefPointer<QQmlScriptBlob> &blob, const QV4::CompiledData::Location &location, const QString &qualifier, const QString &nameSpace)
{
    assertTypeLoaderThread();

    ScriptReference ref;
    ref.script = blob;
    ref.location = location;
    ref.qualifier = qualifier;
    ref.nameSpace = nameSpace;

    m_scripts << ref;
}

//  from ../qtdeclarative/src/qml/qml/qqmlscriptblob.cpp, line 124, as _ZN14QQmlScriptBlob24initializeFromCachedUnitEPKN11QQmlPrivate13CachedQmlUnitE
inline void QQmlScriptBlob::initializeFromCachedUnit(const QQmlPrivate::CachedQmlUnit *cachedUnit)
{
    assertTypeLoaderThread();
    initializeFromCompilationUnit(QQml::makeRefPointer<QV4::CompiledData::CompilationUnit>(
            cachedUnit->qmlData, cachedUnit->aotCompiledFunctions,
            cachedUnit->validateLookupSignatures, urlString(), finalUrlString()));
}

//  from ../qtdeclarative/src/qml/qml/qqmlscriptblob.cpp, line 132, as _ZN14QQmlScriptBlob4doneEv
inline void QQmlScriptBlob::done()
{
    assertTypeLoaderThread();

    if (isError())
        return;

    // Check all script dependencies for errors
    for (int ii = 0; ii < m_scripts.size(); ++ii) {
        const ScriptReference &script = m_scripts.at(ii);
        // We would like to assert on isCompleteOrError() here, but since ECMAScript dependencies
        // can be cyclic, we need to live with certain scripts formally not being complete.
        // However, since we only omit the dependency if the compilation unit already exists when
        // loading, we will still catch all errors here.
        if (script.script->isError()) {
            QList<QQmlError> errors = script.script->errors();
            QQmlError error;
            error.setUrl(url());
            error.setLine(qmlConvertSourceCoordinate<quint32, int>(script.location.line()));
            error.setColumn(qmlConvertSourceCoordinate<quint32, int>(script.location.column()));
            error.setDescription(QQmlTypeLoader::tr("Script %1 unavailable").arg(script.script->urlString()));
            errors.prepend(error);
            setError(errors);
            return;
        }
    }

    if (!m_isModule) {
        m_scriptData->typeNameCache.adopt(new QQmlTypeNameCache(m_importCache));

        QSet<QString> ns;

        for (int scriptIndex = 0; scriptIndex < m_scripts.size(); ++scriptIndex) {
            const ScriptReference &script = m_scripts.at(scriptIndex);

            m_scriptData->scripts.append(script.script->scriptData());

            if (!script.nameSpace.isNull()) {
                if (!ns.contains(script.nameSpace)) {
                    ns.insert(script.nameSpace);
                    m_scriptData->typeNameCache->add(script.nameSpace);
                }
            }
            m_scriptData->typeNameCache->add(script.qualifier, scriptIndex, script.nameSpace);
        }

        m_importCache->populateCache(m_scriptData->typeNameCache.data());
    }

    if (auto cu = m_scriptData->compilationUnit()) {
        cu->qmlType = QQmlMetaType::findCompositeType(url(), cu, QQmlMetaType::JavaScript);
        for (const auto &script : std::as_const(m_scripts))
            cu->dependentScripts.append(script.script->scriptData());
        QQmlMetaType::registerInternalCompositeType(cu);
    }

    m_scripts.clear();
}

//  from ../qtdeclarative/src/qml/qml/qqmlscriptblob.cpp, line 25, as _ZN14QQmlScriptBlobD2Ev
inline QQmlScriptBlob::~QQmlScriptBlob()
{
}

//  from ../qtdeclarative/src/qml/qml/qqmlscriptblob.cpp, line 191, as _ZNK14QQmlScriptBlob8stringAtEi
inline QString QQmlScriptBlob::stringAt(int index) const
{
    return m_scriptData->m_precompiledScript->stringAt(index);
}

//  from ../qtdeclarative/src/qml/qml/qqmlscriptblob.cpp, line 17, as _Z14DBG_DISK_CACHEv
inline const QLoggingCategory &DBG_DISK_CACHE()
{
    static const QLoggingCategory category("qt.qml.diskcache");
    return category;
}

//  from ../qtdeclarative/src/qml/qml/qqmlscriptblob.cpp, line 209, as _ZN14QQmlScriptBlob29initializeFromCompilationUnitEO14QQmlRefPointerIN3QV412CompiledData15CompilationUnitEE
inline void QQmlScriptBlob::initializeFromCompilationUnit(
        QQmlRefPointer<QV4::CompiledData::CompilationUnit> &&unit)
{
    assertTypeLoaderThread();
    Q_ASSERT(!m_scriptData);
    Q_ASSERT(unit);

    m_scriptData.adopt(new QQmlScriptData());
    m_scriptData->url = finalUrl();
    m_scriptData->urlString = finalUrlString();
    m_scriptData->m_precompiledScript = unit;

    m_importCache->setBaseUrl(finalUrl(), finalUrlString());

    if (!m_isModule) {
        QList<QQmlError> errors;
        for (quint32 i = 0, count = unit->importCount(); i < count; ++i) {
            const QV4::CompiledData::Import *import = unit->importAt(i);
            if (!addImport(import, {}, &errors)) {
                Q_ASSERT(errors.size());
                QQmlError error(errors.takeFirst());
                error.setUrl(m_importCache->baseUrl());
                error.setLine(import->location.line());
                error.setColumn(import->location.column());
                errors.prepend(error); // put it back on the list after filling out information.
                setError(errors);
                return;
            }
        }
    }

    const QStringList moduleRequests = unit->moduleRequests();
    for (const QString &request: moduleRequests) {
        const QUrl relativeRequest(request);
        QUrl absoluteRequest = unit->finalUrl().resolved(relativeRequest);
        if (!request.endsWith(QLatin1String(".mjs")))
            absoluteRequest.setFragment(QLatin1String("module"));
        QQmlRefPointer<QQmlScriptBlob> absoluteBlob
                = typeLoader()->getScript(absoluteRequest, relativeRequest);
        if (!absoluteBlob->m_scriptData || !absoluteBlob->m_scriptData->m_precompiledScript)
            addDependency(absoluteBlob.data());
        scriptImported(
                absoluteBlob, /* ### */QV4::CompiledData::Location(), /*qualifier*/QString(),
                /*namespace*/QString());
    }
}
//  -----------------------------------------------------------------------

//  Only a class built on QQmlScriptBlob may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQmlScriptBlob : QQmlScriptBlob {
  using QQmlScriptBlob::stringAt;
};

//  A QQmlScriptBlob that Python can take functions over in. Every QQmlScriptBlob
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQmlScriptBlobCall0)(const void *, const QQmlDataBlob::SourceCodeData *, int *);
typedef void (*CuteQQmlScriptBlobCall1)(const void *, const QQmlPrivate::CachedQmlUnit *, int *);
typedef void (*CuteQQmlScriptBlobCall2)(const void *, int *);
typedef QString * (*CuteQQmlScriptBlobCall3)(const void *, int, int *);
typedef void (*CuteQQmlScriptBlobCall4)(const void *, int *);
typedef void (*CuteQQmlScriptBlobCall5)(const void *, qreal, int *);
#if QT_CONFIG(qml_network)
typedef void (*CuteQQmlScriptBlobCall6)(const void *, int, int *);
#endif  // QT_CONFIG(qml_network)
typedef void (*CuteQQmlScriptBlobCall7)(const void *, int *);
class CuteQQmlScriptBlob : public QQmlScriptBlob {
public:
  using QQmlScriptBlob::QQmlScriptBlob;
  void *taken[8] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN12QQmlDataBlob12dataReceivedERKNS_14SourceCodeDataE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QQmlDataBlob24initializeFromCachedUnitEPKN11QQmlPrivate13CachedQmlUnitE")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QQmlDataBlob4doneEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QQmlTypeLoader4Blob8stringAtEi")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QQmlDataBlob9completedEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QQmlDataBlob23downloadProgressChangedEd")) {
      taken[5] = call;
      return true;
    }
#if QT_CONFIG(qml_network)
    if (!std::strcmp(key, "_ZN12QQmlDataBlob12networkErrorEN13QNetworkReply12NetworkErrorE")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_network)
    if (!std::strcmp(key, "_ZN12QQmlDataBlob19allDependenciesDoneEv")) {
      taken[7] = call;
      return true;
    }
    return false;
  }

  //  void QQmlScriptBlob::dataReceived(const SourceCodeData &a0)
  void dataReceived(const QQmlDataBlob::SourceCodeData &a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlScriptBlobCall0 call = reinterpret_cast<CuteQQmlScriptBlobCall0>(taken[0]);
      call(this, &a0, &handled);
      if (handled) return;
    }
    QQmlScriptBlob::dataReceived(a0);
  }

  //  void QQmlScriptBlob::initializeFromCachedUnit(const
  //      QQmlPrivate::CachedQmlUnit *unit)
  void initializeFromCachedUnit(
      const QQmlPrivate::CachedQmlUnit *unit) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQmlScriptBlobCall1 call = reinterpret_cast<CuteQQmlScriptBlobCall1>(taken[1]);
      call(this, unit, &handled);
      if (handled) return;
    }
    QQmlScriptBlob::initializeFromCachedUnit(unit);
  }

  //  void QQmlScriptBlob::done()
  void done() override {
    if (taken[2]) {
      int handled = 0;
      CuteQQmlScriptBlobCall2 call = reinterpret_cast<CuteQQmlScriptBlobCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlScriptBlob::done();
  }

  //  QString QQmlScriptBlob::stringAt(int index) const
  QString stringAt(int index) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQQmlScriptBlobCall3 call = reinterpret_cast<CuteQQmlScriptBlobCall3>(taken[3]);
      QString * given = call(this, index, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QQmlScriptBlob::stringAt(index);
  }

  //  void QQmlNotifyingBlob::completed()
  void completed() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQmlScriptBlobCall4 call = reinterpret_cast<CuteQQmlScriptBlobCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlNotifyingBlob::completed();
  }

  //  void QQmlNotifyingBlob::downloadProgressChanged(qreal a0)
  void downloadProgressChanged(qreal a0) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQmlScriptBlobCall5 call = reinterpret_cast<CuteQQmlScriptBlobCall5>(taken[5]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlNotifyingBlob::downloadProgressChanged(a0);
  }

#if QT_CONFIG(qml_network)
  //  void QQmlDataBlob::networkError(QNetworkReply::NetworkError a0)
  void networkError(QNetworkReply::NetworkError a0) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQmlScriptBlobCall6 call = reinterpret_cast<CuteQQmlScriptBlobCall6>(taken[6]);
      call(this, static_cast<int>(a0), &handled);
      if (handled) return;
    }
    QQmlDataBlob::networkError(a0);
  }
#endif  // QT_CONFIG(qml_network)

  //  void QQmlDataBlob::allDependenciesDone()
  void allDependenciesDone() override {
    if (taken[7]) {
      int handled = 0;
      CuteQQmlScriptBlobCall7 call = reinterpret_cast<CuteQQmlScriptBlobCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlDataBlob::allDependenciesDone();
  }
};

//  QQmlScriptBlob::~QQmlScriptBlob()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlScriptBlobD1Ev(QQmlScriptBlob *self) {
  delete self;
}

//  QQmlRefPointer<QQmlScriptData> QQmlScriptBlob::scriptData() const
extern "C" Q_DECL_EXPORT
QQmlRefPointer<QQmlScriptData> *ritual_ZNK14QQmlScriptBlob10scriptDataEv(
    const QQmlScriptBlob *self) {
  return new QQmlRefPointer<QQmlScriptData>(self->scriptData());
}

//  void QQmlScriptBlob::dataReceived(const SourceCodeData &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlScriptBlob12dataReceivedERKN12QQmlDataBlob14SourceCodeDataE(
    QQmlScriptBlob *self,
    const QQmlDataBlob::SourceCodeData *a0) {
  self->dataReceived(*a0);
}

//  void QQmlScriptBlob::initializeFromCachedUnit(const
//      QQmlPrivate::CachedQmlUnit *unit)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlScriptBlob24initializeFromCachedUnitEPKN11QQmlPrivate13CachedQmlUnitE(
    QQmlScriptBlob *self,
    const QQmlPrivate::CachedQmlUnit *unit) {
  self->initializeFromCachedUnit(unit);
}

//  void QQmlScriptBlob::done()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlScriptBlob4doneEv(QQmlScriptBlob *self) {
  self->done();
}

//  QString QQmlScriptBlob::stringAt(int index) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QQmlScriptBlob8stringAtEi(
    const QQmlScriptBlob *self,
    int index) {
  return new QString(self->stringAt(index));
}

//  void QQmlScriptBlob::scriptImported(const QQmlRefPointer<QQmlScriptBlob>
//      &blob, const QV4::CompiledData::Location &location, const QString
//      &qualifier, const QString &nameSpace)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlScriptBlob14scriptImportedERK14QQmlRefPointerIS_ERKN3QV412CompiledData8LocationERK7QStringSB_(
    QQmlScriptBlob *self,
    const QQmlRefPointer<QQmlScriptBlob> *blob,
    const QV4::CompiledData::Location *location,
    const QString *qualifier,
    const QString *nameSpace) {
  self->scriptImported(*blob, *location, *qualifier, *nameSpace);
}

//  a Python function taken by a CuteQQmlScriptBlob, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlScriptBlob(
    QQmlScriptBlob *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlScriptBlob *>(self)->take(key, call);
}

//  QString QQmlScriptBlob::stringAt(int index) const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK14QQmlScriptBlob8stringAtEi(
    const QQmlScriptBlob *self,
    int index) {
  return new QString(
      static_cast<const OwnQQmlScriptBlob *>(self)->OwnQQmlScriptBlob::stringAt(
          index));
}

//  a QQmlRefPointer<QQmlScriptData> a ritual of QQmlScriptBlob gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQmlScriptBlob__QQmlRefPointer_QQmlScriptData(
    QQmlRefPointer<QQmlScriptData> *self) {
  delete self;
}
