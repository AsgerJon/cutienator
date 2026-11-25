//  Written by hand on 2026-11-25 from
//  QtAxContainer/qaxscript.h, Qt 6.12.0, from Qt's source. Kept as it is
//  when the generator runs again. ActiveQt is built for Windows alone, as a
//  static library, so every function of it is compiled into ours. Not
//  written: the 'addObject' taking a 'QObject *', whose code calls
//  'qAxFactory', which only a server of ActiveQt (QtAxServer) has, so our
//  library would not link with it; 'functions' and 'scriptNames', which give
//  a list of texts, and the 'call' taking a 'QList<QVariant> &'; and the
//  signal 'error'.
#include <QtCore/qglobal.h>
#if defined(Q_OS_WIN)
#include <QtAxContainer/qaxscript.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QAxScriptManager that Python can take functions over in. Every
//  QAxScriptManager Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAxScriptManagerCall0)(const void *, QEvent *, int *);
typedef bool (*CuteQAxScriptManagerCall1)(const void *, QObject *, QEvent *, int *);
typedef void (*CuteQAxScriptManagerCall2)(const void *, QTimerEvent *, int *);
typedef void (*CuteQAxScriptManagerCall3)(const void *, QChildEvent *, int *);
typedef void (*CuteQAxScriptManagerCall4)(const void *, QEvent *, int *);
typedef void (*CuteQAxScriptManagerCall5)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQAxScriptManagerCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQAxScriptManager : public QAxScriptManager {
public:
  using QAxScriptManager::QAxScriptManager;
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
      CuteQAxScriptManagerCall0 call = reinterpret_cast<CuteQAxScriptManagerCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }

  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQAxScriptManagerCall1 call = reinterpret_cast<CuteQAxScriptManagerCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }

  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQAxScriptManagerCall2 call = reinterpret_cast<CuteQAxScriptManagerCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQAxScriptManagerCall3 call = reinterpret_cast<CuteQAxScriptManagerCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQAxScriptManagerCall4 call = reinterpret_cast<CuteQAxScriptManagerCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQAxScriptManagerCall5 call = reinterpret_cast<CuteQAxScriptManagerCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQAxScriptManagerCall6 call = reinterpret_cast<CuteQAxScriptManagerCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QAxScriptManager::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QAxScriptManager10metaObjectEv(
    const QAxScriptManager *self) {
  return self->metaObject();
}

//  QString QAxScriptManager::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QAxScriptManager2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QAxScriptManager::tr(s, c, n));
}

//  QAxScriptManager::QAxScriptManager(QObject *parent)
extern "C" Q_DECL_EXPORT
QAxScriptManager *ritual_ZN16QAxScriptManagerC1EP7QObject(QObject *parent) {
  return new CuteQAxScriptManager(parent);
}

//  QAxScriptManager::~QAxScriptManager()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAxScriptManagerD1Ev(QAxScriptManager *self) {
  delete self;
}

//  void QAxScriptManager::addObject(QAxBase *object)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAxScriptManager9addObjectEP7QAxBase(
    QAxScriptManager *self,
    QAxBase *object) {
  self->addObject(object);
}

//  QAxScript *QAxScriptManager::script(const QString &name) const
extern "C" Q_DECL_EXPORT
QAxScript *ritual_ZNK16QAxScriptManager6scriptERK7QString(
    const QAxScriptManager *self,
    const QString *name) {
  return self->script(*name);
}

//  QAxScript *QAxScriptManager::load(const QString &code, const QString
//      &name, const QString &language)
extern "C" Q_DECL_EXPORT
QAxScript *ritual_ZN16QAxScriptManager4loadERK7QStringS2_S2_(
    QAxScriptManager *self,
    const QString *code,
    const QString *name,
    const QString *language) {
  return self->load(*code, *name, *language);
}

//  QAxScript *QAxScriptManager::load(const QString &file, const QString
//      &name)
extern "C" Q_DECL_EXPORT
QAxScript *ritual_ZN16QAxScriptManager4loadERK7QStringS2_(
    QAxScriptManager *self,
    const QString *file,
    const QString *name) {
  return self->load(*file, *name);
}

//  QVariant QAxScriptManager::call(const QString &function, const QVariant
//      &v1, const QVariant &v2, const QVariant &v3, const QVariant &v4,
//      const QVariant &v5, const QVariant &v6, const QVariant &v7, const
//      QVariant &v8)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN16QAxScriptManager4callERK7QStringRK8QVariantS5_S5_S5_S5_S5_S5_S5_(
    QAxScriptManager *self,
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

//  bool QAxScriptManager::registerEngine(const QString &name, const QString
//      &extension, const QString &code)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QAxScriptManager14registerEngineERK7QStringS2_S2_(
    const QString *name,
    const QString *extension,
    const QString *code) {
  return QAxScriptManager::registerEngine(*name, *extension, *code);
}

//  QString QAxScriptManager::scriptFileFilter()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QAxScriptManager16scriptFileFilterEv() {
  return new QString(QAxScriptManager::scriptFileFilter());
}

//  a Python function taken by a CuteQAxScriptManager, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAxScriptManager(
    QAxScriptManager *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAxScriptManager *>(self)->take(key, call);
}

#endif  // defined(Q_OS_WIN)
