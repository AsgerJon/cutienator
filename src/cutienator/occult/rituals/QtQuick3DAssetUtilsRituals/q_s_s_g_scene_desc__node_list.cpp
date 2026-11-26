//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3DAssetUtils/6.12.0/QtQuick3DAssetUtils/private/qssgscenedesc_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DAssetUtils/6.12.0/QtQuick3DAssetUtils/private/qtquick3dassetutilsglobal_p.h>
#include <QtQuick3DAssetUtils/QtQuick3DAssetUtils>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DAssetUtils/6.12.0/QtQuick3DAssetUtils/private/qssgscenedesc_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QSSGSceneDesc::NodeList::NodeList(void *const *data, qsizetype n)
extern "C" Q_DECL_EXPORT
QSSGSceneDesc::NodeList *ritual_ZN13QSSGSceneDesc8NodeListC1EPKPvx(
    void *const *data,
    qsizetype n) {
  return new QSSGSceneDesc::NodeList(data, n);
}

//  QSSGSceneDesc::NodeList::~NodeList()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSSGSceneDesc8NodeListD1Ev(QSSGSceneDesc::NodeList *self) {
  delete self;
}
