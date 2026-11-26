//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickControls2/qquickattachedpropertypropagator.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuickControls2/QtQuickControls2>
#include <QtQuickControls2/qquickattachedpropertypropagator.h>
#include <QtCore/qstring.h>
#include <QtCore/qdebug.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on QQuickAttachedPropertyPropagator may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickAttachedPropertyPropagator : QQuickAttachedPropertyPropagator {
  using QQuickAttachedPropertyPropagator::attachedParentChange;
};

//  A QQuickAttachedPropertyPropagator that Python can take functions over in. Every QQuickAttachedPropertyPropagator
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickAttachedPropertyPropagatorCall0)(const void *, QQuickAttachedPropertyPropagator *, QQuickAttachedPropertyPropagator *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickAttachedPropertyPropagatorCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickAttachedPropertyPropagatorCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickAttachedPropertyPropagatorCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickAttachedPropertyPropagatorCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickAttachedPropertyPropagatorCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickAttachedPropertyPropagatorCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickAttachedPropertyPropagatorCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickAttachedPropertyPropagator : public QQuickAttachedPropertyPropagator {
public:
  using QQuickAttachedPropertyPropagator::QQuickAttachedPropertyPropagator;
  void *taken[8] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN32QQuickAttachedPropertyPropagator20attachedParentChangeEPS_S0_")) {
      taken[0] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QQuickAttachedPropertyPropagator::attachedParentChange(QQuickAtt
  //      achedPropertyPropagator *newParent,
  //      QQuickAttachedPropertyPropagator *oldParent)
  void attachedParentChange(
      QQuickAttachedPropertyPropagator *newParent,
      QQuickAttachedPropertyPropagator *oldParent) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickAttachedPropertyPropagatorCall0 call = reinterpret_cast<CuteQQuickAttachedPropertyPropagatorCall0>(taken[0]);
      call(this, newParent, oldParent, &handled);
      if (handled) return;
    }
    QQuickAttachedPropertyPropagator::attachedParentChange(newParent, oldParent);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickAttachedPropertyPropagatorCall1 call = reinterpret_cast<CuteQQuickAttachedPropertyPropagatorCall1>(taken[1]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickAttachedPropertyPropagatorCall2 call = reinterpret_cast<CuteQQuickAttachedPropertyPropagatorCall2>(taken[2]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickAttachedPropertyPropagatorCall3 call = reinterpret_cast<CuteQQuickAttachedPropertyPropagatorCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickAttachedPropertyPropagatorCall4 call = reinterpret_cast<CuteQQuickAttachedPropertyPropagatorCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickAttachedPropertyPropagatorCall5 call = reinterpret_cast<CuteQQuickAttachedPropertyPropagatorCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickAttachedPropertyPropagatorCall6 call = reinterpret_cast<CuteQQuickAttachedPropertyPropagatorCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickAttachedPropertyPropagatorCall7 call = reinterpret_cast<CuteQQuickAttachedPropertyPropagatorCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickAttachedPropertyPropagator::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK32QQuickAttachedPropertyPropagator10metaObjectEv(
    const QQuickAttachedPropertyPropagator *self) {
  return self->metaObject();
}

//  void *QQuickAttachedPropertyPropagator::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN32QQuickAttachedPropertyPropagator11qt_metacastEPKc(
    QQuickAttachedPropertyPropagator *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickAttachedPropertyPropagator::qt_metacall(QMetaObject::Call a0,
//      int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN32QQuickAttachedPropertyPropagator11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickAttachedPropertyPropagator *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickAttachedPropertyPropagator::tr(const char *s, const char
//      *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN32QQuickAttachedPropertyPropagator2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickAttachedPropertyPropagator::tr(s, c, n));
}

//  QQuickAttachedPropertyPropagator::QQuickAttachedPropertyPropagator(QObjec
//      t *parent)
extern "C" Q_DECL_EXPORT
QQuickAttachedPropertyPropagator *ritual_ZN32QQuickAttachedPropertyPropagatorC1EP7QObject(
    QObject *parent) {
  return new CuteQQuickAttachedPropertyPropagator(parent);
}

//  QQuickAttachedPropertyPropagator::~QQuickAttachedPropertyPropagator()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuickAttachedPropertyPropagatorD1Ev(
    QQuickAttachedPropertyPropagator *self) {
  delete self;
}

//  QList<QQuickAttachedPropertyPropagator *>
//      QQuickAttachedPropertyPropagator::attachedChildren() const
extern "C" Q_DECL_EXPORT
QList<QQuickAttachedPropertyPropagator *> *ritual_ZNK32QQuickAttachedPropertyPropagator16attachedChildrenEv(
    const QQuickAttachedPropertyPropagator *self) {
  return new QList<QQuickAttachedPropertyPropagator *>(
      self->attachedChildren());
}

//  QQuickAttachedPropertyPropagator
//      *QQuickAttachedPropertyPropagator::attachedParent() const
extern "C" Q_DECL_EXPORT
QQuickAttachedPropertyPropagator *ritual_ZNK32QQuickAttachedPropertyPropagator14attachedParentEv(
    const QQuickAttachedPropertyPropagator *self) {
  return self->attachedParent();
}

//  void QQuickAttachedPropertyPropagator::initialize()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuickAttachedPropertyPropagator10initializeEv(
    QQuickAttachedPropertyPropagator *self) {
  self->initialize();
}

//  void QQuickAttachedPropertyPropagator::attachedParentChange(QQuickAttache
//      dPropertyPropagator *newParent, QQuickAttachedPropertyPropagator
//      *oldParent)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuickAttachedPropertyPropagator20attachedParentChangeEPS_S0_(
    QQuickAttachedPropertyPropagator *self,
    QQuickAttachedPropertyPropagator *newParent,
    QQuickAttachedPropertyPropagator *oldParent) {
  self->attachedParentChange(newParent, oldParent);
}

#if !defined(QT_NO_DEBUG_STREAM)
//  QDebug operator<<(QDebug debug, const QQuickAttachedPropertyPropagator
//      *propagator)
extern "C" Q_DECL_EXPORT
QDebug *ritual_Zls6QDebugPK32QQuickAttachedPropertyPropagator(
    const QDebug *debug,
    const QQuickAttachedPropertyPropagator *propagator) {
  return new QDebug(operator<<(*debug, propagator));
}
#endif  // !defined(QT_NO_DEBUG_STREAM)

//  QQuickAttachedPropertyPropagatorPrivate
//      *QQuickAttachedPropertyPropagator::d_func()
extern "C" Q_DECL_EXPORT
QQuickAttachedPropertyPropagatorPrivate *ritual_ZN32QQuickAttachedPropertyPropagator6d_funcEv(
    QQuickAttachedPropertyPropagator *self) {
  return self->d_func();
}

//  const QQuickAttachedPropertyPropagatorPrivate
//      *QQuickAttachedPropertyPropagator::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickAttachedPropertyPropagatorPrivate *ritual_ZNK32QQuickAttachedPropertyPropagator6d_funcEv(
    const QQuickAttachedPropertyPropagator *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQQuickAttachedPropertyPropagator, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickAttachedPropertyPropagator(
    QQuickAttachedPropertyPropagator *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickAttachedPropertyPropagator *>(self)->take(key, call);
}

//  void QQuickAttachedPropertyPropagator::attachedParentChange(QQuickAttache
//      dPropertyPropagator *newParent, QQuickAttachedPropertyPropagator
//      *oldParent)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN32QQuickAttachedPropertyPropagator20attachedParentChangeEPS_S0_(
    QQuickAttachedPropertyPropagator *self,
    QQuickAttachedPropertyPropagator *newParent,
    QQuickAttachedPropertyPropagator *oldParent) {
  static_cast<OwnQQuickAttachedPropertyPropagator *>(self)->OwnQQuickAttachedPropertyPropagator::attachedParentChange(
      newParent,
      oldParent);
}

