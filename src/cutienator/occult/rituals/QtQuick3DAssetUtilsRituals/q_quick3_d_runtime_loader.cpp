//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DAsset
//  Utils/6.12.0/QtQuick3DAssetUtils/private/qquick3druntimeloader_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#include <QtQuick3DAssetUtils/6.12.0/QtQuick3DAssetUtils/private/qtquick3dassetutilsglobal_p.h>
#include <QtQuick3DAssetUtils/QtQuick3DAssetUtils>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DAssetUtils/6.12.0/QtQuick3DAssetUtils/private/qquick3druntimeloader_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtCore/qmimetype.h>
#include <QtQuick3D/QtQuick3D>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3D/6.12.0/QtQuick3D/private/qquick3dmodel_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3D/qquick3dobject.h>
#include <QtCore/qlist.h>

//  Only a class built on QQuick3DRuntimeLoader may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuick3DRuntimeLoader : QQuick3DRuntimeLoader {
  using QQuick3DRuntimeLoader::updateSpatialNode;
};

//  const QMetaObject *QQuick3DRuntimeLoader::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QQuick3DRuntimeLoader10metaObjectEv(
    const QQuick3DRuntimeLoader *self) {
  return self->metaObject();
}

//  QString QQuick3DRuntimeLoader::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN21QQuick3DRuntimeLoader2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuick3DRuntimeLoader::tr(s, c, n));
}

//  QQuick3DRuntimeLoader::QQuick3DRuntimeLoader(QQuick3DNode *parent)
extern "C" Q_DECL_EXPORT
QQuick3DRuntimeLoader *ritual_ZN21QQuick3DRuntimeLoaderC1EP12QQuick3DNode(
    QQuick3DNode *parent) {
  return new QQuick3DRuntimeLoader(parent);
}

//  QUrl QQuick3DRuntimeLoader::source() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK21QQuick3DRuntimeLoader6sourceEv(
    const QQuick3DRuntimeLoader *self) {
  return new QUrl(self->source());
}

//  void QQuick3DRuntimeLoader::setSource(const QUrl &newSource)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DRuntimeLoader9setSourceERK4QUrl(
    QQuick3DRuntimeLoader *self,
    const QUrl *newSource) {
  self->setSource(*newSource);
}

//  void QQuick3DRuntimeLoader::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DRuntimeLoader17componentCompleteEv(
    QQuick3DRuntimeLoader *self) {
  self->componentComplete();
}

//  QStringList QQuick3DRuntimeLoader::supportedExtensions()
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN21QQuick3DRuntimeLoader19supportedExtensionsEv() {
  return new QList<QString>(QQuick3DRuntimeLoader::supportedExtensions());
}

#if QT_CONFIG(mimetype)
//  QList<QMimeType> QQuick3DRuntimeLoader::supportedMimeTypes()
extern "C" Q_DECL_EXPORT
QList<QMimeType> *ritual_ZN21QQuick3DRuntimeLoader18supportedMimeTypesEv() {
  return new QList<QMimeType>(QQuick3DRuntimeLoader::supportedMimeTypes());
}
#endif  // QT_CONFIG(mimetype)

//  Status QQuick3DRuntimeLoader::status() const
extern "C" Q_DECL_EXPORT
QQuick3DRuntimeLoader::Status ritual_ZNK21QQuick3DRuntimeLoader6statusEv(
    const QQuick3DRuntimeLoader *self) {
  return self->status();
}

//  QString QQuick3DRuntimeLoader::errorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK21QQuick3DRuntimeLoader11errorStringEv(
    const QQuick3DRuntimeLoader *self) {
  return new QString(self->errorString());
}

//  const QQuick3DBounds3 &QQuick3DRuntimeLoader::bounds() const
extern "C" Q_DECL_EXPORT
QQuick3DBounds3 *ritual_ZNK21QQuick3DRuntimeLoader6boundsEv(
    const QQuick3DRuntimeLoader *self) {
  return new QQuick3DBounds3(self->bounds());
}

//  QQuick3DInstancing *QQuick3DRuntimeLoader::instancing() const
extern "C" Q_DECL_EXPORT
QQuick3DInstancing *ritual_ZNK21QQuick3DRuntimeLoader10instancingEv(
    const QQuick3DRuntimeLoader *self) {
  return self->instancing();
}

//  void QQuick3DRuntimeLoader::setInstancing(QQuick3DInstancing
//      *newInstancing)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DRuntimeLoader13setInstancingEP18QQuick3DInstancing(
    QQuick3DRuntimeLoader *self,
    QQuick3DInstancing *newInstancing) {
  self->setInstancing(newInstancing);
}

//  QQuick3DObject *QQuick3DRuntimeLoader::query(const QString &name) const
extern "C" Q_DECL_EXPORT
QQuick3DObject *ritual_ZNK21QQuick3DRuntimeLoader5queryERK7QString(
    const QQuick3DRuntimeLoader *self,
    const QString *name) {
  return self->query(*name);
}

//  QList<QQuick3DObject *> QQuick3DRuntimeLoader::queryAll(QueryFilter
//      filter) const
extern "C" Q_DECL_EXPORT
QList<QQuick3DObject *> *ritual_ZNK21QQuick3DRuntimeLoader8queryAllENS_11QueryFilterE(
    const QQuick3DRuntimeLoader *self,
    QQuick3DRuntimeLoader::QueryFilter filter) {
  return new QList<QQuick3DObject *>(self->queryAll(filter));
}

//  QSSGRenderGraphObject
//      *QQuick3DRuntimeLoader::updateSpatialNode(QSSGRenderGraphObject
//      *node)
extern "C" Q_DECL_EXPORT
QSSGRenderGraphObject *ritual_ZN21QQuick3DRuntimeLoader17updateSpatialNodeEP21QSSGRenderGraphObject(
    QQuick3DRuntimeLoader *self,
    QSSGRenderGraphObject *node) {
  return self->updateSpatialNode(node);
}

//  void QQuick3DRuntimeLoader::calculateBounds()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DRuntimeLoader15calculateBoundsEv(
    QQuick3DRuntimeLoader *self) {
  self->calculateBounds();
}

//  void QQuick3DRuntimeLoader::loadSource()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DRuntimeLoader10loadSourceEv(
    QQuick3DRuntimeLoader *self) {
  self->loadSource();
}

//  void QQuick3DRuntimeLoader::updateModels()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DRuntimeLoader12updateModelsEv(
    QQuick3DRuntimeLoader *self) {
  self->updateModels();
}

//  void QQuick3DRuntimeLoader::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QQuick3DRuntimeLoader17componentCompleteEv(
    QQuick3DRuntimeLoader *self) {
  self->QQuick3DRuntimeLoader::componentComplete();
}

//  QSSGRenderGraphObject
//      *QQuick3DRuntimeLoader::updateSpatialNode(QSSGRenderGraphObject
//      *node)
extern "C" Q_DECL_EXPORT
QSSGRenderGraphObject *ritual_own_ZN21QQuick3DRuntimeLoader17updateSpatialNodeEP21QSSGRenderGraphObject(
    QQuick3DRuntimeLoader *self,
    QSSGRenderGraphObject *node) {
  return static_cast<OwnQQuick3DRuntimeLoader *>(self)->OwnQQuick3DRuntimeLoader::updateSpatialNode(
      node);
}
