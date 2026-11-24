//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickitem_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickitem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQuickKeysAttached that Python can take functions over in. Every QQuickKeysAttached
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickKeysAttachedCall0)(const void *, int *);
typedef void (*CuteQQuickKeysAttachedCall1)(const void *, QKeyEvent *, bool, int *);
typedef void (*CuteQQuickKeysAttachedCall2)(const void *, QKeyEvent *, bool, int *);
#if QT_CONFIG(im)
typedef void (*CuteQQuickKeysAttachedCall3)(const void *, QInputMethodEvent *, bool, int *);
#endif  // QT_CONFIG(im)
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQQuickKeysAttachedCall4)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQQuickKeysAttachedCall5)(const void *, QKeyEvent *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickKeysAttachedCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickKeysAttachedCall7)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickKeysAttachedCall8)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickKeysAttachedCall9)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickKeysAttachedCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickKeysAttachedCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickKeysAttachedCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickKeysAttached : public QQuickKeysAttached {
public:
  using QQuickKeysAttached::QQuickKeysAttached;
  void *taken[13] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN19QQuickItemKeyFilter17componentCompleteEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QQuickItemKeyFilter10keyPressedEP9QKeyEventb")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QQuickItemKeyFilter11keyReleasedEP9QKeyEventb")) {
      taken[2] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN19QQuickItemKeyFilter16inputMethodEventEP17QInputMethodEventb")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK19QQuickItemKeyFilter16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN19QQuickItemKeyFilter21shortcutOverrideEventEP9QKeyEvent")) {
      taken[5] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QQuickKeysAttached::componentComplete()
  void componentComplete() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickKeysAttachedCall0 call = reinterpret_cast<CuteQQuickKeysAttachedCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickKeysAttached::componentComplete();
  }

  //  void QQuickKeysAttached::keyPressed(QKeyEvent *event, bool post)
  void keyPressed(QKeyEvent *event, bool post) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickKeysAttachedCall1 call = reinterpret_cast<CuteQQuickKeysAttachedCall1>(taken[1]);
      call(this, event, post, &handled);
      if (handled) return;
    }
    QQuickKeysAttached::keyPressed(event, post);
  }

  //  void QQuickKeysAttached::keyReleased(QKeyEvent *event, bool post)
  void keyReleased(QKeyEvent *event, bool post) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickKeysAttachedCall2 call = reinterpret_cast<CuteQQuickKeysAttachedCall2>(taken[2]);
      call(this, event, post, &handled);
      if (handled) return;
    }
    QQuickKeysAttached::keyReleased(event, post);
  }

#if QT_CONFIG(im)
  //  void QQuickKeysAttached::inputMethodEvent(QInputMethodEvent *a0, bool
  //      post)
  void inputMethodEvent(QInputMethodEvent *a0, bool post) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickKeysAttachedCall3 call = reinterpret_cast<CuteQQuickKeysAttachedCall3>(taken[3]);
      call(this, a0, post, &handled);
      if (handled) return;
    }
    QQuickKeysAttached::inputMethodEvent(a0, post);
  }
#endif  // QT_CONFIG(im)

#if QT_CONFIG(im)
  //  QVariant QQuickKeysAttached::inputMethodQuery(Qt::InputMethodQuery
  //      query) const
  QVariant inputMethodQuery(Qt::InputMethodQuery query) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickKeysAttachedCall4 call = reinterpret_cast<CuteQQuickKeysAttachedCall4>(taken[4]);
      const QVariant * given = call(this, static_cast<int>(query), &handled);
      if (handled && given) return *given;
    }
    return QQuickKeysAttached::inputMethodQuery(query);
  }
