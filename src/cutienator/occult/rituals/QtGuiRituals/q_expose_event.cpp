//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qevent.h>
#include <QtGui/qregion.h>
#include <cstring>

//  A QExposeEvent that Python can take functions over in. Every QExposeEvent
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQExposeEventCall0)(const void *, int *);
typedef void (*CuteQExposeEventCall1)(const void *, bool, int *);
class CuteQExposeEvent : public QExposeEvent {
public:
  using QExposeEvent::QExposeEvent;
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

  //  QExposeEvent *QExposeEvent::clone() const
  QExposeEvent *clone() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQExposeEventCall0 call = reinterpret_cast<CuteQExposeEventCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QExposeEvent *>(given);
    }
    return QExposeEvent::clone();
  }

  //  void QEvent::setAccepted(bool accepted)
  void setAccepted(bool accepted) override {
    if (taken[1]) {
      int handled = 0;
      CuteQExposeEventCall1 call = reinterpret_cast<CuteQExposeEventCall1>(taken[1]);
      call(this, accepted, &handled);
      if (handled) return;
    }
    QEvent::setAccepted(accepted);
  }
};

//  QExposeEvent *QExposeEvent::clone() const
extern "C" Q_DECL_EXPORT
QExposeEvent *ritual_ZNK12QExposeEvent5cloneEv(const QExposeEvent *self) {
  return self->clone();
}

//  QExposeEvent::~QExposeEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QExposeEventD1Ev(QExposeEvent *self) {
  delete self;
}

//  QExposeEvent::QExposeEvent(const QRegion &m_region)
extern "C" Q_DECL_EXPORT
QExposeEvent *ritual_ZN12QExposeEventC1ERK7QRegion(const QRegion *m_region) {
  return new CuteQExposeEvent(*m_region);
}

#if QT_DEPRECATED_SINCE(6, 0)
//  const QRegion &QExposeEvent::region() const
extern "C" Q_DECL_EXPORT
QRegion *ritual_ZNK12QExposeEvent6regionEv(const QExposeEvent *self) {
  return new QRegion(self->region());
}
#endif  // QT_DEPRECATED_SINCE(6, 0)

//  a Python function taken by a CuteQExposeEvent, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QExposeEvent(
    QExposeEvent *self,
    const char *key,
    void *call) {
  return static_cast<CuteQExposeEvent *>(self)->take(key, call);
}

//  QExposeEvent *QExposeEvent::clone() const
extern "C" Q_DECL_EXPORT
QExposeEvent *ritual_own_ZNK12QExposeEvent5cloneEv(
    const QExposeEvent *self) {
  return self->QExposeEvent::clone();
}
