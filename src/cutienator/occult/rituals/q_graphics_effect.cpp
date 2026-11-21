//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qgraphicseffect.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qgraphicseffect.h>
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>

//  const QMetaObject *QGraphicsEffect::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QGraphicsEffect10metaObjectEv(
    const QGraphicsEffect *self) {
  return self->metaObject();
}

//  QString QGraphicsEffect::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QGraphicsEffect2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QGraphicsEffect::tr(s, c, n));
}

//  QGraphicsEffect::~QGraphicsEffect()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsEffectD1Ev(QGraphicsEffect *self) {
  delete self;
}

//  QRectF QGraphicsEffect::boundingRectFor(const QRectF &sourceRect) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK15QGraphicsEffect15boundingRectForERK6QRectF(
    const QGraphicsEffect *self,
    const QRectF *sourceRect) {
  return new QRectF(self->boundingRectFor(*sourceRect));
}

//  QRectF QGraphicsEffect::boundingRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK15QGraphicsEffect12boundingRectEv(
    const QGraphicsEffect *self) {
  return new QRectF(self->boundingRect());
}

//  bool QGraphicsEffect::isEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QGraphicsEffect9isEnabledEv(const QGraphicsEffect *self) {
  return self->isEnabled();
}

//  void QGraphicsEffect::setEnabled(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsEffect10setEnabledEb(
    QGraphicsEffect *self,
    bool enable) {
  self->setEnabled(enable);
}

//  void QGraphicsEffect::update()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsEffect6updateEv(QGraphicsEffect *self) {
  self->update();
}
