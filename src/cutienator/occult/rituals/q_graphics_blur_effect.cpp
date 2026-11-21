//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qgraphicseffect.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qgraphicseffect.h>
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>

//  const QMetaObject *QGraphicsBlurEffect::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QGraphicsBlurEffect10metaObjectEv(
    const QGraphicsBlurEffect *self) {
  return self->metaObject();
}

//  QString QGraphicsBlurEffect::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QGraphicsBlurEffect2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QGraphicsBlurEffect::tr(s, c, n));
}

//  QGraphicsBlurEffect::QGraphicsBlurEffect(QObject *parent)
extern "C" Q_DECL_EXPORT
QGraphicsBlurEffect *ritual_ZN19QGraphicsBlurEffectC1EP7QObject(
    QObject *parent) {
  return new QGraphicsBlurEffect(parent);
}

//  QGraphicsBlurEffect::~QGraphicsBlurEffect()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphicsBlurEffectD1Ev(QGraphicsBlurEffect *self) {
  delete self;
}

//  QRectF QGraphicsBlurEffect::boundingRectFor(const QRectF &rect) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK19QGraphicsBlurEffect15boundingRectForERK6QRectF(
    const QGraphicsBlurEffect *self,
    const QRectF *rect) {
  return new QRectF(self->boundingRectFor(*rect));
}

//  qreal QGraphicsBlurEffect::blurRadius() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK19QGraphicsBlurEffect10blurRadiusEv(
    const QGraphicsBlurEffect *self) {
  return self->blurRadius();
}

//  BlurHints QGraphicsBlurEffect::blurHints() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QGraphicsBlurEffect9blurHintsEv(
    const QGraphicsBlurEffect *self) {
  return static_cast<int>(self->blurHints().toInt());
}

//  void QGraphicsBlurEffect::setBlurRadius(qreal blurRadius)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphicsBlurEffect13setBlurRadiusEd(
    QGraphicsBlurEffect *self,
    qreal blurRadius) {
  self->setBlurRadius(blurRadius);
}

//  void QGraphicsBlurEffect::setBlurHints(BlurHints hints)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphicsBlurEffect12setBlurHintsE6QFlagsINS_8BlurHintEE(
    QGraphicsBlurEffect *self,
    int hints) {
  self->setBlurHints(QFlags<QGraphicsBlurEffect::BlurHint>::fromInt(hints));
}
