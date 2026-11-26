//  Written by hand on 2026-11-25 from
//  QtQuick3DXr/6.12.0/QtQuick3DXr/private/qquick3dxranchormanager_visionos_p.h,
//  Qt 6.12.0, from Qt's source. Kept as it is when the generator runs
//  again. Objective-C++: Qt writes these functions only in
//  'qquick3dxranchormanager_visionos.mm', for visionOS, and Qt's library
//  has no name for them, so their code is copied here, which only a
//  compiler of Objective-C++ on Apple's systems reads; 'summon' builds
//  this file there only. The signals of the class these emit are moc's
//  code, which moc writes into Qt's library under no name: they are
//  written out as moc writes a signal, with the class's meta-object
//  found through the object and the signal by its name. An object of
//  ARKit a function takes, as 'ar_data_providers_t', crosses as its
//  address, and the ritual is named as if the function took 'void *'.
#include <QtQuick3DXr/6.12.0/QtQuick3DXr/private/qtquick3dxrglobal_p.h>
#if defined(Q_OS_VISIONOS)
#include <QtQuick3DXr/6.12.0/QtQuick3DXr/private/qquick3dxranchormanager_visionos_p.h>
#include <QtQuick3DUtils/private/qssgassert_p.h>
#include <QtQuick3DUtils/private/qssgutils_p.h>
#include <QtQuick3DXr/6.12.0/QtQuick3DXr/private/qquick3dxrspatialanchor_p.h>
#include <QtCore/qreadwritelock.h>

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.
QT_BEGIN_NAMESPACE

//  A signal of the class, as moc writes it: 'QMetaObject::activate' with
//  the class's own meta-object and the signal's index among its signals.
//  Qt's library keeps the meta-object to itself; the object's own
//  'metaObject()' leads to it, and it names the signal's index.
static void qt_emitAnchorManagerSignal(
    QQuick3DXrAnchorManager *sender, const char *signature, void **argv)
{
    const QMetaObject *meta = sender->metaObject();
    while (meta && qstrcmp(meta->className(), "QQuick3DXrAnchorManager"))
        meta = meta->superClass();
    if (!meta)
        qFatal("no meta-object of QQuick3DXrAnchorManager");
    const int index = meta->indexOfSignal(signature);
    if (index < 0)
        qFatal("QQuick3DXrAnchorManager has no signal %s", signature);
    QMetaObject::activate(sender, meta, index - meta->methodOffset(), argv);
}

//  from moc's code for qquick3dxranchormanager_visionos_p.h, line 68
inline void QQuick3DXrAnchorManager::anchorAdded(QQuick3DXrSpatialAnchor *_t1)
{
    void *_a[] = { nullptr, const_cast<void *>(
        reinterpret_cast<const void *>(std::addressof(_t1))) };
    qt_emitAnchorManagerSignal(
        this, "anchorAdded(QQuick3DXrSpatialAnchor*)", _a);
}

//  from moc's code for qquick3dxranchormanager_visionos_p.h, line 69
inline void QQuick3DXrAnchorManager::anchorRemoved(QUuid _t1)
{
    void *_a[] = { nullptr, const_cast<void *>(
        reinterpret_cast<const void *>(std::addressof(_t1))) };
    qt_emitAnchorManagerSignal(this, "anchorRemoved(QUuid)", _a);
}

//  from moc's code for qquick3dxranchormanager_visionos_p.h, line 70
inline void QQuick3DXrAnchorManager::anchorUpdated(QQuick3DXrSpatialAnchor *_t1)
{
    void *_a[] = { nullptr, const_cast<void *>(
        reinterpret_cast<const void *>(std::addressof(_t1))) };
    qt_emitAnchorManagerSignal(
        this, "anchorUpdated(QQuick3DXrSpatialAnchor*)", _a);
}

//  from qtquick3d/src/xr/quick3dxr/visionos/qquick3dxranchormanager_visionos.mm, line 47
inline void QQuick3DXrAnchorManager::removeAnchor(QUuid uuid)
{
    if (QQuick3DXrSpatialAnchor *anchor = m_anchorsByUuid.take(uuid))
        anchor->deleteLater();
    else
        qWarning() << "Anchor not found for removal: " << uuid;

    Q_EMIT anchorRemoved(uuid);
}

//  line 57
inline void QQuick3DXrAnchorManager::updateAnchor(QQuick3DXrSpatialAnchor *anchor)
{
    anchor->moveToThread(qApp->thread());

    Q_EMIT anchorUpdated(anchor);
}

