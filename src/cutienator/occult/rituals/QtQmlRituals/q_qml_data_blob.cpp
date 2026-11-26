//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmldatablob_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmldatablob_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qurl.h>
#include <QtCore/qstring.h>
#include <QtQml/qqmlerror.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmljsdiagnosticmessage_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on QQmlDataBlob may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQmlDataBlob : QQmlDataBlob {
  using QQmlDataBlob::done;
  using QQmlDataBlob::networkError;
  using QQmlDataBlob::allDependenciesDone;
  using QQmlDataBlob::downloadProgressChanged;
  using QQmlDataBlob::completed;
};

//  A QQmlDataBlob that Python can take functions over in. Every QQmlDataBlob
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQmlDataBlobCall0)(const void *, const QQmlDataBlob::SourceCodeData *, int *);
typedef void (*CuteQQmlDataBlobCall1)(const void *, const QQmlPrivate::CachedQmlUnit *, int *);
typedef void (*CuteQQmlDataBlobCall2)(const void *, int *);
#if QT_CONFIG(qml_network)
typedef void (*CuteQQmlDataBlobCall3)(const void *, int, int *);
#endif  // QT_CONFIG(qml_network)
typedef void (*CuteQQmlDataBlobCall4)(const void *, int *);
typedef void (*CuteQQmlDataBlobCall5)(const void *, qreal, int *);
typedef void (*CuteQQmlDataBlobCall6)(const void *, int *);
class CuteQQmlDataBlob : public QQmlDataBlob {
public:
  using QQmlDataBlob::QQmlDataBlob;
  void *taken[7] = {};

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
#if QT_CONFIG(qml_network)
    if (!std::strcmp(key, "_ZN12QQmlDataBlob12networkErrorEN13QNetworkReply12NetworkErrorE")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_network)
    if (!std::strcmp(key, "_ZN12QQmlDataBlob19allDependenciesDoneEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QQmlDataBlob23downloadProgressChangedEd")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QQmlDataBlob9completedEv")) {
      taken[6] = call;
      return true;
    }
    return false;
  }

  //  void QQmlDataBlob::dataReceived(const SourceCodeData &a0)
  void dataReceived(const QQmlDataBlob::SourceCodeData &a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlDataBlobCall0 call = reinterpret_cast<CuteQQmlDataBlobCall0>(taken[0]);
      call(this, &a0, &handled);
      if (handled) return;
    }
  }

  //  void QQmlDataBlob::initializeFromCachedUnit(const
  //      QQmlPrivate::CachedQmlUnit *a0)
  void initializeFromCachedUnit(
      const QQmlPrivate::CachedQmlUnit *a0) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQmlDataBlobCall1 call = reinterpret_cast<CuteQQmlDataBlobCall1>(taken[1]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  void QQmlDataBlob::done()
  void done() override {
    if (taken[2]) {
      int handled = 0;
      CuteQQmlDataBlobCall2 call = reinterpret_cast<CuteQQmlDataBlobCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlDataBlob::done();
  }

#if QT_CONFIG(qml_network)
  //  void QQmlDataBlob::networkError(QNetworkReply::NetworkError a0)
  void networkError(QNetworkReply::NetworkError a0) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQmlDataBlobCall3 call = reinterpret_cast<CuteQQmlDataBlobCall3>(taken[3]);
      call(this, static_cast<int>(a0), &handled);
      if (handled) return;
    }
    QQmlDataBlob::networkError(a0);
  }
#endif  // QT_CONFIG(qml_network)

  //  void QQmlDataBlob::allDependenciesDone()
  void allDependenciesDone() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQmlDataBlobCall4 call = reinterpret_cast<CuteQQmlDataBlobCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlDataBlob::allDependenciesDone();
  }

  //  void QQmlDataBlob::downloadProgressChanged(qreal a0)
  void downloadProgressChanged(qreal a0) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQmlDataBlobCall5 call = reinterpret_cast<CuteQQmlDataBlobCall5>(taken[5]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlDataBlob::downloadProgressChanged(a0);
  }

  //  void QQmlDataBlob::completed()
  void completed() override {
    if (taken[6]) {
      int handled = 0;
      CuteQQmlDataBlobCall6 call = reinterpret_cast<CuteQQmlDataBlobCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlDataBlob::completed();
  }
};

//  QQmlDataBlob::QQmlDataBlob(const QUrl &a0, Type a1, QQmlTypeLoader
//      *manager)
extern "C" Q_DECL_EXPORT
QQmlDataBlob *ritual_ZN12QQmlDataBlobC1ERK4QUrlNS_4TypeEP14QQmlTypeLoader(
    const QUrl *a0,
    QQmlDataBlob::Type a1,
    QQmlTypeLoader *manager) {
  return new CuteQQmlDataBlob(*a0, a1, manager);
}

//  QQmlDataBlob::~QQmlDataBlob()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlDataBlobD1Ev(QQmlDataBlob *self) {
  delete self;
}

//  void QQmlDataBlob::startLoading()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlDataBlob12startLoadingEv(QQmlDataBlob *self) {
  self->startLoading();
}

