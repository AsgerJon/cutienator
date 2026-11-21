//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qgraphicseffect.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qgraphicseffect.h>
#include <QtCore/qstring.h>
#include <QtGui/qbrush.h>

//  const QMetaObject *QGraphicsOpacityEffect::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK22QGraphicsOpacityEffect10metaObjectEv(
    const QGraphicsOpacityEffect *self) {
  return self->metaObject();
}

//  QString QGraphicsOpacityEffect::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN22QGraphicsOpacityEffect2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QGraphicsOpacityEffect::tr(s, c, n));
}

//  QGraphicsOpacityEffect::QGraphicsOpacityEffect(QObject *parent)
extern "C" Q_DECL_EXPORT
QGraphicsOpacityEffect *ritual_ZN22QGraphicsOpacityEffectC1EP7QObject(
    QObject *parent) {
  return new QGraphicsOpacityEffect(parent);
}

//  QGraphicsOpacityEffect::~QGraphicsOpacityEffect()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGraphicsOpacityEffectD1Ev(QGraphicsOpacityEffect *self) {
  delete self;
}

//  qreal QGraphicsOpacityEffect::opacity() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK22QGraphicsOpacityEffect7opacityEv(
    const QGraphicsOpacityEffect *self) {
  return self->opacity();
}

//  QBrush QGraphicsOpacityEffect::opacityMask() const
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZNK22QGraphicsOpacityEffect11opacityMaskEv(
    const QGraphicsOpacityEffect *self) {
  return new QBrush(self->opacityMask());
}

//  void QGraphicsOpacityEffect::setOpacity(qreal opacity)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGraphicsOpacityEffect10setOpacityEd(
    QGraphicsOpacityEffect *self,
    qreal opacity) {
  self->setOpacity(opacity);
}

//  void QGraphicsOpacityEffect::setOpacityMask(const QBrush &mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGraphicsOpacityEffect14setOpacityMaskERK6QBrush(
    QGraphicsOpacityEffect *self,
    const QBrush *mask) {
  self->setOpacityMask(*mask);
}
