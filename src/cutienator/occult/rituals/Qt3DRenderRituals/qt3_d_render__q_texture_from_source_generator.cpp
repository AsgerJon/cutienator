//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/qtexture_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/qtexture_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QAbstractTexture::Status
//      Qt3DRender::QTextureFromSourceGenerator::status() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QAbstractTexture::Status ritual_ZNK10Qt3DRender27QTextureFromSourceGenerator6statusEv(
    const Qt3DRender::QTextureFromSourceGenerator *self) {
  return self->status();
}

//  qintptr Qt3DRender::QTextureFromSourceGenerator::id() const
extern "C" Q_DECL_EXPORT
qintptr ritual_ZNK10Qt3DRender27QTextureFromSourceGenerator2idEv(
    const Qt3DRender::QTextureFromSourceGenerator *self) {
  return self->id();
}

//  Qt3DRender::QTextureFromSourceGenerator::~QTextureFromSourceGenerator()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender27QTextureFromSourceGeneratorD1Ev(
    Qt3DRender::QTextureFromSourceGenerator *self) {
  delete self;
}

//  qintptr Qt3DRender::QTextureFromSourceGenerator::id() const
extern "C" Q_DECL_EXPORT
qintptr ritual_own_ZNK10Qt3DRender27QTextureFromSourceGenerator2idEv(
    const Qt3DRender::QTextureFromSourceGenerator *self) {
  return self->Qt3DRender::QTextureFromSourceGenerator::id();
}
