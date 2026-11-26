//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmltypeloader_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmltypeloader_p.h>
#include <QtQml/6.12.0/QtQml/private/qqmltypeloaderqmldircontent_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qurl.h>
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4compileddata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qtyperevision.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmldatablob_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  Only a class built on QQmlTypeLoader::Blob may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQmlTypeLoader_Blob : QQmlTypeLoader::Blob {
  using QQmlTypeLoader::Blob::stringAt;
};

//  A QQmlTypeLoader::Blob that Python can take functions over in. Every QQmlTypeLoader::Blob
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef QString * (*CuteQQmlTypeLoader_BlobCall0)(const void *, int, int *);
typedef void (*CuteQQmlTypeLoader_BlobCall1)(const void *, const QQmlDataBlob::SourceCodeData *, int *);
typedef void (*CuteQQmlTypeLoader_BlobCall2)(const void *, const QQmlPrivate::CachedQmlUnit *, int *);
typedef void (*CuteQQmlTypeLoader_BlobCall3)(const void *, int *);
#if QT_CONFIG(qml_network)
typedef void (*CuteQQmlTypeLoader_BlobCall4)(const void *, int, int *);
#endif  // QT_CONFIG(qml_network)
typedef void (*CuteQQmlTypeLoader_BlobCall5)(const void *, int *);
typedef void (*CuteQQmlTypeLoader_BlobCall6)(const void *, qreal, int *);
typedef void (*CuteQQmlTypeLoader_BlobCall7)(const void *, int *);
class CuteQQmlTypeLoader_Blob : public QQmlTypeLoader::Blob {
public:
  using QQmlTypeLoader::Blob::Blob;
  void *taken[8] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK14QQmlTypeLoader4Blob8stringAtEi")) {
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
    if (!std::strcmp(key, "_ZN12QQmlDataBlob4doneEv")) {
      taken[3] = call;
      return true;
    }
#if QT_CONFIG(qml_network)
    if (!std::strcmp(key, "_ZN12QQmlDataBlob12networkErrorEN13QNetworkReply12NetworkErrorE")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_network)
    if (!std::strcmp(key, "_ZN12QQmlDataBlob19allDependenciesDoneEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QQmlDataBlob23downloadProgressChangedEd")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QQmlDataBlob9completedEv")) {
      taken[7] = call;
      return true;
    }
    return false;
  }

  //  QString QQmlTypeLoader::Blob::stringAt(int a0) const
  QString stringAt(int a0) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlTypeLoader_BlobCall0 call = reinterpret_cast<CuteQQmlTypeLoader_BlobCall0>(taken[0]);
      QString * given = call(this, a0, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QQmlTypeLoader::Blob::stringAt(a0);
  }

  //  void QQmlDataBlob::dataReceived(const SourceCodeData &a0)
  void dataReceived(const QQmlDataBlob::SourceCodeData &a0) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQmlTypeLoader_BlobCall1 call = reinterpret_cast<CuteQQmlTypeLoader_BlobCall1>(taken[1]);
      call(this, &a0, &handled);
      if (handled) return;
    }
  }

  //  void QQmlDataBlob::initializeFromCachedUnit(const
  //      QQmlPrivate::CachedQmlUnit *a0)
  void initializeFromCachedUnit(
      const QQmlPrivate::CachedQmlUnit *a0) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQmlTypeLoader_BlobCall2 call = reinterpret_cast<CuteQQmlTypeLoader_BlobCall2>(taken[2]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  void QQmlDataBlob::done()
  void done() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQmlTypeLoader_BlobCall3 call = reinterpret_cast<CuteQQmlTypeLoader_BlobCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlDataBlob::done();
  }

#if QT_CONFIG(qml_network)
  //  void QQmlDataBlob::networkError(QNetworkReply::NetworkError a0)
  void networkError(QNetworkReply::NetworkError a0) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQmlTypeLoader_BlobCall4 call = reinterpret_cast<CuteQQmlTypeLoader_BlobCall4>(taken[4]);
      call(this, static_cast<int>(a0), &handled);
      if (handled) return;
    }
    QQmlDataBlob::networkError(a0);
  }
