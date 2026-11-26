//  Written by hand on 2026-11-25 from
//  Qt3DQuick/6.12.0/Qt3DQuick/private/quick3dnodeinstantiator_p.h,
//  Qt 6.12.0, from Qt's source. Kept as it is when the generator runs
//  again.
//  Not written: 'qt_metacast', and the 'Q_PRIVATE_SLOT' functions of
//  the private class, which are not of this class.
#include <Qt3DQuick/6.12.0/Qt3DQuick/private/qt3dquick_global_p.h>
#include <Qt3DQuick/Qt3DQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DQuick/6.12.0/Qt3DQuick/private/quick3dnodeinstantiator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtQml/qqmlcomponent.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DCore::Quick::Quick3DNodeInstantiator that Python can take
//  functions over in. Every Qt3DCore::Quick::Quick3DNodeInstantiator
//  Python makes is one. Each function below asks the Python function
//  handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DCore_Quick_Quick3DNodeInstantiatorCall0)(const void *, int *);
typedef void (*CuteQt3DCore_Quick_Quick3DNodeInstantiatorCall1)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DCore_Quick_Quick3DNodeInstantiatorCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DCore_Quick_Quick3DNodeInstantiatorCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_Quick_Quick3DNodeInstantiatorCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_Quick_Quick3DNodeInstantiatorCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_Quick_Quick3DNodeInstantiatorCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_Quick_Quick3DNodeInstantiatorCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_Quick_Quick3DNodeInstantiatorCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DCore_Quick_Quick3DNodeInstantiator : public Qt3DCore::Quick::Quick3DNodeInstantiator {
public:
  using Qt3DCore::Quick::Quick3DNodeInstantiator::Quick3DNodeInstantiator;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
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

  //  void Qt3DCore::Quick::Quick3DNodeInstantiator::classBegin()
  void classBegin() override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DCore_Quick_Quick3DNodeInstantiatorCall0 call = reinterpret_cast<CuteQt3DCore_Quick_Quick3DNodeInstantiatorCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::Quick::Quick3DNodeInstantiator::classBegin();
  }

  //  void Qt3DCore::Quick::Quick3DNodeInstantiator::componentComplete()
  void componentComplete() override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DCore_Quick_Quick3DNodeInstantiatorCall1 call = reinterpret_cast<CuteQt3DCore_Quick_Quick3DNodeInstantiatorCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::Quick::Quick3DNodeInstantiator::componentComplete();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQt3DCore_Quick_Quick3DNodeInstantiatorCall2 call = reinterpret_cast<CuteQt3DCore_Quick_Quick3DNodeInstantiatorCall2>(taken[2]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQt3DCore_Quick_Quick3DNodeInstantiatorCall3 call = reinterpret_cast<CuteQt3DCore_Quick_Quick3DNodeInstantiatorCall3>(taken[3]);
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
      CuteQt3DCore_Quick_Quick3DNodeInstantiatorCall4 call = reinterpret_cast<CuteQt3DCore_Quick_Quick3DNodeInstantiatorCall4>(taken[4]);
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
      CuteQt3DCore_Quick_Quick3DNodeInstantiatorCall5 call = reinterpret_cast<CuteQt3DCore_Quick_Quick3DNodeInstantiatorCall5>(taken[5]);
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
      CuteQt3DCore_Quick_Quick3DNodeInstantiatorCall6 call = reinterpret_cast<CuteQt3DCore_Quick_Quick3DNodeInstantiatorCall6>(taken[6]);
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
      CuteQt3DCore_Quick_Quick3DNodeInstantiatorCall7 call = reinterpret_cast<CuteQt3DCore_Quick_Quick3DNodeInstantiatorCall7>(taken[7]);
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
      CuteQt3DCore_Quick_Quick3DNodeInstantiatorCall8 call = reinterpret_cast<CuteQt3DCore_Quick_Quick3DNodeInstantiatorCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DCore::Quick::Quick3DNodeInstantiator::metaObject()
//      const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK8Qt3DCore5Quick23Quick3DNodeInstantiator10metaObjectEv(
    const Qt3DCore::Quick::Quick3DNodeInstantiator *self) {
  return self->metaObject();
}

//  QString Qt3DCore::Quick::Quick3DNodeInstantiator::tr(const char *s, const
//      char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN8Qt3DCore5Quick23Quick3DNodeInstantiator2trEPKcS3_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DCore::Quick::Quick3DNodeInstantiator::tr(s, c, n));
}

