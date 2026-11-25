//  Written by hand on 2026-11-25 from
//  QtAxContainer/qaxscript.h, Qt 6.12.0, from Qt's source. Kept as it is
//  when the generator runs again. ActiveQt is built for Windows alone, as a
//  static library, so every function of it is compiled into ours.
//  'IUnknown', a COM interface of Windows, and a 'void **' are passed as
//  addresses; a 'long' and a 'ulong' as the numbers Windows has. Nothing it
//  declares is left out. Its Cute class takes no 'propertyWritable' or
//  'setPropertyWritable' over: they take a 'const char *', which is handed
//  to no Python function.
#include <QtCore/qglobal.h>
#if defined(Q_OS_WIN)
#include <QtAxContainer/qaxscript.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/quuid.h>
#include <cstring>

//  Only a class built on QAxScriptEngine may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQAxScriptEngine : QAxScriptEngine {
  using QAxScriptEngine::initialize;
};

//  A QAxScriptEngine that Python can take functions over in. Every
//  QAxScriptEngine Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQAxScriptEngineCall0)(const void *, IUnknown **, int *);
typedef ulong (*CuteQAxScriptEngineCall1)(const void *, int *);
typedef void (*CuteQAxScriptEngineCall2)(const void *, ulong, int *);
typedef QString * (*CuteQAxScriptEngineCall3)(const void *, int *);
typedef bool (*CuteQAxScriptEngineCall4)(const void *, const QString *, int *);
typedef void (*CuteQAxScriptEngineCall5)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAxScriptEngineCall6)(const void *, const QMetaMethod *, int *);
typedef bool (*CuteQAxScriptEngineCall7)(const void *, QEvent *, int *);
typedef bool (*CuteQAxScriptEngineCall8)(const void *, QObject *, QEvent *, int *);
typedef void (*CuteQAxScriptEngineCall9)(const void *, QTimerEvent *, int *);
typedef void (*CuteQAxScriptEngineCall10)(const void *, QChildEvent *, int *);
typedef void (*CuteQAxScriptEngineCall11)(const void *, QEvent *, int *);
typedef void (*CuteQAxScriptEngineCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQAxScriptEngine : public QAxScriptEngine {
public:
  using QAxScriptEngine::QAxScriptEngine;
  void *taken[13] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN7QAxBase10initializeEPP8IUnknown")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QAxObjectInterface12classContextEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAxObjectInterface15setClassContextEm")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QAxObjectInterface7controlEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAxObjectInterface10setControlERK7QString")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAxObjectInterface12resetControlEv")) {
      taken[5] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  bool QAxScriptEngine::initialize(IUnknown **ptr)
  bool initialize(IUnknown **ptr) override {
    if (taken[0]) {
      int handled = 0;
      CuteQAxScriptEngineCall0 call = reinterpret_cast<CuteQAxScriptEngineCall0>(taken[0]);
      bool given = call(this, ptr, &handled);
      if (handled) return given;
    }
    return QAxScriptEngine::initialize(ptr);
  }

  //  ulong QAxObject::classContext() const
  ulong classContext() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQAxScriptEngineCall1 call = reinterpret_cast<CuteQAxScriptEngineCall1>(taken[1]);
      ulong given = call(this, &handled);
      if (handled) return given;
    }
    return QAxObject::classContext();
  }

  //  void QAxObject::setClassContext(ulong classContext)
  void setClassContext(ulong classContext) override {
    if (taken[2]) {
      int handled = 0;
      CuteQAxScriptEngineCall2 call = reinterpret_cast<CuteQAxScriptEngineCall2>(taken[2]);
      call(this, classContext, &handled);
      if (handled) return;
    }
    QAxObject::setClassContext(classContext);
  }

  //  QString QAxObject::control() const
  QString control() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQAxScriptEngineCall3 call = reinterpret_cast<CuteQAxScriptEngineCall3>(taken[3]);
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
    if (taken[4]) {
      int handled = 0;
      CuteQAxScriptEngineCall4 call = reinterpret_cast<CuteQAxScriptEngineCall4>(taken[4]);
      bool given = call(this, &c, &handled);
      if (handled) return given;
    }
    return QAxObject::setControl(c);
  }

  //  void QAxObject::resetControl()
  void resetControl() override {
    if (taken[5]) {
      int handled = 0;
      CuteQAxScriptEngineCall5 call = reinterpret_cast<CuteQAxScriptEngineCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QAxObject::resetControl();
  }

#if !defined(QT_NO_QOBJECT)
  //  void QAxObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQAxScriptEngineCall6 call = reinterpret_cast<CuteQAxScriptEngineCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QAxObject::connectNotify(signal);
  }

  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQAxScriptEngineCall7 call = reinterpret_cast<CuteQAxScriptEngineCall7>(taken[7]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }

  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQAxScriptEngineCall8 call = reinterpret_cast<CuteQAxScriptEngineCall8>(taken[8]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }

  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQAxScriptEngineCall9 call = reinterpret_cast<CuteQAxScriptEngineCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQAxScriptEngineCall10 call = reinterpret_cast<CuteQAxScriptEngineCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQAxScriptEngineCall11 call = reinterpret_cast<CuteQAxScriptEngineCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[12]) {
      int handled = 0;
      CuteQAxScriptEngineCall12 call = reinterpret_cast<CuteQAxScriptEngineCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  QAxScriptEngine::QAxScriptEngine(const QString &language, QAxScript
//      *script)
extern "C" Q_DECL_EXPORT
QAxScriptEngine *ritual_ZN15QAxScriptEngineC1ERK7QStringP9QAxScript(
    const QString *language,
    QAxScript *script) {
  return new CuteQAxScriptEngine(*language, script);
}

//  QAxScriptEngine::~QAxScriptEngine()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAxScriptEngineD1Ev(QAxScriptEngine *self) {
  delete self;
}

//  bool QAxScriptEngine::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QAxScriptEngine7isValidEv(const QAxScriptEngine *self) {
  return self->isValid();
}

