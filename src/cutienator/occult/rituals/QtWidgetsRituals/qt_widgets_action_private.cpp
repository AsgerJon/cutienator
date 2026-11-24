//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qaction_widgets_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(action)
#if QT_CONFIG(action)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtGui/qaction.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qaction_widgets_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QtWidgetsActionPrivate that Python can take functions over in. Every QtWidgetsActionPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(action)
typedef void (*CuteQtWidgetsActionPrivateCall0)(const void *, int *);
#endif  // QT_CONFIG(action)
#if QT_CONFIG(action)
#if QT_CONFIG(menu)
typedef void * (*CuteQtWidgetsActionPrivateCall1)(const void *, int *);
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(action)
#if QT_CONFIG(action)
#if QT_CONFIG(menu)
typedef void (*CuteQtWidgetsActionPrivateCall2)(const void *, QObject *, int *);
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(action)
class CuteQtWidgetsActionPrivate : public QtWidgetsActionPrivate {
public:
  using QtWidgetsActionPrivate::QtWidgetsActionPrivate;
  void *taken[3] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(action)
    if (!std::strcmp(key, "_ZN14QActionPrivate7destroyEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(action)
#if QT_CONFIG(action)
#if QT_CONFIG(menu)
    if (!std::strcmp(key, "_ZNK14QActionPrivate4menuEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(action)
#if QT_CONFIG(action)
#if QT_CONFIG(menu)
    if (!std::strcmp(key, "_ZN14QActionPrivate7setMenuEP7QObject")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(action)
    return false;
  }

#if QT_CONFIG(action)
  //  void QtWidgetsActionPrivate::destroy()
  void destroy() override {
    if (taken[0]) {
      int handled = 0;
      CuteQtWidgetsActionPrivateCall0 call = reinterpret_cast<CuteQtWidgetsActionPrivateCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QtWidgetsActionPrivate::destroy();
  }
#endif  // QT_CONFIG(action)

#if QT_CONFIG(action)
#if QT_CONFIG(menu)
  //  QObject *QtWidgetsActionPrivate::menu() const
  QObject *menu() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQtWidgetsActionPrivateCall1 call = reinterpret_cast<CuteQtWidgetsActionPrivateCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return QtWidgetsActionPrivate::menu();
  }
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(action)

#if QT_CONFIG(action)
#if QT_CONFIG(menu)
  //  void QtWidgetsActionPrivate::setMenu(QObject *menu)
  void setMenu(QObject *menu) override {
    if (taken[2]) {
      int handled = 0;
      CuteQtWidgetsActionPrivateCall2 call = reinterpret_cast<CuteQtWidgetsActionPrivateCall2>(taken[2]);
      call(this, menu, &handled);
      if (handled) return;
    }
    QtWidgetsActionPrivate::setMenu(menu);
  }
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(action)
};

//  QAction *QtWidgetsActionPrivate::q_func()
extern "C" Q_DECL_EXPORT
QAction *ritual_ZN22QtWidgetsActionPrivate6q_funcEv(
    QtWidgetsActionPrivate *self) {
  return self->q_func();
}

//  const QAction *QtWidgetsActionPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QAction *ritual_ZNK22QtWidgetsActionPrivate6q_funcEv(
    const QtWidgetsActionPrivate *self) {
  return self->q_func();
}

//  QtWidgetsActionPrivate::QtWidgetsActionPrivate()
extern "C" Q_DECL_EXPORT
QtWidgetsActionPrivate *ritual_ZN22QtWidgetsActionPrivateC1Ev() {
  return new CuteQtWidgetsActionPrivate();
}

//  QtWidgetsActionPrivate::~QtWidgetsActionPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QtWidgetsActionPrivateD1Ev(QtWidgetsActionPrivate *self) {
  delete self;
}

//  void QtWidgetsActionPrivate::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QtWidgetsActionPrivate7destroyEv(
    QtWidgetsActionPrivate *self) {
  self->destroy();
}

#if QT_CONFIG(menu)
//  QObject *QtWidgetsActionPrivate::menu() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK22QtWidgetsActionPrivate4menuEv(
    const QtWidgetsActionPrivate *self) {
  return self->menu();
}
#endif  // QT_CONFIG(menu)

#if QT_CONFIG(menu)
//  void QtWidgetsActionPrivate::setMenu(QObject *menu)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QtWidgetsActionPrivate7setMenuEP7QObject(
    QtWidgetsActionPrivate *self,
    QObject *menu) {
  self->setMenu(menu);
}
#endif  // QT_CONFIG(menu)

//  a Python function taken by a CuteQtWidgetsActionPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QtWidgetsActionPrivate(
    QtWidgetsActionPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQtWidgetsActionPrivate *>(self)->take(key, call);
}

//  void QtWidgetsActionPrivate::destroy()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QtWidgetsActionPrivate7destroyEv(
    QtWidgetsActionPrivate *self) {
  self->QtWidgetsActionPrivate::destroy();
}

#if QT_CONFIG(menu)
//  QObject *QtWidgetsActionPrivate::menu() const
extern "C" Q_DECL_EXPORT
QObject *ritual_own_ZNK22QtWidgetsActionPrivate4menuEv(
    const QtWidgetsActionPrivate *self) {
  return self->QtWidgetsActionPrivate::menu();
}
#endif  // QT_CONFIG(menu)

#if QT_CONFIG(menu)
//  void QtWidgetsActionPrivate::setMenu(QObject *menu)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QtWidgetsActionPrivate7setMenuEP7QObject(
    QtWidgetsActionPrivate *self,
    QObject *menu) {
  self->QtWidgetsActionPrivate::setMenu(menu);
}
#endif  // QT_CONFIG(menu)

#endif  // QT_CONFIG(action)
#endif  // QT_CONFIG(action)
