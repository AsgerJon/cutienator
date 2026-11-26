//  Written by dev_tooling.RitualGenerator from the records of
//  QtDataVisualization/6.12.0/QtDataVisualization/private/q3dcamera_p.h, Qt
//  6.12.0.
//  Edited by hand on 2026-11-26: moc's output for 'Q3DCameraPrivate' is
//  pasted in, cut from what the moc of Qt 6.12.0 writes for its header: Qt's
//  library keeps it to itself; added are 9 rituals that lean on what moc
//  writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/datavisualizationglobal_p.h>
#include <QtDataVisualization/QtDataVisualization>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/q3dcamera_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qmatrix4x4.h>
#include <QtGui/qvectornd.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtDataVisualization/private/q3dcamera_p.h>
#include <QtDataVisualization/private/utils_p.h>
#include <QtCore/qmath.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from QtDataVisualization__Q3DCameraPrivate.cpp, line 1, as moc:Q3DCameraPrivate
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN16Q3DCameraPrivateE_t {};
} // unnamed namespace

template <> constexpr inline auto Q3DCameraPrivate::qt_create_metaobjectdata<qt_meta_tag_ZN16Q3DCameraPrivateE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "Q3DCameraPrivate",
        "minXRotationChanged",
        "",
        "rotation",
        "minYRotationChanged",
        "maxXRotationChanged",
        "maxYRotationChanged",
        "viewMatrixChanged",
        "QMatrix4x4",
        "viewMatrix",
        "viewMatrixAutoUpdateChanged",
        "enabled"
    };

    QtMocHelpers::UintData qt_methods {
        // Signal 'minXRotationChanged'
        QtMocHelpers::SignalData<void(float)>(1, 2, QMC::AccessPublic, QMetaType::Void, {{
            { QMetaType::Float, 3 },
        }}),
        // Signal 'minYRotationChanged'
        QtMocHelpers::SignalData<void(float)>(4, 2, QMC::AccessPublic, QMetaType::Void, {{
            { QMetaType::Float, 3 },
        }}),
        // Signal 'maxXRotationChanged'
        QtMocHelpers::SignalData<void(float)>(5, 2, QMC::AccessPublic, QMetaType::Void, {{
            { QMetaType::Float, 3 },
        }}),
        // Signal 'maxYRotationChanged'
        QtMocHelpers::SignalData<void(float)>(6, 2, QMC::AccessPublic, QMetaType::Void, {{
            { QMetaType::Float, 3 },
        }}),
        // Signal 'viewMatrixChanged'
        QtMocHelpers::SignalData<void(const QMatrix4x4 &)>(7, 2, QMC::AccessPublic, QMetaType::Void, {{
            { 0x80000000 | 8, 9 },
        }}),
        // Signal 'viewMatrixAutoUpdateChanged'
        QtMocHelpers::SignalData<void(bool)>(10, 2, QMC::AccessPublic, QMetaType::Void, {{
            { QMetaType::Bool, 11 },
        }}),
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<Q3DCameraPrivate, qt_meta_tag_ZN16Q3DCameraPrivateE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject Q3DCameraPrivate::staticMetaObject = { {
    QMetaObject::SuperData::link<QObject::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN16Q3DCameraPrivateE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN16Q3DCameraPrivateE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN16Q3DCameraPrivateE_t>.metaTypes,
    nullptr
} };

void Q3DCameraPrivate::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<Q3DCameraPrivate *>(_o);
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: _t->minXRotationChanged((*reinterpret_cast<std::add_pointer_t<float>>(_a[1]))); break;
        case 1: _t->minYRotationChanged((*reinterpret_cast<std::add_pointer_t<float>>(_a[1]))); break;
        case 2: _t->maxXRotationChanged((*reinterpret_cast<std::add_pointer_t<float>>(_a[1]))); break;
        case 3: _t->maxYRotationChanged((*reinterpret_cast<std::add_pointer_t<float>>(_a[1]))); break;
        case 4: _t->viewMatrixChanged((*reinterpret_cast<std::add_pointer_t<QMatrix4x4>>(_a[1]))); break;
        case 5: _t->viewMatrixAutoUpdateChanged((*reinterpret_cast<std::add_pointer_t<bool>>(_a[1]))); break;
        default: ;
        }
    }
    if (_c == QMetaObject::IndexOfMethod) {
        if (QtMocHelpers::indexOfMethod<void (Q3DCameraPrivate::*)(float )>(_a, &Q3DCameraPrivate::minXRotationChanged, 0))
            return;
        if (QtMocHelpers::indexOfMethod<void (Q3DCameraPrivate::*)(float )>(_a, &Q3DCameraPrivate::minYRotationChanged, 1))
            return;
        if (QtMocHelpers::indexOfMethod<void (Q3DCameraPrivate::*)(float )>(_a, &Q3DCameraPrivate::maxXRotationChanged, 2))
            return;
        if (QtMocHelpers::indexOfMethod<void (Q3DCameraPrivate::*)(float )>(_a, &Q3DCameraPrivate::maxYRotationChanged, 3))
            return;
        if (QtMocHelpers::indexOfMethod<void (Q3DCameraPrivate::*)(const QMatrix4x4 & )>(_a, &Q3DCameraPrivate::viewMatrixChanged, 4))
            return;
        if (QtMocHelpers::indexOfMethod<void (Q3DCameraPrivate::*)(bool )>(_a, &Q3DCameraPrivate::viewMatrixAutoUpdateChanged, 5))
            return;
    }
}

