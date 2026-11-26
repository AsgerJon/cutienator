//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/6.12.0/QtGraphs/private/axisticker_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for 'AxisTicker' is pasted in,
//  cut from what the moc of Qt 6.12.0 writes for its header: Qt's library
//  keeps it to itself; added are 18 rituals that lean on what moc writes for
//  a class of the part Qt keeps to itself, whose ritual file carries moc's
//  output, drafted by a copy of the generator that lets those names through.
//  A copy of a meta-object is a second one: 'qobject_cast' between it and
//  Qt's own does not match. Kept as it is when the generator runs again.
#include <QtQuick/qtquickglobal.h>
#include <QtGui/qtguiglobal.h>
#include <QtGraphs/qgraphsglobal.h>
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#if (QT_CONFIG(graphs_2d)) && (!(!QT_CONFIG(graphs_2d_area) && !QT_CONFIG(graphs_2d_bar) && !QT_CONFIG(graphs_2d_donut_pie) && !QT_CONFIG(graphs_2d_line) && !QT_CONFIG(graphs_2d_scatter) && !QT_CONFIG(graphs_2d_spline) && !QT_CONFIG(graphs_2d_custom)))
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#include <QtGraphs/QtGraphs>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/6.12.0/QtGraphs/private/axisticker_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qvectornd.h>
#include <QtGui/qcolor.h>
#include <QtCore/qrect.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>
#include <QtCore/qpoint.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtGraphs/private/axisticker_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from QtGraphs__AxisTicker.cpp, line 1, as moc:AxisTicker
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN10AxisTickerE_t {};
} // unnamed namespace

