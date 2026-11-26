//  Written by dev_tooling.RitualGenerator from the records of QtWaylandCompo
//  sitor/6.12.0/QtWaylandCompositor/private/qwaylandxdgshellintegration_p.h,
//  Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for
//  'QtWayland::XdgToplevelIntegration' is pasted in, cut from what the moc
//  of Qt 6.12.0 writes for its header: Qt's library keeps it to itself;
//  added are 2 rituals that lean on what moc writes for a class of the part
//  Qt keeps to itself, whose ritual file carries moc's output, drafted by a
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
#include <QtCore/qpoint.h>
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
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtwayland/src/compositor/extensions/qwaylandxdgshellintegration.cpp, line 15, as local:qwaylandxdgshellintegration.cpp:handlePopupCreated
namespace QtWayland {
static void handlePopupCreated(QWaylandQuickShellSurfaceItem *parentItem, QWaylandXdgPopup *popup)
{
    if (parentItem->shellSurface() == popup->parentXdgSurface())
        QWaylandQuickShellSurfaceItemPrivate::get(parentItem)->maybeCreateAutoPopup(popup->xdgSurface());
}
}  // namespace QtWayland

//  from QtWaylandCompositor__QtWayland_XdgToplevelIntegration.cpp, line 1, as moc:QtWayland::XdgToplevelIntegration
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN9QtWayland22XdgToplevelIntegrationE_t {};
} // unnamed namespace

template <> constexpr inline auto QtWayland::XdgToplevelIntegration::qt_create_metaobjectdata<qt_meta_tag_ZN9QtWayland22XdgToplevelIntegrationE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QtWayland::XdgToplevelIntegration",
        "handleStartMove",
        "",
        "QWaylandSeat*",
        "seat",
        "handleStartResize",
        "Qt::Edges",
        "edges",
        "handleSetMaximized",
        "handleUnsetMaximized",
        "handleMaximizedChanged",
        "handleSetFullscreen",
        "handleUnsetFullscreen",
        "handleFullscreenChanged",
        "handleActivatedChanged",
        "handleSurfaceSizeChanged",
        "handleToplevelDestroyed",
        "handleMaximizedSizeChanged",
        "handleFullscreenSizeChanged"
    };

    QtMocHelpers::UintData qt_methods {
        // Slot 'handleStartMove'
        QtMocHelpers::SlotData<void(QWaylandSeat *)>(1, 2, QMC::AccessPrivate, QMetaType::Void, {{
            { 0x80000000 | 3, 4 },
        }}),
        // Slot 'handleStartResize'
        QtMocHelpers::SlotData<void(QWaylandSeat *, Qt::Edges)>(5, 2, QMC::AccessPrivate, QMetaType::Void, {{
            { 0x80000000 | 3, 4 }, { 0x80000000 | 6, 7 },
        }}),
        // Slot 'handleSetMaximized'
        QtMocHelpers::SlotData<void()>(8, 2, QMC::AccessPrivate, QMetaType::Void),
        // Slot 'handleUnsetMaximized'
        QtMocHelpers::SlotData<void()>(9, 2, QMC::AccessPrivate, QMetaType::Void),
        // Slot 'handleMaximizedChanged'
        QtMocHelpers::SlotData<void()>(10, 2, QMC::AccessPrivate, QMetaType::Void),
        // Slot 'handleSetFullscreen'
        QtMocHelpers::SlotData<void()>(11, 2, QMC::AccessPrivate, QMetaType::Void),
        // Slot 'handleUnsetFullscreen'
        QtMocHelpers::SlotData<void()>(12, 2, QMC::AccessPrivate, QMetaType::Void),
        // Slot 'handleFullscreenChanged'
        QtMocHelpers::SlotData<void()>(13, 2, QMC::AccessPrivate, QMetaType::Void),
        // Slot 'handleActivatedChanged'
        QtMocHelpers::SlotData<void()>(14, 2, QMC::AccessPrivate, QMetaType::Void),
        // Slot 'handleSurfaceSizeChanged'
        QtMocHelpers::SlotData<void()>(15, 2, QMC::AccessPrivate, QMetaType::Void),
        // Slot 'handleToplevelDestroyed'
        QtMocHelpers::SlotData<void()>(16, 2, QMC::AccessPrivate, QMetaType::Void),
        // Slot 'handleMaximizedSizeChanged'
        QtMocHelpers::SlotData<void()>(17, 2, QMC::AccessPrivate, QMetaType::Void),
        // Slot 'handleFullscreenSizeChanged'
        QtMocHelpers::SlotData<void()>(18, 2, QMC::AccessPrivate, QMetaType::Void),
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<XdgToplevelIntegration, qt_meta_tag_ZN9QtWayland22XdgToplevelIntegrationE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject QtWayland::XdgToplevelIntegration::staticMetaObject = { {
    QMetaObject::SuperData::link<QWaylandQuickShellIntegration::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN9QtWayland22XdgToplevelIntegrationE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN9QtWayland22XdgToplevelIntegrationE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN9QtWayland22XdgToplevelIntegrationE_t>.metaTypes,
    nullptr
} };

void QtWayland::XdgToplevelIntegration::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<XdgToplevelIntegration *>(_o);
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: _t->handleStartMove((*reinterpret_cast<std::add_pointer_t<QWaylandSeat*>>(_a[1]))); break;
        case 1: _t->handleStartResize((*reinterpret_cast<std::add_pointer_t<QWaylandSeat*>>(_a[1])),(*reinterpret_cast<std::add_pointer_t<Qt::Edges>>(_a[2]))); break;
        case 2: _t->handleSetMaximized(); break;
        case 3: _t->handleUnsetMaximized(); break;
        case 4: _t->handleMaximizedChanged(); break;
        case 5: _t->handleSetFullscreen(); break;
        case 6: _t->handleUnsetFullscreen(); break;
        case 7: _t->handleFullscreenChanged(); break;
        case 8: _t->handleActivatedChanged(); break;
        case 9: _t->handleSurfaceSizeChanged(); break;
        case 10: _t->handleToplevelDestroyed(); break;
        case 11: _t->handleMaximizedSizeChanged(); break;
        case 12: _t->handleFullscreenSizeChanged(); break;
        default: ;
        }
    }
}

