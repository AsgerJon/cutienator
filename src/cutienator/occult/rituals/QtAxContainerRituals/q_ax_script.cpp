//  Written by hand on 2026-11-25 from
//  QtAxContainer/qaxscript.h, Qt 6.12.0, from Qt's source. Kept as it is
//  when the generator runs again. ActiveQt is built for Windows alone, as a
//  static library, so every function of it is compiled into ours. Not
//  written: 'functions', which gives a list of texts, and the 'call' taking
//  a 'QList<QVariant> &'; and the signals 'entered', 'finished' (three of
//  them), 'stateChanged' and 'error'.
#include <QtCore/qglobal.h>
#if defined(Q_OS_WIN)
#include <QtAxContainer/qaxscript.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QAxScript that Python can take functions over in. Every QAxScript
//  Python makes is one. Each function below asks the Python function handed
//  over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAxScriptCall0)(const void *, QEvent *, int *);
typedef bool (*CuteQAxScriptCall1)(const void *, QObject *, QEvent *, int *);
typedef void (*CuteQAxScriptCall2)(const void *, QTimerEvent *, int *);
typedef void (*CuteQAxScriptCall3)(const void *, QChildEvent *, int *);
typedef void (*CuteQAxScriptCall4)(const void *, QEvent *, int *);
typedef void (*CuteQAxScriptCall5)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQAxScriptCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQAxScript : public QAxScript {
public:
  using QAxScript::QAxScript;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
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
      CuteQAxScriptCall0 call = reinterpret_cast<CuteQAxScriptCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }

  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQAxScriptCall1 call = reinterpret_cast<CuteQAxScriptCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }

  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQAxScriptCall2 call = reinterpret_cast<CuteQAxScriptCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQAxScriptCall3 call = reinterpret_cast<CuteQAxScriptCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQAxScriptCall4 call = reinterpret_cast<CuteQAxScriptCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQAxScriptCall5 call = reinterpret_cast<CuteQAxScriptCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQAxScriptCall6 call = reinterpret_cast<CuteQAxScriptCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QAxScript::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9QAxScript10metaObjectEv(
    const QAxScript *self) {
  return self->metaObject();
}

//  QString QAxScript::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN9QAxScript2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QAxScript::tr(s, c, n));
}

//  QAxScript::QAxScript(const QString &name, QAxScriptManager *manager)
extern "C" Q_DECL_EXPORT
QAxScript *ritual_ZN9QAxScriptC1ERK7QStringP16QAxScriptManager(
    const QString *name,
    QAxScriptManager *manager) {
  return new CuteQAxScript(*name, manager);
}

//  QAxScript::~QAxScript()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QAxScriptD1Ev(QAxScript *self) {
  delete self;
}

//  bool QAxScript::load(const QString &code, const QString &language)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QAxScript4loadERK7QStringS2_(
    QAxScript *self,
    const QString *code,
    const QString *language) {
  return self->load(*code, *language);
}

//  QString QAxScript::scriptCode() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QAxScript10scriptCodeEv(const QAxScript *self) {
  return new QString(self->scriptCode());
}

//  QString QAxScript::scriptName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QAxScript10scriptNameEv(const QAxScript *self) {
  return new QString(self->scriptName());
}

//  QAxScriptEngine *QAxScript::scriptEngine() const
extern "C" Q_DECL_EXPORT
QAxScriptEngine *ritual_ZNK9QAxScript12scriptEngineEv(
    const QAxScript *self) {
  return self->scriptEngine();
}

//  QVariant QAxScript::call(const QString &function, const QVariant &v1,
//      const QVariant &v2, const QVariant &v3, const QVariant &v4, const
//      QVariant &v5, const QVariant &v6, const QVariant &v7, const QVariant
//      &v8)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN9QAxScript4callERK7QStringRK8QVariantS5_S5_S5_S5_S5_S5_S5_(
    QAxScript *self,
    const QString *function,
    const QVariant *v1,
    const QVariant *v2,
    const QVariant *v3,
    const QVariant *v4,
    const QVariant *v5,
    const QVariant *v6,
    const QVariant *v7,
    const QVariant *v8) {
  return new QVariant(
      self->call(
          *function,
          *v1,
          *v2,
          *v3,
          *v4,
          *v5,
          *v6,
          *v7,
          *v8));
}

//  void QAxScript::updateObjects()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QAxScript13updateObjectsEv(QAxScript *self) {
  self->updateObjects();
}

//  QAxBase *QAxScript::findObject(const QString &name)
extern "C" Q_DECL_EXPORT
QAxBase *ritual_ZN9QAxScript10findObjectERK7QString(
    QAxScript *self,
    const QString *name) {
  return self->findObject(*name);
}

//  a Python function taken by a CuteQAxScript, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAxScript(QAxScript *self, const char *key, void *call) {
  return static_cast<CuteQAxScript *>(self)->take(key, call);
}

#endif  // defined(Q_OS_WIN)
