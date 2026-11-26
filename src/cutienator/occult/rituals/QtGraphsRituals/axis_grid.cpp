//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/6.12.0/QtGraphs/private/axisgrid_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for 'AxisGrid' is pasted in,
//  cut from what the moc of Qt 6.12.0 writes for its header: Qt's library
//  keeps it to itself; added are 20 rituals that lean on what moc writes for
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
#include <QtGraphs/6.12.0/QtGraphs/private/axisgrid_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qvectornd.h>
#include <QtCore/qpoint.h>
#include <QtGui/qcolor.h>
#include <QtCore/qrect.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtGraphs/private/axisgrid_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from QtGraphs__AxisGrid.cpp, line 1, as moc:AxisGrid
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN8AxisGridE_t {};
} // unnamed namespace

template <> constexpr inline auto AxisGrid::qt_create_metaobjectdata<qt_meta_tag_ZN8AxisGridE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "AxisGrid",
        "iResolutionChanged",
        "",
        "smoothingChanged",
        "origoChanged",
        "gridVisibilityChanged",
        "gridWidthChanged",
        "gridHeightChanged",
        "gridMovementChanged",
        "subGridColorChanged",
        "gridColorChanged",
        "plotAreaBackgroundColorChanged",
        "subGridLineWidthChanged",
        "gridLineWidthChanged",
        "verticalSubGridScaleChanged",
        "horizontalSubGridScaleChanged",
        "verticalLogarithmicChanged",
        "logarithmic",
        "horizontalLogarithmicChanged",
        "verticalBaseChanged",
        "base",
        "horizontalBaseChanged",
        "iResolution",
        "QVector3D",
        "smoothing",
        "origo",
        "gridVisibility",
        "QVector4D",
        "gridWidth",
        "gridHeight",
        "gridMovement",
        "QPointF",
        "subGridColor",
        "QColor",
        "gridColor",
        "plotAreaBackgroundColor",
        "subGridLineWidth",
        "gridLineWidth",
        "verticalSubGridScale",
        "horizontalSubGridScale",
        "verticalLogarithmic",
        "horizontalLogarithmic",
        "verticalBase",
        "horizontalBase"
    };

    QtMocHelpers::UintData qt_methods {
        // Signal 'iResolutionChanged'
        QtMocHelpers::SignalData<void()>(1, 2, QMC::AccessPublic, QMetaType::Void),
        // Signal 'smoothingChanged'
        QtMocHelpers::SignalData<void()>(3, 2, QMC::AccessPublic, QMetaType::Void),
        // Signal 'origoChanged'
        QtMocHelpers::SignalData<void()>(4, 2, QMC::AccessPublic, QMetaType::Void),
        // Signal 'gridVisibilityChanged'
        QtMocHelpers::SignalData<void()>(5, 2, QMC::AccessPublic, QMetaType::Void),
        // Signal 'gridWidthChanged'
        QtMocHelpers::SignalData<void()>(6, 2, QMC::AccessPublic, QMetaType::Void),
        // Signal 'gridHeightChanged'
        QtMocHelpers::SignalData<void()>(7, 2, QMC::AccessPublic, QMetaType::Void),
        // Signal 'gridMovementChanged'
        QtMocHelpers::SignalData<void()>(8, 2, QMC::AccessPublic, QMetaType::Void),
        // Signal 'subGridColorChanged'
        QtMocHelpers::SignalData<void()>(9, 2, QMC::AccessPublic, QMetaType::Void),
        // Signal 'gridColorChanged'
        QtMocHelpers::SignalData<void()>(10, 2, QMC::AccessPublic, QMetaType::Void),
        // Signal 'plotAreaBackgroundColorChanged'
        QtMocHelpers::SignalData<void()>(11, 2, QMC::AccessPublic, QMetaType::Void),
        // Signal 'subGridLineWidthChanged'
        QtMocHelpers::SignalData<void()>(12, 2, QMC::AccessPublic, QMetaType::Void),
        // Signal 'gridLineWidthChanged'
        QtMocHelpers::SignalData<void()>(13, 2, QMC::AccessPublic, QMetaType::Void),
        // Signal 'verticalSubGridScaleChanged'
        QtMocHelpers::SignalData<void()>(14, 2, QMC::AccessPublic, QMetaType::Void),
        // Signal 'horizontalSubGridScaleChanged'
        QtMocHelpers::SignalData<void()>(15, 2, QMC::AccessPublic, QMetaType::Void),
        // Signal 'verticalLogarithmicChanged'
        QtMocHelpers::RevisionedSignalData<void(bool)>(16, 2, QMC::AccessPublic, 0x60c, QMetaType::Void, {{
            { QMetaType::Bool, 17 },
        }}),
        // Signal 'horizontalLogarithmicChanged'
        QtMocHelpers::RevisionedSignalData<void(bool)>(18, 2, QMC::AccessPublic, 0x60c, QMetaType::Void, {{
            { QMetaType::Bool, 17 },
        }}),
        // Signal 'verticalBaseChanged'
        QtMocHelpers::RevisionedSignalData<void(qreal)>(19, 2, QMC::AccessPublic, 0x60c, QMetaType::Void, {{
            { QMetaType::QReal, 20 },
        }}),
        // Signal 'horizontalBaseChanged'
        QtMocHelpers::RevisionedSignalData<void(qreal)>(21, 2, QMC::AccessPublic, 0x60c, QMetaType::Void, {{
            { QMetaType::QReal, 20 },
        }}),
    };
    QtMocHelpers::UintData qt_properties {
        // property 'iResolution'
        QtMocHelpers::PropertyData<QVector3D>(22, 0x80000000 | 23, QMC::DefaultPropertyFlags | QMC::EnumOrFlag | QMC::Final, 0),
        // property 'smoothing'
        QtMocHelpers::PropertyData<qreal>(24, QMetaType::QReal, QMC::DefaultPropertyFlags | QMC::Writable | QMC::StdCppSet | QMC::Final, 1),
        // property 'origo'
        QtMocHelpers::PropertyData<int>(25, QMetaType::Int, QMC::DefaultPropertyFlags | QMC::Writable | QMC::StdCppSet | QMC::Final, 2),
        // property 'gridVisibility'
        QtMocHelpers::PropertyData<QVector4D>(26, 0x80000000 | 27, QMC::DefaultPropertyFlags | QMC::Writable | QMC::EnumOrFlag | QMC::StdCppSet | QMC::Final, 3),
        // property 'gridWidth'
        QtMocHelpers::PropertyData<qreal>(28, QMetaType::QReal, QMC::DefaultPropertyFlags | QMC::Writable | QMC::StdCppSet | QMC::Final, 4),
        // property 'gridHeight'
        QtMocHelpers::PropertyData<qreal>(29, QMetaType::QReal, QMC::DefaultPropertyFlags | QMC::Writable | QMC::StdCppSet | QMC::Final, 5),
        // property 'gridMovement'
        QtMocHelpers::PropertyData<QPointF>(30, 0x80000000 | 31, QMC::DefaultPropertyFlags | QMC::Writable | QMC::EnumOrFlag | QMC::StdCppSet | QMC::Final, 6),
        // property 'subGridColor'
        QtMocHelpers::PropertyData<QColor>(32, 0x80000000 | 33, QMC::DefaultPropertyFlags | QMC::Writable | QMC::EnumOrFlag | QMC::StdCppSet | QMC::Final, 7),
        // property 'gridColor'
        QtMocHelpers::PropertyData<QColor>(34, 0x80000000 | 33, QMC::DefaultPropertyFlags | QMC::Writable | QMC::EnumOrFlag | QMC::StdCppSet | QMC::Final, 8),
        // property 'plotAreaBackgroundColor'
        QtMocHelpers::PropertyData<QColor>(35, 0x80000000 | 33, QMC::DefaultPropertyFlags | QMC::Writable | QMC::EnumOrFlag | QMC::StdCppSet | QMC::Final, 9),
        // property 'subGridLineWidth'
        QtMocHelpers::PropertyData<qreal>(36, QMetaType::QReal, QMC::DefaultPropertyFlags | QMC::Writable | QMC::StdCppSet | QMC::Final, 10),
        // property 'gridLineWidth'
        QtMocHelpers::PropertyData<qreal>(37, QMetaType::QReal, QMC::DefaultPropertyFlags | QMC::Writable | QMC::StdCppSet | QMC::Final, 11),
        // property 'verticalSubGridScale'
        QtMocHelpers::PropertyData<qreal>(38, QMetaType::QReal, QMC::DefaultPropertyFlags | QMC::Writable | QMC::StdCppSet | QMC::Final, 12),
        // property 'horizontalSubGridScale'
        QtMocHelpers::PropertyData<qreal>(39, QMetaType::QReal, QMC::DefaultPropertyFlags | QMC::Writable | QMC::StdCppSet | QMC::Final, 13),
        // property 'verticalLogarithmic'
        QtMocHelpers::PropertyData<bool>(40, QMetaType::Bool, QMC::DefaultPropertyFlags | QMC::Writable | QMC::StdCppSet, 14, 0x60c),
        // property 'horizontalLogarithmic'
        QtMocHelpers::PropertyData<bool>(41, QMetaType::Bool, QMC::DefaultPropertyFlags | QMC::Writable | QMC::StdCppSet, 15, 0x60c),
        // property 'verticalBase'
        QtMocHelpers::PropertyData<qreal>(42, QMetaType::QReal, QMC::DefaultPropertyFlags | QMC::Writable | QMC::StdCppSet, 16, 0x60c),
        // property 'horizontalBase'
        QtMocHelpers::PropertyData<qreal>(43, QMetaType::QReal, QMC::DefaultPropertyFlags | QMC::Writable | QMC::StdCppSet, 17, 0x60c),
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<AxisGrid, qt_meta_tag_ZN8AxisGridE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject AxisGrid::staticMetaObject = { {
    QMetaObject::SuperData::link<QQuickShaderEffect::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN8AxisGridE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN8AxisGridE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN8AxisGridE_t>.metaTypes,
    nullptr
} };

void AxisGrid::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<AxisGrid *>(_o);
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: _t->iResolutionChanged(); break;
        case 1: _t->smoothingChanged(); break;
        case 2: _t->origoChanged(); break;
        case 3: _t->gridVisibilityChanged(); break;
        case 4: _t->gridWidthChanged(); break;
        case 5: _t->gridHeightChanged(); break;
        case 6: _t->gridMovementChanged(); break;
        case 7: _t->subGridColorChanged(); break;
        case 8: _t->gridColorChanged(); break;
        case 9: _t->plotAreaBackgroundColorChanged(); break;
        case 10: _t->subGridLineWidthChanged(); break;
        case 11: _t->gridLineWidthChanged(); break;
        case 12: _t->verticalSubGridScaleChanged(); break;
        case 13: _t->horizontalSubGridScaleChanged(); break;
        case 14: _t->verticalLogarithmicChanged((*reinterpret_cast<std::add_pointer_t<bool>>(_a[1]))); break;
        case 15: _t->horizontalLogarithmicChanged((*reinterpret_cast<std::add_pointer_t<bool>>(_a[1]))); break;
        case 16: _t->verticalBaseChanged((*reinterpret_cast<std::add_pointer_t<qreal>>(_a[1]))); break;
        case 17: _t->horizontalBaseChanged((*reinterpret_cast<std::add_pointer_t<qreal>>(_a[1]))); break;
        default: ;
        }
    }
    if (_c == QMetaObject::IndexOfMethod) {
        if (QtMocHelpers::indexOfMethod<void (AxisGrid::*)()>(_a, &AxisGrid::iResolutionChanged, 0))
            return;
        if (QtMocHelpers::indexOfMethod<void (AxisGrid::*)()>(_a, &AxisGrid::smoothingChanged, 1))
            return;
        if (QtMocHelpers::indexOfMethod<void (AxisGrid::*)()>(_a, &AxisGrid::origoChanged, 2))
            return;
        if (QtMocHelpers::indexOfMethod<void (AxisGrid::*)()>(_a, &AxisGrid::gridVisibilityChanged, 3))
            return;
        if (QtMocHelpers::indexOfMethod<void (AxisGrid::*)()>(_a, &AxisGrid::gridWidthChanged, 4))
            return;
        if (QtMocHelpers::indexOfMethod<void (AxisGrid::*)()>(_a, &AxisGrid::gridHeightChanged, 5))
            return;
        if (QtMocHelpers::indexOfMethod<void (AxisGrid::*)()>(_a, &AxisGrid::gridMovementChanged, 6))
            return;
        if (QtMocHelpers::indexOfMethod<void (AxisGrid::*)()>(_a, &AxisGrid::subGridColorChanged, 7))
            return;
        if (QtMocHelpers::indexOfMethod<void (AxisGrid::*)()>(_a, &AxisGrid::gridColorChanged, 8))
            return;
        if (QtMocHelpers::indexOfMethod<void (AxisGrid::*)()>(_a, &AxisGrid::plotAreaBackgroundColorChanged, 9))
            return;
        if (QtMocHelpers::indexOfMethod<void (AxisGrid::*)()>(_a, &AxisGrid::subGridLineWidthChanged, 10))
            return;
        if (QtMocHelpers::indexOfMethod<void (AxisGrid::*)()>(_a, &AxisGrid::gridLineWidthChanged, 11))
            return;
        if (QtMocHelpers::indexOfMethod<void (AxisGrid::*)()>(_a, &AxisGrid::verticalSubGridScaleChanged, 12))
            return;
        if (QtMocHelpers::indexOfMethod<void (AxisGrid::*)()>(_a, &AxisGrid::horizontalSubGridScaleChanged, 13))
            return;
        if (QtMocHelpers::indexOfMethod<void (AxisGrid::*)(bool )>(_a, &AxisGrid::verticalLogarithmicChanged, 14))
            return;
        if (QtMocHelpers::indexOfMethod<void (AxisGrid::*)(bool )>(_a, &AxisGrid::horizontalLogarithmicChanged, 15))
            return;
        if (QtMocHelpers::indexOfMethod<void (AxisGrid::*)(qreal )>(_a, &AxisGrid::verticalBaseChanged, 16))
            return;
        if (QtMocHelpers::indexOfMethod<void (AxisGrid::*)(qreal )>(_a, &AxisGrid::horizontalBaseChanged, 17))
            return;
    }
    if (_c == QMetaObject::ReadProperty) {
        void *_v = _a[0];
        switch (_id) {
        case 0: *reinterpret_cast<QVector3D*>(_v) = _t->iResolution(); break;
        case 1: *reinterpret_cast<qreal*>(_v) = _t->smoothing(); break;
        case 2: *reinterpret_cast<int*>(_v) = _t->origo(); break;
        case 3: *reinterpret_cast<QVector4D*>(_v) = _t->gridVisibility(); break;
        case 4: *reinterpret_cast<qreal*>(_v) = _t->gridWidth(); break;
        case 5: *reinterpret_cast<qreal*>(_v) = _t->gridHeight(); break;
        case 6: *reinterpret_cast<QPointF*>(_v) = _t->gridMovement(); break;
        case 7: *reinterpret_cast<QColor*>(_v) = _t->subGridColor(); break;
        case 8: *reinterpret_cast<QColor*>(_v) = _t->gridColor(); break;
        case 9: *reinterpret_cast<QColor*>(_v) = _t->plotAreaBackgroundColor(); break;
        case 10: *reinterpret_cast<qreal*>(_v) = _t->subGridLineWidth(); break;
        case 11: *reinterpret_cast<qreal*>(_v) = _t->gridLineWidth(); break;
        case 12: *reinterpret_cast<qreal*>(_v) = _t->verticalSubGridScale(); break;
        case 13: *reinterpret_cast<qreal*>(_v) = _t->horizontalSubGridScale(); break;
        case 14: *reinterpret_cast<bool*>(_v) = _t->isVerticalLogarithmic(); break;
        case 15: *reinterpret_cast<bool*>(_v) = _t->isHorizontalLogarithmic(); break;
        case 16: *reinterpret_cast<qreal*>(_v) = _t->verticalBase(); break;
        case 17: *reinterpret_cast<qreal*>(_v) = _t->horizontalBase(); break;
        default: break;
        }
    }
    if (_c == QMetaObject::WriteProperty) {
        void *_v = _a[0];
        switch (_id) {
        case 1: _t->setSmoothing(*reinterpret_cast<qreal*>(_v)); break;
        case 2: _t->setOrigo(*reinterpret_cast<int*>(_v)); break;
        case 3: _t->setGridVisibility(*reinterpret_cast<QVector4D*>(_v)); break;
        case 4: _t->setGridWidth(*reinterpret_cast<qreal*>(_v)); break;
        case 5: _t->setGridHeight(*reinterpret_cast<qreal*>(_v)); break;
        case 6: _t->setGridMovement(*reinterpret_cast<QPointF*>(_v)); break;
        case 7: _t->setSubGridColor(*reinterpret_cast<QColor*>(_v)); break;
        case 8: _t->setGridColor(*reinterpret_cast<QColor*>(_v)); break;
        case 9: _t->setPlotAreaBackgroundColor(*reinterpret_cast<QColor*>(_v)); break;
        case 10: _t->setSubGridLineWidth(*reinterpret_cast<qreal*>(_v)); break;
        case 11: _t->setGridLineWidth(*reinterpret_cast<qreal*>(_v)); break;
        case 12: _t->setVerticalSubGridScale(*reinterpret_cast<qreal*>(_v)); break;
        case 13: _t->setHorizontalSubGridScale(*reinterpret_cast<qreal*>(_v)); break;
        case 14: _t->setVerticalLogarithmic(*reinterpret_cast<bool*>(_v)); break;
        case 15: _t->setHorizontalLogarithmic(*reinterpret_cast<bool*>(_v)); break;
        case 16: _t->setVerticalBase(*reinterpret_cast<qreal*>(_v)); break;
        case 17: _t->setHorizontalBase(*reinterpret_cast<qreal*>(_v)); break;
        default: break;
        }
    }
}

