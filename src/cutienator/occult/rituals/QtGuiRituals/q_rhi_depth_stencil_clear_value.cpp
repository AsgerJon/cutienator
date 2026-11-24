//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/rhi/qrhi.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/rhi/qrhi.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QRhiDepthStencilClearValue::QRhiDepthStencilClearValue()
extern "C" Q_DECL_EXPORT
QRhiDepthStencilClearValue *ritual_ZN26QRhiDepthStencilClearValueC1Ev() {
  return new QRhiDepthStencilClearValue();
}

//  QRhiDepthStencilClearValue::QRhiDepthStencilClearValue(float d, quint32
//      s)
extern "C" Q_DECL_EXPORT
QRhiDepthStencilClearValue *ritual_ZN26QRhiDepthStencilClearValueC1Efj(
    float d,
    quint32 s) {
  return new QRhiDepthStencilClearValue(d, s);
}

//  float QRhiDepthStencilClearValue::depthClearValue() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK26QRhiDepthStencilClearValue15depthClearValueEv(
    const QRhiDepthStencilClearValue *self) {
  return self->depthClearValue();
}

//  void QRhiDepthStencilClearValue::setDepthClearValue(float d)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QRhiDepthStencilClearValue18setDepthClearValueEf(
    QRhiDepthStencilClearValue *self,
    float d) {
  self->setDepthClearValue(d);
}

//  quint32 QRhiDepthStencilClearValue::stencilClearValue() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK26QRhiDepthStencilClearValue17stencilClearValueEv(
    const QRhiDepthStencilClearValue *self) {
  return self->stencilClearValue();
}

//  void QRhiDepthStencilClearValue::setStencilClearValue(quint32 s)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QRhiDepthStencilClearValue20setStencilClearValueEj(
    QRhiDepthStencilClearValue *self,
    quint32 s) {
  self->setStencilClearValue(s);
}

//  bool operator==(const QRhiDepthStencilClearValue &a, const
//      QRhiDepthStencilClearValue &b)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK26QRhiDepthStencilClearValueS1_(
    const QRhiDepthStencilClearValue *a,
    const QRhiDepthStencilClearValue *b) {
  return operator==(*a, *b);
}

//  bool operator!=(const QRhiDepthStencilClearValue &a, const
//      QRhiDepthStencilClearValue &b)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK26QRhiDepthStencilClearValueS1_(
    const QRhiDepthStencilClearValue *a,
    const QRhiDepthStencilClearValue *b) {
  return operator!=(*a, *b);
}

//  QRhiDepthStencilClearValue::~QRhiDepthStencilClearValue()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QRhiDepthStencilClearValueD1Ev(
    QRhiDepthStencilClearValue *self) {
  delete self;
}
