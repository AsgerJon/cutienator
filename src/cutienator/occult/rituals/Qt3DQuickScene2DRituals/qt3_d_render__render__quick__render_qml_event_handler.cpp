//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DQuickScene2D/6.12.0/Qt3DQuickScene2D/private/scene2d_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DQuickScene2D/6.12.0/Qt3DQuickScene2D/private/qt3dquickscene2d_global_p.h>
#include <Qt3DQuickScene2D/Qt3DQuickScene2D>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DQuickScene2D/6.12.0/Qt3DQuickScene2D/private/scene2d_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/private/qscene_p.h>
#include <Qt3DQuickScene2D/qscene2d.h>
#include <Qt3DRender/qpicktriangleevent.h>
#include <Qt3DRender/qobjectpicker.h>
#include <QtCore/qthread.h>
#include <QtCore/qatomic.h>
#include <QtGui/qevent.h>
#include <QtGui/rhi/qrhi.h>
#include <QtQuick/QQuickGraphicsDevice>
#include <QtQuick/QQuickRenderTarget>
#include <Qt3DQuickScene2D/private/qscene2d_p.h>
#include <Qt3DQuickScene2D/private/scene2d_p.h>
#include <Qt3DQuickScene2D/private/scene2dmanager_p.h>
#include <Qt3DQuickScene2D/private/scene2devent_p.h>
#include <Qt3DRender/private/texture_p.h>
#include <Qt3DRender/private/nodemanagers_p.h>
#include <Qt3DRender/private/resourceaccessor_p.h>
#include <Qt3DRender/private/attachmentpack_p.h>
#include <Qt3DQuickScene2D/private/qt3dquickscene2d_logging_p.h>
#include <Qt3DCore/private/qbackendnode_p.h>
#include <Qt3DRender/private/qobjectpicker_p.h>
#include <Qt3DRender/private/qpickevent_p.h>
#include <Qt3DRender/private/qpicktriangleevent_p.h>
#include <Qt3DRender/private/entity_p.h>
#include <Qt3DRender/private/trianglesvisitor_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/quick3d/quick3dscene2d/items/scene2d.cpp, line 57, as _ZN10Qt3DRender6Render5Quick21RenderQmlEventHandler5eventEP6QEvent
namespace Qt3DRender::Render::Quick {
using namespace Qt3DRender::Quick;
inline bool RenderQmlEventHandler::event(QEvent *e)
{
    switch (static_cast<Scene2DEvent::Type>(e->type())) {

    case Scene2DEvent::Render: {
        m_node->render();
        return true;
    }

    case Scene2DEvent::Initialize: {
        m_node->initializeRender();
        return true;
    }

    case Scene2DEvent::Invalidate: {
        m_node->invalidate();
        return true;
    }

    case Scene2DEvent::Quit: {
        m_node->cleanup();
        return true;
    }

    default:
        break;
    }
    return QObject::event(e);
}
}  // namespace Qt3DRender::Render::Quick
//  -----------------------------------------------------------------------

//  const QMetaObject
//      *Qt3DRender::Render::Quick::RenderQmlEventHandler::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DRender6Render5Quick21RenderQmlEventHandler10metaObjectEv(
    const Qt3DRender::Render::Quick::RenderQmlEventHandler *self) {
  return self->metaObject();
}

//  void *Qt3DRender::Render::Quick::RenderQmlEventHandler::qt_metacast(const
//      char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DRender6Render5Quick21RenderQmlEventHandler11qt_metacastEPKc(
    Qt3DRender::Render::Quick::RenderQmlEventHandler *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DRender::Render::Quick::RenderQmlEventHandler::qt_metacall(QMetaOb
//      ject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DRender6Render5Quick21RenderQmlEventHandler11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DRender::Render::Quick::RenderQmlEventHandler *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  bool Qt3DRender::Render::Quick::RenderQmlEventHandler::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10Qt3DRender6Render5Quick21RenderQmlEventHandler5eventEP6QEvent(
    Qt3DRender::Render::Quick::RenderQmlEventHandler *self,
    QEvent *e) {
  return self->event(e);
}

//  bool Qt3DRender::Render::Quick::RenderQmlEventHandler::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN10Qt3DRender6Render5Quick21RenderQmlEventHandler5eventEP6QEvent(
    Qt3DRender::Render::Quick::RenderQmlEventHandler *self,
    QEvent *e) {
  return self->Qt3DRender::Render::Quick::RenderQmlEventHandler::event(e);
}
