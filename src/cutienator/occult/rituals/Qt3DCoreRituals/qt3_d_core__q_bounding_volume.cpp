//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DCore/qboundingvolume.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DCore/qboundingvolume.h>
#include <QtCore/qstring.h>
#include <QtGui/qvectornd.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DCore::QBoundingVolume that Python can take functions over in. Every Qt3DCore::QBoundingVolume
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DCore_QBoundingVolumeCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DCore_QBoundingVolumeCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_QBoundingVolumeCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_QBoundingVolumeCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_QBoundingVolumeCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_QBoundingVolumeCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_QBoundingVolumeCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DCore_QBoundingVolume : public Qt3DCore::QBoundingVolume {
public:
  using Qt3DCore::QBoundingVolume::QBoundingVolume;
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
      CuteQt3DCore_QBoundingVolumeCall0 call = reinterpret_cast<CuteQt3DCore_QBoundingVolumeCall0>(taken[0]);
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
      CuteQt3DCore_QBoundingVolumeCall1 call = reinterpret_cast<CuteQt3DCore_QBoundingVolumeCall1>(taken[1]);
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
      CuteQt3DCore_QBoundingVolumeCall2 call = reinterpret_cast<CuteQt3DCore_QBoundingVolumeCall2>(taken[2]);
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
      CuteQt3DCore_QBoundingVolumeCall3 call = reinterpret_cast<CuteQt3DCore_QBoundingVolumeCall3>(taken[3]);
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
      CuteQt3DCore_QBoundingVolumeCall4 call = reinterpret_cast<CuteQt3DCore_QBoundingVolumeCall4>(taken[4]);
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
      CuteQt3DCore_QBoundingVolumeCall5 call = reinterpret_cast<CuteQt3DCore_QBoundingVolumeCall5>(taken[5]);
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
      CuteQt3DCore_QBoundingVolumeCall6 call = reinterpret_cast<CuteQt3DCore_QBoundingVolumeCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DCore::QBoundingVolume::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK8Qt3DCore15QBoundingVolume10metaObjectEv(
    const Qt3DCore::QBoundingVolume *self) {
  return self->metaObject();
}

//  void *Qt3DCore::QBoundingVolume::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN8Qt3DCore15QBoundingVolume11qt_metacastEPKc(
    Qt3DCore::QBoundingVolume *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DCore::QBoundingVolume::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN8Qt3DCore15QBoundingVolume11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DCore::QBoundingVolume *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DCore::QBoundingVolume::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN8Qt3DCore15QBoundingVolume2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DCore::QBoundingVolume::tr(s, c, n));
}

//  Qt3DCore::QBoundingVolume::QBoundingVolume(Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DCore::QBoundingVolume *ritual_ZN8Qt3DCore15QBoundingVolumeC1EPNS_5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DCore_QBoundingVolume(parent);
}

//  Qt3DCore::QBoundingVolume::~QBoundingVolume()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore15QBoundingVolumeD1Ev(
    Qt3DCore::QBoundingVolume *self) {
  delete self;
}

//  QGeometryView *Qt3DCore::QBoundingVolume::view() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QGeometryView *ritual_ZNK8Qt3DCore15QBoundingVolume4viewEv(
    const Qt3DCore::QBoundingVolume *self) {
  return self->view();
}

//  QVector3D Qt3DCore::QBoundingVolume::implicitMinPoint() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK8Qt3DCore15QBoundingVolume16implicitMinPointEv(
    const Qt3DCore::QBoundingVolume *self) {
  return new QVector3D(self->implicitMinPoint());
}

//  QVector3D Qt3DCore::QBoundingVolume::implicitMaxPoint() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK8Qt3DCore15QBoundingVolume16implicitMaxPointEv(
    const Qt3DCore::QBoundingVolume *self) {
  return new QVector3D(self->implicitMaxPoint());
}

//  bool Qt3DCore::QBoundingVolume::areImplicitPointsValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8Qt3DCore15QBoundingVolume22areImplicitPointsValidEv(
    const Qt3DCore::QBoundingVolume *self) {
  return self->areImplicitPointsValid();
}

//  QVector3D Qt3DCore::QBoundingVolume::minPoint() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK8Qt3DCore15QBoundingVolume8minPointEv(
    const Qt3DCore::QBoundingVolume *self) {
  return new QVector3D(self->minPoint());
}

//  QVector3D Qt3DCore::QBoundingVolume::maxPoint() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK8Qt3DCore15QBoundingVolume8maxPointEv(
    const Qt3DCore::QBoundingVolume *self) {
  return new QVector3D(self->maxPoint());
}

