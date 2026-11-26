//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dmodel_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick3D/6.12.0/QtQuick3D/private/qtquick3dglobal_p.h>
#include <QtQuick3D/QtQuick3D>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3D/6.12.0/QtQuick3D/private/qquick3dmodel_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtGui/qmatrix4x4.h>
#include <QtGui/qvectornd.h>
#include <QtQuick3D/qquick3dobject.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>
#include <QtQml/QQmlListProperty>

//  Only a class built on QQuick3DModel may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuick3DModel : QQuick3DModel {
  using QQuick3DModel::updateSpatialNode;
  using QQuick3DModel::markAllDirty;
  using QQuick3DModel::itemChange;
};

//  A QQuick3DModel that Python can take functions over in. Every QQuick3DModel
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQQuick3DModelCall0)(const void *, QSSGRenderGraphObject *, int *);
typedef void (*CuteQQuick3DModelCall1)(const void *, int *);
typedef void (*CuteQQuick3DModelCall2)(const void *, int, const QQuick3DObject::ItemChangeData *, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DModelCall3)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DModelCall4)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DModelCall5)(const void *, int *);
typedef void (*CuteQQuick3DModelCall6)(const void *, int *);
typedef void (*CuteQQuick3DModelCall7)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DModelCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DModelCall9)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DModelCall10)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DModelCall11)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DModelCall12)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuick3DModel : public QQuick3DModel {
public:
  using QQuick3DModel::QQuick3DModel;
  void *taken[13] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN14QQuick3DObject17updateSpatialNodeEP21QSSGRenderGraphObject")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject12markAllDirtyEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[2] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject7preSyncEv")) {
      taken[7] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QSSGRenderGraphObject
  //      *QQuick3DModel::updateSpatialNode(QSSGRenderGraphObject *node)
  QSSGRenderGraphObject *updateSpatialNode(
      QSSGRenderGraphObject *node) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuick3DModelCall0 call = reinterpret_cast<CuteQQuick3DModelCall0>(taken[0]);
      void * given = call(this, node, &handled);
      if (handled) return static_cast<QSSGRenderGraphObject *>(given);
    }
    return QQuick3DModel::updateSpatialNode(node);
  }

  //  void QQuick3DModel::markAllDirty()
  void markAllDirty() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuick3DModelCall1 call = reinterpret_cast<CuteQQuick3DModelCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DModel::markAllDirty();
  }

  //  void QQuick3DModel::itemChange(ItemChange a0, const ItemChangeData
  //      &a1)
  void itemChange(
      QQuick3DObject::ItemChange a0,
      const QQuick3DObject::ItemChangeData &a1) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuick3DModelCall2 call = reinterpret_cast<CuteQQuick3DModelCall2>(taken[2]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuick3DModel::itemChange(a0, a1);
  }

#if !defined(QT_NO_QOBJECT)
  //  void QQuick3DNode::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuick3DModelCall3 call = reinterpret_cast<CuteQQuick3DModelCall3>(taken[3]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QQuick3DNode::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QQuick3DNode::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuick3DModelCall4 call = reinterpret_cast<CuteQQuick3DModelCall4>(taken[4]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QQuick3DNode::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QQuick3DNode::componentComplete()
  void componentComplete() override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuick3DModelCall5 call = reinterpret_cast<CuteQQuick3DModelCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DNode::componentComplete();
  }

  //  void QQuick3DObject::classBegin()
  void classBegin() override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuick3DModelCall6 call = reinterpret_cast<CuteQQuick3DModelCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::classBegin();
  }

  //  void QQuick3DObject::preSync()
  void preSync() override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuick3DModelCall7 call = reinterpret_cast<CuteQQuick3DModelCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::preSync();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuick3DModelCall8 call = reinterpret_cast<CuteQQuick3DModelCall8>(taken[8]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuick3DModelCall9 call = reinterpret_cast<CuteQQuick3DModelCall9>(taken[9]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuick3DModelCall10 call = reinterpret_cast<CuteQQuick3DModelCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuick3DModelCall11 call = reinterpret_cast<CuteQQuick3DModelCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuick3DModelCall12 call = reinterpret_cast<CuteQQuick3DModelCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuick3DModel::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QQuick3DModel10metaObjectEv(
    const QQuick3DModel *self) {
  return self->metaObject();
}

//  void *QQuick3DModel::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN13QQuick3DModel11qt_metacastEPKc(
    QQuick3DModel *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuick3DModel::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN13QQuick3DModel11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuick3DModel *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuick3DModel::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QQuick3DModel2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuick3DModel::tr(s, c, n));
}

