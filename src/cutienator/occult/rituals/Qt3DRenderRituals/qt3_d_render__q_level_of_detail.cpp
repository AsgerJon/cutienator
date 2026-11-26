//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/qlevelofdetail.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DRender/qlevelofdetail.h>
#include <QtCore/qstring.h>
#include <Qt3DRender/qlevelofdetailboundingsphere.h>
#include <QtGui/qvectornd.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <QtCore/QList>

//  A Qt3DRender::QLevelOfDetail that Python can take functions over in. Every Qt3DRender::QLevelOfDetail
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QLevelOfDetailCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QLevelOfDetailCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QLevelOfDetailCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QLevelOfDetailCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QLevelOfDetailCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QLevelOfDetailCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QLevelOfDetailCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DRender_QLevelOfDetail : public Qt3DRender::QLevelOfDetail {
public:
  using Qt3DRender::QLevelOfDetail::QLevelOfDetail;
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
      CuteQt3DRender_QLevelOfDetailCall0 call = reinterpret_cast<CuteQt3DRender_QLevelOfDetailCall0>(taken[0]);
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
      CuteQt3DRender_QLevelOfDetailCall1 call = reinterpret_cast<CuteQt3DRender_QLevelOfDetailCall1>(taken[1]);
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
      CuteQt3DRender_QLevelOfDetailCall2 call = reinterpret_cast<CuteQt3DRender_QLevelOfDetailCall2>(taken[2]);
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
      CuteQt3DRender_QLevelOfDetailCall3 call = reinterpret_cast<CuteQt3DRender_QLevelOfDetailCall3>(taken[3]);
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
      CuteQt3DRender_QLevelOfDetailCall4 call = reinterpret_cast<CuteQt3DRender_QLevelOfDetailCall4>(taken[4]);
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
      CuteQt3DRender_QLevelOfDetailCall5 call = reinterpret_cast<CuteQt3DRender_QLevelOfDetailCall5>(taken[5]);
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
      CuteQt3DRender_QLevelOfDetailCall6 call = reinterpret_cast<CuteQt3DRender_QLevelOfDetailCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DRender::QLevelOfDetail::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DRender14QLevelOfDetail10metaObjectEv(
    const Qt3DRender::QLevelOfDetail *self) {
  return self->metaObject();
}

//  void *Qt3DRender::QLevelOfDetail::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DRender14QLevelOfDetail11qt_metacastEPKc(
    Qt3DRender::QLevelOfDetail *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DRender::QLevelOfDetail::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DRender14QLevelOfDetail11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DRender::QLevelOfDetail *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DRender::QLevelOfDetail::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DRender14QLevelOfDetail2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DRender::QLevelOfDetail::tr(s, c, n));
}

//  Qt3DRender::QLevelOfDetail::QLevelOfDetail(Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DRender::QLevelOfDetail *ritual_ZN10Qt3DRender14QLevelOfDetailC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DRender_QLevelOfDetail(parent);
}

//  Qt3DRender::QLevelOfDetail::~QLevelOfDetail()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender14QLevelOfDetailD1Ev(
    Qt3DRender::QLevelOfDetail *self) {
  delete self;
}

//  QCamera *Qt3DRender::QLevelOfDetail::camera() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QCamera *ritual_ZNK10Qt3DRender14QLevelOfDetail6cameraEv(
    const Qt3DRender::QLevelOfDetail *self) {
  return self->camera();
}

//  int Qt3DRender::QLevelOfDetail::currentIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender14QLevelOfDetail12currentIndexEv(
    const Qt3DRender::QLevelOfDetail *self) {
  return self->currentIndex();
}

//  ThresholdType Qt3DRender::QLevelOfDetail::thresholdType() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QLevelOfDetail::ThresholdType ritual_ZNK10Qt3DRender14QLevelOfDetail13thresholdTypeEv(
    const Qt3DRender::QLevelOfDetail *self) {
  return self->thresholdType();
}

//  QList<qreal> Qt3DRender::QLevelOfDetail::thresholds() const
extern "C" Q_DECL_EXPORT
QList<qreal> *ritual_ZNK10Qt3DRender14QLevelOfDetail10thresholdsEv(
    const Qt3DRender::QLevelOfDetail *self) {
  return new QList<qreal>(self->thresholds());
}

//  QLevelOfDetailBoundingSphere Qt3DRender::QLevelOfDetail::volumeOverride()
//      const
extern "C" Q_DECL_EXPORT
Qt3DRender::QLevelOfDetailBoundingSphere *ritual_ZNK10Qt3DRender14QLevelOfDetail14volumeOverrideEv(
    const Qt3DRender::QLevelOfDetail *self) {
  return new Qt3DRender::QLevelOfDetailBoundingSphere(
      self->volumeOverride());
}

//  Qt3DRender::QLevelOfDetailBoundingSphere
//      Qt3DRender::QLevelOfDetail::createBoundingSphere(const QVector3D
//      &center, float radius)
extern "C" Q_DECL_EXPORT
Qt3DRender::QLevelOfDetailBoundingSphere *ritual_ZN10Qt3DRender14QLevelOfDetail20createBoundingSphereERK9QVector3Df(
    Qt3DRender::QLevelOfDetail *self,
    const QVector3D *center,
    float radius) {
  return new Qt3DRender::QLevelOfDetailBoundingSphere(
      self->createBoundingSphere(
          *center,
          radius));
}

