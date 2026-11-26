//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3DXr/6.12.0/QtQuick3DXr/private/qquick3dxrspatialanchor_p.h, Qt
//  6.12.0.
//  Edited by hand on 2026-11-26: moc's output for 'QQuick3DXrSpatialAnchor'
//  is pasted in, cut from what the moc of Qt 6.12.0 writes for its header:
//  Qt's library keeps it to itself; added are 10 rituals that lean on what
//  moc writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
#include <QtQuick3DXr/6.12.0/QtQuick3DXr/private/qtquick3dxrglobal_p.h>
#include <QtQuick3DXr/QtQuick3DXr>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DXr/6.12.0/QtQuick3DXr/private/qquick3dxrspatialanchor_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qvectornd.h>
#include <QtGui/qquaternion.h>
#include <QtCore/quuid.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>
#include <QtCore/QSet>
#include <QtCore/QUuid>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtQuick3DXr/private/qquick3dxrspatialanchor_p.h>
#if defined(Q_OS_VISIONOS)
#include "visionos/qquick3dxranchormanager_visionos_p.h"
#else
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from QtQuick3DXr__QQuick3DXrSpatialAnchor.cpp, line 1, as moc:QQuick3DXrSpatialAnchor
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN23QQuick3DXrSpatialAnchorE_t {};
} // unnamed namespace

template <> constexpr inline auto QQuick3DXrSpatialAnchor::qt_create_metaobjectdata<qt_meta_tag_ZN23QQuick3DXrSpatialAnchorE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QQuick3DXrSpatialAnchor",
        "QML.Element",
        "XrSpatialAnchor",
        "QML.Creatable",
        "false",
        "QML.UncreatableReason",
        "Spatial anchor objects cannot be created in QML",
        "QML.AddedInVersion",
        "1544",
        "offset3DChanged",
        "",
        "extent3DChanged",
        "positionChanged",
        "rotationChanged",
        "classificationChanged",
        "classificationStringChanged",
        "has2DBoundsChanged",
        "has3DBoundsChanged",
        "offset2DChanged",
        "extent2DChanged",
        "has2DBounds",
        "has3DBounds",
        "offset2D",
        "QVector2D",
        "extent2D",
        "offset3D",
        "QVector3D",
        "extent3D",
        "position",
        "rotation",
        "QQuaternion",
        "classification",
        "Classification",
        "classificationString",
        "identifier",
        "Unknown",
        "Wall",
        "Ceiling",
        "Floor",
        "Table",
        "Seat",
        "Window",
        "Door",
        "Other"
    };

    QtMocHelpers::UintData qt_methods {
        // Signal 'offset3DChanged'
        QtMocHelpers::SignalData<void()>(9, 10, QMC::AccessPublic, QMetaType::Void),
        // Signal 'extent3DChanged'
        QtMocHelpers::SignalData<void()>(11, 10, QMC::AccessPublic, QMetaType::Void),
        // Signal 'positionChanged'
        QtMocHelpers::SignalData<void()>(12, 10, QMC::AccessPublic, QMetaType::Void),
        // Signal 'rotationChanged'
        QtMocHelpers::SignalData<void()>(13, 10, QMC::AccessPublic, QMetaType::Void),
        // Signal 'classificationChanged'
        QtMocHelpers::SignalData<void()>(14, 10, QMC::AccessPublic, QMetaType::Void),
        // Signal 'classificationStringChanged'
        QtMocHelpers::SignalData<void()>(15, 10, QMC::AccessPublic, QMetaType::Void),
        // Signal 'has2DBoundsChanged'
        QtMocHelpers::SignalData<void()>(16, 10, QMC::AccessPublic, QMetaType::Void),
        // Signal 'has3DBoundsChanged'
        QtMocHelpers::SignalData<void()>(17, 10, QMC::AccessPublic, QMetaType::Void),
        // Signal 'offset2DChanged'
        QtMocHelpers::SignalData<void()>(18, 10, QMC::AccessPublic, QMetaType::Void),
        // Signal 'extent2DChanged'
        QtMocHelpers::SignalData<void()>(19, 10, QMC::AccessPublic, QMetaType::Void),
    };
    QtMocHelpers::UintData qt_properties {
        // property 'has2DBounds'
        QtMocHelpers::PropertyData<bool>(20, QMetaType::Bool, QMC::DefaultPropertyFlags | QMC::Final, 6),
        // property 'has3DBounds'
        QtMocHelpers::PropertyData<bool>(21, QMetaType::Bool, QMC::DefaultPropertyFlags | QMC::Final, 7),
        // property 'offset2D'
        QtMocHelpers::PropertyData<QVector2D>(22, 0x80000000 | 23, QMC::DefaultPropertyFlags | QMC::EnumOrFlag | QMC::Final, 8),
        // property 'extent2D'
        QtMocHelpers::PropertyData<QVector2D>(24, 0x80000000 | 23, QMC::DefaultPropertyFlags | QMC::EnumOrFlag | QMC::Final, 9),
        // property 'offset3D'
        QtMocHelpers::PropertyData<QVector3D>(25, 0x80000000 | 26, QMC::DefaultPropertyFlags | QMC::EnumOrFlag | QMC::Final, 0),
        // property 'extent3D'
        QtMocHelpers::PropertyData<QVector3D>(27, 0x80000000 | 26, QMC::DefaultPropertyFlags | QMC::EnumOrFlag | QMC::Final, 1),
        // property 'position'
        QtMocHelpers::PropertyData<QVector3D>(28, 0x80000000 | 26, QMC::DefaultPropertyFlags | QMC::EnumOrFlag | QMC::Final, 2),
        // property 'rotation'
        QtMocHelpers::PropertyData<QQuaternion>(29, 0x80000000 | 30, QMC::DefaultPropertyFlags | QMC::EnumOrFlag | QMC::Final, 3),
        // property 'classification'
        QtMocHelpers::PropertyData<enum Classification>(31, 0x80000000 | 32, QMC::DefaultPropertyFlags | QMC::EnumOrFlag | QMC::Final, 4),
        // property 'classificationString'
        QtMocHelpers::PropertyData<QString>(33, QMetaType::QString, QMC::DefaultPropertyFlags | QMC::Final, 5),
        // property 'identifier'
        QtMocHelpers::PropertyData<QString>(34, QMetaType::QString, QMC::DefaultPropertyFlags | QMC::Constant),
    };
    QtMocHelpers::UintData qt_enums {
        // enum 'Classification'
        QtMocHelpers::EnumData<enum Classification>(32, 32, QMC::EnumIsScoped).add({
            {   35, Classification::Unknown },
            {   36, Classification::Wall },
            {   37, Classification::Ceiling },
            {   38, Classification::Floor },
            {   39, Classification::Table },
            {   40, Classification::Seat },
            {   41, Classification::Window },
            {   42, Classification::Door },
            {   43, Classification::Other },
        }),
    };
    QtMocHelpers::UintData qt_constructors {};
    QtMocHelpers::ClassInfos qt_classinfo({
            {    1,    2 },
            {    3,    4 },
            {    5,    6 },
            {    7,    8 },
    });
    return QtMocHelpers::metaObjectData<QQuick3DXrSpatialAnchor, void>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums, qt_constructors, qt_classinfo);
}
Q_CONSTINIT const QMetaObject QQuick3DXrSpatialAnchor::staticMetaObject = { {
    QMetaObject::SuperData::link<QObject::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN23QQuick3DXrSpatialAnchorE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN23QQuick3DXrSpatialAnchorE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN23QQuick3DXrSpatialAnchorE_t>.metaTypes,
    nullptr
} };

