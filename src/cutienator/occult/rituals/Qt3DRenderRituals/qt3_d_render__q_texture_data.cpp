//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/qtexturedata.h, Qt 6.12.0. Edited by hand on 2026-11-25:
//  QTextureDataPrivate is written Qt3DRender::QTextureDataPrivate in the two
//  d_func rituals, as Qt declares it. Kept as it is when the generator runs
//  again.
#include <Qt3DRender/qtexturedata.h>

//  Qt3DRender::QTextureDataPrivate *Qt3DRender::QTextureData::d_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::QTextureDataPrivate *ritual_ZN10Qt3DRender12QTextureData6d_funcEv(
    Qt3DRender::QTextureData *self) {
  return self->d_func();
}

//  const Qt3DRender::QTextureDataPrivate
//      *Qt3DRender::QTextureData::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DRender::QTextureDataPrivate *ritual_ZNK10Qt3DRender12QTextureData6d_funcEv(
    const Qt3DRender::QTextureData *self) {
  return self->d_func();
}
