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

//  QStringConverterBase::QStringConverterBase(QStringConverterBase &&a0)
extern "C" Q_DECL_EXPORT
QStringConverterBase *ritual_ZN20QStringConverterBaseC1EOS_(
    QStringConverterBase *a0) {
  return new QStringConverterBase(std::move(*a0));
}

//  QStringConverterBase
//      &QStringConverterBase::operator=(QStringConverterBase &&a0)
extern "C" Q_DECL_EXPORT
QStringConverterBase *ritual_ZN20QStringConverterBaseaSEOS_(
    QStringConverterBase *self,
    QStringConverterBase *a0) {
  return &(self->operator=(std::move(*a0)));
}

#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0) && !defined(Q_QDOC) && !defined(QT_BOOTSTRAPPED)