//  from qtquick3d/src/xr/quick3dxr/visionos/qquick3dxranchormanager_visionos.mm, line 64
inline void QQuick3DXrAnchorManager::populateAnchorsList()
{
    m_anchors = m_anchorsByUuid.values();
}

//  line 269
inline void QQuick3DXrAnchorManager::initAnchorManager()
{
    QSSG_ASSERT_X(!m_isInitialized, "Anchor manager already initialized", return);

    m_isInitialized = m_isPlaneDetectionSupported;
}


//  from qtquick3d/src/xr/quick3dxr/visionos/qquick3dxranchormanager_visionos.mm, line 38
inline void QQuick3DXrAnchorManager::addAnchor(QQuick3DXrSpatialAnchor *anchor)
{
    anchor->moveToThread(qApp->thread());

    m_anchorsByUuid.insert(anchor->uuid(), anchor);

    Q_EMIT anchorAdded(anchor);
}

//  lines 69-267
enum class AnchorClassifcation
{
    Unknown = 0,
    NotAvailable,
    Undetermined,
    Wall,
    Ceiling,
    Floor,
    Table,
    Seat,
    Window,
    Door,
};

static constexpr size_t anchorClassificationStart = size_t(AnchorClassifcation::Wall);

struct AnchorClassificationMap {
    ar_plane_classification_t classification;
    AnchorClassifcation classificationEnum;
    QQuick3DXrSpatialAnchor::Classification label;
    const char classificationName[16];
};
static const AnchorClassificationMap anchorClassificationMap[] = {
    {ar_plane_classification_status_unknown, AnchorClassifcation::Unknown, QQuick3DXrSpatialAnchor::Classification::Unknown, "Unknown"},
    {ar_plane_classification_status_not_available, AnchorClassifcation::NotAvailable, QQuick3DXrSpatialAnchor::Classification::Unknown, "Not Available"},
    {ar_plane_classification_status_undetermined, AnchorClassifcation::Undetermined, QQuick3DXrSpatialAnchor::Classification::Unknown, "Undetermined"},
    {ar_plane_classification_wall, AnchorClassifcation::Wall, QQuick3DXrSpatialAnchor::Classification::Wall, "Wall"},
    {ar_plane_classification_ceiling, AnchorClassifcation::Ceiling, QQuick3DXrSpatialAnchor::Classification::Ceiling, "Ceiling"},
    {ar_plane_classification_floor, AnchorClassifcation::Floor, QQuick3DXrSpatialAnchor::Classification::Floor, "Floor"},
    {ar_plane_classification_table, AnchorClassifcation::Table, QQuick3DXrSpatialAnchor::Classification::Table, "Table"},
    {ar_plane_classification_seat, AnchorClassifcation::Seat, QQuick3DXrSpatialAnchor::Classification::Seat, "Seat"},
    {ar_plane_classification_window, AnchorClassifcation::Window, QQuick3DXrSpatialAnchor::Classification::Window, "Window"},
    {ar_plane_classification_door, AnchorClassifcation::Door, QQuick3DXrSpatialAnchor::Classification::Door, "Door"},
};

static const AnchorClassificationMap &getAnchorClassificationName(ar_plane_classification_t classification, bool *identified = nullptr)
{
    size_t foundIndex = 0;
    for (size_t i = 0, end = std::size(anchorClassificationMap); i != end; ++i) {
        if (anchorClassificationMap[i].classification == classification) {
            foundIndex = i;
            break;
        }
    }

    if (identified) // If the caller wants to know if the classification was found (I.e. not Unknown, Not Available, or Undetermined)
        *identified = (foundIndex >= anchorClassificationStart);

    return anchorClassificationMap[foundIndex];
}

