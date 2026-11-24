//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmljavascriptexpression_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmljavascriptexpression_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QQmlPropertyCapture::QQmlPropertyCapture(QQmlEngine *engine,
//      QQmlJavaScriptExpression *e, QQmlJavaScriptExpression::DeleteWatcher
//      *w)
extern "C" Q_DECL_EXPORT
QQmlPropertyCapture *ritual_ZN19QQmlPropertyCaptureC1EP10QQmlEngineP24QQmlJavaScriptExpressionPNS2_13DeleteWatcherE(
    QQmlEngine *engine,
    QQmlJavaScriptExpression *e,
    QQmlJavaScriptExpression::DeleteWatcher *w) {
  return new QQmlPropertyCapture(engine, e, w);
}

//  QQmlPropertyCapture::~QQmlPropertyCapture()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlPropertyCaptureD1Ev(QQmlPropertyCapture *self) {
  delete self;
}

//  void QQmlPropertyCapture::captureProperty(QQmlNotifier *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlPropertyCapture15capturePropertyEP12QQmlNotifier(
    QQmlPropertyCapture *self,
    QQmlNotifier *a0) {
  self->captureProperty(a0);
}

//  void QQmlPropertyCapture::captureProperty(QObject *a0, int a1, int a2,
//      bool doNotify)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlPropertyCapture15capturePropertyEP7QObjectiib(
    QQmlPropertyCapture *self,
    QObject *a0,
    int a1,
    int a2,
    bool doNotify) {
  self->captureProperty(a0, a1, a2, doNotify);
}

//  void QQmlPropertyCapture::captureProperty(QObject *a0, const
//      QQmlPropertyCache *a1, const QQmlPropertyData *a2, bool doNotify)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlPropertyCapture15capturePropertyEP7QObjectPK17QQmlPropertyCachePK16QQmlPropertyDatab(
    QQmlPropertyCapture *self,
    QObject *a0,
    const QQmlPropertyCache *a1,
    const QQmlPropertyData *a2,
    bool doNotify) {
  self->captureProperty(a0, a1, a2, doNotify);
}

//  void QQmlPropertyCapture::captureTranslation()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlPropertyCapture18captureTranslationEv(
    QQmlPropertyCapture *self) {
  self->captureTranslation();
}

//  void QQmlPropertyCapture::captureBindableProperty(QObject *o, const
//      QMetaObject *metaObjectForBindable, int c)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlPropertyCapture23captureBindablePropertyEP7QObjectPK11QMetaObjecti(
    QQmlPropertyCapture *self,
    QObject *o,
    const QMetaObject *metaObjectForBindable,
    int c) {
  self->captureBindableProperty(o, metaObjectForBindable, c);
}

//  void QQmlPropertyCapture::captureNonBindableProperty(QObject *o, int n,
//      int c, bool doNotify)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlPropertyCapture26captureNonBindablePropertyEP7QObjectiib(
    QQmlPropertyCapture *self,
    QObject *o,
    int n,
    int c,
    bool doNotify) {
  self->captureNonBindableProperty(o, n, c, doNotify);
}