template <> constexpr inline auto AxisTicker::qt_create_metaobjectdata<qt_meta_tag_ZN10AxisTickerE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "AxisTicker",
        "iResolutionChanged",
        "",
        "smoothingChanged",
        "origoChanged",
        "subTicksVisibleChanged",
        "spacingChanged",
        "displacementChanged",
        "subTickColorChanged",
        "tickColorChanged",
        "subTickLineWidthChanged",
        "tickLineWidthChanged",
        "subTickScaleChanged",
        "subTickLengthChanged",
        "isHorizontalChanged",
        "flippedChanged",
        "logarithmicChanged",
        "baseChanged",
        "iResolution",
        "QVector3D",
        "smoothing",
        "origo",
        "subTicksVisible",
        "spacing",
        "displacement",
        "subTickColor",
        "QColor",
        "tickColor",
        "subTickLineWidth",
        "tickLineWidth",
        "subTickScale",
        "subTickLength",
        "isHorizontal",
        "flipped",
        "isLogarithmic",
        "base"
    };

    QtMocHelpers::UintData qt_methods {
        // Signal 'iResolutionChanged'
        QtMocHelpers::SignalData<void()>(1, 2, QMC::AccessPublic, QMetaType::Void),
        // Signal 'smoothingChanged'
        QtMocHelpers::SignalData<void()>(3, 2, QMC::AccessPublic, QMetaType::Void),
        // Signal 'origoChanged'
        QtMocHelpers::SignalData<void()>(4, 2, QMC::AccessPublic, QMetaType::Void),
        // Signal 'subTicksVisibleChanged'
        QtMocHelpers::SignalData<void()>(5, 2, QMC::AccessPublic, QMetaType::Void),
        // Signal 'spacingChanged'
        QtMocHelpers::SignalData<void()>(6, 2, QMC::AccessPublic, QMetaType::Void),
        // Signal 'displacementChanged'
        QtMocHelpers::SignalData<void()>(7, 2, QMC::AccessPublic, QMetaType::Void),
        // Signal 'subTickColorChanged'
        QtMocHelpers::SignalData<void()>(8, 2, QMC::AccessPublic, QMetaType::Void),
        // Signal 'tickColorChanged'
        QtMocHelpers::SignalData<void()>(9, 2, QMC::AccessPublic, QMetaType::Void),
        // Signal 'subTickLineWidthChanged'
        QtMocHelpers::SignalData<void()>(10, 2, QMC::AccessPublic, QMetaType::Void),
        // Signal 'tickLineWidthChanged'
        QtMocHelpers::SignalData<void()>(11, 2, QMC::AccessPublic, QMetaType::Void),
        // Signal 'subTickScaleChanged'
        QtMocHelpers::SignalData<void()>(12, 2, QMC::AccessPublic, QMetaType::Void),
        // Signal 'subTickLengthChanged'
        QtMocHelpers::SignalData<void()>(13, 2, QMC::AccessPublic, QMetaType::Void),
        // Signal 'isHorizontalChanged'
        QtMocHelpers::SignalData<void()>(14, 2, QMC::AccessPublic, QMetaType::Void),
        // Signal 'flippedChanged'
        QtMocHelpers::SignalData<void()>(15, 2, QMC::AccessPublic, QMetaType::Void),
        // Signal 'logarithmicChanged'
        QtMocHelpers::RevisionedSignalData<void()>(16, 2, QMC::AccessPublic, 0x60c, QMetaType::Void),
        // Signal 'baseChanged'
        QtMocHelpers::RevisionedSignalData<void()>(17, 2, QMC::AccessPublic, 0x60c, QMetaType::Void),
    };
    QtMocHelpers::UintData qt_properties {
        // property 'iResolution'
        QtMocHelpers::PropertyData<QVector3D>(18, 0x80000000 | 19, QMC::DefaultPropertyFlags | QMC::EnumOrFlag | QMC::Final, 0),
        // property 'smoothing'
        QtMocHelpers::PropertyData<qreal>(20, QMetaType::QReal, QMC::DefaultPropertyFlags | QMC::Writable | QMC::StdCppSet | QMC::Final, 1),
        // property 'origo'
        QtMocHelpers::PropertyData<int>(21, QMetaType::Int, QMC::DefaultPropertyFlags | QMC::Writable | QMC::StdCppSet | QMC::Final, 2),
        // property 'subTicksVisible'
        QtMocHelpers::PropertyData<bool>(22, QMetaType::Bool, QMC::DefaultPropertyFlags | QMC::Writable | QMC::StdCppSet | QMC::Final, 3),
        // property 'spacing'
        QtMocHelpers::PropertyData<qreal>(23, QMetaType::QReal, QMC::DefaultPropertyFlags | QMC::Writable | QMC::StdCppSet | QMC::Final, 4),
        // property 'displacement'
        QtMocHelpers::PropertyData<qreal>(24, QMetaType::QReal, QMC::DefaultPropertyFlags | QMC::Writable | QMC::StdCppSet | QMC::Final, 5),
        // property 'subTickColor'
        QtMocHelpers::PropertyData<QColor>(25, 0x80000000 | 26, QMC::DefaultPropertyFlags | QMC::Writable | QMC::EnumOrFlag | QMC::StdCppSet | QMC::Final, 6),
        // property 'tickColor'
        QtMocHelpers::PropertyData<QColor>(27, 0x80000000 | 26, QMC::DefaultPropertyFlags | QMC::Writable | QMC::EnumOrFlag | QMC::StdCppSet | QMC::Final, 7),
        // property 'subTickLineWidth'
        QtMocHelpers::PropertyData<qreal>(28, QMetaType::QReal, QMC::DefaultPropertyFlags | QMC::Writable | QMC::StdCppSet | QMC::Final, 8),
        // property 'tickLineWidth'
        QtMocHelpers::PropertyData<qreal>(29, QMetaType::QReal, QMC::DefaultPropertyFlags | QMC::Writable | QMC::StdCppSet | QMC::Final, 9),
        // property 'subTickScale'
        QtMocHelpers::PropertyData<qreal>(30, QMetaType::QReal, QMC::DefaultPropertyFlags | QMC::Writable | QMC::StdCppSet | QMC::Final, 10),
        // property 'subTickLength'
        QtMocHelpers::PropertyData<qreal>(31, QMetaType::QReal, QMC::DefaultPropertyFlags | QMC::Writable | QMC::StdCppSet | QMC::Final, 11),
        // property 'isHorizontal'
        QtMocHelpers::PropertyData<bool>(32, QMetaType::Bool, QMC::DefaultPropertyFlags | QMC::Writable | QMC::StdCppSet | QMC::Final, 12),
        // property 'flipped'
        QtMocHelpers::PropertyData<bool>(33, QMetaType::Bool, QMC::DefaultPropertyFlags | QMC::Writable | QMC::StdCppSet | QMC::Final, 13),
        // property 'isLogarithmic'
        QtMocHelpers::PropertyData<bool>(34, QMetaType::Bool, QMC::DefaultPropertyFlags | QMC::Writable, 14, 0x60c),
        // property 'base'
        QtMocHelpers::PropertyData<qreal>(35, QMetaType::QReal, QMC::DefaultPropertyFlags | QMC::Writable | QMC::StdCppSet, 15, 0x60c),
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<AxisTicker, qt_meta_tag_ZN10AxisTickerE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject AxisTicker::staticMetaObject = { {
    QMetaObject::SuperData::link<QQuickShaderEffect::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN10AxisTickerE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN10AxisTickerE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN10AxisTickerE_t>.metaTypes,
    nullptr
} };

void AxisTicker::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<AxisTicker *>(_o);
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: _t->iResolutionChanged(); break;
        case 1: _t->smoothingChanged(); break;
        case 2: _t->origoChanged(); break;
        case 3: _t->subTicksVisibleChanged(); break;
        case 4: _t->spacingChanged(); break;
        case 5: _t->displacementChanged(); break;
        case 6: _t->subTickColorChanged(); break;
        case 7: _t->tickColorChanged(); break;
        case 8: _t->subTickLineWidthChanged(); break;
        case 9: _t->tickLineWidthChanged(); break;
        case 10: _t->subTickScaleChanged(); break;
        case 11: _t->subTickLengthChanged(); break;
        case 12: _t->isHorizontalChanged(); break;
        case 13: _t->flippedChanged(); break;
        case 14: _t->logarithmicChanged(); break;
        case 15: _t->baseChanged(); break;
        default: ;
        }
    }
    if (_c == QMetaObject::IndexOfMethod) {
        if (QtMocHelpers::indexOfMethod<void (AxisTicker::*)()>(_a, &AxisTicker::iResolutionChanged, 0))
            return;
        if (QtMocHelpers::indexOfMethod<void (AxisTicker::*)()>(_a, &AxisTicker::smoothingChanged, 1))
            return;
        if (QtMocHelpers::indexOfMethod<void (AxisTicker::*)()>(_a, &AxisTicker::origoChanged, 2))
            return;
        if (QtMocHelpers::indexOfMethod<void (AxisTicker::*)()>(_a, &AxisTicker::subTicksVisibleChanged, 3))
            return;
        if (QtMocHelpers::indexOfMethod<void (AxisTicker::*)()>(_a, &AxisTicker::spacingChanged, 4))
            return;
        if (QtMocHelpers::indexOfMethod<void (AxisTicker::*)()>(_a, &AxisTicker::displacementChanged, 5))
            return;
        if (QtMocHelpers::indexOfMethod<void (AxisTicker::*)()>(_a, &AxisTicker::subTickColorChanged, 6))
            return;
        if (QtMocHelpers::indexOfMethod<void (AxisTicker::*)()>(_a, &AxisTicker::tickColorChanged, 7))
            return;
        if (QtMocHelpers::indexOfMethod<void (AxisTicker::*)()>(_a, &AxisTicker::subTickLineWidthChanged, 8))
            return;
        if (QtMocHelpers::indexOfMethod<void (AxisTicker::*)()>(_a, &AxisTicker::tickLineWidthChanged, 9))
            return;
        if (QtMocHelpers::indexOfMethod<void (AxisTicker::*)()>(_a, &AxisTicker::subTickScaleChanged, 10))
            return;
        if (QtMocHelpers::indexOfMethod<void (AxisTicker::*)()>(_a, &AxisTicker::subTickLengthChanged, 11))
            return;
        if (QtMocHelpers::indexOfMethod<void (AxisTicker::*)()>(_a, &AxisTicker::isHorizontalChanged, 12))
            return;
        if (QtMocHelpers::indexOfMethod<void (AxisTicker::*)()>(_a, &AxisTicker::flippedChanged, 13))
            return;
        if (QtMocHelpers::indexOfMethod<void (AxisTicker::*)()>(_a, &AxisTicker::logarithmicChanged, 14))
            return;
        if (QtMocHelpers::indexOfMethod<void (AxisTicker::*)()>(_a, &AxisTicker::baseChanged, 15))
            return;
    }
    if (_c == QMetaObject::ReadProperty) {
        void *_v = _a[0];
        switch (_id) {
        case 0: *reinterpret_cast<QVector3D*>(_v) = _t->iResolution(); break;
        case 1: *reinterpret_cast<qreal*>(_v) = _t->smoothing(); break;
        case 2: *reinterpret_cast<int*>(_v) = _t->origo(); break;
        case 3: *reinterpret_cast<bool*>(_v) = _t->subTicksVisible(); break;
        case 4: *reinterpret_cast<qreal*>(_v) = _t->spacing(); break;
        case 5: *reinterpret_cast<qreal*>(_v) = _t->displacement(); break;
        case 6: *reinterpret_cast<QColor*>(_v) = _t->subTickColor(); break;
        case 7: *reinterpret_cast<QColor*>(_v) = _t->tickColor(); break;
        case 8: *reinterpret_cast<qreal*>(_v) = _t->subTickLineWidth(); break;
        case 9: *reinterpret_cast<qreal*>(_v) = _t->tickLineWidth(); break;
        case 10: *reinterpret_cast<qreal*>(_v) = _t->subTickScale(); break;
        case 11: *reinterpret_cast<qreal*>(_v) = _t->subTickLength(); break;
        case 12: *reinterpret_cast<bool*>(_v) = _t->isHorizontal(); break;
        case 13: *reinterpret_cast<bool*>(_v) = _t->isFlipped(); break;
        case 14: *reinterpret_cast<bool*>(_v) = _t->isLogarithmic(); break;
        case 15: *reinterpret_cast<qreal*>(_v) = _t->base(); break;
        default: break;
        }
    }
    if (_c == QMetaObject::WriteProperty) {
        void *_v = _a[0];
        switch (_id) {
        case 1: _t->setSmoothing(*reinterpret_cast<qreal*>(_v)); break;
        case 2: _t->setOrigo(*reinterpret_cast<int*>(_v)); break;
        case 3: _t->setSubTicksVisible(*reinterpret_cast<bool*>(_v)); break;
        case 4: _t->setSpacing(*reinterpret_cast<qreal*>(_v)); break;
        case 5: _t->setDisplacement(*reinterpret_cast<qreal*>(_v)); break;
        case 6: _t->setSubTickColor(*reinterpret_cast<QColor*>(_v)); break;
        case 7: _t->setTickColor(*reinterpret_cast<QColor*>(_v)); break;
        case 8: _t->setSubTickLineWidth(*reinterpret_cast<qreal*>(_v)); break;
        case 9: _t->setTickLineWidth(*reinterpret_cast<qreal*>(_v)); break;
        case 10: _t->setSubTickScale(*reinterpret_cast<qreal*>(_v)); break;
        case 11: _t->setSubTickLength(*reinterpret_cast<qreal*>(_v)); break;
        case 12: _t->setIsHorizontal(*reinterpret_cast<bool*>(_v)); break;
        case 13: _t->setFlipped(*reinterpret_cast<bool*>(_v)); break;
        case 14: _t->setLogarithmic(*reinterpret_cast<bool*>(_v)); break;
        case 15: _t->setBase(*reinterpret_cast<qreal*>(_v)); break;
        default: break;
        }
    }
}

