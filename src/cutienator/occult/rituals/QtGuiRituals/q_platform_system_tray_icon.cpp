//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/qpa/qplatformsystemtrayicon.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if !defined(QT_NO_SYSTEMTRAYICON)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qplatformsystemtrayicon.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qicon.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QPlatformSystemTrayIcon that Python can take functions over in. Every QPlatformSystemTrayIcon
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_SYSTEMTRAYICON)
typedef void (*CuteQPlatformSystemTrayIconCall0)(const void *, int *);
#endif  // !defined(QT_NO_SYSTEMTRAYICON)
#if !defined(QT_NO_SYSTEMTRAYICON)
typedef void (*CuteQPlatformSystemTrayIconCall1)(const void *, int *);
#endif  // !defined(QT_NO_SYSTEMTRAYICON)
#if !defined(QT_NO_SYSTEMTRAYICON)
typedef void (*CuteQPlatformSystemTrayIconCall2)(const void *, const QIcon *, int *);
#endif  // !defined(QT_NO_SYSTEMTRAYICON)
#if !defined(QT_NO_SYSTEMTRAYICON)
typedef void (*CuteQPlatformSystemTrayIconCall3)(const void *, const QString *, int *);
#endif  // !defined(QT_NO_SYSTEMTRAYICON)
#if !defined(QT_NO_SYSTEMTRAYICON)
typedef void (*CuteQPlatformSystemTrayIconCall4)(const void *, QPlatformMenu *, int *);
#endif  // !defined(QT_NO_SYSTEMTRAYICON)
#if !defined(QT_NO_SYSTEMTRAYICON)
typedef const QRect * (*CuteQPlatformSystemTrayIconCall5)(const void *, int *);
#endif  // !defined(QT_NO_SYSTEMTRAYICON)
#if !defined(QT_NO_SYSTEMTRAYICON)
typedef void (*CuteQPlatformSystemTrayIconCall6)(const void *, const QString *, const QString *, const QIcon *, int, int, int *);
#endif  // !defined(QT_NO_SYSTEMTRAYICON)
#if !defined(QT_NO_SYSTEMTRAYICON)
typedef bool (*CuteQPlatformSystemTrayIconCall7)(const void *, int *);
#endif  // !defined(QT_NO_SYSTEMTRAYICON)
#if !defined(QT_NO_SYSTEMTRAYICON)
typedef bool (*CuteQPlatformSystemTrayIconCall8)(const void *, int *);
#endif  // !defined(QT_NO_SYSTEMTRAYICON)
#if !defined(QT_NO_SYSTEMTRAYICON)
typedef void * (*CuteQPlatformSystemTrayIconCall9)(const void *, int *);
#endif  // !defined(QT_NO_SYSTEMTRAYICON)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPlatformSystemTrayIconCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPlatformSystemTrayIconCall11)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformSystemTrayIconCall12)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformSystemTrayIconCall13)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformSystemTrayIconCall14)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformSystemTrayIconCall15)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformSystemTrayIconCall16)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQPlatformSystemTrayIcon : public QPlatformSystemTrayIcon {
public:
  using QPlatformSystemTrayIcon::QPlatformSystemTrayIcon;
  void *taken[17] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_SYSTEMTRAYICON)
    if (!std::strcmp(key, "_ZN23QPlatformSystemTrayIcon4initEv")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_SYSTEMTRAYICON)
#if !defined(QT_NO_SYSTEMTRAYICON)
    if (!std::strcmp(key, "_ZN23QPlatformSystemTrayIcon7cleanupEv")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_SYSTEMTRAYICON)
#if !defined(QT_NO_SYSTEMTRAYICON)
    if (!std::strcmp(key, "_ZN23QPlatformSystemTrayIcon10updateIconERK5QIcon")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_SYSTEMTRAYICON)
#if !defined(QT_NO_SYSTEMTRAYICON)
    if (!std::strcmp(key, "_ZN23QPlatformSystemTrayIcon13updateToolTipERK7QString")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_SYSTEMTRAYICON)
#if !defined(QT_NO_SYSTEMTRAYICON)
    if (!std::strcmp(key, "_ZN23QPlatformSystemTrayIcon10updateMenuEP13QPlatformMenu")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_SYSTEMTRAYICON)
