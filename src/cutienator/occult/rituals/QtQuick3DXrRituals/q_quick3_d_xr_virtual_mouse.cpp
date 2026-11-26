//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3DXr/6.12.0/QtQuick3DXr/private/qquick3dxrvirtualmouse_p.h, Qt
//  6.12.0.
//  Edited by hand on 2026-11-26: moc's output for 'QQuick3DXrVirtualMouse'
//  is pasted in, cut from what the moc of Qt 6.12.0 writes for its header:
//  Qt's library keeps it to itself; added are 2 rituals that lean on what
//  moc writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
#include <QtQuick3DXr/6.12.0/QtQuick3DXr/private/qtquick3dxrglobal_p.h>
#include <QtQuick3DXr/QtQuick3DXr>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DXr/6.12.0/QtQuick3DXr/private/qquick3dxrvirtualmouse_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtQuick3DXr/private/qquick3dxrvirtualmouse_p.h>
#include <QtQuick3DXr/private/qquick3dxrview_p.h>
#include <QtQuick3D/private/qquick3dnode_p.h>
#include <QtGui/QMouseEvent>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from QtQuick3DXr__QQuick3DXrVirtualMouse.cpp, line 1, as moc:QQuick3DXrVirtualMouse
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN22QQuick3DXrVirtualMouseE_t {};
} // unnamed namespace

