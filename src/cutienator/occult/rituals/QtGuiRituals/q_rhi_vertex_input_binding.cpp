//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/rhi/qrhi.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/rhi/qrhi.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QRhiVertexInputBinding::QRhiVertexInputBinding()
extern "C" Q_DECL_EXPORT
QRhiVertexInputBinding *ritual_ZN22QRhiVertexInputBindingC1Ev() {
  return new QRhiVertexInputBinding();
}

//  QRhiVertexInputBinding::QRhiVertexInputBinding(quint32 stride,
//      Classification cls, quint32 stepRate)
extern "C" Q_DECL_EXPORT
QRhiVertexInputBinding *ritual_ZN22QRhiVertexInputBindingC1EjNS_14ClassificationEj(
    quint32 stride,
    QRhiVertexInputBinding::Classification cls,
    quint32 stepRate) {
  return new QRhiVertexInputBinding(stride, cls, stepRate);
}

//  quint32 QRhiVertexInputBinding::stride() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK22QRhiVertexInputBinding6strideEv(
    const QRhiVertexInputBinding *self) {
  return self->stride();
}

//  void QRhiVertexInputBinding::setStride(quint32 s)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QRhiVertexInputBinding9setStrideEj(
    QRhiVertexInputBinding *self,
    quint32 s) {
  self->setStride(s);
}

//  Classification QRhiVertexInputBinding::classification() const
extern "C" Q_DECL_EXPORT
QRhiVertexInputBinding::Classification ritual_ZNK22QRhiVertexInputBinding14classificationEv(
    const QRhiVertexInputBinding *self) {
  return self->classification();
}

//  void QRhiVertexInputBinding::setClassification(Classification c)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QRhiVertexInputBinding17setClassificationENS_14ClassificationE(
    QRhiVertexInputBinding *self,
    QRhiVertexInputBinding::Classification c) {
  self->setClassification(c);
}

//  quint32 QRhiVertexInputBinding::instanceStepRate() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK22QRhiVertexInputBinding16instanceStepRateEv(
    const QRhiVertexInputBinding *self) {
  return self->instanceStepRate();
}

//  void QRhiVertexInputBinding::setInstanceStepRate(quint32 rate)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QRhiVertexInputBinding19setInstanceStepRateEj(
    QRhiVertexInputBinding *self,
    quint32 rate) {
  self->setInstanceStepRate(rate);
}

//  bool operator==(const QRhiVertexInputBinding &a, const
//      QRhiVertexInputBinding &b)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK22QRhiVertexInputBindingS1_(
    const QRhiVertexInputBinding *a,
    const QRhiVertexInputBinding *b) {
  return operator==(*a, *b);
}

//  bool operator!=(const QRhiVertexInputBinding &a, const
//      QRhiVertexInputBinding &b)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK22QRhiVertexInputBindingS1_(
    const QRhiVertexInputBinding *a,
    const QRhiVertexInputBinding *b) {
  return operator!=(*a, *b);
}

//  QRhiVertexInputBinding::~QRhiVertexInputBinding()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QRhiVertexInputBindingD1Ev(QRhiVertexInputBinding *self) {
  delete self;
}