//  QQuick3DModel::QQuick3DModel(QQuick3DNode *parent)
extern "C" Q_DECL_EXPORT
QQuick3DModel *ritual_ZN13QQuick3DModelC1EP12QQuick3DNode(
    QQuick3DNode *parent) {
  return new CuteQQuick3DModel(parent);
}

//  QQuick3DModel::~QQuick3DModel()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuick3DModelD1Ev(QQuick3DModel *self) {
  delete self;
}

//  QUrl QQuick3DModel::source() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK13QQuick3DModel6sourceEv(const QQuick3DModel *self) {
  return new QUrl(self->source());
}

//  bool QQuick3DModel::castsShadows() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QQuick3DModel12castsShadowsEv(const QQuick3DModel *self) {
  return self->castsShadows();
}

//  bool QQuick3DModel::receivesShadows() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QQuick3DModel15receivesShadowsEv(
    const QQuick3DModel *self) {
  return self->receivesShadows();
}

//  bool QQuick3DModel::pickable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QQuick3DModel8pickableEv(const QQuick3DModel *self) {
  return self->pickable();
}

//  QQuick3DGeometry *QQuick3DModel::geometry() const
extern "C" Q_DECL_EXPORT
QQuick3DGeometry *ritual_ZNK13QQuick3DModel8geometryEv(
    const QQuick3DModel *self) {
  return self->geometry();
}

//  QQuick3DSkeleton *QQuick3DModel::skeleton() const
extern "C" Q_DECL_EXPORT
QQuick3DSkeleton *ritual_ZNK13QQuick3DModel8skeletonEv(
    const QQuick3DModel *self) {
  return self->skeleton();
}

//  QList<QMatrix4x4> QQuick3DModel::inverseBindPoses() const
extern "C" Q_DECL_EXPORT
QList<QMatrix4x4> *ritual_ZNK13QQuick3DModel16inverseBindPosesEv(
    const QQuick3DModel *self) {
  return new QList<QMatrix4x4>(self->inverseBindPoses());
}

//  QQuick3DBounds3 QQuick3DModel::bounds() const
extern "C" Q_DECL_EXPORT
QQuick3DBounds3 *ritual_ZNK13QQuick3DModel6boundsEv(
    const QQuick3DModel *self) {
  return new QQuick3DBounds3(self->bounds());
}

//  float QQuick3DModel::depthBias() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK13QQuick3DModel9depthBiasEv(const QQuick3DModel *self) {
  return self->depthBias();
}

//  QQmlListProperty<QQuick3DMaterial> QQuick3DModel::materials()
extern "C" Q_DECL_EXPORT
QQmlListProperty<QQuick3DMaterial> *ritual_ZN13QQuick3DModel9materialsEv(
    QQuick3DModel *self) {
  return new QQmlListProperty<QQuick3DMaterial>(self->materials());
}

//  QQmlListProperty<QQuick3DMorphTarget> QQuick3DModel::morphTargets()
extern "C" Q_DECL_EXPORT
QQmlListProperty<QQuick3DMorphTarget> *ritual_ZN13QQuick3DModel12morphTargetsEv(
    QQuick3DModel *self) {
  return new QQmlListProperty<QQuick3DMorphTarget>(self->morphTargets());
}

//  QQuick3DInstancing *QQuick3DModel::instancing() const
extern "C" Q_DECL_EXPORT
QQuick3DInstancing *ritual_ZNK13QQuick3DModel10instancingEv(
    const QQuick3DModel *self) {
  return self->instancing();
}

//  QQuick3DNode *QQuick3DModel::instanceRoot() const
extern "C" Q_DECL_EXPORT
QQuick3DNode *ritual_ZNK13QQuick3DModel12instanceRootEv(
    const QQuick3DModel *self) {
  return self->instanceRoot();
}

//  bool QQuick3DModel::receivesReflections() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QQuick3DModel19receivesReflectionsEv(
    const QQuick3DModel *self) {
  return self->receivesReflections();
}

