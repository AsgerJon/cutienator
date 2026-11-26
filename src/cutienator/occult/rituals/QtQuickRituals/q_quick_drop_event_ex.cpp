//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickdrag_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickdrag_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QQuickDropEventEx that Python can take functions over in. Every QQuickDropEventEx
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(draganddrop)
typedef void * (*CuteQQuickDropEventExCall0)(const void *, int *);
#endif  // QT_CONFIG(draganddrop)
typedef void (*CuteQQuickDropEventExCall1)(const void *, bool, int *);
class CuteQQuickDropEventEx : public QQuickDropEventEx {
public:
  using QQuickDropEventEx::QQuickDropEventEx;
  CuteQQuickDropEventEx(const QQuickDropEventEx & other) : QQuickDropEventEx(other) {}
  void *taken[2] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZNK6QEvent5cloneEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN6QEvent11setAcceptedEb")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

#if QT_CONFIG(draganddrop)
  //  QDropEvent *QDropEvent::clone() const
  QDropEvent *clone() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickDropEventExCall0 call = reinterpret_cast<CuteQQuickDropEventExCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QDropEvent *>(given);
    }
    return QDropEvent::clone();
  }
#endif  // QT_CONFIG(draganddrop)

  //  void QEvent::setAccepted(bool accepted)
  void setAccepted(bool accepted) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickDropEventExCall1 call = reinterpret_cast<CuteQQuickDropEventExCall1>(taken[1]);
      call(this, accepted, &handled);
      if (handled) return;
    }
    QEvent::setAccepted(accepted);
  }
};

//  void QQuickDropEventEx::setProposedAction(Qt::DropAction action)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickDropEventEx17setProposedActionEN2Qt10DropActionE(
    QQuickDropEventEx *self,
    Qt::DropAction action) {
  self->setProposedAction(action);
}

//  void QQuickDropEventEx::setProposedAction(QDropEvent *event,
//      Qt::DropAction action)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickDropEventEx17setProposedActionEP10QDropEventN2Qt10DropActionE(
    QDropEvent *event,
    Qt::DropAction action) {
  QQuickDropEventEx::setProposedAction(event, action);
}

//  void QQuickDropEventEx::copyActions(const QDropEvent &from)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickDropEventEx11copyActionsERK10QDropEvent(
    QQuickDropEventEx *self,
    const QDropEvent *from) {
  self->copyActions(*from);
}

//  void QQuickDropEventEx::copyActions(QDropEvent *to, const QDropEvent
//      &from)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickDropEventEx11copyActionsEP10QDropEventRKS0_(
    QDropEvent *to,
    const QDropEvent *from) {
  QQuickDropEventEx::copyActions(to, *from);
}

//  QQuickDropEventEx::~QQuickDropEventEx()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickDropEventExD1Ev(QQuickDropEventEx *self) {
  delete self;
}

//  a Python function taken by a CuteQQuickDropEventEx, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickDropEventEx(
    QQuickDropEventEx *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickDropEventEx *>(self)->take(key, call);
}

#endif  // QT_CONFIG(quick_draganddrop)
#endif  // QT_CONFIG(quick_draganddrop)