template <> constexpr inline auto QQuick3DXrVirtualMouse::qt_create_metaobjectdata<qt_meta_tag_ZN22QQuick3DXrVirtualMouseE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QQuick3DXrVirtualMouse",
        "QML.Element",
        "XrVirtualMouse",
        "QML.AddedInVersion",
        "1544",
        "rightMouseButtonChanged",
        "",
        "rightMouseButton",
        "leftMouseButtonChanged",
        "leftMouseButton",
        "middleMouseButtonChanged",
        "middleMouseButton",
        "scrollWheelXChanged",
        "scrollWheelX",
        "scrollWheelYChanged",
        "scrollWheelY",
        "scrollTimerIntervalChanged",
        "scrollTimerInterval",
        "scrollPixelDeltaChanged",
        "scrollPixelDelta",
        "sourceChanged",
        "QQuick3DNode*",
        "source",
        "viewChanged",
        "QQuick3DXrView*",
        "view",
        "enabledChanged",
        "enabled",
        "setRightMouseButton",
        "setLeftMouseButton",
        "setMiddleMouseButton",
        "setScrollWheelX",
        "setScrollWheelY",
        "setScrollTimerInterval",
        "setScrollPixelDelta",
        "setSource",
        "setView",
        "setEnabled",
        "moveEvent",
        "generateWheelEvent"
    };

    QtMocHelpers::UintData qt_methods {
        // Signal 'rightMouseButtonChanged'
        QtMocHelpers::SignalData<void(bool)>(5, 6, QMC::AccessPublic, QMetaType::Void, {{
            { QMetaType::Bool, 7 },
        }}),
        // Signal 'leftMouseButtonChanged'
        QtMocHelpers::SignalData<void(bool)>(8, 6, QMC::AccessPublic, QMetaType::Void, {{
            { QMetaType::Bool, 9 },
        }}),
        // Signal 'middleMouseButtonChanged'
        QtMocHelpers::SignalData<void(bool)>(10, 6, QMC::AccessPublic, QMetaType::Void, {{
            { QMetaType::Bool, 11 },
        }}),
        // Signal 'scrollWheelXChanged'
        QtMocHelpers::SignalData<void(float)>(12, 6, QMC::AccessPublic, QMetaType::Void, {{
            { QMetaType::Float, 13 },
        }}),
        // Signal 'scrollWheelYChanged'
        QtMocHelpers::SignalData<void(float)>(14, 6, QMC::AccessPublic, QMetaType::Void, {{
            { QMetaType::Float, 15 },
        }}),
        // Signal 'scrollTimerIntervalChanged'
        QtMocHelpers::SignalData<void(int)>(16, 6, QMC::AccessPublic, QMetaType::Void, {{
            { QMetaType::Int, 17 },
        }}),
        // Signal 'scrollPixelDeltaChanged'
        QtMocHelpers::SignalData<void(int)>(18, 6, QMC::AccessPublic, QMetaType::Void, {{
            { QMetaType::Int, 19 },
        }}),
        // Signal 'sourceChanged'
        QtMocHelpers::SignalData<void(QQuick3DNode *)>(20, 6, QMC::AccessPublic, QMetaType::Void, {{
            { 0x80000000 | 21, 22 },
        }}),
        // Signal 'viewChanged'
        QtMocHelpers::SignalData<void(QQuick3DXrView *)>(23, 6, QMC::AccessPublic, QMetaType::Void, {{
            { 0x80000000 | 24, 25 },
        }}),
        // Signal 'enabledChanged'
        QtMocHelpers::SignalData<void(bool)>(26, 6, QMC::AccessPublic, QMetaType::Void, {{
            { QMetaType::Bool, 27 },
        }}),
        // Slot 'setRightMouseButton'
        QtMocHelpers::SlotData<void(bool)>(28, 6, QMC::AccessPublic, QMetaType::Void, {{
            { QMetaType::Bool, 7 },
        }}),
        // Slot 'setLeftMouseButton'
        QtMocHelpers::SlotData<void(bool)>(29, 6, QMC::AccessPublic, QMetaType::Void, {{
            { QMetaType::Bool, 9 },
        }}),
        // Slot 'setMiddleMouseButton'
        QtMocHelpers::SlotData<void(bool)>(30, 6, QMC::AccessPublic, QMetaType::Void, {{
            { QMetaType::Bool, 11 },
        }}),
        // Slot 'setScrollWheelX'
        QtMocHelpers::SlotData<void(float)>(31, 6, QMC::AccessPublic, QMetaType::Void, {{
            { QMetaType::Float, 13 },
        }}),
        // Slot 'setScrollWheelY'
        QtMocHelpers::SlotData<void(float)>(32, 6, QMC::AccessPublic, QMetaType::Void, {{
            { QMetaType::Float, 15 },
        }}),
        // Slot 'setScrollTimerInterval'
        QtMocHelpers::SlotData<void(int)>(33, 6, QMC::AccessPublic, QMetaType::Void, {{
            { QMetaType::Int, 17 },
        }}),
        // Slot 'setScrollPixelDelta'
        QtMocHelpers::SlotData<void(int)>(34, 6, QMC::AccessPublic, QMetaType::Void, {{
            { QMetaType::Int, 19 },
        }}),
        // Slot 'setSource'
        QtMocHelpers::SlotData<void(QQuick3DNode *)>(35, 6, QMC::AccessPublic, QMetaType::Void, {{
            { 0x80000000 | 21, 22 },
        }}),
        // Slot 'setView'
        QtMocHelpers::SlotData<void(QQuick3DXrView *)>(36, 6, QMC::AccessPublic, QMetaType::Void, {{
            { 0x80000000 | 24, 25 },
        }}),
        // Slot 'setEnabled'
        QtMocHelpers::SlotData<void(bool)>(37, 6, QMC::AccessPublic, QMetaType::Void, {{
            { QMetaType::Bool, 27 },
        }}),
        // Slot 'moveEvent'
        QtMocHelpers::SlotData<void()>(38, 6, QMC::AccessPrivate, QMetaType::Void),
        // Slot 'generateWheelEvent'
        QtMocHelpers::SlotData<void()>(39, 6, QMC::AccessPrivate, QMetaType::Void),
    };
    QtMocHelpers::UintData qt_properties {
        // property 'rightMouseButton'
        QtMocHelpers::PropertyData<bool>(7, QMetaType::Bool, QMC::DefaultPropertyFlags | QMC::Writable | QMC::StdCppSet, 0),
        // property 'leftMouseButton'
        QtMocHelpers::PropertyData<bool>(9, QMetaType::Bool, QMC::DefaultPropertyFlags | QMC::Writable | QMC::StdCppSet, 1),
        // property 'middleMouseButton'
        QtMocHelpers::PropertyData<bool>(11, QMetaType::Bool, QMC::DefaultPropertyFlags | QMC::Writable | QMC::StdCppSet, 2),
        // property 'scrollWheelX'
        QtMocHelpers::PropertyData<float>(13, QMetaType::Float, QMC::DefaultPropertyFlags | QMC::Writable | QMC::StdCppSet, 3),
        // property 'scrollWheelY'
        QtMocHelpers::PropertyData<float>(15, QMetaType::Float, QMC::DefaultPropertyFlags | QMC::Writable | QMC::StdCppSet, 4),
        // property 'scrollTimerInterval'
        QtMocHelpers::PropertyData<int>(17, QMetaType::Int, QMC::DefaultPropertyFlags | QMC::Writable | QMC::StdCppSet, 5),
        // property 'scrollPixelDelta'
        QtMocHelpers::PropertyData<int>(19, QMetaType::Int, QMC::DefaultPropertyFlags | QMC::Writable | QMC::StdCppSet, 6),
        // property 'source'
        QtMocHelpers::PropertyData<QQuick3DNode*>(22, 0x80000000 | 21, QMC::DefaultPropertyFlags | QMC::Writable | QMC::EnumOrFlag | QMC::StdCppSet, 7),
        // property 'view'
        QtMocHelpers::PropertyData<QQuick3DXrView*>(25, 0x80000000 | 24, QMC::DefaultPropertyFlags | QMC::Writable | QMC::EnumOrFlag | QMC::StdCppSet, 8),
        // property 'enabled'
        QtMocHelpers::PropertyData<bool>(27, QMetaType::Bool, QMC::DefaultPropertyFlags | QMC::Writable | QMC::StdCppSet, 9),
    };
    QtMocHelpers::UintData qt_enums {
    };
    QtMocHelpers::UintData qt_constructors {};
    QtMocHelpers::ClassInfos qt_classinfo({
            {    1,    2 },
            {    3,    4 },
    });
    return QtMocHelpers::metaObjectData<QQuick3DXrVirtualMouse, void>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums, qt_constructors, qt_classinfo);
}
Q_CONSTINIT const QMetaObject QQuick3DXrVirtualMouse::staticMetaObject = { {
    QMetaObject::SuperData::link<QObject::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN22QQuick3DXrVirtualMouseE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN22QQuick3DXrVirtualMouseE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN22QQuick3DXrVirtualMouseE_t>.metaTypes,
    nullptr
} };