#endif  // QT_CONFIG(im)

  //  void QQuickKeysAttached::shortcutOverrideEvent(QKeyEvent *event)
  void shortcutOverrideEvent(QKeyEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickKeysAttachedCall5 call = reinterpret_cast<CuteQQuickKeysAttachedCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickKeysAttached::shortcutOverrideEvent(event);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickKeysAttachedCall6 call = reinterpret_cast<CuteQQuickKeysAttachedCall6>(taken[6]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickKeysAttachedCall7 call = reinterpret_cast<CuteQQuickKeysAttachedCall7>(taken[7]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickKeysAttachedCall8 call = reinterpret_cast<CuteQQuickKeysAttachedCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickKeysAttachedCall9 call = reinterpret_cast<CuteQQuickKeysAttachedCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickKeysAttachedCall10 call = reinterpret_cast<CuteQQuickKeysAttachedCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickKeysAttachedCall11 call = reinterpret_cast<CuteQQuickKeysAttachedCall11>(taken[11]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickKeysAttachedCall12 call = reinterpret_cast<CuteQQuickKeysAttachedCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickKeysAttached::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QQuickKeysAttached10metaObjectEv(
    const QQuickKeysAttached *self) {
  return self->metaObject();
}

//  QString QQuickKeysAttached::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QQuickKeysAttached2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickKeysAttached::tr(s, c, n));
}

//  QQuickKeysAttachedPrivate *QQuickKeysAttached::d_func()
extern "C" Q_DECL_EXPORT
QQuickKeysAttachedPrivate *ritual_ZN18QQuickKeysAttached6d_funcEv(
    QQuickKeysAttached *self) {
  return self->d_func();
}

//  const QQuickKeysAttachedPrivate *QQuickKeysAttached::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickKeysAttachedPrivate *ritual_ZNK18QQuickKeysAttached6d_funcEv(
    const QQuickKeysAttached *self) {
  return self->d_func();
}

//  void QQuickKeysAttached::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickKeysAttached24qt_qmlMarker_uncreatableEv(
    QQuickKeysAttached *self) {
  self->qt_qmlMarker_uncreatable();
}

//  void QQuickKeysAttached::qt_qmlMarker_attached()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickKeysAttached21qt_qmlMarker_attachedEv(
    QQuickKeysAttached *self) {
  self->qt_qmlMarker_attached();
}

//  QQuickKeysAttached::QQuickKeysAttached(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickKeysAttached *ritual_ZN18QQuickKeysAttachedC1EP7QObject(
    QObject *parent) {
  return new CuteQQuickKeysAttached(parent);
}

//  QQuickKeysAttached::~QQuickKeysAttached()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickKeysAttachedD1Ev(QQuickKeysAttached *self) {
  delete self;
}

//  bool QQuickKeysAttached::enabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQuickKeysAttached7enabledEv(
    const QQuickKeysAttached *self) {
  return self->enabled();
}

//  void QQuickKeysAttached::setEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickKeysAttached10setEnabledEb(
    QQuickKeysAttached *self,
    bool enabled) {
  self->setEnabled(enabled);
}

//  Priority QQuickKeysAttached::priority() const
extern "C" Q_DECL_EXPORT
QQuickKeysAttached::Priority ritual_ZNK18QQuickKeysAttached8priorityEv(
    const QQuickKeysAttached *self) {
  return self->priority();
}

//  void QQuickKeysAttached::setPriority(Priority a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickKeysAttached11setPriorityENS_8PriorityE(
    QQuickKeysAttached *self,
    QQuickKeysAttached::Priority a0) {
  self->setPriority(a0);
}

//  void QQuickKeysAttached::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickKeysAttached17componentCompleteEv(
    QQuickKeysAttached *self) {
  self->componentComplete();
}

//  QQuickKeysAttached *QQuickKeysAttached::qmlAttachedProperties(QObject
//      *a0)
extern "C" Q_DECL_EXPORT
QQuickKeysAttached *ritual_ZN18QQuickKeysAttached21qmlAttachedPropertiesEP7QObject(
    QObject *a0) {
  return QQuickKeysAttached::qmlAttachedProperties(a0);
}

//  void QQuickKeysAttached::keyPressed(QKeyEvent *event, bool post)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickKeysAttached10keyPressedEP9QKeyEventb(
    QQuickKeysAttached *self,
    QKeyEvent *event,
    bool post) {
  self->keyPressed(event, post);
}

//  void QQuickKeysAttached::keyReleased(QKeyEvent *event, bool post)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickKeysAttached11keyReleasedEP9QKeyEventb(
    QQuickKeysAttached *self,
    QKeyEvent *event,
    bool post) {
  self->keyReleased(event, post);
}

