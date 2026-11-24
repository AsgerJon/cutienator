//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/qsgtexture_platform.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#if QT_CONFIG(opengl) || defined(Q_QDOC)
#include <QtQuick/QtQuick>
#include <QtQuick/qsgtexture_platform.h>
#include <QtCore/qsize.h>

//  QNativeInterface::QSGOpenGLTexture::~QSGOpenGLTexture()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QNativeInterface16QSGOpenGLTextureD1Ev(
    QNativeInterface::QSGOpenGLTexture *self) {
  delete self;
}

//  QSGTexture *QNativeInterface::QSGOpenGLTexture::fromNative(GLuint
//      textureId, QQuickWindow *window, const QSize &size,
//      QQuickWindow::CreateTextureOptions options)
extern "C" Q_DECL_EXPORT
QSGTexture *ritual_ZN16QNativeInterface16QSGOpenGLTexture10fromNativeEjP12QQuickWindowRK5QSize6QFlagsINS1_19CreateTextureOptionEE(
    GLuint textureId,
    QQuickWindow *window,
    const QSize *size,
    int options) {
  return QNativeInterface::QSGOpenGLTexture::fromNative(
      textureId,
      window,
      *size,
      QFlags<QQuickWindow::CreateTextureOption>::fromInt(options));
}

#endif  // QT_CONFIG(opengl) || defined(Q_QDOC)
