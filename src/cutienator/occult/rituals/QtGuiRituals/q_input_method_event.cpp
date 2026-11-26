//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#if !defined(QT_NO_INPUTMETHOD)
#include <QtGui/qevent.h>
#include <QtCore/qstring.h>
#include <cstring>

//  A QInputMethodEvent that Python can take functions over in. Every QInputMethodEvent
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_INPUTMETHOD)
typedef void * (*CuteQInputMethodEventCall0)(const void *, int *);
#endif  // !defined(QT_NO_INPUTMETHOD)
typedef void (*CuteQInputMethodEventCall1)(const void *, bool, int *);
class CuteQInputMethodEvent : public QInputMethodEvent {
public:
  using QInputMethodEvent::QInputMethodEvent;
  CuteQInputMethodEvent(const QInputMethodEvent & other) : QInputMethodEvent(other) {}
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
  //  QInputMethodEvent *QInputMethodEvent::clone() const
  QInputMethodEvent *clone() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQInputMethodEventCall0 call = reinterpret_cast<CuteQInputMethodEventCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QInputMethodEvent *>(given);
    }
    return QInputMethodEvent::clone();
  }
#endif  // !defined(QT_NO_INPUTMETHOD)

  //  void QEvent::setAccepted(bool accepted)
  void setAccepted(bool accepted) override {
    if (taken[1]) {
      int handled = 0;
      CuteQInputMethodEventCall1 call = reinterpret_cast<CuteQInputMethodEventCall1>(taken[1]);
      call(this, accepted, &handled);
      if (handled) return;
    }
    QEvent::setAccepted(accepted);
  }
};

//  QInputMethodEvent::QInputMethodEvent(const QInputMethodEvent &a0)
extern "C" Q_DECL_EXPORT
QInputMethodEvent *ritual_ZN17QInputMethodEventC1ERKS_(
    const QInputMethodEvent *a0) {
  return new CuteQInputMethodEvent(*a0);
}

//  QInputMethodEvent &QInputMethodEvent::operator=(const QInputMethodEvent
//      &other)
extern "C" Q_DECL_EXPORT
QInputMethodEvent *ritual_ZN17QInputMethodEventaSERKS_(
    QInputMethodEvent *self,
    const QInputMethodEvent *other) {
  return &(self->operator=(*other));
}

//  QInputMethodEvent *QInputMethodEvent::clone() const
extern "C" Q_DECL_EXPORT
QInputMethodEvent *ritual_ZNK17QInputMethodEvent5cloneEv(
    const QInputMethodEvent *self) {
  return self->clone();
}

//  QInputMethodEvent::~QInputMethodEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QInputMethodEventD1Ev(QInputMethodEvent *self) {
  delete self;
}

//  QInputMethodEvent::QInputMethodEvent()
extern "C" Q_DECL_EXPORT
QInputMethodEvent *ritual_ZN17QInputMethodEventC1Ev() {
  return new CuteQInputMethodEvent();
}

//  QInputMethodEvent::QInputMethodEvent(const QString &preeditText, const
//      QList<Attribute> &attributes)
extern "C" Q_DECL_EXPORT
QInputMethodEvent *ritual_ZN17QInputMethodEventC1ERK7QStringRK5QListINS_9AttributeEE(
    const QString *preeditText,
    const QList<QInputMethodEvent::Attribute> *attributes) {
  return new CuteQInputMethodEvent(*preeditText, *attributes);
}

//  void QInputMethodEvent::setCommitString(const QString &commitString, int
//      replaceFrom, int replaceLength)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QInputMethodEvent15setCommitStringERK7QStringii(
    QInputMethodEvent *self,
    const QString *commitString,
    int replaceFrom,
    int replaceLength) {
  self->setCommitString(*commitString, replaceFrom, replaceLength);
}

//  const QList<Attribute> &QInputMethodEvent::attributes() const
extern "C" Q_DECL_EXPORT
const QList<QInputMethodEvent::Attribute> *ritual_ZNK17QInputMethodEvent10attributesEv(
    const QInputMethodEvent *self) {
  return &(self->attributes());
}

//  const QString &QInputMethodEvent::preeditString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QInputMethodEvent13preeditStringEv(
    const QInputMethodEvent *self) {
  return new QString(self->preeditString());
}

//  const QString &QInputMethodEvent::commitString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QInputMethodEvent12commitStringEv(
    const QInputMethodEvent *self) {
  return new QString(self->commitString());
}

//  int QInputMethodEvent::replacementStart() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QInputMethodEvent16replacementStartEv(
    const QInputMethodEvent *self) {
  return self->replacementStart();
}

//  int QInputMethodEvent::replacementLength() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QInputMethodEvent17replacementLengthEv(
    const QInputMethodEvent *self) {
  return self->replacementLength();
}

//  bool operator==(const QInputMethodEvent::Attribute &lhs, const
//      QInputMethodEvent::Attribute &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRKN17QInputMethodEvent9AttributeES2_(
    const QInputMethodEvent::Attribute *lhs,
    const QInputMethodEvent::Attribute *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QInputMethodEvent::Attribute &lhs, const
//      QInputMethodEvent::Attribute &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRKN17QInputMethodEvent9AttributeES2_(
    const QInputMethodEvent::Attribute *lhs,
    const QInputMethodEvent::Attribute *rhs) {
  return operator!=(*lhs, *rhs);
}

//  a Python function taken by a CuteQInputMethodEvent, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QInputMethodEvent(
    QInputMethodEvent *self,
    const char *key,
    void *call) {
  return static_cast<CuteQInputMethodEvent *>(self)->take(key, call);
}

//  QInputMethodEvent *QInputMethodEvent::clone() const
extern "C" Q_DECL_EXPORT
QInputMethodEvent *ritual_own_ZNK17QInputMethodEvent5cloneEv(
    const QInputMethodEvent *self) {
  return self->QInputMethodEvent::clone();
}

#endif  // !defined(QT_NO_INPUTMETHOD)
