//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssglightmapper_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssglightmapper_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/private/qssglightmapper_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrenderer_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrhiquadrenderer_p.h>
#include <QtQuick3DRuntimeRender/private/qssglayerrenderdata_p.h>
#include <QtQuick3DUtils/private/qssgutils_p.h>
#ifdef QT_QUICK3D_HAS_LIGHTMAPPER
#include <QtCore/qfuture.h>
#include <QtCore/qfileinfo.h>
#include <QtConcurrent/qtconcurrentrun.h>
#include <QtCore/QRandomGenerator>
#include <QtCore/qsimd.h>
#include <embree3/rtcore.h>
#include <QtQuick3DRuntimeRender/private/qssglightmapio_p.h>
#include <QtCore/QDir>
#include <QtCore/QBuffer>
#include <QtCore/QWaitCondition>
#include <QtCore/QMutex>
#include <QtCore/QTemporaryFile>
#if QT_CONFIG(opengl)
#include <QtGui/QOffscreenSurface>
#include <QtGui/QOpenGLContext>
#endif
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtquick3d/src/runtimerender/rendererimpl/qssglightmapper.cpp, line 3399, as _ZN15QSSGLightmapper7denoiseEv
#if !(defined(QT_QUICK3D_HAS_LIGHTMAPPER))
inline bool QSSGLightmapper::denoise()
{
    return false;
}
#endif  // !(defined(QT_QUICK3D_HAS_LIGHTMAPPER))
//  -----------------------------------------------------------------------

#if !(defined(QT_QUICK3D_HAS_LIGHTMAPPER))
//  bool QSSGLightmapper::denoise()
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QSSGLightmapper7denoiseEv(QSSGLightmapper *self) {
  return self->denoise();
}
#endif  // !(defined(QT_QUICK3D_HAS_LIGHTMAPPER))