const QMetaObject *Q3DCameraPrivate::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *Q3DCameraPrivate::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN16Q3DCameraPrivateE_t>.strings))
        return static_cast<void*>(this);
    return QObject::qt_metacast(_clname);
}

int Q3DCameraPrivate::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QObject::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 6)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 6;
    }
    if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 6)
            *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType();
        _id -= 6;
    }
    return _id;
}

// SIGNAL 0
void Q3DCameraPrivate::minXRotationChanged(float _t1)
{
    QMetaObject::activate<void>(this, &staticMetaObject, 0, nullptr, _t1);
}

// SIGNAL 1
void Q3DCameraPrivate::minYRotationChanged(float _t1)
{
    QMetaObject::activate<void>(this, &staticMetaObject, 1, nullptr, _t1);
}

// SIGNAL 2
void Q3DCameraPrivate::maxXRotationChanged(float _t1)
{
    QMetaObject::activate<void>(this, &staticMetaObject, 2, nullptr, _t1);
}

// SIGNAL 3
void Q3DCameraPrivate::maxYRotationChanged(float _t1)
{
    QMetaObject::activate<void>(this, &staticMetaObject, 3, nullptr, _t1);
}

// SIGNAL 4
void Q3DCameraPrivate::viewMatrixChanged(const QMatrix4x4 & _t1)
{
    QMetaObject::activate<void>(this, &staticMetaObject, 4, nullptr, _t1);
}

// SIGNAL 5
void Q3DCameraPrivate::viewMatrixAutoUpdateChanged(bool _t1)
{
    QMetaObject::activate<void>(this, &staticMetaObject, 5, nullptr, _t1);
}
QT_WARNING_POP

//  from ../qtdatavis3d/src/datavisualization/engine/q3dcamera.cpp, line 612, as _ZN16Q3DCameraPrivateC1EP9Q3DCamera
inline Q3DCameraPrivate::Q3DCameraPrivate(Q3DCamera *q) :
    q_ptr(q),
    m_isViewMatrixUpdateActive(true),
    m_xRotation(0.0f),
    m_yRotation(0.0f),
    m_minXRotation(-180.0f),
    m_minYRotation(0.0f),
    m_maxXRotation(180.0f),
    m_maxYRotation(90.0f),
    m_zoomLevel(100.0f),
    m_minZoomLevel(10.0f),
    m_maxZoomLevel(500.0f),
    m_wrapXRotation(true),
    m_wrapYRotation(false),
    m_activePreset(Q3DCamera::CameraPresetNone)
{
}

//  from ../qtdatavis3d/src/datavisualization/engine/q3dcamera.cpp, line 630, as _ZN16Q3DCameraPrivateD1Ev
inline Q3DCameraPrivate::~Q3DCameraPrivate()
{
}