void QQuick3DXrSpatialAnchor::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QQuick3DXrSpatialAnchor *>(_o);
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: _t->offset3DChanged(); break;
        case 1: _t->extent3DChanged(); break;
        case 2: _t->positionChanged(); break;
        case 3: _t->rotationChanged(); break;
        case 4: _t->classificationChanged(); break;
        case 5: _t->classificationStringChanged(); break;
        case 6: _t->has2DBoundsChanged(); break;
        case 7: _t->has3DBoundsChanged(); break;
        case 8: _t->offset2DChanged(); break;
        case 9: _t->extent2DChanged(); break;
        default: ;
        }
    }
    if (_c == QMetaObject::IndexOfMethod) {
        if (QtMocHelpers::indexOfMethod<void (QQuick3DXrSpatialAnchor::*)()>(_a, &QQuick3DXrSpatialAnchor::offset3DChanged, 0))
            return;
        if (QtMocHelpers::indexOfMethod<void (QQuick3DXrSpatialAnchor::*)()>(_a, &QQuick3DXrSpatialAnchor::extent3DChanged, 1))
            return;
        if (QtMocHelpers::indexOfMethod<void (QQuick3DXrSpatialAnchor::*)()>(_a, &QQuick3DXrSpatialAnchor::positionChanged, 2))
            return;
        if (QtMocHelpers::indexOfMethod<void (QQuick3DXrSpatialAnchor::*)()>(_a, &QQuick3DXrSpatialAnchor::rotationChanged, 3))
            return;
        if (QtMocHelpers::indexOfMethod<void (QQuick3DXrSpatialAnchor::*)()>(_a, &QQuick3DXrSpatialAnchor::classificationChanged, 4))
            return;
        if (QtMocHelpers::indexOfMethod<void (QQuick3DXrSpatialAnchor::*)()>(_a, &QQuick3DXrSpatialAnchor::classificationStringChanged, 5))
            return;
        if (QtMocHelpers::indexOfMethod<void (QQuick3DXrSpatialAnchor::*)()>(_a, &QQuick3DXrSpatialAnchor::has2DBoundsChanged, 6))
            return;
        if (QtMocHelpers::indexOfMethod<void (QQuick3DXrSpatialAnchor::*)()>(_a, &QQuick3DXrSpatialAnchor::has3DBoundsChanged, 7))
            return;
        if (QtMocHelpers::indexOfMethod<void (QQuick3DXrSpatialAnchor::*)()>(_a, &QQuick3DXrSpatialAnchor::offset2DChanged, 8))
            return;
        if (QtMocHelpers::indexOfMethod<void (QQuick3DXrSpatialAnchor::*)()>(_a, &QQuick3DXrSpatialAnchor::extent2DChanged, 9))
            return;
    }
    if (_c == QMetaObject::ReadProperty) {
        void *_v = _a[0];
        switch (_id) {
        case 0: *reinterpret_cast<bool*>(_v) = _t->has2DBounds(); break;
        case 1: *reinterpret_cast<bool*>(_v) = _t->has3DBounds(); break;
        case 2: *reinterpret_cast<QVector2D*>(_v) = _t->offset2D(); break;
        case 3: *reinterpret_cast<QVector2D*>(_v) = _t->extent2D(); break;
        case 4: *reinterpret_cast<QVector3D*>(_v) = _t->offset3D(); break;
        case 5: *reinterpret_cast<QVector3D*>(_v) = _t->extent3D(); break;
        case 6: *reinterpret_cast<QVector3D*>(_v) = _t->position(); break;
        case 7: *reinterpret_cast<QQuaternion*>(_v) = _t->rotation(); break;
        case 8: *reinterpret_cast<enum Classification*>(_v) = _t->classification(); break;
        case 9: *reinterpret_cast<QString*>(_v) = _t->classificationString(); break;
        case 10: *reinterpret_cast<QString*>(_v) = _t->identifier(); break;
        default: break;
        }
    }
}

