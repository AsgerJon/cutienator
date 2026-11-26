//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DExtras/qspheregeometry.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DExtras/qspheregeometry.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DExtras::QSphereGeometry that Python can take functions over in. Every Qt3DExtras::QSphereGeometry
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DExtras_QSphereGeometryCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DExtras_QSphereGeometryCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QSphereGeometryCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QSphereGeometryCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QSphereGeometryCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QSphereGeometryCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QSphereGeometryCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DExtras_QSphereGeometry : public Qt3DExtras::QSphereGeometry {
public:
  using Qt3DExtras::QSphereGeometry::QSphereGeometry;
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
      CuteQt3DExtras_QSphereGeometryCall0 call = reinterpret_cast<CuteQt3DExtras_QSphereGeometryCall0>(taken[0]);
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
      CuteQt3DExtras_QSphereGeometryCall1 call = reinterpret_cast<CuteQt3DExtras_QSphereGeometryCall1>(taken[1]);
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
      CuteQt3DExtras_QSphereGeometryCall2 call = reinterpret_cast<CuteQt3DExtras_QSphereGeometryCall2>(taken[2]);
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
      CuteQt3DExtras_QSphereGeometryCall3 call = reinterpret_cast<CuteQt3DExtras_QSphereGeometryCall3>(taken[3]);
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
      CuteQt3DExtras_QSphereGeometryCall4 call = reinterpret_cast<CuteQt3DExtras_QSphereGeometryCall4>(taken[4]);
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
      CuteQt3DExtras_QSphereGeometryCall5 call = reinterpret_cast<CuteQt3DExtras_QSphereGeometryCall5>(taken[5]);
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
      CuteQt3DExtras_QSphereGeometryCall6 call = reinterpret_cast<CuteQt3DExtras_QSphereGeometryCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DExtras::QSphereGeometry::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DExtras15QSphereGeometry10metaObjectEv(
    const Qt3DExtras::QSphereGeometry *self) {
  return self->metaObject();
}

//  void *Qt3DExtras::QSphereGeometry::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DExtras15QSphereGeometry11qt_metacastEPKc(
    Qt3DExtras::QSphereGeometry *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DExtras::QSphereGeometry::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DExtras15QSphereGeometry11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DExtras::QSphereGeometry *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DExtras::QSphereGeometry::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DExtras15QSphereGeometry2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DExtras::QSphereGeometry::tr(s, c, n));
}

//  Qt3DExtras::QSphereGeometry::QSphereGeometry(QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DExtras::QSphereGeometry *ritual_ZN10Qt3DExtras15QSphereGeometryC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DExtras_QSphereGeometry(parent);
}

//  Qt3DExtras::QSphereGeometry::~QSphereGeometry()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras15QSphereGeometryD1Ev(
    Qt3DExtras::QSphereGeometry *self) {
  delete self;
}

//  void Qt3DExtras::QSphereGeometry::updateVertices()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras15QSphereGeometry14updateVerticesEv(
    Qt3DExtras::QSphereGeometry *self) {
  self->updateVertices();
}

//  void Qt3DExtras::QSphereGeometry::updateIndices()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras15QSphereGeometry13updateIndicesEv(
    Qt3DExtras::QSphereGeometry *self) {
  self->updateIndices();
}

//  bool Qt3DExtras::QSphereGeometry::generateTangents() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DExtras15QSphereGeometry16generateTangentsEv(
    const Qt3DExtras::QSphereGeometry *self) {
  return self->generateTangents();
}

//  int Qt3DExtras::QSphereGeometry::rings() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DExtras15QSphereGeometry5ringsEv(
    const Qt3DExtras::QSphereGeometry *self) {
  return self->rings();
}

//  int Qt3DExtras::QSphereGeometry::slices() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DExtras15QSphereGeometry6slicesEv(
    const Qt3DExtras::QSphereGeometry *self) {
  return self->slices();
}

//  float Qt3DExtras::QSphereGeometry::radius() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DExtras15QSphereGeometry6radiusEv(
    const Qt3DExtras::QSphereGeometry *self) {
  return self->radius();
}

//  Qt3DCore::QAttribute *Qt3DExtras::QSphereGeometry::positionAttribute()
//      const
extern "C" Q_DECL_EXPORT
Qt3DCore::QAttribute *ritual_ZNK10Qt3DExtras15QSphereGeometry17positionAttributeEv(
    const Qt3DExtras::QSphereGeometry *self) {
  return self->positionAttribute();
}

//  Qt3DCore::QAttribute *Qt3DExtras::QSphereGeometry::normalAttribute()
//      const
extern "C" Q_DECL_EXPORT
Qt3DCore::QAttribute *ritual_ZNK10Qt3DExtras15QSphereGeometry15normalAttributeEv(
    const Qt3DExtras::QSphereGeometry *self) {
  return self->normalAttribute();
}

