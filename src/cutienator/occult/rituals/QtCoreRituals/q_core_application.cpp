//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qcoreapplication.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qcoreapplication.h>
#include <QtCore/qstring.h>
#include <QtCore/qdeadlinetimer.h>
#include <QtCore/qpermissions.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on QCoreApplication may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQCoreApplication : QCoreApplication {
  using QCoreApplication::event;
  using QCoreApplication::compressEvent;
};

//  A QCoreApplication that Python can take functions over in. Every QCoreApplication
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQCoreApplicationCall0)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQCoreApplicationCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef bool (*CuteQCoreApplicationCall2)(const void *, QEvent *, QObject *, QPostEventList *, int *);
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQCoreApplicationCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCoreApplicationCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCoreApplicationCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCoreApplicationCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCoreApplicationCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCoreApplicationCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQCoreApplication : public QCoreApplication {
public:
  using QCoreApplication::QCoreApplication;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN16QCoreApplication6notifyEP7QObjectP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
    if (!std::strcmp(key, "_ZN16QCoreApplication13compressEventEP6QEventP7QObjectP14QPostEventList")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QCoreApplication::notify(QObject *a0, QEvent *a1)
  bool notify(QObject *a0, QEvent *a1) override {
    if (taken[0]) {
      int handled = 0;
      CuteQCoreApplicationCall0 call = reinterpret_cast<CuteQCoreApplicationCall0>(taken[0]);
      bool given = call(this, a0, a1, &handled);
      if (handled) return given;
    }
    return QCoreApplication::notify(a0, a1);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QCoreApplication::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[1]) {
      int handled = 0;
      CuteQCoreApplicationCall1 call = reinterpret_cast<CuteQCoreApplicationCall1>(taken[1]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QCoreApplication::event(a0);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
  //  bool QCoreApplication::compressEvent(QEvent *a0, QObject *receiver,
  //      QPostEventList *a2)
  bool compressEvent(
      QEvent *a0,
      QObject *receiver,
      QPostEventList *a2) override {
    if (taken[2]) {
      int handled = 0;
      CuteQCoreApplicationCall2 call = reinterpret_cast<CuteQCoreApplicationCall2>(taken[2]);
      bool given = call(this, a0, receiver, a2, &handled);
      if (handled) return given;
    }
    return QCoreApplication::compressEvent(a0, receiver, a2);
  }
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQCoreApplicationCall3 call = reinterpret_cast<CuteQCoreApplicationCall3>(taken[3]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQCoreApplicationCall4 call = reinterpret_cast<CuteQCoreApplicationCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQCoreApplicationCall5 call = reinterpret_cast<CuteQCoreApplicationCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQCoreApplicationCall6 call = reinterpret_cast<CuteQCoreApplicationCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      CuteQCoreApplicationCall7 call = reinterpret_cast<CuteQCoreApplicationCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[8]) {
      int handled = 0;
      CuteQCoreApplicationCall8 call = reinterpret_cast<CuteQCoreApplicationCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

#if !defined(QT_NO_QOBJECT)
//  const QMetaObject *QCoreApplication::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QCoreApplication10metaObjectEv(
    const QCoreApplication *self) {
  return self->metaObject();
}
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
//  QString QCoreApplication::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QCoreApplication2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QCoreApplication::tr(s, c, n));
}
#endif  // !defined(QT_NO_QOBJECT)

//  QCoreApplicationPrivate *QCoreApplication::d_func()
extern "C" Q_DECL_EXPORT
QCoreApplicationPrivate *ritual_ZN16QCoreApplication6d_funcEv(
    QCoreApplication *self) {
  return self->d_func();
}

//  const QCoreApplicationPrivate *QCoreApplication::d_func() const
extern "C" Q_DECL_EXPORT
const QCoreApplicationPrivate *ritual_ZNK16QCoreApplication6d_funcEv(
    const QCoreApplication *self) {
  return self->d_func();
}

//  QCoreApplication::QCoreApplication(int &argc, char **argv, int a2)
extern "C" Q_DECL_EXPORT
QCoreApplication *ritual_ZN16QCoreApplicationC1ERiPPci(
    int *argc,
    char **argv,
    int a2) {
  return new CuteQCoreApplication(*argc, argv, a2);
}

//  QCoreApplication::~QCoreApplication()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QCoreApplicationD1Ev(QCoreApplication *self) {
  delete self;
}

//  QStringList QCoreApplication::arguments()
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN16QCoreApplication9argumentsEv() {
  return new QList<QString>(QCoreApplication::arguments());
}

//  void QCoreApplication::setAttribute(Qt::ApplicationAttribute attribute,
//      bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QCoreApplication12setAttributeEN2Qt20ApplicationAttributeEb(
    Qt::ApplicationAttribute attribute,
    bool on) {
  QCoreApplication::setAttribute(attribute, on);
}

//  bool QCoreApplication::testAttribute(Qt::ApplicationAttribute attribute)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QCoreApplication13testAttributeEN2Qt20ApplicationAttributeE(
    Qt::ApplicationAttribute attribute) {
  return QCoreApplication::testAttribute(attribute);
}

