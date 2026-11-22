//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qgesture.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qgesture.h>
#include <QtCore/qstring.h>
#include <QtCore/qpoint.h>

//  const QMetaObject *QGesture::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK8QGesture10metaObjectEv(const QGesture *self) {
  return self->metaObject();
}

//  QString QGesture::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN8QGesture2trEPKcS1_i(const char *s, const char *c, int n) {
  return new QString(QGesture::tr(s, c, n));
}

//  QGesture::QGesture(QObject *parent)
extern "C" Q_DECL_EXPORT
QGesture *ritual_ZN8QGestureC1EP7QObject(QObject *parent) {
  return new QGesture(parent);
}

//  QGesture::~QGesture()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QGestureD1Ev(QGesture *self) {
  delete self;
}

//  Qt::GestureType QGesture::gestureType() const
extern "C" Q_DECL_EXPORT
Qt::GestureType ritual_ZNK8QGesture11gestureTypeEv(const QGesture *self) {
  return self->gestureType();
}

//  Qt::GestureState QGesture::state() const
extern "C" Q_DECL_EXPORT
Qt::GestureState ritual_ZNK8QGesture5stateEv(const QGesture *self) {
  return self->state();
}

//  QPointF QGesture::hotSpot() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK8QGesture7hotSpotEv(const QGesture *self) {
  return new QPointF(self->hotSpot());
}

//  void QGesture::setHotSpot(const QPointF &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QGesture10setHotSpotERK7QPointF(
    QGesture *self,
    const QPointF *value) {
  self->setHotSpot(*value);
}

//  bool QGesture::hasHotSpot() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QGesture10hasHotSpotEv(const QGesture *self) {
  return self->hasHotSpot();
}

//  void QGesture::unsetHotSpot()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QGesture12unsetHotSpotEv(QGesture *self) {
  self->unsetHotSpot();
}

//  void QGesture::setGestureCancelPolicy(GestureCancelPolicy policy)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QGesture22setGestureCancelPolicyENS_19GestureCancelPolicyE(
    QGesture *self,
    QGesture::GestureCancelPolicy policy) {
  self->setGestureCancelPolicy(policy);
}

//  GestureCancelPolicy QGesture::gestureCancelPolicy() const
extern "C" Q_DECL_EXPORT
QGesture::GestureCancelPolicy ritual_ZNK8QGesture19gestureCancelPolicyEv(
    const QGesture *self) {
  return self->gestureCancelPolicy();
}
