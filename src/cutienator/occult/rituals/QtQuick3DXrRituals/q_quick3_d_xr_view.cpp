//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3DXr/6.12.0/QtQuick3DXr/private/qquick3dxrview_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick3DXr/6.12.0/QtQuick3DXr/private/qtquick3dxrglobal_p.h>
#include <QtQuick3DXr/QtQuick3DXr>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DXr/6.12.0/QtQuick3DXr/private/qquick3dxrview_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qvectornd.h>
#include <QtQuick3D/QtQuick3D>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3D/6.12.0/QtQuick3D/private/qquick3dpickresult_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <QtQuick3D/qquick3dobject.h>
#include <QtCore/qlist.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <cstring>
#include <QtGui/QVector3D>

//  A QQuick3DXrView that Python can take functions over in. Every QQuick3DXrView
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuick3DXrViewCall0)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DXrViewCall1)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DXrViewCall2)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DXrViewCall3)(const void *, int *);
typedef void * (*CuteQQuick3DXrViewCall4)(const void *, QSSGRenderGraphObject *, int *);
typedef void (*CuteQQuick3DXrViewCall5)(const void *, int, const QQuick3DObject::ItemChangeData *, int *);
typedef void (*CuteQQuick3DXrViewCall6)(const void *, int *);
typedef void (*CuteQQuick3DXrViewCall7)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DXrViewCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DXrViewCall9)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DXrViewCall10)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DXrViewCall11)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DXrViewCall12)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuick3DXrView : public QQuick3DXrView {
public:
  using QQuick3DXrView::QQuick3DXrView;
  void *taken[13] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN14QQuick3DObject12markAllDirtyEv")) {
      taken[0] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject17updateSpatialNodeEP21QSSGRenderGraphObject")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
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

  //  void QQuick3DNode::markAllDirty()
  void markAllDirty() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuick3DXrViewCall0 call = reinterpret_cast<CuteQQuick3DXrViewCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DNode::markAllDirty();
  }

#if !defined(QT_NO_QOBJECT)
  //  void QQuick3DNode::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuick3DXrViewCall1 call = reinterpret_cast<CuteQQuick3DXrViewCall1>(taken[1]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QQuick3DNode::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QQuick3DNode::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuick3DXrViewCall2 call = reinterpret_cast<CuteQQuick3DXrViewCall2>(taken[2]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QQuick3DNode::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QQuick3DNode::componentComplete()
  void componentComplete() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuick3DXrViewCall3 call = reinterpret_cast<CuteQQuick3DXrViewCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DNode::componentComplete();
  }

  //  QSSGRenderGraphObject
  //      *QQuick3DNode::updateSpatialNode(QSSGRenderGraphObject *node)
  QSSGRenderGraphObject *updateSpatialNode(
      QSSGRenderGraphObject *node) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuick3DXrViewCall4 call = reinterpret_cast<CuteQQuick3DXrViewCall4>(taken[4]);
      void * given = call(this, node, &handled);
      if (handled) return static_cast<QSSGRenderGraphObject *>(given);
    }
    return QQuick3DNode::updateSpatialNode(node);
  }

  //  void QQuick3DNode::itemChange(ItemChange a0, const ItemChangeData
  //      &a1)
  void itemChange(
      QQuick3DObject::ItemChange a0,
      const QQuick3DObject::ItemChangeData &a1) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuick3DXrViewCall5 call = reinterpret_cast<CuteQQuick3DXrViewCall5>(taken[5]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuick3DNode::itemChange(a0, a1);
  }

  //  void QQuick3DObject::classBegin()
  void classBegin() override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuick3DXrViewCall6 call = reinterpret_cast<CuteQQuick3DXrViewCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::classBegin();
  }

  //  void QQuick3DObject::preSync()
  void preSync() override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuick3DXrViewCall7 call = reinterpret_cast<CuteQQuick3DXrViewCall7>(taken[7]);
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
      CuteQQuick3DXrViewCall8 call = reinterpret_cast<CuteQQuick3DXrViewCall8>(taken[8]);
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
      CuteQQuick3DXrViewCall9 call = reinterpret_cast<CuteQQuick3DXrViewCall9>(taken[9]);
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
      CuteQQuick3DXrViewCall10 call = reinterpret_cast<CuteQQuick3DXrViewCall10>(taken[10]);
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
      CuteQQuick3DXrViewCall11 call = reinterpret_cast<CuteQQuick3DXrViewCall11>(taken[11]);
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
      CuteQQuick3DXrViewCall12 call = reinterpret_cast<CuteQQuick3DXrViewCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuick3DXrView::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QQuick3DXrView10metaObjectEv(
    const QQuick3DXrView *self) {
  return self->metaObject();
}

