//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmltypeloadernetworkreplyproxy_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQml/qtqmlglobal.h>
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#if QT_CONFIG(qml_network)
#if QT_CONFIG(qml_network)
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmltypeloadernetworkreplyproxy_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  const QMetaObject *QQmlTypeLoaderNetworkReplyProxy::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK31QQmlTypeLoaderNetworkReplyProxy10metaObjectEv(
    const QQmlTypeLoaderNetworkReplyProxy *self) {
  return self->metaObject();
}

//  void *QQmlTypeLoaderNetworkReplyProxy::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN31QQmlTypeLoaderNetworkReplyProxy11qt_metacastEPKc(
    QQmlTypeLoaderNetworkReplyProxy *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQmlTypeLoaderNetworkReplyProxy::qt_metacall(QMetaObject::Call a0,
//      int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN31QQmlTypeLoaderNetworkReplyProxy11qt_metacallEN11QMetaObject4CallEiPPv(
    QQmlTypeLoaderNetworkReplyProxy *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  void QQmlTypeLoaderNetworkReplyProxy::finished()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQmlTypeLoaderNetworkReplyProxy8finishedEv(
    QQmlTypeLoaderNetworkReplyProxy *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQmlTypeLoaderNetworkReplyProxy")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "finished()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "finished()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQmlTypeLoaderNetworkReplyProxy::downloadProgress(qint64 a0, qint64
//      a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQmlTypeLoaderNetworkReplyProxy16downloadProgressExx(
    QQmlTypeLoaderNetworkReplyProxy *self,
    qint64 a0,
    qint64 a1) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQmlTypeLoaderNetworkReplyProxy")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "downloadProgress(qint64,qint64)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "downloadProgress(qint64,qint64)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&a0)),
      const_cast<void *>(static_cast<const void *>(&a1)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQmlTypeLoaderNetworkReplyProxy::manualFinished(QNetworkReply *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQmlTypeLoaderNetworkReplyProxy14manualFinishedEP13QNetworkReply(
    QQmlTypeLoaderNetworkReplyProxy *self,
    QNetworkReply *a0) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQmlTypeLoaderNetworkReplyProxy")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "manualFinished(QNetworkReply *)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "manualFinished(QNetworkReply *)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&a0)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

#endif  // QT_CONFIG(qml_network)
#endif  // QT_CONFIG(qml_network)
