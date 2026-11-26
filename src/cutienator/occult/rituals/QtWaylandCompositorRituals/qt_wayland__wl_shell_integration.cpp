//  Written by dev_tooling.RitualGenerator from the records of QtWaylandCompo
//  sitor/6.12.0/QtWaylandCompositor/private/qwaylandwlshellintegration_p.h,
//  Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for
//  'QtWayland::WlShellIntegration' is pasted in, cut from what the moc of Qt
//  6.12.0 writes for its header: Qt's library keeps it to itself; added are
//  2 rituals that lean on what moc writes for a class of the part Qt keeps
//  to itself, whose ritual file carries moc's output, drafted by a copy of
//  the generator that lets those names through. A copy of a meta-object is a
//  second one: 'qobject_cast' between it and Qt's own does not match. Kept
//  as it is when the generator runs again.
#include <QtWaylandCompositor/qtwaylandcompositorglobal.h>
#include <QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qtwaylandcompositorglobal_p.h>
#if QT_CONFIG(wayland_compositor_quick)
#include <QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qtwaylandcompositorglobal_p.h>
#include <QtWaylandCompositor/QtWaylandCompositor>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qwaylandwlshellintegration_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qpoint.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtWaylandCompositor/private/qwaylandwlshellintegration_p.h>
#include <QtWaylandCompositor/QWaylandCompositor>
#include <QtWaylandCompositor/QWaylandWlShellSurface>
#include <QtWaylandCompositor/QWaylandQuickShellSurfaceItem>
#include <QtWaylandCompositor/QWaylandSeat>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from QtWaylandCompositor__QtWayland_WlShellIntegration.cpp, line 1, as moc:QtWayland::WlShellIntegration
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN9QtWayland18WlShellIntegrationE_t {};
} // unnamed namespace

