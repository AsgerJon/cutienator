//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DQuickScene2D/6.12.0/Qt3DQuickScene2D/private/scene2d_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for
//  'Qt3DRender::Render::Quick::RenderQmlEventHandler' is pasted in, cut from
//  what the moc of Qt 6.12.0 writes for its header: Qt's library keeps it to
//  itself; added are 2 rituals that lean on what moc writes for a class of
//  the part Qt keeps to itself, whose ritual file carries moc's output,
//  drafted by a copy of the generator that lets those names through. A copy
//  of a meta-object is a second one: 'qobject_cast' between it and Qt's own
//  does not match. Kept as it is when the generator runs again.
#include <Qt3DQuickScene2D/6.12.0/Qt3DQuickScene2D/private/qt3dquickscene2d_global_p.h>
#include <Qt3DQuickScene2D/Qt3DQuickScene2D>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DQuickScene2D/6.12.0/Qt3DQuickScene2D/private/scene2d_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
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

//  from Qt3DQuickScene2D__Qt3DRender_Render_Quick_RenderQmlEventHandler.cpp, line 1, as moc:Qt3DRender::Render::Quick::RenderQmlEventHandler
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN10Qt3DRender6Render5Quick21RenderQmlEventHandlerE_t {};
} // unnamed namespace

template <> constexpr inline auto Qt3DRender::Render::Quick::RenderQmlEventHandler::qt_create_metaobjectdata<qt_meta_tag_ZN10Qt3DRender6Render5Quick21RenderQmlEventHandlerE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "Qt3DRender::Render::Quick::RenderQmlEventHandler"
    };

    QtMocHelpers::UintData qt_methods {
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<RenderQmlEventHandler, qt_meta_tag_ZN10Qt3DRender6Render5Quick21RenderQmlEventHandlerE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject Qt3DRender::Render::Quick::RenderQmlEventHandler::staticMetaObject = { {
    QMetaObject::SuperData::link<QObject::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN10Qt3DRender6Render5Quick21RenderQmlEventHandlerE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN10Qt3DRender6Render5Quick21RenderQmlEventHandlerE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN10Qt3DRender6Render5Quick21RenderQmlEventHandlerE_t>.metaTypes,
    nullptr
} };

void Qt3DRender::Render::Quick::RenderQmlEventHandler::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<RenderQmlEventHandler *>(_o);
    (void)_t;
    (void)_c;
    (void)_id;
    (void)_a;
}

const QMetaObject *Qt3DRender::Render::Quick::RenderQmlEventHandler::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *Qt3DRender::Render::Quick::RenderQmlEventHandler::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN10Qt3DRender6Render5Quick21RenderQmlEventHandlerE_t>.strings))
        return static_cast<void*>(this);
    return QObject::qt_metacast(_clname);
}

int Qt3DRender::Render::Quick::RenderQmlEventHandler::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QObject::qt_metacall(_c, _id, _a);
    return _id;
}
QT_WARNING_POP

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

//  from ../qt3d/src/quick3d/quick3dscene2d/items/scene2d.cpp, line 50, as _ZN10Qt3DRender6Render5Quick21RenderQmlEventHandlerC1EPNS1_7Scene2DE
namespace Qt3DRender::Render::Quick {
using namespace Qt3DRender::Quick;
inline RenderQmlEventHandler::RenderQmlEventHandler(Scene2D *node)
    : QObject()
    , m_node(node)
{
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

//  QString Qt3DRender::Render::Quick::RenderQmlEventHandler::tr(const char
//      *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DRender6Render5Quick21RenderQmlEventHandler2trEPKcS4_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(
      Qt3DRender::Render::Quick::RenderQmlEventHandler::tr(
          s,
          c,
          n));
}

//  Qt3DRender::Render::Quick::RenderQmlEventHandler::RenderQmlEventHandler(S
//      cene2D *node)
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::Quick::RenderQmlEventHandler *ritual_ZN10Qt3DRender6Render5Quick21RenderQmlEventHandlerC1EPNS1_7Scene2DE(
    Qt3DRender::Render::Quick::Scene2D *node) {
  return new Qt3DRender::Render::Quick::RenderQmlEventHandler(node);
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
