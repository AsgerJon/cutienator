//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qgraphicstransform.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qgraphicstransform.h>
#include <QtCore/qstring.h>

//  const QMetaObject *QGraphicsTransform::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QGraphicsTransform10metaObjectEv(
    const QGraphicsTransform *self) {
  return self->metaObject();
}

//  QString QGraphicsTransform::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QGraphicsTransform2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QGraphicsTransform::tr(s, c, n));
}

//  QGraphicsTransform::~QGraphicsTransform()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QGraphicsTransformD1Ev(QGraphicsTransform *self) {
  delete self;
}

//  void QGraphicsTransform::applyTo(QMatrix4x4 *matrix) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK18QGraphicsTransform7applyToEP10QMatrix4x4(
    const QGraphicsTransform *self,
    QMatrix4x4 *matrix) {
  self->applyTo(matrix);
}
