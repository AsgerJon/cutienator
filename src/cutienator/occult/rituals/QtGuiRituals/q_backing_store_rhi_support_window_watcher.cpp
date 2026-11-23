//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qbackingstorerhisupport_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGui/QtGui>
#include <QtGui/6.12.0/QtGui/private/qbackingstorerhisupport_p.h>
#include "qbackingstorerhisupport_p.h"
#include <qpa/qplatformintegration.h>
#include <private/qguiapplication_p.h>
#if QT_CONFIG(opengl)
#include <QtGui/qoffscreensurface.h>
#include <QtGui/private/qopenglcontext_p.h>
#endif
#if QT_CONFIG(vulkan)
#include <QtGui/private/qvulkandefaultinstance_p.h>
#endif

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it.

//  from src/gui/painting/qbackingstorerhisupport.cpp, line 25, as _ZN23QBackingStoreRhiSupport13SwapchainData5resetEv
inline void QBackingStoreRhiSupport::SwapchainData::reset()
{
    delete swapchain;
    delete renderPassDescriptor;
    delete windowWatcher;
    *this = {};
}

//  from src/gui/painting/qbackingstorerhisupport.cpp, line 196, as _ZN36QBackingStoreRhiSupportWindowWatcher11eventFilterEP7QObjectP6QEvent
inline bool QBackingStoreRhiSupportWindowWatcher::eventFilter(QObject *obj, QEvent *event)
{
    if (event->type() == QEvent::WindowAboutToChangeInternal
        || (event->type() == QEvent::PlatformSurface
            && static_cast<QPlatformSurfaceEvent *>(event)->surfaceEventType() == QPlatformSurfaceEvent::SurfaceAboutToBeDestroyed))
    {
        QWindow *window = qobject_cast<QWindow *>(obj);
        auto it = m_rhiSupport->m_swapchains.find(window);
        if (it != m_rhiSupport->m_swapchains.end()) {
            qCDebug(lcQpaBackingStore) << event << "received for" << window << "- cleaning up swapchain";
            auto data = *it;
            m_rhiSupport->m_swapchains.erase(it);
            data.reset(); // deletes 'this'
        }
    }
    return false;
}
//  -----------------------------------------------------------------------

//  bool QBackingStoreRhiSupportWindowWatcher::eventFilter(QObject *obj,
//      QEvent *ev)
extern "C" Q_DECL_EXPORT
bool ritual_ZN36QBackingStoreRhiSupportWindowWatcher11eventFilterEP7QObjectP6QEvent(
    QBackingStoreRhiSupportWindowWatcher *self,
    QObject *obj,
    QEvent *ev) {
  return self->eventFilter(obj, ev);
}

//  bool QBackingStoreRhiSupportWindowWatcher::eventFilter(QObject *obj,
//      QEvent *ev)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN36QBackingStoreRhiSupportWindowWatcher11eventFilterEP7QObjectP6QEvent(
    QBackingStoreRhiSupportWindowWatcher *self,
    QObject *obj,
    QEvent *ev) {
  return self->QBackingStoreRhiSupportWindowWatcher::eventFilter(obj, ev);
}