static void updateAnchorProperties(QQuick3DXrSpatialAnchor &anchor, ar_plane_anchor_t planeAnchor)
{
    constexpr auto s_rot90X = QQuaternion{M_SQRT1_2, -M_SQRT1_2, 0, 0}; // fromEulerAngles(-90, 0, 0);

    simd_float4x4 originFromAnchorTransform = ar_anchor_get_origin_from_anchor_transform(planeAnchor);
    QMatrix4x4 transform{originFromAnchorTransform.columns[0].x, originFromAnchorTransform.columns[1].x, originFromAnchorTransform.columns[2].x, originFromAnchorTransform.columns[3].x,
                           originFromAnchorTransform.columns[0].y, originFromAnchorTransform.columns[1].y, originFromAnchorTransform.columns[2].y, originFromAnchorTransform.columns[3].y,
                           originFromAnchorTransform.columns[0].z, originFromAnchorTransform.columns[1].z, originFromAnchorTransform.columns[2].z, originFromAnchorTransform.columns[3].z,
                           0.0f, 0.0f, 0.0f, 1.0f};

    ar_plane_classification_t classification = ar_plane_anchor_get_plane_classification(planeAnchor);
    const auto &classificationEntry = getAnchorClassificationName(classification);

    if (anchor.classification() != classificationEntry.label) {
        anchor.setClassification(classificationEntry.label);
        anchor.setClassificationString(QString::fromLatin1(classificationEntry.classificationName));
    }

    ar_plane_geometry_t planeGeometry = ar_plane_anchor_get_geometry(planeAnchor);
    ar_plane_extent_t planeExtent = ar_plane_geometry_get_plane_extent(planeGeometry);

    const float width = ar_plane_extent_get_width(planeExtent);
    const float height = ar_plane_extent_get_height(planeExtent);

    // position and rotation
    QVector3D pos;
    QVector3D scale;
    QQuaternion rot;
    QSSGUtils::mat44::decompose(transform, pos, scale, rot);

    // The y-axis of the plane anchor is the plane’s normal vector.
    rot = rot * s_rot90X;

    anchor.setPosition(pos * 100.0f);
    anchor.setRotation(rot);

    QVector2D offset2D{};
    QVector2D extent2D(width, height);
    anchor.setBounds2D(offset2D, extent2D);
}

inline void QQuick3DXrAnchorManager::planeUpdateHandler(void *context, ar_plane_anchors_t added_anchors, ar_plane_anchors_t updated_anchors, ar_plane_anchors_t removed_anchors)
{
    QSSG_ASSERT_X(context != nullptr, "Context is null!", return);

    QQuick3DXrAnchorManager *that = reinterpret_cast<QQuick3DXrAnchorManager *>(context);
    // Lock for writes to the anchors list (Might as well use a simple mutex, the data is only modified by this handler).
    QWriteLocker locker(&that->m_anchorsLock);

    // 1. Remove
    if (removed_anchors) {
        ar_plane_anchors_enumerate_anchors_f(removed_anchors, context, [](void *context, ar_plane_anchor_t planeAnchor) -> bool {
            QSSG_ASSERT_X(QSSG_DEBUG_COND(context != nullptr), "Unexpected context!", return false);

            QQuick3DXrAnchorManager *that = reinterpret_cast<QQuick3DXrAnchorManager *>(context);

            unsigned char identifier[16] {};
            ar_anchor_get_identifier(planeAnchor, identifier);

            if (Q_UNLIKELY(QtQuick3DXr::isNullUuid(identifier))) {
                qWarning() << "Invalid UUID for anchor";
                return false;
            }

            QUuid uuid = QUuid::fromRfc4122(QByteArrayView(reinterpret_cast<const char *>(identifier), 16));
            that->removeAnchor(uuid);

            return true;
        });
    }

    // 2. Add
    if (added_anchors) {
        ar_plane_anchors_enumerate_anchors_f(added_anchors, context, [](void *context, ar_plane_anchor_t planeAnchor) -> bool {
            QSSG_ASSERT_X(QSSG_DEBUG_COND(context != nullptr), "Unexpected context!", return false);

            QQuick3DXrAnchorManager *that = reinterpret_cast<QQuick3DXrAnchorManager *>(context);

            // NOTE: The API documentation for this is severely lacking, but the swift docs have some more information
            // saying the identifier follows RFC 4122 for UUIDs, meaning the identifier is a 128-bit value (Big Endian)
            unsigned char identifier[16] {};
            ar_anchor_get_identifier(planeAnchor, identifier);

            if (Q_UNLIKELY(QtQuick3DXr::isNullUuid(identifier))) {
                qWarning() << "Invalid UUID for anchor";
                return false;
            }

            QUuid uuid = QUuid::fromRfc4122(QByteArrayView(reinterpret_cast<const char *>(identifier), 16));
            const QtQuick3DXr::XrSpaceId space = that->getCurrentSpaceId();
            QQuick3DXrSpatialAnchor *anchor = new QQuick3DXrSpatialAnchor(space, uuid);
            updateAnchorProperties(*anchor, planeAnchor);
            that->addAnchor(anchor);

            return true;
        });
    }

    // 3. Update
    if (updated_anchors) {
        ar_plane_anchors_enumerate_anchors_f(updated_anchors, context, [](void *context, ar_plane_anchor_t planeAnchor) -> bool {
            QSSG_ASSERT_X(QSSG_DEBUG_COND(context != nullptr), "Unexpected context!", return false);

            QQuick3DXrAnchorManager *that = reinterpret_cast<QQuick3DXrAnchorManager *>(context);

            unsigned char identifier[16] {};
            ar_anchor_get_identifier(planeAnchor, identifier);

            if (Q_UNLIKELY(QtQuick3DXr::isNullUuid(identifier))) {
                qWarning() << "Invalid UUID for anchor";
                return false;
            }

            QUuid uuid = QUuid::fromRfc4122(QByteArrayView(reinterpret_cast<const char *>(identifier), 16));

            QQuick3DXrSpatialAnchor *anchor = that->m_anchorsByUuid.value(uuid);
            // This does occur in some cases, so we need to create a new anchor if it's not found
            // NOTE: Ideally this should not happen, but it does, reason unknown atm.
            if (!anchor) {
                anchor = new QQuick3DXrSpatialAnchor(that->getCurrentSpaceId(), uuid);
                updateAnchorProperties(*anchor, planeAnchor);
                that->addAnchor(anchor);
            } else {
                updateAnchorProperties(*anchor, planeAnchor);
                that->updateAnchor(anchor);
            }

            return true;
        });
    }

    that->populateAnchorsList();
}

