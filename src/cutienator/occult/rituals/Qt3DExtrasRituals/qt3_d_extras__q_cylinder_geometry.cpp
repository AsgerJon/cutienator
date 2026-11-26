//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DExtras/qcylindergeometry.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DExtras/qcylindergeometry.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DExtras::QCylinderGeometry that Python can take functions over in. Every Qt3DExtras::QCylinderGeometry
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DExtras_QCylinderGeometryCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DExtras_QCylinderGeometryCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QCylinderGeometryCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QCylinderGeometryCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QCylinderGeometryCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QCylinderGeometryCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QCylinderGeometryCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DExtras_QCylinderGeometry : public Qt3DExtras::QCylinderGeometry {
public:
  using Qt3DExtras::QCylinderGeometry::QCylinderGeometry;
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
      CuteQt3DExtras_QCylinderGeometryCall0 call = reinterpret_cast<CuteQt3DExtras_QCylinderGeometryCall0>(taken[0]);
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
      CuteQt3DExtras_QCylinderGeometryCall1 call = reinterpret_cast<CuteQt3DExtras_QCylinderGeometryCall1>(taken[1]);
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
      CuteQt3DExtras_QCylinderGeometryCall2 call = reinterpret_cast<CuteQt3DExtras_QCylinderGeometryCall2>(taken[2]);
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
      CuteQt3DExtras_QCylinderGeometryCall3 call = reinterpret_cast<CuteQt3DExtras_QCylinderGeometryCall3>(taken[3]);
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
      CuteQt3DExtras_QCylinderGeometryCall4 call = reinterpret_cast<CuteQt3DExtras_QCylinderGeometryCall4>(taken[4]);
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
      CuteQt3DExtras_QCylinderGeometryCall5 call = reinterpret_cast<CuteQt3DExtras_QCylinderGeometryCall5>(taken[5]);
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
      CuteQt3DExtras_QCylinderGeometryCall6 call = reinterpret_cast<CuteQt3DExtras_QCylinderGeometryCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DExtras::QCylinderGeometry::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DExtras17QCylinderGeometry10metaObjectEv(
    const Qt3DExtras::QCylinderGeometry *self) {
  return self->metaObject();
}

//  void *Qt3DExtras::QCylinderGeometry::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DExtras17QCylinderGeometry11qt_metacastEPKc(
    Qt3DExtras::QCylinderGeometry *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DExtras::QCylinderGeometry::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DExtras17QCylinderGeometry11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DExtras::QCylinderGeometry *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DExtras::QCylinderGeometry::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DExtras17QCylinderGeometry2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DExtras::QCylinderGeometry::tr(s, c, n));
}

//  Qt3DExtras::QCylinderGeometry::QCylinderGeometry(QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DExtras::QCylinderGeometry *ritual_ZN10Qt3DExtras17QCylinderGeometryC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DExtras_QCylinderGeometry(parent);
}

//  Qt3DExtras::QCylinderGeometry::~QCylinderGeometry()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras17QCylinderGeometryD1Ev(
    Qt3DExtras::QCylinderGeometry *self) {
  delete self;
}

//  void Qt3DExtras::QCylinderGeometry::updateVertices()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras17QCylinderGeometry14updateVerticesEv(
    Qt3DExtras::QCylinderGeometry *self) {
  self->updateVertices();
}

//  void Qt3DExtras::QCylinderGeometry::updateIndices()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras17QCylinderGeometry13updateIndicesEv(
    Qt3DExtras::QCylinderGeometry *self) {
  self->updateIndices();
}

//  int Qt3DExtras::QCylinderGeometry::rings() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DExtras17QCylinderGeometry5ringsEv(
    const Qt3DExtras::QCylinderGeometry *self) {
  return self->rings();
}

//  int Qt3DExtras::QCylinderGeometry::slices() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DExtras17QCylinderGeometry6slicesEv(
    const Qt3DExtras::QCylinderGeometry *self) {
  return self->slices();
}

//  float Qt3DExtras::QCylinderGeometry::radius() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DExtras17QCylinderGeometry6radiusEv(
    const Qt3DExtras::QCylinderGeometry *self) {
  return self->radius();
}

//  float Qt3DExtras::QCylinderGeometry::length() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DExtras17QCylinderGeometry6lengthEv(
    const Qt3DExtras::QCylinderGeometry *self) {
  return self->length();
}

//  Qt3DCore::QAttribute *Qt3DExtras::QCylinderGeometry::positionAttribute()
//      const
extern "C" Q_DECL_EXPORT
Qt3DCore::QAttribute *ritual_ZNK10Qt3DExtras17QCylinderGeometry17positionAttributeEv(
    const Qt3DExtras::QCylinderGeometry *self) {
  return self->positionAttribute();
}

