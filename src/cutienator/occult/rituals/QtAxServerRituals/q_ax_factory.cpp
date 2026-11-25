//  Written by hand on 2026-11-25 from
//  QtAxServer/qaxfactory.h, Qt 6.12.0, from Qt's source. Kept as it
//  is when the generator runs again.
//  Qt builds ActiveQt for Windows only. AxServer is a static library,
//  all of it compiled into ours, so the class is taken as exported.
//  The class has no Q_OBJECT: no 'metaObject()' and no 'tr' of its
//  own; its 'metaObject' takes a key.
//  Not written: the constructor, as the class is abstract
//  ('featureList', 'createObject' and 'metaObject' are pure);
//  'featureList', giving a 'QStringList', a QList; the class
//  template 'QAxClass' and the macros of the same header.
#include <QtCore/qglobal.h>
#if defined(Q_OS_WIN)
#include <QtAxServer/qaxfactory.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qsettings.h>
#include <QtCore/qstring.h>
#include <QtCore/quuid.h>
#include <cstring>

//  A QAxFactory that Python can take functions over in. Every
//  QAxFactory Python makes is one. Each function below asks the
//  Python function handed over for it, and runs Qt's own without
//  one.
typedef void * (*CuteQAxFactoryCall0)(const void *, const QString *, int *);
typedef void * (*CuteQAxFactoryCall1)(const void *, const QString *, int *);
typedef bool (*CuteQAxFactoryCall2)(const void *, QObject *, IDispatch **, int *);
typedef const QUuid * (*CuteQAxFactoryCall3)(const void *, const QString *, int *);
typedef const QUuid * (*CuteQAxFactoryCall4)(const void *, const QString *, int *);
typedef const QUuid * (*CuteQAxFactoryCall5)(const void *, const QString *, int *);
typedef const QUuid * (*CuteQAxFactoryCall6)(const void *, int *);
typedef const QUuid * (*CuteQAxFactoryCall7)(const void *, int *);
typedef void (*CuteQAxFactoryCall8)(const void *, const QString *, QSettings *, int *);
typedef void (*CuteQAxFactoryCall9)(const void *, const QString *, QSettings *, int *);
typedef bool (*CuteQAxFactoryCall10)(const void *, const QString *, const QString *, int *);
typedef QString * (*CuteQAxFactoryCall11)(const void *, const QString *, int *);
typedef bool (*CuteQAxFactoryCall12)(const void *, const QString *, int *);
typedef bool (*CuteQAxFactoryCall13)(const void *, const QString *, int *);
typedef bool (*CuteQAxFactoryCall14)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAxFactoryCall15)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAxFactoryCall16)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAxFactoryCall17)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAxFactoryCall18)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAxFactoryCall19)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAxFactoryCall20)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAxFactoryCall21)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQAxFactory : public QAxFactory {
public:
  using QAxFactory::QAxFactory;
  void *taken[22] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN10QAxFactory12createObjectERK7QString")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QAxFactory10metaObjectERK7QString")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QAxFactory19createObjectWrapperEP7QObjectPP9IDispatch")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QAxFactory7classIDERK7QString")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QAxFactory11interfaceIDERK7QString")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QAxFactory8eventsIDERK7QString")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QAxFactory9typeLibIDEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QAxFactory5appIDEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QAxFactory13registerClassERK7QStringP9QSettings")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QAxFactory15unregisterClassERK7QStringP9QSettings")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QAxFactory18validateLicenseKeyERK7QStringS2_")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QAxFactory18exposeToSuperClassERK7QString")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QAxFactory12stayTopLevelERK7QString")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QAxFactory14hasStockEventsERK7QString")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QAxFactory9isServiceEv")) {
      taken[14] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[15] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[16] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[17] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[18] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[19] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[20] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[21] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QObject *QAxFactory::createObject(const QString &key)
  QObject *createObject(const QString &key) override {
    if (taken[0]) {
      int handled = 0;
      CuteQAxFactoryCall0 call = reinterpret_cast<CuteQAxFactoryCall0>(taken[0]);
      void * given = call(this, &key, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return {};
  }

  //  const QMetaObject *QAxFactory::metaObject(const QString &key) const
  const QMetaObject *metaObject(const QString &key) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQAxFactoryCall1 call = reinterpret_cast<CuteQAxFactoryCall1>(taken[1]);
      void * given = call(this, &key, &handled);
      if (handled) return static_cast<const QMetaObject *>(given);
    }
    return {};
  }

  //  bool QAxFactory::createObjectWrapper(QObject *object, IDispatch
  //      **wrapper)
  bool createObjectWrapper(QObject *object, IDispatch **wrapper) override {
    if (taken[2]) {
      int handled = 0;
      CuteQAxFactoryCall2 call = reinterpret_cast<CuteQAxFactoryCall2>(taken[2]);
      bool given = call(this, object, wrapper, &handled);
      if (handled) return given;
    }
    return QAxFactory::createObjectWrapper(object, wrapper);
  }

  //  QUuid QAxFactory::classID(const QString &key) const
  QUuid classID(const QString &key) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQAxFactoryCall3 call = reinterpret_cast<CuteQAxFactoryCall3>(taken[3]);
      const QUuid * given = call(this, &key, &handled);
      if (handled && given) return *given;
    }
    return QAxFactory::classID(key);
  }

  //  QUuid QAxFactory::interfaceID(const QString &key) const
  QUuid interfaceID(const QString &key) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQAxFactoryCall4 call = reinterpret_cast<CuteQAxFactoryCall4>(taken[4]);
      const QUuid * given = call(this, &key, &handled);
      if (handled && given) return *given;
    }
    return QAxFactory::interfaceID(key);
  }

  //  QUuid QAxFactory::eventsID(const QString &key) const
  QUuid eventsID(const QString &key) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQAxFactoryCall5 call = reinterpret_cast<CuteQAxFactoryCall5>(taken[5]);
      const QUuid * given = call(this, &key, &handled);
      if (handled && given) return *given;
    }
    return QAxFactory::eventsID(key);
  }

  //  QUuid QAxFactory::typeLibID() const
  QUuid typeLibID() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQAxFactoryCall6 call = reinterpret_cast<CuteQAxFactoryCall6>(taken[6]);
      const QUuid * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAxFactory::typeLibID();
  }

  //  QUuid QAxFactory::appID() const
  QUuid appID() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQAxFactoryCall7 call = reinterpret_cast<CuteQAxFactoryCall7>(taken[7]);
      const QUuid * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAxFactory::appID();
  }

  //  void QAxFactory::registerClass(const QString &key, QSettings *a1) const
  void registerClass(const QString &key, QSettings *a1) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQAxFactoryCall8 call = reinterpret_cast<CuteQAxFactoryCall8>(taken[8]);
      call(this, &key, a1, &handled);
      if (handled) return;
    }
    QAxFactory::registerClass(key, a1);
  }

  //  void QAxFactory::unregisterClass(const QString &key, QSettings *a1)
  //      const
  void unregisterClass(const QString &key, QSettings *a1) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQAxFactoryCall9 call = reinterpret_cast<CuteQAxFactoryCall9>(taken[9]);
      call(this, &key, a1, &handled);
      if (handled) return;
    }
    QAxFactory::unregisterClass(key, a1);
  }

  //  bool QAxFactory::validateLicenseKey(const QString &key, const QString
  //      &licenseKey) const
  bool validateLicenseKey(const QString &key, const QString &licenseKey) const override {
    if (taken[10]) {
      int handled = 0;
      CuteQAxFactoryCall10 call = reinterpret_cast<CuteQAxFactoryCall10>(taken[10]);
      bool given = call(this, &key, &licenseKey, &handled);
      if (handled) return given;
    }
    return QAxFactory::validateLicenseKey(key, licenseKey);
  }

  //  QString QAxFactory::exposeToSuperClass(const QString &key) const
  QString exposeToSuperClass(const QString &key) const override {
    if (taken[11]) {
      int handled = 0;
      CuteQAxFactoryCall11 call = reinterpret_cast<CuteQAxFactoryCall11>(taken[11]);
      QString * given = call(this, &key, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QAxFactory::exposeToSuperClass(key);
  }

  //  bool QAxFactory::stayTopLevel(const QString &key) const
  bool stayTopLevel(const QString &key) const override {
    if (taken[12]) {
      int handled = 0;
      CuteQAxFactoryCall12 call = reinterpret_cast<CuteQAxFactoryCall12>(taken[12]);
      bool given = call(this, &key, &handled);
      if (handled) return given;
    }
    return QAxFactory::stayTopLevel(key);
  }

  //  bool QAxFactory::hasStockEvents(const QString &key) const
  bool hasStockEvents(const QString &key) const override {
    if (taken[13]) {
      int handled = 0;
      CuteQAxFactoryCall13 call = reinterpret_cast<CuteQAxFactoryCall13>(taken[13]);
      bool given = call(this, &key, &handled);
      if (handled) return given;
    }
    return QAxFactory::hasStockEvents(key);
  }

  //  bool QAxFactory::isService() const
  bool isService() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQAxFactoryCall14 call = reinterpret_cast<CuteQAxFactoryCall14>(taken[14]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QAxFactory::isService();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQAxFactoryCall15 call = reinterpret_cast<CuteQAxFactoryCall15>(taken[15]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQAxFactoryCall16 call = reinterpret_cast<CuteQAxFactoryCall16>(taken[16]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQAxFactoryCall17 call = reinterpret_cast<CuteQAxFactoryCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQAxFactoryCall18 call = reinterpret_cast<CuteQAxFactoryCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQAxFactoryCall19 call = reinterpret_cast<CuteQAxFactoryCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[20]) {
      int handled = 0;
      CuteQAxFactoryCall20 call = reinterpret_cast<CuteQAxFactoryCall20>(taken[20]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[21]) {
      int handled = 0;
      CuteQAxFactoryCall21 call = reinterpret_cast<CuteQAxFactoryCall21>(taken[21]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  QAxFactory::~QAxFactory()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QAxFactoryD1Ev(QAxFactory *self) {
  delete self;
}

//  QObject *QAxFactory::createObject(const QString &key)
extern "C" Q_DECL_EXPORT
QObject *ritual_ZN10QAxFactory12createObjectERK7QString(
    QAxFactory *self,
    const QString *key) {
  return self->createObject(*key);
}

//  const QMetaObject *QAxFactory::metaObject(const QString &key) const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10QAxFactory10metaObjectERK7QString(
    const QAxFactory *self,
    const QString *key) {
  return self->metaObject(*key);
}

//  bool QAxFactory::createObjectWrapper(QObject *object, IDispatch
//      **wrapper)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QAxFactory19createObjectWrapperEP7QObjectPP9IDispatch(
    QAxFactory *self,
    QObject *object,
    IDispatch **wrapper) {
  return self->createObjectWrapper(object, wrapper);
}

//  QUuid QAxFactory::classID(const QString &key) const
extern "C" Q_DECL_EXPORT
QUuid *ritual_ZNK10QAxFactory7classIDERK7QString(
    const QAxFactory *self,
    const QString *key) {
  return new QUuid(self->classID(*key));
}

//  QUuid QAxFactory::interfaceID(const QString &key) const
extern "C" Q_DECL_EXPORT
QUuid *ritual_ZNK10QAxFactory11interfaceIDERK7QString(
    const QAxFactory *self,
    const QString *key) {
  return new QUuid(self->interfaceID(*key));
}

//  QUuid QAxFactory::eventsID(const QString &key) const
extern "C" Q_DECL_EXPORT
QUuid *ritual_ZNK10QAxFactory8eventsIDERK7QString(
    const QAxFactory *self,
    const QString *key) {
  return new QUuid(self->eventsID(*key));
}

//  QUuid QAxFactory::typeLibID() const
extern "C" Q_DECL_EXPORT
QUuid *ritual_ZNK10QAxFactory9typeLibIDEv(const QAxFactory *self) {
  return new QUuid(self->typeLibID());
}

//  QUuid QAxFactory::appID() const
extern "C" Q_DECL_EXPORT
QUuid *ritual_ZNK10QAxFactory5appIDEv(const QAxFactory *self) {
  return new QUuid(self->appID());
}

//  void QAxFactory::registerClass(const QString &key, QSettings *a1) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK10QAxFactory13registerClassERK7QStringP9QSettings(
    const QAxFactory *self,
    const QString *key,
    QSettings *a1) {
  self->registerClass(*key, a1);
}

//  void QAxFactory::unregisterClass(const QString &key, QSettings *a1) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK10QAxFactory15unregisterClassERK7QStringP9QSettings(
    const QAxFactory *self,
    const QString *key,
    QSettings *a1) {
  self->unregisterClass(*key, a1);
}

//  bool QAxFactory::validateLicenseKey(const QString &key, const QString
//      &licenseKey) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QAxFactory18validateLicenseKeyERK7QStringS2_(
    const QAxFactory *self,
    const QString *key,
    const QString *licenseKey) {
  return self->validateLicenseKey(*key, *licenseKey);
}

//  QString QAxFactory::exposeToSuperClass(const QString &key) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10QAxFactory18exposeToSuperClassERK7QString(
    const QAxFactory *self,
    const QString *key) {
  return new QString(self->exposeToSuperClass(*key));
}

//  bool QAxFactory::stayTopLevel(const QString &key) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QAxFactory12stayTopLevelERK7QString(
    const QAxFactory *self,
    const QString *key) {
  return self->stayTopLevel(*key);
}

