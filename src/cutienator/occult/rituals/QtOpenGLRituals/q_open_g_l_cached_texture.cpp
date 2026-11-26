//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpenGL/6.12.0/QtOpenGL/private/qopengltexturecache_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtOpenGL/QtOpenGL>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtOpenGL/6.12.0/QtOpenGL/private/qopengltexturecache_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtOpenGL/private/qopengltexturecache_p.h>
#include <QtOpenGL/private/qopengltextureuploader_p.h>
#include <QtCore/qmath.h>
#include <QtGui/qopenglfunctions.h>
#include <QtGui/private/qimagepixmapcleanuphooks_p.h>
#include <QtGui/qpa/qplatformpixmap.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/opengl/qopengltexturecache.cpp, line 177, as local:qopengltexturecache.cpp:freeTexture
static void freeTexture(QOpenGLFunctions *funcs, GLuint id)
{
    funcs->glDeleteTextures(1, &id);
}

//  from src/opengl/qopengltexturecache.cpp, line 182, as _ZN20QOpenGLCachedTextureC1Ej6QFlagsIN22QOpenGLTextureUploader10BindOptionEEP14QOpenGLContext
inline QOpenGLCachedTexture::QOpenGLCachedTexture(GLuint id, QOpenGLTextureUploader::BindOptions options, QOpenGLContext *context) : m_options(options)
{
    m_resource = new QOpenGLSharedResourceGuard(context, id, freeTexture);
}
//  -----------------------------------------------------------------------

//  QOpenGLCachedTexture::QOpenGLCachedTexture(GLuint id,
//      QOpenGLTextureUploader::BindOptions options, QOpenGLContext *context)
extern "C" Q_DECL_EXPORT
QOpenGLCachedTexture *ritual_ZN20QOpenGLCachedTextureC1Ej6QFlagsIN22QOpenGLTextureUploader10BindOptionEEP14QOpenGLContext(
    GLuint id,
    int options,
    QOpenGLContext *context) {
  return new QOpenGLCachedTexture(
      id,
      QFlags<QOpenGLTextureUploader::BindOption>::fromInt(options),
      context);
}

//  QOpenGLCachedTexture::~QOpenGLCachedTexture()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLCachedTextureD1Ev(QOpenGLCachedTexture *self) {
  delete self;
}

//  GLuint QOpenGLCachedTexture::id() const
extern "C" Q_DECL_EXPORT
GLuint ritual_ZNK20QOpenGLCachedTexture2idEv(
    const QOpenGLCachedTexture *self) {
  return self->id();
}

//  QOpenGLTextureUploader::BindOptions QOpenGLCachedTexture::options() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QOpenGLCachedTexture7optionsEv(
    const QOpenGLCachedTexture *self) {
  return static_cast<int>(self->options().toInt());
}
