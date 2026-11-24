//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qcompleter_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(completer)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qcompleter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QIndexMapper::QIndexMapper()
extern "C" Q_DECL_EXPORT
QIndexMapper *ritual_ZN12QIndexMapperC1Ev() {
  return new QIndexMapper();
}

//  QIndexMapper::QIndexMapper(int f, int t)
extern "C" Q_DECL_EXPORT
QIndexMapper *ritual_ZN12QIndexMapperC1Eii(int f, int t) {
  return new QIndexMapper(f, t);
}

//  int QIndexMapper::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QIndexMapper5countEv(const QIndexMapper *self) {
  return self->count();
}

//  int QIndexMapper::operator[](int index) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QIndexMapperixEi(const QIndexMapper *self, int index) {
  return self->operator[](index);
}

//  int QIndexMapper::indexOf(int x) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QIndexMapper7indexOfEi(const QIndexMapper *self, int x) {
  return self->indexOf(x);
}

//  bool QIndexMapper::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QIndexMapper7isValidEv(const QIndexMapper *self) {
  return self->isValid();
}

//  bool QIndexMapper::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QIndexMapper7isEmptyEv(const QIndexMapper *self) {
  return self->isEmpty();
}

//  void QIndexMapper::append(int x)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QIndexMapper6appendEi(QIndexMapper *self, int x) {
  self->append(x);
}

//  int QIndexMapper::first() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QIndexMapper5firstEv(const QIndexMapper *self) {
  return self->first();
}

//  int QIndexMapper::last() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QIndexMapper4lastEv(const QIndexMapper *self) {
  return self->last();
}

//  int QIndexMapper::from() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QIndexMapper4fromEv(const QIndexMapper *self) {
  return self->from();
}

//  int QIndexMapper::to() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QIndexMapper2toEv(const QIndexMapper *self) {
  return self->to();
}

//  int QIndexMapper::cost() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QIndexMapper4costEv(const QIndexMapper *self) {
  return self->cost();
}

//  QIndexMapper::~QIndexMapper()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QIndexMapperD1Ev(QIndexMapper *self) {
  delete self;
}

#endif  // QT_CONFIG(completer)