template <> constexpr inline auto QtWayland::WlShellIntegration::qt_create_metaobjectdata<qt_meta_tag_ZN9QtWayland18WlShellIntegrationE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QtWayland::WlShellIntegration",
        "handleStartMove",
        "",
        "QWaylandSeat*",
        "seat",
        "handleStartResize",
        "QWaylandWlShellSurface::ResizeEdge",
        "edges",
        "handleSetDefaultTopLevel",
        "handleSetTransient",
        "QWaylandSurface*",
        "parentSurface",
        "QPoint",
        "relativeToParent",
        "inactive",
        "handleSetMaximized",
        "QWaylandOutput*",
        "output",
        "handleSetFullScreen",
        "QWaylandWlShellSurface::FullScreenMethod",
        "method",
        "framerate",
        "handleSetPopup",
        "parent",
        "handleShellSurfaceDestroyed",
        "handleSurfaceHasContentChanged",
        "handleRedraw",
        "adjustOffsetForNextFrame",
        "QPointF",
        "offset",
        "handleFullScreenSizeChanged",
        "handleMaximizedSizeChanged"
    };

    QtMocHelpers::UintData qt_methods {
        // Slot 'handleStartMove'
        QtMocHelpers::SlotData<void(QWaylandSeat *)>(1, 2, QMC::AccessPrivate, QMetaType::Void, {{
            { 0x80000000 | 3, 4 },
        }}),
        // Slot 'handleStartResize'
        QtMocHelpers::SlotData<void(QWaylandSeat *, QWaylandWlShellSurface::ResizeEdge)>(5, 2, QMC::AccessPrivate, QMetaType::Void, {{
            { 0x80000000 | 3, 4 }, { 0x80000000 | 6, 7 },
        }}),
        // Slot 'handleSetDefaultTopLevel'
        QtMocHelpers::SlotData<void()>(8, 2, QMC::AccessPrivate, QMetaType::Void),
        // Slot 'handleSetTransient'
        QtMocHelpers::SlotData<void(QWaylandSurface *, const QPoint &, bool)>(9, 2, QMC::AccessPrivate, QMetaType::Void, {{
            { 0x80000000 | 10, 11 }, { 0x80000000 | 12, 13 }, { QMetaType::Bool, 14 },
        }}),
        // Slot 'handleSetMaximized'
        QtMocHelpers::SlotData<void(QWaylandOutput *)>(15, 2, QMC::AccessPrivate, QMetaType::Void, {{
            { 0x80000000 | 16, 17 },
        }}),
        // Slot 'handleSetFullScreen'
        QtMocHelpers::SlotData<void(QWaylandWlShellSurface::FullScreenMethod, uint, QWaylandOutput *)>(18, 2, QMC::AccessPrivate, QMetaType::Void, {{
            { 0x80000000 | 19, 20 }, { QMetaType::UInt, 21 }, { 0x80000000 | 16, 17 },
        }}),
        // Slot 'handleSetPopup'
        QtMocHelpers::SlotData<void(QWaylandSeat *, QWaylandSurface *, const QPoint &)>(22, 2, QMC::AccessPrivate, QMetaType::Void, {{
            { 0x80000000 | 3, 4 }, { 0x80000000 | 10, 23 }, { 0x80000000 | 12, 13 },
        }}),
        // Slot 'handleShellSurfaceDestroyed'
        QtMocHelpers::SlotData<void()>(24, 2, QMC::AccessPrivate, QMetaType::Void),
        // Slot 'handleSurfaceHasContentChanged'
        QtMocHelpers::SlotData<void()>(25, 2, QMC::AccessPrivate, QMetaType::Void),
        // Slot 'handleRedraw'
        QtMocHelpers::SlotData<void()>(26, 2, QMC::AccessPrivate, QMetaType::Void),
        // Slot 'adjustOffsetForNextFrame'
        QtMocHelpers::SlotData<void(const QPointF &)>(27, 2, QMC::AccessPrivate, QMetaType::Void, {{
            { 0x80000000 | 28, 29 },
        }}),
        // Slot 'handleFullScreenSizeChanged'
        QtMocHelpers::SlotData<void()>(30, 2, QMC::AccessPrivate, QMetaType::Void),
        // Slot 'handleMaximizedSizeChanged'
        QtMocHelpers::SlotData<void()>(31, 2, QMC::AccessPrivate, QMetaType::Void),
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<WlShellIntegration, qt_meta_tag_ZN9QtWayland18WlShellIntegrationE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject QtWayland::WlShellIntegration::staticMetaObject = { {
    QMetaObject::SuperData::link<QWaylandQuickShellIntegration::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN9QtWayland18WlShellIntegrationE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN9QtWayland18WlShellIntegrationE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN9QtWayland18WlShellIntegrationE_t>.metaTypes,
    nullptr
} };

void QtWayland::WlShellIntegration::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<WlShellIntegration *>(_o);
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: _t->handleStartMove((*reinterpret_cast<std::add_pointer_t<QWaylandSeat*>>(_a[1]))); break;
        case 1: _t->handleStartResize((*reinterpret_cast<std::add_pointer_t<QWaylandSeat*>>(_a[1])),(*reinterpret_cast<std::add_pointer_t<QWaylandWlShellSurface::ResizeEdge>>(_a[2]))); break;
        case 2: _t->handleSetDefaultTopLevel(); break;
        case 3: _t->handleSetTransient((*reinterpret_cast<std::add_pointer_t<QWaylandSurface*>>(_a[1])),(*reinterpret_cast<std::add_pointer_t<QPoint>>(_a[2])),(*reinterpret_cast<std::add_pointer_t<bool>>(_a[3]))); break;
        case 4: _t->handleSetMaximized((*reinterpret_cast<std::add_pointer_t<QWaylandOutput*>>(_a[1]))); break;
        case 5: _t->handleSetFullScreen((*reinterpret_cast<std::add_pointer_t<QWaylandWlShellSurface::FullScreenMethod>>(_a[1])),(*reinterpret_cast<std::add_pointer_t<uint>>(_a[2])),(*reinterpret_cast<std::add_pointer_t<QWaylandOutput*>>(_a[3]))); break;
        case 6: _t->handleSetPopup((*reinterpret_cast<std::add_pointer_t<QWaylandSeat*>>(_a[1])),(*reinterpret_cast<std::add_pointer_t<QWaylandSurface*>>(_a[2])),(*reinterpret_cast<std::add_pointer_t<QPoint>>(_a[3]))); break;
        case 7: _t->handleShellSurfaceDestroyed(); break;
        case 8: _t->handleSurfaceHasContentChanged(); break;
        case 9: _t->handleRedraw(); break;
        case 10: _t->adjustOffsetForNextFrame((*reinterpret_cast<std::add_pointer_t<QPointF>>(_a[1]))); break;
        case 11: _t->handleFullScreenSizeChanged(); break;
        case 12: _t->handleMaximizedSizeChanged(); break;
        default: ;
        }
    }
    if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        switch (_id) {
        default: *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType(); break;
        case 3:
            switch (*reinterpret_cast<int*>(_a[1])) {
            default: *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType(); break;
            case 0:
                *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType::fromType< QWaylandSurface* >(); break;
            }
            break;
        case 4:
            switch (*reinterpret_cast<int*>(_a[1])) {
            default: *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType(); break;
            case 0:
                *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType::fromType< QWaylandOutput* >(); break;
            }
            break;
        case 5:
            switch (*reinterpret_cast<int*>(_a[1])) {
            default: *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType(); break;
            case 2:
                *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType::fromType< QWaylandOutput* >(); break;
            }
            break;
        case 6:
            switch (*reinterpret_cast<int*>(_a[1])) {
            default: *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType(); break;
            case 1:
                *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType::fromType< QWaylandSurface* >(); break;
            }
            break;
        }
    }
}

const QMetaObject *QtWayland::WlShellIntegration::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QtWayland::WlShellIntegration::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN9QtWayland18WlShellIntegrationE_t>.strings))
        return static_cast<void*>(this);
    return QWaylandQuickShellIntegration::qt_metacast(_clname);
}