const QMetaObject *QtWayland::XdgToplevelIntegration::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QtWayland::XdgToplevelIntegration::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN9QtWayland22XdgToplevelIntegrationE_t>.strings))
        return static_cast<void*>(this);
    return QWaylandQuickShellIntegration::qt_metacast(_clname);
}

int QtWayland::XdgToplevelIntegration::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QWaylandQuickShellIntegration::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 13)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 13;
    }
    if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 13)
            *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType();
        _id -= 13;
    }
    return _id;
}
QT_WARNING_POP

//  from ../qtwayland/src/compositor/extensions/qwaylandxdgshellintegration.cpp, line 48, as _ZN9QtWayland22XdgToplevelIntegration11eventFilterEP7QObjectP6QEvent
namespace QtWayland {
inline bool XdgToplevelIntegration::eventFilter(QObject *object, QEvent *event)
{
    if (event->type() == QEvent::MouseMove) {
        QMouseEvent *mouseEvent = static_cast<QMouseEvent *>(event);
        return filterMouseMoveEvent(mouseEvent);
    } else if (event->type() == QEvent::MouseButtonRelease || event->type() == QEvent::TouchEnd || event->type() == QEvent::TouchCancel) {
        return filterPointerReleaseEvent();
    } else if (event->type() == QEvent::TouchUpdate) {
        QTouchEvent *touchEvent = static_cast<QTouchEvent *>(event);
        return filterTouchUpdateEvent(touchEvent);
    }
    return QWaylandQuickShellIntegration::eventFilter(object, event);
}
}  // namespace QtWayland

