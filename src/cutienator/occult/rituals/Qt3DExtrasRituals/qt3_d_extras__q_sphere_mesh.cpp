//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DExtras/qspheremesh.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DExtras/qspheremesh.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DExtras::QSphereMesh that Python can take functions over in. Every Qt3DExtras::QSphereMesh
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DExtras_QSphereMeshCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DExtras_QSphereMeshCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QSphereMeshCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QSphereMeshCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QSphereMeshCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QSphereMeshCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QSphereMeshCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DExtras_QSphereMesh : public Qt3DExtras::QSphereMesh {
public:
  using Qt3DExtras::QSphereMesh::QSphereMesh;
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
      CuteQt3DExtras_QSphereMeshCall0 call = reinterpret_cast<CuteQt3DExtras_QSphereMeshCall0>(taken[0]);
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
      CuteQt3DExtras_QSphereMeshCall1 call = reinterpret_cast<CuteQt3DExtras_QSphereMeshCall1>(taken[1]);
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
      CuteQt3DExtras_QSphereMeshCall2 call = reinterpret_cast<CuteQt3DExtras_QSphereMeshCall2>(taken[2]);
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
      CuteQt3DExtras_QSphereMeshCall3 call = reinterpret_cast<CuteQt3DExtras_QSphereMeshCall3>(taken[3]);
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
      CuteQt3DExtras_QSphereMeshCall4 call = reinterpret_cast<CuteQt3DExtras_QSphereMeshCall4>(taken[4]);
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
      CuteQt3DExtras_QSphereMeshCall5 call = reinterpret_cast<CuteQt3DExtras_QSphereMeshCall5>(taken[5]);
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
      CuteQt3DExtras_QSphereMeshCall6 call = reinterpret_cast<CuteQt3DExtras_QSphereMeshCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DExtras::QSphereMesh::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DExtras11QSphereMesh10metaObjectEv(
    const Qt3DExtras::QSphereMesh *self) {
  return self->metaObject();
}

//  void *Qt3DExtras::QSphereMesh::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DExtras11QSphereMesh11qt_metacastEPKc(
    Qt3DExtras::QSphereMesh *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DExtras::QSphereMesh::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DExtras11QSphereMesh11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DExtras::QSphereMesh *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DExtras::QSphereMesh::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DExtras11QSphereMesh2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DExtras::QSphereMesh::tr(s, c, n));
}

//  Qt3DExtras::QSphereMesh::QSphereMesh(Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DExtras::QSphereMesh *ritual_ZN10Qt3DExtras11QSphereMeshC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DExtras_QSphereMesh(parent);
}

//  Qt3DExtras::QSphereMesh::~QSphereMesh()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras11QSphereMeshD1Ev(Qt3DExtras::QSphereMesh *self) {
  delete self;
}

//  int Qt3DExtras::QSphereMesh::rings() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DExtras11QSphereMesh5ringsEv(
    const Qt3DExtras::QSphereMesh *self) {
  return self->rings();
}

//  int Qt3DExtras::QSphereMesh::slices() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DExtras11QSphereMesh6slicesEv(
    const Qt3DExtras::QSphereMesh *self) {
  return self->slices();
}

//  float Qt3DExtras::QSphereMesh::radius() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DExtras11QSphereMesh6radiusEv(
    const Qt3DExtras::QSphereMesh *self) {
  return self->radius();
}

//  bool Qt3DExtras::QSphereMesh::generateTangents() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DExtras11QSphereMesh16generateTangentsEv(
    const Qt3DExtras::QSphereMesh *self) {
  return self->generateTangents();
}

//  void Qt3DExtras::QSphereMesh::setRings(int rings)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras11QSphereMesh8setRingsEi(
    Qt3DExtras::QSphereMesh *self,
    int rings) {
  self->setRings(rings);
}

//  void Qt3DExtras::QSphereMesh::setSlices(int slices)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras11QSphereMesh9setSlicesEi(
    Qt3DExtras::QSphereMesh *self,
    int slices) {
  self->setSlices(slices);
}

//  void Qt3DExtras::QSphereMesh::setRadius(float radius)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras11QSphereMesh9setRadiusEf(
    Qt3DExtras::QSphereMesh *self,
    float radius) {
  self->setRadius(radius);
}

//  void Qt3DExtras::QSphereMesh::setGenerateTangents(bool gen)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras11QSphereMesh19setGenerateTangentsEb(
    Qt3DExtras::QSphereMesh *self,
    bool gen) {
  self->setGenerateTangents(gen);
}

//  void Qt3DExtras::QSphereMesh::radiusChanged(float radius)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras11QSphereMesh13radiusChangedEf(
    Qt3DExtras::QSphereMesh *self,
    float radius) {
  self->radiusChanged(radius);
}

//  void Qt3DExtras::QSphereMesh::ringsChanged(int rings)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras11QSphereMesh12ringsChangedEi(
    Qt3DExtras::QSphereMesh *self,
    int rings) {
  self->ringsChanged(rings);
}

//  void Qt3DExtras::QSphereMesh::slicesChanged(int slices)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras11QSphereMesh13slicesChangedEi(
    Qt3DExtras::QSphereMesh *self,
    int slices) {
  self->slicesChanged(slices);
}

//  void Qt3DExtras::QSphereMesh::generateTangentsChanged(bool
//      generateTangents)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras11QSphereMesh23generateTangentsChangedEb(
    Qt3DExtras::QSphereMesh *self,
    bool generateTangents) {
  self->generateTangentsChanged(generateTangents);
}

//  a Python function taken by a CuteQt3DExtras_QSphereMesh, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DExtras_QSphereMesh(
    Qt3DExtras::QSphereMesh *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DExtras_QSphereMesh *>(self)->take(key, call);
}