void QQuick3DXrVirtualMouse::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QQuick3DXrVirtualMouse *>(_o);
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: _t->rightMouseButtonChanged((*reinterpret_cast<std::add_pointer_t<bool>>(_a[1]))); break;
        case 1: _t->leftMouseButtonChanged((*reinterpret_cast<std::add_pointer_t<bool>>(_a[1]))); break;
        case 2: _t->middleMouseButtonChanged((*reinterpret_cast<std::add_pointer_t<bool>>(_a[1]))); break;
        case 3: _t->scrollWheelXChanged((*reinterpret_cast<std::add_pointer_t<float>>(_a[1]))); break;
        case 4: _t->scrollWheelYChanged((*reinterpret_cast<std::add_pointer_t<float>>(_a[1]))); break;
        case 5: _t->scrollTimerIntervalChanged((*reinterpret_cast<std::add_pointer_t<int>>(_a[1]))); break;
        case 6: _t->scrollPixelDeltaChanged((*reinterpret_cast<std::add_pointer_t<int>>(_a[1]))); break;
        case 7: _t->sourceChanged((*reinterpret_cast<std::add_pointer_t<QQuick3DNode*>>(_a[1]))); break;
        case 8: _t->viewChanged((*reinterpret_cast<std::add_pointer_t<QQuick3DXrView*>>(_a[1]))); break;
        case 9: _t->enabledChanged((*reinterpret_cast<std::add_pointer_t<bool>>(_a[1]))); break;
        case 10: _t->setRightMouseButton((*reinterpret_cast<std::add_pointer_t<bool>>(_a[1]))); break;
        case 11: _t->setLeftMouseButton((*reinterpret_cast<std::add_pointer_t<bool>>(_a[1]))); break;
        case 12: _t->setMiddleMouseButton((*reinterpret_cast<std::add_pointer_t<bool>>(_a[1]))); break;
        case 13: _t->setScrollWheelX((*reinterpret_cast<std::add_pointer_t<float>>(_a[1]))); break;
        case 14: _t->setScrollWheelY((*reinterpret_cast<std::add_pointer_t<float>>(_a[1]))); break;
        case 15: _t->setScrollTimerInterval((*reinterpret_cast<std::add_pointer_t<int>>(_a[1]))); break;
        case 16: _t->setScrollPixelDelta((*reinterpret_cast<std::add_pointer_t<int>>(_a[1]))); break;
        case 17: _t->setSource((*reinterpret_cast<std::add_pointer_t<QQuick3DNode*>>(_a[1]))); break;
        case 18: _t->setView((*reinterpret_cast<std::add_pointer_t<QQuick3DXrView*>>(_a[1]))); break;
        case 19: _t->setEnabled((*reinterpret_cast<std::add_pointer_t<bool>>(_a[1]))); break;
        case 20: _t->moveEvent(); break;
        case 21: _t->generateWheelEvent(); break;
        default: ;
        }
    }
    if (_c == QMetaObject::IndexOfMethod) {
        if (QtMocHelpers::indexOfMethod<void (QQuick3DXrVirtualMouse::*)(bool )>(_a, &QQuick3DXrVirtualMouse::rightMouseButtonChanged, 0))
            return;
        if (QtMocHelpers::indexOfMethod<void (QQuick3DXrVirtualMouse::*)(bool )>(_a, &QQuick3DXrVirtualMouse::leftMouseButtonChanged, 1))
            return;
        if (QtMocHelpers::indexOfMethod<void (QQuick3DXrVirtualMouse::*)(bool )>(_a, &QQuick3DXrVirtualMouse::middleMouseButtonChanged, 2))
            return;
        if (QtMocHelpers::indexOfMethod<void (QQuick3DXrVirtualMouse::*)(float )>(_a, &QQuick3DXrVirtualMouse::scrollWheelXChanged, 3))
            return;
        if (QtMocHelpers::indexOfMethod<void (QQuick3DXrVirtualMouse::*)(float )>(_a, &QQuick3DXrVirtualMouse::scrollWheelYChanged, 4))
            return;
        if (QtMocHelpers::indexOfMethod<void (QQuick3DXrVirtualMouse::*)(int )>(_a, &QQuick3DXrVirtualMouse::scrollTimerIntervalChanged, 5))
            return;
        if (QtMocHelpers::indexOfMethod<void (QQuick3DXrVirtualMouse::*)(int )>(_a, &QQuick3DXrVirtualMouse::scrollPixelDeltaChanged, 6))
            return;
        if (QtMocHelpers::indexOfMethod<void (QQuick3DXrVirtualMouse::*)(QQuick3DNode * )>(_a, &QQuick3DXrVirtualMouse::sourceChanged, 7))
            return;
        if (QtMocHelpers::indexOfMethod<void (QQuick3DXrVirtualMouse::*)(QQuick3DXrView * )>(_a, &QQuick3DXrVirtualMouse::viewChanged, 8))
            return;
        if (QtMocHelpers::indexOfMethod<void (QQuick3DXrVirtualMouse::*)(bool )>(_a, &QQuick3DXrVirtualMouse::enabledChanged, 9))
            return;
    }
    if (_c == QMetaObject::ReadProperty) {
        void *_v = _a[0];
        switch (_id) {
        case 0: *reinterpret_cast<bool*>(_v) = _t->rightMouseButton(); break;
        case 1: *reinterpret_cast<bool*>(_v) = _t->leftMouseButton(); break;
        case 2: *reinterpret_cast<bool*>(_v) = _t->middleMouseButton(); break;
        case 3: *reinterpret_cast<float*>(_v) = _t->scrollWheelX(); break;
        case 4: *reinterpret_cast<float*>(_v) = _t->scrollWheelY(); break;
        case 5: *reinterpret_cast<int*>(_v) = _t->scrollTimerInterval(); break;
        case 6: *reinterpret_cast<int*>(_v) = _t->scrollPixelDelta(); break;
        case 7: *reinterpret_cast<QQuick3DNode**>(_v) = _t->source(); break;
        case 8: *reinterpret_cast<QQuick3DXrView**>(_v) = _t->view(); break;
        case 9: *reinterpret_cast<bool*>(_v) = _t->enabled(); break;
        default: break;
        }
    }
    if (_c == QMetaObject::WriteProperty) {
        void *_v = _a[0];
        switch (_id) {
        case 0: _t->setRightMouseButton(*reinterpret_cast<bool*>(_v)); break;
        case 1: _t->setLeftMouseButton(*reinterpret_cast<bool*>(_v)); break;
        case 2: _t->setMiddleMouseButton(*reinterpret_cast<bool*>(_v)); break;
        case 3: _t->setScrollWheelX(*reinterpret_cast<float*>(_v)); break;
        case 4: _t->setScrollWheelY(*reinterpret_cast<float*>(_v)); break;
        case 5: _t->setScrollTimerInterval(*reinterpret_cast<int*>(_v)); break;
        case 6: _t->setScrollPixelDelta(*reinterpret_cast<int*>(_v)); break;
        case 7: _t->setSource(*reinterpret_cast<QQuick3DNode**>(_v)); break;
        case 8: _t->setView(*reinterpret_cast<QQuick3DXrView**>(_v)); break;
        case 9: _t->setEnabled(*reinterpret_cast<bool*>(_v)); break;
        default: break;
        }
    }
}

