//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qproperty.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qproperty.h>

//  QPropertyBindingSourceLocation::QPropertyBindingSourceLocation()
extern "C" Q_DECL_EXPORT
QPropertyBindingSourceLocation *ritual_ZN30QPropertyBindingSourceLocationC1Ev() {
  return new QPropertyBindingSourceLocation();
}

#if defined(__cpp_lib_experimental_source_location)
//  QPropertyBindingSourceLocation::QPropertyBindingSourceLocation(const
//      std::experimental::source_location &cppLocation)
extern "C" Q_DECL_EXPORT
QPropertyBindingSourceLocation *ritual_ZN30QPropertyBindingSourceLocationC1ERKNSt12experimental15fundamentals_v215source_locationE(
    const std::experimental::source_location *cppLocation) {
  return new QPropertyBindingSourceLocation(*cppLocation);
}
#endif  // defined(__cpp_lib_experimental_source_location)

//  QPropertyBindingSourceLocation::~QPropertyBindingSourceLocation()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QPropertyBindingSourceLocationD1Ev(
    QPropertyBindingSourceLocation *self) {
  delete self;
}
