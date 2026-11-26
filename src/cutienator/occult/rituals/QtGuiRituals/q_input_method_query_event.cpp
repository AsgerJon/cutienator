//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#if !defined(QT_NO_INPUTMETHOD)
#include <QtGui/qevent.h>
#include <QtCore/qvariant.h>
#include <cstring>

//  A QInputMethodQueryEvent that Python can take functions over in. Every QInputMethodQueryEvent
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_INPUTMETHOD)
typedef void * (*CuteQInputMethodQueryEventCall0)(const void *, int *);
#endif  // !defined(QT_NO_INPUTMETHOD)
typedef void (*CuteQInputMethodQueryEventCall1)(const void *, bool, int *);
class CuteQInputMethodQueryEvent : public QInputMethodQueryEvent {
public:
  using QInputMethodQueryEvent::QInputMethodQueryEvent;
  CuteQInputMethodQueryEvent(const QInputMethodQueryEvent & other) : QInputMethodQueryEvent(other) {}
  void *taken[2] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_INPUTMETHOD)
    if (!std::strcmp(key, "_ZNK6QEvent5cloneEv")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_INPUTMETHOD)
    if (!std::strcmp(key, "_ZN6QEvent11setAcceptedEb")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

#if !defined(QT_NO_INPUTMETHOD)
  //  QInputMethodQueryEvent *QInputMethodQueryEvent::clone() const
  QInputMethodQueryEvent *clone() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQInputMethodQueryEventCall0 call = reinterpret_cast<CuteQInputMethodQueryEventCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QInputMethodQueryEvent *>(given);
    }
    return QInputMethodQueryEvent::clone();
  }
#endif  // !defined(QT_NO_INPUTMETHOD)

  //  void QEvent::setAccepted(bool accepted)
  void setAccepted(bool accepted) override {
    if (taken[1]) {
      int handled = 0;
      CuteQInputMethodQueryEventCall1 call = reinterpret_cast<CuteQInputMethodQueryEventCall1>(taken[1]);
      call(this, accepted, &handled);
      if (handled) return;
    }
    QEvent::setAccepted(accepted);
  }
};

//  QInputMethodQueryEvent::QInputMethodQueryEvent(const
//      QInputMethodQueryEvent &a0)
extern "C" Q_DECL_EXPORT
QInputMethodQueryEvent *ritual_ZN22QInputMethodQueryEventC1ERKS_(
    const QInputMethodQueryEvent *a0) {
  return new CuteQInputMethodQueryEvent(*a0);
}

//  QInputMethodQueryEvent &QInputMethodQueryEvent::operator=(const
//      QInputMethodQueryEvent &other)
extern "C" Q_DECL_EXPORT
QInputMethodQueryEvent *ritual_ZN22QInputMethodQueryEventaSERKS_(
    QInputMethodQueryEvent *self,
    const QInputMethodQueryEvent *other) {
  return &(self->operator=(*other));
}

//  QInputMethodQueryEvent *QInputMethodQueryEvent::clone() const
extern "C" Q_DECL_EXPORT
QInputMethodQueryEvent *ritual_ZNK22QInputMethodQueryEvent5cloneEv(
    const QInputMethodQueryEvent *self) {
  return self->clone();
}

//  QInputMethodQueryEvent::~QInputMethodQueryEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QInputMethodQueryEventD1Ev(QInputMethodQueryEvent *self) {
  delete self;
}

//  QInputMethodQueryEvent::QInputMethodQueryEvent(Qt::InputMethodQueries
//      queries)
extern "C" Q_DECL_EXPORT
QInputMethodQueryEvent *ritual_ZN22QInputMethodQueryEventC1E6QFlagsIN2Qt16InputMethodQueryEE(
    int queries) {
  return new CuteQInputMethodQueryEvent(
      QFlags<Qt::InputMethodQuery>::fromInt(queries));
}

//  Qt::InputMethodQueries QInputMethodQueryEvent::queries() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22QInputMethodQueryEvent7queriesEv(
    const QInputMethodQueryEvent *self) {
  return static_cast<int>(self->queries().toInt());
}

//  void QInputMethodQueryEvent::setValue(Qt::InputMethodQuery query, const
//      QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QInputMethodQueryEvent8setValueEN2Qt16InputMethodQueryERK8QVariant(
    QInputMethodQueryEvent *self,
    Qt::InputMethodQuery query,
    const QVariant *value) {
  self->setValue(query, *value);
}

//  QVariant QInputMethodQueryEvent::value(Qt::InputMethodQuery query) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK22QInputMethodQueryEvent5valueEN2Qt16InputMethodQueryE(
    const QInputMethodQueryEvent *self,
    Qt::InputMethodQuery query) {
  return new QVariant(self->value(query));
}

//  a Python function taken by a CuteQInputMethodQueryEvent, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QInputMethodQueryEvent(
    QInputMethodQueryEvent *self,
    const char *key,
    void *call) {
  return static_cast<CuteQInputMethodQueryEvent *>(self)->take(key, call);
}

//  QInputMethodQueryEvent *QInputMethodQueryEvent::clone() const
extern "C" Q_DECL_EXPORT
QInputMethodQueryEvent *ritual_own_ZNK22QInputMethodQueryEvent5cloneEv(
    const QInputMethodQueryEvent *self) {
  return self->QInputMethodQueryEvent::clone();
}

#endif  // !defined(QT_NO_INPUTMETHOD)