//  from ../qtdatavis3d/src/datavisualization/engine/q3dcamera.cpp, line 636, as _ZN16Q3DCameraPrivate4syncER9Q3DCamera
inline void Q3DCameraPrivate::sync(Q3DCamera &other)
{
    if (q_ptr->isDirty()) {
        other.copyValuesFrom(*q_ptr);
        q_ptr->setDirty(false);
        other.setDirty(false);
    }
}

//  from ../qtdatavis3d/src/datavisualization/engine/q3dcamera.cpp, line 645, as _ZN16Q3DCameraPrivate12setXRotationEf
inline void Q3DCameraPrivate::setXRotation(const float rotation)
{
    if (m_xRotation != rotation) {
        m_xRotation = rotation;
        q_ptr->setDirty(true);
    }
}

//  from ../qtdatavis3d/src/datavisualization/engine/q3dcamera.cpp, line 653, as _ZN16Q3DCameraPrivate12setYRotationEf
inline void Q3DCameraPrivate::setYRotation(const float rotation)
{
    if (m_yRotation != rotation) {
        m_yRotation = rotation;
        q_ptr->setDirty(true);
    }
}

//  from ../qtdatavis3d/src/datavisualization/engine/q3dcamera.cpp, line 674, as _ZN16Q3DCameraPrivate15setMinXRotationEf
inline void Q3DCameraPrivate::setMinXRotation(float minRotation)
{
    minRotation = qBound(-180.0f, minRotation, 180.0f);
    if (minRotation > m_maxXRotation)
        minRotation = m_maxXRotation;

    if (m_minXRotation != minRotation) {
        m_minXRotation = minRotation;
        emit minXRotationChanged(minRotation);

        if (m_xRotation < m_minXRotation)
            setXRotation(m_xRotation);
        q_ptr->setDirty(true);
    }
}

//  from ../qtdatavis3d/src/datavisualization/engine/q3dcamera.cpp, line 669, as _ZNK16Q3DCameraPrivate12minXRotationEv
inline float Q3DCameraPrivate::minXRotation() const
{
    return m_minXRotation;
}

//  from ../qtdatavis3d/src/datavisualization/engine/q3dcamera.cpp, line 703, as _ZN16Q3DCameraPrivate15setMinYRotationEf
inline void Q3DCameraPrivate::setMinYRotation(float minRotation)
{
    minRotation = qBound(-90.0f, minRotation, 90.0f);
    if (minRotation > m_maxYRotation)
        minRotation = m_maxYRotation;

    if (m_minYRotation != minRotation) {
        m_minYRotation = minRotation;
        emit minYRotationChanged(minRotation);

        if (m_yRotation < m_minYRotation)
            setYRotation(m_yRotation);
        q_ptr->setDirty(true);
    }
}

//  from ../qtdatavis3d/src/datavisualization/engine/q3dcamera.cpp, line 698, as _ZNK16Q3DCameraPrivate12minYRotationEv
inline float Q3DCameraPrivate::minYRotation() const
{
    return m_minYRotation;
}

//  from ../qtdatavis3d/src/datavisualization/engine/q3dcamera.cpp, line 732, as _ZN16Q3DCameraPrivate15setMaxXRotationEf
inline void Q3DCameraPrivate::setMaxXRotation(float maxRotation)
{
    maxRotation = qBound(-180.0f, maxRotation, 180.0f);

    if (maxRotation < m_minXRotation)
        maxRotation = m_minXRotation;

    if (m_maxXRotation != maxRotation) {
        m_maxXRotation = maxRotation;
        emit maxXRotationChanged(maxRotation);

        if (m_xRotation > m_maxXRotation)
            setXRotation(m_xRotation);
        q_ptr->setDirty(true);
    }
}

//  from ../qtdatavis3d/src/datavisualization/engine/q3dcamera.cpp, line 727, as _ZNK16Q3DCameraPrivate12maxXRotationEv
inline float Q3DCameraPrivate::maxXRotation() const
{
    return m_maxXRotation;
}

//  from ../qtdatavis3d/src/datavisualization/engine/q3dcamera.cpp, line 762, as _ZN16Q3DCameraPrivate15setMaxYRotationEf
inline void Q3DCameraPrivate::setMaxYRotation(float maxRotation)
{
    maxRotation = qBound(-90.0f, maxRotation, 90.0f);

    if (maxRotation < m_minYRotation)
        maxRotation = m_minYRotation;

    if (m_maxYRotation != maxRotation) {
        m_maxYRotation = maxRotation;
        emit maxYRotationChanged(maxRotation);

        if (m_yRotation > m_maxYRotation)
            setYRotation(m_yRotation);
        q_ptr->setDirty(true);
    }
}

