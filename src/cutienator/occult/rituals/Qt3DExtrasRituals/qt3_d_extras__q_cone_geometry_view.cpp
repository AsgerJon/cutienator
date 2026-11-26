//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DExtras/qconegeometryview.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DExtras/qconegeometryview.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DExtras::QConeGeometryView that Python can take functions over in. Every Qt3DExtras::QConeGeometryView
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DExtras_QConeGeometryViewCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DExtras_QConeGeometryViewCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QConeGeometryViewCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QConeGeometryViewCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QConeGeometryViewCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QConeGeometryViewCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QConeGeometryViewCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DExtras_QConeGeometryView : public Qt3DExtras::QConeGeometryView {
public:
  using Qt3DExtras::QConeGeometryView::QConeGeometryView;
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
      CuteQt3DExtras_QConeGeometryViewCall0 call = reinterpret_cast<CuteQt3DExtras_QConeGeometryViewCall0>(taken[0]);
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
      CuteQt3DExtras_QConeGeometryViewCall1 call = reinterpret_cast<CuteQt3DExtras_QConeGeometryViewCall1>(taken[1]);
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
      CuteQt3DExtras_QConeGeometryViewCall2 call = reinterpret_cast<CuteQt3DExtras_QConeGeometryViewCall2>(taken[2]);
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
      CuteQt3DExtras_QConeGeometryViewCall3 call = reinterpret_cast<CuteQt3DExtras_QConeGeometryViewCall3>(taken[3]);
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
      CuteQt3DExtras_QConeGeometryViewCall4 call = reinterpret_cast<CuteQt3DExtras_QConeGeometryViewCall4>(taken[4]);
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
      CuteQt3DExtras_QConeGeometryViewCall5 call = reinterpret_cast<CuteQt3DExtras_QConeGeometryViewCall5>(taken[5]);
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
      CuteQt3DExtras_QConeGeometryViewCall6 call = reinterpret_cast<CuteQt3DExtras_QConeGeometryViewCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DExtras::QConeGeometryView::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DExtras17QConeGeometryView10metaObjectEv(
    const Qt3DExtras::QConeGeometryView *self) {
  return self->metaObject();
}

//  void *Qt3DExtras::QConeGeometryView::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DExtras17QConeGeometryView11qt_metacastEPKc(
    Qt3DExtras::QConeGeometryView *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DExtras::QConeGeometryView::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DExtras17QConeGeometryView11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DExtras::QConeGeometryView *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DExtras::QConeGeometryView::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DExtras17QConeGeometryView2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DExtras::QConeGeometryView::tr(s, c, n));
}

//  Qt3DExtras::QConeGeometryView::QConeGeometryView(Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DExtras::QConeGeometryView *ritual_ZN10Qt3DExtras17QConeGeometryViewC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DExtras_QConeGeometryView(parent);
}

//  Qt3DExtras::QConeGeometryView::~QConeGeometryView()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras17QConeGeometryViewD1Ev(
    Qt3DExtras::QConeGeometryView *self) {
  delete self;
}

//  int Qt3DExtras::QConeGeometryView::rings() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DExtras17QConeGeometryView5ringsEv(
    const Qt3DExtras::QConeGeometryView *self) {
  return self->rings();
}

//  int Qt3DExtras::QConeGeometryView::slices() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DExtras17QConeGeometryView6slicesEv(
    const Qt3DExtras::QConeGeometryView *self) {
  return self->slices();
}

//  bool Qt3DExtras::QConeGeometryView::hasTopEndcap() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DExtras17QConeGeometryView12hasTopEndcapEv(
    const Qt3DExtras::QConeGeometryView *self) {
  return self->hasTopEndcap();
}

//  bool Qt3DExtras::QConeGeometryView::hasBottomEndcap() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DExtras17QConeGeometryView15hasBottomEndcapEv(
    const Qt3DExtras::QConeGeometryView *self) {
  return self->hasBottomEndcap();
}

//  float Qt3DExtras::QConeGeometryView::topRadius() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DExtras17QConeGeometryView9topRadiusEv(
    const Qt3DExtras::QConeGeometryView *self) {
  return self->topRadius();
}

//  float Qt3DExtras::QConeGeometryView::bottomRadius() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DExtras17QConeGeometryView12bottomRadiusEv(
    const Qt3DExtras::QConeGeometryView *self) {
  return self->bottomRadius();
}