//  from ../qtwayland/src/compositor/extensions/qwaylandxdgshellintegration.cpp, line 117, as _ZN9QtWayland22XdgToplevelIntegration15handleStartMoveEP12QWaylandSeat
namespace QtWayland {
inline void XdgToplevelIntegration::handleStartMove(QWaylandSeat *seat)
{
    grabberState = GrabberState::Move;
    moveState.seat = seat;
    moveState.initialized = false;
}
}  // namespace QtWayland

//  from ../qtwayland/src/compositor/extensions/qwaylandxdgshellintegration.cpp, line 124, as _ZN9QtWayland22XdgToplevelIntegration17handleStartResizeEP12QWaylandSeat6QFlagsIN2Qt4EdgeEE
namespace QtWayland {
inline void XdgToplevelIntegration::handleStartResize(QWaylandSeat *seat, Qt::Edges edges)
{
    grabberState = GrabberState::Resize;
    resizeState.seat = seat;
    resizeState.resizeEdges = edges;
    resizeState.initialWindowSize = m_xdgSurface->windowGeometry().size();
    resizeState.initialPosition = m_item->moveItem()->position();
    resizeState.initialSurfaceSize = m_item->surface()->destinationSize();
    resizeState.initialized = false;
}
}  // namespace QtWayland

//  from ../qtwayland/src/compositor/extensions/qwaylandxdgshellintegration.cpp, line 135, as _ZN9QtWayland22XdgToplevelIntegration18handleSetMaximizedEv
namespace QtWayland {
inline void XdgToplevelIntegration::handleSetMaximized()
{
    if (!m_item->view()->isPrimary())
        return;

    QList<QWaylandXdgToplevel::State> states = m_toplevel->states();

    if (!states.contains(QWaylandXdgToplevel::State::FullscreenState) && !states.contains(QWaylandXdgToplevel::State::MaximizedState)) {
        windowedGeometry.initialWindowSize = m_xdgSurface->windowGeometry().size();
        windowedGeometry.initialPosition = m_item->moveItem()->position();
    }

    // Any prior output-resize handlers are irrelevant at this point.
    disconnect(nonwindowedState.sizeChangedConnection);
    nonwindowedState.output = m_item->view()->output();
    nonwindowedState.sizeChangedConnection = connect(nonwindowedState.output, &QWaylandOutput::availableGeometryChanged, this, &XdgToplevelIntegration::handleMaximizedSizeChanged);
    handleMaximizedSizeChanged();
}
}  // namespace QtWayland

//  from ../qtwayland/src/compositor/extensions/qwaylandxdgshellintegration.cpp, line 191, as _ZN9QtWayland22XdgToplevelIntegration19handleSetFullscreenEv
namespace QtWayland {
inline void XdgToplevelIntegration::handleSetFullscreen()
{
    if (!m_item->view()->isPrimary())
        return;

    QList<QWaylandXdgToplevel::State> states = m_toplevel->states();

    if (!states.contains(QWaylandXdgToplevel::State::FullscreenState) && !states.contains(QWaylandXdgToplevel::State::MaximizedState)) {
        windowedGeometry.initialWindowSize = m_xdgSurface->windowGeometry().size();
        windowedGeometry.initialPosition = m_item->moveItem()->position();
    }

    // Any prior output-resize handlers are irrelevant at this point.
    disconnect(nonwindowedState.sizeChangedConnection);
    nonwindowedState.output = m_item->view()->output();
    nonwindowedState.sizeChangedConnection = connect(nonwindowedState.output, &QWaylandOutput::geometryChanged, this, &XdgToplevelIntegration::handleFullscreenSizeChanged);
    handleFullscreenSizeChanged();
}
}  // namespace QtWayland

//  from ../qtwayland/src/compositor/extensions/qwaylandxdgshellintegration.cpp, line 164, as _ZN9QtWayland22XdgToplevelIntegration20handleUnsetMaximizedEv
namespace QtWayland {
inline void XdgToplevelIntegration::handleUnsetMaximized()
{
    if (!m_item->view()->isPrimary())
        return;

    // If no prior windowed size was recorded, send a 0x0 configure event
    // to allow the client to choose its preferred size.
    if (windowedGeometry.initialWindowSize.isValid())
        m_toplevel->sendUnmaximized(windowedGeometry.initialWindowSize);
    else
        m_toplevel->sendUnmaximized();
}
}  // namespace QtWayland

