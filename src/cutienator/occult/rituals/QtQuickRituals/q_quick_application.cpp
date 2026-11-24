//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickapplication_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickapplication_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qfont.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQuickApplication that Python can take functions over in. Every QQuickApplication
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickApplicationCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickApplicationCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickApplicationCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickApplicationCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickApplicationCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickApplicationCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickApplicationCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickApplication : public QQuickApplication {
public:
  using QQuickApplication::QQuickApplication;
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
      CuteQQuickApplicationCall0 call = reinterpret_cast<CuteQQuickApplicationCall0>(taken[0]);
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
      CuteQQuickApplicationCall1 call = reinterpret_cast<CuteQQuickApplicationCall1>(taken[1]);
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
      CuteQQuickApplicationCall2 call = reinterpret_cast<CuteQQuickApplicationCall2>(taken[2]);
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
      CuteQQuickApplicationCall3 call = reinterpret_cast<CuteQQuickApplicationCall3>(taken[3]);
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
      CuteQQuickApplicationCall4 call = reinterpret_cast<CuteQQuickApplicationCall4>(taken[4]);
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
      CuteQQuickApplicationCall5 call = reinterpret_cast<CuteQQuickApplicationCall5>(taken[5]);
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
      CuteQQuickApplicationCall6 call = reinterpret_cast<CuteQQuickApplicationCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickApplication::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QQuickApplication10metaObjectEv(
    const QQuickApplication *self) {
  return self->metaObject();
}

//  QString QQuickApplication::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QQuickApplication2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickApplication::tr(s, c, n));
}

//  void QQuickApplication::qt_qmlMarker_singleton()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickApplication22qt_qmlMarker_singletonEv(
    QQuickApplication *self) {
  self->qt_qmlMarker_singleton();
}

//  QQuickApplication::QQuickApplication(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickApplication *ritual_ZN17QQuickApplicationC1EP7QObject(
    QObject *parent) {
  return new CuteQQuickApplication(parent);
}

//  QQuickApplication::~QQuickApplication()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickApplicationD1Ev(QQuickApplication *self) {
  delete self;
}

//  bool QQuickApplication::active() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QQuickApplication6activeEv(const QQuickApplication *self) {
  return self->active();
}

//  Qt::LayoutDirection QQuickApplication::layoutDirection() const
extern "C" Q_DECL_EXPORT
Qt::LayoutDirection ritual_ZNK17QQuickApplication15layoutDirectionEv(
    const QQuickApplication *self) {
  return self->layoutDirection();
}

//  bool QQuickApplication::supportsMultipleWindows() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QQuickApplication23supportsMultipleWindowsEv(
    const QQuickApplication *self) {
  return self->supportsMultipleWindows();
}

//  Qt::ApplicationState QQuickApplication::state() const
extern "C" Q_DECL_EXPORT
Qt::ApplicationState ritual_ZNK17QQuickApplication5stateEv(
    const QQuickApplication *self) {
  return self->state();
}

//  QFont QQuickApplication::font() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK17QQuickApplication4fontEv(const QQuickApplication *self) {
  return new QFont(self->font());
}

//  QString QQuickApplication::displayName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QQuickApplication11displayNameEv(
    const QQuickApplication *self) {
  return new QString(self->displayName());
}

//  void QQuickApplication::setDisplayName(const QString &displayName)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickApplication14setDisplayNameERK7QString(
    QQuickApplication *self,
    const QString *displayName) {
  self->setDisplayName(*displayName);
}

//  QStyleHints *QQuickApplication::styleHints()
extern "C" Q_DECL_EXPORT
QStyleHints *ritual_ZN17QQuickApplication10styleHintsEv(
    QQuickApplication *self) {
  return self->styleHints();
}

//  void QQuickApplication::updateScreens()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickApplication13updateScreensEv(QQuickApplication *self) {
  self->updateScreens();
}

//  a Python function taken by a CuteQQuickApplication, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickApplication(
    QQuickApplication *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickApplication *>(self)->take(key, call);
}
