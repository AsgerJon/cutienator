//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/qqmlmoduleregistration.h, Qt 6.12.0. Changes made here are lost.
#include <QtQml/QtQml>
#include <QtQml/qqmlmoduleregistration.h>

//  QQmlModuleRegistration::QQmlModuleRegistration(const char *uri, void
//      (*)() registerFunction)
extern "C" Q_DECL_EXPORT
QQmlModuleRegistration *ritual_ZN22QQmlModuleRegistrationC1EPKcPFvvE(
    const char *uri,
    void *registerFunction) {
  return new QQmlModuleRegistration(
      uri,
      reinterpret_cast<void (*)()>(registerFunction));
}

//  QQmlModuleRegistration::~QQmlModuleRegistration()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQmlModuleRegistrationD1Ev(QQmlModuleRegistration *self) {
  delete self;
}

#if QT_DEPRECATED_SINCE(6, 0)
//  QQmlModuleRegistration::QQmlModuleRegistration(const char *uri, int
//      majorVersion, void (*)() registerFunction)
extern "C" Q_DECL_EXPORT
QQmlModuleRegistration *ritual_ZN22QQmlModuleRegistrationC1EPKciPFvvE(
    const char *uri,
    int majorVersion,
    void *registerFunction) {
  return new QQmlModuleRegistration(
      uri,
      majorVersion,
      reinterpret_cast<void (*)()>(registerFunction));
}
#endif  // QT_DEPRECATED_SINCE(6, 0)
