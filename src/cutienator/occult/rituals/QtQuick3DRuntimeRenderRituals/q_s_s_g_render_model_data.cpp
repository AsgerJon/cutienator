//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderdata_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderdata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qssgrenderdata_p.h"
#if QT_CONFIG(thread)
#include <QtCore/qthreadpool.h>
#endif
#include <QtCore/qtenvironmentvariables.h>
#include <QtQuick/private/qsgcontext_p.h>
#include <QtQuick/private/qsgrenderer_p.h>
#include "qssgrenderer_p.h"
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtquick3d/src/runtimerender/rendererimpl/qssgrenderdata.cpp, line 655, as _ZN19QSSGRenderModelData22getThreadPoolThresholdEv
inline quint32 QSSGRenderModelData::getThreadPoolThreshold()
{
    // The threshold is the minimum number of models in a layer to consider using the thread pool for per-model calculations.
    const int ret = qEnvironmentVariableIntValue("QSSG_MODEL_DATA_THREAD_POOL_THRESHOLD");
    return (ret > 0) ? quint32(ret) : 32u;
}
//  -----------------------------------------------------------------------

//  quint32 QSSGRenderModelData::getThreadPoolThreshold()
extern "C" Q_DECL_EXPORT
quint32 ritual_ZN19QSSGRenderModelData22getThreadPoolThresholdEv() {
  return QSSGRenderModelData::getThreadPoolThreshold();
}