//  from ../qtdatavis3d/src/datavisualization/engine/q3dcamera.cpp, line 757, as _ZNK16Q3DCameraPrivate12maxYRotationEv
inline float Q3DCameraPrivate::maxYRotation() const
{
    return m_maxYRotation;
}

//  from ../qtdatavis3d/src/datavisualization/engine/q3dcamera.cpp, line 781, as _ZN16Q3DCameraPrivate16updateViewMatrixEf
inline void Q3DCameraPrivate::updateViewMatrix(float zoomAdjustment)
{
    if (!m_isViewMatrixUpdateActive)
        return;

    GLfloat zoom = m_zoomLevel * zoomAdjustment;
    QMatrix4x4 viewMatrix;

    // Apply to view matrix
    viewMatrix.lookAt(q_ptr->position(), m_actualTarget, m_up);
    // Compensate for translation (if d_ptr->m_target is off origin)
    viewMatrix.translate(m_actualTarget.x(), m_actualTarget.y(), m_actualTarget.z());
    // Apply rotations
    // Handle x and z rotation when y -angle is other than 0
    viewMatrix.rotate(m_xRotation, 0, qCos(qDegreesToRadians(m_yRotation)),
                      qSin(qDegreesToRadians(m_yRotation)));
    // y rotation is always "clean"
    viewMatrix.rotate(m_yRotation, 1.0f, 0.0f, 0.0f);
    // handle zoom by scaling
    viewMatrix.scale(zoom / 100.0f);
    // Compensate for translation (if d_ptr->m_target is off origin)
    viewMatrix.translate(-m_actualTarget.x(), -m_actualTarget.y(), -m_actualTarget.z());

    setViewMatrix(viewMatrix);
}

//  from ../qtdatavis3d/src/datavisualization/engine/q3dcamera.cpp, line 815, as _ZNK16Q3DCameraPrivate10viewMatrixEv
inline QMatrix4x4 Q3DCameraPrivate::viewMatrix() const
{
    return m_viewMatrix;
}

//  from ../qtdatavis3d/src/datavisualization/engine/q3dcamera.cpp, line 820, as _ZN16Q3DCameraPrivate13setViewMatrixERK10QMatrix4x4
inline void Q3DCameraPrivate::setViewMatrix(const QMatrix4x4 &viewMatrix)
{
    if (m_viewMatrix != viewMatrix) {
        m_viewMatrix = viewMatrix;
        q_ptr->setDirty(true);
        emit viewMatrixChanged(m_viewMatrix);
    }
}

//  from ../qtdatavis3d/src/datavisualization/engine/q3dcamera.cpp, line 835, as _ZNK16Q3DCameraPrivate29isViewMatrixAutoUpdateEnabledEv
inline bool Q3DCameraPrivate::isViewMatrixAutoUpdateEnabled() const
{
    return m_isViewMatrixUpdateActive;
}

//  from ../qtdatavis3d/src/datavisualization/engine/q3dcamera.cpp, line 840, as _ZN16Q3DCameraPrivate30setViewMatrixAutoUpdateEnabledEb
inline void Q3DCameraPrivate::setViewMatrixAutoUpdateEnabled(bool isEnabled)
{
    m_isViewMatrixUpdateActive = isEnabled;
    emit viewMatrixAutoUpdateChanged(isEnabled);
}

//  from ../qtdatavis3d/src/datavisualization/engine/q3dcamera.cpp, line 854, as _ZN16Q3DCameraPrivate18setBaseOrientationERK9QVector3DS2_S2_
inline void Q3DCameraPrivate::setBaseOrientation(const QVector3D &basePosition,
                                          const QVector3D &target,
                                          const QVector3D &baseUp)
{
    if (q_ptr->position() != basePosition || m_actualTarget != target || m_up != baseUp) {
        q_ptr->setPosition(basePosition);
        m_actualTarget = target;
        m_up = baseUp;
        q_ptr->setDirty(true);
    }
}