int QtWayland::WlShellIntegration::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
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
            qt_static_metacall(this, _c, _id, _a);
        _id -= 13;
    }
    return _id;
}
QT_WARNING_POP

//  from ../qtwayland/src/compositor/extensions/qwaylandwlshellintegration.cpp, line 257, as _ZN9QtWayland18WlShellIntegration11eventFilterEP7QObjectP6QEvent
namespace QtWayland {
inline bool WlShellIntegration::eventFilter(QObject *object, QEvent *event)
{
    if (event->type() == QEvent::MouseMove) {
        QMouseEvent *mouseEvent = static_cast<QMouseEvent *>(event);
        return filterMouseMoveEvent(mouseEvent);
    } else if (event->type() == QEvent::MouseButtonRelease) {
        QMouseEvent *mouseEvent = static_cast<QMouseEvent *>(event);
        return filterMouseReleaseEvent(mouseEvent);
    }
    return QWaylandQuickShellIntegration::eventFilter(object, event);
}
}  // namespace QtWayland

//  from ../qtwayland/src/compositor/extensions/qwaylandwlshellintegration.cpp, line 239, as _ZN9QtWayland18WlShellIntegration12handleRedrawEv
namespace QtWayland {
inline void WlShellIntegration::handleRedraw()
{
    if (currentState == nextState)
        return;

    m_item->moveItem()->setPosition(nextState == State::Windowed ? normalPosition : finalPosition);
    currentState = nextState;
}
}  // namespace QtWayland

//  from ../qtwayland/src/compositor/extensions/qwaylandwlshellintegration.cpp, line 160, as _ZN9QtWayland18WlShellIntegration14handleSetPopupEP12QWaylandSeatP15QWaylandSurfaceRK6QPoint
namespace QtWayland {
inline void WlShellIntegration::handleSetPopup(QWaylandSeat *seat, QWaylandSurface *parent, const QPoint &relativeToParent)
{
    Q_UNUSED(seat);

    // Find the parent item on the same output
    QWaylandQuickShellSurfaceItem *parentItem = nullptr;
    const auto views = parent->views();
    for (QWaylandView *view : views) {
        if (view->output() == m_item->view()->output()) {
            QWaylandQuickShellSurfaceItem *item = qobject_cast<QWaylandQuickShellSurfaceItem*>(view->renderObject());
            if (item) {
                parentItem = item;
                break;
            }
        }
    }

    if (parentItem) {
        // Clear all the transforms for this ShellSurfaceItem. They are not
        // applicable when the item becomes a child to a surface that has its
        // own transforms. Otherwise the transforms would be applied twice.
        QQmlListProperty<QQuickTransform> t = m_item->transform();
        t.clear(&t);
        m_item->setRotation(0);
        m_item->setScale(1.0);
        m_item->setPosition(m_item->mapFromSurface(relativeToParent));
        m_item->setParentItem(parentItem);
    }

    isPopup = true;
    auto shell = m_shellSurface->shell();
    QWaylandQuickShellEventFilter::startFilter(m_shellSurface->surface()->client(), [shell]() {
        shell->closeAllPopups();
    });

    QObject::connect(m_shellSurface->surface(), &QWaylandSurface::hasContentChanged,
                     this, &WlShellIntegration::handleSurfaceHasContentChanged);
}
}  // namespace QtWayland

//  from ../qtwayland/src/compositor/extensions/qwaylandwlshellintegration.cpp, line 40, as _ZN9QtWayland18WlShellIntegration15handleStartMoveEP12QWaylandSeat
namespace QtWayland {
inline void WlShellIntegration::handleStartMove(QWaylandSeat *seat)
{
    grabberState = GrabberState::Move;
    moveState.seat = seat;
    moveState.initialized = false;
}
}  // namespace QtWayland

//  from ../qtwayland/src/compositor/extensions/qwaylandwlshellintegration.cpp, line 47, as _ZN9QtWayland18WlShellIntegration17handleStartResizeEP12QWaylandSeatN22QWaylandWlShellSurface10ResizeEdgeE
namespace QtWayland {
inline void WlShellIntegration::handleStartResize(QWaylandSeat *seat, QWaylandWlShellSurface::ResizeEdge edges)
{
    grabberState = GrabberState::Resize;
    resizeState.seat = seat;
    resizeState.resizeEdges = edges;
    resizeState.initialSize = m_shellSurface->surface()->destinationSize();
    resizeState.initialized = false;
}
}  // namespace QtWayland

