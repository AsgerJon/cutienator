//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DCore/6.12.0/Qt3DCore/private/qdownloadnetworkworker_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DCore/6.12.0/Qt3DCore/private/qt3dcore_global_p.h>
#include <Qt3DCore/Qt3DCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/6.12.0/Qt3DCore/private/qdownloadnetworkworker_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  const QMetaObject *Qt3DCore::QDownloadNetworkWorker::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK8Qt3DCore22QDownloadNetworkWorker10metaObjectEv(
    const Qt3DCore::QDownloadNetworkWorker *self) {
  return self->metaObject();
}

//  void *Qt3DCore::QDownloadNetworkWorker::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN8Qt3DCore22QDownloadNetworkWorker11qt_metacastEPKc(
    Qt3DCore::QDownloadNetworkWorker *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DCore::QDownloadNetworkWorker::qt_metacall(QMetaObject::Call a0,
//      int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN8Qt3DCore22QDownloadNetworkWorker11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DCore::QDownloadNetworkWorker *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  void Qt3DCore::QDownloadNetworkWorker::submitRequest(const
//      Qt3DCore::QDownloadRequestPtr &request)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore22QDownloadNetworkWorker13submitRequestERK14QSharedPointerINS_16QDownloadRequestEE(
    Qt3DCore::QDownloadNetworkWorker *self,
    const Qt3DCore::QDownloadRequestPtr *request) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "Qt3DCore::QDownloadNetworkWorker")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "submitRequest(const Qt3DCore::QDownloadRequestPtr &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "submitRequest(const Qt3DCore::QDownloadRequestPtr &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(request)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void Qt3DCore::QDownloadNetworkWorker::cancelRequest(const
//      Qt3DCore::QDownloadRequestPtr &request)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore22QDownloadNetworkWorker13cancelRequestERK14QSharedPointerINS_16QDownloadRequestEE(
    Qt3DCore::QDownloadNetworkWorker *self,
    const Qt3DCore::QDownloadRequestPtr *request) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "Qt3DCore::QDownloadNetworkWorker")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "cancelRequest(const Qt3DCore::QDownloadRequestPtr &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "cancelRequest(const Qt3DCore::QDownloadRequestPtr &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(request)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void Qt3DCore::QDownloadNetworkWorker::cancelAllRequests()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore22QDownloadNetworkWorker17cancelAllRequestsEv(
    Qt3DCore::QDownloadNetworkWorker *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "Qt3DCore::QDownloadNetworkWorker")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "cancelAllRequests()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "cancelAllRequests()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void Qt3DCore::QDownloadNetworkWorker::requestDownloaded(const
//      Qt3DCore::QDownloadRequestPtr &request)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore22QDownloadNetworkWorker17requestDownloadedERK14QSharedPointerINS_16QDownloadRequestEE(
    Qt3DCore::QDownloadNetworkWorker *self,
    const Qt3DCore::QDownloadRequestPtr *request) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "Qt3DCore::QDownloadNetworkWorker")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "requestDownloaded(const Qt3DCore::QDownloadRequestPtr &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "requestDownloaded(const Qt3DCore::QDownloadRequestPtr &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(request)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void Qt3DCore::QDownloadNetworkWorker::onRequestSubmited(const
//      Qt3DCore::QDownloadRequestPtr &request)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore22QDownloadNetworkWorker17onRequestSubmitedERK14QSharedPointerINS_16QDownloadRequestEE(
    Qt3DCore::QDownloadNetworkWorker *self,
    const Qt3DCore::QDownloadRequestPtr *request) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "Qt3DCore::QDownloadNetworkWorker")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "onRequestSubmited(const Qt3DCore::QDownloadRequestPtr &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "onRequestSubmited(const Qt3DCore::QDownloadRequestPtr &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(request)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void Qt3DCore::QDownloadNetworkWorker::onRequestCancelled(const
//      Qt3DCore::QDownloadRequestPtr &request)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore22QDownloadNetworkWorker18onRequestCancelledERK14QSharedPointerINS_16QDownloadRequestEE(
    Qt3DCore::QDownloadNetworkWorker *self,
    const Qt3DCore::QDownloadRequestPtr *request) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "Qt3DCore::QDownloadNetworkWorker")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "onRequestCancelled(const Qt3DCore::QDownloadRequestPtr &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "onRequestCancelled(const Qt3DCore::QDownloadRequestPtr &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(request)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void Qt3DCore::QDownloadNetworkWorker::onAllRequestsCancelled()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore22QDownloadNetworkWorker22onAllRequestsCancelledEv(
    Qt3DCore::QDownloadNetworkWorker *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "Qt3DCore::QDownloadNetworkWorker")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "onAllRequestsCancelled()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "onAllRequestsCancelled()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void Qt3DCore::QDownloadNetworkWorker::onRequestFinished(QNetworkReply
//      *reply)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore22QDownloadNetworkWorker17onRequestFinishedEP13QNetworkReply(
    Qt3DCore::QDownloadNetworkWorker *self,
    QNetworkReply *reply) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "Qt3DCore::QDownloadNetworkWorker")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "onRequestFinished(QNetworkReply *)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "onRequestFinished(QNetworkReply *)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&reply)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void Qt3DCore::QDownloadNetworkWorker::onDownloadProgressed(qint64
//      bytesReceived, qint64 bytesTotal)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore22QDownloadNetworkWorker20onDownloadProgressedExx(
    Qt3DCore::QDownloadNetworkWorker *self,
    qint64 bytesReceived,
    qint64 bytesTotal) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "Qt3DCore::QDownloadNetworkWorker")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "onDownloadProgressed(qint64,qint64)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "onDownloadProgressed(qint64,qint64)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&bytesReceived)),
      const_cast<void *>(static_cast<const void *>(&bytesTotal)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}