#endif  // QT_CONFIG(qml_network)

  //  void QQmlDataBlob::allDependenciesDone()
  void allDependenciesDone() override {
    if (taken[5]) {
      int handled = 0;
      CuteQQmlTypeLoader_BlobCall5 call = reinterpret_cast<CuteQQmlTypeLoader_BlobCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlDataBlob::allDependenciesDone();
  }

  //  void QQmlDataBlob::downloadProgressChanged(qreal a0)
  void downloadProgressChanged(qreal a0) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQmlTypeLoader_BlobCall6 call = reinterpret_cast<CuteQQmlTypeLoader_BlobCall6>(taken[6]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlDataBlob::downloadProgressChanged(a0);
  }

  //  void QQmlDataBlob::completed()
  void completed() override {
    if (taken[7]) {
      int handled = 0;
      CuteQQmlTypeLoader_BlobCall7 call = reinterpret_cast<CuteQQmlTypeLoader_BlobCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlDataBlob::completed();
  }
};

//  QQmlTypeLoader::Blob::~Blob()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlTypeLoader4BlobD1Ev(QQmlTypeLoader::Blob *self) {
  delete self;
}

//  const QQmlImports *QQmlTypeLoader::Blob::imports() const
extern "C" Q_DECL_EXPORT
const QQmlImports *ritual_ZNK14QQmlTypeLoader4Blob7importsEv(
    const QQmlTypeLoader::Blob *self) {
  return self->imports();
}

//  void QQmlTypeLoader::Blob::setCachedUnitStatus(QQmlMetaType::CachedUnitLo
//      okupError status)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlTypeLoader4Blob19setCachedUnitStatusEN12QQmlMetaType21CachedUnitLookupErrorE(
    QQmlTypeLoader::Blob *self,
    QQmlMetaType::CachedUnitLookupError status) {
  self->setCachedUnitStatus(status);
}

//  void QQmlTypeLoader::Blob::importQmldirScripts(const PendingImportPtr
//      &import, const QQmlTypeLoaderQmldirContent &qmldir, const QUrl
//      &qmldirUrl)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlTypeLoader4Blob19importQmldirScriptsERKSt10shared_ptrINS0_13PendingImportEERK27QQmlTypeLoaderQmldirContentRK4QUrl(
    QQmlTypeLoader::Blob *self,
    const QQmlTypeLoader::Blob::PendingImportPtr *import,
    const QQmlTypeLoaderQmldirContent *qmldir,
    const QUrl *qmldirUrl) {
  self->importQmldirScripts(*import, *qmldir, *qmldirUrl);
}

//  bool QQmlTypeLoader::Blob::handleLocalQmldirForImport(const
//      PendingImportPtr &import, const QString &qmldirFilePath, const
//      QString &qmldirUrl, QList<QQmlError> *errors)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QQmlTypeLoader4Blob26handleLocalQmldirForImportERKSt10shared_ptrINS0_13PendingImportEERK7QStringS8_P5QListI9QQmlErrorE(
    QQmlTypeLoader::Blob *self,
    const QQmlTypeLoader::Blob::PendingImportPtr *import,
    const QString *qmldirFilePath,
    const QString *qmldirUrl,
    QList<QQmlError> *errors) {
  return self->handleLocalQmldirForImport(
      *import,
      *qmldirFilePath,
      *qmldirUrl,
      errors);
}

//  bool QQmlTypeLoader::Blob::addImport(const QV4::CompiledData::Import
//      *import, QQmlImports::ImportFlags a1, QList<QQmlError> *errors)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QQmlTypeLoader4Blob9addImportEPKN3QV412CompiledData6ImportE6QFlagsIN11QQmlImports10ImportFlagEEP5QListI9QQmlErrorE(
    QQmlTypeLoader::Blob *self,
    const QV4::CompiledData::Import *import,
    int a1,
    QList<QQmlError> *errors) {
  return self->addImport(
      import,
      QFlags<QQmlImports::ImportFlag>::fromInt(a1),
      errors);
}