//  bool QQuick3DModel::castsReflections() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QQuick3DModel16castsReflectionsEv(
    const QQuick3DModel *self) {
  return self->castsReflections();
}

//  QQuick3DSkin *QQuick3DModel::skin() const
extern "C" Q_DECL_EXPORT
QQuick3DSkin *ritual_ZNK13QQuick3DModel4skinEv(const QQuick3DModel *self) {
  return self->skin();
}

//  QString QQuick3DModel::translateMeshSource(const QUrl &source, QObject
//      *contextObject)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QQuick3DModel19translateMeshSourceERK4QUrlP7QObject(
    const QUrl *source,
    QObject *contextObject) {
  return new QString(
      QQuick3DModel::translateMeshSource(
          *source,
          contextObject));
}

//  bool QQuick3DModel::isUsedInBakedLighting() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QQuick3DModel21isUsedInBakedLightingEv(
    const QQuick3DModel *self) {
  return self->isUsedInBakedLighting();
}

//  int QQuick3DModel::lightmapBaseResolution() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QQuick3DModel22lightmapBaseResolutionEv(
    const QQuick3DModel *self) {
  return self->lightmapBaseResolution();
}

//  QQuick3DBakedLightmap *QQuick3DModel::bakedLightmap() const
extern "C" Q_DECL_EXPORT
QQuick3DBakedLightmap *ritual_ZNK13QQuick3DModel13bakedLightmapEv(
    const QQuick3DModel *self) {
  return self->bakedLightmap();
}

//  float QQuick3DModel::instancingLodMin() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK13QQuick3DModel16instancingLodMinEv(
    const QQuick3DModel *self) {
  return self->instancingLodMin();
}

//  float QQuick3DModel::instancingLodMax() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK13QQuick3DModel16instancingLodMaxEv(
    const QQuick3DModel *self) {
  return self->instancingLodMax();
}

//  float QQuick3DModel::levelOfDetailBias() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK13QQuick3DModel17levelOfDetailBiasEv(
    const QQuick3DModel *self) {
  return self->levelOfDetailBias();
}

//  float QQuick3DModel::instancingLodFactor() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK13QQuick3DModel19instancingLodFactorEv(
    const QQuick3DModel *self) {
  return self->instancingLodFactor();
}

//  float QQuick3DModel::texelsPerUnit() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK13QQuick3DModel13texelsPerUnitEv(const QQuick3DModel *self) {
  return self->texelsPerUnit();
}

//  void QQuick3DModel::setTexelsPerUnit(float newTexelsPerUnit)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuick3DModel16setTexelsPerUnitEf(
    QQuick3DModel *self,
    float newTexelsPerUnit) {
  self->setTexelsPerUnit(newTexelsPerUnit);
}

//  bool QQuick3DModel::motionVectorEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QQuick3DModel19motionVectorEnabledEv(
    const QQuick3DModel *self) {
  return self->motionVectorEnabled();
}

//  float QQuick3DModel::motionVectorScale() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK13QQuick3DModel17motionVectorScaleEv(
    const QQuick3DModel *self) {
  return self->motionVectorScale();
}

//  void QQuick3DModel::setSource(const QUrl &source)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuick3DModel9setSourceERK4QUrl(
    QQuick3DModel *self,
    const QUrl *source) {
  self->setSource(*source);
}

//  void QQuick3DModel::setCastsShadows(bool castsShadows)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuick3DModel15setCastsShadowsEb(
    QQuick3DModel *self,
    bool castsShadows) {
  self->setCastsShadows(castsShadows);
}

//  void QQuick3DModel::setReceivesShadows(bool receivesShadows)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuick3DModel18setReceivesShadowsEb(
    QQuick3DModel *self,
    bool receivesShadows) {
  self->setReceivesShadows(receivesShadows);
}

//  void QQuick3DModel::setPickable(bool pickable)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuick3DModel11setPickableEb(
    QQuick3DModel *self,
    bool pickable) {
  self->setPickable(pickable);
}

//  void QQuick3DModel::setGeometry(QQuick3DGeometry *geometry)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuick3DModel11setGeometryEP16QQuick3DGeometry(
    QQuick3DModel *self,
    QQuick3DGeometry *geometry) {
  self->setGeometry(geometry);
}

