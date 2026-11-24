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

//  from ../qtquick3d/src/runtimerender/rendererimpl/qssgrenderdata.cpp, line 701, as _ZN20QSSGRenderItem2DDataD1Ev
inline QSSGRenderItem2DData::~QSSGRenderItem2DData()
{
    releaseAll();
}

//  from ../qtquick3d/src/runtimerender/rendererimpl/qssgrenderdata.cpp, line 783, as _ZN20QSSGRenderItem2DData10releaseAllEv
inline void QSSGRenderItem2DData::releaseAll()
{
    for (auto &it : item2DRenderers)
        delete it.second;
    item2DRenderers.clear();
    item2DRenderContext = nullptr;
    modelViewProjections.clear();
    m_version = 0;
}
//  -----------------------------------------------------------------------

//  QSSGRenderItem2DData::~QSSGRenderItem2DData()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSSGRenderItem2DDataD1Ev(QSSGRenderItem2DData *self) {
  delete self;
}

//  void QSSGRenderItem2DData::releaseAll()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSSGRenderItem2DData10releaseAllEv(
    QSSGRenderItem2DData *self) {
  self->releaseAll();
}