const QMetaObject *AxisGrid::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *AxisGrid::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN8AxisGridE_t>.strings))
        return static_cast<void*>(this);
    return QQuickShaderEffect::qt_metacast(_clname);
}

int AxisGrid::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QQuickShaderEffect::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 18)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 18;
    }
    if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 18)
            *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType();
        _id -= 18;
    }
    if (_c == QMetaObject::ReadProperty || _c == QMetaObject::WriteProperty
            || _c == QMetaObject::ResetProperty || _c == QMetaObject::BindableProperty
            || _c == QMetaObject::RegisterPropertyMetaType) {
        qt_static_metacall(this, _c, _id, _a);
        _id -= 18;
    }
    return _id;
}

// SIGNAL 0
void AxisGrid::iResolutionChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 0, nullptr);
}

// SIGNAL 1
void AxisGrid::smoothingChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 1, nullptr);
}

// SIGNAL 2
void AxisGrid::origoChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 2, nullptr);
}

// SIGNAL 3
void AxisGrid::gridVisibilityChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 3, nullptr);
}

// SIGNAL 4
void AxisGrid::gridWidthChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 4, nullptr);
}

// SIGNAL 5
void AxisGrid::gridHeightChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 5, nullptr);
}

// SIGNAL 6
void AxisGrid::gridMovementChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 6, nullptr);
}

