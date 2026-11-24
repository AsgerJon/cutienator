//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qcheckedint_impl.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qpoint.h>

//  void QtPrivate::QCheckedIntegers::AssertReportPolicy::check(bool ok,
//      const char *where, const char *description)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtPrivate16QCheckedIntegers18AssertReportPolicy5checkEbPKcS3_(
    bool ok,
    const char *where,
    const char *description) {
  QtPrivate::QCheckedIntegers::AssertReportPolicy::check(
      ok,
      where,
      description);
}

//  QtPrivate::QCheckedIntegers::AssertReportPolicy::~AssertReportPolicy()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtPrivate16QCheckedIntegers18AssertReportPolicyD1Ev(
    QtPrivate::QCheckedIntegers::AssertReportPolicy *self) {
  delete self;
}
