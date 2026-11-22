//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qevent.h>

//  QToolBarChangeEvent *QToolBarChangeEvent::clone() const
extern "C" Q_DECL_EXPORT
QToolBarChangeEvent *ritual_ZNK19QToolBarChangeEvent5cloneEv(
    const QToolBarChangeEvent *self) {
  return self->clone();
}

//  QToolBarChangeEvent::~QToolBarChangeEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QToolBarChangeEventD1Ev(QToolBarChangeEvent *self) {
  delete self;
}

//  QToolBarChangeEvent::QToolBarChangeEvent(bool t)
extern "C" Q_DECL_EXPORT
QToolBarChangeEvent *ritual_ZN19QToolBarChangeEventC1Eb(bool t) {
  return new QToolBarChangeEvent(t);
}

//  bool QToolBarChangeEvent::toggle() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QToolBarChangeEvent6toggleEv(
    const QToolBarChangeEvent *self) {
  return self->toggle();
}