//  void QCoreApplication::setOrganizationDomain(const QString &orgDomain)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QCoreApplication21setOrganizationDomainERK7QString(
    const QString *orgDomain) {
  QCoreApplication::setOrganizationDomain(*orgDomain);
}

//  QString QCoreApplication::organizationDomain()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QCoreApplication18organizationDomainEv() {
  return new QString(QCoreApplication::organizationDomain());
}

//  void QCoreApplication::setOrganizationName(const QString &orgName)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QCoreApplication19setOrganizationNameERK7QString(
    const QString *orgName) {
  QCoreApplication::setOrganizationName(*orgName);
}

//  QString QCoreApplication::organizationName()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QCoreApplication16organizationNameEv() {
  return new QString(QCoreApplication::organizationName());
}

//  void QCoreApplication::setApplicationName(const QString &application)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QCoreApplication18setApplicationNameERK7QString(
    const QString *application) {
  QCoreApplication::setApplicationName(*application);
}

//  QString QCoreApplication::applicationName()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QCoreApplication15applicationNameEv() {
  return new QString(QCoreApplication::applicationName());
}

//  void QCoreApplication::setApplicationVersion(const QString &version)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QCoreApplication21setApplicationVersionERK7QString(
    const QString *version) {
  QCoreApplication::setApplicationVersion(*version);
}

//  QString QCoreApplication::applicationVersion()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QCoreApplication18applicationVersionEv() {
  return new QString(QCoreApplication::applicationVersion());
}

//  void QCoreApplication::setSetuidAllowed(bool allow)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QCoreApplication16setSetuidAllowedEb(bool allow) {
  QCoreApplication::setSetuidAllowed(allow);
}

//  bool QCoreApplication::isSetuidAllowed()
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QCoreApplication15isSetuidAllowedEv() {
  return QCoreApplication::isSetuidAllowed();
}

#if !(QT_VERSION >= QT_VERSION_CHECK(7, 0, 0))
#if !(defined(__cpp_lib_atomic_ref))
//  QCoreApplication *QCoreApplication::instance()
extern "C" Q_DECL_EXPORT
QCoreApplication *ritual_ZN16QCoreApplication8instanceEv() {
  return QCoreApplication::instance();
}
#endif  // !(defined(__cpp_lib_atomic_ref))
#endif  // !(QT_VERSION >= QT_VERSION_CHECK(7, 0, 0))

#if !(QT_VERSION >= QT_VERSION_CHECK(7, 0, 0))
//  bool QCoreApplication::instanceExists()
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QCoreApplication14instanceExistsEv() {
  return QCoreApplication::instanceExists();
}
#endif  // !(QT_VERSION >= QT_VERSION_CHECK(7, 0, 0))

