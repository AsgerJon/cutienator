//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3D/6.12.0/QtQuick3D/ssg/qquick3dextensionhelpers.h, Qt 6.12.0.
//  Changes made here are lost.
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