//  bool QAxFactory::hasStockEvents(const QString &key) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QAxFactory14hasStockEventsERK7QString(
    const QAxFactory *self,
    const QString *key) {
  return self->hasStockEvents(*key);
}

//  bool QAxFactory::isService() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QAxFactory9isServiceEv(const QAxFactory *self) {
  return self->isService();
}

//  bool QAxFactory::isServer()
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QAxFactory8isServerEv() {
  return QAxFactory::isServer();
}

//  QString QAxFactory::serverDirPath()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10QAxFactory13serverDirPathEv() {
  return new QString(QAxFactory::serverDirPath());
}

//  QString QAxFactory::serverFilePath()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10QAxFactory14serverFilePathEv() {
  return new QString(QAxFactory::serverFilePath());
}

//  bool QAxFactory::startServer(ServerType type)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QAxFactory11startServerENS_10ServerTypeE(
    QAxFactory::ServerType type) {
  return QAxFactory::startServer(type);
}

//  bool QAxFactory::stopServer()
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QAxFactory10stopServerEv() {
  return QAxFactory::stopServer();
}

//  bool QAxFactory::registerActiveObject(QObject *object)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QAxFactory20registerActiveObjectEP7QObject(QObject *object) {
  return QAxFactory::registerActiveObject(object);
}