#if !defined(QT_NO_QOBJECT)
//  int QCoreApplication::exec()
extern "C" Q_DECL_EXPORT
int ritual_ZN16QCoreApplication4execEv() {
  return QCoreApplication::exec();
}
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
//  void QCoreApplication::processEvents(QEventLoop::ProcessEventsFlags
//      flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QCoreApplication13processEventsE6QFlagsIN10QEventLoop17ProcessEventsFlagEE(
    int flags) {
  QCoreApplication::processEvents(
      QFlags<QEventLoop::ProcessEventsFlag>::fromInt(flags));
}
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
//  void QCoreApplication::processEvents(QEventLoop::ProcessEventsFlags
//      flags, int maxtime)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QCoreApplication13processEventsE6QFlagsIN10QEventLoop17ProcessEventsFlagEEi(
    int flags,
    int maxtime) {
  QCoreApplication::processEvents(
      QFlags<QEventLoop::ProcessEventsFlag>::fromInt(flags),
      maxtime);
}
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
//  void QCoreApplication::processEvents(QEventLoop::ProcessEventsFlags
//      flags, QDeadlineTimer deadline)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QCoreApplication13processEventsE6QFlagsIN10QEventLoop17ProcessEventsFlagEE14QDeadlineTimer(
    int flags,
    const QDeadlineTimer *deadline) {
  QCoreApplication::processEvents(
      QFlags<QEventLoop::ProcessEventsFlag>::fromInt(flags),
      *deadline);
}
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
//  bool QCoreApplication::sendEvent(QObject *receiver, QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QCoreApplication9sendEventEP7QObjectP6QEvent(
    QObject *receiver,
    QEvent *event) {
  return QCoreApplication::sendEvent(receiver, event);
}
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
//  void QCoreApplication::postEvent(QObject *receiver, QEvent *event, int
//      priority)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QCoreApplication9postEventEP7QObjectP6QEventi(
    QObject *receiver,
    QEvent *event,
    int priority) {
  QCoreApplication::postEvent(receiver, event, priority);
}
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
//  void QCoreApplication::sendPostedEvents(QObject *receiver, int
//      event_type)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QCoreApplication16sendPostedEventsEP7QObjecti(
    QObject *receiver,
    int event_type) {
  QCoreApplication::sendPostedEvents(receiver, event_type);
}
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
//  void QCoreApplication::removePostedEvents(QObject *receiver, int
//      eventType)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QCoreApplication18removePostedEventsEP7QObjecti(
    QObject *receiver,
    int eventType) {
  QCoreApplication::removePostedEvents(receiver, eventType);
}
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
//  QAbstractEventDispatcher *QCoreApplication::eventDispatcher()
extern "C" Q_DECL_EXPORT
QAbstractEventDispatcher *ritual_ZN16QCoreApplication15eventDispatcherEv() {
  return QCoreApplication::eventDispatcher();
}
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
//  void QCoreApplication::setEventDispatcher(QAbstractEventDispatcher
//      *eventDispatcher)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QCoreApplication18setEventDispatcherEP24QAbstractEventDispatcher(
    QAbstractEventDispatcher *eventDispatcher) {
  QCoreApplication::setEventDispatcher(eventDispatcher);
}
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
//  bool QCoreApplication::notify(QObject *a0, QEvent *a1)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QCoreApplication6notifyEP7QObjectP6QEvent(
    QCoreApplication *self,
    QObject *a0,
    QEvent *a1) {
  return self->notify(a0, a1);
}
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
//  bool QCoreApplication::startingUp()
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QCoreApplication10startingUpEv() {
  return QCoreApplication::startingUp();
}
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
//  bool QCoreApplication::closingDown()
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QCoreApplication11closingDownEv() {
  return QCoreApplication::closingDown();
}
#endif  // !defined(QT_NO_QOBJECT)

//  QString QCoreApplication::applicationDirPath()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QCoreApplication18applicationDirPathEv() {
  return new QString(QCoreApplication::applicationDirPath());
}