const QMetaObject *AxisTicker::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *AxisTicker::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN10AxisTickerE_t>.strings))
        return static_cast<void*>(this);
    return QQuickShaderEffect::qt_metacast(_clname);
}

int AxisTicker::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QQuickShaderEffect::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 16)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 16;
    }
    if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 16)
            *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType();
        _id -= 16;
    }
    if (_c == QMetaObject::ReadProperty || _c == QMetaObject::WriteProperty
            || _c == QMetaObject::ResetProperty || _c == QMetaObject::BindableProperty
            || _c == QMetaObject::RegisterPropertyMetaType) {
        qt_static_metacall(this, _c, _id, _a);
        _id -= 16;
    }
    return _id;
}

// SIGNAL 0
void AxisTicker::iResolutionChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 0, nullptr);
}

// SIGNAL 1
void AxisTicker::smoothingChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 1, nullptr);
}

// SIGNAL 2
void AxisTicker::origoChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 2, nullptr);
}

// SIGNAL 3
void AxisTicker::subTicksVisibleChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 3, nullptr);
}

// SIGNAL 4
void AxisTicker::spacingChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 4, nullptr);
}

// SIGNAL 5
void AxisTicker::displacementChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 5, nullptr);
}

// SIGNAL 6
void AxisTicker::subTickColorChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 6, nullptr);
}

// SIGNAL 7
void AxisTicker::tickColorChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 7, nullptr);
}

// SIGNAL 8
void AxisTicker::subTickLineWidthChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 8, nullptr);
}

// SIGNAL 9
void AxisTicker::tickLineWidthChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 9, nullptr);
}

// SIGNAL 10
void AxisTicker::subTickScaleChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 10, nullptr);
}

// SIGNAL 11
void AxisTicker::subTickLengthChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 11, nullptr);
}

// SIGNAL 12
void AxisTicker::isHorizontalChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 12, nullptr);
}

// SIGNAL 13
void AxisTicker::flippedChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 13, nullptr);
}

// SIGNAL 14
void AxisTicker::logarithmicChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 14, nullptr);
}

// SIGNAL 15
void AxisTicker::baseChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 15, nullptr);
}
QT_WARNING_POP

//  from ../qtgraphs/src/graphs2d/axis/axisticker.cpp, line 23, as _ZN10AxisTicker14geometryChangeERK6QRectFS2_
inline void AxisTicker::geometryChange(const QRectF &newGeometry, const QRectF &oldGeometry)
{
    m_iResolution = QVector3D(newGeometry.width(), newGeometry.height(), 1.0);
    emit iResolutionChanged();

    QQuickShaderEffect::geometryChange(newGeometry, oldGeometry);
}

//  from ../qtgraphs/src/graphs2d/axis/axisticker.cpp, line 17, as _ZN10AxisTicker17componentCompleteEv
inline void AxisTicker::componentComplete()
{
    QQuickShaderEffect::componentComplete();
    setupShaders();
}

//  from ../qtgraphs/src/graphs2d/axis/axisticker.cpp, line 15, as _ZN10AxisTickerD0Ev
inline AxisTicker::~AxisTicker() {}

//  from ../qtgraphs/src/graphs2d/axis/axisticker.cpp, line 10, as _ZN10AxisTickerC1EP10QQuickItem
inline AxisTicker::AxisTicker(QQuickItem *parent) :
      QQuickShaderEffect(parent)
{
}

//  from ../qtgraphs/src/graphs2d/axis/axisticker.cpp, line 31, as _ZN10AxisTicker12setupShadersEv
inline void AxisTicker::setupShaders()
{
    if (m_isHorizontal) {
        setFragmentShader(QUrl(QStringLiteral("qrc:/shaders/tickershaderhorizontal.frag.qsb")));
        setVertexShader(QUrl(QStringLiteral("qrc:/shaders/tickershaderhorizontal.vert.qsb")));
    } else {
        setFragmentShader(QUrl(QStringLiteral("qrc:/shaders/tickershader.frag.qsb")));
        setVertexShader(QUrl(QStringLiteral("qrc:/shaders/tickershader.vert.qsb")));
    }
}

//  from ../qtgraphs/src/graphs2d/axis/axisticker.cpp, line 42, as _ZNK10AxisTicker11iResolutionEv
inline QVector3D AxisTicker::iResolution() const
{
    return m_iResolution;
}

//  from ../qtgraphs/src/graphs2d/axis/axisticker.cpp, line 47, as _ZNK10AxisTicker9smoothingEv
inline qreal AxisTicker::smoothing() const
{
    return m_smoothing;
}

//  from ../qtgraphs/src/graphs2d/axis/axisticker.cpp, line 52, as _ZN10AxisTicker12setSmoothingEd
inline void AxisTicker::setSmoothing(qreal newSmoothing)
{
    if (QtPrivate::fuzzyCompare(m_smoothing, newSmoothing))
        return;
    m_smoothing = newSmoothing;
    emit smoothingChanged();
}

//  from ../qtgraphs/src/graphs2d/axis/axisticker.cpp, line 60, as _ZNK10AxisTicker5origoEv
inline int AxisTicker::origo() const
{
    return m_origo;
}

//  from ../qtgraphs/src/graphs2d/axis/axisticker.cpp, line 65, as _ZN10AxisTicker8setOrigoEi
inline void AxisTicker::setOrigo(int newOrigo)
{
    if (m_origo == newOrigo)
        return;
    m_origo = newOrigo;
    emit origoChanged();
}

//  from ../qtgraphs/src/graphs2d/axis/axisticker.cpp, line 73, as _ZNK10AxisTicker15subTicksVisibleEv
inline bool AxisTicker::subTicksVisible() const
{
    return m_subTicksVisible;
}