#if !defined(QT_NO_SYSTEMTRAYICON)
    if (!std::strcmp(key, "_ZNK23QPlatformSystemTrayIcon8geometryEv")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_SYSTEMTRAYICON)
#if !defined(QT_NO_SYSTEMTRAYICON)
    if (!std::strcmp(key, "_ZN23QPlatformSystemTrayIcon11showMessageERK7QStringS2_RK5QIconNS_11MessageIconEi")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_SYSTEMTRAYICON)
#if !defined(QT_NO_SYSTEMTRAYICON)
    if (!std::strcmp(key, "_ZNK23QPlatformSystemTrayIcon21isSystemTrayAvailableEv")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_SYSTEMTRAYICON)
#if !defined(QT_NO_SYSTEMTRAYICON)
    if (!std::strcmp(key, "_ZNK23QPlatformSystemTrayIcon16supportsMessagesEv")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_SYSTEMTRAYICON)
#if !defined(QT_NO_SYSTEMTRAYICON)
    if (!std::strcmp(key, "_ZNK23QPlatformSystemTrayIcon10createMenuEv")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_SYSTEMTRAYICON)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[15] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[16] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_SYSTEMTRAYICON)
  //  void QPlatformSystemTrayIcon::init()
  void init() override {
    if (taken[0]) {
      int handled = 0;
      CuteQPlatformSystemTrayIconCall0 call = reinterpret_cast<CuteQPlatformSystemTrayIconCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
  }
#endif  // !defined(QT_NO_SYSTEMTRAYICON)

#if !defined(QT_NO_SYSTEMTRAYICON)
  //  void QPlatformSystemTrayIcon::cleanup()
  void cleanup() override {
    if (taken[1]) {
      int handled = 0;
      CuteQPlatformSystemTrayIconCall1 call = reinterpret_cast<CuteQPlatformSystemTrayIconCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
  }
#endif  // !defined(QT_NO_SYSTEMTRAYICON)

#if !defined(QT_NO_SYSTEMTRAYICON)
  //  void QPlatformSystemTrayIcon::updateIcon(const QIcon &icon)
  void updateIcon(const QIcon &icon) override {
    if (taken[2]) {
      int handled = 0;
      CuteQPlatformSystemTrayIconCall2 call = reinterpret_cast<CuteQPlatformSystemTrayIconCall2>(taken[2]);
      call(this, &icon, &handled);
      if (handled) return;
    }
  }
#endif  // !defined(QT_NO_SYSTEMTRAYICON)

#if !defined(QT_NO_SYSTEMTRAYICON)
  //  void QPlatformSystemTrayIcon::updateToolTip(const QString &tooltip)
  void updateToolTip(const QString &tooltip) override {
    if (taken[3]) {
      int handled = 0;
      CuteQPlatformSystemTrayIconCall3 call = reinterpret_cast<CuteQPlatformSystemTrayIconCall3>(taken[3]);
      call(this, &tooltip, &handled);
      if (handled) return;
    }
  }
#endif  // !defined(QT_NO_SYSTEMTRAYICON)

#if !defined(QT_NO_SYSTEMTRAYICON)
  //  void QPlatformSystemTrayIcon::updateMenu(QPlatformMenu *menu)
  void updateMenu(QPlatformMenu *menu) override {
    if (taken[4]) {
      int handled = 0;
      CuteQPlatformSystemTrayIconCall4 call = reinterpret_cast<CuteQPlatformSystemTrayIconCall4>(taken[4]);
      call(this, menu, &handled);
      if (handled) return;
    }
  }
#endif  // !defined(QT_NO_SYSTEMTRAYICON)

#if !defined(QT_NO_SYSTEMTRAYICON)
  //  QRect QPlatformSystemTrayIcon::geometry() const
  QRect geometry() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQPlatformSystemTrayIconCall5 call = reinterpret_cast<CuteQPlatformSystemTrayIconCall5>(taken[5]);
      const QRect * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }
#endif  // !defined(QT_NO_SYSTEMTRAYICON)

#if !defined(QT_NO_SYSTEMTRAYICON)
  //  void QPlatformSystemTrayIcon::showMessage(const QString &title, const
  //      QString &msg, const QIcon &icon, MessageIcon iconType, int msecs)
  void showMessage(
      const QString &title,
      const QString &msg,
      const QIcon &icon,
      QPlatformSystemTrayIcon::MessageIcon iconType,
      int msecs) override {
    if (taken[6]) {
      int handled = 0;
      CuteQPlatformSystemTrayIconCall6 call = reinterpret_cast<CuteQPlatformSystemTrayIconCall6>(taken[6]);
      call(this, &title, &msg, &icon, static_cast<int>(iconType), msecs, &handled);
      if (handled) return;
    }
  }
#endif  // !defined(QT_NO_SYSTEMTRAYICON)

#if !defined(QT_NO_SYSTEMTRAYICON)
  //  bool QPlatformSystemTrayIcon::isSystemTrayAvailable() const
  bool isSystemTrayAvailable() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQPlatformSystemTrayIconCall7 call = reinterpret_cast<CuteQPlatformSystemTrayIconCall7>(taken[7]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // !defined(QT_NO_SYSTEMTRAYICON)

#if !defined(QT_NO_SYSTEMTRAYICON)
  //  bool QPlatformSystemTrayIcon::supportsMessages() const
  bool supportsMessages() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQPlatformSystemTrayIconCall8 call = reinterpret_cast<CuteQPlatformSystemTrayIconCall8>(taken[8]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // !defined(QT_NO_SYSTEMTRAYICON)

#if !defined(QT_NO_SYSTEMTRAYICON)
  //  QPlatformMenu *QPlatformSystemTrayIcon::createMenu() const
  QPlatformMenu *createMenu() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQPlatformSystemTrayIconCall9 call = reinterpret_cast<CuteQPlatformSystemTrayIconCall9>(taken[9]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPlatformMenu *>(given);
    }
    return QPlatformSystemTrayIcon::createMenu();
  }
#endif  // !defined(QT_NO_SYSTEMTRAYICON)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQPlatformSystemTrayIconCall10 call = reinterpret_cast<CuteQPlatformSystemTrayIconCall10>(taken[10]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQPlatformSystemTrayIconCall11 call = reinterpret_cast<CuteQPlatformSystemTrayIconCall11>(taken[11]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQPlatformSystemTrayIconCall12 call = reinterpret_cast<CuteQPlatformSystemTrayIconCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQPlatformSystemTrayIconCall13 call = reinterpret_cast<CuteQPlatformSystemTrayIconCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQPlatformSystemTrayIconCall14 call = reinterpret_cast<CuteQPlatformSystemTrayIconCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[15]) {
      int handled = 0;
      CuteQPlatformSystemTrayIconCall15 call = reinterpret_cast<CuteQPlatformSystemTrayIconCall15>(taken[15]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[16]) {
      int handled = 0;
      CuteQPlatformSystemTrayIconCall16 call = reinterpret_cast<CuteQPlatformSystemTrayIconCall16>(taken[16]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QPlatformSystemTrayIcon::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK23QPlatformSystemTrayIcon10metaObjectEv(
    const QPlatformSystemTrayIcon *self) {
  return self->metaObject();
}

//  void *QPlatformSystemTrayIcon::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN23QPlatformSystemTrayIcon11qt_metacastEPKc(
    QPlatformSystemTrayIcon *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QPlatformSystemTrayIcon::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN23QPlatformSystemTrayIcon11qt_metacallEN11QMetaObject4CallEiPPv(
    QPlatformSystemTrayIcon *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QPlatformSystemTrayIcon::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN23QPlatformSystemTrayIcon2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QPlatformSystemTrayIcon::tr(s, c, n));
}

//  QPlatformSystemTrayIcon::QPlatformSystemTrayIcon()
extern "C" Q_DECL_EXPORT
QPlatformSystemTrayIcon *ritual_ZN23QPlatformSystemTrayIconC1Ev() {
  return new CuteQPlatformSystemTrayIcon();
}

//  QPlatformSystemTrayIcon::~QPlatformSystemTrayIcon()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QPlatformSystemTrayIconD1Ev(QPlatformSystemTrayIcon *self) {
  delete self;
}

//  void QPlatformSystemTrayIcon::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QPlatformSystemTrayIcon4initEv(
    QPlatformSystemTrayIcon *self) {
  self->init();
}

//  void QPlatformSystemTrayIcon::cleanup()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QPlatformSystemTrayIcon7cleanupEv(
    QPlatformSystemTrayIcon *self) {
  self->cleanup();
}

