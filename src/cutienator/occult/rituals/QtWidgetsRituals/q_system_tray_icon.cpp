//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qsystemtrayicon.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qsystemtrayicon.h>
#include <QtCore/qstring.h>
#include <QtGui/qicon.h>
#include <QtCore/qrect.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QSystemTrayIcon may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQSystemTrayIcon : QSystemTrayIcon {
  using QSystemTrayIcon::event;
};

//  A QSystemTrayIcon that Python can take functions over in. Every QSystemTrayIcon
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQSystemTrayIconCall0)(const void *, QEvent *, int *);
typedef bool (*CuteQSystemTrayIconCall1)(const void *, QObject *, QEvent *, int *);
typedef void (*CuteQSystemTrayIconCall2)(const void *, QTimerEvent *, int *);
typedef void (*CuteQSystemTrayIconCall3)(const void *, QChildEvent *, int *);
typedef void (*CuteQSystemTrayIconCall4)(const void *, QEvent *, int *);
typedef void (*CuteQSystemTrayIconCall5)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQSystemTrayIconCall6)(const void *, const QMetaMethod *, int *);
class CuteQSystemTrayIcon : public QSystemTrayIcon {
public:
  using QSystemTrayIcon::QSystemTrayIcon;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
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
    return false;
  }

  //  bool QSystemTrayIcon::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQSystemTrayIconCall0 call = reinterpret_cast<CuteQSystemTrayIconCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QSystemTrayIcon::event(event);
  }

  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQSystemTrayIconCall1 call = reinterpret_cast<CuteQSystemTrayIconCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }

  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQSystemTrayIconCall2 call = reinterpret_cast<CuteQSystemTrayIconCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQSystemTrayIconCall3 call = reinterpret_cast<CuteQSystemTrayIconCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQSystemTrayIconCall4 call = reinterpret_cast<CuteQSystemTrayIconCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQSystemTrayIconCall5 call = reinterpret_cast<CuteQSystemTrayIconCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQSystemTrayIconCall6 call = reinterpret_cast<CuteQSystemTrayIconCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
};

//  const QMetaObject *QSystemTrayIcon::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QSystemTrayIcon10metaObjectEv(
    const QSystemTrayIcon *self) {
  return self->metaObject();
}

//  QString QSystemTrayIcon::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QSystemTrayIcon2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QSystemTrayIcon::tr(s, c, n));
}

//  QSystemTrayIcon::QSystemTrayIcon(QObject *parent)
extern "C" Q_DECL_EXPORT
QSystemTrayIcon *ritual_ZN15QSystemTrayIconC1EP7QObject(QObject *parent) {
  return new CuteQSystemTrayIcon(parent);
}

//  QSystemTrayIcon::QSystemTrayIcon(const QIcon &icon, QObject *parent)
extern "C" Q_DECL_EXPORT
QSystemTrayIcon *ritual_ZN15QSystemTrayIconC1ERK5QIconP7QObject(
    const QIcon *icon,
    QObject *parent) {
  return new CuteQSystemTrayIcon(*icon, parent);
}

//  QSystemTrayIcon::~QSystemTrayIcon()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSystemTrayIconD1Ev(QSystemTrayIcon *self) {
  delete self;
}

//  void QSystemTrayIcon::setContextMenu(QMenu *menu)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSystemTrayIcon14setContextMenuEP5QMenu(
    QSystemTrayIcon *self,
    QMenu *menu) {
  self->setContextMenu(menu);
}

//  QMenu *QSystemTrayIcon::contextMenu() const
extern "C" Q_DECL_EXPORT
QMenu *ritual_ZNK15QSystemTrayIcon11contextMenuEv(
    const QSystemTrayIcon *self) {
  return self->contextMenu();
}

//  QIcon QSystemTrayIcon::icon() const
extern "C" Q_DECL_EXPORT
QIcon *ritual_ZNK15QSystemTrayIcon4iconEv(const QSystemTrayIcon *self) {
  return new QIcon(self->icon());
}