//  from ../qtgraphs/src/graphs2d/axis/axisticker.cpp, line 78, as _ZN10AxisTicker18setSubTicksVisibleEb
inline void AxisTicker::setSubTicksVisible(bool newSubTicksVisible)
{
    if (m_subTicksVisible == newSubTicksVisible)
        return;
    m_subTicksVisible = newSubTicksVisible;
    emit subTicksVisibleChanged();
}

//  from ../qtgraphs/src/graphs2d/axis/axisticker.cpp, line 86, as _ZNK10AxisTicker7spacingEv
inline qreal AxisTicker::spacing() const
{
    return m_spacing;
}

//  from ../qtgraphs/src/graphs2d/axis/axisticker.cpp, line 91, as _ZN10AxisTicker10setSpacingEd
inline void AxisTicker::setSpacing(qreal newSpacing)
{
    if (QtPrivate::fuzzyCompare(m_spacing, newSpacing))
        return;
    m_spacing = newSpacing;
    emit spacingChanged();
}

//  from ../qtgraphs/src/graphs2d/axis/axisticker.cpp, line 99, as _ZNK10AxisTicker12displacementEv
inline qreal AxisTicker::displacement() const
{
    return m_displacement;
}

//  from ../qtgraphs/src/graphs2d/axis/axisticker.cpp, line 104, as _ZN10AxisTicker15setDisplacementEd
inline void AxisTicker::setDisplacement(qreal newDisplacement)
{
    if (QtPrivate::fuzzyCompare(m_displacement, newDisplacement))
        return;
    m_displacement = newDisplacement;
    emit displacementChanged();
}

//  from ../qtgraphs/src/graphs2d/axis/axisticker.cpp, line 112, as _ZNK10AxisTicker12subTickColorEv
inline QColor AxisTicker::subTickColor() const
{
    return m_subTickColor;
}

//  from ../qtgraphs/src/graphs2d/axis/axisticker.cpp, line 117, as _ZN10AxisTicker15setSubTickColorE6QColor
inline void AxisTicker::setSubTickColor(QColor newSubTickColor)
{
    if (m_subTickColor == newSubTickColor)
        return;
    m_subTickColor = newSubTickColor;
    emit subTickColorChanged();
}

//  from ../qtgraphs/src/graphs2d/axis/axisticker.cpp, line 125, as _ZNK10AxisTicker9tickColorEv
inline QColor AxisTicker::tickColor() const
{
    return m_tickColor;
}

//  from ../qtgraphs/src/graphs2d/axis/axisticker.cpp, line 130, as _ZN10AxisTicker12setTickColorE6QColor
inline void AxisTicker::setTickColor(QColor newTickColor)
{
    if (m_tickColor == newTickColor)
        return;
    m_tickColor = newTickColor;
    emit tickColorChanged();
}

//  from ../qtgraphs/src/graphs2d/axis/axisticker.cpp, line 138, as _ZNK10AxisTicker16subTickLineWidthEv
inline qreal AxisTicker::subTickLineWidth() const
{
    return m_subTickLineWidth;
}

//  from ../qtgraphs/src/graphs2d/axis/axisticker.cpp, line 143, as _ZN10AxisTicker19setSubTickLineWidthEd
inline void AxisTicker::setSubTickLineWidth(qreal newSubTickLineWidth)
{
    if (QtPrivate::fuzzyCompare(m_subTickLineWidth, newSubTickLineWidth))
        return;
    m_subTickLineWidth = newSubTickLineWidth;
    emit subTickLineWidthChanged();
}

//  from ../qtgraphs/src/graphs2d/axis/axisticker.cpp, line 151, as _ZNK10AxisTicker13tickLineWidthEv
inline qreal AxisTicker::tickLineWidth() const
{
    return m_tickLineWidth;
}

//  from ../qtgraphs/src/graphs2d/axis/axisticker.cpp, line 156, as _ZN10AxisTicker16setTickLineWidthEd
inline void AxisTicker::setTickLineWidth(qreal newTickLineWidth)
{
    if (QtPrivate::fuzzyCompare(m_tickLineWidth, newTickLineWidth))
        return;
    m_tickLineWidth = newTickLineWidth;
    emit tickLineWidthChanged();
}

//  from ../qtgraphs/src/graphs2d/axis/axisticker.cpp, line 164, as _ZNK10AxisTicker12subTickScaleEv
inline qreal AxisTicker::subTickScale() const
{
    return m_subTickScale;
}

//  from ../qtgraphs/src/graphs2d/axis/axisticker.cpp, line 169, as _ZN10AxisTicker15setSubTickScaleEd
inline void AxisTicker::setSubTickScale(qreal newSubTickScale)
{
    if (QtPrivate::fuzzyCompare(m_subTickScale, newSubTickScale))
        return;
    m_subTickScale = newSubTickScale;
    emit subTickScaleChanged();
}

//  from ../qtgraphs/src/graphs2d/axis/axisticker.cpp, line 177, as _ZNK10AxisTicker13subTickLengthEv
inline qreal AxisTicker::subTickLength() const
{
    return m_subTickLength;
}

//  from ../qtgraphs/src/graphs2d/axis/axisticker.cpp, line 182, as _ZN10AxisTicker16setSubTickLengthEd
inline void AxisTicker::setSubTickLength(qreal newSubTickLength)
{
    if (QtPrivate::fuzzyCompare(m_subTickLength, newSubTickLength))
        return;
    m_subTickLength = newSubTickLength;
    emit subTickLengthChanged();
}

//  from ../qtgraphs/src/graphs2d/axis/axisticker.cpp, line 190, as _ZNK10AxisTicker12isHorizontalEv
inline bool AxisTicker::isHorizontal() const
{
    return m_isHorizontal;
}

//  from ../qtgraphs/src/graphs2d/axis/axisticker.cpp, line 195, as _ZN10AxisTicker15setIsHorizontalEb
inline void AxisTicker::setIsHorizontal(bool newIsHorizontal)
{
    if (m_isHorizontal == newIsHorizontal)
        return;
    m_isHorizontal = newIsHorizontal;
    setupShaders();
    emit isHorizontalChanged();
}

//  from ../qtgraphs/src/graphs2d/axis/axisticker.cpp, line 204, as _ZNK10AxisTicker9isFlippedEv
inline bool AxisTicker::isFlipped() const
{
    return m_flipped;
}

//  from ../qtgraphs/src/graphs2d/axis/axisticker.cpp, line 209, as _ZN10AxisTicker10setFlippedEb
inline void AxisTicker::setFlipped(bool newFlipped)
{
    if (m_flipped == newFlipped)
        return;
    m_flipped = newFlipped;
    emit flippedChanged();
}

//  from ../qtgraphs/src/graphs2d/axis/axisticker.cpp, line 217, as _ZNK10AxisTicker13isLogarithmicEv
inline bool AxisTicker::isLogarithmic() const
{
    return m_isLogarithmic;
}

