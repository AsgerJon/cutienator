//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qwidgetaction_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(action)
#if QT_CONFIG(action)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/qwidgetaction.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qwidgetaction_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QWidgetActionPrivate that Python can take functions over in. Every QWidgetActionPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(action)
typedef void (*CuteQWidgetActionPrivateCall0)(const void *, int *);
#endif  // QT_CONFIG(action)
#if QT_CONFIG(action)
#if QT_CONFIG(menu)
typedef void * (*CuteQWidgetActionPrivateCall1)(const void *, int *);
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(action)
#if QT_CONFIG(action)
#if QT_CONFIG(menu)
typedef void (*CuteQWidgetActionPrivateCall2)(const void *, QObject *, int *);
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(action)
class CuteQWidgetActionPrivate : public QWidgetActionPrivate {
public:
  using QWidgetActionPrivate::QWidgetActionPrivate;
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
      CuteQWidgetActionPrivateCall0 call = reinterpret_cast<CuteQWidgetActionPrivateCall0>(taken[0]);
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
      CuteQWidgetActionPrivateCall1 call = reinterpret_cast<CuteQWidgetActionPrivateCall1>(taken[1]);
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
      CuteQWidgetActionPrivateCall2 call = reinterpret_cast<CuteQWidgetActionPrivateCall2>(taken[2]);
      call(this, menu, &handled);
      if (handled) return;
    }
    QtWidgetsActionPrivate::setMenu(menu);
  }
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(action)
};

//  QWidgetAction *QWidgetActionPrivate::q_func()
extern "C" Q_DECL_EXPORT
QWidgetAction *ritual_ZN20QWidgetActionPrivate6q_funcEv(
    QWidgetActionPrivate *self) {
  return self->q_func();
}

//  const QWidgetAction *QWidgetActionPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QWidgetAction *ritual_ZNK20QWidgetActionPrivate6q_funcEv(
    const QWidgetActionPrivate *self) {
  return self->q_func();
}

//  QWidgetActionPrivate::QWidgetActionPrivate()
extern "C" Q_DECL_EXPORT
QWidgetActionPrivate *ritual_ZN20QWidgetActionPrivateC1Ev() {
  return new CuteQWidgetActionPrivate();
}

//  void QWidgetActionPrivate::widgetDestroyed(QObject *o)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QWidgetActionPrivate15widgetDestroyedEP7QObject(
    QWidgetActionPrivate *self,
    QObject *o) {
  self->widgetDestroyed(o);
}

//  a Python function taken by a CuteQWidgetActionPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWidgetActionPrivate(
    QWidgetActionPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWidgetActionPrivate *>(self)->take(key, call);
}

#endif  // QT_CONFIG(action)
#endif  // QT_CONFIG(action)
