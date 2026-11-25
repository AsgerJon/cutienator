//  Written by hand on 2026-11-25 from
//  QtAxContainer/qaxobject.h, Qt 6.12.0, from Qt's source. Kept as it is
//  when the generator runs again. ActiveQt is built for Windows alone, as a
//  static library, so every function of it is compiled into ours.
//  'IUnknown', a COM interface of Windows, is passed as an address; a
//  'ulong' as the number Windows has. Not written: 'qt_metacall',
//  'qt_static_metacall' and 'qt_metacast', which the meta-object system
//  calls itself; and the templates of 'qobject_cast'. Its Cute class takes
//  no 'propertyWritable' or 'setPropertyWritable' over: they take a
//  'const char *', which is handed to no Python function.
#include <QtCore/qglobal.h>
#if defined(Q_OS_WIN)
#include <QtAxContainer/qaxobject.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QAxObject may call these functions of it. This one
//  is, and makes them free for the rituals to call.
struct OwnQAxObject : QAxObject {
  using QAxObject::connectNotify;
};

//  A QAxObject that Python can take functions over in. Every QAxObject
//  Python makes is one. Each function below asks the Python function handed
//  over for it, and runs Qt's own without one.
typedef ulong (*CuteQAxObjectCall0)(const void *, int *);
typedef void (*CuteQAxObjectCall1)(const void *, ulong, int *);
typedef QString * (*CuteQAxObjectCall2)(const void *, int *);
typedef bool (*CuteQAxObjectCall3)(const void *, const QString *, int *);
typedef void (*CuteQAxObjectCall4)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAxObjectCall5)(const void *, const QMetaMethod *, int *);
typedef bool (*CuteQAxObjectCall6)(const void *, QEvent *, int *);
typedef bool (*CuteQAxObjectCall7)(const void *, QObject *, QEvent *, int *);
typedef void (*CuteQAxObjectCall8)(const void *, QTimerEvent *, int *);
typedef void (*CuteQAxObjectCall9)(const void *, QChildEvent *, int *);
typedef void (*CuteQAxObjectCall10)(const void *, QEvent *, int *);
typedef void (*CuteQAxObjectCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAxObjectCall12)(const void *, IUnknown **, int *);
class CuteQAxObject : public QAxObject {
public:
  using QAxObject::QAxObject;
  void *taken[13] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK18QAxObjectInterface12classContextEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAxObjectInterface15setClassContextEm")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QAxObjectInterface7controlEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAxObjectInterface10setControlERK7QString")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAxObjectInterface12resetControlEv")) {
      taken[4] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QAxBase10initializeEPP8IUnknown")) {
      taken[12] = call;
      return true;
    }
    return false;
  }

  //  ulong QAxObject::classContext() const
  ulong classContext() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQAxObjectCall0 call = reinterpret_cast<CuteQAxObjectCall0>(taken[0]);
      ulong given = call(this, &handled);
      if (handled) return given;
    }
    return QAxObject::classContext();
  }

  //  void QAxObject::setClassContext(ulong classContext)
  void setClassContext(ulong classContext) override {
    if (taken[1]) {
      int handled = 0;
      CuteQAxObjectCall1 call = reinterpret_cast<CuteQAxObjectCall1>(taken[1]);
      call(this, classContext, &handled);
      if (handled) return;
    }
    QAxObject::setClassContext(classContext);
  }

  //  QString QAxObject::control() const
  QString control() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQAxObjectCall2 call = reinterpret_cast<CuteQAxObjectCall2>(taken[2]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QAxObject::control();
  }

  //  bool QAxObject::setControl(const QString &c)
  bool setControl(const QString &c) override {
    if (taken[3]) {
      int handled = 0;
      CuteQAxObjectCall3 call = reinterpret_cast<CuteQAxObjectCall3>(taken[3]);
      bool given = call(this, &c, &handled);
      if (handled) return given;
    }
    return QAxObject::setControl(c);
  }

  //  void QAxObject::resetControl()
  void resetControl() override {
    if (taken[4]) {
      int handled = 0;
      CuteQAxObjectCall4 call = reinterpret_cast<CuteQAxObjectCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QAxObject::resetControl();
  }

#if !defined(QT_NO_QOBJECT)
  //  void QAxObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQAxObjectCall5 call = reinterpret_cast<CuteQAxObjectCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QAxObject::connectNotify(signal);
  }

  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQAxObjectCall6 call = reinterpret_cast<CuteQAxObjectCall6>(taken[6]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }

  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQAxObjectCall7 call = reinterpret_cast<CuteQAxObjectCall7>(taken[7]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }

  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQAxObjectCall8 call = reinterpret_cast<CuteQAxObjectCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQAxObjectCall9 call = reinterpret_cast<CuteQAxObjectCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQAxObjectCall10 call = reinterpret_cast<CuteQAxObjectCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[11]) {
      int handled = 0;
      CuteQAxObjectCall11 call = reinterpret_cast<CuteQAxObjectCall11>(taken[11]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  bool QAxBase::initialize(IUnknown **ptr)
  bool initialize(IUnknown **ptr) override {
    if (taken[12]) {
      int handled = 0;
      CuteQAxObjectCall12 call = reinterpret_cast<CuteQAxObjectCall12>(taken[12]);
      bool given = call(this, ptr, &handled);
      if (handled) return given;
    }
    return QAxBase::initialize(ptr);
  }
};

//  QAxObjectPrivate *QAxObject::d_func()
extern "C" Q_DECL_EXPORT
QAxObjectPrivate *ritual_ZN9QAxObject6d_funcEv(QAxObject *self) {
  return self->d_func();
}

//  const QAxObjectPrivate *QAxObject::d_func() const
extern "C" Q_DECL_EXPORT
const QAxObjectPrivate *ritual_ZNK9QAxObject6d_funcEv(
    const QAxObject *self) {
  return self->d_func();
}

//  QAxObject::QAxObject(QObject *parent)
extern "C" Q_DECL_EXPORT
QAxObject *ritual_ZN9QAxObjectC1EP7QObject(QObject *parent) {
  return new CuteQAxObject(parent);
}

//  QAxObject::QAxObject(const QString &c, QObject *parent)
extern "C" Q_DECL_EXPORT
QAxObject *ritual_ZN9QAxObjectC1ERK7QStringP7QObject(
    const QString *c,
    QObject *parent) {
  return new CuteQAxObject(*c, parent);
}

//  QAxObject::QAxObject(IUnknown *iface, QObject *parent)
extern "C" Q_DECL_EXPORT
QAxObject *ritual_ZN9QAxObjectC1EP8IUnknownP7QObject(
    IUnknown *iface,
    QObject *parent) {
  return new CuteQAxObject(iface, parent);
}

//  QAxObject::~QAxObject()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QAxObjectD1Ev(QAxObject *self) {
  delete self;
}