//  from ../qtwayland/src/compositor/extensions/qwaylandxdgshellintegration.cpp, line 220, as _ZN9QtWayland22XdgToplevelIntegration21handleUnsetFullscreenEv
namespace QtWayland {
inline void XdgToplevelIntegration::handleUnsetFullscreen()
{
    if (!m_item->view()->isPrimary())
        return;

    // If no prior windowed size was recorded, send a 0x0 configure event
    // to allow the client to choose its preferred size.
    if (windowedGeometry.initialWindowSize.isValid())
        m_toplevel->sendUnmaximized(windowedGeometry.initialWindowSize);
    else
        m_toplevel->sendUnmaximized();
}
}  // namespace QtWayland

//  from ../qtwayland/src/compositor/extensions/qwaylandxdgshellintegration.cpp, line 247, as _ZN9QtWayland22XdgToplevelIntegration22handleActivatedChangedEv
namespace QtWayland {
inline void XdgToplevelIntegration::handleActivatedChanged()
{
    if (m_toplevel->activated())
        m_item->raise();
}
}  // namespace QtWayland

//  from ../qtwayland/src/compositor/extensions/qwaylandxdgshellintegration.cpp, line 177, as _ZN9QtWayland22XdgToplevelIntegration22handleMaximizedChangedEv
namespace QtWayland {
inline void XdgToplevelIntegration::handleMaximizedChanged()
{
    if (m_toplevel->maximized()) {
        if (auto *output = m_item->view()->output()) {
            m_item->moveItem()->setPosition(output->position() + output->availableGeometry().topLeft());
        } else {
            qCWarning(qLcWaylandCompositor) << "The view does not have a corresponding output,"
                                            << "ignoring maximized state";
        }
    } else {
        m_item->moveItem()->setPosition(windowedGeometry.initialPosition);
    }
}
}  // namespace QtWayland

//  from ../qtwayland/src/compositor/extensions/qwaylandxdgshellintegration.cpp, line 233, as _ZN9QtWayland22XdgToplevelIntegration23handleFullscreenChangedEv
namespace QtWayland {
inline void XdgToplevelIntegration::handleFullscreenChanged()
{
    if (m_toplevel->fullscreen()) {
        if (auto *output = m_item->view()->output()) {
            m_item->moveItem()->setPosition(output->position() + output->geometry().topLeft());
        } else {
            qCWarning(qLcWaylandCompositor) << "The view does not have a corresponding output,"
                                            << "ignoring fullscreen state";
        }
    } else {
        m_item->moveItem()->setPosition(windowedGeometry.initialPosition);
    }
}
}  // namespace QtWayland

//  from ../qtwayland/src/compositor/extensions/qwaylandxdgshellintegration.cpp, line 267, as _ZN9QtWayland22XdgToplevelIntegration23handleToplevelDestroyedEv
namespace QtWayland {
inline void XdgToplevelIntegration::handleToplevelDestroyed()
{
    // Disarm any handlers that might fire on the now-stale toplevel pointer
    nonwindowedState.output = nullptr;
    disconnect(nonwindowedState.sizeChangedConnection);
}
}  // namespace QtWayland

//  from ../qtwayland/src/compositor/extensions/qwaylandxdgshellintegration.cpp, line 253, as _ZN9QtWayland22XdgToplevelIntegration24handleSurfaceSizeChangedEv
namespace QtWayland {
inline void XdgToplevelIntegration::handleSurfaceSizeChanged()
{
    if (grabberState == GrabberState::Resize) {
        qreal dx = 0;
        qreal dy = 0;
        if (resizeState.resizeEdges & Qt::TopEdge)
            dy = resizeState.initialSurfaceSize.height() - m_item->surface()->destinationSize().height();
        if (resizeState.resizeEdges & Qt::LeftEdge)
            dx = resizeState.initialSurfaceSize.width() - m_item->surface()->destinationSize().width();
        QPointF offset = m_item->mapFromSurface({dx, dy});
        m_item->moveItem()->setPosition(resizeState.initialPosition + offset);
    }
}
}  // namespace QtWayland

