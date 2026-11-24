//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickevents_p_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickevents_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  const QMetaObject *QQuickCloseEvent::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QQuickCloseEvent10metaObjectEv(
    const QQuickCloseEvent *self) {
  return self->metaObject();
}

//  QString QQuickCloseEvent::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QQuickCloseEvent2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickCloseEvent::tr(s, c, n));
}

//  void QQuickCloseEvent::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickCloseEvent24qt_qmlMarker_uncreatableEv(
    QQuickCloseEvent *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QQuickCloseEvent::QQuickCloseEvent()
extern "C" Q_DECL_EXPORT
QQuickCloseEvent *ritual_ZN16QQuickCloseEventC1Ev() {
  return new QQuickCloseEvent();
}

//  bool QQuickCloseEvent::isAccepted()
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QQuickCloseEvent10isAcceptedEv(QQuickCloseEvent *self) {
  return self->isAccepted();
}

//  void QQuickCloseEvent::setAccepted(bool accepted)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickCloseEvent11setAcceptedEb(
    QQuickCloseEvent *self,
    bool accepted) {
  self->setAccepted(accepted);
}
