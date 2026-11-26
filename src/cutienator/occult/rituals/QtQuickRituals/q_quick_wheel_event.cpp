//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickevents_p_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(wheelevent)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickevents_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qpoint.h>

//  const QMetaObject *QQuickWheelEvent::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QQuickWheelEvent10metaObjectEv(
    const QQuickWheelEvent *self) {
  return self->metaObject();
}

//  void *QQuickWheelEvent::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN16QQuickWheelEvent11qt_metacastEPKc(
    QQuickWheelEvent *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickWheelEvent::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN16QQuickWheelEvent11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickWheelEvent *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickWheelEvent::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QQuickWheelEvent2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickWheelEvent::tr(s, c, n));
}

//  void QQuickWheelEvent::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickWheelEvent24qt_qmlMarker_uncreatableEv(
    QQuickWheelEvent *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QQuickWheelEvent::QQuickWheelEvent()
extern "C" Q_DECL_EXPORT
QQuickWheelEvent *ritual_ZN16QQuickWheelEventC1Ev() {
  return new QQuickWheelEvent();
}

//  void QQuickWheelEvent::reset(const QWheelEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickWheelEvent5resetEPK11QWheelEvent(
    QQuickWheelEvent *self,
    const QWheelEvent *event) {
  self->reset(event);
}

//  const QPointingDevice *QQuickWheelEvent::pointingDevice() const
extern "C" Q_DECL_EXPORT
const QPointingDevice *ritual_ZNK16QQuickWheelEvent14pointingDeviceEv(
    const QQuickWheelEvent *self) {
  return self->pointingDevice();
}

//  qreal QQuickWheelEvent::x() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16QQuickWheelEvent1xEv(const QQuickWheelEvent *self) {
  return self->x();
}

//  qreal QQuickWheelEvent::y() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16QQuickWheelEvent1yEv(const QQuickWheelEvent *self) {
  return self->y();
}

//  QPoint QQuickWheelEvent::angleDelta() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK16QQuickWheelEvent10angleDeltaEv(
    const QQuickWheelEvent *self) {
  return new QPoint(self->angleDelta());
}

//  QPoint QQuickWheelEvent::pixelDelta() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK16QQuickWheelEvent10pixelDeltaEv(
    const QQuickWheelEvent *self) {
  return new QPoint(self->pixelDelta());
}

//  int QQuickWheelEvent::buttons() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QQuickWheelEvent7buttonsEv(const QQuickWheelEvent *self) {
  return self->buttons();
}

//  int QQuickWheelEvent::modifiers() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QQuickWheelEvent9modifiersEv(const QQuickWheelEvent *self) {
  return self->modifiers();
}

//  Qt::ScrollPhase QQuickWheelEvent::phase() const
extern "C" Q_DECL_EXPORT
Qt::ScrollPhase ritual_ZNK16QQuickWheelEvent5phaseEv(
    const QQuickWheelEvent *self) {
  return self->phase();
}

//  bool QQuickWheelEvent::inverted() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQuickWheelEvent8invertedEv(const QQuickWheelEvent *self) {
  return self->inverted();
}

//  bool QQuickWheelEvent::isAccepted()
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QQuickWheelEvent10isAcceptedEv(QQuickWheelEvent *self) {
  return self->isAccepted();
}

//  void QQuickWheelEvent::setAccepted(bool accepted)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickWheelEvent11setAcceptedEb(
    QQuickWheelEvent *self,
    bool accepted) {
  self->setAccepted(accepted);
}

#endif  // QT_CONFIG(wheelevent)