// SIGNAL 7
void AxisGrid::subGridColorChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 7, nullptr);
}

// SIGNAL 8
void AxisGrid::gridColorChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 8, nullptr);
}

// SIGNAL 9
void AxisGrid::plotAreaBackgroundColorChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 9, nullptr);
}

// SIGNAL 10
void AxisGrid::subGridLineWidthChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 10, nullptr);
}

// SIGNAL 11
void AxisGrid::gridLineWidthChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 11, nullptr);
}

// SIGNAL 12
void AxisGrid::verticalSubGridScaleChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 12, nullptr);
}

// SIGNAL 13
void AxisGrid::horizontalSubGridScaleChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 13, nullptr);
}

// SIGNAL 14
void AxisGrid::verticalLogarithmicChanged(bool _t1)
{
    QMetaObject::activate<void>(this, &staticMetaObject, 14, nullptr, _t1);
}

// SIGNAL 15
void AxisGrid::horizontalLogarithmicChanged(bool _t1)
{
    QMetaObject::activate<void>(this, &staticMetaObject, 15, nullptr, _t1);
}

// SIGNAL 16
void AxisGrid::verticalBaseChanged(qreal _t1)
{
    QMetaObject::activate<void>(this, &staticMetaObject, 16, nullptr, _t1);
}

// SIGNAL 17
void AxisGrid::horizontalBaseChanged(qreal _t1)
{
    QMetaObject::activate<void>(this, &staticMetaObject, 17, nullptr, _t1);
}
QT_WARNING_POP

//  from ../qtgraphs/src/graphs2d/axis/axisgrid.cpp, line 23, as _ZN8AxisGrid14geometryChangeERK6QRectFS2_
inline void AxisGrid::geometryChange(const QRectF &newGeometry, const QRectF &oldGeometry)
{
    m_iResolution = QVector3D(newGeometry.width(), newGeometry.height(), 1.0);
    emit iResolutionChanged();

    QQuickShaderEffect::geometryChange(newGeometry, oldGeometry);
}

//  from ../qtgraphs/src/graphs2d/axis/axisgrid.cpp, line 17, as _ZN8AxisGrid17componentCompleteEv
inline void AxisGrid::componentComplete()
{
    QQuickShaderEffect::componentComplete();
    setupShaders();
}

//  from ../qtgraphs/src/graphs2d/axis/axisgrid.cpp, line 15, as _ZN8AxisGridD0Ev
inline AxisGrid::~AxisGrid() {}

//  from ../qtgraphs/src/graphs2d/axis/axisgrid.cpp, line 10, as _ZN8AxisGridC1EP10QQuickItem
inline AxisGrid::AxisGrid(QQuickItem *parent) :
      QQuickShaderEffect(parent)
{
}

