//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qshortcutmap_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtCore/qglobal.h>
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if QT_CONFIG(shortcut)
#if QT_CONFIG(shortcut)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qshortcutmap_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qkeysequence.h>
#include <QtCore/qlist.h>

//  QShortcutMap::QShortcutMap()
extern "C" Q_DECL_EXPORT
QShortcutMap *ritual_ZN12QShortcutMapC1Ev() {
  return new QShortcutMap();
}

//  QShortcutMap::~QShortcutMap()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QShortcutMapD1Ev(QShortcutMap *self) {
  delete self;
}

//  int QShortcutMap::removeShortcut(int id, QObject *owner, const
//      QKeySequence &key)
extern "C" Q_DECL_EXPORT
int ritual_ZN12QShortcutMap14removeShortcutEiP7QObjectRK12QKeySequence(
    QShortcutMap *self,
    int id,
    QObject *owner,
    const QKeySequence *key) {
  return self->removeShortcut(id, owner, *key);
}

//  int QShortcutMap::setShortcutEnabled(bool enable, int id, QObject *owner,
//      const QKeySequence &key)
extern "C" Q_DECL_EXPORT
int ritual_ZN12QShortcutMap18setShortcutEnabledEbiP7QObjectRK12QKeySequence(
    QShortcutMap *self,
    bool enable,
    int id,
    QObject *owner,
    const QKeySequence *key) {
  return self->setShortcutEnabled(enable, id, owner, *key);
}

//  int QShortcutMap::setShortcutAutoRepeat(bool on, int id, QObject *owner,
//      const QKeySequence &key)
extern "C" Q_DECL_EXPORT
int ritual_ZN12QShortcutMap21setShortcutAutoRepeatEbiP7QObjectRK12QKeySequence(
    QShortcutMap *self,
    bool on,
    int id,
    QObject *owner,
    const QKeySequence *key) {
  return self->setShortcutAutoRepeat(on, id, owner, *key);
}

//  QKeySequence::SequenceMatch QShortcutMap::state()
extern "C" Q_DECL_EXPORT
QKeySequence::SequenceMatch ritual_ZN12QShortcutMap5stateEv(
    QShortcutMap *self) {
  return self->state();
}

//  bool QShortcutMap::tryShortcut(QKeyEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QShortcutMap11tryShortcutEP9QKeyEvent(
    QShortcutMap *self,
    QKeyEvent *e) {
  return self->tryShortcut(e);
}

//  bool QShortcutMap::hasShortcutForKeySequence(const QKeySequence &seq)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QShortcutMap25hasShortcutForKeySequenceERK12QKeySequence(
    const QShortcutMap *self,
    const QKeySequence *seq) {
  return self->hasShortcutForKeySequence(*seq);
}

//  QList<QKeySequence> QShortcutMap::keySequences(bool getAll) const
extern "C" Q_DECL_EXPORT
QList<QKeySequence> *ritual_ZNK12QShortcutMap12keySequencesEb(
    const QShortcutMap *self,
    bool getAll) {
  return new QList<QKeySequence>(self->keySequences(getAll));
}

//  void QShortcutMap::resetState()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QShortcutMap10resetStateEv(QShortcutMap *self) {
  self->resetState();
}

//  QKeySequence::SequenceMatch QShortcutMap::nextState(QKeyEvent *e)
extern "C" Q_DECL_EXPORT
QKeySequence::SequenceMatch ritual_ZN12QShortcutMap9nextStateEP9QKeyEvent(
    QShortcutMap *self,
    QKeyEvent *e) {
  return self->nextState(e);
}

//  void QShortcutMap::dispatchEvent(QKeyEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QShortcutMap13dispatchEventEP9QKeyEvent(
    QShortcutMap *self,
    QKeyEvent *e) {
  self->dispatchEvent(e);
}

//  QKeySequence::SequenceMatch QShortcutMap::find(QKeyEvent *e, int
//      ignoredModifiers)
extern "C" Q_DECL_EXPORT
QKeySequence::SequenceMatch ritual_ZN12QShortcutMap4findEP9QKeyEventi(
    QShortcutMap *self,
    QKeyEvent *e,
    int ignoredModifiers) {
  return self->find(e, ignoredModifiers);
}

//  int QShortcutMap::translateModifiers(Qt::KeyboardModifiers modifiers)
extern "C" Q_DECL_EXPORT
int ritual_ZN12QShortcutMap18translateModifiersE6QFlagsIN2Qt16KeyboardModifierEE(
    QShortcutMap *self,
    int modifiers) {
  return self->translateModifiers(
      QFlags<Qt::KeyboardModifier>::fromInt(modifiers));
}

#endif  // QT_CONFIG(shortcut)
#endif  // QT_CONFIG(shortcut)