//  void Qt3DCore::QBoundingVolume::setView(QGeometryView *view)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore15QBoundingVolume7setViewEPNS_13QGeometryViewE(
    Qt3DCore::QBoundingVolume *self,
    Qt3DCore::QGeometryView *view) {
  self->setView(view);
}

//  void Qt3DCore::QBoundingVolume::setMinPoint(const QVector3D &minPoint)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore15QBoundingVolume11setMinPointERK9QVector3D(
    Qt3DCore::QBoundingVolume *self,
    const QVector3D *minPoint) {
  self->setMinPoint(*minPoint);
}

//  void Qt3DCore::QBoundingVolume::setMaxPoint(const QVector3D &maxPoint)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore15QBoundingVolume11setMaxPointERK9QVector3D(
    Qt3DCore::QBoundingVolume *self,
    const QVector3D *maxPoint) {
  self->setMaxPoint(*maxPoint);
}

//  bool Qt3DCore::QBoundingVolume::updateImplicitBounds()
extern "C" Q_DECL_EXPORT
bool ritual_ZN8Qt3DCore15QBoundingVolume20updateImplicitBoundsEv(
    Qt3DCore::QBoundingVolume *self) {
  return self->updateImplicitBounds();
}

//  void Qt3DCore::QBoundingVolume::viewChanged(QGeometryView *view)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore15QBoundingVolume11viewChangedEPNS_13QGeometryViewE(
    Qt3DCore::QBoundingVolume *self,
    Qt3DCore::QGeometryView *view) {
  self->viewChanged(view);
}

//  void Qt3DCore::QBoundingVolume::implicitMinPointChanged(const QVector3D
//      &implicitMinPoint)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore15QBoundingVolume23implicitMinPointChangedERK9QVector3D(
    Qt3DCore::QBoundingVolume *self,
    const QVector3D *implicitMinPoint) {
  self->implicitMinPointChanged(*implicitMinPoint);
}

//  void Qt3DCore::QBoundingVolume::implicitMaxPointChanged(const QVector3D
//      &implicitMaxPoint)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore15QBoundingVolume23implicitMaxPointChangedERK9QVector3D(
    Qt3DCore::QBoundingVolume *self,
    const QVector3D *implicitMaxPoint) {
  self->implicitMaxPointChanged(*implicitMaxPoint);
}

//  void Qt3DCore::QBoundingVolume::implicitPointsValidChanged(bool
//      implicitPointsValid)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore15QBoundingVolume26implicitPointsValidChangedEb(
    Qt3DCore::QBoundingVolume *self,
    bool implicitPointsValid) {
  self->implicitPointsValidChanged(implicitPointsValid);
}

//  void Qt3DCore::QBoundingVolume::minPointChanged(QVector3D minPoint)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore15QBoundingVolume15minPointChangedE9QVector3D(
    Qt3DCore::QBoundingVolume *self,
    const QVector3D *minPoint) {
  self->minPointChanged(*minPoint);
}

//  void Qt3DCore::QBoundingVolume::maxPointChanged(QVector3D maxPoint)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore15QBoundingVolume15maxPointChangedE9QVector3D(
    Qt3DCore::QBoundingVolume *self,
    const QVector3D *maxPoint) {
  self->maxPointChanged(*maxPoint);
}

//  Qt3DCore::QBoundingVolume::QBoundingVolume(QBoundingVolumePrivate &dd,
//      Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DCore::QBoundingVolume *ritual_ZN8Qt3DCore15QBoundingVolumeC1ERNS_22QBoundingVolumePrivateEPNS_5QNodeE(
    Qt3DCore::QBoundingVolumePrivate *dd,
    Qt3DCore::QNode *parent) {
  return new CuteQt3DCore_QBoundingVolume(*dd, parent);
}

//  QBoundingVolumePrivate *Qt3DCore::QBoundingVolume::d_func()
extern "C" Q_DECL_EXPORT
Qt3DCore::QBoundingVolumePrivate *ritual_ZN8Qt3DCore15QBoundingVolume6d_funcEv(
    Qt3DCore::QBoundingVolume *self) {
  return self->d_func();
}

//  const QBoundingVolumePrivate *Qt3DCore::QBoundingVolume::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DCore::QBoundingVolumePrivate *ritual_ZNK8Qt3DCore15QBoundingVolume6d_funcEv(
    const Qt3DCore::QBoundingVolume *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DCore_QBoundingVolume, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DCore_QBoundingVolume(
    Qt3DCore::QBoundingVolume *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DCore_QBoundingVolume *>(self)->take(key, call);
}
