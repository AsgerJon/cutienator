//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DExtras/qconemesh.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DExtras/qconemesh.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DExtras::QConeMesh that Python can take functions over in. Every Qt3DExtras::QConeMesh
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DExtras_QConeMeshCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DExtras_QConeMeshCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QConeMeshCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QConeMeshCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QConeMeshCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QConeMeshCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QConeMeshCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DExtras_QConeMesh : public Qt3DExtras::QConeMesh {
public:
  using Qt3DExtras::QConeMesh::QConeMesh;
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
      CuteQt3DExtras_QConeMeshCall0 call = reinterpret_cast<CuteQt3DExtras_QConeMeshCall0>(taken[0]);
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
      CuteQt3DExtras_QConeMeshCall1 call = reinterpret_cast<CuteQt3DExtras_QConeMeshCall1>(taken[1]);
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
      CuteQt3DExtras_QConeMeshCall2 call = reinterpret_cast<CuteQt3DExtras_QConeMeshCall2>(taken[2]);
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
      CuteQt3DExtras_QConeMeshCall3 call = reinterpret_cast<CuteQt3DExtras_QConeMeshCall3>(taken[3]);
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
      CuteQt3DExtras_QConeMeshCall4 call = reinterpret_cast<CuteQt3DExtras_QConeMeshCall4>(taken[4]);
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
      CuteQt3DExtras_QConeMeshCall5 call = reinterpret_cast<CuteQt3DExtras_QConeMeshCall5>(taken[5]);
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
      CuteQt3DExtras_QConeMeshCall6 call = reinterpret_cast<CuteQt3DExtras_QConeMeshCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DExtras::QConeMesh::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DExtras9QConeMesh10metaObjectEv(
    const Qt3DExtras::QConeMesh *self) {
  return self->metaObject();
}

//  void *Qt3DExtras::QConeMesh::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DExtras9QConeMesh11qt_metacastEPKc(
    Qt3DExtras::QConeMesh *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DExtras::QConeMesh::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DExtras9QConeMesh11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DExtras::QConeMesh *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DExtras::QConeMesh::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DExtras9QConeMesh2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DExtras::QConeMesh::tr(s, c, n));
}

//  Qt3DExtras::QConeMesh::QConeMesh(Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DExtras::QConeMesh *ritual_ZN10Qt3DExtras9QConeMeshC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DExtras_QConeMesh(parent);
}

//  Qt3DExtras::QConeMesh::~QConeMesh()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras9QConeMeshD1Ev(Qt3DExtras::QConeMesh *self) {
  delete self;
}

//  int Qt3DExtras::QConeMesh::rings() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DExtras9QConeMesh5ringsEv(
    const Qt3DExtras::QConeMesh *self) {
  return self->rings();
}

//  int Qt3DExtras::QConeMesh::slices() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DExtras9QConeMesh6slicesEv(
    const Qt3DExtras::QConeMesh *self) {
  return self->slices();
}

//  bool Qt3DExtras::QConeMesh::hasTopEndcap() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DExtras9QConeMesh12hasTopEndcapEv(
    const Qt3DExtras::QConeMesh *self) {
  return self->hasTopEndcap();
}

//  bool Qt3DExtras::QConeMesh::hasBottomEndcap() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DExtras9QConeMesh15hasBottomEndcapEv(
    const Qt3DExtras::QConeMesh *self) {
  return self->hasBottomEndcap();
}

//  float Qt3DExtras::QConeMesh::topRadius() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DExtras9QConeMesh9topRadiusEv(
    const Qt3DExtras::QConeMesh *self) {
  return self->topRadius();
}

//  float Qt3DExtras::QConeMesh::bottomRadius() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DExtras9QConeMesh12bottomRadiusEv(
    const Qt3DExtras::QConeMesh *self) {
  return self->bottomRadius();
}

//  float Qt3DExtras::QConeMesh::length() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DExtras9QConeMesh6lengthEv(
    const Qt3DExtras::QConeMesh *self) {
  return self->length();
}

