//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3D/6.12.0/QtQuick3D/private/qquick3deffect_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick3D/6.12.0/QtQuick3D/private/qtquick3dglobal_p.h>
#include <QtQuick3D/QtQuick3D>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3D/6.12.0/QtQuick3D/private/qquick3deffect_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtQuick3D/qquick3dobject.h>
#include <QtQml/QQmlListProperty>

//  Only a class built on QQuick3DEffect may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuick3DEffect : QQuick3DEffect {
  using QQuick3DEffect::updateSpatialNode;
  using QQuick3DEffect::itemChange;
};

//  const QMetaObject *QQuick3DEffect::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QQuick3DEffect10metaObjectEv(
    const QQuick3DEffect *self) {
  return self->metaObject();
}

//  void *QQuick3DEffect::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN14QQuick3DEffect11qt_metacastEPKc(
    QQuick3DEffect *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuick3DEffect::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN14QQuick3DEffect11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuick3DEffect *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuick3DEffect::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QQuick3DEffect2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuick3DEffect::tr(s, c, n));
}

//  QQuick3DEffect::QQuick3DEffect(QQuick3DObject *parent)
extern "C" Q_DECL_EXPORT
QQuick3DEffect *ritual_ZN14QQuick3DEffectC1EP14QQuick3DObject(
    QQuick3DObject *parent) {
  return new QQuick3DEffect(parent);
}

//  QQmlListProperty<QQuick3DShaderUtilsRenderPass> QQuick3DEffect::passes()
extern "C" Q_DECL_EXPORT
QQmlListProperty<QQuick3DShaderUtilsRenderPass> *ritual_ZN14QQuick3DEffect6passesEv(
    QQuick3DEffect *self) {
  return new QQmlListProperty<QQuick3DShaderUtilsRenderPass>(self->passes());
}

//  void QQuick3DEffect::qmlAppendPass(QQmlListProperty<QQuick3DShaderUtilsRe
//      nderPass> *list, QQuick3DShaderUtilsRenderPass *pass)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuick3DEffect13qmlAppendPassEP16QQmlListPropertyI29QQuick3DShaderUtilsRenderPassEPS1_(
    QQmlListProperty<QQuick3DShaderUtilsRenderPass> *list,
    QQuick3DShaderUtilsRenderPass *pass) {
  QQuick3DEffect::qmlAppendPass(list, pass);
}

//  QQuick3DShaderUtilsRenderPass *QQuick3DEffect::qmlPassAt(QQmlListProperty
//      <QQuick3DShaderUtilsRenderPass> *list, qsizetype index)
extern "C" Q_DECL_EXPORT
QQuick3DShaderUtilsRenderPass *ritual_ZN14QQuick3DEffect9qmlPassAtEP16QQmlListPropertyI29QQuick3DShaderUtilsRenderPassEx(
    QQmlListProperty<QQuick3DShaderUtilsRenderPass> *list,
    qsizetype index) {
  return QQuick3DEffect::qmlPassAt(list, index);
}

//  qsizetype QQuick3DEffect::qmlPassCount(QQmlListProperty<QQuick3DShaderUti
//      lsRenderPass> *list)
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN14QQuick3DEffect12qmlPassCountEP16QQmlListPropertyI29QQuick3DShaderUtilsRenderPassE(
    QQmlListProperty<QQuick3DShaderUtilsRenderPass> *list) {
  return QQuick3DEffect::qmlPassCount(list);
}

//  void QQuick3DEffect::qmlPassClear(QQmlListProperty<QQuick3DShaderUtilsRen
//      derPass> *list)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuick3DEffect12qmlPassClearEP16QQmlListPropertyI29QQuick3DShaderUtilsRenderPassE(
    QQmlListProperty<QQuick3DShaderUtilsRenderPass> *list) {
  QQuick3DEffect::qmlPassClear(list);
}