//  Qt3DCore::Quick::Quick3DNodeInstantiatorPrivate
//      *Qt3DCore::Quick::Quick3DNodeInstantiator::d_func()
extern "C" Q_DECL_EXPORT
Qt3DCore::Quick::Quick3DNodeInstantiatorPrivate *ritual_ZN8Qt3DCore5Quick23Quick3DNodeInstantiator6d_funcEv(
    Qt3DCore::Quick::Quick3DNodeInstantiator *self) {
  return self->d_func();
}

//  const Qt3DCore::Quick::Quick3DNodeInstantiatorPrivate
//      *Qt3DCore::Quick::Quick3DNodeInstantiator::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DCore::Quick::Quick3DNodeInstantiatorPrivate *ritual_ZNK8Qt3DCore5Quick23Quick3DNodeInstantiator6d_funcEv(
    const Qt3DCore::Quick::Quick3DNodeInstantiator *self) {
  return self->d_func();
}

//  Qt3DCore::Quick::Quick3DNodeInstantiator::Quick3DNodeInstantiator(QNode
//      *parent)
extern "C" Q_DECL_EXPORT
Qt3DCore::Quick::Quick3DNodeInstantiator *ritual_ZN8Qt3DCore5Quick23Quick3DNodeInstantiatorC1EPNS_5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DCore_Quick_Quick3DNodeInstantiator(parent);
}

//  bool Qt3DCore::Quick::Quick3DNodeInstantiator::isActive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8Qt3DCore5Quick23Quick3DNodeInstantiator8isActiveEv(
    const Qt3DCore::Quick::Quick3DNodeInstantiator *self) {
  return self->isActive();
}

//  void Qt3DCore::Quick::Quick3DNodeInstantiator::setActive(bool newVal)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore5Quick23Quick3DNodeInstantiator9setActiveEb(
    Qt3DCore::Quick::Quick3DNodeInstantiator *self,
    bool newVal) {
  self->setActive(newVal);
}

//  bool Qt3DCore::Quick::Quick3DNodeInstantiator::isAsync() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8Qt3DCore5Quick23Quick3DNodeInstantiator7isAsyncEv(
    const Qt3DCore::Quick::Quick3DNodeInstantiator *self) {
  return self->isAsync();
}

//  void Qt3DCore::Quick::Quick3DNodeInstantiator::setAsync(bool newVal)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore5Quick23Quick3DNodeInstantiator8setAsyncEb(
    Qt3DCore::Quick::Quick3DNodeInstantiator *self,
    bool newVal) {
  self->setAsync(newVal);
}

//  int Qt3DCore::Quick::Quick3DNodeInstantiator::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK8Qt3DCore5Quick23Quick3DNodeInstantiator5countEv(
    const Qt3DCore::Quick::Quick3DNodeInstantiator *self) {
  return self->count();
}

//  QQmlComponent *Qt3DCore::Quick::Quick3DNodeInstantiator::delegate()
extern "C" Q_DECL_EXPORT
QQmlComponent *ritual_ZN8Qt3DCore5Quick23Quick3DNodeInstantiator8delegateEv(
    Qt3DCore::Quick::Quick3DNodeInstantiator *self) {
  return self->delegate();
}

//  void Qt3DCore::Quick::Quick3DNodeInstantiator::setDelegate(QQmlComponent
//      *c)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore5Quick23Quick3DNodeInstantiator11setDelegateEP13QQmlComponent(
    Qt3DCore::Quick::Quick3DNodeInstantiator *self,
    QQmlComponent *c) {
  self->setDelegate(c);
}

//  QVariant Qt3DCore::Quick::Quick3DNodeInstantiator::model() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK8Qt3DCore5Quick23Quick3DNodeInstantiator5modelEv(
    const Qt3DCore::Quick::Quick3DNodeInstantiator *self) {
  return new QVariant(self->model());
}

//  void Qt3DCore::Quick::Quick3DNodeInstantiator::setModel(const QVariant
//      &v)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore5Quick23Quick3DNodeInstantiator8setModelERK8QVariant(
    Qt3DCore::Quick::Quick3DNodeInstantiator *self,
    const QVariant *v) {
  self->setModel(*v);
}

//  QObject *Qt3DCore::Quick::Quick3DNodeInstantiator::object() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK8Qt3DCore5Quick23Quick3DNodeInstantiator6objectEv(
    const Qt3DCore::Quick::Quick3DNodeInstantiator *self) {
  return self->object();
}

//  QObject *Qt3DCore::Quick::Quick3DNodeInstantiator::objectAt(int index)
//      const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK8Qt3DCore5Quick23Quick3DNodeInstantiator8objectAtEi(
    const Qt3DCore::Quick::Quick3DNodeInstantiator *self,
    int index) {
  return self->objectAt(index);
}