//  from ../qtwayland/src/compositor/extensions/qwaylandxdgshellintegration.cpp, line 154, as _ZN9QtWayland22XdgToplevelIntegration26handleMaximizedSizeChangedEv
namespace QtWayland {
inline void XdgToplevelIntegration::handleMaximizedSizeChanged()
{
    // Insurance against handleToplevelDestroyed() not managing to disconnect this
    // handler in time.
    if (m_toplevel == nullptr)
        return;

    m_toplevel->sendMaximized(nonwindowedState.output->availableGeometry().size() / nonwindowedState.output->scaleFactor());
}
}  // namespace QtWayland

//  from ../qtwayland/src/compositor/extensions/qwaylandxdgshellintegration.cpp, line 210, as _ZN9QtWayland22XdgToplevelIntegration27handleFullscreenSizeChangedEv
namespace QtWayland {
inline void XdgToplevelIntegration::handleFullscreenSizeChanged()
{
    // Insurance against handleToplevelDestroyed() not managing to disconnect this
    // handler in time.
    if (m_toplevel == nullptr)
        return;

    m_toplevel->sendFullscreen(nonwindowedState.output->geometry().size() / nonwindowedState.output->scaleFactor());
}
}  // namespace QtWayland

//  from ../qtwayland/src/compositor/extensions/qwaylandxdgshellintegration.cpp, line 21, as _ZN9QtWayland22XdgToplevelIntegrationC1EP29QWaylandQuickShellSurfaceItem
namespace QtWayland {
inline XdgToplevelIntegration::XdgToplevelIntegration(QWaylandQuickShellSurfaceItem *item)
    : QWaylandQuickShellIntegration(item)
    , m_item(item)
    , m_xdgSurface(qobject_cast<QWaylandXdgSurface *>(item->shellSurface()))
    , m_toplevel(m_xdgSurface->toplevel())
    , grabberState(GrabberState::Default)
{
    Q_ASSERT(m_toplevel);

    m_item->setSurface(m_xdgSurface->surface());

    connect(m_toplevel, &QWaylandXdgToplevel::startMove, this, &XdgToplevelIntegration::handleStartMove);
    connect(m_toplevel, &QWaylandXdgToplevel::startResize, this, &XdgToplevelIntegration::handleStartResize);
    connect(m_toplevel, &QWaylandXdgToplevel::setMaximized, this, &XdgToplevelIntegration::handleSetMaximized);
    connect(m_toplevel, &QWaylandXdgToplevel::unsetMaximized, this, &XdgToplevelIntegration::handleUnsetMaximized);
    connect(m_toplevel, &QWaylandXdgToplevel::maximizedChanged, this, &XdgToplevelIntegration::handleMaximizedChanged);
    connect(m_toplevel, &QWaylandXdgToplevel::setFullscreen, this, &XdgToplevelIntegration::handleSetFullscreen);
    connect(m_toplevel, &QWaylandXdgToplevel::unsetFullscreen, this, &XdgToplevelIntegration::handleUnsetFullscreen);
    connect(m_toplevel, &QWaylandXdgToplevel::fullscreenChanged, this, &XdgToplevelIntegration::handleFullscreenChanged);
    connect(m_toplevel, &QWaylandXdgToplevel::activatedChanged, this, &XdgToplevelIntegration::handleActivatedChanged);
    connect(m_xdgSurface->shell(), &QWaylandXdgShell::popupCreated, this, [item](QWaylandXdgPopup *popup, QWaylandXdgSurface *){
        handlePopupCreated(item, popup);
    });
    connect(m_xdgSurface->surface(), &QWaylandSurface::destinationSizeChanged, this, &XdgToplevelIntegration::handleSurfaceSizeChanged);
    connect(m_toplevel, &QObject::destroyed, this, &XdgToplevelIntegration::handleToplevelDestroyed);
}
}  // namespace QtWayland

