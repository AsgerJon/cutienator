//  Written by dev_tooling.RitualGenerator from the records of
//  QtWaylandCompositor/qwaylandcompositorextension.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtWaylandCompositor/qwaylandcompositorextension.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on QWaylandCompositorExtension may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQWaylandCompositorExtension : QWaylandCompositorExtension {
  using QWaylandCompositorExtension::event;
};

//  A QWaylandCompositorExtension that Python can take functions over in. Every QWaylandCompositorExtension
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQWaylandCompositorExtensionCall0)(const void *, int *);
typedef void * (*CuteQWaylandCompositorExtensionCall1)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWaylandCompositorExtensionCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWaylandCompositorExtensionCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandCompositorExtensionCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandCompositorExtensionCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandCompositorExtensionCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandCompositorExtensionCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandCompositorExtensionCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQWaylandCompositorExtension : public QWaylandCompositorExtension {
public:
  using QWaylandCompositorExtension::QWaylandCompositorExtension;
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
      CuteQWaylandCompositorExtensionCall0 call = reinterpret_cast<CuteQWaylandCompositorExtensionCall0>(taken[0]);
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
      CuteQWaylandCompositorExtensionCall1 call = reinterpret_cast<CuteQWaylandCompositorExtensionCall1>(taken[1]);
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
      CuteQWaylandCompositorExtensionCall2 call = reinterpret_cast<CuteQWaylandCompositorExtensionCall2>(taken[2]);
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
      CuteQWaylandCompositorExtensionCall3 call = reinterpret_cast<CuteQWaylandCompositorExtensionCall3>(taken[3]);
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
      CuteQWaylandCompositorExtensionCall4 call = reinterpret_cast<CuteQWaylandCompositorExtensionCall4>(taken[4]);
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
      CuteQWaylandCompositorExtensionCall5 call = reinterpret_cast<CuteQWaylandCompositorExtensionCall5>(taken[5]);
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
      CuteQWaylandCompositorExtensionCall6 call = reinterpret_cast<CuteQWaylandCompositorExtensionCall6>(taken[6]);
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
      CuteQWaylandCompositorExtensionCall7 call = reinterpret_cast<CuteQWaylandCompositorExtensionCall7>(taken[7]);
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
      CuteQWaylandCompositorExtensionCall8 call = reinterpret_cast<CuteQWaylandCompositorExtensionCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QWaylandCompositorExtension::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK27QWaylandCompositorExtension10metaObjectEv(
    const QWaylandCompositorExtension *self) {
  return self->metaObject();
}

//  void *QWaylandCompositorExtension::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN27QWaylandCompositorExtension11qt_metacastEPKc(
    QWaylandCompositorExtension *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QWaylandCompositorExtension::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN27QWaylandCompositorExtension11qt_metacallEN11QMetaObject4CallEiPPv(
    QWaylandCompositorExtension *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QWaylandCompositorExtension::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN27QWaylandCompositorExtension2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QWaylandCompositorExtension::tr(s, c, n));
}

//  QWaylandCompositorExtensionPrivate *QWaylandCompositorExtension::d_func()
extern "C" Q_DECL_EXPORT
QWaylandCompositorExtensionPrivate *ritual_ZN27QWaylandCompositorExtension6d_funcEv(
    QWaylandCompositorExtension *self) {
  return self->d_func();
}

//  const QWaylandCompositorExtensionPrivate
//      *QWaylandCompositorExtension::d_func() const
extern "C" Q_DECL_EXPORT
const QWaylandCompositorExtensionPrivate *ritual_ZNK27QWaylandCompositorExtension6d_funcEv(
    const QWaylandCompositorExtension *self) {
  return self->d_func();
}

//  void QWaylandCompositorExtension::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QWaylandCompositorExtension24qt_qmlMarker_uncreatableEv(
    QWaylandCompositorExtension *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QWaylandCompositorExtension::QWaylandCompositorExtension()
extern "C" Q_DECL_EXPORT
QWaylandCompositorExtension *ritual_ZN27QWaylandCompositorExtensionC1Ev() {
  return new CuteQWaylandCompositorExtension();
}

//  QWaylandCompositorExtension::QWaylandCompositorExtension(QWaylandObject
//      *container)
extern "C" Q_DECL_EXPORT
QWaylandCompositorExtension *ritual_ZN27QWaylandCompositorExtensionC1EP14QWaylandObject(
    QWaylandObject *container) {
  return new CuteQWaylandCompositorExtension(container);
}