const QMetaObject *QQuick3DXrSpatialAnchor::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QQuick3DXrSpatialAnchor::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN23QQuick3DXrSpatialAnchorE_t>.strings))
        return static_cast<void*>(this);
    return QObject::qt_metacast(_clname);
}

int QQuick3DXrSpatialAnchor::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QObject::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 10)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 10;
    }
    if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 10)
            *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType();
        _id -= 10;
    }
    if (_c == QMetaObject::ReadProperty || _c == QMetaObject::WriteProperty
            || _c == QMetaObject::ResetProperty || _c == QMetaObject::BindableProperty
            || _c == QMetaObject::RegisterPropertyMetaType) {
        qt_static_metacall(this, _c, _id, _a);
        _id -= 11;
    }
    return _id;
}

// SIGNAL 0
void QQuick3DXrSpatialAnchor::offset3DChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 0, nullptr);
}

// SIGNAL 1
void QQuick3DXrSpatialAnchor::extent3DChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 1, nullptr);
}

// SIGNAL 2
void QQuick3DXrSpatialAnchor::positionChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 2, nullptr);
}

// SIGNAL 3
void QQuick3DXrSpatialAnchor::rotationChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 3, nullptr);
}

// SIGNAL 4
void QQuick3DXrSpatialAnchor::classificationChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 4, nullptr);
}

// SIGNAL 5
void QQuick3DXrSpatialAnchor::classificationStringChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 5, nullptr);
}

// SIGNAL 6
void QQuick3DXrSpatialAnchor::has2DBoundsChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 6, nullptr);
}

// SIGNAL 7
void QQuick3DXrSpatialAnchor::has3DBoundsChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 7, nullptr);
}

// SIGNAL 8
void QQuick3DXrSpatialAnchor::offset2DChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 8, nullptr);
}

