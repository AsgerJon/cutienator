//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmltypedata_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmltypedata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmltype_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmldatablob_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <private/qqmlcomponentandaliasresolver_p.h>
#include <private/qqmlengine_p.h>
#include <private/qqmlirbuilder_p.h>
#include <private/qqmlirloader_p.h>
#include <private/qqmlpropertycachecreator_p.h>
#include <private/qqmlpropertyvalidator_p.h>
#include <private/qqmlscriptblob_p.h>
#include <private/qqmlscriptdata_p.h>
#include <private/qqmltypecompiler_p.h>
#include <private/qqmltypedata_p.h>
#include <private/qqmltypeloaderqmldircontent_p.h>
#include <QtCore/qloggingcategory.h>
#include <QtCore/qcryptographichash.h>
#include <memory>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/qml/qqmltypedata.cpp, line 43, as _ZN12QQmlTypeDataD1Ev
inline QQmlTypeData::~QQmlTypeData()
{
    m_scripts.clear();
    m_compositeSingletons.clear();
    m_resolvedTypes.clear();
}

//  from ../qtdeclarative/src/qml/qml/qqmltypedata.cpp, line 50, as _ZNK12QQmlTypeData15compilationUnitEv
inline QV4::CompiledData::CompilationUnit *QQmlTypeData::compilationUnit() const
{
    return m_compiledData.data();
}

//  from ../qtdeclarative/src/qml/qml/qqmltypedata.cpp, line 55, as _ZNK12QQmlTypeData7qmlTypeERK7QString
inline QQmlType QQmlTypeData::qmlType(const QString &inlineComponentName) const
{
    if (inlineComponentName.isEmpty())
        return m_qmlType;
    return m_inlineComponentData[inlineComponentName].qmlType;
}

//  from ../qtdeclarative/src/qml/qml/qqmltypedata.cpp, line 769, as _ZN12QQmlTypeData12dataReceivedERKN12QQmlDataBlob14SourceCodeDataE
inline void QQmlTypeData::dataReceived(const SourceCodeData &data)
{
    assertTypeLoaderThread();

    m_backupSourceCode = data;

    if (tryLoadFromDiskCache())
        return;

    if (isError())
        return;

    if (!m_backupSourceCode.exists()) {
        if (m_cachedUnitStatus == QQmlMetaType::CachedUnitLookupError::VersionMismatch)
            setError(QQmlTypeLoader::tr("File was compiled ahead of time with an incompatible version of Qt and the original file cannot be found. Please recompile"));
        else
            setError(QQmlTypeLoader::tr("No such file or directory"));
        return;
    }

    if (!loadFromSource())
        return;

    continueLoadFromIR();
}

//  from ../qtdeclarative/src/qml/qml/qqmltypedata.cpp, line 795, as _ZN12QQmlTypeData24initializeFromCachedUnitEPKN11QQmlPrivate13CachedQmlUnitE
inline void QQmlTypeData::initializeFromCachedUnit(const QQmlPrivate::CachedQmlUnit *unit)
{
    assertTypeLoaderThread();

    if (unit->qmlData->qmlUnit()->nObjects == 0) {
        setError(QQmlTypeLoader::tr("Cached QML Unit has no objects"));
        return;
    }

    m_document.reset(
            new QmlIR::Document(urlString(), finalUrlString(), m_typeLoader->isDebugging()));
    QQmlIRLoader loader(unit->qmlData, m_document.data());
    loader.load();
    m_document->javaScriptCompilationUnit
            = QQmlRefPointer<QV4::CompiledData::CompilationUnit>(
                new QV4::CompiledData::CompilationUnit(unit->qmlData, unit->aotCompiledFunctions, unit->validateLookupSignatures),
                QQmlRefPointer<QV4::CompiledData::CompilationUnit>::Adopt);
    continueLoadFromIR();
}

//  from ../qtdeclarative/src/qml/qml/qqmltypedata.cpp, line 917, as _ZN12QQmlTypeData19allDependenciesDoneEv
inline void QQmlTypeData::allDependenciesDone()
{
    assertTypeLoaderThread();

    QQmlTypeLoader::Blob::allDependenciesDone();

    if (!m_typesResolved)
        resolveTypes();
}

