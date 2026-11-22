//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qgesture.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qgesture.h>
#include <QtCore/qstring.h>

//  const QMetaObject *QSwipeGesture::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QSwipeGesture10metaObjectEv(
    const QSwipeGesture *self) {
  return self->metaObject();
}

//  QString QSwipeGesture::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QSwipeGesture2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QSwipeGesture::tr(s, c, n));
}

//  QSwipeGesture::QSwipeGesture(QObject *parent)
extern "C" Q_DECL_EXPORT
QSwipeGesture *ritual_ZN13QSwipeGestureC1EP7QObject(QObject *parent) {
  return new QSwipeGesture(parent);
}

//  QSwipeGesture::~QSwipeGesture()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSwipeGestureD1Ev(QSwipeGesture *self) {
  delete self;
}

//  SwipeDirection QSwipeGesture::horizontalDirection() const
extern "C" Q_DECL_EXPORT
QSwipeGesture::SwipeDirection ritual_ZNK13QSwipeGesture19horizontalDirectionEv(
    const QSwipeGesture *self) {
  return self->horizontalDirection();
}

//  SwipeDirection QSwipeGesture::verticalDirection() const
extern "C" Q_DECL_EXPORT
QSwipeGesture::SwipeDirection ritual_ZNK13QSwipeGesture17verticalDirectionEv(
    const QSwipeGesture *self) {
  return self->verticalDirection();
}

//  qreal QSwipeGesture::swipeAngle() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK13QSwipeGesture10swipeAngleEv(const QSwipeGesture *self) {
  return self->swipeAngle();
}

//  void QSwipeGesture::setSwipeAngle(qreal value)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSwipeGesture13setSwipeAngleEd(
    QSwipeGesture *self,
    qreal value) {
  self->setSwipeAngle(value);
}
