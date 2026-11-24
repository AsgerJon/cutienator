//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qcompleter_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(completer)
#if QT_CONFIG(completer)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qcompleter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QMatchData::QMatchData()
extern "C" Q_DECL_EXPORT
QMatchData *ritual_ZN10QMatchDataC1Ev() {
  return new QMatchData();
}

//  QMatchData::QMatchData(const QIndexMapper &indices, int em, bool p)
extern "C" Q_DECL_EXPORT
QMatchData *ritual_ZN10QMatchDataC1ERK12QIndexMapperib(
    const QIndexMapper *indices,
    int em,
    bool p) {
  return new QMatchData(*indices, em, p);
}

//  bool QMatchData::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QMatchData7isValidEv(const QMatchData *self) {
  return self->isValid();
}

//  QMatchData::~QMatchData()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QMatchDataD1Ev(QMatchData *self) {
  delete self;
}

#endif  // QT_CONFIG(completer)
#endif  // QT_CONFIG(completer)
