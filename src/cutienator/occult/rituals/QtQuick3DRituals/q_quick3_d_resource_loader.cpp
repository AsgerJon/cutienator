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
#include <QtQml/QQmlListProperty>
#include <QtQuick3D/QQuick3DGeometry>

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

//  void *QQuick3DResourceLoader::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN22QQuick3DResourceLoader11qt_metacastEPKc(
    QQuick3DResourceLoader *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuick3DResourceLoader::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN22QQuick3DResourceLoader11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuick3DResourceLoader *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
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

//  QQmlListProperty<QQuick3DGeometry> QQuick3DResourceLoader::geometries()
extern "C" Q_DECL_EXPORT
QQmlListProperty<QQuick3DGeometry> *ritual_ZN22QQuick3DResourceLoader10geometriesEv(
    QQuick3DResourceLoader *self) {
  return new QQmlListProperty<QQuick3DGeometry>(self->geometries());
}

//  QQmlListProperty<QQuick3DTexture> QQuick3DResourceLoader::textures()
extern "C" Q_DECL_EXPORT
QQmlListProperty<QQuick3DTexture> *ritual_ZN22QQuick3DResourceLoader8texturesEv(
    QQuick3DResourceLoader *self) {
  return new QQmlListProperty<QQuick3DTexture>(self->textures());
}

//  void QQuick3DResourceLoader::meshSourcesChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DResourceLoader18meshSourcesChangedEv(
    QQuick3DResourceLoader *self) {
  self->meshSourcesChanged();
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

//  void QQuick3DResourceLoader::qmlAppendGeometry(QQmlListProperty<QQuick3DG
//      eometry> *list, QQuick3DGeometry *geometry)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DResourceLoader17qmlAppendGeometryEP16QQmlListPropertyI16QQuick3DGeometryEPS1_(
    QQmlListProperty<QQuick3DGeometry> *list,
    QQuick3DGeometry *geometry) {
  QQuick3DResourceLoader::qmlAppendGeometry(list, geometry);
}

//  QQuick3DGeometry
//      *QQuick3DResourceLoader::qmlGeometryAt(QQmlListProperty<QQuick3DGeome
//      try> *list, qsizetype index)
extern "C" Q_DECL_EXPORT
QQuick3DGeometry *ritual_ZN22QQuick3DResourceLoader13qmlGeometryAtEP16QQmlListPropertyI16QQuick3DGeometryEx(
    QQmlListProperty<QQuick3DGeometry> *list,
    qsizetype index) {
  return QQuick3DResourceLoader::qmlGeometryAt(list, index);
}

//  qsizetype QQuick3DResourceLoader::qmlGeometriesCount(QQmlListProperty<QQu
//      ick3DGeometry> *list)
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN22QQuick3DResourceLoader18qmlGeometriesCountEP16QQmlListPropertyI16QQuick3DGeometryE(
    QQmlListProperty<QQuick3DGeometry> *list) {
  return QQuick3DResourceLoader::qmlGeometriesCount(list);
}

//  void QQuick3DResourceLoader::qmlClearGeometries(QQmlListProperty<QQuick3D
//      Geometry> *list)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DResourceLoader18qmlClearGeometriesEP16QQmlListPropertyI16QQuick3DGeometryE(
    QQmlListProperty<QQuick3DGeometry> *list) {
  QQuick3DResourceLoader::qmlClearGeometries(list);
}

//  void QQuick3DResourceLoader::qmlAppendTexture(QQmlListProperty<QQuick3DTe
//      xture> *list, QQuick3DTexture *texture)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DResourceLoader16qmlAppendTextureEP16QQmlListPropertyI15QQuick3DTextureEPS1_(
    QQmlListProperty<QQuick3DTexture> *list,
    QQuick3DTexture *texture) {
  QQuick3DResourceLoader::qmlAppendTexture(list, texture);
}

//  QQuick3DTexture
//      *QQuick3DResourceLoader::qmlTextureAt(QQmlListProperty<QQuick3DTextur
//      e> *list, qsizetype index)
extern "C" Q_DECL_EXPORT
QQuick3DTexture *ritual_ZN22QQuick3DResourceLoader12qmlTextureAtEP16QQmlListPropertyI15QQuick3DTextureEx(
    QQmlListProperty<QQuick3DTexture> *list,
    qsizetype index) {
  return QQuick3DResourceLoader::qmlTextureAt(list, index);
}

//  qsizetype QQuick3DResourceLoader::qmlTexturesCount(QQmlListProperty<QQuic
//      k3DTexture> *list)
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN22QQuick3DResourceLoader16qmlTexturesCountEP16QQmlListPropertyI15QQuick3DTextureE(
    QQmlListProperty<QQuick3DTexture> *list) {
  return QQuick3DResourceLoader::qmlTexturesCount(list);
}

//  void QQuick3DResourceLoader::qmlClearTextures(QQmlListProperty<QQuick3DTe
//      xture> *list)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DResourceLoader16qmlClearTexturesEP16QQmlListPropertyI15QQuick3DTextureE(
    QQmlListProperty<QQuick3DTexture> *list) {
  QQuick3DResourceLoader::qmlClearTextures(list);
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

//  a QQmlListProperty<QQuick3DGeometry> a ritual of QQuick3DResourceLoader
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQuick3DResourceLoader__QQmlListProperty_QQuick3DGeometry(
    QQmlListProperty<QQuick3DGeometry> *self) {
  delete self;
}

//  a QQmlListProperty<QQuick3DTexture> a ritual of QQuick3DResourceLoader
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQuick3DResourceLoader__QQmlListProperty_QQuick3DTexture(
    QQmlListProperty<QQuick3DTexture> *self) {
  delete self;
}
