//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickshortcut_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickshortcut_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on QQuickShortcut may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickShortcut : QQuickShortcut {
  using QQuickShortcut::classBegin;
  using QQuickShortcut::componentComplete;
  using QQuickShortcut::event;
};

//  A QQuickShortcut that Python can take functions over in. Every QQuickShortcut
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickShortcutCall0)(const void *, int *);
typedef void (*CuteQQuickShortcutCall1)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickShortcutCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickShortcutCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickShortcutCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickShortcutCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickShortcutCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickShortcutCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickShortcutCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickShortcut : public QQuickShortcut {
public:
  using QQuickShortcut::QQuickShortcut;
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

  //  void QQuickShortcut::classBegin()
  void classBegin() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickShortcutCall0 call = reinterpret_cast<CuteQQuickShortcutCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickShortcut::classBegin();
  }

  //  void QQuickShortcut::componentComplete()
  void componentComplete() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickShortcutCall1 call = reinterpret_cast<CuteQQuickShortcutCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickShortcut::componentComplete();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QQuickShortcut::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickShortcutCall2 call = reinterpret_cast<CuteQQuickShortcutCall2>(taken[2]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QQuickShortcut::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickShortcutCall3 call = reinterpret_cast<CuteQQuickShortcutCall3>(taken[3]);
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
      CuteQQuickShortcutCall4 call = reinterpret_cast<CuteQQuickShortcutCall4>(taken[4]);
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
      CuteQQuickShortcutCall5 call = reinterpret_cast<CuteQQuickShortcutCall5>(taken[5]);
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
      CuteQQuickShortcutCall6 call = reinterpret_cast<CuteQQuickShortcutCall6>(taken[6]);
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
      CuteQQuickShortcutCall7 call = reinterpret_cast<CuteQQuickShortcutCall7>(taken[7]);
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
      CuteQQuickShortcutCall8 call = reinterpret_cast<CuteQQuickShortcutCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickShortcut::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QQuickShortcut10metaObjectEv(
    const QQuickShortcut *self) {
  return self->metaObject();
}

//  QString QQuickShortcut::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QQuickShortcut2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickShortcut::tr(s, c, n));
}

//  QQuickShortcut::QQuickShortcut(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickShortcut *ritual_ZN14QQuickShortcutC1EP7QObject(QObject *parent) {
  return new CuteQQuickShortcut(parent);
}

//  QQuickShortcut::~QQuickShortcut()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickShortcutD1Ev(QQuickShortcut *self) {
  delete self;
}

//  QVariant QQuickShortcut::sequence() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK14QQuickShortcut8sequenceEv(const QQuickShortcut *self) {
  return new QVariant(self->sequence());
}

//  void QQuickShortcut::setSequence(const QVariant &sequence)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickShortcut11setSequenceERK8QVariant(
    QQuickShortcut *self,
    const QVariant *sequence) {
  self->setSequence(*sequence);
}

//  QVariantList QQuickShortcut::sequences() const
extern "C" Q_DECL_EXPORT
QList<QVariant> *ritual_ZNK14QQuickShortcut9sequencesEv(
    const QQuickShortcut *self) {
  return new QList<QVariant>(self->sequences());
}

//  void QQuickShortcut::setSequences(const QVariantList &sequences)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickShortcut12setSequencesERK5QListI8QVariantE(
    QQuickShortcut *self,
    const QList<QVariant> *sequences) {
  self->setSequences(*sequences);
}

//  QString QQuickShortcut::nativeText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QQuickShortcut10nativeTextEv(
    const QQuickShortcut *self) {
  return new QString(self->nativeText());
}

//  QString QQuickShortcut::portableText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QQuickShortcut12portableTextEv(
    const QQuickShortcut *self) {
  return new QString(self->portableText());
}

//  bool QQuickShortcut::isEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QQuickShortcut9isEnabledEv(const QQuickShortcut *self) {
  return self->isEnabled();
}

//  void QQuickShortcut::setEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickShortcut10setEnabledEb(
    QQuickShortcut *self,
    bool enabled) {
  self->setEnabled(enabled);
}

//  bool QQuickShortcut::autoRepeat() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QQuickShortcut10autoRepeatEv(const QQuickShortcut *self) {
  return self->autoRepeat();
}

//  void QQuickShortcut::setAutoRepeat(bool repeat)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickShortcut13setAutoRepeatEb(
    QQuickShortcut *self,
    bool repeat) {
  self->setAutoRepeat(repeat);
}

//  Qt::ShortcutContext QQuickShortcut::context() const
extern "C" Q_DECL_EXPORT
Qt::ShortcutContext ritual_ZNK14QQuickShortcut7contextEv(
    const QQuickShortcut *self) {
  return self->context();
}

//  void QQuickShortcut::setContext(Qt::ShortcutContext context)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickShortcut10setContextEN2Qt15ShortcutContextE(
    QQuickShortcut *self,
    Qt::ShortcutContext context) {
  self->setContext(context);
}

//  void QQuickShortcut::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickShortcut10classBeginEv(QQuickShortcut *self) {
  self->classBegin();
}

//  void QQuickShortcut::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickShortcut17componentCompleteEv(QQuickShortcut *self) {
  self->componentComplete();
}

//  bool QQuickShortcut::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QQuickShortcut5eventEP6QEvent(
    QQuickShortcut *self,
    QEvent *event) {
  return self->event(event);
}

//  QQuickShortcut as the QQmlParserStatus it is built on
extern "C" Q_DECL_EXPORT
QQmlParserStatus *ritual_cast_QQuickShortcut_QQmlParserStatus(
    QQuickShortcut *self) {
  return static_cast<QQmlParserStatus *>(self);
}

//  a Python function taken by a CuteQQuickShortcut, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickShortcut(
    QQuickShortcut *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickShortcut *>(self)->take(key, call);
}

//  void QQuickShortcut::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuickShortcut10classBeginEv(QQuickShortcut *self) {
  static_cast<OwnQQuickShortcut *>(self)->OwnQQuickShortcut::classBegin();
}

//  void QQuickShortcut::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuickShortcut17componentCompleteEv(
    QQuickShortcut *self) {
  static_cast<OwnQQuickShortcut *>(self)->OwnQQuickShortcut::componentComplete();
}

//  bool QQuickShortcut::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN14QQuickShortcut5eventEP6QEvent(
    QQuickShortcut *self,
    QEvent *event) {
  return static_cast<OwnQQuickShortcut *>(self)->OwnQQuickShortcut::event(
      event);
}