const QMetaObject *QQuick3DXrVirtualMouse::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QQuick3DXrVirtualMouse::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN22QQuick3DXrVirtualMouseE_t>.strings))
        return static_cast<void*>(this);
    return QObject::qt_metacast(_clname);
}

int QQuick3DXrVirtualMouse::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QObject::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 22)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 22;
    }
    if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 22)
            *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType();
        _id -= 22;
    }
    if (_c == QMetaObject::ReadProperty || _c == QMetaObject::WriteProperty
            || _c == QMetaObject::ResetProperty || _c == QMetaObject::BindableProperty
            || _c == QMetaObject::RegisterPropertyMetaType) {
        qt_static_metacall(this, _c, _id, _a);
        _id -= 10;
    }
    return _id;
}

// SIGNAL 0
void QQuick3DXrVirtualMouse::rightMouseButtonChanged(bool _t1)
{
    QMetaObject::activate<void>(this, &staticMetaObject, 0, nullptr, _t1);
}

// SIGNAL 1
void QQuick3DXrVirtualMouse::leftMouseButtonChanged(bool _t1)
{
    QMetaObject::activate<void>(this, &staticMetaObject, 1, nullptr, _t1);
}

// SIGNAL 2
void QQuick3DXrVirtualMouse::middleMouseButtonChanged(bool _t1)
{
    QMetaObject::activate<void>(this, &staticMetaObject, 2, nullptr, _t1);
}

// SIGNAL 3
void QQuick3DXrVirtualMouse::scrollWheelXChanged(float _t1)
{
    QMetaObject::activate<void>(this, &staticMetaObject, 3, nullptr, _t1);
}

// SIGNAL 4
void QQuick3DXrVirtualMouse::scrollWheelYChanged(float _t1)
{
    QMetaObject::activate<void>(this, &staticMetaObject, 4, nullptr, _t1);
}

// SIGNAL 5
void QQuick3DXrVirtualMouse::scrollTimerIntervalChanged(int _t1)
{
    QMetaObject::activate<void>(this, &staticMetaObject, 5, nullptr, _t1);
}

// SIGNAL 6
void QQuick3DXrVirtualMouse::scrollPixelDeltaChanged(int _t1)
{
    QMetaObject::activate<void>(this, &staticMetaObject, 6, nullptr, _t1);
}

// SIGNAL 7
void QQuick3DXrVirtualMouse::sourceChanged(QQuick3DNode * _t1)
{
    QMetaObject::activate<void>(this, &staticMetaObject, 7, nullptr, _t1);
}

// SIGNAL 8
void QQuick3DXrVirtualMouse::viewChanged(QQuick3DXrView * _t1)
{
    QMetaObject::activate<void>(this, &staticMetaObject, 8, nullptr, _t1);
}

