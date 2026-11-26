//  Written by dev_tooling.RitualGenerator from the records of
//  QtVirtualKeyboard/qvirtualkeyboarddictionarymanager.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtVirtualKeyboard/QtVirtualKeyboard>
#include <QtVirtualKeyboard/qvirtualkeyboarddictionarymanager.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QVirtualKeyboardDictionaryManager that Python can take functions over in. Every QVirtualKeyboardDictionaryManager
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQVirtualKeyboardDictionaryManagerCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQVirtualKeyboardDictionaryManagerCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQVirtualKeyboardDictionaryManagerCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQVirtualKeyboardDictionaryManagerCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQVirtualKeyboardDictionaryManagerCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQVirtualKeyboardDictionaryManagerCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQVirtualKeyboardDictionaryManagerCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQVirtualKeyboardDictionaryManager : public QVirtualKeyboardDictionaryManager {
public:
  using QVirtualKeyboardDictionaryManager::QVirtualKeyboardDictionaryManager;
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
      CuteQVirtualKeyboardDictionaryManagerCall0 call = reinterpret_cast<CuteQVirtualKeyboardDictionaryManagerCall0>(taken[0]);
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
      CuteQVirtualKeyboardDictionaryManagerCall1 call = reinterpret_cast<CuteQVirtualKeyboardDictionaryManagerCall1>(taken[1]);
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
      CuteQVirtualKeyboardDictionaryManagerCall2 call = reinterpret_cast<CuteQVirtualKeyboardDictionaryManagerCall2>(taken[2]);
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
      CuteQVirtualKeyboardDictionaryManagerCall3 call = reinterpret_cast<CuteQVirtualKeyboardDictionaryManagerCall3>(taken[3]);
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
      CuteQVirtualKeyboardDictionaryManagerCall4 call = reinterpret_cast<CuteQVirtualKeyboardDictionaryManagerCall4>(taken[4]);
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
      CuteQVirtualKeyboardDictionaryManagerCall5 call = reinterpret_cast<CuteQVirtualKeyboardDictionaryManagerCall5>(taken[5]);
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
      CuteQVirtualKeyboardDictionaryManagerCall6 call = reinterpret_cast<CuteQVirtualKeyboardDictionaryManagerCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QVirtualKeyboardDictionaryManager::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK33QVirtualKeyboardDictionaryManager10metaObjectEv(
    const QVirtualKeyboardDictionaryManager *self) {
  return self->metaObject();
}

//  void *QVirtualKeyboardDictionaryManager::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN33QVirtualKeyboardDictionaryManager11qt_metacastEPKc(
    QVirtualKeyboardDictionaryManager *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QVirtualKeyboardDictionaryManager::qt_metacall(QMetaObject::Call a0,
//      int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN33QVirtualKeyboardDictionaryManager11qt_metacallEN11QMetaObject4CallEiPPv(
    QVirtualKeyboardDictionaryManager *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QVirtualKeyboardDictionaryManager::tr(const char *s, const char
//      *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN33QVirtualKeyboardDictionaryManager2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QVirtualKeyboardDictionaryManager::tr(s, c, n));
}

//  QVirtualKeyboardDictionaryManagerPrivate
//      *QVirtualKeyboardDictionaryManager::d_func()
extern "C" Q_DECL_EXPORT
QVirtualKeyboardDictionaryManagerPrivate *ritual_ZN33QVirtualKeyboardDictionaryManager6d_funcEv(
    QVirtualKeyboardDictionaryManager *self) {
  return self->d_func();
}

//  const QVirtualKeyboardDictionaryManagerPrivate
//      *QVirtualKeyboardDictionaryManager::d_func() const
extern "C" Q_DECL_EXPORT
const QVirtualKeyboardDictionaryManagerPrivate *ritual_ZNK33QVirtualKeyboardDictionaryManager6d_funcEv(
    const QVirtualKeyboardDictionaryManager *self) {
  return self->d_func();
}

//  QVirtualKeyboardDictionaryManager::QVirtualKeyboardDictionaryManager(QObj
//      ect *parent)
extern "C" Q_DECL_EXPORT
QVirtualKeyboardDictionaryManager *ritual_ZN33QVirtualKeyboardDictionaryManagerC1EP7QObject(
    QObject *parent) {
  return new CuteQVirtualKeyboardDictionaryManager(parent);
}

//  QVirtualKeyboardDictionaryManager
//      *QVirtualKeyboardDictionaryManager::instance()
extern "C" Q_DECL_EXPORT
QVirtualKeyboardDictionaryManager *ritual_ZN33QVirtualKeyboardDictionaryManager8instanceEv() {
  return QVirtualKeyboardDictionaryManager::instance();
}

//  QStringList QVirtualKeyboardDictionaryManager::availableDictionaries()
//      const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK33QVirtualKeyboardDictionaryManager21availableDictionariesEv(
    const QVirtualKeyboardDictionaryManager *self) {
  return new QList<QString>(self->availableDictionaries());
}

//  QStringList QVirtualKeyboardDictionaryManager::baseDictionaries() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK33QVirtualKeyboardDictionaryManager16baseDictionariesEv(
    const QVirtualKeyboardDictionaryManager *self) {
  return new QList<QString>(self->baseDictionaries());
}