//  void QQuick3DModel::setSkeleton(QQuick3DSkeleton *skeleton)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuick3DModel11setSkeletonEP16QQuick3DSkeleton(
    QQuick3DModel *self,
    QQuick3DSkeleton *skeleton) {
  self->setSkeleton(skeleton);
}

//  void QQuick3DModel::setInverseBindPoses(const QList<QMatrix4x4> &poses)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuick3DModel19setInverseBindPosesERK5QListI10QMatrix4x4E(
    QQuick3DModel *self,
    const QList<QMatrix4x4> *poses) {
  self->setInverseBindPoses(*poses);
}

//  void QQuick3DModel::setBounds(const QVector3D &min, const QVector3D &max)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuick3DModel9setBoundsERK9QVector3DS2_(
    QQuick3DModel *self,
    const QVector3D *min,
    const QVector3D *max) {
  self->setBounds(*min, *max);
}

//  void QQuick3DModel::setInstancing(QQuick3DInstancing *instancing)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuick3DModel13setInstancingEP18QQuick3DInstancing(
    QQuick3DModel *self,
    QQuick3DInstancing *instancing) {
  self->setInstancing(instancing);
}

//  void QQuick3DModel::setInstanceRoot(QQuick3DNode *instanceRoot)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuick3DModel15setInstanceRootEP12QQuick3DNode(
    QQuick3DModel *self,
    QQuick3DNode *instanceRoot) {
  self->setInstanceRoot(instanceRoot);
}

//  void QQuick3DModel::setDepthBias(float bias)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuick3DModel12setDepthBiasEf(
    QQuick3DModel *self,
    float bias) {
  self->setDepthBias(bias);
}

//  void QQuick3DModel::setReceivesReflections(bool receivesReflections)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuick3DModel22setReceivesReflectionsEb(
    QQuick3DModel *self,
    bool receivesReflections) {
  self->setReceivesReflections(receivesReflections);
}

//  void QQuick3DModel::setCastsReflections(bool castsReflections)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuick3DModel19setCastsReflectionsEb(
    QQuick3DModel *self,
    bool castsReflections) {
  self->setCastsReflections(castsReflections);
}

//  void QQuick3DModel::setSkin(QQuick3DSkin *skin)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuick3DModel7setSkinEP12QQuick3DSkin(
    QQuick3DModel *self,
    QQuick3DSkin *skin) {
  self->setSkin(skin);
}

//  void QQuick3DModel::setUsedInBakedLighting(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuick3DModel22setUsedInBakedLightingEb(
    QQuick3DModel *self,
    bool enable) {
  self->setUsedInBakedLighting(enable);
}

//  void QQuick3DModel::setLightmapBaseResolution(int resolution)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuick3DModel25setLightmapBaseResolutionEi(
    QQuick3DModel *self,
    int resolution) {
  self->setLightmapBaseResolution(resolution);
}

//  void QQuick3DModel::setBakedLightmap(QQuick3DBakedLightmap
//      *bakedLightmap)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuick3DModel16setBakedLightmapEP21QQuick3DBakedLightmap(
    QQuick3DModel *self,
    QQuick3DBakedLightmap *bakedLightmap) {
  self->setBakedLightmap(bakedLightmap);
}

//  void QQuick3DModel::setInstancingLodMin(float minDistance)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuick3DModel19setInstancingLodMinEf(
    QQuick3DModel *self,
    float minDistance) {
  self->setInstancingLodMin(minDistance);
}

//  void QQuick3DModel::setInstancingLodMax(float maxDistance)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuick3DModel19setInstancingLodMaxEf(
    QQuick3DModel *self,
    float maxDistance) {
  self->setInstancingLodMax(maxDistance);
}

//  void QQuick3DModel::setLevelOfDetailBias(float newLevelOfDetailBias)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuick3DModel20setLevelOfDetailBiasEf(
    QQuick3DModel *self,
    float newLevelOfDetailBias) {
  self->setLevelOfDetailBias(newLevelOfDetailBias);
}

//  void QQuick3DModel::setInstancingLodFactor(float newInstancingLodFactor)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuick3DModel22setInstancingLodFactorEf(
    QQuick3DModel *self,
    float newInstancingLodFactor) {
  self->setInstancingLodFactor(newInstancingLodFactor);
}

