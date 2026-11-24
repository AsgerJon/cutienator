//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3DHelpers/6.12.0/QtQuick3DHelpers/private/cuboidgeometry_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DHelpers/6.12.0/QtQuick3DHelpers/private/qtquick3dhelpersglobal_p.h>
#include <QtQuick3DHelpers/QtQuick3DHelpers>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DHelpers/6.12.0/QtQuick3DHelpers/private/cuboidgeometry_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtQuick3D/qquick3dobject.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A CuboidGeometry that Python can take functions over in. Every CuboidGeometry
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteCuboidGeometryCall0)(const void *, QSSGRenderGraphObject *, int *);
typedef void (*CuteCuboidGeometryCall1)(const void *, int *);
typedef void (*CuteCuboidGeometryCall2)(const void *, int, const QQuick3DObject::ItemChangeData *, int *);
typedef void (*CuteCuboidGeometryCall3)(const void *, int *);
typedef void (*CuteCuboidGeometryCall4)(const void *, int *);
typedef void (*CuteCuboidGeometryCall5)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteCuboidGeometryCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteCuboidGeometryCall7)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteCuboidGeometryCall8)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteCuboidGeometryCall9)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteCuboidGeometryCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteCuboidGeometryCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteCuboidGeometryCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteCuboidGeometry : public CuboidGeometry {
public:
  using CuboidGeometry::CuboidGeometry;
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
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject7preSyncEv")) {
      taken[5] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QSSGRenderGraphObject
  //      *QQuick3DGeometry::updateSpatialNode(QSSGRenderGraphObject *node)
  QSSGRenderGraphObject *updateSpatialNode(
      QSSGRenderGraphObject *node) override {
    if (taken[0]) {
      int handled = 0;
      CuteCuboidGeometryCall0 call = reinterpret_cast<CuteCuboidGeometryCall0>(taken[0]);
      void * given = call(this, node, &handled);
      if (handled) return static_cast<QSSGRenderGraphObject *>(given);
    }
    return QQuick3DGeometry::updateSpatialNode(node);
  }

  //  void QQuick3DGeometry::markAllDirty()
  void markAllDirty() override {
    if (taken[1]) {
      int handled = 0;
      CuteCuboidGeometryCall1 call = reinterpret_cast<CuteCuboidGeometryCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DGeometry::markAllDirty();
  }

  //  void QQuick3DObject::itemChange(ItemChange a0, const ItemChangeData
  //      &a1)
  void itemChange(
      QQuick3DObject::ItemChange a0,
      const QQuick3DObject::ItemChangeData &a1) override {
    if (taken[2]) {
      int handled = 0;
      CuteCuboidGeometryCall2 call = reinterpret_cast<CuteCuboidGeometryCall2>(taken[2]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuick3DObject::itemChange(a0, a1);
  }

  //  void QQuick3DObject::classBegin()
  void classBegin() override {
    if (taken[3]) {
      int handled = 0;
      CuteCuboidGeometryCall3 call = reinterpret_cast<CuteCuboidGeometryCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::classBegin();
  }

  //  void QQuick3DObject::componentComplete()
  void componentComplete() override {
    if (taken[4]) {
      int handled = 0;
      CuteCuboidGeometryCall4 call = reinterpret_cast<CuteCuboidGeometryCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::componentComplete();
  }

  //  void QQuick3DObject::preSync()
  void preSync() override {
    if (taken[5]) {
      int handled = 0;
      CuteCuboidGeometryCall5 call = reinterpret_cast<CuteCuboidGeometryCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::preSync();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteCuboidGeometryCall6 call = reinterpret_cast<CuteCuboidGeometryCall6>(taken[6]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteCuboidGeometryCall7 call = reinterpret_cast<CuteCuboidGeometryCall7>(taken[7]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteCuboidGeometryCall8 call = reinterpret_cast<CuteCuboidGeometryCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteCuboidGeometryCall9 call = reinterpret_cast<CuteCuboidGeometryCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteCuboidGeometryCall10 call = reinterpret_cast<CuteCuboidGeometryCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[11]) {
      int handled = 0;
      CuteCuboidGeometryCall11 call = reinterpret_cast<CuteCuboidGeometryCall11>(taken[11]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[12]) {
      int handled = 0;
      CuteCuboidGeometryCall12 call = reinterpret_cast<CuteCuboidGeometryCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *CuboidGeometry::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14CuboidGeometry10metaObjectEv(
    const CuboidGeometry *self) {
  return self->metaObject();
}

//  QString CuboidGeometry::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14CuboidGeometry2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(CuboidGeometry::tr(s, c, n));
}

//  CuboidGeometry::CuboidGeometry(QQuick3DObject *parent)
extern "C" Q_DECL_EXPORT
CuboidGeometry *ritual_ZN14CuboidGeometryC1EP14QQuick3DObject(
    QQuick3DObject *parent) {
  return new CuteCuboidGeometry(parent);
}

//  CuboidGeometry::~CuboidGeometry()
extern "C" Q_DECL_EXPORT
void ritual_ZN14CuboidGeometryD1Ev(CuboidGeometry *self) {
  delete self;
}

//  float CuboidGeometry::xExtent() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK14CuboidGeometry7xExtentEv(const CuboidGeometry *self) {
  return self->xExtent();
}

//  void CuboidGeometry::setXExtent(float newXExtent)
extern "C" Q_DECL_EXPORT
void ritual_ZN14CuboidGeometry10setXExtentEf(
    CuboidGeometry *self,
    float newXExtent) {
  self->setXExtent(newXExtent);
}

//  float CuboidGeometry::yExtent() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK14CuboidGeometry7yExtentEv(const CuboidGeometry *self) {
  return self->yExtent();
}

//  void CuboidGeometry::setYExtent(float newYExtent)
extern "C" Q_DECL_EXPORT
void ritual_ZN14CuboidGeometry10setYExtentEf(
    CuboidGeometry *self,
    float newYExtent) {
  self->setYExtent(newYExtent);
}

//  float CuboidGeometry::zExtent() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK14CuboidGeometry7zExtentEv(const CuboidGeometry *self) {
  return self->zExtent();
}

//  void CuboidGeometry::setZExtent(float newZExtent)
extern "C" Q_DECL_EXPORT
void ritual_ZN14CuboidGeometry10setZExtentEf(
    CuboidGeometry *self,
    float newZExtent) {
  self->setZExtent(newZExtent);
}

//  QSize CuboidGeometry::yzMeshResolution() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK14CuboidGeometry16yzMeshResolutionEv(
    const CuboidGeometry *self) {
  return new QSize(self->yzMeshResolution());
}

//  void CuboidGeometry::setYzMeshResolution(const QSize
//      &newYzMeshResolution)
extern "C" Q_DECL_EXPORT
void ritual_ZN14CuboidGeometry19setYzMeshResolutionERK5QSize(
    CuboidGeometry *self,
    const QSize *newYzMeshResolution) {
  self->setYzMeshResolution(*newYzMeshResolution);
}

//  QSize CuboidGeometry::xzMeshResolution() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK14CuboidGeometry16xzMeshResolutionEv(
    const CuboidGeometry *self) {
  return new QSize(self->xzMeshResolution());
}

//  void CuboidGeometry::setXzMeshResolution(const QSize
//      &newXzMeshResolution)
extern "C" Q_DECL_EXPORT
void ritual_ZN14CuboidGeometry19setXzMeshResolutionERK5QSize(
    CuboidGeometry *self,
    const QSize *newXzMeshResolution) {
  self->setXzMeshResolution(*newXzMeshResolution);
}

//  QSize CuboidGeometry::xyMeshResolution() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK14CuboidGeometry16xyMeshResolutionEv(
    const CuboidGeometry *self) {
  return new QSize(self->xyMeshResolution());
}

//  void CuboidGeometry::setXyMeshResolution(const QSize
//      &newXyMeshResolution)
extern "C" Q_DECL_EXPORT
void ritual_ZN14CuboidGeometry19setXyMeshResolutionERK5QSize(
    CuboidGeometry *self,
    const QSize *newXyMeshResolution) {
  self->setXyMeshResolution(*newXyMeshResolution);
}

//  bool CuboidGeometry::asynchronous() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14CuboidGeometry12asynchronousEv(const CuboidGeometry *self) {
  return self->asynchronous();
}

//  void CuboidGeometry::setAsynchronous(bool newAsynchronous)
extern "C" Q_DECL_EXPORT
void ritual_ZN14CuboidGeometry15setAsynchronousEb(
    CuboidGeometry *self,
    bool newAsynchronous) {
  self->setAsynchronous(newAsynchronous);
}

//  Status CuboidGeometry::status() const
extern "C" Q_DECL_EXPORT
CuboidGeometry::Status ritual_ZNK14CuboidGeometry6statusEv(
    const CuboidGeometry *self) {
  return self->status();
}

//  void CuboidGeometry::doUpdateGeometry()
extern "C" Q_DECL_EXPORT
void ritual_ZN14CuboidGeometry16doUpdateGeometryEv(CuboidGeometry *self) {
  self->doUpdateGeometry();
}

//  void CuboidGeometry::requestFinished()
extern "C" Q_DECL_EXPORT
void ritual_ZN14CuboidGeometry15requestFinishedEv(CuboidGeometry *self) {
  self->requestFinished();
}

//  void CuboidGeometry::scheduleGeometryUpdate()
extern "C" Q_DECL_EXPORT
void ritual_ZN14CuboidGeometry22scheduleGeometryUpdateEv(
    CuboidGeometry *self) {
  self->scheduleGeometryUpdate();
}

//  a Python function taken by a CuteCuboidGeometry, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_CuboidGeometry(
    CuboidGeometry *self,
    const char *key,
    void *call) {
  return static_cast<CuteCuboidGeometry *>(self)->take(key, call);
}
