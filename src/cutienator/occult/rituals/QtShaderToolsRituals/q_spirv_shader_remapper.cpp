//  Written by dev_tooling.RitualGenerator from the records of
//  QtShaderTools/6.12.0/QtShaderTools/private/qspirvshaderremap_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtShaderTools/QtShaderTools>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtShaderTools/6.12.0/QtShaderTools/private/qspirvshaderremap_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtCore/qstring.h>

//  QByteArray QSpirvShaderRemapper::remap(const QByteArray &ir,
//      QSpirvShader::RemapFlags flags)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN20QSpirvShaderRemapper5remapERK10QByteArray6QFlagsIN12QSpirvShader9RemapFlagEE(
    QSpirvShaderRemapper *self,
    const QByteArray *ir,
    int flags) {
  return new QByteArray(
      self->remap(
          *ir,
          QFlags<QSpirvShader::RemapFlag>::fromInt(flags)));
}

//  QString QSpirvShaderRemapper::errorMessage() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK20QSpirvShaderRemapper12errorMessageEv(
    const QSpirvShaderRemapper *self) {
  return new QString(self->errorMessage());
}

//  void QSpirvShaderRemapper::remapErrorHandler(const std::string &s)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSpirvShaderRemapper17remapErrorHandlerERKNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEE(
    QSpirvShaderRemapper *self,
    const std::string *s) {
  self->remapErrorHandler(*s);
}

//  void QSpirvShaderRemapper::remapLogHandler(const std::string &s)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSpirvShaderRemapper15remapLogHandlerERKNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEE(
    QSpirvShaderRemapper *self,
    const std::string *s) {
  self->remapLogHandler(*s);
}

//  QSpirvShaderRemapper::~QSpirvShaderRemapper()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSpirvShaderRemapperD1Ev(QSpirvShaderRemapper *self) {
  delete self;
}