//  ulong QAxObject::classContext() const
extern "C" Q_DECL_EXPORT
ulong ritual_ZNK9QAxObject12classContextEv(const QAxObject *self) {
  return self->classContext();
}

//  void QAxObject::setClassContext(ulong classContext)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QAxObject15setClassContextEm(
    QAxObject *self,
    ulong classContext) {
  self->setClassContext(classContext);
}

//  QString QAxObject::control() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QAxObject7controlEv(const QAxObject *self) {
  return new QString(self->control());
}

//  bool QAxObject::setControl(const QString &c)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QAxObject10setControlERK7QString(
    QAxObject *self,
    const QString *c) {
  return self->setControl(*c);
}

//  void QAxObject::resetControl()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QAxObject12resetControlEv(QAxObject *self) {
  self->resetControl();
}

//  void QAxObject::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QAxObject5clearEv(QAxObject *self) {
  self->clear();
}

//  bool QAxObject::doVerb(const QString &verb)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QAxObject6doVerbERK7QString(
    QAxObject *self,
    const QString *verb) {
  return self->doVerb(*verb);
}

//  const QMetaObject *QAxObject::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9QAxObject10metaObjectEv(
    const QAxObject *self) {
  return self->metaObject();
}

//  void QAxObject::connectNotify(const QMetaMethod &signal)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QAxObject13connectNotifyERK11QMetaMethod(
    QAxObject *self,
    const QMetaMethod *signal) {
  self->connectNotify(*signal);
}

//  QAxObject as the QAxBase it is built on
extern "C" Q_DECL_EXPORT
QAxBase *ritual_cast_QAxObject_QAxBase(QAxObject *self) {
  return static_cast<QAxBase *>(self);
}

//  a Python function taken by a CuteQAxObject, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAxObject(QAxObject *self, const char *key, void *call) {
  return static_cast<CuteQAxObject *>(self)->take(key, call);
}

//  ulong QAxObject::classContext() const
extern "C" Q_DECL_EXPORT
ulong ritual_own_ZNK9QAxObject12classContextEv(const QAxObject *self) {
  return self->QAxObject::classContext();
}

//  void QAxObject::setClassContext(ulong classContext)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QAxObject15setClassContextEm(
    QAxObject *self,
    ulong classContext) {
  self->QAxObject::setClassContext(classContext);
}

//  QString QAxObject::control() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK9QAxObject7controlEv(const QAxObject *self) {
  return new QString(self->QAxObject::control());
}

//  bool QAxObject::setControl(const QString &c)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN9QAxObject10setControlERK7QString(
    QAxObject *self,
    const QString *c) {
  return self->QAxObject::setControl(*c);
}

//  void QAxObject::resetControl()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QAxObject12resetControlEv(QAxObject *self) {
  self->QAxObject::resetControl();
}

//  void QAxObject::connectNotify(const QMetaMethod &signal)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QAxObject13connectNotifyERK11QMetaMethod(
    QAxObject *self,
    const QMetaMethod *signal) {
  static_cast<OwnQAxObject *>(self)->OwnQAxObject::connectNotify(*signal);
}

#endif  // defined(Q_OS_WIN)
