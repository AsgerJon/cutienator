//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DCore/6.12.0/Qt3DCore/private/qabstractnodefactory_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DCore/6.12.0/Qt3DCore/private/qt3dcore_global_p.h>
#include <Qt3DCore/Qt3DCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/6.12.0/Qt3DCore/private/qabstractnodefactory_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt3DCore::QAbstractNodeFactory::~QAbstractNodeFactory()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore20QAbstractNodeFactoryD1Ev(
    Qt3DCore::QAbstractNodeFactory *self) {
  delete self;
}

//  QNode *Qt3DCore::QAbstractNodeFactory::createNode(const char *type)
extern "C" Q_DECL_EXPORT
Qt3DCore::QNode *ritual_ZN8Qt3DCore20QAbstractNodeFactory10createNodeEPKc(
    Qt3DCore::QAbstractNodeFactory *self,
    const char *type) {
  return self->createNode(type);
}