//  bool QQmlTypeLoader::Blob::addImport(const PendingImportPtr &import,
//      QList<QQmlError> *errors)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QQmlTypeLoader4Blob9addImportERKSt10shared_ptrINS0_13PendingImportEEP5QListI9QQmlErrorE(
    QQmlTypeLoader::Blob *self,
    const QQmlTypeLoader::Blob::PendingImportPtr *import,
    QList<QQmlError> *errors) {
  return self->addImport(*import, errors);
}

//  bool QQmlTypeLoader::Blob::fetchQmldir(const QUrl &url, const
//      PendingImportPtr &import, int priority, QList<QQmlError> *errors)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QQmlTypeLoader4Blob11fetchQmldirERK4QUrlRKSt10shared_ptrINS0_13PendingImportEEiP5QListI9QQmlErrorE(
    QQmlTypeLoader::Blob *self,
    const QUrl *url,
    const QQmlTypeLoader::Blob::PendingImportPtr *import,
    int priority,
    QList<QQmlError> *errors) {
  return self->fetchQmldir(*url, *import, priority, errors);
}

//  bool QQmlTypeLoader::Blob::updateQmldir(const
//      QQmlRefPointer<QQmlQmldirData> &data, const PendingImportPtr &import,
//      QList<QQmlError> *errors)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QQmlTypeLoader4Blob12updateQmldirERK14QQmlRefPointerI14QQmlQmldirDataERKSt10shared_ptrINS0_13PendingImportEEP5QListI9QQmlErrorE(
    QQmlTypeLoader::Blob *self,
    const QQmlRefPointer<QQmlQmldirData> *data,
    const QQmlTypeLoader::Blob::PendingImportPtr *import,
    QList<QQmlError> *errors) {
  return self->updateQmldir(*data, *import, errors);
}

//  bool QQmlTypeLoader::Blob::addScriptImport(const PendingImportPtr
//      &import)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QQmlTypeLoader4Blob15addScriptImportERKSt10shared_ptrINS0_13PendingImportEE(
    QQmlTypeLoader::Blob *self,
    const QQmlTypeLoader::Blob::PendingImportPtr *import) {
  return self->addScriptImport(*import);
}

//  bool QQmlTypeLoader::Blob::addFileImport(const PendingImportPtr &import,
//      QList<QQmlError> *errors)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QQmlTypeLoader4Blob13addFileImportERKSt10shared_ptrINS0_13PendingImportEEP5QListI9QQmlErrorE(
    QQmlTypeLoader::Blob *self,
    const QQmlTypeLoader::Blob::PendingImportPtr *import,
    QList<QQmlError> *errors) {
  return self->addFileImport(*import, errors);
}

//  bool QQmlTypeLoader::Blob::addLibraryImport(const PendingImportPtr
//      &import, QList<QQmlError> *errors)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QQmlTypeLoader4Blob16addLibraryImportERKSt10shared_ptrINS0_13PendingImportEEP5QListI9QQmlErrorE(
    QQmlTypeLoader::Blob *self,
    const QQmlTypeLoader::Blob::PendingImportPtr *import,
    QList<QQmlError> *errors) {
  return self->addLibraryImport(*import, errors);
}

//  bool QQmlTypeLoader::Blob::qmldirDataAvailable(const
//      QQmlRefPointer<QQmlQmldirData> &a0, QList<QQmlError> *a1)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QQmlTypeLoader4Blob19qmldirDataAvailableERK14QQmlRefPointerI14QQmlQmldirDataEP5QListI9QQmlErrorE(
    QQmlTypeLoader::Blob *self,
    const QQmlRefPointer<QQmlQmldirData> *a0,
    QList<QQmlError> *a1) {
  return self->qmldirDataAvailable(*a0, a1);
}

