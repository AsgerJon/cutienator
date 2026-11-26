//  Written by dev_tooling.RitualGenerator from the records of QtWaylandCompo
//  sitor/6.12.0/QtWaylandCompositor/private/qwaylandxdgshellintegration_p.h,
//  Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for
//  'QtWayland::XdgPopupIntegration' is pasted in, cut from what the moc of
//  Qt 6.12.0 writes for its header: Qt's library keeps it to itself; added
//  are 2 rituals that lean on what moc writes for a class of the part Qt
//  keeps to itself, whose ritual file carries moc's output, drafted by a
//  copy of the generator that lets those names through. A copy of a meta-
//  object is a second one: 'qobject_cast' between it and Qt's own does not
//  match. Kept as it is when the generator runs again.
#include <QtWaylandCompositor/qtwaylandcompositorglobal.h>
#include <QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qtwaylandcompositorglobal_p.h>
#if QT_CONFIG(wayland_compositor_quick)
#include <QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qtwaylandcompositorglobal_p.h>
#include <QtWaylandCompositor/QtWaylandCompositor>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qwaylandxdgshellintegration_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtWaylandCompositor/private/qwaylandxdgshellintegration_p.h>
#include <QtWaylandCompositor/QWaylandXdgSurface>
#include <QtWaylandCompositor/QWaylandCompositor>
#include <QtWaylandCompositor/QWaylandSeat>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtwayland/src/compositor/extensions/qwaylandxdgshellintegration.cpp, line 15, as local:qwaylandxdgshellintegration.cpp:handlePopupCreated
namespace QtWayland {
static void handlePopupCreated(QWaylandQuickShellSurfaceItem *parentItem, QWaylandXdgPopup *popup)
{
    if (parentItem->shellSurface() == popup->parentXdgSurface())
        QWaylandQuickShellSurfaceItemPrivate::get(parentItem)->maybeCreateAutoPopup(popup->xdgSurface());
}
}  // namespace QtWayland

//  from QtWaylandCompositor__QtWayland_XdgPopupIntegration.cpp, line 1, as moc:QtWayland::XdgPopupIntegration
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN9QtWayland19XdgPopupIntegrationE_t {};
} // unnamed namespace

template <> constexpr inline auto QtWayland::XdgPopupIntegration::qt_create_metaobjectdata<qt_meta_tag_ZN9QtWayland19XdgPopupIntegrationE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QtWayland::XdgPopupIntegration",
        "handleGeometryChanged",
        ""
    };

    QtMocHelpers::UintData qt_methods {
        // Slot 'handleGeometryChanged'
        QtMocHelpers::SlotData<void()>(1, 2, QMC::AccessPrivate, QMetaType::Void),
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<XdgPopupIntegration, qt_meta_tag_ZN9QtWayland19XdgPopupIntegrationE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject QtWayland::XdgPopupIntegration::staticMetaObject = { {
    QMetaObject::SuperData::link<QWaylandQuickShellIntegration::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN9QtWayland19XdgPopupIntegrationE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN9QtWayland19XdgPopupIntegrationE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN9QtWayland19XdgPopupIntegrationE_t>.metaTypes,
    nullptr
} };

void QtWayland::XdgPopupIntegration::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<XdgPopupIntegration *>(_o);
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: _t->handleGeometryChanged(); break;
        default: ;
        }
    }
    (void)_a;
}

const QMetaObject *QtWayland::XdgPopupIntegration::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QtWayland::XdgPopupIntegration::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN9QtWayland19XdgPopupIntegrationE_t>.strings))
        return static_cast<void*>(this);
    return QWaylandQuickShellIntegration::qt_metacast(_clname);
}

int QtWayland::XdgPopupIntegration::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QWaylandQuickShellIntegration::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 1)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 1;
    }
    if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 1)
            *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType();
        _id -= 1;
    }
    return _id;
}
QT_WARNING_POP

//  from ../qtwayland/src/compositor/extensions/qwaylandxdgshellintegration.cpp, line 290, as _ZN9QtWayland19XdgPopupIntegration21handleGeometryChangedEv
namespace QtWayland {
inline void XdgPopupIntegration::handleGeometryChanged()
{
    if (m_item->view()->output()) {
        const QPoint windowOffset = m_popup->parentXdgSurface()->windowGeometry().topLeft();
        const QPoint surfacePosition = m_popup->unconstrainedPosition() + windowOffset;
        const QPoint itemPosition = m_item->mapFromSurface(surfacePosition).toPoint();
        //TODO: positioner size or other size...?
        //TODO check positioner constraints etc... sliding, flipping
        m_item->moveItem()->setPosition(itemPosition);
    } else {
        qWarning() << "XdgPopupIntegration popup item without output" << m_item;
    }
}
}  // namespace QtWayland

//  from ../qtwayland/src/compositor/extensions/qwaylandxdgshellintegration.cpp, line 274, as _ZN9QtWayland19XdgPopupIntegrationC1EP29QWaylandQuickShellSurfaceItem
namespace QtWayland {
inline XdgPopupIntegration::XdgPopupIntegration(QWaylandQuickShellSurfaceItem *item)
    : m_item(item)
    , m_xdgSurface(qobject_cast<QWaylandXdgSurface *>(item->shellSurface()))
    , m_popup(m_xdgSurface->popup())
{
    Q_ASSERT(m_popup);

    m_item->setSurface(m_xdgSurface->surface());
    handleGeometryChanged();

    connect(m_popup, &QWaylandXdgPopup::configuredGeometryChanged, this, &XdgPopupIntegration::handleGeometryChanged);
    connect(m_xdgSurface->shell(), &QWaylandXdgShell::popupCreated, this, [item](QWaylandXdgPopup *popup, QWaylandXdgSurface *){
        handlePopupCreated(item, popup);
    });
}
}  // namespace QtWayland
//  -----------------------------------------------------------------------

//  const QMetaObject *QtWayland::XdgPopupIntegration::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9QtWayland19XdgPopupIntegration10metaObjectEv(
    const QtWayland::XdgPopupIntegration *self) {
  return self->metaObject();
}

//  void *QtWayland::XdgPopupIntegration::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN9QtWayland19XdgPopupIntegration11qt_metacastEPKc(
    QtWayland::XdgPopupIntegration *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QtWayland::XdgPopupIntegration::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN9QtWayland19XdgPopupIntegration11qt_metacallEN11QMetaObject4CallEiPPv(
    QtWayland::XdgPopupIntegration *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QtWayland::XdgPopupIntegration::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN9QtWayland19XdgPopupIntegration2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QtWayland::XdgPopupIntegration::tr(s, c, n));
}

//  QtWayland::XdgPopupIntegration::XdgPopupIntegration(QWaylandQuickShellSur
//      faceItem *item)
extern "C" Q_DECL_EXPORT
QtWayland::XdgPopupIntegration *ritual_ZN9QtWayland19XdgPopupIntegrationC1EP29QWaylandQuickShellSurfaceItem(
    QWaylandQuickShellSurfaceItem *item) {
  return new QtWayland::XdgPopupIntegration(item);
}

//  void QtWayland::XdgPopupIntegration::handleGeometryChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtWayland19XdgPopupIntegration21handleGeometryChangedEv(
    QtWayland::XdgPopupIntegration *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QtWayland::XdgPopupIntegration")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "handleGeometryChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "handleGeometryChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

#endif  // QT_CONFIG(wayland_compositor_quick)