//  void QQuick3DModel::setMotionVectorScale(float newMotionVectorScale)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuick3DModel20setMotionVectorScaleEf(
    QQuick3DModel *self,
    float newMotionVectorScale) {
  self->setMotionVectorScale(newMotionVectorScale);
}

//  void QQuick3DModel::setMotionVectorEnabled(bool newMotionVectorEnabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuick3DModel22setMotionVectorEnabledEb(
    QQuick3DModel *self,
    bool newMotionVectorEnabled) {
  self->setMotionVectorEnabled(newMotionVectorEnabled);
}

//  void QQuick3DModel::sourceChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuick3DModel13sourceChangedEv(QQuick3DModel *self) {
  self->sourceChanged();
}

//  void QQuick3DModel::castsShadowsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuick3DModel19castsShadowsChangedEv(QQuick3DModel *self) {
  self->castsShadowsChanged();
}

//  void QQuick3DModel::receivesShadowsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuick3DModel22receivesShadowsChangedEv(
    QQuick3DModel *self) {
  self->receivesShadowsChanged();
}

//  void QQuick3DModel::pickableChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuick3DModel15pickableChangedEv(QQuick3DModel *self) {
  self->pickableChanged();
}

//  void QQuick3DModel::geometryChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuick3DModel15geometryChangedEv(QQuick3DModel *self) {
  self->geometryChanged();
}

//  void QQuick3DModel::skeletonChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuick3DModel15skeletonChangedEv(QQuick3DModel *self) {
  self->skeletonChanged();
}

//  void QQuick3DModel::inverseBindPosesChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuick3DModel23inverseBindPosesChangedEv(
    QQuick3DModel *self) {
  self->inverseBindPosesChanged();
}

//  void QQuick3DModel::boundsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuick3DModel13boundsChangedEv(QQuick3DModel *self) {
  self->boundsChanged();
}

//  void QQuick3DModel::instancingChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuick3DModel17instancingChangedEv(QQuick3DModel *self) {
  self->instancingChanged();
}

//  void QQuick3DModel::instanceRootChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuick3DModel19instanceRootChangedEv(QQuick3DModel *self) {
  self->instanceRootChanged();
}

//  void QQuick3DModel::morphTargetsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuick3DModel19morphTargetsChangedEv(QQuick3DModel *self) {
  self->morphTargetsChanged();
}

//  void QQuick3DModel::depthBiasChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuick3DModel16depthBiasChangedEv(QQuick3DModel *self) {
  self->depthBiasChanged();
}

//  void QQuick3DModel::receivesReflectionsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuick3DModel26receivesReflectionsChangedEv(
    QQuick3DModel *self) {
  self->receivesReflectionsChanged();
}

//  void QQuick3DModel::castsReflectionsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuick3DModel23castsReflectionsChangedEv(
    QQuick3DModel *self) {
  self->castsReflectionsChanged();
}

//  void QQuick3DModel::skinChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuick3DModel11skinChangedEv(QQuick3DModel *self) {
  self->skinChanged();
}

//  void QQuick3DModel::usedInBakedLightingChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuick3DModel26usedInBakedLightingChangedEv(
    QQuick3DModel *self) {
  self->usedInBakedLightingChanged();
}

//  void QQuick3DModel::lightmapBaseResolutionChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuick3DModel29lightmapBaseResolutionChangedEv(
    QQuick3DModel *self) {
  self->lightmapBaseResolutionChanged();
}

//  void QQuick3DModel::bakedLightmapChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuick3DModel20bakedLightmapChangedEv(QQuick3DModel *self) {
  self->bakedLightmapChanged();
}

//  void QQuick3DModel::instancingLodMinChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuick3DModel23instancingLodMinChangedEv(
    QQuick3DModel *self) {
  self->instancingLodMinChanged();
}

//  void QQuick3DModel::instancingLodMaxChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuick3DModel23instancingLodMaxChangedEv(
    QQuick3DModel *self) {
  self->instancingLodMaxChanged();
}

//  void QQuick3DModel::instancingLodFactorChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuick3DModel26instancingLodFactorChangedEv(
    QQuick3DModel *self) {
  self->instancingLodFactorChanged();
}