//  from ../qtdatavis3d/src/datavisualization/engine/q3dcamera.cpp, line 877, as _ZNK16Q3DCameraPrivate33calculatePositionRelativeToCameraERK9QVector3Dff
inline QVector3D Q3DCameraPrivate::calculatePositionRelativeToCamera(const QVector3D &relativePosition,
                                                              float fixedRotation,
                                                              float distanceModifier) const
{
    // Move the position with camera
    const float radiusFactor = cameraDistance * (1.5f + distanceModifier);
    float xAngle;
    float yAngle;

    if (!fixedRotation) {
        xAngle = qDegreesToRadians(m_xRotation);
        float yRotation = m_yRotation;
        // Light must not be paraller to eye vector, so fudge the y rotation a bit.
        // Note: This needs redoing if we ever allow arbitrary light positioning.
        const float yMargin = 0.1f; // Smaller margins cause weird shadow artifacts on tops of bars
        const float absYRotation = qAbs(yRotation);
        if (absYRotation < 90.0f + yMargin && absYRotation > 90.0f - yMargin) {
            if (yRotation < 0.0f)
                yRotation = -90.0f + yMargin;
            else
                yRotation = 90.0f - yMargin;
        }
        yAngle = qDegreesToRadians(yRotation);
    } else {
        xAngle = qDegreesToRadians(fixedRotation);
        yAngle = 0;
    }
    // Set radius to match the highest height of the position
    const float radius = (radiusFactor + relativePosition.y());
    const float zPos = radius * qCos(xAngle) * qCos(yAngle);
    const float xPos = radius * qSin(xAngle) * qCos(yAngle);
    const float yPos = radius * qSin(yAngle);

    // Keep in the set position in relation to camera
    return QVector3D(-xPos + relativePosition.x(),
                     yPos + relativePosition.y(),
                     zPos + relativePosition.z());
}
//  -----------------------------------------------------------------------

//  A Q3DCameraPrivate that Python can take functions over in. Every Q3DCameraPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQ3DCameraPrivateCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQ3DCameraPrivateCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQ3DCameraPrivateCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQ3DCameraPrivateCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQ3DCameraPrivateCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQ3DCameraPrivateCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQ3DCameraPrivateCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQ3DCameraPrivate : public Q3DCameraPrivate {
public:
  using Q3DCameraPrivate::Q3DCameraPrivate;
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
      CuteQ3DCameraPrivateCall0 call = reinterpret_cast<CuteQ3DCameraPrivateCall0>(taken[0]);
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
      CuteQ3DCameraPrivateCall1 call = reinterpret_cast<CuteQ3DCameraPrivateCall1>(taken[1]);
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
      CuteQ3DCameraPrivateCall2 call = reinterpret_cast<CuteQ3DCameraPrivateCall2>(taken[2]);
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
      CuteQ3DCameraPrivateCall3 call = reinterpret_cast<CuteQ3DCameraPrivateCall3>(taken[3]);
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
      CuteQ3DCameraPrivateCall4 call = reinterpret_cast<CuteQ3DCameraPrivateCall4>(taken[4]);
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
      CuteQ3DCameraPrivateCall5 call = reinterpret_cast<CuteQ3DCameraPrivateCall5>(taken[5]);
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
      CuteQ3DCameraPrivateCall6 call = reinterpret_cast<CuteQ3DCameraPrivateCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Q3DCameraPrivate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16Q3DCameraPrivate10metaObjectEv(
    const Q3DCameraPrivate *self) {
  return self->metaObject();
}

//  void *Q3DCameraPrivate::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN16Q3DCameraPrivate11qt_metacastEPKc(
    Q3DCameraPrivate *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Q3DCameraPrivate::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN16Q3DCameraPrivate11qt_metacallEN11QMetaObject4CallEiPPv(
    Q3DCameraPrivate *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Q3DCameraPrivate::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16Q3DCameraPrivate2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Q3DCameraPrivate::tr(s, c, n));
}

//  Q3DCameraPrivate::Q3DCameraPrivate(Q3DCamera *q)
extern "C" Q_DECL_EXPORT
Q3DCameraPrivate *ritual_ZN16Q3DCameraPrivateC1EP9Q3DCamera(Q3DCamera *q) {
  return new CuteQ3DCameraPrivate(q);
}

