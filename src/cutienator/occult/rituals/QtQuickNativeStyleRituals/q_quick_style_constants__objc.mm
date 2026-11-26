//  Written by hand on 2026-11-25 from
//  QtQuickNativeStyle/6.12.0/QtQuickNativeStyle/private/qquickstyleconstants_p.h,
//  Qt 6.12.0, from Qt's source. Kept as it is when the generator runs
//  again. Objective-C++: Qt writes these functions only in
//  'qquickstyleconstants.mm', and Qt's library has no name for them, so
//  their code is copied here, which only a compiler of Objective-C++ on
//  Apple's systems reads; 'summon' builds this file there only. With the
//  constructor and moc's code for the class, its meta-object among it,
//  the compiler writes the class's table of virtual functions here,
//  which Qt's library keeps to itself: an object made here has the
//  meta-object of this file, a copy of Qt's.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if defined(Q_OS_MACOS)
#include <QtQuickNativeStyle/6.12.0/QtQuickNativeStyle/private/qquickstyleconstants_p.h>
#include <QtCore/6.12.0/QtCore/private/qcore_mac_p.h>
#include <QtGui/6.12.0/QtGui/private/qcoregraphics_p.h>
#include <QtGui/qguiapplication.h>
#include <QtGui/qstylehints.h>
#include <AppKit/AppKit.h>
#include <functional>
#include <QtCore/qmetaobject.h>

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from qtdeclarative/src/quickcontrols/quicknativestyle/util/
//  qquickstyleconstants.mm, lines 26-52
QT_BEGIN_NAMESPACE

//  from qtdeclarative/src/quickcontrols/quicknativestyle/util/qquickstyleconstants.mm, line 18
QQuickStyleConstants::QQuickStyleConstants()
{
    connect(QGuiApplication::styleHints(), &QStyleHints::colorSchemeChanged, this, [this] {
        emit secondarySystemFillColorChanged();
        emit tertiarySystemFillColorChanged();
    });
}

inline bool QQuickStyleConstants::runningWithLiquidGlass() const
{
    return qt_apple_runningWithLiquidGlass();
}

static QColor systemColor(std::function<NSColor *()> block)
{
    __block QColor color;
    [NSApp.effectiveAppearance performAsCurrentDrawingAppearance:^{
        color = qt_mac_toQBrush(block()).color();
    }];
    return color;
}

inline QColor QQuickStyleConstants::secondarySystemFillColor() const
{
    if (@available(macOS 14.0, *))
        return systemColor([] { return NSColor.secondarySystemFillColor; });
    return Qt::black;
}

inline QColor QQuickStyleConstants::tertiarySystemFillColor() const
{
    if (@available(macOS 14.0, *))
        return systemColor([] { return NSColor.tertiarySystemFillColor; });
    return Qt::black;
}

