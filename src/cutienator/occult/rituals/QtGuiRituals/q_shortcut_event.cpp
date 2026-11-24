//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#if QT_CONFIG(shortcut)
#include <QtGui/qevent.h>
#include <QtGui/qkeysequence.h>
#include <cstring>

//  A QShortcutEvent that Python can take functions over in. Every QShortcutEvent
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(shortcut)
typedef void * (*CuteQShortcutEventCall0)(const void *, int *);
#endif  // QT_CONFIG(shortcut)
typedef void (*CuteQShortcutEventCall1)(const void *, bool, int *);
class CuteQShortcutEvent : public QShortcutEvent {
public:
  using QShortcutEvent::QShortcutEvent;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(shortcut)
    if (!std::strcmp(key, "_ZNK6QEvent5cloneEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(shortcut)
    if (!std::strcmp(key, "_ZN6QEvent11setAcceptedEb")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

#if QT_CONFIG(shortcut)
  //  QShortcutEvent *QShortcutEvent::clone() const
  QShortcutEvent *clone() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQShortcutEventCall0 call = reinterpret_cast<CuteQShortcutEventCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QShortcutEvent *>(given);
    }
    return QShortcutEvent::clone();
  }
#endif  // QT_CONFIG(shortcut)

  //  void QEvent::setAccepted(bool accepted)
  void setAccepted(bool accepted) override {
    if (taken[1]) {
      int handled = 0;
      CuteQShortcutEventCall1 call = reinterpret_cast<CuteQShortcutEventCall1>(taken[1]);
      call(this, accepted, &handled);
      if (handled) return;
    }
    QEvent::setAccepted(accepted);
  }
};

//  QShortcutEvent *QShortcutEvent::clone() const
extern "C" Q_DECL_EXPORT
QShortcutEvent *ritual_ZNK14QShortcutEvent5cloneEv(
    const QShortcutEvent *self) {
  return self->clone();
}

//  QShortcutEvent::~QShortcutEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QShortcutEventD1Ev(QShortcutEvent *self) {
  delete self;
}

//  QShortcutEvent::QShortcutEvent(const QKeySequence &key, int id, bool
//      ambiguous)
extern "C" Q_DECL_EXPORT
QShortcutEvent *ritual_ZN14QShortcutEventC1ERK12QKeySequenceib(
    const QKeySequence *key,
    int id,
    bool ambiguous) {
  return new CuteQShortcutEvent(*key, id, ambiguous);
}

//  QShortcutEvent::QShortcutEvent(const QKeySequence &key, const QShortcut
//      *shortcut, bool ambiguous)
extern "C" Q_DECL_EXPORT
QShortcutEvent *ritual_ZN14QShortcutEventC1ERK12QKeySequencePK9QShortcutb(
    const QKeySequence *key,
    const QShortcut *shortcut,
    bool ambiguous) {
  return new CuteQShortcutEvent(*key, shortcut, ambiguous);
}

//  const QKeySequence &QShortcutEvent::key() const
extern "C" Q_DECL_EXPORT
QKeySequence *ritual_ZNK14QShortcutEvent3keyEv(const QShortcutEvent *self) {
  return new QKeySequence(self->key());
}

//  int QShortcutEvent::shortcutId() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QShortcutEvent10shortcutIdEv(const QShortcutEvent *self) {
  return self->shortcutId();
}

//  bool QShortcutEvent::isAmbiguous() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QShortcutEvent11isAmbiguousEv(const QShortcutEvent *self) {
  return self->isAmbiguous();
}

//  a Python function taken by a CuteQShortcutEvent, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QShortcutEvent(
    QShortcutEvent *self,
    const char *key,
    void *call) {
  return static_cast<CuteQShortcutEvent *>(self)->take(key, call);
}

//  QShortcutEvent *QShortcutEvent::clone() const
extern "C" Q_DECL_EXPORT
QShortcutEvent *ritual_own_ZNK14QShortcutEvent5cloneEv(
    const QShortcutEvent *self) {
  return self->QShortcutEvent::clone();
}

#endif  // QT_CONFIG(shortcut)
