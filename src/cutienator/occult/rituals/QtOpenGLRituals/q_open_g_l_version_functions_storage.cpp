//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpenGL/qopenglversionfunctions.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtOpenGL/qtopenglglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if !defined(QT_NO_OPENGL)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtOpenGL/qopenglversionfunctions.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qopenglversionfunctions.h"
#include "qopenglversionfunctions_p.h"
#include "qopenglcontext.h"
#include "qdebug.h"
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
//  -----------------------------------------------------------------------

//  QOpenGLVersionFunctionsStorage::QOpenGLVersionFunctionsStorage()
extern "C" Q_DECL_EXPORT
QOpenGLVersionFunctionsStorage *ritual_ZN30QOpenGLVersionFunctionsStorageC1Ev() {
  return new QOpenGLVersionFunctionsStorage();
}

//  QOpenGLVersionFunctionsStorage::~QOpenGLVersionFunctionsStorage()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QOpenGLVersionFunctionsStorageD1Ev(
    QOpenGLVersionFunctionsStorage *self) {
  delete self;
}

#endif  // !defined(QT_NO_OPENGL)
