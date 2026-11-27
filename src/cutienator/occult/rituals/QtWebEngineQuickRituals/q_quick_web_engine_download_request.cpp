//  Written by dev_tooling.RitualGenerator from the records of
//  QtWebEngineQuick/qquickwebenginedownloadrequest.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtWebEngineQuick/QtWebEngineQuick>
#include <QtWebEngineQuick/qquickwebenginedownloadrequest.h>
#include <QtCore/qstring.h>

//  const QMetaObject *QQuickWebEngineDownloadRequest::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK30QQuickWebEngineDownloadRequest10metaObjectEv(
    const QQuickWebEngineDownloadRequest *self) {
  return self->metaObject();
}

//  void *QQuickWebEngineDownloadRequest::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN30QQuickWebEngineDownloadRequest11qt_metacastEPKc(
    QQuickWebEngineDownloadRequest *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickWebEngineDownloadRequest::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN30QQuickWebEngineDownloadRequest11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickWebEngineDownloadRequest *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickWebEngineDownloadRequest::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN30QQuickWebEngineDownloadRequest2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickWebEngineDownloadRequest::tr(s, c, n));
}

//  void QQuickWebEngineDownloadRequest::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuickWebEngineDownloadRequest24qt_qmlMarker_uncreatableEv(
    QQuickWebEngineDownloadRequest *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QQuickWebEngineView *QQuickWebEngineDownloadRequest::view() const
extern "C" Q_DECL_EXPORT
QQuickWebEngineView *ritual_ZNK30QQuickWebEngineDownloadRequest4viewEv(
    const QQuickWebEngineDownloadRequest *self) {
  return self->view();
}

//  QQuickWebEngineDownloadRequest::QQuickWebEngineDownloadRequest(QWebEngine
//      DownloadRequestPrivate *a0, QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickWebEngineDownloadRequest *ritual_ZN30QQuickWebEngineDownloadRequestC1EP32QWebEngineDownloadRequestPrivateP7QObject(
    QWebEngineDownloadRequestPrivate *a0,
    QObject *parent) {
  return new QQuickWebEngineDownloadRequest(a0, parent);
}