//  void Qt3DRender::QLevelOfDetail::setCamera(QCamera *camera)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender14QLevelOfDetail9setCameraEPNS_7QCameraE(
    Qt3DRender::QLevelOfDetail *self,
    Qt3DRender::QCamera *camera) {
  self->setCamera(camera);
}

//  void Qt3DRender::QLevelOfDetail::setCurrentIndex(int currentIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender14QLevelOfDetail15setCurrentIndexEi(
    Qt3DRender::QLevelOfDetail *self,
    int currentIndex) {
  self->setCurrentIndex(currentIndex);
}

//  void Qt3DRender::QLevelOfDetail::setThresholdType(ThresholdType
//      thresholdType)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender14QLevelOfDetail16setThresholdTypeENS0_13ThresholdTypeE(
    Qt3DRender::QLevelOfDetail *self,
    Qt3DRender::QLevelOfDetail::ThresholdType thresholdType) {
  self->setThresholdType(thresholdType);
}

//  void Qt3DRender::QLevelOfDetail::setThresholds(const QList<qreal>
//      &thresholds)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender14QLevelOfDetail13setThresholdsERK5QListIdE(
    Qt3DRender::QLevelOfDetail *self,
    const QList<qreal> *thresholds) {
  self->setThresholds(*thresholds);
}

//  void Qt3DRender::QLevelOfDetail::setVolumeOverride(const
//      QLevelOfDetailBoundingSphere &volumeOverride)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender14QLevelOfDetail17setVolumeOverrideERKNS_28QLevelOfDetailBoundingSphereE(
    Qt3DRender::QLevelOfDetail *self,
    const Qt3DRender::QLevelOfDetailBoundingSphere *volumeOverride) {
  self->setVolumeOverride(*volumeOverride);
}

//  void Qt3DRender::QLevelOfDetail::cameraChanged(QCamera *camera)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender14QLevelOfDetail13cameraChangedEPNS_7QCameraE(
    Qt3DRender::QLevelOfDetail *self,
    Qt3DRender::QCamera *camera) {
  self->cameraChanged(camera);
}

//  void Qt3DRender::QLevelOfDetail::currentIndexChanged(int currentIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender14QLevelOfDetail19currentIndexChangedEi(
    Qt3DRender::QLevelOfDetail *self,
    int currentIndex) {
  self->currentIndexChanged(currentIndex);
}

//  void Qt3DRender::QLevelOfDetail::thresholdTypeChanged(ThresholdType
//      thresholdType)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender14QLevelOfDetail20thresholdTypeChangedENS0_13ThresholdTypeE(
    Qt3DRender::QLevelOfDetail *self,
    Qt3DRender::QLevelOfDetail::ThresholdType thresholdType) {
  self->thresholdTypeChanged(thresholdType);
}

//  void Qt3DRender::QLevelOfDetail::thresholdsChanged(const QList<qreal>
//      &thresholds)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender14QLevelOfDetail17thresholdsChangedERK5QListIdE(
    Qt3DRender::QLevelOfDetail *self,
    const QList<qreal> *thresholds) {
  self->thresholdsChanged(*thresholds);
}

//  void Qt3DRender::QLevelOfDetail::volumeOverrideChanged(const
//      QLevelOfDetailBoundingSphere &volumeOverride)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender14QLevelOfDetail21volumeOverrideChangedERKNS_28QLevelOfDetailBoundingSphereE(
    Qt3DRender::QLevelOfDetail *self,
    const Qt3DRender::QLevelOfDetailBoundingSphere *volumeOverride) {
  self->volumeOverrideChanged(*volumeOverride);
}

//  Qt3DRender::QLevelOfDetail::QLevelOfDetail(QLevelOfDetailPrivate &dd,
//      Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DRender::QLevelOfDetail *ritual_ZN10Qt3DRender14QLevelOfDetailC1ERNS_21QLevelOfDetailPrivateEPN8Qt3DCore5QNodeE(
    Qt3DRender::QLevelOfDetailPrivate *dd,
    Qt3DCore::QNode *parent) {
  return new CuteQt3DRender_QLevelOfDetail(*dd, parent);
}

//  QLevelOfDetailPrivate *Qt3DRender::QLevelOfDetail::d_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::QLevelOfDetailPrivate *ritual_ZN10Qt3DRender14QLevelOfDetail6d_funcEv(
    Qt3DRender::QLevelOfDetail *self) {
  return self->d_func();
}

//  const QLevelOfDetailPrivate *Qt3DRender::QLevelOfDetail::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DRender::QLevelOfDetailPrivate *ritual_ZNK10Qt3DRender14QLevelOfDetail6d_funcEv(
    const Qt3DRender::QLevelOfDetail *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DRender_QLevelOfDetail, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_QLevelOfDetail(
    Qt3DRender::QLevelOfDetail *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_QLevelOfDetail *>(self)->take(key, call);
}

//  a QList<qreal> a ritual of Qt3DRender::QLevelOfDetail gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DRender_QLevelOfDetail__QList_qreal(QList<qreal> *self) {
  delete self;
}
