//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qtextdocument_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qtextdocument_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QTextFragmentData::initialize()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QTextFragmentData10initializeEv(QTextFragmentData *self) {
  self->initialize();
}

//  void QTextFragmentData::invalidate() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK17QTextFragmentData10invalidateEv(
    const QTextFragmentData *self) {
  self->invalidate();
}

//  void QTextFragmentData::free()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QTextFragmentData4freeEv(QTextFragmentData *self) {
  self->free();
}

//  QTextFragmentData::~QTextFragmentData()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QTextFragmentDataD1Ev(QTextFragmentData *self) {
  delete self;
}