//  void QQmlTypeLoader::Blob::scriptImported(const
//      QQmlRefPointer<QQmlScriptBlob> &a0, const QV4::CompiledData::Location
//      &a1, const QString &a2, const QString &a3)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlTypeLoader4Blob14scriptImportedERK14QQmlRefPointerI14QQmlScriptBlobERKN3QV412CompiledData8LocationERK7QStringSD_(
    QQmlTypeLoader::Blob *self,
    const QQmlRefPointer<QQmlScriptBlob> *a0,
    const QV4::CompiledData::Location *a1,
    const QString *a2,
    const QString *a3) {
  self->scriptImported(*a0, *a1, *a2, *a3);
}

//  void QQmlTypeLoader::Blob::dependencyComplete(const QQmlDataBlob::Ptr
//      &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlTypeLoader4Blob18dependencyCompleteERK14QQmlRefPointerI12QQmlDataBlobE(
    QQmlTypeLoader::Blob *self,
    const QQmlDataBlob::Ptr *a0) {
  self->dependencyComplete(*a0);
}

//  bool QQmlTypeLoader::Blob::loadImportDependencies(const PendingImportPtr
//      &currentImport, const QString &qmldirUri, QQmlImports::ImportFlags
//      flags, QList<QQmlError> *errors)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QQmlTypeLoader4Blob22loadImportDependenciesERKSt10shared_ptrINS0_13PendingImportEERK7QString6QFlagsIN11QQmlImports10ImportFlagEEP5QListI9QQmlErrorE(
    QQmlTypeLoader::Blob *self,
    const QQmlTypeLoader::Blob::PendingImportPtr *currentImport,
    const QString *qmldirUri,
    int flags,
    QList<QQmlError> *errors) {
  return self->loadImportDependencies(
      *currentImport,
      *qmldirUri,
      QFlags<QQmlImports::ImportFlag>::fromInt(flags),
      errors);
}

//  bool QQmlTypeLoader::Blob::registerPendingTypes(const PendingImportPtr
//      &import)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QQmlTypeLoader4Blob20registerPendingTypesERKSt10shared_ptrINS0_13PendingImportEE(
    QQmlTypeLoader::Blob *self,
    const QQmlTypeLoader::Blob::PendingImportPtr *import) {
  return self->registerPendingTypes(*import);
}

//  bool QQmlTypeLoader::Blob::loadDependentImports(const
//      QList<QQmlDirParser::Import> &imports, const QString &qualifier,
//      QTypeRevision version, quint8 precedence, QQmlImports::ImportFlags
//      flags, QList<QQmlError> *errors)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QQmlTypeLoader4Blob20loadDependentImportsERK5QListIN13QQmlDirParser6ImportEERK7QString13QTypeRevisionh6QFlagsIN11QQmlImports10ImportFlagEEPS1_I9QQmlErrorE(
    QQmlTypeLoader::Blob *self,
    const QList<QQmlDirParser::Import> *imports,
    const QString *qualifier,
    const QTypeRevision *version,
    quint8 precedence,
    int flags,
    QList<QQmlError> *errors) {
  return self->loadDependentImports(
      *imports,
      *qualifier,
      *version,
      precedence,
      QFlags<QQmlImports::ImportFlag>::fromInt(flags),
      errors);
}

//  QString QQmlTypeLoader::Blob::stringAt(int a0) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QQmlTypeLoader4Blob8stringAtEi(
    const QQmlTypeLoader::Blob *self,
    int a0) {
  return new QString(self->stringAt(a0));
}

//  a Python function taken by a CuteQQmlTypeLoader_Blob, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlTypeLoader_Blob(
    QQmlTypeLoader::Blob *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlTypeLoader_Blob *>(self)->take(key, call);
}

//  QString QQmlTypeLoader::Blob::stringAt(int a0) const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK14QQmlTypeLoader4Blob8stringAtEi(
    const QQmlTypeLoader::Blob *self,
    int a0) {
  return new QString(
      static_cast<const OwnQQmlTypeLoader_Blob *>(self)->OwnQQmlTypeLoader_Blob::stringAt(
          a0));
}
