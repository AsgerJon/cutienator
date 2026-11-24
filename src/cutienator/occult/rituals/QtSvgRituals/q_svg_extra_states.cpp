//  Written by dev_tooling.RitualGenerator from the records of
//  QtSvg/6.12.0/QtSvg/private/qsvgstyle_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtSvg/6.12.0/QtSvg/private/qtsvgglobal_p.h>
#include <QtSvg/QtSvg>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSvg/6.12.0/QtSvg/private/qsvgstyle_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QSvgExtraStates::QSvgExtraStates()
extern "C" Q_DECL_EXPORT
QSvgExtraStates *ritual_ZN15QSvgExtraStatesC1Ev() {
  return new QSvgExtraStates();
}

//  QSvgExtraStates::QSvgExtraStates(const QSvgDocument *doc)
extern "C" Q_DECL_EXPORT
QSvgExtraStates *ritual_ZN15QSvgExtraStatesC1EPK12QSvgDocument(
    const QSvgDocument *doc) {
  return new QSvgExtraStates(doc);
}

//  const QSvgDocument *QSvgExtraStates::doc() const
extern "C" Q_DECL_EXPORT
const QSvgDocument *ritual_ZNK15QSvgExtraStates3docEv(
    const QSvgExtraStates *self) {
  return self->doc();
}

//  QSvgExtraStates::~QSvgExtraStates()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSvgExtraStatesD1Ev(QSvgExtraStates *self) {
  delete self;
}
