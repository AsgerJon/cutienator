//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/qsgmaterialshader.h, Qt 6.12.0. Changes made here are lost.
#include <QtQuick/QtQuick>
#include <QtQuick/qsgmaterialshader.h>
#include <QtCore/qstring.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/rhi/qshader.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QSGMaterialShader::QSGMaterialShader()
extern "C" Q_DECL_EXPORT
QSGMaterialShader *ritual_ZN17QSGMaterialShaderC1Ev() {
  return new QSGMaterialShader();
}

//  QSGMaterialShader::~QSGMaterialShader()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSGMaterialShaderD1Ev(QSGMaterialShader *self) {
  delete self;
}

//  Flags QSGMaterialShader::flags() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QSGMaterialShader5flagsEv(const QSGMaterialShader *self) {
  return static_cast<int>(self->flags().toInt());
}

//  void QSGMaterialShader::setFlag(Flags flags, bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSGMaterialShader7setFlagE6QFlagsINS_4FlagEEb(
    QSGMaterialShader *self,
    int flags,
    bool on) {
  self->setFlag(QFlags<QSGMaterialShader::Flag>::fromInt(flags), on);
}

//  void QSGMaterialShader::setFlags(Flags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSGMaterialShader8setFlagsE6QFlagsINS_4FlagEE(
    QSGMaterialShader *self,
    int flags) {
  self->setFlags(QFlags<QSGMaterialShader::Flag>::fromInt(flags));
}

//  int QSGMaterialShader::combinedImageSamplerCount(int binding) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QSGMaterialShader25combinedImageSamplerCountEi(
    const QSGMaterialShader *self,
    int binding) {
  return self->combinedImageSamplerCount(binding);
}

//  QSGMaterialShaderPrivate *QSGMaterialShader::d_func()
extern "C" Q_DECL_EXPORT
QSGMaterialShaderPrivate *ritual_ZN17QSGMaterialShader6d_funcEv(
    QSGMaterialShader *self) {
  return self->d_func();
}

//  const QSGMaterialShaderPrivate *QSGMaterialShader::d_func() const
extern "C" Q_DECL_EXPORT
const QSGMaterialShaderPrivate *ritual_ZNK17QSGMaterialShader6d_funcEv(
    const QSGMaterialShader *self) {
  return self->d_func();
}

//  void QSGMaterialShader::setShaderFileName(Stage stage, const QString
//      &filename)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSGMaterialShader17setShaderFileNameENS_5StageERK7QString(
    QSGMaterialShader *self,
    QSGMaterialShader::Stage stage,
    const QString *filename) {
  self->setShaderFileName(stage, *filename);
}

//  void QSGMaterialShader::setShaderFileName(Stage stage, const QString
//      &filename, int viewCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSGMaterialShader17setShaderFileNameENS_5StageERK7QStringi(
    QSGMaterialShader *self,
    QSGMaterialShader::Stage stage,
    const QString *filename,
    int viewCount) {
  self->setShaderFileName(stage, *filename, viewCount);
}

//  void QSGMaterialShader::setShader(Stage stage, const QShader &shader)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSGMaterialShader9setShaderENS_5StageERK7QShader(
    QSGMaterialShader *self,
    QSGMaterialShader::Stage stage,
    const QShader *shader) {
  self->setShader(stage, *shader);
}