//  void QQuick3DModel::levelOfDetailBiasChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuick3DModel24levelOfDetailBiasChangedEv(
    QQuick3DModel *self) {
  self->levelOfDetailBiasChanged();
}

//  void QQuick3DModel::texelsPerUnitChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuick3DModel20texelsPerUnitChangedEv(QQuick3DModel *self) {
  self->texelsPerUnitChanged();
}

//  void QQuick3DModel::motionVectorEnabledChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuick3DModel26motionVectorEnabledChangedEv(
    QQuick3DModel *self) {
  self->motionVectorEnabledChanged();
}

//  void QQuick3DModel::motionVectorScaleChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuick3DModel24motionVectorScaleChangedEv(
    QQuick3DModel *self) {
  self->motionVectorScaleChanged();
}

//  QSSGRenderGraphObject
//      *QQuick3DModel::updateSpatialNode(QSSGRenderGraphObject *node)
extern "C" Q_DECL_EXPORT
QSSGRenderGraphObject *ritual_ZN13QQuick3DModel17updateSpatialNodeEP21QSSGRenderGraphObject(
    QQuick3DModel *self,
    QSSGRenderGraphObject *node) {
  return self->updateSpatialNode(node);
}

//  void QQuick3DModel::markAllDirty()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuick3DModel12markAllDirtyEv(QQuick3DModel *self) {
  self->markAllDirty();
}

//  void QQuick3DModel::itemChange(ItemChange a0, const ItemChangeData &a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuick3DModel10itemChangeEN14QQuick3DObject10ItemChangeERKNS0_14ItemChangeDataE(
    QQuick3DModel *self,
    QQuick3DObject::ItemChange a0,
    const QQuick3DObject::ItemChangeData *a1) {
  self->itemChange(a0, *a1);
}

//  void QQuick3DModel::onMaterialDestroyed(QObject *object)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuick3DModel19onMaterialDestroyedEP7QObject(
    QQuick3DModel *self,
    QObject *object) {
  self->onMaterialDestroyed(object);
}

//  void QQuick3DModel::onMorphTargetDestroyed(QObject *object)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuick3DModel22onMorphTargetDestroyedEP7QObject(
    QQuick3DModel *self,
    QObject *object) {
  self->onMorphTargetDestroyed(object);
}

//  void QQuick3DModel::markDirty(QSSGModelDirtyType type)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuick3DModel9markDirtyENS_18QSSGModelDirtyTypeE(
    QQuick3DModel *self,
    QQuick3DModel::QSSGModelDirtyType type) {
  self->markDirty(type);
}

//  void QQuick3DModel::updateSceneManager(QQuick3DSceneManager
//      *sceneManager)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuick3DModel18updateSceneManagerEP20QQuick3DSceneManager(
    QQuick3DModel *self,
    QQuick3DSceneManager *sceneManager) {
  self->updateSceneManager(sceneManager);
}

//  void QQuick3DModel::qmlAppendMaterial(QQmlListProperty<QQuick3DMaterial>
//      *list, QQuick3DMaterial *material)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuick3DModel17qmlAppendMaterialEP16QQmlListPropertyI16QQuick3DMaterialEPS1_(
    QQmlListProperty<QQuick3DMaterial> *list,
    QQuick3DMaterial *material) {
  QQuick3DModel::qmlAppendMaterial(list, material);
}

//  QQuick3DMaterial
//      *QQuick3DModel::qmlMaterialAt(QQmlListProperty<QQuick3DMaterial>
//      *list, qsizetype index)
extern "C" Q_DECL_EXPORT
QQuick3DMaterial *ritual_ZN13QQuick3DModel13qmlMaterialAtEP16QQmlListPropertyI16QQuick3DMaterialEx(
    QQmlListProperty<QQuick3DMaterial> *list,
    qsizetype index) {
  return QQuick3DModel::qmlMaterialAt(list, index);
}

//  qsizetype
//      QQuick3DModel::qmlMaterialsCount(QQmlListProperty<QQuick3DMaterial>
//      *list)
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN13QQuick3DModel17qmlMaterialsCountEP16QQmlListPropertyI16QQuick3DMaterialE(
    QQmlListProperty<QQuick3DMaterial> *list) {
  return QQuick3DModel::qmlMaterialsCount(list);
}

