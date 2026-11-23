//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qlogging.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>

//  QMessageLogContext::QMessageLogContext()
extern "C" Q_DECL_EXPORT
QMessageLogContext *ritual_ZN18QMessageLogContextC1Ev() {
  return new QMessageLogContext();
}

//  QMessageLogContext::QMessageLogContext(const char *fileName, int
//      lineNumber, const char *functionName, const char *categoryName)
extern "C" Q_DECL_EXPORT
QMessageLogContext *ritual_ZN18QMessageLogContextC1EPKciS1_S1_(
    const char *fileName,
    int lineNumber,
    const char *functionName,
    const char *categoryName) {
  return new QMessageLogContext(
      fileName,
      lineNumber,
      functionName,
      categoryName);
}
