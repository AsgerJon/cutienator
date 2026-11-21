//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qgesture.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qgesture.h>
#include <QtCore/qstring.h>
#include <QtCore/qpoint.h>

//  const QMetaObject *QTapAndHoldGesture::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QTapAndHoldGesture10metaObjectEv(
    const QTapAndHoldGesture *self) {
  return self->metaObject();
}

//  QString QTapAndHoldGesture::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QTapAndHoldGesture2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QTapAndHoldGesture::tr(s, c, n));
}

//  QTapAndHoldGesture::QTapAndHoldGesture(QObject *parent)
extern "C" Q_DECL_EXPORT
QTapAndHoldGesture *ritual_ZN18QTapAndHoldGestureC1EP7QObject(
    QObject *parent) {
  return new QTapAndHoldGesture(parent);
}

//  QTapAndHoldGesture::~QTapAndHoldGesture()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QTapAndHoldGestureD1Ev(QTapAndHoldGesture *self) {
  delete self;
}

//  QPointF QTapAndHoldGesture::position() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK18QTapAndHoldGesture8positionEv(
    const QTapAndHoldGesture *self) {
  return new QPointF(self->position());
}

//  void QTapAndHoldGesture::setPosition(const QPointF &pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QTapAndHoldGesture11setPositionERK7QPointF(
    QTapAndHoldGesture *self,
    const QPointF *pos) {
  self->setPosition(*pos);
}

//  void QTapAndHoldGesture::setTimeout(int msecs)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QTapAndHoldGesture10setTimeoutEi(int msecs) {
  QTapAndHoldGesture::setTimeout(msecs);
}

//  int QTapAndHoldGesture::timeout()
extern "C" Q_DECL_EXPORT
int ritual_ZN18QTapAndHoldGesture7timeoutEv() {
  return QTapAndHoldGesture::timeout();
}
