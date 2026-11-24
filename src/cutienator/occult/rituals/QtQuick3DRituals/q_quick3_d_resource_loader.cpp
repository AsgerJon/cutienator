//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dresourceloader_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick3D/6.12.0/QtQuick3D/private/qtquick3dglobal_p.h>
#include <QtQuick3D/QtQuick3D>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3D/6.12.0/QtQuick3D/private/qquick3dresourceloader_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtQuick3D/qquick3dobject.h>
#include <QtCore/qlist.h>

//  Only a class built on QQuick3DResourceLoader may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuick3DResourceLoader : QQuick3DResourceLoader {
  using QQuick3DResourceLoader::updateSpatialNode;
  using QQuick3DResourceLoader::markAllDirty;
  using QQuick3DResourceLoader::itemChange;
};

//  const QMetaObject *QQuick3DResourceLoader::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK22QQuick3DResourceLoader10metaObjectEv(
    const QQuick3DResourceLoader *self) {
  return self->metaObject();
}

//  QString QQuick3DResourceLoader::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN22QQuick3DResourceLoader2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuick3DResourceLoader::tr(s, c, n));
}

//  QQuick3DResourceLoader::QQuick3DResourceLoader(QQuick3DObject *parent)
extern "C" Q_DECL_EXPORT
QQuick3DResourceLoader *ritual_ZN22QQuick3DResourceLoaderC1EP14QQuick3DObject(
    QQuick3DObject *parent) {
  return new QQuick3DResourceLoader(parent);
}

//  const QList<QUrl> &QQuick3DResourceLoader::meshSources() const
extern "C" Q_DECL_EXPORT
QList<QUrl> *ritual_ZNK22QQuick3DResourceLoader11meshSourcesEv(
    const QQuick3DResourceLoader *self) {
  return new QList<QUrl>(self->meshSources());
}

//  void QQuick3DResourceLoader::setMeshSources(const QList<QUrl>
//      &newMeshSources)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DResourceLoader14setMeshSourcesERK5QListI4QUrlE(
    QQuick3DResourceLoader *self,
    const QList<QUrl> *newMeshSources) {
  self->setMeshSources(*newMeshSources);
}

//  void QQuick3DResourceLoader::onGeometryDestroyed(QObject *object)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DResourceLoader19onGeometryDestroyedEP7QObject(
    QQuick3DResourceLoader *self,
    QObject *object) {
  self->onGeometryDestroyed(object);
}

//  void QQuick3DResourceLoader::onTextureDestroyed(QObject *object)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DResourceLoader18onTextureDestroyedEP7QObject(
    QQuick3DResourceLoader *self,
    QObject *object) {
  self->onTextureDestroyed(object);
}

//  QSSGRenderGraphObject
//      *QQuick3DResourceLoader::updateSpatialNode(QSSGRenderGraphObject
//      *node)
extern "C" Q_DECL_EXPORT
QSSGRenderGraphObject *ritual_ZN22QQuick3DResourceLoader17updateSpatialNodeEP21QSSGRenderGraphObject(
    QQuick3DResourceLoader *self,
    QSSGRenderGraphObject *node) {
  return self->updateSpatialNode(node);
}

//  void QQuick3DResourceLoader::markAllDirty()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DResourceLoader12markAllDirtyEv(
    QQuick3DResourceLoader *self) {
  self->markAllDirty();
}

//  void QQuick3DResourceLoader::itemChange(ItemChange change, const
//      ItemChangeData &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DResourceLoader10itemChangeEN14QQuick3DObject10ItemChangeERKNS0_14ItemChangeDataE(
    QQuick3DResourceLoader *self,
    QQuick3DObject::ItemChange change,
    const QQuick3DObject::ItemChangeData *value) {
  self->itemChange(change, *value);
}

//  void QQuick3DResourceLoader::markDirty(ResourceLoaderDirtyType type)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DResourceLoader9markDirtyENS_23ResourceLoaderDirtyTypeE(
    QQuick3DResourceLoader *self,
    QQuick3DResourceLoader::ResourceLoaderDirtyType type) {
  self->markDirty(type);
}

//  void QQuick3DResourceLoader::updateSceneManager(QQuick3DSceneManager
//      *sceneManager)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DResourceLoader18updateSceneManagerEP20QQuick3DSceneManager(
    QQuick3DResourceLoader *self,
    QQuick3DSceneManager *sceneManager) {
  self->updateSceneManager(sceneManager);
}

//  QSSGRenderGraphObject
//      *QQuick3DResourceLoader::updateSpatialNode(QSSGRenderGraphObject
//      *node)
extern "C" Q_DECL_EXPORT
QSSGRenderGraphObject *ritual_own_ZN22QQuick3DResourceLoader17updateSpatialNodeEP21QSSGRenderGraphObject(
    QQuick3DResourceLoader *self,
    QSSGRenderGraphObject *node) {
  return static_cast<OwnQQuick3DResourceLoader *>(self)->OwnQQuick3DResourceLoader::updateSpatialNode(
      node);
}

//  void QQuick3DResourceLoader::markAllDirty()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QQuick3DResourceLoader12markAllDirtyEv(
    QQuick3DResourceLoader *self) {
  static_cast<OwnQQuick3DResourceLoader *>(self)->OwnQQuick3DResourceLoader::markAllDirty();
}

//  void QQuick3DResourceLoader::itemChange(ItemChange change, const
//      ItemChangeData &value)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QQuick3DResourceLoader10itemChangeEN14QQuick3DObject10ItemChangeERKNS0_14ItemChangeDataE(
    QQuick3DResourceLoader *self,
    QQuick3DObject::ItemChange change,
    const QQuick3DObject::ItemChangeData *value) {
  static_cast<OwnQQuick3DResourceLoader *>(self)->OwnQQuick3DResourceLoader::itemChange(
      change,
      *value);
}