//  from ../qtgraphs/src/graphs2d/axis/axisticker.cpp, line 222, as _ZN10AxisTicker14setLogarithmicEb
inline void AxisTicker::setLogarithmic(bool newLogarithmic)
{
    if (m_isLogarithmic == newLogarithmic)
        return;

    m_isLogarithmic = newLogarithmic;
    emit logarithmicChanged();
}

//  from ../qtgraphs/src/graphs2d/axis/axisticker.cpp, line 231, as _ZNK10AxisTicker4baseEv
inline qreal AxisTicker::base() const
{
    return m_base;
}

//  from ../qtgraphs/src/graphs2d/axis/axisticker.cpp, line 236, as _ZN10AxisTicker7setBaseEd
inline void AxisTicker::setBase(qreal newBase)
{
    if (qFuzzyCompare(m_base, newBase))
        return;

    m_base = newBase;
    emit baseChanged();
}
//  -----------------------------------------------------------------------

//  Only a class built on AxisTicker may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnAxisTicker : AxisTicker {
  using AxisTicker::componentComplete;
  using AxisTicker::geometryChange;
};

//  A AxisTicker that Python can take functions over in. Every AxisTicker
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteAxisTickerCall0)(const void *, int *);
typedef void (*CuteAxisTickerCall1)(const void *, const QRectF *, const QRectF *, int *);
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(quick_shadereffect)
typedef bool (*CuteAxisTickerCall2)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(quick_shadereffect)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(quick_shadereffect)
typedef void * (*CuteAxisTickerCall3)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
#endif  // QT_CONFIG(quick_shadereffect)
#if QT_CONFIG(quick_shadereffect)
typedef void (*CuteAxisTickerCall4)(const void *, int, const QQuickItem::ItemChangeData *, int *);
#endif  // QT_CONFIG(quick_shadereffect)
typedef const QRectF * (*CuteAxisTickerCall5)(const void *, int *);
typedef const QRectF * (*CuteAxisTickerCall6)(const void *, int *);
typedef bool (*CuteAxisTickerCall7)(const void *, const QPointF *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteAxisTickerCall8)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef bool (*CuteAxisTickerCall9)(const void *, int *);
typedef void * (*CuteAxisTickerCall10)(const void *, int *);
typedef void (*CuteAxisTickerCall11)(const void *, int *);
typedef void (*CuteAxisTickerCall12)(const void *, QKeyEvent *, int *);
typedef void (*CuteAxisTickerCall13)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteAxisTickerCall14)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteAxisTickerCall15)(const void *, QFocusEvent *, int *);
typedef void (*CuteAxisTickerCall16)(const void *, QFocusEvent *, int *);
typedef void (*CuteAxisTickerCall17)(const void *, QMouseEvent *, int *);
typedef void (*CuteAxisTickerCall18)(const void *, QMouseEvent *, int *);
typedef void (*CuteAxisTickerCall19)(const void *, QMouseEvent *, int *);
typedef void (*CuteAxisTickerCall20)(const void *, QMouseEvent *, int *);
typedef void (*CuteAxisTickerCall21)(const void *, int *);
typedef void (*CuteAxisTickerCall22)(const void *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteAxisTickerCall23)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteAxisTickerCall24)(const void *, QTouchEvent *, int *);
typedef void (*CuteAxisTickerCall25)(const void *, QHoverEvent *, int *);
typedef void (*CuteAxisTickerCall26)(const void *, QHoverEvent *, int *);
typedef void (*CuteAxisTickerCall27)(const void *, QHoverEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteAxisTickerCall28)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteAxisTickerCall29)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteAxisTickerCall30)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteAxisTickerCall31)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef bool (*CuteAxisTickerCall32)(const void *, QQuickItem *, QEvent *, int *);
typedef void (*CuteAxisTickerCall33)(const void *, int *);
typedef void (*CuteAxisTickerCall34)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteAxisTickerCall35)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteAxisTickerCall36)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteAxisTickerCall37)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteAxisTickerCall38)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteAxisTickerCall39)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteAxisTickerCall40)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteAxisTicker : public AxisTicker {
public:
  using AxisTicker::AxisTicker;
  void *taken[41] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14geometryChangeERK6QRectFS2_")) {
      taken[1] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(quick_shadereffect)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_shadereffect)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(quick_shadereffect)
    if (!std::strcmp(key, "_ZN10QQuickItem15updatePaintNodeEP7QSGNodePNS_19UpdatePaintNodeDataE")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_shadereffect)
