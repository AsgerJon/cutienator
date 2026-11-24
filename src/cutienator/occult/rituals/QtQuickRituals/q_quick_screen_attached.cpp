//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickscreen_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickscreen_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  const QMetaObject *QQuickScreenAttached::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QQuickScreenAttached10metaObjectEv(
    const QQuickScreenAttached *self) {
  return self->metaObject();
}

//  QString QQuickScreenAttached::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QQuickScreenAttached2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickScreenAttached::tr(s, c, n));
}

//  void QQuickScreenAttached::qt_qmlMarker_anonymous()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickScreenAttached22qt_qmlMarker_anonymousEv(
    QQuickScreenAttached *self) {
  self->qt_qmlMarker_anonymous();
}

//  QQuickScreenAttached::QQuickScreenAttached(QObject *attachee)
extern "C" Q_DECL_EXPORT
QQuickScreenAttached *ritual_ZN20QQuickScreenAttachedC1EP7QObject(
    QObject *attachee) {
  return new QQuickScreenAttached(attachee);
}

//  int QQuickScreenAttached::angleBetween(int a, int b)
extern "C" Q_DECL_EXPORT
int ritual_ZN20QQuickScreenAttached12angleBetweenEii(
    QQuickScreenAttached *self,
    int a,
    int b) {
  return self->angleBetween(a, b);
}

//  void QQuickScreenAttached::windowChanged(QQuickWindow *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickScreenAttached13windowChangedEP12QQuickWindow(
    QQuickScreenAttached *self,
    QQuickWindow *a0) {
  self->windowChanged(a0);
}

//  void QQuickScreenAttached::screenChanged(QScreen *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickScreenAttached13screenChangedEP7QScreen(
    QQuickScreenAttached *self,
    QScreen *a0) {
  self->screenChanged(a0);
}
