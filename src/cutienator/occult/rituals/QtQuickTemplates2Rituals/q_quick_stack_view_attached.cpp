//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickstackview_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickstackview_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQuickStackViewAttached that Python can take functions over in. Every QQuickStackViewAttached
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickStackViewAttachedCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickStackViewAttachedCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickStackViewAttachedCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickStackViewAttachedCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickStackViewAttachedCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickStackViewAttachedCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickStackViewAttachedCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickStackViewAttached : public QQuickStackViewAttached {
public:
  using QQuickStackViewAttached::QQuickStackViewAttached;
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
      CuteQQuickStackViewAttachedCall0 call = reinterpret_cast<CuteQQuickStackViewAttachedCall0>(taken[0]);
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
      CuteQQuickStackViewAttachedCall1 call = reinterpret_cast<CuteQQuickStackViewAttachedCall1>(taken[1]);
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
      CuteQQuickStackViewAttachedCall2 call = reinterpret_cast<CuteQQuickStackViewAttachedCall2>(taken[2]);
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
      CuteQQuickStackViewAttachedCall3 call = reinterpret_cast<CuteQQuickStackViewAttachedCall3>(taken[3]);
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
      CuteQQuickStackViewAttachedCall4 call = reinterpret_cast<CuteQQuickStackViewAttachedCall4>(taken[4]);
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
      CuteQQuickStackViewAttachedCall5 call = reinterpret_cast<CuteQQuickStackViewAttachedCall5>(taken[5]);
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
      CuteQQuickStackViewAttachedCall6 call = reinterpret_cast<CuteQQuickStackViewAttachedCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickStackViewAttached::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK23QQuickStackViewAttached10metaObjectEv(
    const QQuickStackViewAttached *self) {
  return self->metaObject();
}

//  void *QQuickStackViewAttached::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN23QQuickStackViewAttached11qt_metacastEPKc(
    QQuickStackViewAttached *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickStackViewAttached::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN23QQuickStackViewAttached11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickStackViewAttached *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickStackViewAttached::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN23QQuickStackViewAttached2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickStackViewAttached::tr(s, c, n));
}

//  QQuickStackViewAttached::QQuickStackViewAttached(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickStackViewAttached *ritual_ZN23QQuickStackViewAttachedC1EP7QObject(
    QObject *parent) {
  return new CuteQQuickStackViewAttached(parent);
}

//  QQuickStackViewAttached::~QQuickStackViewAttached()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickStackViewAttachedD1Ev(QQuickStackViewAttached *self) {
  delete self;
}

//  int QQuickStackViewAttached::index() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK23QQuickStackViewAttached5indexEv(
    const QQuickStackViewAttached *self) {
  return self->index();
}

//  QQuickStackView *QQuickStackViewAttached::view() const
extern "C" Q_DECL_EXPORT
QQuickStackView *ritual_ZNK23QQuickStackViewAttached4viewEv(
    const QQuickStackViewAttached *self) {
  return self->view();
}

//  QQuickStackView::Status QQuickStackViewAttached::status() const
extern "C" Q_DECL_EXPORT
QQuickStackView::Status ritual_ZNK23QQuickStackViewAttached6statusEv(
    const QQuickStackViewAttached *self) {
  return self->status();
}

//  bool QQuickStackViewAttached::isVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QQuickStackViewAttached9isVisibleEv(
    const QQuickStackViewAttached *self) {
  return self->isVisible();
}

//  void QQuickStackViewAttached::setVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickStackViewAttached10setVisibleEb(
    QQuickStackViewAttached *self,
    bool visible) {
  self->setVisible(visible);
}

//  void QQuickStackViewAttached::resetVisible()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickStackViewAttached12resetVisibleEv(
    QQuickStackViewAttached *self) {
  self->resetVisible();
}

//  void QQuickStackViewAttached::indexChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickStackViewAttached12indexChangedEv(
    QQuickStackViewAttached *self) {
  self->indexChanged();
}

//  void QQuickStackViewAttached::viewChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickStackViewAttached11viewChangedEv(
    QQuickStackViewAttached *self) {
  self->viewChanged();
}

//  void QQuickStackViewAttached::statusChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickStackViewAttached13statusChangedEv(
    QQuickStackViewAttached *self) {
  self->statusChanged();
}

//  void QQuickStackViewAttached::activated()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickStackViewAttached9activatedEv(
    QQuickStackViewAttached *self) {
  self->activated();
}

//  void QQuickStackViewAttached::activating()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickStackViewAttached10activatingEv(
    QQuickStackViewAttached *self) {
  self->activating();
}

//  void QQuickStackViewAttached::deactivated()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickStackViewAttached11deactivatedEv(
    QQuickStackViewAttached *self) {
  self->deactivated();
}

//  void QQuickStackViewAttached::deactivating()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickStackViewAttached12deactivatingEv(
    QQuickStackViewAttached *self) {
  self->deactivating();
}

//  void QQuickStackViewAttached::removed()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickStackViewAttached7removedEv(
    QQuickStackViewAttached *self) {
  self->removed();
}

//  void QQuickStackViewAttached::visibleChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickStackViewAttached14visibleChangedEv(
    QQuickStackViewAttached *self) {
  self->visibleChanged();
}

//  QQuickStackViewAttachedPrivate *QQuickStackViewAttached::d_func()
extern "C" Q_DECL_EXPORT
QQuickStackViewAttachedPrivate *ritual_ZN23QQuickStackViewAttached6d_funcEv(
    QQuickStackViewAttached *self) {
  return self->d_func();
}

//  const QQuickStackViewAttachedPrivate *QQuickStackViewAttached::d_func()
//      const
extern "C" Q_DECL_EXPORT
const QQuickStackViewAttachedPrivate *ritual_ZNK23QQuickStackViewAttached6d_funcEv(
    const QQuickStackViewAttached *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQQuickStackViewAttached, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickStackViewAttached(
    QQuickStackViewAttached *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickStackViewAttached *>(self)->take(key, call);
}
