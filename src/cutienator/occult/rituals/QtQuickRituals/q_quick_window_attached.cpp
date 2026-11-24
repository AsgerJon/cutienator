//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickwindowattached_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickwindowattached_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  const QMetaObject *QQuickWindowAttached::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QQuickWindowAttached10metaObjectEv(
    const QQuickWindowAttached *self) {
  return self->metaObject();
}

//  QString QQuickWindowAttached::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QQuickWindowAttached2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickWindowAttached::tr(s, c, n));
}

//  void QQuickWindowAttached::qt_qmlMarker_anonymous()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickWindowAttached22qt_qmlMarker_anonymousEv(
    QQuickWindowAttached *self) {
  self->qt_qmlMarker_anonymous();
}

//  QQuickWindowAttached::QQuickWindowAttached(QObject *attachee)
extern "C" Q_DECL_EXPORT
QQuickWindowAttached *ritual_ZN20QQuickWindowAttachedC1EP7QObject(
    QObject *attachee) {
  return new QQuickWindowAttached(attachee);
}

//  QWindow::Visibility QQuickWindowAttached::visibility() const
extern "C" Q_DECL_EXPORT
QWindow::Visibility ritual_ZNK20QQuickWindowAttached10visibilityEv(
    const QQuickWindowAttached *self) {
  return self->visibility();
}

//  bool QQuickWindowAttached::isActive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QQuickWindowAttached8isActiveEv(
    const QQuickWindowAttached *self) {
  return self->isActive();
}

//  QQuickItem *QQuickWindowAttached::activeFocusItem() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK20QQuickWindowAttached15activeFocusItemEv(
    const QQuickWindowAttached *self) {
  return self->activeFocusItem();
}

//  QQuickItem *QQuickWindowAttached::contentItem() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK20QQuickWindowAttached11contentItemEv(
    const QQuickWindowAttached *self) {
  return self->contentItem();
}

//  int QQuickWindowAttached::width() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QQuickWindowAttached5widthEv(
    const QQuickWindowAttached *self) {
  return self->width();
}

//  int QQuickWindowAttached::height() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QQuickWindowAttached6heightEv(
    const QQuickWindowAttached *self) {
  return self->height();
}

//  QQuickWindow *QQuickWindowAttached::window() const
extern "C" Q_DECL_EXPORT
QQuickWindow *ritual_ZNK20QQuickWindowAttached6windowEv(
    const QQuickWindowAttached *self) {
  return self->window();
}

//  void QQuickWindowAttached::windowChange(QQuickWindow *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickWindowAttached12windowChangeEP12QQuickWindow(
    QQuickWindowAttached *self,
    QQuickWindow *a0) {
  self->windowChange(a0);
}
