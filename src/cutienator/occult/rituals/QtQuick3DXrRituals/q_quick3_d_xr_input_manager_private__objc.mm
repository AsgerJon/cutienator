//  Written by hand on 2026-11-25 from
//  QtQuick3DXr/6.12.0/QtQuick3DXr/private/qquick3dxrinputmanager_visionos_p.h,
//  Qt 6.12.0, from Qt's source. Kept as it is when the generator runs
//  again. Objective-C++: Qt writes these functions only in
//  'qquick3dxrinputmanager_visionos.mm', for visionOS, and Qt's library
//  has no name for them, so their code is copied here, with the things of
//  the file it needs, which only a compiler of Objective-C++ on Apple's
//  systems reads; 'summon' builds this file there only. Qt's logging
//  category 'lcQuick3DXr' is written out, as it is in qquick3dxrmanager.cpp.
//  An object of ARKit a function takes, as 'ar_data_providers_t', crosses
//  as its address, and the ritual is named as if it took 'void *'.
#include <QtQuick3DXr/6.12.0/QtQuick3DXr/private/qtquick3dxrglobal_p.h>
#if defined(Q_OS_VISIONOS)
#include <QtQuick3DXr/6.12.0/QtQuick3DXr/private/qquick3dxrinputmanager_p.h>
#include <QtQuick3DXr/6.12.0/QtQuick3DXr/private/qquick3dxrinputmanager_visionos_p.h>
#include <QtQuick3DUtils/private/qssgassert_p.h>
#include <QtCore/qloggingcategory.h>
#include <QtCore/qvarlengtharray.h>
#include <QtCore/qjsonobject.h>
#include <QtCore/qjsonarray.h>
#include <QtQuick3D/6.12.0/QtQuick3D/private/qquick3dviewport_p.h>
#include <QtQuick3DXr/6.12.0/QtQuick3DXr/private/qquick3dxrcontroller_p.h>
#include <QtQuick3DXr/6.12.0/QtQuick3DXr/private/qquick3dxrhandinput_p.h>
#include <QtQuick3DXr/6.12.0/QtQuick3DXr/private/qquick3dxractionmapper_p.h>
#include <QtQuick3DUtils/private/qssgutils_p.h>

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.
QT_BEGIN_NAMESPACE

//  from qtquick3d/src/xr/quick3dxr/qquick3dxrmanager.cpp, line 39, as a
//  function, as Q_LOGGING_CATEGORY defines it
inline const QLoggingCategory &lcQuick3DXr()
{
    static const QLoggingCategory category("qt.quick3d.xr");
    return category;
}

//  from qtquick3d/src/xr/quick3dxr/visionos/qquick3dxrinputmanager_visionos.mm, line 162
using HandJointList = QVarLengthArray<ar_hand_skeleton_joint_name_t, 28>;

//  line 164
inline const HandJointList &getJointNameTable()
{
    // NOTE: "Joints" are placed in the order from the forarm to the fingers (This might differ from Apple's documentation),
    // moving from the wrist to the finger tips going from the left to the right.
    // That means the forarm is at position 0, and the wrist is at position 1 (this is the origin).

    static const HandJointList jointNames {
        ar_hand_skeleton_joint_name_forearm_arm, // This is the forearm.

        // These are technically the same joint, but depends on the orientation of the hand.
        ar_hand_skeleton_joint_name_wrist, // This is the actual wrist.
        ar_hand_skeleton_joint_name_forearm_wrist,

        // The thumb.
        ar_hand_skeleton_joint_name_thumb_knuckle,
        ar_hand_skeleton_joint_name_thumb_intermediate_base,
        ar_hand_skeleton_joint_name_thumb_intermediate_tip,
        ar_hand_skeleton_joint_name_thumb_tip,

        // The index finger.
        ar_hand_skeleton_joint_name_index_finger_metacarpal,
        ar_hand_skeleton_joint_name_index_finger_knuckle,
        ar_hand_skeleton_joint_name_index_finger_intermediate_base,
        ar_hand_skeleton_joint_name_index_finger_intermediate_tip,
        ar_hand_skeleton_joint_name_index_finger_tip,

        // The middle finger.
        ar_hand_skeleton_joint_name_middle_finger_metacarpal,
        ar_hand_skeleton_joint_name_middle_finger_knuckle,
        ar_hand_skeleton_joint_name_middle_finger_intermediate_base,
        ar_hand_skeleton_joint_name_middle_finger_intermediate_tip,
        ar_hand_skeleton_joint_name_middle_finger_tip,

        // The ring finger.
        ar_hand_skeleton_joint_name_ring_finger_metacarpal,
        ar_hand_skeleton_joint_name_ring_finger_knuckle,
        ar_hand_skeleton_joint_name_ring_finger_intermediate_base,
        ar_hand_skeleton_joint_name_ring_finger_intermediate_tip,
        ar_hand_skeleton_joint_name_ring_finger_tip,

        // The little finger.
        ar_hand_skeleton_joint_name_little_finger_metacarpal,
        ar_hand_skeleton_joint_name_little_finger_knuckle,
        ar_hand_skeleton_joint_name_little_finger_intermediate_base,
        ar_hand_skeleton_joint_name_little_finger_intermediate_tip,
        ar_hand_skeleton_joint_name_little_finger_tip,
    };

    return jointNames;
}

