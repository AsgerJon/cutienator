//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DExtras/qcuboidgeometry.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DExtras/qcuboidgeometry.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DExtras::QCuboidGeometry that Python can take functions over in. Every Qt3DExtras::QCuboidGeometry
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DExtras_QCuboidGeometryCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DExtras_QCuboidGeometryCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QCuboidGeometryCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QCuboidGeometryCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QCuboidGeometryCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QCuboidGeometryCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QCuboidGeometryCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DExtras_QCuboidGeometry : public Qt3DExtras::QCuboidGeometry {
public:
  using Qt3DExtras::QCuboidGeometry::QCuboidGeometry;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DExtras_QCuboidGeometryCall0 call = reinterpret_cast<CuteQt3DExtras_QCuboidGeometryCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DExtras_QCuboidGeometryCall1 call = reinterpret_cast<CuteQt3DExtras_QCuboidGeometryCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQt3DExtras_QCuboidGeometryCall2 call = reinterpret_cast<CuteQt3DExtras_QCuboidGeometryCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQt3DExtras_QCuboidGeometryCall3 call = reinterpret_cast<CuteQt3DExtras_QCuboidGeometryCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQt3DExtras_QCuboidGeometryCall4 call = reinterpret_cast<CuteQt3DExtras_QCuboidGeometryCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQt3DExtras_QCuboidGeometryCall5 call = reinterpret_cast<CuteQt3DExtras_QCuboidGeometryCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQt3DExtras_QCuboidGeometryCall6 call = reinterpret_cast<CuteQt3DExtras_QCuboidGeometryCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DExtras::QCuboidGeometry::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DExtras15QCuboidGeometry10metaObjectEv(
    const Qt3DExtras::QCuboidGeometry *self) {
  return self->metaObject();
}

//  void *Qt3DExtras::QCuboidGeometry::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DExtras15QCuboidGeometry11qt_metacastEPKc(
    Qt3DExtras::QCuboidGeometry *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DExtras::QCuboidGeometry::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DExtras15QCuboidGeometry11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DExtras::QCuboidGeometry *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DExtras::QCuboidGeometry::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DExtras15QCuboidGeometry2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DExtras::QCuboidGeometry::tr(s, c, n));
}

//  Qt3DExtras::QCuboidGeometry::QCuboidGeometry(QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DExtras::QCuboidGeometry *ritual_ZN10Qt3DExtras15QCuboidGeometryC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DExtras_QCuboidGeometry(parent);
}

//  Qt3DExtras::QCuboidGeometry::~QCuboidGeometry()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras15QCuboidGeometryD1Ev(
    Qt3DExtras::QCuboidGeometry *self) {
  delete self;
}

//  void Qt3DExtras::QCuboidGeometry::updateIndices()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras15QCuboidGeometry13updateIndicesEv(
    Qt3DExtras::QCuboidGeometry *self) {
  self->updateIndices();
}

//  void Qt3DExtras::QCuboidGeometry::updateVertices()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras15QCuboidGeometry14updateVerticesEv(
    Qt3DExtras::QCuboidGeometry *self) {
  self->updateVertices();
}

//  float Qt3DExtras::QCuboidGeometry::xExtent() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DExtras15QCuboidGeometry7xExtentEv(
    const Qt3DExtras::QCuboidGeometry *self) {
  return self->xExtent();
}

//  float Qt3DExtras::QCuboidGeometry::yExtent() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DExtras15QCuboidGeometry7yExtentEv(
    const Qt3DExtras::QCuboidGeometry *self) {
  return self->yExtent();
}

//  float Qt3DExtras::QCuboidGeometry::zExtent() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DExtras15QCuboidGeometry7zExtentEv(
    const Qt3DExtras::QCuboidGeometry *self) {
  return self->zExtent();
}

