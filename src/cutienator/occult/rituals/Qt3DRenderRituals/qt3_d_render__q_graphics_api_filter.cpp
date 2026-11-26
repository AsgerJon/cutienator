//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/qgraphicsapifilter.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DRender/qgraphicsapifilter.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A Qt3DRender::QGraphicsApiFilter that Python can take functions over in. Every Qt3DRender::QGraphicsApiFilter
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QGraphicsApiFilterCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QGraphicsApiFilterCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QGraphicsApiFilterCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QGraphicsApiFilterCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QGraphicsApiFilterCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QGraphicsApiFilterCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QGraphicsApiFilterCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DRender_QGraphicsApiFilter : public Qt3DRender::QGraphicsApiFilter {
public:
  using Qt3DRender::QGraphicsApiFilter::QGraphicsApiFilter;
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
      CuteQt3DRender_QGraphicsApiFilterCall0 call = reinterpret_cast<CuteQt3DRender_QGraphicsApiFilterCall0>(taken[0]);
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
      CuteQt3DRender_QGraphicsApiFilterCall1 call = reinterpret_cast<CuteQt3DRender_QGraphicsApiFilterCall1>(taken[1]);
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
      CuteQt3DRender_QGraphicsApiFilterCall2 call = reinterpret_cast<CuteQt3DRender_QGraphicsApiFilterCall2>(taken[2]);
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
      CuteQt3DRender_QGraphicsApiFilterCall3 call = reinterpret_cast<CuteQt3DRender_QGraphicsApiFilterCall3>(taken[3]);
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
      CuteQt3DRender_QGraphicsApiFilterCall4 call = reinterpret_cast<CuteQt3DRender_QGraphicsApiFilterCall4>(taken[4]);
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
      CuteQt3DRender_QGraphicsApiFilterCall5 call = reinterpret_cast<CuteQt3DRender_QGraphicsApiFilterCall5>(taken[5]);
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
      CuteQt3DRender_QGraphicsApiFilterCall6 call = reinterpret_cast<CuteQt3DRender_QGraphicsApiFilterCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DRender::QGraphicsApiFilter::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DRender18QGraphicsApiFilter10metaObjectEv(
    const Qt3DRender::QGraphicsApiFilter *self) {
  return self->metaObject();
}

//  void *Qt3DRender::QGraphicsApiFilter::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DRender18QGraphicsApiFilter11qt_metacastEPKc(
    Qt3DRender::QGraphicsApiFilter *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DRender::QGraphicsApiFilter::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DRender18QGraphicsApiFilter11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DRender::QGraphicsApiFilter *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DRender::QGraphicsApiFilter::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DRender18QGraphicsApiFilter2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DRender::QGraphicsApiFilter::tr(s, c, n));
}

//  Qt3DRender::QGraphicsApiFilter::QGraphicsApiFilter(QObject *parent)
extern "C" Q_DECL_EXPORT
Qt3DRender::QGraphicsApiFilter *ritual_ZN10Qt3DRender18QGraphicsApiFilterC1EP7QObject(
    QObject *parent) {
  return new CuteQt3DRender_QGraphicsApiFilter(parent);
}

//  Qt3DRender::QGraphicsApiFilter::~QGraphicsApiFilter()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender18QGraphicsApiFilterD1Ev(
    Qt3DRender::QGraphicsApiFilter *self) {
  delete self;
}

//  Api Qt3DRender::QGraphicsApiFilter::api() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QGraphicsApiFilter::Api ritual_ZNK10Qt3DRender18QGraphicsApiFilter3apiEv(
    const Qt3DRender::QGraphicsApiFilter *self) {
  return self->api();
}

//  OpenGLProfile Qt3DRender::QGraphicsApiFilter::profile() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QGraphicsApiFilter::OpenGLProfile ritual_ZNK10Qt3DRender18QGraphicsApiFilter7profileEv(
    const Qt3DRender::QGraphicsApiFilter *self) {
  return self->profile();
}

//  int Qt3DRender::QGraphicsApiFilter::minorVersion() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender18QGraphicsApiFilter12minorVersionEv(
    const Qt3DRender::QGraphicsApiFilter *self) {
  return self->minorVersion();
}

//  int Qt3DRender::QGraphicsApiFilter::majorVersion() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender18QGraphicsApiFilter12majorVersionEv(
    const Qt3DRender::QGraphicsApiFilter *self) {
  return self->majorVersion();
}

//  QStringList Qt3DRender::QGraphicsApiFilter::extensions() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK10Qt3DRender18QGraphicsApiFilter10extensionsEv(
    const Qt3DRender::QGraphicsApiFilter *self) {
  return new QList<QString>(self->extensions());
}

//  QString Qt3DRender::QGraphicsApiFilter::vendor() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10Qt3DRender18QGraphicsApiFilter6vendorEv(
    const Qt3DRender::QGraphicsApiFilter *self) {
  return new QString(self->vendor());
}

