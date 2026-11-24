//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qstringconverter_base.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0) && !defined(Q_QDOC) && !defined(QT_BOOTSTRAPPED)
#include <QtCore/qstringconverter.h>

//  QStringConverterBase::QStringConverterBase()
extern "C" Q_DECL_EXPORT
QStringConverterBase *ritual_ZN20QStringConverterBaseC1Ev() {
  return new QStringConverterBase();
}

//  QStringConverterBase::~QStringConverterBase()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QStringConverterBaseD1Ev(QStringConverterBase *self) {
  delete self;
}

#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0) && !defined(Q_QDOC) && !defined(QT_BOOTSTRAPPED)
