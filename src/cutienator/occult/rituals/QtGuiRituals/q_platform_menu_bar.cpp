//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/qpa/qplatformmenu.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qplatformmenu.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QPlatformMenuBar that Python can take functions over in. Every QPlatformMenuBar
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQPlatformMenuBarCall0)(const void *, QPlatformMenu *, QPlatformMenu *, int *);
typedef void (*CuteQPlatformMenuBarCall1)(const void *, QPlatformMenu *, int *);
typedef void (*CuteQPlatformMenuBarCall2)(const void *, QPlatformMenu *, int *);
typedef void (*CuteQPlatformMenuBarCall3)(const void *, QWindow *, int *);
typedef void * (*CuteQPlatformMenuBarCall4)(const void *, int *);
typedef void * (*CuteQPlatformMenuBarCall5)(const void *, quintptr, int *);
typedef void * (*CuteQPlatformMenuBarCall6)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPlatformMenuBarCall7)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPlatformMenuBarCall8)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformMenuBarCall9)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformMenuBarCall10)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformMenuBarCall11)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformMenuBarCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformMenuBarCall13)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQPlatformMenuBar : public QPlatformMenuBar {
public:
  using QPlatformMenuBar::QPlatformMenuBar;
  void *taken[14] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN16QPlatformMenuBar10insertMenuEP13QPlatformMenuS1_")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QPlatformMenuBar10removeMenuEP13QPlatformMenu")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QPlatformMenuBar8syncMenuEP13QPlatformMenu")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QPlatformMenuBar14handleReparentEP7QWindow")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QPlatformMenuBar12parentWindowEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QPlatformMenuBar10menuForTagEy")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QPlatformMenuBar10createMenuEv")) {
      taken[6] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QPlatformMenuBar::insertMenu(QPlatformMenu *menu, QPlatformMenu
  //      *before)
  void insertMenu(QPlatformMenu *menu, QPlatformMenu *before) override {
    if (taken[0]) {
      int handled = 0;
      CuteQPlatformMenuBarCall0 call = reinterpret_cast<CuteQPlatformMenuBarCall0>(taken[0]);
      call(this, menu, before, &handled);
      if (handled) return;
    }
  }

  //  void QPlatformMenuBar::removeMenu(QPlatformMenu *menu)
  void removeMenu(QPlatformMenu *menu) override {
    if (taken[1]) {
      int handled = 0;
      CuteQPlatformMenuBarCall1 call = reinterpret_cast<CuteQPlatformMenuBarCall1>(taken[1]);
      call(this, menu, &handled);
      if (handled) return;
    }
  }

  //  void QPlatformMenuBar::syncMenu(QPlatformMenu *menuItem)
  void syncMenu(QPlatformMenu *menuItem) override {
    if (taken[2]) {
      int handled = 0;
      CuteQPlatformMenuBarCall2 call = reinterpret_cast<CuteQPlatformMenuBarCall2>(taken[2]);
      call(this, menuItem, &handled);
      if (handled) return;
    }
  }

  //  void QPlatformMenuBar::handleReparent(QWindow *newParentWindow)
  void handleReparent(QWindow *newParentWindow) override {
    if (taken[3]) {
      int handled = 0;
      CuteQPlatformMenuBarCall3 call = reinterpret_cast<CuteQPlatformMenuBarCall3>(taken[3]);
      call(this, newParentWindow, &handled);
      if (handled) return;
    }
  }

  //  QWindow *QPlatformMenuBar::parentWindow() const
  QWindow *parentWindow() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQPlatformMenuBarCall4 call = reinterpret_cast<CuteQPlatformMenuBarCall4>(taken[4]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QWindow *>(given);
    }
    return QPlatformMenuBar::parentWindow();
  }

  //  QPlatformMenu *QPlatformMenuBar::menuForTag(quintptr tag) const
  QPlatformMenu *menuForTag(quintptr tag) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQPlatformMenuBarCall5 call = reinterpret_cast<CuteQPlatformMenuBarCall5>(taken[5]);
      void * given = call(this, tag, &handled);
      if (handled) return static_cast<QPlatformMenu *>(given);
    }
    return {};
  }

  //  QPlatformMenu *QPlatformMenuBar::createMenu() const
  QPlatformMenu *createMenu() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQPlatformMenuBarCall6 call = reinterpret_cast<CuteQPlatformMenuBarCall6>(taken[6]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPlatformMenu *>(given);
    }
    return QPlatformMenuBar::createMenu();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQPlatformMenuBarCall7 call = reinterpret_cast<CuteQPlatformMenuBarCall7>(taken[7]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQPlatformMenuBarCall8 call = reinterpret_cast<CuteQPlatformMenuBarCall8>(taken[8]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQPlatformMenuBarCall9 call = reinterpret_cast<CuteQPlatformMenuBarCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQPlatformMenuBarCall10 call = reinterpret_cast<CuteQPlatformMenuBarCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQPlatformMenuBarCall11 call = reinterpret_cast<CuteQPlatformMenuBarCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[12]) {
      int handled = 0;
      CuteQPlatformMenuBarCall12 call = reinterpret_cast<CuteQPlatformMenuBarCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[13]) {
      int handled = 0;
      CuteQPlatformMenuBarCall13 call = reinterpret_cast<CuteQPlatformMenuBarCall13>(taken[13]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QPlatformMenuBar::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QPlatformMenuBar10metaObjectEv(
    const QPlatformMenuBar *self) {
  return self->metaObject();
}

//  void *QPlatformMenuBar::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN16QPlatformMenuBar11qt_metacastEPKc(
    QPlatformMenuBar *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QPlatformMenuBar::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN16QPlatformMenuBar11qt_metacallEN11QMetaObject4CallEiPPv(
    QPlatformMenuBar *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QPlatformMenuBar::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QPlatformMenuBar2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QPlatformMenuBar::tr(s, c, n));
}

//  void QPlatformMenuBar::insertMenu(QPlatformMenu *menu, QPlatformMenu
//      *before)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QPlatformMenuBar10insertMenuEP13QPlatformMenuS1_(
    QPlatformMenuBar *self,
    QPlatformMenu *menu,
    QPlatformMenu *before) {
  self->insertMenu(menu, before);
}

//  void QPlatformMenuBar::removeMenu(QPlatformMenu *menu)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QPlatformMenuBar10removeMenuEP13QPlatformMenu(
    QPlatformMenuBar *self,
    QPlatformMenu *menu) {
  self->removeMenu(menu);
}

