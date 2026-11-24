//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qshortcut.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#include <QtGui/qtguiglobal.h>
#if QT_CONFIG(shortcut)
#if QT_CONFIG(shortcut)
#include <QtGui/qshortcut.h>
#include <QtCore/qstring.h>
#include <QtGui/qkeysequence.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on QShortcut may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQShortcut : QShortcut {
  using QShortcut::event;
};

//  A QShortcut that Python can take functions over in. Every QShortcut
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(shortcut)
typedef bool (*CuteQShortcutCall0)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(shortcut)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQShortcutCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQShortcutCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQShortcutCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQShortcutCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQShortcutCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQShortcutCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQShortcut : public QShortcut {
public:
  using QShortcut::QShortcut;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(shortcut)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(shortcut)
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
#if QT_CONFIG(shortcut)
  //  bool QShortcut::event(QEvent *e)
  bool event(QEvent *e) override {
    if (taken[0]) {
      int handled = 0;
      CuteQShortcutCall0 call = reinterpret_cast<CuteQShortcutCall0>(taken[0]);
      bool given = call(this, e, &handled);
      if (handled) return given;
    }
    return QShortcut::event(e);
  }
#endif  // QT_CONFIG(shortcut)
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQShortcutCall1 call = reinterpret_cast<CuteQShortcutCall1>(taken[1]);
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
      CuteQShortcutCall2 call = reinterpret_cast<CuteQShortcutCall2>(taken[2]);
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
      CuteQShortcutCall3 call = reinterpret_cast<CuteQShortcutCall3>(taken[3]);
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
      CuteQShortcutCall4 call = reinterpret_cast<CuteQShortcutCall4>(taken[4]);
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
      CuteQShortcutCall5 call = reinterpret_cast<CuteQShortcutCall5>(taken[5]);
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
      CuteQShortcutCall6 call = reinterpret_cast<CuteQShortcutCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QShortcut::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9QShortcut10metaObjectEv(
    const QShortcut *self) {
  return self->metaObject();
}

//  QString QShortcut::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN9QShortcut2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QShortcut::tr(s, c, n));
}

//  QShortcutPrivate *QShortcut::d_func()
extern "C" Q_DECL_EXPORT
QShortcutPrivate *ritual_ZN9QShortcut6d_funcEv(QShortcut *self) {
  return self->d_func();
}

//  const QShortcutPrivate *QShortcut::d_func() const
extern "C" Q_DECL_EXPORT
const QShortcutPrivate *ritual_ZNK9QShortcut6d_funcEv(
    const QShortcut *self) {
  return self->d_func();
}

//  QShortcut::QShortcut(QObject *parent)
extern "C" Q_DECL_EXPORT
QShortcut *ritual_ZN9QShortcutC1EP7QObject(QObject *parent) {
  return new CuteQShortcut(parent);
}

//  QShortcut::QShortcut(const QKeySequence &key, QObject *parent, const char
//      *member, const char *ambiguousMember, Qt::ShortcutContext context)
extern "C" Q_DECL_EXPORT
QShortcut *ritual_ZN9QShortcutC1ERK12QKeySequenceP7QObjectPKcS6_N2Qt15ShortcutContextE(
    const QKeySequence *key,
    QObject *parent,
    const char *member,
    const char *ambiguousMember,
    Qt::ShortcutContext context) {
  return new CuteQShortcut(*key, parent, member, ambiguousMember, context);
}

//  QShortcut::QShortcut(QKeySequence::StandardKey key, QObject *parent,
//      const char *member, const char *ambiguousMember, Qt::ShortcutContext
//      context)
extern "C" Q_DECL_EXPORT
QShortcut *ritual_ZN9QShortcutC1EN12QKeySequence11StandardKeyEP7QObjectPKcS5_N2Qt15ShortcutContextE(
    QKeySequence::StandardKey key,
    QObject *parent,
    const char *member,
    const char *ambiguousMember,
    Qt::ShortcutContext context) {
  return new CuteQShortcut(key, parent, member, ambiguousMember, context);
}

//  QShortcut::~QShortcut()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QShortcutD1Ev(QShortcut *self) {
  delete self;
}

//  void QShortcut::setKey(const QKeySequence &key)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QShortcut6setKeyERK12QKeySequence(
    QShortcut *self,
    const QKeySequence *key) {
  self->setKey(*key);
}

//  QKeySequence QShortcut::key() const
extern "C" Q_DECL_EXPORT
QKeySequence *ritual_ZNK9QShortcut3keyEv(const QShortcut *self) {
  return new QKeySequence(self->key());
}

//  void QShortcut::setKeys(QKeySequence::StandardKey key)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QShortcut7setKeysEN12QKeySequence11StandardKeyE(
    QShortcut *self,
    QKeySequence::StandardKey key) {
  self->setKeys(key);
}

//  void QShortcut::setKeys(const QList<QKeySequence> &keys)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QShortcut7setKeysERK5QListI12QKeySequenceE(
    QShortcut *self,
    const QList<QKeySequence> *keys) {
  self->setKeys(*keys);
}

//  QList<QKeySequence> QShortcut::keys() const
extern "C" Q_DECL_EXPORT
QList<QKeySequence> *ritual_ZNK9QShortcut4keysEv(const QShortcut *self) {
  return new QList<QKeySequence>(self->keys());
}

//  void QShortcut::setEnabled(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QShortcut10setEnabledEb(QShortcut *self, bool enable) {
  self->setEnabled(enable);
}

//  bool QShortcut::isEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QShortcut9isEnabledEv(const QShortcut *self) {
  return self->isEnabled();
}

//  void QShortcut::setContext(Qt::ShortcutContext context)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QShortcut10setContextEN2Qt15ShortcutContextE(
    QShortcut *self,
    Qt::ShortcutContext context) {
  self->setContext(context);
}

//  Qt::ShortcutContext QShortcut::context() const
extern "C" Q_DECL_EXPORT
Qt::ShortcutContext ritual_ZNK9QShortcut7contextEv(const QShortcut *self) {
  return self->context();
}

//  void QShortcut::setAutoRepeat(bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QShortcut13setAutoRepeatEb(QShortcut *self, bool on) {
  self->setAutoRepeat(on);
}

//  bool QShortcut::autoRepeat() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QShortcut10autoRepeatEv(const QShortcut *self) {
  return self->autoRepeat();
}

#if QT_DEPRECATED_SINCE(6,0)
//  int QShortcut::id() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QShortcut2idEv(const QShortcut *self) {
  return self->id();
}
#endif  // QT_DEPRECATED_SINCE(6,0)

//  void QShortcut::setWhatsThis(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QShortcut12setWhatsThisERK7QString(
    QShortcut *self,
    const QString *text) {
  self->setWhatsThis(*text);
}

//  QString QShortcut::whatsThis() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QShortcut9whatsThisEv(const QShortcut *self) {
  return new QString(self->whatsThis());
}

//  bool QShortcut::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QShortcut5eventEP6QEvent(QShortcut *self, QEvent *e) {
  return self->event(e);
}

//  a Python function taken by a CuteQShortcut, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_QShortcut(QShortcut *self, const char *key, void *call) {
  return static_cast<CuteQShortcut *>(self)->take(key, call);
}

//  bool QShortcut::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN9QShortcut5eventEP6QEvent(QShortcut *self, QEvent *e) {
  return static_cast<OwnQShortcut *>(self)->OwnQShortcut::event(e);
}

#endif  // QT_CONFIG(shortcut)
#endif  // QT_CONFIG(shortcut)
