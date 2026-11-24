//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmltypeloader_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmltypeloader_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
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
