//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DExtras/qconegeometry.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DExtras/qconegeometry.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DExtras::QConeGeometry that Python can take functions over in. Every Qt3DExtras::QConeGeometry
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DExtras_QConeGeometryCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DExtras_QConeGeometryCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QConeGeometryCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QConeGeometryCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QConeGeometryCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QConeGeometryCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QConeGeometryCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DExtras_QConeGeometry : public Qt3DExtras::QConeGeometry {
public:
  using Qt3DExtras::QConeGeometry::QConeGeometry;
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
      CuteQt3DExtras_QConeGeometryCall0 call = reinterpret_cast<CuteQt3DExtras_QConeGeometryCall0>(taken[0]);
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
      CuteQt3DExtras_QConeGeometryCall1 call = reinterpret_cast<CuteQt3DExtras_QConeGeometryCall1>(taken[1]);
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
      CuteQt3DExtras_QConeGeometryCall2 call = reinterpret_cast<CuteQt3DExtras_QConeGeometryCall2>(taken[2]);
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
      CuteQt3DExtras_QConeGeometryCall3 call = reinterpret_cast<CuteQt3DExtras_QConeGeometryCall3>(taken[3]);
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
      CuteQt3DExtras_QConeGeometryCall4 call = reinterpret_cast<CuteQt3DExtras_QConeGeometryCall4>(taken[4]);
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
      CuteQt3DExtras_QConeGeometryCall5 call = reinterpret_cast<CuteQt3DExtras_QConeGeometryCall5>(taken[5]);
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
      CuteQt3DExtras_QConeGeometryCall6 call = reinterpret_cast<CuteQt3DExtras_QConeGeometryCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DExtras::QConeGeometry::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DExtras13QConeGeometry10metaObjectEv(
    const Qt3DExtras::QConeGeometry *self) {
  return self->metaObject();
}

//  void *Qt3DExtras::QConeGeometry::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DExtras13QConeGeometry11qt_metacastEPKc(
    Qt3DExtras::QConeGeometry *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DExtras::QConeGeometry::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DExtras13QConeGeometry11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DExtras::QConeGeometry *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DExtras::QConeGeometry::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DExtras13QConeGeometry2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DExtras::QConeGeometry::tr(s, c, n));
}

//  Qt3DExtras::QConeGeometry::QConeGeometry(QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DExtras::QConeGeometry *ritual_ZN10Qt3DExtras13QConeGeometryC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DExtras_QConeGeometry(parent);
}

//  Qt3DExtras::QConeGeometry::~QConeGeometry()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras13QConeGeometryD1Ev(
    Qt3DExtras::QConeGeometry *self) {
  delete self;
}

//  void Qt3DExtras::QConeGeometry::updateVertices()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras13QConeGeometry14updateVerticesEv(
    Qt3DExtras::QConeGeometry *self) {
  self->updateVertices();
}

//  void Qt3DExtras::QConeGeometry::updateIndices()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras13QConeGeometry13updateIndicesEv(
    Qt3DExtras::QConeGeometry *self) {
  self->updateIndices();
}

//  bool Qt3DExtras::QConeGeometry::hasTopEndcap() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DExtras13QConeGeometry12hasTopEndcapEv(
    const Qt3DExtras::QConeGeometry *self) {
  return self->hasTopEndcap();
}

//  bool Qt3DExtras::QConeGeometry::hasBottomEndcap() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DExtras13QConeGeometry15hasBottomEndcapEv(
    const Qt3DExtras::QConeGeometry *self) {
  return self->hasBottomEndcap();
}

//  float Qt3DExtras::QConeGeometry::topRadius() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DExtras13QConeGeometry9topRadiusEv(
    const Qt3DExtras::QConeGeometry *self) {
  return self->topRadius();
}

//  float Qt3DExtras::QConeGeometry::bottomRadius() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DExtras13QConeGeometry12bottomRadiusEv(
    const Qt3DExtras::QConeGeometry *self) {
  return self->bottomRadius();
}

//  int Qt3DExtras::QConeGeometry::rings() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DExtras13QConeGeometry5ringsEv(
    const Qt3DExtras::QConeGeometry *self) {
  return self->rings();
}

//  int Qt3DExtras::QConeGeometry::slices() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DExtras13QConeGeometry6slicesEv(
    const Qt3DExtras::QConeGeometry *self) {
  return self->slices();
}

//  float Qt3DExtras::QConeGeometry::length() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DExtras13QConeGeometry6lengthEv(
    const Qt3DExtras::QConeGeometry *self) {
  return self->length();
}

//  Qt3DCore::QAttribute *Qt3DExtras::QConeGeometry::positionAttribute()
//      const
extern "C" Q_DECL_EXPORT
Qt3DCore::QAttribute *ritual_ZNK10Qt3DExtras13QConeGeometry17positionAttributeEv(
    const Qt3DExtras::QConeGeometry *self) {
  return self->positionAttribute();
}

//  Qt3DCore::QAttribute *Qt3DExtras::QConeGeometry::normalAttribute() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QAttribute *ritual_ZNK10Qt3DExtras13QConeGeometry15normalAttributeEv(
    const Qt3DExtras::QConeGeometry *self) {
  return self->normalAttribute();
}

//  Qt3DCore::QAttribute *Qt3DExtras::QConeGeometry::texCoordAttribute()
//      const
extern "C" Q_DECL_EXPORT
Qt3DCore::QAttribute *ritual_ZNK10Qt3DExtras13QConeGeometry17texCoordAttributeEv(
    const Qt3DExtras::QConeGeometry *self) {
  return self->texCoordAttribute();
}