//  from ../qtwayland/src/compositor/extensions/qwaylandxdgshellintegration.cpp, line 62, as _ZN9QtWayland22XdgToplevelIntegration22filterPointerMoveEventERK7QPointF
namespace QtWayland {
inline bool XdgToplevelIntegration::filterPointerMoveEvent(const QPointF &scenePosition)
{
    if (grabberState == GrabberState::Resize) {
        if (!resizeState.initialized) {
            resizeState.initialMousePos = scenePosition;
            resizeState.initialized = true;
            return true;
        }
        QPointF delta = m_item->mapToSurface(scenePosition - resizeState.initialMousePos);
        QSize newSize = m_toplevel->sizeForResize(resizeState.initialWindowSize, delta, resizeState.resizeEdges);
        m_toplevel->sendResizing(newSize);
    } else if (grabberState == GrabberState::Move) {
        QQuickItem *moveItem = m_item->moveItem();
        if (!moveState.initialized) {
            moveState.initialOffset = moveItem->mapFromItem(nullptr, scenePosition);
            moveState.initialized = true;
            return true;
        }
        if (!moveItem->parentItem())
            return true;
        QPointF parentPos = moveItem->parentItem()->mapFromItem(nullptr, scenePosition);
        moveItem->setPosition(parentPos - moveState.initialOffset);
    }
    return false;
}
}  // namespace QtWayland

//  from ../qtwayland/src/compositor/extensions/qwaylandxdgshellintegration.cpp, line 100, as _ZN9QtWayland22XdgToplevelIntegration20filterMouseMoveEventEP11QMouseEvent
namespace QtWayland {
inline bool XdgToplevelIntegration::filterMouseMoveEvent(QMouseEvent *event)
{
    Q_ASSERT(grabberState != GrabberState::Move || moveState.seat == m_item->compositor()->seatFor(event));
    Q_ASSERT(grabberState != GrabberState::Resize || resizeState.seat == m_item->compositor()->seatFor(event));

    return filterPointerMoveEvent(event->scenePosition());
}
}  // namespace QtWayland

//  from ../qtwayland/src/compositor/extensions/qwaylandxdgshellintegration.cpp, line 108, as _ZN9QtWayland22XdgToplevelIntegration25filterPointerReleaseEventEv
namespace QtWayland {
inline bool XdgToplevelIntegration::filterPointerReleaseEvent()
{
    if (grabberState != GrabberState::Default) {
        grabberState = GrabberState::Default;
        return true;
    }
    return false;
}
}  // namespace QtWayland

//  from ../qtwayland/src/compositor/extensions/qwaylandxdgshellintegration.cpp, line 88, as _ZN9QtWayland22XdgToplevelIntegration22filterTouchUpdateEventEP11QTouchEvent
namespace QtWayland {
inline bool XdgToplevelIntegration::filterTouchUpdateEvent(QTouchEvent *event)
{
    if (event->pointCount() == 0)
        return false;

    Q_ASSERT(grabberState != GrabberState::Move || moveState.seat == m_item->compositor()->seatFor(event));
    Q_ASSERT(grabberState != GrabberState::Resize || resizeState.seat == m_item->compositor()->seatFor(event));

    QEventPoint point = event->points().first();
    return filterPointerMoveEvent(point.scenePosition());
 }
}  // namespace QtWayland
//  -----------------------------------------------------------------------

//  Only a class built on QtWayland::XdgToplevelIntegration may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQtWayland_XdgToplevelIntegration : QtWayland::XdgToplevelIntegration {
  using QtWayland::XdgToplevelIntegration::eventFilter;
};

//  const QMetaObject *QtWayland::XdgToplevelIntegration::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9QtWayland22XdgToplevelIntegration10metaObjectEv(
    const QtWayland::XdgToplevelIntegration *self) {
  return self->metaObject();
}