//  QAxFactory *qAxFactory()
extern "C" Q_DECL_EXPORT
QAxFactory *ritual_Z10qAxFactoryv() {
  return qAxFactory();
}

//  bool qax_startServer(QAxFactory::ServerType a0)
extern "C" Q_DECL_EXPORT
bool ritual_Z15qax_startServerN10QAxFactory10ServerTypeE(
    QAxFactory::ServerType a0) {
  return qax_startServer(a0);
}

//  bool qax_stopServer()
extern "C" Q_DECL_EXPORT
bool ritual_Z14qax_stopServerv() {
  return qax_stopServer();
}

//  a Python function taken by a CuteQAxFactory, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAxFactory(QAxFactory *self, const char *key, void *call) {
  return static_cast<CuteQAxFactory *>(self)->take(key, call);
}

//  bool QAxFactory::createObjectWrapper(QObject *object, IDispatch
//      **wrapper)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN10QAxFactory19createObjectWrapperEP7QObjectPP9IDispatch(
    QAxFactory *self,
    QObject *object,
    IDispatch **wrapper) {
  return self->QAxFactory::createObjectWrapper(object, wrapper);
}

//  QUuid QAxFactory::classID(const QString &key) const
extern "C" Q_DECL_EXPORT
QUuid *ritual_own_ZNK10QAxFactory7classIDERK7QString(
    const QAxFactory *self,
    const QString *key) {
  return new QUuid(self->QAxFactory::classID(*key));
}

