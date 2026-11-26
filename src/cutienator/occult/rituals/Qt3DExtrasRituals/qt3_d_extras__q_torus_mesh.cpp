//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DExtras/qtorusmesh.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DExtras/qtorusmesh.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DExtras::QTorusMesh that Python can take functions over in. Every Qt3DExtras::QTorusMesh
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DExtras_QTorusMeshCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DExtras_QTorusMeshCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QTorusMeshCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QTorusMeshCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QTorusMeshCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QTorusMeshCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QTorusMeshCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DExtras_QTorusMesh : public Qt3DExtras::QTorusMesh {
public:
  using Qt3DExtras::QTorusMesh::QTorusMesh;
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
      CuteQt3DExtras_QTorusMeshCall0 call = reinterpret_cast<CuteQt3DExtras_QTorusMeshCall0>(taken[0]);
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
      CuteQt3DExtras_QTorusMeshCall1 call = reinterpret_cast<CuteQt3DExtras_QTorusMeshCall1>(taken[1]);
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
      CuteQt3DExtras_QTorusMeshCall2 call = reinterpret_cast<CuteQt3DExtras_QTorusMeshCall2>(taken[2]);
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
      CuteQt3DExtras_QTorusMeshCall3 call = reinterpret_cast<CuteQt3DExtras_QTorusMeshCall3>(taken[3]);
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
      CuteQt3DExtras_QTorusMeshCall4 call = reinterpret_cast<CuteQt3DExtras_QTorusMeshCall4>(taken[4]);
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
      CuteQt3DExtras_QTorusMeshCall5 call = reinterpret_cast<CuteQt3DExtras_QTorusMeshCall5>(taken[5]);
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
      CuteQt3DExtras_QTorusMeshCall6 call = reinterpret_cast<CuteQt3DExtras_QTorusMeshCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DExtras::QTorusMesh::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DExtras10QTorusMesh10metaObjectEv(
    const Qt3DExtras::QTorusMesh *self) {
  return self->metaObject();
}

//  void *Qt3DExtras::QTorusMesh::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DExtras10QTorusMesh11qt_metacastEPKc(
    Qt3DExtras::QTorusMesh *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DExtras::QTorusMesh::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DExtras10QTorusMesh11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DExtras::QTorusMesh *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DExtras::QTorusMesh::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DExtras10QTorusMesh2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DExtras::QTorusMesh::tr(s, c, n));
}

//  Qt3DExtras::QTorusMesh::QTorusMesh(Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DExtras::QTorusMesh *ritual_ZN10Qt3DExtras10QTorusMeshC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DExtras_QTorusMesh(parent);
}

//  Qt3DExtras::QTorusMesh::~QTorusMesh()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras10QTorusMeshD1Ev(Qt3DExtras::QTorusMesh *self) {
  delete self;
}

//  int Qt3DExtras::QTorusMesh::rings() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DExtras10QTorusMesh5ringsEv(
    const Qt3DExtras::QTorusMesh *self) {
  return self->rings();
}

//  int Qt3DExtras::QTorusMesh::slices() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DExtras10QTorusMesh6slicesEv(
    const Qt3DExtras::QTorusMesh *self) {
  return self->slices();
}

//  float Qt3DExtras::QTorusMesh::radius() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DExtras10QTorusMesh6radiusEv(
    const Qt3DExtras::QTorusMesh *self) {
  return self->radius();
}

//  float Qt3DExtras::QTorusMesh::minorRadius() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DExtras10QTorusMesh11minorRadiusEv(
    const Qt3DExtras::QTorusMesh *self) {
  return self->minorRadius();
}

//  void Qt3DExtras::QTorusMesh::setRings(int rings)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras10QTorusMesh8setRingsEi(
    Qt3DExtras::QTorusMesh *self,
    int rings) {
  self->setRings(rings);
}

//  void Qt3DExtras::QTorusMesh::setSlices(int slices)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras10QTorusMesh9setSlicesEi(
    Qt3DExtras::QTorusMesh *self,
    int slices) {
  self->setSlices(slices);
}

//  void Qt3DExtras::QTorusMesh::setRadius(float radius)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras10QTorusMesh9setRadiusEf(
    Qt3DExtras::QTorusMesh *self,
    float radius) {
  self->setRadius(radius);
}

//  void Qt3DExtras::QTorusMesh::setMinorRadius(float minorRadius)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras10QTorusMesh14setMinorRadiusEf(
    Qt3DExtras::QTorusMesh *self,
    float minorRadius) {
  self->setMinorRadius(minorRadius);
}

//  void Qt3DExtras::QTorusMesh::radiusChanged(float radius)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras10QTorusMesh13radiusChangedEf(
    Qt3DExtras::QTorusMesh *self,
    float radius) {
  self->radiusChanged(radius);
}

//  void Qt3DExtras::QTorusMesh::ringsChanged(int rings)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras10QTorusMesh12ringsChangedEi(
    Qt3DExtras::QTorusMesh *self,
    int rings) {
  self->ringsChanged(rings);
}

//  void Qt3DExtras::QTorusMesh::slicesChanged(int slices)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras10QTorusMesh13slicesChangedEi(
    Qt3DExtras::QTorusMesh *self,
    int slices) {
  self->slicesChanged(slices);
}

//  void Qt3DExtras::QTorusMesh::minorRadiusChanged(float minorRadius)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras10QTorusMesh18minorRadiusChangedEf(
    Qt3DExtras::QTorusMesh *self,
    float minorRadius) {
  self->minorRadiusChanged(minorRadius);
}

//  a Python function taken by a CuteQt3DExtras_QTorusMesh, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DExtras_QTorusMesh(
    Qt3DExtras::QTorusMesh *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DExtras_QTorusMesh *>(self)->take(key, call);
}
