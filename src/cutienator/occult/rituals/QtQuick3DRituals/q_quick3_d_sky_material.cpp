//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dskymaterial_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick3D/6.12.0/QtQuick3D/private/qtquick3dglobal_p.h>
#include <QtQuick3D/QtQuick3D>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3D/6.12.0/QtQuick3D/private/qquick3dskymaterial_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtCore/qmetaobject.h>

//  Only a class built on QQuick3DSkyMaterial may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuick3DSkyMaterial : QQuick3DSkyMaterial {
  using QQuick3DSkyMaterial::updateSpatialNode;
  using QQuick3DSkyMaterial::markTrackedPropertyDirty;
};

//  const QMetaObject *QQuick3DSkyMaterial::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QQuick3DSkyMaterial10metaObjectEv(
    const QQuick3DSkyMaterial *self) {
  return self->metaObject();
}

//  void *QQuick3DSkyMaterial::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN19QQuick3DSkyMaterial11qt_metacastEPKc(
    QQuick3DSkyMaterial *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuick3DSkyMaterial::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN19QQuick3DSkyMaterial11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuick3DSkyMaterial *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuick3DSkyMaterial::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QQuick3DSkyMaterial2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuick3DSkyMaterial::tr(s, c, n));
}

//  QQuick3DSkyMaterial::QQuick3DSkyMaterial(QQuick3DObject *parent)
extern "C" Q_DECL_EXPORT
QQuick3DSkyMaterial *ritual_ZN19QQuick3DSkyMaterialC1EP14QQuick3DObject(
    QQuick3DObject *parent) {
  return new QQuick3DSkyMaterial(parent);
}

//  int QQuick3DSkyMaterial::radianceMapSize() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QQuick3DSkyMaterial15radianceMapSizeEv(
    const QQuick3DSkyMaterial *self) {
  return self->radianceMapSize();
}

//  QUrl QQuick3DSkyMaterial::fragmentShader() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK19QQuick3DSkyMaterial14fragmentShaderEv(
    const QQuick3DSkyMaterial *self) {
  return new QUrl(self->fragmentShader());
}

//  bool QQuick3DSkyMaterial::enableIBL() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QQuick3DSkyMaterial9enableIBLEv(
    const QQuick3DSkyMaterial *self) {
  return self->enableIBL();
}

//  QString QQuick3DSkyMaterial::fragmentShaderCode() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QQuick3DSkyMaterial18fragmentShaderCodeEv(
    const QQuick3DSkyMaterial *self) {
  return new QString(self->fragmentShaderCode());
}

//  int QQuick3DSkyMaterial::iblSampleCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QQuick3DSkyMaterial14iblSampleCountEv(
    const QQuick3DSkyMaterial *self) {
  return self->iblSampleCount();
}

//  int QQuick3DSkyMaterial::iblRenderFrames() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QQuick3DSkyMaterial15iblRenderFramesEv(
    const QQuick3DSkyMaterial *self) {
  return self->iblRenderFrames();
}

//  SkyboxMode QQuick3DSkyMaterial::skyboxMode() const
extern "C" Q_DECL_EXPORT
QQuick3DSkyMaterial::SkyboxMode ritual_ZNK19QQuick3DSkyMaterial10skyboxModeEv(
    const QQuick3DSkyMaterial *self) {
  return self->skyboxMode();
}

//  void QQuick3DSkyMaterial::setRadianceMapSize(int radianceMapSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DSkyMaterial18setRadianceMapSizeEi(
    QQuick3DSkyMaterial *self,
    int radianceMapSize) {
  self->setRadianceMapSize(radianceMapSize);
}

//  void QQuick3DSkyMaterial::setFragmentShader(const QUrl
//      &newFragmentShader)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DSkyMaterial17setFragmentShaderERK4QUrl(
    QQuick3DSkyMaterial *self,
    const QUrl *newFragmentShader) {
  self->setFragmentShader(*newFragmentShader);
}

//  void QQuick3DSkyMaterial::setFragmentShaderCode(const QString
//      &newFragmentShaderCode)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DSkyMaterial21setFragmentShaderCodeERK7QString(
    QQuick3DSkyMaterial *self,
    const QString *newFragmentShaderCode) {
  self->setFragmentShaderCode(*newFragmentShaderCode);
}

//  void QQuick3DSkyMaterial::setEnableIBL(bool newEnableIBL)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DSkyMaterial12setEnableIBLEb(
    QQuick3DSkyMaterial *self,
    bool newEnableIBL) {
  self->setEnableIBL(newEnableIBL);
}

//  void QQuick3DSkyMaterial::setIblSampleCount(int newIblSampleCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DSkyMaterial17setIblSampleCountEi(
    QQuick3DSkyMaterial *self,
    int newIblSampleCount) {
  self->setIblSampleCount(newIblSampleCount);
}