//  from ../qtwayland/src/compositor/extensions/qwaylandwlshellintegration.cpp, line 84, as _ZN9QtWayland18WlShellIntegration18handleSetMaximizedEP14QWaylandOutput
namespace QtWayland {
inline void WlShellIntegration::handleSetMaximized(QWaylandOutput *output)
{
    if (!m_item->view()->isPrimary())
        return;

    if (currentState == State::Maximized)
        return;

    QWaylandOutput *designatedOutput = output ? output : m_item->view()->output();
    if (!designatedOutput)
        return;

    if (currentState == State::Windowed)
        normalPosition = m_item->moveItem()->position();

    nextState = State::Maximized;
    finalPosition = designatedOutput->position() + designatedOutput->availableGeometry().topLeft();

    // Any prior output-resize handlers are irrelevant at this point
    disconnect(nonwindowedState.sizeChangedConnection);
    nonwindowedState.output = designatedOutput;
    nonwindowedState.sizeChangedConnection = connect(designatedOutput, &QWaylandOutput::availableGeometryChanged, this, &WlShellIntegration::handleMaximizedSizeChanged);
    handleMaximizedSizeChanged();
}
}  // namespace QtWayland

//  from ../qtwayland/src/compositor/extensions/qwaylandwlshellintegration.cpp, line 74, as _ZN9QtWayland18WlShellIntegration18handleSetTransientEP15QWaylandSurfaceRK6QPointb
namespace QtWayland {
inline void WlShellIntegration::handleSetTransient(QWaylandSurface *parentSurface, const QPoint &relativeToParent, bool inactive)
{
    Q_UNUSED(parentSurface);
    Q_UNUSED(relativeToParent);

    // Take focus if the policy allows and it's not inactive
    if (m_shellSurface->shell()->focusPolicy() == QWaylandShell::AutomaticFocus && !inactive)
        m_item->takeFocus();
}
}  // namespace QtWayland

//  from ../qtwayland/src/compositor/extensions/qwaylandwlshellintegration.cpp, line 121, as _ZN9QtWayland18WlShellIntegration19handleSetFullScreenEN22QWaylandWlShellSurface16FullScreenMethodEjP14QWaylandOutput
namespace QtWayland {
inline void WlShellIntegration::handleSetFullScreen(QWaylandWlShellSurface::FullScreenMethod method, uint framerate, QWaylandOutput *output)
{
    Q_UNUSED(method);
    Q_UNUSED(framerate);

    if (!m_item->view()->isPrimary())
        return;

    if (currentState == State::FullScreen)
        return;

    QWaylandOutput *designatedOutput = output ? output : m_item->view()->output();
    if (!designatedOutput)
        return;

    if (currentState == State::Windowed)
        normalPosition = m_item->moveItem()->position();

    nextState = State::FullScreen;
    finalPosition = designatedOutput->position();

    // Any prior output-resize handlers are irrelevant at this point
    disconnect(nonwindowedState.sizeChangedConnection);
    nonwindowedState.output = designatedOutput;
    nonwindowedState.sizeChangedConnection = connect(designatedOutput, &QWaylandOutput::geometryChanged, this, &WlShellIntegration::handleFullScreenSizeChanged);
    handleFullScreenSizeChanged();
}
}  // namespace QtWayland

//  from ../qtwayland/src/compositor/extensions/qwaylandwlshellintegration.cpp, line 248, as _ZN9QtWayland18WlShellIntegration24adjustOffsetForNextFrameERK7QPointF
namespace QtWayland {
inline void WlShellIntegration::adjustOffsetForNextFrame(const QPointF &offset)
{
    if (!m_item->view()->isPrimary())
        return;

    QQuickItem *moveItem = m_item->moveItem();
    moveItem->setPosition(moveItem->position() + m_item->mapFromSurface(offset));
}
}  // namespace QtWayland

//  from ../qtwayland/src/compositor/extensions/qwaylandwlshellintegration.cpp, line 56, as _ZN9QtWayland18WlShellIntegration24handleSetDefaultTopLevelEv
namespace QtWayland {
inline void WlShellIntegration::handleSetDefaultTopLevel()
{
    // Take focus if the policy allows
    if (m_shellSurface->shell()->focusPolicy() == QWaylandShell::AutomaticFocus)
        m_item->takeFocus();

    // In order to restore the window state, the client calls setDefaultToplevel()
    // so we need to unset the flags here but we save the previous state and move
    // to the initial position when redrawing
    nextState = State::Windowed;

    // Any handlers for making maximized or fullscreen state track the size of
    // the designated output, are unneeded now that we're going to windowed
    // state.
    nonwindowedState.output = nullptr;
    disconnect(nonwindowedState.sizeChangedConnection);
}
}  // namespace QtWayland

//  from ../qtwayland/src/compositor/extensions/qwaylandwlshellintegration.cpp, line 109, as _ZN9QtWayland18WlShellIntegration26handleMaximizedSizeChangedEv
namespace QtWayland {
inline void WlShellIntegration::handleMaximizedSizeChanged()
{
    if (!m_shellSurface)
        return;

    if (nextState == State::Maximized) {
        QWaylandOutput *designatedOutput = nonwindowedState.output;
        auto scaleFactor = designatedOutput->scaleFactor();
        m_shellSurface->sendConfigure(designatedOutput->availableGeometry().size() / scaleFactor, QWaylandWlShellSurface::NoneEdge);
    }
}
}  // namespace QtWayland