//  Q3DCameraPrivate::~Q3DCameraPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN16Q3DCameraPrivateD1Ev(Q3DCameraPrivate *self) {
  delete self;
}

//  void Q3DCameraPrivate::sync(Q3DCamera &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN16Q3DCameraPrivate4syncER9Q3DCamera(
    Q3DCameraPrivate *self,
    Q3DCamera *other) {
  self->sync(*other);
}

//  void Q3DCameraPrivate::setXRotation(float rotation)
extern "C" Q_DECL_EXPORT
void ritual_ZN16Q3DCameraPrivate12setXRotationEf(
    Q3DCameraPrivate *self,
    float rotation) {
  self->setXRotation(rotation);
}

//  void Q3DCameraPrivate::setYRotation(float rotation)
extern "C" Q_DECL_EXPORT
void ritual_ZN16Q3DCameraPrivate12setYRotationEf(
    Q3DCameraPrivate *self,
    float rotation) {
  self->setYRotation(rotation);
}

//  void Q3DCameraPrivate::setMinXRotation(float rotation)
extern "C" Q_DECL_EXPORT
void ritual_ZN16Q3DCameraPrivate15setMinXRotationEf(
    Q3DCameraPrivate *self,
    float rotation) {
  self->setMinXRotation(rotation);
}

//  float Q3DCameraPrivate::minXRotation() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK16Q3DCameraPrivate12minXRotationEv(
    const Q3DCameraPrivate *self) {
  return self->minXRotation();
}

//  void Q3DCameraPrivate::setMinYRotation(float rotation)
extern "C" Q_DECL_EXPORT
void ritual_ZN16Q3DCameraPrivate15setMinYRotationEf(
    Q3DCameraPrivate *self,
    float rotation) {
  self->setMinYRotation(rotation);
}

//  float Q3DCameraPrivate::minYRotation() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK16Q3DCameraPrivate12minYRotationEv(
    const Q3DCameraPrivate *self) {
  return self->minYRotation();
}

//  void Q3DCameraPrivate::setMaxXRotation(float rotation)
extern "C" Q_DECL_EXPORT
void ritual_ZN16Q3DCameraPrivate15setMaxXRotationEf(
    Q3DCameraPrivate *self,
    float rotation) {
  self->setMaxXRotation(rotation);
}

//  float Q3DCameraPrivate::maxXRotation() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK16Q3DCameraPrivate12maxXRotationEv(
    const Q3DCameraPrivate *self) {
  return self->maxXRotation();
}

//  void Q3DCameraPrivate::setMaxYRotation(float rotation)
extern "C" Q_DECL_EXPORT
void ritual_ZN16Q3DCameraPrivate15setMaxYRotationEf(
    Q3DCameraPrivate *self,
    float rotation) {
  self->setMaxYRotation(rotation);
}

//  float Q3DCameraPrivate::maxYRotation() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK16Q3DCameraPrivate12maxYRotationEv(
    const Q3DCameraPrivate *self) {
  return self->maxYRotation();
}

//  void Q3DCameraPrivate::updateViewMatrix(float zoomAdjustment)
extern "C" Q_DECL_EXPORT
void ritual_ZN16Q3DCameraPrivate16updateViewMatrixEf(
    Q3DCameraPrivate *self,
    float zoomAdjustment) {
  self->updateViewMatrix(zoomAdjustment);
}

//  QMatrix4x4 Q3DCameraPrivate::viewMatrix() const
extern "C" Q_DECL_EXPORT
QMatrix4x4 *ritual_ZNK16Q3DCameraPrivate10viewMatrixEv(
    const Q3DCameraPrivate *self) {
  return new QMatrix4x4(self->viewMatrix());
}

//  void Q3DCameraPrivate::setViewMatrix(const QMatrix4x4 &viewMatrix)
extern "C" Q_DECL_EXPORT
void ritual_ZN16Q3DCameraPrivate13setViewMatrixERK10QMatrix4x4(
    Q3DCameraPrivate *self,
    const QMatrix4x4 *viewMatrix) {
  self->setViewMatrix(*viewMatrix);
}

//  bool Q3DCameraPrivate::isViewMatrixAutoUpdateEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16Q3DCameraPrivate29isViewMatrixAutoUpdateEnabledEv(
    const Q3DCameraPrivate *self) {
  return self->isViewMatrixAutoUpdateEnabled();
}