//  from ../qtdeclarative/src/qml/qml/qqmltypedata.cpp, line 927, as _ZNK12QQmlTypeData8stringAtEi
inline QString QQmlTypeData::stringAt(int index) const
{
    if (m_compiledData)
        return m_compiledData->stringAt(index);
    return m_document->jsGenerator.stringTable.stringForIndex(index);
}

//  from ../qtdeclarative/src/qml/qml/qqmltypedata.cpp, line 431, as _ZN12QQmlTypeData12checkScriptsEv
inline bool QQmlTypeData::checkScripts()
{
    // Check all script dependencies for errors
    for (int ii = 0; ii < m_scripts.size(); ++ii) {
        const ScriptReference &script = m_scripts.at(ii);
        Q_ASSERT(script.script->isCompleteOrError());
        if (script.script->isError()) {
            createError(
                    script,
                    QQmlTypeLoader::tr("Script %1 unavailable").arg(script.script->urlString()));
            return false;
        }
    }
    return true;
}

//  from ../qtdeclarative/src/qml/qml/qqmltypedata.cpp, line 457, as _ZN12QQmlTypeData17checkDependenciesEv
inline bool QQmlTypeData::checkDependencies()
{
    // Check all type dependencies for errors
    for (auto it = std::as_const(m_resolvedTypes).begin(), end = std::as_const(m_resolvedTypes).end();
         it != end; ++it) {
        const TypeReference &type = *it;
        Q_ASSERT(!type.typeData
                 || type.typeData->isCompleteOrError()
                 || type.type.isInlineComponentType());

        if (type.typeData && type.typeData->isError()) {
            const QString &typeName = stringAt(it.key());
            createError(type, QQmlTypeLoader::tr("Type %1 unavailable").arg(typeName));
            return false;
        }

        if (!type.selfReference && type.type.isInlineComponentType()) {
            const QString icName = type.type.elementName();
            Q_ASSERT(!icName.isEmpty());

            // We have a CU here. Check if the inline component exists.
            if (type.typeData && type.typeData->compilationUnit()->inlineComponentId(icName) >= 0)
                return true;

            const QString typeName = stringAt(it.key());
            const qsizetype lastDot = typeName.lastIndexOf(u'.');
            createError(
                    type,
                    QQmlTypeLoader::tr("Type %1 has no inline component type called %2")
                            .arg(QStringView{typeName}.left(lastDot), icName));
            return false;
        }
    }

    return true;
}

//  from ../qtdeclarative/src/qml/qml/qqmltypedata.cpp, line 447, as _ZN12QQmlTypeData11createErrorERKNS_13TypeReferenceERK7QString
inline void QQmlTypeData::createError(const TypeReference &type, const QString &message)
{
    createError(type, message, type.typeData ? type.typeData->errors() : QList<QQmlError>());
}

//  from ../qtdeclarative/src/qml/qml/qqmltypedata.cpp, line 452, as _ZN12QQmlTypeData11createErrorERKNS_15ScriptReferenceERK7QString
inline void QQmlTypeData::createError(const ScriptReference &script, const QString &message)
{
    createError(script, message, script.script ? script.script->errors() : QList<QQmlError>());
}

//  from ../qtdeclarative/src/qml/qml/qqmltypedata.cpp, line 494, as _ZN12QQmlTypeData24checkCompositeSingletonsEv
inline bool QQmlTypeData::checkCompositeSingletons()
{
    // Check all composite singleton type dependencies for errors
    for (int ii = 0; ii < m_compositeSingletons.size(); ++ii) {
        const TypeReference &type = m_compositeSingletons.at(ii);
        Q_ASSERT(!type.typeData || type.typeData->isCompleteOrError());
        if (type.typeData && type.typeData->isError()) {
            QString typeName = type.type.qmlTypeName();
            createError(type, QQmlTypeLoader::tr("Type %1 unavailable").arg(typeName));
            return false;
        }
    }

    return true;
}
//  -----------------------------------------------------------------------

//  Only a class built on QQmlTypeData may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQmlTypeData : QQmlTypeData {
  using QQmlTypeData::stringAt;
};