//  void *QQuick3DXrView::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN14QQuick3DXrView11qt_metacastEPKc(
    QQuick3DXrView *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuick3DXrView::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN14QQuick3DXrView11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuick3DXrView *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuick3DXrView::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QQuick3DXrView2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuick3DXrView::tr(s, c, n));
}

//  QQuick3DXrView::QQuick3DXrView()
extern "C" Q_DECL_EXPORT
QQuick3DXrView *ritual_ZN14QQuick3DXrViewC1Ev() {
  return new CuteQQuick3DXrView();
}

//  QQuick3DXrView::~QQuick3DXrView()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuick3DXrViewD1Ev(QQuick3DXrView *self) {
  delete self;
}

//  QQuick3DXrOrigin *QQuick3DXrView::xrOrigin() const
extern "C" Q_DECL_EXPORT
QQuick3DXrOrigin *ritual_ZNK14QQuick3DXrView8xrOriginEv(
    const QQuick3DXrView *self) {
  return self->xrOrigin();
}

//  QQuick3DSceneEnvironment *QQuick3DXrView::environment() const
extern "C" Q_DECL_EXPORT
QQuick3DSceneEnvironment *ritual_ZNK14QQuick3DXrView11environmentEv(
    const QQuick3DXrView *self) {
  return self->environment();
}

//  bool QQuick3DXrView::passthroughSupported() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QQuick3DXrView20passthroughSupportedEv(
    const QQuick3DXrView *self) {
  return self->passthroughSupported();
}

//  bool QQuick3DXrView::passthroughEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QQuick3DXrView18passthroughEnabledEv(
    const QQuick3DXrView *self) {
  return self->passthroughEnabled();
}

//  FoveationLevel QQuick3DXrView::fixedFoveation() const
extern "C" Q_DECL_EXPORT
QQuick3DXrView::FoveationLevel ritual_ZNK14QQuick3DXrView14fixedFoveationEv(
    const QQuick3DXrView *self) {
  return self->fixedFoveation();
}

//  void QQuick3DXrView::setFixedFoveation(FoveationLevel level)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuick3DXrView17setFixedFoveationENS_14FoveationLevelE(
    QQuick3DXrView *self,
    QQuick3DXrView::FoveationLevel level) {
  self->setFixedFoveation(level);
}

//  QQuick3DXrRuntimeInfo *QQuick3DXrView::runtimeInfo() const
extern "C" Q_DECL_EXPORT
QQuick3DXrRuntimeInfo *ritual_ZNK14QQuick3DXrView11runtimeInfoEv(
    const QQuick3DXrView *self) {
  return self->runtimeInfo();
}

//  bool QQuick3DXrView::isQuitOnSessionEndEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QQuick3DXrView25isQuitOnSessionEndEnabledEv(
    const QQuick3DXrView *self) {
  return self->isQuitOnSessionEndEnabled();
}

//  QQuick3DRenderStats *QQuick3DXrView::renderStats() const
extern "C" Q_DECL_EXPORT
QQuick3DRenderStats *ritual_ZNK14QQuick3DXrView11renderStatsEv(
    const QQuick3DXrView *self) {
  return self->renderStats();
}

//  QQuick3DPickResult QQuick3DXrView::rayPick(const QVector3D &origin, const
//      QVector3D &direction) const
extern "C" Q_DECL_EXPORT
QQuick3DPickResult *ritual_ZNK14QQuick3DXrView7rayPickERK9QVector3DS2_(
    const QQuick3DXrView *self,
    const QVector3D *origin,
    const QVector3D *direction) {
  return new QQuick3DPickResult(self->rayPick(*origin, *direction));
}

//  QList<QQuick3DPickResult> QQuick3DXrView::rayPickAll(const QVector3D
//      &origin, const QVector3D &direction) const
extern "C" Q_DECL_EXPORT
QList<QQuick3DPickResult> *ritual_ZNK14QQuick3DXrView10rayPickAllERK9QVector3DS2_(
    const QQuick3DXrView *self,
    const QVector3D *origin,
    const QVector3D *direction) {
  return new QList<QQuick3DPickResult>(
      self->rayPickAll(
          *origin,
          *direction));
}

//  QQuick3DPickResult QQuick3DXrView::rayPick(const QVector3D &origin, const
//      QVector3D &direction, QQuick3DModel *model) const
extern "C" Q_DECL_EXPORT
QQuick3DPickResult *ritual_ZNK14QQuick3DXrView7rayPickERK9QVector3DS2_P13QQuick3DModel(
    const QQuick3DXrView *self,
    const QVector3D *origin,
    const QVector3D *direction,
    QQuick3DModel *model) {
  return new QQuick3DPickResult(self->rayPick(*origin, *direction, model));
}