//  QString QCoreApplication::applicationFilePath()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QCoreApplication19applicationFilePathEv() {
  return new QString(QCoreApplication::applicationFilePath());
}

//  qint64 QCoreApplication::applicationPid()
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN16QCoreApplication14applicationPidEv() {
  return QCoreApplication::applicationPid();
}

#if QT_CONFIG(permissions) || defined(Q_QDOC)
//  Qt::PermissionStatus QCoreApplication::checkPermission(const QPermission
//      &permission)
extern "C" Q_DECL_EXPORT
Qt::PermissionStatus ritual_ZN16QCoreApplication15checkPermissionERK11QPermission(
    QCoreApplication *self,
    const QPermission *permission) {
  return self->checkPermission(*permission);
}
#endif  // QT_CONFIG(permissions) || defined(Q_QDOC)

#if QT_CONFIG(library)
//  void QCoreApplication::setLibraryPaths(const QStringList &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QCoreApplication15setLibraryPathsERK5QListI7QStringE(
    const QList<QString> *a0) {
  QCoreApplication::setLibraryPaths(*a0);
}
#endif  // QT_CONFIG(library)

#if QT_CONFIG(library)
//  QStringList QCoreApplication::libraryPaths()
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN16QCoreApplication12libraryPathsEv() {
  return new QList<QString>(QCoreApplication::libraryPaths());
}
#endif  // QT_CONFIG(library)

#if QT_CONFIG(library)
//  void QCoreApplication::addLibraryPath(const QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QCoreApplication14addLibraryPathERK7QString(
    const QString *a0) {
  QCoreApplication::addLibraryPath(*a0);
}
#endif  // QT_CONFIG(library)

#if QT_CONFIG(library)
//  void QCoreApplication::removeLibraryPath(const QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QCoreApplication17removeLibraryPathERK7QString(
    const QString *a0) {
  QCoreApplication::removeLibraryPath(*a0);
}
#endif  // QT_CONFIG(library)

#if !defined(QT_NO_TRANSLATION)
//  bool QCoreApplication::installTranslator(QTranslator *messageFile)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QCoreApplication17installTranslatorEP11QTranslator(
    QTranslator *messageFile) {
  return QCoreApplication::installTranslator(messageFile);
}
#endif  // !defined(QT_NO_TRANSLATION)

#if !defined(QT_NO_TRANSLATION)
//  bool QCoreApplication::removeTranslator(QTranslator *messageFile)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QCoreApplication16removeTranslatorEP11QTranslator(
    QTranslator *messageFile) {
  return QCoreApplication::removeTranslator(messageFile);
}
#endif  // !defined(QT_NO_TRANSLATION)

//  QString QCoreApplication::translate(const char *context, const char *key,
//      const char *disambiguation, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QCoreApplication9translateEPKcS1_S1_i(
    const char *context,
    const char *key,
    const char *disambiguation,
    int n) {
  return new QString(
      QCoreApplication::translate(
          context,
          key,
          disambiguation,
          n));
}