#if QT_CONFIG(quick_shadereffect)
    if (!std::strcmp(key, "_ZN10QQuickItem10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_shadereffect)
    if (!std::strcmp(key, "_ZNK10QQuickItem12boundingRectEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8clipRectEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8containsERK7QPointF")) {
      taken[7] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem17isTextureProviderEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem15textureProviderEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13keyPressEventEP9QKeyEvent")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15keyReleaseEventEP9QKeyEvent")) {
      taken[13] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem16inputMethodEventEP17QInputMethodEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem12focusInEventEP11QFocusEvent")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13focusOutEventEP11QFocusEvent")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15mousePressEventEP11QMouseEvent")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14mouseMoveEventEP11QMouseEvent")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem17mouseReleaseEventEP11QMouseEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16mouseUngrabEventEv")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16touchUngrabEventEv")) {
      taken[22] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10wheelEventEP11QWheelEvent")) {
      taken[23] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10touchEventEP11QTouchEvent")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverEnterEventEP11QHoverEvent")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14hoverMoveEventEP11QHoverEvent")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverLeaveEventEP11QHoverEvent")) {
      taken[27] = call;
      return true;
    }
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem14dragEnterEventEP15QDragEnterEvent")) {
      taken[28] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem13dragMoveEventEP14QDragMoveEvent")) {
      taken[29] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[30] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem9dropEventEP10QDropEvent")) {
      taken[31] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem21childMouseEventFilterEPS_P6QEvent")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16releaseResourcesEv")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem12updatePolishEv")) {
      taken[34] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[35] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[36] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[37] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[38] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[39] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[40] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void AxisTicker::componentComplete()
  void componentComplete() override {
    if (taken[0]) {
      int handled = 0;
      CuteAxisTickerCall0 call = reinterpret_cast<CuteAxisTickerCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    AxisTicker::componentComplete();
  }

  //  void AxisTicker::geometryChange(const QRectF &newGeometry, const
  //      QRectF &oldGeometry)
  void geometryChange(
      const QRectF &newGeometry,
      const QRectF &oldGeometry) override {
    if (taken[1]) {
      int handled = 0;
      CuteAxisTickerCall1 call = reinterpret_cast<CuteAxisTickerCall1>(taken[1]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    AxisTicker::geometryChange(newGeometry, oldGeometry);
  }

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(quick_shadereffect)
  //  bool QQuickShaderEffect::event(QEvent *e)
  bool event(QEvent *e) override {
    if (taken[2]) {
      int handled = 0;
      CuteAxisTickerCall2 call = reinterpret_cast<CuteAxisTickerCall2>(taken[2]);
      bool given = call(this, e, &handled);
      if (handled) return given;
    }
    return QQuickShaderEffect::event(e);
  }
#endif  // QT_CONFIG(quick_shadereffect)
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(quick_shadereffect)
  //  QSGNode *QQuickShaderEffect::updatePaintNode(QSGNode *oldNode,
  //      UpdatePaintNodeData *updatePaintNodeData)
  QSGNode *updatePaintNode(
      QSGNode *oldNode,
      QQuickItem::UpdatePaintNodeData *updatePaintNodeData) override {
    if (taken[3]) {
      int handled = 0;
      CuteAxisTickerCall3 call = reinterpret_cast<CuteAxisTickerCall3>(taken[3]);
      void * given = call(this, oldNode, updatePaintNodeData, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QQuickShaderEffect::updatePaintNode(oldNode, updatePaintNodeData);
  }
#endif  // QT_CONFIG(quick_shadereffect)

#if QT_CONFIG(quick_shadereffect)
  //  void QQuickShaderEffect::itemChange(ItemChange change, const
  //      ItemChangeData &value)
  void itemChange(
      QQuickItem::ItemChange change,
      const QQuickItem::ItemChangeData &value) override {
    if (taken[4]) {
      int handled = 0;
      CuteAxisTickerCall4 call = reinterpret_cast<CuteAxisTickerCall4>(taken[4]);
      call(this, static_cast<int>(change), &value, &handled);
      if (handled) return;
    }
    QQuickShaderEffect::itemChange(change, value);
  }
#endif  // QT_CONFIG(quick_shadereffect)

  //  QRectF QQuickItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[5]) {
      int handled = 0;
      CuteAxisTickerCall5 call = reinterpret_cast<CuteAxisTickerCall5>(taken[5]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::boundingRect();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[6]) {
      int handled = 0;
      CuteAxisTickerCall6 call = reinterpret_cast<CuteAxisTickerCall6>(taken[6]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::clipRect();
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[7]) {
      int handled = 0;
      CuteAxisTickerCall7 call = reinterpret_cast<CuteAxisTickerCall7>(taken[7]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QQuickItem::contains(point);
  }

#if QT_CONFIG(im)
  //  QVariant QQuickItem::inputMethodQuery(Qt::InputMethodQuery query)
  //      const
  QVariant inputMethodQuery(Qt::InputMethodQuery query) const override {
    if (taken[8]) {
      int handled = 0;
      CuteAxisTickerCall8 call = reinterpret_cast<CuteAxisTickerCall8>(taken[8]);
      const QVariant * given = call(this, static_cast<int>(query), &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::inputMethodQuery(query);
  }
#endif  // QT_CONFIG(im)

  //  bool QQuickItem::isTextureProvider() const
  bool isTextureProvider() const override {
    if (taken[9]) {
      int handled = 0;
      CuteAxisTickerCall9 call = reinterpret_cast<CuteAxisTickerCall9>(taken[9]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[10]) {
      int handled = 0;
      CuteAxisTickerCall10 call = reinterpret_cast<CuteAxisTickerCall10>(taken[10]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTextureProvider *>(given);
    }
    return QQuickItem::textureProvider();
  }

  //  void QQuickItem::classBegin()
  void classBegin() override {
    if (taken[11]) {
      int handled = 0;
      CuteAxisTickerCall11 call = reinterpret_cast<CuteAxisTickerCall11>(taken[11]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::classBegin();
  }

  //  void QQuickItem::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteAxisTickerCall12 call = reinterpret_cast<CuteAxisTickerCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyPressEvent(event);
  }

  //  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteAxisTickerCall13 call = reinterpret_cast<CuteAxisTickerCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyReleaseEvent(event);
  }

#if QT_CONFIG(im)
  //  void QQuickItem::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[14]) {
      int handled = 0;
      CuteAxisTickerCall14 call = reinterpret_cast<CuteAxisTickerCall14>(taken[14]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::inputMethodEvent(a0);
  }
#endif  // QT_CONFIG(im)

  //  void QQuickItem::focusInEvent(QFocusEvent *a0)
  void focusInEvent(QFocusEvent *a0) override {
    if (taken[15]) {
      int handled = 0;
      CuteAxisTickerCall15 call = reinterpret_cast<CuteAxisTickerCall15>(taken[15]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusInEvent(a0);
  }

  //  void QQuickItem::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[16]) {
      int handled = 0;
      CuteAxisTickerCall16 call = reinterpret_cast<CuteAxisTickerCall16>(taken[16]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusOutEvent(a0);
  }

  //  void QQuickItem::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteAxisTickerCall17 call = reinterpret_cast<CuteAxisTickerCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mousePressEvent(event);
  }

  //  void QQuickItem::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteAxisTickerCall18 call = reinterpret_cast<CuteAxisTickerCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseMoveEvent(event);
  }

  //  void QQuickItem::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteAxisTickerCall19 call = reinterpret_cast<CuteAxisTickerCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseReleaseEvent(event);
  }

  //  void QQuickItem::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteAxisTickerCall20 call = reinterpret_cast<CuteAxisTickerCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseDoubleClickEvent(event);
  }

  //  void QQuickItem::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[21]) {
      int handled = 0;
      CuteAxisTickerCall21 call = reinterpret_cast<CuteAxisTickerCall21>(taken[21]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::mouseUngrabEvent();
  }

  //  void QQuickItem::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[22]) {
      int handled = 0;
      CuteAxisTickerCall22 call = reinterpret_cast<CuteAxisTickerCall22>(taken[22]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::touchUngrabEvent();
  }

#if QT_CONFIG(wheelevent)
  //  void QQuickItem::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteAxisTickerCall23 call = reinterpret_cast<CuteAxisTickerCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QQuickItem::touchEvent(QTouchEvent *event)
  void touchEvent(QTouchEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteAxisTickerCall24 call = reinterpret_cast<CuteAxisTickerCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::touchEvent(event);
  }

  //  void QQuickItem::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteAxisTickerCall25 call = reinterpret_cast<CuteAxisTickerCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverEnterEvent(event);
  }

  //  void QQuickItem::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteAxisTickerCall26 call = reinterpret_cast<CuteAxisTickerCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverMoveEvent(event);
  }

  //  void QQuickItem::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteAxisTickerCall27 call = reinterpret_cast<CuteAxisTickerCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverLeaveEvent(event);
  }

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragEnterEvent(QDragEnterEvent *a0)
  void dragEnterEvent(QDragEnterEvent *a0) override {
    if (taken[28]) {
      int handled = 0;
      CuteAxisTickerCall28 call = reinterpret_cast<CuteAxisTickerCall28>(taken[28]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragEnterEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragMoveEvent(QDragMoveEvent *a0)
  void dragMoveEvent(QDragMoveEvent *a0) override {
    if (taken[29]) {
      int handled = 0;
      CuteAxisTickerCall29 call = reinterpret_cast<CuteAxisTickerCall29>(taken[29]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragMoveEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragLeaveEvent(QDragLeaveEvent *a0)
  void dragLeaveEvent(QDragLeaveEvent *a0) override {
    if (taken[30]) {
      int handled = 0;
      CuteAxisTickerCall30 call = reinterpret_cast<CuteAxisTickerCall30>(taken[30]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragLeaveEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dropEvent(QDropEvent *a0)
  void dropEvent(QDropEvent *a0) override {
    if (taken[31]) {
      int handled = 0;
      CuteAxisTickerCall31 call = reinterpret_cast<CuteAxisTickerCall31>(taken[31]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dropEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

  //  bool QQuickItem::childMouseEventFilter(QQuickItem *a0, QEvent *a1)
  bool childMouseEventFilter(QQuickItem *a0, QEvent *a1) override {
    if (taken[32]) {
      int handled = 0;
      CuteAxisTickerCall32 call = reinterpret_cast<CuteAxisTickerCall32>(taken[32]);
      bool given = call(this, a0, a1, &handled);
      if (handled) return given;
    }
    return QQuickItem::childMouseEventFilter(a0, a1);
  }

  //  void QQuickItem::releaseResources()
  void releaseResources() override {
    if (taken[33]) {
      int handled = 0;
      CuteAxisTickerCall33 call = reinterpret_cast<CuteAxisTickerCall33>(taken[33]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::releaseResources();
  }

  //  void QQuickItem::updatePolish()
  void updatePolish() override {
    if (taken[34]) {
      int handled = 0;
      CuteAxisTickerCall34 call = reinterpret_cast<CuteAxisTickerCall34>(taken[34]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::updatePolish();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[35]) {
      int handled = 0;
      CuteAxisTickerCall35 call = reinterpret_cast<CuteAxisTickerCall35>(taken[35]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[36]) {
      int handled = 0;
      CuteAxisTickerCall36 call = reinterpret_cast<CuteAxisTickerCall36>(taken[36]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[37]) {
      int handled = 0;
      CuteAxisTickerCall37 call = reinterpret_cast<CuteAxisTickerCall37>(taken[37]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[38]) {
      int handled = 0;
      CuteAxisTickerCall38 call = reinterpret_cast<CuteAxisTickerCall38>(taken[38]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[39]) {
      int handled = 0;
      CuteAxisTickerCall39 call = reinterpret_cast<CuteAxisTickerCall39>(taken[39]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[40]) {
      int handled = 0;
      CuteAxisTickerCall40 call = reinterpret_cast<CuteAxisTickerCall40>(taken[40]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *AxisTicker::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10AxisTicker10metaObjectEv(
    const AxisTicker *self) {
  return self->metaObject();
}

//  void *AxisTicker::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10AxisTicker11qt_metacastEPKc(
    AxisTicker *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int AxisTicker::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10AxisTicker11qt_metacallEN11QMetaObject4CallEiPPv(
    AxisTicker *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString AxisTicker::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10AxisTicker2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(AxisTicker::tr(s, c, n));
}

//  AxisTicker::AxisTicker(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
AxisTicker *ritual_ZN10AxisTickerC1EP10QQuickItem(QQuickItem *parent) {
  return new CuteAxisTicker(parent);
}

//  AxisTicker::~AxisTicker()
extern "C" Q_DECL_EXPORT
void ritual_ZN10AxisTickerD1Ev(AxisTicker *self) {
  delete self;
}

//  void AxisTicker::setupShaders()
extern "C" Q_DECL_EXPORT
void ritual_ZN10AxisTicker12setupShadersEv(AxisTicker *self) {
  self->setupShaders();
}

//  QVector3D AxisTicker::iResolution() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK10AxisTicker11iResolutionEv(const AxisTicker *self) {
  return new QVector3D(self->iResolution());
}

//  qreal AxisTicker::smoothing() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK10AxisTicker9smoothingEv(const AxisTicker *self) {
  return self->smoothing();
}

//  void AxisTicker::setSmoothing(qreal newSmoothing)
extern "C" Q_DECL_EXPORT
void ritual_ZN10AxisTicker12setSmoothingEd(
    AxisTicker *self,
    qreal newSmoothing) {
  self->setSmoothing(newSmoothing);
}

//  int AxisTicker::origo() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10AxisTicker5origoEv(const AxisTicker *self) {
  return self->origo();
}

//  void AxisTicker::setOrigo(int newOrigo)
extern "C" Q_DECL_EXPORT
void ritual_ZN10AxisTicker8setOrigoEi(AxisTicker *self, int newOrigo) {
  self->setOrigo(newOrigo);
}

//  bool AxisTicker::subTicksVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10AxisTicker15subTicksVisibleEv(const AxisTicker *self) {
  return self->subTicksVisible();
}

//  void AxisTicker::setSubTicksVisible(bool newSubTicksVisible)
extern "C" Q_DECL_EXPORT
void ritual_ZN10AxisTicker18setSubTicksVisibleEb(
    AxisTicker *self,
    bool newSubTicksVisible) {
  self->setSubTicksVisible(newSubTicksVisible);
}

//  qreal AxisTicker::spacing() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK10AxisTicker7spacingEv(const AxisTicker *self) {
  return self->spacing();
}

//  void AxisTicker::setSpacing(qreal newSpacing)
extern "C" Q_DECL_EXPORT
void ritual_ZN10AxisTicker10setSpacingEd(
    AxisTicker *self,
    qreal newSpacing) {
  self->setSpacing(newSpacing);
}

//  qreal AxisTicker::displacement() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK10AxisTicker12displacementEv(const AxisTicker *self) {
  return self->displacement();
}

//  void AxisTicker::setDisplacement(qreal newDisplacement)
extern "C" Q_DECL_EXPORT
void ritual_ZN10AxisTicker15setDisplacementEd(
    AxisTicker *self,
    qreal newDisplacement) {
  self->setDisplacement(newDisplacement);
}

//  QColor AxisTicker::subTickColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK10AxisTicker12subTickColorEv(const AxisTicker *self) {
  return new QColor(self->subTickColor());
}

//  void AxisTicker::setSubTickColor(QColor newSubTickColor)
extern "C" Q_DECL_EXPORT
void ritual_ZN10AxisTicker15setSubTickColorE6QColor(
    AxisTicker *self,
    const QColor *newSubTickColor) {
  self->setSubTickColor(*newSubTickColor);
}

//  QColor AxisTicker::tickColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK10AxisTicker9tickColorEv(const AxisTicker *self) {
  return new QColor(self->tickColor());
}

//  void AxisTicker::setTickColor(QColor newTickColor)
extern "C" Q_DECL_EXPORT
void ritual_ZN10AxisTicker12setTickColorE6QColor(
    AxisTicker *self,
    const QColor *newTickColor) {
  self->setTickColor(*newTickColor);
}

//  qreal AxisTicker::subTickLineWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK10AxisTicker16subTickLineWidthEv(const AxisTicker *self) {
  return self->subTickLineWidth();
}

//  void AxisTicker::setSubTickLineWidth(qreal newSubTickLineWidth)
extern "C" Q_DECL_EXPORT
void ritual_ZN10AxisTicker19setSubTickLineWidthEd(
    AxisTicker *self,
    qreal newSubTickLineWidth) {
  self->setSubTickLineWidth(newSubTickLineWidth);
}

//  qreal AxisTicker::tickLineWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK10AxisTicker13tickLineWidthEv(const AxisTicker *self) {
  return self->tickLineWidth();
}

//  void AxisTicker::setTickLineWidth(qreal newTickLineWidth)
extern "C" Q_DECL_EXPORT
void ritual_ZN10AxisTicker16setTickLineWidthEd(
    AxisTicker *self,
    qreal newTickLineWidth) {
  self->setTickLineWidth(newTickLineWidth);
}

//  qreal AxisTicker::subTickScale() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK10AxisTicker12subTickScaleEv(const AxisTicker *self) {
  return self->subTickScale();
}

//  void AxisTicker::setSubTickScale(qreal newSubTickScale)
extern "C" Q_DECL_EXPORT
void ritual_ZN10AxisTicker15setSubTickScaleEd(
    AxisTicker *self,
    qreal newSubTickScale) {
  self->setSubTickScale(newSubTickScale);
}

//  qreal AxisTicker::subTickLength() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK10AxisTicker13subTickLengthEv(const AxisTicker *self) {
  return self->subTickLength();
}

//  void AxisTicker::setSubTickLength(qreal newSubTickLength)
extern "C" Q_DECL_EXPORT
void ritual_ZN10AxisTicker16setSubTickLengthEd(
    AxisTicker *self,
    qreal newSubTickLength) {
  self->setSubTickLength(newSubTickLength);
}

//  bool AxisTicker::isHorizontal() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10AxisTicker12isHorizontalEv(const AxisTicker *self) {
  return self->isHorizontal();
}

//  void AxisTicker::setIsHorizontal(bool newIsHorizontal)
extern "C" Q_DECL_EXPORT
void ritual_ZN10AxisTicker15setIsHorizontalEb(
    AxisTicker *self,
    bool newIsHorizontal) {
  self->setIsHorizontal(newIsHorizontal);
}

//  bool AxisTicker::isFlipped() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10AxisTicker9isFlippedEv(const AxisTicker *self) {
  return self->isFlipped();
}

//  void AxisTicker::setFlipped(bool newFlipped)
extern "C" Q_DECL_EXPORT
void ritual_ZN10AxisTicker10setFlippedEb(AxisTicker *self, bool newFlipped) {
  self->setFlipped(newFlipped);
}

//  bool AxisTicker::isLogarithmic() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10AxisTicker13isLogarithmicEv(const AxisTicker *self) {
  return self->isLogarithmic();
}

//  void AxisTicker::setLogarithmic(bool newLogarithmic)
extern "C" Q_DECL_EXPORT
void ritual_ZN10AxisTicker14setLogarithmicEb(
    AxisTicker *self,
    bool newLogarithmic) {
  self->setLogarithmic(newLogarithmic);
}

//  qreal AxisTicker::base() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK10AxisTicker4baseEv(const AxisTicker *self) {
  return self->base();
}

//  void AxisTicker::setBase(qreal newBase)
extern "C" Q_DECL_EXPORT
void ritual_ZN10AxisTicker7setBaseEd(AxisTicker *self, qreal newBase) {
  self->setBase(newBase);
}

//  void AxisTicker::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN10AxisTicker17componentCompleteEv(AxisTicker *self) {
  self->componentComplete();
}

//  void AxisTicker::geometryChange(const QRectF &newGeometry, const QRectF
//      &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_ZN10AxisTicker14geometryChangeERK6QRectFS2_(
    AxisTicker *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  self->geometryChange(*newGeometry, *oldGeometry);
}

//  void AxisTicker::iResolutionChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN10AxisTicker18iResolutionChangedEv(AxisTicker *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "AxisTicker")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "iResolutionChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "iResolutionChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void AxisTicker::smoothingChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN10AxisTicker16smoothingChangedEv(AxisTicker *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "AxisTicker")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "smoothingChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "smoothingChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void AxisTicker::origoChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN10AxisTicker12origoChangedEv(AxisTicker *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "AxisTicker")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "origoChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "origoChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void AxisTicker::subTicksVisibleChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN10AxisTicker22subTicksVisibleChangedEv(AxisTicker *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "AxisTicker")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "subTicksVisibleChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "subTicksVisibleChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void AxisTicker::spacingChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN10AxisTicker14spacingChangedEv(AxisTicker *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "AxisTicker")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "spacingChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "spacingChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void AxisTicker::displacementChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN10AxisTicker19displacementChangedEv(AxisTicker *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "AxisTicker")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "displacementChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "displacementChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void AxisTicker::subTickColorChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN10AxisTicker19subTickColorChangedEv(AxisTicker *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "AxisTicker")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "subTickColorChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "subTickColorChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void AxisTicker::tickColorChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN10AxisTicker16tickColorChangedEv(AxisTicker *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "AxisTicker")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "tickColorChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "tickColorChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void AxisTicker::subTickLineWidthChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN10AxisTicker23subTickLineWidthChangedEv(AxisTicker *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "AxisTicker")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "subTickLineWidthChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "subTickLineWidthChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void AxisTicker::tickLineWidthChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN10AxisTicker20tickLineWidthChangedEv(AxisTicker *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "AxisTicker")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "tickLineWidthChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "tickLineWidthChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void AxisTicker::subTickScaleChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN10AxisTicker19subTickScaleChangedEv(AxisTicker *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "AxisTicker")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "subTickScaleChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "subTickScaleChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void AxisTicker::subTickLengthChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN10AxisTicker20subTickLengthChangedEv(AxisTicker *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "AxisTicker")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "subTickLengthChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "subTickLengthChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void AxisTicker::isHorizontalChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN10AxisTicker19isHorizontalChangedEv(AxisTicker *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "AxisTicker")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "isHorizontalChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "isHorizontalChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void AxisTicker::flippedChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN10AxisTicker14flippedChangedEv(AxisTicker *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "AxisTicker")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "flippedChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "flippedChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void AxisTicker::logarithmicChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN10AxisTicker18logarithmicChangedEv(AxisTicker *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "AxisTicker")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "logarithmicChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "logarithmicChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void AxisTicker::baseChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN10AxisTicker11baseChangedEv(AxisTicker *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "AxisTicker")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "baseChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "baseChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  a Python function taken by a CuteAxisTicker, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_AxisTicker(AxisTicker *self, const char *key, void *call) {
  return static_cast<CuteAxisTicker *>(self)->take(key, call);
}

//  void AxisTicker::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10AxisTicker17componentCompleteEv(AxisTicker *self) {
  static_cast<OwnAxisTicker *>(self)->OwnAxisTicker::componentComplete();
}

//  void AxisTicker::geometryChange(const QRectF &newGeometry, const QRectF
//      &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10AxisTicker14geometryChangeERK6QRectFS2_(
    AxisTicker *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  static_cast<OwnAxisTicker *>(self)->OwnAxisTicker::geometryChange(
      *newGeometry,
      *oldGeometry);
}

#endif  // (QT_CONFIG(graphs_2d)) && (!(!QT_CONFIG(graphs_2d_area) && !QT_CONFIG(graphs_2d_bar) && !QT_CONFIG(graphs_2d_donut_pie) && !QT_CONFIG(graphs_2d_line) && !QT_CONFIG(graphs_2d_scatter) && !QT_CONFIG(graphs_2d_spline) && !QT_CONFIG(graphs_2d_custom)))
