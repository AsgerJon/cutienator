//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DExtras/qcuboidgeometryview.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DExtras/qcuboidgeometryview.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DExtras::QCuboidGeometryView that Python can take functions over in. Every Qt3DExtras::QCuboidGeometryView
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DExtras_QCuboidGeometryViewCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DExtras_QCuboidGeometryViewCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QCuboidGeometryViewCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QCuboidGeometryViewCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QCuboidGeometryViewCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QCuboidGeometryViewCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QCuboidGeometryViewCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DExtras_QCuboidGeometryView : public Qt3DExtras::QCuboidGeometryView {
public:
  using Qt3DExtras::QCuboidGeometryView::QCuboidGeometryView;
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
      CuteQt3DExtras_QCuboidGeometryViewCall0 call = reinterpret_cast<CuteQt3DExtras_QCuboidGeometryViewCall0>(taken[0]);
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
      CuteQt3DExtras_QCuboidGeometryViewCall1 call = reinterpret_cast<CuteQt3DExtras_QCuboidGeometryViewCall1>(taken[1]);
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
      CuteQt3DExtras_QCuboidGeometryViewCall2 call = reinterpret_cast<CuteQt3DExtras_QCuboidGeometryViewCall2>(taken[2]);
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
      CuteQt3DExtras_QCuboidGeometryViewCall3 call = reinterpret_cast<CuteQt3DExtras_QCuboidGeometryViewCall3>(taken[3]);
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
      CuteQt3DExtras_QCuboidGeometryViewCall4 call = reinterpret_cast<CuteQt3DExtras_QCuboidGeometryViewCall4>(taken[4]);
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
      CuteQt3DExtras_QCuboidGeometryViewCall5 call = reinterpret_cast<CuteQt3DExtras_QCuboidGeometryViewCall5>(taken[5]);
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
      CuteQt3DExtras_QCuboidGeometryViewCall6 call = reinterpret_cast<CuteQt3DExtras_QCuboidGeometryViewCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DExtras::QCuboidGeometryView::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DExtras19QCuboidGeometryView10metaObjectEv(
    const Qt3DExtras::QCuboidGeometryView *self) {
  return self->metaObject();
}

//  void *Qt3DExtras::QCuboidGeometryView::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DExtras19QCuboidGeometryView11qt_metacastEPKc(
    Qt3DExtras::QCuboidGeometryView *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DExtras::QCuboidGeometryView::qt_metacall(QMetaObject::Call a0,
//      int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DExtras19QCuboidGeometryView11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DExtras::QCuboidGeometryView *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DExtras::QCuboidGeometryView::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DExtras19QCuboidGeometryView2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DExtras::QCuboidGeometryView::tr(s, c, n));
}

//  Qt3DExtras::QCuboidGeometryView::QCuboidGeometryView(Qt3DCore::QNode
//      *parent)
extern "C" Q_DECL_EXPORT
Qt3DExtras::QCuboidGeometryView *ritual_ZN10Qt3DExtras19QCuboidGeometryViewC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DExtras_QCuboidGeometryView(parent);
}

//  Qt3DExtras::QCuboidGeometryView::~QCuboidGeometryView()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras19QCuboidGeometryViewD1Ev(
    Qt3DExtras::QCuboidGeometryView *self) {
  delete self;
}

//  float Qt3DExtras::QCuboidGeometryView::xExtent() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DExtras19QCuboidGeometryView7xExtentEv(
    const Qt3DExtras::QCuboidGeometryView *self) {
  return self->xExtent();
}

//  float Qt3DExtras::QCuboidGeometryView::yExtent() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DExtras19QCuboidGeometryView7yExtentEv(
    const Qt3DExtras::QCuboidGeometryView *self) {
  return self->yExtent();
}

//  float Qt3DExtras::QCuboidGeometryView::zExtent() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DExtras19QCuboidGeometryView7zExtentEv(
    const Qt3DExtras::QCuboidGeometryView *self) {
  return self->zExtent();
}

//  QSize Qt3DExtras::QCuboidGeometryView::yzMeshResolution() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK10Qt3DExtras19QCuboidGeometryView16yzMeshResolutionEv(
    const Qt3DExtras::QCuboidGeometryView *self) {
  return new QSize(self->yzMeshResolution());
}

//  QSize Qt3DExtras::QCuboidGeometryView::xzMeshResolution() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK10Qt3DExtras19QCuboidGeometryView16xzMeshResolutionEv(
    const Qt3DExtras::QCuboidGeometryView *self) {
  return new QSize(self->xzMeshResolution());
}

