//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickaction_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickaction_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickicon_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qkeysequence.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QQuickAction may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickAction : QQuickAction {
  using QQuickAction::event;
  using QQuickAction::eventFilter;
};

//  A QQuickAction that Python can take functions over in. Every QQuickAction
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickActionCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickActionCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickActionCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickActionCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickActionCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickActionCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickActionCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickAction : public QQuickAction {
public:
  using QQuickAction::QQuickAction;
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
  //  bool QQuickAction::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickActionCall0 call = reinterpret_cast<CuteQQuickActionCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QQuickAction::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QQuickAction::eventFilter(QObject *object, QEvent *event)
  bool eventFilter(QObject *object, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickActionCall1 call = reinterpret_cast<CuteQQuickActionCall1>(taken[1]);
      bool given = call(this, object, event, &handled);
      if (handled) return given;
    }
    return QQuickAction::eventFilter(object, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickActionCall2 call = reinterpret_cast<CuteQQuickActionCall2>(taken[2]);
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
      CuteQQuickActionCall3 call = reinterpret_cast<CuteQQuickActionCall3>(taken[3]);
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
      CuteQQuickActionCall4 call = reinterpret_cast<CuteQQuickActionCall4>(taken[4]);
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
      CuteQQuickActionCall5 call = reinterpret_cast<CuteQQuickActionCall5>(taken[5]);
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
      CuteQQuickActionCall6 call = reinterpret_cast<CuteQQuickActionCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickAction::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK12QQuickAction10metaObjectEv(
    const QQuickAction *self) {
  return self->metaObject();
}

//  QString QQuickAction::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12QQuickAction2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickAction::tr(s, c, n));
}

//  QQuickAction::QQuickAction(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickAction *ritual_ZN12QQuickActionC1EP7QObject(QObject *parent) {
  return new CuteQQuickAction(parent);
}

//  QQuickAction::~QQuickAction()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickActionD1Ev(QQuickAction *self) {
  delete self;
}

//  QString QQuickAction::text() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QQuickAction4textEv(const QQuickAction *self) {
  return new QString(self->text());
}

//  void QQuickAction::setText(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickAction7setTextERK7QString(
    QQuickAction *self,
    const QString *text) {
  self->setText(*text);
}

//  QQuickIcon QQuickAction::icon() const
extern "C" Q_DECL_EXPORT
QQuickIcon *ritual_ZNK12QQuickAction4iconEv(const QQuickAction *self) {
  return new QQuickIcon(self->icon());
}

//  void QQuickAction::setIcon(const QQuickIcon &icon)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickAction7setIconERK10QQuickIcon(
    QQuickAction *self,
    const QQuickIcon *icon) {
  self->setIcon(*icon);
}

//  bool QQuickAction::isEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QQuickAction9isEnabledEv(const QQuickAction *self) {
  return self->isEnabled();
}

//  void QQuickAction::setEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickAction10setEnabledEb(
    QQuickAction *self,
    bool enabled) {
  self->setEnabled(enabled);
}

//  void QQuickAction::resetEnabled()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickAction12resetEnabledEv(QQuickAction *self) {
  self->resetEnabled();
}

//  bool QQuickAction::isChecked() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QQuickAction9isCheckedEv(const QQuickAction *self) {
  return self->isChecked();
}

//  void QQuickAction::setChecked(bool checked)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickAction10setCheckedEb(
    QQuickAction *self,
    bool checked) {
  self->setChecked(checked);
}

//  bool QQuickAction::isCheckable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QQuickAction11isCheckableEv(const QQuickAction *self) {
  return self->isCheckable();
}

//  void QQuickAction::setCheckable(bool checkable)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickAction12setCheckableEb(
    QQuickAction *self,
    bool checkable) {
  self->setCheckable(checkable);
}

#if QT_CONFIG(shortcut)
//  QKeySequence QQuickAction::shortcut() const
extern "C" Q_DECL_EXPORT
QKeySequence *ritual_ZNK12QQuickAction8shortcutEv(const QQuickAction *self) {
  return new QKeySequence(self->shortcut());
}
#endif  // QT_CONFIG(shortcut)

#if QT_CONFIG(shortcut)
//  void QQuickAction::setShortcut(const QKeySequence &shortcut)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickAction11setShortcutERK12QKeySequence(
    QQuickAction *self,
    const QKeySequence *shortcut) {
  self->setShortcut(*shortcut);
}
#endif  // QT_CONFIG(shortcut)

//  void QQuickAction::toggle(QObject *source)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickAction6toggleEP7QObject(
    QQuickAction *self,
    QObject *source) {
  self->toggle(source);
}

//  void QQuickAction::trigger(QObject *source)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickAction7triggerEP7QObject(
    QQuickAction *self,
    QObject *source) {
  self->trigger(source);
}

//  bool QQuickAction::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QQuickAction5eventEP6QEvent(
    QQuickAction *self,
    QEvent *event) {
  return self->event(event);
}

//  bool QQuickAction::eventFilter(QObject *object, QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QQuickAction11eventFilterEP7QObjectP6QEvent(
    QQuickAction *self,
    QObject *object,
    QEvent *event) {
  return self->eventFilter(object, event);
}

//  a Python function taken by a CuteQQuickAction, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickAction(
    QQuickAction *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickAction *>(self)->take(key, call);
}

//  bool QQuickAction::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN12QQuickAction5eventEP6QEvent(
    QQuickAction *self,
    QEvent *event) {
  return static_cast<OwnQQuickAction *>(self)->OwnQQuickAction::event(event);
}

//  bool QQuickAction::eventFilter(QObject *object, QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN12QQuickAction11eventFilterEP7QObjectP6QEvent(
    QQuickAction *self,
    QObject *object,
    QEvent *event) {
  return static_cast<OwnQQuickAction *>(self)->OwnQQuickAction::eventFilter(
      object,
      event);
}