//  Qt3DCore::QAttribute *Qt3DExtras::QCylinderGeometry::normalAttribute()
//      const
extern "C" Q_DECL_EXPORT
Qt3DCore::QAttribute *ritual_ZNK10Qt3DExtras17QCylinderGeometry15normalAttributeEv(
    const Qt3DExtras::QCylinderGeometry *self) {
  return self->normalAttribute();
}

//  Qt3DCore::QAttribute *Qt3DExtras::QCylinderGeometry::texCoordAttribute()
//      const
extern "C" Q_DECL_EXPORT
Qt3DCore::QAttribute *ritual_ZNK10Qt3DExtras17QCylinderGeometry17texCoordAttributeEv(
    const Qt3DExtras::QCylinderGeometry *self) {
  return self->texCoordAttribute();
}

//  Qt3DCore::QAttribute *Qt3DExtras::QCylinderGeometry::indexAttribute()
//      const
extern "C" Q_DECL_EXPORT
Qt3DCore::QAttribute *ritual_ZNK10Qt3DExtras17QCylinderGeometry14indexAttributeEv(
    const Qt3DExtras::QCylinderGeometry *self) {
  return self->indexAttribute();
}

//  void Qt3DExtras::QCylinderGeometry::setRings(int rings)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras17QCylinderGeometry8setRingsEi(
    Qt3DExtras::QCylinderGeometry *self,
    int rings) {
  self->setRings(rings);
}

//  void Qt3DExtras::QCylinderGeometry::setSlices(int slices)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras17QCylinderGeometry9setSlicesEi(
    Qt3DExtras::QCylinderGeometry *self,
    int slices) {
  self->setSlices(slices);
}

//  void Qt3DExtras::QCylinderGeometry::setRadius(float radius)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras17QCylinderGeometry9setRadiusEf(
    Qt3DExtras::QCylinderGeometry *self,
    float radius) {
  self->setRadius(radius);
}

//  void Qt3DExtras::QCylinderGeometry::setLength(float length)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras17QCylinderGeometry9setLengthEf(
    Qt3DExtras::QCylinderGeometry *self,
    float length) {
  self->setLength(length);
}

//  void Qt3DExtras::QCylinderGeometry::radiusChanged(float radius)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras17QCylinderGeometry13radiusChangedEf(
    Qt3DExtras::QCylinderGeometry *self,
    float radius) {
  self->radiusChanged(radius);
}

//  void Qt3DExtras::QCylinderGeometry::ringsChanged(int rings)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras17QCylinderGeometry12ringsChangedEi(
    Qt3DExtras::QCylinderGeometry *self,
    int rings) {
  self->ringsChanged(rings);
}

//  void Qt3DExtras::QCylinderGeometry::slicesChanged(int slices)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras17QCylinderGeometry13slicesChangedEi(
    Qt3DExtras::QCylinderGeometry *self,
    int slices) {
  self->slicesChanged(slices);
}

//  void Qt3DExtras::QCylinderGeometry::lengthChanged(float length)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras17QCylinderGeometry13lengthChangedEf(
    Qt3DExtras::QCylinderGeometry *self,
    float length) {
  self->lengthChanged(length);
}

//  Qt3DExtras::QCylinderGeometry::QCylinderGeometry(QCylinderGeometryPrivate
//      &dd, QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DExtras::QCylinderGeometry *ritual_ZN10Qt3DExtras17QCylinderGeometryC1ERNS_24QCylinderGeometryPrivateEPN8Qt3DCore5QNodeE(
    Qt3DExtras::QCylinderGeometryPrivate *dd,
    Qt3DCore::QNode *parent) {
  return new CuteQt3DExtras_QCylinderGeometry(*dd, parent);
}

//  QCylinderGeometryPrivate *Qt3DExtras::QCylinderGeometry::d_func()
extern "C" Q_DECL_EXPORT
Qt3DExtras::QCylinderGeometryPrivate *ritual_ZN10Qt3DExtras17QCylinderGeometry6d_funcEv(
    Qt3DExtras::QCylinderGeometry *self) {
  return self->d_func();
}

//  const QCylinderGeometryPrivate *Qt3DExtras::QCylinderGeometry::d_func()
//      const
extern "C" Q_DECL_EXPORT
const Qt3DExtras::QCylinderGeometryPrivate *ritual_ZNK10Qt3DExtras17QCylinderGeometry6d_funcEv(
    const Qt3DExtras::QCylinderGeometry *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DExtras_QCylinderGeometry, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DExtras_QCylinderGeometry(
    Qt3DExtras::QCylinderGeometry *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DExtras_QCylinderGeometry *>(self)->take(key, call);
}