//  QQuick3DPickResult QQuick3DXrView::closestPointPick(const QVector3D
//      &origin, float radius, QQuick3DModel *model) const
extern "C" Q_DECL_EXPORT
QQuick3DPickResult *ritual_ZNK14QQuick3DXrView16closestPointPickERK9QVector3DfP13QQuick3DModel(
    const QQuick3DXrView *self,
    const QVector3D *origin,
    float radius,
    QQuick3DModel *model) {
  return new QQuick3DPickResult(
      self->closestPointPick(
          *origin,
          radius,
          model));
}

//  void QQuick3DXrView::setTouchpoint(QQuickItem *target, const QPointF
//      &position, int pointId, bool active)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuick3DXrView13setTouchpointEP10QQuickItemRK7QPointFib(
    QQuick3DXrView *self,
    QQuickItem *target,
    const QPointF *position,
    int pointId,
    bool active) {
  self->setTouchpoint(target, *position, pointId, active);
}

//  QVector3D QQuick3DXrView::processTouch(const QVector3D &pos, int pointId)
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZN14QQuick3DXrView12processTouchERK9QVector3Di(
    QQuick3DXrView *self,
    const QVector3D *pos,
    int pointId) {
  return new QVector3D(self->processTouch(*pos, pointId));
}

//  QVariantMap QQuick3DXrView::touchpointState(int pointId) const
extern "C" Q_DECL_EXPORT
QMap<QString, QVariant> *ritual_ZNK14QQuick3DXrView15touchpointStateEi(
    const QQuick3DXrView *self,
    int pointId) {
  return new QMap<QString, QVariant>(self->touchpointState(pointId));
}

//  ReferenceSpace QQuick3DXrView::referenceSpace() const
extern "C" Q_DECL_EXPORT
QQuick3DXrView::ReferenceSpace ritual_ZNK14QQuick3DXrView14referenceSpaceEv(
    const QQuick3DXrView *self) {
  return self->referenceSpace();
}

//  void QQuick3DXrView::setReferenceSpace(ReferenceSpace newReferenceSpace)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuick3DXrView17setReferenceSpaceENS_14ReferenceSpaceE(
    QQuick3DXrView *self,
    QQuick3DXrView::ReferenceSpace newReferenceSpace) {
  self->setReferenceSpace(newReferenceSpace);
}

//  bool QQuick3DXrView::depthSubmissionEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QQuick3DXrView22depthSubmissionEnabledEv(
    const QQuick3DXrView *self) {
  return self->depthSubmissionEnabled();
}

//  void QQuick3DXrView::registerXrItem(QQuick3DXrItem *newXrItem)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuick3DXrView14registerXrItemEP14QQuick3DXrItem(
    QQuick3DXrView *self,
    QQuick3DXrItem *newXrItem) {
  self->registerXrItem(newXrItem);
}

//  void QQuick3DXrView::unregisterXrItem(QQuick3DXrItem *xrItem)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuick3DXrView16unregisterXrItemEP14QQuick3DXrItem(
    QQuick3DXrView *self,
    QQuick3DXrItem *xrItem) {
  self->unregisterXrItem(xrItem);
}

//  bool QQuick3DXrView::isMultiViewRenderingSupported() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QQuick3DXrView29isMultiViewRenderingSupportedEv(
    const QQuick3DXrView *self) {
  return self->isMultiViewRenderingSupported();
}

//  bool QQuick3DXrView::multiViewRenderingEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QQuick3DXrView25multiViewRenderingEnabledEv(
    const QQuick3DXrView *self) {
  return self->multiViewRenderingEnabled();
}

//  QQuick3DXrManager *QQuick3DXrView::xrManager()
extern "C" Q_DECL_EXPORT
QQuick3DXrManager *ritual_ZN14QQuick3DXrView9xrManagerEv(
    QQuick3DXrView *self) {
  return self->xrManager();
}

//  void QQuick3DXrView::setEnvironment(QQuick3DSceneEnvironment
//      *environment)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuick3DXrView14setEnvironmentEP24QQuick3DSceneEnvironment(
    QQuick3DXrView *self,
    QQuick3DSceneEnvironment *environment) {
  self->setEnvironment(environment);
}

//  void QQuick3DXrView::setPassthroughEnabled(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuick3DXrView21setPassthroughEnabledEb(
    QQuick3DXrView *self,
    bool enable) {
  self->setPassthroughEnabled(enable);
}

//  void QQuick3DXrView::setQuitOnSessionEnd(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuick3DXrView19setQuitOnSessionEndEb(
    QQuick3DXrView *self,
    bool enable) {
  self->setQuitOnSessionEnd(enable);
}