#if !defined(QT_NO_QOBJECT)
//  void
//      QCoreApplication::installNativeEventFilter(QAbstractNativeEventFilter
//      *filterObj)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QCoreApplication24installNativeEventFilterEP26QAbstractNativeEventFilter(
    QCoreApplication *self,
    QAbstractNativeEventFilter *filterObj) {
  self->installNativeEventFilter(filterObj);
}
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
//  void QCoreApplication::removeNativeEventFilter(QAbstractNativeEventFilter
//      *filterObj)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QCoreApplication23removeNativeEventFilterEP26QAbstractNativeEventFilter(
    QCoreApplication *self,
    QAbstractNativeEventFilter *filterObj) {
  self->removeNativeEventFilter(filterObj);
}
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
//  bool QCoreApplication::isQuitLockEnabled()
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QCoreApplication17isQuitLockEnabledEv() {
  return QCoreApplication::isQuitLockEnabled();
}
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
//  void QCoreApplication::setQuitLockEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QCoreApplication18setQuitLockEnabledEb(bool enabled) {
  QCoreApplication::setQuitLockEnabled(enabled);
}
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
//  void QCoreApplication::quit()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QCoreApplication4quitEv() {
  QCoreApplication::quit();
}
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
//  void QCoreApplication::exit(int retcode)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QCoreApplication4exitEi(int retcode) {
  QCoreApplication::exit(retcode);
}
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
//  bool QCoreApplication::event(QEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QCoreApplication5eventEP6QEvent(
    QCoreApplication *self,
    QEvent *a0) {
  return self->event(a0);
}
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
//  bool QCoreApplication::compressEvent(QEvent *a0, QObject *receiver,
//      QPostEventList *a2)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QCoreApplication13compressEventEP6QEventP7QObjectP14QPostEventList(
    QCoreApplication *self,
    QEvent *a0,
    QObject *receiver,
    QPostEventList *a2) {
  return self->compressEvent(a0, receiver, a2);
}
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
//  bool QCoreApplication::sendSpontaneousEvent(QObject *receiver, QEvent
//      *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QCoreApplication20sendSpontaneousEventEP7QObjectP6QEvent(
    QObject *receiver,
    QEvent *event) {
  return QCoreApplication::sendSpontaneousEvent(receiver, event);
}
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
//  bool QCoreApplication::notifyInternal2(QObject *receiver, QEvent *a1)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QCoreApplication15notifyInternal2EP7QObjectP6QEvent(
    QObject *receiver,
    QEvent *a1) {
  return QCoreApplication::notifyInternal2(receiver, a1);
}
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
//  bool QCoreApplication::forwardEvent(QObject *receiver, QEvent *event,
//      QEvent *originatingEvent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QCoreApplication12forwardEventEP7QObjectP6QEventS3_(
    QObject *receiver,
    QEvent *event,
    QEvent *originatingEvent) {
  return QCoreApplication::forwardEvent(receiver, event, originatingEvent);
}
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
//  void QCoreApplication::requestPermissionImpl(const QPermission
//      &permission, QtPrivate::QSlotObjectBase *slotObj, const QObject
//      *context)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QCoreApplication21requestPermissionImplERK11QPermissionPN9QtPrivate15QSlotObjectBaseEPK7QObject(
    QCoreApplication *self,
    const QPermission *permission,
    QtPrivate::QSlotObjectBase *slotObj,
    const QObject *context) {
  self->requestPermissionImpl(*permission, slotObj, context);
}
#endif  // !defined(QT_NO_QOBJECT)

//  a Python function taken by a CuteQCoreApplication, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QCoreApplication(
    QCoreApplication *self,
    const char *key,
    void *call) {
  return static_cast<CuteQCoreApplication *>(self)->take(key, call);
}

#if !defined(QT_NO_QOBJECT)
//  bool QCoreApplication::notify(QObject *a0, QEvent *a1)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN16QCoreApplication6notifyEP7QObjectP6QEvent(
    QCoreApplication *self,
    QObject *a0,
    QEvent *a1) {
  return self->QCoreApplication::notify(a0, a1);
}
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
//  bool QCoreApplication::event(QEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN16QCoreApplication5eventEP6QEvent(
    QCoreApplication *self,
    QEvent *a0) {
  return static_cast<OwnQCoreApplication *>(self)->OwnQCoreApplication::event(
      a0);
}
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
//  bool QCoreApplication::compressEvent(QEvent *a0, QObject *receiver,
//      QPostEventList *a2)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN16QCoreApplication13compressEventEP6QEventP7QObjectP14QPostEventList(
    QCoreApplication *self,
    QEvent *a0,
    QObject *receiver,
    QPostEventList *a2) {
  return static_cast<OwnQCoreApplication *>(self)->OwnQCoreApplication::compressEvent(
      a0,
      receiver,
      a2);
}
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
#endif  // !defined(QT_NO_QOBJECT)