//  void Qt3DCore::Quick::Quick3DNodeInstantiator::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore5Quick23Quick3DNodeInstantiator10classBeginEv(
    Qt3DCore::Quick::Quick3DNodeInstantiator *self) {
  self->classBegin();
}

//  void Qt3DCore::Quick::Quick3DNodeInstantiator::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore5Quick23Quick3DNodeInstantiator17componentCompleteEv(
    Qt3DCore::Quick::Quick3DNodeInstantiator *self) {
  self->componentComplete();
}

//  void Qt3DCore::Quick::Quick3DNodeInstantiator::modelChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore5Quick23Quick3DNodeInstantiator12modelChangedEv(
    Qt3DCore::Quick::Quick3DNodeInstantiator *self) {
  self->modelChanged();
}

//  void Qt3DCore::Quick::Quick3DNodeInstantiator::delegateChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore5Quick23Quick3DNodeInstantiator15delegateChangedEv(
    Qt3DCore::Quick::Quick3DNodeInstantiator *self) {
  self->delegateChanged();
}

//  void Qt3DCore::Quick::Quick3DNodeInstantiator::countChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore5Quick23Quick3DNodeInstantiator12countChangedEv(
    Qt3DCore::Quick::Quick3DNodeInstantiator *self) {
  self->countChanged();
}

//  void Qt3DCore::Quick::Quick3DNodeInstantiator::objectChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore5Quick23Quick3DNodeInstantiator13objectChangedEv(
    Qt3DCore::Quick::Quick3DNodeInstantiator *self) {
  self->objectChanged();
}

//  void Qt3DCore::Quick::Quick3DNodeInstantiator::activeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore5Quick23Quick3DNodeInstantiator13activeChangedEv(
    Qt3DCore::Quick::Quick3DNodeInstantiator *self) {
  self->activeChanged();
}

//  void Qt3DCore::Quick::Quick3DNodeInstantiator::asynchronousChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore5Quick23Quick3DNodeInstantiator19asynchronousChangedEv(
    Qt3DCore::Quick::Quick3DNodeInstantiator *self) {
  self->asynchronousChanged();
}

//  void Qt3DCore::Quick::Quick3DNodeInstantiator::objectAdded(int index,
//      QObject *object)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore5Quick23Quick3DNodeInstantiator11objectAddedEiP7QObject(
    Qt3DCore::Quick::Quick3DNodeInstantiator *self,
    int index,
    QObject *object) {
  self->objectAdded(index, object);
}

//  void Qt3DCore::Quick::Quick3DNodeInstantiator::objectRemoved(int index,
//      QObject *object)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore5Quick23Quick3DNodeInstantiator13objectRemovedEiP7QObject(
    Qt3DCore::Quick::Quick3DNodeInstantiator *self,
    int index,
    QObject *object) {
  self->objectRemoved(index, object);
}

//  void Qt3DCore::Quick::Quick3DNodeInstantiator::onParentChanged(QObject
//      *parent)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore5Quick23Quick3DNodeInstantiator15onParentChangedEP7QObject(
    Qt3DCore::Quick::Quick3DNodeInstantiator *self,
    QObject *parent) {
  self->onParentChanged(parent);
}

//  a Python function taken by a CuteQt3DCore_Quick_Quick3DNodeInstantiator,
//      for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DCore_Quick_Quick3DNodeInstantiator(
    Qt3DCore::Quick::Quick3DNodeInstantiator *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DCore_Quick_Quick3DNodeInstantiator *>(self)->take(key, call);
}

//  Qt3DCore::Quick::Quick3DNodeInstantiator as the QQmlParserStatus it is
//      built on
extern "C" Q_DECL_EXPORT
QQmlParserStatus *ritual_cast_Qt3DCore_Quick_Quick3DNodeInstantiator_QQmlParserStatus(
    Qt3DCore::Quick::Quick3DNodeInstantiator *self) {
  return static_cast<QQmlParserStatus *>(self);
}

//  void Qt3DCore::Quick::Quick3DNodeInstantiator::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8Qt3DCore5Quick23Quick3DNodeInstantiator10classBeginEv(
    Qt3DCore::Quick::Quick3DNodeInstantiator *self) {
  self->Qt3DCore::Quick::Quick3DNodeInstantiator::classBegin();
}

//  void Qt3DCore::Quick::Quick3DNodeInstantiator::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8Qt3DCore5Quick23Quick3DNodeInstantiator17componentCompleteEv(
    Qt3DCore::Quick::Quick3DNodeInstantiator *self) {
  self->Qt3DCore::Quick::Quick3DNodeInstantiator::componentComplete();
}
