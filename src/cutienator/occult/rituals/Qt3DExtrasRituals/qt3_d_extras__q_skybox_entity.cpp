//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DExtras/qskyboxentity.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DExtras/qskyboxentity.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DExtras::QSkyboxEntity that Python can take functions over in. Every Qt3DExtras::QSkyboxEntity
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DExtras_QSkyboxEntityCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DExtras_QSkyboxEntityCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QSkyboxEntityCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QSkyboxEntityCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QSkyboxEntityCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QSkyboxEntityCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QSkyboxEntityCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DExtras_QSkyboxEntity : public Qt3DExtras::QSkyboxEntity {
public:
  using Qt3DExtras::QSkyboxEntity::QSkyboxEntity;
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
      CuteQt3DExtras_QSkyboxEntityCall0 call = reinterpret_cast<CuteQt3DExtras_QSkyboxEntityCall0>(taken[0]);
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
      CuteQt3DExtras_QSkyboxEntityCall1 call = reinterpret_cast<CuteQt3DExtras_QSkyboxEntityCall1>(taken[1]);
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
      CuteQt3DExtras_QSkyboxEntityCall2 call = reinterpret_cast<CuteQt3DExtras_QSkyboxEntityCall2>(taken[2]);
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
      CuteQt3DExtras_QSkyboxEntityCall3 call = reinterpret_cast<CuteQt3DExtras_QSkyboxEntityCall3>(taken[3]);
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
      CuteQt3DExtras_QSkyboxEntityCall4 call = reinterpret_cast<CuteQt3DExtras_QSkyboxEntityCall4>(taken[4]);
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
      CuteQt3DExtras_QSkyboxEntityCall5 call = reinterpret_cast<CuteQt3DExtras_QSkyboxEntityCall5>(taken[5]);
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
      CuteQt3DExtras_QSkyboxEntityCall6 call = reinterpret_cast<CuteQt3DExtras_QSkyboxEntityCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DExtras::QSkyboxEntity::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DExtras13QSkyboxEntity10metaObjectEv(
    const Qt3DExtras::QSkyboxEntity *self) {
  return self->metaObject();
}

//  void *Qt3DExtras::QSkyboxEntity::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DExtras13QSkyboxEntity11qt_metacastEPKc(
    Qt3DExtras::QSkyboxEntity *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DExtras::QSkyboxEntity::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DExtras13QSkyboxEntity11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DExtras::QSkyboxEntity *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DExtras::QSkyboxEntity::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DExtras13QSkyboxEntity2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DExtras::QSkyboxEntity::tr(s, c, n));
}

//  Qt3DExtras::QSkyboxEntity::QSkyboxEntity(Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DExtras::QSkyboxEntity *ritual_ZN10Qt3DExtras13QSkyboxEntityC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DExtras_QSkyboxEntity(parent);
}

//  Qt3DExtras::QSkyboxEntity::~QSkyboxEntity()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras13QSkyboxEntityD1Ev(
    Qt3DExtras::QSkyboxEntity *self) {
  delete self;
}

//  QString Qt3DExtras::QSkyboxEntity::baseName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10Qt3DExtras13QSkyboxEntity8baseNameEv(
    const Qt3DExtras::QSkyboxEntity *self) {
  return new QString(self->baseName());
}

//  QString Qt3DExtras::QSkyboxEntity::extension() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10Qt3DExtras13QSkyboxEntity9extensionEv(
    const Qt3DExtras::QSkyboxEntity *self) {
  return new QString(self->extension());
}

//  bool Qt3DExtras::QSkyboxEntity::isGammaCorrectEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DExtras13QSkyboxEntity21isGammaCorrectEnabledEv(
    const Qt3DExtras::QSkyboxEntity *self) {
  return self->isGammaCorrectEnabled();
}

//  void Qt3DExtras::QSkyboxEntity::setBaseName(const QString &path)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras13QSkyboxEntity11setBaseNameERK7QString(
    Qt3DExtras::QSkyboxEntity *self,
    const QString *path) {
  self->setBaseName(*path);
}

//  void Qt3DExtras::QSkyboxEntity::setExtension(const QString &extension)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras13QSkyboxEntity12setExtensionERK7QString(
    Qt3DExtras::QSkyboxEntity *self,
    const QString *extension) {
  self->setExtension(*extension);
}

//  void Qt3DExtras::QSkyboxEntity::setGammaCorrectEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras13QSkyboxEntity22setGammaCorrectEnabledEb(
    Qt3DExtras::QSkyboxEntity *self,
    bool enabled) {
  self->setGammaCorrectEnabled(enabled);
}

//  void Qt3DExtras::QSkyboxEntity::baseNameChanged(const QString &path)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras13QSkyboxEntity15baseNameChangedERK7QString(
    Qt3DExtras::QSkyboxEntity *self,
    const QString *path) {
  self->baseNameChanged(*path);
}

//  void Qt3DExtras::QSkyboxEntity::extensionChanged(const QString
//      &extension)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras13QSkyboxEntity16extensionChangedERK7QString(
    Qt3DExtras::QSkyboxEntity *self,
    const QString *extension) {
  self->extensionChanged(*extension);
}

//  void Qt3DExtras::QSkyboxEntity::gammaCorrectEnabledChanged(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras13QSkyboxEntity26gammaCorrectEnabledChangedEb(
    Qt3DExtras::QSkyboxEntity *self,
    bool enabled) {
  self->gammaCorrectEnabledChanged(enabled);
}

//  QSkyboxEntityPrivate *Qt3DExtras::QSkyboxEntity::d_func()
extern "C" Q_DECL_EXPORT
Qt3DExtras::QSkyboxEntityPrivate *ritual_ZN10Qt3DExtras13QSkyboxEntity6d_funcEv(
    Qt3DExtras::QSkyboxEntity *self) {
  return self->d_func();
}

//  const QSkyboxEntityPrivate *Qt3DExtras::QSkyboxEntity::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DExtras::QSkyboxEntityPrivate *ritual_ZNK10Qt3DExtras13QSkyboxEntity6d_funcEv(
    const Qt3DExtras::QSkyboxEntity *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DExtras_QSkyboxEntity, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DExtras_QSkyboxEntity(
    Qt3DExtras::QSkyboxEntity *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DExtras_QSkyboxEntity *>(self)->take(key, call);
}
