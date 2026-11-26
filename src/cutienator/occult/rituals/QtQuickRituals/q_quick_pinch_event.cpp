//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickpincharea_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickpincharea_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qpoint.h>

//  const QMetaObject *QQuickPinchEvent::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QQuickPinchEvent10metaObjectEv(
    const QQuickPinchEvent *self) {
  return self->metaObject();
}

//  void *QQuickPinchEvent::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN16QQuickPinchEvent11qt_metacastEPKc(
    QQuickPinchEvent *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickPinchEvent::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN16QQuickPinchEvent11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickPinchEvent *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickPinchEvent::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QQuickPinchEvent2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickPinchEvent::tr(s, c, n));
}

//  void QQuickPinchEvent::qt_qmlMarker_anonymous()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickPinchEvent22qt_qmlMarker_anonymousEv(
    QQuickPinchEvent *self) {
  self->qt_qmlMarker_anonymous();
}

//  QQuickPinchEvent::QQuickPinchEvent(QPointF c, qreal s, qreal a, qreal r)
extern "C" Q_DECL_EXPORT
QQuickPinchEvent *ritual_ZN16QQuickPinchEventC1E7QPointFddd(
    const QPointF *c,
    qreal s,
    qreal a,
    qreal r) {
  return new QQuickPinchEvent(*c, s, a, r);
}

//  QPointF QQuickPinchEvent::center() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK16QQuickPinchEvent6centerEv(
    const QQuickPinchEvent *self) {
  return new QPointF(self->center());
}

//  QPointF QQuickPinchEvent::startCenter() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK16QQuickPinchEvent11startCenterEv(
    const QQuickPinchEvent *self) {
  return new QPointF(self->startCenter());
}

//  void QQuickPinchEvent::setStartCenter(QPointF c)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickPinchEvent14setStartCenterE7QPointF(
    QQuickPinchEvent *self,
    const QPointF *c) {
  self->setStartCenter(*c);
}

//  QPointF QQuickPinchEvent::previousCenter() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK16QQuickPinchEvent14previousCenterEv(
    const QQuickPinchEvent *self) {
  return new QPointF(self->previousCenter());
}

//  void QQuickPinchEvent::setPreviousCenter(QPointF c)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickPinchEvent17setPreviousCenterE7QPointF(
    QQuickPinchEvent *self,
    const QPointF *c) {
  self->setPreviousCenter(*c);
}

//  qreal QQuickPinchEvent::scale() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16QQuickPinchEvent5scaleEv(const QQuickPinchEvent *self) {
  return self->scale();
}

//  qreal QQuickPinchEvent::previousScale() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16QQuickPinchEvent13previousScaleEv(
    const QQuickPinchEvent *self) {
  return self->previousScale();
}

//  void QQuickPinchEvent::setPreviousScale(qreal s)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickPinchEvent16setPreviousScaleEd(
    QQuickPinchEvent *self,
    qreal s) {
  self->setPreviousScale(s);
}

//  qreal QQuickPinchEvent::angle() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16QQuickPinchEvent5angleEv(const QQuickPinchEvent *self) {
  return self->angle();
}

//  qreal QQuickPinchEvent::previousAngle() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16QQuickPinchEvent13previousAngleEv(
    const QQuickPinchEvent *self) {
  return self->previousAngle();
}

//  void QQuickPinchEvent::setPreviousAngle(qreal a)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickPinchEvent16setPreviousAngleEd(
    QQuickPinchEvent *self,
    qreal a) {
  self->setPreviousAngle(a);
}

//  qreal QQuickPinchEvent::rotation() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16QQuickPinchEvent8rotationEv(const QQuickPinchEvent *self) {
  return self->rotation();
}

//  QPointF QQuickPinchEvent::point1() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK16QQuickPinchEvent6point1Ev(
    const QQuickPinchEvent *self) {
  return new QPointF(self->point1());
}

//  void QQuickPinchEvent::setPoint1(QPointF p)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickPinchEvent9setPoint1E7QPointF(
    QQuickPinchEvent *self,
    const QPointF *p) {
  self->setPoint1(*p);
}

//  QPointF QQuickPinchEvent::startPoint1() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK16QQuickPinchEvent11startPoint1Ev(
    const QQuickPinchEvent *self) {
  return new QPointF(self->startPoint1());
}

//  void QQuickPinchEvent::setStartPoint1(QPointF p)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickPinchEvent14setStartPoint1E7QPointF(
    QQuickPinchEvent *self,
    const QPointF *p) {
  self->setStartPoint1(*p);
}

//  QPointF QQuickPinchEvent::point2() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK16QQuickPinchEvent6point2Ev(
    const QQuickPinchEvent *self) {
  return new QPointF(self->point2());
}

//  void QQuickPinchEvent::setPoint2(QPointF p)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickPinchEvent9setPoint2E7QPointF(
    QQuickPinchEvent *self,
    const QPointF *p) {
  self->setPoint2(*p);
}

//  QPointF QQuickPinchEvent::startPoint2() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK16QQuickPinchEvent11startPoint2Ev(
    const QQuickPinchEvent *self) {
  return new QPointF(self->startPoint2());
}

//  void QQuickPinchEvent::setStartPoint2(QPointF p)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickPinchEvent14setStartPoint2E7QPointF(
    QQuickPinchEvent *self,
    const QPointF *p) {
  self->setStartPoint2(*p);
}

//  int QQuickPinchEvent::pointCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QQuickPinchEvent10pointCountEv(
    const QQuickPinchEvent *self) {
  return self->pointCount();
}

//  void QQuickPinchEvent::setPointCount(int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickPinchEvent13setPointCountEi(
    QQuickPinchEvent *self,
    int count) {
  self->setPointCount(count);
}

//  bool QQuickPinchEvent::accepted() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQuickPinchEvent8acceptedEv(const QQuickPinchEvent *self) {
  return self->accepted();
}

//  void QQuickPinchEvent::setAccepted(bool a)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickPinchEvent11setAcceptedEb(
    QQuickPinchEvent *self,
    bool a) {
  self->setAccepted(a);
}