//  void *QtWayland::XdgToplevelIntegration::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN9QtWayland22XdgToplevelIntegration11qt_metacastEPKc(
    QtWayland::XdgToplevelIntegration *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QtWayland::XdgToplevelIntegration::qt_metacall(QMetaObject::Call a0,
//      int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN9QtWayland22XdgToplevelIntegration11qt_metacallEN11QMetaObject4CallEiPPv(
    QtWayland::XdgToplevelIntegration *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QtWayland::XdgToplevelIntegration::tr(const char *s, const char
//      *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN9QtWayland22XdgToplevelIntegration2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QtWayland::XdgToplevelIntegration::tr(s, c, n));
}

//  QtWayland::XdgToplevelIntegration::XdgToplevelIntegration(QWaylandQuickSh
//      ellSurfaceItem *item)
extern "C" Q_DECL_EXPORT
QtWayland::XdgToplevelIntegration *ritual_ZN9QtWayland22XdgToplevelIntegrationC1EP29QWaylandQuickShellSurfaceItem(
    QWaylandQuickShellSurfaceItem *item) {
  return new QtWayland::XdgToplevelIntegration(item);
}

//  bool QtWayland::XdgToplevelIntegration::eventFilter(QObject *object,
//      QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QtWayland22XdgToplevelIntegration11eventFilterEP7QObjectP6QEvent(
    QtWayland::XdgToplevelIntegration *self,
    QObject *object,
    QEvent *event) {
  return self->eventFilter(object, event);
}

//  void QtWayland::XdgToplevelIntegration::handleStartMove(QWaylandSeat
//      *seat)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtWayland22XdgToplevelIntegration15handleStartMoveEP12QWaylandSeat(
    QtWayland::XdgToplevelIntegration *self,
    QWaylandSeat *seat) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QtWayland::XdgToplevelIntegration")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "handleStartMove(QWaylandSeat *)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "handleStartMove(QWaylandSeat *)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&seat)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QtWayland::XdgToplevelIntegration::handleStartResize(QWaylandSeat
