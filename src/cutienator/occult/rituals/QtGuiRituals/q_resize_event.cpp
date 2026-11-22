//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qevent.h>
#include <QtCore/qsize.h>
#include <cstring>

//  A QResizeEvent that Python can take functions over in. Every QResizeEvent
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQResizeEventCall0)(const void *, int *);
typedef void (*CuteQResizeEventCall1)(const void *, bool, int *);
class CuteQResizeEvent : public QResizeEvent {
public:
  using QResizeEvent::QResizeEvent;
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

  //  QResizeEvent *QResizeEvent::clone() const
  QResizeEvent *clone() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQResizeEventCall0 call = reinterpret_cast<CuteQResizeEventCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QResizeEvent *>(given);
    }
    return QResizeEvent::clone();
  }

  //  void QEvent::setAccepted(bool accepted)
  void setAccepted(bool accepted) override {
    if (taken[1]) {
      int handled = 0;
      CuteQResizeEventCall1 call = reinterpret_cast<CuteQResizeEventCall1>(taken[1]);
      call(this, accepted, &handled);
      if (handled) return;
    }
    QEvent::setAccepted(accepted);
  }
};

//  QResizeEvent *QResizeEvent::clone() const
extern "C" Q_DECL_EXPORT
QResizeEvent *ritual_ZNK12QResizeEvent5cloneEv(const QResizeEvent *self) {
  return self->clone();
}

//  QResizeEvent::~QResizeEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QResizeEventD1Ev(QResizeEvent *self) {
  delete self;
}

//  QResizeEvent::QResizeEvent(const QSize &size, const QSize &oldSize)
extern "C" Q_DECL_EXPORT
QResizeEvent *ritual_ZN12QResizeEventC1ERK5QSizeS2_(
    const QSize *size,
    const QSize *oldSize) {
  return new CuteQResizeEvent(*size, *oldSize);
}

//  const QSize &QResizeEvent::size() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK12QResizeEvent4sizeEv(const QResizeEvent *self) {
  return new QSize(self->size());
}

//  const QSize &QResizeEvent::oldSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK12QResizeEvent7oldSizeEv(const QResizeEvent *self) {
  return new QSize(self->oldSize());
}

//  a Python function taken by a CuteQResizeEvent, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QResizeEvent(
    QResizeEvent *self,
    const char *key,
    void *call) {
  return static_cast<CuteQResizeEvent *>(self)->take(key, call);
}

//  QResizeEvent *QResizeEvent::clone() const
extern "C" Q_DECL_EXPORT
QResizeEvent *ritual_own_ZNK12QResizeEvent5cloneEv(
    const QResizeEvent *self) {
  return self->QResizeEvent::clone();
}