//  from ../qtgraphs/src/graphs2d/axis/axisgrid.cpp, line 31, as _ZN8AxisGrid12setupShadersEv
inline void AxisGrid::setupShaders()
{
    setFragmentShader(QUrl(QStringLiteral("qrc:/shaders/gridshader.frag.qsb")));
    setVertexShader(QUrl(QStringLiteral("qrc:/shaders/gridshader.vert.qsb")));
}

//  from ../qtgraphs/src/graphs2d/axis/axisgrid.cpp, line 37, as _ZNK8AxisGrid11iResolutionEv
inline QVector3D AxisGrid::iResolution() const
{
    return m_iResolution;
}

//  from ../qtgraphs/src/graphs2d/axis/axisgrid.cpp, line 42, as _ZNK8AxisGrid9smoothingEv
inline qreal AxisGrid::smoothing() const
{
    return m_smoothing;
}

//  from ../qtgraphs/src/graphs2d/axis/axisgrid.cpp, line 47, as _ZN8AxisGrid12setSmoothingEd
inline void AxisGrid::setSmoothing(qreal newSmoothing)
{
    if (QtPrivate::fuzzyCompare(m_smoothing, newSmoothing))
        return;
    m_smoothing = newSmoothing;
    emit smoothingChanged();
}

//  from ../qtgraphs/src/graphs2d/axis/axisgrid.cpp, line 55, as _ZNK8AxisGrid5origoEv
inline int AxisGrid::origo() const
{
    return m_origo;
}

//  from ../qtgraphs/src/graphs2d/axis/axisgrid.cpp, line 60, as _ZN8AxisGrid8setOrigoEi
inline void AxisGrid::setOrigo(int newOrigo)
{
    if (m_origo == newOrigo)
        return;
    m_origo = newOrigo;
    emit origoChanged();
}

//  from ../qtgraphs/src/graphs2d/axis/axisgrid.cpp, line 68, as _ZNK8AxisGrid14gridVisibilityEv
inline QVector4D AxisGrid::gridVisibility() const
{
    return m_gridVisibility;
}

//  from ../qtgraphs/src/graphs2d/axis/axisgrid.cpp, line 73, as _ZN8AxisGrid17setGridVisibilityERK9QVector4D
inline void AxisGrid::setGridVisibility(const QVector4D &newGridVisibility)
{
    if (m_gridVisibility == newGridVisibility)
        return;
    m_gridVisibility = newGridVisibility;
    emit gridVisibilityChanged();
}

//  from ../qtgraphs/src/graphs2d/axis/axisgrid.cpp, line 81, as _ZNK8AxisGrid9gridWidthEv
inline qreal AxisGrid::gridWidth() const
{
    return m_gridWidth;
}

//  from ../qtgraphs/src/graphs2d/axis/axisgrid.cpp, line 86, as _ZN8AxisGrid12setGridWidthEd
inline void AxisGrid::setGridWidth(qreal newGridWidth)
{
    if (QtPrivate::fuzzyCompare(m_gridWidth, newGridWidth))
        return;
    m_gridWidth = newGridWidth;
    emit gridWidthChanged();
}

//  from ../qtgraphs/src/graphs2d/axis/axisgrid.cpp, line 94, as _ZNK8AxisGrid10gridHeightEv
inline qreal AxisGrid::gridHeight() const
{
    return m_gridHeight;
}

//  from ../qtgraphs/src/graphs2d/axis/axisgrid.cpp, line 99, as _ZN8AxisGrid13setGridHeightEd
inline void AxisGrid::setGridHeight(qreal newGridHeight)
{
    if (QtPrivate::fuzzyCompare(m_gridHeight, newGridHeight))
        return;
    m_gridHeight = newGridHeight;
    emit gridHeightChanged();
}

//  from ../qtgraphs/src/graphs2d/axis/axisgrid.cpp, line 107, as _ZNK8AxisGrid12gridMovementEv
inline QPointF AxisGrid::gridMovement() const
{
    return m_gridMovement;
}

//  from ../qtgraphs/src/graphs2d/axis/axisgrid.cpp, line 112, as _ZN8AxisGrid15setGridMovementE7QPointF
inline void AxisGrid::setGridMovement(QPointF newGridMovement)
{
    if (m_gridMovement == newGridMovement)
        return;
    m_gridMovement = newGridMovement;
    emit gridMovementChanged();
}

//  from ../qtgraphs/src/graphs2d/axis/axisgrid.cpp, line 120, as _ZNK8AxisGrid12subGridColorEv
inline QColor AxisGrid::subGridColor() const
{
    return m_subGridColor;
}

//  from ../qtgraphs/src/graphs2d/axis/axisgrid.cpp, line 125, as _ZN8AxisGrid15setSubGridColorE6QColor
inline void AxisGrid::setSubGridColor(QColor newSubGridColor)
{
    if (m_subGridColor == newSubGridColor)
        return;
    m_subGridColor = newSubGridColor;
    emit subGridColorChanged();
}

//  from ../qtgraphs/src/graphs2d/axis/axisgrid.cpp, line 133, as _ZNK8AxisGrid9gridColorEv
inline QColor AxisGrid::gridColor() const
{
    return m_gridColor;
}

//  from ../qtgraphs/src/graphs2d/axis/axisgrid.cpp, line 138, as _ZN8AxisGrid12setGridColorE6QColor
inline void AxisGrid::setGridColor(QColor newGridColor)
{
    if (m_gridColor == newGridColor)
        return;
    m_gridColor = newGridColor;
    emit gridColorChanged();
}

//  from ../qtgraphs/src/graphs2d/axis/axisgrid.cpp, line 146, as _ZNK8AxisGrid23plotAreaBackgroundColorEv
inline QColor AxisGrid::plotAreaBackgroundColor() const
{
    return m_plotAreaBackgroundColor;
}

//  from ../qtgraphs/src/graphs2d/axis/axisgrid.cpp, line 151, as _ZN8AxisGrid26setPlotAreaBackgroundColorE6QColor
inline void AxisGrid::setPlotAreaBackgroundColor(QColor color)
{
    if (m_plotAreaBackgroundColor == color)
        return;
    m_plotAreaBackgroundColor = color;
    emit plotAreaBackgroundColorChanged();
}

//  from ../qtgraphs/src/graphs2d/axis/axisgrid.cpp, line 159, as _ZNK8AxisGrid16subGridLineWidthEv
inline qreal AxisGrid::subGridLineWidth() const
{
    return m_subGridLineWidth;
}

//  from ../qtgraphs/src/graphs2d/axis/axisgrid.cpp, line 164, as _ZN8AxisGrid19setSubGridLineWidthEd
inline void AxisGrid::setSubGridLineWidth(qreal newSubGridLineWidth)
{
    if (QtPrivate::fuzzyCompare(m_subGridLineWidth, newSubGridLineWidth))
        return;
    m_subGridLineWidth = newSubGridLineWidth;
    emit subGridLineWidthChanged();
}

//  from ../qtgraphs/src/graphs2d/axis/axisgrid.cpp, line 172, as _ZNK8AxisGrid13gridLineWidthEv
inline qreal AxisGrid::gridLineWidth() const
{
    return m_gridLineWidth;
}

