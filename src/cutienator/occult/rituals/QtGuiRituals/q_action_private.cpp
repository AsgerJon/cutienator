//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qaction_p.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if QT_CONFIG(action)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/qaction.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qaction_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <cstring>

//  A QActionPrivate that Python can take functions over in. Every QActionPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(action)
typedef void (*CuteQActionPrivateCall0)(const void *, int *);
#endif  // QT_CONFIG(action)
#if QT_CONFIG(action)
typedef void * (*CuteQActionPrivateCall1)(const void *, int *);
#endif  // QT_CONFIG(action)
#if QT_CONFIG(action)
typedef void (*CuteQActionPrivateCall2)(const void *, QObject *, int *);
#endif  // QT_CONFIG(action)
class CuteQActionPrivate : public QActionPrivate {
public:
  using QActionPrivate::QActionPrivate;
  void *taken[3] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(action)
    if (!std::strcmp(key, "_ZN14QActionPrivate7destroyEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(action)
#if QT_CONFIG(action)
    if (!std::strcmp(key, "_ZNK14QActionPrivate4menuEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(action)
#if QT_CONFIG(action)
    if (!std::strcmp(key, "_ZN14QActionPrivate7setMenuEP7QObject")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(action)
    return false;
  }

#if QT_CONFIG(action)
  //  void QActionPrivate::destroy()
  void destroy() override {
    if (taken[0]) {
      int handled = 0;
      CuteQActionPrivateCall0 call = reinterpret_cast<CuteQActionPrivateCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QActionPrivate::destroy();
  }
#endif  // QT_CONFIG(action)

#if QT_CONFIG(action)
  //  QObject *QActionPrivate::menu() const
  QObject *menu() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQActionPrivateCall1 call = reinterpret_cast<CuteQActionPrivateCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return QActionPrivate::menu();
  }
#endif  // QT_CONFIG(action)

#if QT_CONFIG(action)
  //  void QActionPrivate::setMenu(QObject *menu)
  void setMenu(QObject *menu) override {
    if (taken[2]) {
      int handled = 0;
      CuteQActionPrivateCall2 call = reinterpret_cast<CuteQActionPrivateCall2>(taken[2]);
      call(this, menu, &handled);
      if (handled) return;
    }
    QActionPrivate::setMenu(menu);
  }
#endif  // QT_CONFIG(action)
};

//  QAction *QActionPrivate::q_func()
extern "C" Q_DECL_EXPORT
QAction *ritual_ZN14QActionPrivate6q_funcEv(QActionPrivate *self) {
  return self->q_func();
}

//  const QAction *QActionPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QAction *ritual_ZNK14QActionPrivate6q_funcEv(
    const QActionPrivate *self) {
  return self->q_func();
}

//  QActionPrivate::QActionPrivate()
extern "C" Q_DECL_EXPORT
QActionPrivate *ritual_ZN14QActionPrivateC1Ev() {
  return new CuteQActionPrivate();
}

//  QActionPrivate::~QActionPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QActionPrivateD1Ev(QActionPrivate *self) {
  delete self;
}

//  void QActionPrivate::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QActionPrivate7destroyEv(QActionPrivate *self) {
  self->destroy();
}

//  QActionPrivate *QActionPrivate::get(QAction *q)
extern "C" Q_DECL_EXPORT
QActionPrivate *ritual_ZN14QActionPrivate3getEP7QAction(QAction *q) {
  return QActionPrivate::get(q);
}

//  bool QActionPrivate::setEnabled(bool enable, bool byGroup)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QActionPrivate10setEnabledEbb(
    QActionPrivate *self,
    bool enable,
    bool byGroup) {
  return self->setEnabled(enable, byGroup);
}

//  void QActionPrivate::setVisible(bool b)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QActionPrivate10setVisibleEb(QActionPrivate *self, bool b) {
  self->setVisible(b);
}

//  QObject *QActionPrivate::menu() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK14QActionPrivate4menuEv(const QActionPrivate *self) {
  return self->menu();
}

//  void QActionPrivate::setMenu(QObject *menu)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QActionPrivate7setMenuEP7QObject(
    QActionPrivate *self,
    QObject *menu) {
  self->setMenu(menu);
}

//  bool QActionPrivate::showStatusText(QObject *widget, const QString &str)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QActionPrivate14showStatusTextEP7QObjectRK7QString(
    QActionPrivate *self,
    QObject *widget,
    const QString *str) {
  return self->showStatusText(widget, *str);
}

//  void QActionPrivate::sendDataChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QActionPrivate15sendDataChangedEv(QActionPrivate *self) {
  self->sendDataChanged();
}

//  a Python function taken by a CuteQActionPrivate, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QActionPrivate(
    QActionPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQActionPrivate *>(self)->take(key, call);
}

//  void QActionPrivate::destroy()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QActionPrivate7destroyEv(QActionPrivate *self) {
  self->QActionPrivate::destroy();
}

//  QObject *QActionPrivate::menu() const
extern "C" Q_DECL_EXPORT
QObject *ritual_own_ZNK14QActionPrivate4menuEv(const QActionPrivate *self) {
  return self->QActionPrivate::menu();
}

//  void QActionPrivate::setMenu(QObject *menu)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QActionPrivate7setMenuEP7QObject(
    QActionPrivate *self,
    QObject *menu) {
  self->QActionPrivate::setMenu(menu);
}

#endif  // QT_CONFIG(action)
