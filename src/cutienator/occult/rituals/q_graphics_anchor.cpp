//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qgraphicsanchorlayout.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qgraphicsanchorlayout.h>
#include <QtCore/qstring.h>

//  const QMetaObject *QGraphicsAnchor::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QGraphicsAnchor10metaObjectEv(
    const QGraphicsAnchor *self) {
  return self->metaObject();
}

//  QString QGraphicsAnchor::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QGraphicsAnchor2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QGraphicsAnchor::tr(s, c, n));
}

//  void QGraphicsAnchor::setSpacing(qreal spacing)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsAnchor10setSpacingEd(
    QGraphicsAnchor *self,
    qreal spacing) {
  self->setSpacing(spacing);
}

//  void QGraphicsAnchor::unsetSpacing()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsAnchor12unsetSpacingEv(QGraphicsAnchor *self) {
  self->unsetSpacing();
}

//  qreal QGraphicsAnchor::spacing() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QGraphicsAnchor7spacingEv(const QGraphicsAnchor *self) {
  return self->spacing();
}

//  void QGraphicsAnchor::setSizePolicy(QSizePolicy::Policy policy)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsAnchor13setSizePolicyEN11QSizePolicy6PolicyE(
    QGraphicsAnchor *self,
    QSizePolicy::Policy policy) {
  self->setSizePolicy(policy);
}

//  QSizePolicy::Policy QGraphicsAnchor::sizePolicy() const
extern "C" Q_DECL_EXPORT
QSizePolicy::Policy ritual_ZNK15QGraphicsAnchor10sizePolicyEv(
    const QGraphicsAnchor *self) {
  return self->sizePolicy();
}

//  QGraphicsAnchor::~QGraphicsAnchor()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsAnchorD1Ev(QGraphicsAnchor *self) {
  delete self;
}
