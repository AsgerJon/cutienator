//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DCore/6.12.0/Qt3DCore/private/qabstractnodefactory_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-25: added by hand, instances of templates of
//  the class: 2. Kept as it is when the generator runs again.
#include <Qt3DCore/6.12.0/Qt3DCore/private/qt3dcore_global_p.h>
#include <Qt3DCore/Qt3DCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/6.12.0/Qt3DCore/private/qabstractnodefactory_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/QList>
#include <Qt3DCore/qnode.h>
#include <Qt3DCore/qentity.h>

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

//  void
//      Qt3DCore::QAbstractNodeFactory::registerNodeFactory(QAbstractNodeFact
//      ory *factory)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore20QAbstractNodeFactory19registerNodeFactoryEPS0_(
    Qt3DCore::QAbstractNodeFactory *factory) {
  Qt3DCore::QAbstractNodeFactory::registerNodeFactory(factory);
}

//  QList<QAbstractNodeFactory *>
//      Qt3DCore::QAbstractNodeFactory::nodeFactories()
extern "C" Q_DECL_EXPORT
QList<Qt3DCore::QAbstractNodeFactory *> *ritual_ZN8Qt3DCore20QAbstractNodeFactory13nodeFactoriesEv() {
  return new QList<Qt3DCore::QAbstractNodeFactory *>(
      Qt3DCore::QAbstractNodeFactory::nodeFactories());
}

//  a QList<Qt3DCore::QAbstractNodeFactory *> a ritual of
//      Qt3DCore::QAbstractNodeFactory gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DCore_QAbstractNodeFactory__QList_Qt3DCore_QAbstractNodeFactory(
    QList<Qt3DCore::QAbstractNodeFactory *> *self) {
  delete self;
}

//  static Qt3DCore::QNode
//      *Qt3DCore::QAbstractNodeFactory::createNode<Qt3DCore::QNode>( const
//      char *type)
extern "C" Q_DECL_EXPORT
Qt3DCore::QNode * ritual_ZN8Qt3DCore20QAbstractNodeFactory10createNodeINS_5QNodeEEEPT_PKc(
    const char *type) {
  return Qt3DCore::QAbstractNodeFactory::createNode<Qt3DCore::QNode>(type);
}

//  static Qt3DCore::QEntity
//      *Qt3DCore::QAbstractNodeFactory::createNode<Qt3DCore::QEntity>( const
//      char *type)
extern "C" Q_DECL_EXPORT
Qt3DCore::QEntity * ritual_ZN8Qt3DCore20QAbstractNodeFactory10createNodeINS_7QEntityEEEPT_PKc(
    const char *type) {
  return Qt3DCore::QAbstractNodeFactory::createNode<Qt3DCore::QEntity>(type);
}
