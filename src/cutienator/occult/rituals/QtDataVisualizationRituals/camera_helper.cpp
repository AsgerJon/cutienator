//  Written by dev_tooling.RitualGenerator from the records of
//  QtDataVisualization/6.12.0/QtDataVisualization/private/camerahelper_p.h,
//  Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for 'CameraHelper' is pasted
//  in, cut from what the moc of Qt 6.12.0 writes for its header: Qt's
//  library keeps it to itself; added are 2 rituals that lean on what moc
//  writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/datavisualizationglobal_p.h>
#include <QtDataVisualization/QtDataVisualization>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/camerahelper_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qpoint.h>
#include <QtGui/qvectornd.h>
#include <QtGui/qmatrix4x4.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtDataVisualization/private/camerahelper_p.h>
#include <QtCore/qmath.h>
#include <QtGui/QMatrix4x4>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from QtDataVisualization__CameraHelper.cpp, line 1, as moc:CameraHelper
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN12CameraHelperE_t {};
} // unnamed namespace

template <> constexpr inline auto CameraHelper::qt_create_metaobjectdata<qt_meta_tag_ZN12CameraHelperE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "CameraHelper"
    };

    QtMocHelpers::UintData qt_methods {
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<CameraHelper, qt_meta_tag_ZN12CameraHelperE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject CameraHelper::staticMetaObject = { {
    QMetaObject::SuperData::link<QObject::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN12CameraHelperE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN12CameraHelperE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN12CameraHelperE_t>.metaTypes,
    nullptr
} };

void CameraHelper::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<CameraHelper *>(_o);
    (void)_t;
    (void)_c;
    (void)_id;
    (void)_a;
}

const QMetaObject *CameraHelper::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *CameraHelper::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN12CameraHelperE_t>.strings))
        return static_cast<void*>(this);
    return QObject::qt_metacast(_clname);
}

int CameraHelper::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QObject::qt_metacall(_c, _id, _a);
    return _id;
}
QT_WARNING_POP

//  from ../qtdatavis3d/src/datavisualization/utils/camerahelper.cpp, line 11, as _ZN12CameraHelperC1EP7QObject
inline CameraHelper::CameraHelper(QObject *parent) :
    QObject(parent),
    m_position(0, 0.25, 3),
    m_target(0, 0, 0),
    m_up(0, 1, 0),
    m_previousMousePos(0,0),
    m_xRotation(0),
    m_yRotation(0),
    m_defaultXRotation(0),
    m_defaultYRotation(0),
    m_rotationSpeed(100)
{
}

//  from ../qtdatavis3d/src/datavisualization/utils/camerahelper.cpp, line 25, as _ZN12CameraHelperD1Ev
inline CameraHelper::~CameraHelper()
{
}

//  from ../qtdatavis3d/src/datavisualization/utils/camerahelper.cpp, line 29, as _ZN12CameraHelper16setRotationSpeedEi
inline void CameraHelper::setRotationSpeed(int speed)
{
    // increase for faster rotation
    m_rotationSpeed = speed;
}

//  from ../qtdatavis3d/src/datavisualization/utils/camerahelper.cpp, line 35, as _ZN12CameraHelper17setCameraRotationERK7QPointF
inline void CameraHelper::setCameraRotation(const QPointF &rotation)
{
    m_xRotation = rotation.x();
    m_defaultXRotation = m_xRotation;
    m_yRotation = rotation.y();
    m_defaultYRotation = m_yRotation;
}

//  from ../qtdatavis3d/src/datavisualization/utils/camerahelper.cpp, line 132, as _ZN12CameraHelper18getCameraRotationsEv
inline QPointF CameraHelper::getCameraRotations()
{
    QPointF rotations(m_xRotation, m_yRotation);
    return rotations;
}

//  from ../qtdatavis3d/src/datavisualization/utils/camerahelper.cpp, line 43, as _ZN12CameraHelper27setDefaultCameraOrientationERK9QVector3DS2_S2_
inline void CameraHelper::setDefaultCameraOrientation(const QVector3D &defaultPosition,
                                               const QVector3D &defaultTarget,
                                               const QVector3D &defaultUp)
{
    m_position = defaultPosition;
    m_target = defaultTarget;
    m_up = defaultUp;
}

