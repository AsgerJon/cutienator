//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpenGL/qopenglversionfunctions.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtOpenGL/qtopenglglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if !defined(QT_NO_OPENGL)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtOpenGL/qopenglversionfunctions.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtOpenGL/qopenglversionfunctions.h>
#include <QtOpenGL/private/qopenglversionfunctions_p.h>
#include <QtGui/qopenglcontext.h>
#include <QtCore/qdebug.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/opengl/qopenglversionfunctions.cpp, line 35, as _ZN25QOpenGLContextVersionData10forContextEP14QOpenGLContext
inline QOpenGLContextVersionData *QOpenGLContextVersionData::forContext(QOpenGLContext *context)
{
    QOpenGLContextPrivate *context_d = QOpenGLContextPrivate::get(context);
    if (context_d->versionFunctions == nullptr)
        context_d->versionFunctions = new QOpenGLContextVersionData;

    return static_cast<QOpenGLContextVersionData *>(context_d->versionFunctions);
}

//  from src/opengl/qopenglversionfunctions.cpp, line 82, as _ZN30QOpenGLVersionFunctionsStorage7backendEP14QOpenGLContextN30QOpenGLVersionFunctionsBackend7VersionE
inline QOpenGLVersionFunctionsBackend *QOpenGLVersionFunctionsStorage::backend(QOpenGLContext *context, QOpenGLVersionFunctionsBackend::Version v)
{
#if QT_CONFIG(opengles2)
    Q_UNUSED(context);
    Q_UNUSED(v);
    return 0;
#else
    if (!backends) {
        backends = new QOpenGLVersionFunctionsBackend *[QOpenGLVersionFunctionsBackend::OpenGLVersionBackendCount];
        memset(backends, 0, sizeof(QOpenGLVersionFunctionsBackend *)*QOpenGLVersionFunctionsBackend::OpenGLVersionBackendCount);
    }
    if (backends[v])
        return backends[v];

    switch(v) {
#define VERSION_ENUM(X) QOpenGLVersionFunctionsBackend::OpenGL_##X
#define CREATE_BACKEND(X) \
    case VERSION_ENUM(X): \
        backends[VERSION_ENUM(X)] = new QOpenGLFunctions_##X##Backend(context); \
        break;
    QT_OPENGL_VERSIONS(CREATE_BACKEND)
    case QOpenGLVersionFunctionsBackend::OpenGLVersionBackendCount:
        Q_UNREACHABLE();
    }
    // the storage keeps one ref
    ++backends[v]->refs;
    return backends[v];
#endif
}

//  from src/opengl/qopenglversionfunctions.cpp, line 58, as _ZN30QOpenGLVersionFunctionsStorageC1Ev
inline QOpenGLVersionFunctionsStorage::QOpenGLVersionFunctionsStorage()
    : backends(nullptr)
{
}
//  -----------------------------------------------------------------------

//  QAbstractOpenGLFunctionsPrivate::QAbstractOpenGLFunctionsPrivate()
extern "C" Q_DECL_EXPORT
QAbstractOpenGLFunctionsPrivate *ritual_ZN31QAbstractOpenGLFunctionsPrivateC1Ev() {
  return new QAbstractOpenGLFunctionsPrivate();
}

//  QAbstractOpenGLFunctionsPrivate
//      *QAbstractOpenGLFunctionsPrivate::get(QAbstractOpenGLFunctions *q)
extern "C" Q_DECL_EXPORT
QAbstractOpenGLFunctionsPrivate *ritual_ZN31QAbstractOpenGLFunctionsPrivate3getEP24QAbstractOpenGLFunctions(
    QAbstractOpenGLFunctions *q) {
  return QAbstractOpenGLFunctionsPrivate::get(q);
}

//  QAbstractOpenGLFunctionsPrivate::~QAbstractOpenGLFunctionsPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QAbstractOpenGLFunctionsPrivateD1Ev(
    QAbstractOpenGLFunctionsPrivate *self) {
  delete self;
}

#endif  // !defined(QT_NO_OPENGL)