//  from ../qtgraphs/src/graphs2d/axis/axisgrid.cpp, line 177, as _ZN8AxisGrid16setGridLineWidthEd
inline void AxisGrid::setGridLineWidth(qreal newGridLineWidth)
{
    if (QtPrivate::fuzzyCompare(m_gridLineWidth, newGridLineWidth))
        return;
    m_gridLineWidth = newGridLineWidth;
    emit gridLineWidthChanged();
}

//  from ../qtgraphs/src/graphs2d/axis/axisgrid.cpp, line 185, as _ZNK8AxisGrid20verticalSubGridScaleEv
inline qreal AxisGrid::verticalSubGridScale() const
{
    return m_verticalSubGridScale;
}

//  from ../qtgraphs/src/graphs2d/axis/axisgrid.cpp, line 190, as _ZN8AxisGrid23setVerticalSubGridScaleEd
inline void AxisGrid::setVerticalSubGridScale(qreal newVerticalSubGridScale)
{
    if (QtPrivate::fuzzyCompare(m_verticalSubGridScale, newVerticalSubGridScale))
        return;
    m_verticalSubGridScale = newVerticalSubGridScale;
    emit verticalSubGridScaleChanged();
}

//  from ../qtgraphs/src/graphs2d/axis/axisgrid.cpp, line 198, as _ZNK8AxisGrid22horizontalSubGridScaleEv
inline qreal AxisGrid::horizontalSubGridScale() const
{
    return m_horizontalSubGridScale;
}

//  from ../qtgraphs/src/graphs2d/axis/axisgrid.cpp, line 203, as _ZN8AxisGrid25setHorizontalSubGridScaleEd
inline void AxisGrid::setHorizontalSubGridScale(qreal newHorizontalSubGridScale)
{
    if (QtPrivate::fuzzyCompare(m_horizontalSubGridScale, newHorizontalSubGridScale))
        return;
    m_horizontalSubGridScale = newHorizontalSubGridScale;
    emit horizontalSubGridScaleChanged();
}

//  from ../qtgraphs/src/graphs2d/axis/axisgrid.cpp, line 211, as _ZNK8AxisGrid21isVerticalLogarithmicEv
inline bool AxisGrid::isVerticalLogarithmic() const
{
    return m_isVerticalLogarithmic;
}

//  from ../qtgraphs/src/graphs2d/axis/axisgrid.cpp, line 216, as _ZN8AxisGrid22setVerticalLogarithmicEb
inline void AxisGrid::setVerticalLogarithmic(bool newLogarithmic)
{
    if (m_isVerticalLogarithmic == newLogarithmic)
        return;
    m_isVerticalLogarithmic = newLogarithmic;
    emit verticalLogarithmicChanged(newLogarithmic);
}

//  from ../qtgraphs/src/graphs2d/axis/axisgrid.cpp, line 224, as _ZNK8AxisGrid23isHorizontalLogarithmicEv
inline bool AxisGrid::isHorizontalLogarithmic() const
{
    return m_isHorizontalLogarithmic;
}

//  from ../qtgraphs/src/graphs2d/axis/axisgrid.cpp, line 229, as _ZN8AxisGrid24setHorizontalLogarithmicEb
inline void AxisGrid::setHorizontalLogarithmic(bool newLogarithmic)
{
    if (m_isHorizontalLogarithmic == newLogarithmic)
        return;
    m_isHorizontalLogarithmic = newLogarithmic;
    emit horizontalLogarithmicChanged(newLogarithmic);
}

//  from ../qtgraphs/src/graphs2d/axis/axisgrid.cpp, line 237, as _ZNK8AxisGrid12verticalBaseEv
inline qreal AxisGrid::verticalBase() const
{
    return m_verticalBase;
}

//  from ../qtgraphs/src/graphs2d/axis/axisgrid.cpp, line 242, as _ZN8AxisGrid15setVerticalBaseEd
inline void AxisGrid::setVerticalBase(qreal newBase)
{
    if (qFuzzyCompare(m_verticalBase, newBase))
        return;
    m_verticalBase = newBase;
    emit verticalBaseChanged(newBase);
}

//  from ../qtgraphs/src/graphs2d/axis/axisgrid.cpp, line 250, as _ZNK8AxisGrid14horizontalBaseEv
inline qreal AxisGrid::horizontalBase() const
{
    return m_horizontalBase;
}

//  from ../qtgraphs/src/graphs2d/axis/axisgrid.cpp, line 255, as _ZN8AxisGrid17setHorizontalBaseEd
inline void AxisGrid::setHorizontalBase(qreal newBase)
{
    if (qFuzzyCompare(m_horizontalBase, newBase))
        return;
    m_horizontalBase = newBase;
    emit verticalBaseChanged(newBase);
}
//  -----------------------------------------------------------------------

//  Only a class built on AxisGrid may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnAxisGrid : AxisGrid {
  using AxisGrid::componentComplete;
  using AxisGrid::geometryChange;
};