//  void QPlatformSystemTrayIcon::updateIcon(const QIcon &icon)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QPlatformSystemTrayIcon10updateIconERK5QIcon(
    QPlatformSystemTrayIcon *self,
    const QIcon *icon) {
  self->updateIcon(*icon);
}

//  void QPlatformSystemTrayIcon::updateToolTip(const QString &tooltip)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QPlatformSystemTrayIcon13updateToolTipERK7QString(
    QPlatformSystemTrayIcon *self,
    const QString *tooltip) {
  self->updateToolTip(*tooltip);
}

//  void QPlatformSystemTrayIcon::updateMenu(QPlatformMenu *menu)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QPlatformSystemTrayIcon10updateMenuEP13QPlatformMenu(
    QPlatformSystemTrayIcon *self,
    QPlatformMenu *menu) {
  self->updateMenu(menu);
}

//  QRect QPlatformSystemTrayIcon::geometry() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK23QPlatformSystemTrayIcon8geometryEv(
    const QPlatformSystemTrayIcon *self) {
  return new QRect(self->geometry());
}

//  void QPlatformSystemTrayIcon::showMessage(const QString &title, const
//      QString &msg, const QIcon &icon, MessageIcon iconType, int msecs)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QPlatformSystemTrayIcon11showMessageERK7QStringS2_RK5QIconNS_11MessageIconEi(
    QPlatformSystemTrayIcon *self,
    const QString *title,
    const QString *msg,
    const QIcon *icon,
    QPlatformSystemTrayIcon::MessageIcon iconType,
    int msecs) {
  self->showMessage(*title, *msg, *icon, iconType, msecs);
}

