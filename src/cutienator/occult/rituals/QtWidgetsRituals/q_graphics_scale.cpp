//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qgraphicstransform.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qgraphicstransform.h>
#include <QtCore/qstring.h>
#include <QtGui/qvectornd.h>

//  const QMetaObject *QGraphicsScale::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QGraphicsScale10metaObjectEv(
    const QGraphicsScale *self) {
  return self->metaObject();
}

//  QString QGraphicsScale::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QGraphicsScale2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QGraphicsScale::tr(s, c, n));
}

//  QGraphicsScale::QGraphicsScale(QObject *parent)
extern "C" Q_DECL_EXPORT
QGraphicsScale *ritual_ZN14QGraphicsScaleC1EP7QObject(QObject *parent) {
  return new QGraphicsScale(parent);
}

//  QGraphicsScale::~QGraphicsScale()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGraphicsScaleD1Ev(QGraphicsScale *self) {
  delete self;
}

//  QVector3D QGraphicsScale::origin() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK14QGraphicsScale6originEv(const QGraphicsScale *self) {
  return new QVector3D(self->origin());
}

//  void QGraphicsScale::setOrigin(const QVector3D &point)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGraphicsScale9setOriginERK9QVector3D(
    QGraphicsScale *self,
    const QVector3D *point) {
  self->setOrigin(*point);
}

//  qreal QGraphicsScale::xScale() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14QGraphicsScale6xScaleEv(const QGraphicsScale *self) {
  return self->xScale();
}

//  void QGraphicsScale::setXScale(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGraphicsScale9setXScaleEd(QGraphicsScale *self, qreal a0) {
  self->setXScale(a0);
}

//  qreal QGraphicsScale::yScale() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14QGraphicsScale6yScaleEv(const QGraphicsScale *self) {
  return self->yScale();
}

//  void QGraphicsScale::setYScale(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGraphicsScale9setYScaleEd(QGraphicsScale *self, qreal a0) {
  self->setYScale(a0);
}

//  qreal QGraphicsScale::zScale() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14QGraphicsScale6zScaleEv(const QGraphicsScale *self) {
  return self->zScale();
}

//  void QGraphicsScale::setZScale(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGraphicsScale9setZScaleEd(QGraphicsScale *self, qreal a0) {
  self->setZScale(a0);
}

//  void QGraphicsScale::applyTo(QMatrix4x4 *matrix) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK14QGraphicsScale7applyToEP10QMatrix4x4(
    const QGraphicsScale *self,
    QMatrix4x4 *matrix) {
  self->applyTo(matrix);
}