//  QSize Qt3DExtras::QCuboidGeometry::yzMeshResolution() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK10Qt3DExtras15QCuboidGeometry16yzMeshResolutionEv(
    const Qt3DExtras::QCuboidGeometry *self) {
  return new QSize(self->yzMeshResolution());
}

//  QSize Qt3DExtras::QCuboidGeometry::xyMeshResolution() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK10Qt3DExtras15QCuboidGeometry16xyMeshResolutionEv(
    const Qt3DExtras::QCuboidGeometry *self) {
  return new QSize(self->xyMeshResolution());
}

//  QSize Qt3DExtras::QCuboidGeometry::xzMeshResolution() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK10Qt3DExtras15QCuboidGeometry16xzMeshResolutionEv(
    const Qt3DExtras::QCuboidGeometry *self) {
  return new QSize(self->xzMeshResolution());
}

//  Qt3DCore::QAttribute *Qt3DExtras::QCuboidGeometry::positionAttribute()
//      const
extern "C" Q_DECL_EXPORT
Qt3DCore::QAttribute *ritual_ZNK10Qt3DExtras15QCuboidGeometry17positionAttributeEv(
    const Qt3DExtras::QCuboidGeometry *self) {
  return self->positionAttribute();
}

//  Qt3DCore::QAttribute *Qt3DExtras::QCuboidGeometry::normalAttribute()
//      const
extern "C" Q_DECL_EXPORT
Qt3DCore::QAttribute *ritual_ZNK10Qt3DExtras15QCuboidGeometry15normalAttributeEv(
    const Qt3DExtras::QCuboidGeometry *self) {
  return self->normalAttribute();
}

//  Qt3DCore::QAttribute *Qt3DExtras::QCuboidGeometry::texCoordAttribute()
//      const
extern "C" Q_DECL_EXPORT
Qt3DCore::QAttribute *ritual_ZNK10Qt3DExtras15QCuboidGeometry17texCoordAttributeEv(
    const Qt3DExtras::QCuboidGeometry *self) {
  return self->texCoordAttribute();
}

//  Qt3DCore::QAttribute *Qt3DExtras::QCuboidGeometry::tangentAttribute()
//      const
extern "C" Q_DECL_EXPORT
Qt3DCore::QAttribute *ritual_ZNK10Qt3DExtras15QCuboidGeometry16tangentAttributeEv(
    const Qt3DExtras::QCuboidGeometry *self) {
  return self->tangentAttribute();
}

//  Qt3DCore::QAttribute *Qt3DExtras::QCuboidGeometry::indexAttribute() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QAttribute *ritual_ZNK10Qt3DExtras15QCuboidGeometry14indexAttributeEv(
    const Qt3DExtras::QCuboidGeometry *self) {
  return self->indexAttribute();
}

//  void Qt3DExtras::QCuboidGeometry::setXExtent(float xExtent)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras15QCuboidGeometry10setXExtentEf(
    Qt3DExtras::QCuboidGeometry *self,
    float xExtent) {
  self->setXExtent(xExtent);
}

//  void Qt3DExtras::QCuboidGeometry::setYExtent(float yExtent)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras15QCuboidGeometry10setYExtentEf(
    Qt3DExtras::QCuboidGeometry *self,
    float yExtent) {
  self->setYExtent(yExtent);
}

//  void Qt3DExtras::QCuboidGeometry::setZExtent(float zExtent)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras15QCuboidGeometry10setZExtentEf(
    Qt3DExtras::QCuboidGeometry *self,
    float zExtent) {
  self->setZExtent(zExtent);
}

//  void Qt3DExtras::QCuboidGeometry::setYZMeshResolution(const QSize
//      &resolution)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras15QCuboidGeometry19setYZMeshResolutionERK5QSize(
    Qt3DExtras::QCuboidGeometry *self,
    const QSize *resolution) {
  self->setYZMeshResolution(*resolution);
}