//  QWaylandCompositorExtension::~QWaylandCompositorExtension()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QWaylandCompositorExtensionD1Ev(
    QWaylandCompositorExtension *self) {
  delete self;
}

//  QWaylandObject *QWaylandCompositorExtension::extensionContainer() const
extern "C" Q_DECL_EXPORT
QWaylandObject *ritual_ZNK27QWaylandCompositorExtension18extensionContainerEv(
    const QWaylandCompositorExtension *self) {
  return self->extensionContainer();
}

//  void QWaylandCompositorExtension::setExtensionContainer(QWaylandObject
//      *container)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QWaylandCompositorExtension21setExtensionContainerEP14QWaylandObject(
    QWaylandCompositorExtension *self,
    QWaylandObject *container) {
  self->setExtensionContainer(container);
}

//  void QWaylandCompositorExtension::initialize()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QWaylandCompositorExtension10initializeEv(
    QWaylandCompositorExtension *self) {
  self->initialize();
}

//  bool QWaylandCompositorExtension::isInitialized() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK27QWaylandCompositorExtension13isInitializedEv(
    const QWaylandCompositorExtension *self) {
  return self->isInitialized();
}

//  const struct wl_interface
//      *QWaylandCompositorExtension::extensionInterface() const
extern "C" Q_DECL_EXPORT
const struct wl_interface *ritual_ZNK27QWaylandCompositorExtension18extensionInterfaceEv(
    const QWaylandCompositorExtension *self) {
  return self->extensionInterface();
}

//  QWaylandCompositorExtension::QWaylandCompositorExtension(QWaylandComposit
//      orExtensionPrivate &dd)
extern "C" Q_DECL_EXPORT
QWaylandCompositorExtension *ritual_ZN27QWaylandCompositorExtensionC1ER34QWaylandCompositorExtensionPrivate(
    QWaylandCompositorExtensionPrivate *dd) {
  return new CuteQWaylandCompositorExtension(*dd);
}

//  QWaylandCompositorExtension::QWaylandCompositorExtension(QWaylandObject
//      *container, QWaylandCompositorExtensionPrivate &dd)
extern "C" Q_DECL_EXPORT
QWaylandCompositorExtension *ritual_ZN27QWaylandCompositorExtensionC1EP14QWaylandObjectR34QWaylandCompositorExtensionPrivate(
    QWaylandObject *container,
    QWaylandCompositorExtensionPrivate *dd) {
  return new CuteQWaylandCompositorExtension(container, *dd);
}

//  bool QWaylandCompositorExtension::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN27QWaylandCompositorExtension5eventEP6QEvent(
    QWaylandCompositorExtension *self,
    QEvent *event) {
  return self->event(event);
}

//  a Python function taken by a CuteQWaylandCompositorExtension, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWaylandCompositorExtension(
    QWaylandCompositorExtension *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWaylandCompositorExtension *>(self)->take(key, call);
}

//  void QWaylandCompositorExtension::initialize()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27QWaylandCompositorExtension10initializeEv(
    QWaylandCompositorExtension *self) {
  self->QWaylandCompositorExtension::initialize();
}

//  bool QWaylandCompositorExtension::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN27QWaylandCompositorExtension5eventEP6QEvent(
    QWaylandCompositorExtension *self,
    QEvent *event) {
  return static_cast<OwnQWaylandCompositorExtension *>(self)->OwnQWaylandCompositorExtension::event(
      event);
}

//  QList<QWaylandCompositorExtension *>::QList()
extern "C" Q_DECL_EXPORT
QList<QWaylandCompositorExtension *> *ritual_list_make_QWaylandCompositorExtension_ptr() {
  return new QList<QWaylandCompositorExtension *>();
}

//  void QList<QWaylandCompositorExtension *>::append(const
//      QWaylandCompositorExtension * &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QWaylandCompositorExtension_ptr(
    QList<QWaylandCompositorExtension *> *self,
    QWaylandCompositorExtension *element) {
  self->append(element);
}

//  qsizetype QList<QWaylandCompositorExtension *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QWaylandCompositorExtension_ptr(
    const QList<QWaylandCompositorExtension *> *self) {
  return self->size();
}

//  const QWaylandCompositorExtension * &QList<QWaylandCompositorExtension
//      *>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QWaylandCompositorExtension *ritual_list_at_QWaylandCompositorExtension_ptr(
    const QList<QWaylandCompositorExtension *> *self,
    long long index) {
  return self->at(index);
}

//  QList<QWaylandCompositorExtension *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QWaylandCompositorExtension_ptr(
    QList<QWaylandCompositorExtension *> *self) {
  delete self;
}
