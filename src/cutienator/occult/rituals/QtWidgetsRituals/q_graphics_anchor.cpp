//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qgraphicsanchorlayout.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#if QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
#include <QtWidgets/qgraphicsanchorlayout.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QGraphicsAnchor that Python can take functions over in. Every QGraphicsAnchor
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQGraphicsAnchorCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQGraphicsAnchorCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGraphicsAnchorCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGraphicsAnchorCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGraphicsAnchorCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGraphicsAnchorCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGraphicsAnchorCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQGraphicsAnchor : public QGraphicsAnchor {
public:
  using QGraphicsAnchor::QGraphicsAnchor;
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
      CuteQGraphicsAnchorCall0 call = reinterpret_cast<CuteQGraphicsAnchorCall0>(taken[0]);
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
      CuteQGraphicsAnchorCall1 call = reinterpret_cast<CuteQGraphicsAnchorCall1>(taken[1]);
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
      CuteQGraphicsAnchorCall2 call = reinterpret_cast<CuteQGraphicsAnchorCall2>(taken[2]);
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
      CuteQGraphicsAnchorCall3 call = reinterpret_cast<CuteQGraphicsAnchorCall3>(taken[3]);
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
      CuteQGraphicsAnchorCall4 call = reinterpret_cast<CuteQGraphicsAnchorCall4>(taken[4]);
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
      CuteQGraphicsAnchorCall5 call = reinterpret_cast<CuteQGraphicsAnchorCall5>(taken[5]);
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
      CuteQGraphicsAnchorCall6 call = reinterpret_cast<CuteQGraphicsAnchorCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QGraphicsAnchor::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QGraphicsAnchor10metaObjectEv(
    const QGraphicsAnchor *self) {
  return self->metaObject();
}

//  void *QGraphicsAnchor::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN15QGraphicsAnchor11qt_metacastEPKc(
    QGraphicsAnchor *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QGraphicsAnchor::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN15QGraphicsAnchor11qt_metacallEN11QMetaObject4CallEiPPv(
    QGraphicsAnchor *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QGraphicsAnchor::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QGraphicsAnchor2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QGraphicsAnchor::tr(s, c, n));
}

//  void QGraphicsAnchor::setSpacing(qreal spacing)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsAnchor10setSpacingEd(
    QGraphicsAnchor *self,
    qreal spacing) {
  self->setSpacing(spacing);
}

//  void QGraphicsAnchor::unsetSpacing()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsAnchor12unsetSpacingEv(QGraphicsAnchor *self) {
  self->unsetSpacing();
}

//  qreal QGraphicsAnchor::spacing() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QGraphicsAnchor7spacingEv(const QGraphicsAnchor *self) {
  return self->spacing();
}

//  void QGraphicsAnchor::setSizePolicy(QSizePolicy::Policy policy)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsAnchor13setSizePolicyEN11QSizePolicy6PolicyE(
    QGraphicsAnchor *self,
    QSizePolicy::Policy policy) {
  self->setSizePolicy(policy);
}

//  QSizePolicy::Policy QGraphicsAnchor::sizePolicy() const
extern "C" Q_DECL_EXPORT
QSizePolicy::Policy ritual_ZNK15QGraphicsAnchor10sizePolicyEv(
    const QGraphicsAnchor *self) {
  return self->sizePolicy();
}

//  QGraphicsAnchor::~QGraphicsAnchor()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsAnchorD1Ev(QGraphicsAnchor *self) {
  delete self;
}

//  QGraphicsAnchor::QGraphicsAnchor(QGraphicsAnchorLayout *parent)
extern "C" Q_DECL_EXPORT
QGraphicsAnchor *ritual_ZN15QGraphicsAnchorC1EP21QGraphicsAnchorLayout(
    QGraphicsAnchorLayout *parent) {
  return new CuteQGraphicsAnchor(parent);
}

//  QGraphicsAnchorPrivate *QGraphicsAnchor::d_func()
extern "C" Q_DECL_EXPORT
QGraphicsAnchorPrivate *ritual_ZN15QGraphicsAnchor6d_funcEv(
    QGraphicsAnchor *self) {
  return self->d_func();
}

//  const QGraphicsAnchorPrivate *QGraphicsAnchor::d_func() const
extern "C" Q_DECL_EXPORT
const QGraphicsAnchorPrivate *ritual_ZNK15QGraphicsAnchor6d_funcEv(
    const QGraphicsAnchor *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQGraphicsAnchor, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGraphicsAnchor(
    QGraphicsAnchor *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGraphicsAnchor *>(self)->take(key, call);
}

#endif  // QT_CONFIG(graphicsview)
#endif  // QT_CONFIG(graphicsview)
