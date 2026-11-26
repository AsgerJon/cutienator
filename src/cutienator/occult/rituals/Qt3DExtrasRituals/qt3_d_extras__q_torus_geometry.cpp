//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DExtras/qtorusgeometry.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DExtras/qtorusgeometry.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DExtras::QTorusGeometry that Python can take functions over in. Every Qt3DExtras::QTorusGeometry
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DExtras_QTorusGeometryCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DExtras_QTorusGeometryCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QTorusGeometryCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QTorusGeometryCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QTorusGeometryCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QTorusGeometryCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QTorusGeometryCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DExtras_QTorusGeometry : public Qt3DExtras::QTorusGeometry {
public:
  using Qt3DExtras::QTorusGeometry::QTorusGeometry;
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
      CuteQt3DExtras_QTorusGeometryCall0 call = reinterpret_cast<CuteQt3DExtras_QTorusGeometryCall0>(taken[0]);
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
      CuteQt3DExtras_QTorusGeometryCall1 call = reinterpret_cast<CuteQt3DExtras_QTorusGeometryCall1>(taken[1]);
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
      CuteQt3DExtras_QTorusGeometryCall2 call = reinterpret_cast<CuteQt3DExtras_QTorusGeometryCall2>(taken[2]);
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
      CuteQt3DExtras_QTorusGeometryCall3 call = reinterpret_cast<CuteQt3DExtras_QTorusGeometryCall3>(taken[3]);
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
      CuteQt3DExtras_QTorusGeometryCall4 call = reinterpret_cast<CuteQt3DExtras_QTorusGeometryCall4>(taken[4]);
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
      CuteQt3DExtras_QTorusGeometryCall5 call = reinterpret_cast<CuteQt3DExtras_QTorusGeometryCall5>(taken[5]);
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
      CuteQt3DExtras_QTorusGeometryCall6 call = reinterpret_cast<CuteQt3DExtras_QTorusGeometryCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DExtras::QTorusGeometry::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DExtras14QTorusGeometry10metaObjectEv(
    const Qt3DExtras::QTorusGeometry *self) {
  return self->metaObject();
}

//  void *Qt3DExtras::QTorusGeometry::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DExtras14QTorusGeometry11qt_metacastEPKc(
    Qt3DExtras::QTorusGeometry *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DExtras::QTorusGeometry::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DExtras14QTorusGeometry11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DExtras::QTorusGeometry *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DExtras::QTorusGeometry::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DExtras14QTorusGeometry2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DExtras::QTorusGeometry::tr(s, c, n));
}

//  Qt3DExtras::QTorusGeometry::QTorusGeometry(QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DExtras::QTorusGeometry *ritual_ZN10Qt3DExtras14QTorusGeometryC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DExtras_QTorusGeometry(parent);
}

//  Qt3DExtras::QTorusGeometry::~QTorusGeometry()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras14QTorusGeometryD1Ev(
    Qt3DExtras::QTorusGeometry *self) {
  delete self;
}

//  void Qt3DExtras::QTorusGeometry::updateVertices()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras14QTorusGeometry14updateVerticesEv(
    Qt3DExtras::QTorusGeometry *self) {
  self->updateVertices();
}

//  void Qt3DExtras::QTorusGeometry::updateIndices()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras14QTorusGeometry13updateIndicesEv(
    Qt3DExtras::QTorusGeometry *self) {
  self->updateIndices();
}

//  int Qt3DExtras::QTorusGeometry::rings() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DExtras14QTorusGeometry5ringsEv(
    const Qt3DExtras::QTorusGeometry *self) {
  return self->rings();
}

//  int Qt3DExtras::QTorusGeometry::slices() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DExtras14QTorusGeometry6slicesEv(
    const Qt3DExtras::QTorusGeometry *self) {
  return self->slices();
}

//  float Qt3DExtras::QTorusGeometry::radius() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DExtras14QTorusGeometry6radiusEv(
    const Qt3DExtras::QTorusGeometry *self) {
  return self->radius();
}

//  float Qt3DExtras::QTorusGeometry::minorRadius() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DExtras14QTorusGeometry11minorRadiusEv(
    const Qt3DExtras::QTorusGeometry *self) {
  return self->minorRadius();
}

//  Qt3DCore::QAttribute *Qt3DExtras::QTorusGeometry::positionAttribute()
//      const
extern "C" Q_DECL_EXPORT
Qt3DCore::QAttribute *ritual_ZNK10Qt3DExtras14QTorusGeometry17positionAttributeEv(
    const Qt3DExtras::QTorusGeometry *self) {
  return self->positionAttribute();
}

