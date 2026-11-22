//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qgraphicsitem.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qgraphicsitem.h>
#include <QtCore/qstring.h>

//  const QMetaObject *QGraphicsObject::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QGraphicsObject10metaObjectEv(
    const QGraphicsObject *self) {
  return self->metaObject();
}

//  QString QGraphicsObject::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QGraphicsObject2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QGraphicsObject::tr(s, c, n));
}

//  QGraphicsObject::~QGraphicsObject()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsObjectD1Ev(QGraphicsObject *self) {
  delete self;
}

//  void QGraphicsObject::grabGesture(Qt::GestureType type, Qt::GestureFlags
//      flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsObject11grabGestureEN2Qt11GestureTypeE6QFlagsINS0_11GestureFlagEE(
    QGraphicsObject *self,
    Qt::GestureType type,
    int flags) {
  self->grabGesture(type, QFlags<Qt::GestureFlag>::fromInt(flags));
}

//  void QGraphicsObject::ungrabGesture(Qt::GestureType type)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsObject13ungrabGestureEN2Qt11GestureTypeE(
    QGraphicsObject *self,
    Qt::GestureType type) {
  self->ungrabGesture(type);
}

//  QGraphicsObject as the QGraphicsItem it is built on
extern "C" Q_DECL_EXPORT
QGraphicsItem *ritual_cast_QGraphicsObject_QGraphicsItem(
    QGraphicsObject *self) {
  return static_cast<QGraphicsItem *>(self);
}
