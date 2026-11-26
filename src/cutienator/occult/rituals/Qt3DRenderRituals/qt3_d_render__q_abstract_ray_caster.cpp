//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/qabstractraycaster.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DRender/qabstractraycaster.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <Qt3DRender/Qt3DRender>
#include <QtCore/QList>

//  A Qt3DRender::QAbstractRayCaster that Python can take functions over in. Every Qt3DRender::QAbstractRayCaster
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QAbstractRayCasterCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QAbstractRayCasterCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QAbstractRayCasterCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QAbstractRayCasterCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QAbstractRayCasterCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QAbstractRayCasterCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QAbstractRayCasterCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DRender_QAbstractRayCaster : public Qt3DRender::QAbstractRayCaster {
public:
  using Qt3DRender::QAbstractRayCaster::QAbstractRayCaster;
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
      CuteQt3DRender_QAbstractRayCasterCall0 call = reinterpret_cast<CuteQt3DRender_QAbstractRayCasterCall0>(taken[0]);
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
      CuteQt3DRender_QAbstractRayCasterCall1 call = reinterpret_cast<CuteQt3DRender_QAbstractRayCasterCall1>(taken[1]);
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
      CuteQt3DRender_QAbstractRayCasterCall2 call = reinterpret_cast<CuteQt3DRender_QAbstractRayCasterCall2>(taken[2]);
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
      CuteQt3DRender_QAbstractRayCasterCall3 call = reinterpret_cast<CuteQt3DRender_QAbstractRayCasterCall3>(taken[3]);
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
      CuteQt3DRender_QAbstractRayCasterCall4 call = reinterpret_cast<CuteQt3DRender_QAbstractRayCasterCall4>(taken[4]);
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
      CuteQt3DRender_QAbstractRayCasterCall5 call = reinterpret_cast<CuteQt3DRender_QAbstractRayCasterCall5>(taken[5]);
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
      CuteQt3DRender_QAbstractRayCasterCall6 call = reinterpret_cast<CuteQt3DRender_QAbstractRayCasterCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DRender::QAbstractRayCaster::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DRender18QAbstractRayCaster10metaObjectEv(
    const Qt3DRender::QAbstractRayCaster *self) {
  return self->metaObject();
}

//  void *Qt3DRender::QAbstractRayCaster::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DRender18QAbstractRayCaster11qt_metacastEPKc(
    Qt3DRender::QAbstractRayCaster *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DRender::QAbstractRayCaster::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DRender18QAbstractRayCaster11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DRender::QAbstractRayCaster *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DRender::QAbstractRayCaster::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DRender18QAbstractRayCaster2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DRender::QAbstractRayCaster::tr(s, c, n));
}

//  Qt3DRender::QAbstractRayCaster::QAbstractRayCaster(QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DRender::QAbstractRayCaster *ritual_ZN10Qt3DRender18QAbstractRayCasterC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DRender_QAbstractRayCaster(parent);
}

//  Qt3DRender::QAbstractRayCaster::~QAbstractRayCaster()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender18QAbstractRayCasterD1Ev(
    Qt3DRender::QAbstractRayCaster *self) {
  delete self;
}

//  RunMode Qt3DRender::QAbstractRayCaster::runMode() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QAbstractRayCaster::RunMode ritual_ZNK10Qt3DRender18QAbstractRayCaster7runModeEv(
    const Qt3DRender::QAbstractRayCaster *self) {
  return self->runMode();
}

//  FilterMode Qt3DRender::QAbstractRayCaster::filterMode() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QAbstractRayCaster::FilterMode ritual_ZNK10Qt3DRender18QAbstractRayCaster10filterModeEv(
    const Qt3DRender::QAbstractRayCaster *self) {
  return self->filterMode();
}

//  Hits Qt3DRender::QAbstractRayCaster::hits() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QAbstractRayCaster::Hits *ritual_ZNK10Qt3DRender18QAbstractRayCaster4hitsEv(
    const Qt3DRender::QAbstractRayCaster *self) {
  return new Qt3DRender::QAbstractRayCaster::Hits(self->hits());
}

//  void Qt3DRender::QAbstractRayCaster::addLayer(QLayer *layer)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender18QAbstractRayCaster8addLayerEPNS_6QLayerE(
    Qt3DRender::QAbstractRayCaster *self,
    Qt3DRender::QLayer *layer) {
  self->addLayer(layer);
}