//  A QQmlTypeData that Python can take functions over in. Every QQmlTypeData
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQmlTypeDataCall0)(const void *, int *);
typedef void (*CuteQQmlTypeDataCall1)(const void *, const QQmlDataBlob::SourceCodeData *, int *);
typedef void (*CuteQQmlTypeDataCall2)(const void *, const QQmlPrivate::CachedQmlUnit *, int *);
typedef void (*CuteQQmlTypeDataCall3)(const void *, int *);
typedef QString * (*CuteQQmlTypeDataCall4)(const void *, int, int *);
typedef void (*CuteQQmlTypeDataCall5)(const void *, int *);
typedef void (*CuteQQmlTypeDataCall6)(const void *, qreal, int *);
#if QT_CONFIG(qml_network)
typedef void (*CuteQQmlTypeDataCall7)(const void *, int, int *);
#endif  // QT_CONFIG(qml_network)
class CuteQQmlTypeData : public QQmlTypeData {
public:
  using QQmlTypeData::QQmlTypeData;
  void *taken[8] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN12QQmlDataBlob4doneEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QQmlDataBlob12dataReceivedERKNS_14SourceCodeDataE")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QQmlDataBlob24initializeFromCachedUnitEPKN11QQmlPrivate13CachedQmlUnitE")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QQmlDataBlob19allDependenciesDoneEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QQmlTypeLoader4Blob8stringAtEi")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QQmlDataBlob9completedEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QQmlDataBlob23downloadProgressChangedEd")) {
      taken[6] = call;
      return true;
    }
#if QT_CONFIG(qml_network)
    if (!std::strcmp(key, "_ZN12QQmlDataBlob12networkErrorEN13QNetworkReply12NetworkErrorE")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_network)
    return false;
  }

  //  void QQmlTypeData::done()
  void done() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlTypeDataCall0 call = reinterpret_cast<CuteQQmlTypeDataCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlTypeData::done();
  }

  //  void QQmlTypeData::dataReceived(const SourceCodeData &a0)
  void dataReceived(const QQmlDataBlob::SourceCodeData &a0) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQmlTypeDataCall1 call = reinterpret_cast<CuteQQmlTypeDataCall1>(taken[1]);
      call(this, &a0, &handled);
      if (handled) return;
    }
    QQmlTypeData::dataReceived(a0);
  }

  //  void QQmlTypeData::initializeFromCachedUnit(const
  //      QQmlPrivate::CachedQmlUnit *unit)
  void initializeFromCachedUnit(
      const QQmlPrivate::CachedQmlUnit *unit) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQmlTypeDataCall2 call = reinterpret_cast<CuteQQmlTypeDataCall2>(taken[2]);
      call(this, unit, &handled);
      if (handled) return;
    }
    QQmlTypeData::initializeFromCachedUnit(unit);
  }

  //  void QQmlTypeData::allDependenciesDone()
  void allDependenciesDone() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQmlTypeDataCall3 call = reinterpret_cast<CuteQQmlTypeDataCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlTypeData::allDependenciesDone();
  }

  //  QString QQmlTypeData::stringAt(int index) const
  QString stringAt(int index) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQQmlTypeDataCall4 call = reinterpret_cast<CuteQQmlTypeDataCall4>(taken[4]);
      QString * given = call(this, index, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QQmlTypeData::stringAt(index);
  }

  //  void QQmlNotifyingBlob::completed()
  void completed() override {
    if (taken[5]) {
      int handled = 0;
      CuteQQmlTypeDataCall5 call = reinterpret_cast<CuteQQmlTypeDataCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlNotifyingBlob::completed();
  }

  //  void QQmlNotifyingBlob::downloadProgressChanged(qreal a0)
  void downloadProgressChanged(qreal a0) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQmlTypeDataCall6 call = reinterpret_cast<CuteQQmlTypeDataCall6>(taken[6]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlNotifyingBlob::downloadProgressChanged(a0);
  }

#if QT_CONFIG(qml_network)
  //  void QQmlDataBlob::networkError(QNetworkReply::NetworkError a0)
  void networkError(QNetworkReply::NetworkError a0) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQmlTypeDataCall7 call = reinterpret_cast<CuteQQmlTypeDataCall7>(taken[7]);
      call(this, static_cast<int>(a0), &handled);
      if (handled) return;
    }
    QQmlDataBlob::networkError(a0);
  }
#endif  // QT_CONFIG(qml_network)
};