//      *seat, Qt::Edges edges)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtWayland22XdgToplevelIntegration17handleStartResizeEP12QWaylandSeat6QFlagsIN2Qt4EdgeEE(
    QtWayland::XdgToplevelIntegration *self,
    QWaylandSeat *seat,
    int edges) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QtWayland::XdgToplevelIntegration")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "handleStartResize(QWaylandSeat *,Qt::Edges)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "handleStartResize(QWaylandSeat *,Qt::Edges)");
  Qt::Edges value1 = QFlags<Qt::Edge>::fromInt(edges);
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&seat)),
      const_cast<void *>(static_cast<const void *>(&value1)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QtWayland::XdgToplevelIntegration::handleSetMaximized()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtWayland22XdgToplevelIntegration18handleSetMaximizedEv(
    QtWayland::XdgToplevelIntegration *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QtWayland::XdgToplevelIntegration")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "handleSetMaximized()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "handleSetMaximized()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QtWayland::XdgToplevelIntegration::handleUnsetMaximized()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtWayland22XdgToplevelIntegration20handleUnsetMaximizedEv(
    QtWayland::XdgToplevelIntegration *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QtWayland::XdgToplevelIntegration")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "handleUnsetMaximized()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "handleUnsetMaximized()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QtWayland::XdgToplevelIntegration::handleMaximizedChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtWayland22XdgToplevelIntegration22handleMaximizedChangedEv(
    QtWayland::XdgToplevelIntegration *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QtWayland::XdgToplevelIntegration")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "handleMaximizedChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "handleMaximizedChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QtWayland::XdgToplevelIntegration::handleSetFullscreen()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtWayland22XdgToplevelIntegration19handleSetFullscreenEv(
    QtWayland::XdgToplevelIntegration *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QtWayland::XdgToplevelIntegration")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "handleSetFullscreen()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "handleSetFullscreen()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QtWayland::XdgToplevelIntegration::handleUnsetFullscreen()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtWayland22XdgToplevelIntegration21handleUnsetFullscreenEv(
    QtWayland::XdgToplevelIntegration *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QtWayland::XdgToplevelIntegration")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "handleUnsetFullscreen()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "handleUnsetFullscreen()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QtWayland::XdgToplevelIntegration::handleFullscreenChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtWayland22XdgToplevelIntegration23handleFullscreenChangedEv(
    QtWayland::XdgToplevelIntegration *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QtWayland::XdgToplevelIntegration")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "handleFullscreenChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "handleFullscreenChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QtWayland::XdgToplevelIntegration::handleActivatedChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtWayland22XdgToplevelIntegration22handleActivatedChangedEv(
    QtWayland::XdgToplevelIntegration *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QtWayland::XdgToplevelIntegration")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "handleActivatedChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "handleActivatedChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QtWayland::XdgToplevelIntegration::handleSurfaceSizeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtWayland22XdgToplevelIntegration24handleSurfaceSizeChangedEv(
    QtWayland::XdgToplevelIntegration *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QtWayland::XdgToplevelIntegration")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "handleSurfaceSizeChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "handleSurfaceSizeChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QtWayland::XdgToplevelIntegration::handleToplevelDestroyed()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtWayland22XdgToplevelIntegration23handleToplevelDestroyedEv(
    QtWayland::XdgToplevelIntegration *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QtWayland::XdgToplevelIntegration")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "handleToplevelDestroyed()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "handleToplevelDestroyed()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QtWayland::XdgToplevelIntegration::handleMaximizedSizeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtWayland22XdgToplevelIntegration26handleMaximizedSizeChangedEv(
    QtWayland::XdgToplevelIntegration *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QtWayland::XdgToplevelIntegration")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "handleMaximizedSizeChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "handleMaximizedSizeChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QtWayland::XdgToplevelIntegration::handleFullscreenSizeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtWayland22XdgToplevelIntegration27handleFullscreenSizeChangedEv(
    QtWayland::XdgToplevelIntegration *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QtWayland::XdgToplevelIntegration")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "handleFullscreenSizeChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "handleFullscreenSizeChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  bool QtWayland::XdgToplevelIntegration::filterPointerMoveEvent(const
//      QPointF &scenePosition)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QtWayland22XdgToplevelIntegration22filterPointerMoveEventERK7QPointF(
    QtWayland::XdgToplevelIntegration *self,
    const QPointF *scenePosition) {
  return self->filterPointerMoveEvent(*scenePosition);
}

//  bool QtWayland::XdgToplevelIntegration::filterMouseMoveEvent(QMouseEvent
//      *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QtWayland22XdgToplevelIntegration20filterMouseMoveEventEP11QMouseEvent(
    QtWayland::XdgToplevelIntegration *self,
    QMouseEvent *event) {
  return self->filterMouseMoveEvent(event);
}

//  bool QtWayland::XdgToplevelIntegration::filterPointerReleaseEvent()
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QtWayland22XdgToplevelIntegration25filterPointerReleaseEventEv(
    QtWayland::XdgToplevelIntegration *self) {
  return self->filterPointerReleaseEvent();
}

//  bool
//      QtWayland::XdgToplevelIntegration::filterTouchUpdateEvent(QTouchEvent
//      *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QtWayland22XdgToplevelIntegration22filterTouchUpdateEventEP11QTouchEvent(
    QtWayland::XdgToplevelIntegration *self,
    QTouchEvent *event) {
  return self->filterTouchUpdateEvent(event);
}

//  bool QtWayland::XdgToplevelIntegration::eventFilter(QObject *object,
//      QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN9QtWayland22XdgToplevelIntegration11eventFilterEP7QObjectP6QEvent(
    QtWayland::XdgToplevelIntegration *self,
    QObject *object,
    QEvent *event) {
  return static_cast<OwnQtWayland_XdgToplevelIntegration *>(self)->OwnQtWayland_XdgToplevelIntegration::eventFilter(
      object,
      event);
}

#endif  // QT_CONFIG(wayland_compositor_quick)