//  from ../qtdatavis3d/src/datavisualization/utils/camerahelper.cpp, line 52, as _ZN12CameraHelper19calculateViewMatrixERK6QPointiiib
inline QMatrix4x4 CameraHelper::calculateViewMatrix(const QPoint &mousePos, int zoom,
                                             int screenWidth, int screenHeight, bool showUnder)
{
    QMatrix4x4 viewMatrix;
    GLfloat lowerLimit = 0.0f;

    if (showUnder)
        lowerLimit = -90.0f;

    // Calculate mouse movement since last frame
    GLfloat mouseMoveX = GLfloat(m_previousMousePos.x() - mousePos.x())
            / (screenWidth / m_rotationSpeed);
    GLfloat mouseMoveY = GLfloat(m_previousMousePos.y() - mousePos.y())
            / (screenHeight / m_rotationSpeed);
    // Apply to rotations
    m_xRotation -= mouseMoveX;
    m_yRotation -= mouseMoveY;
    // Reset at 360 in x and limit to 0...90 in y
    if (qAbs(m_xRotation) >= 360.0f)
        m_xRotation = 0.0f;
    if (m_yRotation >= 90.0f)
        m_yRotation = 90.0f;
    else if (m_yRotation <= lowerLimit)
        m_yRotation = lowerLimit;

    // Apply to view matrix
    viewMatrix.lookAt(m_position, m_target, m_up);
    // Compensate for translation (if m_target is off origin)
    viewMatrix.translate(m_target.x(), m_target.y(), m_target.z());
    // Apply rotations
    // Handle x and z rotation when y -angle is other than 0
    viewMatrix.rotate(m_xRotation, 0, qCos(qDegreesToRadians(m_yRotation)),
                      qSin(qDegreesToRadians(m_yRotation)));
    // y rotation is always "clean"
    viewMatrix.rotate(m_yRotation, 1.0f, 0.0f, 0.0f);
    // handle zoom by scaling
    viewMatrix.scale((GLfloat)zoom / 100.0f);
    // Compensate for translation (if m_target is off origin)
    viewMatrix.translate(-m_target.x(), -m_target.y(), -m_target.z());

    m_previousMousePos = mousePos;
    return viewMatrix;
}

//  from ../qtdatavis3d/src/datavisualization/utils/camerahelper.cpp, line 96, as _ZN12CameraHelper22calculateLightPositionERK9QVector3Dff
inline QVector3D CameraHelper::calculateLightPosition(const QVector3D &lightPosition,
                                               GLfloat fixedRotation, GLfloat distanceModifier)
{
    // Move light with camera
    QVector3D newLightPosition;
    GLfloat radiusFactor = lightPosition.z() * (1.5f + distanceModifier); // for making sure light is outside the scene at its lowest point
    GLfloat xAngle;
    GLfloat yAngle;
    if (!fixedRotation) {
        xAngle = qDegreesToRadians(m_xRotation);
        yAngle = qDegreesToRadians(m_yRotation);
    } else {
        xAngle = qDegreesToRadians(fixedRotation);
        yAngle = 0;
    }
    GLfloat radius = (radiusFactor + lightPosition.y()); // set radius to match the highest height of the light
    GLfloat zPos = radius * qCos(xAngle) * qCos(yAngle);
    GLfloat xPos = radius * qSin(xAngle) * qCos(yAngle);
    GLfloat yPos = (radiusFactor + lightPosition.y()) * qSin(yAngle);
    // Keep light in the set position in relation to camera
    newLightPosition = QVector3D(-xPos + lightPosition.x(),
                                 yPos + lightPosition.y(),
                                 zPos + lightPosition.z());
    return newLightPosition;
}

//  from ../qtdatavis3d/src/datavisualization/utils/camerahelper.cpp, line 122, as _ZN12CameraHelper14updateMousePosERK6QPoint
inline void CameraHelper::updateMousePos(const QPoint &mousePos)
{
    m_previousMousePos = mousePos;
    // if mouse position is set to (0, 0), reset rotations
    if (QPoint(0, 0) == mousePos) {
        m_xRotation = m_defaultXRotation;
        m_yRotation = m_defaultYRotation;
    }
}