//  line 215
static qsizetype getJointIndex(ar_hand_skeleton_joint_name_t jointName)
{
    qsizetype index = -1;
    const auto &jointNames = getJointNameTable();
    for (size_t i = 0, e = jointNames.size(); i != e && index == -1; ++i) {
        if (jointNames[i] == jointName)
             index = i;
     }

    return index;
}

//  line 56
inline void QQuick3DXrInputManagerPrivate::initHandtracking()
{
    if (m_isHandTrackingSupported) {
        m_handAnchors[uint(Handedness::Left)] = ar_hand_anchor_create();
        m_handAnchors[uint(Handedness::Right)] = ar_hand_anchor_create();
        m_initialized = true;
    }

    qCDebug(lcQuick3DXr) << Q_FUNC_INFO << ", Initialized: " << m_initialized;
}

//  line 319
inline qsizetype QQuick3DXrInputManagerPrivate::getPokeJointIndex() const
{
    // NOTE: Static for now...
    static const qsizetype idx = getJointIndex(ar_hand_skeleton_joint_name_index_finger_tip);
    return idx;
}


//  from qtquick3d/src/xr/quick3dxr/visionos/qquick3dxrinputmanager_visionos.mm
//  line 403
inline void QQuick3DXrInputManagerPrivate::processSpatialEvents(const QQuick3DViewport &vrViewport, const QJsonObject &events)
{
  // An example of the input data
  // {
  //     "id":4404736049417834088,
  //     "inputDevicePose": {
  //         "altitude":0,
  //         "azimuth":1.5707963267948966,
  //         "pose3D":{
  //             "position":{
  //                 "x":0.227996826171875,
  //                 "y":0.957000732421875,
  //                 "z":-0.55999755859375
  //             },
  //             "rotation":{
  //                 "vector":[0,0,0,1]
  //             }
  //         }
  //     },
  //     "kind":"indirectPinch",
  //     "location":[0,0],
  //     "location3D":{
  //         "x":0,
  //         "y":0,
  //         "z":0
  //     },
  //     "modifierKeys":0,
  //     "phase":"ended",
  //     "selectionRay":{
  //         "direction":{
  //             "x":0.3321685791015625,
  //             "y":0.25982666015625,
  //             "z":-0.9067230224609375
  //         },
  //         "origin":{
  //             "x":0.227996826171875,
  //             "y":0.957000732421875,
  //             "z":0
  //         }
  //     },
  //     "timestamp":74368.590710375
  // }

    static qint64 lastId = -1;

    QJsonArray eventArray = events.value(QStringLiteral("events")).toArray();
    for (const auto &event : eventArray) {
        QJsonObject eventObj = event.toObject();
        // qDebug() << eventObj;

        // ID (unique per event)
        const qint64 id = eventObj.value(QStringLiteral("id")).toDouble();
        // timestamp (in seconds)
        //const double timestamp = eventObj.value(QStringLiteral("timestamp")).toDouble();
        // kind
        const QString kind = eventObj.value(QStringLiteral("kind")).toString();
        if (kind != QStringLiteral("indirectPinch"))
            qWarning() << "kind is " << kind << "!";


        // phase
        const QString phase = eventObj.value(QStringLiteral("phase")).toString();

        // selectionRay (check if exists first)
        QJsonObject selectionRayObj = eventObj.value(QStringLiteral("selectionRay")).toObject();
        if (!selectionRayObj.isEmpty()) {
            // origin
            QJsonObject originObj = selectionRayObj.value(QStringLiteral("origin")).toObject();
            QVector3D origin(originObj.value(QStringLiteral("x")).toDouble(), originObj.value(QStringLiteral("y")).toDouble(), originObj.value(QStringLiteral("z")).toDouble());
            // convert meters to cm
            origin *= 100.0;

            // direction
            QJsonObject directionObj = selectionRayObj.value(QStringLiteral("direction")).toObject();
            QVector3D direction(directionObj.value(QStringLiteral("x")).toDouble(), directionObj.value(QStringLiteral("y")).toDouble(), directionObj.value(QStringLiteral("z")).toDouble());

            QEvent::Type eventType;

            if (phase == QStringLiteral("active")) {
                if (lastId != id) {
                    // Press
                    lastId = id;
                    eventType = QEvent::MouseButtonPress;
                } else {
                    // Move
                    eventType = QEvent::MouseMove;
                }
            } else {
                // Release
                lastId = -1;
                eventType = QEvent::MouseButtonRelease;
            }

            QMouseEvent *event = new QMouseEvent(eventType, QPointF(), QPointF(), Qt::LeftButton, Qt::LeftButton, Qt::NoModifier);
            vrViewport.processPointerEventFromRay(origin, direction, event);
            delete event;
        }
    }
}

