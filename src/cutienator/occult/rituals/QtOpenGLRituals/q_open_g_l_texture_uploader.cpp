//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpenGL/6.12.0/QtOpenGL/private/qopengltextureuploader_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtOpenGL/QtOpenGL>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtOpenGL/6.12.0/QtOpenGL/private/qopengltextureuploader_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qimage.h>
#include <QtCore/qsize.h>

//  qsizetype QOpenGLTextureUploader::textureImage(GLenum target, const
//      QImage &image, BindOptions options, QSize maxSize)
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN22QOpenGLTextureUploader12textureImageEjRK6QImage6QFlagsINS_10BindOptionEE5QSize(
    GLenum target,
    const QImage *image,
    int options,
    const QSize *maxSize) {
  return QOpenGLTextureUploader::textureImage(
      target,
      *image,
      QFlags<QOpenGLTextureUploader::BindOption>::fromInt(options),
      *maxSize);
}

//  QOpenGLTextureUploader::~QOpenGLTextureUploader()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QOpenGLTextureUploaderD1Ev(QOpenGLTextureUploader *self) {
  delete self;
}