//  void QQuick3DModel::qmlClearMaterials(QQmlListProperty<QQuick3DMaterial>
//      *list)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuick3DModel17qmlClearMaterialsEP16QQmlListPropertyI16QQuick3DMaterialE(
    QQmlListProperty<QQuick3DMaterial> *list) {
  QQuick3DModel::qmlClearMaterials(list);
}

//  void
//      QQuick3DModel::qmlAppendMorphTarget(QQmlListProperty<QQuick3DMorphTar
//      get> *list, QQuick3DMorphTarget *morphTarget)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuick3DModel20qmlAppendMorphTargetEP16QQmlListPropertyI19QQuick3DMorphTargetEPS1_(
    QQmlListProperty<QQuick3DMorphTarget> *list,
    QQuick3DMorphTarget *morphTarget) {
  QQuick3DModel::qmlAppendMorphTarget(list, morphTarget);
}

//  QQuick3DMorphTarget
//      *QQuick3DModel::qmlMorphTargetAt(QQmlListProperty<QQuick3DMorphTarget
//      > *list, qsizetype index)
extern "C" Q_DECL_EXPORT
QQuick3DMorphTarget *ritual_ZN13QQuick3DModel16qmlMorphTargetAtEP16QQmlListPropertyI19QQuick3DMorphTargetEx(
    QQmlListProperty<QQuick3DMorphTarget> *list,
    qsizetype index) {
  return QQuick3DModel::qmlMorphTargetAt(list, index);
}

//  qsizetype
//      QQuick3DModel::qmlMorphTargetsCount(QQmlListProperty<QQuick3DMorphTar
//      get> *list)
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN13QQuick3DModel20qmlMorphTargetsCountEP16QQmlListPropertyI19QQuick3DMorphTargetE(
    QQmlListProperty<QQuick3DMorphTarget> *list) {
  return QQuick3DModel::qmlMorphTargetsCount(list);
}

//  void
//      QQuick3DModel::qmlClearMorphTargets(QQmlListProperty<QQuick3DMorphTar
//      get> *list)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuick3DModel20qmlClearMorphTargetsEP16QQmlListPropertyI19QQuick3DMorphTargetE(
    QQmlListProperty<QQuick3DMorphTarget> *list) {
  QQuick3DModel::qmlClearMorphTargets(list);
}

//  a Python function taken by a CuteQQuick3DModel, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuick3DModel(
    QQuick3DModel *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuick3DModel *>(self)->take(key, call);
}

//  QSSGRenderGraphObject
//      *QQuick3DModel::updateSpatialNode(QSSGRenderGraphObject *node)
extern "C" Q_DECL_EXPORT
QSSGRenderGraphObject *ritual_own_ZN13QQuick3DModel17updateSpatialNodeEP21QSSGRenderGraphObject(
    QQuick3DModel *self,
    QSSGRenderGraphObject *node) {
  return static_cast<OwnQQuick3DModel *>(self)->OwnQQuick3DModel::updateSpatialNode(
      node);
}

//  void QQuick3DModel::markAllDirty()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QQuick3DModel12markAllDirtyEv(QQuick3DModel *self) {
  static_cast<OwnQQuick3DModel *>(self)->OwnQQuick3DModel::markAllDirty();
}

//  void QQuick3DModel::itemChange(ItemChange a0, const ItemChangeData &a1)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QQuick3DModel10itemChangeEN14QQuick3DObject10ItemChangeERKNS0_14ItemChangeDataE(
    QQuick3DModel *self,
    QQuick3DObject::ItemChange a0,
    const QQuick3DObject::ItemChangeData *a1) {
  static_cast<OwnQQuick3DModel *>(self)->OwnQQuick3DModel::itemChange(
      a0,
      *a1);
}

//  a QQmlListProperty<QQuick3DMaterial> a ritual of QQuick3DModel gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQuick3DModel__QQmlListProperty_QQuick3DMaterial(
    QQmlListProperty<QQuick3DMaterial> *self) {
  delete self;
}

//  a QQmlListProperty<QQuick3DMorphTarget> a ritual of QQuick3DModel gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQuick3DModel__QQmlListProperty_QQuick3DMorphTarget(
    QQmlListProperty<QQuick3DMorphTarget> *self) {
  delete self;
}