//  QString QQmlTypeData::tr(const char *sourceText, const char
//      *disambiguation, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12QQmlTypeData2trEPKcS1_i(
    const char *sourceText,
    const char *disambiguation,
    int n) {
  return new QString(QQmlTypeData::tr(sourceText, disambiguation, n));
}

//  QQmlTypeData::~QQmlTypeData()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlTypeDataD1Ev(QQmlTypeData *self) {
  delete self;
}

//  QV4::CompiledData::CompilationUnit *QQmlTypeData::compilationUnit() const
extern "C" Q_DECL_EXPORT
QV4::CompiledData::CompilationUnit *ritual_ZNK12QQmlTypeData15compilationUnitEv(
    const QQmlTypeData *self) {
  return self->compilationUnit();
}

//  QQmlType QQmlTypeData::qmlType(const QString &inlineComponentName) const
extern "C" Q_DECL_EXPORT
QQmlType *ritual_ZNK12QQmlTypeData7qmlTypeERK7QString(
    const QQmlTypeData *self,
    const QString *inlineComponentName) {
  return new QQmlType(self->qmlType(*inlineComponentName));
}

//  QByteArray QQmlTypeData::typeClassName() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK12QQmlTypeData13typeClassNameEv(
    const QQmlTypeData *self) {
  return new QByteArray(self->typeClassName());
}

//  SourceCodeData QQmlTypeData::backupSourceCode() const
extern "C" Q_DECL_EXPORT
QQmlDataBlob::SourceCodeData *ritual_ZNK12QQmlTypeData16backupSourceCodeEv(
    const QQmlTypeData *self) {
  return new QQmlDataBlob::SourceCodeData(self->backupSourceCode());
}

//  void QQmlTypeData::dataReceived(const SourceCodeData &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlTypeData12dataReceivedERKN12QQmlDataBlob14SourceCodeDataE(
    QQmlTypeData *self,
    const QQmlDataBlob::SourceCodeData *a0) {
  self->dataReceived(*a0);
}

//  void QQmlTypeData::initializeFromCachedUnit(const
//      QQmlPrivate::CachedQmlUnit *unit)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlTypeData24initializeFromCachedUnitEPKN11QQmlPrivate13CachedQmlUnitE(
    QQmlTypeData *self,
    const QQmlPrivate::CachedQmlUnit *unit) {
  self->initializeFromCachedUnit(unit);
}

//  void QQmlTypeData::allDependenciesDone()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlTypeData19allDependenciesDoneEv(QQmlTypeData *self) {
  self->allDependenciesDone();
}

//  QString QQmlTypeData::stringAt(int index) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QQmlTypeData8stringAtEi(
    const QQmlTypeData *self,
    int index) {
  return new QString(self->stringAt(index));
}

//  bool QQmlTypeData::checkScripts()
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QQmlTypeData12checkScriptsEv(QQmlTypeData *self) {
  return self->checkScripts();
}

//  bool QQmlTypeData::checkDependencies()
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QQmlTypeData17checkDependenciesEv(QQmlTypeData *self) {
  return self->checkDependencies();
}

//  void QQmlTypeData::createError(const TypeReference &type, const QString
//      &message)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlTypeData11createErrorERKNS_13TypeReferenceERK7QString(
    QQmlTypeData *self,
    const QQmlTypeData::TypeReference *type,
    const QString *message) {
  self->createError(*type, *message);
}

//  void QQmlTypeData::createError(const ScriptReference &script, const
//      QString &message)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlTypeData11createErrorERKNS_15ScriptReferenceERK7QString(
    QQmlTypeData *self,
    const QQmlTypeData::ScriptReference *script,
    const QString *message) {
  self->createError(*script, *message);
}

//  bool QQmlTypeData::checkCompositeSingletons()
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QQmlTypeData24checkCompositeSingletonsEv(
    QQmlTypeData *self) {
  return self->checkCompositeSingletons();
}

//  a Python function taken by a CuteQQmlTypeData, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlTypeData(
    QQmlTypeData *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlTypeData *>(self)->take(key, call);
}

//  QString QQmlTypeData::stringAt(int index) const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK12QQmlTypeData8stringAtEi(
    const QQmlTypeData *self,
    int index) {
  return new QString(
      static_cast<const OwnQQmlTypeData *>(self)->OwnQQmlTypeData::stringAt(
          index));
}
