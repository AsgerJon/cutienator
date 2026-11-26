//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3D/6.12.0/QtQuick3D/ssg/qquick3dextensionhelpers.h, Qt 6.12.0.
//  Edited by hand on 2026-11-25: added by hand, instances of templates of
//  the class: 4. Kept as it is when the generator runs again.
#include <QtQuick3D/6.12.0/QtQuick3D/private/qtquick3dglobal_p.h>
#include <QtQuick3D/QtQuick3D>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3D/6.12.0/QtQuick3D/ssg/qquick3dextensionhelpers.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QQuick3DExtensionHelpers::QQuick3DExtensionHelpers()
extern "C" Q_DECL_EXPORT
QQuick3DExtensionHelpers *ritual_ZN24QQuick3DExtensionHelpersC1Ev() {
  return new QQuick3DExtensionHelpers();
}

//  QSSGNodeId QQuick3DExtensionHelpers::getNodeId(const QQuick3DObject
//      &node)
extern "C" Q_DECL_EXPORT
QSSGNodeId ritual_ZN24QQuick3DExtensionHelpers9getNodeIdERK14QQuick3DObject(
    const QQuick3DObject *node) {
  return QQuick3DExtensionHelpers::getNodeId(*node);
}

//  QSSGResourceId QQuick3DExtensionHelpers::getResourceId(const
//      QQuick3DObject &resource)
extern "C" Q_DECL_EXPORT
QSSGResourceId ritual_ZN24QQuick3DExtensionHelpers13getResourceIdERK14QQuick3DObject(
    const QQuick3DObject *resource) {
  return QQuick3DExtensionHelpers::getResourceId(*resource);
}

//  QSSGCameraId QQuick3DExtensionHelpers::getCameraId(const QQuick3DObject
//      &camera)
extern "C" Q_DECL_EXPORT
QSSGCameraId ritual_ZN24QQuick3DExtensionHelpers11getCameraIdERK14QQuick3DObject(
    const QQuick3DObject *camera) {
  return QQuick3DExtensionHelpers::getCameraId(*camera);
}

//  QSSGExtensionId QQuick3DExtensionHelpers::getExtensionId(const
//      QQuick3DObject &extension)
extern "C" Q_DECL_EXPORT
QSSGExtensionId ritual_ZN24QQuick3DExtensionHelpers14getExtensionIdERK14QQuick3DObject(
    const QQuick3DObject *extension) {
  return QQuick3DExtensionHelpers::getExtensionId(*extension);
}

//  QSSGRenderGraphObject::Type
//      QQuick3DExtensionHelpers::getNodeIdType(QSSGNodeId nodeId)
extern "C" Q_DECL_EXPORT
QSSGRenderGraphObject::Type ritual_ZN24QQuick3DExtensionHelpers13getNodeIdTypeE10QSSGNodeId(
    QSSGNodeId nodeId) {
  return QQuick3DExtensionHelpers::getNodeIdType(nodeId);
}

//  QQuick3DExtensionHelpers::~QQuick3DExtensionHelpers()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DExtensionHelpersD1Ev(
    QQuick3DExtensionHelpers *self) {
  delete self;
}

//  static constexpr bool
//      QQuick3DExtensionHelpers::isNull<QSSGNodeId>(QSSGNodeId id)
extern "C" Q_DECL_EXPORT
bool ritual_ZN24QQuick3DExtensionHelpers6isNullI10QSSGNodeIdEEbT_(long long id) {
  return QQuick3DExtensionHelpers::isNull<QSSGNodeId>(
      static_cast<QSSGNodeId>(id));
}

//  static constexpr bool
//      QQuick3DExtensionHelpers::isNull<QSSGResourceId>(QSSGResourceId id)
extern "C" Q_DECL_EXPORT
bool ritual_ZN24QQuick3DExtensionHelpers6isNullI14QSSGResourceIdEEbT_(long long id) {
  return QQuick3DExtensionHelpers::isNull<QSSGResourceId>(
      static_cast<QSSGResourceId>(id));
}

//  static constexpr bool
//      QQuick3DExtensionHelpers::isNull<QSSGCameraId>(QSSGCameraId id)
extern "C" Q_DECL_EXPORT
bool ritual_ZN24QQuick3DExtensionHelpers6isNullI12QSSGCameraIdEEbT_(long long id) {
  return QQuick3DExtensionHelpers::isNull<QSSGCameraId>(
      static_cast<QSSGCameraId>(id));
}

//  static constexpr bool
//      QQuick3DExtensionHelpers::isNull<QSSGExtensionId>(QSSGExtensionId id)
extern "C" Q_DECL_EXPORT
bool ritual_ZN24QQuick3DExtensionHelpers6isNullI15QSSGExtensionIdEEbT_(long long id) {
  return QQuick3DExtensionHelpers::isNull<QSSGExtensionId>(
      static_cast<QSSGExtensionId>(id));
}