//  void Q3DCameraPrivate::setViewMatrixAutoUpdateEnabled(bool isEnabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN16Q3DCameraPrivate30setViewMatrixAutoUpdateEnabledEb(
    Q3DCameraPrivate *self,
    bool isEnabled) {
  self->setViewMatrixAutoUpdateEnabled(isEnabled);
}

//  void Q3DCameraPrivate::setBaseOrientation(const QVector3D
//      &defaultPosition, const QVector3D &defaultTarget, const QVector3D
//      &defaultUp)
extern "C" Q_DECL_EXPORT
void ritual_ZN16Q3DCameraPrivate18setBaseOrientationERK9QVector3DS2_S2_(
    Q3DCameraPrivate *self,
    const QVector3D *defaultPosition,
    const QVector3D *defaultTarget,
    const QVector3D *defaultUp) {
  self->setBaseOrientation(*defaultPosition, *defaultTarget, *defaultUp);
}

//  QVector3D Q3DCameraPrivate::calculatePositionRelativeToCamera(const
//      QVector3D &relativePosition, float fixedRotation, float
//      distanceModifier) const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK16Q3DCameraPrivate33calculatePositionRelativeToCameraERK9QVector3Dff(
    const Q3DCameraPrivate *self,
    const QVector3D *relativePosition,
    float fixedRotation,
    float distanceModifier) {
  return new QVector3D(
      self->calculatePositionRelativeToCamera(
          *relativePosition,
          fixedRotation,
          distanceModifier));
}

//  void Q3DCameraPrivate::minXRotationChanged(float rotation)
extern "C" Q_DECL_EXPORT
void ritual_ZN16Q3DCameraPrivate19minXRotationChangedEf(
    Q3DCameraPrivate *self,
    float rotation) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "Q3DCameraPrivate")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "minXRotationChanged(float)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "minXRotationChanged(float)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&rotation)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void Q3DCameraPrivate::minYRotationChanged(float rotation)
extern "C" Q_DECL_EXPORT
void ritual_ZN16Q3DCameraPrivate19minYRotationChangedEf(
    Q3DCameraPrivate *self,
    float rotation) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "Q3DCameraPrivate")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "minYRotationChanged(float)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "minYRotationChanged(float)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&rotation)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void Q3DCameraPrivate::maxXRotationChanged(float rotation)
extern "C" Q_DECL_EXPORT
void ritual_ZN16Q3DCameraPrivate19maxXRotationChangedEf(
    Q3DCameraPrivate *self,
    float rotation) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "Q3DCameraPrivate")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "maxXRotationChanged(float)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "maxXRotationChanged(float)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&rotation)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void Q3DCameraPrivate::maxYRotationChanged(float rotation)
extern "C" Q_DECL_EXPORT
void ritual_ZN16Q3DCameraPrivate19maxYRotationChangedEf(
    Q3DCameraPrivate *self,
    float rotation) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "Q3DCameraPrivate")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "maxYRotationChanged(float)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "maxYRotationChanged(float)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&rotation)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void Q3DCameraPrivate::viewMatrixChanged(const QMatrix4x4 &viewMatrix)
extern "C" Q_DECL_EXPORT
void ritual_ZN16Q3DCameraPrivate17viewMatrixChangedERK10QMatrix4x4(
    Q3DCameraPrivate *self,
    const QMatrix4x4 *viewMatrix) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "Q3DCameraPrivate")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "viewMatrixChanged(const QMatrix4x4 &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "viewMatrixChanged(const QMatrix4x4 &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(viewMatrix)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void Q3DCameraPrivate::viewMatrixAutoUpdateChanged(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN16Q3DCameraPrivate27viewMatrixAutoUpdateChangedEb(
    Q3DCameraPrivate *self,
    bool enabled) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "Q3DCameraPrivate")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "viewMatrixAutoUpdateChanged(bool)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "viewMatrixAutoUpdateChanged(bool)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&enabled)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  a Python function taken by a CuteQ3DCameraPrivate, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Q3DCameraPrivate(
    Q3DCameraPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQ3DCameraPrivate *>(self)->take(key, call);
}