//  Qt3DCore::QAttribute *Qt3DExtras::QSphereGeometry::texCoordAttribute()
//      const
extern "C" Q_DECL_EXPORT
Qt3DCore::QAttribute *ritual_ZNK10Qt3DExtras15QSphereGeometry17texCoordAttributeEv(
    const Qt3DExtras::QSphereGeometry *self) {
  return self->texCoordAttribute();
}

//  Qt3DCore::QAttribute *Qt3DExtras::QSphereGeometry::tangentAttribute()
//      const
extern "C" Q_DECL_EXPORT
Qt3DCore::QAttribute *ritual_ZNK10Qt3DExtras15QSphereGeometry16tangentAttributeEv(
    const Qt3DExtras::QSphereGeometry *self) {
  return self->tangentAttribute();
}

//  Qt3DCore::QAttribute *Qt3DExtras::QSphereGeometry::indexAttribute() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QAttribute *ritual_ZNK10Qt3DExtras15QSphereGeometry14indexAttributeEv(
    const Qt3DExtras::QSphereGeometry *self) {
  return self->indexAttribute();
}

//  void Qt3DExtras::QSphereGeometry::setRings(int rings)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras15QSphereGeometry8setRingsEi(
    Qt3DExtras::QSphereGeometry *self,
    int rings) {
  self->setRings(rings);
}

//  void Qt3DExtras::QSphereGeometry::setSlices(int slices)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras15QSphereGeometry9setSlicesEi(
    Qt3DExtras::QSphereGeometry *self,
    int slices) {
  self->setSlices(slices);
}

//  void Qt3DExtras::QSphereGeometry::setRadius(float radius)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras15QSphereGeometry9setRadiusEf(
    Qt3DExtras::QSphereGeometry *self,
    float radius) {
  self->setRadius(radius);
}

//  void Qt3DExtras::QSphereGeometry::setGenerateTangents(bool gen)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras15QSphereGeometry19setGenerateTangentsEb(
    Qt3DExtras::QSphereGeometry *self,
    bool gen) {
  self->setGenerateTangents(gen);
}

//  void Qt3DExtras::QSphereGeometry::radiusChanged(float radius)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras15QSphereGeometry13radiusChangedEf(
    Qt3DExtras::QSphereGeometry *self,
    float radius) {
  self->radiusChanged(radius);
}

//  void Qt3DExtras::QSphereGeometry::ringsChanged(int rings)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras15QSphereGeometry12ringsChangedEi(
    Qt3DExtras::QSphereGeometry *self,
    int rings) {
  self->ringsChanged(rings);
}

//  void Qt3DExtras::QSphereGeometry::slicesChanged(int slices)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras15QSphereGeometry13slicesChangedEi(
    Qt3DExtras::QSphereGeometry *self,
    int slices) {
  self->slicesChanged(slices);
}

//  void Qt3DExtras::QSphereGeometry::generateTangentsChanged(bool
//      generateTangents)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras15QSphereGeometry23generateTangentsChangedEb(
    Qt3DExtras::QSphereGeometry *self,
    bool generateTangents) {
  self->generateTangentsChanged(generateTangents);
}

//  Qt3DExtras::QSphereGeometry::QSphereGeometry(QSphereGeometryPrivate &dd,
//      QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DExtras::QSphereGeometry *ritual_ZN10Qt3DExtras15QSphereGeometryC1ERNS_22QSphereGeometryPrivateEPN8Qt3DCore5QNodeE(
    Qt3DExtras::QSphereGeometryPrivate *dd,
    Qt3DCore::QNode *parent) {
  return new CuteQt3DExtras_QSphereGeometry(*dd, parent);
}

//  QSphereGeometryPrivate *Qt3DExtras::QSphereGeometry::d_func()
extern "C" Q_DECL_EXPORT
Qt3DExtras::QSphereGeometryPrivate *ritual_ZN10Qt3DExtras15QSphereGeometry6d_funcEv(
    Qt3DExtras::QSphereGeometry *self) {
  return self->d_func();
}

//  const QSphereGeometryPrivate *Qt3DExtras::QSphereGeometry::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DExtras::QSphereGeometryPrivate *ritual_ZNK10Qt3DExtras15QSphereGeometry6d_funcEv(
    const Qt3DExtras::QSphereGeometry *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DExtras_QSphereGeometry, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DExtras_QSphereGeometry(
    Qt3DExtras::QSphereGeometry *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DExtras_QSphereGeometry *>(self)->take(key, call);
}
