//  Written by dev_tooling.RitualGenerator from the records of QtQuickTemplat
//  es2/6.12.0/QtQuickTemplates2/private/qquicknativemenuitem_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquicknativemenuitem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickicon_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQuickNativeMenuItem that Python can take functions over in. Every QQuickNativeMenuItem
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickNativeMenuItemCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickNativeMenuItemCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickNativeMenuItemCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickNativeMenuItemCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickNativeMenuItemCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickNativeMenuItemCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickNativeMenuItemCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickNativeMenuItem : public QQuickNativeMenuItem {
public:
  using QQuickNativeMenuItem::QQuickNativeMenuItem;
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
      CuteQQuickNativeMenuItemCall0 call = reinterpret_cast<CuteQQuickNativeMenuItemCall0>(taken[0]);
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
      CuteQQuickNativeMenuItemCall1 call = reinterpret_cast<CuteQQuickNativeMenuItemCall1>(taken[1]);
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
      CuteQQuickNativeMenuItemCall2 call = reinterpret_cast<CuteQQuickNativeMenuItemCall2>(taken[2]);
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
      CuteQQuickNativeMenuItemCall3 call = reinterpret_cast<CuteQQuickNativeMenuItemCall3>(taken[3]);
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
      CuteQQuickNativeMenuItemCall4 call = reinterpret_cast<CuteQQuickNativeMenuItemCall4>(taken[4]);
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
      CuteQQuickNativeMenuItemCall5 call = reinterpret_cast<CuteQQuickNativeMenuItemCall5>(taken[5]);
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
      CuteQQuickNativeMenuItemCall6 call = reinterpret_cast<CuteQQuickNativeMenuItemCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickNativeMenuItem::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QQuickNativeMenuItem10metaObjectEv(
    const QQuickNativeMenuItem *self) {
  return self->metaObject();
}

//  void *QQuickNativeMenuItem::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN20QQuickNativeMenuItem11qt_metacastEPKc(
    QQuickNativeMenuItem *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickNativeMenuItem::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN20QQuickNativeMenuItem11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickNativeMenuItem *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickNativeMenuItem::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QQuickNativeMenuItem2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickNativeMenuItem::tr(s, c, n));
}

//  QQuickNativeMenuItem
//      *QQuickNativeMenuItem::createFromNonNativeItem(QQuickMenu
//      *parentMenu, QQuickItem *nonNativeItem)
extern "C" Q_DECL_EXPORT
QQuickNativeMenuItem *ritual_ZN20QQuickNativeMenuItem23createFromNonNativeItemEP10QQuickMenuP10QQuickItem(
    QQuickMenu *parentMenu,
    QQuickItem *nonNativeItem) {
  return QQuickNativeMenuItem::createFromNonNativeItem(
      parentMenu,
      nonNativeItem);
}

//  QQuickNativeMenuItem::~QQuickNativeMenuItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickNativeMenuItemD1Ev(QQuickNativeMenuItem *self) {
  delete self;
}

//  QQuickAction *QQuickNativeMenuItem::action() const
extern "C" Q_DECL_EXPORT
QQuickAction *ritual_ZNK20QQuickNativeMenuItem6actionEv(
    const QQuickNativeMenuItem *self) {
  return self->action();
}

//  QQuickMenu *QQuickNativeMenuItem::subMenu() const
extern "C" Q_DECL_EXPORT
QQuickMenu *ritual_ZNK20QQuickNativeMenuItem7subMenuEv(
    const QQuickNativeMenuItem *self) {
  return self->subMenu();
}

//  QQuickMenuSeparator *QQuickNativeMenuItem::separator() const
extern "C" Q_DECL_EXPORT
QQuickMenuSeparator *ritual_ZNK20QQuickNativeMenuItem9separatorEv(
    const QQuickNativeMenuItem *self) {
  return self->separator();
}

//  QPlatformMenuItem *QQuickNativeMenuItem::handle() const
extern "C" Q_DECL_EXPORT
QPlatformMenuItem *ritual_ZNK20QQuickNativeMenuItem6handleEv(
    const QQuickNativeMenuItem *self) {
  return self->handle();
}

//  void QQuickNativeMenuItem::sync()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickNativeMenuItem4syncEv(QQuickNativeMenuItem *self) {
  self->sync();
}

//  QQuickIcon QQuickNativeMenuItem::effectiveIcon() const
extern "C" Q_DECL_EXPORT
QQuickIcon *ritual_ZNK20QQuickNativeMenuItem13effectiveIconEv(
    const QQuickNativeMenuItem *self) {
  return new QQuickIcon(self->effectiveIcon());
}

//  QQuickNativeIconLoader *QQuickNativeMenuItem::iconLoader() const
extern "C" Q_DECL_EXPORT
QQuickNativeIconLoader *ritual_ZNK20QQuickNativeMenuItem10iconLoaderEv(
    const QQuickNativeMenuItem *self) {
  return self->iconLoader();
}

//  void QQuickNativeMenuItem::reloadIcon()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickNativeMenuItem10reloadIconEv(
    QQuickNativeMenuItem *self) {
  self->reloadIcon();
}

//  QString QQuickNativeMenuItem::debugText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK20QQuickNativeMenuItem9debugTextEv(
    const QQuickNativeMenuItem *self) {
  return new QString(self->debugText());
}

//  void QQuickNativeMenuItem::updateIcon()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickNativeMenuItem10updateIconEv(
    QQuickNativeMenuItem *self) {
  self->updateIcon();
}

//  QQuickNativeMenuItem::QQuickNativeMenuItem(QQuickMenu *parentMenu,
//      QQuickItem *nonNativeItem, Type type)
extern "C" Q_DECL_EXPORT
QQuickNativeMenuItem *ritual_ZN20QQuickNativeMenuItemC1EP10QQuickMenuP10QQuickItemNS_4TypeE(
    QQuickMenu *parentMenu,
    QQuickItem *nonNativeItem,
    QQuickNativeMenuItem::Type type) {
  return new CuteQQuickNativeMenuItem(parentMenu, nonNativeItem, type);
}

//  void QQuickNativeMenuItem::addShortcut()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickNativeMenuItem11addShortcutEv(
    QQuickNativeMenuItem *self) {
  self->addShortcut();
}

//  void QQuickNativeMenuItem::removeShortcut()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickNativeMenuItem14removeShortcutEv(
    QQuickNativeMenuItem *self) {
  self->removeShortcut();
}

//  a Python function taken by a CuteQQuickNativeMenuItem, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickNativeMenuItem(
    QQuickNativeMenuItem *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickNativeMenuItem *>(self)->take(key, call);
}
