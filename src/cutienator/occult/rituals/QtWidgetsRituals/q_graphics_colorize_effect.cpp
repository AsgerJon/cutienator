//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qgraphicseffect.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qgraphicseffect.h>
#include <QtCore/qstring.h>
#include <QtGui/qcolor.h>

//  const QMetaObject *QGraphicsColorizeEffect::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK23QGraphicsColorizeEffect10metaObjectEv(
    const QGraphicsColorizeEffect *self) {
  return self->metaObject();
}

//  QString QGraphicsColorizeEffect::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN23QGraphicsColorizeEffect2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QGraphicsColorizeEffect::tr(s, c, n));
}

//  QGraphicsColorizeEffect::QGraphicsColorizeEffect(QObject *parent)
extern "C" Q_DECL_EXPORT
QGraphicsColorizeEffect *ritual_ZN23QGraphicsColorizeEffectC1EP7QObject(
    QObject *parent) {
  return new QGraphicsColorizeEffect(parent);
}

//  QGraphicsColorizeEffect::~QGraphicsColorizeEffect()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QGraphicsColorizeEffectD1Ev(QGraphicsColorizeEffect *self) {
  delete self;
}

//  QColor QGraphicsColorizeEffect::color() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK23QGraphicsColorizeEffect5colorEv(
    const QGraphicsColorizeEffect *self) {
  return new QColor(self->color());
}

//  qreal QGraphicsColorizeEffect::strength() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK23QGraphicsColorizeEffect8strengthEv(
    const QGraphicsColorizeEffect *self) {
  return self->strength();
}

//  void QGraphicsColorizeEffect::setColor(const QColor &c)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QGraphicsColorizeEffect8setColorERK6QColor(
    QGraphicsColorizeEffect *self,
    const QColor *c) {
  self->setColor(*c);
}

//  void QGraphicsColorizeEffect::setStrength(qreal strength)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QGraphicsColorizeEffect11setStrengthEd(
    QGraphicsColorizeEffect *self,
    qreal strength) {
  self->setStrength(strength);
}
