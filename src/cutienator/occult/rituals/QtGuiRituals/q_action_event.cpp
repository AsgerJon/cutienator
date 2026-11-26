//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#if QT_CONFIG(action)
#include <QtGui/qevent.h>
#include <cstring>

//  A QActionEvent that Python can take functions over in. Every QActionEvent
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(action)
typedef void * (*CuteQActionEventCall0)(const void *, int *);
#endif  // QT_CONFIG(action)
typedef void (*CuteQActionEventCall1)(const void *, bool, int *);
class CuteQActionEvent : public QActionEvent {
public:
  using QActionEvent::QActionEvent;
  CuteQActionEvent(const QActionEvent & other) : QActionEvent(other) {}
  void *taken[2] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(action)
    if (!std::strcmp(key, "_ZNK6QEvent5cloneEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(action)
    if (!std::strcmp(key, "_ZN6QEvent11setAcceptedEb")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

#if QT_CONFIG(action)
  //  QActionEvent *QActionEvent::clone() const
  QActionEvent *clone() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQActionEventCall0 call = reinterpret_cast<CuteQActionEventCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QActionEvent *>(given);
    }
    return QActionEvent::clone();
  }
#endif  // QT_CONFIG(action)

  //  void QEvent::setAccepted(bool accepted)
  void setAccepted(bool accepted) override {
    if (taken[1]) {
      int handled = 0;
      CuteQActionEventCall1 call = reinterpret_cast<CuteQActionEventCall1>(taken[1]);
      call(this, accepted, &handled);
      if (handled) return;
    }
    QEvent::setAccepted(accepted);
  }
};

//  QActionEvent::QActionEvent(const QActionEvent &a0)
extern "C" Q_DECL_EXPORT
QActionEvent *ritual_ZN12QActionEventC1ERKS_(const QActionEvent *a0) {
  return new CuteQActionEvent(*a0);
}

//  QActionEvent &QActionEvent::operator=(const QActionEvent &other)
extern "C" Q_DECL_EXPORT
QActionEvent *ritual_ZN12QActionEventaSERKS_(
    QActionEvent *self,
    const QActionEvent *other) {
  return &(self->operator=(*other));
}

//  QActionEvent *QActionEvent::clone() const
extern "C" Q_DECL_EXPORT
QActionEvent *ritual_ZNK12QActionEvent5cloneEv(const QActionEvent *self) {
  return self->clone();
}

//  QActionEvent::~QActionEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QActionEventD1Ev(QActionEvent *self) {
  delete self;
}

//  QActionEvent::QActionEvent(int type, QAction *action, QAction *before)
extern "C" Q_DECL_EXPORT
QActionEvent *ritual_ZN12QActionEventC1EiP7QActionS1_(
    int type,
    QAction *action,
    QAction *before) {
  return new CuteQActionEvent(type, action, before);
}

//  QAction *QActionEvent::action() const
extern "C" Q_DECL_EXPORT
QAction *ritual_ZNK12QActionEvent6actionEv(const QActionEvent *self) {
  return self->action();
}

//  QAction *QActionEvent::before() const
extern "C" Q_DECL_EXPORT
QAction *ritual_ZNK12QActionEvent6beforeEv(const QActionEvent *self) {
  return self->before();
}

//  a Python function taken by a CuteQActionEvent, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QActionEvent(
    QActionEvent *self,
    const char *key,
    void *call) {
  return static_cast<CuteQActionEvent *>(self)->take(key, call);
}

//  QActionEvent *QActionEvent::clone() const
extern "C" Q_DECL_EXPORT
QActionEvent *ritual_own_ZNK12QActionEvent5cloneEv(
    const QActionEvent *self) {
  return self->QActionEvent::clone();
}

#endif  // QT_CONFIG(action)