inline void QQuick3DXrAnchorManager::prepareAnchorManager(ar_data_providers_t dataProviders)
{
    QSSG_ASSERT_X(!m_isInitialized, "Anchor manager already initialized", return);

    m_isPlaneDetectionSupported = (m_requestedAnchorType == AnchorType::Plane) && ar_plane_detection_provider_is_supported();
    if (m_isPlaneDetectionSupported) {
        ar_plane_detection_configuration_t planeDetectionConfiguration = ar_plane_detection_configuration_create();
        m_planeDetectionProvider = ar_plane_detection_provider_create(planeDetectionConfiguration);
        ar_plane_detection_provider_set_update_handler_f(m_planeDetectionProvider, dispatch_get_global_queue(DISPATCH_QUEUE_PRIORITY_DEFAULT, 0), this, &planeUpdateHandler);
        ar_data_providers_add_data_provider(dataProviders, m_planeDetectionProvider);
    } else {
        qCWarning(lcQuick3DXr, "Plane detection is not supported on this device.");
    }
}
QT_END_NAMESPACE
//  ---------------------------------------------------------------------

//  void QQuick3DXrAnchorManager::populateAnchorsList()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DXrAnchorManager19populateAnchorsListEv(
    QQuick3DXrAnchorManager *self) {
  self->populateAnchorsList();
}

//  void QQuick3DXrAnchorManager::initAnchorManager()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DXrAnchorManager17initAnchorManagerEv(
    QQuick3DXrAnchorManager *self) {
  self->initAnchorManager();
}

//  void QQuick3DXrAnchorManager::removeAnchor(QUuid uuid)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DXrAnchorManager12removeAnchorE5QUuid(
    QQuick3DXrAnchorManager *self,
    const QUuid *uuid) {
  self->removeAnchor(*uuid);
}

//  void QQuick3DXrAnchorManager::updateAnchor(QQuick3DXrSpatialAnchor
//      *anchor)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DXrAnchorManager12updateAnchorEP23QQuick3DXrSpatialAnchor(
    QQuick3DXrAnchorManager *self,
    QQuick3DXrSpatialAnchor *anchor) {
  self->updateAnchor(anchor);
}

//  void QQuick3DXrAnchorManager::prepareAnchorManager(ar_data_providers_t
//      dataProviders)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DXrAnchorManager20prepareAnchorManagerEPv(
    QQuick3DXrAnchorManager *self,
    void *dataProviders) {
  self->prepareAnchorManager((ar_data_providers_t)dataProviders);
}

//  static void QQuick3DXrAnchorManager::planeUpdateHandler(void *a0,
//      ar_plane_anchors_t a1, ar_plane_anchors_t a2, ar_plane_anchors_t a3)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DXrAnchorManager18planeUpdateHandlerEPvS0_S0_S0_(
    void *a0,
    void *a1,
    void *a2,
    void *a3) {
  QQuick3DXrAnchorManager::planeUpdateHandler(
      a0, (ar_plane_anchors_t)a1, (ar_plane_anchors_t)a2,
      (ar_plane_anchors_t)a3);
}

#endif
