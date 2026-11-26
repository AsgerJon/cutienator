//  Written by dev_tooling.RitualGenerator from the records of
//  QtWaylandCompositor/qwaylandshell.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtWaylandCompositor/qwaylandshell.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QWaylandShell that Python can take functions over in. Every QWaylandShell
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQWaylandShellCall0)(const void *, int *);
typedef void * (*CuteQWaylandShellCall1)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWaylandShellCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWaylandShellCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandShellCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandShellCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandShellCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandShellCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandShellCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQWaylandShell : public QWaylandShell {
public:
  using QWaylandShell::QWaylandShell;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN27QWaylandCompositorExtension10initializeEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK27QWaylandCompositorExtension18extensionInterfaceEv")) {
      taken[1] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[2] = call;
      return true;
    }
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

  //  void QWaylandCompositorExtension::initialize()
  void initialize() override {
    if (taken[0]) {
      int handled = 0;
      CuteQWaylandShellCall0 call = reinterpret_cast<CuteQWaylandShellCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QWaylandCompositorExtension::initialize();
  }

  //  const struct wl_interface
  //      *QWaylandCompositorExtension::extensionInterface() const
  const struct wl_interface *extensionInterface() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQWaylandShellCall1 call = reinterpret_cast<CuteQWaylandShellCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<const struct wl_interface *>(given);
    }
    return {};
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QWaylandCompositorExtension::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQWaylandShellCall2 call = reinterpret_cast<CuteQWaylandShellCall2>(taken[2]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QWaylandCompositorExtension::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQWaylandShellCall3 call = reinterpret_cast<CuteQWaylandShellCall3>(taken[3]);
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
      CuteQWaylandShellCall4 call = reinterpret_cast<CuteQWaylandShellCall4>(taken[4]);
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
      CuteQWaylandShellCall5 call = reinterpret_cast<CuteQWaylandShellCall5>(taken[5]);
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
      CuteQWaylandShellCall6 call = reinterpret_cast<CuteQWaylandShellCall6>(taken[6]);
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
      CuteQWaylandShellCall7 call = reinterpret_cast<CuteQWaylandShellCall7>(taken[7]);
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
      CuteQWaylandShellCall8 call = reinterpret_cast<CuteQWaylandShellCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QWaylandShell::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QWaylandShell10metaObjectEv(
    const QWaylandShell *self) {
  return self->metaObject();
}

//  void *QWaylandShell::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN13QWaylandShell11qt_metacastEPKc(
    QWaylandShell *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QWaylandShell::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN13QWaylandShell11qt_metacallEN11QMetaObject4CallEiPPv(
    QWaylandShell *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QWaylandShell::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QWaylandShell2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QWaylandShell::tr(s, c, n));
}

//  QWaylandShellPrivate *QWaylandShell::d_func()
extern "C" Q_DECL_EXPORT
QWaylandShellPrivate *ritual_ZN13QWaylandShell6d_funcEv(
    QWaylandShell *self) {
  return self->d_func();
}

//  const QWaylandShellPrivate *QWaylandShell::d_func() const
extern "C" Q_DECL_EXPORT
const QWaylandShellPrivate *ritual_ZNK13QWaylandShell6d_funcEv(
    const QWaylandShell *self) {
  return self->d_func();
}

//  void QWaylandShell::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QWaylandShell24qt_qmlMarker_uncreatableEv(
    QWaylandShell *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QWaylandShell::QWaylandShell()
extern "C" Q_DECL_EXPORT
QWaylandShell *ritual_ZN13QWaylandShellC1Ev() {
  return new CuteQWaylandShell();
}

//  QWaylandShell::QWaylandShell(QWaylandObject *waylandObject)
extern "C" Q_DECL_EXPORT
QWaylandShell *ritual_ZN13QWaylandShellC1EP14QWaylandObject(
    QWaylandObject *waylandObject) {
  return new CuteQWaylandShell(waylandObject);
}

//  FocusPolicy QWaylandShell::focusPolicy() const
extern "C" Q_DECL_EXPORT
QWaylandShell::FocusPolicy ritual_ZNK13QWaylandShell11focusPolicyEv(
    const QWaylandShell *self) {
  return self->focusPolicy();
}

//  void QWaylandShell::setFocusPolicy(FocusPolicy focusPolicy)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QWaylandShell14setFocusPolicyENS_11FocusPolicyE(
    QWaylandShell *self,
    QWaylandShell::FocusPolicy focusPolicy) {
  self->setFocusPolicy(focusPolicy);
}

//  void QWaylandShell::focusPolicyChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QWaylandShell18focusPolicyChangedEv(QWaylandShell *self) {
  self->focusPolicyChanged();
}

//  QWaylandShell::QWaylandShell(QWaylandShellPrivate &dd)
extern "C" Q_DECL_EXPORT
QWaylandShell *ritual_ZN13QWaylandShellC1ER20QWaylandShellPrivate(
    QWaylandShellPrivate *dd) {
  return new CuteQWaylandShell(*dd);
}

//  QWaylandShell::QWaylandShell(QWaylandObject *container,
//      QWaylandShellPrivate &dd)
extern "C" Q_DECL_EXPORT
QWaylandShell *ritual_ZN13QWaylandShellC1EP14QWaylandObjectR20QWaylandShellPrivate(
    QWaylandObject *container,
    QWaylandShellPrivate *dd) {
  return new CuteQWaylandShell(container, *dd);
}

//  a Python function taken by a CuteQWaylandShell, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWaylandShell(
    QWaylandShell *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWaylandShell *>(self)->take(key, call);
}
