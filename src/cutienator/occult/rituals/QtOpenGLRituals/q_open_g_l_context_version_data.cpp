//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpenGL/6.12.0/QtOpenGL/private/qopenglversionfunctions_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtOpenGL/QtOpenGL>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtOpenGL/6.12.0/QtOpenGL/private/qopenglversionfunctions_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
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

//  from src/opengl/qopenglversionfunctions.cpp, line 58, as _ZN30QOpenGLVersionFunctionsStorageC1Ev
inline QOpenGLVersionFunctionsStorage::QOpenGLVersionFunctionsStorage()
    : backends(nullptr)
{
}

//  from src/opengl/qopenglversionfunctions.cpp, line 63, as _ZN30QOpenGLVersionFunctionsStorageD1Ev
inline QOpenGLVersionFunctionsStorage::~QOpenGLVersionFunctionsStorage()
{
#if !QT_CONFIG(opengles2)
    if (backends) {

        int i = 0;

#define DELETE_BACKEND(X) \
        if (backends[i] && !--backends[i]->refs) \
            delete static_cast<QOpenGLFunctions_##X##Backend*>(backends[i]); \
        ++i;

        QT_OPENGL_VERSIONS(DELETE_BACKEND)
#undef DELETE_BACKEND
        delete[] backends;
    }
#endif
}

//  from src/opengl/qopenglversionfunctions.cpp, line 23, as _ZN25QOpenGLContextVersionDataD1Ev
inline QOpenGLContextVersionData::~QOpenGLContextVersionData()
{
    for (auto *f : std::as_const(externalFunctions)) {
        auto *fp = QAbstractOpenGLFunctionsPrivate::get(f);
        fp->owningContext = nullptr;
        fp->initialized = false;
    }
    externalFunctions.clear();
    qDeleteAll(functions);
    functions.clear();
}

//  from src/opengl/qopenglversionfunctions.cpp, line 35, as _ZN25QOpenGLContextVersionData10forContextEP14QOpenGLContext
inline QOpenGLContextVersionData *QOpenGLContextVersionData::forContext(QOpenGLContext *context)
{
    QOpenGLContextPrivate *context_d = QOpenGLContextPrivate::get(context);
    if (context_d->versionFunctions == nullptr)
        context_d->versionFunctions = new QOpenGLContextVersionData;

    return static_cast<QOpenGLContextVersionData *>(context_d->versionFunctions);
}
//  -----------------------------------------------------------------------

//  QOpenGLContextVersionData::~QOpenGLContextVersionData()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLContextVersionDataD1Ev(
    QOpenGLContextVersionData *self) {
  delete self;
}

//  QOpenGLContextVersionData
//      *QOpenGLContextVersionData::forContext(QOpenGLContext *context)
extern "C" Q_DECL_EXPORT
QOpenGLContextVersionData *ritual_ZN25QOpenGLContextVersionData10forContextEP14QOpenGLContext(
    QOpenGLContext *context) {
  return QOpenGLContextVersionData::forContext(context);
}