//  QQmlTypeLoader *QQmlDataBlob::typeLoader() const
extern "C" Q_DECL_EXPORT
QQmlTypeLoader *ritual_ZNK12QQmlDataBlob10typeLoaderEv(
    const QQmlDataBlob *self) {
  return self->typeLoader();
}

//  void QQmlDataBlob::resetTypeLoader()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlDataBlob15resetTypeLoaderEv(QQmlDataBlob *self) {
  self->resetTypeLoader();
}

//  Type QQmlDataBlob::type() const
extern "C" Q_DECL_EXPORT
QQmlDataBlob::Type ritual_ZNK12QQmlDataBlob4typeEv(
    const QQmlDataBlob *self) {
  return self->type();
}

//  Status QQmlDataBlob::status() const
extern "C" Q_DECL_EXPORT
QQmlDataBlob::Status ritual_ZNK12QQmlDataBlob6statusEv(
    const QQmlDataBlob *self) {
  return self->status();
}

//  bool QQmlDataBlob::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QQmlDataBlob6isNullEv(const QQmlDataBlob *self) {
  return self->isNull();
}

//  bool QQmlDataBlob::isLoading() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QQmlDataBlob9isLoadingEv(const QQmlDataBlob *self) {
  return self->isLoading();
}

//  bool QQmlDataBlob::isWaiting() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QQmlDataBlob9isWaitingEv(const QQmlDataBlob *self) {
  return self->isWaiting();
}

//  bool QQmlDataBlob::isComplete() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QQmlDataBlob10isCompleteEv(const QQmlDataBlob *self) {
  return self->isComplete();
}

//  bool QQmlDataBlob::isError() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QQmlDataBlob7isErrorEv(const QQmlDataBlob *self) {
  return self->isError();
}

//  bool QQmlDataBlob::isCompleteOrError() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QQmlDataBlob17isCompleteOrErrorEv(
    const QQmlDataBlob *self) {
  return self->isCompleteOrError();
}

//  bool QQmlDataBlob::isAsync() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QQmlDataBlob7isAsyncEv(const QQmlDataBlob *self) {
  return self->isAsync();
}

//  qreal QQmlDataBlob::progress() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK12QQmlDataBlob8progressEv(const QQmlDataBlob *self) {
  return self->progress();
}

//  QUrl QQmlDataBlob::url() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK12QQmlDataBlob3urlEv(const QQmlDataBlob *self) {
  return new QUrl(self->url());
}

//  QString QQmlDataBlob::urlString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QQmlDataBlob9urlStringEv(const QQmlDataBlob *self) {
  return new QString(self->urlString());
}

//  QUrl QQmlDataBlob::finalUrl() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK12QQmlDataBlob8finalUrlEv(const QQmlDataBlob *self) {
  return new QUrl(self->finalUrl());
}

//  QString QQmlDataBlob::finalUrlString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QQmlDataBlob14finalUrlStringEv(
    const QQmlDataBlob *self) {
  return new QString(self->finalUrlString());
}

//  QList<QQmlError> QQmlDataBlob::errors() const
extern "C" Q_DECL_EXPORT
QList<QQmlError> *ritual_ZNK12QQmlDataBlob6errorsEv(
    const QQmlDataBlob *self) {
  return new QList<QQmlError>(self->errors());
}

//  void QQmlDataBlob::setError(const QQmlError &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlDataBlob8setErrorERK9QQmlError(
    QQmlDataBlob *self,
    const QQmlError *a0) {
  self->setError(*a0);
}

//  void QQmlDataBlob::setError(const QList<QQmlError> &errors)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlDataBlob8setErrorERK5QListI9QQmlErrorE(
    QQmlDataBlob *self,
    const QList<QQmlError> *errors) {
  self->setError(*errors);
}

//  void QQmlDataBlob::setError(const QQmlJS::DiagnosticMessage &error)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlDataBlob8setErrorERKN6QQmlJS17DiagnosticMessageE(
    QQmlDataBlob *self,
    const QQmlJS::DiagnosticMessage *error) {
  self->setError(*error);
}

//  void QQmlDataBlob::setError(const QString &description)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlDataBlob8setErrorERK7QString(
    QQmlDataBlob *self,
    const QString *description) {
  self->setError(*description);
}

//  void QQmlDataBlob::addDependency(const QQmlDataBlob::Ptr &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlDataBlob13addDependencyERK14QQmlRefPointerIS_E(
    QQmlDataBlob *self,
    const QQmlDataBlob::Ptr *a0) {
  self->addDependency(*a0);
}

//  void QQmlDataBlob::dataReceived(const SourceCodeData &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlDataBlob12dataReceivedERKNS_14SourceCodeDataE(
    QQmlDataBlob *self,
    const QQmlDataBlob::SourceCodeData *a0) {
  self->dataReceived(*a0);
}