//  void QPlatformMenuBar::syncMenu(QPlatformMenu *menuItem)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QPlatformMenuBar8syncMenuEP13QPlatformMenu(
    QPlatformMenuBar *self,
    QPlatformMenu *menuItem) {
  self->syncMenu(menuItem);
}

//  void QPlatformMenuBar::handleReparent(QWindow *newParentWindow)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QPlatformMenuBar14handleReparentEP7QWindow(
    QPlatformMenuBar *self,
    QWindow *newParentWindow) {
  self->handleReparent(newParentWindow);
}

//  QWindow *QPlatformMenuBar::parentWindow() const
extern "C" Q_DECL_EXPORT
QWindow *ritual_ZNK16QPlatformMenuBar12parentWindowEv(
    const QPlatformMenuBar *self) {
  return self->parentWindow();
}

//  QPlatformMenu *QPlatformMenuBar::menuForTag(quintptr tag) const
extern "C" Q_DECL_EXPORT
QPlatformMenu *ritual_ZNK16QPlatformMenuBar10menuForTagEy(
    const QPlatformMenuBar *self,
    quintptr tag) {
  return self->menuForTag(tag);
}

//  QPlatformMenu *QPlatformMenuBar::createMenu() const
extern "C" Q_DECL_EXPORT
QPlatformMenu *ritual_ZNK16QPlatformMenuBar10createMenuEv(
    const QPlatformMenuBar *self) {
  return self->createMenu();
}

//  a Python function taken by a CuteQPlatformMenuBar, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPlatformMenuBar(
    QPlatformMenuBar *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPlatformMenuBar *>(self)->take(key, call);
}

//  QWindow *QPlatformMenuBar::parentWindow() const
extern "C" Q_DECL_EXPORT
QWindow *ritual_own_ZNK16QPlatformMenuBar12parentWindowEv(
    const QPlatformMenuBar *self) {
  return self->QPlatformMenuBar::parentWindow();
}

//  QPlatformMenu *QPlatformMenuBar::createMenu() const
extern "C" Q_DECL_EXPORT
QPlatformMenu *ritual_own_ZNK16QPlatformMenuBar10createMenuEv(
    const QPlatformMenuBar *self) {
  return self->QPlatformMenuBar::createMenu();
}