//  QUuid QAxFactory::interfaceID(const QString &key) const
extern "C" Q_DECL_EXPORT
QUuid *ritual_own_ZNK10QAxFactory11interfaceIDERK7QString(
    const QAxFactory *self,
    const QString *key) {
  return new QUuid(self->QAxFactory::interfaceID(*key));
}

//  QUuid QAxFactory::eventsID(const QString &key) const
extern "C" Q_DECL_EXPORT
QUuid *ritual_own_ZNK10QAxFactory8eventsIDERK7QString(
    const QAxFactory *self,
    const QString *key) {
  return new QUuid(self->QAxFactory::eventsID(*key));
}

//  QUuid QAxFactory::typeLibID() const
extern "C" Q_DECL_EXPORT
QUuid *ritual_own_ZNK10QAxFactory9typeLibIDEv(const QAxFactory *self) {
  return new QUuid(self->QAxFactory::typeLibID());
}

//  QUuid QAxFactory::appID() const
extern "C" Q_DECL_EXPORT
QUuid *ritual_own_ZNK10QAxFactory5appIDEv(const QAxFactory *self) {
  return new QUuid(self->QAxFactory::appID());
}

//  void QAxFactory::registerClass(const QString &key, QSettings *a1) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK10QAxFactory13registerClassERK7QStringP9QSettings(
    const QAxFactory *self,
    const QString *key,
    QSettings *a1) {
  self->QAxFactory::registerClass(*key, a1);
}

