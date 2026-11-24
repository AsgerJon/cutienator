//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3DHelpers/6.12.0/QtQuick3DHelpers/private/planegeometry_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DHelpers/6.12.0/QtQuick3DHelpers/private/qtquick3dhelpersglobal_p.h>
#include <QtQuick3DHelpers/QtQuick3DHelpers>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DHelpers/6.12.0/QtQuick3DHelpers/private/planegeometry_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtQuick3D/qquick3dobject.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A PlaneGeometry that Python can take functions over in. Every PlaneGeometry
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CutePlaneGeometryCall0)(const void *, QSSGRenderGraphObject *, int *);
typedef void (*CutePlaneGeometryCall1)(const void *, int *);
typedef void (*CutePlaneGeometryCall2)(const void *, int, const QQuick3DObject::ItemChangeData *, int *);
typedef void (*CutePlaneGeometryCall3)(const void *, int *);
typedef void (*CutePlaneGeometryCall4)(const void *, int *);
typedef void (*CutePlaneGeometryCall5)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CutePlaneGeometryCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CutePlaneGeometryCall7)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CutePlaneGeometryCall8)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CutePlaneGeometryCall9)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CutePlaneGeometryCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CutePlaneGeometryCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CutePlaneGeometryCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CutePlaneGeometry : public PlaneGeometry {
public:
  using PlaneGeometry::PlaneGeometry;
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
      CutePlaneGeometryCall0 call = reinterpret_cast<CutePlaneGeometryCall0>(taken[0]);
      void * given = call(this, node, &handled);
      if (handled) return static_cast<QSSGRenderGraphObject *>(given);
    }
    return QQuick3DGeometry::updateSpatialNode(node);
  }

  //  void QQuick3DGeometry::markAllDirty()
  void markAllDirty() override {
    if (taken[1]) {
      int handled = 0;
      CutePlaneGeometryCall1 call = reinterpret_cast<CutePlaneGeometryCall1>(taken[1]);
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
      CutePlaneGeometryCall2 call = reinterpret_cast<CutePlaneGeometryCall2>(taken[2]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuick3DObject::itemChange(a0, a1);
  }

  //  void QQuick3DObject::classBegin()
  void classBegin() override {
    if (taken[3]) {
      int handled = 0;
      CutePlaneGeometryCall3 call = reinterpret_cast<CutePlaneGeometryCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::classBegin();
  }

  //  void QQuick3DObject::componentComplete()
  void componentComplete() override {
    if (taken[4]) {
      int handled = 0;
      CutePlaneGeometryCall4 call = reinterpret_cast<CutePlaneGeometryCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::componentComplete();
  }

  //  void QQuick3DObject::preSync()
  void preSync() override {
    if (taken[5]) {
      int handled = 0;
      CutePlaneGeometryCall5 call = reinterpret_cast<CutePlaneGeometryCall5>(taken[5]);
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
      CutePlaneGeometryCall6 call = reinterpret_cast<CutePlaneGeometryCall6>(taken[6]);
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
      CutePlaneGeometryCall7 call = reinterpret_cast<CutePlaneGeometryCall7>(taken[7]);
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
      CutePlaneGeometryCall8 call = reinterpret_cast<CutePlaneGeometryCall8>(taken[8]);
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
      CutePlaneGeometryCall9 call = reinterpret_cast<CutePlaneGeometryCall9>(taken[9]);
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
      CutePlaneGeometryCall10 call = reinterpret_cast<CutePlaneGeometryCall10>(taken[10]);
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
      CutePlaneGeometryCall11 call = reinterpret_cast<CutePlaneGeometryCall11>(taken[11]);
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
      CutePlaneGeometryCall12 call = reinterpret_cast<CutePlaneGeometryCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *PlaneGeometry::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13PlaneGeometry10metaObjectEv(
    const PlaneGeometry *self) {
  return self->metaObject();
}

//  QString PlaneGeometry::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13PlaneGeometry2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(PlaneGeometry::tr(s, c, n));
}

//  PlaneGeometry::PlaneGeometry(QQuick3DObject *parent)
extern "C" Q_DECL_EXPORT
PlaneGeometry *ritual_ZN13PlaneGeometryC1EP14QQuick3DObject(
    QQuick3DObject *parent) {
  return new CutePlaneGeometry(parent);
}

//  PlaneGeometry::~PlaneGeometry()
extern "C" Q_DECL_EXPORT
void ritual_ZN13PlaneGeometryD1Ev(PlaneGeometry *self) {
  delete self;
}

//  float PlaneGeometry::width() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK13PlaneGeometry5widthEv(const PlaneGeometry *self) {
  return self->width();
}

//  void PlaneGeometry::setWidth(float newWidth)
extern "C" Q_DECL_EXPORT
void ritual_ZN13PlaneGeometry8setWidthEf(
    PlaneGeometry *self,
    float newWidth) {
  self->setWidth(newWidth);
}

//  float PlaneGeometry::height() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK13PlaneGeometry6heightEv(const PlaneGeometry *self) {
  return self->height();
}

//  void PlaneGeometry::setHeight(float newHeight)
extern "C" Q_DECL_EXPORT
void ritual_ZN13PlaneGeometry9setHeightEf(
    PlaneGeometry *self,
    float newHeight) {
  self->setHeight(newHeight);
}

//  QSize PlaneGeometry::meshResolution() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK13PlaneGeometry14meshResolutionEv(
    const PlaneGeometry *self) {
  return new QSize(self->meshResolution());
}

//  void PlaneGeometry::setMeshResolution(const QSize &newMeshResolution)
extern "C" Q_DECL_EXPORT
void ritual_ZN13PlaneGeometry17setMeshResolutionERK5QSize(
    PlaneGeometry *self,
    const QSize *newMeshResolution) {
  self->setMeshResolution(*newMeshResolution);
}

//  Plane PlaneGeometry::plane() const
extern "C" Q_DECL_EXPORT
PlaneGeometry::Plane ritual_ZNK13PlaneGeometry5planeEv(
    const PlaneGeometry *self) {
  return self->plane();
}

//  void PlaneGeometry::setPlane(Plane newPlane)
extern "C" Q_DECL_EXPORT
void ritual_ZN13PlaneGeometry8setPlaneENS_5PlaneE(
    PlaneGeometry *self,
    PlaneGeometry::Plane newPlane) {
  self->setPlane(newPlane);
}

//  bool PlaneGeometry::mirrored() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13PlaneGeometry8mirroredEv(const PlaneGeometry *self) {
  return self->mirrored();
}

//  void PlaneGeometry::setMirrored(bool newMirrored)
extern "C" Q_DECL_EXPORT
void ritual_ZN13PlaneGeometry11setMirroredEb(
    PlaneGeometry *self,
    bool newMirrored) {
  self->setMirrored(newMirrored);
}

//  bool PlaneGeometry::asynchronous() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13PlaneGeometry12asynchronousEv(const PlaneGeometry *self) {
  return self->asynchronous();
}