#if QT_CONFIG(im)
//  void QQuickKeysAttached::inputMethodEvent(QInputMethodEvent *a0, bool
//      post)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickKeysAttached16inputMethodEventEP17QInputMethodEventb(
    QQuickKeysAttached *self,
    QInputMethodEvent *a0,
    bool post) {
  self->inputMethodEvent(a0, post);
}
#endif  // QT_CONFIG(im)

#if QT_CONFIG(im)
//  QVariant QQuickKeysAttached::inputMethodQuery(Qt::InputMethodQuery query)
//      const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK18QQuickKeysAttached16inputMethodQueryEN2Qt16InputMethodQueryE(
    const QQuickKeysAttached *self,
    Qt::InputMethodQuery query) {
  return new QVariant(self->inputMethodQuery(query));
}
#endif  // QT_CONFIG(im)

//  void QQuickKeysAttached::shortcutOverrideEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickKeysAttached21shortcutOverrideEventEP9QKeyEvent(
    QQuickKeysAttached *self,
    QKeyEvent *event) {
  self->shortcutOverrideEvent(event);
}

//  QByteArray QQuickKeysAttached::keyToSignal(int key)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN18QQuickKeysAttached11keyToSignalEi(int key) {
  return new QByteArray(QQuickKeysAttached::keyToSignal(key));
}

//  bool QQuickKeysAttached::isConnected(const char *signalName) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQuickKeysAttached11isConnectedEPKc(
    const QQuickKeysAttached *self,
    const char *signalName) {
  return self->isConnected(signalName);
}

//  QQuickKeysAttached as the QQuickItemKeyFilter it is built on
extern "C" Q_DECL_EXPORT
QQuickItemKeyFilter *ritual_cast_QQuickKeysAttached_QQuickItemKeyFilter(
    QQuickKeysAttached *self) {
  return static_cast<QQuickItemKeyFilter *>(self);
}

//  a Python function taken by a CuteQQuickKeysAttached, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickKeysAttached(
    QQuickKeysAttached *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickKeysAttached *>(self)->take(key, call);
}

//  void QQuickKeysAttached::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QQuickKeysAttached17componentCompleteEv(
    QQuickKeysAttached *self) {
  self->QQuickKeysAttached::componentComplete();
}

//  void QQuickKeysAttached::keyPressed(QKeyEvent *event, bool post)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QQuickKeysAttached10keyPressedEP9QKeyEventb(
    QQuickKeysAttached *self,
    QKeyEvent *event,
    bool post) {
  self->QQuickKeysAttached::keyPressed(event, post);
}

//  void QQuickKeysAttached::keyReleased(QKeyEvent *event, bool post)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QQuickKeysAttached11keyReleasedEP9QKeyEventb(
    QQuickKeysAttached *self,
    QKeyEvent *event,
    bool post) {
  self->QQuickKeysAttached::keyReleased(event, post);
}

#if QT_CONFIG(im)
//  void QQuickKeysAttached::inputMethodEvent(QInputMethodEvent *a0, bool
//      post)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QQuickKeysAttached16inputMethodEventEP17QInputMethodEventb(
    QQuickKeysAttached *self,
    QInputMethodEvent *a0,
    bool post) {
  self->QQuickKeysAttached::inputMethodEvent(a0, post);
}
#endif  // QT_CONFIG(im)

#if QT_CONFIG(im)
//  QVariant QQuickKeysAttached::inputMethodQuery(Qt::InputMethodQuery query)
//      const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK18QQuickKeysAttached16inputMethodQueryEN2Qt16InputMethodQueryE(
    const QQuickKeysAttached *self,
    Qt::InputMethodQuery query) {
  return new QVariant(self->QQuickKeysAttached::inputMethodQuery(query));
}
#endif  // QT_CONFIG(im)

//  void QQuickKeysAttached::shortcutOverrideEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QQuickKeysAttached21shortcutOverrideEventEP9QKeyEvent(
    QQuickKeysAttached *self,
    QKeyEvent *event) {
  self->QQuickKeysAttached::shortcutOverrideEvent(event);
}
