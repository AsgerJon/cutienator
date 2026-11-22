//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qevent.h>
#include <QtGui/qkeysequence.h>

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
  return new QShortcutEvent(*key, id, ambiguous);
}

//  QShortcutEvent::QShortcutEvent(const QKeySequence &key, const QShortcut
//      *shortcut, bool ambiguous)
extern "C" Q_DECL_EXPORT
QShortcutEvent *ritual_ZN14QShortcutEventC1ERK12QKeySequencePK9QShortcutb(
    const QKeySequence *key,
    const QShortcut *shortcut,
    bool ambiguous) {
  return new QShortcutEvent(*key, shortcut, ambiguous);
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
