//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/qjslist.h, Qt 6.12.0. Changes made here are lost.
#include <QtQml/QtQml>
#include <QtQml/qjslist.h>

//  qsizetype QJSListIndexClamp::clamp(qsizetype start, qsizetype max,
//      qsizetype min)
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN17QJSListIndexClamp5clampExxx(
    qsizetype start,
    qsizetype max,
    qsizetype min) {
  return QJSListIndexClamp::clamp(start, max, min);
}

//  QJSListIndexClamp::~QJSListIndexClamp()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QJSListIndexClampD1Ev(QJSListIndexClamp *self) {
  delete self;
}