//  void QQuick3DSkyMaterial::setIblRenderFrames(int newIblRenderFrames)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DSkyMaterial18setIblRenderFramesEi(
    QQuick3DSkyMaterial *self,
    int newIblRenderFrames) {
  self->setIblRenderFrames(newIblRenderFrames);
}

//  void QQuick3DSkyMaterial::setSkyboxMode(SkyboxMode skyboxMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DSkyMaterial13setSkyboxModeENS_10SkyboxModeE(
    QQuick3DSkyMaterial *self,
    QQuick3DSkyMaterial::SkyboxMode skyboxMode) {
  self->setSkyboxMode(skyboxMode);
}

//  void QQuick3DSkyMaterial::radianceMapSizeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DSkyMaterial22radianceMapSizeChangedEv(
    QQuick3DSkyMaterial *self) {
  self->radianceMapSizeChanged();
}

//  void QQuick3DSkyMaterial::fragmentShaderChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DSkyMaterial21fragmentShaderChangedEv(
    QQuick3DSkyMaterial *self) {
  self->fragmentShaderChanged();
}

//  void QQuick3DSkyMaterial::fragmentShaderCodeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DSkyMaterial25fragmentShaderCodeChangedEv(
    QQuick3DSkyMaterial *self) {
  self->fragmentShaderCodeChanged();
}

//  void QQuick3DSkyMaterial::enableIBLChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DSkyMaterial16enableIBLChangedEv(
    QQuick3DSkyMaterial *self) {
  self->enableIBLChanged();
}

//  void QQuick3DSkyMaterial::iblSampleCountChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DSkyMaterial21iblSampleCountChangedEv(
    QQuick3DSkyMaterial *self) {
  self->iblSampleCountChanged();
}

//  void QQuick3DSkyMaterial::iblRenderFramesChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DSkyMaterial22iblRenderFramesChangedEv(
    QQuick3DSkyMaterial *self) {
  self->iblRenderFramesChanged();
}

//  void QQuick3DSkyMaterial::skyboxModeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DSkyMaterial17skyboxModeChangedEv(
    QQuick3DSkyMaterial *self) {
  self->skyboxModeChanged();
}

//  QSSGRenderGraphObject
//      *QQuick3DSkyMaterial::updateSpatialNode(QSSGRenderGraphObject *node)
extern "C" Q_DECL_EXPORT
QSSGRenderGraphObject *ritual_ZN19QQuick3DSkyMaterial17updateSpatialNodeEP21QSSGRenderGraphObject(
    QQuick3DSkyMaterial *self,
    QSSGRenderGraphObject *node) {
  return self->updateSpatialNode(node);
}

//  void QQuick3DSkyMaterial::markTrackedPropertyDirty(QMetaProperty
//      property, DirtyPropertyHint hint)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DSkyMaterial24markTrackedPropertyDirtyE13QMetaPropertyN30QQuick3DPropertyChangedTracker17DirtyPropertyHintE(
    QQuick3DSkyMaterial *self,
    const QMetaProperty *property,
    QQuick3DPropertyChangedTracker::DirtyPropertyHint hint) {
  self->markTrackedPropertyDirty(*property, hint);
}

//  void QQuick3DSkyMaterial::markDirty(Dirty v)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DSkyMaterial9markDirtyENS_5DirtyE(
    QQuick3DSkyMaterial *self,
    QQuick3DSkyMaterial::Dirty v) {
  self->markDirty(v);
}

//  QQuick3DSkyMaterial as the QQuick3DPropertyChangedTracker it is built on
extern "C" Q_DECL_EXPORT
QQuick3DPropertyChangedTracker *ritual_cast_QQuick3DSkyMaterial_QQuick3DPropertyChangedTracker(
    QQuick3DSkyMaterial *self) {
  return static_cast<QQuick3DPropertyChangedTracker *>(self);
}

//  QSSGRenderGraphObject
//      *QQuick3DSkyMaterial::updateSpatialNode(QSSGRenderGraphObject *node)
extern "C" Q_DECL_EXPORT
QSSGRenderGraphObject *ritual_own_ZN19QQuick3DSkyMaterial17updateSpatialNodeEP21QSSGRenderGraphObject(
    QQuick3DSkyMaterial *self,
    QSSGRenderGraphObject *node) {
  return static_cast<OwnQQuick3DSkyMaterial *>(self)->OwnQQuick3DSkyMaterial::updateSpatialNode(
      node);
}

//  void QQuick3DSkyMaterial::markTrackedPropertyDirty(QMetaProperty
//      property, DirtyPropertyHint hint)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuick3DSkyMaterial24markTrackedPropertyDirtyE13QMetaPropertyN30QQuick3DPropertyChangedTracker17DirtyPropertyHintE(
    QQuick3DSkyMaterial *self,
    const QMetaProperty *property,
    QQuick3DPropertyChangedTracker::DirtyPropertyHint hint) {
  static_cast<OwnQQuick3DSkyMaterial *>(self)->OwnQQuick3DSkyMaterial::markTrackedPropertyDirty(
      *property,
      hint);
}