//  void QAxFactory::unregisterClass(const QString &key, QSettings *a1) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK10QAxFactory15unregisterClassERK7QStringP9QSettings(
    const QAxFactory *self,
    const QString *key,
    QSettings *a1) {
  self->QAxFactory::unregisterClass(*key, a1);
}

//  bool QAxFactory::validateLicenseKey(const QString &key, const QString
//      &licenseKey) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK10QAxFactory18validateLicenseKeyERK7QStringS2_(
    const QAxFactory *self,
    const QString *key,
    const QString *licenseKey) {
  return self->QAxFactory::validateLicenseKey(*key, *licenseKey);
}

//  QString QAxFactory::exposeToSuperClass(const QString &key) const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK10QAxFactory18exposeToSuperClassERK7QString(
    const QAxFactory *self,
    const QString *key) {
  return new QString(self->QAxFactory::exposeToSuperClass(*key));
}

//  bool QAxFactory::stayTopLevel(const QString &key) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK10QAxFactory12stayTopLevelERK7QString(
    const QAxFactory *self,
    const QString *key) {
  return self->QAxFactory::stayTopLevel(*key);
}

//  bool QAxFactory::hasStockEvents(const QString &key) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK10QAxFactory14hasStockEventsERK7QString(
    const QAxFactory *self,
    const QString *key) {
  return self->QAxFactory::hasStockEvents(*key);
}

//  bool QAxFactory::isService() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK10QAxFactory9isServiceEv(const QAxFactory *self) {
  return self->QAxFactory::isService();
}

#endif  // defined(Q_OS_WIN)