//  void Qt3DRender::QAbstractRayCaster::removeLayer(QLayer *layer)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender18QAbstractRayCaster11removeLayerEPNS_6QLayerE(
    Qt3DRender::QAbstractRayCaster *self,
    Qt3DRender::QLayer *layer) {
  self->removeLayer(layer);
}

//  QList<QLayer *> Qt3DRender::QAbstractRayCaster::layers() const
extern "C" Q_DECL_EXPORT
QList<Qt3DRender::QLayer *> *ritual_ZNK10Qt3DRender18QAbstractRayCaster6layersEv(
    const Qt3DRender::QAbstractRayCaster *self) {
  return new QList<Qt3DRender::QLayer *>(self->layers());
}

//  void Qt3DRender::QAbstractRayCaster::setRunMode(RunMode runMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender18QAbstractRayCaster10setRunModeENS0_7RunModeE(
    Qt3DRender::QAbstractRayCaster *self,
    Qt3DRender::QAbstractRayCaster::RunMode runMode) {
  self->setRunMode(runMode);
}

//  void Qt3DRender::QAbstractRayCaster::setFilterMode(FilterMode filterMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender18QAbstractRayCaster13setFilterModeENS0_10FilterModeE(
    Qt3DRender::QAbstractRayCaster *self,
    Qt3DRender::QAbstractRayCaster::FilterMode filterMode) {
  self->setFilterMode(filterMode);
}

//  void Qt3DRender::QAbstractRayCaster::runModeChanged(Qt3DRender::QAbstract
//      RayCaster::RunMode runMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender18QAbstractRayCaster14runModeChangedENS0_7RunModeE(
    Qt3DRender::QAbstractRayCaster *self,
    Qt3DRender::QAbstractRayCaster::RunMode runMode) {
  self->runModeChanged(runMode);
}

//  void Qt3DRender::QAbstractRayCaster::hitsChanged(const
//      Qt3DRender::QAbstractRayCaster::Hits &hits)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender18QAbstractRayCaster11hitsChangedERK5QListINS_13QRayCasterHitEE(
    Qt3DRender::QAbstractRayCaster *self,
    const Qt3DRender::QAbstractRayCaster::Hits *hits) {
  self->hitsChanged(*hits);
}

//  void Qt3DRender::QAbstractRayCaster::filterModeChanged(Qt3DRender::QAbstr
//      actRayCaster::FilterMode filterMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender18QAbstractRayCaster17filterModeChangedENS0_10FilterModeE(
    Qt3DRender::QAbstractRayCaster *self,
    Qt3DRender::QAbstractRayCaster::FilterMode filterMode) {
  self->filterModeChanged(filterMode);
}

//  Qt3DRender::QAbstractRayCaster::QAbstractRayCaster(QAbstractRayCasterPriv
//      ate &dd, QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DRender::QAbstractRayCaster *ritual_ZN10Qt3DRender18QAbstractRayCasterC1ERNS_25QAbstractRayCasterPrivateEPN8Qt3DCore5QNodeE(
    Qt3DRender::QAbstractRayCasterPrivate *dd,
    Qt3DCore::QNode *parent) {
  return new CuteQt3DRender_QAbstractRayCaster(*dd, parent);
}

//  QAbstractRayCasterPrivate *Qt3DRender::QAbstractRayCaster::d_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::QAbstractRayCasterPrivate *ritual_ZN10Qt3DRender18QAbstractRayCaster6d_funcEv(
    Qt3DRender::QAbstractRayCaster *self) {
  return self->d_func();
}

//  const QAbstractRayCasterPrivate *Qt3DRender::QAbstractRayCaster::d_func()
//      const
extern "C" Q_DECL_EXPORT
const Qt3DRender::QAbstractRayCasterPrivate *ritual_ZNK10Qt3DRender18QAbstractRayCaster6d_funcEv(
    const Qt3DRender::QAbstractRayCaster *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DRender_QAbstractRayCaster, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_QAbstractRayCaster(
    Qt3DRender::QAbstractRayCaster *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_QAbstractRayCaster *>(self)->take(key, call);
}

//  a Qt3DRender::QAbstractRayCaster::Hits a ritual of
//      Qt3DRender::QAbstractRayCaster gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DRender_QAbstractRayCaster__Qt3DRender_QAbstractRayCaster_Hits(
    Qt3DRender::QAbstractRayCaster::Hits *self) {
  delete self;
}

//  a QList<Qt3DRender::QLayer *> a ritual of Qt3DRender::QAbstractRayCaster
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DRender_QAbstractRayCaster__QList_Qt3DRender_QLayer(
    QList<Qt3DRender::QLayer *> *self) {
  delete self;
}