//  void QQmlDataBlob::initializeFromCachedUnit(const
//      QQmlPrivate::CachedQmlUnit *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlDataBlob24initializeFromCachedUnitEPKN11QQmlPrivate13CachedQmlUnitE(
    QQmlDataBlob *self,
    const QQmlPrivate::CachedQmlUnit *a0) {
  self->initializeFromCachedUnit(a0);
}

//  void QQmlDataBlob::done()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlDataBlob4doneEv(QQmlDataBlob *self) {
  self->done();
}

#if QT_CONFIG(qml_network)
//  void QQmlDataBlob::networkError(QNetworkReply::NetworkError a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlDataBlob12networkErrorEN13QNetworkReply12NetworkErrorE(
    QQmlDataBlob *self,
    QNetworkReply::NetworkError a0) {
  self->networkError(a0);
}
#endif  // QT_CONFIG(qml_network)

//  void QQmlDataBlob::dependencyError(const QQmlDataBlob::Ptr &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlDataBlob15dependencyErrorERK14QQmlRefPointerIS_E(
    QQmlDataBlob *self,
    const QQmlDataBlob::Ptr *a0) {
  self->dependencyError(*a0);
}

//  void QQmlDataBlob::dependencyComplete(const QQmlDataBlob::Ptr &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlDataBlob18dependencyCompleteERK14QQmlRefPointerIS_E(
    QQmlDataBlob *self,
    const QQmlDataBlob::Ptr *a0) {
  self->dependencyComplete(*a0);
}

//  void QQmlDataBlob::allDependenciesDone()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlDataBlob19allDependenciesDoneEv(QQmlDataBlob *self) {
  self->allDependenciesDone();
}

//  void QQmlDataBlob::downloadProgressChanged(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlDataBlob23downloadProgressChangedEd(
    QQmlDataBlob *self,
    qreal a0) {
  self->downloadProgressChanged(a0);
}

//  void QQmlDataBlob::completed()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlDataBlob9completedEv(QQmlDataBlob *self) {
  self->completed();
}

//  void QQmlDataBlob::tryDone()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlDataBlob7tryDoneEv(QQmlDataBlob *self) {
  self->tryDone();
}

//  void QQmlDataBlob::cancelAllWaitingFor()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlDataBlob19cancelAllWaitingForEv(QQmlDataBlob *self) {
  self->cancelAllWaitingFor();
}

//  void QQmlDataBlob::notifyAllWaitingOnMe()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlDataBlob20notifyAllWaitingOnMeEv(QQmlDataBlob *self) {
  self->notifyAllWaitingOnMe();
}

//  void QQmlDataBlob::notifyComplete(const QQmlDataBlob::Ptr &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlDataBlob14notifyCompleteERK14QQmlRefPointerIS_E(
    QQmlDataBlob *self,
    const QQmlDataBlob::Ptr *a0) {
  self->notifyComplete(*a0);
}

//  bool QQmlDataBlob::setStatus(Status status)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QQmlDataBlob9setStatusENS_6StatusE(
    QQmlDataBlob *self,
    QQmlDataBlob::Status status) {
  return self->setStatus(status);
}

//  bool QQmlDataBlob::setIsAsync(bool async)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QQmlDataBlob10setIsAsyncEb(QQmlDataBlob *self, bool async) {
  return self->setIsAsync(async);
}

//  bool QQmlDataBlob::setProgress(qreal progress)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QQmlDataBlob11setProgressEd(
    QQmlDataBlob *self,
    qreal progress) {
  return self->setProgress(progress);
}

//  a Python function taken by a CuteQQmlDataBlob, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlDataBlob(
    QQmlDataBlob *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlDataBlob *>(self)->take(key, call);
}

//  void QQmlDataBlob::done()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QQmlDataBlob4doneEv(QQmlDataBlob *self) {
  static_cast<OwnQQmlDataBlob *>(self)->OwnQQmlDataBlob::done();
}

#if QT_CONFIG(qml_network)
//  void QQmlDataBlob::networkError(QNetworkReply::NetworkError a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QQmlDataBlob12networkErrorEN13QNetworkReply12NetworkErrorE(
    QQmlDataBlob *self,
    QNetworkReply::NetworkError a0) {
  static_cast<OwnQQmlDataBlob *>(self)->OwnQQmlDataBlob::networkError(a0);
}
#endif  // QT_CONFIG(qml_network)

//  void QQmlDataBlob::allDependenciesDone()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QQmlDataBlob19allDependenciesDoneEv(QQmlDataBlob *self) {
  static_cast<OwnQQmlDataBlob *>(self)->OwnQQmlDataBlob::allDependenciesDone();
}

//  void QQmlDataBlob::downloadProgressChanged(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QQmlDataBlob23downloadProgressChangedEd(
    QQmlDataBlob *self,
    qreal a0) {
  static_cast<OwnQQmlDataBlob *>(self)->OwnQQmlDataBlob::downloadProgressChanged(
      a0);
}

//  void QQmlDataBlob::completed()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QQmlDataBlob9completedEv(QQmlDataBlob *self) {
  static_cast<OwnQQmlDataBlob *>(self)->OwnQQmlDataBlob::completed();
}