//  from ../qtwayland/src/compositor/extensions/qwaylandwlshellintegration.cpp, line 149, as _ZN9QtWayland18WlShellIntegration27handleFullScreenSizeChangedEv
namespace QtWayland {
inline void WlShellIntegration::handleFullScreenSizeChanged()
{
    if (!m_shellSurface)
        return;

    if (nextState == State::FullScreen) {
        QWaylandOutput *designatedOutput = nonwindowedState.output;
        m_shellSurface->sendConfigure(designatedOutput->geometry().size(), QWaylandWlShellSurface::NoneEdge);
    }
}
}  // namespace QtWayland

//  from ../qtwayland/src/compositor/extensions/qwaylandwlshellintegration.cpp, line 219, as _ZN9QtWayland18WlShellIntegration27handleShellSurfaceDestroyedEv
namespace QtWayland {
inline void WlShellIntegration::handleShellSurfaceDestroyed()
{
    if (isPopup)
        handlePopupRemoved();

    // Disarm any handlers that might fire and attempt to use the now-stale pointer
    nonwindowedState.output = nullptr;
    disconnect(nonwindowedState.sizeChangedConnection);

    m_shellSurface = nullptr;
}
}  // namespace QtWayland

//  from ../qtwayland/src/compositor/extensions/qwaylandwlshellintegration.cpp, line 231, as _ZN9QtWayland18WlShellIntegration30handleSurfaceHasContentChangedEv
namespace QtWayland {
inline void WlShellIntegration::handleSurfaceHasContentChanged()
{
    if (m_shellSurface && m_shellSurface->surface()->destinationSize().isEmpty()
            && m_shellSurface->windowType() == Qt::WindowType::Popup) {
        handlePopupClosed();
    }
}
}  // namespace QtWayland

//  from ../qtwayland/src/compositor/extensions/qwaylandwlshellintegration.cpp, line 35, as _ZN9QtWayland18WlShellIntegrationD0Ev
namespace QtWayland {
inline WlShellIntegration::~WlShellIntegration()
{
    m_item->setSurface(nullptr);
}
}  // namespace QtWayland

//  from ../qtwayland/src/compositor/extensions/qwaylandwlshellintegration.cpp, line 16, as _ZN9QtWayland18WlShellIntegrationC1EP29QWaylandQuickShellSurfaceItem
namespace QtWayland {
inline WlShellIntegration::WlShellIntegration(QWaylandQuickShellSurfaceItem *item)
    : QWaylandQuickShellIntegration(item)
    , m_item(item)
    , m_shellSurface(qobject_cast<QWaylandWlShellSurface *>(item->shellSurface()))
{
    m_item->setSurface(m_shellSurface->surface());
    connect(m_shellSurface.data(), &QWaylandWlShellSurface::startMove, this, &WlShellIntegration::handleStartMove);
    connect(m_shellSurface.data(), &QWaylandWlShellSurface::startResize, this, &WlShellIntegration::handleStartResize);
    connect(m_shellSurface->surface(), &QWaylandSurface::redraw, this, &WlShellIntegration::handleRedraw);
    connect(m_shellSurface->surface(), &QWaylandSurface::offsetForNextFrame, this, &WlShellIntegration::adjustOffsetForNextFrame);
    connect(m_shellSurface->surface(), &QWaylandSurface::hasContentChanged, this, &WlShellIntegration::handleSurfaceHasContentChanged);
    connect(m_shellSurface.data(), &QWaylandWlShellSurface::setDefaultToplevel, this, &WlShellIntegration::handleSetDefaultTopLevel);
    connect(m_shellSurface.data(), &QWaylandWlShellSurface::setTransient, this, &WlShellIntegration::handleSetTransient);
    connect(m_shellSurface.data(), &QWaylandWlShellSurface::setMaximized, this, &WlShellIntegration::handleSetMaximized);
    connect(m_shellSurface.data(), &QWaylandWlShellSurface::setFullScreen, this, &WlShellIntegration::handleSetFullScreen);
    connect(m_shellSurface.data(), &QWaylandWlShellSurface::setPopup, this, &WlShellIntegration::handleSetPopup);
    connect(m_shellSurface.data(), &QWaylandWlShellSurface::destroyed, this, &WlShellIntegration::handleShellSurfaceDestroyed);
}
}  // namespace QtWayland

//  from ../qtwayland/src/compositor/extensions/qwaylandwlshellintegration.cpp, line 199, as _ZN9QtWayland18WlShellIntegration17handlePopupClosedEv
namespace QtWayland {
inline void WlShellIntegration::handlePopupClosed()
{
    handlePopupRemoved();
    if (m_shellSurface)
        QObject::disconnect(m_shellSurface->surface(), &QWaylandSurface::hasContentChanged,
                            this, &WlShellIntegration::handleSurfaceHasContentChanged);
}
}  // namespace QtWayland