//  A AxisGrid that Python can take functions over in. Every AxisGrid
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteAxisGridCall0)(const void *, int *);
typedef void (*CuteAxisGridCall1)(const void *, const QRectF *, const QRectF *, int *);
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(quick_shadereffect)
typedef bool (*CuteAxisGridCall2)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(quick_shadereffect)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(quick_shadereffect)
typedef void * (*CuteAxisGridCall3)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
#endif  // QT_CONFIG(quick_shadereffect)
#if QT_CONFIG(quick_shadereffect)
typedef void (*CuteAxisGridCall4)(const void *, int, const QQuickItem::ItemChangeData *, int *);
#endif  // QT_CONFIG(quick_shadereffect)
typedef const QRectF * (*CuteAxisGridCall5)(const void *, int *);
typedef const QRectF * (*CuteAxisGridCall6)(const void *, int *);
typedef bool (*CuteAxisGridCall7)(const void *, const QPointF *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteAxisGridCall8)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef bool (*CuteAxisGridCall9)(const void *, int *);
typedef void * (*CuteAxisGridCall10)(const void *, int *);
typedef void (*CuteAxisGridCall11)(const void *, int *);
typedef void (*CuteAxisGridCall12)(const void *, QKeyEvent *, int *);
typedef void (*CuteAxisGridCall13)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteAxisGridCall14)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteAxisGridCall15)(const void *, QFocusEvent *, int *);
typedef void (*CuteAxisGridCall16)(const void *, QFocusEvent *, int *);
typedef void (*CuteAxisGridCall17)(const void *, QMouseEvent *, int *);
typedef void (*CuteAxisGridCall18)(const void *, QMouseEvent *, int *);
typedef void (*CuteAxisGridCall19)(const void *, QMouseEvent *, int *);
typedef void (*CuteAxisGridCall20)(const void *, QMouseEvent *, int *);
typedef void (*CuteAxisGridCall21)(const void *, int *);
typedef void (*CuteAxisGridCall22)(const void *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteAxisGridCall23)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteAxisGridCall24)(const void *, QTouchEvent *, int *);
typedef void (*CuteAxisGridCall25)(const void *, QHoverEvent *, int *);
typedef void (*CuteAxisGridCall26)(const void *, QHoverEvent *, int *);
typedef void (*CuteAxisGridCall27)(const void *, QHoverEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteAxisGridCall28)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteAxisGridCall29)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteAxisGridCall30)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteAxisGridCall31)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef bool (*CuteAxisGridCall32)(const void *, QQuickItem *, QEvent *, int *);
typedef void (*CuteAxisGridCall33)(const void *, int *);
typedef void (*CuteAxisGridCall34)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteAxisGridCall35)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteAxisGridCall36)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteAxisGridCall37)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteAxisGridCall38)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteAxisGridCall39)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteAxisGridCall40)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteAxisGrid : public AxisGrid {
public:
  using AxisGrid::AxisGrid;
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

  //  void AxisGrid::componentComplete()
  void componentComplete() override {
    if (taken[0]) {
      int handled = 0;
      CuteAxisGridCall0 call = reinterpret_cast<CuteAxisGridCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    AxisGrid::componentComplete();
  }

  //  void AxisGrid::geometryChange(const QRectF &newGeometry, const QRectF
  //      &oldGeometry)
  void geometryChange(
      const QRectF &newGeometry,
      const QRectF &oldGeometry) override {
    if (taken[1]) {
      int handled = 0;
      CuteAxisGridCall1 call = reinterpret_cast<CuteAxisGridCall1>(taken[1]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    AxisGrid::geometryChange(newGeometry, oldGeometry);
  }

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(quick_shadereffect)
  //  bool QQuickShaderEffect::event(QEvent *e)
  bool event(QEvent *e) override {
    if (taken[2]) {
      int handled = 0;
      CuteAxisGridCall2 call = reinterpret_cast<CuteAxisGridCall2>(taken[2]);
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
      CuteAxisGridCall3 call = reinterpret_cast<CuteAxisGridCall3>(taken[3]);
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
      CuteAxisGridCall4 call = reinterpret_cast<CuteAxisGridCall4>(taken[4]);
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
      CuteAxisGridCall5 call = reinterpret_cast<CuteAxisGridCall5>(taken[5]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::boundingRect();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[6]) {
      int handled = 0;
      CuteAxisGridCall6 call = reinterpret_cast<CuteAxisGridCall6>(taken[6]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::clipRect();
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[7]) {
      int handled = 0;
      CuteAxisGridCall7 call = reinterpret_cast<CuteAxisGridCall7>(taken[7]);
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
      CuteAxisGridCall8 call = reinterpret_cast<CuteAxisGridCall8>(taken[8]);
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
      CuteAxisGridCall9 call = reinterpret_cast<CuteAxisGridCall9>(taken[9]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[10]) {
      int handled = 0;
      CuteAxisGridCall10 call = reinterpret_cast<CuteAxisGridCall10>(taken[10]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTextureProvider *>(given);
    }
    return QQuickItem::textureProvider();
  }

  //  void QQuickItem::classBegin()
  void classBegin() override {
    if (taken[11]) {
      int handled = 0;
      CuteAxisGridCall11 call = reinterpret_cast<CuteAxisGridCall11>(taken[11]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::classBegin();
  }

  //  void QQuickItem::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteAxisGridCall12 call = reinterpret_cast<CuteAxisGridCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyPressEvent(event);
  }

  //  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteAxisGridCall13 call = reinterpret_cast<CuteAxisGridCall13>(taken[13]);
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
      CuteAxisGridCall14 call = reinterpret_cast<CuteAxisGridCall14>(taken[14]);
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
      CuteAxisGridCall15 call = reinterpret_cast<CuteAxisGridCall15>(taken[15]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusInEvent(a0);
  }

  //  void QQuickItem::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[16]) {
      int handled = 0;
      CuteAxisGridCall16 call = reinterpret_cast<CuteAxisGridCall16>(taken[16]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusOutEvent(a0);
  }

  //  void QQuickItem::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteAxisGridCall17 call = reinterpret_cast<CuteAxisGridCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mousePressEvent(event);
  }

  //  void QQuickItem::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteAxisGridCall18 call = reinterpret_cast<CuteAxisGridCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseMoveEvent(event);
  }

  //  void QQuickItem::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteAxisGridCall19 call = reinterpret_cast<CuteAxisGridCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseReleaseEvent(event);
  }

  //  void QQuickItem::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteAxisGridCall20 call = reinterpret_cast<CuteAxisGridCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseDoubleClickEvent(event);
  }

  //  void QQuickItem::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[21]) {
      int handled = 0;
      CuteAxisGridCall21 call = reinterpret_cast<CuteAxisGridCall21>(taken[21]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::mouseUngrabEvent();
  }

  //  void QQuickItem::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[22]) {
      int handled = 0;
      CuteAxisGridCall22 call = reinterpret_cast<CuteAxisGridCall22>(taken[22]);
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
      CuteAxisGridCall23 call = reinterpret_cast<CuteAxisGridCall23>(taken[23]);
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
      CuteAxisGridCall24 call = reinterpret_cast<CuteAxisGridCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::touchEvent(event);
  }

  //  void QQuickItem::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteAxisGridCall25 call = reinterpret_cast<CuteAxisGridCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverEnterEvent(event);
  }

  //  void QQuickItem::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteAxisGridCall26 call = reinterpret_cast<CuteAxisGridCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverMoveEvent(event);
  }

  //  void QQuickItem::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteAxisGridCall27 call = reinterpret_cast<CuteAxisGridCall27>(taken[27]);
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
      CuteAxisGridCall28 call = reinterpret_cast<CuteAxisGridCall28>(taken[28]);
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
      CuteAxisGridCall29 call = reinterpret_cast<CuteAxisGridCall29>(taken[29]);
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
      CuteAxisGridCall30 call = reinterpret_cast<CuteAxisGridCall30>(taken[30]);
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
      CuteAxisGridCall31 call = reinterpret_cast<CuteAxisGridCall31>(taken[31]);
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
      CuteAxisGridCall32 call = reinterpret_cast<CuteAxisGridCall32>(taken[32]);
      bool given = call(this, a0, a1, &handled);
      if (handled) return given;
    }
    return QQuickItem::childMouseEventFilter(a0, a1);
  }

  //  void QQuickItem::releaseResources()
  void releaseResources() override {
    if (taken[33]) {
      int handled = 0;
      CuteAxisGridCall33 call = reinterpret_cast<CuteAxisGridCall33>(taken[33]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::releaseResources();
  }

  //  void QQuickItem::updatePolish()
  void updatePolish() override {
    if (taken[34]) {
      int handled = 0;
      CuteAxisGridCall34 call = reinterpret_cast<CuteAxisGridCall34>(taken[34]);
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
      CuteAxisGridCall35 call = reinterpret_cast<CuteAxisGridCall35>(taken[35]);
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
      CuteAxisGridCall36 call = reinterpret_cast<CuteAxisGridCall36>(taken[36]);
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
      CuteAxisGridCall37 call = reinterpret_cast<CuteAxisGridCall37>(taken[37]);
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
      CuteAxisGridCall38 call = reinterpret_cast<CuteAxisGridCall38>(taken[38]);
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
      CuteAxisGridCall39 call = reinterpret_cast<CuteAxisGridCall39>(taken[39]);
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
      CuteAxisGridCall40 call = reinterpret_cast<CuteAxisGridCall40>(taken[40]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *AxisGrid::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK8AxisGrid10metaObjectEv(const AxisGrid *self) {
  return self->metaObject();
}

//  void *AxisGrid::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN8AxisGrid11qt_metacastEPKc(AxisGrid *self, const char *a0) {
  return self->qt_metacast(a0);
}

//  int AxisGrid::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN8AxisGrid11qt_metacallEN11QMetaObject4CallEiPPv(
    AxisGrid *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString AxisGrid::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN8AxisGrid2trEPKcS1_i(const char *s, const char *c, int n) {
  return new QString(AxisGrid::tr(s, c, n));
}

//  AxisGrid::AxisGrid(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
AxisGrid *ritual_ZN8AxisGridC1EP10QQuickItem(QQuickItem *parent) {
  return new CuteAxisGrid(parent);
}

//  AxisGrid::~AxisGrid()
extern "C" Q_DECL_EXPORT
void ritual_ZN8AxisGridD1Ev(AxisGrid *self) {
  delete self;
}

//  void AxisGrid::setupShaders()
extern "C" Q_DECL_EXPORT
void ritual_ZN8AxisGrid12setupShadersEv(AxisGrid *self) {
  self->setupShaders();
}

//  QVector3D AxisGrid::iResolution() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK8AxisGrid11iResolutionEv(const AxisGrid *self) {
  return new QVector3D(self->iResolution());
}

//  qreal AxisGrid::smoothing() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK8AxisGrid9smoothingEv(const AxisGrid *self) {
  return self->smoothing();
}

//  void AxisGrid::setSmoothing(qreal newSmoothing)
extern "C" Q_DECL_EXPORT
void ritual_ZN8AxisGrid12setSmoothingEd(AxisGrid *self, qreal newSmoothing) {
  self->setSmoothing(newSmoothing);
}

//  int AxisGrid::origo() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK8AxisGrid5origoEv(const AxisGrid *self) {
  return self->origo();
}

//  void AxisGrid::setOrigo(int newOrigo)
extern "C" Q_DECL_EXPORT
void ritual_ZN8AxisGrid8setOrigoEi(AxisGrid *self, int newOrigo) {
  self->setOrigo(newOrigo);
}

//  QVector4D AxisGrid::gridVisibility() const
extern "C" Q_DECL_EXPORT
QVector4D *ritual_ZNK8AxisGrid14gridVisibilityEv(const AxisGrid *self) {
  return new QVector4D(self->gridVisibility());
}

//  void AxisGrid::setGridVisibility(const QVector4D &newGridVisibility)
extern "C" Q_DECL_EXPORT
void ritual_ZN8AxisGrid17setGridVisibilityERK9QVector4D(
    AxisGrid *self,
    const QVector4D *newGridVisibility) {
  self->setGridVisibility(*newGridVisibility);
}

//  qreal AxisGrid::gridWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK8AxisGrid9gridWidthEv(const AxisGrid *self) {
  return self->gridWidth();
}