//  Qt3DCore::QAttribute *Qt3DExtras::QConeGeometry::indexAttribute() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QAttribute *ritual_ZNK10Qt3DExtras13QConeGeometry14indexAttributeEv(
    const Qt3DExtras::QConeGeometry *self) {
  return self->indexAttribute();
}

//  void Qt3DExtras::QConeGeometry::setHasTopEndcap(bool hasTopEndcap)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras13QConeGeometry15setHasTopEndcapEb(
    Qt3DExtras::QConeGeometry *self,
    bool hasTopEndcap) {
  self->setHasTopEndcap(hasTopEndcap);
}

//  void Qt3DExtras::QConeGeometry::setHasBottomEndcap(bool hasBottomEndcap)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras13QConeGeometry18setHasBottomEndcapEb(
    Qt3DExtras::QConeGeometry *self,
    bool hasBottomEndcap) {
  self->setHasBottomEndcap(hasBottomEndcap);
}

//  void Qt3DExtras::QConeGeometry::setTopRadius(float topRadius)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras13QConeGeometry12setTopRadiusEf(
    Qt3DExtras::QConeGeometry *self,
    float topRadius) {
  self->setTopRadius(topRadius);
}

//  void Qt3DExtras::QConeGeometry::setBottomRadius(float bottomRadius)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras13QConeGeometry15setBottomRadiusEf(
    Qt3DExtras::QConeGeometry *self,
    float bottomRadius) {
  self->setBottomRadius(bottomRadius);
}

//  void Qt3DExtras::QConeGeometry::setRings(int rings)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras13QConeGeometry8setRingsEi(
    Qt3DExtras::QConeGeometry *self,
    int rings) {
  self->setRings(rings);
}

//  void Qt3DExtras::QConeGeometry::setSlices(int slices)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras13QConeGeometry9setSlicesEi(
    Qt3DExtras::QConeGeometry *self,
    int slices) {
  self->setSlices(slices);
}

//  void Qt3DExtras::QConeGeometry::setLength(float length)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras13QConeGeometry9setLengthEf(
    Qt3DExtras::QConeGeometry *self,
    float length) {
  self->setLength(length);
}

//  void Qt3DExtras::QConeGeometry::hasTopEndcapChanged(bool hasTopEndcap)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras13QConeGeometry19hasTopEndcapChangedEb(
    Qt3DExtras::QConeGeometry *self,
    bool hasTopEndcap) {
  self->hasTopEndcapChanged(hasTopEndcap);
}

//  void Qt3DExtras::QConeGeometry::hasBottomEndcapChanged(bool
//      hasBottomEndcap)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras13QConeGeometry22hasBottomEndcapChangedEb(
    Qt3DExtras::QConeGeometry *self,
    bool hasBottomEndcap) {
  self->hasBottomEndcapChanged(hasBottomEndcap);
}

//  void Qt3DExtras::QConeGeometry::topRadiusChanged(float topRadius)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras13QConeGeometry16topRadiusChangedEf(
    Qt3DExtras::QConeGeometry *self,
    float topRadius) {
  self->topRadiusChanged(topRadius);
}

//  void Qt3DExtras::QConeGeometry::bottomRadiusChanged(float bottomRadius)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras13QConeGeometry19bottomRadiusChangedEf(
    Qt3DExtras::QConeGeometry *self,
    float bottomRadius) {
  self->bottomRadiusChanged(bottomRadius);
}

//  void Qt3DExtras::QConeGeometry::ringsChanged(int rings)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras13QConeGeometry12ringsChangedEi(
    Qt3DExtras::QConeGeometry *self,
    int rings) {
  self->ringsChanged(rings);
}

//  void Qt3DExtras::QConeGeometry::slicesChanged(int slices)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras13QConeGeometry13slicesChangedEi(
    Qt3DExtras::QConeGeometry *self,
    int slices) {
  self->slicesChanged(slices);
}

//  void Qt3DExtras::QConeGeometry::lengthChanged(float length)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras13QConeGeometry13lengthChangedEf(
    Qt3DExtras::QConeGeometry *self,
    float length) {
  self->lengthChanged(length);
}

//  Qt3DExtras::QConeGeometry::QConeGeometry(QConeGeometryPrivate &dd, QNode
//      *parent)
extern "C" Q_DECL_EXPORT
Qt3DExtras::QConeGeometry *ritual_ZN10Qt3DExtras13QConeGeometryC1ERNS_20QConeGeometryPrivateEPN8Qt3DCore5QNodeE(
    Qt3DExtras::QConeGeometryPrivate *dd,
    Qt3DCore::QNode *parent) {
  return new CuteQt3DExtras_QConeGeometry(*dd, parent);
}

//  QConeGeometryPrivate *Qt3DExtras::QConeGeometry::d_func()
extern "C" Q_DECL_EXPORT
Qt3DExtras::QConeGeometryPrivate *ritual_ZN10Qt3DExtras13QConeGeometry6d_funcEv(
    Qt3DExtras::QConeGeometry *self) {
  return self->d_func();
}

//  const QConeGeometryPrivate *Qt3DExtras::QConeGeometry::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DExtras::QConeGeometryPrivate *ritual_ZNK10Qt3DExtras13QConeGeometry6d_funcEv(
    const Qt3DExtras::QConeGeometry *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DExtras_QConeGeometry, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DExtras_QConeGeometry(
    Qt3DExtras::QConeGeometry *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DExtras_QConeGeometry *>(self)->take(key, call);
}