//  from ../qtwayland/src/compositor/extensions/qwaylandwlshellintegration.cpp, line 207, as _ZN9QtWayland18WlShellIntegration18handlePopupRemovedEv
namespace QtWayland {
inline void WlShellIntegration::handlePopupRemoved()
{
    if (!m_shellSurface || m_shellSurface->shell()->mappedPopups().isEmpty())
        QWaylandQuickShellEventFilter::cancelFilter();
    isPopup = false;
}
}  // namespace QtWayland

//  from ../qtwayland/src/compositor/extensions/qwaylandwlshellintegration.cpp, line 214, as _ZNK9QtWayland18WlShellIntegration16devicePixelRatioEv
namespace QtWayland {
inline qreal WlShellIntegration::devicePixelRatio() const
{
    return m_item->window() ? m_item->window()->devicePixelRatio() : 1;
}
}  // namespace QtWayland

//  from ../qtwayland/src/compositor/extensions/qwaylandwlshellintegration.cpp, line 269, as _ZN9QtWayland18WlShellIntegration20filterMouseMoveEventEP11QMouseEvent
namespace QtWayland {
inline bool WlShellIntegration::filterMouseMoveEvent(QMouseEvent *event)
{
    if (grabberState == GrabberState::Resize) {
        Q_ASSERT(resizeState.seat == m_item->compositor()->seatFor(event));
        if (!resizeState.initialized) {
            resizeState.initialMousePos = event->scenePosition();
            resizeState.initialized = true;
            return true;
        }
        float scaleFactor = m_item->view()->output()->scaleFactor();
        QPointF delta = (event->scenePosition() - resizeState.initialMousePos) / scaleFactor * devicePixelRatio();
        QSize newSize = m_shellSurface->sizeForResize(resizeState.initialSize, delta, resizeState.resizeEdges);
        m_shellSurface->sendConfigure(newSize, resizeState.resizeEdges);
    } else if (grabberState == GrabberState::Move) {
        Q_ASSERT(moveState.seat == m_item->compositor()->seatFor(event));
        QQuickItem *moveItem = m_item->moveItem();
        if (!moveState.initialized) {
            moveState.initialOffset = moveItem->mapFromItem(nullptr, event->scenePosition());
            moveState.initialized = true;
            return true;
        }
        if (!moveItem->parentItem())
            return true;
        QPointF parentPos = moveItem->parentItem()->mapFromItem(nullptr, event->scenePosition());
        moveItem->setPosition(parentPos - moveState.initialOffset);
    }
    return false;
}
}  // namespace QtWayland

//  from ../qtwayland/src/compositor/extensions/qwaylandwlshellintegration.cpp, line 298, as _ZN9QtWayland18WlShellIntegration23filterMouseReleaseEventEP11QMouseEvent
namespace QtWayland {
inline bool WlShellIntegration::filterMouseReleaseEvent(QMouseEvent *event)
{
    Q_UNUSED(event);
    if (grabberState != GrabberState::Default) {
        grabberState = GrabberState::Default;
        return true;
    }
    return false;
}
}  // namespace QtWayland
//  -----------------------------------------------------------------------

//  Only a class built on QtWayland::WlShellIntegration may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQtWayland_WlShellIntegration : QtWayland::WlShellIntegration {
  using QtWayland::WlShellIntegration::eventFilter;
};