//  void Qt3DExtras::QConeMesh::setHasTopEndcap(bool hasTopEndcap)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras9QConeMesh15setHasTopEndcapEb(
    Qt3DExtras::QConeMesh *self,
    bool hasTopEndcap) {
  self->setHasTopEndcap(hasTopEndcap);
}

//  void Qt3DExtras::QConeMesh::setHasBottomEndcap(bool hasBottomEndcap)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras9QConeMesh18setHasBottomEndcapEb(
    Qt3DExtras::QConeMesh *self,
    bool hasBottomEndcap) {
  self->setHasBottomEndcap(hasBottomEndcap);
}

//  void Qt3DExtras::QConeMesh::setTopRadius(float topRadius)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras9QConeMesh12setTopRadiusEf(
    Qt3DExtras::QConeMesh *self,
    float topRadius) {
  self->setTopRadius(topRadius);
}

//  void Qt3DExtras::QConeMesh::setBottomRadius(float bottomRadius)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras9QConeMesh15setBottomRadiusEf(
    Qt3DExtras::QConeMesh *self,
    float bottomRadius) {
  self->setBottomRadius(bottomRadius);
}

//  void Qt3DExtras::QConeMesh::setRings(int rings)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras9QConeMesh8setRingsEi(
    Qt3DExtras::QConeMesh *self,
    int rings) {
  self->setRings(rings);
}

//  void Qt3DExtras::QConeMesh::setSlices(int slices)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras9QConeMesh9setSlicesEi(
    Qt3DExtras::QConeMesh *self,
    int slices) {
  self->setSlices(slices);
}

//  void Qt3DExtras::QConeMesh::setLength(float length)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras9QConeMesh9setLengthEf(
    Qt3DExtras::QConeMesh *self,
    float length) {
  self->setLength(length);
}

//  void Qt3DExtras::QConeMesh::hasTopEndcapChanged(bool hasTopEndcap)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras9QConeMesh19hasTopEndcapChangedEb(
    Qt3DExtras::QConeMesh *self,
    bool hasTopEndcap) {
  self->hasTopEndcapChanged(hasTopEndcap);
}

//  void Qt3DExtras::QConeMesh::hasBottomEndcapChanged(bool hasBottomEndcap)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras9QConeMesh22hasBottomEndcapChangedEb(
    Qt3DExtras::QConeMesh *self,
    bool hasBottomEndcap) {
  self->hasBottomEndcapChanged(hasBottomEndcap);
}

//  void Qt3DExtras::QConeMesh::topRadiusChanged(float topRadius)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras9QConeMesh16topRadiusChangedEf(
    Qt3DExtras::QConeMesh *self,
    float topRadius) {
  self->topRadiusChanged(topRadius);
}

//  void Qt3DExtras::QConeMesh::bottomRadiusChanged(float bottomRadius)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras9QConeMesh19bottomRadiusChangedEf(
    Qt3DExtras::QConeMesh *self,
    float bottomRadius) {
  self->bottomRadiusChanged(bottomRadius);
}

//  void Qt3DExtras::QConeMesh::ringsChanged(int rings)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras9QConeMesh12ringsChangedEi(
    Qt3DExtras::QConeMesh *self,
    int rings) {
  self->ringsChanged(rings);
}

//  void Qt3DExtras::QConeMesh::slicesChanged(int slices)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras9QConeMesh13slicesChangedEi(
    Qt3DExtras::QConeMesh *self,
    int slices) {
  self->slicesChanged(slices);
}

//  void Qt3DExtras::QConeMesh::lengthChanged(float length)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras9QConeMesh13lengthChangedEf(
    Qt3DExtras::QConeMesh *self,
    float length) {
  self->lengthChanged(length);
}

//  a Python function taken by a CuteQt3DExtras_QConeMesh, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DExtras_QConeMesh(
    Qt3DExtras::QConeMesh *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DExtras_QConeMesh *>(self)->take(key, call);
}
