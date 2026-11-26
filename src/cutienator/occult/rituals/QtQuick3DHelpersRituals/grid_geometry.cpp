//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3DHelpers/6.12.0/QtQuick3DHelpers/private/gridgeometry_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DHelpers/6.12.0/QtQuick3DHelpers/private/qtquick3dhelpersglobal_p.h>
#include <QtQuick3DHelpers/QtQuick3DHelpers>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DHelpers/6.12.0/QtQuick3DHelpers/private/gridgeometry_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtQuick3D/qquick3dobject.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A GridGeometry that Python can take functions over in. Every GridGeometry
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteGridGeometryCall0)(const void *, QSSGRenderGraphObject *, int *);
typedef void (*CuteGridGeometryCall1)(const void *, int *);
typedef void (*CuteGridGeometryCall2)(const void *, int, const QQuick3DObject::ItemChangeData *, int *);
typedef void (*CuteGridGeometryCall3)(const void *, int *);
typedef void (*CuteGridGeometryCall4)(const void *, int *);
typedef void (*CuteGridGeometryCall5)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteGridGeometryCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteGridGeometryCall7)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteGridGeometryCall8)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteGridGeometryCall9)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteGridGeometryCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteGridGeometryCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteGridGeometryCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteGridGeometry : public GridGeometry {
public:
  using GridGeometry::GridGeometry;
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
      CuteGridGeometryCall0 call = reinterpret_cast<CuteGridGeometryCall0>(taken[0]);
      void * given = call(this, node, &handled);
      if (handled) return static_cast<QSSGRenderGraphObject *>(given);
    }
    return QQuick3DGeometry::updateSpatialNode(node);
  }

  //  void QQuick3DGeometry::markAllDirty()
  void markAllDirty() override {
    if (taken[1]) {
      int handled = 0;
      CuteGridGeometryCall1 call = reinterpret_cast<CuteGridGeometryCall1>(taken[1]);
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
      CuteGridGeometryCall2 call = reinterpret_cast<CuteGridGeometryCall2>(taken[2]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuick3DObject::itemChange(a0, a1);
  }

  //  void QQuick3DObject::classBegin()
  void classBegin() override {
    if (taken[3]) {
      int handled = 0;
      CuteGridGeometryCall3 call = reinterpret_cast<CuteGridGeometryCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::classBegin();
  }

  //  void QQuick3DObject::componentComplete()
  void componentComplete() override {
    if (taken[4]) {
      int handled = 0;
      CuteGridGeometryCall4 call = reinterpret_cast<CuteGridGeometryCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::componentComplete();
  }

  //  void QQuick3DObject::preSync()
  void preSync() override {
    if (taken[5]) {
      int handled = 0;
      CuteGridGeometryCall5 call = reinterpret_cast<CuteGridGeometryCall5>(taken[5]);
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
      CuteGridGeometryCall6 call = reinterpret_cast<CuteGridGeometryCall6>(taken[6]);
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
      CuteGridGeometryCall7 call = reinterpret_cast<CuteGridGeometryCall7>(taken[7]);
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
      CuteGridGeometryCall8 call = reinterpret_cast<CuteGridGeometryCall8>(taken[8]);
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
      CuteGridGeometryCall9 call = reinterpret_cast<CuteGridGeometryCall9>(taken[9]);
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
      CuteGridGeometryCall10 call = reinterpret_cast<CuteGridGeometryCall10>(taken[10]);
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
      CuteGridGeometryCall11 call = reinterpret_cast<CuteGridGeometryCall11>(taken[11]);
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
      CuteGridGeometryCall12 call = reinterpret_cast<CuteGridGeometryCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *GridGeometry::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK12GridGeometry10metaObjectEv(
    const GridGeometry *self) {
  return self->metaObject();
}

//  void *GridGeometry::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN12GridGeometry11qt_metacastEPKc(
    GridGeometry *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int GridGeometry::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN12GridGeometry11qt_metacallEN11QMetaObject4CallEiPPv(
    GridGeometry *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString GridGeometry::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12GridGeometry2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(GridGeometry::tr(s, c, n));
}

//  GridGeometry::GridGeometry()
extern "C" Q_DECL_EXPORT
GridGeometry *ritual_ZN12GridGeometryC1Ev() {
  return new CuteGridGeometry();
}

//  GridGeometry::~GridGeometry()
extern "C" Q_DECL_EXPORT
void ritual_ZN12GridGeometryD1Ev(GridGeometry *self) {
  delete self;
}

//  int GridGeometry::horizontalLines() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12GridGeometry15horizontalLinesEv(const GridGeometry *self) {
  return self->horizontalLines();
}

//  int GridGeometry::verticalLines() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12GridGeometry13verticalLinesEv(const GridGeometry *self) {
  return self->verticalLines();
}

//  float GridGeometry::horizontalStep() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK12GridGeometry14horizontalStepEv(const GridGeometry *self) {
  return self->horizontalStep();
}

//  float GridGeometry::verticalStep() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK12GridGeometry12verticalStepEv(const GridGeometry *self) {
  return self->verticalStep();
}

//  void GridGeometry::setHorizontalLines(int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN12GridGeometry18setHorizontalLinesEi(
    GridGeometry *self,
    int count) {
  self->setHorizontalLines(count);
}

//  void GridGeometry::setVerticalLines(int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN12GridGeometry16setVerticalLinesEi(
    GridGeometry *self,
    int count) {
  self->setVerticalLines(count);
}

//  void GridGeometry::setHorizontalStep(float step)
extern "C" Q_DECL_EXPORT
void ritual_ZN12GridGeometry17setHorizontalStepEf(
    GridGeometry *self,
    float step) {
  self->setHorizontalStep(step);
}

//  void GridGeometry::setVerticalStep(float step)
extern "C" Q_DECL_EXPORT
void ritual_ZN12GridGeometry15setVerticalStepEf(
    GridGeometry *self,
    float step) {
  self->setVerticalStep(step);
}

//  void GridGeometry::horizontalLinesChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN12GridGeometry22horizontalLinesChangedEv(GridGeometry *self) {
  self->horizontalLinesChanged();
}

//  void GridGeometry::verticalLinesChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN12GridGeometry20verticalLinesChangedEv(GridGeometry *self) {
  self->verticalLinesChanged();
}

//  void GridGeometry::horizontalStepChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN12GridGeometry21horizontalStepChangedEv(GridGeometry *self) {
  self->horizontalStepChanged();
}

//  void GridGeometry::verticalStepChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN12GridGeometry19verticalStepChangedEv(GridGeometry *self) {
  self->verticalStepChanged();
}

//  void GridGeometry::updateData()
extern "C" Q_DECL_EXPORT
void ritual_ZN12GridGeometry10updateDataEv(GridGeometry *self) {
  self->updateData();
}

//  a Python function taken by a CuteGridGeometry, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_GridGeometry(
    GridGeometry *self,
    const char *key,
    void *call) {
  return static_cast<CuteGridGeometry *>(self)->take(key, call);
}
