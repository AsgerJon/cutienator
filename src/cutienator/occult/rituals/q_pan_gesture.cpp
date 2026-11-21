//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qgesture.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qgesture.h>
#include <QtCore/qstring.h>
#include <QtCore/qpoint.h>

//  const QMetaObject *QPanGesture::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11QPanGesture10metaObjectEv(
    const QPanGesture *self) {
  return self->metaObject();
}

//  QString QPanGesture::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QPanGesture2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QPanGesture::tr(s, c, n));
}

//  QPanGesture::QPanGesture(QObject *parent)
extern "C" Q_DECL_EXPORT
QPanGesture *ritual_ZN11QPanGestureC1EP7QObject(QObject *parent) {
  return new QPanGesture(parent);
}

//  QPanGesture::~QPanGesture()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QPanGestureD1Ev(QPanGesture *self) {
  delete self;
}

//  QPointF QPanGesture::lastOffset() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK11QPanGesture10lastOffsetEv(const QPanGesture *self) {
  return new QPointF(self->lastOffset());
}

//  QPointF QPanGesture::offset() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK11QPanGesture6offsetEv(const QPanGesture *self) {
  return new QPointF(self->offset());
}

//  QPointF QPanGesture::delta() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK11QPanGesture5deltaEv(const QPanGesture *self) {
  return new QPointF(self->delta());
}

//  qreal QPanGesture::acceleration() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QPanGesture12accelerationEv(const QPanGesture *self) {
  return self->acceleration();
}

//  void QPanGesture::setLastOffset(const QPointF &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QPanGesture13setLastOffsetERK7QPointF(
    QPanGesture *self,
    const QPointF *value) {
  self->setLastOffset(*value);
}

//  void QPanGesture::setOffset(const QPointF &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QPanGesture9setOffsetERK7QPointF(
    QPanGesture *self,
    const QPointF *value) {
  self->setOffset(*value);
}

//  void QPanGesture::setAcceleration(qreal value)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QPanGesture15setAccelerationEd(
    QPanGesture *self,
    qreal value) {
  self->setAcceleration(value);
}