//  bool QPlatformSystemTrayIcon::isSystemTrayAvailable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QPlatformSystemTrayIcon21isSystemTrayAvailableEv(
    const QPlatformSystemTrayIcon *self) {
  return self->isSystemTrayAvailable();
}

//  bool QPlatformSystemTrayIcon::supportsMessages() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QPlatformSystemTrayIcon16supportsMessagesEv(
    const QPlatformSystemTrayIcon *self) {
  return self->supportsMessages();
}

//  QPlatformMenu *QPlatformSystemTrayIcon::createMenu() const
extern "C" Q_DECL_EXPORT
QPlatformMenu *ritual_ZNK23QPlatformSystemTrayIcon10createMenuEv(
    const QPlatformSystemTrayIcon *self) {
  return self->createMenu();
}

//  void QPlatformSystemTrayIcon::activated(QPlatformSystemTrayIcon::Activati
//      onReason reason)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QPlatformSystemTrayIcon9activatedENS_16ActivationReasonE(
    QPlatformSystemTrayIcon *self,
    QPlatformSystemTrayIcon::ActivationReason reason) {
  self->activated(reason);
}

//  void QPlatformSystemTrayIcon::contextMenuRequested(QPoint globalPos,
//      const QPlatformScreen *screen)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QPlatformSystemTrayIcon20contextMenuRequestedE6QPointPK15QPlatformScreen(
    QPlatformSystemTrayIcon *self,
    const QPoint *globalPos,
    const QPlatformScreen *screen) {
  self->contextMenuRequested(*globalPos, screen);
}

//  void QPlatformSystemTrayIcon::messageClicked()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QPlatformSystemTrayIcon14messageClickedEv(
    QPlatformSystemTrayIcon *self) {
  self->messageClicked();
}

//  a Python function taken by a CuteQPlatformSystemTrayIcon, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPlatformSystemTrayIcon(
    QPlatformSystemTrayIcon *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPlatformSystemTrayIcon *>(self)->take(key, call);
}

//  QPlatformMenu *QPlatformSystemTrayIcon::createMenu() const
extern "C" Q_DECL_EXPORT
QPlatformMenu *ritual_own_ZNK23QPlatformSystemTrayIcon10createMenuEv(
    const QPlatformSystemTrayIcon *self) {
  return self->QPlatformSystemTrayIcon::createMenu();
}

#endif  // !defined(QT_NO_SYSTEMTRAYICON)