//  QList<QQuickAttachedPropertyPropagator *>::QList()
extern "C" Q_DECL_EXPORT
QList<QQuickAttachedPropertyPropagator *> *ritual_list_make_QQuickAttachedPropertyPropagator_ptr() {
  return new QList<QQuickAttachedPropertyPropagator *>();
}

//  void QList<QQuickAttachedPropertyPropagator *>::append(const
//      QQuickAttachedPropertyPropagator * &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QQuickAttachedPropertyPropagator_ptr(
    QList<QQuickAttachedPropertyPropagator *> *self,
    QQuickAttachedPropertyPropagator *element) {
  self->append(element);
}

//  qsizetype QList<QQuickAttachedPropertyPropagator *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QQuickAttachedPropertyPropagator_ptr(
    const QList<QQuickAttachedPropertyPropagator *> *self) {
  return self->size();
}

//  const QQuickAttachedPropertyPropagator *
//      &QList<QQuickAttachedPropertyPropagator *>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QQuickAttachedPropertyPropagator *ritual_list_at_QQuickAttachedPropertyPropagator_ptr(
    const QList<QQuickAttachedPropertyPropagator *> *self,
    long long index) {
  return self->at(index);
}

//  QList<QQuickAttachedPropertyPropagator *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QQuickAttachedPropertyPropagator_ptr(
    QList<QQuickAttachedPropertyPropagator *> *self) {
  delete self;
}
