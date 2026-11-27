//  Written by dev_tooling.RitualGenerator from the records of
//  QtWebEngineCore/qwebenginenotification.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtWebEngineCore/qwebenginenotification.h>
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtGui/qimage.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QWebEngineNotification that Python can take functions over in. Every QWebEngineNotification
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWebEngineNotificationCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWebEngineNotificationCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebEngineNotificationCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebEngineNotificationCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebEngineNotificationCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebEngineNotificationCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebEngineNotificationCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQWebEngineNotification : public QWebEngineNotification {
public:
  using QWebEngineNotification::QWebEngineNotification;
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
      CuteQWebEngineNotificationCall0 call = reinterpret_cast<CuteQWebEngineNotificationCall0>(taken[0]);
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
      CuteQWebEngineNotificationCall1 call = reinterpret_cast<CuteQWebEngineNotificationCall1>(taken[1]);
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
      CuteQWebEngineNotificationCall2 call = reinterpret_cast<CuteQWebEngineNotificationCall2>(taken[2]);
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
      CuteQWebEngineNotificationCall3 call = reinterpret_cast<CuteQWebEngineNotificationCall3>(taken[3]);
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
      CuteQWebEngineNotificationCall4 call = reinterpret_cast<CuteQWebEngineNotificationCall4>(taken[4]);
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
      CuteQWebEngineNotificationCall5 call = reinterpret_cast<CuteQWebEngineNotificationCall5>(taken[5]);
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
      CuteQWebEngineNotificationCall6 call = reinterpret_cast<CuteQWebEngineNotificationCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QWebEngineNotification::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK22QWebEngineNotification10metaObjectEv(
    const QWebEngineNotification *self) {
  return self->metaObject();
}

//  void *QWebEngineNotification::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN22QWebEngineNotification11qt_metacastEPKc(
    QWebEngineNotification *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QWebEngineNotification::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN22QWebEngineNotification11qt_metacallEN11QMetaObject4CallEiPPv(
    QWebEngineNotification *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QWebEngineNotification::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN22QWebEngineNotification2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QWebEngineNotification::tr(s, c, n));
}

//  QWebEngineNotification::~QWebEngineNotification()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QWebEngineNotificationD1Ev(QWebEngineNotification *self) {
  delete self;
}

//  bool QWebEngineNotification::matches(const QWebEngineNotification *other)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QWebEngineNotification7matchesEPKS_(
    const QWebEngineNotification *self,
    const QWebEngineNotification *other) {
  return self->matches(other);
}

//  QUrl QWebEngineNotification::origin() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK22QWebEngineNotification6originEv(
    const QWebEngineNotification *self) {
  return new QUrl(self->origin());
}

//  QImage QWebEngineNotification::icon() const
extern "C" Q_DECL_EXPORT
QImage *ritual_ZNK22QWebEngineNotification4iconEv(
    const QWebEngineNotification *self) {
  return new QImage(self->icon());
}

//  QString QWebEngineNotification::title() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QWebEngineNotification5titleEv(
    const QWebEngineNotification *self) {
  return new QString(self->title());
}

//  QString QWebEngineNotification::message() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QWebEngineNotification7messageEv(
    const QWebEngineNotification *self) {
  return new QString(self->message());
}

//  QString QWebEngineNotification::tag() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QWebEngineNotification3tagEv(
    const QWebEngineNotification *self) {
  return new QString(self->tag());
}

//  QString QWebEngineNotification::language() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QWebEngineNotification8languageEv(
    const QWebEngineNotification *self) {
  return new QString(self->language());
}

//  Qt::LayoutDirection QWebEngineNotification::direction() const
extern "C" Q_DECL_EXPORT
Qt::LayoutDirection ritual_ZNK22QWebEngineNotification9directionEv(
    const QWebEngineNotification *self) {
  return self->direction();
}

//  void QWebEngineNotification::show() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK22QWebEngineNotification4showEv(
    const QWebEngineNotification *self) {
  self->show();
}

//  void QWebEngineNotification::click() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK22QWebEngineNotification5clickEv(
    const QWebEngineNotification *self) {
  self->click();
}

//  void QWebEngineNotification::close() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK22QWebEngineNotification5closeEv(
    const QWebEngineNotification *self) {
  self->close();
}

//  void QWebEngineNotification::closed()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QWebEngineNotification6closedEv(
    QWebEngineNotification *self) {
  self->closed();
}

//  QWebEngineNotificationPrivate *QWebEngineNotification::d_func()
extern "C" Q_DECL_EXPORT
QWebEngineNotificationPrivate *ritual_ZN22QWebEngineNotification6d_funcEv(
    QWebEngineNotification *self) {
  return self->d_func();
}

//  const QWebEngineNotificationPrivate *QWebEngineNotification::d_func()
//      const
extern "C" Q_DECL_EXPORT
const QWebEngineNotificationPrivate *ritual_ZNK22QWebEngineNotification6d_funcEv(
    const QWebEngineNotification *self) {
  return self->d_func();
}

//  QWebEngineNotification::QWebEngineNotification(const
//      QSharedPointer<QtWebEngineCore::UserNotificationController>
//      &controller)
extern "C" Q_DECL_EXPORT
QWebEngineNotification *ritual_ZN22QWebEngineNotificationC1ERK14QSharedPointerIN15QtWebEngineCore26UserNotificationControllerEE(
    const QSharedPointer<QtWebEngineCore::UserNotificationController> *controller) {
  return new CuteQWebEngineNotification(*controller);
}

//  a Python function taken by a CuteQWebEngineNotification, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWebEngineNotification(
    QWebEngineNotification *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWebEngineNotification *>(self)->take(key, call);
}