// SIGNAL 9
void QQuick3DXrVirtualMouse::enabledChanged(bool _t1)
{
    QMetaObject::activate<void>(this, &staticMetaObject, 9, nullptr, _t1);
}
QT_WARNING_POP

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrvirtualmouse.cpp, line 297, as _ZN22QQuick3DXrVirtualMouse10setEnabledEb
inline void QQuick3DXrVirtualMouse::setEnabled(bool enabled)
{
    if (m_enabled == enabled)
        return;
    m_enabled = enabled;
    emit enabledChanged(m_enabled);

    // Generate mouse release event if we disable when pressed
    if (!m_enabled && (m_leftMouseButton || m_rightMouseButton || m_middleMouseButton)) {
        Qt::MouseButton button = m_leftMouseButton ? Qt::LeftButton : m_rightMouseButton ? Qt::RightButton : Qt::MiddleButton;
        m_leftMouseButton = m_rightMouseButton = m_middleMouseButton = false;
        generateEvent(QEvent::MouseButtonRelease, button);
    }
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrvirtualmouse.cpp, line 224, as _ZN22QQuick3DXrVirtualMouse15setScrollWheelXEf
inline void QQuick3DXrVirtualMouse::setScrollWheelX(float scrollWheelX)
{
    if (m_scrollWheelX == scrollWheelX)
        return;

    m_scrollWheelX = scrollWheelX;
    emit scrollWheelXChanged(m_scrollWheelX);
    if ((m_scrollTimer->isActive()) && (m_scrollWheelX == 0)) {
        m_scrollTimer->stop();
    } else if (!m_scrollTimer->isActive()) {
        m_scrollTimer->start();
    }
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrvirtualmouse.cpp, line 238, as _ZN22QQuick3DXrVirtualMouse15setScrollWheelYEf
inline void QQuick3DXrVirtualMouse::setScrollWheelY(float scrollWheelY)
{
    if (m_scrollWheelY == scrollWheelY)
        return;

    m_scrollWheelY = scrollWheelY;
    emit scrollWheelYChanged(m_scrollWheelY);
    if ((m_scrollTimer->isActive()) && (m_scrollWheelY == 0)) {
        m_scrollTimer->stop();
    } else if (!m_scrollTimer->isActive()) {
        m_scrollTimer->start();
    }
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrvirtualmouse.cpp, line 317, as _ZN22QQuick3DXrVirtualMouse18generateWheelEventEv
inline void QQuick3DXrVirtualMouse::generateWheelEvent()
{
    if (!m_view || !m_source || m_view->m_inDestructor || !m_enabled)
        return;

    // Get Ray
    const QVector3D origin = m_source->scenePosition();
    const QVector3D direction = m_source->forward();

    float x = 0;
    float y = 0;

    if (m_scrollWheelX > 0) {
        x = m_scrollPixelDelta * m_scrollWheelX * m_scrollWheelX;
    } else if (m_scrollWheelX < 0) {
        x = -m_scrollPixelDelta * m_scrollWheelX * m_scrollWheelX;
    }

    if (m_scrollWheelY > 0) {
        y = m_scrollPixelDelta * m_scrollWheelY * m_scrollWheelY;
    } else if (m_scrollWheelY < 0) {
        y = -m_scrollPixelDelta * m_scrollWheelY * m_scrollWheelY;
    }

    QPoint pixelDelta = QPoint(x, y);
    QPoint angleDelta = QPoint(x*8, y*8);

    // Position will be generated by QtQuick3D
    QWheelEvent *event = new QWheelEvent(QPointF(), QPointF(), pixelDelta, angleDelta,
                                         Qt::NoButton, Qt::NoModifier, Qt::NoScrollPhase, false);

    // Send to View with Ray
    if (m_view->view3d()) // no internal view3D if XrView init failed but the object is still alive, handle this gracefully
        m_view->view3d()->singlePointPick(event, origin, direction);

    // Cleanup
    delete event;
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrvirtualmouse.cpp, line 192, as _ZN22QQuick3DXrVirtualMouse18setLeftMouseButtonEb
inline void QQuick3DXrVirtualMouse::setLeftMouseButton(bool leftMouseButton)
{
    if (m_leftMouseButton == leftMouseButton)
        return;

    m_leftMouseButton = leftMouseButton;
    emit leftMouseButtonChanged(m_leftMouseButton);
    if (m_leftMouseButton) {
        // Press
        generateEvent(QEvent::MouseButtonPress, Qt::LeftButton);
    } else {
        // Release
        generateEvent(QEvent::MouseButtonRelease, Qt::LeftButton);
    }
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrvirtualmouse.cpp, line 176, as _ZN22QQuick3DXrVirtualMouse19setRightMouseButtonEb
inline void QQuick3DXrVirtualMouse::setRightMouseButton(bool rightMouseButton)
{
    if (m_rightMouseButton == rightMouseButton)
        return;

    m_rightMouseButton = rightMouseButton;
    emit rightMouseButtonChanged(m_rightMouseButton);
    if (m_rightMouseButton) {
        // Press
        generateEvent(QEvent::MouseButtonPress, Qt::RightButton);
    } else {
        // Release
        generateEvent(QEvent::MouseButtonRelease, Qt::RightButton);
    }
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrvirtualmouse.cpp, line 263, as _ZN22QQuick3DXrVirtualMouse19setScrollPixelDeltaEi
inline void QQuick3DXrVirtualMouse::setScrollPixelDelta(int scrollPixelDelta)
{
    if (m_scrollPixelDelta == scrollPixelDelta)
        return;

    m_scrollPixelDelta = scrollPixelDelta;

    emit scrollPixelDeltaChanged(m_scrollPixelDelta);
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrvirtualmouse.cpp, line 208, as _ZN22QQuick3DXrVirtualMouse20setMiddleMouseButtonEb
inline void QQuick3DXrVirtualMouse::setMiddleMouseButton(bool middleMouseButton)
{
    if (m_middleMouseButton == middleMouseButton)
        return;

    m_middleMouseButton = middleMouseButton;
    emit middleMouseButtonChanged(m_middleMouseButton);
    if (m_middleMouseButton) {
        // Press
        generateEvent(QEvent::MouseButtonPress, Qt::MiddleButton);
    } else {
        // Release
        generateEvent(QEvent::MouseButtonRelease, Qt::MiddleButton);
    }
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrvirtualmouse.cpp, line 252, as _ZN22QQuick3DXrVirtualMouse22setScrollTimerIntervalEi
inline void QQuick3DXrVirtualMouse::setScrollTimerInterval(int scrollTimerInterval)
{
    if (m_scrollTimerInterval == scrollTimerInterval)
        return;

    m_scrollTimerInterval = scrollTimerInterval;
    m_scrollTimer->setInterval(m_scrollTimerInterval);

    emit scrollTimerIntervalChanged(m_scrollTimerInterval);
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrvirtualmouse.cpp, line 288, as _ZN22QQuick3DXrVirtualMouse7setViewEP14QQuick3DXrView
inline void QQuick3DXrVirtualMouse::setView(QQuick3DXrView *view)
{
    if (m_view == view)
        return;

    m_view = view;
    emit viewChanged(m_view);
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrvirtualmouse.cpp, line 312, as _ZN22QQuick3DXrVirtualMouse9moveEventEv
inline void QQuick3DXrVirtualMouse::moveEvent()
{
    generateEvent(QEvent::MouseMove, Qt::NoButton);
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrvirtualmouse.cpp, line 273, as _ZN22QQuick3DXrVirtualMouse9setSourceEP12QQuick3DNode
inline void QQuick3DXrVirtualMouse::setSource(QQuick3DNode *source)
{
    if (m_source == source)
        return;

    if (!source)
        disconnect(m_source, &QQuick3DNode::sceneTransformChanged, this, &QQuick3DXrVirtualMouse::moveEvent);

    m_source = source;
    emit sourceChanged(m_source);

    if (m_source)
        connect(m_source, &QQuick3DNode::sceneTransformChanged, this, &QQuick3DXrVirtualMouse::moveEvent);
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrvirtualmouse.cpp, line 41, as _ZN22QQuick3DXrVirtualMouseC1EP7QObject
inline QQuick3DXrVirtualMouse::QQuick3DXrVirtualMouse(QObject *parent) : QObject(parent)
{
    m_scrollTimer = new QTimer(this);
    m_scrollTimer->setInterval(m_scrollTimerInterval);
    connect(m_scrollTimer, SIGNAL(timeout()), this, SLOT(generateWheelEvent()));
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrvirtualmouse.cpp, line 55, as _ZNK22QQuick3DXrVirtualMouse16rightMouseButtonEv
inline bool QQuick3DXrVirtualMouse::rightMouseButton() const
{
    return m_rightMouseButton;
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrvirtualmouse.cpp, line 67, as _ZNK22QQuick3DXrVirtualMouse15leftMouseButtonEv
inline bool QQuick3DXrVirtualMouse::leftMouseButton() const
{
    return m_leftMouseButton;
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrvirtualmouse.cpp, line 79, as _ZNK22QQuick3DXrVirtualMouse17middleMouseButtonEv
inline bool QQuick3DXrVirtualMouse::middleMouseButton() const
{
    return m_middleMouseButton;
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrvirtualmouse.cpp, line 94, as _ZNK22QQuick3DXrVirtualMouse12scrollWheelXEv
inline float QQuick3DXrVirtualMouse::scrollWheelX() const
{
    return m_scrollWheelX;
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrvirtualmouse.cpp, line 109, as _ZNK22QQuick3DXrVirtualMouse12scrollWheelYEv
inline float QQuick3DXrVirtualMouse::scrollWheelY() const
{
    return m_scrollWheelY;
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrvirtualmouse.cpp, line 120, as _ZNK22QQuick3DXrVirtualMouse19scrollTimerIntervalEv
inline int QQuick3DXrVirtualMouse::scrollTimerInterval() const
{
    return m_scrollTimerInterval;
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrvirtualmouse.cpp, line 135, as _ZNK22QQuick3DXrVirtualMouse16scrollPixelDeltaEv
inline int QQuick3DXrVirtualMouse::scrollPixelDelta() const
{
    return m_scrollPixelDelta;
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrvirtualmouse.cpp, line 149, as _ZNK22QQuick3DXrVirtualMouse6sourceEv
inline QQuick3DNode *QQuick3DXrVirtualMouse::source() const
{
    return m_source;
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrvirtualmouse.cpp, line 160, as _ZNK22QQuick3DXrVirtualMouse4viewEv
inline QQuick3DXrView *QQuick3DXrVirtualMouse::view() const
{
    return m_view;
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrvirtualmouse.cpp, line 171, as _ZNK22QQuick3DXrVirtualMouse7enabledEv
inline bool QQuick3DXrVirtualMouse::enabled() const
{
    return m_enabled;
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrvirtualmouse.cpp, line 356, as _ZN22QQuick3DXrVirtualMouse13generateEventEN6QEvent4TypeEN2Qt11MouseButtonE
inline void QQuick3DXrVirtualMouse::generateEvent(QEvent::Type type,  Qt::MouseButton button)
{
    if (!m_view || !m_source || m_view->m_inDestructor || !m_enabled)
        return;

    // Get Ray
    const QVector3D origin = m_source->scenePosition();
    const QVector3D direction = m_source->forward();

    // Generate Pointer Event
    Qt::MouseButtons buttons = Qt::NoButton;
    if (m_leftMouseButton)
        buttons |= Qt::LeftButton;
    if (m_rightMouseButton)
        buttons |= Qt::RightButton;
    if (m_middleMouseButton)
        buttons |= Qt::MiddleButton;

    // Position will be generated by QtQuick3D
    QMouseEvent *event = new QMouseEvent(type, QPointF(), QPointF(), button, buttons, Qt::NoModifier);

    // Send to View with Ray
    if (m_view->view3d()) // no internal view3D if XrView init failed but the object is still alive, handle this gracefully
        m_view->view3d()->singlePointPick(event, origin, direction);

    // Cleanup
    delete event;
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QQuick3DXrVirtualMouse::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK22QQuick3DXrVirtualMouse10metaObjectEv(
    const QQuick3DXrVirtualMouse *self) {
  return self->metaObject();
}

//  void *QQuick3DXrVirtualMouse::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN22QQuick3DXrVirtualMouse11qt_metacastEPKc(
    QQuick3DXrVirtualMouse *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuick3DXrVirtualMouse::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN22QQuick3DXrVirtualMouse11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuick3DXrVirtualMouse *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuick3DXrVirtualMouse::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN22QQuick3DXrVirtualMouse2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuick3DXrVirtualMouse::tr(s, c, n));
}

//  QQuick3DXrVirtualMouse::QQuick3DXrVirtualMouse(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuick3DXrVirtualMouse *ritual_ZN22QQuick3DXrVirtualMouseC1EP7QObject(
    QObject *parent) {
  return new QQuick3DXrVirtualMouse(parent);
}

//  bool QQuick3DXrVirtualMouse::rightMouseButton() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QQuick3DXrVirtualMouse16rightMouseButtonEv(
    const QQuick3DXrVirtualMouse *self) {
  return self->rightMouseButton();
}

//  bool QQuick3DXrVirtualMouse::leftMouseButton() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QQuick3DXrVirtualMouse15leftMouseButtonEv(
    const QQuick3DXrVirtualMouse *self) {
  return self->leftMouseButton();
}

//  bool QQuick3DXrVirtualMouse::middleMouseButton() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QQuick3DXrVirtualMouse17middleMouseButtonEv(
    const QQuick3DXrVirtualMouse *self) {
  return self->middleMouseButton();
}

//  float QQuick3DXrVirtualMouse::scrollWheelX() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK22QQuick3DXrVirtualMouse12scrollWheelXEv(
    const QQuick3DXrVirtualMouse *self) {
  return self->scrollWheelX();
}

//  float QQuick3DXrVirtualMouse::scrollWheelY() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK22QQuick3DXrVirtualMouse12scrollWheelYEv(
    const QQuick3DXrVirtualMouse *self) {
  return self->scrollWheelY();
}

//  int QQuick3DXrVirtualMouse::scrollTimerInterval() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22QQuick3DXrVirtualMouse19scrollTimerIntervalEv(
    const QQuick3DXrVirtualMouse *self) {
  return self->scrollTimerInterval();
}

//  int QQuick3DXrVirtualMouse::scrollPixelDelta() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22QQuick3DXrVirtualMouse16scrollPixelDeltaEv(
    const QQuick3DXrVirtualMouse *self) {
  return self->scrollPixelDelta();
}

//  QQuick3DNode *QQuick3DXrVirtualMouse::source() const
extern "C" Q_DECL_EXPORT
QQuick3DNode *ritual_ZNK22QQuick3DXrVirtualMouse6sourceEv(
    const QQuick3DXrVirtualMouse *self) {
  return self->source();
}

//  QQuick3DXrView *QQuick3DXrVirtualMouse::view() const
extern "C" Q_DECL_EXPORT
QQuick3DXrView *ritual_ZNK22QQuick3DXrVirtualMouse4viewEv(
    const QQuick3DXrVirtualMouse *self) {
  return self->view();
}

//  bool QQuick3DXrVirtualMouse::enabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QQuick3DXrVirtualMouse7enabledEv(
    const QQuick3DXrVirtualMouse *self) {
  return self->enabled();
}

//  void QQuick3DXrVirtualMouse::setRightMouseButton(bool rightMouseButton)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DXrVirtualMouse19setRightMouseButtonEb(
    QQuick3DXrVirtualMouse *self,
    bool rightMouseButton) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DXrVirtualMouse")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "setRightMouseButton(bool)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "setRightMouseButton(bool)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&rightMouseButton)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DXrVirtualMouse::setLeftMouseButton(bool leftMouseButton)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DXrVirtualMouse18setLeftMouseButtonEb(
    QQuick3DXrVirtualMouse *self,
    bool leftMouseButton) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DXrVirtualMouse")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "setLeftMouseButton(bool)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "setLeftMouseButton(bool)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&leftMouseButton)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DXrVirtualMouse::setMiddleMouseButton(bool middleMouseButton)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DXrVirtualMouse20setMiddleMouseButtonEb(
    QQuick3DXrVirtualMouse *self,
    bool middleMouseButton) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DXrVirtualMouse")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "setMiddleMouseButton(bool)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "setMiddleMouseButton(bool)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&middleMouseButton)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DXrVirtualMouse::setScrollWheelX(float scrollWheelX)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DXrVirtualMouse15setScrollWheelXEf(
    QQuick3DXrVirtualMouse *self,
    float scrollWheelX) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DXrVirtualMouse")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "setScrollWheelX(float)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "setScrollWheelX(float)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&scrollWheelX)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DXrVirtualMouse::setScrollWheelY(float scrollWheelY)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DXrVirtualMouse15setScrollWheelYEf(
    QQuick3DXrVirtualMouse *self,
    float scrollWheelY) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DXrVirtualMouse")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "setScrollWheelY(float)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "setScrollWheelY(float)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&scrollWheelY)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DXrVirtualMouse::setScrollTimerInterval(int
//      scrollTimerInterval)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DXrVirtualMouse22setScrollTimerIntervalEi(
    QQuick3DXrVirtualMouse *self,
    int scrollTimerInterval) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DXrVirtualMouse")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "setScrollTimerInterval(int)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "setScrollTimerInterval(int)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&scrollTimerInterval)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DXrVirtualMouse::setScrollPixelDelta(int scrollPixelDelta)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DXrVirtualMouse19setScrollPixelDeltaEi(
    QQuick3DXrVirtualMouse *self,
    int scrollPixelDelta) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DXrVirtualMouse")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "setScrollPixelDelta(int)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "setScrollPixelDelta(int)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&scrollPixelDelta)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DXrVirtualMouse::setSource(QQuick3DNode *source)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DXrVirtualMouse9setSourceEP12QQuick3DNode(
    QQuick3DXrVirtualMouse *self,
    QQuick3DNode *source) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DXrVirtualMouse")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "setSource(QQuick3DNode *)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "setSource(QQuick3DNode *)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&source)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DXrVirtualMouse::setView(QQuick3DXrView *view)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DXrVirtualMouse7setViewEP14QQuick3DXrView(
    QQuick3DXrVirtualMouse *self,
    QQuick3DXrView *view) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DXrVirtualMouse")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "setView(QQuick3DXrView *)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "setView(QQuick3DXrView *)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&view)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DXrVirtualMouse::setEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DXrVirtualMouse10setEnabledEb(
    QQuick3DXrVirtualMouse *self,
    bool enabled) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DXrVirtualMouse")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "setEnabled(bool)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "setEnabled(bool)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&enabled)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DXrVirtualMouse::moveEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DXrVirtualMouse9moveEventEv(
    QQuick3DXrVirtualMouse *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DXrVirtualMouse")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "moveEvent()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "moveEvent()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DXrVirtualMouse::generateWheelEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DXrVirtualMouse18generateWheelEventEv(
    QQuick3DXrVirtualMouse *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DXrVirtualMouse")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "generateWheelEvent()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "generateWheelEvent()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DXrVirtualMouse::rightMouseButtonChanged(bool
//      rightMouseButton)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DXrVirtualMouse23rightMouseButtonChangedEb(
    QQuick3DXrVirtualMouse *self,
    bool rightMouseButton) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DXrVirtualMouse")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "rightMouseButtonChanged(bool)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "rightMouseButtonChanged(bool)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&rightMouseButton)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DXrVirtualMouse::leftMouseButtonChanged(bool leftMouseButton)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DXrVirtualMouse22leftMouseButtonChangedEb(
    QQuick3DXrVirtualMouse *self,
    bool leftMouseButton) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DXrVirtualMouse")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "leftMouseButtonChanged(bool)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "leftMouseButtonChanged(bool)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&leftMouseButton)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DXrVirtualMouse::middleMouseButtonChanged(bool
//      middleMouseButton)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DXrVirtualMouse24middleMouseButtonChangedEb(
    QQuick3DXrVirtualMouse *self,
    bool middleMouseButton) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DXrVirtualMouse")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "middleMouseButtonChanged(bool)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "middleMouseButtonChanged(bool)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&middleMouseButton)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DXrVirtualMouse::scrollWheelXChanged(float scrollWheelX)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DXrVirtualMouse19scrollWheelXChangedEf(
    QQuick3DXrVirtualMouse *self,
    float scrollWheelX) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DXrVirtualMouse")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "scrollWheelXChanged(float)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "scrollWheelXChanged(float)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&scrollWheelX)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DXrVirtualMouse::scrollWheelYChanged(float scrollWheelY)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DXrVirtualMouse19scrollWheelYChangedEf(
    QQuick3DXrVirtualMouse *self,
    float scrollWheelY) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DXrVirtualMouse")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "scrollWheelYChanged(float)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "scrollWheelYChanged(float)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&scrollWheelY)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DXrVirtualMouse::scrollTimerIntervalChanged(int
