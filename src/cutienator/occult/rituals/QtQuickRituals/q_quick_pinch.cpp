//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickpincharea_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickpincharea_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  const QMetaObject *QQuickPinch::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11QQuickPinch10metaObjectEv(
    const QQuickPinch *self) {
  return self->metaObject();
}

//  QString QQuickPinch::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QQuickPinch2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickPinch::tr(s, c, n));
}

//  QQuickPinch::QQuickPinch()
extern "C" Q_DECL_EXPORT
QQuickPinch *ritual_ZN11QQuickPinchC1Ev() {
  return new QQuickPinch();
}

//  QQuickItem *QQuickPinch::target() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK11QQuickPinch6targetEv(const QQuickPinch *self) {
  return self->target();
}

//  void QQuickPinch::setTarget(QQuickItem *target)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPinch9setTargetEP10QQuickItem(
    QQuickPinch *self,
    QQuickItem *target) {
  self->setTarget(target);
}

//  void QQuickPinch::resetTarget()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPinch11resetTargetEv(QQuickPinch *self) {
  self->resetTarget();
}

//  qreal QQuickPinch::minimumScale() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QQuickPinch12minimumScaleEv(const QQuickPinch *self) {
  return self->minimumScale();
}

//  void QQuickPinch::setMinimumScale(qreal s)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPinch15setMinimumScaleEd(QQuickPinch *self, qreal s) {
  self->setMinimumScale(s);
}

//  qreal QQuickPinch::maximumScale() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QQuickPinch12maximumScaleEv(const QQuickPinch *self) {
  return self->maximumScale();
}

//  void QQuickPinch::setMaximumScale(qreal s)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPinch15setMaximumScaleEd(QQuickPinch *self, qreal s) {
  self->setMaximumScale(s);
}

//  qreal QQuickPinch::minimumRotation() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QQuickPinch15minimumRotationEv(const QQuickPinch *self) {
  return self->minimumRotation();
}

//  void QQuickPinch::setMinimumRotation(qreal r)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPinch18setMinimumRotationEd(
    QQuickPinch *self,
    qreal r) {
  self->setMinimumRotation(r);
}

//  qreal QQuickPinch::maximumRotation() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QQuickPinch15maximumRotationEv(const QQuickPinch *self) {
  return self->maximumRotation();
}

//  void QQuickPinch::setMaximumRotation(qreal r)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPinch18setMaximumRotationEd(
    QQuickPinch *self,
    qreal r) {
  self->setMaximumRotation(r);
}

//  Axis QQuickPinch::axis() const
extern "C" Q_DECL_EXPORT
QQuickPinch::Axis ritual_ZNK11QQuickPinch4axisEv(const QQuickPinch *self) {
  return self->axis();
}

//  void QQuickPinch::setAxis(Axis a)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPinch7setAxisENS_4AxisE(
    QQuickPinch *self,
    QQuickPinch::Axis a) {
  self->setAxis(a);
}

//  qreal QQuickPinch::xmin() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QQuickPinch4xminEv(const QQuickPinch *self) {
  return self->xmin();
}

//  void QQuickPinch::setXmin(qreal x)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPinch7setXminEd(QQuickPinch *self, qreal x) {
  self->setXmin(x);
}

//  qreal QQuickPinch::xmax() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QQuickPinch4xmaxEv(const QQuickPinch *self) {
  return self->xmax();
}

//  void QQuickPinch::setXmax(qreal x)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPinch7setXmaxEd(QQuickPinch *self, qreal x) {
  self->setXmax(x);
}

//  qreal QQuickPinch::ymin() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QQuickPinch4yminEv(const QQuickPinch *self) {
  return self->ymin();
}

//  void QQuickPinch::setYmin(qreal y)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPinch7setYminEd(QQuickPinch *self, qreal y) {
  self->setYmin(y);
}

//  qreal QQuickPinch::ymax() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QQuickPinch4ymaxEv(const QQuickPinch *self) {
  return self->ymax();
}

//  void QQuickPinch::setYmax(qreal y)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPinch7setYmaxEd(QQuickPinch *self, qreal y) {
  self->setYmax(y);
}

//  bool QQuickPinch::active() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QQuickPinch6activeEv(const QQuickPinch *self) {
  return self->active();
}

//  void QQuickPinch::setActive(bool a)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPinch9setActiveEb(QQuickPinch *self, bool a) {
  self->setActive(a);
}