//  void AxisGrid::setGridWidth(qreal newGridWidth)
extern "C" Q_DECL_EXPORT
void ritual_ZN8AxisGrid12setGridWidthEd(AxisGrid *self, qreal newGridWidth) {
  self->setGridWidth(newGridWidth);
}

//  qreal AxisGrid::gridHeight() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK8AxisGrid10gridHeightEv(const AxisGrid *self) {
  return self->gridHeight();
}

//  void AxisGrid::setGridHeight(qreal newGridHeight)
extern "C" Q_DECL_EXPORT
void ritual_ZN8AxisGrid13setGridHeightEd(
    AxisGrid *self,
    qreal newGridHeight) {
  self->setGridHeight(newGridHeight);
}

//  QPointF AxisGrid::gridMovement() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK8AxisGrid12gridMovementEv(const AxisGrid *self) {
  return new QPointF(self->gridMovement());
}

//  void AxisGrid::setGridMovement(QPointF newGridMovement)
extern "C" Q_DECL_EXPORT
void ritual_ZN8AxisGrid15setGridMovementE7QPointF(
    AxisGrid *self,
    const QPointF *newGridMovement) {
  self->setGridMovement(*newGridMovement);
}

//  QColor AxisGrid::subGridColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK8AxisGrid12subGridColorEv(const AxisGrid *self) {
  return new QColor(self->subGridColor());
}

//  void AxisGrid::setSubGridColor(QColor newSubGridColor)
extern "C" Q_DECL_EXPORT
void ritual_ZN8AxisGrid15setSubGridColorE6QColor(
    AxisGrid *self,
    const QColor *newSubGridColor) {
  self->setSubGridColor(*newSubGridColor);
}

//  QColor AxisGrid::gridColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK8AxisGrid9gridColorEv(const AxisGrid *self) {
  return new QColor(self->gridColor());
}

//  void AxisGrid::setGridColor(QColor newGridColor)
extern "C" Q_DECL_EXPORT
void ritual_ZN8AxisGrid12setGridColorE6QColor(
    AxisGrid *self,
    const QColor *newGridColor) {
  self->setGridColor(*newGridColor);
}

//  QColor AxisGrid::plotAreaBackgroundColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK8AxisGrid23plotAreaBackgroundColorEv(
    const AxisGrid *self) {
  return new QColor(self->plotAreaBackgroundColor());
}

//  void AxisGrid::setPlotAreaBackgroundColor(QColor color)
extern "C" Q_DECL_EXPORT
void ritual_ZN8AxisGrid26setPlotAreaBackgroundColorE6QColor(
    AxisGrid *self,
    const QColor *color) {
  self->setPlotAreaBackgroundColor(*color);
}

//  qreal AxisGrid::subGridLineWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK8AxisGrid16subGridLineWidthEv(const AxisGrid *self) {
  return self->subGridLineWidth();
}

//  void AxisGrid::setSubGridLineWidth(qreal newSubGridLineWidth)
extern "C" Q_DECL_EXPORT
void ritual_ZN8AxisGrid19setSubGridLineWidthEd(
    AxisGrid *self,
    qreal newSubGridLineWidth) {
  self->setSubGridLineWidth(newSubGridLineWidth);
}

//  qreal AxisGrid::gridLineWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK8AxisGrid13gridLineWidthEv(const AxisGrid *self) {
  return self->gridLineWidth();
}

//  void AxisGrid::setGridLineWidth(qreal newGridLineWidth)
extern "C" Q_DECL_EXPORT
void ritual_ZN8AxisGrid16setGridLineWidthEd(
    AxisGrid *self,
    qreal newGridLineWidth) {
  self->setGridLineWidth(newGridLineWidth);
}

//  qreal AxisGrid::verticalSubGridScale() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK8AxisGrid20verticalSubGridScaleEv(const AxisGrid *self) {
  return self->verticalSubGridScale();
}

//  void AxisGrid::setVerticalSubGridScale(qreal newVerticalSubGridScale)
extern "C" Q_DECL_EXPORT
void ritual_ZN8AxisGrid23setVerticalSubGridScaleEd(
    AxisGrid *self,
    qreal newVerticalSubGridScale) {
  self->setVerticalSubGridScale(newVerticalSubGridScale);
}

//  qreal AxisGrid::horizontalSubGridScale() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK8AxisGrid22horizontalSubGridScaleEv(const AxisGrid *self) {
  return self->horizontalSubGridScale();
}

//  void AxisGrid::setHorizontalSubGridScale(qreal newHorizontalSubGridScale)
extern "C" Q_DECL_EXPORT
void ritual_ZN8AxisGrid25setHorizontalSubGridScaleEd(
    AxisGrid *self,
    qreal newHorizontalSubGridScale) {
  self->setHorizontalSubGridScale(newHorizontalSubGridScale);
}

//  bool AxisGrid::isVerticalLogarithmic() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8AxisGrid21isVerticalLogarithmicEv(const AxisGrid *self) {
  return self->isVerticalLogarithmic();
}

