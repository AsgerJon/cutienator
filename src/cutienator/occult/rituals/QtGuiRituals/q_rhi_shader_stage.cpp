//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/rhi/qrhi.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/rhi/qrhi.h>
#include <QtGui/6.12.0/QtGui/rhi/qshader.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QRhiShaderStage::QRhiShaderStage()
extern "C" Q_DECL_EXPORT
QRhiShaderStage *ritual_ZN15QRhiShaderStageC1Ev() {
  return new QRhiShaderStage();
}

//  QRhiShaderStage::QRhiShaderStage(Type type, const QShader &shader,
//      QShader::Variant v)
extern "C" Q_DECL_EXPORT
QRhiShaderStage *ritual_ZN15QRhiShaderStageC1ENS_4TypeERK7QShaderNS1_7VariantE(
    QRhiShaderStage::Type type,
    const QShader *shader,
    QShader::Variant v) {
  return new QRhiShaderStage(type, *shader, v);
}

//  Type QRhiShaderStage::type() const
extern "C" Q_DECL_EXPORT
QRhiShaderStage::Type ritual_ZNK15QRhiShaderStage4typeEv(
    const QRhiShaderStage *self) {
  return self->type();
}

//  void QRhiShaderStage::setType(Type t)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QRhiShaderStage7setTypeENS_4TypeE(
    QRhiShaderStage *self,
    QRhiShaderStage::Type t) {
  self->setType(t);
}

//  QShader QRhiShaderStage::shader() const
extern "C" Q_DECL_EXPORT
QShader *ritual_ZNK15QRhiShaderStage6shaderEv(const QRhiShaderStage *self) {
  return new QShader(self->shader());
}

//  void QRhiShaderStage::setShader(const QShader &s)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QRhiShaderStage9setShaderERK7QShader(
    QRhiShaderStage *self,
    const QShader *s) {
  self->setShader(*s);
}

//  QShader::Variant QRhiShaderStage::shaderVariant() const
extern "C" Q_DECL_EXPORT
QShader::Variant ritual_ZNK15QRhiShaderStage13shaderVariantEv(
    const QRhiShaderStage *self) {
  return self->shaderVariant();
}

//  void QRhiShaderStage::setShaderVariant(QShader::Variant v)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QRhiShaderStage16setShaderVariantEN7QShader7VariantE(
    QRhiShaderStage *self,
    QShader::Variant v) {
  self->setShaderVariant(v);
}

//  bool operator==(const QRhiShaderStage &a, const QRhiShaderStage &b)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK15QRhiShaderStageS1_(
    const QRhiShaderStage *a,
    const QRhiShaderStage *b) {
  return operator==(*a, *b);
}

//  bool operator!=(const QRhiShaderStage &a, const QRhiShaderStage &b)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK15QRhiShaderStageS1_(
    const QRhiShaderStage *a,
    const QRhiShaderStage *b) {
  return operator!=(*a, *b);
}

//  QRhiShaderStage::~QRhiShaderStage()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QRhiShaderStageD1Ev(QRhiShaderStage *self) {
  delete self;
}