//  void QQuick3DXrView::setDepthSubmissionEnabled(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuick3DXrView25setDepthSubmissionEnabledEb(
    QQuick3DXrView *self,
    bool enable) {
  self->setDepthSubmissionEnabled(enable);
}

//  void QQuick3DXrView::setXROrigin(QQuick3DXrOrigin *newXrOrigin)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuick3DXrView11setXROriginEP16QQuick3DXrOrigin(
    QQuick3DXrView *self,
    QQuick3DXrOrigin *newXrOrigin) {
  self->setXROrigin(newXrOrigin);
}

//  void QQuick3DXrView::updateViewportGeometry()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuick3DXrView22updateViewportGeometryEv(
    QQuick3DXrView *self) {
  self->updateViewportGeometry();
}

//  void QQuick3DXrView::handleSessionEnded()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuick3DXrView18handleSessionEndedEv(QQuick3DXrView *self) {
  self->handleSessionEnded();
}

//  void QQuick3DXrView::handleClearColorChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuick3DXrView23handleClearColorChangedEv(
    QQuick3DXrView *self) {
  self->handleClearColorChanged();
}

//  void QQuick3DXrView::handleAAChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuick3DXrView15handleAAChangedEv(QQuick3DXrView *self) {
  self->handleAAChanged();
}

//  bool QQuick3DXrView::init()
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QQuick3DXrView4initEv(QQuick3DXrView *self) {
  return self->init();
}

//  void QQuick3DXrView::initializeFailed(const QString &errorString)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuick3DXrView16initializeFailedERK7QString(
    QQuick3DXrView *self,
    const QString *errorString) {
  self->initializeFailed(*errorString);
}

//  void QQuick3DXrView::sessionEnded()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuick3DXrView12sessionEndedEv(QQuick3DXrView *self) {
  self->sessionEnded();
}

//  void QQuick3DXrView::xrOriginChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuick3DXrView15xrOriginChangedEv(QQuick3DXrView *self) {
  self->xrOriginChanged();
}

//  void QQuick3DXrView::environmentChanged(QQuick3DSceneEnvironment
//      *environment)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuick3DXrView18environmentChangedEP24QQuick3DSceneEnvironment(
    QQuick3DXrView *self,
    QQuick3DSceneEnvironment *environment) {
  self->environmentChanged(environment);
}

//  void QQuick3DXrView::passthroughEnabledChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuick3DXrView25passthroughEnabledChangedEv(
    QQuick3DXrView *self) {
  self->passthroughEnabledChanged();
}

//  void QQuick3DXrView::quitOnSessionEndChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuick3DXrView23quitOnSessionEndChangedEv(
    QQuick3DXrView *self) {
  self->quitOnSessionEndChanged();
}

//  void QQuick3DXrView::fixedFoveationChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuick3DXrView21fixedFoveationChangedEv(
    QQuick3DXrView *self) {
  self->fixedFoveationChanged();
}

//  void QQuick3DXrView::frameReady()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuick3DXrView10frameReadyEv(QQuick3DXrView *self) {
  self->frameReady();
}

//  void QQuick3DXrView::referenceSpaceChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuick3DXrView21referenceSpaceChangedEv(
    QQuick3DXrView *self) {
  self->referenceSpaceChanged();
}

//  void QQuick3DXrView::depthSubmissionEnabledChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuick3DXrView29depthSubmissionEnabledChangedEv(
    QQuick3DXrView *self) {
  self->depthSubmissionEnabledChanged();
}

//  void QQuick3DXrView::multiViewRenderingEnabledChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuick3DXrView32multiViewRenderingEnabledChangedEv(
    QQuick3DXrView *self) {
  self->multiViewRenderingEnabledChanged();
}

//  QQuick3DViewport *QQuick3DXrView::view3d() const
extern "C" Q_DECL_EXPORT
QQuick3DViewport *ritual_ZNK14QQuick3DXrView6view3dEv(
    const QQuick3DXrView *self) {
  return self->view3d();
}

//  bool QQuick3DXrView::handleVirtualTouch(TouchTarget target, const
//      QVector3D &pos, TouchState *touchState, QVector3D *offset)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QQuick3DXrView18handleVirtualTouchESt7variantIJSt9monostateP14QQuick3DXrItemP13QQuick3DModelEERK9QVector3DPNS_10TouchStateEPS7_(
    QQuick3DXrView *self,
    const QQuick3DXrView::TouchTarget *target,
    const QVector3D *pos,
    QQuick3DXrView::TouchState *touchState,
    QVector3D *offset) {
  return self->handleVirtualTouch(*target, *pos, touchState, offset);
}

//  a Python function taken by a CuteQQuick3DXrView, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuick3DXrView(
    QQuick3DXrView *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuick3DXrView *>(self)->take(key, call);
}
