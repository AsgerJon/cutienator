//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/rhi/qshader.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/rhi/qshader.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>

//  QShaderCode::QShaderCode()
extern "C" Q_DECL_EXPORT
QShaderCode *ritual_ZN11QShaderCodeC1Ev() {
  return new QShaderCode();
}

//  QShaderCode::QShaderCode(const QByteArray &code, const QByteArray &entry)
extern "C" Q_DECL_EXPORT
QShaderCode *ritual_ZN11QShaderCodeC1ERK10QByteArrayS2_(
    const QByteArray *code,
    const QByteArray *entry) {
  return new QShaderCode(*code, *entry);
}

//  QByteArray QShaderCode::shader() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK11QShaderCode6shaderEv(const QShaderCode *self) {
  return new QByteArray(self->shader());
}

//  void QShaderCode::setShader(const QByteArray &code)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QShaderCode9setShaderERK10QByteArray(
    QShaderCode *self,
    const QByteArray *code) {
  self->setShader(*code);
}

//  QByteArray QShaderCode::entryPoint() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK11QShaderCode10entryPointEv(const QShaderCode *self) {
  return new QByteArray(self->entryPoint());
}

//  void QShaderCode::setEntryPoint(const QByteArray &entry)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QShaderCode13setEntryPointERK10QByteArray(
    QShaderCode *self,
    const QByteArray *entry) {
  self->setEntryPoint(*entry);
}

//  QShaderCode::~QShaderCode()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QShaderCodeD1Ev(QShaderCode *self) {
  delete self;
}