//  from ../qtdatavis3d/src/datavisualization/utils/camerahelper.cpp, line 138, as _ZN12CameraHelper15setCameraPresetEN9Q3DCamera12CameraPresetE
inline void CameraHelper::setCameraPreset(Q3DCamera::CameraPreset preset)
{
    switch (preset) {
    case Q3DCamera::CameraPresetFrontLow: {
        CameraHelper::setCameraRotation(QPointF(0.0f, 0.0f));
        break;
    }
    case Q3DCamera::CameraPresetFront: {
        CameraHelper::setCameraRotation(QPointF(0.0f, 22.5f));
        break;
    }
    case Q3DCamera::CameraPresetFrontHigh: {
        CameraHelper::setCameraRotation(QPointF(0.0f, 45.0f));
        break;
    }
    case Q3DCamera::CameraPresetLeftLow: {
        CameraHelper::setCameraRotation(QPointF(90.0f, 0.0f));
        break;
    }
    case Q3DCamera::CameraPresetLeft: {
        CameraHelper::setCameraRotation(QPointF(90.0f, 22.5f));
        break;
    }
    case Q3DCamera::CameraPresetLeftHigh: {
        CameraHelper::setCameraRotation(QPointF(90.0f, 45.0f));
        break;
    }
    case Q3DCamera::CameraPresetRightLow: {
        CameraHelper::setCameraRotation(QPointF(-90.0f, 0.0f));
        break;
    }
    case Q3DCamera::CameraPresetRight: {
        CameraHelper::setCameraRotation(QPointF(-90.0f, 22.5f));
        break;
    }
    case Q3DCamera::CameraPresetRightHigh: {
        CameraHelper::setCameraRotation(QPointF(-90.0f, 45.0f));
        break;
    }
    case Q3DCamera::CameraPresetBehindLow: {
        CameraHelper::setCameraRotation(QPointF(180.0f, 0.0f));
        break;
    }
    case Q3DCamera::CameraPresetBehind: {
        CameraHelper::setCameraRotation(QPointF(180.0f, 22.5f));
        break;
    }
    case Q3DCamera::CameraPresetBehindHigh: {
        CameraHelper::setCameraRotation(QPointF(180.0f, 45.0f));
        break;
    }
    case Q3DCamera::CameraPresetIsometricLeft: {
        CameraHelper::setCameraRotation(QPointF(45.0f, 22.5f));
        break;
    }
    case Q3DCamera::CameraPresetIsometricLeftHigh: {
        CameraHelper::setCameraRotation(QPointF(45.0f, 45.0f));
        break;
    }
    case Q3DCamera::CameraPresetIsometricRight: {
        CameraHelper::setCameraRotation(QPointF(-45.0f, 22.5f));
        break;
    }
    case Q3DCamera::CameraPresetIsometricRightHigh: {
        CameraHelper::setCameraRotation(QPointF(-45.0f, 45.0f));
        break;
    }
    case Q3DCamera::CameraPresetDirectlyAbove: {
        CameraHelper::setCameraRotation(QPointF(0.0f, 90.0f));
        break;
    }
    case Q3DCamera::CameraPresetDirectlyAboveCW45: {
        CameraHelper::setCameraRotation(QPointF(-45.0f, 90.0f));
        break;
    }
    case Q3DCamera::CameraPresetDirectlyAboveCCW45: {
        CameraHelper::setCameraRotation(QPointF(45.0f, 90.0f));
        break;
    }
    case Q3DCamera::CameraPresetFrontBelow: {
        CameraHelper::setCameraRotation(QPointF(0.0f, -45.0f));
        break;
    }
    case Q3DCamera::CameraPresetLeftBelow: {
        CameraHelper::setCameraRotation(QPointF(90.0f, -45.0f));
        break;
    }
    case Q3DCamera::CameraPresetRightBelow: {
        CameraHelper::setCameraRotation(QPointF(-90.0f, -45.0f));
        break;
    }
    case Q3DCamera::CameraPresetBehindBelow: {
        CameraHelper::setCameraRotation(QPointF(180.0f, -45.0f));
        break;
    }
    case Q3DCamera::CameraPresetDirectlyBelow: {
        CameraHelper::setCameraRotation(QPointF(0.0f, -90.0f));
        break;
    }
    default:
        break;
    }
}
//  -----------------------------------------------------------------------