//      scrollTimerInterval)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DXrVirtualMouse26scrollTimerIntervalChangedEi(
    QQuick3DXrVirtualMouse *self,
    int scrollTimerInterval) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DXrVirtualMouse")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "scrollTimerIntervalChanged(int)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "scrollTimerIntervalChanged(int)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&scrollTimerInterval)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DXrVirtualMouse::scrollPixelDeltaChanged(int
//      scrollPixelDelta)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DXrVirtualMouse23scrollPixelDeltaChangedEi(
    QQuick3DXrVirtualMouse *self,
    int scrollPixelDelta) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DXrVirtualMouse")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "scrollPixelDeltaChanged(int)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "scrollPixelDeltaChanged(int)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&scrollPixelDelta)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DXrVirtualMouse::sourceChanged(QQuick3DNode *source)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DXrVirtualMouse13sourceChangedEP12QQuick3DNode(
    QQuick3DXrVirtualMouse *self,
    QQuick3DNode *source) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DXrVirtualMouse")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "sourceChanged(QQuick3DNode *)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "sourceChanged(QQuick3DNode *)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&source)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DXrVirtualMouse::viewChanged(QQuick3DXrView *view)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DXrVirtualMouse11viewChangedEP14QQuick3DXrView(
    QQuick3DXrVirtualMouse *self,
    QQuick3DXrView *view) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DXrVirtualMouse")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "viewChanged(QQuick3DXrView *)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "viewChanged(QQuick3DXrView *)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&view)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DXrVirtualMouse::enabledChanged(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DXrVirtualMouse14enabledChangedEb(
    QQuick3DXrVirtualMouse *self,
    bool enabled) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DXrVirtualMouse")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "enabledChanged(bool)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "enabledChanged(bool)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&enabled)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DXrVirtualMouse::generateEvent(QEvent::Type type,
//      Qt::MouseButton button)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DXrVirtualMouse13generateEventEN6QEvent4TypeEN2Qt11MouseButtonE(
    QQuick3DXrVirtualMouse *self,
    QEvent::Type type,
    Qt::MouseButton button) {
  self->generateEvent(type, button);
}