//  void QSystemTrayIcon::setIcon(const QIcon &icon)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSystemTrayIcon7setIconERK5QIcon(
    QSystemTrayIcon *self,
    const QIcon *icon) {
  self->setIcon(*icon);
}

//  QString QSystemTrayIcon::toolTip() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QSystemTrayIcon7toolTipEv(const QSystemTrayIcon *self) {
  return new QString(self->toolTip());
}

//  void QSystemTrayIcon::setToolTip(const QString &tip)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSystemTrayIcon10setToolTipERK7QString(
    QSystemTrayIcon *self,
    const QString *tip) {
  self->setToolTip(*tip);
}

//  bool QSystemTrayIcon::isSystemTrayAvailable()
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QSystemTrayIcon21isSystemTrayAvailableEv() {
  return QSystemTrayIcon::isSystemTrayAvailable();
}

//  bool QSystemTrayIcon::supportsMessages()
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QSystemTrayIcon16supportsMessagesEv() {
  return QSystemTrayIcon::supportsMessages();
}

//  QRect QSystemTrayIcon::geometry() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK15QSystemTrayIcon8geometryEv(const QSystemTrayIcon *self) {
  return new QRect(self->geometry());
}

//  bool QSystemTrayIcon::isVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QSystemTrayIcon9isVisibleEv(const QSystemTrayIcon *self) {
  return self->isVisible();
}

//  void QSystemTrayIcon::setVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSystemTrayIcon10setVisibleEb(
    QSystemTrayIcon *self,
    bool visible) {
  self->setVisible(visible);
}

//  void QSystemTrayIcon::show()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSystemTrayIcon4showEv(QSystemTrayIcon *self) {
  self->show();
}

//  void QSystemTrayIcon::hide()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSystemTrayIcon4hideEv(QSystemTrayIcon *self) {
  self->hide();
}

//  void QSystemTrayIcon::showMessage(const QString &title, const QString
//      &msg, const QIcon &icon, int msecs)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSystemTrayIcon11showMessageERK7QStringS2_RK5QIconi(
    QSystemTrayIcon *self,
    const QString *title,
    const QString *msg,
    const QIcon *icon,
    int msecs) {
  self->showMessage(*title, *msg, *icon, msecs);
}

//  void QSystemTrayIcon::showMessage(const QString &title, const QString
//      &msg, QSystemTrayIcon::MessageIcon icon, int msecs)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSystemTrayIcon11showMessageERK7QStringS2_NS_11MessageIconEi(
    QSystemTrayIcon *self,
    const QString *title,
    const QString *msg,
    QSystemTrayIcon::MessageIcon icon,
    int msecs) {
  self->showMessage(*title, *msg, icon, msecs);
}

//  bool QSystemTrayIcon::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QSystemTrayIcon5eventEP6QEvent(
    QSystemTrayIcon *self,
    QEvent *event) {
  return self->event(event);
}

//  QSystemTrayIconPrivate *QSystemTrayIcon::d_func()
extern "C" Q_DECL_EXPORT
QSystemTrayIconPrivate *ritual_ZN15QSystemTrayIcon6d_funcEv(
    QSystemTrayIcon *self) {
  return self->d_func();
}

//  const QSystemTrayIconPrivate *QSystemTrayIcon::d_func() const
extern "C" Q_DECL_EXPORT
const QSystemTrayIconPrivate *ritual_ZNK15QSystemTrayIcon6d_funcEv(
    const QSystemTrayIcon *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQSystemTrayIcon, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSystemTrayIcon(
    QSystemTrayIcon *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSystemTrayIcon *>(self)->take(key, call);
}

//  bool QSystemTrayIcon::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN15QSystemTrayIcon5eventEP6QEvent(
    QSystemTrayIcon *self,
    QEvent *event) {
  return static_cast<OwnQSystemTrayIcon *>(self)->OwnQSystemTrayIcon::event(
      event);
}
