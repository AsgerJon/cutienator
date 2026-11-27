//  Written by dev_tooling.RitualGenerator from the records of QtWebEngineQui
//  ck/6.12.0/QtWebEngineQuick/private/qquickwebengineaction_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtWebEngineQuick/6.12.0/QtWebEngineQuick/private/qtwebenginequickglobal_p.h>
#include <QtWebEngineQuick/QtWebEngineQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWebEngineQuick/6.12.0/QtWebEngineQuick/private/qquickwebengineaction_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQuickWebEngineAction that Python can take functions over in. Every QQuickWebEngineAction
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickWebEngineActionCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickWebEngineActionCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWebEngineActionCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWebEngineActionCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWebEngineActionCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWebEngineActionCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWebEngineActionCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickWebEngineAction : public QQuickWebEngineAction {
public:
  using QQuickWebEngineAction::QQuickWebEngineAction;
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
      CuteQQuickWebEngineActionCall0 call = reinterpret_cast<CuteQQuickWebEngineActionCall0>(taken[0]);
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
      CuteQQuickWebEngineActionCall1 call = reinterpret_cast<CuteQQuickWebEngineActionCall1>(taken[1]);
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
      CuteQQuickWebEngineActionCall2 call = reinterpret_cast<CuteQQuickWebEngineActionCall2>(taken[2]);
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
      CuteQQuickWebEngineActionCall3 call = reinterpret_cast<CuteQQuickWebEngineActionCall3>(taken[3]);
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
      CuteQQuickWebEngineActionCall4 call = reinterpret_cast<CuteQQuickWebEngineActionCall4>(taken[4]);
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
      CuteQQuickWebEngineActionCall5 call = reinterpret_cast<CuteQQuickWebEngineActionCall5>(taken[5]);
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
      CuteQQuickWebEngineActionCall6 call = reinterpret_cast<CuteQQuickWebEngineActionCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickWebEngineAction::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QQuickWebEngineAction10metaObjectEv(
    const QQuickWebEngineAction *self) {
  return self->metaObject();
}

//  void *QQuickWebEngineAction::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN21QQuickWebEngineAction11qt_metacastEPKc(
    QQuickWebEngineAction *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickWebEngineAction::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN21QQuickWebEngineAction11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickWebEngineAction *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickWebEngineAction::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN21QQuickWebEngineAction2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickWebEngineAction::tr(s, c, n));
}

//  void QQuickWebEngineAction::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickWebEngineAction24qt_qmlMarker_uncreatableEv(
    QQuickWebEngineAction *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QQuickWebEngineAction::QQuickWebEngineAction(const QVariant &data, const
//      QString &text, const QString &iconName, bool enabled, QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QQuickWebEngineAction *ritual_ZN21QQuickWebEngineActionC1ERK8QVariantRK7QStringS5_bP7QObject(
    const QVariant *data,
    const QString *text,
    const QString *iconName,
    bool enabled,
    QObject *parent) {
  return new CuteQQuickWebEngineAction(
      *data,
      *text,
      *iconName,
      enabled,
      parent);
}

//  QQuickWebEngineAction::QQuickWebEngineAction(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickWebEngineAction *ritual_ZN21QQuickWebEngineActionC1EP7QObject(
    QObject *parent) {
  return new CuteQQuickWebEngineAction(parent);
}

//  QQuickWebEngineAction::~QQuickWebEngineAction()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickWebEngineActionD1Ev(QQuickWebEngineAction *self) {
  delete self;
}

//  QString QQuickWebEngineAction::text() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK21QQuickWebEngineAction4textEv(
    const QQuickWebEngineAction *self) {
  return new QString(self->text());
}

//  QString QQuickWebEngineAction::iconName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK21QQuickWebEngineAction8iconNameEv(
    const QQuickWebEngineAction *self) {
  return new QString(self->iconName());
}

//  bool QQuickWebEngineAction::isEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QQuickWebEngineAction9isEnabledEv(
    const QQuickWebEngineAction *self) {
  return self->isEnabled();
}

//  void QQuickWebEngineAction::trigger()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickWebEngineAction7triggerEv(
    QQuickWebEngineAction *self) {
  self->trigger();
}

//  void QQuickWebEngineAction::triggered()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickWebEngineAction9triggeredEv(
    QQuickWebEngineAction *self) {
  self->triggered();
}

//  void QQuickWebEngineAction::enabledChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickWebEngineAction14enabledChangedEv(
    QQuickWebEngineAction *self) {
  self->enabledChanged();
}

//  QQuickWebEngineActionPrivate *QQuickWebEngineAction::d_func()
extern "C" Q_DECL_EXPORT
QQuickWebEngineActionPrivate *ritual_ZN21QQuickWebEngineAction6d_funcEv(
    QQuickWebEngineAction *self) {
  return self->d_func();
}

//  const QQuickWebEngineActionPrivate *QQuickWebEngineAction::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickWebEngineActionPrivate *ritual_ZNK21QQuickWebEngineAction6d_funcEv(
    const QQuickWebEngineAction *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQQuickWebEngineAction, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickWebEngineAction(
    QQuickWebEngineAction *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickWebEngineAction *>(self)->take(key, call);
}
