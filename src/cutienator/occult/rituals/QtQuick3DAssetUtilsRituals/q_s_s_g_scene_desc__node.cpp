//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3DAssetUtils/6.12.0/QtQuick3DAssetUtils/private/qssgscenedesc_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DAssetUtils/6.12.0/QtQuick3DAssetUtils/private/qtquick3dassetutilsglobal_p.h>
#include <QtQuick3DAssetUtils/QtQuick3DAssetUtils>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DAssetUtils/6.12.0/QtQuick3DAssetUtils/private/qssgscenedesc_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>

//  QSSGSceneDesc::Node::Node(QByteArray name, Node::Type type,
//      Node::RuntimeType rt)
extern "C" Q_DECL_EXPORT
QSSGSceneDesc::Node *ritual_ZN13QSSGSceneDesc4NodeC1E10QByteArrayNS0_4TypeEN21QSSGRenderGraphObject4TypeE(
    const QByteArray *name,
    QSSGSceneDesc::Node::Type type,
    QSSGSceneDesc::Node::RuntimeType rt) {
  return new QSSGSceneDesc::Node(*name, type, rt);
}

//  QSSGSceneDesc::Node::Node(Node::Type type, Node::RuntimeType rt)
extern "C" Q_DECL_EXPORT
QSSGSceneDesc::Node *ritual_ZN13QSSGSceneDesc4NodeC1ENS0_4TypeEN21QSSGRenderGraphObject4TypeE(
    QSSGSceneDesc::Node::Type type,
    QSSGSceneDesc::Node::RuntimeType rt) {
  return new QSSGSceneDesc::Node(type, rt);
}

//  QSSGSceneDesc::Node::~Node()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSSGSceneDesc4NodeD1Ev(QSSGSceneDesc::Node *self) {
  delete self;
}

//  void QSSGSceneDesc::Node::cleanupChildren()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSSGSceneDesc4Node15cleanupChildrenEv(
    QSSGSceneDesc::Node *self) {
  self->cleanupChildren();
}
