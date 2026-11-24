//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickwindow_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickwindow_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qquickwindow.h"
#include "qquickwindow_p.h"
#include "qquickitem.h"
#include "qquickitem_p.h"
#include "qquickevents_p_p.h"
#include "qquickmousearea_p.h"
#include "qquickwindowcontainer_p.h"
#include "qquicksafearea_p.h"
#include <QtQuick/private/qsgrenderer_p.h>
#include <QtQuick/private/qsgplaintexture_p.h>
#include <QtQuick/private/qquickpointerhandler_p.h>
#include <QtQuick/private/qquickpointerhandler_p_p.h>
#include <QtQuick/private/qquicktaphandler_p.h>
#include <QtQuick/private/qsgnode_p.h>
#include <private/qsgrenderloop_p.h>
#include <private/qsgrhisupport_p.h>
#include <private/qquickrendercontrol_p.h>
#include <private/qquickanimatorcontroller_p.h>
#include <private/qquickprofiler_p.h>
#include <private/qquicktextinterface_p.h>
#include <private/qguiapplication_p.h>
#include <private/qabstractanimation_p.h>
#include <QtGui/qpainter.h>
#include <QtGui/qevent.h>
#include <QtGui/qmatrix4x4.h>
#include <QtGui/private/qevent_p.h>
#include <QtGui/private/qpointingdevice_p.h>
#include <QtCore/qvarlengtharray.h>
#include <QtCore/qabstractanimation.h>
#include <QtCore/QLibraryInfo>
#include <QtCore/QRunnable>
#include <QtQml/qqmlincubator.h>
#include <QtQml/qqmlinfo.h>
#include <QtQml/private/qqmlmetatype_p.h>
#include <QtQuick/private/qquickpixmap_p.h>
#include <private/qqmldebugserviceinterfaces_p.h>
#include <private/qqmldebugconnector_p.h>
#include <private/qsgdefaultrendercontext_p.h>
#include <private/qsgsoftwarerenderer_p.h>
#if QT_CONFIG(opengl)
#include <private/qopengl_p.h>
#include <QOpenGLContext>
#endif
#ifndef QT_NO_DEBUG_STREAM
#include <private/qdebug_p.h>
#endif
#include <QtCore/qpointer.h>
#include <rhi/qrhi.h>
#include <algorithm>
#include <utility>
#include <mutex>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/items/qquickwindow.cpp, line 481, as _ZN24QQuickWindowRenderTarget15ImplicitBuffers5resetEP4QRhi
inline void QQuickWindowRenderTarget::ImplicitBuffers::reset(QRhi *rhi)
{
    if (rhi) {
        delete depthStencil;
        delete depthStencilTexture;
        delete multisampleTexture;
    }
    *this = {};
}

//  from ../qtdeclarative/src/quick/items/qquickwindow.cpp, line 458, as _ZN24QQuickWindowRenderTarget5resetEP4QRhi6QFlagsINS_9ResetFlagEE
inline void QQuickWindowRenderTarget::reset(QRhi *rhi, ResetFlags flags)
{
    if (rhi) {
        if (rt.owns)
            delete rt.renderTarget;

        delete res.texture;
        delete res.renderBuffer;
        delete res.rpDesc;
    }

    rt = {};
    res = {};

    if (!flags.testFlag(ResetFlag::KeepImplicitBuffers))
        implicitBuffers.reset(rhi);

    if (sw.owns)
        delete sw.paintDevice;

    sw = {};
}
//  -----------------------------------------------------------------------

//  void QQuickWindowRenderTarget::reset(QRhi *rhi, ResetFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickWindowRenderTarget5resetEP4QRhi6QFlagsINS_9ResetFlagEE(
    QQuickWindowRenderTarget *self,
    QRhi *rhi,
    int flags) {
  self->reset(
      rhi,
      QFlags<QQuickWindowRenderTarget::ResetFlag>::fromInt(flags));
}

//  QQuickWindowRenderTarget::~QQuickWindowRenderTarget()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickWindowRenderTargetD1Ev(
    QQuickWindowRenderTarget *self) {
  delete self;
}