//  from qtquick3d/src/xr/quick3dxr/visionos/qquick3dxrinputmanager_visionos.mm, line 40
inline void QQuick3DXrInputManagerPrivate::prepareHandtracking(ar_data_providers_t dataProviders)
{
    QSSG_ASSERT_X(!m_initialized, "Handtracking is already initialized!", return);

    m_isHandTrackingSupported = ar_hand_tracking_provider_is_supported();
    if (m_isHandTrackingSupported) {
        ar_hand_tracking_configuration_t handTrackingConfiguration = ar_hand_tracking_configuration_create();
        m_handTrackingProvider = ar_hand_tracking_provider_create(handTrackingConfiguration);
        ar_data_providers_add_data_provider(dataProviders, m_handTrackingProvider);
    } else {
        qCWarning(lcQuick3DXr, "Handtracking is not supported on this device!");
    }

    qCDebug(lcQuick3DXr) << Q_FUNC_INFO << ", Handtracking supported: " << m_isHandTrackingSupported;
}
QT_END_NAMESPACE
//  ---------------------------------------------------------------------

//  void QQuick3DXrInputManagerPrivate::initHandtracking()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQuick3DXrInputManagerPrivate16initHandtrackingEv(
    QQuick3DXrInputManagerPrivate *self) {
  self->initHandtracking();
}

//  qsizetype QQuick3DXrInputManagerPrivate::getPokeJointIndex() const
//  Its row is in 'q_quick3_d_xr_input_manager_private.json', whose
//  ritual of the name stands for the other systems: a name has one row.
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK29QQuick3DXrInputManagerPrivate17getPokeJointIndexEv(
    const QQuick3DXrInputManagerPrivate *self) {
  return self->getPokeJointIndex();
}

//  void QQuick3DXrInputManagerPrivate::processSpatialEvents(const
//      QQuick3DViewport &vrViewport, const QJsonObject &events)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQuick3DXrInputManagerPrivate20processSpatialEventsERK16QQuick3DViewportRK11QJsonObject(
    QQuick3DXrInputManagerPrivate *self,
    const QQuick3DViewport *vrViewport,
    const QJsonObject *events) {
  self->processSpatialEvents(*vrViewport, *events);
}

//  void QQuick3DXrInputManagerPrivate::prepareHandtracking(
//      ar_data_providers_t dataProviders)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQuick3DXrInputManagerPrivate19prepareHandtrackingEPv(
    QQuick3DXrInputManagerPrivate *self,
    void *dataProviders) {
  self->prepareHandtracking((ar_data_providers_t)dataProviders);
}

#endif