// SIGNAL 9
void QQuick3DXrSpatialAnchor::extent2DChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 9, nullptr);
}
QT_WARNING_POP

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrspatialanchor.cpp, line 134, as _ZN23QQuick3DXrSpatialAnchorD0Ev
inline QQuick3DXrSpatialAnchor::~QQuick3DXrSpatialAnchor()
{
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrspatialanchor.cpp, line 127, as _ZN23QQuick3DXrSpatialAnchorC1EN11QtQuick3DXr9XrSpaceIdER5QUuidP7QObject
inline QQuick3DXrSpatialAnchor::QQuick3DXrSpatialAnchor(QtQuick3DXr::XrSpaceId space, QUuid &uuid, QObject *parent)
    : QObject(parent)
    , m_space(space)
    , m_uuid(uuid)
{
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrspatialanchor.cpp, line 148, as _ZNK23QQuick3DXrSpatialAnchor8offset3DEv
inline QVector3D QQuick3DXrSpatialAnchor::offset3D() const
{
    return m_offset3D;
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrspatialanchor.cpp, line 153, as _ZN23QQuick3DXrSpatialAnchor11setOffset3DERK9QVector3D
inline void QQuick3DXrSpatialAnchor::setOffset3D(const QVector3D &newOffset)
{
    if (m_offset3D == newOffset)
        return;
    m_offset3D = newOffset;
    emit offset3DChanged();
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrspatialanchor.cpp, line 172, as _ZNK23QQuick3DXrSpatialAnchor8extent3DEv
inline QVector3D QQuick3DXrSpatialAnchor::extent3D() const
{
    return m_extent3D;
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrspatialanchor.cpp, line 177, as _ZN23QQuick3DXrSpatialAnchor11setExtent3DERK9QVector3D
inline void QQuick3DXrSpatialAnchor::setExtent3D(const QVector3D &newExtent)
{
    if (m_extent3D == newExtent)
        return;
    m_extent3D = newExtent;
    emit extent3DChanged();
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrspatialanchor.cpp, line 194, as _ZNK23QQuick3DXrSpatialAnchor8positionEv
inline QVector3D QQuick3DXrSpatialAnchor::position() const
{
    return m_position;
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrspatialanchor.cpp, line 199, as _ZN23QQuick3DXrSpatialAnchor11setPositionERK9QVector3D
inline void QQuick3DXrSpatialAnchor::setPosition(const QVector3D &newPosition)
{
    if (m_position == newPosition)
        return;
    m_position = newPosition;
    emit positionChanged();
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrspatialanchor.cpp, line 215, as _ZNK23QQuick3DXrSpatialAnchor8rotationEv
inline QQuaternion QQuick3DXrSpatialAnchor::rotation() const
{
    return m_rotation;
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrspatialanchor.cpp, line 220, as _ZN23QQuick3DXrSpatialAnchor11setRotationERK11QQuaternion
inline void QQuick3DXrSpatialAnchor::setRotation(const QQuaternion &newRotation)
{
    if (m_rotation == newRotation)
        return;
    m_rotation = newRotation;
    emit rotationChanged();
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrspatialanchor.cpp, line 243, as _ZNK23QQuick3DXrSpatialAnchor14classificationEv
inline QQuick3DXrSpatialAnchor::Classification QQuick3DXrSpatialAnchor::classification() const
{
    return m_classification;
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrspatialanchor.cpp, line 248, as _ZN23QQuick3DXrSpatialAnchor17setClassificationENS_14ClassificationE
inline void QQuick3DXrSpatialAnchor::setClassification(Classification newClassification)
{
    if (m_classification == newClassification)
        return;
    m_classification = newClassification;
    emit classificationChanged();
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrspatialanchor.cpp, line 271, as _ZNK23QQuick3DXrSpatialAnchor20classificationStringEv
inline QString QQuick3DXrSpatialAnchor::classificationString() const
{
    return m_classificationString;
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrspatialanchor.cpp, line 276, as _ZN23QQuick3DXrSpatialAnchor23setClassificationStringERK7QString
inline void QQuick3DXrSpatialAnchor::setClassificationString(const QString &newClassificationString)
{
    if (m_classificationString == newClassificationString)
        return;
    m_classificationString = newClassificationString;
    emit classificationStringChanged();
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrspatialanchor.cpp, line 297, as _ZNK23QQuick3DXrSpatialAnchor11has2DBoundsEv
inline bool QQuick3DXrSpatialAnchor::has2DBounds() const
{
    return m_has2DBounds;
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrspatialanchor.cpp, line 302, as _ZN23QQuick3DXrSpatialAnchor11setBounds2DERK9QVector2DS2_
inline void QQuick3DXrSpatialAnchor::setBounds2D(const QVector2D &offset, const QVector2D &extent)
{
    if (qFuzzyCompare(m_offset2D, offset) && qFuzzyCompare(m_extent2D, extent))
        return;

    m_offset2D = offset;
    m_extent2D = extent;

    // FIXME: verify
    m_has2DBounds = true;

    emit has2DBoundsChanged();
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrspatialanchor.cpp, line 330, as _ZNK23QQuick3DXrSpatialAnchor11has3DBoundsEv
inline bool QQuick3DXrSpatialAnchor::has3DBounds() const
{
    return m_has3DBounds;
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrspatialanchor.cpp, line 335, as _ZN23QQuick3DXrSpatialAnchor11setBounds3DERK9QVector3DS2_
inline void QQuick3DXrSpatialAnchor::setBounds3D(const QVector3D &offset, const QVector3D &extent)
{
    if (qFuzzyCompare(m_offset3D, offset) && qFuzzyCompare(m_extent3D, extent))
        return;

    m_offset3D = offset;
    m_extent3D = extent;

    // FIXME: Store the 3D bounds and verify
    m_has3DBounds = true;

    emit has3DBoundsChanged();
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrspatialanchor.cpp, line 360, as _ZNK23QQuick3DXrSpatialAnchor8offset2DEv
inline QVector2D QQuick3DXrSpatialAnchor::offset2D() const
{
    return m_offset2D;
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrspatialanchor.cpp, line 376, as _ZNK23QQuick3DXrSpatialAnchor8extent2DEv
inline QVector2D QQuick3DXrSpatialAnchor::extent2D() const
{
    return m_extent2D;
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrspatialanchor.cpp, line 390, as _ZNK23QQuick3DXrSpatialAnchor10identifierEv
inline QString QQuick3DXrSpatialAnchor::identifier() const
{
    return QString::fromLatin1(m_uuid.toRfc4122());
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrspatialanchor.cpp, line 395, as _ZNK23QQuick3DXrSpatialAnchor15roomLayoutUuidsEv
inline QSet<QUuid> QQuick3DXrSpatialAnchor::roomLayoutUuids() const
{
    return m_roomLayoutUuids;
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrspatialanchor.cpp, line 400, as _ZN23QQuick3DXrSpatialAnchor18setRoomLayoutUuidsERK4QSetI5QUuidE
inline void QQuick3DXrSpatialAnchor::setRoomLayoutUuids(const QSet<QUuid> &newRoomLayoutUuids)
{
    m_roomLayoutUuids = newRoomLayoutUuids;
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrspatialanchor.cpp, line 405, as _ZNK23QQuick3DXrSpatialAnchor19spaceContainerUuidsEv
inline QSet<QUuid> QQuick3DXrSpatialAnchor::spaceContainerUuids() const
{
    return m_spaceContainerUuids;
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrspatialanchor.cpp, line 410, as _ZN23QQuick3DXrSpatialAnchor22setSpaceContainerUuidsERK4QSetI5QUuidE
inline void QQuick3DXrSpatialAnchor::setSpaceContainerUuids(const QSet<QUuid> &newSpaceContainerUuids)
{
    m_spaceContainerUuids = newSpaceContainerUuids;
}
//  -----------------------------------------------------------------------

//  A QQuick3DXrSpatialAnchor that Python can take functions over in. Every QQuick3DXrSpatialAnchor
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DXrSpatialAnchorCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DXrSpatialAnchorCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DXrSpatialAnchorCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DXrSpatialAnchorCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DXrSpatialAnchorCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DXrSpatialAnchorCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DXrSpatialAnchorCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuick3DXrSpatialAnchor : public QQuick3DXrSpatialAnchor {
public:
  using QQuick3DXrSpatialAnchor::QQuick3DXrSpatialAnchor;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
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
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuick3DXrSpatialAnchorCall0 call = reinterpret_cast<CuteQQuick3DXrSpatialAnchorCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuick3DXrSpatialAnchorCall1 call = reinterpret_cast<CuteQQuick3DXrSpatialAnchorCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuick3DXrSpatialAnchorCall2 call = reinterpret_cast<CuteQQuick3DXrSpatialAnchorCall2>(taken[2]);
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
      CuteQQuick3DXrSpatialAnchorCall3 call = reinterpret_cast<CuteQQuick3DXrSpatialAnchorCall3>(taken[3]);
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
      CuteQQuick3DXrSpatialAnchorCall4 call = reinterpret_cast<CuteQQuick3DXrSpatialAnchorCall4>(taken[4]);
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
      CuteQQuick3DXrSpatialAnchorCall5 call = reinterpret_cast<CuteQQuick3DXrSpatialAnchorCall5>(taken[5]);
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
      CuteQQuick3DXrSpatialAnchorCall6 call = reinterpret_cast<CuteQQuick3DXrSpatialAnchorCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuick3DXrSpatialAnchor::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK23QQuick3DXrSpatialAnchor10metaObjectEv(
    const QQuick3DXrSpatialAnchor *self) {
  return self->metaObject();
}

//  void *QQuick3DXrSpatialAnchor::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN23QQuick3DXrSpatialAnchor11qt_metacastEPKc(
    QQuick3DXrSpatialAnchor *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuick3DXrSpatialAnchor::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN23QQuick3DXrSpatialAnchor11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuick3DXrSpatialAnchor *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuick3DXrSpatialAnchor::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN23QQuick3DXrSpatialAnchor2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuick3DXrSpatialAnchor::tr(s, c, n));
}

//  void QQuick3DXrSpatialAnchor::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DXrSpatialAnchor24qt_qmlMarker_uncreatableEv(
    QQuick3DXrSpatialAnchor *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QQuick3DXrSpatialAnchor::QQuick3DXrSpatialAnchor(QtQuick3DXr::XrSpaceId
//      space, QUuid &uuid, QObject *parent)
extern "C" Q_DECL_EXPORT
QQuick3DXrSpatialAnchor *ritual_ZN23QQuick3DXrSpatialAnchorC1EN11QtQuick3DXr9XrSpaceIdER5QUuidP7QObject(
    QtQuick3DXr::XrSpaceId space,
    QUuid *uuid,
    QObject *parent) {
  return new CuteQQuick3DXrSpatialAnchor(space, *uuid, parent);
}

//  QQuick3DXrSpatialAnchor::~QQuick3DXrSpatialAnchor()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DXrSpatialAnchorD1Ev(QQuick3DXrSpatialAnchor *self) {
  delete self;
}

//  QVector3D QQuick3DXrSpatialAnchor::offset3D() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK23QQuick3DXrSpatialAnchor8offset3DEv(
    const QQuick3DXrSpatialAnchor *self) {
  return new QVector3D(self->offset3D());
}

//  void QQuick3DXrSpatialAnchor::setOffset3D(const QVector3D &newOffset)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DXrSpatialAnchor11setOffset3DERK9QVector3D(
    QQuick3DXrSpatialAnchor *self,
    const QVector3D *newOffset) {
  self->setOffset3D(*newOffset);
}

//  QVector3D QQuick3DXrSpatialAnchor::extent3D() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK23QQuick3DXrSpatialAnchor8extent3DEv(
    const QQuick3DXrSpatialAnchor *self) {
  return new QVector3D(self->extent3D());
}

//  void QQuick3DXrSpatialAnchor::setExtent3D(const QVector3D &newExtent)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DXrSpatialAnchor11setExtent3DERK9QVector3D(
    QQuick3DXrSpatialAnchor *self,
    const QVector3D *newExtent) {
  self->setExtent3D(*newExtent);
}

//  QVector3D QQuick3DXrSpatialAnchor::position() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK23QQuick3DXrSpatialAnchor8positionEv(
    const QQuick3DXrSpatialAnchor *self) {
  return new QVector3D(self->position());
}

//  void QQuick3DXrSpatialAnchor::setPosition(const QVector3D &newPosition)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DXrSpatialAnchor11setPositionERK9QVector3D(
    QQuick3DXrSpatialAnchor *self,
    const QVector3D *newPosition) {
  self->setPosition(*newPosition);
}

//  QQuaternion QQuick3DXrSpatialAnchor::rotation() const
extern "C" Q_DECL_EXPORT
QQuaternion *ritual_ZNK23QQuick3DXrSpatialAnchor8rotationEv(
    const QQuick3DXrSpatialAnchor *self) {
  return new QQuaternion(self->rotation());
}

//  void QQuick3DXrSpatialAnchor::setRotation(const QQuaternion &newRotation)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DXrSpatialAnchor11setRotationERK11QQuaternion(
    QQuick3DXrSpatialAnchor *self,
    const QQuaternion *newRotation) {
  self->setRotation(*newRotation);
}

//  Classification QQuick3DXrSpatialAnchor::classification() const
extern "C" Q_DECL_EXPORT
QQuick3DXrSpatialAnchor::Classification ritual_ZNK23QQuick3DXrSpatialAnchor14classificationEv(
    const QQuick3DXrSpatialAnchor *self) {
  return self->classification();
}

//  void QQuick3DXrSpatialAnchor::setClassification(Classification
//      newClassification)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DXrSpatialAnchor17setClassificationENS_14ClassificationE(
    QQuick3DXrSpatialAnchor *self,
    QQuick3DXrSpatialAnchor::Classification newClassification) {
  self->setClassification(newClassification);
}

//  QString QQuick3DXrSpatialAnchor::classificationString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK23QQuick3DXrSpatialAnchor20classificationStringEv(
    const QQuick3DXrSpatialAnchor *self) {
  return new QString(self->classificationString());
}

//  void QQuick3DXrSpatialAnchor::setClassificationString(const QString
//      &newClassificationString)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DXrSpatialAnchor23setClassificationStringERK7QString(
    QQuick3DXrSpatialAnchor *self,
    const QString *newClassificationString) {
  self->setClassificationString(*newClassificationString);
}

//  bool QQuick3DXrSpatialAnchor::has2DBounds() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QQuick3DXrSpatialAnchor11has2DBoundsEv(
    const QQuick3DXrSpatialAnchor *self) {
  return self->has2DBounds();
}

//  void QQuick3DXrSpatialAnchor::setBounds2D(const QVector2D &offset, const
//      QVector2D &extent)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DXrSpatialAnchor11setBounds2DERK9QVector2DS2_(
    QQuick3DXrSpatialAnchor *self,
    const QVector2D *offset,
    const QVector2D *extent) {
  self->setBounds2D(*offset, *extent);
}

//  bool QQuick3DXrSpatialAnchor::has3DBounds() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QQuick3DXrSpatialAnchor11has3DBoundsEv(
    const QQuick3DXrSpatialAnchor *self) {
  return self->has3DBounds();
}

//  void QQuick3DXrSpatialAnchor::setBounds3D(const QVector3D &offset, const
//      QVector3D &extent)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DXrSpatialAnchor11setBounds3DERK9QVector3DS2_(
    QQuick3DXrSpatialAnchor *self,
    const QVector3D *offset,
    const QVector3D *extent) {
  self->setBounds3D(*offset, *extent);
}

//  QVector2D QQuick3DXrSpatialAnchor::offset2D() const
extern "C" Q_DECL_EXPORT
QVector2D *ritual_ZNK23QQuick3DXrSpatialAnchor8offset2DEv(
    const QQuick3DXrSpatialAnchor *self) {
  return new QVector2D(self->offset2D());
}

//  QVector2D QQuick3DXrSpatialAnchor::extent2D() const
extern "C" Q_DECL_EXPORT
QVector2D *ritual_ZNK23QQuick3DXrSpatialAnchor8extent2DEv(
    const QQuick3DXrSpatialAnchor *self) {
  return new QVector2D(self->extent2D());
}

//  QString QQuick3DXrSpatialAnchor::identifier() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK23QQuick3DXrSpatialAnchor10identifierEv(
    const QQuick3DXrSpatialAnchor *self) {
  return new QString(self->identifier());
}

//  QSet<QUuid> QQuick3DXrSpatialAnchor::roomLayoutUuids() const
extern "C" Q_DECL_EXPORT
QSet<QUuid> *ritual_ZNK23QQuick3DXrSpatialAnchor15roomLayoutUuidsEv(
    const QQuick3DXrSpatialAnchor *self) {
  return new QSet<QUuid>(self->roomLayoutUuids());
}

//  void QQuick3DXrSpatialAnchor::setRoomLayoutUuids(const QSet<QUuid>
//      &newRoomLayoutUuids)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DXrSpatialAnchor18setRoomLayoutUuidsERK4QSetI5QUuidE(
    QQuick3DXrSpatialAnchor *self,
    const QSet<QUuid> *newRoomLayoutUuids) {
  self->setRoomLayoutUuids(*newRoomLayoutUuids);
}

//  QSet<QUuid> QQuick3DXrSpatialAnchor::spaceContainerUuids() const
extern "C" Q_DECL_EXPORT
QSet<QUuid> *ritual_ZNK23QQuick3DXrSpatialAnchor19spaceContainerUuidsEv(
    const QQuick3DXrSpatialAnchor *self) {
  return new QSet<QUuid>(self->spaceContainerUuids());
}

//  void QQuick3DXrSpatialAnchor::setSpaceContainerUuids(const QSet<QUuid>
//      &newSpaceContainerUuids)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DXrSpatialAnchor22setSpaceContainerUuidsERK4QSetI5QUuidE(
    QQuick3DXrSpatialAnchor *self,
    const QSet<QUuid> *newSpaceContainerUuids) {
  self->setSpaceContainerUuids(*newSpaceContainerUuids);
}

//  QtQuick3DXr::XrSpaceId QQuick3DXrSpatialAnchor::space() const
extern "C" Q_DECL_EXPORT
QtQuick3DXr::XrSpaceId ritual_ZNK23QQuick3DXrSpatialAnchor5spaceEv(
    const QQuick3DXrSpatialAnchor *self) {
  return self->space();
}

//  void QQuick3DXrSpatialAnchor::offset3DChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DXrSpatialAnchor15offset3DChangedEv(
    QQuick3DXrSpatialAnchor *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DXrSpatialAnchor")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "offset3DChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "offset3DChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DXrSpatialAnchor::extent3DChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DXrSpatialAnchor15extent3DChangedEv(
    QQuick3DXrSpatialAnchor *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DXrSpatialAnchor")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "extent3DChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "extent3DChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DXrSpatialAnchor::positionChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DXrSpatialAnchor15positionChangedEv(
    QQuick3DXrSpatialAnchor *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DXrSpatialAnchor")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "positionChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "positionChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DXrSpatialAnchor::rotationChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DXrSpatialAnchor15rotationChangedEv(
    QQuick3DXrSpatialAnchor *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DXrSpatialAnchor")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "rotationChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "rotationChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DXrSpatialAnchor::classificationChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DXrSpatialAnchor21classificationChangedEv(
    QQuick3DXrSpatialAnchor *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DXrSpatialAnchor")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "classificationChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "classificationChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DXrSpatialAnchor::classificationStringChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DXrSpatialAnchor27classificationStringChangedEv(
    QQuick3DXrSpatialAnchor *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DXrSpatialAnchor")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "classificationStringChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "classificationStringChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DXrSpatialAnchor::has2DBoundsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DXrSpatialAnchor18has2DBoundsChangedEv(
    QQuick3DXrSpatialAnchor *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DXrSpatialAnchor")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "has2DBoundsChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "has2DBoundsChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DXrSpatialAnchor::has3DBoundsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DXrSpatialAnchor18has3DBoundsChangedEv(
    QQuick3DXrSpatialAnchor *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DXrSpatialAnchor")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "has3DBoundsChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "has3DBoundsChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DXrSpatialAnchor::offset2DChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DXrSpatialAnchor15offset2DChangedEv(
    QQuick3DXrSpatialAnchor *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DXrSpatialAnchor")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "offset2DChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "offset2DChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DXrSpatialAnchor::extent2DChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DXrSpatialAnchor15extent2DChangedEv(
    QQuick3DXrSpatialAnchor *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DXrSpatialAnchor")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "extent2DChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "extent2DChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  QUuid QQuick3DXrSpatialAnchor::uuid() const
extern "C" Q_DECL_EXPORT
QUuid *ritual_ZNK23QQuick3DXrSpatialAnchor4uuidEv(
    const QQuick3DXrSpatialAnchor *self) {
  return new QUuid(self->uuid());
}

//  a Python function taken by a CuteQQuick3DXrSpatialAnchor, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuick3DXrSpatialAnchor(
    QQuick3DXrSpatialAnchor *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuick3DXrSpatialAnchor *>(self)->take(key, call);
}

//  QList<QQuick3DXrSpatialAnchor *>::QList()
extern "C" Q_DECL_EXPORT
QList<QQuick3DXrSpatialAnchor *> *ritual_list_make_QQuick3DXrSpatialAnchor_ptr() {
  return new QList<QQuick3DXrSpatialAnchor *>();
}

//  void QList<QQuick3DXrSpatialAnchor *>::append(const
//      QQuick3DXrSpatialAnchor * &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QQuick3DXrSpatialAnchor_ptr(
    QList<QQuick3DXrSpatialAnchor *> *self,
    QQuick3DXrSpatialAnchor *element) {
  self->append(element);
}

//  qsizetype QList<QQuick3DXrSpatialAnchor *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QQuick3DXrSpatialAnchor_ptr(
    const QList<QQuick3DXrSpatialAnchor *> *self) {
  return self->size();
}

//  const QQuick3DXrSpatialAnchor * &QList<QQuick3DXrSpatialAnchor
//      *>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QQuick3DXrSpatialAnchor *ritual_list_at_QQuick3DXrSpatialAnchor_ptr(
    const QList<QQuick3DXrSpatialAnchor *> *self,
    long long index) {
  return self->at(index);
}

//  QList<QQuick3DXrSpatialAnchor *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QQuick3DXrSpatialAnchor_ptr(
    QList<QQuick3DXrSpatialAnchor *> *self) {
  delete self;
}

//  a QSet<QUuid> a ritual of QQuick3DXrSpatialAnchor gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQuick3DXrSpatialAnchor__QSet_QUuid(QSet<QUuid> *self) {
  delete self;
}