//  void Qt3DExtras::QCuboidGeometry::setXZMeshResolution(const QSize
//      &resolution)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras15QCuboidGeometry19setXZMeshResolutionERK5QSize(
    Qt3DExtras::QCuboidGeometry *self,
    const QSize *resolution) {
  self->setXZMeshResolution(*resolution);
}

//  void Qt3DExtras::QCuboidGeometry::setXYMeshResolution(const QSize
//      &resolution)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras15QCuboidGeometry19setXYMeshResolutionERK5QSize(
    Qt3DExtras::QCuboidGeometry *self,
    const QSize *resolution) {
  self->setXYMeshResolution(*resolution);
}

//  void Qt3DExtras::QCuboidGeometry::xExtentChanged(float xExtent)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras15QCuboidGeometry14xExtentChangedEf(
    Qt3DExtras::QCuboidGeometry *self,
    float xExtent) {
  self->xExtentChanged(xExtent);
}

//  void Qt3DExtras::QCuboidGeometry::yExtentChanged(float yExtent)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras15QCuboidGeometry14yExtentChangedEf(
    Qt3DExtras::QCuboidGeometry *self,
    float yExtent) {
  self->yExtentChanged(yExtent);
}

//  void Qt3DExtras::QCuboidGeometry::zExtentChanged(float zExtent)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras15QCuboidGeometry14zExtentChangedEf(
    Qt3DExtras::QCuboidGeometry *self,
    float zExtent) {
  self->zExtentChanged(zExtent);
}

//  void Qt3DExtras::QCuboidGeometry::yzMeshResolutionChanged(const QSize
//      &yzMeshResolution)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras15QCuboidGeometry23yzMeshResolutionChangedERK5QSize(
    Qt3DExtras::QCuboidGeometry *self,
    const QSize *yzMeshResolution) {
  self->yzMeshResolutionChanged(*yzMeshResolution);
}

//  void Qt3DExtras::QCuboidGeometry::xzMeshResolutionChanged(const QSize
//      &xzMeshResolution)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras15QCuboidGeometry23xzMeshResolutionChangedERK5QSize(
    Qt3DExtras::QCuboidGeometry *self,
    const QSize *xzMeshResolution) {
  self->xzMeshResolutionChanged(*xzMeshResolution);
}

//  void Qt3DExtras::QCuboidGeometry::xyMeshResolutionChanged(const QSize
//      &xyMeshResolution)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras15QCuboidGeometry23xyMeshResolutionChangedERK5QSize(
    Qt3DExtras::QCuboidGeometry *self,
    const QSize *xyMeshResolution) {
  self->xyMeshResolutionChanged(*xyMeshResolution);
}

//  Qt3DExtras::QCuboidGeometry::QCuboidGeometry(QCuboidGeometryPrivate &dd,
//      QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DExtras::QCuboidGeometry *ritual_ZN10Qt3DExtras15QCuboidGeometryC1ERNS_22QCuboidGeometryPrivateEPN8Qt3DCore5QNodeE(
    Qt3DExtras::QCuboidGeometryPrivate *dd,
    Qt3DCore::QNode *parent) {
  return new CuteQt3DExtras_QCuboidGeometry(*dd, parent);
}

//  QCuboidGeometryPrivate *Qt3DExtras::QCuboidGeometry::d_func()
extern "C" Q_DECL_EXPORT
Qt3DExtras::QCuboidGeometryPrivate *ritual_ZN10Qt3DExtras15QCuboidGeometry6d_funcEv(
    Qt3DExtras::QCuboidGeometry *self) {
  return self->d_func();
}

//  const QCuboidGeometryPrivate *Qt3DExtras::QCuboidGeometry::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DExtras::QCuboidGeometryPrivate *ritual_ZNK10Qt3DExtras15QCuboidGeometry6d_funcEv(
    const Qt3DExtras::QCuboidGeometry *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DExtras_QCuboidGeometry, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DExtras_QCuboidGeometry(
    Qt3DExtras::QCuboidGeometry *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DExtras_QCuboidGeometry *>(self)->take(key, call);
}