//  QSize Qt3DExtras::QCuboidGeometryView::xyMeshResolution() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK10Qt3DExtras19QCuboidGeometryView16xyMeshResolutionEv(
    const Qt3DExtras::QCuboidGeometryView *self) {
  return new QSize(self->xyMeshResolution());
}

//  void Qt3DExtras::QCuboidGeometryView::setXExtent(float xExtent)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras19QCuboidGeometryView10setXExtentEf(
    Qt3DExtras::QCuboidGeometryView *self,
    float xExtent) {
  self->setXExtent(xExtent);
}

//  void Qt3DExtras::QCuboidGeometryView::setYExtent(float yExtent)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras19QCuboidGeometryView10setYExtentEf(
    Qt3DExtras::QCuboidGeometryView *self,
    float yExtent) {
  self->setYExtent(yExtent);
}

//  void Qt3DExtras::QCuboidGeometryView::setZExtent(float zExtent)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras19QCuboidGeometryView10setZExtentEf(
    Qt3DExtras::QCuboidGeometryView *self,
    float zExtent) {
  self->setZExtent(zExtent);
}

//  void Qt3DExtras::QCuboidGeometryView::setYZMeshResolution(const QSize
//      &resolution)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras19QCuboidGeometryView19setYZMeshResolutionERK5QSize(
    Qt3DExtras::QCuboidGeometryView *self,
    const QSize *resolution) {
  self->setYZMeshResolution(*resolution);
}

//  void Qt3DExtras::QCuboidGeometryView::setXZMeshResolution(const QSize
//      &resolution)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras19QCuboidGeometryView19setXZMeshResolutionERK5QSize(
    Qt3DExtras::QCuboidGeometryView *self,
    const QSize *resolution) {
  self->setXZMeshResolution(*resolution);
}

//  void Qt3DExtras::QCuboidGeometryView::setXYMeshResolution(const QSize
//      &resolution)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras19QCuboidGeometryView19setXYMeshResolutionERK5QSize(
    Qt3DExtras::QCuboidGeometryView *self,
    const QSize *resolution) {
  self->setXYMeshResolution(*resolution);
}

//  void Qt3DExtras::QCuboidGeometryView::xExtentChanged(float xExtent)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras19QCuboidGeometryView14xExtentChangedEf(
    Qt3DExtras::QCuboidGeometryView *self,
    float xExtent) {
  self->xExtentChanged(xExtent);
}

//  void Qt3DExtras::QCuboidGeometryView::yExtentChanged(float yExtent)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras19QCuboidGeometryView14yExtentChangedEf(
    Qt3DExtras::QCuboidGeometryView *self,
    float yExtent) {
  self->yExtentChanged(yExtent);
}

//  void Qt3DExtras::QCuboidGeometryView::zExtentChanged(float zExtent)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras19QCuboidGeometryView14zExtentChangedEf(
    Qt3DExtras::QCuboidGeometryView *self,
    float zExtent) {
  self->zExtentChanged(zExtent);
}

//  void Qt3DExtras::QCuboidGeometryView::yzMeshResolutionChanged(const QSize
//      &yzMeshResolution)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras19QCuboidGeometryView23yzMeshResolutionChangedERK5QSize(
    Qt3DExtras::QCuboidGeometryView *self,
    const QSize *yzMeshResolution) {
  self->yzMeshResolutionChanged(*yzMeshResolution);
}

//  void Qt3DExtras::QCuboidGeometryView::xzMeshResolutionChanged(const QSize
//      &xzMeshResolution)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras19QCuboidGeometryView23xzMeshResolutionChangedERK5QSize(
    Qt3DExtras::QCuboidGeometryView *self,
    const QSize *xzMeshResolution) {
  self->xzMeshResolutionChanged(*xzMeshResolution);
}

//  void Qt3DExtras::QCuboidGeometryView::xyMeshResolutionChanged(const QSize
//      &xyMeshResolution)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras19QCuboidGeometryView23xyMeshResolutionChangedERK5QSize(
    Qt3DExtras::QCuboidGeometryView *self,
    const QSize *xyMeshResolution) {
  self->xyMeshResolutionChanged(*xyMeshResolution);
}

//  a Python function taken by a CuteQt3DExtras_QCuboidGeometryView, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DExtras_QCuboidGeometryView(
    Qt3DExtras::QCuboidGeometryView *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DExtras_QCuboidGeometryView *>(self)->take(key, call);
}
