//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qgesture.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qgesture.h>
#include <QtCore/qstring.h>
#include <QtCore/qpoint.h>

//  const QMetaObject *QTapGesture::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11QTapGesture10metaObjectEv(
    const QTapGesture *self) {
  return self->metaObject();
}

//  QString QTapGesture::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QTapGesture2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QTapGesture::tr(s, c, n));
}

//  QTapGesture::QTapGesture(QObject *parent)
extern "C" Q_DECL_EXPORT
QTapGesture *ritual_ZN11QTapGestureC1EP7QObject(QObject *parent) {
  return new QTapGesture(parent);
}

//  QTapGesture::~QTapGesture()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTapGestureD1Ev(QTapGesture *self) {
  delete self;
}

//  QPointF QTapGesture::position() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK11QTapGesture8positionEv(const QTapGesture *self) {
  return new QPointF(self->position());
}

//  void QTapGesture::setPosition(const QPointF &pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTapGesture11setPositionERK7QPointF(
    QTapGesture *self,
    const QPointF *pos) {
  self->setPosition(*pos);
}