//  void QQuick3DEffect::effectChainDirty()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuick3DEffect16effectChainDirtyEv(QQuick3DEffect *self) {
  self->effectChainDirty();
}

//  QSSGRenderGraphObject
//      *QQuick3DEffect::updateSpatialNode(QSSGRenderGraphObject *node)
extern "C" Q_DECL_EXPORT
QSSGRenderGraphObject *ritual_ZN14QQuick3DEffect17updateSpatialNodeEP21QSSGRenderGraphObject(
    QQuick3DEffect *self,
    QSSGRenderGraphObject *node) {
  return self->updateSpatialNode(node);
}

//  void QQuick3DEffect::itemChange(QQuick3DObject::ItemChange a0, const
//      QQuick3DObject::ItemChangeData &a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuick3DEffect10itemChangeEN14QQuick3DObject10ItemChangeERKNS0_14ItemChangeDataE(
    QQuick3DEffect *self,
    QQuick3DObject::ItemChange a0,
    const QQuick3DObject::ItemChangeData *a1) {
  self->itemChange(a0, *a1);
}

//  void QQuick3DEffect::onPropertyDirty()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuick3DEffect15onPropertyDirtyEv(QQuick3DEffect *self) {
  self->onPropertyDirty();
}

//  void QQuick3DEffect::onTextureDirty()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuick3DEffect14onTextureDirtyEv(QQuick3DEffect *self) {
  self->onTextureDirty();
}

//  void QQuick3DEffect::onPassDirty()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuick3DEffect11onPassDirtyEv(QQuick3DEffect *self) {
  self->onPassDirty();
}

//  void QQuick3DEffect::setDynamicTextureMap(QQuick3DShaderUtilsTextureInput
//      *textureMap)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuick3DEffect20setDynamicTextureMapEP31QQuick3DShaderUtilsTextureInput(
    QQuick3DEffect *self,
    QQuick3DShaderUtilsTextureInput *textureMap) {
  self->setDynamicTextureMap(textureMap);
}

//  void QQuick3DEffect::markDirty(QQuick3DEffect::Dirty type)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuick3DEffect9markDirtyENS_5DirtyE(
    QQuick3DEffect *self,
    QQuick3DEffect::Dirty type) {
  self->markDirty(type);
}

//  void QQuick3DEffect::updateSceneManager(QQuick3DSceneManager
//      *sceneManager)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuick3DEffect18updateSceneManagerEP20QQuick3DSceneManager(
    QQuick3DEffect *self,
    QQuick3DSceneManager *sceneManager) {
  self->updateSceneManager(sceneManager);
}

//  QSSGRenderGraphObject
//      *QQuick3DEffect::updateSpatialNode(QSSGRenderGraphObject *node)
extern "C" Q_DECL_EXPORT
QSSGRenderGraphObject *ritual_own_ZN14QQuick3DEffect17updateSpatialNodeEP21QSSGRenderGraphObject(
    QQuick3DEffect *self,
    QSSGRenderGraphObject *node) {
  return static_cast<OwnQQuick3DEffect *>(self)->OwnQQuick3DEffect::updateSpatialNode(
      node);
}

//  void QQuick3DEffect::itemChange(QQuick3DObject::ItemChange a0, const
//      QQuick3DObject::ItemChangeData &a1)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuick3DEffect10itemChangeEN14QQuick3DObject10ItemChangeERKNS0_14ItemChangeDataE(
    QQuick3DEffect *self,
    QQuick3DObject::ItemChange a0,
    const QQuick3DObject::ItemChangeData *a1) {
  static_cast<OwnQQuick3DEffect *>(self)->OwnQQuick3DEffect::itemChange(
      a0,
      *a1);
}

//  a QQmlListProperty<QQuick3DShaderUtilsRenderPass> a ritual of
//      QQuick3DEffect gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQuick3DEffect__QQmlListProperty_QQuick3DShaderUtilsRenderPass(
    QQmlListProperty<QQuick3DShaderUtilsRenderPass> *self) {
  delete self;
}
