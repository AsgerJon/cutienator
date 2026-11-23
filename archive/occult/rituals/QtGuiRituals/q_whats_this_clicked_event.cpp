//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qevent.h>
#include <QtCore/qstring.h>
#include <cstring>

//  A QWhatsThisClickedEvent that Python can take functions over in. Every QWhatsThisClickedEvent
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQWhatsThisClickedEventCall0)(const void *, int *);
typedef void (*CuteQWhatsThisClickedEventCall1)(const void *, bool, int *);
class CuteQWhatsThisClickedEvent : public QWhatsThisClickedEvent {
public:
  using QWhatsThisClickedEvent::QWhatsThisClickedEvent;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK6QEvent5cloneEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QEvent11setAcceptedEb")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  QWhatsThisClickedEvent *QWhatsThisClickedEvent::clone() const
  QWhatsThisClickedEvent *clone() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQWhatsThisClickedEventCall0 call = reinterpret_cast<CuteQWhatsThisClickedEventCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QWhatsThisClickedEvent *>(given);
    }
    return QWhatsThisClickedEvent::clone();
  }

  //  void QEvent::setAccepted(bool accepted)
  void setAccepted(bool accepted) override {
    if (taken[1]) {
      int handled = 0;
      CuteQWhatsThisClickedEventCall1 call = reinterpret_cast<CuteQWhatsThisClickedEventCall1>(taken[1]);
      call(this, accepted, &handled);
      if (handled) return;
    }
    QEvent::setAccepted(accepted);
  }
};

//  QWhatsThisClickedEvent *QWhatsThisClickedEvent::clone() const
extern "C" Q_DECL_EXPORT
QWhatsThisClickedEvent *ritual_ZNK22QWhatsThisClickedEvent5cloneEv(
    const QWhatsThisClickedEvent *self) {
  return self->clone();
}

//  QWhatsThisClickedEvent::~QWhatsThisClickedEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QWhatsThisClickedEventD1Ev(QWhatsThisClickedEvent *self) {
  delete self;
}

//  QWhatsThisClickedEvent::QWhatsThisClickedEvent(const QString &href)
extern "C" Q_DECL_EXPORT
QWhatsThisClickedEvent *ritual_ZN22QWhatsThisClickedEventC1ERK7QString(
    const QString *href) {
  return new CuteQWhatsThisClickedEvent(*href);
}

//  QString QWhatsThisClickedEvent::href() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QWhatsThisClickedEvent4hrefEv(
    const QWhatsThisClickedEvent *self) {
  return new QString(self->href());
}

//  a Python function taken by a CuteQWhatsThisClickedEvent, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWhatsThisClickedEvent(
    QWhatsThisClickedEvent *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWhatsThisClickedEvent *>(self)->take(key, call);
}

//  QWhatsThisClickedEvent *QWhatsThisClickedEvent::clone() const
extern "C" Q_DECL_EXPORT
QWhatsThisClickedEvent *ritual_own_ZNK22QWhatsThisClickedEvent5cloneEv(
    const QWhatsThisClickedEvent *self) {
  return self->QWhatsThisClickedEvent::clone();
}