//  A CameraHelper that Python can take functions over in. Every CameraHelper
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteCameraHelperCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteCameraHelperCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteCameraHelperCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteCameraHelperCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteCameraHelperCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteCameraHelperCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteCameraHelperCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteCameraHelper : public CameraHelper {
public:
  using CameraHelper::CameraHelper;
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
      CuteCameraHelperCall0 call = reinterpret_cast<CuteCameraHelperCall0>(taken[0]);
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
      CuteCameraHelperCall1 call = reinterpret_cast<CuteCameraHelperCall1>(taken[1]);
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
      CuteCameraHelperCall2 call = reinterpret_cast<CuteCameraHelperCall2>(taken[2]);
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
      CuteCameraHelperCall3 call = reinterpret_cast<CuteCameraHelperCall3>(taken[3]);
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
      CuteCameraHelperCall4 call = reinterpret_cast<CuteCameraHelperCall4>(taken[4]);
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
      CuteCameraHelperCall5 call = reinterpret_cast<CuteCameraHelperCall5>(taken[5]);
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
      CuteCameraHelperCall6 call = reinterpret_cast<CuteCameraHelperCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *CameraHelper::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK12CameraHelper10metaObjectEv(
    const CameraHelper *self) {
  return self->metaObject();
}

//  void *CameraHelper::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN12CameraHelper11qt_metacastEPKc(
    CameraHelper *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int CameraHelper::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN12CameraHelper11qt_metacallEN11QMetaObject4CallEiPPv(
    CameraHelper *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString CameraHelper::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12CameraHelper2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(CameraHelper::tr(s, c, n));
}

//  CameraHelper::CameraHelper(QObject *parent)
extern "C" Q_DECL_EXPORT
CameraHelper *ritual_ZN12CameraHelperC1EP7QObject(QObject *parent) {
  return new CuteCameraHelper(parent);
}

//  CameraHelper::~CameraHelper()
extern "C" Q_DECL_EXPORT
void ritual_ZN12CameraHelperD1Ev(CameraHelper *self) {
  delete self;
}

//  void CameraHelper::setRotationSpeed(int speed)
extern "C" Q_DECL_EXPORT
void ritual_ZN12CameraHelper16setRotationSpeedEi(
    CameraHelper *self,
    int speed) {
  self->setRotationSpeed(speed);
}

//  void CameraHelper::setCameraRotation(const QPointF &rotation)
extern "C" Q_DECL_EXPORT
void ritual_ZN12CameraHelper17setCameraRotationERK7QPointF(
    CameraHelper *self,
    const QPointF *rotation) {
  self->setCameraRotation(*rotation);
}

//  QPointF CameraHelper::getCameraRotations()
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZN12CameraHelper18getCameraRotationsEv(CameraHelper *self) {
  return new QPointF(self->getCameraRotations());
}

//  void CameraHelper::setDefaultCameraOrientation(const QVector3D
//      &defaultPosition, const QVector3D &defaultTarget, const QVector3D
//      &defaultUp)
extern "C" Q_DECL_EXPORT
void ritual_ZN12CameraHelper27setDefaultCameraOrientationERK9QVector3DS2_S2_(
    CameraHelper *self,
    const QVector3D *defaultPosition,
    const QVector3D *defaultTarget,
    const QVector3D *defaultUp) {
  self->setDefaultCameraOrientation(
      *defaultPosition,
      *defaultTarget,
      *defaultUp);
}

//  QMatrix4x4 CameraHelper::calculateViewMatrix(const QPoint &mousePos, int
//      zoom, int screenWidth, int screenHeight, bool showUnder)
extern "C" Q_DECL_EXPORT
QMatrix4x4 *ritual_ZN12CameraHelper19calculateViewMatrixERK6QPointiiib(
    CameraHelper *self,
    const QPoint *mousePos,
    int zoom,
    int screenWidth,
    int screenHeight,
    bool showUnder) {
  return new QMatrix4x4(
      self->calculateViewMatrix(
          *mousePos,
          zoom,
          screenWidth,
          screenHeight,
          showUnder));
}

//  QVector3D CameraHelper::calculateLightPosition(const QVector3D
//      &lightPosition, GLfloat fixedRotation, GLfloat distanceModifier)
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZN12CameraHelper22calculateLightPositionERK9QVector3Dff(
    CameraHelper *self,
    const QVector3D *lightPosition,
    GLfloat fixedRotation,
    GLfloat distanceModifier) {
  return new QVector3D(
      self->calculateLightPosition(
          *lightPosition,
          fixedRotation,
          distanceModifier));
}

//  void CameraHelper::updateMousePos(const QPoint &mousePos)
extern "C" Q_DECL_EXPORT
void ritual_ZN12CameraHelper14updateMousePosERK6QPoint(
    CameraHelper *self,
    const QPoint *mousePos) {
  self->updateMousePos(*mousePos);
}

//  void CameraHelper::setCameraPreset(Q3DCamera::CameraPreset preset)
extern "C" Q_DECL_EXPORT
void ritual_ZN12CameraHelper15setCameraPresetEN9Q3DCamera12CameraPresetE(
    CameraHelper *self,
    Q3DCamera::CameraPreset preset) {
  self->setCameraPreset(preset);
}

//  a Python function taken by a CuteCameraHelper, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_CameraHelper(
    CameraHelper *self,
    const char *key,
    void *call) {
  return static_cast<CuteCameraHelper *>(self)->take(key, call);
}