//  A QtWayland::WlShellIntegration that Python can take functions over in. Every QtWayland::WlShellIntegration
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtWayland_WlShellIntegrationCall0)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtWayland_WlShellIntegrationCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtWayland_WlShellIntegrationCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtWayland_WlShellIntegrationCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtWayland_WlShellIntegrationCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtWayland_WlShellIntegrationCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtWayland_WlShellIntegrationCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQtWayland_WlShellIntegration : public QtWayland::WlShellIntegration {
public:
  using QtWayland::WlShellIntegration::WlShellIntegration;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QtWayland::WlShellIntegration::eventFilter(QObject *object,
  //      QEvent *event)
  bool eventFilter(QObject *object, QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQtWayland_WlShellIntegrationCall0 call = reinterpret_cast<CuteQtWayland_WlShellIntegrationCall0>(taken[0]);
      bool given = call(this, object, event, &handled);
      if (handled) return given;
    }
    return QtWayland::WlShellIntegration::eventFilter(object, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQtWayland_WlShellIntegrationCall1 call = reinterpret_cast<CuteQtWayland_WlShellIntegrationCall1>(taken[1]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQtWayland_WlShellIntegrationCall2 call = reinterpret_cast<CuteQtWayland_WlShellIntegrationCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQtWayland_WlShellIntegrationCall3 call = reinterpret_cast<CuteQtWayland_WlShellIntegrationCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQtWayland_WlShellIntegrationCall4 call = reinterpret_cast<CuteQtWayland_WlShellIntegrationCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQtWayland_WlShellIntegrationCall5 call = reinterpret_cast<CuteQtWayland_WlShellIntegrationCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQtWayland_WlShellIntegrationCall6 call = reinterpret_cast<CuteQtWayland_WlShellIntegrationCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QtWayland::WlShellIntegration::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9QtWayland18WlShellIntegration10metaObjectEv(
    const QtWayland::WlShellIntegration *self) {
  return self->metaObject();
}

//  void *QtWayland::WlShellIntegration::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN9QtWayland18WlShellIntegration11qt_metacastEPKc(
    QtWayland::WlShellIntegration *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QtWayland::WlShellIntegration::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN9QtWayland18WlShellIntegration11qt_metacallEN11QMetaObject4CallEiPPv(
    QtWayland::WlShellIntegration *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QtWayland::WlShellIntegration::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN9QtWayland18WlShellIntegration2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QtWayland::WlShellIntegration::tr(s, c, n));
}

//  QtWayland::WlShellIntegration::WlShellIntegration(QWaylandQuickShellSurfa
//      ceItem *item)
extern "C" Q_DECL_EXPORT
QtWayland::WlShellIntegration *ritual_ZN9QtWayland18WlShellIntegrationC1EP29QWaylandQuickShellSurfaceItem(
    QWaylandQuickShellSurfaceItem *item) {
  return new CuteQtWayland_WlShellIntegration(item);
}

//  QtWayland::WlShellIntegration::~WlShellIntegration()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtWayland18WlShellIntegrationD1Ev(
    QtWayland::WlShellIntegration *self) {
  delete self;
}

//  bool QtWayland::WlShellIntegration::eventFilter(QObject *object, QEvent
//      *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QtWayland18WlShellIntegration11eventFilterEP7QObjectP6QEvent(
    QtWayland::WlShellIntegration *self,
    QObject *object,
    QEvent *event) {
  return self->eventFilter(object, event);
}

//  void QtWayland::WlShellIntegration::handleStartMove(QWaylandSeat *seat)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtWayland18WlShellIntegration15handleStartMoveEP12QWaylandSeat(
    QtWayland::WlShellIntegration *self,
    QWaylandSeat *seat) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QtWayland::WlShellIntegration")) {
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