//  void QVirtualKeyboardDictionaryManager::setBaseDictionaries(const
//      QStringList &baseDictionaries)
extern "C" Q_DECL_EXPORT
void ritual_ZN33QVirtualKeyboardDictionaryManager19setBaseDictionariesERK5QListI7QStringE(
    QVirtualKeyboardDictionaryManager *self,
    const QList<QString> *baseDictionaries) {
  self->setBaseDictionaries(*baseDictionaries);
}

//  QStringList QVirtualKeyboardDictionaryManager::extraDictionaries() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK33QVirtualKeyboardDictionaryManager17extraDictionariesEv(
    const QVirtualKeyboardDictionaryManager *self) {
  return new QList<QString>(self->extraDictionaries());
}

//  void QVirtualKeyboardDictionaryManager::setExtraDictionaries(const
//      QStringList &extraDictionaries)
extern "C" Q_DECL_EXPORT
void ritual_ZN33QVirtualKeyboardDictionaryManager20setExtraDictionariesERK5QListI7QStringE(
    QVirtualKeyboardDictionaryManager *self,
    const QList<QString> *extraDictionaries) {
  self->setExtraDictionaries(*extraDictionaries);
}

//  QStringList QVirtualKeyboardDictionaryManager::activeDictionaries() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK33QVirtualKeyboardDictionaryManager18activeDictionariesEv(
    const QVirtualKeyboardDictionaryManager *self) {
  return new QList<QString>(self->activeDictionaries());
}

//  QVirtualKeyboardDictionary
//      *QVirtualKeyboardDictionaryManager::createDictionary(const QString
//      &name)
extern "C" Q_DECL_EXPORT
QVirtualKeyboardDictionary *ritual_ZN33QVirtualKeyboardDictionaryManager16createDictionaryERK7QString(
    QVirtualKeyboardDictionaryManager *self,
    const QString *name) {
  return self->createDictionary(*name);
}

//  QVirtualKeyboardDictionary
//      *QVirtualKeyboardDictionaryManager::dictionary(const QString &name)
//      const
extern "C" Q_DECL_EXPORT
QVirtualKeyboardDictionary *ritual_ZNK33QVirtualKeyboardDictionaryManager10dictionaryERK7QString(
    const QVirtualKeyboardDictionaryManager *self,
    const QString *name) {
  return self->dictionary(*name);
}

//  void QVirtualKeyboardDictionaryManager::availableDictionariesChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN33QVirtualKeyboardDictionaryManager28availableDictionariesChangedEv(
    QVirtualKeyboardDictionaryManager *self) {
  self->availableDictionariesChanged();
}

//  void QVirtualKeyboardDictionaryManager::baseDictionariesChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN33QVirtualKeyboardDictionaryManager23baseDictionariesChangedEv(
    QVirtualKeyboardDictionaryManager *self) {
  self->baseDictionariesChanged();
}

//  void QVirtualKeyboardDictionaryManager::extraDictionariesChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN33QVirtualKeyboardDictionaryManager24extraDictionariesChangedEv(
    QVirtualKeyboardDictionaryManager *self) {
  self->extraDictionariesChanged();
}

//  void QVirtualKeyboardDictionaryManager::activeDictionariesChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN33QVirtualKeyboardDictionaryManager25activeDictionariesChangedEv(
    QVirtualKeyboardDictionaryManager *self) {
  self->activeDictionariesChanged();
}

//  a Python function taken by a CuteQVirtualKeyboardDictionaryManager, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QVirtualKeyboardDictionaryManager(
    QVirtualKeyboardDictionaryManager *self,
    const char *key,
    void *call) {
  return static_cast<CuteQVirtualKeyboardDictionaryManager *>(self)->take(key, call);
}
