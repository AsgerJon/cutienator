//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpenGL/6.12.0/QtOpenGL/private/qopenglframebufferobject_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtOpenGL/QtOpenGL>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtOpenGL/6.12.0/QtOpenGL/private/qopenglframebufferobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtOpenGL/qopenglframebufferobject.h>
#include <QtOpenGL/private/qopenglframebufferobject_p.h>
#include <QtCore/qdebug.h>
#include <QtGui/private/qopengl_p.h>
#include <QtGui/private/qopenglcontext_p.h>
#include <QtGui/private/qopenglextensions_p.h>
#include <QtGui/private/qfont_p.h>
#include <QtGui/qwindow.h>
#include <QtGui/qimage.h>
#include <QtCore/qbytearray.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/opengl/qopenglframebufferobject.cpp, line 392, as _ZNK31QOpenGLFramebufferObjectPrivate22checkFramebufferStatusEP14QOpenGLContext
inline bool QOpenGLFramebufferObjectPrivate::checkFramebufferStatus(QOpenGLContext *ctx) const
{
    if (!ctx)
        return false;   // Context no longer exists.
    GLenum status = ctx->functions()->glCheckFramebufferStatus(GL_FRAMEBUFFER);
    switch(status) {
    case GL_NO_ERROR:
    case GL_FRAMEBUFFER_COMPLETE:
        return true;
    case GL_FRAMEBUFFER_UNSUPPORTED:
        qDebug("QOpenGLFramebufferObject: Unsupported framebuffer format.");
        break;
    case GL_FRAMEBUFFER_INCOMPLETE_ATTACHMENT:
        qDebug("QOpenGLFramebufferObject: Framebuffer incomplete attachment.");
        break;
    case GL_FRAMEBUFFER_INCOMPLETE_MISSING_ATTACHMENT:
        qDebug("QOpenGLFramebufferObject: Framebuffer incomplete, missing attachment.");
        break;
#ifdef GL_FRAMEBUFFER_INCOMPLETE_DUPLICATE_ATTACHMENT
    case GL_FRAMEBUFFER_INCOMPLETE_DUPLICATE_ATTACHMENT:
        qDebug("QOpenGLFramebufferObject: Framebuffer incomplete, duplicate attachment.");
        break;
#endif
#ifdef GL_FRAMEBUFFER_INCOMPLETE_DIMENSIONS
    case GL_FRAMEBUFFER_INCOMPLETE_DIMENSIONS:
        qDebug("QOpenGLFramebufferObject: Framebuffer incomplete, attached images must have same dimensions.");
        break;
#endif
#ifdef GL_FRAMEBUFFER_INCOMPLETE_FORMATS
    case GL_FRAMEBUFFER_INCOMPLETE_FORMATS:
        qDebug("QOpenGLFramebufferObject: Framebuffer incomplete, attached images must have same format.");
        break;
#endif
#ifdef GL_FRAMEBUFFER_INCOMPLETE_DRAW_BUFFER
    case GL_FRAMEBUFFER_INCOMPLETE_DRAW_BUFFER:
        qDebug("QOpenGLFramebufferObject: Framebuffer incomplete, missing draw buffer.");
        break;
#endif
#ifdef GL_FRAMEBUFFER_INCOMPLETE_READ_BUFFER
    case GL_FRAMEBUFFER_INCOMPLETE_READ_BUFFER:
        qDebug("QOpenGLFramebufferObject: Framebuffer incomplete, missing read buffer.");
        break;
#endif
#ifdef GL_FRAMEBUFFER_INCOMPLETE_MULTISAMPLE
    case GL_FRAMEBUFFER_INCOMPLETE_MULTISAMPLE:
        qDebug("QOpenGLFramebufferObject: Framebuffer incomplete, attachments must have same number of samples per pixel.");
        break;
#endif
    default:
        qDebug() <<"QOpenGLFramebufferObject: An undefined error has occurred: "<< status;
        break;
    }
    return false;
}
//  -----------------------------------------------------------------------

//  QOpenGLFramebufferObjectPrivate::QOpenGLFramebufferObjectPrivate()
extern "C" Q_DECL_EXPORT
QOpenGLFramebufferObjectPrivate *ritual_ZN31QOpenGLFramebufferObjectPrivateC1Ev() {
  return new QOpenGLFramebufferObjectPrivate();
}

//  QOpenGLFramebufferObjectPrivate::~QOpenGLFramebufferObjectPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QOpenGLFramebufferObjectPrivateD1Ev(
    QOpenGLFramebufferObjectPrivate *self) {
  delete self;
}

//  bool
//      QOpenGLFramebufferObjectPrivate::checkFramebufferStatus(QOpenGLContex
//      t *ctx) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK31QOpenGLFramebufferObjectPrivate22checkFramebufferStatusEP14QOpenGLContext(
    const QOpenGLFramebufferObjectPrivate *self,
    QOpenGLContext *ctx) {
  return self->checkFramebufferStatus(ctx);
}
