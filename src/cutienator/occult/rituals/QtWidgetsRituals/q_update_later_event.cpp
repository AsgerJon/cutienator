//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qwidget_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qwidget_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qregion.h>
#include <cstring>

//  A QUpdateLaterEvent that Python can take functions over in. Every QUpdateLaterEvent
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQUpdateLaterEventCall0)(const void *, bool, int *);
typedef void * (*CuteQUpdateLaterEventCall1)(const void *, int *);
class CuteQUpdateLaterEvent : public QUpdateLaterEvent {
public:
  using QUpdateLaterEvent::QUpdateLaterEvent;
  CuteQUpdateLaterEvent(const QUpdateLaterEvent & other) : QUpdateLaterEvent(other) {}
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN6QEvent11setAcceptedEb")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QEvent5cloneEv")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  void QEvent::setAccepted(bool accepted)
  void setAccepted(bool accepted) override {
    if (taken[0]) {
      int handled = 0;
      CuteQUpdateLaterEventCall0 call = reinterpret_cast<CuteQUpdateLaterEventCall0>(taken[0]);
      call(this, accepted, &handled);
      if (handled) return;
    }
    QEvent::setAccepted(accepted);
  }

  //  QEvent *QEvent::clone() const
  QEvent *clone() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQUpdateLaterEventCall1 call = reinterpret_cast<CuteQUpdateLaterEventCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QEvent *>(given);
    }
    return QEvent::clone();
  }
};

//  QUpdateLaterEvent::QUpdateLaterEvent(const QRegion &paintRegion)
extern "C" Q_DECL_EXPORT
QUpdateLaterEvent *ritual_ZN17QUpdateLaterEventC1ERK7QRegion(
    const QRegion *paintRegion) {
  return new CuteQUpdateLaterEvent(*paintRegion);
}

//  const QRegion &QUpdateLaterEvent::region() const
extern "C" Q_DECL_EXPORT
QRegion *ritual_ZNK17QUpdateLaterEvent6regionEv(
    const QUpdateLaterEvent *self) {
  return new QRegion(self->region());
}

//  QUpdateLaterEvent::~QUpdateLaterEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QUpdateLaterEventD1Ev(QUpdateLaterEvent *self) {
  delete self;
}

//  a Python function taken by a CuteQUpdateLaterEvent, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QUpdateLaterEvent(
    QUpdateLaterEvent *self,
    const char *key,
    void *call) {
  return static_cast<CuteQUpdateLaterEvent *>(self)->take(key, call);
}