//  void PlaneGeometry::setAsynchronous(bool newAsynchronous)
extern "C" Q_DECL_EXPORT
void ritual_ZN13PlaneGeometry15setAsynchronousEb(
    PlaneGeometry *self,
    bool newAsynchronous) {
  self->setAsynchronous(newAsynchronous);
}

//  Status PlaneGeometry::status() const
extern "C" Q_DECL_EXPORT
PlaneGeometry::Status ritual_ZNK13PlaneGeometry6statusEv(
    const PlaneGeometry *self) {
  return self->status();
}

//  bool PlaneGeometry::reversed() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13PlaneGeometry8reversedEv(const PlaneGeometry *self) {
  return self->reversed();
}

//  void PlaneGeometry::setReversed(bool newReversed)
extern "C" Q_DECL_EXPORT
void ritual_ZN13PlaneGeometry11setReversedEb(
    PlaneGeometry *self,
    bool newReversed) {
  self->setReversed(newReversed);
}

//  void PlaneGeometry::doUpdateGeometry()
extern "C" Q_DECL_EXPORT
void ritual_ZN13PlaneGeometry16doUpdateGeometryEv(PlaneGeometry *self) {
  self->doUpdateGeometry();
}

//  void PlaneGeometry::requestFinished()
extern "C" Q_DECL_EXPORT
void ritual_ZN13PlaneGeometry15requestFinishedEv(PlaneGeometry *self) {
  self->requestFinished();
}

//  void PlaneGeometry::scheduleGeometryUpdate()
extern "C" Q_DECL_EXPORT
void ritual_ZN13PlaneGeometry22scheduleGeometryUpdateEv(
    PlaneGeometry *self) {
  self->scheduleGeometryUpdate();
}

//  a Python function taken by a CutePlaneGeometry, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_PlaneGeometry(
    PlaneGeometry *self,
    const char *key,
    void *call) {
  return static_cast<CutePlaneGeometry *>(self)->take(key, call);
}