//  void Qt3DRender::QGraphicsApiFilter::setApi(Api api)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender18QGraphicsApiFilter6setApiENS0_3ApiE(
    Qt3DRender::QGraphicsApiFilter *self,
    Qt3DRender::QGraphicsApiFilter::Api api) {
  self->setApi(api);
}

//  void Qt3DRender::QGraphicsApiFilter::setProfile(OpenGLProfile profile)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender18QGraphicsApiFilter10setProfileENS0_13OpenGLProfileE(
    Qt3DRender::QGraphicsApiFilter *self,
    Qt3DRender::QGraphicsApiFilter::OpenGLProfile profile) {
  self->setProfile(profile);
}

//  void Qt3DRender::QGraphicsApiFilter::setMinorVersion(int minorVersion)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender18QGraphicsApiFilter15setMinorVersionEi(
    Qt3DRender::QGraphicsApiFilter *self,
    int minorVersion) {
  self->setMinorVersion(minorVersion);
}

//  void Qt3DRender::QGraphicsApiFilter::setMajorVersion(int majorVersion)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender18QGraphicsApiFilter15setMajorVersionEi(
    Qt3DRender::QGraphicsApiFilter *self,
    int majorVersion) {
  self->setMajorVersion(majorVersion);
}

//  void Qt3DRender::QGraphicsApiFilter::setExtensions(const QStringList
//      &extensions)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender18QGraphicsApiFilter13setExtensionsERK5QListI7QStringE(
    Qt3DRender::QGraphicsApiFilter *self,
    const QList<QString> *extensions) {
  self->setExtensions(*extensions);
}

//  void Qt3DRender::QGraphicsApiFilter::setVendor(const QString &vendor)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender18QGraphicsApiFilter9setVendorERK7QString(
    Qt3DRender::QGraphicsApiFilter *self,
    const QString *vendor) {
  self->setVendor(*vendor);
}

//  void Qt3DRender::QGraphicsApiFilter::apiChanged(Qt3DRender::QGraphicsApiF
//      ilter::Api api)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender18QGraphicsApiFilter10apiChangedENS0_3ApiE(
    Qt3DRender::QGraphicsApiFilter *self,
    Qt3DRender::QGraphicsApiFilter::Api api) {
  self->apiChanged(api);
}

//  void Qt3DRender::QGraphicsApiFilter::profileChanged(Qt3DRender::QGraphics
//      ApiFilter::OpenGLProfile profile)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender18QGraphicsApiFilter14profileChangedENS0_13OpenGLProfileE(
    Qt3DRender::QGraphicsApiFilter *self,
    Qt3DRender::QGraphicsApiFilter::OpenGLProfile profile) {
  self->profileChanged(profile);
}

//  void Qt3DRender::QGraphicsApiFilter::minorVersionChanged(int
//      minorVersion)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender18QGraphicsApiFilter19minorVersionChangedEi(
    Qt3DRender::QGraphicsApiFilter *self,
    int minorVersion) {
  self->minorVersionChanged(minorVersion);
}

//  void Qt3DRender::QGraphicsApiFilter::majorVersionChanged(int
//      majorVersion)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender18QGraphicsApiFilter19majorVersionChangedEi(
    Qt3DRender::QGraphicsApiFilter *self,
    int majorVersion) {
  self->majorVersionChanged(majorVersion);
}

//  void Qt3DRender::QGraphicsApiFilter::extensionsChanged(const QStringList
//      &extensions)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender18QGraphicsApiFilter17extensionsChangedERK5QListI7QStringE(
    Qt3DRender::QGraphicsApiFilter *self,
    const QList<QString> *extensions) {
  self->extensionsChanged(*extensions);
}

//  void Qt3DRender::QGraphicsApiFilter::vendorChanged(const QString &vendor)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender18QGraphicsApiFilter13vendorChangedERK7QString(
    Qt3DRender::QGraphicsApiFilter *self,
    const QString *vendor) {
  self->vendorChanged(*vendor);
}

//  void Qt3DRender::QGraphicsApiFilter::graphicsApiFilterChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender18QGraphicsApiFilter24graphicsApiFilterChangedEv(
    Qt3DRender::QGraphicsApiFilter *self) {
  self->graphicsApiFilterChanged();
}

//  QGraphicsApiFilterPrivate *Qt3DRender::QGraphicsApiFilter::d_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::QGraphicsApiFilterPrivate *ritual_ZN10Qt3DRender18QGraphicsApiFilter6d_funcEv(
    Qt3DRender::QGraphicsApiFilter *self) {
  return self->d_func();
}

//  const QGraphicsApiFilterPrivate *Qt3DRender::QGraphicsApiFilter::d_func()
//      const
extern "C" Q_DECL_EXPORT
const Qt3DRender::QGraphicsApiFilterPrivate *ritual_ZNK10Qt3DRender18QGraphicsApiFilter6d_funcEv(
    const Qt3DRender::QGraphicsApiFilter *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DRender_QGraphicsApiFilter, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_QGraphicsApiFilter(
    Qt3DRender::QGraphicsApiFilter *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_QGraphicsApiFilter *>(self)->take(key, call);
}