//  void QtWayland::WlShellIntegration::handleStartResize(QWaylandSeat *seat,
//      QWaylandWlShellSurface::ResizeEdge edges)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtWayland18WlShellIntegration17handleStartResizeEP12QWaylandSeatN22QWaylandWlShellSurface10ResizeEdgeE(
    QtWayland::WlShellIntegration *self,
    QWaylandSeat *seat,
    QWaylandWlShellSurface::ResizeEdge edges) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QtWayland::WlShellIntegration")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "handleStartResize(QWaylandSeat *,QWaylandWlShellSurface::ResizeEdge)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "handleStartResize(QWaylandSeat *,QWaylandWlShellSurface::ResizeEdge)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&seat)),
      const_cast<void *>(static_cast<const void *>(&edges)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QtWayland::WlShellIntegration::handleSetDefaultTopLevel()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtWayland18WlShellIntegration24handleSetDefaultTopLevelEv(
    QtWayland::WlShellIntegration *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QtWayland::WlShellIntegration")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "handleSetDefaultTopLevel()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "handleSetDefaultTopLevel()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QtWayland::WlShellIntegration::handleSetTransient(QWaylandSurface
//      *parentSurface, const QPoint &relativeToParent, bool inactive)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtWayland18WlShellIntegration18handleSetTransientEP15QWaylandSurfaceRK6QPointb(
    QtWayland::WlShellIntegration *self,
    QWaylandSurface *parentSurface,
    const QPoint *relativeToParent,
    bool inactive) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QtWayland::WlShellIntegration")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "handleSetTransient(QWaylandSurface *,const QPoint &,bool)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "handleSetTransient(QWaylandSurface *,const QPoint &,bool)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&parentSurface)),
      const_cast<void *>(static_cast<const void *>(relativeToParent)),
      const_cast<void *>(static_cast<const void *>(&inactive)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QtWayland::WlShellIntegration::handleSetMaximized(QWaylandOutput
//      *output)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtWayland18WlShellIntegration18handleSetMaximizedEP14QWaylandOutput(
    QtWayland::WlShellIntegration *self,
    QWaylandOutput *output) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QtWayland::WlShellIntegration")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "handleSetMaximized(QWaylandOutput *)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "handleSetMaximized(QWaylandOutput *)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&output)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QtWayland::WlShellIntegration::handleSetFullScreen(QWaylandWlShellSu
//      rface::FullScreenMethod method, uint framerate, QWaylandOutput
//      *output)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtWayland18WlShellIntegration19handleSetFullScreenEN22QWaylandWlShellSurface16FullScreenMethodEjP14QWaylandOutput(
    QtWayland::WlShellIntegration *self,
    QWaylandWlShellSurface::FullScreenMethod method,
    uint framerate,
    QWaylandOutput *output) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QtWayland::WlShellIntegration")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "handleSetFullScreen(QWaylandWlShellSurface::FullScreenMethod,uint,QWaylandOutput *)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "handleSetFullScreen(QWaylandWlShellSurface::FullScreenMethod,uint,QWaylandOutput *)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&method)),
      const_cast<void *>(static_cast<const void *>(&framerate)),
      const_cast<void *>(static_cast<const void *>(&output)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QtWayland::WlShellIntegration::handleSetPopup(QWaylandSeat *seat,
//      QWaylandSurface *parent, const QPoint &relativeToParent)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtWayland18WlShellIntegration14handleSetPopupEP12QWaylandSeatP15QWaylandSurfaceRK6QPoint(
    QtWayland::WlShellIntegration *self,
    QWaylandSeat *seat,
    QWaylandSurface *parent,
    const QPoint *relativeToParent) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QtWayland::WlShellIntegration")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "handleSetPopup(QWaylandSeat *,QWaylandSurface *,const QPoint &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "handleSetPopup(QWaylandSeat *,QWaylandSurface *,const QPoint &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&seat)),
      const_cast<void *>(static_cast<const void *>(&parent)),
      const_cast<void *>(static_cast<const void *>(relativeToParent)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QtWayland::WlShellIntegration::handleShellSurfaceDestroyed()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtWayland18WlShellIntegration27handleShellSurfaceDestroyedEv(
    QtWayland::WlShellIntegration *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QtWayland::WlShellIntegration")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "handleShellSurfaceDestroyed()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "handleShellSurfaceDestroyed()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QtWayland::WlShellIntegration::handleSurfaceHasContentChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtWayland18WlShellIntegration30handleSurfaceHasContentChangedEv(
    QtWayland::WlShellIntegration *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QtWayland::WlShellIntegration")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "handleSurfaceHasContentChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "handleSurfaceHasContentChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QtWayland::WlShellIntegration::handleRedraw()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtWayland18WlShellIntegration12handleRedrawEv(
    QtWayland::WlShellIntegration *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QtWayland::WlShellIntegration")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "handleRedraw()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "handleRedraw()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QtWayland::WlShellIntegration::adjustOffsetForNextFrame(const
//      QPointF &offset)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtWayland18WlShellIntegration24adjustOffsetForNextFrameERK7QPointF(
    QtWayland::WlShellIntegration *self,
    const QPointF *offset) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QtWayland::WlShellIntegration")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "adjustOffsetForNextFrame(const QPointF &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "adjustOffsetForNextFrame(const QPointF &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(offset)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QtWayland::WlShellIntegration::handleFullScreenSizeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtWayland18WlShellIntegration27handleFullScreenSizeChangedEv(
    QtWayland::WlShellIntegration *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QtWayland::WlShellIntegration")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "handleFullScreenSizeChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "handleFullScreenSizeChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QtWayland::WlShellIntegration::handleMaximizedSizeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtWayland18WlShellIntegration26handleMaximizedSizeChangedEv(
    QtWayland::WlShellIntegration *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QtWayland::WlShellIntegration")) {
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

//  void QtWayland::WlShellIntegration::handlePopupClosed()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtWayland18WlShellIntegration17handlePopupClosedEv(
    QtWayland::WlShellIntegration *self) {
  self->handlePopupClosed();
}

//  void QtWayland::WlShellIntegration::handlePopupRemoved()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtWayland18WlShellIntegration18handlePopupRemovedEv(
    QtWayland::WlShellIntegration *self) {
  self->handlePopupRemoved();
}

//  qreal QtWayland::WlShellIntegration::devicePixelRatio() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK9QtWayland18WlShellIntegration16devicePixelRatioEv(
    const QtWayland::WlShellIntegration *self) {
  return self->devicePixelRatio();
}

//  bool QtWayland::WlShellIntegration::filterMouseMoveEvent(QMouseEvent
//      *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QtWayland18WlShellIntegration20filterMouseMoveEventEP11QMouseEvent(
    QtWayland::WlShellIntegration *self,
    QMouseEvent *event) {
  return self->filterMouseMoveEvent(event);
}

//  bool QtWayland::WlShellIntegration::filterMouseReleaseEvent(QMouseEvent
//      *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QtWayland18WlShellIntegration23filterMouseReleaseEventEP11QMouseEvent(
    QtWayland::WlShellIntegration *self,
    QMouseEvent *event) {
  return self->filterMouseReleaseEvent(event);
}

//  a Python function taken by a CuteQtWayland_WlShellIntegration, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QtWayland_WlShellIntegration(
    QtWayland::WlShellIntegration *self,
    const char *key,
    void *call) {
  return static_cast<CuteQtWayland_WlShellIntegration *>(self)->take(key, call);
}

//  bool QtWayland::WlShellIntegration::eventFilter(QObject *object, QEvent
//      *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN9QtWayland18WlShellIntegration11eventFilterEP7QObjectP6QEvent(
    QtWayland::WlShellIntegration *self,
    QObject *object,
    QEvent *event) {
  return static_cast<OwnQtWayland_WlShellIntegration *>(self)->OwnQtWayland_WlShellIntegration::eventFilter(
      object,
      event);
}

#endif  // QT_CONFIG(wayland_compositor_quick)
