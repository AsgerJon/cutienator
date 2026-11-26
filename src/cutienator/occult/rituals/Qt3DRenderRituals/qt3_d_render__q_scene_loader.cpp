//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/qsceneloader.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DRender/qsceneloader.h>
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A Qt3DRender::QSceneLoader that Python can take functions over in. Every Qt3DRender::QSceneLoader
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QSceneLoaderCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QSceneLoaderCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QSceneLoaderCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QSceneLoaderCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QSceneLoaderCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QSceneLoaderCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QSceneLoaderCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DRender_QSceneLoader : public Qt3DRender::QSceneLoader {
public:
  using Qt3DRender::QSceneLoader::QSceneLoader;
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
      CuteQt3DRender_QSceneLoaderCall0 call = reinterpret_cast<CuteQt3DRender_QSceneLoaderCall0>(taken[0]);
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
      CuteQt3DRender_QSceneLoaderCall1 call = reinterpret_cast<CuteQt3DRender_QSceneLoaderCall1>(taken[1]);
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
      CuteQt3DRender_QSceneLoaderCall2 call = reinterpret_cast<CuteQt3DRender_QSceneLoaderCall2>(taken[2]);
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
      CuteQt3DRender_QSceneLoaderCall3 call = reinterpret_cast<CuteQt3DRender_QSceneLoaderCall3>(taken[3]);
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
      CuteQt3DRender_QSceneLoaderCall4 call = reinterpret_cast<CuteQt3DRender_QSceneLoaderCall4>(taken[4]);
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
      CuteQt3DRender_QSceneLoaderCall5 call = reinterpret_cast<CuteQt3DRender_QSceneLoaderCall5>(taken[5]);
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
      CuteQt3DRender_QSceneLoaderCall6 call = reinterpret_cast<CuteQt3DRender_QSceneLoaderCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DRender::QSceneLoader::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DRender12QSceneLoader10metaObjectEv(
    const Qt3DRender::QSceneLoader *self) {
  return self->metaObject();
}

//  void *Qt3DRender::QSceneLoader::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DRender12QSceneLoader11qt_metacastEPKc(
    Qt3DRender::QSceneLoader *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DRender::QSceneLoader::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DRender12QSceneLoader11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DRender::QSceneLoader *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DRender::QSceneLoader::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DRender12QSceneLoader2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DRender::QSceneLoader::tr(s, c, n));
}

//  Qt3DRender::QSceneLoader::QSceneLoader(Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DRender::QSceneLoader *ritual_ZN10Qt3DRender12QSceneLoaderC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DRender_QSceneLoader(parent);
}

//  Qt3DRender::QSceneLoader::~QSceneLoader()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender12QSceneLoaderD1Ev(
    Qt3DRender::QSceneLoader *self) {
  delete self;
}

//  QUrl Qt3DRender::QSceneLoader::source() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK10Qt3DRender12QSceneLoader6sourceEv(
    const Qt3DRender::QSceneLoader *self) {
  return new QUrl(self->source());
}

//  Status Qt3DRender::QSceneLoader::status() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QSceneLoader::Status ritual_ZNK10Qt3DRender12QSceneLoader6statusEv(
    const Qt3DRender::QSceneLoader *self) {
  return self->status();
}

//  Qt3DCore::QEntity *Qt3DRender::QSceneLoader::entity(const QString
//      &entityName) const
extern "C" Q_DECL_EXPORT
Qt3DCore::QEntity *ritual_ZNK10Qt3DRender12QSceneLoader6entityERK7QString(
    const Qt3DRender::QSceneLoader *self,
    const QString *entityName) {
  return self->entity(*entityName);
}

//  QStringList Qt3DRender::QSceneLoader::entityNames() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK10Qt3DRender12QSceneLoader11entityNamesEv(
    const Qt3DRender::QSceneLoader *self) {
  return new QList<QString>(self->entityNames());
}

//  Qt3DCore::QComponent *Qt3DRender::QSceneLoader::component(const QString
//      &entityName, ComponentType componentType) const
extern "C" Q_DECL_EXPORT
Qt3DCore::QComponent *ritual_ZNK10Qt3DRender12QSceneLoader9componentERK7QStringNS0_13ComponentTypeE(
    const Qt3DRender::QSceneLoader *self,
    const QString *entityName,
    Qt3DRender::QSceneLoader::ComponentType componentType) {
  return self->component(*entityName, componentType);
}

//  void Qt3DRender::QSceneLoader::setSource(const QUrl &arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender12QSceneLoader9setSourceERK4QUrl(
    Qt3DRender::QSceneLoader *self,
    const QUrl *arg) {
  self->setSource(*arg);
}

//  void Qt3DRender::QSceneLoader::sourceChanged(const QUrl &source)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender12QSceneLoader13sourceChangedERK4QUrl(
    Qt3DRender::QSceneLoader *self,
    const QUrl *source) {
  self->sourceChanged(*source);
}

//  void Qt3DRender::QSceneLoader::statusChanged(Status status)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender12QSceneLoader13statusChangedENS0_6StatusE(
    Qt3DRender::QSceneLoader *self,
    Qt3DRender::QSceneLoader::Status status) {
  self->statusChanged(status);
}

//  Qt3DRender::QSceneLoader::QSceneLoader(QSceneLoaderPrivate &dd,
//      Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DRender::QSceneLoader *ritual_ZN10Qt3DRender12QSceneLoaderC1ERNS_19QSceneLoaderPrivateEPN8Qt3DCore5QNodeE(
    Qt3DRender::QSceneLoaderPrivate *dd,
    Qt3DCore::QNode *parent) {
  return new CuteQt3DRender_QSceneLoader(*dd, parent);
}

//  QSceneLoaderPrivate *Qt3DRender::QSceneLoader::d_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::QSceneLoaderPrivate *ritual_ZN10Qt3DRender12QSceneLoader6d_funcEv(
    Qt3DRender::QSceneLoader *self) {
  return self->d_func();
}

//  const QSceneLoaderPrivate *Qt3DRender::QSceneLoader::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DRender::QSceneLoaderPrivate *ritual_ZNK10Qt3DRender12QSceneLoader6d_funcEv(
    const Qt3DRender::QSceneLoader *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DRender_QSceneLoader, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_QSceneLoader(
    Qt3DRender::QSceneLoader *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_QSceneLoader *>(self)->take(key, call);
}
