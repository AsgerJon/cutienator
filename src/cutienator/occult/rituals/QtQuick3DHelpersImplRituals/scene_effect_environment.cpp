//  Written by hand on 2026-11-25 from
//  QtQuick3DHelpersImpl/6.12.0/QtQuick3DHelpersImpl/private/sceneeffects_p.h,
//  Qt 6.12.0. Kept as it is when the generator runs again.
//  Qt's library offers nothing of this class by name: the class has no
//  Q_..._EXPORT macro, so only its virtual functions are written, called
//  through the object: metaObject(), the implicit destructor (virtual
//  through QObject), useBuiltinTonemapper() and updateSpatialNode().
//  Not written: the constructor; the setters and the other non-virtual
//  functions, which are defined outside the header; effectList(), which
//  returns a reference to a QVector, a list return; and the moc
//  functions qt_metacast and qt_metacall, which the example leaves out.
#include <QtQuick3D/qtquick3dglobal.h>
#include <QtQuick3D/qtquick3dexports.h>
#include <QtQuick3DHelpersImpl/6.12.0/QtQuick3DHelpersImpl/private/sceneeffects_p.h>

//  const QMetaObject *SceneEffectEnvironment::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK22SceneEffectEnvironment10metaObjectEv(
    const SceneEffectEnvironment *self) {
  return self->metaObject();
}

//  SceneEffectEnvironment::~SceneEffectEnvironment()
extern "C" Q_DECL_EXPORT
void ritual_ZN22SceneEffectEnvironmentD1Ev(
    SceneEffectEnvironment *self) {
  delete self;
}

//  bool SceneEffectEnvironment::useBuiltinTonemapper() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22SceneEffectEnvironment20useBuiltinTonemapperEv(
    const SceneEffectEnvironment *self) {
  return self->useBuiltinTonemapper();
}

//  QSSGRenderGraphObject *SceneEffectEnvironment::updateSpatialNode(
//      QSSGRenderGraphObject *node)
extern "C" Q_DECL_EXPORT
QSSGRenderGraphObject *ritual_ZN22SceneEffectEnvironment17updateSpatialNodeEP21QSSGRenderGraphObject(
    SceneEffectEnvironment *self,
    QSSGRenderGraphObject *node) {
  return self->updateSpatialNode(node);
}
