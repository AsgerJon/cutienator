//  Written by dev_tooling.RitualGenerator from the records of
//  QtWaylandCompositor/qwaylandshellsurface.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtWaylandCompositor/qwaylandshellsurface.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QWaylandShellSurface that Python can take functions over in. Every QWaylandShellSurface
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(wayland_compositor_quick)
typedef void * (*CuteQWaylandShellSurfaceCall0)(const void *, QWaylandQuickShellSurfaceItem *, int *);
#endif  // QT_CONFIG(wayland_compositor_quick)
typedef int (*CuteQWaylandShellSurfaceCall1)(const void *, int *);
typedef void (*CuteQWaylandShellSurfaceCall2)(const void *, int *);
typedef void * (*CuteQWaylandShellSurfaceCall3)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWaylandShellSurfaceCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWaylandShellSurfaceCall5)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandShellSurfaceCall6)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandShellSurfaceCall7)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandShellSurfaceCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandShellSurfaceCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandShellSurfaceCall10)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQWaylandShellSurface : public QWaylandShellSurface {
public:
  using QWaylandShellSurface::QWaylandShellSurface;
  void *taken[11] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(wayland_compositor_quick)
    if (!std::strcmp(key, "_ZN20QWaylandShellSurface17createIntegrationEP29QWaylandQuickShellSurfaceItem")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(wayland_compositor_quick)
    if (!std::strcmp(key, "_ZNK20QWaylandShellSurface10windowTypeEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN27QWaylandCompositorExtension10initializeEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK27QWaylandCompositorExtension18extensionInterfaceEv")) {
      taken[3] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if QT_CONFIG(wayland_compositor_quick)
  //  QWaylandQuickShellIntegration *QWaylandShellSurface::createIntegratio
  //      n(QWaylandQuickShellSurfaceItem *item)
  QWaylandQuickShellIntegration *createIntegration(
      QWaylandQuickShellSurfaceItem *item) override {
    if (taken[0]) {
      int handled = 0;
      CuteQWaylandShellSurfaceCall0 call = reinterpret_cast<CuteQWaylandShellSurfaceCall0>(taken[0]);
      void * given = call(this, item, &handled);
      if (handled) return static_cast<QWaylandQuickShellIntegration *>(given);
    }
    return {};
  }
#endif  // QT_CONFIG(wayland_compositor_quick)

  //  Qt::WindowType QWaylandShellSurface::windowType() const
  Qt::WindowType windowType() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQWaylandShellSurfaceCall1 call = reinterpret_cast<CuteQWaylandShellSurfaceCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return static_cast<Qt::WindowType>(given);
    }
    return QWaylandShellSurface::windowType();
  }

  //  void QWaylandCompositorExtension::initialize()
  void initialize() override {
    if (taken[2]) {
      int handled = 0;
      CuteQWaylandShellSurfaceCall2 call = reinterpret_cast<CuteQWaylandShellSurfaceCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QWaylandCompositorExtension::initialize();
  }

  //  const struct wl_interface
  //      *QWaylandCompositorExtension::extensionInterface() const
  const struct wl_interface *extensionInterface() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQWaylandShellSurfaceCall3 call = reinterpret_cast<CuteQWaylandShellSurfaceCall3>(taken[3]);
      void * given = call(this, &handled);
      if (handled) return static_cast<const struct wl_interface *>(given);
    }
    return {};
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QWaylandCompositorExtension::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQWaylandShellSurfaceCall4 call = reinterpret_cast<CuteQWaylandShellSurfaceCall4>(taken[4]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QWaylandCompositorExtension::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQWaylandShellSurfaceCall5 call = reinterpret_cast<CuteQWaylandShellSurfaceCall5>(taken[5]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQWaylandShellSurfaceCall6 call = reinterpret_cast<CuteQWaylandShellSurfaceCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQWaylandShellSurfaceCall7 call = reinterpret_cast<CuteQWaylandShellSurfaceCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQWaylandShellSurfaceCall8 call = reinterpret_cast<CuteQWaylandShellSurfaceCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[9]) {
      int handled = 0;
      CuteQWaylandShellSurfaceCall9 call = reinterpret_cast<CuteQWaylandShellSurfaceCall9>(taken[9]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[10]) {
      int handled = 0;
      CuteQWaylandShellSurfaceCall10 call = reinterpret_cast<CuteQWaylandShellSurfaceCall10>(taken[10]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QWaylandShellSurface::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QWaylandShellSurface10metaObjectEv(
    const QWaylandShellSurface *self) {
  return self->metaObject();
}

//  void *QWaylandShellSurface::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN20QWaylandShellSurface11qt_metacastEPKc(
    QWaylandShellSurface *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QWaylandShellSurface::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN20QWaylandShellSurface11qt_metacallEN11QMetaObject4CallEiPPv(
    QWaylandShellSurface *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QWaylandShellSurface::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QWaylandShellSurface2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QWaylandShellSurface::tr(s, c, n));
}

//  QWaylandShellSurfacePrivate *QWaylandShellSurface::d_func()
extern "C" Q_DECL_EXPORT
QWaylandShellSurfacePrivate *ritual_ZN20QWaylandShellSurface6d_funcEv(
    QWaylandShellSurface *self) {
  return self->d_func();
}

//  const QWaylandShellSurfacePrivate *QWaylandShellSurface::d_func() const
extern "C" Q_DECL_EXPORT
const QWaylandShellSurfacePrivate *ritual_ZNK20QWaylandShellSurface6d_funcEv(
    const QWaylandShellSurface *self) {
  return self->d_func();
}

//  void QWaylandShellSurface::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QWaylandShellSurface24qt_qmlMarker_uncreatableEv(
    QWaylandShellSurface *self) {
  self->qt_qmlMarker_uncreatable();
}

#if QT_CONFIG(wayland_compositor_quick)
//  QWaylandQuickShellIntegration
//      *QWaylandShellSurface::createIntegration(QWaylandQuickShellSurfaceIte
//      m *item)
extern "C" Q_DECL_EXPORT
QWaylandQuickShellIntegration *ritual_ZN20QWaylandShellSurface17createIntegrationEP29QWaylandQuickShellSurfaceItem(
    QWaylandShellSurface *self,
    QWaylandQuickShellSurfaceItem *item) {
  return self->createIntegration(item);
}
#endif  // QT_CONFIG(wayland_compositor_quick)

//  QWaylandShellSurface::QWaylandShellSurface(QWaylandObject *waylandObject)
extern "C" Q_DECL_EXPORT
QWaylandShellSurface *ritual_ZN20QWaylandShellSurfaceC1EP14QWaylandObject(
    QWaylandObject *waylandObject) {
  return new CuteQWaylandShellSurface(waylandObject);
}

//  Qt::WindowType QWaylandShellSurface::windowType() const
extern "C" Q_DECL_EXPORT
Qt::WindowType ritual_ZNK20QWaylandShellSurface10windowTypeEv(
    const QWaylandShellSurface *self) {
  return self->windowType();
}

//  bool QWaylandShellSurface::isModal() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QWaylandShellSurface7isModalEv(
    const QWaylandShellSurface *self) {
  return self->isModal();
}

//  QWaylandShellSurface::QWaylandShellSurface(QWaylandShellSurfacePrivate
//      &dd)
extern "C" Q_DECL_EXPORT
QWaylandShellSurface *ritual_ZN20QWaylandShellSurfaceC1ER27QWaylandShellSurfacePrivate(
    QWaylandShellSurfacePrivate *dd) {
  return new CuteQWaylandShellSurface(*dd);
}

//  QWaylandShellSurface::QWaylandShellSurface(QWaylandObject *container,
//      QWaylandShellSurfacePrivate &dd)
extern "C" Q_DECL_EXPORT
QWaylandShellSurface *ritual_ZN20QWaylandShellSurfaceC1EP14QWaylandObjectR27QWaylandShellSurfacePrivate(
    QWaylandObject *container,
    QWaylandShellSurfacePrivate *dd) {
  return new CuteQWaylandShellSurface(container, *dd);
}

//  void QWaylandShellSurface::setModal(bool newModal)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QWaylandShellSurface8setModalEb(
    QWaylandShellSurface *self,
    bool newModal) {
  self->setModal(newModal);
}

//  void QWaylandShellSurface::windowTypeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QWaylandShellSurface17windowTypeChangedEv(
    QWaylandShellSurface *self) {
  self->windowTypeChanged();
}

//  void QWaylandShellSurface::modalChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QWaylandShellSurface12modalChangedEv(
    QWaylandShellSurface *self) {
  self->modalChanged();
}

//  a Python function taken by a CuteQWaylandShellSurface, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWaylandShellSurface(
    QWaylandShellSurface *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWaylandShellSurface *>(self)->take(key, call);
}

//  Qt::WindowType QWaylandShellSurface::windowType() const
extern "C" Q_DECL_EXPORT
Qt::WindowType ritual_own_ZNK20QWaylandShellSurface10windowTypeEv(
    const QWaylandShellSurface *self) {
  return self->QWaylandShellSurface::windowType();
}