//  Qt3DCore::QAttribute *Qt3DExtras::QTorusGeometry::normalAttribute() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QAttribute *ritual_ZNK10Qt3DExtras14QTorusGeometry15normalAttributeEv(
    const Qt3DExtras::QTorusGeometry *self) {
  return self->normalAttribute();
}

//  Qt3DCore::QAttribute *Qt3DExtras::QTorusGeometry::texCoordAttribute()
//      const
extern "C" Q_DECL_EXPORT
Qt3DCore::QAttribute *ritual_ZNK10Qt3DExtras14QTorusGeometry17texCoordAttributeEv(
    const Qt3DExtras::QTorusGeometry *self) {
  return self->texCoordAttribute();
}

//  Qt3DCore::QAttribute *Qt3DExtras::QTorusGeometry::indexAttribute() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QAttribute *ritual_ZNK10Qt3DExtras14QTorusGeometry14indexAttributeEv(
    const Qt3DExtras::QTorusGeometry *self) {
  return self->indexAttribute();
}

//  void Qt3DExtras::QTorusGeometry::setRings(int rings)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras14QTorusGeometry8setRingsEi(
    Qt3DExtras::QTorusGeometry *self,
    int rings) {
  self->setRings(rings);
}

//  void Qt3DExtras::QTorusGeometry::setSlices(int slices)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras14QTorusGeometry9setSlicesEi(
    Qt3DExtras::QTorusGeometry *self,
    int slices) {
  self->setSlices(slices);
}

//  void Qt3DExtras::QTorusGeometry::setRadius(float radius)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras14QTorusGeometry9setRadiusEf(
    Qt3DExtras::QTorusGeometry *self,
    float radius) {
  self->setRadius(radius);
}

//  void Qt3DExtras::QTorusGeometry::setMinorRadius(float minorRadius)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras14QTorusGeometry14setMinorRadiusEf(
    Qt3DExtras::QTorusGeometry *self,
    float minorRadius) {
  self->setMinorRadius(minorRadius);
}

//  void Qt3DExtras::QTorusGeometry::radiusChanged(float radius)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras14QTorusGeometry13radiusChangedEf(
    Qt3DExtras::QTorusGeometry *self,
    float radius) {
  self->radiusChanged(radius);
}

//  void Qt3DExtras::QTorusGeometry::ringsChanged(int rings)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras14QTorusGeometry12ringsChangedEi(
    Qt3DExtras::QTorusGeometry *self,
    int rings) {
  self->ringsChanged(rings);
}

//  void Qt3DExtras::QTorusGeometry::slicesChanged(int slices)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras14QTorusGeometry13slicesChangedEi(
    Qt3DExtras::QTorusGeometry *self,
    int slices) {
  self->slicesChanged(slices);
}

//  void Qt3DExtras::QTorusGeometry::minorRadiusChanged(float minorRadius)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras14QTorusGeometry18minorRadiusChangedEf(
    Qt3DExtras::QTorusGeometry *self,
    float minorRadius) {
  self->minorRadiusChanged(minorRadius);
}

//  Qt3DExtras::QTorusGeometry::QTorusGeometry(QTorusGeometryPrivate &dd,
//      QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DExtras::QTorusGeometry *ritual_ZN10Qt3DExtras14QTorusGeometryC1ERNS_21QTorusGeometryPrivateEPN8Qt3DCore5QNodeE(
    Qt3DExtras::QTorusGeometryPrivate *dd,
    Qt3DCore::QNode *parent) {
  return new CuteQt3DExtras_QTorusGeometry(*dd, parent);
}

//  QTorusGeometryPrivate *Qt3DExtras::QTorusGeometry::d_func()
extern "C" Q_DECL_EXPORT
Qt3DExtras::QTorusGeometryPrivate *ritual_ZN10Qt3DExtras14QTorusGeometry6d_funcEv(
    Qt3DExtras::QTorusGeometry *self) {
  return self->d_func();
}

//  const QTorusGeometryPrivate *Qt3DExtras::QTorusGeometry::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DExtras::QTorusGeometryPrivate *ritual_ZNK10Qt3DExtras14QTorusGeometry6d_funcEv(
    const Qt3DExtras::QTorusGeometry *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DExtras_QTorusGeometry, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DExtras_QTorusGeometry(
    Qt3DExtras::QTorusGeometry *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DExtras_QTorusGeometry *>(self)->take(key, call);
}
