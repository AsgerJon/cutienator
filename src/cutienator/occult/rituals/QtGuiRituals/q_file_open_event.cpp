//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qevent.h>
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <cstring>

//  A QFileOpenEvent that Python can take functions over in. Every QFileOpenEvent
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQFileOpenEventCall0)(const void *, int *);
typedef void (*CuteQFileOpenEventCall1)(const void *, bool, int *);
class CuteQFileOpenEvent : public QFileOpenEvent {
public:
  using QFileOpenEvent::QFileOpenEvent;
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

  //  QFileOpenEvent *QFileOpenEvent::clone() const
  QFileOpenEvent *clone() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQFileOpenEventCall0 call = reinterpret_cast<CuteQFileOpenEventCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QFileOpenEvent *>(given);
    }
    return QFileOpenEvent::clone();
  }

  //  void QEvent::setAccepted(bool accepted)
  void setAccepted(bool accepted) override {
    if (taken[1]) {
      int handled = 0;
      CuteQFileOpenEventCall1 call = reinterpret_cast<CuteQFileOpenEventCall1>(taken[1]);
      call(this, accepted, &handled);
      if (handled) return;
    }
    QEvent::setAccepted(accepted);
  }
};

//  QFileOpenEvent *QFileOpenEvent::clone() const
extern "C" Q_DECL_EXPORT
QFileOpenEvent *ritual_ZNK14QFileOpenEvent5cloneEv(
    const QFileOpenEvent *self) {
  return self->clone();
}

//  QFileOpenEvent::~QFileOpenEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QFileOpenEventD1Ev(QFileOpenEvent *self) {
  delete self;
}

//  QFileOpenEvent::QFileOpenEvent(const QString &file)
extern "C" Q_DECL_EXPORT
QFileOpenEvent *ritual_ZN14QFileOpenEventC1ERK7QString(const QString *file) {
  return new CuteQFileOpenEvent(*file);
}

//  QFileOpenEvent::QFileOpenEvent(const QUrl &url)
extern "C" Q_DECL_EXPORT
QFileOpenEvent *ritual_ZN14QFileOpenEventC1ERK4QUrl(const QUrl *url) {
  return new CuteQFileOpenEvent(*url);
}

//  QString QFileOpenEvent::file() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QFileOpenEvent4fileEv(const QFileOpenEvent *self) {
  return new QString(self->file());
}

//  QUrl QFileOpenEvent::url() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK14QFileOpenEvent3urlEv(const QFileOpenEvent *self) {
  return new QUrl(self->url());
}

//  a Python function taken by a CuteQFileOpenEvent, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QFileOpenEvent(
    QFileOpenEvent *self,
    const char *key,
    void *call) {
  return static_cast<CuteQFileOpenEvent *>(self)->take(key, call);
}

//  QFileOpenEvent *QFileOpenEvent::clone() const
extern "C" Q_DECL_EXPORT
QFileOpenEvent *ritual_own_ZNK14QFileOpenEvent5cloneEv(
    const QFileOpenEvent *self) {
  return self->QFileOpenEvent::clone();
}
