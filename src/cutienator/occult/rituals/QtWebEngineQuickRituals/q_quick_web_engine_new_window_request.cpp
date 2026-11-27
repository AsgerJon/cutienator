//  Written by dev_tooling.RitualGenerator from the records of QtWebEngineQui
//  ck/6.12.0/QtWebEngineQuick/private/qquickwebenginenewwindowrequest_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtWebEngineQuick/6.12.0/QtWebEngineQuick/private/qtwebenginequickglobal_p.h>
#include <QtWebEngineQuick/QtWebEngineQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWebEngineQuick/6.12.0/QtWebEngineQuick/private/qquickwebenginenewwindowrequest_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtCore/qurl.h>
#include <QtCore/QRect>
#include <QtCore/QUrl>
#include <QtCore/QSharedPointer>
#include <QtWebEngineCore/QtWebEngineCore>

//  const QMetaObject *QQuickWebEngineNewWindowRequest::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK31QQuickWebEngineNewWindowRequest10metaObjectEv(
    const QQuickWebEngineNewWindowRequest *self) {
  return self->metaObject();
}

//  void *QQuickWebEngineNewWindowRequest::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN31QQuickWebEngineNewWindowRequest11qt_metacastEPKc(
    QQuickWebEngineNewWindowRequest *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickWebEngineNewWindowRequest::qt_metacall(QMetaObject::Call a0,
//      int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN31QQuickWebEngineNewWindowRequest11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickWebEngineNewWindowRequest *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickWebEngineNewWindowRequest::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN31QQuickWebEngineNewWindowRequest2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickWebEngineNewWindowRequest::tr(s, c, n));
}

//  void QQuickWebEngineNewWindowRequest::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQuickWebEngineNewWindowRequest24qt_qmlMarker_uncreatableEv(
    QQuickWebEngineNewWindowRequest *self) {
  self->qt_qmlMarker_uncreatable();
}

//  void QQuickWebEngineNewWindowRequest::openIn(QQuickWebEngineView *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQuickWebEngineNewWindowRequest6openInEP19QQuickWebEngineView(
    QQuickWebEngineNewWindowRequest *self,
    QQuickWebEngineView *a0) {
  self->openIn(a0);
}

//  QQuickWebEngineNewWindowRequest::QQuickWebEngineNewWindowRequest(Destinat
//      ionType a0, const QRect &a1, const QUrl &a2, bool a3,
//      QSharedPointer<QtWebEngineCore::WebContentsAdapter> a4, QObject *a5)
extern "C" Q_DECL_EXPORT
QQuickWebEngineNewWindowRequest *ritual_ZN31QQuickWebEngineNewWindowRequestC1EN26QWebEngineNewWindowRequest15DestinationTypeERK5QRectRK4QUrlb14QSharedPointerIN15QtWebEngineCore18WebContentsAdapterEEP7QObject(
    QWebEngineNewWindowRequest::DestinationType a0,
    const QRect *a1,
    const QUrl *a2,
    bool a3,
    const QSharedPointer<QtWebEngineCore::WebContentsAdapter> *a4,
    QObject *a5) {
  return new QQuickWebEngineNewWindowRequest(a0, *a1, *a2, a3, *a4, a5);
}