//  float Qt3DExtras::QConeGeometryView::length() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DExtras17QConeGeometryView6lengthEv(
    const Qt3DExtras::QConeGeometryView *self) {
  return self->length();
}

//  void Qt3DExtras::QConeGeometryView::setHasTopEndcap(bool hasTopEndcap)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras17QConeGeometryView15setHasTopEndcapEb(
    Qt3DExtras::QConeGeometryView *self,
    bool hasTopEndcap) {
  self->setHasTopEndcap(hasTopEndcap);
}

//  void Qt3DExtras::QConeGeometryView::setHasBottomEndcap(bool
//      hasBottomEndcap)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras17QConeGeometryView18setHasBottomEndcapEb(
    Qt3DExtras::QConeGeometryView *self,
    bool hasBottomEndcap) {
  self->setHasBottomEndcap(hasBottomEndcap);
}

//  void Qt3DExtras::QConeGeometryView::setTopRadius(float topRadius)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras17QConeGeometryView12setTopRadiusEf(
    Qt3DExtras::QConeGeometryView *self,
    float topRadius) {
  self->setTopRadius(topRadius);
}

//  void Qt3DExtras::QConeGeometryView::setBottomRadius(float bottomRadius)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras17QConeGeometryView15setBottomRadiusEf(
    Qt3DExtras::QConeGeometryView *self,
    float bottomRadius) {
  self->setBottomRadius(bottomRadius);
}

//  void Qt3DExtras::QConeGeometryView::setRings(int rings)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras17QConeGeometryView8setRingsEi(
    Qt3DExtras::QConeGeometryView *self,
    int rings) {
  self->setRings(rings);
}

//  void Qt3DExtras::QConeGeometryView::setSlices(int slices)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras17QConeGeometryView9setSlicesEi(
    Qt3DExtras::QConeGeometryView *self,
    int slices) {
  self->setSlices(slices);
}

//  void Qt3DExtras::QConeGeometryView::setLength(float length)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras17QConeGeometryView9setLengthEf(
    Qt3DExtras::QConeGeometryView *self,
    float length) {
  self->setLength(length);
}

//  void Qt3DExtras::QConeGeometryView::hasTopEndcapChanged(bool
//      hasTopEndcap)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras17QConeGeometryView19hasTopEndcapChangedEb(
    Qt3DExtras::QConeGeometryView *self,
    bool hasTopEndcap) {
  self->hasTopEndcapChanged(hasTopEndcap);
}

//  void Qt3DExtras::QConeGeometryView::hasBottomEndcapChanged(bool
//      hasBottomEndcap)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras17QConeGeometryView22hasBottomEndcapChangedEb(
    Qt3DExtras::QConeGeometryView *self,
    bool hasBottomEndcap) {
  self->hasBottomEndcapChanged(hasBottomEndcap);
}

//  void Qt3DExtras::QConeGeometryView::topRadiusChanged(float topRadius)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras17QConeGeometryView16topRadiusChangedEf(
    Qt3DExtras::QConeGeometryView *self,
    float topRadius) {
  self->topRadiusChanged(topRadius);
}

//  void Qt3DExtras::QConeGeometryView::bottomRadiusChanged(float
//      bottomRadius)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras17QConeGeometryView19bottomRadiusChangedEf(
    Qt3DExtras::QConeGeometryView *self,
    float bottomRadius) {
  self->bottomRadiusChanged(bottomRadius);
}

//  void Qt3DExtras::QConeGeometryView::ringsChanged(int rings)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras17QConeGeometryView12ringsChangedEi(
    Qt3DExtras::QConeGeometryView *self,
    int rings) {
  self->ringsChanged(rings);
}

//  void Qt3DExtras::QConeGeometryView::slicesChanged(int slices)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras17QConeGeometryView13slicesChangedEi(
    Qt3DExtras::QConeGeometryView *self,
    int slices) {
  self->slicesChanged(slices);
}

//  void Qt3DExtras::QConeGeometryView::lengthChanged(float length)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras17QConeGeometryView13lengthChangedEf(
    Qt3DExtras::QConeGeometryView *self,
    float length) {
  self->lengthChanged(length);
}

//  a Python function taken by a CuteQt3DExtras_QConeGeometryView, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DExtras_QConeGeometryView(
    Qt3DExtras::QConeGeometryView *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DExtras_QConeGeometryView *>(self)->take(key, call);
}
