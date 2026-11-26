//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DExtras/qspheregeometryview.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DExtras/qspheregeometryview.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DExtras::QSphereGeometryView that Python can take functions over in. Every Qt3DExtras::QSphereGeometryView
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DExtras_QSphereGeometryViewCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DExtras_QSphereGeometryViewCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QSphereGeometryViewCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QSphereGeometryViewCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QSphereGeometryViewCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QSphereGeometryViewCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QSphereGeometryViewCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DExtras_QSphereGeometryView : public Qt3DExtras::QSphereGeometryView {
public:
  using Qt3DExtras::QSphereGeometryView::QSphereGeometryView;
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
      CuteQt3DExtras_QSphereGeometryViewCall0 call = reinterpret_cast<CuteQt3DExtras_QSphereGeometryViewCall0>(taken[0]);
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
      CuteQt3DExtras_QSphereGeometryViewCall1 call = reinterpret_cast<CuteQt3DExtras_QSphereGeometryViewCall1>(taken[1]);
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
      CuteQt3DExtras_QSphereGeometryViewCall2 call = reinterpret_cast<CuteQt3DExtras_QSphereGeometryViewCall2>(taken[2]);
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
      CuteQt3DExtras_QSphereGeometryViewCall3 call = reinterpret_cast<CuteQt3DExtras_QSphereGeometryViewCall3>(taken[3]);
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
      CuteQt3DExtras_QSphereGeometryViewCall4 call = reinterpret_cast<CuteQt3DExtras_QSphereGeometryViewCall4>(taken[4]);
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
      CuteQt3DExtras_QSphereGeometryViewCall5 call = reinterpret_cast<CuteQt3DExtras_QSphereGeometryViewCall5>(taken[5]);
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
      CuteQt3DExtras_QSphereGeometryViewCall6 call = reinterpret_cast<CuteQt3DExtras_QSphereGeometryViewCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DExtras::QSphereGeometryView::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DExtras19QSphereGeometryView10metaObjectEv(
    const Qt3DExtras::QSphereGeometryView *self) {
  return self->metaObject();
}

//  void *Qt3DExtras::QSphereGeometryView::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DExtras19QSphereGeometryView11qt_metacastEPKc(
    Qt3DExtras::QSphereGeometryView *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DExtras::QSphereGeometryView::qt_metacall(QMetaObject::Call a0,
//      int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DExtras19QSphereGeometryView11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DExtras::QSphereGeometryView *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DExtras::QSphereGeometryView::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DExtras19QSphereGeometryView2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DExtras::QSphereGeometryView::tr(s, c, n));
}

//  Qt3DExtras::QSphereGeometryView::QSphereGeometryView(Qt3DCore::QNode
//      *parent)
extern "C" Q_DECL_EXPORT
Qt3DExtras::QSphereGeometryView *ritual_ZN10Qt3DExtras19QSphereGeometryViewC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DExtras_QSphereGeometryView(parent);
}

//  Qt3DExtras::QSphereGeometryView::~QSphereGeometryView()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras19QSphereGeometryViewD1Ev(
    Qt3DExtras::QSphereGeometryView *self) {
  delete self;
}

//  int Qt3DExtras::QSphereGeometryView::rings() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DExtras19QSphereGeometryView5ringsEv(
    const Qt3DExtras::QSphereGeometryView *self) {
  return self->rings();
}

//  int Qt3DExtras::QSphereGeometryView::slices() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DExtras19QSphereGeometryView6slicesEv(
    const Qt3DExtras::QSphereGeometryView *self) {
  return self->slices();
}

//  float Qt3DExtras::QSphereGeometryView::radius() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DExtras19QSphereGeometryView6radiusEv(
    const Qt3DExtras::QSphereGeometryView *self) {
  return self->radius();
}

//  bool Qt3DExtras::QSphereGeometryView::generateTangents() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DExtras19QSphereGeometryView16generateTangentsEv(
    const Qt3DExtras::QSphereGeometryView *self) {
  return self->generateTangents();
}

//  void Qt3DExtras::QSphereGeometryView::setRings(int rings)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras19QSphereGeometryView8setRingsEi(
    Qt3DExtras::QSphereGeometryView *self,
    int rings) {
  self->setRings(rings);
}

//  void Qt3DExtras::QSphereGeometryView::setSlices(int slices)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras19QSphereGeometryView9setSlicesEi(
    Qt3DExtras::QSphereGeometryView *self,
    int slices) {
  self->setSlices(slices);
}

//  void Qt3DExtras::QSphereGeometryView::setRadius(float radius)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras19QSphereGeometryView9setRadiusEf(
    Qt3DExtras::QSphereGeometryView *self,
    float radius) {
  self->setRadius(radius);
}

//  void Qt3DExtras::QSphereGeometryView::setGenerateTangents(bool gen)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras19QSphereGeometryView19setGenerateTangentsEb(
    Qt3DExtras::QSphereGeometryView *self,
    bool gen) {
  self->setGenerateTangents(gen);
}

//  void Qt3DExtras::QSphereGeometryView::radiusChanged(float radius)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras19QSphereGeometryView13radiusChangedEf(
    Qt3DExtras::QSphereGeometryView *self,
    float radius) {
  self->radiusChanged(radius);
}

//  void Qt3DExtras::QSphereGeometryView::ringsChanged(int rings)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras19QSphereGeometryView12ringsChangedEi(
    Qt3DExtras::QSphereGeometryView *self,
    int rings) {
  self->ringsChanged(rings);
}

//  void Qt3DExtras::QSphereGeometryView::slicesChanged(int slices)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras19QSphereGeometryView13slicesChangedEi(
    Qt3DExtras::QSphereGeometryView *self,
    int slices) {
  self->slicesChanged(slices);
}

//  void Qt3DExtras::QSphereGeometryView::generateTangentsChanged(bool
//      generateTangents)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras19QSphereGeometryView23generateTangentsChangedEb(
    Qt3DExtras::QSphereGeometryView *self,
    bool generateTangents) {
  self->generateTangentsChanged(generateTangents);
}

//  a Python function taken by a CuteQt3DExtras_QSphereGeometryView, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DExtras_QSphereGeometryView(
    Qt3DExtras::QSphereGeometryView *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DExtras_QSphereGeometryView *>(self)->take(key, call);
}