//  void AxisGrid::setVerticalLogarithmic(bool newLogarithmic)
extern "C" Q_DECL_EXPORT
void ritual_ZN8AxisGrid22setVerticalLogarithmicEb(
    AxisGrid *self,
    bool newLogarithmic) {
  self->setVerticalLogarithmic(newLogarithmic);
}

//  bool AxisGrid::isHorizontalLogarithmic() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8AxisGrid23isHorizontalLogarithmicEv(const AxisGrid *self) {
  return self->isHorizontalLogarithmic();
}

//  void AxisGrid::setHorizontalLogarithmic(bool newLogarithmic)
extern "C" Q_DECL_EXPORT
void ritual_ZN8AxisGrid24setHorizontalLogarithmicEb(
    AxisGrid *self,
    bool newLogarithmic) {
  self->setHorizontalLogarithmic(newLogarithmic);
}

//  qreal AxisGrid::verticalBase() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK8AxisGrid12verticalBaseEv(const AxisGrid *self) {
  return self->verticalBase();
}

//  void AxisGrid::setVerticalBase(qreal newBase)
extern "C" Q_DECL_EXPORT
void ritual_ZN8AxisGrid15setVerticalBaseEd(AxisGrid *self, qreal newBase) {
  self->setVerticalBase(newBase);
}

//  qreal AxisGrid::horizontalBase() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK8AxisGrid14horizontalBaseEv(const AxisGrid *self) {
  return self->horizontalBase();
}

//  void AxisGrid::setHorizontalBase(qreal newBase)
extern "C" Q_DECL_EXPORT
void ritual_ZN8AxisGrid17setHorizontalBaseEd(AxisGrid *self, qreal newBase) {
  self->setHorizontalBase(newBase);
}

//  void AxisGrid::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN8AxisGrid17componentCompleteEv(AxisGrid *self) {
  self->componentComplete();
}

//  void AxisGrid::geometryChange(const QRectF &newGeometry, const QRectF
//      &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_ZN8AxisGrid14geometryChangeERK6QRectFS2_(
    AxisGrid *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  self->geometryChange(*newGeometry, *oldGeometry);
}

//  void AxisGrid::iResolutionChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN8AxisGrid18iResolutionChangedEv(AxisGrid *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "AxisGrid")) {
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

//  void AxisGrid::smoothingChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN8AxisGrid16smoothingChangedEv(AxisGrid *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "AxisGrid")) {
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

//  void AxisGrid::origoChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN8AxisGrid12origoChangedEv(AxisGrid *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "AxisGrid")) {
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

//  void AxisGrid::gridVisibilityChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN8AxisGrid21gridVisibilityChangedEv(AxisGrid *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "AxisGrid")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "gridVisibilityChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "gridVisibilityChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void AxisGrid::gridWidthChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN8AxisGrid16gridWidthChangedEv(AxisGrid *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "AxisGrid")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "gridWidthChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "gridWidthChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void AxisGrid::gridHeightChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN8AxisGrid17gridHeightChangedEv(AxisGrid *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "AxisGrid")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "gridHeightChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "gridHeightChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void AxisGrid::gridMovementChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN8AxisGrid19gridMovementChangedEv(AxisGrid *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "AxisGrid")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "gridMovementChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "gridMovementChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void AxisGrid::subGridColorChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN8AxisGrid19subGridColorChangedEv(AxisGrid *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "AxisGrid")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "subGridColorChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "subGridColorChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void AxisGrid::gridColorChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN8AxisGrid16gridColorChangedEv(AxisGrid *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "AxisGrid")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "gridColorChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "gridColorChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void AxisGrid::plotAreaBackgroundColorChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN8AxisGrid30plotAreaBackgroundColorChangedEv(AxisGrid *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "AxisGrid")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "plotAreaBackgroundColorChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "plotAreaBackgroundColorChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void AxisGrid::subGridLineWidthChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN8AxisGrid23subGridLineWidthChangedEv(AxisGrid *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "AxisGrid")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "subGridLineWidthChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "subGridLineWidthChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void AxisGrid::gridLineWidthChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN8AxisGrid20gridLineWidthChangedEv(AxisGrid *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "AxisGrid")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "gridLineWidthChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "gridLineWidthChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void AxisGrid::verticalSubGridScaleChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN8AxisGrid27verticalSubGridScaleChangedEv(AxisGrid *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "AxisGrid")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "verticalSubGridScaleChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "verticalSubGridScaleChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void AxisGrid::horizontalSubGridScaleChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN8AxisGrid29horizontalSubGridScaleChangedEv(AxisGrid *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "AxisGrid")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "horizontalSubGridScaleChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "horizontalSubGridScaleChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void AxisGrid::verticalLogarithmicChanged(bool logarithmic)
extern "C" Q_DECL_EXPORT
void ritual_ZN8AxisGrid26verticalLogarithmicChangedEb(
    AxisGrid *self,
    bool logarithmic) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "AxisGrid")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "verticalLogarithmicChanged(bool)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "verticalLogarithmicChanged(bool)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&logarithmic)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void AxisGrid::horizontalLogarithmicChanged(bool logarithmic)
extern "C" Q_DECL_EXPORT
void ritual_ZN8AxisGrid28horizontalLogarithmicChangedEb(
    AxisGrid *self,
    bool logarithmic) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "AxisGrid")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "horizontalLogarithmicChanged(bool)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "horizontalLogarithmicChanged(bool)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&logarithmic)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void AxisGrid::verticalBaseChanged(qreal base)
extern "C" Q_DECL_EXPORT
void ritual_ZN8AxisGrid19verticalBaseChangedEd(AxisGrid *self, qreal base) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "AxisGrid")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "verticalBaseChanged(qreal)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "verticalBaseChanged(qreal)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&base)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void AxisGrid::horizontalBaseChanged(qreal base)
extern "C" Q_DECL_EXPORT
void ritual_ZN8AxisGrid21horizontalBaseChangedEd(
    AxisGrid *self,
    qreal base) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "AxisGrid")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "horizontalBaseChanged(qreal)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "horizontalBaseChanged(qreal)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&base)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  a Python function taken by a CuteAxisGrid, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_AxisGrid(AxisGrid *self, const char *key, void *call) {
  return static_cast<CuteAxisGrid *>(self)->take(key, call);
}

//  void AxisGrid::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8AxisGrid17componentCompleteEv(AxisGrid *self) {
  static_cast<OwnAxisGrid *>(self)->OwnAxisGrid::componentComplete();
}

//  void AxisGrid::geometryChange(const QRectF &newGeometry, const QRectF
//      &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8AxisGrid14geometryChangeERK6QRectFS2_(
    AxisGrid *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  static_cast<OwnAxisGrid *>(self)->OwnAxisGrid::geometryChange(
      *newGeometry,
      *oldGeometry);
}

#endif  // (QT_CONFIG(graphs_2d)) && (!(!QT_CONFIG(graphs_2d_area) && !QT_CONFIG(graphs_2d_bar) && !QT_CONFIG(graphs_2d_donut_pie) && !QT_CONFIG(graphs_2d_line) && !QT_CONFIG(graphs_2d_scatter) && !QT_CONFIG(graphs_2d_spline) && !QT_CONFIG(graphs_2d_custom)))