//  bool QAxScriptEngine::hasIntrospection() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QAxScriptEngine16hasIntrospectionEv(
    const QAxScriptEngine *self) {
  return self->hasIntrospection();
}

//  QString QAxScriptEngine::scriptLanguage() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QAxScriptEngine14scriptLanguageEv(
    const QAxScriptEngine *self) {
  return new QString(self->scriptLanguage());
}

//  State QAxScriptEngine::state() const
extern "C" Q_DECL_EXPORT
QAxScriptEngine::State ritual_ZNK15QAxScriptEngine5stateEv(
    const QAxScriptEngine *self) {
  return self->state();
}

//  void QAxScriptEngine::setState(State st)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAxScriptEngine8setStateENS_5StateE(
    QAxScriptEngine *self,
    QAxScriptEngine::State st) {
  self->setState(st);
}

//  void QAxScriptEngine::addItem(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAxScriptEngine7addItemERK7QString(
    QAxScriptEngine *self,
    const QString *name) {
  self->addItem(*name);
}

//  long QAxScriptEngine::queryInterface(const QUuid &a0, void **a1) const
extern "C" Q_DECL_EXPORT
long ritual_ZNK15QAxScriptEngine14queryInterfaceERK5QUuidPPv(
    const QAxScriptEngine *self,
    const QUuid *a0,
    void **a1) {
  return self->queryInterface(*a0, a1);
}

//  bool QAxScriptEngine::initialize(IUnknown **ptr)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QAxScriptEngine10initializeEPP8IUnknown(
    QAxScriptEngine *self,
    IUnknown **ptr) {
  return self->initialize(ptr);
}

//  a Python function taken by a CuteQAxScriptEngine, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAxScriptEngine(
    QAxScriptEngine *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAxScriptEngine *>(self)->take(key, call);
}

//  bool QAxScriptEngine::initialize(IUnknown **ptr)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN15QAxScriptEngine10initializeEPP8IUnknown(
    QAxScriptEngine *self,
    IUnknown **ptr) {
  return static_cast<OwnQAxScriptEngine *>(self)->OwnQAxScriptEngine::initialize(
      ptr);
}

#endif  // defined(Q_OS_WIN)