QT_END_NAMESPACE
//  moc's code for qquickstyleconstants_p.h, as Qt's moc 6.12.0 writes it
//  from that header (run on gcloud with the full Linux kit): the class's
//  meta-object and the functions moc writes, which Qt's library holds
//  under no name.
/****************************************************************************
** Meta object code from reading C++ file 'qquickstyleconstants_p.h'
**
** Created by: The Qt Meta Object Compiler version 69 (Qt 6.12.0)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include <QtCore/qmetatype.h>

#include <QtCore/qtmochelpers.h>

#include <memory>


#include <QtCore/qxptype_traits.h>
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'qquickstyleconstants_p.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 69
#error "This file was generated using the moc from 6.12.0. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif

QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
QT_WARNING_DISABLE_GCC("-Wuseless-cast")
namespace {
struct qt_meta_tag_ZN20QQuickStyleConstantsE_t {};
} // unnamed namespace

template <> constexpr inline auto QQuickStyleConstants::qt_create_metaobjectdata<qt_meta_tag_ZN20QQuickStyleConstantsE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QQuickStyleConstants",
        "secondarySystemFillColorChanged",
        "",
        "tertiarySystemFillColorChanged",
        "runningWithLiquidGlass",
        "secondarySystemFillColor",
        "QColor",
        "tertiarySystemFillColor"
    };

    QtMocHelpers::UintData qt_methods {
        // Signal 'secondarySystemFillColorChanged'
        QtMocHelpers::SignalData<void()>(1, 2, QMC::AccessPublic, QMetaType::Void),
        // Signal 'tertiarySystemFillColorChanged'
        QtMocHelpers::SignalData<void()>(3, 2, QMC::AccessPublic, QMetaType::Void),
    };
    QtMocHelpers::UintData qt_properties {
        // property 'runningWithLiquidGlass'
        QtMocHelpers::PropertyData<bool>(4, QMetaType::Bool, QMC::DefaultPropertyFlags | QMC::Constant | QMC::Final),
        // property 'secondarySystemFillColor'
        QtMocHelpers::PropertyData<QColor>(5, 0x80000000 | 6, QMC::DefaultPropertyFlags | QMC::EnumOrFlag | QMC::Final, 0),
        // property 'tertiarySystemFillColor'
        QtMocHelpers::PropertyData<QColor>(7, 0x80000000 | 6, QMC::DefaultPropertyFlags | QMC::EnumOrFlag | QMC::Final, 1),
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<QQuickStyleConstants, qt_meta_tag_ZN20QQuickStyleConstantsE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject QQuickStyleConstants::staticMetaObject = { {
    QMetaObject::SuperData::link<QObject::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN20QQuickStyleConstantsE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN20QQuickStyleConstantsE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN20QQuickStyleConstantsE_t>.metaTypes,
    nullptr
} };

void QQuickStyleConstants::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QQuickStyleConstants *>(_o);
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: _t->secondarySystemFillColorChanged(); break;
        case 1: _t->tertiarySystemFillColorChanged(); break;
        default: ;
        }
    }
    if (_c == QMetaObject::IndexOfMethod) {
        if (QtMocHelpers::indexOfMethod<void (QQuickStyleConstants::*)()>(_a, &QQuickStyleConstants::secondarySystemFillColorChanged, 0))
            return;
        if (QtMocHelpers::indexOfMethod<void (QQuickStyleConstants::*)()>(_a, &QQuickStyleConstants::tertiarySystemFillColorChanged, 1))
            return;
    }
    if (_c == QMetaObject::ReadProperty) {
        void *_v = _a[0];
        switch (_id) {
        case 0: *reinterpret_cast<bool*>(_v) = _t->runningWithLiquidGlass(); break;
        case 1: *reinterpret_cast<QColor*>(_v) = _t->secondarySystemFillColor(); break;
        case 2: *reinterpret_cast<QColor*>(_v) = _t->tertiarySystemFillColor(); break;
        default: break;
        }
    }
}

const QMetaObject *QQuickStyleConstants::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QQuickStyleConstants::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN20QQuickStyleConstantsE_t>.strings))
        return static_cast<void*>(this);
    return QObject::qt_metacast(_clname);
}

int QQuickStyleConstants::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QObject::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 2)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 2;
    }
    if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 2)
            *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType();
        _id -= 2;
    }
    if (_c == QMetaObject::ReadProperty || _c == QMetaObject::WriteProperty
            || _c == QMetaObject::ResetProperty || _c == QMetaObject::BindableProperty
            || _c == QMetaObject::RegisterPropertyMetaType) {
        qt_static_metacall(this, _c, _id, _a);
        _id -= 3;
    }
    return _id;
}

// SIGNAL 0
void QQuickStyleConstants::secondarySystemFillColorChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 0, nullptr);
}

// SIGNAL 1
void QQuickStyleConstants::tertiarySystemFillColorChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 1, nullptr);
}
QT_WARNING_POP
//  ---------------------------------------------------------------------

//  bool QQuickStyleConstants::runningWithLiquidGlass() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QQuickStyleConstants22runningWithLiquidGlassEv(
    const QQuickStyleConstants *self) {
  return self->runningWithLiquidGlass();
}

//  QColor QQuickStyleConstants::secondarySystemFillColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK20QQuickStyleConstants24secondarySystemFillColorEv(
    const QQuickStyleConstants *self) {
  return new QColor(self->secondarySystemFillColor());
}

//  QColor QQuickStyleConstants::tertiarySystemFillColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK20QQuickStyleConstants23tertiarySystemFillColorEv(
    const QQuickStyleConstants *self) {
  return new QColor(self->tertiarySystemFillColor());
}

//  QQuickStyleConstants::QQuickStyleConstants()
extern "C" Q_DECL_EXPORT
QQuickStyleConstants *ritual_ZN20QQuickStyleConstantsC1Ev() {
  return new QQuickStyleConstants();
}

#endif
