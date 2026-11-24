//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpenGL/6.12.0/QtOpenGL/private/qopengltexturecache_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtOpenGL/QtOpenGL>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtOpenGL/6.12.0/QtOpenGL/private/qopengltexturecache_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QOpenGLCachedTexture::~QOpenGLCachedTexture()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLCachedTextureD1Ev(QOpenGLCachedTexture *self) {
  delete self;
}

//  QOpenGLTextureUploader::BindOptions QOpenGLCachedTexture::options() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QOpenGLCachedTexture7optionsEv(
    const QOpenGLCachedTexture *self) {
  return static_cast<int>(self->options().toInt());
}
